# Arabic Legal Information Retrieval: The Impact of Morphological Segmentation and Semantic Embeddings

**Targeted gap-analysis status:** COMPLETED
**Completed:** 2026-09-10
**Literature ID:** HYB-011

## 1. Bibliographic record

- **Authors:** Rawan Aboasal; Salma Montasser; Fouad Hossam Eldin; Ali Abdelwahab; Hazem Abdelazim
- **Year:** 2026
- **Venue:** *Procedia Computer Science*, Volume 275, pp. 275–282; work associated with ACLING 2025 proceedings metadata
- **DOI:** `10.1016/j.procs.2026.01.034`
- **Official record:** https://www.sciencedirect.com/science/article/pii/S1877050926000347
- **Source type:** peer-reviewed proceedings/journal-volume article, open access
- **Reliability:** B
- **Evidence limitation for this card:** the official abstract/metadata were fully verified, but a complete methods-section audit was not available through the current access path. Claims below are therefore restricted to what the official record directly supports.

## 2. Why this work matters to the PhD

This is one of the strongest global gap-boundary papers for the current Uzbek project because it places in the same Arabic legal IR study:

- BM25;
- explicit morphological processing with Farasa;
- modern embedding models including BGE-M3, GTE, Ada v3 and Mistral-embed;
- hybrid lexical–semantic retrieval;
- MAP and nDCG@10.

Therefore the current PhD cannot claim novelty from the mere presence of:

`morphology-aware BM25 + modern embeddings + hybrid retrieval`.

## 3. Research problem

Arabic legal retrieval is difficult because of both rich morphology and specialized legal terminology. The paper studies whether morphological segmentation and semantic embedding representations improve retrieval effectiveness and whether their combination helps.

The study therefore directly addresses a broad form of:

`morphology × lexical retrieval × semantic retrieval`.

## 4. Dataset

The official abstract reports a synthetic benchmark with:

- **500 legal articles**;
- **1,000 question–answer pairs**;
- answers generated with **GPT-4.1-mini** used as ground truth for model assessment.

### Important caution

The available official abstract does not fully explain how answer-level synthetic ground truth maps to document-level relevance judgments required by MAP and nDCG. The final dissertation must not infer a stronger qrels protocol than the full paper explicitly documents.

For the current Uzbek project, independent human relevance judgments would provide stronger evidence.

## 5. Lexical retrieval and morphology

The official record reports BM25 both without and with Farasa morphological processing.

Key MAP values:

- **BM25:** 0.7178
- **BM25 + Farasa:** 0.7715

Absolute difference:

`+0.0537 MAP`.

### What this establishes

In this Arabic legal setting, adding the Farasa morphological analysis/segmentation pipeline is associated with a clear numerical improvement in BM25 MAP.

### What this does not establish

It does not establish:

- `raw vs stem vs lemma` as three controlled conditions;
- that Farasa is equivalent to stemming or lemmatization in the sense intended for the Uzbek experiment;
- that the effect transfers to Uzbek;
- that the reported difference is statistically significant unless the exact inferential test is verified from full text.

## 6. Modern embedding models

The official abstract names advanced embedding-based models including:

- Ada v3;
- BGE-M3;
- GTE;
- Mistral-embed.

Among the embedding models, the abstract reports **Mistral-embed** as the strongest overall standalone result:

- MAP = **0.7570**;
- nDCG@10 = **0.7964**.

A key methodological consequence is that a morphology-aware lexical model can remain highly competitive with modern embedding retrieval in a morphologically rich language.

The current PhD should therefore not assume `Dense > BM25` before measurement.

## 7. Hybrid result

The official abstract reports a hybrid configuration combining:

`BM25 (Farasa) + Ada v3 embeddings`.

Reported values:

- MAP = **0.8304**;
- nDCG@10 = **0.8626**.

This numerically exceeds the reported standalone BM25+Farasa and standalone embedding results.

### Consequence

The global claim:

> “It is not known whether morphology-aware lexical retrieval can be productively combined with modern semantic embeddings.”

is no longer defensible.

## 8. Why the paper does not close the refined gap

The residual Uzbek question is not whether such a hybrid can work. It is whether changing the **lexical morphological representation itself** changes the structure of complementarity with a fixed semantic retriever.

The official abstract does not establish a controlled matrix such as:

`BM25_raw + D`
`BM25_stem + D`
`BM25_lemma + D`

with the same dense retriever `D` and the same fusion procedure.

It also does not establish a decomposition of:

- unique relevant documents found only by BM25;
- unique relevant documents found only by the dense retriever;
- intersection/overlap;
- oracle union;
- per-query incremental hybrid gain;
- how those quantities change after morphological normalization.

## 9. Query-level explanation

The available official record does not provide a systematic analysis of which linguistic query properties cause:

- BM25 gains from morphology;
- dense-only wins;
- hybrid-only wins;
- changes in lexical–dense overlap.

For the Uzbek project this leaves room for interpretable factors such as:

- affix/morphological complexity;
- script variation;
- rare terms;
- named entities;
- numbers/identifiers;
- query length;
- lexical overlap;
- paraphrastic or descriptive formulation.

The novelty cannot be “query-type analysis” in general; it must be tied to the morphology-induced change in lexical–semantic behavior for Uzbek.

## 10. Statistical significance

The official abstract provides numerical effectiveness values but does not state an inferential statistical test for the main retrieval comparisons.

Until the full methods/results section is verified, the project should say:

> “Farasa numerically increased BM25 MAP from 0.7178 to 0.7715.”

and avoid upgrading this to “statistically significant improvement.”

## 11. What the paper really establishes

The paper establishes at the verified abstract level that:

1. morphology-aware BM25 is already evaluated together with modern embedding models in Arabic legal IR;
2. Farasa preprocessing can numerically improve BM25;
3. modern dense/embedding retrieval does not automatically dominate morphology-aware BM25;
4. a morphology-aware lexical + semantic hybrid can outperform the reported standalone components.

## 12. What the paper does not establish

It does not establish:

1. raw/stem/lemma comparative effects;
2. morphology-conditioned complementarity decomposition;
3. fixed-dense controlled interaction across morphology variants;
4. Uzbek-specific behavior;
5. Uzbek script normalization effects;
6. per-query linguistic explanation of the morphology × retrieval interaction;
7. human-judged Uzbek qrels.

## 13. Consequence for the current research gap

A broad gap based on “morphology + BM25 + modern dense + hybrid has not been studied” is invalid.

The residual research opportunity must move to:

> whether and how changing the lexical morphological representation changes **which relevant documents remain unique to lexical versus semantic retrieval**, and therefore changes the incremental value of hybridization.

## 14. Final status

**Role in project:** CRITICAL global gap-boundary evidence.
**Gap-killer risk:** VERY HIGH for broad morphology-aware hybrid claims.
**Residual gap after this work:** morphology-induced change in lexical–dense complementarity, especially under a controlled fixed-dense design and for Uzbek query characteristics.
