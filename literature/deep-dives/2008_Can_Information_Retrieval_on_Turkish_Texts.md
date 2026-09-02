# Information Retrieval on Turkish Texts

**Deep-dive status:** COMPLETED  
**Completed:** 2026-09-02  
**Literature ID:** MORPH-001

## 1. Bibliographic record

- **Authors:** Fazli Can, Seyit Kocberber, Erman Balcik, Cihan Kaynak, H. Cagdas Ocalan, Onur M. Vursavas
- **Year:** 2008
- **Venue:** *Journal of the American Society for Information Science and Technology*, 59(3), 407–421
- **DOI:** `10.1002/asi.20750`
- **Official publisher URL:** https://doi.org/10.1002/asi.20750
- **Full-text repository:** https://repository.bilkent.edu.tr/items/5be10741-6b40-44ba-b324-9e7951d54c03
- **Source type:** peer-reviewed journal research article
- **Reliability:** A
- **Full text available:** yes

## 2. Why this work matters to the PhD

Работа является одним из наиболее важных сравнительных источников для линии «морфология → лексический информационный поиск» в тюркском агглютинативном языке.

Для текущей PhD она важна по четырём причинам:

1. Турецкий и узбекский относятся к тюркским агглютинативным языкам, поэтому проблема большого числа словоформ методологически близка.
2. Авторы оценивают не точность морфологического анализа сама по себе, а конечную **эффективность поиска документов**.
3. Сравниваются методы от предельно простого усечения слова до лемматизаторного подхода.
4. Анализ длины запроса показывает, что эффект морфологической обработки не обязательно одинаков для всех запросов.

Работа напрямую относится к разделу 1.1 диссертации и к будущей постановке `raw/stem/lemma` для узбекского лексического поиска.

Она не исследует современный семантический или гибридный поиск и поэтому не закрывает текущий research gap.

## 3. Research problem

### Simple explanation

В агглютинативном языке одно исходное слово может иметь много форм из-за присоединения аффиксов. Если поисковая система рассматривает каждую форму как отдельный термин, запрос и релевантный документ могут не совпасть лексически.

Простой перенос на узбекский:

`kitob`, `kitoblar`, `kitobimiz`, `kitoblarimizdan`

без нормализации могут индексироваться как разные термины.

Исследовательский вопрос Can et al.:

> Улучшает ли объединение таких словоформ реальный поиск документов, и нужен ли для этого сложный морфологический анализ?

### Formal formulation

Работа изучает влияние различных стратегий стемминга/лемматизации и функций сопоставления запроса и документа на эффективность ad-hoc информационного поиска по крупной турецкой коллекции.

Дополнительно исследуются:

- длина запроса;
- длина документа;
- размер коллекции;
- стоп-слова;
- размер и эффективность индексной структуры.

## 4. Main idea

### Simple explanation

Авторы не принимают заранее, что «самый сложный морфологический алгоритм должен быть лучшим».

Они создают несколько вариантов индекса одной и той же коллекции:

- вообще без стемминга;
- с механическим усечением слова;
- со статистическим поиском границы основы;
- с морфологическим анализатором/лемматизатором.

После этого они запускают одни и те же запросы и сравнивают качество ранжирования.

### Concrete example

Условный узбекский пример:

`kitoblarimizdan`

- NS: `kitoblarimizdan`
- F5: `kitob`
- SV: статистически выбранная основа, потенциально `kitob`
- LV: лемматизатор пытается получить `kitob`; если анализ невозможен, используется статистический fallback

Пример служит только для объяснения механизма. Он не является примером из турецкого экспериментального корпуса статьи.

### Formal method

Эксперимент варьирует два основных компонента:

1. представление терминов после морфологической обработки;
2. функцию лексического сопоставления запроса и документа.

Это позволяет отделить эффект морфологии от эффекта одной конкретной формулы ранжирования.

## 5. Architecture / algorithm

### 5.1 No stemming — NS

Слова используются в исходном виде. NS является базовой конфигурацией.

### 5.2 Fixed-prefix truncation — F3, F4, F5, F6, F7

Сохраняются первые `n` символов слова.

Например, F5 оставляет максимум первые пять символов.

