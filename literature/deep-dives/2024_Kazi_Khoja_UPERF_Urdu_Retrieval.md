# UPERF: Urdu Proximity Enhanced Retrieval Framework

**Targeted deep-dive status:** COMPLETED
**Completed:** 2026-09-10
**Literature ID:** MORPH-003

## 1. Bibliographic record

- **Authors:** Samreen Kazi; Shakeel Khoja
- **Year:** 2024
- **Venue:** Proceedings of the 38th Pacific Asia Conference on Language, Information and Computation (PACLIC 2024)
- **Pages:** 1009–1017
- **Publisher:** Tokyo University of Foreign Studies
- **ACL Anthology ID:** `2024.paclic-1.96`
- **Official record:** https://aclanthology.org/2024.paclic-1.96/
- **Full text:** https://aclanthology.org/2024.paclic-1.96.pdf
- **Source type:** peer-reviewed conference paper
- **Reliability:** B

## 2. Why this work matters to the PhD

UPERF is a major boundary paper for the current Uzbek research gap because it combines several elements that cannot be claimed as independently novel:

- real corpus-level document retrieval in a low-resource, morphologically complex language;
- BM25 and TF-IDF;
- embedding-based retrieval signals;
- three text preprocessing variants: raw, stemmed, lemmatized;
- query-type analysis (single-word vs multiple-word);
- weighted lexical–semantic combination.

It therefore invalidates any broad novelty claim based merely on jointly studying morphology, lexical retrieval and semantic representations in a low-resource language.

## 3. Research problem

### Simple explanation

Urdu words vary morphologically and exact term matching can miss semantically related documents. The authors ask whether retrieval improves when traditional lexical methods are combined with embedding-based proximity and whether preprocessing affects retrieval effectiveness.

### Formal experimental factors

The paper varies:

`retrieval representation/model × preprocessing × query type × similarity measure`.

The explicit preprocessing variants are:

- raw text;
- stemmed text;
- lemmatized text.

Query types are:

- single-word;
- multiple-word.

## 4. Dataset and relevance evidence

The experiments use the **Urdu News Document (UND) corpus**:

- **2,887,169** news articles;
- collected from **11 newspapers**;
- TREC-standard SGML representation;
- **105 queries** derived from **35 base queries with three variants each**;
- relevance levels: highly relevant, fairly relevant, marginally relevant, irrelevant.

The paper states that the corpus had been processed for relevance judgments using retrieval methods including BM25, TF-IDF and Boolean similarity. This deep dive does not independently re-audit the original UND qrels construction; claims about the exact assessor protocol should therefore be taken from the original UND publication if needed in final dissertation text.

## 5. Models and configurations

The study evaluates:

- **BM25**;
- **TF-IDF** (bigram/trigram variants);
- **Word2Vec**;
- **FastText**;
- **Doc2Vec**;
- **mBERT**.

Embedding models are evaluated with several proximity functions, including cosine, Euclidean, Manhattan and Jaccard-style measures.

Important methodological distinction for the current PhD:

- Word2Vec/FastText/Doc2Vec and mBERT representations are not equivalent to a modern retrieval-trained multilingual dense retriever such as multilingual E5, BGE-M3, Contriever or a ColBERT-style model.

## 6. Evaluation metric

The paper uses **Recall@5** as the main evaluation metric.

Recall@5 asks what fraction of all relevant documents are present among the first five returned results.

For the current PhD this is too narrow as a complete evaluation protocol. A stronger Uzbek retrieval evaluation should use several complementary ranking/coverage metrics, for example nDCG@k, Recall@k and MAP/MRR as appropriate to the final qrels design.

## 7. Morphology results

The key table explicitly compares raw, stemmed and lemmatized variants.

For multiple-word queries with cosine similarity, the reported values include:

| Model | Raw | Stemmed | Lemmatized |
|---|---:|---:|---:|
| Word2Vec | 0.82 | **0.85** | 0.83 |
| mBERT | 0.78 | **0.79** | 0.78 |
| TF-IDF trigram | 0.75 | **0.76** | 0.75 |
| FastText | 0.73 | **0.74** | 0.73 |
| Doc2Vec | 0.22 | **0.23** | 0.22 |
| BM25 | 0.35 | **0.36** | 0.35 |

The authors summarize that stemmed text performs better than raw and lemmatized text across the tested models, while multiple-word queries outperform single-word queries.

### Safe interpretation

The result establishes that preprocessing choice can affect both traditional and embedding-based retrieval in this Urdu setting.

