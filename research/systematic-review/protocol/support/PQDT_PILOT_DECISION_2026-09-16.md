# PQDT GLOBAL PILOT DECISION — 2026-09-16

## Current status

P1 pilot completed.

- Database: ProQuest Dissertations & Theses Global
- Field: NOFT
- Date range: 2000–2026
- Results: 123
- First 50: R1=20, R2=15, X=15
- R1+R2: 70%

## Required final refinement

ProQuest standard `*` truncation replaces up to 5 characters.

Therefore replace both:

`lemmat*`

with:

`lemmat[*10]`

and call the new query **P2**.

No other change is allowed during this test.

## Why

`lemmat*` may fail to cover:

- lemmatization
- lemmatisation

The refinement is a recall correction, not a precision optimization.

## Do not yet change

- database
- NOFT field
- date range
- document type
- language
- subject
- university/country
- proximity operators
- any other term

## Doctoral/master's decision

Do not apply doctoral-only during P2.

After P2, handle master's theses as a separate evidence-policy decision.

## Next decision

If P2 preserves P1 relevant records and behaves normally, accept P2 as the working PQDT query.
