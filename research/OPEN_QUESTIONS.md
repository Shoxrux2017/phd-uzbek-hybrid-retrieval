# Open Questions

**Evidence/status sync:** 2026-09-15; current gap remains **v0.8 refined**.

## A. Highest-priority literature questions

### A1. USHRA — full-text verification

**Completed:** [bibliographic/verified-abstract deep dive, 2026-09-14](../literature/deep-dives/2025_Absalamova_Muminov_Absalamova_USHRA_Uzbek_Legal_RAG.md); ACM ICFNDS ’25, **2025**, pp. 1036–1042, DOI `10.1145/3789692.3789825`, reliability **B**. Reported 85% is chatbot answer accuracy on 200 criminal-law queries, not retrieval effectiveness. **Full-text verification remains open.**

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

**Completed:** [bibliographic/verified-abstract deep dive, 2026-09-14](../literature/deep-dives/2025_Absalamova_Muminov_Absalamova_O_RAG_Uzbek_Legal_Ontology.md); ACM ICFNDS ’25, **2025**, pp. 680–687, DOI `10.1145/3789692.3789782`, reliability **B**. Custom legal ontology, hybrid retrieval and ontology-based reranking are verified at abstract level; exact components and metric values remain unknown. **Full-text verification remains open.**

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

**COMPLETED 2026-09-15 — HYB-009, A:** [deep-dive card](../literature/deep-dives/2026_Posokhov_Query_Adaptive_Hybrid_Search.md).

Query-Driven Alpha Prediction, dynamic `alpha(q)` and dense training on BM25 failures are established. No raw/stem/lemma × same fixed D or morphology-conditioned set decomposition. Its per-query best-alpha oracle is not oracle union. No remaining literature blocker for the baseline pilot; recheck the exact inferential test only if a statistical-significance claim is needed in later prose.

### A4. CLEAR

**COMPLETED 2026-09-15 — HYB-003, A:** [deep-dive card](../literature/deep-dives/2021_Gao_CLEAR_Semantic_Residual_Embeddings.md).

Semantic residual training explicitly optimizes complementarity to BM25. Generic complementarity-aware training is occupied; morphology-induced change remains untested. Keep the same semantic `D` across morphology conditions rather than retraining a residual model for each one.

### A5. DHR / Lin & Lin

**COMPLETED 2026-09-15 — HYB-006, A:** [deep-dive card](../literature/deep-dives/2023_Lin_Lin_Dense_Representation_Framework_DHR.md).

DLR/DHR establish representation-level lexical–semantic integration and joint training; dense representation != semantic matching. The primary comparator must be a fixed retrieval-trained semantic dense retriever. No controlled raw/stem/lemma experiment is reported.

### A6. BGE-M3

**COMPLETED 2026-09-15 — HYB-007, A:** [deep-dive card](../literature/deep-dives/2024_Chen_BGE_M3_Embedding.md).

Unified dense / learned sparse / multi-vector retrieval is established, but the paper has no Uzbek retrieval evaluation. BGE-M3 Dense is a pilot candidate; All is unsuitable as the primary causal comparator. Candidate selection and preprocessing controls are experimental-resource questions in section D.

### A7. Uzbek morphology

**Completed 2026-09-11:** [Bakaev](../literature/deep-dives/2021_Bakaev_Uzbek_Morphology_Search.md) and [Xusainova](../literature/deep-dives/2024_Xusainova_Uzbek_Tokenization_Stemming_Lemmatization.md), both **A**, defended PhDs. Morphology/search deployment is documented; analyzer accuracy and workflow gains do not establish qrels-based IR effectiveness.

Остаётся проверить:

- детали полных защищённых диссертаций и приложений, включая возможные поисковые эксперименты, отсутствующие в авторефератах;
- доступность, лицензии и возможность повторного использования Morphoanalyzer/API, tokenizer, UzbStemmer, lemmatizer и лексических ресурсов;
- точную эталонную разметку для 97.5% у Xusainova и сопоставимость 88.9%/91.3% для религиозных текстов у Bakaev;
- наличие количественной оценки поиска в отчётах о внедрении и ошибки морфологии, значимые для будущего поискового эксперимента.

