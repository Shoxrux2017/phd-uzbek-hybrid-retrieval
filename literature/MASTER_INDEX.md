# Literature Master Index

**Status:** working master index updated through 2026-09-10.
This is not the final bibliography. It is a research navigation index.

Legend:

- **A** strong primary/official evidence.
- **B** useful verified evidence with narrower scope.
- **C** preprint/model/dataset/infrastructure evidence.
- **D** unverified; not citable as established result.
- Deep-dive priority: `CRITICAL`, `VERY HIGH`, `HIGH`, `MEDIUM`, `LOW`.

---

## A. Structural PhD references

| ID | Work | Year | Focus | Reliability | Priority | Current role |
|---|---|---:|---|---|---|---|
| PHD-INT-001 | Sheng-Chieh Lin — *Building a Robust Retrieval System with Dense Retrieval Models* (Waterloo) | 2024 | Dense robustness, lexical-semantic integration | A | CRITICAL | Main modern IR PhD structural/reference anchor |
| PHD-INT-002 | Minghan Li — *Pretrained Transformers for Efficient and Robust Information Retrieval* (Waterloo) | 2024 | Dense/sparse/hybrid/multi-vector robustness | A | VERY HIGH | Architecture taxonomy, representation limitations |
| PHD-INT-003 | Georgios Sidiropoulos — *Improving the Robustness and Effectiveness of Neural Retrievers in Noisy and Low-Resource Settings* (UvA) | 2025 | Low-resource neural retrieval | A | VERY HIGH | Low-resource framing |
| PHD-UZ-001 | I. I. Bakaev — *Models and Algorithms of Morphological Analysis of Uzbek Word Forms* | 2021 | Uzbek morphology and search applications | A | CRITICAL | National morphology/IR anchor |
| PHD-UZ-002 | Kh. I. Akhmedova — semantic analysis of Uzbek sentences, specialty 05.01.10 | 2023 | Uzbek semantic processing | A | HIGH | National semantic-processing anchor |
| PHD-UZ-003 | Z. Y. Xusainova — tokenization/stemming/lemmatization of Uzbek units | 2024 | Uzbek preprocessing/search optimization | A | CRITICAL | Morphology preprocessing anchor |

---

## B. Lexical information retrieval

| ID | Work | Year | Reliability | Priority | What it contributes |
|---|---|---:|---|---|---|
| LEX-001 | Manning, Raghavan, Schütze — *Introduction to Information Retrieval* | 2008 | A- | MEDIUM | Standard IR definitions/indexing background |
| LEX-002 | Salton, Wong, Yang — *A Vector Space Model for Automatic Indexing* | 1975 | A | MEDIUM | VSM foundation |
| LEX-003 | Spärck Jones — *A Statistical Interpretation of Term Specificity...* | 1972 | A | MEDIUM | IDF/term specificity |
| LEX-004 | Robertson et al. — *Okapi at TREC-3* | 1994 | A | MEDIUM | Historical BM25 development |
| LEX-005 | Robertson & Zaragoza — *The Probabilistic Relevance Framework: BM25 and Beyond* | 2009 | A | VERY HIGH | Main BM25 theoretical source |
| LEX-006 | Trotman, Puurula, Burgess — *Improvements to BM25 and Language Models Examined* | 2014 | A | MEDIUM | BM25 variants / stemming evidence |
| LEX-007 | Furnas et al. — *The Vocabulary Problem in Human-System Communication* | 1987 | A | HIGH | Empirical vocabulary mismatch foundation |
| LEX-008 | Thakur et al. — BEIR | 2021 | A | VERY HIGH | BM25 as robust heterogeneous zero-shot baseline |
| LEX-009 | Mallia et al. — DeepImpact | 2021 | A | HIGH | Learned sparse term impacts |
| LEX-010 | Formal, Piwowarski, Clinchant — SPLADE | 2021 | A | HIGH | Learned sparse/expansion |
| LEX-011 | Lin & Ma — conceptual sparse/dense learned framework notes | 2021 | B/C | MEDIUM | `sparse != non-neural` classification |

---

## C. Morphology / Turkic / Uzbek lexical processing

