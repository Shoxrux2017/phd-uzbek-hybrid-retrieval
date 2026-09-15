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

## C. Candidate research questions and hypotheses — provisional / working v0.1

Рабочие вопросы согласованы с **v0.8 refined**, но **не утверждены как окончательные вопросы диссертации**.

- **RQ1:** Как изменение морфологического представления узбекского текста — исходные словоформы, стемы и леммы — влияет на эффективность BM25 и состав найденных им релевантных документов?
- **RQ2:** Как изменение морфологического представления лексического канала влияет на его взаимодополняемость с одной и той же фиксированной моделью плотного поиска и на дополнительный эффект гибридного поиска?
- **RQ3:** Какие характеристики запросов на узбекском языке связаны с изменением взаимодополняемости лексического и плотного поиска при переходе от исходных словоформ к стемам и леммам?

### Provisional hypotheses — not established facts

- **H1:** Изменение морфологического представления меняет не только совокупную эффективность BM25, но и состав найденных релевантных документов для существенной части запросов.
- **H2:** При фиксированных модели плотного поиска и протоколе объединения изменение морфологического представления меняет структуру уникальных релевантных находок и перекрытия, а также дополнительный эффект гибридного поиска.
- **H3:** Величина и направление этих изменений связаны с измеримыми характеристиками узбекских запросов, особенно с морфологией и лексическим перекрытием.

Это проверяемые предположения, а не выводы литературы. Основное сравнение: `BM25_raw`, `BM25_stem`, `BM25_lemma` с одной фиксированной моделью плотного поиска `D`, затем `BM25_raw + D`, `BM25_stem + D`, `BM25_lemma + D` при фиксированном протоколе объединения. Анализ включает lexical-only и dense-only relevant hits, intersection/overlap, oracle union, incremental hybrid gain, изменения по запросам и связь с интерпретируемыми характеристиками запросов.

### Null hypotheses / falsifiability

Нулевые гипотезы допускают, что смена представления не даёт содержательно значимых и воспроизводимых изменений эффективности/состава релевантных находок (H1), взаимодополняемости/дополнительного гибридного эффекта (H2) либо устойчивой связи с характеристиками запросов (H3). Критерии величины эффекта и статистической проверки следует определить в протоколе до основного анализа. Если эффекты слабы или нестабильны, **v0.8 необходимо пересмотреть** до выбора нового метода; отсутствие убедительного эффекта нельзя подменять утверждением о новизне fixed fusion, RRF или dynamic alpha.

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

Candidate-set complementarity и oracle union измеряют доступное релевантное evidence; fusion ranking и per-query best-alpha oracle — его упорядочение. Эти величины не взаимозаменяемы. RQ1–RQ3 и H1–H3 остаются **provisional / working v0.1**, без изменения формулировок.

## E. Citation verification

Особое внимание:

- USHRA / O-RAG: verified ACM ICFNDS ’25, publication year **2025**, pages/DOIs recorded in completed cards; secondary 2026 appearance dates do not change the year;
- morphology-oriented STS: ICFNDS '25 vs 2026 metadata remains a separate open verification item;
- Bruch, Gai & Ingber: основной год синхронизирован как **2023** по официальной ACM publication date **August 2023**; Volume 42(1) в части индексов относится к **2024** — сохранить metadata note при подготовке библиографии;
- официальный ACM record должен иметь приоритет над агрегаторами;
- полные страницы, volume/issue и DOI национальных/турецких источников;
- preprint vs peer-reviewed version для UzBERT/Uzbek embeddings.