Метод:

- не использует словарь;
- не использует грамматические правила;
- не определяет настоящую лемму;
- является псевдостеммингом.

F5 был выбран как основной представитель этого семейства после экспериментального сравнения нескольких длин префикса.

### 5.3 Successor Variety — SV

SV использует статистику корпуса.

Для последовательных префиксов слова оценивается количество различных символов, которые могут следовать за данным префиксом в корпусе. Высокое разнообразие продолжений рассматривается как возможный признак границы основы.

Турецкая реализация авторов выбирает наиболее длинный префикс, соответствующий максимальному successor variety.

### 5.4 Lemmatizer-based variants — LM5 / LM6

Морфологический анализатор может возвращать несколько вариантов леммы.

Авторы используют длину и частеречную информацию для выбора одного варианта:

- LM6 ориентируется на среднюю длину турецкой леммы около 6.58 символа;
- LM5 использует ориентир около 5 символов, поскольку фиксированный F5 показал хорошие поисковые результаты.

### 5.5 LV

LV — комбинированный вариант:

1. используется LM5;
2. если слово не анализируется лемматизатором, применяется SV.

Это было важно, поскольку около 40% различных словоформ, включая иностранные и ошибочно написанные формы, не анализировались используемым лемматизатором.

### 5.6 Matching functions

Авторы используют восемь функций сопоставления `MF1–MF8`, основанных на векторной модели поиска и различных вариантах взвешивания терминов.

MF8 показывает наилучшую общую эффективность в ключевом сравнении.

**Важно:** BM25 в этой работе не тестируется.

## 6. Data

- **Dataset/corpus:** Milliyet newspaper collection
- **Language:** Turkish
- **Domain:** news / newspaper articles and columns
- **Period:** 2001–2005
- **Documents:** 408,305
- **Collection size:** approximately 800 MB
- **Tokens before stop-word removal:** approximately 95.5 million
- **Average document length:** approximately 234 tokens before stop-word removal
- **Queries:** 72 ad-hoc queries after filtering
- **Assessors:** 33 native Turkish speakers
- **Relevance judgments:** binary
- **Pooling:** union of top-100 documents from 24 runs = 8 matching functions × NS/F6/SV
- **Average pool size:** 466.5 unique documents/query
- **Average relevant documents in pool:** 104.3/query
- **Unique relevant documents identified:** 6,923
- **Train/dev/test:** no modern explicit train/dev/test separation is defined for the reported comparison
- **Label production:** query owners judged pooled documents through a Web interface; documents outside the pool were not manually assessed

Query forms:

- **QS:** Topic only
- **QM:** Topic + Description
- **QL:** Topic + Description + Narrative

Average number of unique words:

- QS: 2.89
- QM: 12.00
- QL: 26.11

## 7. Baselines

### NS

Main no-stemming baseline.

Purpose: establish how the system performs when morphology is ignored.

### Fixed-prefix methods

F3–F7 test whether a very simple language-light normalization can recover much of the benefit of morphology-aware processing.

### SV

Represents a corpus-statistical stemming approach rather than a hand-crafted morphological analyzer.

### LM5 / LM6 / LV

Represent more linguistically informed approaches.

### Matching functions MF1–MF8

Used to check whether conclusions about stemming survive changes in lexical scoring.

### Fairness of comparison

Strong point:

- the same collection and query set are used across variants;
- multiple matching functions reduce dependence on one scoring formula.

Limitation:

- the pool was built using NS, F6 and SV, not all later variants;
- there is no modern held-out development set for selecting F5/LM choices separately from final evaluation.

## 8. Metrics

### bpref

**Simple meaning:** measures whether judged relevant documents are ranked ahead of judged non-relevant documents.

**Why appropriate here:** relevance judgments are incomplete because only pooled documents were manually assessed.

`bpref` is therefore less sensitive than ordinary measures to the large number of unjudged documents.

### MAP — Mean Average Precision

For each query, Average Precision rewards systems that place relevant documents early throughout the ranking. MAP averages this value across queries.

### Precision@10 / Precision@20

Measures the proportion of relevant documents among the top 10 or top 20 results.

