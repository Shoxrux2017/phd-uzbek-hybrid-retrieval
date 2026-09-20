# PRIMARY TITLE/ABSTRACT SCREENING COMPLETE

Assembly version: 1.0.0. Review date: 2026-09-20.

**Primary screening was AI-assisted and is NOT an independent dual-review process.**

Reviewer: Codex, AI-assisted primary screening. Historical reviewer descriptions and review dates are retained. Batch 002 uses the same-workflow AI-assisted calibration-adjudication role and date documented in its final report. No independent second review was performed.

## Frozen codebook versions

- TITLE_ABSTRACT_SCREENING_CODEBOOK.md: v1.0.0; frozen 2026-09-18.
- Clarification 001: dated 2026-09-20; operationally authorized. Its original PROPOSED heading remains unchanged.
- Clarification 002: dated 2026-09-20; adopted operational clarification. No eligibility change.

## Decision precedence and provenance

latest explicit correction overlay > finalized batch artifact > older preliminary artifact.
Only the explicit 21-file list below supplies decisions. Batch 001/002/012 use *_SCREENED_FINAL.csv. Preliminary Batch 012 and original non-final Batch 001/002 are never loaded. The preparation master supplies original metadata and frozen sample flags only, after the Batch 021 PASS gate; it is not screening evidence. MASTER_INDEX is not loaded.

All preparation metadata fields and values are retained. Its six empty decision fields have preparation_ prefixes. Final primary decisions have distinct *_primary fields. The complete finalized source row is also preserved in finalized_source_row_json. No historical primary label is changed except the authorized explicit overlay.

Batch 001 lacks structured gates. PRIMARY_SCREENING_LEGACY_DIAGNOSTICS.csv transcribes only its finalized rationales, with unrecorded/unresolved diagnostic details kept UNCLEAR; it supplies no labels. Batch 002 gates come from Pass B embedded in the FINAL file, except CR000197, whose final adjudication explicitly retains Pass A uncertainty about Q3. This schema harmonization is not a new screening pass. Legacy diagnostic provenance is stored per row.

The correction ledger explicitly changes CR000691 Q1 to UNCLEAR and retains Q2=YES. Q3 is not specified by that ledger and is preserved from the historical artifact; no new diagnostic claim is inferred. Original batch label/code and source remain available. The ledger records same-primary-workflow correction but no separate reviewer identity, so the historical reviewer is retained and this limitation is explicit.

## Counts

| Item | Count |
| --- | ---: |
| Input canonical records | 2010 |
| Finalized batches 001–020 | 2000 |
| Batch 021 | 10 |
| Output rows / unique canonical IDs | 2010 / 2010 |
| INCLUDE | 256 |
| EXCLUDE | 1111 |
| UNCERTAIN / TA8 | 643 |
| Frozen random second-review sample | 402 |

Batch 021: INCLUDE 3; EXCLUDE 5; UNCERTAIN 2. Safety changes: 1; codebook issue: NO; validation: PASS.
Baseline after overlay: 253 / 1106 / 641. Adding Batch 021 gives 256 / 1111 / 643. The existing overlay is applied once to the historical batch decision, not again to the already corrected baseline.

| Exclusion reason | Count |
| --- | ---: |
| TA1 | 705 |
| TA2 | 17 |
| TA3 | 337 |
| TA4 | 26 |
| TA5 | 2 |
| TA6 | 7 |
| TA7 | 17 |

## Correction overlay validation

Corrections applied: 1. All ledger IDs exist; each is applied exactly once; final label and code equal the latest explicit ledger. Historical Batch 007 remains unchanged.

| Canonical ID | Ledger CSV row | Historical label | Effective label / reason |
| --- | ---: | --- | --- |
| CR000691 | 2 | INCLUDE | UNCERTAIN / TA8 |

## Validation

PASS: complete screening_order 1..2010; coverage 2010/2010; 2010 unique IDs; missing decisions 0; duplicate final decisions 0. INCLUDE, UNCERTAIN and EXCLUDE invariant violations are all 0. No INCLUDE gate exception is required. All 402 frozen random sample IDs and flags are preserved without resampling.
Bibliographic metadata match the preparation master and original reviewer packets. All historical batch hashes and the overlay hash match Production Drift Checkpoint #4. All inputs are rehashed before and after writing outputs. Original TA_BATCH_021.csv matches its screening summary hash.

