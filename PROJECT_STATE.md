# Current PhD State

**Last updated:** 2026-09-10
**Status:** working research state; not final dissertation state.

## Topic

> **Гибридный подход к поиску информации на узбекском языке на основе интеграции лексических и семантических методов**

## Chapter I

Рабочее название:

> **АНАЛИЗ МЕТОДОВ И МОДЕЛЕЙ ЛЕКСИЧЕСКОГО, СЕМАНТИЧЕСКОГО И ГИБРИДНОГО ИНФОРМАЦИОННОГО ПОИСКА**

### Structure

- **1.1.** Теоретические основы и модели лексического информационного поиска.
- **1.2.** Современные методы и модели семантического поиска текстовой информации.
- **1.3.** Методы интеграции лексических и семантических моделей в гибридном поиске текстов на узбекском языке.
- Выводы.

### Status

- 1.1 — рабочая финальная редакция сформирована.
- 1.2 — рабочая финальная редакция сформирована и актуализирована с учётом Uzbek retrieval работ 2026 года.
- 1.3 — рабочая финальная редакция сформирована.
- Выводы — сформированы.
- Research gap — пересмотрен после targeted gap-killer search 2026-09-10 и остаётся **provisional**.

Собранная Word-версия `v0.9` имела:

- 1.1 — около 9 страниц;
- 1.2 — около 13 страниц;
- 1.3 — около 10 страниц;
- выводы — около 3 страниц;
- итого около **35 страниц без списка литературы**.

### Current decision on length

Изначальная цель после анализа реальных PhD была около 26–28 страниц. Реальная версия получилась длиннее.

**Решение:** пока **не фиксировать сокращение объёма**. Сначала завершить переход от literature gap к research questions / hypotheses / experimental design; затем повторно проверить, какие части главы действительно нужны для обоснования финальной постановки.

## Current research gap — v0.8 refined

Полная формулировка: `research/CURRENT_GAP.md`.

Кратко:

> Недостаточно установлено, как изменение морфологического представления лексического канала для Uzbek — исходные словоформы, стемы, леммы — изменяет структуру его взаимодополняемости с фиксированной моделью плотного поиска: уникально найденные релевантные документы, перекрытие результатов и дополнительный эффект гибридного поиска, включая зависимость этих изменений от характеристик узбекских запросов.

Это **не окончательная новизна** и не утверждение, что adaptive fusion обязательно является решением.

## Evidence update — 2026-09-10

Targeted analysis и aggressive gap-killer search существенно сузили прежний v0.4.

### National boundary

Уже установлено/обнаружено:

- Bakaev / Xusainova / related Uzbek research — morphology, stemming, lemmatization and search-oriented processing exist;
- Ishkobilov et al. — corpus-level Uzbek semantic retrieval with standard IR metrics exists;
- USHRA / O-RAG — Uzbek hybrid/RAG exists;
- Axmedova 2026 screening — modern multilingual semantic matching, including Multilingual E5-related use, exists for Uzbek paraphrase processing, but STS/paraphrase != corpus-level IR;
- Turayev 2026 screening — neural/statistical morphology and explicit Uzbek lemmatization exist;
- Elov 2026 screening — integrated Uzbek morphology/syntax/semantics and IR-oriented infrastructure exist;
- Sharifbaev 2026 manuscript describes lemmatized BM25 + LaBSE + graph retrieval + adaptive controller for Uzbek legal/parliamentary data, but remains **D-level unverified manuscript evidence** until official final/defense verification.

### International boundary

New key gap killers:

- **UPERF (Kazi & Khoja, PACLIC 2024):** raw/stem/lemma × BM25/TF-IDF/embeddings × query type + weighted combination in Urdu;
- **Kazi & Khoja, Computer Speech & Language 2026:** multi-benchmark Urdu retrieval with lexical/embedding features and SVMrank reranking;
- **Aboasal et al. 2026:** Farasa morphology + BM25 + modern embeddings (including BGE-M3/GTE/Ada/Mistral-embed) + hybrid Arabic legal retrieval;
- **Munetsi et al., SIGIR 2026:** morphology-aware low-resource Shona retrieval as a direct modern IR research line;
- **GreekBarRetrieval, 2026 preprint:** three BM25 morphology/preprocessing variants + nine modern dense retrievers + fusion + query reformulation in one statutory-retrieval benchmark.

Full synthesis: `research/GAP_BOUNDARY_2026-09-10.md`.

## Current scientific position

Already established:

- BM25 remains a strong lexical baseline; it is not assumed to be optimal for Uzbek.
- Learned sparse retrieval shows that `sparse != old/non-neural`.
- Dense retrieval addresses part of vocabulary mismatch but is not a universal replacement for lexical retrieval.
- Uzbek morphology and script variation are important to lexical representation.
- Uzbek semantic infrastructure and corpus-level semantic retrieval already exist.
- Uzbek hybrid retrieval/RAG already exists.
- Raw/stem/lemma comparisons already exist in other low-resource/morphologically complex retrieval research.
- Morphology-aware BM25 has already been compared with modern semantic embeddings internationally.
- Hybrid lexical–semantic retrieval and query-dependent strategy selection are already established ideas.
- Therefore novelty cannot be based on the existence of these components or on RRF/fixed fusion/dynamic alpha alone.

### Current residual question

The strongest surviving direction is:

`morphological representation change`

→ `change in lexical relevant set`

→ `change in overlap/unique hits vs the same dense retriever`

→ `change in incremental hybrid gain`

→ `relation to Uzbek query features`.

## Current experimental guardrails

If the project proceeds with v0.8, the core controlled design should keep the semantic comparator constant while changing the lexical morphology representation:

`BM25_raw`
`BM25_stem`
`BM25_lemma`

with the same dense retriever `D`, then:

`BM25_raw + D`
`BM25_stem + D`
`BM25_lemma + D`.

Aggregate metrics alone are insufficient for the main explanatory claim. The analysis should include per-query overlap, unique relevant hits, oracle union and incremental hybrid gain where the qrels permit this.

## Reliability cautions

- **Sharifbaev 2026 manuscript:** D until official final/defense evidence is verified.
- **GreekBarRetrieval:** C while only arXiv/preprint status is verified.
- **Aboasal et al. 2026:** B; project card intentionally does not invent methods/details absent from verified official record.
- **UPERF:** B; full paper inspected, but its main metric is Recall@5 and statistical-test details are not clearly specified.

## Next scientific phase

Broad generic gap-search has reached **provisional saturation**.

Next priorities:

1. Formalize research questions from v0.8 without predetermining the answer.
2. Formulate falsifiable hypotheses.
3. Design Uzbek retrieval benchmark / qrels protocol.
4. Select and justify BM25 preprocessing variants.
5. Select at least one modern retrieval-trained multilingual dense baseline and keep it fixed for the main interaction analysis.
6. Define fusion baselines (RRF and/or normalized score fusion) as controls, not novelty.
7. Run pilot experiments to test whether morphology actually changes lexical–semantic complementarity.
8. If the interaction is weak/unstable, revise the gap before inventing a new method.

High-priority background/deep-dive work remains useful where it directly affects design (CLEAR, DHR, BGE-M3, Bruch fusion analysis, Query-Adaptive Hybrid Search, modern dense/learned-sparse baselines), but broad literature accumulation is no longer the immediate bottleneck.
