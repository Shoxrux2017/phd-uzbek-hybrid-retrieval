# Research Map

**Purpose:** сквозная карта того, что уже изучено и как отдельные линии связаны с текущей PhD.
**Evidence cut-off:** 2026-09-15.

---

# 1. Structural PhD references

Эти работы используются не только как источники фактов, но и как образцы того, **как строится первая глава и исследовательская аргументация**.

## 1.1 Sheng-Chieh Lin, PhD, University of Waterloo, 2024

**Topic:** robust dense retrieval; lexical–semantic matching/fusion.

Что важно:

- BM25 рассматривается как реальный сильный first-stage lexical retriever, а не «устаревшая модель».
- Dense retrieval вводится как способ преодолеть term mismatch.
- Затем анализируются ограничения dense retrieval: robustness, data/resources, transfer.
- Lexical + semantic integration становится ответом на выявленную проблему, а не случайным дополнительным experiment.
- Полезна для структуры: `problem → limitation → method → evidence`.

**Deep dive priority:** very high.

## 1.2 Minghan Li, PhD, University of Waterloo, 2024

**Topic:** pretrained Transformers for efficient and robust IR.

Важно:

- чёткое разделение sparse, dense, hybrid, multi-vector, cross-encoder stages;
- pretrained representation рассматривается как lossy: возможно недостаточное сохранение fine-grained details;
- хороший ориентир для классификации современных retrievers.

**Deep dive priority:** very high.

## 1.3 Georgios Sidiropoulos, PhD, University of Amsterdam, 2025

**Topic:** robustness/effectiveness of neural retrievers in noisy and low-resource settings.

Важно:

- low-resource problem рассматривается как самостоятельная research problem;
- показывает, что neural retrieval нельзя оценивать только in-domain;
- полезен для Uzbek low-resource framing.

**Deep dive priority:** high.

## 1.4 I. I. Bakaev, PhD, Uzbekistan, 2021

**Topic:** models and algorithms for morphological analysis of Uzbek word forms.
**Status:** defended PhD, A; [deep dive completed 2026-09-11](../literature/deep-dives/2021_Bakaev_Uzbek_Morphology_Search.md).

Важно:

- официально подтверждённая защищённая национальная PhD;
- первая глава построена как theory → critical analysis → comparison → international/domestic work → gaps → tasks;
- morphology напрямую связана с обработкой Uzbek search queries и практическими library systems;
- результаты внедрения нельзя автоматически считать modern qrels-based IR benchmark.

Morphoanalyzer, genre-specific base correctness and full-text/library deployment are detailed in section 3.2; practical deployment does not establish qrels-based retrieval effectiveness.

## 1.5 Kh. I. Akhmedova, PhD, Uzbekistan, 2023

**Topic:** models/algorithms/information system for semantic analysis of Uzbek sentences; specialty 05.01.10.

Важно:

- подтверждает национальное развитие semantic processing;
- не является dense query–document retrieval;
- структурный ориентир: global methods → Uzbek context → own model.

**Deep dive priority:** high.

## 1.6 Z. Y. Xusainova, PhD, Uzbekistan, 2024

**Topic:** tokenization, stemming, lemmatization of Uzbek units and software.
**Status:** defended PhD, A; [deep dive completed 2026-09-11](../literature/deep-dives/2024_Xusainova_Uzbek_Tokenization_Stemming_Lemmatization.md).

Важно:

- BPE/tokenizer, UzbStemmer и lemmatizer для Uzbek corpus/search;
- reported 97.5% is stemmer/analyzer accuracy, not retrieval effectiveness;
- search/corpus optimization is documented, but no controlled BM25/qrels/raw-stem-lemma retrieval benchmark is established; details in section 3.2.

## 1.7 Botir B. Elov, DSc, Uzbekistan, defended 2026

**Topic:** NLP-based automatic analysis and processing of Uzbek texts.
**Status:** officially defended DSc on **2026-02-05**, A; [deep dive completed 2026-09-11](../literature/deep-dives/2026_Elov_Uzbek_NLP_Morphology_Information_System.md).

- The supplied 387-page manuscript is dated **2025**; project chronology uses **2026** for the defended DSc.
- Integrated UzNLP covers morphology, POS, syntax, semantic roles and NER, with normalization and lemma-based indexing for search applications.
- This is an A-level national structural/infrastructure reference; integration of NLP modules is not lexical+dense retrieval fusion.
- Section 3.2 preserves the separate module-result and corpus-scale cautions; module accuracy/F1 is not IR effectiveness.

---

# 2. Lexical retrieval landscape

## 2.1 Foundations

Ключевые линии:

- Salton et al. — Vector Space Model.
- Spärck Jones — term specificity / IDF.
- Robertson & Zaragoza — Probabilistic Relevance Framework / BM25.
- Furnas et al. — vocabulary problem.

### Established

- lexical retrieval — не literal substring search;
- term matches имеют неодинаковую информативность;
- BM25 моделирует term specificity, TF saturation, document length;
- vocabulary mismatch фундаментально ограничивает surface lexical matching.