## Deterministic assembly and regression tests

Run `python build_primary_screening_master.py` from this directory. Optional `--output-dir` writes the same five outputs elsewhere. Run `python -m unittest discover -s . -p test_build_primary_screening_master.py -v` for regression tests.
Requires pyarrow==25.0.1. Stable screening-order rows, explicit column order, UTF-8 CSV with LF row delimiters, sorted JSON keys, fixed Parquet schema/settings and no wall-clock values. All Parquet columns are strings to preserve source values exactly. The SHA file covers CSV, Parquet, counts and this manifest; the manifest excludes its own hash to avoid a circular hash dependency.
Regression tests verify counts, coverage, metadata preservation, invariants, correction precedence, frozen sample, Batch 021, failure paths, Parquet equivalence and byte-identical repeated output. Actual execution results are reported separately after running the suite.

## Authoritative batch artifacts

| Batch | Records | Finalized source | SHA-256 |
| --- | ---: | --- | --- |
| 001 | 100 | `results/batch_001/TA_BATCH_001_SCREENED_FINAL.csv` | `7b4527ebb1df2c238aeb5135b8a56468b800f78372cc1183b487119434c40196` |
| 002 | 100 | `results/batch_002/TA_BATCH_002_SCREENED_FINAL.csv` | `2f3362e5da36978d533912a154933251628361d163ee7b1254529a5f378197d3` |
| 003 | 100 | `results/batch_003/TA_BATCH_003_SCREENED.csv` | `82b60eff0ca2e5980c48e501b861d643f0ac0e42f9e0fa672154e4baed7a1272` |
| 004 | 100 | `results/batch_004/TA_BATCH_004_SCREENED.csv` | `d9797599282775cade8180cd47d5c031a7b19baa99e069a4d4c8d2aa6d3d3305` |
| 005 | 100 | `results/batch_005/TA_BATCH_005_SCREENED.csv` | `0ad0d37b00a7d6eaaf52c40291b3d8d8701bb564f9a285f74a81c033561e6e52` |
| 006 | 100 | `results/batch_006/TA_BATCH_006_SCREENED.csv` | `471d5391e663b2c7d602ce6a3862d2299dfa967ed37645f95cc16b4d737e60c2` |
| 007 | 100 | `results/batch_007/TA_BATCH_007_SCREENED.csv` | `b82dbd97ccde8c490f57ef03d9c8706562247444d1624d125f4d32639b1436d4` |
| 008 | 100 | `results/batch_008/TA_BATCH_008_SCREENED.csv` | `1b59773121010085484f4161bc4de24010788039f6ad7b1dfa04a14deabbe634` |
| 009 | 100 | `results/batch_009/TA_BATCH_009_SCREENED.csv` | `6600a59c8c219a7fe268724aa4c0f1be4066d0a0d3df7b1a26d5a86f6bd31741` |
| 010 | 100 | `results/batch_010/TA_BATCH_010_SCREENED.csv` | `4a1d155b140824852762e09c93505edd5531bde05c0001e9e283793b7919848f` |
| 011 | 100 | `results/batch_011/TA_BATCH_011_SCREENED.csv` | `b203fc863155ea3b3a0d7ca6146a76e5378ae79ffe3f64ad75d3b4350741bc53` |
| 012 | 100 | `results/batch_012/TA_BATCH_012_SCREENED_FINAL.csv` | `0cb13ec18c487bd79083fb8ade537c4262ea63d95a31672711bd4518fdfcc82f` |
| 013 | 100 | `results/batch_013/TA_BATCH_013_SCREENED.csv` | `e252164510f274f3b6483973a3e020e2e54865337183b8f464cb81b5dca45a11` |
| 014 | 100 | `results/batch_014/TA_BATCH_014_SCREENED.csv` | `47eece4d8bebbb3ef87285acb37eb312c590d6f0453c5625e8ad3550e2c18e34` |
| 015 | 100 | `results/batch_015/TA_BATCH_015_SCREENED.csv` | `59a7cef10ff0163fc779648df4842fe5b3a020cb63e712a305fc58777f67ac42` |
| 016 | 100 | `results/batch_016/TA_BATCH_016_SCREENED.csv` | `e3de7e3f2e9503b2c64896734b3bcf286d7444031e0509628523ebb4eeed6a5b` |
| 017 | 100 | `results/batch_017/TA_BATCH_017_SCREENED.csv` | `205140266f6b43d763ffd57a70038de0ba1a041345cb11c707321249cd520369` |
| 018 | 100 | `results/batch_018/TA_BATCH_018_SCREENED.csv` | `d866064f37577264511c60688ef22fff887799e7d07f6af25077df490a1c2e7f` |
| 019 | 100 | `results/batch_019/TA_BATCH_019_SCREENED.csv` | `2f722346724ad5fee1339ff517f4cb0ce204a4fbc963b7812728d95796744680` |
| 020 | 100 | `results/batch_020/TA_BATCH_020_SCREENED.csv` | `67c0e879ac4552d63a91d799255af97d2f3806b3524622fc50067a579b51fbfc` |
| 021 | 10 | `results/batch_021/TA_BATCH_021_SCREENED.csv` | `e3beba3dcad0dceb736208bd49f300a8bcdfc068829a464a9d9c0021ad328e91` |