| ID | Work | Year | Reliability | Priority | What it contributes |
|---|---|---:|---|---|---|
| MORPH-001 | Can et al. — *Information Retrieval on Turkish Texts* (JASIST) — [deep dive](deep-dives/2008_Can_Information_Retrieval_on_Turkish_Texts.md) | 2008 | A | CRITICAL | Deep dive completed 2026-09-02. Large Turkic/agglutinative IR study: morphology improves lexical retrieval in the tested setting; query length changes the observed stemming effect; elaborate lemmatization does not guarantee superiority; **BM25, semantic and hybrid retrieval were not evaluated**. |
| MORPH-002 | Haddad & Bechikh Ali — *Performance of Turkish Information Retrieval: Evaluating the Impact of Linguistic Parameters and Compound Nouns* (CICLing/LNCS) — [deep dive](deep-dives/2014_Haddad_Bechikh_Ali_Performance_of_Turkish_IR.md) | 2014 | B | VERY HIGH | Deep dive completed 2026-09-04. Same Milliyet collection, now with TF-IDF, **BM25** and a classical language-model retrieval formulation. Zemberek gives the strongest BM25 MAP/bpref among the tested preprocessing configurations, while simple 4/5-prefix truncation remains highly competitive. Stop-word effects are small; compound-noun effects depend on model/configuration. **No paired significance test was reported; no semantic or hybrid retrieval was evaluated.** |
| MORPH-003 | Kazi & Khoja — *UPERF: Urdu Proximity Enhanced Retrieval Framework* (PACLIC 2024) — [deep dive](deep-dives/2024_Kazi_Khoja_UPERF_Urdu_Retrieval.md) | 2024 | B | CRITICAL | Controlled Urdu document retrieval with raw/stemmed/lemmatized preprocessing across BM25, TF-IDF and embedding-based representations; query-type and weighted lexical–semantic combination evidence. No modern retrieval-trained dense comparator or morphology-conditioned overlap/unique-hit decomposition. |
| MORPH-004 | Munetsi, Mukande, O'Connor — *Morphology-Aware Retrieval for Low-Resource Environments: Advancing Information Retrieval for Shona Language* (SIGIR 2026) | 2026 | A | CRITICAL | A-level evidence that morphology-aware low-resource IR is already a direct modern research line with BM25 and neural retrieval comparators. Does not close the controlled raw/stem/lemma × fixed-dense complementarity question. |
| MORPH-UZ-001 | Bakaev & Shafiev — full-text search with morphology | 2020 | B | HIGH | Direct Uzbek morphology/search link |
| MORPH-UZ-002 | Bakaev PhD | 2021 | A | CRITICAL | Uzbek morphological analyzer and search applications |
| MORPH-UZ-003 | Xusainova — lemmatization for Uzbek National Corpus search | 2023 | B/A- | HIGH | Lemmatization/search optimization |
| MORPH-UZ-004 | Xusainova PhD | 2024 | A | CRITICAL | Tokenizer/stemmer/lemmatizer |
| MORPH-UZ-005 | Elov, Xusainova, Berdieva — Uzbek stemming/morphological issues | 2023 | B | MEDIUM | Phonetic/morphological stemming complications |
| MORPH-UZ-006 | IL-402104209 morpholexicon/morphological analyzer project | 2022–2024 | B | HIGH | Official Uzbek NLP/IR morphology project |
| SCRIPT-UZ-001 | Mansurov & Mansurov — Uzbek Cyrillic-Latin transliteration using MT | 2021 | C/B | MEDIUM | Script normalization |
| SCRIPT-UZ-002 | Salaev et al. — automatic Uzbek writing-system transliteration | 2022 | B/C | MEDIUM | Script normalization |

---

## D. Semantic representations and retrieval