It does **not** establish that:

- stemming is universally superior to lemmatization;
- the same ordering transfers to Uzbek;
- morphology produces a large effect for BM25;
- the effect is statistically significant unless the exact statistical test is verified.

## 8. Query-type result

The paper reports a strong difference between multiple-word and single-word queries. For example, mBERT with stemmed text is reported around 0.79 for multiple-word queries but around 0.34 for single-word queries.

This means query length/type is already an established experimental factor in morphology-aware low-resource retrieval. The current PhD cannot claim novelty merely from splitting queries by length.

## 9. Hybrid / weighted combination

The paper defines a score-level combination:

`Final Score = α·TF-IDF + β·BM25 + γ·ProximityScore`.

Scores are normalized before combination and weights are explored by grid search.

Reported Recall@5 examples include:

| Configuration | Recall@5 |
|---|---:|
| TF-IDF only | 0.45 |
| BM25 only | 0.48 |
| Word2Vec proximity only | **0.85** |
| Heavy proximity `(0.1, 0.1, 0.8)` | 0.82 |
| Moderate proximity `(0.2, 0.2, 0.6)` | 0.80 |
| Equal weights | 0.72 |

A critical result for the current PhD is that the best reported weighted hybrid in this table does **not** exceed the best standalone proximity result.

Therefore:

> hybrid integration does not automatically guarantee improvement over the strongest individual component.

## 10. Complementarity analysis

The paper qualitatively analyzes rankings for two example queries and shows that lexical and embedding-based approaches rank relevant documents differently.

However, it does not provide the decomposition needed for the current residual gap:

- unique relevant hits of each component over all queries;
- intersection of relevant hits;
- oracle union;
- change of overlap after morphology normalization;
- per-query incremental hybrid gain for raw/stem/lemma variants.

The paper therefore demonstrates different ranking behavior and weighted integration, but not a systematic morphology-conditioned complementarity analysis.

## 11. Statistical significance

The prose uses wording such as “significantly outperforming”, but the full text inspected in this deep dive did not reveal a clearly specified paired significance test, p-value, confidence interval or randomization procedure for the main retrieval comparisons.

Safe dissertation wording should therefore prefer **numerical superiority** unless an exact inferential test is later verified.

## 12. What the paper really establishes

UPERF establishes in its Urdu setting that:

1. raw/stemmed/lemmatized preprocessing can be evaluated as explicit retrieval factors;
2. preprocessing can affect both lexical and embedding-based methods;
3. query type can materially affect retrieval effectiveness;
4. lexical and semantic/proximity methods may produce different rankings;
5. simple fixed weighted fusion is not guaranteed to beat the strongest individual component.

## 13. What the paper does not establish

It does not establish:

1. the optimal preprocessing strategy for Uzbek;
2. controlled morphology effects with a modern retrieval-trained dense retriever;
3. morphology-conditioned lexical–dense overlap/unique-hit structure;
4. whether morphology increases or decreases the incremental value of a fixed dense retriever;
5. a systematic explanation of per-query lexical/dense/hybrid wins using interpretable linguistic query features;
6. a modern learned-sparse comparison.

## 14. Consequence for the current Uzbek research gap

UPERF kills the broad claim:

> “raw/stem/lemma has not been compared together with lexical and semantic representations in a low-resource morphologically complex language.”

The residual question must be narrower:

> how changing the lexical morphological representation changes **the structure of complementarity** with a fixed modern semantic retriever, especially for Uzbek and its own morphological/script characteristics.

## 15. Experimental design consequence

UPERF supports retaining a controlled Uzbek matrix such as:

`BM25_raw ↔ BM25_stem ↔ BM25_lemma`

followed by the same fixed dense retriever `D`:

`BM25_raw + D`
`BM25_stem + D`
`BM25_lemma + D`.

But the contribution must not be presented as the mere existence of these components. The important analysis should measure:

- per-query gains/losses;
- relevant-set overlap;
- unique relevant hits;
- oracle union;
- incremental hybrid gain;
- relation of these changes to Uzbek query features.

## 16. Final status

**Role in project:** CRITICAL gap-boundary evidence.
**Gap-killer risk:** HIGH for broad morphology+hybrid claims; LOW–MEDIUM for the refined morphology→complementarity question.
**Deep-dive conclusion:** keep as a primary comparative reference for experimental design, but do not copy its single-metric evaluation or treat its embedding methods as equivalent to modern retrieval-trained dense models.