These metrics are useful for the quality of the visible top of the ranking.

## 9. Results

### 9.1 Fixed-prefix selection

Using MF8:

| Variant | bpref | MAP | P@10 | P@20 |
|---|---:|---:|---:|---:|
| F3 | 0.4120 | 0.3134 | 0.5139 | 0.4757 |
| F4 | **0.4382** | 0.4013 | 0.5625 | 0.5361 |
| F5 | 0.4322 | **0.4092** | **0.5917** | **0.5653** |
| F6 | 0.4014 | 0.3885 | 0.5667 | 0.5382 |
| F7 | 0.3901 | 0.3658 | 0.5556 | 0.5181 |

F4 gives the highest bpref, whereas F5 gives the best MAP, P@10 and P@20. F5 is retained as the main fixed-prefix representative.

### 9.2 Main morphology comparison with MF8

| Method | bpref | Relative change vs NS |
|---|---:|---:|
| NS | 0.3255 | — |
| F5 | 0.4322 | +32.78% |
| SV | 0.4304 | +32.23% |
| LV | **0.4504** | **+38.37%** |

Main interpretation:

- all three normalization approaches strongly outperform no stemming;
- LV is numerically best;
- simple F5 remains surprisingly competitive with the much more elaborate LV.

### 9.3 Index vocabulary / storage effect

Reported number of indexed terms:

| Method | Terms |
|---|---:|
| NS | 1,437,581 |
| F5 | 280,272 |
| F6 | 519,704 |
| SV | 418,194 |
| LV | 434,335 |

Approximate posting-list entries:

- NS: 60 million
- F5: 51 million
- LV: 48 million

Thus morphological normalization also reduces index size.

### 9.4 Query length

Moving from QS to QM significantly improves retrieval for F5/LV.

Moving from QM to QL gives a smaller, non-significant additional gain in the reported comparison.

For NS, additional query terms partly compensate for the absence of stemming. This is an important indication that the benefit of morphology can depend on query characteristics.

### 9.5 Stop words

Different stop-word configurations did not produce a statistically significant retrieval-effectiveness gain in the authors' tested ranking setup.

This must not be generalized to BM25 or Uzbek without new experiments.

### 9.6 Scalability

The authors repeat experiments while increasing collection size from 50,000 documents up to the complete 408,305-document collection.

The main relative pattern remains stable: normalization outperforms NS, while the elaborate LV approach does not develop a decisive advantage over simple F5.

## 10. Statistical evidence

- F5, SV and LV significantly outperform NS in the key MF8 comparison: `p < 0.001`.
- LV has a numerical advantage over F5 at MF8, but the per-query difference is not statistically significant in that key comparison.
- The paper also reports comparisons aggregated across matching functions where LV receives stronger statistical support; therefore the safest interpretation is **comparable effectiveness with a numerical advantage for LV**, not universal superiority.
- QS → QM query expansion gives statistically significant improvement for the main normalized variants (`p < 0.01` in the reported analysis).
- Further QM → QL improvement is not statistically significant for those variants.
- No confidence intervals or repeated random-seed analysis are reported in the modern neural sense because these are deterministic classical retrieval experiments.
- There is no modern neural ablation study; instead, the paper performs controlled component/configuration comparisons.

## 11. Strengths

1. Large-scale Turkish IR collection for its period.
2. Real query–document ranking rather than isolated morphology accuracy.
3. Human relevance judgments from native speakers.
4. Comparison of simple and linguistically sophisticated morphology processing.
5. Multiple matching functions reduce dependence on one scoring formula.
6. Statistical testing rather than only reporting raw metric differences.
7. Analysis of query length, document length, collection scale and stop words.
8. Measures index efficiency as well as retrieval effectiveness.
9. Particularly useful as comparative evidence for morphologically rich Turkic-language retrieval.

## 12. Limitations

### Limitations stated or directly visible in the paper

- one language: Turkish;
- one main collection/domain: Milliyet news;
- incomplete relevance judgments from pooling;
- used lemmatizer cannot analyze a large share of distinct forms, motivating LV fallback;
- BM25 and language-model retrieval are outside the main study and are mentioned as future directions.

