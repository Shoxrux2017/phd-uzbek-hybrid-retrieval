# Urinov E.M. — BM25 vs vector search in Uzbek RAG

**Deep-dive status:** COMPLETED AT VERIFIED-METADATA/ABSTRACT LEVEL  
**Completed:** 2026-09-14  
**Literature ID:** UZ-IR-003  
**Reliability:** C  
**Priority for current PhD:** MEDIUM national boundary

## 1. Bibliographic record

- **Author:** Elmurod Urinov / Urinov Elmurod
- **Title:** *O‘zbek tilidagi RAG tizimlarda vektor qidiruv va an’anaviy qidiruv algoritmlarini qiyosiy tahlili*
- **English sense of title:** “Comparative analysis of vector search and traditional search algorithms in Uzbek RAG systems”
- **Year:** 2025
- **Repository publication date:** 2025-10-13
- **Resource type in Zenodo:** Conference paper
- **Repository:** Zenodo
- **DOI:** 10.5281/zenodo.17341315
- **Available file:** `442-445.pdf`, 226.9 kB
- **Author affiliation in Zenodo record:** Oriental University
- **Author status:** independent official OAK material confirms Elmurod Murodjonovich Urinov holds a PhD in technical sciences
- **Reliability:** **C** for the paper as evidence, because the underlying peer-reviewed conference/venue was not independently verified in the current deep dive; the Zenodo record alone is not sufficient to upgrade it to B.

## 2. Why this work matters to our PhD

This work is directly relevant because it places two retrieval paradigms side by side for Uzbek RAG:

- **BM25-like traditional lexical retrieval**
- **semantic vector retrieval**

The verified abstract says their results were compared.

This means the national literature already contains at least a direct discussion/experimental comparison of lexical BM25-style search and vector semantic search for Uzbek.

Therefore we should not claim:

> “BM25 and vector search have never been compared for Uzbek.”

However, the verified evidence does **not** show:
- controlled raw/stem/lemma variants;
- a fixed dense comparator across morphology conditions;
- fusion of BM25 and vector scores/ranks;
- complementarity analysis.

## 3. Scientific problem

### Simple explanation

A RAG system must first find relevant text before an LLM can answer.

There are two obvious search strategies:

1. **BM25 / traditional lexical search**
   - strong when query words and document words match directly;
   - fast and computationally cheap.

2. **Vector / semantic search**
   - represents texts with embeddings;
   - can retrieve passages that are semantically close even if wording differs.

Urinov compares the strengths of these approaches for Uzbek RAG.

## 4. Main verified conclusion

The Zenodo abstract states that:

- traditional approaches such as BM25 are distinguished by speed and efficient use of computational resources;
- vector search provides deeper understanding of contextual meaning.

This is a qualitative comparative conclusion.

The accessible record does not expose enough information to determine:
- exact retrieval metrics;
- dataset size;
- query count;
- exact vector model;
- exact statistical significance.

## 5. BM25 side

The abstract explicitly names **BM25-like traditional search** as the lexical/traditional comparator.

What BM25 contributes conceptually:
- exact/lexical term evidence;
- efficient inverted-index retrieval;
- low computational cost.

The paper’s accessible description emphasizes speed and resource efficiency of the traditional approach.

## 6. Vector-search side

The semantic/vector branch is described as capable of better contextual-meaning understanding.

However, from the accessible evidence the following are **not verified**:

- embedding model name;
- whether vectors are sentence/document/passages;
- cosine/dot-product similarity;
- vector index technology;
- fine-tuning;
- Uzbek-specific training;
- whether the model is retrieval-trained.

Therefore this source cannot be treated as evidence for a particular modern dense retriever architecture.

## 7. Is this hybrid retrieval?

**Not established.**

The Zenodo keywords include `hybrid yondashuv`, but the title and abstract explicitly describe a **comparative analysis** of vector search and traditional search.

From the verified evidence we have:

`BM25`
**vs**
`vector search`

not a demonstrated:

`BM25 + vector search`.

Until the full paper is inspected, do not classify this work as:
- RRF fusion;
- score fusion;
- weighted hybrid;
- rank fusion;
- query routing.

## 8. Data / corpus

Not verifiable from the accessible Zenodo record:

- corpus source;
- number of documents/passages;
- domain;
- query count;
- relevance judgments;
- train/validation/test split;
- chunking;
- qrels.

These details must remain unknown.

## 9. Baselines

Verified:
- BM25-like traditional retrieval;
- semantic vector retrieval.

Not verified:
- TF-IDF;
- dense model name;
- hybrid fusion;
- reranker;
- RAG generator baseline.

## 10. Metrics

No standard retrieval metrics are visible in the accessible abstract.