## 2.2 BM25 remains a strong baseline

BEIR (Thakur et al., 2021):

- BM25 остаётся robust zero-shot baseline across heterogeneous datasets;
- более сложная neural model не гарантирует universal superiority.

### Safe claim

> BM25 сохраняет значение сильной базовой модели; это не означает, что BM25 всегда лучше dense retrieval.

## 2.3 Learned sparse retrieval

DeepImpact, SPLADE и related work показывают:

- `neural != dense`;
- sparse representation может быть learned;
- learned sparse может выполнять expansion/learned term weighting;
- нельзя писать «lexical = старое; semantic/neural = новое».

---

# 3. Morphology and lexical retrieval

## 3.1 Turkic comparative evidence

### Can et al. — *Information Retrieval on Turkish Texts* (JASIST, 2008)

**Deep dive:** completed 2026-09-02.
**Card:** [`literature/deep-dives/2008_Can_Information_Retrieval_on_Turkish_Texts.md`](../literature/deep-dives/2008_Can_Information_Retrieval_on_Turkish_Texts.md)

Experimental setting:

- 408,305 Turkish newspaper documents (Milliyet, 2001–2005);
- approximately 95.5 million tokens before stop-word removal;
- 72 ad-hoc queries after filtering;
- 33 native-speaker assessors;
- binary relevance judgments built with pooling;
- pool construction used 24 runs: 8 matching functions × NS/F6/SV;
- evaluation included `bpref`, MAP and precision at fixed cutoffs;
- eight vector-space query–document matching functions were tested.

Morphological variants:

- **NS** — no stemming;
- **F3–F7** — fixed-prefix truncation;
- **SV** — successor-variety statistical stemming;
- **LM5/LM6** — lemmatizer-based variants;
- **LV** — LM5 with SV fallback for words not analyzed by the lemmatizer.

Established results relevant to the current PhD:

- morphological normalization substantially improved lexical retrieval relative to NS in this collection;
- with the best reported matching function (MF8), `bpref` was 0.3255 for NS, 0.4322 for F5, 0.4304 for SV and 0.4504 for LV;
- F5, SV and LV were significantly better than NS in the key MF8 comparison (`p < 0.001`);
- the numerically better LV did **not** show a statistically significant per-query advantage over F5 in the key MF8 comparison; therefore, a more linguistically elaborate lemmatizer does not automatically guarantee better retrieval effectiveness;
- query length changes the observed effect: moving from short to medium queries significantly improved F5/LV, while longer queries partly compensated for the absence of stemming in NS;
- stop-word removal did not produce a statistically significant effectiveness gain in the authors' tested ranking setting;
- normalization greatly reduced vocabulary/posting-list size, so morphology can affect both effectiveness and index efficiency.

Critical limitations:

- the study evaluates Turkish, not Uzbek;
- the domain is one newspaper collection;
- **BM25 is not evaluated**;
- no modern dense semantic retriever is evaluated;
- no lexical–semantic hybrid retrieval is evaluated;
- relevance judgments are incomplete and depend on pooling; F5 and LV were not among the systems used to build the original pool;
- the study does not establish that its optimal prefix lengths or morphology choices transfer to Uzbek.

### Consequence for Uzbek retrieval

Для Uzbek нельзя заранее предполагать:

`lemma BM25 > stem BM25 > raw BM25`.

Это должно измеряться в контролируемой постановке с одной и той же моделью BM25:

`BM25_raw ↔ BM25_stem ↔ BM25_lemma`.

После этого необходимо отдельно проверить, меняет ли морфологическая нормализация взаимодополняемость с современным семантическим поиском:

`Semantic ↔ BM25_raw + Semantic ↔ BM25_stem + Semantic ↔ BM25_lemma + Semantic`.

Результаты следует анализировать не только в среднем, но и по характеристикам запросов. Can et al. уже дают прямое свидетельство, что **длина запроса** может менять наблюдаемый эффект морфологической обработки в лексическом поиске. Это поддерживает текущий research gap, но не закрывает его.

### Haddad & Bechikh Ali — *Performance of Turkish Information Retrieval: Evaluating the Impact of Linguistic Parameters and Compound Nouns* (CICLing 2014)

**Deep dive:** completed 2026-09-04.
**Card:** [`literature/deep-dives/2014_Haddad_Bechikh_Ali_Performance_of_Turkish_IR.md`](../literature/deep-dives/2014_Haddad_Bechikh_Ali_Performance_of_Turkish_IR.md)

This work directly extends the Milliyet evidence from Can et al. to BM25 and a broader set of linguistic preprocessing choices.

Experimental setting:

- same Milliyet Turkish news collection: 408,305 articles/columns, 2001–2005, about 800 MB and 95.5 million words before stop-word removal;
- incomplete relevance judgments created with pooling and binary judgments by 33 native-speaker assessors;
- Terrier IR framework;
- three lexical/statistical retrieval models: TF-IDF, BM25 and a classical language-model retrieval formulation;
- evaluation: P@5, P@10, P@15, 11pt-avg, MAP and `bpref`;
- `bpref` is treated as especially appropriate because judgments are incomplete.

