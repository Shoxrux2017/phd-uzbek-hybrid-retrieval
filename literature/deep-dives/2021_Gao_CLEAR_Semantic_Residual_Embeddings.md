# Gao et al. (2021) — CLEAR: Complement Lexical Retrieval Model with Semantic Residual Embeddings

**Targeted deep-dive status:** COMPLETED  
**Completed:** 2026-09-15  
**Literature ID:** HYB-003  
**Project role:** CRITICAL international boundary paper for lexical–semantic complementarity  
**Reliability:** A — peer-reviewed ECIR 2021 full paper

## 1. Bibliographic record

Luyu Gao, Zhuyun Dai, Tongfei Chen, Zhen Fan, Benjamin Van Durme, Jamie Callan.  
**Complement Lexical Retrieval Model with Semantic Residual Embeddings.**  
In: *Advances in Information Retrieval — 43rd European Conference on IR Research (ECIR 2021), Proceedings, Part I*.  
LNCS 12656, pp. 146–160. Springer, 2021.  
DOI: `10.1007/978-3-030-72113-8_10`.

Earlier arXiv version: *Complementing Lexical Retrieval with Semantic Residual Embedding*, arXiv:2004.13969 (2020).

## 2. Why this work matters to the PhD

CLEAR is important because it makes lexical–semantic **complementarity itself** an explicit training objective.

The method does not merely:
- run BM25;
- run a dense retriever;
- fuse two independently trained result lists.

Instead, the dense component is trained specifically to **correct what BM25 fails to capture**.

This means the present PhD cannot claim novelty from the generic idea:
- "dense retrieval complements BM25";
- "train the dense component on lexical errors";
- "optimize complementarity rather than standalone dense quality";
- "hybrid retrieval should capture lexical and semantic signals jointly".

However, CLEAR does not study how changing the morphological representation of the lexical component changes that complementarity.

## 3. Scientific problem

The paper starts from two complementary limitations.

### Lexical retrieval

BM25 is efficient and preserves exact token-level evidence, but fails under vocabulary mismatch:

`query term != document term`, even when meaning is similar.

### Dense retrieval

A single dense vector enables semantic soft matching, but compresses the whole query/document into fixed-dimensional representation and may lose fine-grained lexical specificity.

Therefore:

`BM25 strength = exact lexical specificity`

`Dense strength = semantic matching beyond exact words`

The target is not to replace one with the other, but to make the dense model learn the **semantic information not already captured by BM25**.

## 4. Main idea in simple language

Suppose a query has one relevant document and one misleading document.

### Case A — BM25 already solves it

BM25 gives:

`relevant = 8.0`

`irrelevant = 2.0`

The lexical model already separates the pair well.

CLEAR tells the dense model:

> Do not spend much training effort relearning this easy exact-match distinction.

### Case B — BM25 fails

BM25 gives:

`relevant = 3.0`

`irrelevant = 4.0`

Now the lexical model ranks the wrong document higher.

CLEAR tells the dense model:

> This is exactly the kind of pair you must learn to correct semantically.

Thus the dense retriever is trained as a **residual complement** to BM25.

## 5. Architecture

CLEAR has two first-stage retrievers.

### 5.1 Lexical component

BM25:

`s_lex(q,d) = BM25(q,d)`.

It is indexed with a conventional inverted index.

### 5.2 Dense component

A Siamese BERT encoder is used for both query and document.

- initialized from `bert-base-uncased`;
- query and document encoders share parameters;
- special query/document markers are added;
- final representations are obtained by average pooling;
- matching score is dot product:

`s_emb(q,d) = v_q^T v_d`.

The dense index can use maximum inner-product search such as FAISS/ScaNN.

### 5.3 Final retrieval

The candidate sets from BM25 and dense retrieval are unioned.

Final score:

`s_CLEAR(q,d) = λ_test * s_lex(q,d) + s_emb(q,d)`.

`λ_test` controls the contribution of the lexical score during retrieval.

This fixed score interpolation is **not** the main novelty; the central idea is how the embedding model is trained.

## 6. Standard dense training baseline

A conventional triplet hinge loss uses:

- query `q`;
- relevant document `d+`;
- irrelevant document `d-`.

`L = [m - s_emb(q,d+) + s_emb(q,d-)]_+`

with a fixed margin `m`.

The problem is that this trains the embedding model independently of what BM25 already knows.

## 7. Error-based negative sampling

CLEAR samples negative documents from documents that BM25 retrieves highly but that are actually non-relevant.

Experimental setup:

- one negative document per training step;
- sampled from the top 1,000 BM25 results.

Why this matters:

A random negative can be trivially unrelated.

A BM25 false positive is more useful:

> it looks lexically convincing but is not actually relevant.

The dense retriever must learn the semantic distinction precisely where the lexical retriever is confused.

## 8. Residual-based margin

The second key mechanism changes the hinge-loss margin according to the lexical model's error.

The residual margin is:

`m_r = ξ - λ_train [s_lex(q,d+) - s_lex(q,d-)]`.

Then:

`L = [m_r - s_emb(q,d+) + s_emb(q,d-)]_+`.

### Interpretation

If BM25 strongly prefers the relevant document:

`s_lex(q,d+) - s_lex(q,d-)` is large and positive.

Therefore the residual margin becomes smaller.

The dense model receives little or no pressure to relearn the distinction.

If BM25 is weak or wrong:

`s_lex(q,d+) - s_lex(q,d-)` is small or negative.

The residual margin becomes larger.

The dense model receives a stronger training signal.

This is the paper's central meaning of **semantic residual**:

> learn semantic evidence that remains uncaptured after the lexical model has contributed its signal.

## 9. Important distinction for the PhD

CLEAR's "residual" is not the same as the present PhD's planned set-based decomposition.

CLEAR uses a **score residual inside the training loss**.

The current v0.8 study plans to analyze:

- lexical-only relevant hits;
- dense-only relevant hits;
- intersection;
- oracle union;
- incremental hybrid gain.

Those are **retrieved-set/relevance decomposition quantities**, not CLEAR's residual-margin definition.

## 10. Dataset

The main collection is **MS MARCO passage ranking**:

- approximately 8.8 million passages;
- approximately 0.5 million training query–relevant-passage pairs;
- typically around one relevant passage per training query.

Two evaluation sets are used.

### MS MARCO Dev

- 6,980 queries;
- mostly one binary relevant passage per query;
- metrics:
  - MRR@10;
  - Recall@1000.

### TREC 2019 Deep Learning Track

- 43 queries;
- manually judged by NIST;
- 4-level graded relevance;
- approximately 94 relevant documents per query on average;
- metrics:
  - nDCG@10;
  - MAP@1000;
  - Recall@1000.

This second set is especially useful because it contains multiple graded relevant documents per query, unlike the sparse MS MARCO dev judgments.

## 11. Baselines

First-stage retrieval:

- BM25;
- BM25 + RM3;
- DeepCT;
- DeepCT + RM3;
- BERT-Siamese dense retriever;
- CLEAR.

Pipeline evaluation:

- BM25 + BERT-base reranker;
- BM25 + BERT-large reranker;
- CLEAR + BERT-base reranker;
- CLEAR + BERT-large reranker.

## 12. Training/setup

Reported setup includes:

- `bert-base-uncased`;
- 8 training epochs;
- one RTX 2080 Ti;
- Adam;
- learning rate `2×10^-5`;
- batch size 28;
- `ξ = 1`;
- `λ_train = 0.1`;
- `λ_test` searched on 500 training queries;
- `λ_test = 0.5` selected as robust.

BM25/DeepCT use Anserini.

RM3 hyperparameters are tuned with 2-fold cross-validation.

Statistical significance is tested with a **permutation test, p < 0.05**.

## 13. Main first-stage results

| Model | MS MARCO Dev MRR@10 | R@1000 | TREC DL nDCG@10 | MAP@1000 | R@1000 |
|---|---:|---:|---:|---:|---:|
| BM25 | 0.191 | 0.864 | 0.506 | 0.377 | 0.739 |
| BM25+RM3 | 0.166 | 0.861 | 0.555 | 0.452 | 0.789 |
| DeepCT | 0.243 | 0.913 | 0.551 | 0.422 | 0.756 |
| DeepCT+RM3 | 0.232 | 0.914 | 0.601 | 0.481 | 0.794 |
| BERT-Siamese | 0.308 | 0.928 | 0.594 | 0.307 | 0.584 |
| **CLEAR** | **0.338** | **0.969** | **0.699** | **0.511** | **0.812** |

