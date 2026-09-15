# Posokhov et al. (2026) — Query-Adaptive Hybrid Search

**Targeted deep-dive status:** COMPLETED  
**Completed:** 2026-09-15  
**Literature ID:** HYB-009  
**Project role:** critical boundary work for query-dependent hybrid retrieval and complementarity  
**Reliability:** A (peer-reviewed primary journal article; project evidence hierarchy)

## 1. Bibliographic record

Pavel Posokhov, Stepan Skrylnikov, Sergei Masliukhin, Alina Zavgorodniaia, Olesia Koroteeva, Yuri Matveev.  
**Query-Adaptive Hybrid Search.**  
*Machine Learning and Knowledge Extraction*, 2026, 8(4), Article 91.  
DOI: `10.3390/make8040091`  
Published: 5 April 2026.  
Open access.

## 2. Why this work matters to the PhD

This work is highly relevant because it directly addresses two ideas close to the current Uzbek hybrid-retrieval research direction:

1. **query-dependent fusion** — the lexical/dense balance is selected separately for each query;
2. **explicit complementarity-oriented dense training** — the dense retriever is trained to correct cases where BM25 performs poorly.

Therefore the PhD cannot claim novelty merely from:
- dynamic `alpha(q)`;
- predicting lexical-vs-dense weights from the query;
- adapting fusion to query characteristics;
- training one hybrid component to compensate for another;
- the general idea that hybrid quality depends on complementarity.

However, this work does **not** study the current v0.8 residual question: how changing the morphological representation of the lexical channel (`raw → stem → lemma`) changes lexical–dense complementarity under a fixed dense comparator.

## 3. Problem addressed by the paper

A conventional hybrid score can be written as:

`S_hybrid(q,d) = α S_dense(q,d) + (1-α) S_sparse(q,d)`.

A fixed global `α` assumes that every query needs the same balance between exact lexical matching and semantic matching.

The authors argue that this is unrealistic:
- some queries benefit more from BM25;
- others benefit more from dense retrieval;
- optimal balance varies across datasets, languages and individual queries.

A second problem is that dense and sparse retrievers are often trained independently. The dense component therefore does not explicitly learn to correct BM25 failure modes.

## 4. Main idea in plain language

The system asks two questions.

First:

> “For this query, how much should I trust BM25 and how much should I trust the dense retriever?”

A predictor called **QDAP (Query-Driven Alpha Prediction)** estimates the mixing weight `α` from the query representation.

Second:

> “Can the dense retriever be trained specifically on cases where BM25 is weak?”

The authors introduce **antagonist negative sampling** to focus dense training on BM25 failure cases and jointly confusing negative documents.

## 5. Simple example

Suppose two queries are issued.

**Query A:** `ISO 27001 access control requirements`

Exact terms such as `ISO 27001` are highly informative. BM25 may be very strong, so the useful `α` may be relatively low if `α` weights the dense component.

**Query B:** `why does the system deny a user even when the password is correct`

A relevant document may use different terminology such as `authorization policy`, `account state` or `access privileges`. Dense retrieval may be more useful, so `α` can be higher.

QDAP attempts to infer this balance automatically from the query.

## 6. Architecture

### Sparse component

Classical **BM25** is intentionally kept as the fixed lexical component.

The authors use language-specific preprocessing/tokenization and dataset-specific BM25 parameters.

### Dense component

The dense retriever is architecturally similar to multilingual GTE:
- Transformer encoder;
- rotary position embeddings (RoPE);
- normalized `[CLS]` representation;
- single-vector query/document representation;
- cosine similarity or dot product.

The paper reports approximately 305M parameters and 768-dimensional embeddings for the proposed dense model.

### Fusion

Sparse and dense scores are normalized and combined through weighted score fusion:

`S_hybrid = α S_dense + (1-α) S_sparse`.

The important novelty of the paper is not this equation itself, but predicting `α` for each query.

## 7. QDAP

The paper proposes two variants.

### QDAP-S

A lightweight predictor operating on a fixed query embedding.

Purpose:
- low latency;
- very small additional inference cost.

### QDAP-L

A full encoder-scale predictor initialized from the dense retriever.

Purpose:
- more accurate prediction of the useful `α`;
- higher GPU memory requirement.

Both output a distribution over **101 possible α values**:

`0.00, 0.01, ..., 1.00`.

A one-dimensional convolution with kernel size 7 smooths neighboring bins.

## 8. QDAP training target

For each training query, the system evaluates the hybrid result for all 101 values of `α`.

For each `α` it computes `nDCG@10`.

