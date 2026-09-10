# Gap Boundary Update — 2026-09-10

**Status:** ACTIVE research synthesis
**Purpose:** preserve the evidence that narrowed the previous `v0.4` research gap to the current `v0.8 refined` formulation.
**Scope:** Uzbek national evidence + closest international morphology/lexical/semantic/hybrid retrieval gap killers.

---

## 1. Executive conclusion

The broad research opportunity has changed materially.

The project can no longer claim novelty from any of the following by themselves:

- Uzbek hybrid retrieval;
- Uzbek semantic retrieval;
- morphology-aware BM25;
- `raw/stem/lemma` comparisons in a morphologically complex low-resource language;
- BM25 vs embedding/dense retrieval;
- morphology-aware lexical + semantic hybrid retrieval;
- fixed weighted fusion or RRF;
- query-dependent retrieval strategy selection;
- query-type analysis in general;
- lexical–semantic complementarity as a general research idea.

The strongest surviving research question is an **interaction/decomposition problem**:

> how changing the morphological representation of the Uzbek lexical channel changes the structure of its complementarity with a fixed modern semantic retriever.

The key observable quantities are not only aggregate MAP/nDCG/Recall, but also:

- unique relevant hits of the lexical component;
- unique relevant hits of the semantic component;
- relevant-set intersection/overlap;
- oracle union;
- incremental hybrid gain;
- per-query changes in these quantities;
- relation of the changes to interpretable Uzbek query features.

---

## 2. National evidence boundary

### 2.1 Bakaev PhD (2021)

Established:

- Uzbek morphological analysis is a mature research line;
- morphology is linked to query processing and library/full-text search applications.

Not established:

- controlled modern `BM25_raw ↔ BM25_stem ↔ BM25_lemma` retrieval benchmark;
- interaction with a modern dense retriever.

### 2.2 Xusainova PhD (2024)

Established:

- Uzbek tokenization, stemming and lemmatization tools exist;
- morphology is applied to corpus/search optimization.

Not established:

- standard qrels-based comparison of raw/stem/lemma BM25;
- morphology-conditioned lexical–dense complementarity.

### 2.3 Elov DSc abstract (2026 screening)

Established at the abstract level:

- integrated Uzbek NLP infrastructure covers morphology, syntax and semantics;
- morphology normalization is connected to information-retrieval applications;
- substantial corpora and linguistic tools exist.

Important distinction:

- integration of NLP analysis levels is **not** the same as lexical+semantic retrieval fusion;
- reported NLP module accuracy/F1 values are not retrieval effectiveness metrics.

Not established:

- controlled BM25 morphology ablation;
- modern dense/hybrid retrieval interaction;
- query-level complementarity analysis.

### 2.4 Turayev PhD abstract (2026 screening)

Established:

- Uzbek lemmatization is explicitly implemented using a lexical base of more than 32k base forms;
- neural/statistical morphology and syntactic analysis are developed.

Not established:

- BM25 retrieval experiment;
- dense retrieval;
- lexical–semantic hybrid retrieval;
- standard IR metrics for morphology effects.

### 2.5 Axmedova PhD abstract (2026 screening)

Established:

- modern multilingual semantic matching for Uzbek includes Multilingual E5/Jina-style embedding use in paraphrase-related processing;
- paraphrastic variation is computationally modeled for Uzbek.

Important distinction:

- semantic similarity/paraphrase detection is not corpus-level ad-hoc retrieval.

Not established:

- BM25 vs modern dense retrieval in one controlled Uzbek benchmark;
- morphology × complementarity.

### 2.6 Ishkobilov et al. (2026)

Established:

- real corpus-level Uzbek semantic retrieval exists;
- TF-IDF vs FastText comparison is evaluated with standard IR metrics;
- semantic representation can outperform the tested lexical baseline in the seismic-regulation domain.

Not established:

- BM25;
- raw/stem/lemma morphology intervention;
- hybrid lexical+dense retrieval;
- per-query complementarity analysis.

### 2.7 USHRA / O-RAG

Established:

- Uzbek hybrid/RAG systems exist, particularly in legal retrieval;
- ontology/reranking and semantic retrieval are already part of national work.

Important distinction:

- RAG answer accuracy or Citation Accuracy cannot automatically be interpreted as pure retrieval effectiveness.

### 2.8 Sharifbaev 2026 dissertation manuscript

**Reliability:** D until official final/defense evidence is verified.

The analyzed manuscript describes:

- 1,197 Uzbek/Russian parliamentary/legal documents;
- lemmatized BM25 in Elasticsearch;
- LaBSE dense retrieval in Milvus;
- graph retrieval in Neo4j;
- adaptive GraphRAG-RL selection among lexical/vector/graph retrieval;
- expert query scenarios and a 300-query final test table.

If officially verified, this closes broad claims that Uzbek lacks:

- morphology-aware BM25 + dense retrieval;
- hybrid retrieval;
- query-dependent strategy selection.

But it still does not isolate:

`BM25_raw ↔ BM25_stem ↔ BM25_lemma`

or explain how morphology changes lexical–dense overlap/unique-hit structure.

