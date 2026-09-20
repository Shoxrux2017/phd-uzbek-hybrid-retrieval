# Systematic Review State

**Last updated:** 2026-09-20

**Status:** primary title/abstract screening complete; second review not started; full-text stage not started.

This state records the primary-screening milestone before the second-review stage. It does not certify or advance any existing local preparation work.

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
