# Gap Boundary Update — 2026-09-10

**Status:** ACTIVE research synthesis
**Evidence additions reviewed through:** 2026-09-15
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
- lexical–semantic complementarity as a general research idea;
- complementarity-aware component training;
- unified/joint lexical–semantic representation;
- query-adaptive fusion or Query-Driven Alpha Prediction;
- unified multilingual dense / learned sparse / multi-vector retrieval.

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

**Reliability:** A, defended PhD; [deep dive completed 2026-09-11](../literature/deep-dives/2021_Bakaev_Uzbek_Morphology_Search.md).

**Established:** Morphoanalyzer combines tokenization, normalization, morphemic analysis and grammatical tagging. Reported base correctness is 96% for fairy tales, 92.4% for legal documents, 88.9% for hadiths and 94% for proverbs. The related 2020 full-text search paper uses stemmer + lemmatizer with term/field weighting; real library deployment includes the National Library of Uzbekistan.

**Important distinction:** analyzer accuracy and qualitative search-deployment claims are not qrels-based IR effectiveness. The **9–11%** result concerns catalog/document-processing time/labor, not retrieval gain. The later 91.3% religious-text result must not be merged with the 88.9% hadith result without checking comparability.

**Not established:** BM25/qrels evaluation, a controlled `BM25_raw ↔ BM25_stem ↔ BM25_lemma` benchmark or interaction with a fixed modern dense retriever.

### 2.2 Xusainova PhD (2024)

**Reliability:** A, defended PhD; [deep dive completed 2026-09-11](../literature/deep-dives/2024_Xusainova_Uzbek_Tokenization_Stemming_Lemmatization.md).

**Established:** BPE/tokenizer, UzbStemmer and lemmatizer; application to >100k sentences, reported **97.5% stemmer/analyzer accuracy**, and >32k simple + >7.5k compound lexical units. Corpus/platform search optimization is reported.

**Important distinction:** analyzer accuracy != retrieval effectiveness; search deployment and SEO discussion != ad-hoc IR evaluation.

**Not established:** BM25/qrels/raw-stem-lemma retrieval comparison or morphology-conditioned lexical–dense complementarity.

### 2.3 Elov DSc (defended 2026)

**Reliability:** A, officially defended DSc on **2026-02-05**; [full-manuscript deep dive completed 2026-09-11](../literature/deep-dives/2026_Elov_Uzbek_NLP_Morphology_Information_System.md). The supplied manuscript is dated **2025**.

**Established:** hybrid rule/statistical/neural morphology, normalization, lemma-based inverted indexing and integrated UzNLP morphology/POS/syntax/semantic-role/NER modules. SQL Server full-text / Elasticsearch are explicitly named infrastructure.

**Important distinction:** NLP module integration is not lexical+dense retrieval fusion, and module accuracy/F1 != IR effectiveness. Chapter-level **94% accuracy / 92% F1** and later **96.4% / 96.5%** describe unreconciled evaluation contexts. The headline **~50 billion sentences / ~380M words** is internally implausible; other counts (~124M tokens, ~38M tagged words) must retain their separate contexts and be verified before corpus-scale citation.

**Not established:** controlled BM25 morphology ablation, modern dense/hybrid retrieval interaction or query-level complementarity decomposition.

### 2.4 Turayev candidate PhD (2026)

**Reliability:** B pending final-defense verification; [deep dive completed 2026-09-11](../literature/deep-dives/2026_Turayev_Uzbek_Morphosyntactic_Neural_Analysis.md).

**Established:** TUIT scientific seminar **2026-07-11**; >32k base forms (table: 32,225) and explicit lemmatization; **MaxEnt+BiLSTM+CRF** and **RNN+CYK** morphosyntactic lines.

**Important distinction:** registration **B2025.3.PhD/T5887** conflicts with another dissertation in the official OAK index, and final-defense fields are blank. Seminar verification does not prove final defense. National Library deployment concerns document/speech input and syntactic editing, not search effectiveness; large corpus counts and nonstandard POS metric usage require further verification.

