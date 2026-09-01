# Dissertation Terminology Guide

**Status:** ACTIVE

**Established:** 2026-09-01

## Purpose

Normative terminology policy for the Russian-language PhD dissertation:

> **Гибридный подход к поиску информации на узбекском языке на основе интеграции лексических и семантических методов.**

The main scientific prose must remain Russian while preserving precise international IR/NLP terminology.

## Evidence basis

The policy follows terminology practice observed in real Russian-language dissertations close to information retrieval, NLP and vector semantics, including works by P. I. Braslavskiy, A. V. Pugachev, A. A. Potapenko and A. I. Panchenko.

Observed pattern:

1. Russian is the main scientific language.
2. The English original may be given at first introduction for identification and precision.
3. Subsequent prose normally uses the Russian form or an established abbreviation.
4. Official names of models, algorithms and resources remain unchanged.
5. English descriptive words should not be inserted into Russian sentences when a clear Russian scientific equivalent exists.

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

1. introduce the concept in Russian;
2. when useful for unambiguous identification, give the English original in parentheses;
3. afterwards use the Russian form or established abbreviation consistently;
4. retain English unchanged for official model, algorithm, resource and named-method identifiers when translation would obscure identity or meaning.

Example:

> Плотный векторный поиск (dense retrieval) представляет запрос и документы плотными числовыми векторами. Далее: «плотный поиск».

## Preferred terminology

| English / mixed form | Preferred Russian form |
|---|---|
| lexical retrieval | лексический поиск |
| semantic retrieval | семантический поиск |
| hybrid retrieval | гибридный поиск |
| dense retrieval | плотный векторный поиск (dense retrieval) → далее плотный поиск |
| sparse retrieval | разреженный поиск (sparse retrieval) → далее разреженный поиск |
| learned sparse retrieval | обучаемый разреженный поиск (learned sparse retrieval) |
| retrieval effectiveness | эффективность поиска |
| retrieval model | поисковая модель |
| retrieval system | поисковая система |
| retrieval evaluation | оценка эффективности поиска |
| retrieval dataset | набор данных для информационного поиска |
| matching | сопоставление |
| lexical matching | лексическое сопоставление |
| semantic matching | семантическое сопоставление |
| representation | представление |
| dense representation | плотное векторное представление |
| distributed representation | распределённое представление |
| pipeline | схема / процесс / многоэтапная схема поиска |
| objective | целевая функция обучения |
| relevance judgments | оценки релевантности / разметка релевантности |
| baseline | базовый метод / базовая модель |
| dataset | набор данных |
| reranking | повторное ранжирование (reranking) → далее повторное ранжирование |
| cross-encoder | кросс-энкодер (cross-encoder) |
| hard negative | сложный отрицательный пример (hard negative) |
| embedding | векторное представление (embedding), если английский термин нужен для идентификации |
| domain | предметная область |
| query–document pair | пара «запрос–документ» |

## Official names retained unchanged

BM25, TF-IDF, BERT, DPR, ANCE, Contriever, ColBERT, DeepImpact, SPLADE, CLEAR, BGE-M3, UZWORDNET, UzBERT, BERTbek, SimRelUz, MIRACL, Reciprocal Rank Fusion (RRF), and named constructs such as Dense Lexical Representation, Dense Hybrid Representation and Query-Driven Alpha Prediction when referring to the original method.

After a named English construct is introduced, explanatory prose should return to Russian where possible.

## Important wording distinctions

- A retrieval score is not automatically model confidence. Prefer «оценка соответствия» unless a source explicitly defines calibrated confidence/probability.
- Terminological Russianization must not blur methodological boundaries: STS ≠ corpus-level IR; retrieval ≠ reranking; RAG answer quality ≠ retrieval effectiveness; language/embedding model ≠ retriever.

## Conversation vs dissertation

When explaining research to the user: simple explanation first, short example if useful, then the formal term.

When writing dissertation text: concise academic Russian; explain only enough to make the term unambiguous and readable, without turning the chapter into a textbook.

## Pending terminology decisions

Do not silently standardize these until separately agreed:

- bi-encoder: «би-энкодер» vs «двойной энкодер»;
- benchmark: «бенчмарк» vs a Russian descriptive form depending on context;
- encoder: «энкодер» vs «кодировщик»;
- late interaction: preferred stable Russian rendering;
- score-level fusion / rank-level fusion: preferred stable Russian labels;
- query-adaptive fusion: preferred stable Russian label.

## Final terminology pass

Before a section is considered final:

- main prose is Russian;
- specialized terms have consistent first-use forms;
- unnecessary English descriptive words are removed;
- official names remain unchanged;
- one form is used consistently after introduction;
- translation does not change scientific meaning;
- terminology is consistent across text, tables, formulas and conclusions.