**Also completed:** [Elov](../literature/deep-dives/2026_Elov_Uzbek_NLP_Morphology_Information_System.md), **A**, officially defended DSc 2026-02-05, and [Turayev](../literature/deep-dives/2026_Turayev_Uzbek_Morphosyntactic_Neural_Analysis.md), **B pending final-defense verification**. For Elov, reconcile corpus counts and the separate morphology/system result tables; for Turayev, resolve registration conflict **B2025.3.PhD/T5887** and verify final defense. Check resource access/licensing before reuse.

### A8. Uzbek semantic retrieval 2026

**Ishkobilov et al.: [verified-abstract deep dive completed 2026-09-14](../literature/deep-dives/2026_Ishkobilov_Uzbek_Seismic_Semantic_Retrieval.md), B.** The publication and P@5/R@5 values are verified; full-paper follow-up remains needed for:

- corpus construction and exact 120-document / 8,450-paragraph counts recorded by the project;
- query construction and relevance judgments/qrels;
- number of relevant docs per query;
- exact MAP/MRR definitions and values, and F1 use/definition/value;
- exact FastText checkpoint/training and paragraph aggregation/similarity;
- exact per-query quantity behind reported paired **t=15.1372, p<0.001**, assumptions and any multiple-testing treatment;
- limitations of 100-query domain-specific setup.

**SIGTURK 2026 — deep dive remains open:**

- Uzbek subset;
- idiom retrieval task construction;
- metrics;
- best models;
- насколько conclusions generalize beyond idioms.

### A9. Urinov — full-text verification

**Completed:** [Zenodo metadata/abstract-level deep dive, 2026-09-14](../literature/deep-dives/2025_Urinov_Uzbek_RAG_BM25_Vector_Search.md), DOI `10.5281/zenodo.17341315`, **C**. BM25-like vs vector comparison is verified at this level; genuine hybrid fusion is not.

По полному тексту необходимо проверить:

- underlying conference/proceedings venue and peer review;
- corpus, query set and relevance judgments/qrels;
- exact vector model, retrieval training and aggregation/index;
- BM25 implementation/parameters and preprocessing;
- effectiveness, latency/resource metrics and statistical evidence;
- whether an actual BM25 + vector fusion condition exists, and its protocol.

### A10. Completed contextual NLP cards — targeted verification

- [Axmedova](../literature/deep-dives/2026_Axmedova_Uzbek_Paraphrase_Semantic_Matching.md): **B pending final-defense protocol verification**; reconcile dataset/result descriptions and verify splits, human validation and exact E5/Jina checkpoints.
- [Abdisalomova](../literature/deep-dives/2026_Abdisalomova_Uzbek_Coreference_UzCoref.md): **B pending final-defense verification**; reconcile coreference score contexts and check corpus licensing and any quantitative search-deployment evidence.
- [Allanazarova](../literature/deep-dives/2026_Allanazarova_Uzbek_Sentiment_SentiUzNet.md): **B pending final-defense verification**, background only; clarify merged-review versus sentiment-experiment counts if cited.

These completed deep dives establish paraphrase/coreference/sentiment evidence, not corpus-level retrieval effectiveness.

### A11. Completed international structural and methodology cards

- **PHD-INT-001 — Sheng-Chieh Lin PhD: COMPLETED 2026-09-15, A**, [card](../literature/deep-dives/2024_Sheng_Chieh_Lin_PhD_Robust_Dense_Retrieval.md). Robust transfer requires an Uzbek pilot/dev validation gate before freezing `D`; the structural lesson is experiment before method. No uncompleted literature blocker remains for this dissertation.
- **MORPH-004 — Munetsi et al.: COMPLETED 2026-09-15, A**, [card](../literature/deep-dives/2026_Munetsi_Mukande_OConnor_Shona_Morphology_Aware_IR.md). Four-page preliminary Shona comparison with morphology-sensitive failures; stemming/lemmatization are future benchmark work. No implemented raw/stem/lemma or BM25+dense fusion in the main table. Pooling and annotation lessons are tracked in section D.
- **HYB-005 — Bruch, Gai & Ingber: COMPLETED 2026-09-15, A**, [card](../literature/deep-dives/2023_Bruch_Gai_Ingber_Fusion_Functions_Hybrid_Retrieval.md). Normalized convex fusion and global-alpha tuning are established; RRF is parametric. Candidate-set coverage differs from fusion ranking; protocol details remain to be specified in section D.

## B. Turkic / morphology-aware IR search still needed

