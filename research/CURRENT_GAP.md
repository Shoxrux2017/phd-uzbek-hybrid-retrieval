# Current Research Gap

**Status:** provisional / working
**Current version:** v0.8 refined
**Evidence cut-off:** 2026-09-10
**Do not treat as final novelty.**

## Current formulation

> **Несмотря на то что в современных исследованиях морфологически богатых языков уже одновременно сравниваются различные варианты морфологической обработки лексического поиска, современные модели плотного поиска и способы их гибридного использования, недостаточно установлено, как изменение морфологического представления лексического канала изменяет саму структуру его взаимодополняемости с семантическим поиском. Для узбекского языка, в частности, не установлено в единой контролируемой задаче ранжирования документов, как переход от исходных словоформ к стеммам и леммам изменяет набор уникально найденных релевантных документов, степень перекрытия с фиксированной моделью плотного поиска и дополнительный эффект гибридного поиска, а также как эти изменения связаны с морфологическими, графическими и лексико-структурными характеристиками запросов.**

## Что изменилось относительно v0.4

Версия v0.4 была сформулирована шире: она концентрировалась на недостаточно изученной взаимодополняемости лексического и семантического поиска для Uzbek, влиянии морфологической нормализации и характеристик запроса.

После targeted deep dives и gap-killer search 2026-09-10 выяснилось, что отдельные части этой постановки уже существенно заняты литературой:

- Uzbek hybrid/RAG уже существует;
- Uzbek semantic retrieval уже существует;
- Uzbek morphology давно используется в поисковой/NLP-инфраструктуре;
- в Uzbek manuscript-level evidence уже описано сочетание лемматизированного BM25, LaBSE и адаптивного hybrid/graph retrieval;
- `raw/stem/lemma` уже сравнивались в low-resource document retrieval (UPERF, Urdu);
- morphology-aware BM25 уже сравнивался с современными embedding models и использовался в hybrid retrieval (Aboasal et al., Arabic legal IR);
- современные работы уже ставят рядом несколько morphology-sensitive BM25 pipelines, modern dense retrievers и sparse–dense fusion (GreekBarRetrieval, Greek);
- query-dependent retrieval/fusion и query-type analysis уже существуют как общие идеи;
- lexical–semantic complementarity уже является самостоятельным объектом международного IR research.

Поэтому gap теперь строится не вокруг наличия компонентов, а вокруг **неисследованного взаимодействия факторов**.

## Центральное различие

Текущий вопрос не:

> «Помогает ли стемминг/лемматизация?»

и не:

> «Что лучше — BM25 или плотный поиск?»

и не:

> «Помогает ли hybrid?»

Эти вопросы уже исследовались в других языках и частично в Uzbek-related работах.

Текущий вопрос:

> **Как изменение морфологического представления Uzbek lexical channel изменяет то, какие релевантные документы остаются уникальными для lexical и semantic retrieval и, следовательно, изменяет дополнительную полезность их гибридного использования?**

Именно эта `morphological representation → complementarity change` связь является текущим residual gap.

## Что литература уже не позволяет утверждать

Нельзя строить gap/новизну на тезисах:

- «для Uzbek hybrid retrieval отсутствует»;
- «для Uzbek semantic retrieval отсутствует»;
- «морфология ранее не применялась к Uzbek search»;
- «raw/stem/lemma ранее не сравнивались в low-resource IR»;
- «morphology-aware BM25 не сравнивали с semantic embeddings»;
- «morphology-aware lexical + semantic hybrid retrieval отсутствует»;
- «RRF / fixed weighted fusion — новая идея»;
- «dynamic `alpha(q)` / query-dependent strategy — новая идея»;
- «query-type analysis lexical vs semantic — новая идея»;
- «взаимодополняемость lexical и semantic retrieval сама по себе ранее не исследовалась».

## Evidence boundary

Подробный синтез evidence, который привёл к этой формулировке:

- `research/GAP_BOUNDARY_2026-09-10.md`

Ключевые новые gap-boundary cards:

- `literature/deep-dives/2024_Kazi_Khoja_UPERF_Urdu_Retrieval.md`
- `literature/deep-dives/2026_Aboasal_Arabic_Legal_IR_Morphology_Semantic.md`
- `literature/deep-dives/2026_Beta_GreekBarRetrieval.md`
- `literature/deep-dives/2026_Sharifbaev_Uzbek_Legal_Hybrid_Retrieval_Manuscript.md`

## Важное уточнение о morphology

Morphology по-прежнему **не фиксируется как третий независимый retrieval paradigm**.

Рабочая логика:

`Lexical_raw → Lexical_stem → Lexical_lemma`

Это альтернативные варианты формирования лексического представления.

Затем каждый вариант сравнивается и интегрируется с одной и той же семантической моделью.

Если эксперименты покажут, что raw/stem/lemma lexical representations дают устойчиво независимые полезные результаты, архитектурное решение может быть расширено. Это пока не предполагается заранее.

## Минимальная controlled experimental logic

Чтобы действительно проверить текущий gap, основной анализ должен удерживать semantic comparator постоянным.

### Lexical variants

`BM25_raw`
`BM25_stem`
`BM25_lemma`

Дополнительный простой control при необходимости:

`BM25_simple-normalization`.

### Fixed dense comparator

Пусть `D` — выбранная современная retrieval-trained multilingual модель плотного поиска.

Для причинной интерпретации morphology-effect модель `D` должна быть одной и той же для всех основных сравнений.

### Hybrid conditions

`H_raw = fusion(BM25_raw, D)`
`H_stem = fusion(BM25_stem, D)`
`H_lemma = fusion(BM25_lemma, D)`.

Fusion/normalization protocol также должен быть зафиксирован или настраиваться только на validation set.

## Что нужно измерять кроме aggregate metrics

Одних MAP/nDCG/Recall недостаточно для основного объяснительного вклада.

Для каждого запроса желательно измерять:

- effectiveness lexical component;
- effectiveness dense component;
- effectiveness hybrid condition;
- релевантные документы, найденные только lexical component;
- релевантные документы, найденные только dense component;
- пересечение релевантных результатов;
- объединение/oracle upper bound;
- incremental hybrid gain;
- изменение этих величин при переходе `raw → stem → lemma`.

Статистическая проверка должна проводиться на уровне запросов, если размер и структура benchmark это позволяют.

## Какие характеристики запроса рассматриваются как кандидаты

Это **не доказанные причины**, а признаки для проверки:

- морфологическая вариативность;
- количество/тип аффиксальных форм;
- proxy морфологической сложности;
- rare terms;
- named entities;
- числа/идентификаторы/названия;
- Latin/Cyrillic variation;
- Unicode/apostrophe variation, если релевантно корпусу;
- длина запроса;
- степень lexical overlap;
- paraphrastic/описательная формулировка;
- domain.

Новизна не должна формулироваться как «впервые анализируем query types». Значение имеет только их связь с **изменением complementarity вследствие morphological representation**.

## Gap ≠ solution

Текущий gap не означает, что решение обязано быть adaptive fusion, learned routing или новая neural architecture.

Сначала необходимо установить саму закономерность.

Возможная будущая гипотеза может возникнуть только после baseline evidence, например:

> если morphology-induced complementarity shift систематически связан с определёнными Uzbek query features, использование этой информации может улучшить стратегию интеграции.

Это пока **гипотеза**, а не доказанный результат и не зафиксированная новизна.

## What can still kill this gap

Gap необходимо пересмотреть снова, если новые evidence покажут хотя бы одно из следующего:

1. Для Uzbek уже существует controlled benchmark, где `BM25_raw/stem/lemma` сравниваются с одной и той же современной dense model и несколькими fusion conditions.
2. Уже выполнен Uzbek per-query overlap/unique-hit/oracle analysis, показывающий morphology-induced lexical–dense complementarity changes.
3. Очень близкая работа для другого агглютинативного Turkic language полностью закрывает тот же interaction mechanism и есть сильное основание считать перенос на Uzbek прямым.
4. Собственные baseline experiments показывают, что `raw/stem/lemma` практически не меняют lexical–semantic complementarity или эффект нестабилен.

## Evidence reliability cautions

- Sharifbaev 2026 dissertation manuscript — **D** until official final/defense evidence is verified.
- GreekBarRetrieval — **C** while it remains an arXiv preprint in the project evidence hierarchy.
- Aboasal et al. — **B**; current project card is intentionally limited to what is verified from official metadata/abstract where full methods were not recovered.
- UPERF — **B**; full paper inspected, but the main evaluation is Recall@5 and inferential significance details are unclear.

## Current stopping decision

Broad gap-search has reached **provisional saturation** as of 2026-09-10.

The next phase should prioritize:

1. research questions;
2. testable hypotheses;
3. benchmark/qrels design;
4. selection of fixed modern dense baseline(s);
5. controlled morphology baselines;
6. pilot experiments testing whether morphology-induced complementarity change actually exists.

Broad literature search should resume only when a new direct gap killer, new 2026 publication, or experimental result requires reassessment.
