# Literature Master Index

**Status:** working master index updated through 2026-09-15.
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
| PHD-INT-001 | Sheng-Chieh Lin — *Building a Robust Retrieval System with Dense Retrieval Models* (Waterloo) — [deep dive](deep-dives/2024_Sheng_Chieh_Lin_PhD_Robust_Dense_Retrieval.md) | 2024 | Dense robustness, lexical-semantic integration | A | CRITICAL | Deep dive COMPLETED 2026-09-15. Main structural PhD anchor: problem → evidence of limitation → controlled experiment → method only if justified. Dense transfer requires Uzbek pilot/dev validation before selecting and freezing D. |
| PHD-INT-002 | Minghan Li — *Pretrained Transformers for Efficient and Robust Information Retrieval* (Waterloo) | 2024 | Dense/sparse/hybrid/multi-vector robustness | A | VERY HIGH | Architecture taxonomy, representation limitations |
| PHD-INT-003 | Georgios Sidiropoulos — *Improving the Robustness and Effectiveness of Neural Retrievers in Noisy and Low-Resource Settings* (UvA) | 2025 | Low-resource neural retrieval | A | VERY HIGH | Low-resource framing |
| PHD-UZ-001 | I. I. Bakaev — *Models and Algorithms of Morphological Analysis of Uzbek Word Forms* — [deep dive](deep-dives/2021_Bakaev_Uzbek_Morphology_Search.md) | 2021 | Uzbek morphology and search applications | A | CRITICAL | Defended PhD; Morphoanalyzer and full-text/library deployment; analyzer accuracy and workflow gains are not qrels-based IR effectiveness. |
| PHD-UZ-002 | Kh. I. Akhmedova — semantic analysis of Uzbek sentences, specialty 05.01.10 | 2023 | Uzbek semantic processing | A | HIGH | National semantic-processing anchor |
| PHD-UZ-003 | Z. Y. Xusainova — tokenization/stemming/lemmatization of Uzbek units — [deep dive](deep-dives/2024_Xusainova_Uzbek_Tokenization_Stemming_Lemmatization.md) | 2024 | Uzbek preprocessing/search optimization | A | CRITICAL | Defended PhD; BPE/tokenizer, UzbStemmer and lemmatizer; reported 97.5% is stemmer/analyzer accuracy, not retrieval effectiveness. |
| PHD-UZ-004 | Botir B. Elov — NLP-based automatic analysis and processing of Uzbek texts — [deep dive](deep-dives/2026_Elov_Uzbek_NLP_Morphology_Information_System.md) | 2026 | Integrated Uzbek NLP and search-oriented indexing | A | CRITICAL | Officially defended DSc, 2026-02-05; supplied manuscript dated 2025. Morphology/syntax/semantics integration is not lexical+dense IR fusion; module metrics and corpus-scale inconsistencies require context. |

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
| MORPH-004 | Munetsi, Mukande, O'Connor — *Morphology-Aware Retrieval for Low-Resource Environments: Advancing Information Retrieval for Shona Language* (SIGIR 2026) — [deep dive](deep-dives/2026_Munetsi_Mukande_OConnor_Shona_Morphology_Aware_IR.md) | 2026 | A | CRITICAL | Deep dive COMPLETED 2026-09-15. Peer-reviewed 4-page preliminary Shona IR study: BM25 / ColBERT-v2 / dense comparison, morphology-sensitive failure analysis and proposed future morphology-aware benchmark. No implemented raw/stem/lemma comparison or BM25+dense fusion in the main table; shallow top-10 pooling limits Recall/unique-hit/oracle-union evidence. |
| MORPH-UZ-001 | Bakaev & Shafiev — full-text search with morphology — [deep dive](deep-dives/2021_Bakaev_Uzbek_Morphology_Search.md) | 2020 | B | HIGH | Stemmer + lemmatizer with term/field-weighted ranking; qualitative search examples, no BM25 or qrels-based IR evaluation. |
| MORPH-UZ-002 | Bakaev PhD — [deep dive](deep-dives/2021_Bakaev_Uzbek_Morphology_Search.md) | 2021 | A | CRITICAL | Morphoanalyzer; genre-specific base-identification accuracy and real National Library deployment. The 9–11% catalog workflow/productivity gain is not retrieval effectiveness; no raw/stem/lemma × dense benchmark. |
| MORPH-UZ-003 | Xusainova — lemmatization for Uzbek National Corpus search — [deep dive](deep-dives/2024_Xusainova_Uzbek_Tokenization_Stemming_Lemmatization.md) | 2023 | B/A- | HIGH | Lemmatization/search optimization evidence; related PhD's 97.5% measures stemmer/analyzer accuracy, not retrieval effectiveness. No controlled BM25/qrels benchmark; SEO != ad-hoc IR. |
| MORPH-UZ-004 | Xusainova PhD — [deep dive](deep-dives/2024_Xusainova_Uzbek_Tokenization_Stemming_Lemmatization.md) | 2024 | A | CRITICAL | BPE/tokenizer, UzbStemmer, lemmatizer; >100k sentences and reported 97.5% analyzer accuracy; >32k simple + >7.5k compound lexemes. No controlled raw/stem/lemma BM25 IR. |
| MORPH-UZ-005 | Elov, Xusainova, Berdieva — Uzbek stemming/morphological issues | 2023 | B | MEDIUM | Phonetic/morphological stemming complications |
| MORPH-UZ-006 | IL-402104209 morpholexicon/morphological analyzer project | 2022–2024 | B | HIGH | Official Uzbek NLP/IR morphology project |
| MORPH-UZ-007 | Elov DSc — morphology/normalization/indexing — [deep dive](deep-dives/2026_Elov_Uzbek_NLP_Morphology_Information_System.md) | 2026 | A | CRITICAL | Hybrid morphology, lemma-based inverted indexing and UzNLP; SQL Server full-text / Elasticsearch are infrastructure, not proof of a BM25+dense benchmark. NLP accuracy/F1 != MAP/nDCG/Recall; preserve differing evaluation and corpus-count contexts. |
| MORPH-UZ-008 | Turayev B.Sh. — candidate PhD, Uzbek morphosyntactic analysis — [deep dive](deep-dives/2026_Turayev_Uzbek_Morphosyntactic_Neural_Analysis.md) | 2026 | B pending final-defense verification | HIGH | TUIT seminar 2026-07-11; 32,225 base forms and explicit lemmatization; MaxEnt+BiLSTM+CRF / RNN+CYK. Registration B2025.3.PhD/T5887 conflicts with another OAK dissertation; National Library document workflow is not an IR benchmark. |
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
| UZ-SEM-008 | Axmedova X.X. — Uzbek paraphrasing and semantic matching — [deep dive](deep-dives/2026_Axmedova_Uzbek_Paraphrase_Semantic_Matching.md) | 2026 | B pending final-defense protocol verification | HIGH | Multilingual E5 + cosine matching, Jina-assisted candidate selection, Gemma3 paraphrasing; dataset/result descriptions remain unreconciled. **Paraphrase/semantic matching != corpus-level retrieval.** |
| UZ-SEM-009 | Abdisalomova Sh.A. — Uzbek coreference / UzCoref — [deep dive](deep-dives/2026_Abdisalomova_Uzbek_Coreference_UzCoref.md) | 2026 | B pending final-defense verification | MEDIUM | Expert-corrected CoNLL-style corpus: 1,020 documents, ~320k tokens, 18,451 mentions, 5,326 chains; hybrid coreference and UzRoBERTa. **Coreference and search-related deployment != retrieval evaluation.** |
| UZ-NLP-001 | Allanazarova S.Y. — sentiment / SentiUzNet — [deep dive](deep-dives/2026_Allanazarova_Uzbek_Sentiment_SentiUzNet.md) | 2026 | B pending final-defense verification | LOW / background | 3,336 synsets, six annotators, κ=0.79; 384k+ comments, reported 91% sentiment accuracy. **Sentiment classification/resource hybridization != lexical+dense retrieval.** |