Broad national synthesis is **provisionally saturated**: see the [national evidence matrix](NATIONAL_EVIDENCE_MATRIX_2026-09-14.md). Following the current stopping rule, reopen targeted searches when a direct analogue or stronger/new source could change the residual v0.8 question. Relevant language lines remain:

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

## C. Candidate research questions and hypotheses — working v0.2

**Статус:** provisional / working v0.2; научный аудит и уточнение RQ1–RQ3 / H1–H3 выполнены 2026-09-15. Это рабочие формулировки, **не окончательные вопросы и гипотезы диссертации**. Текущий research gap **v0.8 refined** остаётся без изменений и provisional.

### RQ1 v0.2

В какой степени, если вообще, переход между исходными словоформами, стемами и леммами при неизменных остальных параметрах лексического поиска изменяет эффективность BM25 и состав найденных релевантных документов для запросов на узбекском языке?

### RQ2 v0.2

В какой степени, если вообще, переход между исходными словоформами, стемами и леммами в лексическом канале при одной и той же фиксированной модели плотного поиска `D` и неизменном протоколе объединения изменяет:

1. структуру взаимодополняемости лексического и плотного поиска:

   - lexical-only relevant hits;
   - dense-only relevant hits;
   - intersection;
   - overlap;
   - oracle union;

2. дополнительный эффект соответствующего гибридного поиска:

   - относительно соответствующего лексического компонента;
   - относительно лучшего отдельного компонента.

**RQ2 — центральный исследовательский вопрос текущего `v0.8 refined`.** Он проверяет изменение взаимодополняемости вследствие смены морфологического представления и связанное с ним изменение дополнительного эффекта гибридного поиска; общий вопрос «улучшает ли гибридный поиск» не заменяет эту постановку.

### RQ3 v0.2

Какие заранее определённые и интерпретируемые характеристики запросов на узбекском языке связаны с величиной и направлением изменения взаимодополняемости лексического и плотного поиска, вызванного переходом между исходными словоформами, стемами и леммами при фиксированной модели плотного поиска `D`?

**Методологическая граница RQ3:** вопрос не является задачей:

- предсказания лучшего `alpha(q)`;
- динамического изменения весов лексического и плотного поиска (dynamic lexical/dense weighting);
- generic query-adaptive fusion;
- выбора лучшей поисковой стратегии по характеристикам запроса.

Эти общие направления уже существенно заняты литературой, включая [Query-Adaptive Hybrid Search](../literature/deep-dives/2026_Posokhov_Query_Adaptive_Hybrid_Search.md). RQ3 исследует только связь `query characteristics → morphology-induced complementarity change`: связь характеристик запроса с изменением взаимодополняемости, вызванным сменой морфологического представления.

### Provisional hypotheses v0.2 — not established facts

**H1 v0.2:** При неизменных остальных условиях лексического поиска по крайней мере один переход между `raw`, `stem` и `lemma` приводит к воспроизводимому и практически значимому изменению состава релевантных документов, найденных BM25 на фиксированной глубине поиска.

Порядок `lemma > stem > raw` заранее не предполагается. Изменение совокупной эффективности BM25 анализируется отдельно и не является обязательным условием H1.

**H2 v0.2:** При фиксированной модели плотного поиска `D` и фиксированном протоколе объединения по крайней мере один переход между `raw`, `stem` и `lemma` приводит к практически значимому и воспроизводимому изменению set-based complementarity между BM25 и `D`, сопровождаемому изменением дополнительного эффекта соответствующей гибридной конфигурации.

Диагностически H2 разделяется на:

- **H2a:** смена морфологического представления изменяет взаимодополняемость на уровне множеств кандидатов / релевантных документов (candidate-set / relevant-set complementarity);
- **H2b:** это изменение сопровождается изменением дополнительного эффекта гибридного поиска (incremental hybrid gain).

H2a и H2b проверяются и интерпретируются раздельно: изменение взаимодополняемости само по себе не подтверждает изменение эффекта гибридного поиска. Превосходство `hybrid > best standalone` заранее не предполагается.

**H3 v0.2:** Величина morphology-induced изменения lexical–dense complementarity имеет воспроизводимую связь по крайней мере с одной заранее определённой характеристикой узбекского запроса, рассчитанной независимо от результатов сравниваемых retrieval systems.

Какие именно признаки окажутся значимыми, заранее неизвестно. Набор признаков и способ их расчёта должны быть определены до анализа результатов сравниваемых поисковых систем.

