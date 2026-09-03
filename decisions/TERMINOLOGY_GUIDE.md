# Dissertation Terminology Guide

**Status:** ACTIVE

**Established:** 2026-09-01  
**Last terminology verification:** 2026-09-03

## Purpose

Normative terminology policy for the Russian-language PhD dissertation:

> **Гибридный подход к поиску информации на узбекском языке на основе интеграции лексических и семантических методов.**

The main scientific prose must remain Russian while preserving precise international IR/NLP terminology.

## Evidence basis

The policy follows terminology practice observed in real Russian-language dissertations close to information retrieval, NLP and vector semantics, including works by P. I. Braslavskiy, A. V. Pugachev, A. A. Potapenko and A. I. Panchenko.

The terminology used in Chapter I was additionally checked term-by-term against real Russian-language dissertations, author abstracts, official university research works and peer-reviewed scientific publications in IR/NLP and adjacent fields.

Observed pattern:

1. Russian is the main scientific language.
2. The English original may be given at first introduction for identification and precision.
3. Subsequent prose normally uses the Russian form or an established abbreviation.
4. Official names of models, algorithms, datasets, resources and named methods remain unchanged.
5. English descriptive words should not be inserted into Russian sentences when a verified and natural Russian scientific equivalent exists.
6. A Russian equivalent must not be invented solely by literal translation. If stable Russian usage is not sufficiently supported, retain the international term and explain the concept in Russian.
7. When several Russian variants are genuinely attested, this guide may select one house form for consistency without claiming that the alternatives are incorrect.

### Russian-language dissertation anchors

The terminology policy was checked against the following real Russian-language dissertations:

1. П. И. Браславский — «Методы и наборы данных для оценки моделей информационного поиска и обработки естественного языка», докторская диссертация, НИУ ВШЭ, 2026.  
   Relevance: direct information retrieval + NLP terminology reference.
2. А. В. Пугачев — «Методы переноса обучения в задачах автоматической обработки текста», кандидатская диссертация, НИУ ВШЭ, 2026.  
   Relevance: modern NLP, Transformer methods, information retrieval, lexical/vector/hybrid retrieval terminology.
3. А. А. Потапенко — «Семантические векторные представления текста на основе вероятностного тематического моделирования», кандидатская диссертация, специальность 05.13.17 «Теоретические основы информатики», защита 2019.  
   Relevance: explicit treatment of terminology and Russian rendering of vector/semantic representation concepts.
4. А. И. Панченко — «Методы и алгоритмы для извлечения, связывания, векторизации и разрешения неоднозначности лексико-семантических графов», докторская диссертация, НИУ ВШЭ, 2024.  
   Relevance: Russian-language computational lexical semantics and vector representation terminology.

These works are terminology/structural reference points, not sources that automatically determine terminology for the present dissertation. Terminology must still preserve the exact methodological meaning used in the IR literature.

## Core rule

For a specialized term in dissertation text:

1. introduce the concept in Russian when a verified Russian form exists;
2. when useful for unambiguous identification, give the English original in parentheses;
3. afterwards use the selected Russian form or established abbreviation consistently;
4. retain English unchanged for official model, algorithm, dataset, resource and named-method identifiers when translation would obscure identity or meaning;
5. if a stable Russian equivalent has not been verified, do not create one ad hoc: retain the international term and explain its function in Russian;
6. preserve source-specific metric and method names when translating them would change identification or methodological meaning.

Example:

> Плотный векторный поиск (dense retrieval) представляет запрос и документы плотными числовыми векторами. Далее: «плотный поиск».

## Preferred terminology