Preprocessing and representation variants:

- baseline with no stemming and no stop-word removal;
- 223-word Turkish stop list;
- structured indexing/querying using `HEADLINE + TEXT` and `title + description`;
- fixed-prefix truncation: 3-prefix, 4-prefix, 5-prefix;
- Snowball stemming;
- Zemberek morphology-aware/root-dictionary stemming;
- compound-noun candidates extracted with Zemberek POS tags and three patterns: `Noun+Noun`, `Noun+Adjective`, `Adjective+Noun`;
- compound nouns are added in addition to ordinary keyword terms.

Key BM25 results:

| Configuration | MAP | bpref |
|---|---:|---:|
| Baseline | 0.2522 | 0.4041 |
| Stop words | 0.2567 | 0.4081 |
| Structure | 0.3149 | 0.4039 |
| Structure + stop words | 0.3186 | 0.4075 |
| 3-prefix | 0.1989 | 0.3634 |
| 4-prefix | 0.3213 | 0.4462 |
| 5-prefix | 0.3396 | 0.4439 |
| Snowball | 0.2865 | 0.4104 |
| **Zemberek** | **0.3440** | **0.4603** |
| Compound nouns (CN) | 0.2310 | 0.4144 |
| CN + structure | 0.2971 | 0.4372 |
| CN + structure + `ignore.low.idf` | 0.3030 | 0.4472 |

Established conclusions relevant to the current PhD:

- the same preprocessing choice can affect TF-IDF, BM25 and the classical language-model retrieval formulation differently;
- BM25 is the strongest baseline among the three models in the unprocessed configuration;
- 3-prefix truncation is too aggressive for BM25 in this setting and degrades both MAP and `bpref`;
- 4/5-prefix truncation yields large gains over raw BM25 and remains highly competitive with the more linguistically elaborate Zemberek configuration;
- Zemberek gives the strongest reported BM25 MAP and `bpref` among the tested preprocessing variants;
- Snowball yields only a small `bpref` gain over raw BM25 and is clearly below 4/5-prefix and Zemberek in this collection;
- stop-word removal produces only small changes;
- document/query structure improves some metrics strongly (especially MAP) but the authors themselves describe the effect as partly inherent to the test collection;
- compound-noun indexing is not universally beneficial; its effect depends on retrieval model, metric and configuration;
- the classical language-model retrieval formulation is more sensitive than TF-IDF/BM25 to added linguistic analysis in several compound-noun configurations.

Critical methodological cautions:

- the paper states that stop words have no significant influence, but **no paired t-test is reported**; the authors explicitly list paired t-testing as future work;
- the paper attributes Zemberek's advantage over Snowball to its root-dictionary-based processing, but no ablation isolates the dictionary contribution from other implementation/morphological differences;
- although Zemberek is numerically stronger overall than fixed-prefix truncation, the work does not statistically establish universal superiority of morphology-aware stemming;
- both this paper and Can et al. use the same Milliyet collection, so the agreement between 4/5-prefix results is not an independent cross-dataset replication;
- the work evaluates classical lexical/statistical retrieval only: no modern dense semantic retriever and no lexical–semantic hybrid retrieval are tested.

### Consequence for Uzbek retrieval

The combined Can et al. + Haddad & Bechikh Ali evidence strengthens the need for a controlled Uzbek lexical baseline family rather than assuming that linguistic sophistication determines retrieval quality:

`BM25_raw ↔ BM25_simple-normalization ↔ BM25_stem ↔ BM25_lemma`.

A simple fixed-prefix or other low-cost normalization can be useful as a control baseline even if it is not linguistically correct, because the Turkish evidence shows that simple normalization can remain surprisingly competitive.

Only after establishing the lexical variants should the current PhD test how each one interacts with the same semantic retriever:

`Semantic ↔ BM25_raw + Semantic ↔ BM25_stem + Semantic ↔ BM25_lemma + Semantic`.

The paper therefore **supports the current gap but does not narrow or close it**: it says nothing about Uzbek, modern semantic retrieval, or how morphology changes lexical–semantic complementarity.


## 3.2 Uzbek morphology research

### Bakaev — defended PhD, A

[Completed deep dive](../literature/deep-dives/2021_Bakaev_Uzbek_Morphology_Search.md): Morphoanalyzer combines tokenization, normalization, morphemic analysis and grammatical tagging, with web-service/API integration.

The author abstract reports **base-identification correctness** by genre:

| Genre | Words | Correct bases |
|---|---:|---:|
| Fairy tales | 1,246 | 96% |
| Legal documents | 1,290 | 92.4% |
| Hadiths | 1,285 | 88.9% |
| Uzbek proverbs | 1,200 | 94% |

The later 2022 paper reports 91.3% for religious works; its comparability with the 88.9% hadith result is not established. These are analyzer results, not retrieval metrics.

