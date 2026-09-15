# Bruch, Gai & Ingber — An Analysis of Fusion Functions for Hybrid Retrieval

**Targeted deep-dive status:** COMPLETED  
**Completed:** 2026-09-15  
**Literature ID:** HYB-005  
**Project role:** CRITICAL experimental-design source for fixed hybrid fusion  
**Reliability:** A — peer-reviewed ACM Transactions on Information Systems article

## 1. Bibliographic record

Sebastian Bruch, Siyu Gai, Amir Ingber.  
**An Analysis of Fusion Functions for Hybrid Retrieval.**  
*ACM Transactions on Information Systems*, Vol. 42, No. 1, Article 20, 35 pages.  
DOI: `10.1145/3596512`.

**Bibliographic year caution:** the official ACM reference gives **2023** and publication date **August 2023**. Some indexes (including DBLP and the current project `MASTER_INDEX`) associate Volume 42(1) with **2024**. For the final bibliography, prefer the official ACM publication record and explicitly reconcile this metadata rather than silently switching years.

Earlier arXiv record: `2210.11934`, first posted 2022, revised 2023.

## 2. Why this paper matters to the PhD

The current Uzbek PhD requires a fixed fusion protocol for:

- `BM25_raw + D`;
- `BM25_stem + D`;
- `BM25_lemma + D`.

If the fusion method itself changes unpredictably, a difference in hybrid effectiveness can no longer be cleanly attributed to morphology.

This paper is therefore not mainly a gap-killer for the morphology question. It is a **methodological control paper** answering:

> How should lexical and semantic scores be fused so that the fusion itself does not become an unnecessary source of instability?

Its most important conclusion for the current project is that a properly normalized **convex combination of scores** is a strong, interpretable and sample-efficient primary fusion baseline, while Reciprocal Rank Fusion (RRF) is not genuinely parameter-free and discards score-distance information.

## 3. Scientific problem

A lexical retriever and a semantic dense retriever generate scores on different scales.

For example:

- BM25 may produce scores such as `2.1`, `8.7`, `14.3`;
- cosine similarity may produce values such as `0.31`, `0.72`, `0.84`.

A naive sum is meaningless because the scales are not comparable.

Two common solutions are:

1. normalize the scores and combine them;
2. ignore scores and combine only ranks using RRF.

The paper asks which approach is theoretically and empirically better behaved.

## 4. Convex combination

Let:

- `s_lex(q,d)` be the lexical score;
- `s_sem(q,d)` be the semantic score.

After normalization, fusion is:

`S_CC(q,d) = α S_sem(q,d) + (1-α) S_lex(q,d)`

with:

`0 ≤ α ≤ 1`.

Interpretation:

- `α = 0` → purely lexical;
- `α = 1` → purely semantic;
- values between them → hybrid.

The parameter is directly interpretable as the relative semantic weight after normalization.

## 5. Why normalization is necessary

A fixed `α` has no stable meaning when the two scoring functions have incompatible or query-dependent scales.

The paper studies several transformations, including:

- ordinary min-max normalization;
- theoretical min-max normalization;
- z-score normalization;
- partially normalized variants;
- unnormalized fusion.

The key result is subtle:

> normalization is important, but among reasonable linear normalization schemes the exact choice is often much less important than commonly assumed.

The authors show that convex combinations under different positive linear transformations can often be mapped to rank-equivalent solutions by changing `α`.

Therefore the scientific concern should be:

- make the score spaces bounded/comparable;
- use a consistent normalization protocol;

rather than treating min-max vs z-score as a major research novelty.

## 6. Theoretical minimum-maximum normalization

The paper's preferred practical form replaces the empirical minimum of the retrieved candidate set with the **theoretical lower bound** of the scoring function.

For retrieval system `o`:

`phi_tmm(s_o(q,d)) = (s_o(q,d) - inf s_o(q,*)) / (M_q - inf s_o(q,*))`

where:

- `M_q` is the maximum observed score for query `q`;
- `inf s_o` is the theoretical minimum possible score.