See:

`literature/deep-dives/2026_Sharifbaev_Uzbek_Legal_Hybrid_Retrieval_Manuscript.md`.

---

## 3. International gap-killer boundary

### 3.1 Can et al. (2008), Turkish

Already established:

- morphology can materially affect lexical retrieval in an agglutinative Turkic language;
- query length changes the observed morphology effect;
- more sophisticated linguistic normalization does not automatically guarantee better retrieval.

Does not include BM25/dense/hybrid in the modern sense.

### 3.2 Haddad & Bechikh Ali (2014), Turkish

Already established:

- BM25 is directly affected by Turkish preprocessing/stemming choices;
- simple fixed-prefix normalization can remain competitive with morphology-aware processing;
- preprocessing effect depends on retrieval model/configuration.

Does not include modern dense or lexical–semantic hybrid retrieval.

### 3.3 Kazi & Khoja — UPERF (PACLIC 2024), Urdu

**Reliability:** B.

Key boundary evidence:

- 2,887,169-document Urdu corpus;
- raw/stemmed/lemmatized preprocessing;
- BM25, TF-IDF, Word2Vec, FastText, Doc2Vec, mBERT;
- single-word vs multiple-word queries;
- weighted lexical–semantic combination;
- Recall@5 evaluation.

Critical consequence:

- the project cannot claim that raw/stem/lemma has never been studied together with lexical and semantic representations in a morphologically complex low-resource language.

Residual:

- no modern retrieval-trained dense retriever;
- no fixed-dense morphology-conditioned overlap/unique-hit decomposition;
- no systematic morphology × hybrid-gain interaction analysis.

See:

`literature/deep-dives/2024_Kazi_Khoja_UPERF_Urdu_Retrieval.md`.

### 3.4 Kazi & Khoja — U-RR² (Computer Speech & Language, 2026), Urdu

**Reliability:** A.

Key boundary evidence:

- journal-level Urdu document retrieval;
- three benchmark collections (CURE, ROSHNI, UIR-21);
- BM25/DFR/Jelinek-Mercer/VSM and embedding representations;
- two-stage retrieval + SVMrank learned reranking;
- strong lexical–semantic feature integration.

Residual:

- the current verified record does not establish a clean `raw/stem/lemma × fixed modern dense × complementarity` experiment;
- it is primarily a learned feature/reranking framework rather than a controlled morphology-induced complementarity decomposition.

Official DOI: `10.1016/j.csl.2025.101797`.

### 3.5 Aboasal et al. (2026), Arabic legal IR

**Reliability:** B.

Official abstract establishes:

- 500 legal articles + 1,000 synthetic QA pairs;
- BM25;
- Farasa morphology;
- Ada v3, BGE-M3, GTE, Mistral-embed;
- BM25 MAP 0.7178 → 0.7715 with Farasa;
- Mistral-embed MAP 0.7570, nDCG@10 0.7964;
- BM25(Farasa)+Ada v3 hybrid MAP 0.8304, nDCG@10 0.8626.

Critical consequence:

- morphology-aware BM25 + modern semantic embeddings + hybrid retrieval is already studied globally.

Residual:

- no verified `raw/stem/lemma` three-way controlled lexical matrix;
- no verified same-dense comparison across morphology variants;
- no unique-hit/overlap/oracle decomposition;
- no systematic morphology-conditioned query analysis.

See:

`literature/deep-dives/2026_Aboasal_Arabic_Legal_IR_Morphology_Semantic.md`.

### 3.6 Munetsi, Mukande & O'Connor (SIGIR 2026), Shona

**Reliability:** A.

Verified SIGIR paper:

- low-resource Shona IR;
- sparse and dense retrieval models;
- morphology identified as a direct retrieval challenge;
- evidence that modern IR research already treats morphology-sensitive retrieval behavior as a low-resource problem.

Critical consequence:

- “morphology-aware low-resource retrieval” is not itself a novel research direction.

Residual:

- the paper is a preliminary study and does not provide the complete `raw/stem/lemma × fixed dense × complementarity decomposition` required by the current Uzbek gap.

DOI: `10.1145/3805712.3808522`.

### 3.7 GreekBarRetrieval (Beta et al., 2026)

**Reliability:** C as of 2026-09-10 (arXiv preprint).

This is the strongest current global gap-killer found.

Primary arXiv evidence:

- 283 Greek bar-exam questions;
- 6,308 candidate statutory articles;
- three BM25 variants;
- nine dense retrievers;
- sparse–dense fusion;
- LLM query reformulation;
- nDCG/MAP/Recall evaluation.

Detailed paper extraction identifies morphology-related BM25 variants based on:

- Greek stemming;
- spaCy lemmatization;
- tokenization/minimal normalization.

Critical consequence:

- even the experimental matrix `different BM25 morphology pipelines + modern dense retrievers + fusion` already exists.

Residual:

- no verified full factorial test that holds the same dense retriever/fusion fixed while changing only the lexical morphology representation;
- no systematic relevant-set overlap/unique-hit/oracle-union decomposition for each morphology variant;
- no Uzbek morphology/script-specific interaction analysis.

