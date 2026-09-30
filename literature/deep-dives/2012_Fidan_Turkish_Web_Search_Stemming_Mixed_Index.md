# Fidan (2012): Identifying the Effectiveness of a Web Search Engine with Turkish Domain Dependent Impacts and Global Scale Information Retrieval Improvements (PhD thesis, METU), Chapter 4: stemming and a mixed stemmed/unstemmed index for Turkish web search

**Targeted deep-dive status:** COMPLETED (AI-assisted, pending researcher review)
**Completed:** 2026-09-28
**Literature ID:** `MORPH-024` (assigned 2026-09-28, approved by researcher)
**Systematic-review record:** `CR002210`. Full-text triage: INCLUDE, reading priority HIGH, reading tier 1 ("прямо по теме пробела"), `carries_complementarity_evidence = NO`. Triage evidence location: Ch. 4.4, Tables 4.4–4.8.
**Provenance:** AI-assisted deep dive (Claude). The thesis is written in **English** (with a Turkish abstract, "Öz"); 106 PDF pages (the abstract states "February 2012, 90 pages"). **PDF page = printed page + 14** in the main body. What was read: title and approval pages, English and Turkish abstracts, table of contents and lists of tables/figures, Ch. 1 (motivation, contributions), Ch. 2 (background; Sec. 2.3 on stemming in full), **all of Ch. 4** (the only chapter with morphology and retrieval-effectiveness experiments), Ch. 6 (conclusions), references on stemming, and the CV/vita. Ch. 3 (PageRank/TrustRank vs Alexa lists, Kendall tau) and Ch. 5 (eye-tracking with thumbnails) were checked only by table of contents and grep: they contain no morphology or lexical-representation experiments. **Pages checked visually** (110 dpi page images): PDF p. 2 (approval page), PDF pp. 56–71 (printed pp. 42–57: Fig. 4.1, Table 4.2, Eqs. 4.1–4.7, Sec. 4.4.2 data, Tables 4.4–4.8, Fig. 4.3). Every number from Tables 4.4–4.8 below was compared with the page image. Numbers computed by us are marked **[computed]** and were computed in Python.
**Source rule:** **the thesis is the primary and only authoritative source** for what the author did and found. The web was used only to verify the bibliographic record (bibliographic check: dblp, see §1). Statements about other Turkish IR works come from the thesis's own citations or from other project cards and are marked as such; they are not used as evidence about this thesis.
**Verification:** independent AI verifier pass 2026-09-28; 7 findings addressed.
**Reliability:** **A for source type, weak as evidence.** It is a doctoral thesis (Ph.D., Information Systems, Middle East Technical University, examining committee date 09.02.2012), listed as a METU PhD thesis in dblp. The morphology experiment in Ch. 4, however, is small and under-reported: 25 queries, top-10 only, "Precision at K" with K never stated, "statistically significant" claims with no test named, no per-query data, and ambiguous details of the stemmer and of the mixed run. The author also led the company that built the search engine under test (vita, p. 88; see §12). Treat its numbers as indicative only.

---

## Кратко для исследователя (RU)

- **Что это.** Докторская диссертация (PhD, Middle East Technical University, Анкара, 2012; руководитель Assoc. Prof. Dr. Onur Demirörs, соруководитель Assist. Prof. Dr. Meltem Turhan Yöndem). Текст на английском. Из трёх частей к нашей теме относится только **гл. 4** (pp. 37–57): стемминг для турецкого веб-поиска на коммерческой поисковой системе Bilgi.com. Гл. 3 (PageRank) и гл. 5 (миниатюры страниц, eye-tracking) к морфологии не относятся.
- **Что сделано в гл. 4.**
  - Коллекция: 583 771 турецких веб-страниц (≈3.2 GB). Построены **два индекса** Lucene: по исходным словоформам и по «стеммам».
  - Стемминг — адаптированный для работы (p. 44) турецкий «stemmer/lemmatizer» на основе морфологической модели Oflazer (1994) и словаря ≈96 000 статей (на базе словаря TDK).
  - Ранжирование — **TF-IDF Lucene (классическая векторная модель), не BM25** (Eq. 4.1–4.3, p. 47).
  - 25 запросов из месячного журнала запросов (только многословные, без опечаток); у 18 из них стеммированная форма отличается от исходной.
  - 7 конфигураций «тип запроса × тип индекса» (Table 4.5), включая **смешанную выдачу**: половина top-10 из поиска «исходный запрос → исходный индекс», половина из «стеммированный запрос → стеммированный индекс».
  - Оценка: 10 студентов METU размечали top-10 по пяти градациям (PERFECT…BAD); метрики «Precision at K» (релевантно = GOOD и выше) и NDCG.
- **Главные числа** (Tables 4.6–4.8, pp. 55–56):
  - исходный запрос → исходный индекс: P 0.75 / NDCG 0.53;
  - стеммированный → стеммированный: P 0.86 / NDCG 0.48;
  - смешанная выдача (Exp. 7): P 0.81 / NDCG 0.52;
  - несогласованные пары (запрос и индекс в разных представлениях): P 0.62–0.64, NDCG 0.36–0.42.