| English / mixed form | Preferred dissertation form |
|---|---|
| lexical retrieval | лексический поиск |
| semantic retrieval | семантический поиск |
| hybrid retrieval / hybrid search | гибридный поиск |
| dense retrieval | плотный векторный поиск (dense retrieval) → далее плотный поиск |
| sparse retrieval | разреженный поиск (sparse retrieval) → далее разреженный поиск |
| retrieval effectiveness | эффективность информационного поиска |
| retrieval model | модель информационного поиска / поисковая модель |
| retrieval system | информационно-поисковая система / поисковая система |
| retrieval evaluation | оценка эффективности информационного поиска |
| retrieval dataset | набор данных для информационного поиска |
| retrieval task | задача информационного поиска |
| retrieval score | оценка соответствия → далее оценка, если контекст однозначен |
| matching | сопоставление |
| lexical matching | лексическое сопоставление |
| semantic matching | семантическое сопоставление |
| representation | представление |
| dense representation | плотное векторное представление |
| distributed representation | распределённое представление |
| dataset | набор данных |
| baseline | базовый метод / базовая модель |
| relevance judgments | оценки релевантности / разметка релевантности |
| objective | целевая функция обучения |
| domain | предметная область |
| query–document pair | пара «запрос–документ» |
| query–document ranking | ранжирование документов по запросу |
| benchmark | бенчмарк (benchmark) → далее бенчмарк |
| benchmarking (model comparison context) | сравнительная оценка |
| ad hoc retrieval | поиск по произвольному запросу (ad hoc retrieval) |
| vocabulary mismatch | проблема несоответствия словарей запроса и документа |
| stemming | стемминг |
| lemmatization | лемматизация |
| Transformer | Трансформер / архитектура Трансформер |
| cross-encoder | кросс-энкодер (cross-encoder) |
| bi-encoder | би-энкодер (bi-encoder) |
| dual-encoder when used as an alternative name for the same architecture | при первом вводе можно указать: би-энкодер (bi-encoder, также dual-encoder) |
| encoder | энкодер |
| dense retriever | плотный нейросетевой ретривер / модель плотного поиска — по контексту |
| reranking | переранжирование (reranking) → далее переранжирование |
| reranker | переранжировщик |
| late interaction | позднее взаимодействие (late interaction) → далее позднее взаимодействие |
| multi-vector model | многовекторная модель |
| token-level | на уровне токенов |
| approximate nearest-neighbor search | приближённый поиск ближайших соседей (ANN) |
| hard negative | отрицательный пример повышенной сложности (hard negative) |
| multilingual model | многоязычная модель |
| monolingual model | одноязычная модель |
| cross-lingual transfer | межъязыковой перенос |
| cross-lingual transfer learning | межъязыковой перенос обучения |
| pretrained model | предварительно обученная модель |
| pretraining | предварительное обучение |
| out-of-vocabulary / OOV | внесловарный |
| embedding | эмбеддинг / векторное представление — выбирать по функции термина в конкретном контексте |
| word embeddings | эмбеддинги слов / векторные представления слов |
| semantic similarity | семантическая близость |
| semantic relatedness | семантическая связанность |
| synset | синсет |
| masked language modeling / MLM | маскированное языковое моделирование (MLM) |
| sentiment analysis | анализ тональности |
| named entity recognition / NER | распознавание именованных сущностей (NER) |
| Spearman correlation | коэффициент ранговой корреляции Спирмена |
| ablation analysis | абляционный анализ |
| complementarity | взаимодополняемость |
| convex combination | выпуклая комбинация |
| score-level fusion | объединение на уровне оценок (score-level fusion) |
| rank-level fusion | объединение ранжированных списков (rank-level fusion) |
| hybrid retrieval + reranking | гибридный поиск с переранжированием |
| pairwise | попарный |
| pairwise matching | попарное сопоставление |
| representation-level integration | интеграция на уровне представлений |
| query-dependent | запросозависимый; в сложных фразах предпочтительно описывать действие: «выбор стратегии в зависимости от запроса» |
| low-resource language | язык с ограниченными ресурсами |
| framework | фреймворк — допустимый академический термин |
| ontology | онтология |
| legal QA / legal question answering | вопросно-ответная система / задача в юридической предметной области — по контексту |
| hybrid system pipeline | многоэтапный конвейер поиска; «пайплайн» также академически употребим, но не является формой по умолчанию |

## Terms requiring special handling

These terms are considered resolved not by assigning an invented Russian equivalent, but by defining an explicit usage rule.

### Learned Sparse Retrieval

`learned sparse retrieval` does not currently have a sufficiently stable single Russian equivalent in the checked literature.

Use:

> **Learned Sparse Retrieval (LSR)**

at first introduction, with a concise Russian explanation of the class. Afterwards use:

> **LSR-модели**, **обучаемые разреженные модели**, or **модели данного класса**

when the context is unambiguous.

Do **not** treat «обучаемый разреженный поиск» as an established normative Russian translation.

### Single-vector bi-encoder

No sufficiently stable Russian technical term was verified for `single-vector bi-encoder`.

Do not standardize «одновекторный би-энкодер» as a normative term.

Prefer an explanatory form such as:

> **би-энкодер, формирующий одно векторное представление текста**

when a Russian explanation is needed.

### Fine-grained

`fine-grained` has no single universal Russian equivalent across the checked literature.

Translate only according to the source-specific meaning, for example:

- детальный;
- локальный;
- на уровне отдельных элементов.

Do not create a one-to-one dictionary rule.

### Retrieval-oriented

`retrieval-oriented` should normally not be calqued as a standalone Russian term.

Rewrite the phrase according to meaning, for example:

- для задачи информационного поиска;
- в задаче информационного поиска;
- оценка непосредственно в постановке информационного поиска;
- обучающие данные для информационного поиска.

### Query-adaptive fusion

Do not standardize an invented Russian technical label for `query-adaptive fusion`.

When referring to the named method, retain:

> **Query-Adaptive Hybrid Search**

and explain the mechanism in Russian, e.g. that the balance or coefficient between search components is determined separately for each query.

### Query-aware

No single normative Russian technical equivalent is fixed.

Use a source-faithful descriptive form such as:

> **с учётом характеристик запроса**

only when that meaning is actually supported by the method being described.

### Entity-centric

No sufficiently stable Russian IR term is fixed.

Do not introduce an artificial one-word equivalent. Describe the actual query type or experimental setting in Russian.

### Unified multi-function retrieval

Do not create a new Russian taxonomy label unless the source itself motivates it.

For BGE-M3 prefer factual description, for example:

> **модель поддерживает плотный, разреженный и многовекторный режимы поиска**.

### Ontological reranking

Do not standardize a standalone Russian term before the source-specific O-RAG mechanism is verified from the full method description.

If the source supports the interpretation, explanatory prose may say:

> **переранжирование с использованием онтологии**.

### Attentional representations

No standalone Russian term is standardized.

If the source meaning requires explanation, describe the representation through the **механизм внимания** rather than inventing a calque.

### Semantic Textual Similarity

Because Russian usage is not fully uniform, preserve the international task name at first introduction:

> **Semantic Textual Similarity (STS)**

and explain it as:

> **задача оценки семантической близости текстов**.

Afterwards use **STS** when unambiguous.

### Source-specific metrics

Do not independently translate names of metrics when the original label identifies a specific reported measure.

Examples:

- Hit Rate;
- Citation Accuracy;
- top-20 passage retrieval accuracy;
- MLM accuracy.

Explain the metric in Russian only after verifying its definition in the primary source.

## Official names retained unchanged

BM25, TF-IDF, BERT, DPR, ANCE, Contriever, ColBERT, DeepImpact, SPLADE, CLEAR, BGE-M3, UZWORDNET, UzBERT, BERTbek, SimRelUz, MIRACL, Reciprocal Rank Fusion (RRF), Dense Passage Retrieval, Dense Lexical Representation, Dense Hybrid Representation, Query-Driven Alpha Prediction, Query-Adaptive Hybrid Search, EntityQuestions and other official model, dataset, resource and named-method identifiers.

After a named English construct is introduced, explanatory prose should return to Russian where possible.

## Important wording distinctions

- A retrieval score is not automatically model confidence. Prefer **«оценка соответствия»** unless a source explicitly defines calibrated confidence/probability.
- Terminological Russianization must not blur methodological boundaries:
  - STS ≠ corpus-level IR;
  - retrieval ≠ reranking;
  - IR ≠ RAG;
  - RAG answer quality ≠ retrieval effectiveness;
  - language model / embedding model ≠ retriever;
  - sparse/dense representation ≠ neural/non-neural learning method.
- `embedding` may legitimately be rendered as **эмбеддинг** or **векторное представление** depending on the scientific function of the term; do not replace mechanically.
- `reranking` has multiple attested Russian variants, but this dissertation uses **переранжирование** consistently as its house form.
- `pretrained` also has multiple attested Russian variants; this dissertation uses **предварительно обученный** consistently as its house form.
- `pipeline` and **пайплайн** are attested in Russian academic practice; this dissertation prefers **многоэтапный конвейер поиска** when a Russian descriptive form is natural.

## Conversation vs dissertation

When explaining research to the user: simple explanation first, short example if useful, then the formal term.

When writing dissertation text: concise academic Russian; explain only enough to make the term unambiguous and readable, without turning the chapter into a textbook.

## Verification rule for new terminology

Before adding a new specialized term to `Preferred terminology`:

1. check real Russian-language dissertations, author abstracts or comparable peer-reviewed scientific works;
2. distinguish established Russian usage from machine translation, documentation-only wording or an isolated calque;
3. preserve the original methodological meaning;
4. if no stable equivalent is supported, add an explicit handling rule instead of inventing a translation;
5. record any house-style choice separately from claims about universal correctness.

## Final terminology pass

Before a section is considered final:

- main prose is Russian;
- specialized terms have consistent first-use forms;
- unnecessary English descriptive words are removed;
- official names remain unchanged;
- one selected form is used consistently after introduction;
- unsupported literal translations are not introduced;
- source-specific terms and metrics preserve their identity;
- translation does not change scientific meaning;
- terminology is consistent across text, tables, formulas and conclusions.
