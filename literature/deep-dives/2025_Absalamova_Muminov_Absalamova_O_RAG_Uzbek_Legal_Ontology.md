# Absalamova, Muminov & Absalamova — O-RAG for the Uzbek legal domain

**Deep-dive status:** COMPLETED AT VERIFIED-ABSTRACT LEVEL  
**Completed:** 2026-09-14  
**Suggested literature ID:** UZ-HYB-002  
**Reliability:** B  
**Priority for current PhD:** CRITICAL national hybrid/RAG boundary

## 1. Bibliographic record

- **Authors:** Diyora Absalamova, Bahodir Muminov, Gozal Absalamova
- **Title:** *O-Rag Ontology-Enhanced Retrieval-Augmented Generation For The Uzbek Legal Domain*
- **Venue:** *Proceedings of the 9th International Conference on Future Networks and Distributed Systems (ICFNDS ’25)*
- **Publisher:** Association for Computing Machinery (ACM)
- **Publication year:** 2025
- **Pages:** 680–687
- **DOI:** 10.1145/3789692.3789782
- **Language:** English
- **Full text status in this deep dive:** not recovered; ACM full text was not accessible and ResearchGate exposes metadata/request-full-text only
- **Reliability:** **B** — verified ACM proceedings paper; current methodological analysis is intentionally limited to what is supported by verified metadata/abstract

### Metadata note

Some secondary pages show a 2026 appearance date, but ACM-proceedings metadata and independent library/JST records identify the paper as part of **ICFNDS ’25**, pages 680–687, publication year **2025**.

For the project, use **2025** as publication year.

## 2. Why this work matters to our PhD

O-RAG is one of the strongest national gap-boundary papers because it explicitly combines:

- Uzbek legal retrieval;
- RAG;
- a custom domain ontology;
- hybrid retrieval;
- ontology-based reranking;
- evaluation over a Lex.uz-derived question-answering dataset.

It therefore closes broad novelty claims such as:

- “Uzbek hybrid retrieval does not exist”;
- “Uzbek legal RAG does not use structured/domain knowledge”;
- “reranking has not been applied in Uzbek hybrid retrieval”.

However, the currently verified evidence does **not** close our residual `v0.8` question because it does not establish a controlled `raw/stem/lemma × fixed dense` experiment or a complementarity decomposition.

## 3. Ontology explained simply

An **ontology** is a structured map of concepts and their relations.

In a legal domain, an ontology may encode ideas such as:

`crime`
→ has type → `theft`

`theft`
→ governed by → `article X`

`penalty`
→ related to → `sanction`

The purpose is to represent domain meaning explicitly instead of relying only on surface word similarity.

### Why this matters for retrieval

Suppose a query and a legal article use different words but refer to related legal concepts.

A standard lexical match may miss the relation.

A semantic retriever may find a broadly similar passage.

An ontology can add explicit domain knowledge such as:
- concept hierarchy;
- legal-category relation;
- article–concept relation.

O-RAG uses this structured knowledge to rerank initially retrieved legal articles.

## 4. Scientific problem

The paper starts from a practical limitation:

- Uzbek is morphologically rich and low-resource;
- legal text is terminology-sensitive and high-stakes;
- generic RAG can retrieve semantically nearby but legally wrong material.

The proposed solution is to inject a custom legal ontology into the retrieval/reranking pipeline.

## 5. Verified architecture

At the level supported by the abstract, the pipeline can be represented as:

`Uzbek legal query`
→ `hybrid retrieval`
→ `candidate legal articles`
→ `ontology-based reranking`
→ `higher-ranked conceptually relevant legal articles`
→ `RAG generation / citation`

The key new component described by the authors is an **ontological reranking algorithm**.

### What reranking means

First-stage retrieval gets a candidate list.

Reranking means:
> take those candidates and reorder them using a stronger or additional signal.

In O-RAG the additional signal is structured legal knowledge from the ontology.

### What is NOT verified

The accessible abstract does not expose enough detail to safely identify:

- the lexical first-stage algorithm;
- whether BM25 is used;
- whether TF-IDF is used;
- exact dense/embedding model;
- vector database/index;
- fusion formula;
- RRF;
- weighted fusion;
- morphology preprocessing;
- top-k candidate counts;
- ontology schema size;
- exact ontology score formula.

These must remain unknown until the full paper is inspected.

## 6. Data

Verified:
- a new question-answering dataset was developed;
- source: official Uzbekistan legislative database **Lex.uz**;
- domain: Uzbek law / legal articles.

Not verified from accessible evidence:
- total number of legal documents/articles;
- total number of questions;
- train/dev/test split;
- annotation procedure;
- qrels structure;
- number of assessors;
- inter-annotator agreement;
- whether the dataset is public.

Therefore no dataset-size number should be invented.

## 7. Baselines

The abstract states that O-RAG outperforms **standard RAG baselines**.

However, the accessible evidence does not specify the full baseline list.

Do not currently claim:
- “O-RAG beats BM25”;
- “O-RAG beats dense-only”;
- “O-RAG beats RRF”;
- “O-RAG beats USHRA”;

unless the full paper confirms it.

## 8. Metrics

Two metrics are explicitly named in the abstract:

### Retrieval Precision / Hit Rate

Simple meaning:
> Did the retrieval stage include the correct/relevant legal material among the retrieved results?

The paper labels this broadly as retrieval precision / hit rate.

Exact cutoff (`@k`) and formula are not recoverable from the abstract.

### Citation Accuracy

Simple meaning:
> Does the final answer cite the correct legal source/article?

This is highly relevant for legal RAG, because a fluent answer with a wrong law citation is unsafe.

### Critical distinction

Citation Accuracy is not the same as document-ranking effectiveness.

Hit Rate is retrieval-related, but without the paper’s exact definition and cutoff it should not be equated automatically with Recall@k or Precision@k.

## 9. Numerical results

The verified abstract states that:

- O-RAG outperforms standard RAG baselines across the reported measures;
- O-RAG has higher Retrieval Precision (Hit Rate);
- O-RAG has higher Citation Accuracy.

Exact metric values were **not recovered** from the accessible primary/metadata record.

Therefore no numerical values should be inserted into the project until the full paper is obtained.

## 10. Statistical evidence

No statistical significance test, confidence interval, bootstrap or repeated-run protocol is verifiable from the accessible abstract-level evidence.

Do not infer significance merely from “outperforms”.

## 11. What O-RAG proves

At the current evidence level, O-RAG supports that:

1. published Uzbek legal RAG already uses a custom legal ontology;
2. ontology-guided hybrid retrieval is already a national research direction;
3. ontology-based reranking is already applied to Uzbek legal information;
4. Lex.uz-derived legal QA evaluation exists;
5. the authors report improvements over standard RAG baselines in retrieval-related Hit Rate and Citation Accuracy.

## 12. What O-RAG does NOT prove for our current PhD

It does not establish:

- `BM25_raw`;
- `BM25_stem`;
- `BM25_lemma`;
- a controlled morphology intervention;
- a fixed modern dense comparator across morphology variants;
- lexical-only relevant hits;
- dense-only relevant hits;
- lexical–dense overlap/intersection;
- oracle union;
- incremental hybrid gain;
- morphology-conditioned query analysis.

It also does not currently establish, from accessible evidence:
- exact BM25 use;
- exact fusion method;
- exact dense model.

## 13. Why O-RAG is not the same as our planned hybrid

Our core controlled PhD design is deliberately simple:

`BM25_x + fixed Dense D`

where only the lexical representation changes.

O-RAG adds another major source of information:

`domain ontology`.

Therefore if O-RAG improves retrieval, the improvement may come from:
- initial lexical/semantic retrieval;
- ontology expansion/matching;
- ontology-based reranking;
- interaction among these components.

Without an ablation, the gain cannot be attributed simply to “lexical + semantic hybrid”.

This distinction is central for interpreting the work.

## 14. Ablation explained simply

An **ablation** means removing one component at a time to measure what it really contributes.