---

## F. Hybrid retrieval — international

| ID | Work | Year | Reliability | Priority | What it contributes |
|---|---|---:|---|---|---|
| HYB-001 | Cormack, Clarke, Büttcher — RRF | 2009 | A | VERY HIGH | Rank fusion baseline |
| HYB-002 | Luan et al. — *Sparse, Dense, and Attentional Representations for Text Retrieval* | 2021 | A | VERY HIGH | Sparse/dense complementarity, fusion |
| HYB-003 | Gao et al. — CLEAR — [deep dive](deep-dives/2021_Gao_CLEAR_Semantic_Residual_Embeddings.md) | 2021 | A | CRITICAL | Deep dive COMPLETED 2026-09-15. Training-level complementarity: dense semantic residual learns to correct BM25 errors. Generic complementarity-aware training is occupied; no morphology-induced complementarity experiment. |
| HYB-004 | Kuzi et al. — semantic + lexical matching | 2020 | B/C | MEDIUM | Hybrid ad-hoc retrieval analysis |
| HYB-005 | Bruch, Gai, Ingber — *An Analysis of Fusion Functions for Hybrid Retrieval* — [deep dive](deep-dives/2023_Bruch_Gai_Ingber_Fusion_Functions_Hybrid_Retrieval.md) | 2023 | A | CRITICAL | Deep dive COMPLETED 2026-09-15. Normalized convex fusion, sample-efficient global alpha tuning, RRF parameter/transfer sensitivity; candidate-union coverage != fusion ranking. Primary morphology comparison should fix D, alpha, normalization and depth k. ACM: August 2023; Volume 42(1) is indexed as 2024 in some records. |
| HYB-006 | Lin & Lin — Dense Representation Framework / DHR — [deep dive](deep-dives/2023_Lin_Lin_Dense_Representation_Framework_DHR.md) | 2023 | A | CRITICAL | Deep dive COMPLETED 2026-09-15. Unified lexical–semantic representation and joint training already exist; dense representation != semantic matching. Define D as a fixed retrieval-trained semantic dense retriever; no raw/stem/lemma intervention. |
| HYB-007 | Chen et al. — BGE-M3 / M3-Embedding — [deep dive](deep-dives/2024_Chen_BGE_M3_Embedding.md) | 2024 | A | CRITICAL | Deep dive COMPLETED 2026-09-15. Unified multilingual dense / learned sparse / multi-vector retrieval with joint training. Dense-only is a candidate D requiring Uzbek validation; no Uzbek retrieval evaluation in the paper. All adds sparse/multi-vector signals and is unsuitable as the primary causal comparator; BM25 preprocessing must be controlled. |
| HYB-008 | Arabzadeh, Yan, Clarke — query-based sparse/dense/hybrid strategy selection | 2021 | A | VERY HIGH | Query-dependent strategy already exists |
| HYB-009 | Posokhov et al. — Query-Adaptive Hybrid Search — [deep dive](deep-dives/2026_Posokhov_Query_Adaptive_Hybrid_Search.md) | 2026 | A | CRITICAL | Deep dive COMPLETED 2026-09-15. Query-Driven Alpha Prediction, dynamic alpha(q) and dense training on BM25 failures already exist. No raw/stem/lemma × same fixed D or morphology-conditioned unique-hit/overlap/oracle-union analysis. |
| HYB-010 | Kazi & Khoja — *Towards building Urdu language document retrieval framework* (*Computer Speech & Language*) | 2026 | A | CRITICAL | Multi-benchmark Urdu retrieval with lexical/statistical models, embedding features and SVMrank learned reranking. Strong low-resource lexical–semantic integration evidence; no verified full morphology × fixed-modern-dense complementarity decomposition. |
| HYB-011 | Aboasal et al. — *Arabic Legal Information Retrieval: The Impact of Morphological Segmentation and Semantic Embeddings* — [deep dive](deep-dives/2026_Aboasal_Arabic_Legal_IR_Morphology_Semantic.md) | 2026 | B | CRITICAL | Farasa morphology + BM25 + modern embeddings (including BGE-M3/GTE/Ada/Mistral-embed) + hybrid legal retrieval. Kills broad morphology-aware BM25 + modern semantic + hybrid novelty claims; does not isolate morphology-induced complementarity structure. |
| HYB-012 | Beta et al. — *GreekBarRetrieval: A Benchmark for Greek Statutory Retrieval* — [deep dive](deep-dives/2026_Beta_GreekBarRetrieval.md) | 2026 | C | CRITICAL | Preprint with three BM25 morphology/preprocessing variants, nine modern dense retrievers, fusion and query reformulation. Closest global gap killer found; no verified full unique-hit/overlap/oracle decomposition across morphology variants with the same dense comparator. |