Examples used by the paper:

- BM25 lower bound: `0`;
- cosine similarity lower bound: `-1`.

The resulting convex-combination method is referred to as **TM2C2** in the paper.

### Why this matters

Ordinary candidate-set min-max scaling depends on whichever minimum happens to occur in the retrieved pool.

The theoretical minimum is less dependent on the particular candidate sample, which the authors argue gives more stable behavior across domains.

## 7. Reciprocal Rank Fusion (RRF)

For two systems, conventional RRF is:

`S_RRF(q,d) = 1/(η + rank_lex(q,d)) + 1/(η + rank_sem(q,d))`.

A common choice is:

`η = 60`.

RRF has an obvious operational advantage:

> it does not require lexical and semantic scores to be on comparable scales.

But the paper challenges two common beliefs:

1. RRF is not truly “parameter-free”;
2. throwing away the original score distances can lose useful information.

## 8. Why RRF is actually parametric

The authors generalize RRF to:

`S_RRF = 1/(η_lex + rank_lex) + 1/(η_sem + rank_sem)`.

Now each retrieval function effectively has a parameter controlling how strongly its ranks contribute.

For two retrievers:

- convex combination needs one effective mixing parameter;
- this generalized RRF has two rank-offset parameters.

If:

`η_lex > η_sem`

the lexical contribution is more strongly discounted because its denominator is larger.

Therefore treating `η=60` as a universal non-parametric constant hides a real weighting choice.

## 9. Why rank-only fusion loses information

Suppose two documents have semantic scores:

- A = `0.91`;
- B = `0.90`.

Another pair has:

- C = `0.91`;
- D = `0.20`.

Both pairs may be adjacent in rank.

RRF sees only:

`rank 1` vs `rank 2`.

It does not know that the first pair is almost tied while the second pair is very far apart.

A score-based convex combination preserves that distance information.

The paper formalizes this discussion through **Lipschitz continuity**.

Plain-language interpretation:

> a well-behaved fusion function should change smoothly when the input scores change slightly.

RRF changes discretely whenever document ranks swap and therefore does not preserve raw score geometry as smoothly as score-based fusion.

## 10. Smooth RRF experiment

To test whether this lost score-distribution information matters, the authors construct a smoothed approximation of RRF (SRRF).

The hard rank indicator is replaced by a sigmoid approximation controlled by parameter `β`.

As `β → ∞`, the soft approximation approaches ordinary ranks/RRF.

The experiments show that suitable smoothing can improve RRF in several cases, supporting the claim that completely discarding score-distribution information can be harmful.

However, TM2C2 remains the stronger general baseline across the reported datasets; SRRF can outperform it on particular cases (e.g., one HotpotQA setting), so the result should not be overstated as “TM2C2 wins every individual configuration”.

## 11. Experimental retrieval systems

### Lexical channel

- PISA;
- BM25;
- `k1 = 0.9`;
- `b = 0.4`;
- whitespace tokenization;
- PISA stemming;
- no stopword removal, lemmatization or expansion;
- top-1000 retrieval.

Important for the Uzbek project:

the paper uses **one fixed stemmed lexical pipeline**. It is not a morphology ablation and says nothing about `raw/stem/lemma`.

### Semantic channel

- `sentence-transformers/all-MiniLM-L6-v2`;
- 384-dimensional vectors;
- cosine/inner-product-style vector retrieval;
- exact FAISS `IndexFlatIP`;
- top-1000 retrieval.

This model is suitable for their fusion analysis but is **not** a candidate primary semantic comparator for Uzbek in 2026 because the paper provides no Uzbek validation and modern multilingual retrieval-trained alternatives are stronger candidates.

## 12. Candidate-union protocol

For every query, the authors form the union:

`U^k(q) = R_lex^k(q) ∪ R_sem^k(q)`.

For a document found by only one channel, the missing score from the other channel is computed before fusion.

This is very important for the current PhD.

The fusion stage can reorder only documents available in this candidate union.

