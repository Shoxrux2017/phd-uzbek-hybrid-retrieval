# Open Questions

## A. Highest-priority literature questions

### A1. USHRA — full-text verification

Нужно установить по полному тексту:

- что именно авторы называют `Uzbek-Specific Hybrid Semantic Retrieval Algorithm`;
- есть ли BM25/TF-IDF или другой lexical retriever;
- на каком уровне происходит fusion;
- есть ли score normalization;
- какие embeddings используются;
- как сформированы 200 legal queries;
- какие retrieval metrics есть помимо answer accuracy;
- есть ли qrels;
- какие baselines;
- какой вклад retrieval отделён от generation.

### A2. O-RAG — full-text verification

Нужно установить:

- точную hybrid retrieval architecture;
- роль ontology;
- формулу/алгоритм ontological reranking;
- retrieval baselines;
- dataset/query construction;
- Hit Rate definition;
- Citation Accuracy definition;
- насколько improvement связан именно с fusion, а не domain ontology.

### A3. Query-Adaptive Hybrid Search 2026

Нужно глубоко разобрать:

- Query-Driven Alpha Prediction;
- входные query features/representation;
- antagonist negative sampling;
- MIRACL/MLDR experimental design;
- fixed-fusion baselines;
- насколько выигрыш устойчив across languages/domains;
- какие свойства запроса коррелируют с alpha;
- что можно и нельзя перенести на Uzbek.

### A4. CLEAR

Нужно понять:

- semantic residual objective;
- связь с BM25;
- как строятся negatives;
- где именно появляется complementarity;
- baselines;
- datasets;
- ablation;
- чем CLEAR отличается от simple fusion.

### A5. DHR / Lin & Lin

Нужно подробно понять:

- Dense Lexical Representation;
- Dense Hybrid Representation;
- index/search mechanism;
- representation construction;
- multilingual results;
- robustness claims;
- насколько эта архитектура релевантна Uzbek.

### A6. BGE-M3

Нужно установить:

- sparse/dense/multi-vector mechanisms;
- hybrid use in original experiments;
- language coverage vs actual Uzbek evaluation;
- fine-tuning requirements;
- feasibility as a strong experimental baseline.

### A7. Uzbek morphology

Глубоко разобрать:

- Bakaev PhD;
- Xusainova PhD;
- morphology algorithms;
- exact search deployment;
- datasets/queries;
- что реально измерено;
- есть ли standard IR metrics;
- какие morphology errors важны для retrieval.

### A8. Uzbek semantic retrieval 2026

Ishkobilov et al.:

- corpus construction;
- relevance judgments;
- number of relevant docs per query;
- exact FastText aggregation;
- statistical test;
- limitations of 100-query domain-specific setup.

SIGTURK 2026:

- Uzbek subset;
- idiom retrieval task construction;
- metrics;
- best models;
- насколько conclusions generalize beyond idioms.

## B. Turkic / morphology-aware IR search still needed

Продолжить систематический поиск по:

- Kazakh;
- Kyrgyz;
- Azerbaijani;
- Uyghur;
- Turkish;
- other agglutinative low-resource languages.

Особенно:

- morphology-aware BM25;
- lemma/stem/raw comparison;
- dense retrievers on agglutinative languages;
- hybrid sparse+dense retrieval;
- query-adaptive retrieval using morphological features.

## C. Candidate research questions (not fixed)

- **RQ1:** Как морфологическая нормализация влияет на effectiveness lexical retrieval для Uzbek?
- **RQ2:** Для каких типов Uzbek queries lexical и semantic retrieval имеют различную эффективность?
- **RQ3:** Насколько известные fixed fusion / RRF методы улучшают результаты относительно отдельных components?
- **RQ4:** Существует ли статистически устойчивое отношение между query characteristics и относительной полезностью lexical/semantic retrieval?
- **RQ5:** Если да, может ли использование этой зависимости улучшить hybrid fusion?

Эти RQ пока **не утверждены**.

## D. Experimental-resource questions

Нужно определить:

- есть ли подходящий general-purpose Uzbek corpus;
- есть ли реальные query logs;
- как строить qrels;
- сколько queries требуется;
- нужны ли несколько domains;
- нужен ли Latin/Cyrillic split;
- какие baselines обязательны;
- какие metrics primary;
- какой statistical significance test;
- как делать per-query error analysis;
- как избежать leakage при synthetic query generation.

## E. Citation verification

Особое внимание:

- ICFNDS '25 vs publication metadata 2026 для morphology-oriented STS / USHRA / O-RAG;
- официальный ACM record должен иметь приоритет над агрегаторами;
- полные страницы, volume/issue и DOI национальных/турецких источников;
- preprint vs peer-reviewed version для UzBERT/Uzbek embeddings.