- **Вывод автора:** стемминг повышает «IR precision», но снижает «Web relevance» (NDCG), а смешанная выдача даёт лучшую пару (P +6, NDCG −1). Все «%» в тексте — это **абсолютные пункты**, а не относительные изменения **[computed]**: например, «11% improvement» = 0.75 → 0.86 (+14.7% относительно).
- **Что это значит для нас.** Это ранний пример **объединения двух лексических представлений одного языка** (исходные формы + стеммы) в одной выдаче. Идея близка к нашей логике «морфология как вариант лексического представления». Но:
  - нет BM25 (TF-IDF Lucene);
  - нет плотного поиска и гибрида lexical + dense;
  - нет перекрытия выдач, уникально найденных релевантных документов, oracle union;
  - нет анализа по отдельным запросам и по признакам запросов (автор сам ставит это как future work: длина запроса, informational/navigational/transactional, p. 57);
  - «смешивание» — простая склейка 5 + 5 результатов, порядок и удаление дубликатов не описаны.
- **Слабые места (по тексту работы):**
  - K в «Precision at K» нигде не указан (извлекается top-10);
  - «statistically significant» заявлено без названия теста и без p-значений;
  - не описано, как объединялись оценки 10 разметчиков, согласованность разметчиков не приводится;
  - неясно, считаются ли Table 4.7 и Exp. 7 по 18 или по 25 запросам;
  - неясно, какой из двух компонентов (стеммер без словаря или лемматизатор со словарём) использовался при индексации; подпись Table 4.2 «stemmer», а текст перед ней — «lemmatizer»; во введении (p. 38) сказано «lemmatizer-based stemmer», что указывает на лемматизатор со словарём, но в Sec. 4.3.1 и 4.4.2 везде «stemmer/lemmatizer»;
  - «стеммы» запросов часто срезают и словообразовательные аффиксы (sözlük → söz, yetkili → yetki, askerlik → asker; Table 4.4), то есть это ближе к агрессивному стеммингу, чем к лемматизации.
- **Внутренние несоответствия:** MapReduce-эксперимент — «кластер из более чем ста компьютеров» (p. 49) против «кластера из 4 компьютеров» (p. 51); «≈16 млн терминов», из них 4.1 млн исходных и 3.78 млн стеммированных (p. 51) — части не складываются в целое; гл. 6 (p. 80) приписывает «рост precision при падении Web relevance» предыдущим работам, а гл. 4 (p. 56) — собственным экспериментам.
- **Для gap (предложение):** существенного влияния на ядро v0.8 нет. Работа слабо поддерживает мотивацию: исходные формы и стеммы в турецком дают разные выдачи, и их объединение может сохранить сильные стороны обоих. Как это устроено (перекрытие, уникальные релевантные документы), в работе не измерено.
- **Практическая польза:** (1) в эксперименте с запросом и индексом в разных представлениях качество резко падает — для узбекского индекс и запрос нужно нормализовать одним и тем же анализатором; (2) доля запросов, не меняющихся при стемминге (здесь 7 из 25), — простой признак запроса; (3) P и NDCG здесь расходятся, поэтому нужно сообщать несколько метрик и полные параметры (K, метка порога, нормировка NDCG).

---

## 1. Bibliographic record

- **Author:** Güven Fidan
- **Degree:** Doctor of Philosophy in Information Systems (approval page, p. ii; "Ph.D., Department of Information Systems", abstract p. iv)
- **University / institute:** Middle East Technical University (METU / ODTÜ), Graduate School of Informatics, Ankara, Turkey
- **Supervisor:** Assoc. Prof. Dr. Onur Demirörs (Information Systems, METU)
- **Co-supervisor:** Assist. Prof. Dr. Meltem Turhan Yöndem (Computer Engineering, Okan University)
- **Examining committee:** Assist. Prof. Dr. Aysu Betin Can, Assoc. Prof. Dr. Onur Demirörs, Assist. Prof. Dr. Meltem Turhan Yöndem, Dr. Ali Arifoğlu, Prof. Dr. İsmail Hakkı Toroslu (approval page; date 09.02.2012). The signature lines are blank in this PDF copy.
- **Year:** 2012 (February)
- **Length:** "90 pages" (abstract); 106 PDF pages including front matter
- **Venue metadata (triage):** PQDT – Global (ProQuest Number 31670238, last PDF page)
- **Bibliographic check:** dblp lists "Identifying the effectiveness of a web search engine with Turkish domain dependent impacts and global scale information retrieval improvements", PhD thesis, Middle East Technical University, 2012, under Guven Fidan (bibliographic check: dblp.org/pid/11/6904). DOI: not found; a METU repository URL was not verified.
- **Related publication of Ch. 4:** none listed in the thesis's publication list (vita, pp. 88–89); dblp shows no separate Ch. 4 paper (bibliographic check: dblp).
- **Source type:** doctoral thesis
- **Reliability:** A (source type) / weak evidence (see header)
- **Full text available:** yes (`07_full_text/pdfs/CR002210.pdf`, 106 pages)

