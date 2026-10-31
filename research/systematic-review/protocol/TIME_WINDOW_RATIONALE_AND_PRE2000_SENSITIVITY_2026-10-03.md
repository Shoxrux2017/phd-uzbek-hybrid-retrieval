# Time window 2000–2026: rationale and pre-2000 sensitivity check

Decision by the first author on 2026-10-03 ("Вариант А"). Prepared with AI assistance (Claude).

This document records the reasoning and planned method for keeping the 2000–2026 window and adding a pre-2000 sensitivity check. The steps are specified before any pre-2000 full text is read.

## 1. Decision
The primary-study window stays **2000-01-01 – 2026-12-31**, unchanged from protocol §5. No database search is rerun. Two things are added:
- an explicit rationale for the lower bound, so the window is no longer an unexplained limit;
- a pre-specified **sensitivity check** on eligible-except-date studies from before 2000 that were identified by citation chasing (§6.4).

## 2. Why the lower bound needed a rationale
Methodological guidance accepts date limits only when they are reported and justified:
- **Cochrane Handbook, ch. 4:** date limits are acceptable "as long as the restriction is reported and justified", ideally tied to an event such as the date an intervention became available.
- **SuRe Info:** a date restriction belongs in the search only if it is part of the eligibility criteria.

Surveys of stemming do not limit dates:
- Moral et al. 2014 covers 1968–2013;
- Singh & Gupta 2016 sets no limit.

Recent systematic reviews tend to use short windows without saying why:
- regional Indonesian stemming, 2014–2023;
- RAG, 2020–2025.

The frozen protocol justified 2000 only generically (v0.1 §8: "modern multilingual and language-specific morphology-aware retrieval literature … pre-neural lexical era … comparison with dense/hybrid"). Peer review is likely to ask for a better reason.

## 3. Rationale for 2000 (proposed manuscript wording)
> The lower bound marks the start of shared, large-scale evaluation campaigns for retrieval in languages other than English. CLEF ran its first campaign in 2000 (workshop, Lisbon, 21–22 September 2000; a multilingual newspaper corpus). The first large Arabic retrieval test collection followed in the TREC-2001 cross-language track (383,872 AFP news stories). These campaigns later added morphologically rich languages such as Finnish, Swedish, Hungarian, Bulgarian and Czech. From then on, morphological indexing choices were evaluated on shared collections with pooled relevance judgements, which makes results comparable across studies — the precondition for the cross-study synthesis planned here (RQ1–RQ3). The dense and hybrid comparisons central to RQ4–RQ5 appear only after 2019, so the lower bound does not affect them. Pre-2000 studies were typically single-site experiments on small or locally built collections (for example Slovene, Turkish and Arabic bibliographic sets); we treat them in a separate sensitivity check rather than mixing them into the main synthesis.

Caveats that must be stated honestly:
- CLEF 2000 itself covered only English, French, German and Italian. The morphologically rich languages arrived in later CLEF years (from 2001–2002).
- Some pre-2000 studies used valid shared collections, for example TREC-based English experiments (Hull 1996; Xu & Croft 1998).

The rationale is therefore about comparability and scope, not a claim that earlier evidence is invalid.

## 4. Pre-2000 sensitivity check (pre-specified)
- **Source.** Only pre-2000 records found by citation chasing from the 30 seeds: 470 identified, 467 unique. No new database search is run. Report this limitation: the pre-2000 set is not a systematic sample.
- **Screening.** AI_CC_01 screens title and abstract with date ignored: 15 INCLUDE, 29 UNCERTAIN, 423 EXCLUDE. The first author then reviews blind all 44 advanced records, a random 10 of the exclusions and 2 consistency checks (Lovins, Dawson), using `PRE2000_SENSITIVITY_REVIEW_BLIND_2026-10-03.xlsx`.
- **Full text.** Studies advanced by either reviewer are retrieved where possible and assessed with the same full-text criteria A/B/C.
- **Minimal extraction.** For each eligible pre-2000 study, record:
  - language;
  - collection (size, queries, qrels source);
  - representations compared;
  - metric;
  - direction of the morphology effect (raw < stem/lemma/root, equal, or worse);
  - any per-query, query-type or failure analysis.
- **Comparison.** A narrative comparison with the main-synthesis findings for RQ1 (direction and consistency of the morphology effect by typology) and for complementarity-relevant analyses. The question is whether including these studies would change any conclusion. There is no pooling with the main set and no change to the main counts.
- **Reporting.** One sentence in Methods, one short paragraph plus a supplementary table in Results/Discussion, and a PRISMA note. Pre-2000 records "removed before screening (outside date range)" are reported in the citation-chasing arm.

## 5. Status on 2026-10-03
- AI screening is done (decisions in `11_citation_chasing/_KEY_do_not_open_before_finishing/PRE2000_AI_SCREENING_AI_CC_01_2026-10-03.csv`).
- The first author's blind review is pending.

## Sources
- Cochrane Handbook, Chapter 4: https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-04
- SuRe Info, Other limits — language, date: https://sites.google.com/york.ac.uk/sureinfo/home/other-limits-language-date
- Peters, CLEF 2000 (ERCIM News 44): https://www.ercim.eu/publication/Ercim_News/enw44/peters.html
- Oard, Gey & Dorr 2002, TREC-2001 CLIR track (first large Arabic IR test collection): https://lccd.umiacs.umd.edu/publications/evaluating-arabic-retrieval-english-or-french-queries-trec-2001-cross-language
- Moral et al. 2014, A survey of stemming algorithms in IR: https://www.informationr.net/ir/19-1/paper605.html
- JISEBI 2024, Indonesian regional-language stemming SLR (2014–2023): https://e-journal.unair.ac.id/JISEBI/article/view/50341
- SLR of RAG (2020–May 2025), arXiv 2508.06401: https://arxiv.org/abs/2508.06401v3
