# GreekBarRetrieval: A Benchmark for Greek Statutory Retrieval

**Targeted deep-dive status:** COMPLETED
**Completed:** 2026-09-10
**Literature ID:** HYB-012

## 1. Bibliographic record

- **Authors:** Ernest Beta; Odysseas S. Chlapanis; Dimitrios Galanis; Ion Androutsopoulos
- **Year:** 2026
- **arXiv:** `2608.18752`
- **Primary class:** cs.IR
- **First posted:** 2026-08-19
- **Official record:** https://arxiv.org/abs/2608.18752
- **Source type:** preprint / benchmark paper
- **Reliability:** C
- **Publication warning:** as of 2026-09-10 the project has verified the arXiv preprint; a final peer-reviewed proceedings record has not yet been established in the project evidence base.

## 2. Why this work matters to the PhD

GreekBarRetrieval is the closest global gap-killer found during the 2026-09-10 search because the same study contains:

- three BM25 variants with different Greek preprocessing/morphology handling;
- nine modern dense retrievers;
- standard ranking metrics;
- sparse–dense fusion;
- query reformulation;
- a real statutory-retrieval benchmark.

It therefore invalidates any novelty claim based simply on putting morphology-aware BM25 variants and modern dense retrieval in the same experiment.

## 3. Benchmark

The primary arXiv abstract reports:

- **283** Greek bar-exam questions;
- case facts supplied with each question;
- **6,308** candidate statutory articles;
- questions/facts written in everyday language that must be mapped to formal statutory terminology and abstract legal concepts.

The benchmark is derived from and complements GreekBarBench by isolating the statutory retrieval step.

The detailed paper extraction used during this deep dive reports approximately **2.74 relevant articles per query** and evaluation with:

- nDCG@10;
- nDCG@100;
- MAP@100;
- Recall@10;
- Recall@100.

## 4. Morphology-aware BM25 variants

The study evaluates three BM25 pipelines that differ in Greek preprocessing:

- **BM25-GreekStemmer** — Greek stemming;
- **BM25-spaCy** — spaCy Greek lemmatization;
- **BM25-gr-nlp-toolkit** — tokenization-oriented pipeline without extensive morphological normalization.

### Important terminology caution

The third pipeline should not automatically be labelled `raw BM25`. It is better interpreted as a minimal/tokenization-oriented condition. The current Uzbek experiment can still define a cleaner raw baseline explicitly.

### Consequence

The claim:

> “BM25 stemming/lemmatization variants have not been compared alongside modern dense retrieval.”

is no longer defensible globally.

## 5. Dense retrieval

The primary abstract states that **nine dense retrievers** are evaluated.

Detailed paper extraction identifies models including:

- Gemini-001;
- Qwen3-8B;
- Qwen3-4B;
- Qwen3-0.6B;
- Euler-Legal-V1;
- Jina-v5-small;
- Arctic-v2;
- EmbGemma-300M;
- Nomic-v1.5.

The paper reports that vanilla dense retrieval strongly outperforms vanilla sparse retrieval on Recall@100.

Representative values from the paper extraction:

- best vanilla BM25 Recall@100 ≈ **0.36**;
- Gemini-001 Recall@100 ≈ **0.77**;
- Qwen3-8B Recall@100 ≈ **0.67**;
- Euler-Legal-V1 Recall@100 ≈ **0.68**.

These values are useful boundary evidence but should be rechecked against the final paper PDF before being copied into final dissertation prose.

## 6. Query reformulation

The primary abstract reports that LLM-based query reformulation substantially closes the sparse–dense gap and improves dense retrieval as well.

For BM25-GreekStemmer, the extracted table reports:

| Condition | nDCG@10 | nDCG@100 | Recall@10 | Recall@100 | MAP@100 |
|---|---:|---:|---:|---:|---:|
| Original | 0.10 | 0.14 | 0.16 | 0.36 | 0.09 |
| Tuned | 0.10 | 0.16 | 0.16 | 0.41 | 0.07 |
| LLM reformulation | **0.20** | **0.28** | **0.30** | **0.60** | **0.16** |
| Reformulation + tuned | 0.18 | 0.26 | 0.25 | 0.61 | 0.14 |

The paper warns that BM25 parameter tuning was selected on the full benchmark and should therefore be viewed as an oracle upper bound rather than a clean held-out tuning protocol.

### Consequence for Uzbek design

BM25 parameters must be tuned only on validation queries, not on the final test set.

## 7. Sparse–dense fusion

The study includes sparse–dense fusion, including Reciprocal Rank Fusion (RRF).