**Not established:** defended/A-level status, BM25/dense/hybrid ranking, qrels or morphology-induced IR gains.

### 2.5 Axmedova X.X. candidate PhD (2026)

**Reliability:** B pending final-defense protocol verification; [deep dive completed 2026-09-11](../literature/deep-dives/2026_Axmedova_Uzbek_Paraphrase_Semantic_Matching.md).

**Established:** TUIT seminar and OAK defense announcement; **Multilingual E5 + cosine** semantic duplicate/paraphrase matching, **Jina-assisted** candidate selection, and **Gemma3-based** paraphrase generation.

**Important distinction:** final defense outcome is not verified. Dataset/result descriptions **250K pairs / 5K test sentences / 88.3%** and **375K triplets / 91.3% / F1 0.954** are not reconciled. Embedding use does not by itself establish a retriever; paraphrase/semantic similarity != corpus-level IR.

**Not established:** controlled BM25 vs modern dense retrieval, query-document qrels or morphology × complementarity.

### 2.6 Abdisalomova Sh.A. candidate PhD (2026)

**Reliability:** B pending final-defense verification; [deep dive completed 2026-09-11](../literature/deep-dives/2026_Abdisalomova_Uzbek_Coreference_UzCoref.md).

**Established:** Uzbek coreference corpus of **1,020 documents, ~320k tokens, 18,451 mentions and 5,326 chains**, with expert-corrected CoNLL-style annotation. Hybrid rule+ML+neural coreference reports CoNLL F1 **64.3**; the separate UzRoBERTa table reports **67.8**.

**Important distinction:** registration/discussion evidence does not establish final defense; rounded/prose ~68/70% results are not fully reconciled with the tables. Coreference is within-document reference resolution, not query-document retrieval. Reported search-related platform deployment is not a retrieval benchmark.

**Not established:** qrels-based BM25/dense/hybrid effectiveness or morphology-induced complementarity.

### 2.7 Allanazarova S.Y. candidate PhD (2026) — background only

**Reliability:** B pending final-defense verification; [deep dive completed 2026-09-11](../literature/deep-dives/2026_Allanazarova_Uzbek_Sentiment_SentiUzNet.md).

**Established:** SentiUzNet, **3,336 synsets**, six annotators, **κ=0.79**; **384k+ comments** and reported **91% sentiment accuracy**.

**Important distinction:** final defense remains unverified; the 397,227 merged-review pool is a separate reported count. “Hybrid” refers to sentiment-resource construction/classification, not lexical+dense retrieval.

**Not established:** corpus retrieval or any part of the controlled morphology–complementarity experiment. Keep as LOW/background evidence.

### 2.8 Ishkobilov et al. (2026)

**Reliability:** B; [verified-abstract deep dive completed 2026-09-14](../literature/deep-dives/2026_Ishkobilov_Uzbek_Seismic_Semantic_Retrieval.md). Verified *Vibroengineering Procedia* 63, pp. 227–231 (2026).

**Established:** real corpus-level Uzbek paragraph retrieval; project record of **120 documents, 8,450 paragraphs, 100 queries**. Verified abstract values: TF-IDF **P@5 0.6017 / R@5 0.5418**, FastText **P@5 0.7444 / R@5 0.6875**; paired test **t=15.1372, p<0.001** is reported.

**Important distinction:** the abstract independently confirms 100 queries, but exact corpus counts and qrels construction need full text. Exact MAP/MRR values, F1 use/value and the per-query quantity/assumptions of the t-test remain unverified. Static/subword FastText comparison is not a modern retrieval-trained dense or hybrid experiment.

**Not established:** BM25, raw/stem/lemma intervention, fusion or complementarity decomposition.

### 2.9 USHRA (2025)

**Reliability:** B; [bibliographic/verified-abstract deep dive completed 2026-09-14](../literature/deep-dives/2025_Absalamova_Muminov_Absalamova_USHRA_Uzbek_Legal_RAG.md). **ACM ICFNDS ’25, 2025, pp. 1036–1042; DOI `10.1145/3789692.3789825`.**

