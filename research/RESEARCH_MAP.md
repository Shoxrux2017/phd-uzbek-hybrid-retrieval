# Research Map

**Purpose:** сквозная карта того, что уже изучено и как отдельные линии связаны с текущей PhD.  
**Evidence cut-off:** 2026-08-31.

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

Важно:

- реальная национальная PhD;
- первая глава построена как theory → critical analysis → comparison → international/domestic work → gaps → tasks;
- morphology напрямую связана с обработкой Uzbek search queries и практическими library systems;
- результаты внедрения нельзя автоматически считать modern qrels-based IR benchmark.

**Deep dive priority:** very high.

## 1.5 Kh. I. Akhmedova, PhD, Uzbekistan, 2023

**Topic:** models/algorithms/information system for semantic analysis of Uzbek sentences; specialty 05.01.10.

Важно:

- подтверждает национальное развитие semantic processing;
- не является dense query–document retrieval;
- структурный ориентир: global methods → Uzbek context → own model.

**Deep dive priority:** high.

## 1.6 Z. Y. Xusainova, PhD, Uzbekistan, 2024

**Topic:** tokenization, stemming, lemmatization of Uzbek units and software.

Важно:

- morphology preprocessing для Uzbek corpus/search;
- practical search optimization;
- необходимо отдельно выяснить exact retrieval evaluation.

**Deep dive priority:** very high.

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

Can et al., Turkish IR (JASIST, 2008):

- 408,305 documents;
- 72 ad-hoc queries;
- сравнение stemming strategies;
- morphology matters for IR, но более сложный lemmatizer не гарантирует automatic superiority.

### Consequence

Для Uzbek нельзя заранее предполагать:

`lemma BM25 > stem BM25 > raw BM25`.

Это надо измерять.

## 3.2 Uzbek morphology research

Bakaev:

- morphological analysis;
- search-query processing;
- library implementation.

Xusainova:

- tokenization/stemming/lemmatization;
- National Corpus search optimization.

National project IL-402104209:

- morpholexicon and morphological analyzer for IR/NLP systems.

### Established

- morphology relevant for Uzbek search;
- national infrastructure exists.

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

---

# 6. Uzbek semantic retrieval — 2026 update

## 6.1 Ishkobilov et al., Semantic Retrieval of Uzbek Seismic Safety Regulations

Reported setup:

- 120 documents;
- 8,450 indexed paragraphs;
- 100 domain queries;
- TF-IDF baseline;
- FastText semantic representation;
- metrics: Precision@5, Recall@5, MAP, MRR, F1;
- FastText reported higher results across main metrics.

Important consequence:

> Нельзя утверждать, что Uzbek corpus-level semantic retrieval со стандартными IR-метриками отсутствует.

Limitations relevant to current PhD:

- specialized seismic/engineering domain;
- comparison, not fusion;
- static FastText rather than modern contextual dense retriever;
- no explicit morphology-normalized lexical vs semantic complementarity study.

**Deep dive priority:** very high.

## 6.2 SIGTURK 2026 Turkic Idiom Benchmark

Aslantaş & Gungor:

- five Turkic languages including Uzbek;
- semantic retrieval task;
- multiple embedding models;
- dense retrieval metrics.

Important:

- Uzbek semantic retrieval exists in benchmark setting;
- task is specialized idiom-to-meaning retrieval, not general document retrieval.

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

Absalamova, Muminov, Absalamova.

Verified at current level:

- Uzbek legal queries;
- Lex.uz;
- multilingual embeddings;
- RAG;
- authors call their method `Uzbek-Specific Hybrid Semantic Retrieval Algorithm`;
- reported 85% answer accuracy on 200 criminal-law queries.

Important limitations of current knowledge:

- full fusion mechanism not yet verified;
- answer accuracy != retrieval effectiveness;
- exact qrels/IR metrics/baselines need full-text analysis.

Therefore:

- **cannot say Uzbek hybrid search does not exist**;
- **cannot yet classify USHRA confidently as score fusion/RRF/etc.**

**Deep dive priority:** critical.

## 8.2 O-RAG

Verified at current level:

- Uzbek legal domain;
- hybrid retrieval;
- custom legal ontology;
- ontological reranking;
- Lex.uz-derived data;
- reported Hit Rate / Citation Accuracy improvement.

Important:

- domain ontology contributes to effect;
- domain-specific legal RAG != general-purpose Uzbek IR;
- exact fusion classification needs full-text verification.

**Deep dive priority:** critical.

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

The strongest current research direction is **not** “build the first Uzbek hybrid search system”.

It is to understand:

> how morphology-aware lexical representation and query characteristics affect the relative and joint effectiveness of lexical and semantic retrieval for Uzbek text ranking.

Only after that evidence is available should the project decide whether the final method is:

- fixed score fusion;
- RRF;
- learned fusion;
- query-adaptive fusion;
- another architecture.

See `CURRENT_GAP.md` and `OPEN_QUESTIONS.md`.
