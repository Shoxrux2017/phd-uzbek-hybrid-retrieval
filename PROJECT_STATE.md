# Current PhD State

**Last updated:** 2026-09-15
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

## Evidence update — 2026-09-15

Targeted analysis и aggressive gap-killer search существенно сузили прежний v0.4.

### National boundary

National deep dives completed 2026-09-11–2026-09-14 strengthen the existing boundary; **v0.8 refined remains unchanged**. Cards and evidence limits are consolidated in the [national evidence matrix](research/NATIONAL_EVIDENCE_MATRIX_2026-09-14.md) and [master index](literature/MASTER_INDEX.md).

- **Bakaev — A, defended PhD, deep dive completed:** morphology/full-text/library search and National Library deployment exist; no modern qrels-based BM25+dense benchmark. Analyzer accuracy and 9–11% workflow gains are not retrieval effectiveness.
- **Xusainova — A, defended PhD, deep dive completed:** tokenizer/stemmer/lemmatizer, reported 97.5% analyzer accuracy; no controlled BM25 raw/stem/lemma IR benchmark.
- **Elov — A, DSc officially defended 2026-02-05, deep dive completed:** 2025 manuscript; integrated morphology/syntax/semantics and search-oriented lemma indexing, not lexical+dense IR. Corpus counts and module-score contexts require caution.
- **Turayev — B pending final-defense verification:** 32k+ lemma/base-form infrastructure; TUIT seminar verified, registration-number conflict unresolved; document workflow, no IR benchmark.
- **Axmedova — B pending final-defense protocol verification:** modern E5/Jina/Gemma3 semantic/paraphrase matching, not corpus-level IR; dataset descriptions remain unreconciled.
- **Abdisalomova — B pending final-defense verification:** contextual/coreference NLP and UzCoref, not corpus retrieval or verified search-effectiveness gains.
- **Allanazarova — B pending final-defense verification, background:** SentiUzNet/sentiment classification, not retrieval.
- **Ishkobilov — B, verified-abstract deep dive completed:** real corpus-level Uzbek semantic retrieval with standard metrics; TF-IDF vs FastText, no BM25/raw-stem-lemma/fusion. Full qrels/metric/test details remain open.
- **USHRA — 2025, B, verified ACM bibliographic/abstract deep dive completed:** hybrid/RAG; 85% answer accuracy on 200 criminal-law queries != retrieval effectiveness; exact fusion unverified.
- **O-RAG — 2025, B, verified ACM bibliographic/abstract deep dive completed:** ontology-enhanced hybrid retrieval/reranking; exact components and metric values unverified; gains cannot be attributed to fusion alone.
- **Urinov — C, metadata/abstract deep dive completed:** supporting BM25-like-vs-vector comparison evidence; full protocol and genuine fusion unverified.
- **Sharifbaev — D unchanged:** manuscript describes lemmatized BM25 + LaBSE + graph retrieval + adaptive control; remains unverified until official final/defense verification.

### International boundary

The targeted international deep-dive wave is **substantially completed as of 2026-09-15**; all seven new cards are integrated in the [master index](literature/MASTER_INDEX.md). **v0.8 refined remains unchanged** and provisional.

Completed evidence/design update:

- **CLEAR:** complementarity-aware dense training as a semantic residual to BM25 is already established.
- **DHR:** unified lexical–semantic representation and joint training already exist; dense representation does not automatically mean semantic matching.
- **Query-Adaptive Hybrid Search:** Query-Driven Alpha Prediction, dynamic `alpha(q)` and dense training on BM25 failure cases already exist.
- **BGE-M3:** unified multilingual dense / learned sparse / multi-vector retrieval is established. Dense-only is a candidate `D` requiring Uzbek validation; All includes additional sparse/multi-vector signals.
- **Sheng-Chieh Lin PhD:** dense robustness/transfer must be tested; English/BEIR strength does not establish Uzbek effectiveness. Structural lesson: `problem → evidence of limitation → controlled experiment → method only if justified`.
- **Bruch, Gai & Ingber (2023):** normalized convex fusion is a strong interpretable control; RRF has parameters and loses score-distance information. Candidate-union coverage and fusion ranking are separate analytical levels.

Closest morphology/low-resource boundary evidence:

- **UPERF (Kazi & Khoja, PACLIC 2024):** raw/stem/lemma × BM25/TF-IDF/embeddings × query type + weighted combination in Urdu;
- **Kazi & Khoja, Computer Speech & Language 2026:** multi-benchmark Urdu retrieval with lexical/embedding features and SVMrank reranking;
- **Aboasal et al. 2026:** Farasa morphology + BM25 + modern embeddings (including BGE-M3/GTE/Ada/Mistral-embed) + hybrid Arabic legal retrieval;
- **Munetsi et al., SIGIR 2026:** A-level, 4-page preliminary Shona BM25 / ColBERT-v2 / dense comparison with morphology-sensitive failure analysis; stemming/lemmatization are proposed future benchmark work, not implemented raw/stem/lemma conditions. No BM25+dense fusion in the main table; top-10 pooling limits set/Recall analysis;
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

### Provisional experimental design implications — 2026-09-15

These are design controls for testing the working gap, **not final novelty or established Uzbek results**.

1. Validate candidate retrieval-trained semantic dense retrievers on Uzbek pilot/dev data before choosing `D`; BGE-M3 Dense and multilingual E5 are candidate families, not predetermined winners.
2. After selection, freeze the same `D`, its mode and input preprocessing across every lexical morphology condition. BGE-M3 All is unsuitable as the primary comparator because it adds sparse/multi-vector signals.
3. Use **normalized convex combination** as the provisional primary fusion control.
4. Keep the same **global `alpha`**, selected on validation only, the same normalization rule, fusion formula and candidate depth `k` across `raw/stem/lemma`. Explicitly control BM25 tokenization, script/Unicode normalization and stop-word handling. Independently tuned `alpha_raw`, `alpha_stem`, `alpha_lemma` belong to an optional secondary practical experiment.
5. Use RRF as a **secondary robustness baseline**, with its parameter and candidate depth specified; it is not parameter-free.
6. Build deeper multi-system pooling/qrels than a top-10 pool for reliable unique-hit, Recall and oracle-union analysis; document assessors, agreement and adjudication. Candidate-set complementarity is separate from fusion ranking, and per-query best-alpha oracle is not oracle union.

## Reliability cautions

- **Sharifbaev 2026 manuscript:** D until official final/defense evidence is verified.
- **GreekBarRetrieval:** C while only arXiv/preprint status is verified.
- **Aboasal et al. 2026:** B; project card intentionally does not invent methods/details absent from verified official record.
- **UPERF:** B; full paper inspected, but its main metric is Recall@5 and statistical-test details are not clearly specified.

## Next scientific phase

Broad generic gap-search and broad national evidence synthesis have reached **provisional saturation**.

Scientific audit/refinement of provisional RQ1–RQ3 / H1–H3 is **completed as of 2026-09-15**. Current **working RQ/H v0.2**, including null hypotheses, falsifiability and measurement logic, is recorded in [OPEN_QUESTIONS](research/OPEN_QUESTIONS.md). These remain provisional, not final dissertation RQs or established findings; **v0.8 refined remains unchanged and provisional**.

Immediate next step: create **`BENCHMARK_QRELS_PROTOCOL_v0.1`** to design the corpus, retrieval unit, query set, morphology/query strata, pooling, qrels, assessors, relevance scale, adjudication, inter-annotator agreement, dev/test split, metrics, statistical tests, leakage controls, candidate depth and dense-baseline pilot protocol. The protocol has not yet been created; numerical equivalence margins / SESOI and concrete statistical tests remain to be specified there.

Next priorities:

1. Design `BENCHMARK_QRELS_PROTOCOL_v0.1` under working RQ/H v0.2.
2. Select and justify BM25 preprocessing variants.
3. Pilot/dev-validate candidate semantic dense retrievers for Uzbek, select primary `D` by a predefined rule and freeze it for the main interaction analysis.
4. Specify primary normalized convex fusion with one global alpha, normalization and candidate depth across morphology conditions; use RRF as a secondary robustness control.
5. Run pilot experiments to test whether morphology actually changes lexical–semantic complementarity.
6. Reassess the gap if the interaction is weak/unstable; convincing support for practically negligible complementarity changes requires revision before inventing a new method. Insufficient evidence alone does not prove no effect.

The seven targeted international deep dives are complete. UZ-SEM-007 and targeted verification questions remain tracked in the index/open questions, but the immediate bottleneck is **benchmark/qrels + Uzbek pilot**, not broad literature search.