Not verified:
- Precision@k;
- Recall@k;
- MAP;
- MRR;
- nDCG;
- Hit Rate;
- latency values;
- memory/CPU/GPU measurements.

Although the abstract concludes that traditional algorithms are faster/resource-efficient, exact benchmark values are not exposed in the accessible record.

## 11. Numerical results

No trustworthy numerical effectiveness table was recovered in this deep dive.

Therefore no numerical BM25-vs-vector result should be added to the dissertation from this source until the PDF/full publication is inspected.

## 12. Statistical evidence

No significance test, confidence interval, bootstrap or per-query statistical analysis is verifiable from the accessible metadata/abstract.

## 13. Strengths

1. Directly Uzbek.
2. Directly compares BM25-style lexical retrieval with semantic vector search.
3. Framed in a RAG setting, so retrieval is tied to a practical downstream system.
4. Supports the national evidence that lexical and semantic retrieval are both actively considered for Uzbek.

## 14. Limitations

1. Full text was not recovered in the current deep dive.
2. Underlying conference/peer-review venue is not independently verified.
3. Vector model is not identified in the accessible abstract.
4. Dataset/query/qrels protocol is not available.
5. No standard IR metrics are visible.
6. No morphology intervention.
7. No verified hybrid fusion.
8. No complementarity decomposition.

## 15. What this work actually proves

At the current evidence level, the safe conclusion is:

> A 2025 Uzbek RAG conference-paper record compares traditional BM25-like search with semantic vector search and reports the qualitative trade-off that traditional search is faster/resource-efficient while vector retrieval better captures contextual meaning.

It supports:

- BM25 vs vector-search comparison already exists in Uzbek-oriented work;
- lexical and semantic retrieval are both recognized as viable Uzbek RAG components.

## 16. What this work does NOT prove

It does not establish:

- BM25 is better/worse than vector retrieval by MAP/nDCG/Recall;
- a modern retrieval-trained dense model outperforms BM25;
- hybrid fusion improves over both;
- morphology improves BM25;
- `raw/stem/lemma` effects;
- lexical and vector systems retrieve complementary relevant documents;
- morphology changes that complementarity.

## 17. Relationship to Ishkobilov, USHRA and O-RAG

### Ishkobilov et al.
Stronger evidence for **pure IR evaluation**:
- explicit retrieval metrics;
- TF-IDF vs FastText;
- corpus-level paragraph ranking.

### Urinov
Direct **BM25 vs vector-search comparison**, but currently weakly documented from accessible evidence.

### USHRA
Stronger evidence that **Uzbek hybrid/RAG exists**.

### O-RAG
Stronger evidence for **ontology-enhanced hybrid retrieval and reranking**.

Therefore Urinov fills a narrow national slot:

> BM25 vs vector search is already discussed/compared for Uzbek RAG, but not with a sufficiently documented modern controlled IR protocol to close our interaction gap.

## 18. Relationship to CURRENT_GAP v0.8

**Status:** no change.

The current PhD does not ask merely:

> “BM25 or vector search — which is better?”

It asks:

`BM25_raw / BM25_stem / BM25_lemma`
with the same fixed `D`

→ how morphology changes:
- unique lexical relevant hits;
- unique dense relevant hits;
- overlap;
- oracle union;
- incremental hybrid gain.

Urinov does not establish this chain.

Therefore `CURRENT_GAP v0.8` remains open.

## 19. Implications for our research design

1. A simple BM25-vs-vector comparison is **not enough** for our scientific contribution.
2. Our experiment must use standard qrels-based retrieval metrics.
3. We should explicitly report latency/resource cost as a secondary engineering metric because Urinov highlights the lexical-vs-vector efficiency trade-off.
4. The semantic comparator should be a named, retrieval-trained modern multilingual model.
5. Hybrid conditions should be evaluated explicitly rather than inferred from side-by-side comparison.
6. The main novelty/evidence should remain morphology-induced complementarity analysis.

## 20. Open questions

To upgrade this source:

1. Obtain/read `442-445.pdf`.
2. Identify conference/proceedings venue.
3. Identify corpus and query set.
4. Identify exact vector model.
5. Identify BM25 implementation/parameters.
6. Verify whether stemming/lemmatization is used.
7. Recover effectiveness/latency/resource metrics.
8. Determine whether an actual hybrid `BM25 + vector` condition is evaluated.
9. Determine whether relevance judgments/qrels exist.
10. Check statistical significance.

## 21. Decision

- **Keep v0.8:** yes.
- **Change gap/history/decisions:** no.
- **Current reliability:** C.
- **Role:** supporting national evidence for BM25-vs-vector comparison, not a critical gap killer.
- **Use in Chapter I:** optional/supporting citation; do not use for strong numerical or methodological claims until full text is verified.