Все H1–H3 — проверяемые рабочие предположения, а не установленные результаты. Заранее не предполагается и превосходство `dense > BM25`.

### Null hypotheses / falsifiability

**H0₁:** Различия между `BM25_raw`, `BM25_stem` и `BM25_lemma` по составу найденных релевантных документов находятся в заранее определённых пределах практически незначимого эффекта.

**H0₂:** При фиксированной `D` и фиксированном протоколе объединения переход между `raw`, `stem` и `lemma` не вызывает практически значимых и воспроизводимых изменений:

- lexical-only relevant hits;
- dense-only relevant hits;
- intersection;
- overlap;
- oracle union;

а различия incremental hybrid gain также находятся в пределах практически незначимого эффекта.

Если **H0₂ получает убедительную эмпирическую поддержку**, это является основанием для пересмотра текущего **`v0.8 refined`**. Отрицательный результат является допустимым научным результатом.

**H0₃:** Заранее определённые характеристики запросов не демонстрируют воспроизводимой практически значимой связи с morphology-induced изменениями lexical–dense complementarity после учёта множественных проверок и основных контрольных переменных.

**`failure to reject H0 != proof of no effect`**: неотклонение нулевой гипотезы не доказывает отсутствие эффекта. Будущий протокол должен различать:

1. свидетельства в пользу практически значимого эффекта;
2. недостаточность свидетельств;
3. свидетельства того, что эффект практически незначим.

Границы практической эквивалентности (equivalence margins), минимальный практически значимый размер эффекта (SESOI) и конкретные статистические тесты будут определены до основного анализа в `BENCHMARK_QRELS_PROTOCOL_v0.1`. Численные пороги и конкретные тесты здесь не фиксируются.

### Measurement logic — operationalization

Для морфологического условия `m ∈ {raw, stem, lemma}`:

- лексический ретривер: `L_m = BM25_m`;
- фиксированный плотный ретривер: `D`;
- соответствующий гибрид: `H_m = fusion(L_m, D)`.

Основной контролируемый эксперимент удерживает постоянными:

- `D`, включая checkpoint, режим поиска и предобработку входа;
- формулу объединения и правило нормализации оценок;
- **один global `alpha`**, выбранный только на validation и одинаковый для всех трёх условий;
- глубину кандидатов `k` для каждого компонента и всех морфологических условий;
- реализацию BM25 и основные параметры;
- политику токенизации, обработки письменности, Unicode/апострофов и стоп-слов, кроме непосредственно исследуемого морфологического представления.

Отдельные `alpha_raw`, `alpha_stem`, `alpha_lemma` **не вводятся в primary causal experiment**. Их независимая настройка на validation возможна позднее только в отдельном secondary practical experiment, поскольку одновременно меняет представление и вес объединения.

Для каждого запроса и каждого `m` анализируются множества `top-k L_m` и `top-k D` и релевантность входящих в них документов по одним и тем же qrels:

- **lexical-only relevant hits** — релевантные документы только в лексическом множестве;
- **dense-only relevant hits** — релевантные документы только в плотном множестве;
- **intersection** — пересечение найденных релевантных множеств;
- **overlap** — степень перекрытия множеств; конкретная мера и её нормировка задаются будущим протоколом с явным различением всех кандидатов и релевантных документов;
- **oracle union** — релевантные документы, доступные в объединении кандидатов независимо от формулы и качества ранжирования;
- **incremental hybrid gain** — разность эффективности `H_m` и соответствующего `L_m`, а также разность эффективности `H_m` и лучшего отдельного компонента из `L_m` и `D`, при общей метрике и глубине оценки; эффект может быть положительным, нулевым или отрицательным;
- **per-query changes** — попарные изменения этих величин между `raw`, `stem` и `lemma` для одного и того же запроса.

Эффективность `L_m`, `D` и `H_m` анализируется отдельно от состава множеств. Правило определения лучшего отдельного компонента и агрегации по запросам задаётся будущим протоколом; оно не подменяется выбором поисковой стратегии для каждого запроса. Интерпретация множеств должна учитывать полноту qrels; неразмеченный документ не является доказанно нерелевантным.

Сохраняются два разграничения:

- **`candidate-set complementarity != fusion ranking quality`**: доступность релевантных документов в объединении и качество их упорядочения — разные уровни анализа;
- **`per-query best-alpha oracle != oracle union`**: выбор лучшего веса по известной релевантности для каждого запроса не равен охвату релевантных документов объединением кандидатов.

Основание разделения объединения кандидатов и качества ранжирования: [Bruch, Gai & Ingber](../literature/deep-dives/2023_Bruch_Gai_Ingber_Fusion_Functions_Hybrid_Retrieval.md); граница RQ3 и различие oracle — [Query-Adaptive Hybrid Search](../literature/deep-dives/2026_Posokhov_Query_Adaptive_Hybrid_Search.md).

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

### D1. Uzbek validation gate for the semantic comparator

- Какие retrieval-trained multilingual candidates включить в pilot: BGE-M3 Dense, multilingual E5 и, при обосновании, ещё один ретривер? Уточнить checkpoint, retrieval mode, требования к ресурсам и обработку входа.
- Какое минимальное evidence достаточно, чтобы считать `D` убедительным для Uzbek: объём и покрытие dev/pilot, заранее выбранные IR-метрики, величина/неопределённость эффекта и анализ ошибок? Высокий English/BEIR score, STS или заявленная multilingual coverage сами по себе недостаточны; превосходство над BM25 на каждом запросе не предполагается.
- Как зафиксировать правило выбора `D` без test leakage и настройки отдельно под raw/stem/lemma? После выбора заморозить тот же semantic dense retriever, mode и preprocessing для основного held-out сравнения.

### D2. Pooling and annotation resources

- Какую глубину multi-system pooling выбрать, какие runs включить и сколько пар «запрос–документ» разметить? Для reliable unique hits / Recall / oracle union нужен более глубокий pool, чем top-10; определить критерий достаточности и остаточные ограничения неполной qrels.
- Сколько assessors нужно, какую долю размечать независимо несколькими экспертами, как определить relevance scale и инструкции?
- Как измерять inter-annotator agreement, разрешать расхождения через adjudication и документировать число итоговых judgments?

### D3. Primary fixed-alpha fusion protocol — provisional

- Какую нормализацию и точную convex-combination formula зафиксировать, какой компонент обозначать весом `alpha`, как обрабатывать равные/вырожденные scores и tie-breaking?
- Как выбрать **один global `alpha` на validation**: метрика, сетка/процедура поиска, правило агрегации по morphology conditions и разрешения равенств? В основном causal experiment использовать **одинаковые `D`, global `alpha`, normalization, formula и candidate depth `k`** для raw/stem/lemma.
- Какой `k` выбрать для `top-k BM25_m ∪ top-k D`, как получить оба scores для всех кандидатов и отделить pooling depth для qrels от retrieval candidate depth? Одинаковый `k` не означает одинаковый состав/размер union: изменение состава — предмет измерения.
- Какие non-morphological preprocessing операции удерживать постоянными: tokenization, script/Unicode/apostrophe normalization и stop-word handling?
- Какой rank-offset parameter задать для **secondary RRF robustness baseline** при том же `k`? RRF не является parameter-free.
- Нужен ли после главного сравнения **secondary practical experiment** с независимо validation-tuned `alpha_raw`, `alpha_stem`, `alpha_lemma`? Его результаты нужно показывать отдельно: он одновременно меняет morphology и fusion weight.

Candidate-set complementarity и oracle union измеряют доступное релевантное evidence; fusion ranking и per-query best-alpha oracle — его упорядочение. Эти величины не взаимозаменяемы. RQ1–RQ3 и H1–H3 уточнены до **provisional / working v0.2** в разделе C; текущий gap **v0.8 refined** остаётся без изменений.

## E. Citation verification

Особое внимание:

- USHRA / O-RAG: verified ACM ICFNDS ’25, publication year **2025**, pages/DOIs recorded in completed cards; secondary 2026 appearance dates do not change the year;
- morphology-oriented STS: ICFNDS '25 vs 2026 metadata remains a separate open verification item;
- Bruch, Gai & Ingber: основной год синхронизирован как **2023** по официальной ACM publication date **August 2023**; Volume 42(1) в части индексов относится к **2024** — сохранить metadata note при подготовке библиографии;
- официальный ACM record должен иметь приоритет над агрегаторами;
- полные страницы, volume/issue и DOI национальных/турецких источников;
- preprint vs peer-reviewed version для UzBERT/Uzbek embeddings.