The primary abstract states that LLM query reformulation outperforms sparse–dense fusion. Detailed extraction reports that RRF hurts several dense encoders rather than universally improving them.

Therefore the project must retain the decision:

> `BM25 + dense` or RRF is not automatically superior to the strongest standalone retriever and is not a novelty claim.

## 8. ReAct-like BM25 retrieval

The authors also introduce a ten-round ReAct-like LLM reformulation loop for BM25. The primary abstract states that this system obtains the best nDCG and MAP scores among tested retrievers.

Detailed extraction reports approximately:

- Recall@100 = 0.67;
- nDCG@10 = 0.43;
- nDCG@100 = 0.47;
- Recall@10 = 0.52;
- MAP@100 = 0.37.

This result is relevant as evidence that sophisticated query reformulation can restore much of BM25's effectiveness in a difficult vocabulary-mismatch setting. It is a separate direction from the current Uzbek morphology–complementarity gap.

## 9. Why GreekBarRetrieval does not close the refined gap

The paper contains morphology-aware BM25 variants, modern dense retrievers and fusion, but the current deep dive did not find evidence of the specific decomposition needed for the Uzbek residual question:

`BM25_minimal + D`
`BM25_stem + D`
`BM25_lemma + D`

where `D` is the **same fixed dense retriever** and all other fusion choices are held constant.

More importantly, it does not systematically report how morphology changes:

- unique relevant hits attributable to BM25;
- unique relevant hits attributable to the dense retriever;
- relevant-set intersection;
- oracle union;
- incremental hybrid gain;
- these quantities on a per-query basis.

Thus the study compares nearby components but does not establish the causal interaction:

`change lexical morphology → change lexical–dense complementarity`.

## 10. Query characteristics

GreekBarRetrieval clearly demonstrates that query formulation matters: everyday case descriptions must be mapped to formal legal terminology, and LLM reformulation strongly helps BM25.

However, the current deep dive did not find a systematic analysis tying the **change caused by stemming/lemmatization** to interpretable linguistic query features such as:

- affix/morphological complexity;
- named entities;
- rare terms;
- numbers/identifiers;
- lexical overlap;
- script variation;
- paraphrasticity.

The current PhD therefore cannot claim novelty for query-type analysis in general. Its residual contribution must concern morphology-conditioned complementarity for Uzbek.

## 11. Statistical analysis

Detailed paper extraction reports statistical testing for selected comparisons with Holm correction for multiple comparisons. The exact underlying significance test should be verified directly from the full paper before being cited in final dissertation text.

## 12. Limitations relevant to the current PhD

- only 283 queries;
- approximately a few relevant statutes per query;
- relevance is derived from official bar-exam solution citations and may not exhaust every arguably relevant article;
- no clean development split for the reported BM25 tuning sweep;
- LLM-dependent experiments may have generation variance;
- the work is currently a preprint in the project's evidence hierarchy;
- Greek morphology is not equivalent to Uzbek agglutinative morphology.

## 13. What the paper really establishes

At the current evidence level, GreekBarRetrieval establishes that:

1. morphology-sensitive BM25 variants can be evaluated in the same benchmark as modern dense retrievers;
2. dense retrieval can strongly outperform vanilla BM25 in legal statutory retrieval;
3. query reformulation can materially change the relative effectiveness of sparse and dense retrieval;
4. sparse–dense fusion is not guaranteed to help;
5. the mere experimental matrix `morphology-aware BM25 + dense + fusion` is no longer sufficient as a novelty claim.

## 14. What the paper does not establish

It does not establish:

1. the morphology-induced change in lexical–dense complementarity under a fixed-dense controlled design;
2. unique-hit/overlap/oracle-union decomposition for each BM25 morphology variant;
3. Uzbek-specific effects;
4. Uzbek Latin/Cyrillic and apostrophe variation effects;
5. a systematic relation between morphology-induced complementarity changes and Uzbek linguistic query features.

## 15. Consequence for the current research gap

GreekBarRetrieval forces the gap away from “components exist together” and toward an **interaction question**:

> how changing the morphological representation of the lexical channel changes which relevant documents are uniquely recovered by lexical versus semantic retrieval and changes the incremental value of hybridization.

## 16. Final status

**Role in project:** #1 current global gap-killer / benchmark boundary paper.
**Reliability:** C until peer-reviewed publication status is verified.
**Gap-killer risk:** EXTREMELY HIGH for broad `raw/stem/lemma + dense + hybrid` claims.
**Deep-dive conclusion:** the refined Uzbek morphology→complementarity gap survives, but only in the narrower interaction/decomposition form.