The table marks CLEAR as statistically significantly better than the indexed competing systems for the reported main comparisons.

## 14. What the result means

### CLEAR vs BM25

CLEAR adds semantic matching while preserving exact lexical evidence and substantially improves both early precision/ranking and first-stage recall.

### CLEAR vs BERT-Siamese

The dense-only system is strong on MS MARCO Dev, but is much weaker on TREC DL MAP/Recall.

This is important:

> a strong semantic single-vector retriever is not automatically a replacement for exact lexical evidence.

CLEAR performs better by grounding semantic matching in the lexical component.

## 15. Ablation study

Two crucial ablations are tested.

| Variant | Dev MRR@10 | R@1000 | TREC nDCG@10 | MAP@1000 | R@1000 |
|---|---:|---:|---:|---:|---:|
| CLEAR | **0.338** | **0.969** | **0.699** | **0.511** | **0.812** |
| Random negative sampling | 0.241 | 0.926 | 0.553 | 0.409 | 0.779 |
| Constant margin | 0.314 | 0.955 | 0.664 | 0.455 | 0.794 |

The constant-margin variant corresponds to a post-training combination of BM25 and an independently trained BERT-Siamese retriever.

Both ablations are worse than full CLEAR.

### Interpretation

The gain is not explained only by:

`BM25 score + dense score`.

Training the dense retriever specifically around lexical errors contributes additional effectiveness.

## 16. Reranking results

| First-stage retriever | Reranker | Dev MRR@10 | TREC nDCG@10 | Optimal reranking depth |
|---|---|---:|---:|---:|
| BM25 | BERT-base | 0.345 | 0.707 | 1000 |
| CLEAR | BERT-base | **0.360** | **0.719** | **20** |
| BM25 | BERT-large | 0.370 | 0.737 | 1000 |
| CLEAR | BERT-large | **0.380** | **0.752** | **100** |

CLEAR therefore provides a stronger first-stage candidate list and lets the expensive reranker work on a much smaller set.

Reported reranking-depth reduction:

- `1000 → 20` for BERT-base;
- `1000 → 100` for BERT-large.

This corresponds to roughly 50× and 10× reductions in the reranking depth respectively.

## 17. Qualitative examples

The paper shows cases where BM25 fails because the query and relevant passage do not use exactly the same critical term.

Examples include:

- `weather` matched through concepts such as sunny/rain/wind;
- `government` related to legal concepts such as attorney/law clerk;
- spelling variation `jabodatek` vs `Jabodetabek`.

Reported example rank changes include:

- `989 → 10`;
- `996 → 7`;
- `not retrieved → 1`.

This demonstrates real vocabulary-mismatch recovery.

## 18. New failure mode introduced by semantic retrieval

CLEAR also retrieves new false positives that BM25 would not retrieve.

These can be:
- topically related;
- semantically similar;
- spelling-similar;

but still non-relevant.

The paper notes that a BERT reranker may even amplify some of these semantic false positives.

Therefore:

> complementarity produces new useful evidence, but semantic expansion also changes the error distribution.

This is conceptually relevant to the current PhD: it reinforces the need to analyze not only aggregate gain but also **which documents become unique hits and unique errors**.

## 19. Strengths

1. Peer-reviewed ECIR primary paper.
2. Large real passage-retrieval collection.
3. Explicit BM25+dense first-stage retrieval.
4. Complementarity is built into training, not only post-hoc fusion.
5. Strong baselines.
6. Clear ablation of error-based negatives and residual margin.
7. Statistical significance with permutation testing.
8. Evaluation on two query sets with very different relevance-label structure.
9. Downstream reranking effectiveness and efficiency are also evaluated.
10. Qualitative winning and losing cases are examined.

## 20. Limitations relative to the current PhD

