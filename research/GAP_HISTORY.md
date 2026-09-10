# Research Gap History

Этот файл сохраняет эволюцию научной позиции. Старые версии не следует удалять только потому, что они оказались слишком широкими.

## v0.1 — ранняя рабочая идея

**Предположение:** гибридный lexical–semantic retrieval для узбекского языка практически отсутствует.

**Почему отклонено:** найдены Uzbek hybrid/RAG работы USHRA и O-RAG. Следовательно, утверждение «hybrid search для Uzbek нет» стало некорректным.

---

## v0.2 — general-purpose hybrid gap

**Рабочая формулировка:** международный hybrid retrieval развит, а для Uzbek general-purpose hybrid IR недостаточно исследован; существующие решения в основном domain-specific.

**Почему потребовалось уточнение:** в 2026 году найдены работы, показывающие реальный corpus-level semantic retrieval Uzbek text по стандартным IR-метрикам (Ishkobilov et al.) и Uzbek semantic retrieval в SIGTURK benchmark. Нельзя строить аргумент на отсутствии retrieval evaluation вообще.

---

## v0.3 — morphology-aware/query-dependent direction

**Рабочая идея:** исследовать surface lexical + morphology-aware lexical + semantic и адаптивно выбирать их веса.

**Почему скорректировано:** мировая литература уже содержит query-dependent strategy selection и Query-Adaptive Hybrid Search с `alpha(q)`. Кроме того, morphology-aware Uzbek semantic similarity уже существует. Само наличие dynamic alpha или morphology + semantics не является достаточной новизной.

---

## v0.4 — 2026-08-31

**Рабочий gap:** недостаточно изучены закономерности взаимодополняемости lexical и semantic retrieval для Uzbek query–document ranking, включая влияние морфологической нормализации на лексическое представление и влияние характеристик запроса на относительную полезность компонентов.

Ключевое изменение:

- Gap = **отсутствующее знание/закономерность**.
- Adaptive fusion = **возможная гипотеза/метод**, только если закономерность будет подтверждена.

**Почему v0.4 стал слишком широким:** targeted literature analysis 2026-09-10 показал, что отдельные компоненты этой постановки уже существенно заняты как Uzbek, так и международной литературой.

---

## v0.5 — промежуточное сужение, 2026-09-10

**Триггер:** targeted deep dive пользовательского full-text manuscript Шарифбаева А.Н. (2026).

Manuscript описывает:

- Uzbek/Russian legal corpus;
- лемматизированный BM25;
- LaBSE dense retrieval;
- graph retrieval;
- адаптивный GraphRAG-RL controller.

**Вывод:** даже для Uzbek уже нельзя безопасно утверждать отсутствие morphology-aware BM25 + dense hybrid retrieval или query-dependent retrieval strategy.

**Почему версия не стала текущей:** manuscript имеет D-reliability до официальной проверки, а международный gap-search показал ещё более близкие peer-reviewed аналоги.

---

## v0.6 — промежуточное сужение после UPERF / Urdu evidence

**Триггер:** Kazi & Khoja, UPERF (PACLIC 2024) и Kazi & Khoja, U-RR² (*Computer Speech & Language*, 2026).

UPERF уже сравнивает:

`raw ↔ stemmed ↔ lemmatized`

для BM25, TF-IDF и embedding-based representations, а также single-word vs multiple-word queries и weighted lexical–semantic combination.

U-RR² дополнительно показывает mature Urdu document retrieval с несколькими benchmark collections и learned lexical–semantic reranking.

**Вывод:** нельзя строить мировой gap на тезисе, что morphology + lexical + semantic retrieval или raw/stem/lemma analysis в low-resource IR ранее отсутствуют.

---

## v0.7 — промежуточное сужение после Arabic legal IR

**Триггер:** Aboasal et al. (2026), *Arabic Legal Information Retrieval: The Impact of Morphological Segmentation and Semantic Embeddings*.

Verified official abstract показывает:

- BM25;
- Farasa morphology;
- modern embeddings, включая BGE-M3/GTE/Ada/Mistral-embed;
- hybrid `BM25(Farasa) + Ada v3`;
- MAP/nDCG improvements.

**Вывод:** broad claim “morphology-aware BM25 + modern semantic embeddings + hybrid retrieval has not been studied” также отвергнут.

**Residual idea:** не само сочетание компонентов, а влияние morphology на структуру lexical–dense complementarity.

---

## v0.8 — current refined gap, 2026-09-10

**Триггер:** aggressive gap-killer search + targeted GreekBarRetrieval analysis.

GreekBarRetrieval (Beta et al., 2026 preprint) уже ставит в одной retrieval benchmark постановке:

- три BM25 preprocessing variants (stemming, lemmatization, minimal/tokenization-oriented processing);
- девять modern dense retrievers;
- sparse–dense fusion;
- query reformulation;
- nDCG/MAP/Recall.

Следовательно, даже экспериментальная матрица “different morphology-aware BM25 variants + modern dense + fusion” недостаточна как новизна.

### Current formulation

> **Несмотря на то что в современных исследованиях морфологически богатых языков уже одновременно сравниваются различные варианты морфологической обработки лексического поиска, современные модели плотного поиска и способы их гибридного использования, недостаточно установлено, как изменение морфологического представления лексического канала изменяет саму структуру его взаимодополняемости с семантическим поиском. Для узбекского языка, в частности, не установлено в единой контролируемой задаче ранжирования документов, как переход от исходных словоформ к стеммам и леммам изменяет набор уникально найденных релевантных документов, степень перекрытия с фиксированной моделью плотного поиска и дополнительный эффект гибридного поиска, а также как эти изменения связаны с морфологическими, графическими и лексико-структурными характеристиками запросов.**

### Ключевое изменение относительно v0.4

Research gap теперь определяется не наличием/отсутствием методов, а **interaction/decomposition question**:

`morphological representation change`

→ `change in lexical retrieval behavior`

→ `change in lexical–dense overlap / unique relevant hits`

→ `change in incremental hybrid gain`

→ `relation to Uzbek query characteristics`.

### Что уже не является новизной

- `raw/stem/lemma` comparison сам по себе;
- morphology-aware BM25 сам по себе;
- BM25 vs dense comparison;
- BM25 + dense fusion;
- RRF / fixed weighted fusion;
- query-dependent alpha/strategy;
- general query-type analysis;
- complementarity as a general idea.

### Что пока не найдено

Прямой verified аналог для Uzbek, который одновременно:

1. меняет только lexical morphology representation (`raw/stem/lemma`);
2. удерживает один и тот же modern dense retriever;
3. удерживает controlled fusion protocol;
4. измеряет unique relevant hits / overlap / oracle union / incremental hybrid gain;
5. связывает изменения с interpretable Uzbek morphological/script/query features.

См. `CURRENT_GAP.md` и `GAP_BOUNDARY_2026-09-10.md`.

---

## Правило дальнейших изменений

При новой версии обязательно записать:

1. новую формулировку;
2. какие новые evidence появились;
3. почему старая версия стала недостаточной/ошибочной;
4. какие последствия это имеет для главы I, RQ, гипотезы и будущей модели.

Если собственные baseline experiments покажут, что morphology не меняет lexical–semantic complementarity устойчивым образом, v0.8 также должен быть пересмотрен.
