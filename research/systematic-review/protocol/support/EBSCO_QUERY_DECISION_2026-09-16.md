# EBSCO QUERY DECISION — 2026-09-16

## Decision

**USE S4 as the working EBSCOhost query.**

Databases:

- Academic Search Premier
- Science & Technology Collection
- LISTA

Period:

- 2000–2026

Results:

- S1 baseline: 868
- S2: 777
- S3: 623
- S4: **527**

S4 reduced the EBSCO platform count by approximately **39.3%** relative to S1 while retaining:

- 8/8 EBSCO retention controls;
- Can et al. 2008;
- Fautsch & Savoy 2009.

## Important interpretation

The 8 records from the first pilot are now called:

**EBSCO RETENTION-CONTROL SET**

They are not automatically a gold-standard included-study set.

Final inclusion still requires protocol-based screening.

## Screening labels

Use:

- R1 = clearly relevant;
- R2 = potentially relevant;
- X = exclude.

Do not use A/B/C for screening relevance because A/B/C/D is reserved for source reliability in the PhD project.

## Final EBSCO validation before bulk export

Construct a deduplicated Boolean-equivalent `S4-clean`.

Rerun once under identical settings.

Expected count:

**527**

If count = 527:
- accept S4-clean as the final reproducible EBSCO expression.

If count differs:
- preserve exact tested S4;
- investigate EBSCO parsing before bulk export.

## Current stop condition

Do not export all 527 yet.

Proceed to:
1. PQDT Global pilot;
2. ACM DL pilot;
3. IEEE Xplore pilot;
4. ACL Anthology pilot.

Then freeze the cross-platform protocol and perform final exports.