The related 2020 Bakaev–Shafiev full-text search paper uses **stemmer + lemmatizer**, with term/field weighting for ranking; it does not use BM25 or report a query/qrels benchmark. Deployment in library systems, including the National Library of Uzbekistan, is documented. The reported **9–11% reduction in time/labor** concerns bibliographic-description/catalog workflows, **not retrieval-effectiveness gain**. National Library search-relevance improvement is a qualitative deployment claim without MAP/nDCG/Recall evidence.

### Xusainova — defended PhD, A

[Completed deep dive](../literature/deep-dives/2024_Xusainova_Uzbek_Tokenization_Stemming_Lemmatization.md): BPE/tokenizer, UzbStemmer and lemmatizer; affix rules, morpholexicon, roots/stems and POS information support normalization.

- UzbStemmer was applied to **more than 100,000 sentences**, with reported **97.5% stemmer/analyzer accuracy**.
- Implementation evidence reports **more than 32,000 simple + more than 7,500 compound lexical units**.
- National Corpus and platform search optimization are reported, but no BM25, qrels or controlled raw/stem/lemma retrieval benchmark is established.
- Part of the search-optimization discussion concerns **SEO**, which is not ad-hoc IR evaluation.

### Elov — officially defended DSc, A

[Completed full-manuscript deep dive](../literature/deep-dives/2026_Elov_Uzbek_NLP_Morphology_Information_System.md): hybrid rule/FST + statistical/neural morphology, orthographic/script normalization, contextual disambiguation, lemma/POS/features, stop-word filtering and UzWordNet synonym mapping feed lemma-based inverted indexing and integrated UzNLP.

SQL Server full-text search and Elasticsearch are named **infrastructure**; they do not establish a controlled BM25 or lexical+dense retrieval experiment.

Numerical cautions from the card:

- The morphology comparison reports **94% complete-analysis accuracy / 92% F1**; a later integrated-system table reports **96.4% accuracy / 96.5% F1**. The source does not reconcile the evaluation conditions; do not merge them or interpret them as IR effectiveness.
- Approximately **38M tagged words**, a particular **80k/20k train/test-word** setup and a **5k-word morphology test** refer to different reported contexts.
- The headline **~50 billion sentences / ~380M words** is internally implausible as written; a later implementation section reports **~124M tokens / ~2.5M unique lemmas**. Corpus scale must be checked against final/official resource documentation before citation; these counts do not describe one verified IR benchmark.

### Turayev — B pending final-defense verification

[Completed supplied-abstract deep dive](../literature/deep-dives/2026_Turayev_Uzbek_Morphosyntactic_Neural_Analysis.md): TUIT seminar verified **2026-07-11**; final defense remains unverified.

- **32k+ base forms** (table: **32,225**) and explicit lemmatization;
- **MaxEnt+BiLSTM+CRF** POS/morphology line and **RNN+CYK** syntactic-analysis line;
- National Library implementation concerns document/speech input and syntactic editing workflows, not search ranking or a retrieval benchmark;
- registration **B2025.3.PhD/T5887** conflicts with another dissertation in the OAK index, and final-defense fields are blank; no A-level structural upgrade is justified;
- large corpus counts and the use of generation-overlap metrics in POS/syntactic tables require full-source clarification; none are qrels-based IR evidence.

### National project IL-402104209

Morpholexicon and morphological analyzer for IR/NLP systems; the completed national cards connect this project to existing morphology infrastructure.

### Established

- morphology relevant for Uzbek search;
- national infrastructure exists.
- morphology preprocessing is a lexical-representation variant, not an independent third retrieval paradigm.

### Not established yet

- comparative modern BM25/raw/stem/lemma evaluation with public qrels/MAP/nDCG;
- effect on complementarity with modern dense retriever.

## 3.3 Script variation

Uzbek digital texts coexist in Latin/Cyrillic forms.

Relevant transliteration work exists.

### Consequence

Lexical preprocessing may need:

- Unicode/apostrophe normalization;
- Latin/Cyrillic normalization/transliteration;
- morphology normalization.

But script normalization must not be conflated with semantic matching.

---

# 4. Semantic retrieval landscape

## 4.1 Evolution of representations

Conceptual line:

`LSI → static embeddings → contextual BERT → retrieval architectures`.

Important: chapter should not become a historical textbook. The key question is how representation becomes query–document retrieval.

## 4.2 Cross-encoder

- joint query-document processing;
- strong pairwise interaction;
- usually reranking, not scalable full-corpus first-stage retrieval.

## 4.3 Bi-encoder / dense retrieval

DPR:

- independent query/document encoding;
- pre-indexable documents;
- demonstrates strong first-stage retrieval in open-domain QA;
- 9–19 absolute points top-20 passage retrieval improvement over the used BM25 baseline in those QA settings.

### Not a universal claim

DPR does **not** prove dense > BM25 for all IR tasks.

## 4.4 Training matters

ANCE:

- hard negatives matter;
- retrieval performance depends on training regime.

Contriever:

- unsupervised contrastive retrieval;
- reduces dependence on large labelled retrieval datasets;
- relevant to low-resource transfer.