See:

`literature/deep-dives/2026_Beta_GreekBarRetrieval.md`.

---

## 4. Claim-status matrix after the 2026-09-10 search

| Candidate novelty/gap claim | Status |
|---|---|
| Uzbek hybrid retrieval is absent | **REJECTED** |
| Uzbek semantic retrieval is absent | **REJECTED** |
| Morphology has not been applied to Uzbek search | **REJECTED** |
| Raw/stem/lemma has not been compared in low-resource IR | **REJECTED** |
| Morphology-aware BM25 is unstudied | **REJECTED** |
| Morphology-aware BM25 has not been compared with modern embeddings | **REJECTED** |
| Morphology-aware lexical + semantic hybrid retrieval is unstudied | **REJECTED** |
| Query-dependent hybrid retrieval is new | **REJECTED** |
| Query-type lexical/dense analysis is new | **REJECTED** |
| Complementarity itself is a new research concept | **REJECTED** |
| For Uzbek, morphology-induced change in lexical–dense complementarity is established | **NOT FOUND** |
| `BM25_raw/stem/lemma + same dense` with controlled fusion and overlap decomposition for Uzbek | **NOT FOUND** |
| Unique relevant hits / overlap / oracle union as morphology changes for Uzbek | **NOT FOUND** |
| Morphology/script-aware query factors explaining that interaction for Uzbek | **NOT FOUND** |

---

## 5. Current gap — v0.8 refined

The current working gap is:

> **Несмотря на то что в современных исследованиях морфологически богатых языков уже одновременно сравниваются различные варианты морфологической обработки лексического поиска, современные модели плотного поиска и способы их гибридного использования, недостаточно установлено, как изменение морфологического представления лексического канала изменяет саму структуру его взаимодополняемости с семантическим поиском. Для узбекского языка, в частности, не установлено в единой контролируемой задаче ранжирования документов, как переход от исходных словоформ к стеммам и леммам изменяет набор уникально найденных релевантных документов, степень перекрытия с фиксированной моделью плотного поиска и дополнительный эффект гибридного поиска, а также как эти изменения связаны с морфологическими, графическими и лексико-структурными характеристиками запросов.**

This formulation remains **provisional**, not final novelty.

---

## 6. Experimental implications if the gap is retained

The minimum controlled family should be:

### Lexical representation

`BM25_raw`
`BM25_stem`
`BM25_lemma`

Potential additional control:

`BM25_simple-normalization`.

### Fixed semantic comparator

Choose at least one modern retrieval-trained multilingual dense retriever `D` and hold it constant when attributing morphology effects.

A second modern dense model may be used for robustness, but the primary interaction analysis must not change dense model and morphology at the same time.

### Hybrid conditions

`H_raw = fusion(BM25_raw, D)`
`H_stem = fusion(BM25_stem, D)`
`H_lemma = fusion(BM25_lemma, D)`.

Fusion/normalization settings must be held constant or tuned under a controlled validation protocol.

### Main explanatory measurements

For each query and each morphology condition:

- lexical retrieval effectiveness;
- semantic retrieval effectiveness;
- hybrid effectiveness;
- unique relevant lexical hits;
- unique relevant semantic hits;
- relevant-set overlap;
- oracle union/upper bound;
- incremental hybrid gain;
- statistical comparison across queries.

### Candidate Uzbek query factors

- number/type of affixal forms;
- morphological complexity;
- rare terms;
- named entities;
- numbers/identifiers;
- Latin/Cyrillic variation;
- apostrophe/Unicode variation where relevant;
- query length;
- lexical overlap;
- paraphrastic/descriptive formulation;
- domain.

These are candidate explanatory factors, not predetermined causes.

---

## 7. Search stopping rule reached

The 2026-09-10 aggressive gap-killer search reached provisional saturation:

- new studies increasingly reproduce already occupied components;
- GreekBarRetrieval is the closest current global analogue found;
- no direct verified work was found that closes the exact interaction/decomposition question for Uzbek.

Broad generic searching should now give way to:

1. targeted verification of direct gap killers;
2. monitoring of very recent 2026 publications;
3. research-question/hypothesis formulation;
4. benchmark/qrels design;
5. baseline experiments that test whether the proposed interaction exists at all.

If baseline experiments show that morphology does **not** change lexical–semantic complementarity in a meaningful/reproducible way, the gap and hypothesis must be revised again.

---

## 8. Evidence hierarchy warnings

- **Sharifbaev manuscript:** D until official defense/final publication is verified.
- **GreekBarRetrieval:** C until peer-reviewed publication status is verified.
- **Aboasal et al.:** B; current project analysis relies primarily on verified official abstract/metadata, so methods not exposed there must not be invented.
- **UPERF:** B; full paper inspected, but evaluation is largely Recall@5 and statistical significance is not clearly specified.
- **Kazi & Khoja 2026:** A; strong journal boundary evidence, but does not by itself establish the current morphology-induced complementarity interaction.
- **Munetsi et al. 2026:** A; SIGIR evidence that morphology-aware low-resource IR is already an active research direction.
