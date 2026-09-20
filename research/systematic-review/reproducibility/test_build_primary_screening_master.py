"""Regression coverage for finalized primary screening assembly, not rescreening."""
import copy
import csv
import io
import json
import tempfile
import unittest
from collections import Counter
from pathlib import Path
from unittest.mock import patch

import pyarrow.parquet as pq

import build_primary_screening_master as builder


class PrimaryScreeningTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows, cls.counts, cls.hashes = builder.assemble()
        cls.index = {r['canonical_id']: r for r in cls.rows}
        cls.temp = tempfile.TemporaryDirectory()
        cls.out = Path(cls.temp.name)
        builder.build(output_dir=cls.out)

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def test_2010_records_and_unique_ids(self):
        self.assertEqual(len(self.rows), 2010)
        self.assertEqual(len(self.index), 2010)

    def test_complete_order(self):
        self.assertEqual([int(r['screening_order']) for r in self.rows], list(range(1, 2011)))

    def test_labels_and_final_counts(self):
        self.assertEqual(Counter(r['screening_label_primary'] for r in self.rows),
                         {'INCLUDE': 256, 'EXCLUDE': 1111, 'UNCERTAIN': 643})
        self.assertEqual(sum(self.counts[k] for k in ('include_primary', 'exclude_primary', 'uncertain_primary')), 2010)

    def test_include_invariants(self):
        for r in self.rows:
            if r['screening_label_primary'] == 'INCLUDE':
                self.assertEqual((r['q1_retrieval_primary'], r['q2_morphology_primary']), ('YES', 'YES'), r['canonical_id'])
                self.assertEqual(r['screening_reason_code_primary'], '')

    def test_uncertain_ta8(self):
        for r in self.rows:
            if r['screening_label_primary'] == 'UNCERTAIN':
                self.assertEqual(r['screening_reason_code_primary'], 'TA8')
        self.assertEqual(self.counts['uncertain_ta8'], 643)

    def test_exclude_valid_reason(self):
        codes = Counter(r['screening_reason_code_primary'] for r in self.rows if r['screening_label_primary'] == 'EXCLUDE')
        self.assertTrue(set(codes) <= set(builder.REASONS))
        self.assertEqual(sum(codes.values()), 1111)
        self.assertEqual({code: codes[code] for code in builder.REASONS}, self.counts['exclude_by_reason'])

    def test_correction_precedence(self):
        original = builder.keyed(builder.read_csv(builder.ROOT / builder.batch_path(7)), 'batch7')['CR000691']
        self.assertEqual(original['screening_label'], 'INCLUDE')
        row = self.index['CR000691']
        self.assertEqual(row['screening_label_primary'], 'UNCERTAIN')
        self.assertEqual(row['screening_reason_code_primary'], 'TA8')
        self.assertEqual(row['q1_retrieval_primary'], 'UNCLEAR')
        self.assertEqual(row['q2_morphology_primary'], 'YES')
        self.assertEqual(row['q3_retrieval_component_primary'], original['q3_retrieval_component'])
        self.assertEqual(row['decision_source_artifact'], builder.OVERLAY)
        self.assertEqual(row['batch_source_artifact'], builder.batch_path(7))
        self.assertEqual(sum(r['correction_overlay_applied'] == 'YES' for r in self.rows), 1)
        self.assertEqual(self.counts['corrections_applied'], 1)

    def test_duplicate_unknown_or_reapplied_overlay_rejected(self):
        corrections = builder.read_csv(builder.ROOT / builder.OVERLAY)
        with self.assertRaisesRegex(ValueError, 'Duplicate canonical ID'):
            builder.apply_overlay(copy.deepcopy(self.rows), corrections + corrections)
        unknown = dict(corrections[0], canonical_id='CR_DOES_NOT_EXIST')
        with self.assertRaisesRegex(ValueError, 'Correction ID absent'):
            builder.apply_overlay(copy.deepcopy(self.rows), [unknown])
        with self.assertRaisesRegex(ValueError, 'applied twice'):
            builder.apply_overlay(copy.deepcopy(self.rows), corrections)

    def test_frozen_sample_exactly_402_same_ids(self):
        selected = {r['canonical_id'] for r in self.rows if r['second_review_random_sample'] == 'YES'}
        frozen = {r['canonical_id'] for r in builder.read_csv(builder.ROOT / builder.SAMPLE)}
        self.assertEqual(len(selected), 402)
        self.assertEqual(selected, frozen)

    def test_batch021_exactly_ten_and_safety_change(self):
        rows = builder.read_csv(builder.ROOT / builder.batch_path(21))
        self.assertEqual(len(rows), 10)
        self.assertEqual(len({r['canonical_id'] for r in rows}), 10)
        self.assertEqual([int(r['screening_order']) for r in rows], list(range(2001, 2011)))
        self.assertEqual(Counter(r['screening_label'] for r in rows), {'INCLUDE': 3, 'EXCLUDE': 5, 'UNCERTAIN': 2})
        changed = [r['canonical_id'] for r in rows if r['safety_audit_change'] == 'YES']
        self.assertEqual(changed, ['CR002215'])
        summary = json.loads((builder.ROOT / builder.B21_SUMMARY).read_text(encoding='utf-8'))
        self.assertEqual(summary['validation'], 'PASS')
        self.assertEqual(summary['POTENTIAL_CODEBOOK_ISSUE'], 'NO')
        self.assertEqual(summary['input_sha256'], builder.file_sha(builder.ROOT / 'batches/TA_BATCH_021.csv'))

    def test_failed_batch_gate_stops_before_outputs(self):
        summary = json.loads((builder.ROOT / builder.B21_SUMMARY).read_text(encoding='utf-8'))
        for update in ({'validation': 'FAIL'}, {'POTENTIAL_CODEBOOK_ISSUE': 'YES'}):
            with self.subTest(update=update), patch.object(builder.json, 'loads', return_value={**summary, **update}):
                with self.assertRaisesRegex(ValueError, 'STOP: Batch 021 gate failed'):
                    builder.assemble()

    def test_finalized_sources_only(self):
        for n in range(1, 22):
            path = builder.batch_path(n)
            source = builder.read_csv(builder.ROOT / path)
            for s in source:
                r = self.index[s['canonical_id']]
                self.assertEqual(r['batch_source_artifact'], path)
                label = s['final_label'] if n == 2 else s['screening_label']
                code = s['final_reason_code'] if n == 2 else s['screening_reason_code']
                reason = s['final_reason_text'] if n == 2 else s['screening_reason_text']
                self.assertEqual(r['batch_final_label'], label)
                self.assertEqual(r['batch_final_reason_code'], code)
                if r['correction_overlay_applied'] == 'NO':
                    self.assertEqual(r['screening_label_primary'], label)
                    self.assertEqual(r['screening_reason_code_primary'], code)
                    self.assertEqual(r['screening_reason_text_primary'], reason)
                self.assertEqual(json.loads(r['finalized_source_row_json']), s)
        for n in (1, 2, 12):
            self.assertTrue(builder.batch_path(n).endswith('_FINAL.csv'))

    def test_metadata_preserved_without_loss(self):
        for source in builder.read_csv(builder.ROOT / builder.PREPARATION):
            row = self.index[source['canonical_id']]
            for field, value in source.items():
                destination = 'preparation_' + field if field in builder.DECISION_FIELDS else field
                self.assertEqual(row[destination], value, (source['canonical_id'], field))

    def test_legacy_diagnostics_are_explicit_and_adjudication_controls_q3(self):
        for r in self.rows[:100]:
            self.assertIn(builder.LEGACY, r['diagnostic_provenance_primary'])
        for cid in ('CR000004', 'CR000005', 'CR000007'):
            self.assertEqual(self.index[cid]['q1_retrieval_primary'], 'YES')
            self.assertEqual(self.index[cid]['q2_morphology_primary'], 'YES')
        self.assertEqual(self.index['CR000197']['q3_retrieval_component_primary'], 'UNCLEAR')
        self.assertEqual(self.index['CR000197']['screening_label_primary'], 'UNCERTAIN')

    def test_invalid_invariants_and_missing_label_rejected(self):
        include = next(r for r in self.rows if r['screening_label_primary'] == 'INCLUDE')
        uncertain = next(r for r in self.rows if r['screening_label_primary'] == 'UNCERTAIN')
        exclude = next(r for r in self.rows if r['screening_label_primary'] == 'EXCLUDE')
        cases = [(include, {'q2_morphology_primary': 'UNCLEAR'}),
                 (uncertain, {'screening_reason_code_primary': 'TA1'}),
                 (exclude, {'screening_reason_code_primary': 'TA8'}),
                 (include, {'screening_label_primary': ''})]
        for row, mutation in cases:
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                builder.validate_decisions([{**row, **mutation}], 1)

    def test_parquet_equals_csv_and_required_fields(self):
        csv_rows = builder.read_csv(self.out / builder.CSV_NAME)
        parquet_rows = pq.read_table(self.out / builder.PARQUET_NAME).to_pylist()
        self.assertEqual(csv_rows, parquet_rows)
        self.assertTrue(set(builder.REQUIRED) <= set(csv_rows[0]))
        self.assertEqual(len(csv_rows), 2010)

    def test_hash_manifest_and_inputs_unchanged(self):
        for line in (self.out / builder.SHA_NAME).read_text(encoding='utf-8').splitlines():
            digest, name = line.split('  ', 1)
            self.assertEqual(builder.file_sha(self.out / name), digest)
        for path, digest in self.hashes.items():
            self.assertEqual(builder.file_sha(builder.ROOT / path), digest)

    def test_deterministic_outputs(self):
        with tempfile.TemporaryDirectory() as temporary:
            second = Path(temporary)
            builder.build(output_dir=second)
            for name in builder.OUTPUT_NAMES:
                self.assertEqual((self.out / name).read_bytes(), (second / name).read_bytes(), name)


if __name__ == '__main__':
    unittest.main()