## 2. Why this work matters to the PhD

| Axis | Relation |
|---|---|
| Lexical retrieval | Lucene TF-IDF (classic vector space + coord factor). **Not BM25.** Two indexes: unstemmed and stemmed |
| Semantic retrieval | **Absent** |
| Hybrid retrieval | **No lexical + dense hybrid.** There is a simple **combination of two lexical representations** (half the top-10 from the unstemmed channel, half from the stemmed channel) |
| Uzbek / Turkic morphology | Direct typological relevance: Turkish is agglutinative and closely related to Uzbek. Morphological model after Oflazer (1994), TDK-based lexicon |
| Low-resource retrieval | Not framed as low-resource; a commercial web search engine with its own crawl |
| Current gap | It touches the idea "raw and stem lexical representations as combinable channels" but measures no complementarity (§16) |

The work is useful mainly as (a) a Turkic example of **query × index representation mismatch** and (b) an early instance of **fusing raw and stemmed lexical runs**, which is conceptually close to our `Lexical_raw / Lexical_stem` variants.

## 3. Research problem

### Simple explanation

Turkish words carry many suffixes, so a search for "sonuçları" (results, plural possessive) may miss pages that write "sonuç" (result). Cutting words to stems helps matching, but it can also merge unrelated words or change what the user meant. The author asks whether stemming helps a real Turkish web search engine, and whether a mixture of stemmed and unstemmed results keeps the benefits of both.

### Formal formulation

The chapter states two claims (p. 37, verbatim): "applying stemming increases retrieval effectiveness while decreasing Web relevance" and "the best precision and Web relevance pair is obtained by combining the results, retrieved by sending unstemmed query to unstemmed content and sending stemmed query to stemmed content." A third contribution is engineering: stemming at indexing time via MapReduce.

