# Национальная матрица evidence для PhD по Uzbek hybrid retrieval

**Дата:** 2026-09-14  
**Статус:** рабочий исследовательский синтез, не финальная формулировка научной новизны.

## Итоговая национальная матрица

| Блок | Что уже установлено для Uzbek | Ключевое evidence | Надёжность | Что ещё не установлено | Влияние на v0.8 |
|---|---|---|---|---|---|
| Морфологический анализ | Computational morphology для Uzbek существует; анализаторы, словари и правила разработаны | Bakaev; Elov; IL-402104209 | A/B | Не центральный вопрос текущей новизны | Широкий gap «нет morphology» закрыт |
| Стемминг | Uzbek stemmer разработан и проверен на уровне определения основы | Bakaev; Xusainova | A | Нет qrels-based `BM25_raw ↔ BM25_stem` для современной Uzbek IR-задачи | v0.8 открыт |
| Лемматизация | Uzbek lemmatizers и lexical resources существуют | Xusainova; Turayev; Elov | A/B | Нет controlled `BM25_raw ↔ BM25_stem ↔ BM25_lemma` на одной collection/qrels | v0.8 открыт |
| Morphology-aware search | Stemming/lemmatization применялись в full-text, corpus и library/search contexts | Bakaev; Xusainova | A | Практические claims не дают современной MAP/nDCG/Recall/qrels оценки morphology-effect | Нельзя заявлять «впервые morphology в Uzbek search» |
| Семантическая инфраструктура | Embeddings, BERT-like models, lexical-semantic resources, sentence semantics, paraphrase/context processing существуют | UZWORDNET, UzBERT/BERTbek, Akhmedova, Axmedova, Abdisalomova | A/B/C | Semantic NLP ≠ modern dense retrieval effectiveness | Широкий gap «нет semantic NLP» закрыт |
| Corpus-level semantic retrieval | Для Uzbek есть query→ranked-passage retrieval со стандартными IR-метриками | Ishkobilov et al. 2026 | B | Нет BM25, raw/stem/lemma, modern retrieval-trained dense, fusion/complementarity decomposition | Нельзя заявлять «нет Uzbek semantic retrieval» |
| BM25 vs vector search | Такое сравнение уже существует в Uzbek RAG literature | Urinov 2025 | C | Полный qrels/metrics/vector model и genuine fusion не подтверждены | Само сравнение BM25 vs vector не новизна |
| Uzbek hybrid retrieval / RAG | Опубликованные hybrid/RAG systems существуют | USHRA, ACM ICFNDS’25 | B | Exact fusion и pure-IR metrics не подтверждены; answer accuracy ≠ retrieval effectiveness | Широкий gap «нет Uzbek hybrid» закрыт |
| Ontology-enhanced hybrid / reranking | Ontology и ontology-based reranking применены для Uzbek legal RAG | O-RAG, ACM ICFNDS’25 | B | Вклад fusion отдельно от ontology/reranker без ablation не установлен | Ontology/reranking сами по себе не новизна |
| Morphology-aware BM25 + semantic retrieval | Есть близкое manuscript-level описание: lemmatized BM25 + LaBSE + graph/adaptive retrieval | Sharifbaev 2026 manuscript | D | Источник не верифицирован; нет raw/stem/lemma × same D decomposition | Сильный gap-killer lead, но v0.8 не закрывает |
| Lexical–semantic complementarity | Общая идея известна; национальные работы подтверждают наличие обоих каналов | International hybrid IR + Uzbek retrieval/RAG | A/B | Для Uzbek не найден lexical-only/dense-only/intersection/oracle анализ при controlled morphology change | Ядро residual gap |
| Morphology-induced complementarity change | В национальном evidence не найдено | — | — | Не установлено, как raw→stem→lemma меняет unique hits, overlap и hybrid gain при fixed D | **Центральная часть v0.8 открыта** |
| Связь с типом Uzbek запроса | Отдельные query effects известны, но не найден controlled Uzbek анализ именно этой связи | — | — | Нет цепочки `morphology change → complementarity change → query features` | **Объяснительная часть v0.8 открыта** |

## Национальная цепочка

```text
Bakaev
morphology → full-text/library search
        ↓
Xusainova
tokenizer + stemmer + lemmatizer → corpus/search optimization
        ↓
Ishkobilov
lexical vs semantic retrieval → standard IR metrics
        ↓
Urinov
BM25 vs vector search in Uzbek RAG
        ↓
USHRA
hybrid semantic retrieval + RAG
        ↓
O-RAG
hybrid retrieval + ontology + reranking
        ↓
Sharifbaev (D-level manuscript)
lemmatized BM25 + LaBSE + graph/adaptive retrieval
```

После этой цепочки остаётся не вопрос **«есть ли компоненты?»**, а вопрос **«как morphology меняет взаимодействие компонентов?»**

## Остаточный вопрос

```text
BM25_raw
BM25_stem
BM25_lemma
        │
        └── сравниваются с одной и той же fixed dense model D
                         │
                         ▼
             lexical-only relevant hits
             dense-only relevant hits
             intersection
             oracle union
                         │
                         ▼
             incremental hybrid gain
                         │
                         ▼
             relation to Uzbek query morphology /
             script / rare terms / named entities /
             lexical overlap / paraphrasing
```

## Минимальный controlled design

```text
Lexical:
BM25_raw
BM25_stem
BM25_lemma

Semantic:
одна фиксированная retrieval-trained multilingual dense model D

Hybrid:
H_raw   = fusion(BM25_raw, D)
H_stem  = fusion(BM25_stem, D)
H_lemma = fusion(BM25_lemma, D)
```

Нужно измерять aggregate effectiveness (MAP/nDCG/Recall@k), per-query gains/losses, lexical-only и dense-only relevant hits, intersection, oracle union, incremental hybrid gain и статистическую связь этих изменений с характеристиками Uzbek-запросов.

## Вывод

Национальный поиск литературы можно считать **provisionally saturated для текущего broad-gap вопроса**. В Узбекистане уже есть morphology/search infrastructure, semantic retrieval, BM25-vs-vector evidence, hybrid/RAG и ontology-enhanced reranking.

Но в изученном evidence не обнаружен controlled Uzbek experiment, который фиксирует dense comparator и измеряет, как переход `raw → stem → lemma` меняет структуру lexical–semantic complementarity.

Поэтому `research gap v0.8 refined` пока сохраняется, но остаётся provisional и должен быть проверен собственным baseline/pilot experiment до формулирования окончательной научной новизны.

## Следующий научный шаг

`research questions → falsifiable hypotheses → benchmark/qrels protocol → baseline experiment`

Если pilot покажет, что `raw/stem/lemma` почти не меняют complementarity, v0.8 нужно пересмотреть до разработки нового метода.