Thus a query obtains a full performance curve:

`α → nDCG@10`.

The predictor is trained to reconstruct this distribution rather than simply regress one scalar optimum.

This is important because a query can have several nearby or separated high-performing α regions.

## 9. QDAP loss

The loss combines:

- cross-entropy;
- one-dimensional Wasserstein distance.

Reported weighting:

`L = 0.62 * L_CE + 0.38 * L_WD`.

The intuition is:

- cross-entropy gives stable optimization;
- Wasserstein distance understands that predicting `α=0.79` when the target is `0.80` is much less wrong than predicting `α=0.10`.

## 10. Antagonist negative sampling

The dense retriever is not trained independently.

### Stage 1 — filter queries

Training pairs are retained when BM25 obtains low `nDCG@10`, i.e. where the lexical retriever struggles.

### Stage 2 — mine difficult negatives

Candidate negatives are drawn from dense and sparse retrieval results.

A negative is especially useful when both systems rank it above the true positive.

The dense encoder is then trained to distinguish the relevant document from these jointly confusing negatives.

The intended result is a dense model that fills BM25's weaknesses rather than simply maximizing standalone dense performance.

## 11. Datasets

### MLDR

Multilingual Long-Document Retrieval:
- 13 languages;
- long documents, often exceeding 8000 words;
- data from sources including Wikipedia, Wudao and mC4;
- lexical retrieval is comparatively strong.

### MIRACL

Multilingual ad-hoc passage retrieval:
- 18 languages in the benchmark;
- authors evaluate 16 languages because two hidden languages lack the required train/validation setup;
- segmented Wikipedia passages;
- very large candidate corpora;
- dense semantic retrieval is comparatively stronger.

The authors train jointly across MLDR and MIRACL rather than creating a separate model for every dataset/language.

**Uzbek is not included.**

For MIRACL, the official development split is used as the final test set because the official test labels are hidden; a custom validation subset is sampled from the training data.

## 12. Metric

Primary metric:

**nDCG@10**.

This evaluates whether relevant documents are ranked near the top and gives more value to relevant documents in earlier positions.

The paper does not use the unique-hit/overlap/oracle-union decomposition required by the current Uzbek v0.8 question.

## 13. Baselines

The comparison includes:
- BM25;
- internal lexical retriever (LTR);
- internal semantic retriever (STR);
- BGE-M3;
- mGTE-TRM;
- fixed/global-optimal hybrid weighting;
- per-query oracle weighting.

## 14. Main results

### MLDR

Reported average `nDCG@10`:
- internal BM25/LTR: **67.3**;
- semantic STR: **61.8**;
- BGE-M3 hybrid: **65.0**;
- mGTE-TRM hybrid: **71.3**;
- proposed HTR: **74.3**.

This is a regime where lexical matching is especially useful.

### MIRACL

Reported:
- lexical BM25/LTR: about **31.4**;
- proposed HTR: **67.1**.

BGE-M3 with dense+sparse+multi-vector remains slightly stronger on MIRACL, according to the paper's discussion, but is more computationally complex because of multi-vector/late-interaction behavior.

## 15. Oracle analysis

The paper defines two important references:

### HTR Optimal

One globally fixed `α` selected to maximize performance over the dataset.

### HTR Oracle

The best `α` is selected **individually for every query**, using relevance information.

The proposed adaptive system reaches **92.54%** of this theoretical per-query oracle and is reported to be roughly four percentage points closer to the oracle than the single globally optimal constant.

### Critical terminology distinction for our PhD

This **oracle is not the same as our planned oracle union**.

Their oracle asks:

> “If I knew the best fusion weight for this query, how well could weighted fusion perform?”

Our `oracle union` asks:

> “How many relevant documents are available in the union of the lexical and dense result sets, regardless of the fusion formula?”

These answer different scientific questions.

## 16. Ablation findings

The paper reports:

- QDAP-L outperforms QDAP-S by about **4.23% on average**;
- combined Wasserstein + cross-entropy loss is about **6.9% better than WD alone** and **2.8% better than CE alone**;
- antagonist-aware sampling gives approximately **3.72% improvement** over training without it.

These ablations support both adaptive weight prediction and complementarity-oriented dense training.

## 17. Statistical/reproducibility notes

The authors report:
- 10 independent runs with different random seeds;
- mean performance values;
- improvements described as consistent across languages and runs.

The accessible official text states statistically/significantly improved performance, but the recovered text used in this deep dive did not expose a clearly named inferential test with explicit per-query `p` values for the main comparisons.