Therefore two distinct quantities must not be confused:

1. **candidate-set complementarity/headroom** — which relevant documents are present in the lexical/dense union;
2. **fusion effectiveness** — how well a fusion function orders that already available union.

This supports the project's plan to measure unique relevant hits and oracle union separately from hybrid ranking gain.

## 13. Datasets

The paper evaluates 9 retrieval datasets.

| Dataset | Documents | Queries | Regime |
|---|---:|---:|---|
| MS MARCO Passage v1 | 8.8M | 6,980 | in-domain |
| Natural Questions | 2.68M | 3,452 | in-domain |
| Quora | 523K | 10,000 | in-domain |
| NFCorpus | 3.6K | 323 | zero-shot/out-of-domain |
| HotpotQA | 5.23M | 7,405 | zero-shot/out-of-domain |
| FEVER | 5.42M | 6,666 | zero-shot/out-of-domain |
| SciFact | 5K | 300 | zero-shot/out-of-domain |
| DBPedia | 4.63M | 400 | zero-shot/out-of-domain |
| FiQA | 57K | 648 | zero-shot/out-of-domain |

MS MARCO, NQ and Quora are treated as in-domain because the MiniLM checkpoint was trained on data including these datasets.

## 14. Metrics

Primary reported metrics:

- Recall@1000;
- nDCG@1000.

For the small NFCorpus and SciFact collections:

- Recall@100;
- nDCG@100.

The deep cutoff is deliberate: the authors study first-stage retrieval behavior and candidate quality, not only top-10 ranking.

## 15. Main NDCG results

The paper fixes:

- `α = 0.8` for TM2C2;
- `η = 60` for baseline RRF.

Representative results:

| Dataset | Lexical | Semantic | TM2C2 | RRF | Per-query-alpha oracle |
|---|---:|---:|---:|---:|---:|
| MS MARCO | 0.309 | 0.441 | **0.454** | 0.425 | 0.547 |
| NQ | 0.382 | 0.505 | **0.542** | 0.514 | 0.637 |
| Quora | 0.800 | 0.889 | **0.901** | 0.877 | 0.936 |
| NFCorpus | 0.298 | 0.309 | **0.343** | 0.326 | 0.371 |
| HotpotQA | 0.682 | 0.520 | **0.699** | 0.675 | 0.767 |
| FEVER | 0.689 | 0.558 | **0.744** | 0.721 | 0.814 |
| SciFact | 0.698 | 0.681 | **0.753** | 0.730 | 0.796 |
| DBPedia | 0.415 | 0.425 | **0.512** | 0.489 | 0.553 |
| FiQA | 0.315 | 0.467 | **0.496** | 0.464 | 0.561 |

The consistent pattern is that the normalized convex combination improves over the individual components and over baseline RRF in these experiments.

## 16. Statistical testing

The main tables use a:

**paired two-tailed t-test**

with:

`p < 0.01`.

The paper marks significance relative to TM2C2 and/or baseline RRF.

The project can safely state that the paper explicitly reports inferential testing, unlike several of the low-resource morphology papers already analyzed.

## 17. RRF parameter sensitivity

The authors tune generalized RRF and find an important domain-generalization problem.

Example:

### MS MARCO

- TM2C2: `0.454`;
- RRF(60,60): `0.425`;
- RRF(5,5): `0.435`;
- RRF(10,4): `0.451`.

A tuned asymmetric RRF can approach TM2C2 in-domain.

### HotpotQA

- TM2C2: `0.699`;
- RRF(60,60): `0.675`;
- RRF(5,5): `0.693`;
- RRF(10,4): `0.621`.

The parameters that work well in the in-domain regime transfer poorly to this out-of-domain dataset.

This supports the paper's argument:

> RRF tuning is real tuning, and its optimum can be domain-sensitive.

## 18. Sample efficiency

The authors progressively increase the amount of labeled training data in 5% steps and tune each fusion method.

A central empirical result:

> with **less than 5% of the training data**, the TM2C2 `α` generally converges to a useful value across the tested datasets.

RRF parameters remain more sensitive to the particular sample, and fully parameterized RRF converges to lower final effectiveness than TM2C2.

This is highly relevant for Uzbek, where qrels will be expensive.

It suggests that a simple normalized score fusion can be tuned with a relatively small validation set instead of building an unnecessarily complex learned fusion model.

## 19. Per-query oracle alpha

The paper also reports an oracle that knows the best `α` separately for every query.

For example:

- MS MARCO TM2C2 = `0.454`, oracle = `0.547`;
- HotpotQA TM2C2 = `0.699`, oracle = `0.767`;
- FEVER TM2C2 = `0.744`, oracle = `0.814`.

This shows substantial query-dependent headroom and anticipates later work such as Query-Adaptive Hybrid Search.

### Critical distinction

This oracle is **not** the current project's planned **oracle union**.

Bruch et al. oracle:

> best fusion weight for each query, using relevance knowledge.

Our oracle union:

> relevant documents available in the union of lexical and dense result sets, independent of the ranking formula.

These are different quantities and must receive different names in the dissertation.

## 20. Properties of a good fusion function

The paper's analysis motivates several desirable properties.

### Monotonicity

Improving a component score should not perversely worsen the fused score.

### Homogeneity

Positive rescaling of underlying vectors/scores should not arbitrarily alter the induced ranking.

### Boundedness

A component with an unbounded scale should not dominate merely because of numerical magnitude.

### Lipschitz continuity

Small score changes should not cause unstable jumps in fused output.

### Interpretability

The parameter should have a comprehensible relationship to component importance.

### Sample efficiency

The fusion should be tunable with limited relevance labels.

The authors argue that TM2C2 satisfies these requirements more naturally than standard RRF.

## 21. Strengths

1. Peer-reviewed A-level ACM TOIS article.
2. 35-page theoretical + empirical analysis rather than a one-dataset comparison.
3. Nine heterogeneous retrieval datasets.
4. In-domain and zero-shot/out-of-domain evaluation.
5. Lexical and semantic components are fixed while fusion behavior is studied.
6. Explicit normalization theory.
7. Direct investigation of RRF parameter sensitivity.
8. Statistical tests are reported.
9. Sample-efficiency analysis is reported.
10. Results are additionally checked with alternative retrieval-pair combinations in appendices.

## 22. Limitations for the Uzbek morphology question

1. English-centric benchmarks.
2. No Uzbek.
3. No agglutinative-language experiment.
4. No controlled `raw/stem/lemma` intervention.
5. The lexical component uses one fixed stemming pipeline.
6. The primary semantic model is all-MiniLM-L6-v2, not a modern Uzbek-validated multilingual retriever.
7. No morphology-conditioned unique-hit analysis.
8. No morphology-conditioned overlap analysis.
9. No morphology-conditioned oracle-union analysis.
10. No query-feature analysis tied to morphology-induced complementarity.
11. Fusion results depend on the fixed top-k candidate-union protocol and should not be interpreted as independent of candidate generation.

## 23. What the paper really proves

The paper provides strong evidence that:

- hybrid score fusion can outperform lexical and semantic channels separately;
- score normalization is necessary for meaningful score fusion;
- among reasonable linear normalization schemes, exact normalization choice is often less important than feared;
- theoretical min-max normalization gives robust behavior;
- RRF is not truly parameter-free;
- RRF can be sensitive to parameters and transfer poorly when tuned across domains;
- rank-only fusion discards score-distance information;
- convex-combination fusion can be tuned sample-efficiently;
- a simple fixed fusion can be a scientifically strong baseline.

## 24. What the paper does NOT prove

It does not establish:

- the best fusion method for Uzbek;
- the best `α` for Uzbek;
- that `α=0.8` should be copied unchanged into the Uzbek experiment;
- whether raw, stemmed or lemmatized Uzbek BM25 is best;
- how changing Uzbek morphology changes the candidate union;
- how morphology changes lexical–dense complementarity;
- how morphology changes hybrid gain.

