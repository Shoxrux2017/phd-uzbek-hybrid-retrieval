# SCOPUS PILOT — PRE-AUTHENTICATED AUDIT

**Project:** Systematic review for the Uzbek Hybrid IR PhD  
**Date:** 2026-09-16  
**Status:** COMPLETED AS FAR AS PUBLIC ACCESS ALLOWS  
**Authenticated Scopus run:** NOT COMPLETED — direct Scopus endpoint returned HTTP 403 in the current environment  
**Protocol tested:** ARTICLE_RESEARCH_PROTOCOL v0.2 → candidate query refined to v0.3

## 1. Purpose

Test whether the planned Scopus Boolean strategy is likely to retrieve known critical morphology-aware IR studies without over-constraining the review to papers that explicitly self-label as low-resource or morphologically rich.

## 2. Result

The core retrieval × morphology query has strong conceptual seed recall, but a single query is insufficient. Two known neighboring studies (GreekBarRetrieval 2026 and Kazi & Khoja 2026 U-RR²) do not foreground explicit morphology terminology in title/abstract and therefore require language-sensitive supplemental searching and citation chaining.

## 3. Candidate core query

Use the exact v0.3 query recorded in `ARTICLE_RESEARCH_PROTOCOL_v0.3.md`.

## 4. Seed audit

- Direct expected core matches: **12/14**
- Not guaranteed by title/abstract morphology terminology: **2/14**
- Conceptual core recall: **85.7%**
- Expected recovery after supplemental language search/citation chaining: **14/14 candidates exposed for screening**

## 5. Precision decision

Do not add aggressive `NOT` exclusions. Public-search simulation shows some contextual NLP noise (e.g. lemmatizer papers mentioning IR only as an application), but such records are safer to remove during screening than through exclusion clauses that could also remove relevant IR studies.

## 6. Critical distinction

Query recall and database coverage are different. This audit tests query wording; it cannot prove that every seed is indexed in Scopus. Scopus coverage must be checked during the authenticated run.

## 7. Freeze decision

**DO NOT FREEZE v1.0 YET.**

Next state:

`ARTICLE_RESEARCH_PROTOCOL_v0.3`
→ authenticated Scopus pilot
→ authenticated WoS pilot
→ one final query adjustment if justified
→ `ARTICLE_RESEARCH_PROTOCOL_v1.0 FROZEN`