## 4.5 Late interaction

ColBERT:

- multi-vector token-level representations;
- late interaction;
- compromise between cross-encoder interaction and bi-encoder scalability.

## 4.6 Dense limitations

EntityQuestions (Sciavolino et al.):

- dense retrievers can underperform sparse methods on rare/entity-centric queries.

### Consequence

Dense retrieval is not universal replacement for lexical retrieval.

---

# 5. Uzbek semantic infrastructure

## 5.1 Uzbek word embeddings

Mansurov & Mansurov:

- Word2Vec/GloVe/FastText;
- infrastructure for distributed representations;
- not retrieval evaluation.

## 5.2 UZWORDNET

- lexical-semantic database;
- 28,140 synsets;
- 64,389 senses;
- 20,683 words.

Important:

`WordNet != retriever`.

## 5.3 UzBERT

- monolingual Uzbek BERT;
- MLM evaluation;
- not direct retrieval evaluation.

## 5.4 BERTbek

- monolingual Uzbek Transformer;
- evaluated on sentiment, topic classification, NER;
- not direct query-document retrieval.

## 5.5 SimRelUz

- >1000 word pairs;
- 11 native speakers;
- similarity/relatedness evaluation;
- not document retrieval.

## 5.6 Akhmedova PhD

- semantic analysis of Uzbek sentences;
- important national semantic-processing line;
- not dense retrieval.

## 5.7 Morphology-oriented Uzbek STS

Muminov & Allaberganova:

- morphology-oriented dual encoder;
- Transformer semantic channel + morphological channel;
- Uzbek STS;
- demonstrates that `morphology + semantic representation` is already researched.

Important:

`STS != IR`.

Full publication metadata/year must be verified against official ACM record because conference branding/aggregators differ.

## 5.8 Axmedova X.X. — paraphrase / semantic matching, 2026

**Status:** B pending final-defense protocol verification; [deep dive completed 2026-09-11](../literature/deep-dives/2026_Axmedova_Uzbek_Paraphrase_Semantic_Matching.md). TUIT seminar 2026-06-24 and OAK defense announcement 2026-07-23 are verified; the final outcome is not.

- **Multilingual E5 + cosine similarity** identifies semantic duplicates/paraphrases among sentences in uploaded documents.
- **Jina embeddings** assist candidate selection from Uzbek news texts; independent human validation of the full resource is not clearly documented.
- A **Gemma3-4B-PT-based** model is fine-tuned for paraphrase generation.
- The **250K pairs / 5K test sentences / 88.3% accuracy** description is not reconciled with the **375K triplets / 91.3% accuracy / F1 0.954** description. Preserve their separate contexts and verify splits/leakage before reuse.

This is modern Uzbek semantic matching, but **paraphrase/semantic similarity != corpus-level IR**, and use of an embedding family does not by itself establish a retriever.

## 5.9 Abdisalomova Sh.A. — coreference / UzCoref, 2026

**Status:** B pending final-defense verification; [deep dive completed 2026-09-11](../literature/deep-dives/2026_Abdisalomova_Uzbek_Coreference_UzCoref.md). Official registration/discussion evidence exists; the supplied abstract has blank final-defense fields.

- **1,020 documents**, approximately **320k tokens**, **18,451 mentions**, **5,326 chains**; 820/100/100 train/validation/test documents.
- Automatic pre-annotation followed by expert checking/correction under **CoNLL-style** conventions.
- Hybrid rule+ML+neural coreference reports **CoNLL F1 64.3**; the separate **UzRoBERTa** comparison reports **67.8**. Prose values of ~68/70% are not fully reconciled; do not collapse them into a single UzCoref score.
- Search-related platform deployment is reported, but there is no verified before/after qrels benchmark attributing retrieval gain to coreference.

**Coreference resolves references within a text; it is not query-document retrieval.** Hybrid coreference is not lexical+dense fusion.

## 5.10 Allanazarova S.Y. — SentiUzNet background, 2026

**B pending final-defense verification; LOW/background.** [Completed deep dive](../literature/deep-dives/2026_Allanazarova_Uzbek_Sentiment_SentiUzNet.md): **3,336 synsets**, six annotators, reported mean Cohen's **κ=0.79**; **384k+ comments**, reported **91% sentiment accuracy**. The 397,227 merged-review pool is a separate reported count. “Hybrid” describes resource/classification construction, **not lexical+dense retrieval**; sentiment accuracy is not retrieval effectiveness.

---

# 6. Uzbek semantic retrieval — 2026 update

## 6.1 Ishkobilov et al., Semantic Retrieval of Uzbek Seismic Safety Regulations

**Status:** B, CRITICAL; [verified-abstract deep dive completed 2026-09-14](../literature/deep-dives/2026_Ishkobilov_Uzbek_Seismic_Semantic_Retrieval.md).
**Verified publication:** *Vibroengineering Procedia*, vol. 63 (2026), pp. 227–231, published 2026-07-16.

