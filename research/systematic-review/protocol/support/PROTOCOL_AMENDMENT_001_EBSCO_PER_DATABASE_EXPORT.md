# PROTOCOL_AMENDMENT_001 — EBSCO PER-DATABASE EXPORT

**Protocol:** `ARTICLE_RESEARCH_PROTOCOL_v1.0_FROZEN.md`  
**Amendment ID:** A001  
**Date:** 2026-09-18  
**Status:** ACCEPTED TECHNICAL EXECUTION AMENDMENT  
**Scientific query logic changed:** NO

## Trigger

The frozen EBSCO S4 search was run jointly across:

1. Academic Search Premier
2. Science & Technology Collection
3. Library, Information Science & Technology Abstracts (LISTA)

The interface continued to show a headline count of **527**, but the result list later reported **323 unique records**. After session restoration, Relevance ordering also changed, making continuation of position-based batch export unsafe.

The first session had already exported canonical partial files covering:

- RIS: positions 1–250
- CSV: positions 1–200

These files remain immutable audit artifacts but are no longer sufficient as the canonical complete EBSCO corpus.

## External platform behavior

EBSCO documentation states that duplicate records can be removed from multi-database search results by comparing citation metadata, with the richer record retained for display.

Therefore a multi-database result list can obscure database-specific duplicate provenance and can make position-based continuation unsuitable for systematic-review export.

## Amendment

For the final systematic-review raw export, run the **same exact tested S4 query separately in each of the three frozen EBSCO databases**.

No search term, wildcard, proximity operator, field, year limit, or conceptual criterion may change.

Use the same frozen settings:

- 2000–2026
- Proximity / Boolean
- All fields
- Equivalent subjects OFF
- Related words OFF
- AI search OFF
- Full Text OFF
- Peer Reviewed OFF
- no language restriction
- no publication-type restriction
- no NOT filter

Export the complete result set from each database independently.

Preferred export method:

**Export results (up to 25,000)**

when available in the authenticated EBSCO interface, to avoid position-based batching and unstable relevance ordering.

Preferred formats:

- RIS
- CSV

## Canonical EBSCO raw corpus

The canonical EBSCO input to later merge/deduplication will be the union of the three independent database exports.

Every record must retain its originating EBSCO database.

The earlier combined-database partial batches remain in the audit trail and must **not** be merged into the canonical corpus once complete per-database exports are available.

## Counts

Record separately:

- `n_ASP`
- `n_STC`
- `n_LISTA`
- sum before deduplication

Do not force the sum to equal the earlier combined headline count of 527.

Also record the platform observation:

- combined S4 headline count: 527
- combined result-list unique message: 323

After independent export, deduplicate the three database datasets using the frozen project deduplication protocol.

Compare the independently deduplicated union with the EBSCO-reported 323 unique records as a reconciliation check, not as a required equality constraint.

## PRISMA consequence

For final PRISMA/PRISMA-S reporting, use the independently exported database-specific counts as the authoritative EBSCO identification counts.

Document EBSCO's automatic multi-database deduplication behavior and explain why independent per-database exports were used.

## Prior partial files

The existing partial combined-database exports and technical attempts are audit evidence only.

They must remain immutable and be clearly tagged as:

`NON_CANONICAL_PARTIAL_COMBINED_EBSCO_EXPORT`

They must not be added to the final master dataset once the three complete per-database exports are obtained.

## Scientific impact

None.

This amendment changes only the export/provenance strategy. It does not change:

- the review questions;
- eligibility criteria;
- S4 conceptual query;
- search years;
- EBSCO database set;
- screening rules;
- evidence synthesis.