**Established:** multilingual embeddings + named Uzbek-Specific Hybrid Semantic Retrieval Algorithm + RAG over Lex.uz; **85% chatbot answer accuracy on 200 criminal-law queries**.

**Important distinction:** answer accuracy != retrieval effectiveness; secondary 2026 appearance dates do not change the 2025 publication year.

**Not established:** exact lexical model, embedding checkpoint, index/fusion mechanism, qrels/pure IR metrics or a controlled morphology–complementarity analysis. Full text remains needed.

### 2.10 O-RAG (2025)

**Reliability:** B; [bibliographic/verified-abstract deep dive completed 2026-09-14](../literature/deep-dives/2025_Absalamova_Muminov_Absalamova_O_RAG_Uzbek_Legal_Ontology.md). **ACM ICFNDS ’25, 2025, pp. 680–687; DOI `10.1145/3789692.3789782`.**

**Established:** custom legal ontology + hybrid retrieval + ontology-based reranking, Lex.uz-derived QA data, and abstract-level Hit Rate / Citation Accuracy improvement over standard RAG baselines.

**Important distinction:** retrieval != reranking; Citation Accuracy is not pure document-ranking effectiveness. Exact Hit Rate definition/cutoff is unverified. Without ablation, gains cannot automatically be attributed to lexical–semantic fusion or to ontology alone.

**Not established:** exact lexical/dense/fusion components, metric values, detailed evaluation/ablation or raw/stem/lemma × fixed-D complementarity. Full text remains needed.

### 2.11 Urinov (2025) — supporting only

**Reliability:** C; [metadata/abstract-level deep dive completed 2026-09-14](../literature/deep-dives/2025_Urinov_Uzbek_RAG_BM25_Vector_Search.md). **Zenodo DOI `10.5281/zenodo.17341315`.**

**Established:** BM25-like traditional vs semantic vector-search comparison in Uzbek RAG at Zenodo metadata/abstract level.

**Important distinction:** underlying venue/peer review is unverified; author's PhD status does not upgrade the paper. **BM25 vs vector comparison != hybrid fusion**, even when metadata uses a “hybrid” keyword.

**Not established:** corpus, queries/qrels, exact vector model, BM25 parameters, standard metrics, genuine fusion or morphology-induced complementarity.

### 2.12 Sharifbaev 2026 dissertation manuscript

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

### National synthesis

The [national evidence matrix, 2026-09-14](NATIONAL_EVIDENCE_MATRIX_2026-09-14.md) confirms that Uzbek morphology/search infrastructure, corpus-level semantic retrieval, supporting BM25-vs-vector comparison, hybrid/RAG and ontology-enhanced reranking already exist. STS/paraphrase/coreference/sentiment remain distinct from corpus IR; morphology preprocessing remains a lexical-representation variant, not an independent third retrieval paradigm.

No verified controlled Uzbek **`BM25_raw/stem/lemma × same fixed D`** complementarity decomposition was found: lexical-only and dense-only relevant hits, intersection/overlap, oracle union, incremental hybrid gain, per-query changes and their relationship to interpretable Uzbek query characteristics remain the residual question. The additions strengthen the boundary and retain **v0.8 refined**; they do not make fixed fusion, RRF, dynamic alpha, ontology or RAG novelty claims.

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

**Reliability:** A, peer-reviewed SIGIR; **4-page preliminary study**. [Deep dive COMPLETED 2026-09-15](../literature/deep-dives/2026_Munetsi_Mukande_OConnor_Shona_Morphology_Aware_IR.md).

Established within this preliminary scope:

- ~5,000 Shona documents and 75 topics; BM25 / ColBERT-v2 / dense-model comparison with manual relevance judgments;
- morphology-sensitive failure analysis identifies surface variation as a retrieval challenge;
- a larger morphology-aware benchmark/framework is **proposed**; stemming/lemmatization are future-work options, not implemented experimental conditions.

Critical consequence:

- “morphology-aware low-resource retrieval” is not itself a novel research direction.