| ID | Work | Year | Reliability | Priority | What it contributes |
|---|---|---:|---|---|---|
| SEM-001 | Deerwester et al. — LSI/LSA | 1990 | A | LOW/MEDIUM | Historical latent semantics |
| SEM-002 | Mikolov et al. — Word2Vec | 2013 | A | MEDIUM | Distributed word vectors |
| SEM-003 | Bojanowski et al. — FastText subword vectors | 2017 | A | HIGH | Subword representations, morphology relevance |
| SEM-004 | Devlin et al. — BERT | 2019 | A | HIGH | Contextual representation |
| SEM-005 | Reimers & Gurevych — Sentence-BERT | 2019 | A | HIGH | Efficient semantic embeddings / bi-encoder style |
| SEM-006 | Nogueira & Cho — BERT passage reranking | 2019 | B/A- | HIGH | Cross-encoder reranking |
| SEM-007 | Karpukhin et al. — DPR | 2020 | A | CRITICAL | Dense bi-encoder first-stage retrieval |
| SEM-008 | Xiong et al. — ANCE | 2021 | A | VERY HIGH | Hard-negative dense retrieval training |
| SEM-009 | Khattab & Zaharia — ColBERT | 2020 | A | CRITICAL | Late interaction / multi-vector |
| SEM-010 | Izacard et al. — Contriever | 2022 | A | VERY HIGH | Unsupervised/multilingual dense retrieval |
| SEM-011 | Wang et al. — Multilingual E5 | 2024 | B/C | HIGH | Modern multilingual embedding baseline |
| SEM-012 | Zhang et al. — MIRACL | 2023 | A | VERY HIGH | Multilingual ad-hoc retrieval benchmark; Uzbek absent |
| SEM-013 | Sciavolino et al. — EntityQuestions | 2021 | A | CRITICAL | Dense weakness on rare/entity-centric queries |
| SEM-014 | Dense retrieval survey, ACM TOIS | 2024 | A | HIGH | Systematic dense limitations |

---

## E. Uzbek semantic infrastructure

| ID | Work | Year | Reliability | Priority | What it contributes / warning |
|---|---|---:|---|---|---|
| UZ-SEM-001 | Mansurov & Mansurov — Uzbek Word2Vec/GloVe/FastText | 2020 | C/B | HIGH | Uzbek word vectors; **not IR evaluation** |
| UZ-SEM-002 | Agostini et al. — UZWORDNET | 2021 | A | HIGH | 28,140 synsets; lexical-semantic resource; **not retriever** |
| UZ-SEM-003 | Mansurov & Mansurov — UzBERT | 2021 | C/B | HIGH | Uzbek contextual LM; MLM eval; **not retriever** |
| UZ-SEM-004 | Salaev, Kuriyozov, Gómez-Rodríguez — SimRelUz | 2022 | A | VERY HIGH | >1000 word pairs, 11 speakers; **not document retrieval** |
| UZ-SEM-005 | Akhmedova PhD | 2023 | A | HIGH | Uzbek sentence semantic analysis; **not dense IR** |
| UZ-SEM-006 | Kuriyozov, Vilares, Gómez-Rodríguez — BERTbek | 2024 | A | VERY HIGH | Uzbek LM; sentiment/topic/NER; **not retrieval** |
| UZ-SEM-007 | Muminov & Allaberganova — morphology-oriented Uzbek STS | 2025/2026 metadata to verify | A-/B+ | CRITICAL | Morphology + semantic dual encoder exists; **STS != IR** |

---

## F. Hybrid retrieval — international

| ID | Work | Year | Reliability | Priority | What it contributes |
|---|---|---:|---|---|---|
| HYB-001 | Cormack, Clarke, Büttcher — RRF | 2009 | A | VERY HIGH | Rank fusion baseline |
| HYB-002 | Luan et al. — *Sparse, Dense, and Attentional Representations for Text Retrieval* | 2021 | A | VERY HIGH | Sparse/dense complementarity, fusion |
| HYB-003 | Gao et al. — CLEAR | 2021 | A | CRITICAL | Learned semantic residual complementarity |
| HYB-004 | Kuzi et al. — semantic + lexical matching | 2020 | B/C | MEDIUM | Hybrid ad-hoc retrieval analysis |
| HYB-005 | Bruch, Gai, Ingber — *Analysis of Fusion Functions for Hybrid Retrieval* | 2024 | A | CRITICAL | Score fusion vs RRF, normalization/transfer |
| HYB-006 | Lin & Lin — Dense Representation Framework / DHR | 2023 | A | CRITICAL | Representation-level lexical-semantic integration |
| HYB-007 | Chen et al. — BGE-M3 / M3-Embedding | 2024 | A | CRITICAL | Dense+sparse+multi-vector unified model |
| HYB-008 | Arabzadeh, Yan, Clarke — query-based sparse/dense/hybrid strategy selection | 2021 | A | VERY HIGH | Query-dependent strategy already exists |
| HYB-009 | Posokhov et al. — Query-Adaptive Hybrid Search | 2026 | A | CRITICAL | Dynamic `alpha(q)` already exists |
| HYB-010 | Kazi & Khoja — *Towards building Urdu language document retrieval framework* (*Computer Speech & Language*) | 2026 | A | CRITICAL | Multi-benchmark Urdu retrieval with lexical/statistical models, embedding features and SVMrank learned reranking. Strong low-resource lexical–semantic integration evidence; no verified full morphology × fixed-modern-dense complementarity decomposition. |
| HYB-011 | Aboasal et al. — *Arabic Legal Information Retrieval: The Impact of Morphological Segmentation and Semantic Embeddings* — [deep dive](deep-dives/2026_Aboasal_Arabic_Legal_IR_Morphology_Semantic.md) | 2026 | B | CRITICAL | Farasa morphology + BM25 + modern embeddings (including BGE-M3/GTE/Ada/Mistral-embed) + hybrid legal retrieval. Kills broad morphology-aware BM25 + modern semantic + hybrid novelty claims; does not isolate morphology-induced complementarity structure. |
| HYB-012 | Beta et al. — *GreekBarRetrieval: A Benchmark for Greek Statutory Retrieval* — [deep dive](deep-dives/2026_Beta_GreekBarRetrieval.md) | 2026 | C | CRITICAL | Preprint with three BM25 morphology/preprocessing variants, nine modern dense retrievers, fusion and query reformulation. Closest global gap killer found; no verified full unique-hit/overlap/oracle decomposition across morphology variants with the same dense comparator. |