### Limitations inferred from the experimental design

1. **No Uzbek evidence.** Numerical gains cannot be transferred directly to Uzbek.
2. **No BM25.** The study cannot prove that stemming or lemmatization improves BM25.
3. **No semantic retrieval.** The study says nothing about a modern dense semantic retriever.
4. **No hybrid retrieval.** It does not test lexical–semantic integration.
5. **Pooling bias risk.** The relevance pool was built from NS/F6/SV configurations; F5 and LV were evaluated later and were not pool-contributing systems.
6. **No explicit held-out development set.** Prefix length and some morphology variants are selected using the same general test collection.
7. **TREC-like authored queries rather than production search logs.**
8. **Single-domain document-length behavior.** Findings about longer documents may be specific to news.
9. **Historical ranking architecture.** Modern learned sparse/dense/hybrid methods are outside the scope.

## 13. What the work proves

Within its experimental setting, the work provides strong evidence that:

1. ignoring morphological variation substantially hurts Turkish lexical retrieval;
2. morphological normalization can substantially improve retrieval effectiveness;
3. a very simple fixed-prefix method can obtain effectiveness close to an elaborate lemmatizer-based method;
4. more linguistically sophisticated processing does not automatically guarantee a practically decisive gain;
5. morphology can reduce index vocabulary and posting-list size;
6. retrieval response to morphology varies with query length;
7. the effect of preprocessing must be evaluated empirically rather than assumed.

## 14. What the work does NOT prove

The paper does **not** prove that:

- F5 is optimal for Uzbek;
- five characters is a linguistically correct Uzbek stem;
- lemmatization is unnecessary;
- stemming always beats lemmatization;
- lemmatization always beats stemming;
- stemming improves BM25;
- stop words are irrelevant for BM25 or Uzbek;
- longer documents are universally easier to retrieve;
- morphology improves semantic retrieval;
- morphology improves hybrid retrieval;
- query length determines the optimal lexical–semantic fusion weight;
- Turkish numerical results can be copied to Uzbek.

Most importantly:

> The study does not test the complementarity of lexical and semantic retrieval.

## 15. Relationship to current Uzbek evidence

The correct transfer is methodological, not numerical.

Uzbek research already provides:

- morphological analyzers;
- tokenization/stemming/lemmatization work;
- search-oriented morphology processing.

Can et al. supplies a strong comparative IR precedent showing how morphology should be tested against actual ranked retrieval effectiveness.

The combined implication is:

> Uzbek morphology infrastructure exists, but the retrieval value of `raw`, `stem` and `lemma` variants should be measured under a modern, controlled retrieval setup rather than inferred from linguistic sophistication.

## 16. Relationship to CURRENT_GAP

**Status:** supports; does not narrow materially; does not contradict; does not close.

Current gap concerns:

- morphology-aware lexical representation;
- characteristics of Uzbek queries;
- relative effectiveness of lexical and semantic retrieval;
- conditions under which integration produces stable improvement.

Can et al. supports two parts:

1. morphology can materially affect lexical retrieval;
2. query characteristics, specifically query length, can change the observed morphology effect.

But it does not evaluate:

- Uzbek;
- BM25;
- modern semantic retrieval;
- lexical–semantic complementarity;
- hybrid fusion.

Therefore the current gap should remain unchanged.

## 17. Implications for our research design

### Baseline selection

Required controlled lexical variants:

`BM25_raw`

`BM25_stem`

`BM25_lemma`

All should use the same BM25 implementation and the same tuning protocol.

### Semantic baseline

Use one fixed modern semantic retriever when measuring how morphology changes lexical–semantic complementarity.

### Hybrid comparisons

At minimum compare:

`Semantic`

`BM25_raw + Semantic`

`BM25_stem + Semantic`

`BM25_lemma + Semantic`

Fusion must be evaluated under the same protocol.

### Query taxonomy

Do not report only an overall average.

At minimum analyze:

- query length;
- morphological complexity / affix load;
- rare terms;
- named entities;
- numbers/identifiers;
- Latin/Cyrillic variation;
- lexical overlap;
- paraphrastic/description-like formulations.