Residual:

- no controlled `raw/stem/lemma` intervention and no BM25+dense hybrid fusion in the main table;
- no morphology-conditioned unique-hit/overlap/oracle-union/hybrid-gain decomposition;
- shallow top-10 pooling and incompletely specified assessors/agreement/adjudication limit Recall and set-coverage interpretation. The Uzbek benchmark needs deeper pooling and an explicit annotation protocol; this paper does not prove stemming/lemmatization gains.

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

### 3.8 Gao et al. — CLEAR (ECIR 2021)

**Reliability:** A; [deep dive COMPLETED 2026-09-15](../literature/deep-dives/2021_Gao_CLEAR_Semantic_Residual_Embeddings.md).

**Occupied boundary:** generic lexical–semantic complementarity and complementarity-aware **training**. The dense semantic residual is trained against BM25 errors using error-based negatives and a residual margin.

**Residual:** no raw/stem/lemma intervention or morphology-induced relevant-set decomposition. Retraining a separate dense component for each lexical variant would change both factors; the primary experiment must keep `D` fixed.

### 3.9 Lin & Lin — DHR (TOIS 2023)

**Reliability:** A; [deep dive COMPLETED 2026-09-15](../literature/deep-dives/2023_Lin_Lin_Dense_Representation_Framework_DHR.md).

**Occupied boundary:** representation-level lexical–semantic integration, unified vector retrieval and joint training. Dense Lexical Representation demonstrates that **dense representation != semantic matching**.

**Residual:** no controlled morphology intervention with the same independent semantic comparator. Define `D` as a **fixed retrieval-trained semantic dense retriever**, rather than identifying the signal solely by its vector format.

### 3.10 Posokhov et al. — Query-Adaptive Hybrid Search (2026)

**Reliability:** A; [deep dive COMPLETED 2026-09-15](../literature/deep-dives/2026_Posokhov_Query_Adaptive_Hybrid_Search.md).

**Occupied boundary:** dynamic `alpha(q)`, Query-Driven Alpha Prediction and dense training targeted at BM25 failure cases. Fusion-level adaptation is already established.

**Residual:** no `raw/stem/lemma × same fixed D` or morphology-conditioned unique hits, overlap, oracle union and hybrid gain. Its per-query best-alpha oracle concerns ranking under an optimal weight, not relevant-document coverage of the candidate union.

### 3.11 Chen et al. — BGE-M3 (Findings of ACL 2024)

**Reliability:** A; [deep dive COMPLETED 2026-09-15](../literature/deep-dives/2024_Chen_BGE_M3_Embedding.md).

**Occupied boundary:** one multilingual model supports dense, learned sparse and multi-vector retrieval with joint training/self-distillation.

**Residual/design consequence:** no Uzbek retrieval evaluation or controlled morphology-induced decomposition. Dense-only is a candidate `D` requiring Uzbek pilot validation; All adds sparse/multi-vector signals and should not be the primary causal comparator. The BM25 tokenizer/analyzer comparison changes multiple preprocessing operations, so it motivates explicit preprocessing control without proving a stemming-specific effect.

### 3.12 Sheng-Chieh Lin — PhD (Waterloo 2024)

**Reliability:** A, officially defended PhD; [deep dive COMPLETED 2026-09-15](../literature/deep-dives/2024_Sheng_Chieh_Lin_PhD_Robust_Dense_Retrieval.md).

**Occupied boundary:** robustness, domain/language transfer and preservation of lexical/semantic evidence are established dense-retrieval concerns. Strong English/BEIR or multilingual results do not establish Uzbek effectiveness.

**Residual/design consequence:** no Uzbek `raw/stem/lemma × fixed D` experiment. Validate candidates on Uzbek pilot/dev, select primary `D` under a predefined rule, then freeze it. Structural lesson: `problem → evidence of limitation → controlled experiment → method only if justified`.

### 3.13 Bruch, Gai & Ingber — Fusion Functions (TOIS 2023)

