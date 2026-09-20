# Primary Screening Checkpoint — 2026-09-20

Public-safe research checkpoint after primary title/abstract screening, before second review and full-text assessment. [Current state](../SYSTEMATIC_REVIEW_STATE.md).

## Identification

- Raw source records: **2224**.
- Duplicates removed: **214**.
- Records screened: **2010**.

`2224 - 214 = 2010`.

## Primary labels

| Label | Count |
| --- | ---: |
| INCLUDE | 256 |
| EXCLUDE | 1111 |
| UNCERTAIN | 643 |
| Total | 2010 |

## Exclusion reasons

| Reason | Count |
| --- | ---: |
| TA1 | 705 |
| TA2 | 17 |
| TA3 | 337 |
| TA4 | 26 |
| TA5 | 2 |
| TA6 | 7 |
| TA7 | 17 |
| EXCLUDE total | 1111 |
| TA8 / UNCERTAIN | 643 |

Verified: `705 + 17 + 337 + 26 + 2 + 7 + 17 = 1111`. TA8 is an uncertainty code, not an exclusion reason.

## Quality controls

- Coverage: **2010/2010**.
- Unique IDs: **2010**.
- Missing decisions: **0**.
- Invariant violations: **0**.
- Correction overlays applied: **1** (CR000691).
- Frozen second-review random sample: **402**.
- Primary build regression tests: **18/18 PASS**.
- Repeated build: **BYTE-IDENTICAL**.

These primary-build results are recorded in the preserved [validation artifact](reproducibility/PRIMARY_SCREENING_FINAL_VALIDATION.json) and [final counts](reproducibility/PRIMARY_SCREENING_FINAL_COUNTS.json). Original build/validation artifacts describe the pre-GitHub primary assembly; their historical `github_modified: false` fields do not describe this publication step.

## Major screening history

1. Calibration of Batch 001–002 established application of the screening rules, including Clarification 001.
2. Stable production screening continued with Drift Checkpoints #1–#4 across the workflow.
3. Batch 012 was placed on HOLD for a modality-boundary issue.
4. Clarification 002 distinguished source modality from retrieval modality.
5. A retrospective modality guard checked earlier decisions and produced the explicit correction overlay for CR000691.
6. Screening resumed under the clarified rules, preserving preliminary artifacts and applying finalized-artifact precedence.
7. Batch 021 completion closed primary screening at 2010 records.

No record titles or abstracts are reproduced here. The historical final manifest documents `latest correction overlay > finalized batch artifact > older preliminary artifact`.

## Provenance limitation

**Primary screening was AI-assisted.** It must not later be reported as:

- dual independent human screening;
- two independent human reviewers.

Same-workflow calibration, safety checks and correction overlays do not constitute independent second review.

## Next methodological step

Prepare a reproducible blinded second-review package: **NOT STARTED at this primary-screening checkpoint**. Existing local preparation files, if present in the inventory, are outside the methodological status asserted by this milestone; this publication task does not create, validate or advance that package.

The planned population is `UNION(frozen random 402, all primary UNCERTAIN 643)`. Actual overlap is **NOT YET COMPUTED at this checkpoint** and must be established before review. Keep random-sample agreement/stability analysis separate from targeted uncertainty resolution; do not report one headline agreement statistic on the enriched union.

Actual second review: **NOT STARTED**. Full-text retrieval/screening: **NOT STARTED**. Evidence synthesis remains pending. CURRENT_GAP **v0.8 refined — provisional** is unchanged.
