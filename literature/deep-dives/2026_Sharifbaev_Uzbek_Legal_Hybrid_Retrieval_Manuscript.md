# Sharifbaev A.N. — Uzbek Legal Hybrid Retrieval / GraphRAG-RL Dissertation Manuscript

**Targeted deep-dive status:** COMPLETED
**Completed:** 2026-09-10
**Literature ID:** UNVER-002

## 1. Source record

- **Author:** Abdurakhmon Nosir ugli Sharifbaev / Шарифбаев Абдурахмон Носир угли
- **Year on manuscript:** 2026
- **Institution on manuscript:** Tashkent University of Information Technologies named after Muhammad al-Khwarizmi
- **Specialty:** 05.01.10 — Information systems and processes
- **Manuscript title:** «Разработка интелектуального гибридного поисковой модели и информационной ситетмы (на основе законадательных документов)» [spelling preserved from the supplied manuscript]
- **Primary evidence used:** user-supplied full dissertation manuscript, 119 parsed pages, analyzed on 2026-09-10
- **External identity check:** TUIT public staff page lists Sharifbaev Abdurakhmon Nosir ugli as an assistant; related 2024 GNN-RL publications are independently verifiable.
- **Official defense/publication status:** not verified
- **Reliability:** D

## 2. Why reliability is D

The manuscript is extremely relevant technically, but it cannot yet be treated as an officially defended dissertation or a clean final publication because the analyzed file contains signs of unfinished editing and internal inconsistency, including:

- placeholder bibliography entries such as `A. Author` / `B. Author`;
- incomplete arXiv identifiers such as `2408.XXXX` and `2501.XXXXX`;
- numerical inconsistency for R1-Searcher (`0.612` in a results table vs `0.512` in surrounding prose);
- different counts of query/answer data across sections;
- incomplete manuscript fields.

Therefore this work is a **critical gap-killer lead**, but not citable established evidence until an official final dissertation/abstract or primary publication record for the relevant experiments is verified.

## 3. Why this work matters to the PhD

This manuscript is the closest Uzbek work found so far to the dissertation topic because it explicitly combines:

- Uzbek/Russian legal text;
- morphological preprocessing and lemmatization;
- BM25 lexical retrieval;
- LaBSE dense retrieval;
- graph retrieval;
- hybrid integration;
- a query-dependent controller trained with reinforcement learning.

It therefore invalidates broad claims that Uzbek lacks morphology-aware lexical + dense hybrid retrieval or query-dependent retrieval strategies.

## 4. Corpus and query setup reported in the manuscript

The manuscript reports a legal/parliamentary corpus of **1,197 documents** from the Republic of Uzbekistan, including laws, Senate resolutions, transcripts, committee opinions and Senate regulations.

Documents are reported as Russian and Uzbek, including Uzbek Cyrillic and Latin forms.

A legal knowledge graph is reported with approximately:

- **14,832 vertices**;
- **43,127 edges**.

The manuscript reports an expert test set of **350 query–reference-answer pairs**, divided into:

- 50 validation queries;
- 300 test queries.

Reported query scenarios include:

- retrieval of a specific legal norm — 35%;
- comparison of norms across documents — 25%;
- procedures/chronology — 20%;
- fact extraction from transcripts/opinions — 15%;
- complex multi-hop queries — 5%.

### Internal data-count warning

Elsewhere the manuscript states:

- 700 query–answer pairs;
- 280 training queries for the applied corpus.

`280 + 50 + 300 = 630`, not 700. The unexplained difference is one reason the manuscript cannot yet be treated as final evidence.

## 5. Lexical retrieval

The manuscript describes the lexical module as:

`tokenization + lemmatization + stop-word processing + inverted index + BM25`.

The index is reported to be built on tokenized and **lemmatized texts with Russian and Uzbek morphology taken into account**.

BM25 parameters are reported as:

- `k1 = 1.2`;
- `b = 0.75`.

Elasticsearch is used for the lexical retrieval implementation.

### What this means for the current gap

Uzbek lemmatization is not merely discussed theoretically here; it is integrated directly into a BM25 retrieval channel inside a hybrid search architecture.

The project therefore must not claim:

> “Uzbek morphology-aware BM25 has never been used together with semantic retrieval.”

## 6. Dense retrieval

The vector module is described as:

- **LaBSE** encoder;
- 768-dimensional representations;
- reportedly fine-tuned on a parallel Russian–Uzbek legal corpus;
- **Milvus** vector store;
- HNSW approximate nearest-neighbor search;
- cosine similarity.

This is a genuine dense-retrieval-style component, not merely a generic BERT mention.

## 7. Graph retrieval and adaptive controller

The manuscript adds a third graph layer using Neo4j and a legal knowledge graph.

The central GraphRAG-RL controller is described as choosing among:

- lexical retrieval;
- vector retrieval;
- graph traversal;
- stopping/continuation actions.

The controller reportedly uses graph neural representations and a policy optimized with GRPO/SFT-style procedures.