**Reliability:** A; [deep dive COMPLETED 2026-09-15](../literature/deep-dives/2023_Bruch_Gai_Ingber_Fusion_Functions_Hybrid_Retrieval.md). Official ACM publication: **August 2023**; some indexes associate Volume 42(1) with **2024**.

**Occupied boundary:** fixed weighted fusion, normalization, convex-combination/RRF comparison and global-alpha tuning. Normalized convex fusion is a strong interpretable baseline with sample-efficient tuning in the tested settings; RRF has parameters, loses score-distance information and can be sensitive to domain transfer.

**Residual/design consequence:** the paper varies fusion with fixed components, not lexical morphology. Candidate-union coverage and fusion ranking are separate levels. The primary Uzbek comparison should freeze `D`, candidate depth `k`, normalization, formula and one global validation-selected `alpha` across raw/stem/lemma; RRF is a secondary robustness control. The best-alpha oracle is not oracle union.

---

## 4. Claim-status matrix after the 2026-09-10 search and 2026-09-15 deep dives

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
| Complementarity-aware dense training is new | **REJECTED** — CLEAR; Posokhov |
| Unified/joint lexical–semantic representation is new | **REJECTED** — DHR |
| Unified multilingual dense / learned sparse / multi-vector retrieval is new | **REJECTED** — BGE-M3 |
| Dense robustness/multilingual transfer is an unstudied concern | **REJECTED** — Lin PhD |
| Fixed weighted fusion, normalization or global-alpha tuning is new | **REJECTED** — Bruch |
| Munetsi already demonstrates raw/stem/lemma or BM25+dense fusion gains | **NOT ESTABLISHED** — preliminary comparison; morphology normalization is future work |
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

Pilot/dev-validate candidate retrieval-trained multilingual semantic dense retrievers for Uzbek, select primary `D` under a predefined rule and freeze its checkpoint, mode and input preprocessing before the held-out morphology experiment. BGE-M3 Dense and multilingual E5 are candidate families; no Uzbek winner is established. BGE-M3 All is unsuitable as the primary causal comparator because it adds sparse and multi-vector signals.

A second modern dense model may be used for robustness, but the primary interaction analysis must not change dense model and morphology at the same time.

### Hybrid conditions

`H_raw = fusion(BM25_raw, D)`
`H_stem = fusion(BM25_stem, D)`
`H_lemma = fusion(BM25_lemma, D)`.

Provisional primary control: **normalized convex combination** with the same formula, normalization rule, candidate depth `k` and **one global `alpha` selected on validation only** across all three conditions. Form `top-k BM25_m ∪ top-k D` and specify how both scores are obtained for union candidates before normalization/fusion. Hold non-morphological BM25 preprocessing constant and document tokenization, script/Unicode normalization and stop-word handling.

RRF is a **secondary robustness control**, with its rank-offset parameter specified and the same candidate depth. An optional secondary practical experiment may independently validation-tune `alpha_raw`, `alpha_stem`, `alpha_lemma`; report it separately from the primary causal comparison.

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

Candidate-set complementarity/coverage must be analyzed separately from fusion ranking quality. Oracle union is not a per-query best-alpha oracle. Reliable unique-hit, Recall and oracle-union estimates require deeper multi-system pooling than top-10, explicit assessors/agreement/adjudication and transparent qrels coverage limits.

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
- **Munetsi et al. 2026:** A as a peer-reviewed SIGIR source, but a 4-page preliminary study with shallow pooling; no implemented raw/stem/lemma or main-table hybrid fusion evidence.

---

## 9. Verdict after the 2026-09-15 international deep dives

The targeted wave is substantially completed. Generic training, representation and fusion novelty routes are more clearly occupied, while no reviewed work closes the controlled chain:

`morphological representation change → lexical relevant-set change → overlap/unique-hit change versus the SAME fixed semantic D → incremental hybrid-gain change → relation to interpretable Uzbek query characteristics`.

The immediate bottleneck is benchmark/qrels plus pilot evidence. This is a provisional literature boundary, not proof of exhaustive absence or final novelty.

**v0.8 refined survives unchanged.**
