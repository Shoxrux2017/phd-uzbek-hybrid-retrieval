# Systematic review — public checkpoint

This directory records the primary title/abstract screening milestone of 2026-09-20 for the morphology-and-retrieval systematic review targeting ACM TALLIP. It is a public-safe snapshot, not a copy of the local operational dataset.

Start with [Systematic Review State](../SYSTEMATIC_REVIEW_STATE.md) and the [primary-screening checkpoint](PRIMARY_SCREENING_CHECKPOINT_2026-09-20.md). Primary screening is complete: **256 INCLUDE / 1111 EXCLUDE / 643 UNCERTAIN**, from **2010** screened records after **214** duplicates were removed from **2224** raw records. Screening was **AI-assisted**, not independent dual-human screening. CURRENT_GAP **v0.8 refined** remains unchanged and provisional.

## Public methodology

Audited, byte-preserved copies from the original primary-screening directory:

- [TITLE_ABSTRACT_SCREENING_CODEBOOK.md](methods/TITLE_ABSTRACT_SCREENING_CODEBOOK.md)
- [SCREENING_CODEBOOK_CLARIFICATION_001.md](methods/SCREENING_CODEBOOK_CLARIFICATION_001.md) — copied from `03_title_abstract_screening/results/batch_001/`; its historical PROPOSED heading is preserved, while the final assembly manifest records operational authorization.
- [SCREENING_CODEBOOK_CLARIFICATION_002.md](methods/SCREENING_CODEBOOK_CLARIFICATION_002.md)

The original primary versions were selected, rather than later reviewer-packet adaptations. These documents contain methodological rules and limited internal-ID decision examples, without record titles, copied abstracts or database metadata dumps. Historical preparation-stage wording remains part of their provenance; the linked current state governs workflow status.

The following requested methodology files were **not found** anywhere under `artifacts/systematic-review-v1.0/`, so no copies were created:

- `ARTICLE_RESEARCH_PROTOCOL_v1.0_FROZEN.md`
- `SYSTEMATIC_REVIEW_EXECUTION_CHECKLIST_v1.0.md`
- `PROTOCOL_AMENDMENT_001_EBSCO_PER_DATABASE_EXPORT.md`

## Public reproducibility

Audited, byte-preserved copies from `03_title_abstract_screening/`:

- [build_primary_screening_master.py](reproducibility/build_primary_screening_master.py)
- [test_build_primary_screening_master.py](reproducibility/test_build_primary_screening_master.py)
- [PRIMARY_SCREENING_FINAL_COUNTS.json](reproducibility/PRIMARY_SCREENING_FINAL_COUNTS.json)
- [PRIMARY_SCREENING_FINAL_SHA256.txt](reproducibility/PRIMARY_SCREENING_FINAL_SHA256.txt)
- [PRIMARY_SCREENING_FINAL_VALIDATION.json](reproducibility/PRIMARY_SCREENING_FINAL_VALIDATION.json)
- [PRIMARY_SCREENING_FINAL_MANIFEST.md](reproducibility/PRIMARY_SCREENING_FINAL_MANIFEST.md)
- [SCREENING_CORRECTIONS_CLARIFICATION_002.csv](reproducibility/SCREENING_CORRECTIONS_CLARIFICATION_002.csv)

The correction CSV contains one internal ID, decision changes and reviewer rationale; it contains no title, copied abstract, DOI, author list or licensed metadata dump. Counts and manifests contain aggregate results, internal provenance identifiers and hashes. All ten copied files passed content and size inspection; no whitelist file was withheld for sensitive contents.

The code and tests depend on non-public local inputs and their original directory layout. They are provided for inspection and provenance; a public-only checkout cannot rebuild the screening master or run the complete regression suite. With authorized local inputs, run the original scripts using their original layout, disable Python bytecode writes, and direct build outputs to a separate temporary directory to preserve the checkpoint. The pinned build dependency is `pyarrow==25.0.1`.

The preserved validation records **18/18 PASS** and **BYTE-IDENTICAL** repeated output. `github_modified: false` and similar scope fields describe the original primary build, before this GitHub checkpoint. The final SHA file describes historical output bytes, including local-only CSV/parquet files; it is not a list of files released publicly. The scoped `.gitattributes` disables line-ending conversion for methodology and reproducibility copies so their published bytes retain the original hashes.

## Local data and exact artifact inventory

Raw database exports, bibliographic masters, batch inputs/results with metadata, mass abstracts, PDFs/full texts, reviewer queues and private second-review keys remain local. The public repository does not redistribute licensed/proprietary row-level data. `.gitignore` excludes the entire `artifacts/systematic-review-v1.0/` tree pending a separate public-release audit.

[LOCAL_ARTIFACT_MANIFEST_2026-09-20.txt](LOCAL_ARTIFACT_MANIFEST_2026-09-20.txt) inventories **every file present in that local tree at checkpoint publication** using tab-separated `relative_path`, `size_bytes`, and `sha256`, sorted by relative path ascending. Paths are relative to `artifacts/systematic-review-v1.0/`. It includes hidden/cache and existing preparation files; it exposes no file contents. The inventory binds the exact local bytes observed, but does not certify the methodological status or validity of every inventoried file.

The inventory therefore also lists the pre-existing `04_second_review_preparation/` directory. None of its contents is released or modified by this task, and its existence does not alter the requested primary-screening milestone status.

## Next stage

The next stage is blinded second review. At the primary-screening milestone, package preparation is **NOT STARTED**, actual second review is **NOT STARTED**, and full-text retrieval/screening is **NOT STARTED**. This publication task does not advance any of them.

The design uses the union of a frozen random sample of **402** and all **643** primary UNCERTAIN records, with overlap still to be calculated for this checkpoint. Analyze random-sample agreement/stability separately from targeted uncertainty resolution; do not compute one headline agreement statistic on the enriched union. Provisional INCLUDE decisions are not validated study-level evidence and are not added to MASTER_INDEX here.