---

## G. Uzbek retrieval / hybrid / RAG

| ID | Work | Year | Reliability | Priority | Current interpretation |
|---|---|---:|---|---|---|
| UZ-IR-001 | Ishkobilov et al. — *Semantic Retrieval of Uzbek Seismic Safety Regulations* (*Vibroengineering Procedia* 63, 227–231) — [deep dive](deep-dives/2026_Ishkobilov_Uzbek_Seismic_Semantic_Retrieval.md) | 2026 | B | CRITICAL | Verified-abstract deep dive; project record: 120 docs, 8,450 paragraphs, 100 queries. TF-IDF P@5/R@5 = 0.6017/0.5418; FastText = 0.7444/0.6875. Paired t=15.1372, p<0.001 reported, but tested quantity/assumptions unclear; exact MAP/MRR and F1 use/value need full text. No BM25, morphology intervention, fusion or complementarity decomposition. |
| UZ-IR-002 | Aslantaş & Gungor — SIGTURK Turkic Idiom benchmark | 2026 | A | VERY HIGH | Uzbek semantic retrieval exists, but specialized idiom task |
| UZ-IR-003 | Urinov — BM25 vs vector search in Uzbek RAG — [deep dive](deep-dives/2025_Urinov_Uzbek_RAG_BM25_Vector_Search.md) | 2025 | C | MEDIUM | BM25-like vs semantic vector comparison verified at Zenodo metadata/abstract level, DOI 10.5281/zenodo.17341315. Venue, dataset/qrels/metrics/vector model and genuine hybrid fusion remain unverified. |
| UZ-HYB-001 | Absalamova, Muminov, Absalamova — USHRA legal chatbot — [deep dive](deep-dives/2025_Absalamova_Muminov_Absalamova_USHRA_Uzbek_Legal_RAG.md) | 2025 | B | CRITICAL | Verified ACM ICFNDS ’25, pp. 1036–1042, DOI 10.1145/3789692.3789825; multilingual embeddings + RAG + Lex.uz + named USHRA. 85% chatbot answer accuracy on 200 criminal-law queries, **not retrieval accuracy**; exact lexical/dense/fusion components and pure IR metrics unverified. |
| UZ-HYB-002 | Absalamova, Muminov, Absalamova — O-RAG — [deep dive](deep-dives/2025_Absalamova_Muminov_Absalamova_O_RAG_Uzbek_Legal_Ontology.md) | 2025 | B | CRITICAL | Verified ACM ICFNDS ’25, pp. 680–687, DOI 10.1145/3789692.3789782; custom legal ontology + hybrid retrieval + ontology-based reranking, Lex.uz QA data. Hit Rate / Citation Accuracy improvement at abstract level; exact lexical/dense/fusion components and metric values unverified. Gains cannot be assigned to fusion without ablation. |
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