## Other inputs and implementation SHA-256

| Artifact | SHA-256 |
| --- | --- |
| `PRIMARY_SCREENING_LEGACY_DIAGNOSTICS.csv` | `0a0264022af28591a8435cd127c79ca3bd306b1ee9d1bf94e0c3e772a239d31d` |
| `PRODUCTION_DRIFT_CHECKPOINT_004.json` | `326d2f5d5dd447d4b74374c859dce030551ac85bbe3ce19cf91e9ab20a65a45e` |
| `SCREENING_CODEBOOK_CLARIFICATION_002.md` | `eecea05807fe9c6e98b7a05349a144452891bf94c74cf555d4973ef38d221870` |
| `SCREENING_CORRECTIONS_CLARIFICATION_002.csv` | `a5fd85ce595742d29ab884f377e8fcc0c7a81e092f9b5cd772694562806ebbcb` |
| `SECOND_REVIEW_SAMPLE_20_PERCENT.csv` | `0d8548fa9b543fc4d538d1a39bc1dbc8e27bcde07c8196d5a814630c5d6a18e6` |
| `TITLE_ABSTRACT_SCREENING_CODEBOOK.md` | `dd9f3b798f2fdb8d60b9e019b2a1c344c6a72469b5c36bd40b4e468fa76ac648` |
| `TITLE_ABSTRACT_SCREENING_MASTER.csv` | `450e0a7da3261715b8e3b572e9cc8e95b00eccda5ac55df7b00a0c810c54375d` |
| `batches/TA_BATCH_001.csv` | `523c83a55727fdfa510e921caca5235528d781b64aadee8fe1d6efe064f8082f` |
| `batches/TA_BATCH_002.csv` | `bbbdc3a64d379bca56cc931995e5c7f7cf9f7b5f67207a7baa3402ae101231f9` |
| `batches/TA_BATCH_003.csv` | `90b497c97eee71a585924f100c50d5ec940b341e349c5514b9507d313b932e3e` |
| `batches/TA_BATCH_004.csv` | `8711c28bc0ca7ff921d27ea66df40d81fe20ebff99b663d1dd49be42430a3021` |
| `batches/TA_BATCH_005.csv` | `4d5ae91748c38ff76f7007574ef17105f51c122e8b58dc7aa13b4e78b4af6c5a` |
| `batches/TA_BATCH_006.csv` | `fc02cbfc27d019716821d0998220a97c4b433e9c42deccdd35098d0048f06791` |
| `batches/TA_BATCH_007.csv` | `e331062e8c07c294488e87acc382cc61776a3340ed5c3493fb3987af67db382e` |
| `batches/TA_BATCH_008.csv` | `bd37aee84a3e67974424db49f2686874ea4280a2efa444f91a12aa35df102c5d` |
| `batches/TA_BATCH_009.csv` | `2f0b7c3e51ea0c7d25a4249c91988ef539550897add7d07f7d9bbbb6d49892bc` |
| `batches/TA_BATCH_010.csv` | `dadb193f89418664a79bf3a3c1c815b9f8a070d79041ae7221b8dcbc459f1bf3` |
| `batches/TA_BATCH_011.csv` | `e4bb4f51fbc9c16ef25d239a56d5e172ce1621459fb28e82506cc41f658de138` |
| `batches/TA_BATCH_012.csv` | `8c29f1f48a09a2edf3598c7399080ef5a8b853b6aa5e3af9e5074f7f606011f0` |
| `batches/TA_BATCH_013.csv` | `924c5daf8f670f52e85e46a0896d657c48fa067d632a8fb7b6e3d5bc81a922f1` |
| `batches/TA_BATCH_014.csv` | `8c88400dc52d9e6a9e3fc7463e6d3edd1723598bfc9dcbe84d428779237ac7a4` |
| `batches/TA_BATCH_015.csv` | `f985af8398ad2012489a425315ab331cf5ceb087f91a63bef8e2095baf85d5f0` |
| `batches/TA_BATCH_016.csv` | `c7be60286c32c16621e0f81306453e95c08de22430c66ae4e2de98fd6d693829` |
| `batches/TA_BATCH_017.csv` | `d407181320b01ea6a6e4c65e9f8f09920914139b3b865a0345378b44879d3121` |
| `batches/TA_BATCH_018.csv` | `8c008fef4dac5c4aa43a0af540761353b7672873a8ef4cee65fd8572bd5a20a5` |
| `batches/TA_BATCH_019.csv` | `b759e548dde0c4ea021abdb650846ce27aa0098e30e46875b4f9fec65696f51b` |
| `batches/TA_BATCH_020.csv` | `61ed567d53efbc0636d675145bc6e396f5a267edadee07c78ccc13a9e55bd0ba` |
| `batches/TA_BATCH_021.csv` | `412319626286c54463dbad4273ce6efc936acd1bc85b1aa360020f35d78c46bb` |
| `build_primary_screening_master.py` | `4b8e823e13ff47ac84255890d6db629075646878afd03706933a508951005e42` |
| `results/batch_001/SCREENING_CODEBOOK_CLARIFICATION_001.md` | `e610d1f88bff99e17d04304c57d8cb8a1cc91c875b896ca9069be48baaede49a` |
| `results/batch_002/TA_BATCH_002_RECALIBRATION_REPORT.md` | `0d348d3f8194cefa0d5ee5eaaa8a63ea8a3cbe62c6de3f2ff38e19db35ee8779` |
| `results/batch_021/TA_BATCH_021_SCREENING_AUDIT.md` | `5fb7cc4dcbed46a287d7f8076437d902b9cdeae4c8a21bd6c57222a33e40455f` |
| `results/batch_021/TA_BATCH_021_SCREENING_SUMMARY.json` | `449b37f8b3874a7ea2362bd6091a56275da1886dbbc13af3ff5188e5e6beb58c` |
| `test_build_primary_screening_master.py` | `d5f7122c58f97d7d85ca1e6256f1afd5c6b3415e4112b714277e94b1ea79895c` |

## Output SHA-256

| Artifact | SHA-256 |
| --- | --- |
| `TITLE_ABSTRACT_SCREENING_PRIMARY_FINAL.csv` | `d548acd0644a9e4bf10c79749fe1adac563335e093de1f338a41b977e3d8a5ba` |
| `TITLE_ABSTRACT_SCREENING_PRIMARY_FINAL.parquet` | `f856797698e18a7330a77efe67344613c8312695d51f4beceeab41d71cb40b5d` |
| `PRIMARY_SCREENING_FINAL_COUNTS.json` | `672688326189ba7faaee02a0d13a655d6de96cacddde9a6526d29b468f6db7b1` |

The manifest hash is in PRIMARY_SCREENING_FINAL_SHA256.txt.

## Scope and stop

No web, publisher pages, Google Scholar, PDFs, full texts, MASTER_INDEX, prior study memory or pilot labels were used to screen Batch 021. No GitHub changes, independent second review, full-text retrieval or further primary-decision changes were performed. STOP after primary assembly and validation.