For O-RAG, an ideal ablation would compare something like:

`standard RAG`
vs
`hybrid retrieval without ontology`
vs
`hybrid + ontology`
vs
`hybrid + ontology reranking`.

The accessible abstract does not provide enough evidence to reconstruct such a table.

Therefore we must not say the ontology alone caused all improvement.

## 15. Relationship to USHRA

Both papers are by the same author group and target Uzbek legal AI.

### USHRA
Verified broad components:
- multilingual embeddings;
- hybrid semantic retrieval;
- RAG;
- Lex.uz;
- 200 criminal-law queries;
- 85% answer accuracy.

### O-RAG
Adds an explicit structured knowledge layer:
- custom legal ontology;
- ontology-driven hybrid retrieval;
- ontological reranking;
- retrieval Hit Rate and Citation Accuracy emphasis.

Conceptually:

`USHRA`
→ hybrid semantic legal retrieval

`O-RAG`
→ hybrid legal retrieval + explicit ontology + reranking.

But the exact relationship between their code/data/components cannot be established without full texts.

## 16. Relationship to CURRENT_GAP v0.8

**Status:** confirms that broad Uzbek hybrid/reranking novelty is closed; does not close v0.8.

Current residual question:

`raw/stem/lemma`
→ `change in lexical relevant set`
→ `change in overlap/unique hits with fixed dense retriever`
→ `change in incremental hybrid gain`
→ `relation to Uzbek query characteristics`.

O-RAG instead studies:

`hybrid legal retrieval`
+ `domain ontology`
→ `ontology-based reranking`
→ `legal RAG`.

Thus it operates at a different explanatory level.

No change to `CURRENT_GAP.md` is required.

## 17. Implications for our PhD scope

This paper actually supports keeping our PhD **simpler**.

We do not need to add:
- legal ontology;
- knowledge graph;
- GraphRAG;
- ontology reranking

to obtain a valid PhD contribution.

Doing so would introduce another causal factor and make it harder to answer the morphology/complementarity question.

For a focused PhD:

`BM25_raw/stem/lemma`
+ `fixed dense`
+ `simple controlled fusion`

is scientifically cleaner.

Ontology/RAG can remain future system enhancement if the National Library later needs:
- subject taxonomy;
- author/topic/entity relations;
- controlled vocabulary;
- semantic browsing.

## 18. Practical lesson for the National Library

O-RAG gives an important **future** architecture idea.

A National Library already has structured metadata and classification information:
- authors;
- subjects;
- publication types;
- dates;
- classifications;
- possibly controlled subject headings.

Later, this structured metadata could play a role similar to an ontology and rerank results.

But adding this now would confound our core PhD experiment.

Recommended order:

1. establish lexical–dense retrieval behavior;
2. build the working hybrid search;
3. validate it on library data;
4. only then consider metadata/ontology-based reranking as a post-PhD/DSc enhancement.

## 19. Open questions requiring full text

1. Exact hybrid retrieval components.
2. Whether BM25 or another lexical retriever is used.
3. Exact embedding model.
4. Vector index/database.
5. Exact ontology schema and concept count.
6. Ontology construction method: manual/automatic/hybrid.
7. Query-to-ontology matching method.
8. Exact reranking score/formula.
9. Candidate top-k before/after reranking.
10. Dataset size and annotation protocol.
11. Baseline list.
12. Exact Hit Rate values and cutoff.
13. Exact Citation Accuracy values.
14. Ablation study, if any.
15. Statistical significance.
16. Whether morphological normalization is used.
17. Whether code/dataset/ontology are public.

## 20. Decision after deep dive

- **Keep CURRENT_GAP v0.8:** yes.
- **Modify gap/history/decisions:** no.
- **National role:** CRITICAL evidence that Uzbek hybrid/RAG + ontology reranking already exists.
- **Reliability:** B; ACM publication verified, methods limited to abstract-level evidence until full text is obtained.
- **Use in Chapter I:** yes, especially 1.3 as national hybrid/reranking evidence.
- **Add ontology to our core PhD:** no.