---

## G. Uzbek retrieval / hybrid / RAG

| ID | Work | Year | Reliability | Priority | Current interpretation |
|---|---|---:|---|---|---|
| UZ-IR-001 | Ishkobilov et al. — *Semantic Retrieval of Uzbek Seismic Safety Regulations* | 2026 | B/A- | CRITICAL | 120 docs, 8,450 paragraphs, 100 queries; TF-IDF vs FastText; P@5/R@5/MAP/MRR/F1; comparison not fusion |
| UZ-IR-002 | Aslantaş & Gungor — SIGTURK Turkic Idiom benchmark | 2026 | A | VERY HIGH | Uzbek semantic retrieval exists, but specialized idiom task |
| UZ-IR-003 | Urinov — BM25 vs vector search in Uzbek RAG | 2025 | C/B | MEDIUM | Comparison, not systematic hybrid fusion |
| UZ-HYB-001 | Absalamova, Muminov, Absalamova — USHRA legal chatbot | 2025/2026 metadata verify | A-/B+ | CRITICAL | Uzbek hybrid/RAG exists; reported 85% answer accuracy/200 criminal-law queries; fusion details need full text |
| UZ-HYB-002 | Absalamova et al. — O-RAG | 2025/2026 metadata verify | A-/B+ | CRITICAL | Hybrid + legal ontology + ontological reranking; domain-specific |
| UZ-RAG-003 | Umarova — Uzbek legal QA architecture | 2025/2026 | B/C | MEDIUM | BM25/dense/Transformer/rule components; verify experimental depth |

---

## H. Unverified / do not cite as evidence

| ID | Work | Reliability | Status |
|---|---|---|---|
| UNVER-001 | *Context-Aware Hybrid BM25–BERT Retrieval for Uzbek Legal Texts* (Scribd manuscript) | D | Keep only as literature-search lead; no reliable publication record confirmed |
| UNVER-002 | Sharifbaev A. N. — 2026 Uzbek/Russian legal hybrid-retrieval dissertation manuscript — [targeted analysis](deep-dives/2026_Sharifbaev_Uzbek_Legal_Hybrid_Retrieval_Manuscript.md) | D | CRITICAL lead only: manuscript describes lemmatized BM25 + LaBSE + graph retrieval + adaptive controller, but official final/defense status is unverified and the manuscript contains unresolved placeholders/internal inconsistencies. |

---

# Deep-dive order recommended

## Completed deep dives

- **MORPH-001 — Can et al. (2008), *Information Retrieval on Turkish Texts*.** Deep dive completed 2026-09-02: [card](deep-dives/2008_Can_Information_Retrieval_on_Turkish_Texts.md).
  - Main retained conclusion: do not assume `lemma > stem > raw` for Uzbek retrieval; measure it.
  - Query length already interacts with the effect of morphological normalization in lexical IR.
  - The paper does not test BM25, semantic retrieval or hybrid retrieval, so it does not close the current Uzbek lexical–semantic gap.

