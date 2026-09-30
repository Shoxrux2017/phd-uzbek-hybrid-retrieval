# ACL PILOT DECISION — 2026-09-17

## Current status

A1:
- 83 hits
- seeds found: 2/3
- UPERF missed because ACL metadata has no abstract and title uses standalone `Retrieval`

A2:
- 180 hits
- A2-only: 157
- UPERF also missed

## Decision

Keep **A1 unchanged**.

Run one controlled refinement for the supplemental language-sensitive layer:

**A2R = A2 with standalone whole-word `retrieval` added to the Retrieval Block.**

Do not use the narrower ad hoc rule restricted only to missing abstracts.

## Why

A2 is the sensitivity layer. Requiring the Language Block already constrains the search enough to test a broader retrieval token cleanly.

The refinement should recover UPERF and may recover other language-specific retrieval papers whose titles use only the generic word `retrieval`.

## Acceptance rule

Use A2R if:
- UPERF is recovered;
- all A2 records are retained;
- added volume is manageable;
- new records contain useful R1/R2 evidence or acceptable sensitivity noise.

Otherwise keep A2.

## After this test

Perform:
1. EBSCO S4-clean equivalence check;
2. archive final queries/scripts;
3. freeze protocol v1.0.