Therefore, for final dissertation prose, strong statements about statistical significance should be checked again directly against the final PDF/table notes before citation.

## 18. Strengths

1. Real peer-reviewed 2026 work.
2. Multilingual evaluation.
3. Direct lexical+dense hybrid retrieval.
4. Explicit per-query fusion.
5. Fixed BM25 makes the lexical component easy to interpret.
6. Dense training is deliberately complementarity-oriented.
7. Has ablations for QDAP architecture, loss and negative sampling.
8. Separates global optimum from per-query oracle.
9. Includes long-document and short-passage regimes with different lexical/semantic behavior.

## 19. Limitations for our research question

1. **No Uzbek.**
2. **No controlled raw/stem/lemma intervention.**
3. BM25 morphology representation is not systematically varied.
4. The dense retriever is itself retrained against BM25 failures, so this is not a fixed-dense causal morphology experiment.
5. Main explanatory analysis focuses on `α` and dataset/query-dependent fusion, not relevant-set set decomposition.
6. No reported systematic lexical-only vs dense-only relevant-hit counts for morphology variants.
7. No morphology-induced intersection/overlap analysis.
8. No morphology-conditioned oracle union.
9. No direct relation between `raw → stem → lemma` and incremental hybrid gain.
10. Query embeddings are used for weight prediction, but the paper does not establish interpretable Uzbek linguistic query features explaining a morphology-induced complementarity shift.

## 20. What the paper really proves for our project

It provides strong evidence that:

- one fixed fusion weight is not universally optimal;
- per-query adaptive weighting is already an established modern idea;
- query representations can be used to predict useful lexical/dense balance;
- dense training can deliberately target BM25 failure modes;
- complementarity can be explicitly optimized rather than treated as an accidental property.

## 21. What it does NOT prove

It does not establish:

- how Uzbek morphology changes BM25 retrieval;
- how `BM25_raw`, `BM25_stem`, and `BM25_lemma` change their overlap with the same fixed dense retriever;
- unique relevant hits under these morphology variants;
- morphology-conditioned oracle-union headroom;
- morphology-conditioned incremental hybrid gain;
- which interpretable Uzbek query characteristics cause such a change.

## 22. Impact on current v0.8

### Does it kill v0.8?

**No.**

The paper strengthens the international boundary but does not close the morphology-induced complementarity question.

### What does it kill?

It prevents novelty claims such as:

- “we dynamically select BM25/dense weight for every query”;
- “query characteristics determine hybrid fusion”;
- “we predict alpha from the query”;
- “we train the dense retriever to complement BM25”;
- “complementarity is more important than standalone component quality”.

These ideas are already directly represented here.

### What survives?

The current controlled chain remains:

`morphological representation change`
→ `lexical relevant-set change`
→ `overlap/unique-hit change vs SAME fixed dense retriever`
→ `incremental hybrid-gain change`
→ `relation to Uzbek query characteristics`.

## 23. Experimental-design consequence

For the **main v0.8 baseline experiment**, do **not** immediately reproduce QDAP or antagonist negative sampling.

Why:

If the dense retriever is retrained separately against `BM25_raw`, `BM25_stem`, and `BM25_lemma`, then two variables change simultaneously:

1. lexical morphology;
2. dense model.

That destroys the clean causal interpretation.

The core experiment should therefore keep:

- the same dense retriever `D`;
- the same fusion protocol;
- the same evaluation set;

and vary only:

- `BM25_raw`;
- `BM25_stem`;
- `BM25_lemma`.

Only after the morphology-induced complementarity effect is established should QDAP-like adaptive fusion be considered as a possible later method.

## 24. Consequence for RQ3

RQ3 must not be formulated merely as:

> “Can query features be used to dynamically select lexical vs semantic weight?”

That is already substantially answered by Query-Adaptive Hybrid Search.

A defensible RQ3 should remain narrower:

> Which interpretable characteristics of Uzbek queries are associated specifically with the **change in lexical–semantic complementarity caused by changing the lexical morphological representation**?

That preserves the `morphology-induced` mechanism.

## 25. Final decision

**Role:** CRITICAL international boundary paper.  
**Gap-killer risk:** HIGH for dynamic/query-adaptive fusion novelty; LOW for the narrowly controlled v0.8 interaction/decomposition gap.  
**Current gap change:** no version change required.  
**Current design change:** reinforces the requirement to keep dense model and fusion fixed in the causal morphology experiment.  
**Future method implication:** QDAP/antagonist training may become a comparison or later extension, but must not be treated as novel by itself.