## 25. Impact on current `v0.8`

### Does this paper kill the gap?

**No.**

It studies:

`fixed lexical retriever + fixed semantic retriever`
→ `fusion-function behavior`.

The current v0.8 studies:

`change lexical morphology`
→ `change lexical relevant set`
→ `change complementarity versus same fixed semantic retriever`
→ `change hybrid gain`.

These are different causal questions.

### What does it kill?

It kills or strongly constrains novelty claims based on:

- fixed weighted score fusion;
- min-max normalized convex combination;
- RRF;
- tuning one global lexical/dense weight;
- arguing that RRF is parameter-free;
- presenting score normalization itself as novelty.

## 26. Experimental-design consequence for the Uzbek PhD

This paper gives a strong basis for defining the fusion control.

### Recommended primary control

Use a **normalized convex combination** as the primary score-fusion baseline.

A reasonable protocol is:

1. create the same-depth lexical and dense candidate lists;
2. form the union;
3. compute both component scores for every candidate;
4. apply a fixed, predeclared normalization protocol;
5. choose **one global `α` on validation data only**;
6. freeze that same `α`, normalization rule and candidate depth for:
   - `H_raw`;
   - `H_stem`;
   - `H_lemma`.

Using exactly the same global `α` across morphology variants is the cleanest causal design because only the lexical morphology changes.

### Recommended secondary robustness control

Also report standard:

`RRF(η=60)`

with the same candidate depth as a widely recognized scale-free baseline.

RRF should be a **robustness/sensitivity control**, not the main method and not novelty.

## 27. Why one global alpha matters

If the project separately optimizes:

- `α_raw`;
- `α_stem`;
- `α_lemma`;

then both morphology and fusion weight change.

That design answers:

> “What is the best separately tuned hybrid for each morphology?”

but it weakens the causal claim:

> “How did morphology itself change hybrid gain?”

Therefore:

- **primary causal experiment:** same `α`;
- **secondary best-achievable analysis:** optionally tune α separately on validation to show practical upper performance.

These should be reported as different experiments.

## 28. Candidate union must also be fixed

Use the same `k` for every lexical condition and the same `k` for `D`.

For example:

`top-k BM25_m ∪ top-k D`.

Otherwise a morphology variant could receive a larger candidate pool and appear more complementary merely because more documents were admitted before fusion.

This control is directly motivated by the paper's union-set formulation.

## 29. Relation to our planned oracle union

The paper strengthens the importance of separating:

### Coverage question

`What relevant documents are available in Lexical ∪ Dense?`

This is our complementarity/oracle-union question.

### Ordering question

`How well does fusion rank those available candidates?`

This is the fusion-function question studied by Bruch et al.

For v0.8, the **coverage/decomposition question is scientifically primary**; fusion is a controlled downstream measurement.

## 30. Consequence for RQ1-RQ3

### RQ1

Unaffected. The paper does not test morphology variants.

### RQ2

Methodologically strengthened.

The hybrid conditions should use a fusion protocol that is fixed across morphology variants; normalized convex combination is now better justified than choosing RRF by default.

### RQ3

Unaffected.

The paper does not analyze interpretable Uzbek morphology/script/query features.

## 31. Final decision

**Role:** CRITICAL fusion-methodology paper.  
**Gap-killer risk for fixed-fusion novelty:** VERY HIGH.  
**Gap-killer risk for `v0.8`:** LOW.  
**Current gap version:** no change required.  
**Primary design implication:** normalized convex combination should be the primary fixed fusion control; RRF should be a secondary robustness baseline.  
**Causal-control implication:** one global alpha, one normalization protocol and one candidate depth should be frozen across `raw/stem/lemma` in the primary experiment.  
**Terminology implication:** distinguish the paper's “per-query alpha oracle” from the project's “oracle union”.  
**Metadata implication:** reconcile project year `2024` with the official ACM publication date `August 2023` before final bibliography.
