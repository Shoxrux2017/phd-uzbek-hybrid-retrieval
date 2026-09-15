# Bakaev I.I. — Uzbek morphology, stemming and search applications

**Deep-dive status:** COMPLETED  
**Completed:** 2026-09-11  
**Suggested IDs:** PHD-UZ-001 / MORPH-UZ-001 / MORPH-UZ-002  
**Reliability:** A for the defended PhD; B/A- for related search paper  
**Priority for current PhD:** CRITICAL national boundary

## 1. Bibliographic record

### Main dissertation
- **Author:** Ilkhom Izatovich Bakaev
- **Title:** *O‘zbek tili so‘z shakllarini morfologik tahlil qilish modellari va algoritmlari*
- **Russian title:** «Модели и алгоритмы морфологического анализа словоформ узбекского языка»
- **English title:** *Models and Algorithms of Morphological Analysis of Word Forms of the Uzbek Language*
- **Degree:** PhD in technical sciences
- **Specialty:** 05.01.04 — Mathematical and software support of computers, complexes and computer networks
- **Institution:** Tashkent University of Information Technologies
- **Scientific adviser:** Ravshanov Normakhmad
- **Registration number:** B2021.3.PhD/T2374
- **Year:** 2021
- **Official author abstract:** 44 pages
- **Evidence:** official OAK registration/defense record + ZiyoNet author abstract
- **Current status confirmation:** later OAK records list Bakaev as `texnika fanlari falsafa doktori, dotsent`, confirming awarded PhD status
- **Reliability:** **A**

### Closely related search paper
Bakaev I.I., Shafiev T.R.  
*Organization of Full-Text Search on Web Resources* / «Организация полнотекстового поиска на веб-ресурсах».  
Problems of Computational and Applied Mathematics, 2020, No. 1(25), pp. 118–127.

This paper is important because it gives the clearest description of how Bakaev connected stemming/lemmatization to full-text search.

## 2. Why Bakaev is critical for our PhD

Bakaev is one of the strongest national gap-boundary sources because his work already combines:

- Uzbek tokenization;
- stemming / root-base extraction;
- morphemic analysis;
- grammatical tagging;
- web-service morphology;
- search-query processing;
- full-text/library search applications;
- deployment in Uzbek information-library institutions, including the National Library of Uzbekistan.

Therefore we cannot claim novelty from:

- applying morphology to Uzbek search;
- using stemming in Uzbek search;
- using lemmatization/morphological normalization in Uzbek full-text search;
- connecting a morphological analyzer to a library/search system.

However, Bakaev does **not** provide a modern qrels-based IR benchmark comparing `raw/stem/lemma`, BM25 and dense retrieval.

## 3. Research goal

The dissertation goal is to develop models, algorithms and web-oriented software for morphological analysis of Uzbek word forms.

Main tasks include:

- modeling Uzbek word formation/morphemes;
- identifying word bases and morphemes;
- forming a lexicon of stems and grammatical tags;
- token recognition with finite automata;
- designing a web-oriented morphological-analysis system.

This is primarily a **morphological/NLP software dissertation**, with search as a major application.

## 4. Morphoanalyzer architecture

The developed `Morphoanalyzer` includes four main functions:

1. tokenization;
2. normalization;
3. morphemic analysis;
4. grammatical-feature/POS identification.

The software exposes REST-style endpoints such as:

- token;
- token list;
- stem;
- POS tag;
- POS tag list.

Example:
`kitobxon` can be analyzed into a base plus the derivational suffix `-xon`.

The underlying method uses:
- finite-state automata/transducers;
- production rules;
- lexicons;
- morphological/morphotactic rules.

## 5. Stemming results

The dissertation author abstract reports stemming tests over several genres:

| Genre | Words | Correct bases |
|---|---:|---:|
| Fairy tales | 1,246 | **96%** |
| Legal documents | 1,290 | **92.4%** |
| Hadiths | 1,285 | **88.9%** |
| Uzbek proverbs | 1,200 | **94%** |