Therefore a broad claim that “query-dependent hybrid retrieval for Uzbek is absent” is not safe.

## 8. Query-dependent behavior

The manuscript explicitly argues that the components have different roles:

- lexical retrieval for exact legal terms, article numbers and fixed formulations;
- vector retrieval for semantic similarity and synonymous/alternative wording;
- graph retrieval for structural and cross-reference relations.

It also reports that simpler queries may be handled with one or two lexical-retriever calls, while more complex questions expand into vector and graph retrieval.

This is already a form of query-dependent retrieval strategy.

### What is still missing

The work does not establish a systematic relation between morphology-specific query properties and relative lexical/dense effectiveness.

It does not report an explanatory model based on:

- number/type of affixes;
- morphological complexity;
- rare terms;
- named entities;
- identifiers/numbers;
- Latin/Cyrillic variation;
- lexical overlap;
- paraphrasticity.

## 9. Reported comparison results

For the 300-query application test set, the manuscript reports the following system-level table:

| Method | F1 | ACCL | SBERT | RA |
|---|---:|---:|---:|---:|
| Vanilla LLM | 0.089 | 0.187 | 0.412 | 0.053 |
| Naive RAG | 0.251 | 0.437 | 0.563 | 0.314 |
| HippoRAG | 0.498 | 0.593 | 0.601 | 0.421 |
| PropRAG | 0.376 | 0.610 | 0.587 | 0.398 |
| R1-Searcher | 0.612 | 0.867 | 0.825 | 0.645 |
| GraphRAG-RL | **0.727** | **0.923** | **0.828** | **0.787** |

The manuscript defines these primarily as answer/context/reference-level metrics rather than a clean standard retrieval-only evaluation.

### Critical distinction

These numbers cannot be interpreted as pure BM25-vs-dense retrieval effectiveness.

## 10. Missing BM25-vs-dense controlled comparison

A BM25-RAG baseline is described in the baseline section, but it is absent as a separate row from the main Uzbek application table above.

Therefore the manuscript does not cleanly establish on the Uzbek legal set:

`standalone BM25 vs standalone LaBSE vs lexical+dense hybrid`

under identical retrieval metrics.

## 11. Morphology is not isolated

The work uses a lemmatized lexical index, but it does not report a controlled ablation such as:

`BM25_raw ↔ BM25_stem ↔ BM25_lemma`.

No separate experiment isolates whether the observed system effectiveness is caused by lemmatization itself.

This is the central surviving distinction for the current PhD.

## 12. Complementarity is asserted but not decomposed

The manuscript states that lexical, vector and graph layers complement one another and reports that removing the lexical module harms overall system quality.

However, the analyzed manuscript does not provide a systematic decomposition of:

- relevant documents found only by BM25;
- relevant documents found only by LaBSE;
- relevant documents found by both;
- oracle union;
- how these sets change under different morphological lexical representations;
- per-query hybrid gain attributable specifically to lexical+dense complementarity.

The graph, GNN, RL policy and reward function also change simultaneously, so overall GraphRAG-RL gains cannot be causally attributed to lexical–dense fusion alone.

## 13. What the manuscript would close if officially verified

If the final official version confirms the described experiments, the project cannot claim:

1. absence of Uzbek BM25 + dense hybrid retrieval;
2. absence of lemmatization inside an Uzbek BM25 hybrid system;
3. absence of query-dependent selection among Uzbek retrieval strategies;
4. absence of a real Uzbek legal/parliamentary corpus for hybrid retrieval evaluation.

## 14. What the manuscript does not close

Even if fully verified, it still does not establish:

1. controlled `raw/stem/lemma` effects on BM25;
2. fixed-dense comparison across morphology variants;
3. morphology-induced change in lexical–dense overlap/unique-hit structure;
4. incremental hybrid gain attributable to morphology;
5. statistical interaction between morphology and retriever type;
6. systematic morphology/script-aware query-level explanation.

## 15. Consequence for the research gap

This manuscript is the main Uzbek reason the gap must be narrower than:

> “Uzbek hybrid search with morphology and dense retrieval is missing.”

The surviving question is instead:

> how changing the morphological representation of the lexical channel changes its complementarity with a fixed modern semantic retriever, and under which Uzbek query characteristics this happens.

## 16. Required verification before citation

Before using this work as dissertation evidence, verify at least one of:

- official OAK defense announcement/abstract;
- final university repository version;
- peer-reviewed publication containing the same Uzbek retrieval experiment and data;
- corrected final manuscript without placeholders/internal contradictions.

Until then, cite only related verified publications where appropriate and keep the dissertation manuscript at **D** reliability.

## 17. Final status

**Role in project:** most important Uzbek gap-killer lead.
**Reliability:** D (unverified manuscript).
**Gap-killer risk:** VERY HIGH for broad Uzbek hybrid/query-dependent claims.
**Residual gap after this work:** controlled morphology-induced change in lexical–dense complementarity and its relation to Uzbek query features.