1. English only.
2. MS MARCO passage retrieval only as the underlying collection.
3. No Uzbek.
4. No agglutinative-language morphology intervention.
5. Only one lexical representation of BM25 is used.
6. No `raw/stem/lemma` controlled comparison.
7. Dense component is trained **dependent on BM25 errors**, not held fixed.
8. No systematic per-query lexical-only/dense-only relevant-hit table.
9. No morphology-conditioned intersection/overlap analysis.
10. No morphology-conditioned oracle union.
11. No analysis of Uzbek script/apostrophe variation or morphology-related query features.
12. Dense model is an early BERT-Siamese design rather than a modern multilingual retrieval-trained baseline.

## 21. What the paper really proves

CLEAR establishes that:

- lexical and dense retrieval have complementary failure modes;
- independently trained BM25 and dense retrieval are not necessarily the best way to exploit complementarity;
- a dense model can be trained explicitly to focus on lexical retrieval errors;
- residual-aware training can outperform simple post-training fusion;
- hybrid first-stage retrieval can improve both ranking effectiveness and downstream reranking efficiency.

## 22. What the paper does NOT prove

It does not establish:

- how Uzbek morphology changes lexical retrieval;
- whether `BM25_raw`, `BM25_stem`, or `BM25_lemma` is best;
- how those morphology variants change overlap with one **fixed** dense retriever;
- how morphology changes lexical-only and dense-only relevant sets;
- how morphology changes oracle-union headroom;
- how morphology changes incremental hybrid gain;
- which interpretable Uzbek query characteristics explain such changes.

## 23. Impact on v0.8

### Does CLEAR kill v0.8?

**No.**

It kills a broader claim:

> "lexical–semantic complementarity has not been studied."

That claim is already invalid and is correctly excluded by the current project state.

But CLEAR keeps the lexical side fixed and changes the dense model through complementarity-aware training.

The current v0.8 asks a different causal question:

`change lexical morphology`
→ `change lexical relevant set`
→ `change overlap/unique hits versus SAME fixed dense model`
→ `change incremental hybrid gain`.

CLEAR does not perform this intervention.

## 24. Important design consequence

CLEAR is also a warning for our experimental design.

If we trained:

- `Dense_raw` specifically against `BM25_raw`;
- `Dense_stem` specifically against `BM25_stem`;
- `Dense_lemma` specifically against `BM25_lemma`;

then both the lexical representation and the dense model would change.

We would no longer know whether a complementarity difference was caused by morphology or by the retrained dense model.

Therefore the main v0.8 experiment should keep:

`D = constant`

and compare:

`BM25_raw + D`

`BM25_stem + D`

`BM25_lemma + D`.

Only after the causal morphology effect is established may CLEAR-like residual training be considered as a later method or comparison.

## 25. Relationship to Query-Adaptive Hybrid Search

The two works occupy different levels.

### CLEAR

Learns **what semantic evidence the dense model should capture** relative to BM25.

### Query-Adaptive Hybrid Search

Learns **how strongly lexical and dense components should be weighted for each query**.

Together they show that both:

- complementarity-aware component training;
- query-dependent fusion;

are already established directions.

Therefore neither can be used alone as the present PhD's novelty.

## 26. Consequence for the provisional RQs

### RQ1

Unaffected. CLEAR does not study raw/stem/lemma effects on BM25.

### RQ2

Strengthened but narrowed.

Generic BM25–dense complementarity is established by CLEAR; the research question must remain explicitly about **morphology-induced change** in complementarity.

### RQ3

CLEAR does not analyze interpretable morphology-conditioned query features, so the current narrow RQ3 remains open.

## 27. Final decision

**Role:** CRITICAL international complementarity boundary paper.  
**Gap-killer risk:** VERY HIGH for generic complementarity or complementarity-aware training novelty.  
**Gap-killer risk for v0.8:** LOW/MEDIUM; it narrows the interpretation but does not close the controlled morphology interaction.  
**Current gap version:** no change required.  
**Experimental implication:** strongly reinforces the fixed-dense-comparator requirement.  
**Future-method implication:** CLEAR-like residual training may be a later comparison or extension only after the baseline interaction is empirically established.