These values measure **stemming/base-identification accuracy**, not document-retrieval effectiveness.

### Later-result inconsistency

A 2022 Bakaev stemming paper reports:

- fairy tales: 96%;
- religious works: **91.3%**;
- Uzbek proverbs: 94%.

The later paper does not reproduce the dissertation's legal-document row and differs from the dissertation's 88.9% value for hadith/religious material.

Therefore the project should not merge these values without context. The safest interpretation is:

- different test subsets/versions may have been used;
- exact comparability is not established from the available sources.

## 6. Full-text search method

The 2020 full-text search paper proposes a search pipeline with:

1. indexing;
2. morphology-aware query/text normalization;
3. search context/field weighting;
4. ranking.

### Morphological processing

The paper explicitly discusses both:

- **stemmer**;
- **lemmatizer**.

The stated motivation is that simple stemming can over-strip or merge unrelated words.

Example:
a stemmer may reduce a word too aggressively and then accidentally match unrelated forms.

The authors therefore argue for deeper normalization/lemmatization using a morphological dictionary/analyzer.

### Ranking

The paper does **not** use BM25.

Its ranking description is comparatively simple:
- count terms/occurrences in documents/pages;
- assign coefficients to different content fields/types;
- use those coefficients when ordering results.

Therefore this work is not a BM25 benchmark.

## 7. What the search paper actually proves

The paper demonstrates:

- a morphology-aware full-text search architecture;
- use of stemmer and lemmatizer modules;
- practical examples where deeper morphological normalization appears more reliable than stem-only matching;
- indexing/search integration for Uzbek web resources.

But the paper does **not** report a standard controlled IR evaluation with:

- query set;
- qrels;
- MAP;
- nDCG;
- MRR;
- Recall@k;
- statistical significance;
- per-query analysis.

Its conclusion that deeper normalization gives “more reliable” results is based on examples/qualitative behavior, not a modern retrieval benchmark.

## 8. Deployment / National Library evidence

This is particularly important for our planned National Library system.

The dissertation states that the morphology models/algorithms/software were deployed in:

- Bukhara regional information-library center named after Abu Ali ibn Sino;
- Bukhara State University information-resource center;
- **National Library of Uzbekistan**.

### Quantified practical result

The dissertation reports **9–11% reduction in time/labor** for creating bibliographic descriptions in electronic catalog operations through automatic spelling correction and correct-word-form support.

Important:
this 9–11% figure is a **catalog/document-processing productivity metric**, not search relevance.

### Search relevance claim

For the National Library deployment, the dissertation states that the morphology module contributed to increased relevance/appropriateness of search results in:

- electronic catalog systems;
- full-text electronic library systems.

However, the author abstract does **not** provide a numerical retrieval metric for this increase.

Therefore we must not convert this statement into:
- “search improved by 9–11%”;
- or any MAP/nDCG/Recall claim.

That would be incorrect.

## 9. Search evidence summary

| Question | Bakaev |
|---|---|
| Uzbek morphological analyzer | ✅ |
| Uzbek tokenizer | ✅ |
| Uzbek stemmer | ✅ |
| Lexicon/grammatical tags | ✅ |
| Lemmatizer discussed/used in full-text search architecture | ✅ |
| Morphology-aware full-text search | ✅ |
| Library-system deployment | ✅ |
| National Library deployment | ✅ |
| Search-relevance improvement claimed | ✅ qualitative / deployment evidence |
| Quantified IR effectiveness | ❌ |
| BM25 | ❌ |
| Raw vs stem vs lemma controlled retrieval | ❌ |
| Dense retrieval | ❌ |
| Lexical+dense hybrid retrieval | ❌ |
| qrels | ❌ |
| MAP/nDCG/Recall@k | ❌ |
| Per-query overlap/unique hits | ❌ |