Can et al. directly motivates query-length analysis. The other factors remain hypotheses to be tested.

### Relevance judgments / pooling

If a new Uzbek benchmark uses pooling, the pool should include outputs from diverse systems:

- raw lexical;
- morphology-normalized lexical;
- semantic;
- hybrid.

This reduces the risk that one family of systems is disadvantaged because it did not contribute documents to the judgment pool.

### Metrics

Use modern ranking metrics such as:

- nDCG@k;
- MAP;
- Recall@k;
- MRR when appropriate.

Also report statistical significance and per-query analysis.

### Efficiency

Measure:

- index vocabulary size;
- index storage;
- indexing time;
- query latency.

Can et al. shows that morphology can affect system efficiency, not only effectiveness.

### Experimental hygiene

Unlike the historical study, separate:

- development/tuning data;
- final test data.

Do not tune stem length, BM25 parameters or fusion weights on the final test set.

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| Stemming | Привести похожие словоформы к общей укороченной форме | Heuristic normalization of inflected/derived forms to a shared stem-like representation |
| Lemmatization | Определить словарную форму слова | Morphological mapping from a word form to a lemma |
| Fixed-prefix stemming | Просто оставить первые `n` символов | Pseudo-stemming by deterministic prefix truncation |
| Successor Variety | Искать вероятную границу основы по разнообразию продолжений в корпусе | Corpus-statistical stemming based on distinct successor characters for prefixes |
| Pooling | Отобрать кандидатов из результатов нескольких систем и разметить их вручную | IR evaluation protocol for constructing incomplete relevance judgments |
| bpref | Проверить, насколько релевантные оценённые документы стоят выше нерелевантных оценённых | Retrieval metric designed to be robust to incomplete relevance judgments |
| MAP | Среднее качество ранжирования релевантных документов по всем запросам | Mean of Average Precision over queries |
| P@10 | Доля релевантных документов среди первых десяти | Precision at rank cutoff 10 |
| Posting list | Список документов, где встречается термин | Inverted-index structure mapping a term to document occurrences/statistics |

## 19. Open questions / verification needed

1. Deep dive Haddad & Bechikh Ali (2014), which evaluates the same Milliyet collection with TF-IDF, BM25 and a language model.
2. Determine whether later Turkish IR work confirms morphology effects with stronger modern BM25 tuning and modern evaluation.
3. Determine which Uzbek stemmers/lemmatizers are sufficiently reproducible for controlled comparison.
4. Test whether Unicode/apostrophe and Latin/Cyrillic normalization interact with morphology.
5. Test whether raw/stem/lemma lexical variants fail on different query types.
6. Measure whether a semantic retriever compensates for morphology-related lexical mismatch.
7. Measure whether morphology normalization reduces or increases complementarity with semantic retrieval.
8. Verify whether morphology contributes independently enough to justify more than one lexical channel.
9. Design a diverse pooling protocol if new Uzbek qrels are constructed.

## 20. Decision after deep dive

- **Keep current gap?** Yes.
- **Modify gap?** No.
- **Add decision?** No separate permanent methodological decision yet; evidence should remain in the research map until Uzbek experiments validate transfer.
- **Add experiment?** Yes:
  - `BM25_raw ↔ BM25_stem ↔ BM25_lemma`;
  - per-query analysis by query characteristics;
  - compare each lexical variant with the same semantic retriever;
  - measure both effectiveness and efficiency.
- **Add citation to Chapter I?** Yes, section 1.1.
- **Priority after deep dive:** remains CRITICAL as comparative Turkic morphology/IR evidence.
- **Next related work:** Haddad & Bechikh Ali (2014), especially because it explicitly evaluates BM25 on the same Turkish test collection.

### Final retained conclusion

> Can et al. provide strong evidence that morphological normalization matters for Turkish lexical IR, while also showing that a more elaborate morphology-aware method does not automatically dominate a simple normalization strategy. The work additionally demonstrates that query characteristics can moderate the observed benefit of morphology. For the Uzbek PhD, the correct consequence is not to adopt a particular Turkish stemmer, but to experimentally compare `raw/stem/lemma` lexical representations and then determine how these choices change complementarity with semantic retrieval.
