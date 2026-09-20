"""Deterministic, fail-closed assembly of immutable primary screening decisions.

Run: python build_primary_screening_master.py [--output-dir DIRECTORY]
Requires pyarrow==25.0.1, already available in the repository's .venv.
No network, screening classifier, resampling, or modification of input files.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LABELS = ('INCLUDE', 'EXCLUDE', 'UNCERTAIN')
REASONS = tuple(f'TA{i}' for i in range(1, 8))
GATES = ('q1_retrieval', 'q2_morphology', 'q3_retrieval_component')
PREPARATION = 'TITLE_ABSTRACT_SCREENING_MASTER.csv'
SAMPLE = 'SECOND_REVIEW_SAMPLE_20_PERCENT.csv'
OVERLAY = 'SCREENING_CORRECTIONS_CLARIFICATION_002.csv'
LEGACY = 'PRIMARY_SCREENING_LEGACY_DIAGNOSTICS.csv'
RULES = ('TITLE_ABSTRACT_SCREENING_CODEBOOK.md',
         'results/batch_001/SCREENING_CODEBOOK_CLARIFICATION_001.md',
         'SCREENING_CODEBOOK_CLARIFICATION_002.md')
B21_SUMMARY = 'results/batch_021/TA_BATCH_021_SCREENING_SUMMARY.json'
B21_AUDIT = 'results/batch_021/TA_BATCH_021_SCREENING_AUDIT.md'
CHECKPOINT = 'PRODUCTION_DRIFT_CHECKPOINT_004.json'
B2_REPORT = 'results/batch_002/TA_BATCH_002_RECALIBRATION_REPORT.md'
CSV_NAME = 'TITLE_ABSTRACT_SCREENING_PRIMARY_FINAL.csv'
PARQUET_NAME = 'TITLE_ABSTRACT_SCREENING_PRIMARY_FINAL.parquet'
COUNTS_NAME = 'PRIMARY_SCREENING_FINAL_COUNTS.json'
MANIFEST_NAME = 'PRIMARY_SCREENING_FINAL_MANIFEST.md'
SHA_NAME = 'PRIMARY_SCREENING_FINAL_SHA256.txt'
OUTPUT_NAMES = (CSV_NAME, PARQUET_NAME, COUNTS_NAME, MANIFEST_NAME, SHA_NAME)
BASELINE = {'INCLUDE': 253, 'EXCLUDE': 1106, 'UNCERTAIN': 641}
DECISION_FIELDS = ('screening_label', 'screening_reason_code', 'screening_reason_text',
                   'reviewer', 'review_date', 'review_notes')
REQUIRED = ('canonical_id', 'screening_order', 'title', 'abstract', 'authors', 'year',
            'venue', 'doi', 'sources', 'screening_label_primary',
            'screening_reason_code_primary', 'screening_reason_text_primary',
            'q1_retrieval_primary', 'q2_morphology_primary',
            'q3_retrieval_component_primary', 'primary_reviewer', 'primary_review_date',
            'decision_source_artifact', 'correction_overlay_applied',
            'dedup_uncertain', 'second_review_random_sample')


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def file_sha(path):
    return sha(path.read_bytes())


def read_csv(path):
    with path.open(encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f)
        require(reader.fieldnames and len(reader.fieldnames) == len(set(reader.fieldnames)),
                f'Invalid or duplicate CSV fields: {path.name}')
        rows = list(reader)
        require(all(None not in r and None not in r.values() for r in rows),
                f'Malformed CSV row: {path.name}')
        return rows


def keyed(rows, name):
    require(all(r.get('canonical_id') for r in rows), f'Missing canonical ID: {name}')
    result = {r['canonical_id']: r for r in rows}
    require(len(result) == len(rows), f'Duplicate canonical ID: {name}')
    return result


def batch_path(n):
    suffix = '_FINAL' if n in (1, 2, 12) else ''
    return f'results/batch_{n:03d}/TA_BATCH_{n:03d}_SCREENED{suffix}.csv'


def label_counts(rows):
    counts = Counter(r['screening_label_primary'] for r in rows)
    return {label: counts[label] for label in LABELS}


def validate_decisions(rows, expected):
    require(len(rows) == expected, f'Expected {expected} decisions, got {len(rows)}')
    keyed(rows, 'final decisions')
    for r in rows:
        cid = r['canonical_id']
        label = r['screening_label_primary']
        reason = r['screening_reason_code_primary']
        require(label in LABELS, f'Missing/invalid label: {cid}')
        require(r['screening_reason_text_primary'].strip(), f'Missing rationale: {cid}')
        for gate in GATES:
            allowed = {'YES', 'NO', 'UNCLEAR'}
            if gate == GATES[2]:
                allowed.add('NOT_APPLICABLE')
            require(r[gate + '_primary'] in allowed, f'Invalid {gate}: {cid}')
        if label == 'INCLUDE':
            # No exception is needed by this fixed corpus. Never infer an exception.
            require(r['q1_retrieval_primary'] == r['q2_morphology_primary'] == 'YES',
                    f'INCLUDE invariant violation: {cid}')
            require(reason == '', f'INCLUDE has exclusion reason: {cid}')
        elif label == 'UNCERTAIN':
            require(reason == 'TA8', f'UNCERTAIN invariant violation: {cid}')
        else:
            require(reason in REASONS, f'EXCLUDE invariant violation: {cid}')
        require(r['primary_reviewer'].strip(), f'Missing reviewer: {cid}')
        require(re.fullmatch(r'\d{4}-\d{2}-\d{2}', r['primary_review_date']),
                f'Invalid review date: {cid}')


def normalize_decision(row, n, legacy):
    """Translate finalized schemas without making scientific label decisions."""
    if n == 2:
        label, code, reason = (row[f'final_{f}'] for f in ('label', 'reason_code', 'reason_text'))
        # The final artifact retains Pass B rationales except the explicitly
        # adjudicated CR000197, whose final adjudication retains Pass A uncertainty.
        which = 'pass_a' if row['canonical_id'] == 'CR000197' else 'pass_b'
        gates = {g + '_primary': row[which + '_' + g] for g in GATES}
        reviewer = 'AI-assisted primary-screening calibration adjudication'
        date = '2026-09-20'  # Documented date in the final recalibration report.
        notes = row['adjudication_basis']
        provenance = f'{which} gates embedded in FINAL artifact; final adjudication controls CR000197 Q3. Reviewer role/date documented in ' + B2_REPORT
    else:
        label, code, reason = (row[f'screening_{f}'] for f in ('label', 'reason_code', 'reason_text'))
        reviewer, date, notes = (row[f] for f in ('reviewer', 'review_date', 'review_notes'))
        if n == 1:
            diagnostic = legacy[row['canonical_id']]
            require(diagnostic['finalized_rationale'] == reason, 'Legacy diagnostic rationale mismatch')
            gates = {g + '_primary': diagnostic[g] for g in GATES}
            provenance = LEGACY + ': ' + diagnostic['diagnostic_basis']
        else:
            gates = {g + '_primary': row[g] for g in GATES}
            provenance = 'Diagnostic columns copied verbatim from finalized batch artifact.'
    return dict(screening_label_primary=label, screening_reason_code_primary=code,
                screening_reason_text_primary=reason, **gates,
                primary_reviewer=reviewer, primary_review_date=date,
                primary_review_notes=notes, diagnostic_provenance_primary=provenance,
                decision_source_artifact=batch_path(n), batch_source_artifact=batch_path(n),
                batch_final_label=label, batch_final_reason_code=code,
                correction_overlay_applied='NO', correction_overlay_artifact='',
                correction_overlay_row='', correction_clarification='',
                correction_review_date='', correction_notes='')


def apply_overlay(rows, corrections):
    """Explicit ledger order, never filesystem timestamps; one application per ID.

    There is exactly one authorized ledger. Duplicate IDs are rejected instead
    of guessing their chronological priority. Later ledgers require an explicit
    authorized update to the input list/order.
    """
    index = keyed(rows, 'master before overlay')
    keyed(corrections, 'correction ledger')
    applied = []
    for ordinal, correction in enumerate(corrections, 2):
        cid = correction['canonical_id']
        require(cid in index, f'Correction ID absent: {cid}')
        r = index[cid]
        require(r['correction_overlay_applied'] == 'NO', f'Correction applied twice: {cid}')
        require((r['screening_label_primary'], r['screening_reason_code_primary']) ==
                (correction['old_label'], correction['old_reason_code']),
                f'Correction old decision mismatch: {cid}')
        require(r['batch'] == 'TA_BATCH_' + correction['batch'].zfill(3),
                f'Correction batch mismatch: {cid}')
        # Only explicit gate assignments in this ledger's notes are applied.
        # Q3 is not in the ledger, so its recorded historical value is preserved.
        for short, gate in zip(('Q1', 'Q2', 'Q3'), GATES):
            matches = re.findall(r'\b' + short + r'=(YES|NO|UNCLEAR|NOT_APPLICABLE)\b', correction['notes'])
            require(len(matches) <= 1, f'Ambiguous correction diagnostic: {cid}/{short}')
            if matches:
                r[gate + '_primary'] = matches[0]
        r.update(screening_label_primary=correction['new_label'],
                 screening_reason_code_primary=correction['new_reason_code'],
                 screening_reason_text_primary=correction['correction_basis'],
                 primary_review_date=correction['review_date'],
                 correction_overlay_applied='YES', correction_overlay_artifact=OVERLAY,
                 correction_overlay_row=str(ordinal),
                 correction_clarification=correction['clarification'],
                 correction_review_date=correction['review_date'],
                 correction_notes=correction['notes'], decision_source_artifact=OVERLAY)
        r['primary_review_notes'] += ' | Correction overlay: ' + correction['notes']
        r['diagnostic_provenance_primary'] += ' Explicit Q1/Q2 override from ledger notes; unmentioned Q3 retained. Ledger has no separate reviewer name; same-primary-workflow batch reviewer retained.'
        applied.append(dict(canonical_id=cid, ledger_row=ordinal, old_label=correction['old_label'],
                            new_label=correction['new_label'], new_reason_code=correction['new_reason_code']))
    return applied


def assemble(root=ROOT):
    root = Path(root)
    # Part B gate is checked before loading the preparation master.
    summary = json.loads((root / B21_SUMMARY).read_text(encoding='utf-8'))
    require(summary['validation'] == 'PASS' and summary['POTENTIAL_CODEBOOK_ISSUE'] == 'NO',
            'STOP: Batch 021 gate failed')
    require(summary['records'] == summary['unique_ids'] == 10, 'Batch 021 size mismatch')
    require(file_sha(root / batch_path(21)) == summary['screened_sha256'], 'Batch 021 finalized hash mismatch')
    require(file_sha(root / 'batches/TA_BATCH_021.csv') == summary['input_sha256'], 'Batch 021 input changed')

    paths = [PREPARATION, SAMPLE, OVERLAY, LEGACY, *RULES, B21_SUMMARY, B21_AUDIT, CHECKPOINT,
             B2_REPORT, 'build_primary_screening_master.py', 'test_build_primary_screening_master.py']
    paths += [batch_path(n) for n in range(1, 22)]
    paths += [f'batches/TA_BATCH_{n:03d}.csv' for n in range(1, 22)]
    hashes = {p: file_sha(root / p) for p in sorted(paths)}
    checkpoint = json.loads((root / CHECKPOINT).read_text(encoding='utf-8'))
    require(checkpoint['validation'] == 'PASS', 'Historical checkpoint not PASS')
    # Verify the historical files against hashes recorded before this assembly.
    for artifact in checkpoint['cumulative_progress']['artifact_manifest']:
        relative = batch_path(int(artifact['batch']))
        require(hashes[relative] == artifact['sha256'], f'Historical finalized artifact changed: {relative}')
    require(hashes[OVERLAY] == checkpoint['cumulative_progress']['overlay_sha256'], 'Historical overlay changed')

    base = read_csv(root / PREPARATION)
    base_index = keyed(base, PREPARATION)
    require(len(base) == 2010, 'Preparation master size mismatch')
    require(sorted(int(r['screening_order']) for r in base) == list(range(1, 2011)), 'Preparation order mismatch')
    require(all(r[f] == '' for r in base for f in DECISION_FIELDS), 'Preparation decisions are not empty')
    legacy = keyed(read_csv(root / LEGACY), LEGACY)
    require(set(legacy) == {r['canonical_id'] for r in base if r['batch'] == 'TA_BATCH_001'}, 'Legacy coverage mismatch')

    rows, batch_counts, seen = [], {}, set()
    for n in range(1, 22):
        source = batch_path(n)
        decisions = read_csv(root / source)
        index = keyed(decisions, source)
        packet = keyed(read_csv(root / f'batches/TA_BATCH_{n:03d}.csv'), f'packet {n}')
        start, stop = (n - 1) * 100 + 1, min(n * 100, 2010)
        require(len(decisions) == stop - start + 1, f'Batch {n} size mismatch')
        require(set(index) == set(packet), f'Batch {n} IDs mismatch')
        require(sorted(int(r['screening_order']) for r in decisions) == list(range(start, stop + 1)), f'Batch {n} order mismatch')
        for decision in decisions:
            cid = decision['canonical_id']
            require(cid in base_index and cid not in seen, f'Missing or duplicate decision: {cid}')
            seen.add(cid)
            original = base_index[cid]
            require(original['screening_order'] == decision['screening_order'] == packet[cid]['screening_order'], f'Order changed: {cid}')
            require(original['batch'] == f'TA_BATCH_{n:03d}', f'Wrong batch: {cid}')
            for field, value in packet[cid].items():
                if field not in DECISION_FIELDS:
                    require(original[field] == value, f'Packet metadata differs: {cid}/{field}')
                    if field in decision:
                        require(decision[field] == value, f'Final metadata differs: {cid}/{field}')
            # Preserve every preparation field; original empty decision columns
            # are explicitly namespaced to avoid a second apparent active label.
            r = {('preparation_' + k if k in DECISION_FIELDS else k): v for k, v in original.items()}
            r.update(normalize_decision(decision, n, legacy))
            # Retain the entire finalized decision row, including embedded audit
            # columns, verbatim as provenance; it is never used as new evidence.
            r['finalized_source_row_json'] = json.dumps(decision, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
            r['primary_reviewer_provenance'] = B2_REPORT if n == 2 else source
            r['secondary_review_exception'] = 'NO'
            rows.append(r)
        batch_counts[f'{n:03d}'] = label_counts(rows[-len(decisions):])
    require(seen == set(base_index), 'Missing final decisions')
    rows.sort(key=lambda r: int(r['screening_order']))
    before_overlay = label_counts(rows)
    corrections = read_csv(root / OVERLAY)
    applied = apply_overlay(rows, corrections)
    validate_decisions(rows, 2010)
    require([int(r['screening_order']) for r in rows] == list(range(1, 2011)), 'Final order gaps')
    require(label_counts(rows[:2000]) == BASELINE, 'Baseline after overlay differs from 253/1106/641')
    b21 = label_counts(rows[2000:])
    require(b21 == summary['counts'], 'Batch 021 summary differs from artifact')
    totals = label_counts(rows)
    require(all(totals[k] == BASELINE[k] + b21[k] for k in LABELS), 'Final totals mismatch')

    sample = keyed(read_csv(root / SAMPLE), SAMPLE)
    sample_ids = {r['canonical_id'] for r in rows if r['second_review_random_sample'] == 'YES'}
    require(all(r['second_review_random_sample'] in {'YES', 'NO'} for r in rows), 'Invalid sample flags')
    require(len(sample_ids) == len(sample) == 402 and sample_ids == set(sample), 'Frozen sample changed')
    for cid, s in sample.items():
        for field in s:
            require(base_index[cid][field] == s[field], f'Sample record changed: {cid}/{field}')
    validation = dict(status='PASS', coverage='2010/2010', unique_canonical_ids=2010,
                      missing_decisions=0, duplicate_final_decisions=0, screening_order_gaps=0,
                      include_invariant_violations=0, uncertain_invariant_violations=0,
                      exclude_invariant_violations=0, correction_ids_missing=0,
                      corrections_applied_exactly_once=True, latest_overlay_labels_match=True,
                      frozen_sample_ids_unchanged=True, bibliographic_metadata_preserved=True,
                      historical_sources_match_checkpoint=True, secondary_review_exceptions=0)
    counts = dict(records_screened_primary=len(rows), include_primary=totals['INCLUDE'],
                  exclude_primary=totals['EXCLUDE'], uncertain_primary=totals['UNCERTAIN'],
                  exclude_by_reason={code: sum(r['screening_label_primary'] == 'EXCLUDE' and r['screening_reason_code_primary'] == code for r in rows) for code in REASONS},
                  uncertain_ta8=sum(r['screening_label_primary'] == 'UNCERTAIN' and r['screening_reason_code_primary'] == 'TA8' for r in rows),
                  batch021_counts=b21, batch_counts_before_overlay=batch_counts,
                  finalized_totals_before_overlay=before_overlay, baseline_through_batch020_after_overlay=BASELINE,
                  corrections_applied=len(applied), correction_details=applied,
                  second_review_random_sample_count=402, primary_screening_complete=True,
                  independent_second_review_performed=False, full_text_retrieval_performed=False,
                  web_used=False, github_modified=False, validation=validation)
    require(sum(counts['exclude_by_reason'].values()) == counts['exclude_primary'], 'Exclusion reasons mismatch')
    require(counts['uncertain_ta8'] == counts['uncertain_primary'], 'TA8 total mismatch')
    require(all(file_sha(root / p) == h for p, h in hashes.items()), 'Input changed during assembly')
    return rows, counts, hashes


def csv_bytes(rows):
    fields = list(REQUIRED) + sorted(set(rows[0]) - set(REQUIRED))
    stream = io.StringIO(newline='')
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode('utf-8'), fields


def build(root=ROOT, output_dir=None):
    import pyarrow as pa
    import pyarrow.parquet as pq
    require(pa.__version__ == '25.0.1', 'Deterministic Parquet requires pyarrow==25.0.1')
    root = Path(root)
    output_dir = Path(output_dir) if output_dir is not None else root
    rows, counts, hashes = assemble(root)
    csv_data, fields = csv_bytes(rows)
    # Strings preserve original empty values, leading zeros and metadata exactly.
    # No pandas metadata, wall-clock timestamps, random IDs or compression state.
    schema = pa.schema([(f, pa.string()) for f in fields])
    table = pa.Table.from_pylist([{f: r[f] for f in fields} for r in rows], schema=schema)
    buffer = pa.BufferOutputStream()
    pq.write_table(table, buffer, compression='NONE', use_dictionary=False,
                   write_statistics=True, row_group_size=2010, version='2.6',
                   data_page_version='1.0', write_batch_size=1024)
    parquet_data = buffer.getvalue().to_pybytes()
    require(pq.read_table(pa.BufferReader(parquet_data)).to_pylist() == table.to_pylist(), 'Parquet round-trip mismatch')
    data = {CSV_NAME: csv_data, PARQUET_NAME: parquet_data,
            COUNTS_NAME: (json.dumps(counts, ensure_ascii=False, sort_keys=True, indent=2) + '\n').encode('utf-8')}
    lines = ['# PRIMARY TITLE/ABSTRACT SCREENING COMPLETE', '',
             'Assembly version: 1.0.0. Review date: 2026-09-20.', '',
             '**Primary screening was AI-assisted and is NOT an independent dual-review process.**', '',
             'Reviewer: Codex, AI-assisted primary screening. Historical reviewer descriptions and review dates are retained. Batch 002 uses the same-workflow AI-assisted calibration-adjudication role and date documented in its final report. No independent second review was performed.', '',
             '## Frozen codebook versions', '',
             '- TITLE_ABSTRACT_SCREENING_CODEBOOK.md: v1.0.0; frozen 2026-09-18.',
             '- Clarification 001: dated 2026-09-20; operationally authorized. Its original PROPOSED heading remains unchanged.',
             '- Clarification 002: dated 2026-09-20; adopted operational clarification. No eligibility change.', '',
             '## Decision precedence and provenance', '',
             'latest explicit correction overlay > finalized batch artifact > older preliminary artifact.',
             'Only the explicit 21-file list below supplies decisions. Batch 001/002/012 use *_SCREENED_FINAL.csv. Preliminary Batch 012 and original non-final Batch 001/002 are never loaded. The preparation master supplies original metadata and frozen sample flags only, after the Batch 021 PASS gate; it is not screening evidence. MASTER_INDEX is not loaded.', '',
             'All preparation metadata fields and values are retained. Its six empty decision fields have preparation_ prefixes. Final primary decisions have distinct *_primary fields. The complete finalized source row is also preserved in finalized_source_row_json. No historical primary label is changed except the authorized explicit overlay.', '',
             'Batch 001 lacks structured gates. PRIMARY_SCREENING_LEGACY_DIAGNOSTICS.csv transcribes only its finalized rationales, with unrecorded/unresolved diagnostic details kept UNCLEAR; it supplies no labels. Batch 002 gates come from Pass B embedded in the FINAL file, except CR000197, whose final adjudication explicitly retains Pass A uncertainty about Q3. This schema harmonization is not a new screening pass. Legacy diagnostic provenance is stored per row.', '',
             'The correction ledger explicitly changes CR000691 Q1 to UNCLEAR and retains Q2=YES. Q3 is not specified by that ledger and is preserved from the historical artifact; no new diagnostic claim is inferred. Original batch label/code and source remain available. The ledger records same-primary-workflow correction but no separate reviewer identity, so the historical reviewer is retained and this limitation is explicit.', '',
             '## Counts', '',
             '| Item | Count |', '| --- | ---: |', '| Input canonical records | 2010 |',
             '| Finalized batches 001–020 | 2000 |', '| Batch 021 | 10 |',
             '| Output rows / unique canonical IDs | 2010 / 2010 |',
             f"| INCLUDE | {counts['include_primary']} |", f"| EXCLUDE | {counts['exclude_primary']} |",
             f"| UNCERTAIN / TA8 | {counts['uncertain_primary']} |", '| Frozen random second-review sample | 402 |', '',
             'Batch 021: INCLUDE 3; EXCLUDE 5; UNCERTAIN 2. Safety changes: 1; codebook issue: NO; validation: PASS.',
             'Baseline after overlay: 253 / 1106 / 641. Adding Batch 021 gives 256 / 1111 / 643. The existing overlay is applied once to the historical batch decision, not again to the already corrected baseline.', '',
             '| Exclusion reason | Count |', '| --- | ---: |']
    lines += [f'| {code} | {count} |' for code, count in counts['exclude_by_reason'].items()]
    lines += ['', '## Correction overlay validation', '',
              f"Corrections applied: {counts['corrections_applied']}. All ledger IDs exist; each is applied exactly once; final label and code equal the latest explicit ledger. Historical Batch 007 remains unchanged.", '',
              '| Canonical ID | Ledger CSV row | Historical label | Effective label / reason |', '| --- | ---: | --- | --- |']
    lines += [f"| {a['canonical_id']} | {a['ledger_row']} | {a['old_label']} | {a['new_label']} / {a['new_reason_code']} |" for a in counts['correction_details']]
    lines += ['', '## Validation', '',
              'PASS: complete screening_order 1..2010; coverage 2010/2010; 2010 unique IDs; missing decisions 0; duplicate final decisions 0. INCLUDE, UNCERTAIN and EXCLUDE invariant violations are all 0. No INCLUDE gate exception is required. All 402 frozen random sample IDs and flags are preserved without resampling.',
              'Bibliographic metadata match the preparation master and original reviewer packets. All historical batch hashes and the overlay hash match Production Drift Checkpoint #4. All inputs are rehashed before and after writing outputs. Original TA_BATCH_021.csv matches its screening summary hash.', '',
              '## Deterministic assembly and regression tests', '',
              'Run `python build_primary_screening_master.py` from this directory. Optional `--output-dir` writes the same five outputs elsewhere. Run `python -m unittest discover -s . -p test_build_primary_screening_master.py -v` for regression tests.',
              'Requires pyarrow==25.0.1. Stable screening-order rows, explicit column order, UTF-8 CSV with LF row delimiters, sorted JSON keys, fixed Parquet schema/settings and no wall-clock values. All Parquet columns are strings to preserve source values exactly. The SHA file covers CSV, Parquet, counts and this manifest; the manifest excludes its own hash to avoid a circular hash dependency.',
              'Regression tests verify counts, coverage, metadata preservation, invariants, correction precedence, frozen sample, Batch 021, failure paths, Parquet equivalence and byte-identical repeated output. Actual execution results are reported separately after running the suite.', '',
              '## Authoritative batch artifacts', '',
              '| Batch | Records | Finalized source | SHA-256 |', '| --- | ---: | --- | --- |']
    lines += [f'| {n:03d} | {10 if n == 21 else 100} | `{batch_path(n)}` | `{hashes[batch_path(n)]}` |' for n in range(1, 22)]
    lines += ['', '## Other inputs and implementation SHA-256', '', '| Artifact | SHA-256 |', '| --- | --- |']
    lines += [f'| `{p}` | `{h}` |' for p, h in hashes.items() if p not in {batch_path(n) for n in range(1, 22)}]
    lines += ['', '## Output SHA-256', '', '| Artifact | SHA-256 |', '| --- | --- |']
    lines += [f'| `{p}` | `{sha(content)}` |' for p, content in data.items()]
    lines += ['', 'The manifest hash is in PRIMARY_SCREENING_FINAL_SHA256.txt.', '',
              '## Scope and stop', '',
              'No web, publisher pages, Google Scholar, PDFs, full texts, MASTER_INDEX, prior study memory or pilot labels were used to screen Batch 021. No GitHub changes, independent second review, full-text retrieval or further primary-decision changes were performed. STOP after primary assembly and validation.', '']
    data[MANIFEST_NAME] = '\n'.join(lines).encode('utf-8')
    data[SHA_NAME] = ''.join(f'{sha(data[name])}  {name}\n' for name in OUTPUT_NAMES[:-1]).encode('utf-8')
    output_dir.mkdir(parents=True, exist_ok=True)
    require(all((output_dir / name).resolve() not in {(root / p).resolve() for p in hashes} for name in data), 'Output overlaps input')
    require(all(file_sha(root / p) == h for p, h in hashes.items()), 'Input changed before write')
    for name, content in data.items():
        (output_dir / name).write_bytes(content)
    require(all(file_sha(root / p) == h for p, h in hashes.items()), 'Input changed during write')
    return counts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path)
    args = parser.parse_args()
    counts = build(output_dir=args.output_dir)
    print(json.dumps({k: counts[k] for k in ('records_screened_primary', 'include_primary',
          'exclude_primary', 'uncertain_primary', 'corrections_applied', 'primary_screening_complete')}, sort_keys=True))


if __name__ == '__main__':
    main()