Project record: **120 documents, 8,450 indexed paragraphs, 100 domain queries**. The publisher abstract independently confirms the specialized seismic/engineering corpus, paragraph retrieval and 100 queries; exact document/paragraph counts and qrels construction still need the full paper.

Verified publisher-abstract results:

| Model | P@5 | R@5 |
|---|---:|---:|
| TF-IDF | 0.6017 | 0.5418 |
| FastText | 0.7444 | 0.6875 |

MAP and MRR are named and improvement is reported, but their exact values were not recovered. F1 is present in the prior project record; its use, definition and value require full-text verification.

The authors report a **paired t-test, t=15.1372, p<0.001**. The abstract does not identify the exact per-query quantity tested, assumption checks or multiple-testing treatment; do not infer those details.

Important consequence:

> Нельзя утверждать, что Uzbek corpus-level semantic retrieval со стандартными IR-метриками отсутствует.

Limitations relevant to current PhD:

- specialized seismic/engineering domain and incompletely documented relevance judgments;
- TF-IDF vs FastText comparison, not fusion;
- static/subword FastText representation, not a modern retrieval-trained Transformer dense retriever;
- no BM25, controlled raw/stem/lemma intervention, hybrid fusion or complementarity decomposition.

## 6.2 SIGTURK 2026 Turkic Idiom Benchmark

Aslantaş & Gungor:

- five Turkic languages including Uzbek;
- semantic retrieval task;
- multiple embedding models;
- dense retrieval metrics.

Important:

- Uzbek semantic retrieval exists in benchmark setting;
- task is specialized idiom-to-meaning retrieval, not general document retrieval.

## 6.3 Urinov — BM25-like vs vector search in Uzbek RAG, 2025

**Status:** C, MEDIUM supporting evidence; [metadata/abstract-level deep dive completed 2026-09-14](../literature/deep-dives/2025_Urinov_Uzbek_RAG_BM25_Vector_Search.md).
**Zenodo DOI:** `10.5281/zenodo.17341315`; repository date 2025-10-13, resource type “Conference paper”; underlying venue/peer review unverified.

The abstract verifies comparison of **BM25-like traditional retrieval vs semantic vector search** in Uzbek RAG, with qualitative efficiency/contextual-meaning claims. Corpus, queries/qrels, standard metric values, BM25 parameters and exact vector model are not verified. A “hybrid” keyword does not establish genuine fusion: **BM25 vs vector comparison != BM25 + vector fusion**.

---

# 7. Hybrid retrieval — international

## 7.1 Score-level fusion

Typical form:

`S_hybrid = alpha * S_lex + (1-alpha) * S_sem`.

Issue:

- BM25 and dense similarity have different scales;
- normalization/calibration matters.

Luan et al.:

- sparse/dense representations are complementary.

Bruch et al.:

- systematic analysis of fusion functions;
- convex combination vs RRF;
- in their experiments learned convex combination can outperform RRF.

## 7.2 Rank-level fusion

RRF (Cormack et al., SIGIR 2009):

- combines rankings, not score scales;
- no score normalization required;
- loses information about magnitude of original score differences.

Important:

RRF = strong baseline, **not novelty**.

## 7.3 Learned complementarity

CLEAR:

- semantic residual component is trained to complement lexical retrieval;
- hybrid research question becomes not only `how to combine`, but `what additional evidence should the second model learn`.

**Deep dive priority:** very high.

## 7.4 Representation-level integration

Lin & Lin DLR/DHR:

- Dense Lexical Representation;
- Dense Hybrid Representation;
- integration happens at representation level, not only post-hoc fusion.

**Deep dive priority:** very high.

## 7.5 Unified multi-function retrieval

BGE-M3:

- dense;
- sparse;
- multi-vector;
- multilingual.

Important:

BGE-M3 should not be described as identical to DHR. It is a unified multi-function model, not necessarily one identical hybrid representation.

**Deep dive priority:** very high.

## 7.6 Query-dependent/adaptive retrieval

Arabzadeh et al., CIKM 2021:

- per-query selection between sparse/dense/hybrid strategy.

Query-Adaptive Hybrid Search, 2026:

- Query-Driven Alpha Prediction;
- dynamic `alpha(q)`;
- therefore dynamic per-query weighting itself is not a new idea.

**Deep dive priority:** very high.

---

# 8. Uzbek hybrid retrieval / RAG

## 8.1 USHRA

**Diyora Absalamova, Bahodir Muminov, Gozal Absalamova.** *Developing A Semantic Search-Based Chatbot For Legal Queries In Uzbek Language Using Big Data Resources*. **ACM ICFNDS ’25, 2025, pp. 1036–1042; DOI `10.1145/3789692.3789825`.**
**Status:** B, CRITICAL; [bibliographic/verified-abstract deep dive completed 2026-09-14](../literature/deep-dives/2025_Absalamova_Muminov_Absalamova_USHRA_Uzbek_Legal_RAG.md). Secondary 2026 appearance dates do not change the publication year.

Verified at abstract level:

- Uzbek legal queries;
- Lex.uz;
- multilingual embeddings;
- RAG;
- authors call their method `Uzbek-Specific Hybrid Semantic Retrieval Algorithm`;
- reported **85% chatbot answer accuracy on 200 criminal-law queries**.

Important limitations of current knowledge:

- exact lexical model, fusion mechanism, index/database and embedding checkpoint remain unverified;
- **85% answer accuracy != 85% retrieval accuracy**; generation/context/prompt effects are not isolated;
- qrels, pure IR metrics, detailed baselines and statistical evidence need full-text verification.

Therefore:

- **cannot say Uzbek hybrid search does not exist**;
- **cannot yet classify USHRA confidently as score fusion/RRF/etc.**

**Remaining work:** full-text verification; do not assign a specific fusion formula from the algorithm name alone.

## 8.2 O-RAG

**Diyora Absalamova, Bahodir Muminov, Gozal Absalamova.** *O-Rag Ontology-Enhanced Retrieval-Augmented Generation For The Uzbek Legal Domain*. **ACM ICFNDS ’25, 2025, pp. 680–687; DOI `10.1145/3789692.3789782`.**
**Status:** B, CRITICAL; [bibliographic/verified-abstract deep dive completed 2026-09-14](../literature/deep-dives/2025_Absalamova_Muminov_Absalamova_O_RAG_Uzbek_Legal_Ontology.md).

Verified at abstract level:

- Uzbek legal domain;
- hybrid retrieval;
- custom legal ontology;
- ontology-based reranking of retrieved legal articles;
- Lex.uz-derived QA data;
- reported **Retrieval Precision / Hit Rate and Citation Accuracy improvement** over standard RAG baselines.

Important:

- custom ontology and reranking add factors whose contributions cannot be separated from fusion without ablation;
- domain-specific legal RAG != general-purpose Uzbek IR;
- exact lexical/dense/fusion components, ontology score, baseline list and **metric values** remain unverified;
- exact Hit Rate definition/cutoff is unknown; it must not be equated with a standard P@k/R@k measure, and Citation Accuracy is not document-ranking effectiveness;
- retrieval != reranking; **do not attribute all gain to lexical–semantic fusion** (or to ontology alone).

**Remaining work:** full-text methods, metrics and ablation verification.

## 8.3 National synthesis after the completed deep dives

The [national evidence matrix, 2026-09-14](NATIONAL_EVIDENCE_MATRIX_2026-09-14.md) connects established morphology/search infrastructure, contextual NLP, corpus-level semantic retrieval, supporting BM25-vs-vector comparison, hybrid/RAG and ontology-enhanced reranking. The reviewed additions through **2026-09-15** strengthen the existing boundary without changing **v0.8 refined**: no verified controlled Uzbek `BM25_raw/stem/lemma × same fixed D` complementarity decomposition was found. The residual question remains morphology-induced change in lexical–dense complementarity.

---

# 9. Key distinctions established

These distinctions must survive all future writing:

1. `BERT model != retriever`.
2. `Word embeddings != retrieval evaluation`.
3. `STS != corpus-level IR`.
4. `RAG answer accuracy != retrieval effectiveness`.
5. `cross-encoder usually = reranking, not full-corpus first-stage retrieval`.
6. `sparse != non-neural`.
7. `dense != universally semantic-superior`.
8. `morphological normalization != semantic matching`.
9. `hybrid Uzbek retrieval exists`; gap must be narrower.
10. `adaptive alpha exists`; possible novelty must be language/problem-specific and empirically justified.
11. `morphology preprocessing != independent third retrieval paradigm`.
12. `paraphrase / coreference / sentiment != corpus-level IR`.
13. `BM25 vs vector comparison != hybrid fusion`.
14. `search deployment/productivity claims != qrels-based retrieval effectiveness`; `NLP analyzer accuracy/F1 != MAP/nDCG/Recall`.
15. `retrieval != reranking`; ontology/reranking gains cannot automatically be attributed to lexical–semantic fusion.

---

# 10. Claims that are currently safe

- BM25 remains a strong lexical baseline.
- Lexical and semantic retrieval have complementary strengths.
- Uzbek morphology affects lexical representation/search processing.
- Uzbek semantic NLP resources are substantial and growing.
- Uzbek semantic retrieval has direct IR evaluations in some 2026 specialized tasks.
- Uzbek hybrid/RAG systems already exist, particularly in legal domain.
- Current literature still leaves open how morphology-normalized lexical representation changes complementarity with semantic retrieval across Uzbek query types.

---

# 11. Claims that must NOT be made without new evidence

- «Для Uzbek hybrid retrieval отсутствует.»
- «Для Uzbek semantic retrieval нет evaluation.»
- «BM25 + BERT — новый метод.»
- «RRF — наша новизна.»
- «Dynamic alpha(q) — наша новизна.»
- «UzBERT/BERTbek proves strong Uzbek retrieval.»
- «Morphology-aware neural semantics has not been studied for Uzbek.»
- «More sophisticated morphological analysis necessarily gives better IR.»
- «USHRA = a specific fusion formula» until full text is verified.
- «O-RAG improvement is caused only by lexical-semantic fusion.»

