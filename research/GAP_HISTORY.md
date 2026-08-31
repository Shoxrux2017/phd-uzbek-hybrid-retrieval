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

## v0.4 — current (2026-08-31)

**Current gap:** недостаточно изучены закономерности взаимодополняемости lexical и semantic retrieval для Uzbek query–document ranking, включая влияние морфологической нормализации на лексическое представление и влияние характеристик запроса на относительную полезность компонентов.

Ключевое изменение:

- Gap = **отсутствующее знание/закономерность**.
- Adaptive fusion = **возможная гипотеза/метод**, только если закономерность будет подтверждена.

См. `CURRENT_GAP.md`.

## Правило дальнейших изменений

При новой версии обязательно записать:

1. новую формулировку;
2. какие новые evidence появились;
3. почему старая версия стала недостаточной/ошибочной;
4. какие последствия это имеет для главы I, RQ, гипотезы и будущей модели.