- **MORPH-002 — Haddad & Bechikh Ali (2014), *Performance of Turkish Information Retrieval: Evaluating the Impact of Linguistic Parameters and Compound Nouns*.** Deep dive completed 2026-09-04: [card](deep-dives/2014_Haddad_Bechikh_Ali_Performance_of_Turkish_IR.md).
  - Directly extends the Milliyet evidence to BM25.
  - Zemberek is the strongest tested BM25 configuration by MAP/bpref, but 4/5-prefix truncation remains competitive and no paired significance test establishes universal superiority.
  - Preprocessing effects depend on the retrieval model and evaluation metric.
  - The work remains lexical IR: it does not test modern semantic retrieval or lexical–semantic hybrid integration.

- **MORPH-003 — Kazi & Khoja (2024), *UPERF: Urdu Proximity Enhanced Retrieval Framework*.** Targeted deep dive completed 2026-09-10: [card](deep-dives/2024_Kazi_Khoja_UPERF_Urdu_Retrieval.md).
  - Raw/stemmed/lemmatized preprocessing is already tested across lexical and embedding-based retrieval in low-resource Urdu.
  - Weighted lexical–semantic combination does not automatically beat the strongest standalone component.
  - No modern retrieval-trained dense comparator and no systematic morphology-conditioned overlap/unique-hit decomposition.

- **HYB-011 — Aboasal et al. (2026), *Arabic Legal Information Retrieval: The Impact of Morphological Segmentation and Semantic Embeddings*.** Targeted gap analysis completed 2026-09-10: [card](deep-dives/2026_Aboasal_Arabic_Legal_IR_Morphology_Semantic.md).
  - Morphology-aware BM25, modern semantic embeddings and hybrid retrieval already coexist in one Arabic legal IR study.
  - The available verified record does not establish a raw/stem/lemma × same-dense interaction or a complementarity decomposition.

- **HYB-012 — Beta et al. (2026), *GreekBarRetrieval*.** Targeted gap analysis completed 2026-09-10: [card](deep-dives/2026_Beta_GreekBarRetrieval.md).
  - Multiple BM25 morphology/preprocessing variants, modern dense retrievers, fusion and query reformulation are already evaluated in one statutory-retrieval benchmark.
  - This kills novelty based on the experimental component list itself; the surviving gap is the morphology-induced change in lexical–dense complementarity.
  - Reliability remains C while only the preprint status is verified.

- **UNVER-002 — Sharifbaev A. N. (2026), Uzbek/Russian legal hybrid-retrieval dissertation manuscript.** Targeted manuscript analysis completed 2026-09-10: [card](deep-dives/2026_Sharifbaev_Uzbek_Legal_Hybrid_Retrieval_Manuscript.md).
  - Describes lemmatized BM25 + LaBSE + graph retrieval + adaptive control on parliamentary/legal data.
  - It is highly relevant to gap boundaries but remains D-level until an official final/defense record is verified.

## Critical first wave

1. UZ-HYB-001 — USHRA
2. UZ-HYB-002 — O-RAG
3. HYB-009 — Query-Adaptive Hybrid Search
4. HYB-003 — CLEAR
5. HYB-006 — DHR / Lin & Lin
6. HYB-007 — BGE-M3
7. PHD-INT-001 — Sheng-Chieh Lin PhD
8. PHD-UZ-001 — Bakaev PhD
9. PHD-UZ-003 — Xusainova PhD
10. UZ-IR-001 — Ishkobilov et al.
11. UZ-SEM-007 — morphology-oriented Uzbek STS

## Second wave

- Minghan Li PhD
- Sidiropoulos PhD
- DPR
- ColBERT
- ANCE
- Contriever
- EntityQuestions
- Bruch fusion analysis
- SIGTURK Uzbek retrieval
- BERTbek / SimRelUz / UZWORDNET.

---

# Citation metadata warnings

1. ICFNDS proceedings branded `'25` may have publication pages/metadata dated 2026. For USHRA/O-RAG/morphology-oriented STS use official ACM record before final bibliography.
2. UzBERT/Uzbek embeddings may remain preprints; do not silently upgrade their evidence level.
3. For national PhDs use official OAK/university metadata where possible.
4. For any strong numerical claim, verify primary/full text before putting it into final dissertation.