## 10. What Bakaev proves

Safe claims:

1. Uzbek morphology is a mature computational research line.
2. Uzbek stemming/base extraction has been implemented and evaluated at analyzer level.
3. Morphological processing has already been integrated with Uzbek full-text/library search.
4. Stemmer and lemmatizer-based search organization was already discussed nationally by 2020.
5. Morphological software was deployed in real library/catalog environments, including the National Library of Uzbekistan.
6. Search-query preprocessing based on morphology is therefore **not new** for our PhD.

## 11. What Bakaev does NOT prove

Bakaev does not establish:

- that lemmatization is better than stemming in a qrels-based Uzbek IR benchmark;
- that stemming is better than raw BM25;
- `lemma > stem > raw`;
- BM25 effectiveness for Uzbek;
- dense retrieval effectiveness;
- lexical–semantic hybrid retrieval;
- morphology-induced lexical/dense overlap change;
- incremental hybrid gain;
- query-characteristic explanations for hybrid gain.

## 12. Relation to CURRENT_GAP v0.8

**Status:** strongly supports the national boundary; does not close v0.8.

Bakaev removes the broad novelty claim:

> “Morphology has not been applied to Uzbek search.”

But the current residual question is much narrower:

`raw/stem/lemma`
→ `BM25 relevant-set change`
→ `overlap/unique hits with fixed dense retriever`
→ `incremental hybrid gain change`
→ `relation to Uzbek query characteristics`.

Bakaev does not perform this experiment.

Therefore `CURRENT_GAP v0.8` remains unchanged.

## 13. Implications for our research design

1. **Do not build a new stemmer/morphological analyzer as the main contribution.**
2. Use existing Uzbek morphology resources where feasible.
3. Keep raw/stem/lemma as controlled lexical representations.
4. Evaluate them with the same BM25.
5. Use qrels-based retrieval metrics.
6. Hold the dense retriever fixed when testing morphology.
7. Separate:
   - morphology-component accuracy;
   - catalog productivity;
   - search effectiveness.
8. Bakaev's National Library deployment is an important precedent for practical implementation, but our modern hybrid system still needs its own retrieval evaluation.

## 14. Why this is especially relevant to our National Library plan

Bakaev shows that:

- Uzbek morphology has already been deployed in the National Library context;
- library workflows can integrate external/web-service morphology;
- full-text/catalog search can benefit operationally from Uzbek language processing.

This is useful for our practical system design.

But our contribution should be a later generation of the search layer:

`BM25_raw/stem/lemma`
+ `fixed modern dense retriever`
+ controlled hybrid evaluation.

We should present our system as building on existing national morphology/search infrastructure, not as the first Uzbek morphology-aware library search system.

## 15. Methodological caution

The phrase “search relevance improved” in deployment documentation is weaker evidence than a controlled IR experiment.

Without:
- a fixed query set;
- relevance judgments;
- a baseline;
- IR metrics;

we cannot quantify how much retrieval quality improved.

This distinction is central for our literature review.

## 16. Open questions

1. Obtain the full defended dissertation if possible, not only the author abstract.
2. Verify whether any appendix contains explicit search-query benchmark results omitted from the abstract.
3. Determine whether the `Morphoanalyzer` software/API or lexicon remains accessible.
4. Determine whether National Library still uses any descendant of this morphology service.
5. If practical cooperation with the National Library begins, ask whether these historical modules/data are available for reuse.
6. Resolve the 88.9% vs 91.3% religious-text stemming result difference.

## 17. Decision

- **Keep CURRENT_GAP v0.8:** yes.
- **Upgrade Bakaev deep-dive status:** completed.
- **Role:** CRITICAL national morphology/search boundary.
- **Change decisions:** no new methodological decision.
- **Use in Chapter I:** yes, strongly.
- **Use as proof of modern IR effectiveness:** no.