- Query representation `Q ∈ {unstemmed, stemmed}`; index/content representation `C ∈ {unstemmed, stemmed, mixed}`.
- For each of 7 `(Q, C)` configurations (Table 4.5), retrieve the top 10 and have users grade them.
- "IR precision score" = Precision at K; "Web relevance" = NDCG (the author's terminology; both come from the same user labels).

## 4. Main idea

### Simple explanation

Keep two copies of the index: one with words as written and one with words reduced to stems. For each query, take half of the results from "original query on original index" and half from "stemmed query on stemmed index", and show them together.

### Concrete example

From Table 4.4 (p. 53):

- "Iddia maç sonuçları" (Table 4.4 gloss: "Bets match result") → stemmed "Iddia maç sonuç".
- The unstemmed channel finds pages containing exactly "sonuçları"; the stemmed channel also finds pages with "sonuç", "sonucu", etc., after both are reduced to "sonuç".
- The mixed page shows (presumably) 5 results from each channel. How they are ordered and whether duplicates are removed is not described.

### Formal method

- Ranking function (Eq. 4.1, p. 47; Lucene "practical scoring function"):
  `score(q,d) = coord(q,d) × queryNorm(q) × Σ_{t in q} ( tf(t in d) × idf(t)² × termBoost × norm(t,d) )`,
  with `tf = frequency^{1/2}` (Eq. 4.2), `idf(t) = 1 + log(numDocs/(docFrequency+1))` (Eq. 4.3), `queryNorm` (Eqs. 4.4–4.5) and `norm(t,d) = docBoost × lengthNorm(field) × Π fieldBoost` (Eq. 4.6).
- Bilgi.com normally uses PageRank variants, but "since the main goal is to measure IR effectiveness and Web relevance, Term Frequency (TF) - Inverse Document Frequency (IDF) is used" (Sec. 4.3.2, p. 43).
- Mixed run: "Half of the results are retrieved from unstemmed content, and the other half is retrieved from stemmed index" (Sec. 4.3.1, p. 42). No score normalization, weighting or rank-based fusion is described.

## 5. Architecture / algorithm

1. **Crawl.** Focused crawler for Turkish pages with language identification (Sec. 4.3.1, p. 42).
2. **Parse and index twice** (Fig. 4.1, p. 42): unstemmed and stemmed inverted indexes (Lucene). No stop-word removal (Sec. 4.4.2, p. 51). Tokenization, lowercasing (including Turkish dotted/dotless i), apostrophe handling and field structure are **NOT_REPORTED**.
3. **Turkish stemmer/lemmatizer** (Sec. 4.3.3, pp. 43–45):
   - both components use a morphological model "based on Oflazer (1994)", which "combines phonological variations and morphotactics as single deterministic finite automata";
   - **stemmer:** "No lexicon is required"; the model is "used in reverse to get a reduced form"; "Certain stem voice changes can be handled";
   - **lemmatizer:** uses a lexicon; longest stem preferred on ambiguity ("adam, ada+m"); "When a stem cannot be determined, the whole form is returned as the stem"; ≈100K words/s;
   - known failures: "does not handle certain types of exceptional stem form changes, such as hakkı, yiyor" (p. 45);
   - **which of the two was used for indexing and query stemming is not stated explicitly** in Secs. 4.3–4.4, which say "stemmer/lemmatizer" throughout; Sec. 4.1 (p. 38) says "we use a language specific lemmatizer-based stemmer (for Turkish)", which points to the lexicon-based lemmatizer (see §19 on Table 4.2).
4. **Lexicon** (Sec. 4.3.4, pp. 45–46): built from TDK (Turkish Language Institute) entries, stored in OLIF, "nearly 96,000 entries". The sample entry (Table 4.3) carries `<updater>guven.fidan@agmlab.com</updater>`.
5. **Query stemming:** the same component stems the query ("query substitution").
6. **Mixed retrieval:** half of the top-10 from each channel (Sec. 4.3.1; Sec. 4.4.3).
7. **Scalability:** stemming during indexing as a MapReduce job (map emits `<stemmedWord, docID>`, reduce emits postings; Sec. 4.3.6, p. 49). Fig. 4.3 (p. 57): indexing time vs number of map tasks (5–30).

## 6. Data

- **Collection:** Turkish web pages from the author's focused crawl; **583,771 pages, "about 3,2GB"** (Sec. 4.4.2, p. 51).
- **Vocabulary:** "The number of overall terms is around 16 million where 4,1 million of terms are indexed as unstemmed content and 3,78 million of terms are indexed as stemmed forms" (p. 51). The relation between 16M and 4.1M + 3.78M = 7.88M **[computed]** is unexplained. If 4.1M and 3.78M are vocabulary sizes, stemming shrinks the vocabulary by only 7.8% **[computed]**. That is small for a Turkish morphological stemmer, but the thesis does not define "terms".
- **Queries:** "randomly 50 queries from a one month query log are selected"; misspelled and one-word queries removed; "Finally, 25 correctly spelled queries, and 18 among them are stemmed ... 7 of them are originally stem forms of words" (p. 52). Table 4.4 lists all 25 with stemmed forms and English glosses; our count of unchanged queries in Table 4.4 = 7 ✓ **[computed]**. All queries have 2–4 words; many look navigational/transactional ("Online film izle", "Hava durumu", "Ucuz uçak bileti").
- **Relevance judgments:** "10 different users ranked the top 10 results for the same queries"; METU students aged 20–28 familiar with web search; five grades PERFECT, EXCELLENT, GOOD, FAIR, BAD (Sec. 4.4.3, p. 54).
  - Relevant for Precision = GOOD, EXCELLENT or PERFECT (Sec. 4.4.1, p. 50).
  - NDCG gain `r ∈ {0..4}`, BAD = 0, PERFECT = 4 (p. 51).
  - How the 10 users' labels were aggregated (mean, majority, per-user metrics then averaged), whether users judged all 7 runs, and inter-annotator agreement: **NOT_REPORTED**.
  - Judgments cover only the top 10 of each run; no pooling across runs is described.
- **Train/dev/test:** not applicable (no learned components); no tuning described.

## 7. Baselines

| Run (Table 4.5) | What it is | Fair comparison? |
|---|---|---|
| Exp. 1: unstemmed query → unstemmed index | Surface-form TF-IDF; the natural baseline | Yes, as the reference |
| Exp. 2: unstemmed query → stemmed index | Representation mismatch | A "straw man": inflected query words cannot match stems. The author says the drop is "as expected" (p. 55) |
| Exp. 3: unstemmed query → mixed | Half each | Mixed with a mismatched channel |
| Exp. 4: stemmed query → unstemmed index | Representation mismatch | Also a straw man ("expected results too", p. 55) |
| Exp. 5: stemmed query → stemmed index | Stemmed TF-IDF | Yes vs Exp. 1, if both use the same query set (unclear, §19) |
| Exp. 6: stemmed query → mixed | Half each | Mixed with a mismatched channel |
| Exp. 7: unstemmed→unstemmed + stemmed→stemmed | The proposed mixed run | Yes vs Exps. 1 and 5; it is the only real "combination" |

There is no stronger lexical baseline (BM25, other stemmers such as fixed-prefix truncation, Zemberek) and no query-expansion alternative, although related work (Sec. 4.2) mentions both.

## 8. Metrics

| Metric | Definition in the thesis | Simple meaning | Comment |
|---|---|---|---|
| Precision at K | "portions of documents ranked in the top K results that are labeled as relevant"; relevant = GOOD or better (p. 50) | Share of good results on the first page | **K is never stated.** Only the top 10 were retrieved and judged, so K ≤ 10; P@10 is the likely reading **[inferred]** |
| NDCG | `Nq = Mq Σ_{j=1..K} (2^{r(j)} − 1)/log₂(1 + j)` (Eq. 4.7, p. 51); `Mq` normalizes so that "a perfect ordering obtains NDCG of 1" | Rewards highly graded results at the top | K again unspecified. Whether the ideal ordering uses only the run's own judged top 10 or all judged documents for the query is not stated; this changes what NDCG measures |
| "IR precision score" vs "Web relevance" | The author's labels for P@K and NDCG | — | Both come from the same user labels. The difference is binary threshold vs graded, rank-discounted gain; it is not two different constructs |
| Indexing time | Seconds vs number of map tasks (Fig. 4.3) | Efficiency | Not retrieval effectiveness |

## 9. Results

### Tables 4.6–4.8 (printed pp. 55–56; checked on page images)

| Exp. | Query → content | Precision at K | NDCG | Source |
|---|---|---:|---:|---|
| 1 | unstemmed → unstemmed | 0.75 | 0.53 | Tables 4.6 and 4.8 |
| 2 | unstemmed → stemmed | 0.62 | 0.42 | Table 4.6 |
| 3 | unstemmed → mixed | 0.71 | 0.51 | Table 4.6 |
| 4 | stemmed → unstemmed | 0.64 | 0.36 | Table 4.7 |
| 5 | stemmed → stemmed | **0.86** | 0.48 | Tables 4.7 and 4.8 |
| 6 | stemmed → mixed | 0.77 | 0.44 | Table 4.7 |
| 7 | unstemmed→unstemmed + stemmed→stemmed | 0.81 | 0.52 | Table 4.8 ("Mix Content") |

The "Mix Content" label means different things in the three tables (Exps. 3, 6 and 7).

### The author's percentages are absolute differences

Recomputed **[computed]**:

| Author's claim (page) | Values | Absolute | Relative |
|---|---|---:|---:|
| Exp. 2 vs 1: "13% decrease" P, "11% decrease" NDCG (p. 55) | 0.75→0.62; 0.53→0.42 | −0.13 / −0.11 ✓ | −17.3% / −20.8% |
| Exp. 5 vs 4: "22% increase" P, "12% increase" NDCG (p. 55) | 0.64→0.86; 0.36→0.48 | +0.22 / +0.12 ✓ | +34.4% / +33.3% |
| Exp. 5 vs 1: "11% improvement" P, "5% decrease" NDCG (p. 56) | 0.75→0.86; 0.53→0.48 | +0.11 / −0.05 ✓ | +14.7% / −9.4% |
| Exp. 7 vs 1: "6% increase" P, NDCG "decreased only by 1%" (p. 56) | 0.75→0.81; 0.53→0.52 | +0.06 / −0.01 ✓ | +8.0% / −1.9% |

All stated percentages match absolute point differences; none match relative changes.

### Further readings of the tables [computed]

- Exp. 7 vs Exp. 5: P −0.05, NDCG +0.04. The mixed run is not best on either metric. It is a compromise: P between Exps. 1 and 5, NDCG just below Exp. 1.
- Exp. 7's P = 0.81 is close to the mean of Exps. 1 and 5 (0.805). That is what one would expect if the mixed list were 5 + 5 results from the two channels. Its NDCG, 0.52, is above the mean (0.505). This is an arithmetic observation only; per-rank data are not reported.
- Mismatched representations (Exps. 2 and 4) are the worst runs on both metrics.
- **P and NDCG disagree between Exps. 1 and 5** (P +0.11, NDCG −0.05). With the thesis's definitions, this can happen if stemmed results are more often GOOD but less often PERFECT/EXCELLENT, or place the best results lower. The thesis gives no label distribution to decide. The author reads it as "stemming ... may reduce the Web relevance" (p. 56).

### Fig. 4.3: indexing time vs map tasks (p. 57)

Read from the plot (approximate): ≈530 s (5 tasks), ≈430 s (10), ≈280 s (15), ≈260 s (20), ≈250 s (25), ≈270 s (30). The data volume used for this run is not stated.

## 10. Statistical evidence

- **Significance tests:** the text calls the Exp. 2 vs 1 and Exp. 5 vs 4 differences "statistically significant" and the −0.01 NDCG of Exp. 7 "statistically insignificant" (pp. 55–56). **No test, unit of analysis (queries? users?), p-value or α is reported.** No significance claim is made for Exp. 5 vs 1 (on either metric) or for Exp. 7 vs 1 on Precision.
- **Confidence intervals:** NOT_REPORTED.
- **Runs:** queries were sent "three times" and the top 10 retrieved each time (p. 52); why, and how the three retrievals were used, is not explained. Variance: NOT_REPORTED.
- **Ablation:** the 7 setups form a small factorial design (query form × index form). There is no ablation of the stemmer vs lemmatizer, stop-words or scoring.
- **Per-query analysis:** **none.** Only averages "over all tested queries" (p. 54). No per-query wins/losses, no split by the 18 changed vs 7 unchanged queries.
- **Overlap / unique relevant hits / oracle union** between the unstemmed and stemmed channels: **NOT_REPORTED**.
- **Inter-annotator agreement:** NOT_REPORTED.

## 11. Strengths

- A real Turkish web collection (≈584K pages) and real log queries, judged by users with graded labels.
- A clean **query-form × index-form factorial design** (Table 4.5) that exposes the cost of representation mismatch.
- It explicitly **combines raw and stemmed lexical runs**, which is conceptually close to treating morphology as alternative lexical representations.
- Queries and their stemmed forms are fully listed (Table 4.4), so the stemmer's behaviour on the test queries can be inspected.
- Morphological analyzer based on a published finite-state model (Oflazer 1994) with a ≈96K-entry lexicon.
- The ranking function is written out in full (Eqs. 4.1–4.6).

## 12. Limitations

### Stated by the author

- Stemming "may reduce unrelated words to the same stem and it may fail to reduce related words to a common stem" (p. 38).
- Stemming one-word queries "has risk of changing query intent", so they were excluded (p. 52).
- The lemmatizer does not handle some exceptional stem changes ("hakkı, yiyor", p. 45).
- Future work: effects of long vs short queries and of query type (informational, navigational, transactional) (p. 57; p. 80). This implies they were not analysed.

### Inferred from the experimental design

1. **Very small evaluation:** 25 queries (18 affected by stemming), top 10 only. Differences of a few points are within plausible noise; no test is described.
2. **Metric under-specification:** K unknown; NDCG ideal ordering unknown; label aggregation over 10 users unknown.
3. **Unclear query set per table.** "we sent unstemmed queries and stemmed 18 queries to indexes" (p. 52) suggests the stemmed-query runs (Exps. 4–6, maybe 7) use 18 queries and the unstemmed runs 25. If so, Exps. 1 vs 5 vs 7 are compared on different query sets.
4. **Stemmer identity not stated explicitly**: stemmer (no lexicon) or lemmatizer (lexicon)? Table 4.2 caption says stemmer; the sentence before it says lemmatizer. Sec. 4.1 (p. 38) says "lemmatizer-based stemmer", which points to the lemmatizer, but Secs. 4.3.1 and 4.4.2 say only "stemmer/lemmatizer".
5. **Aggressive and derivational reduction** in Table 4.4: "Türkçe ingilizce sözlük" → "Türk ingiliz söz" (dictionary → word), "Bedelli askerlik" → "Bedel asker", "Sayısal" → "Sayı", "Telekomünikasyon" → "Telekom". Several of these change the meaning, which may explain part of the lower NDCG. The thesis does not discuss it.
6. **Naive fusion.** 5 + 5 interleaving without described ordering, deduplication or score normalization. No comparison with other fusion schemes.
7. **TF-IDF Lucene, not BM25**; no stop-word removal; tokenization and Turkish case folding not reported.
8. **"IR precision" vs "Web relevance" framing** is terminological: both metrics come from the same labels.
9. **Possible conflict of interest.** The vita lists the author as CEO of AGMLab Ltd. since 2004 (p. 88). Sec. 2.1 says Bilgi.com is a project "conducted by AGMLab"; the lexicon sample names an agmlab.com updater (Table 4.3). The thesis does not discuss this.
10. **Internal inconsistencies** (see §19): cluster size (>100 vs 4 computers); term counts; attribution of the precision/relevance trade-off to prior work (Ch. 6) vs own finding (Ch. 4).

## 13. What the work proves

Within its small, under-specified setting (25 Turkish web queries, Lucene TF-IDF, user-graded top 10):

- **Query and index must use the same representation.** Mismatched runs are clearly worst: P 0.62–0.64 vs 0.75–0.86; NDCG 0.36–0.42 vs 0.48–0.53 (Tables 4.6–4.7).
- **Stemmed → stemmed gives higher binary precision than unstemmed → unstemmed** (0.86 vs 0.75), but **lower graded NDCG** (0.48 vs 0.53) (Table 4.8). Neither difference has a reported significance test.
- **A 50/50 mix of raw and stemmed results** gives intermediate precision (0.81) with NDCG close to the raw run (0.52) (Table 4.8). It is a compromise between the two channels, not a dominant run.
- Stemming at indexing time can be parallelized with MapReduce (Fig. 4.3).

## 14. What the work does NOT prove

- **That the mixed run is the "best" in a statistical sense.** No test is reported for Exp. 7 vs Exp. 1 or vs Exp. 5, and Exp. 7 is lower than Exp. 5 on P and lower than Exp. 1 on NDCG.
- **That stemming "decreases Web relevance" in general.** One stemmer (with visibly aggressive reductions), 25 queries, TF-IDF, unspecified NDCG normalization.
- **Why the raw and stemmed channels differ, or whether they are complementary.** No overlap, no unique relevant documents per channel, no oracle union, no per-query analysis.
- **Anything about BM25, lemmatization vs stemming, dense retrieval or lexical–semantic hybrids.** None were tested.
- **Anything about query features.** Query length and type are explicitly left to future work.
- **Generalization** to other collections or to ad hoc (non-web) retrieval.

## 15. Relationship to current Uzbek evidence

- **No Uzbek data.** Turkish is the closest well-studied relative (Oghuz vs Karluk Turkic; both agglutinative and suffixing), so the query/index mismatch effect and the risk of derivational over-stemming (e.g., -lik, -li, -sal) are directly relevant to Uzbek (-lik, -li, -chi ...) **[context, not from the thesis]**.
- It adds to the Turkish lexical-morphology cluster in section C:
  - MORPH-001 (Can et al. 2008) and CR000651 (Can et al. 2006; pending card): Milliyet, many stemmers, no BM25/dense;
  - MORPH-002 (Haddad & Bechikh Ali 2014): BM25 with Zemberek vs truncation;
  - CR002145 (Kılıç 2008; pending card): Lucene stemmer on Milliyet;
  - CR001537 (Öztürkmenoğlu & Alpkoçak 2012; pending card): Turkish lemmatization in IR;
  - CR002158 (Ocalan 2009; pending card): Bilkent news portal.
  Fidan is the only one in this list that **combines raw and stemmed runs** in one result list, and the only web-search one with graded user judgments.
- Like the rest of this cluster, it has no dense retrieval and no complementarity analysis.

## 16. Relationship to CURRENT_GAP

**Classification (proposal):** *supports (weakly, as motivation)* + *no material effect on the residual core*.

- **Supports / motivates:** the thesis treats raw and stemmed forms as two lexical representations whose results can be combined, and finds that each gives a different quality profile (P vs NDCG). That is consistent with v0.8's view of morphology as a **variant of the lexical representation** rather than an independent paradigm. It also suggests that raw and stemmed runs retrieve partly different documents. The thesis does not measure this.
- **Does not touch** any v0.8 core element:
  - no `BM25_raw/stem/lemma` (TF-IDF, one stemmer; no lemma variant distinguished);
  - no fixed dense comparator D;
  - no `H_raw/H_stem/H_lemma` lexical–dense fusion;
  - no unique relevant hits, overlap, oracle union or incremental hybrid gain;
  - no query-feature analysis.
- **Not a gap killer** under any of the four conditions in "What can still kill this gap".
- **Possible side note for the boundary:** fusing raw and stemmed *lexical* runs of a Turkic language was done as early as 2012 (in a weak form). A claim like "combining morphological variants of the lexical channel is new" should therefore be avoided. This is a proposal only; `CURRENT_GAP.md` has not been edited.

## 17. Implications for our research design

- **Morphology preprocessing.**
  - Always analyse query and documents with the **same** analyzer. Mismatched conditions are not informative baselines (Exps. 2 and 4).
  - Report whether the Uzbek stemmer strips **derivational** suffixes. Table 4.4 shows how derivational stripping changes meaning ("sözlük" → "söz"). Consider separating inflection-only stemming, full stemming and lemmatization as distinct conditions.
  - Report the vocabulary-size change raw → stem → lemma with clear definitions (types vs tokens), unlike the ambiguous "terms" here.
- **Additional lexical condition (optional).** A `BM25_raw ⊕ BM25_stem` fusion run is a cheap way to see how much of the morphology effect is recoverable inside the lexical channel before adding D. Report its overlap / unique hits, which Fidan did not.
- **Fusion.** If fusion is used, describe ordering, deduplication and normalization exactly; a plain 5 + 5 split is not reproducible.
- **Query taxonomy.**
  - Add "query unchanged by the stemmer/lemmatizer" (here 7/25) as a query feature, and report results separately for changed vs unchanged queries.
  - Record query type (informational / navigational / transactional) and length, which the author named as future work.
- **Qrels and metrics.**
  - Specify cutoffs (P@10, nDCG@10), grade thresholds, the NDCG ideal (pooled over all judged documents per query) and label aggregation; report inter-annotator agreement.
  - Report graded and binary metrics; they can disagree, as here.
  - Use pooled judgments over all conditions, not top-10 per run in isolation.
- **Statistics.** Enough queries for per-query paired tests (randomization/bootstrap), with the test and unit named; 25 queries is too few for small effects.

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| Stemming | Cutting a word down to a shorter common form so different endings match | Map word form → stem; the stem need not be a real word |
| Lemmatization | Replacing a word by its dictionary form | Map word form → lemma using morphology + lexicon |
| Unstemmed / stemmed index ("content") | Index built from words as written vs from their stems | Two inverted indexes over the same collection |
| Query substitution | Replacing the user's query words by their stems | Apply the same analyzer to the query |
| Mixed content (Exp. 7) | Showing half the results from the raw index and half from the stemmed index | Naive fusion by fixed quota interleaving |
| Lucene TF-IDF | Classic word-matching score in Lucene (before BM25 became its default) | `coord × queryNorm × Σ tf·idf²·boost·norm` (Eq. 4.1) |
| Precision at K | Share of relevant results among the first K | `|relevant ∩ top-K| / K` |
| NDCG | Graded score that rewards very relevant results at the top | `DCG / ideal DCG`, gain `2^r − 1`, discount `log₂(1+rank)` |
| Derivational vs inflectional suffix | Derivational suffixes make new words ("söz" → "sözlük", word → dictionary); inflectional ones change grammatical form ("sonuç" → "sonuçları") | Morphological categories |
| Complementarity (project term) | Each channel finds some relevant documents the other misses | Unique relevant hits, overlap, oracle-union gain |

## 19. Open questions / verification needed

1. **K** in "Precision at K" and the NDCG cutoff and ideal ordering: NOT_REPORTED (probably 10).
2. **Query set per table:** 25 or 18 queries in Table 4.7 and in Exp. 7? (p. 52 wording).
3. **Stemmer or lemmatizer?** Which component produced the stemmed index and queries? (Sec. 4.3.3 describes both; Table 4.2 caption "stemmer" vs text "lemmatizer", p. 44; Sec. 4.1, p. 38, says "lemmatizer-based stemmer", which suggests the lemmatizer.)
4. **Significance test** behind "statistically significant" (pp. 55–56): test, unit, p-values unknown.
5. **Aggregation of 10 users' labels** and agreement: NOT_REPORTED. Why queries were sent "three times" (p. 52).
6. **Mixed-list construction:** ordering, deduplication, what happens when a channel returns fewer than 5 results.
7. **Internal inconsistencies:**
   - MapReduce cluster: "more than a hundred computers" (Sec. 4.3.6, p. 49) vs "a cluster of 4 computers" (Sec. 4.4.1, p. 51). This may be two different setups, but the thesis does not say so.
   - Term counts: "around 16 million" overall vs 4.1M unstemmed + 3.78M stemmed = 7.88M **[computed]** (p. 51).
   - Attribution: Ch. 6 says "In contrast to the previous studies that improved IR precision scores while decreasing Web relevance with stemming" (p. 80). Ch. 4 presents the precision-up/NDCG-down pattern as the author's own finding, and says previous Turkish studies showed stemming "improves effectiveness" (p. 56).
   - Table 4.2 caption vs preceding sentence (stemmer vs lemmatizer), p. 44.
   - Claim vs results: the abstract (p. v) says the Turkish stemmer "has remarkable improvements on Web relevance when used in a mixed framework", and Ch. 4 (p. 37) proposes a framework that "increases IR precision score and Web relevance". Table 4.8 (p. 56), however, shows mixed NDCG 0.52 vs 0.53 for the unstemmed run, i.e. no gain in Web relevance (the author himself calls it a 1% "statistically insignificant" decrease).
   - Sec. 4.1 refers to "Section 3/4/5" for Sec. 4.3/4.4/4.5 (p. 39), probably left over from a paper version. Minor.
8. Whether Ch. 4 was published as a peer-reviewed paper: none is listed in the vita or dblp (bibliographic check). Not pursued further.

## 20. Decision after deep dive

- **Keep current gap?** Yes; v0.8 refined unchanged (§16).
- **Modify gap?** No. Optionally add a boundary note that fusing raw and stemmed lexical runs for a Turkic language has an early (2012, weak) precedent, so novelty must not rest on "combining morphological lexical variants" (researcher's decision).
- **Add decision?** Proposed (researcher's decision):
  - "Query and document analysis use the same analyzer in every lexical condition; mismatched conditions are not used as baselines."
  - "The stemmer's treatment of derivational suffixes is documented; results are also reported separately for queries changed vs unchanged by normalization."
- **Add experiment?** Optional low-cost control: `BM25_raw ⊕ BM25_stem` (and `⊕ BM25_lemma`) lexical-only fusion, with overlap and unique relevant hits between the lexical variants, before adding D. This isolates within-lexical complementarity from lexical–dense complementarity.
- **Add citation to Chapter I?** Yes, briefly, in §1.3 (morphological normalization in Turkic IR): an example of the precision vs graded-relevance trade-off of Turkish stemming in web search, and an early raw + stem result mixing. Cite with the caveats (25 queries, no reported test).
- **Proposed `MASTER_INDEX.md` row** (to add after approval):

| MORPH-024 | Fidan — *Identifying the Effectiveness of a Web Search Engine with Turkish Domain Dependent Impacts and Global Scale Information Retrieval Improvements* (PhD thesis, METU, 2012), Ch. 4 — [deep dive](deep-dives/2012_Fidan_Turkish_Web_Search_Stemming_Mixed_Index.md) | 2012 | A (source) / weak evidence | MEDIUM | Turkish web search (583,771 pages, Lucene TF-IDF, not BM25): unstemmed vs stemmed index × unstemmed vs stemmed query, plus a 50/50 mixed raw+stem result list; 25 log queries (18 changed by stemming), top-10 graded by 10 users. Stem→stem P 0.86 / NDCG 0.48 vs raw→raw 0.75 / 0.53; mix 0.81 / 0.52; mismatched runs worst (Tables 4.6–4.8). K unspecified; "significant" without a named test; stemmer vs lemmatizer unclear; no dense, no lexical–dense fusion, no overlap/unique-hit/per-query analysis. |