---

# 12. Current interpretation of the research opportunity

The strongest current research direction is **not** “build the first Uzbek hybrid search system”, and it is no longer sufficient to claim novelty from merely placing morphology-aware BM25, a modern dense retriever and fusion in one experiment.

After the 2026-09-10 gap-killer analysis, the current residual question is:

> **how changing the morphological representation of the Uzbek lexical channel changes the structure of its complementarity with the same modern semantic retriever — unique relevant hits, overlap and incremental hybrid gain — and how these changes depend on interpretable Uzbek query characteristics.**

The controlled logic is:

`BM25_raw ↔ BM25_stem ↔ BM25_lemma`

with the same fixed dense comparator `D`, followed by:

`BM25_raw + D`
`BM25_stem + D`
`BM25_lemma + D`.

The main explanatory analysis should go beyond aggregate MAP/nDCG/Recall and include, where qrels permit:

- per-query gains/losses;
- unique relevant hits of each component;
- relevant-set overlap/intersection;
- oracle union;
- incremental hybrid gain;
- statistical relation of these changes to morphology/script/lexical query features.

Only after this interaction is established should the project decide whether the final method is fixed fusion, RRF, learned fusion, query-dependent integration or another architecture.

See `CURRENT_GAP.md`, `GAP_BOUNDARY_2026-09-10.md` and `OPEN_QUESTIONS.md`.

---

# 13. Gap-boundary update — 2026-09-10

The 2026-09-10 national screening and international gap-killer search materially narrowed the previous v0.4 formulation. National deep dives completed 2026-09-11–2026-09-14 now replace the screening records in sections 1, 3, 5, 6 and 8; their [matrix synthesis](NATIONAL_EVIDENCE_MATRIX_2026-09-14.md) strengthens the boundary without changing v0.8 refined.

## 13.1 New boundary evidence

### UPERF — Urdu, PACLIC 2024

- raw/stemmed/lemmatized preprocessing;
- BM25, TF-IDF and embedding-based representations;
- single-word vs multiple-word queries;
- weighted lexical–semantic combination;
- main metric Recall@5.

Consequence: raw/stem/lemma + lexical/semantic analysis in a low-resource morphologically complex language is **not** a novel component combination by itself.

### Kazi & Khoja — Urdu, *Computer Speech & Language* 2026

- multi-benchmark Urdu document retrieval;
- lexical/statistical models plus embedding features;
- learned SVMrank reranking.

Consequence: learned lexical–semantic integration in low-resource retrieval is already established.

### Aboasal et al. — Arabic legal IR, 2026

- BM25 with/without Farasa morphology in the reported setup;
- modern embedding models including BGE-M3/GTE/Ada/Mistral-embed;
- hybrid BM25(Farasa)+semantic retrieval;
- MAP/nDCG evidence.

Consequence: morphology-aware BM25 + modern semantic embeddings + hybrid retrieval cannot be used as a broad novelty claim.

### Munetsi, Mukande & O'Connor — Shona, SIGIR 2026

- direct morphology-aware low-resource IR research;
- BM25 plus modern neural retrieval comparators;
- standard retrieval metrics.

Consequence: morphology-conditioned retrieval behavior is already a mainstream modern IR research question.

### GreekBarRetrieval — Greek statutory retrieval, 2026 preprint

- three BM25 preprocessing/morphology variants;
- nine modern dense retrievers;
- sparse–dense fusion;
- query reformulation;
- nDCG/MAP/Recall.

Consequence: even “several morphology-aware BM25 variants + modern dense + fusion in one benchmark” is insufficient as novelty. The project must study the **interaction/decomposition** that remains unexplained.

### Sharifbaev 2026 Uzbek/Russian manuscript

The analyzed manuscript describes:

- lemmatized BM25;
- LaBSE dense retrieval;
- graph retrieval;
- adaptive selection of retrieval strategy;
- a Uzbek/Russian parliamentary/legal corpus.

It remains D-level until official final/defense evidence is verified, but it is a serious warning against broad claims that Uzbek lacks morphology-aware hybrid retrieval.

## 13.2 Current gap boundary

The current project did **not** find a verified Uzbek analogue that simultaneously:

1. changes only the lexical morphology representation (`raw/stem/lemma`);
2. keeps the same modern dense retriever fixed;
3. keeps a controlled fusion protocol fixed/validation-tuned;
4. measures unique relevant hits, overlap/intersection, oracle union and incremental hybrid gain;
5. links morphology-induced changes to interpretable Uzbek morphology/script/query features.

This is a provisional literature conclusion, not a claim of exhaustive non-existence.

## 13.3 Search stopping rule

Broad generic gap search is provisionally saturated as of 2026-09-10. Future search should be reopened when:

- a direct analogue appears;
- a preprint/working manuscript receives a stronger publication/final-defense status;
- a new 2026+ paper directly targets morphology-induced lexical–dense complementarity;
- pilot experiments contradict the assumed interaction.

Current source of truth for the formulation: `research/CURRENT_GAP.md`.
