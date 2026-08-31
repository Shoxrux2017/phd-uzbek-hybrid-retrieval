# Current Research Gap

**Status:** provisional / working  
**Evidence cut-off:** 2026-08-31  
**Do not treat as final novelty.**

## Current formulation

> **Несмотря на наличие исследований морфологически ориентированного лексического поиска, семантического retrieval и отдельных гибридных RAG-систем для узбекского языка, недостаточно изучены закономерности взаимодополняемости лексического и семантического способов сопоставления в задаче ранжирования узбекских текстов, включая влияние морфологической нормализации на лексическое представление. В частности, недостаточно установлено, как языковые и структурные характеристики пользовательского запроса влияют на относительную эффективность этих поисковых компонентов и при каких условиях их совместное использование обеспечивает устойчивое улучшение относительно отдельных методов.**

## Почему gap сформулирован именно так

Литература уже не позволяет утверждать:

- что Uzbek hybrid retrieval отсутствует;
- что Uzbek semantic retrieval не оценивается как IR-задача;
- что morphology + semantic representation ранее не исследовались;
- что dynamic query-dependent fusion является новой идеей.

При этом найденные Uzbek исследования пока распределены между различными постановками:

- morphology-aware lexical processing;
- Uzbek embeddings/BERT/semantic resources;
- STS;
- domain-specific semantic retrieval;
- Turkic/idiom semantic retrieval;
- legal RAG/hybrid systems.

Пока недостаточно установлено, как эти компоненты ведут себя **в одной контролируемой query–document ranking постановке** и как морфологическая нормализация меняет взаимодополняемость lexical и semantic retrieval.

## Важное уточнение о morphology

Сейчас morphology **не фиксируется как третий независимый retrieval paradigm**.

Рабочая логика:

`Lexical_raw → Lexical_morph-normalized`

и затем сравнение/интеграция с:

`Semantic`.

Если эксперименты покажут, что raw lexical и morphology-normalized lexical дают устойчиво независимое полезное свидетельство, архитектура может быть расширена до трёх компонентов.

## Gap ≠ solution

Current gap не означает, что решение обязано быть adaptive fusion.

Отдельная рабочая гипотеза может звучать так:

> Если относительная полезность lexical и semantic retrieval систематически зависит от характеристик Uzbek query, query-aware integration может превосходить фиксированную схему.

Это **гипотеза**, а не часть доказанного gap.

Если adaptive fusion не даст улучшения, исследовательский вопрос всё равно остаётся валидным.

## Какие характеристики запроса пока рассматриваются как кандидаты

Только как потенциальные факторы, не как доказанные причины:

- морфологическая вариативность;
- количество/тип аффиксальных форм;
- rare terms;
- named entities;
- числа/идентификаторы/названия;
- Latin/Cyrillic variation;
- длина запроса;
- степень lexical overlap;
- paraphrastic/описательная формулировка;
- domain.

Их реальная связь с относительной эффективностью retrieval-компонентов должна быть установлена статистически.

## Что может изменить gap

Gap необходимо пересмотреть, если deep dive или новые публикации покажут:

1. General-purpose Uzbek benchmark уже систематически сравнивает raw BM25, morphology-aware lexical, modern dense и несколько fusion approaches.
2. Уже существует language-aware/query-aware hybrid method для Uzbek с анализом morphological query features.
3. USHRA/O-RAG или другая работа при полном чтении оказывается значительно ближе к нашей постановке, чем следует из abstract/metadata.
4. Turkic-language research закрывает предполагаемую языковую закономерность и она напрямую переносима на Uzbek.
5. Собственные baseline experiments показывают, что morphology не меняет relative lexical/semantic behavior.