### National deep dives completed 2026-09-11–2026-09-14

Cards are linked in the corresponding rows above; repeated structural/morphology IDs refer to the same card.

- **Bakaev / Xusainova / Elov:** A-level defended work; morphology/search infrastructure, with explicit analyzer/deployment versus IR boundaries.
- **Turayev / Axmedova / Abdisalomova / Allanazarova:** completed supplied-source analyses; B pending final-defense verification (Axmedova: final protocol; Turayev: registration conflict). Paraphrase, coreference and sentiment remain separate from corpus IR.
- **Ishkobilov:** B; verified-abstract retrieval deep dive completed; full-paper protocol/metric details remain open.
- **USHRA / O-RAG:** 2025, B; bibliographic/verified-abstract deep dives completed; full-text methods and evaluation verification remain open.
- **Urinov:** C; verified-metadata/abstract deep dive completed; full-text venue/protocol/fusion verification remains open.

Synthesis: [National evidence matrix, 2026-09-14](../research/NATIONAL_EVIDENCE_MATRIX_2026-09-14.md). These additions strengthen the boundary without changing `v0.8 refined`.

### International deep dives completed 2026-09-15

**HYB-009, HYB-003, HYB-006, HYB-007, PHD-INT-001, MORPH-004 and HYB-005 — COMPLETED.** Cards and evidence limits are linked in the rows above. This substantially completes the targeted international wave; `v0.8 refined` remains unchanged. Benchmark/qrels and Uzbek dense pilot validation are the immediate bottleneck.

## Critical first wave — remaining deep dives

1. UZ-SEM-007 — morphology-oriented Uzbek STS

Targeted follow-up verification for completed national cards is tracked in [OPEN_QUESTIONS](../research/OPEN_QUESTIONS.md).

## Second wave

- Minghan Li PhD
- Sidiropoulos PhD
- DPR
- ColBERT
- ANCE
- Contriever
- EntityQuestions
- SIGTURK Uzbek retrieval
- BERTbek / SimRelUz / UZWORDNET.

---

# Citation metadata warnings

1. USHRA and O-RAG are verified ACM ICFNDS ’25 papers with publication year **2025**; secondary 2026 appearance/indexing dates do not change that year. Morphology-oriented STS metadata remains to be verified separately against the official ACM record.
2. UzBERT/Uzbek embeddings may remain preprints; do not silently upgrade their evidence level.
3. For national PhDs use official OAK/university metadata where possible.
4. For any strong numerical claim, verify primary/full text before putting it into final dissertation.
5. Bruch, Gai & Ingber, DOI `10.1145/3596512`: use **2023**, following the official ACM publication date **August 2023**; some indexes associate Volume 42(1) with **2024**. Retain this discrepancy note when preparing the final bibliography.
