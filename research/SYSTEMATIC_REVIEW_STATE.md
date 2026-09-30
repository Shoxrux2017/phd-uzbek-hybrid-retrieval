# Systematic Review State

**Last updated:** 2026-09-28

**Status:** primary title/abstract screening complete; second review not started; full-text stage not started.

This state records the primary-screening milestone before the second-review stage. It does not certify or advance any existing local preparation work.

## Update 2026-09-28 — full-text stage (supersedes the "NOT STARTED" statements below)

- Title/abstract stage finished (second review and adjudication completed); **509** records sought for full text (P1 265, P2 244).
- Full texts obtained: **281** of 509; the remaining **228** (mostly paywalled IEEE) are pending library access. Unretrieved records will be coded FT7 and characterised per protocol §4.
- **Tier 1 triage** (281 full texts, AI-assisted, 10% blind retest): 124 INCLUDE / 157 EXCLUDE. After Tier 2, three records were recoded as FT8 duplicate studies, giving **121 INCLUDE / 160 EXCLUDE**. Revisions are logged in `07_full_text/triage/FULL_TEXT_TRIAGE_REVISIONS_2026-09-28.csv`.
- **Tier 2 extraction** (AI-assisted): **121 studies**, using the 60-field schema and frozen codebook v1.0 plus Extraction Clarification 001. Blind retest on 13 studies: 91.9% agreement over 38 categorical fields and 95.9% on core fields. Files are in `07_full_text/extraction/`.
- **Descriptive observation (not synthesis):** no included study reports lexical ↔ dense complementarity decomposition (unique relevant hits / overlap / oracle union). Dense channel: 13 studies. Lexical + dense hybrid: 4 studies.
- **Deep dives:** 41 cards (see `literature/DEEP_DIVES_BATCH_2026-09-28_SUMMARY.md`).
- **Not yet done:** FT7 characterisation of unretrieved records, retrieval of the 228 pending full texts (triage/extraction for those that arrive), and the synthesis protocol and synthesis.
- Provenance: all stages are AI-assisted; none is human full-text review.

## Article

**Title:** “Morphological Representation in Information Retrieval for Morphologically Rich Languages: A Systematic Review of Lexical, Dense, and Hybrid Retrieval with an Uzbek Perspective”

**Primary target:** ACM TALLIP

## Identification

- Raw records: **2224**.
- Duplicates removed: **214**.
- Records entering title/abstract screening: **2010**.

## Primary screening

- INCLUDE: **256**.
- EXCLUDE: **1111**.
- UNCERTAIN: **643**.
- Coverage: **2010/2010**.
- Unique IDs: **2010**; missing decisions: **0**; invariant violations: **0**.

## Screening provenance

Primary screening: **AI-assisted**.

**This is NOT independent dual-human screening.** Calibration, drift checks and corrections within the primary workflow do not establish two independent human reviewers.

## Screening rules

- [TITLE_ABSTRACT_SCREENING_CODEBOOK.md](systematic-review/methods/TITLE_ABSTRACT_SCREENING_CODEBOOK.md)
- [SCREENING_CODEBOOK_CLARIFICATION_001.md](systematic-review/methods/SCREENING_CODEBOOK_CLARIFICATION_001.md)
- [SCREENING_CODEBOOK_CLARIFICATION_002.md](systematic-review/methods/SCREENING_CODEBOOK_CLARIFICATION_002.md)

Clarification 001:

- Retrieval alone does not establish INCLUDE.
- Meaningful morphology relevance is required.
- A pipeline endpoint alone does not establish EXCLUDE; inspect separately evaluated retrieval.
- An unclear relation requires UNCERTAIN.

Clarification 002:

- Speech/audio/ASR origin does not automatically justify TA1.
- Determine the retrieval object and task.
- Clearly non-text retrieval may justify TA1.
- Unclear modality requires UNCERTAIN.
- Word/subword retrieval does not automatically establish INCLUDE.

The original Clarification 001 retains its historical PROPOSED heading; the primary final manifest records its operational authorization. Copies preserve the original files.

## Primary correction overlay

**CR000691:** one explicit correction changes the historical INCLUDE decision to **UNCERTAIN / TA8**. The historical batch artifact remains intact.

Decision precedence:

`latest correction overlay > finalized batch artifact > older preliminary artifact`

The correction is part of the same AI-assisted primary workflow, not an independent second review.

## Second review

- Frozen random sample: **402**.
- Primary UNCERTAIN: **643**.
- Planned second-review population: `UNION(frozen random 402, all primary UNCERTAIN 643)`.
- Actual overlap: **NOT YET COMPUTED at this checkpoint**.
- Second review: **NOT STARTED**.

Keep the two cohorts analytically distinct: the frozen random cohort supports agreement/stability analysis; the UNCERTAIN cohort supports targeted uncertainty resolution. Calculate overlap before review. Do not compute one headline agreement statistic on the enriched union.

## Full text

Full-text retrieval/screening: **NOT STARTED**.

## Relation to PhD research gap

Completion of primary screening does **NOT** by itself change CURRENT_GAP **v0.8 refined**, which remains **provisional**. Evidence synthesis and full-text assessment are still pending.

Therefore, [research/CURRENT_GAP.md](CURRENT_GAP.md) remains unchanged, as does GAP_HISTORY.md. Screening counts are workflow information, not scientific evidence revising the gap. Provisional INCLUDE records have not been integrated into MASTER_INDEX as validated evidence by this checkpoint.

## Local data

Operational artifacts remain local under `artifacts/systematic-review-v1.0/`.

They are intentionally not committed because the repository is public and the local dataset contains record-level bibliographic metadata/abstracts from multiple databases. Public release requires a separate audit.

See [PRIMARY_SCREENING_CHECKPOINT_2026-09-20.md](systematic-review/PRIMARY_SCREENING_CHECKPOINT_2026-09-20.md) for the public checkpoint and its quality controls.

## Update 2026-09-29 — acquisition round 3 and synthesis plan

- Round 3 (author requests by e-mail, 25 letters sent 2026-09-28 from the researcher's Gmail by the AI on the researcher's instruction; log in `07_full_text/acquisition_round3/SENT_LETTERS_LOG_2026-09-28.csv`): **9** further full texts obtained (8 from authors, 1 arXiv preprint). Full texts now **290** of 509; **219** not retrieved.
- Tier 1 triage of the 9 (AI-assisted, `FULL_TEXT_TRIAGE_AI_FT_01_ROUND3.csv`): **4 INCLUDE** (CR001997, CR000430, CR001199, CR000550) / **5 EXCLUDE** (CR001186 FT1; CR001174, CR001767, CR002054, CR001060 FT2). Included studies now **125**.
- Tier 2 extraction of the 4 (AI-assisted, `FULL_TEXT_EXTRACTION_AI_EX_01_ROUND3.csv`, validated). CR001199 (Turkish, raw vs lemma under BM25 and dense mE5) is the closest study to the gap design; it reports aggregate comparisons only, no complementarity decomposition.
- Two related 2018 papers by El Mahdaouy et al. were sent by the author but were not identified by the database search; stored in `acquisition_round3/other_sources_not_in_search/`, not screened. Decision pending on "identification via other methods".
- Synthesis plan **frozen** 2026-09-29 (`08_publication/SYNTHESIS_PLAN_v1.0.md`, SHA-256 in `SYNTHESIS_PLAN_FREEZE_SHA256.txt`); written after extraction, before synthesis.
- Provenance: all stages AI-assisted; human verification sample issued 2026-09-28 (`09_human_verification/`), not yet returned.
