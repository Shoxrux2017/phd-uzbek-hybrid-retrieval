# Järvelin, Keskustalo, Sormunen, Saastamoinen & Kettunen (2016): Information retrieval from historical newspaper collections in highly inflectional languages: A query expansion approach

**Targeted deep-dive status:** COMPLETED (AI-assisted, pending researcher review)
**Completed:** 2026-09-28
**Literature ID:** `MORPH-030` (assigned 2026-09-28, approved by researcher)
**Systematic-review record:** `CR000342`. Full-text triage: INCLUDE, reading priority HIGH, reading tier "2 — важно", `carries_complementarity_evidence = YES`. In this card we qualify that flag: the evidence is a **per-topic improved/unaffected/damaged tabulation of one expansion run against the unexpanded baseline, broken down by query length and baseline difficulty** (Table 9). There is no relevant-set overlap, unique-hit or oracle-union evidence between methods (§10, §16).
**Provenance:** AI-assisted deep dive (Claude). The source is the **accepted author manuscript** (37 PDF pages; p. 1 carries a "How to cite" block: *JASIST*, doi 10.1002/asi.23379, "Published online June 1, 2015"). It was read in full from the pdftotext extraction. Page images (110 dpi) were checked for every table whose numbers are reported here: PDF pp. 14 (topics, pools, recall-base), 20 (Table 4), 21 (Table 5), 22 (Table 6), 23 (Table 7), 24–25 (Table 8, Table 9), 30–31 (Table 10). **PDF page N = the manuscript's printed page N**; the journal pagination (pp. 2928–2946) cannot be mapped from this file. Numbers computed by us are marked **[computed]** and were recomputed with Python (all 100 printed "Diff-% to baseline" values and all printed ranks in Tables 7–8 were recomputed; both chi-squared statistics were reproduced).
**Source rule:** **the paper is the primary and only authoritative source.** No code, website, later paper or background knowledge is used as evidence about what the authors did. Bibliographic check: EconPapers/RePEc record gives *Journal of the Association for Information Science & Technology* 67(12), 2016, pp. 2928–2946, DOI `10.1002/asi.23379`, author order Järvelin, Keskustalo, Sormunen, Saastamoinen, Kettunen (bibliographic check: EconPapers; a web search also returned the Wiley and ACM DL records labelled "Vol 67, No 12" and dblp key `JarvelinKSSK16`). Crossref and dblp pages could not be opened (proxy 403 / robots.txt), so the publisher page itself was not read. The typeset version may differ in wording from this manuscript; this was not checked.
**Verification:** independent AI verifier pass 2026-09-28; 11 findings addressed.
**Reliability:** **A** (peer-reviewed journal article, *JASIST*, Wiley). Version caveat: the text analysed is the accepted author manuscript, not the typeset version. Year: online 2015, issue 2016; we cite as 2016 following the triage metadata and the issue record.

---

## Кратко для исследователя (RU)

- **Что сделано.** Финский язык, коллекция оцифрованных (OCR) газет 1829–1890 гг.: 180 468 документов, 50 тем с градуированной оценкой релевантности (4 уровня). Поисковая система — Lemur Indri. Сравниваются только варианты **обработки запроса** над **ненормализованным индексом** (стемминг при индексации не применялся из-за OCR-шума, p. 13):
  - исходный запрос (базовый метод);
  - FCG — порождение 6/12/22 наиболее частотных падежных форм слов запроса (генеративный подход к морфологии);
  - расширение по s-граммам — 5…50 наиболее похожих по написанию слов из словаря индекса на каждое слово запроса;
  - комбинация FCG + s-граммы.
  Варианты одного слова объединяются оператором синонимии Indri (метод Пирколы).
- **Главные числа** (Table 7–8, pp. 23–24):
  - MAP: базовый метод 0,128; лучший FCG 0,188 (FCG22); лучший s-грамм 0,279 (SG_CCI2_50); лучшая комбинация 0,270;
  - P@10: 0,294 → лучший FCG 0,376 → SG_CCI1_30 0,506 → лучшая комбинация 0,508.
  - Все пересчитанные нами проценты прироста и ранги в таблицах совпадают с напечатанными.
- **Вывод авторов:** покрытие всех типов вариативности (исторической, OCR, словоизменительной, словосложения) важнее точности обработки одного типа (только словоизменения). Уровень расширения (≈30 вариантов на слово) важнее конкретной настройки s-грамм.
- **Разбор по запросам есть, но узкий** (Table 9–10, pp. 25, 30–31): только для одного прогона SG_CCI1_30 против исходного запроса, по P@10.
  - Улучшено 34 из 50 тем, без изменений 10, ухудшено 6.
  - Однословные запросы: 15 из 17 улучшены, ни один не ухудшен. Все 6 ухудшенных — запросы из 2+ слов с относительно хорошим исходным P@10 (≥ 0,2; у 5 из 6 — ≥ 0,5).
  - Связь «длина запроса → улучшено/не улучшено»: χ²(2) = 6,13, p = 0,047 (воспроизведено нами).
  - Тем без релевантных документов в топ-10: 10 → 4.
  - Авторы: «нет единственного признака темы или слова запроса», объясняющего эффект (p. 29).
- **Чего нет:**
  - BM25 нет (Indri; параметры модели и сглаживания не приведены);
  - стемминг/лемматизация в поисковых прогонах **не тестировались** (только оценка степени сжатия словаря стеммером Snowball);
  - плотного поиска, гибридного поиска и объединения ранжированных списков нет;
  - перекрытия результатов, уникально найденных релевантных документов, oracle union нет;
  - сравнения FCG и s-грамм по отдельным запросам нет.
- **Внутренние несоответствия:**
  - в тексте сказано, что s-граммы с 5 вариантами не отличаются значимо от базового метода, но в Table 7 у SG_CCI1_5 по MAP стоит звёздочка значимости (+52 % *);
  - утверждение «комбинации улучшили результаты по сравнению с чистыми s-граммами» верно при одинаковой настройке (CCI2, 20 вариантов), но не против лучшего s-граммового прогона: по MAP 0,279 > 0,270, по nDCG@10 (log10) 0,426 > 0,420.
- **Методические слабости:**
  - пул оценки для каждой темы построен **одним сложным запросом** (<500 документов), прогоны в пул не входили;
  - лучшие комбинации (2 из нескольких) отобраны и отчитаны по тем же 50 тестовым темам; из 9 уровней расширения показаны 4 («для ясности»), а вывод о ≈30 вариантах сделан на тех же темах (наш вывод, не утверждение авторов);
  - post-hoc процедура после теста Фридмана не описана;
  - число асессоров и согласованность не приведены.
- **Для нашего gap:** работа подтверждает, что эффект обработки словоформ в лексическом поиске зависит от длины запроса, исходной трудности запроса, сложных слов и частотности слов запроса. Это поддерживает включение этих признаков в таксономию запросов. Ядро v0.8 (raw/stem/lemma BM25 × фиксированная D → overlap/unique hits → прирост гибрида) **не затрагивает**. Предложение: gap не менять.
- **Практическая польза:**
  1. Табулирование «улучшено / без изменений / ухудшено» по признакам запроса — готовый формат для нашего позапросного анализа, но с заранее заданным порогом изменения и парными тестами.
  2. Отложить темы для настройки (авторы отложили 6 из 56) — хорошая практика; отбор конфигураций на тестовых темах — плохая.
  3. Пул нужно строить объединением прогонов всех каналов (raw/stem/lemma BM25, D, гибрид), а не одним запросом.
  4. Графическая вариативность (у них — историческое написание и OCR; у нас — апостроф в o‘/g‘, латиница/кириллица) — кандидат в отдельный признак запроса и в «простую нормализацию» как контроль.

---

## 1. Bibliographic record

- **Authors:** Anni Järvelin (corresponding author), Heikki Keskustalo, Eero Sormunen, Miamaria Saastamoinen, Kimmo Kettunen
- **Affiliations (p. 1):** School of Information Sciences, University of Tampere (Järvelin, Keskustalo, Sormunen, Saastamoinen); Centre for Preservation and Digitisation, National Library of Finland, Mikkeli (Kettunen)
- **Year:** 2016 (issue); published online 1 June 2015 (manuscript p. 1)
- **Venue:** *Journal of the Association for Information Science and Technology* (JASIST), 67(12), pp. 2928–2946 (bibliographic check: EconPapers/RePEc)
- **Publisher:** Wiley (ASIS&T)
- **DOI:** `10.1002/asi.23379`
- **Official record:** https://asistdl.onlinelibrary.wiley.com/doi/10.1002/asi.23379 (URL from web search; page not opened)
- **Source type:** peer-reviewed journal article
- **Reliability:** A
- **Full text available:** yes (`07_full_text/pdfs/CR000342.pdf`, accepted author manuscript, 37 pages)
- **Metadata note:** the title page lists Kettunen before Saastamoinen; the "How to cite" block on the same page and the EconPapers record give the order Järvelin, Keskustalo, Sormunen, Saastamoinen, Kettunen. We use the latter.

## 2. Why this work matters to the PhD

It is a rigorous Cranfield-style study of **how to handle word-form variation in the lexical channel** when index-side normalization (stemming/lemmatization) is not feasible. It adds a **topic-level analysis** of when variant handling helps or hurts. Both are directly relevant to our query-feature dimension.

| Axis | Relation |
|---|---|
| Lexical retrieval | Main focus. Indri over an unnormalized word-form index; four query-side representations (raw, FCG, s-gram, FCG + s-gram). **No BM25**; retrieval-model parameters NOT_REPORTED |
| Semantic retrieval | **Absent.** "Semantically related" words appear only as a by-product of string similarity (category 2 variants, §9) |
| Hybrid retrieval | **Absent.** The FCG + s-gram "combination" merges expansion terms inside one query; it is not a fusion of two ranked lists |
| Uzbek morphology | Indirect. Finnish is agglutinative and suffixing like Uzbek, and heavily compounding. Graphic variation here comes from historical spelling and OCR, not from script or apostrophe variants |
| Low-resource retrieval | Partial. A resource-lean setting (noisy historical text, no reliable analyzer for it), not a low-resource language |
| Current gap | Supports the query-feature dimension (query length, baseline difficulty, compounds, rare words). **No effect** on the lexical–dense complementarity core (§16) |

## 3. Research problem

### Simple explanation

Old Finnish newspapers were scanned and turned into text by OCR (optical character recognition). The text now contains three kinds of "wrong" word forms at once:

- old spellings (e.g. `waimo` for modern `vaimo`, "wife");
- OCR errors (e.g. `vaiino`);
- the many inflected forms of Finnish words (e.g. `vaimon`, "wife's").

A user types a modern word, and exact matching misses most occurrences. Stemming the index does not work well because the OCR noise breaks the stemmer. The authors ask whether it is better to add to the query:

- the **linguistically correct inflected forms** of the query word (precise but narrow); or
- the **most similar-looking words found in the index** (broad but noisy).

### Formal formulation

Three research questions (p. 12, verbatim):

- **RQ1** "What kind of variation does the s-gram matching capture? Does the captured variation reflect the variation actually occurring in the historical collection?"
- **RQ2** "Is query expansion using fuzzy query word variants useful in historical document retrieval?"
- **RQ3** "How do the properties of topics and query words affect the performance of the fuzzy query expansion in historical collections?"

Task: ad hoc document retrieval for topical, informational needs, with modern-language title queries over a historical, OCR-noisy collection.

## 4. Main idea

### Simple explanation

For each query word, the system builds a list of alternatives and searches for all of them as if they were one word. Three ways of building the list are compared:

1. **FCG (Frequent Case Generation):** generate the 6, 12 or 22 most common case forms of the modern word.
2. **s-gram matching:** find the N index words that look most similar to the query word, whatever the reason for the difference (inflection, old spelling, OCR error, compound part).
3. **Both:** find similar-looking index words for each generated case form.

### Concrete example

Query word `vaimo` ("wife"). The paper's own examples (Table 3, p. 18; Table 5, p. 21):

- inflectional variant: `vaimon`;
- historical spelling: `waimo`;
- OCR variant: `vaiino`;
- multiple variation: `waimoin` (historical inflection + `w`);
- related word: `aviovaimo` (synonym), `leskivaimo` (widow, compound);
- noise: `vaim` (OCR of "vain").

FCG would add only the correct modern case forms (`vaimon`, `vaimoa`, …). The s-gram expansion can add whatever the index contains that looks similar, e.g. the historical form `waimo`, which is in fact more frequent in the collection than `vaimo` (3,376 vs 2,054 occurrences; Table 5, p. 21). Table 3 gives these as illustrative "possible analyses", not as the actual top-20 list for `vaimo`; the authors also note that high-frequency historical variants are sometimes missed by s-gram matching when OCR errors make other strings more similar to the query word (p. 30).

### Formal method

- **s-grams** (pp. 8–9): character bigrams (n = 2) formed with skips of k characters. **Gram classes** group skip lengths, e.g. {0} = adjacent pairs, {1,2} = pairs skipping 1 or 2 characters. A **CCI** (Character Combination Index) is the set of gram classes used. Strings are compared class by class; similarity = the Dice coefficient over shared s-grams (p. 15).
- Tested CCIs (p. 15): CCI1 = {{0},{0,1},{1,2}}, CCI2 = {{0},{1},{1,2}}, CCI3 = {{0},{0,1},{1},{1,2}}. Only **left padding** is used, to give weight to word beginnings, since Finnish inflection changes word endings.
- **Query structure** (p. 17): all variants of one query word are wrapped in Indri's synonym operator, so they share one weight ("Pirkola's method"). This limits query drift from high-frequency variants.

## 5. Architecture / algorithm

1. **Index:** the collection is indexed **without stemming** (p. 13). The justification is a conflation test with the Snowball stemmer for Finnish (p. 13):
   - historical OCR collection: unique index words 7.03M → 4.87M, i.e. to 69.3% **[computed: 4.87/7.03 = 69.3% ✓]**;
   - OCR-free 19th-century literary Finnish (Kotus corpus): 52.2%;
   - modern Finnish news: 49.9% (citing Kettunen & Baskaya 2011).
   - The authors conclude that mainly OCR errors, not historical variation, reduce stemming performance. Stop-word handling of the index and any other index normalization are NOT_REPORTED.
2. **Queries:** the title fields of 50 topics, giving **100 unique search words** after stop-word removal (p. 14). Six further topics were used only for pre-testing s-gram settings and query structures (p. 14).
3. **Baseline:** query words as-is (p. 15).
4. **PRF control:** Indri pseudo-relevance feedback was tried with 2–20 feedback documents, 10–50 added terms and original-query weight 0.3–0.7. It is not reported because gains were "modest" and none were significant (p. 15).
5. **s-gram expansion** (pp. 15–16): 9 levels (2, 5, 10, 15, 20, 30, 40, 50, 60 variants per query word) × 3 CCIs. Only levels 5, 20, 30 and 50 are reported. Strings shorter than 3 characters and numerals are not expanded; the only such query string was "ii" (p. 15).
6. **FCG** (p. 16): case forms chosen from **modern** Finnish case statistics (Kettunen & Airio 2006), singular + plural:
   - FCG6: nominative, genitive, partitive (6 forms);
   - FCG12: + inessive, elative, illative (12 forms);
   - FCG22: + allative, adessive, ablative, essive, "transitive" [sic; presumably translative] (22 forms).
7. **FCG + s-gram** (pp. 16–17): 5–50 s-gram variants for each FCG6 or FCG12 case form, with CCI1 and CCI2. Duplicates are added once:
   - FCG6 + 30 CCI2 variants: on average 81 unique of 180 generated per word (min 38, max 163);
   - FCG6 + 50 variants: on average 129 of 300 (min 57, max 260);
   - "some queries however became very long": e.g. the query "ida aalbergin ura ulkomailla" received nearly 1,300 words with FCG12 + 50 variants (the paper gives it as an example, not as the longest query).
   - **Only the best two combinations** per FCG level (CCI2_20, CCI2_30) are reported; CCI1 results are omitted as "marginally weaker" (p. 17).
8. **Variant analysis (RQ1)** (pp. 17–18): for each of the 100 query words, the top-20 s-gram candidates were categorized manually by checking the top-10 documents per candidate in both the page images and the OCR text: **8,431 documents** examined.

## 6. Data

- **Collection** (p. 13): a subset of the National Library of Finland historical newspaper archive, Finnish newspapers 1829–1890: **180,468 documents** (84,512 newspaper pages, 772 MB). The documents are news articles, typically very short (p. 14).
- **OCR quality** (p. 13, citing Raitanen 2012): in a 2,105-word sample, roughly one fifth of the words differ from contemporary Finnish and another fifth are OCR errors; 127 different OCR errors, the most common being `w` → `m`.
- **Topics** (pp. 13–14): 56 topics on 19th-century history, written in contemporary language. 50 are used and 6 are held out for pre-testing. Topics are broad and informational and typically need several documents (example topic in Figure 1, p. 14).
- **Queries:** title fields; 100 unique words; 17 one-word, 20 two-word and 13 three-to-five-word queries (Table 9, p. 25) **[computed: if no word repeats across topics, 100 − 17 − 40 = 43 words in the 13 longer queries, i.e. 3.3 on average; the paper counts *unique* words, so this is approximate]**.
- **Relevance judgments** (p. 14):
  - pools of fewer than 500 documents per topic, built by **one complex query per topic** that "covered extensively various letter, word and term variants as well as all the facets of the topic at hand";
  - every pooled document was assessed intellectually on a 4-point scale (0 non-relevant, 1 marginal, 2 relevant, 3 highly relevant);
  - **recall base = levels 2 + 3**; level 1 treated as non-relevant;
  - on average 52 relevant documents per topic (36 at level 2, 16 at level 3); min 5 (topic 48), max 253 (topic 12);
  - number of assessors, agreement and adjudication: NOT_REPORTED. Whether the averages refer to all 56 or the 50 test topics: NOT_REPORTED;
  - new relevant documents were found for two topics during the study but were **not** used (p. 14).
- **Train/dev/test:** no training. 6 topics for pre-testing, 50 for evaluation; see §12 on configuration selection.

## 7. Baselines

| Baseline / run | What it is | Why selected | Fair comparison? |
|---|---|---|---|
| Baseline (unprocessed) | Modern title words as-is, unnormalized index | "no established baseline approaches" for this domain (p. 15) | Yes as a floor. It is not a strong lexical baseline: no normalization of any kind |
| PRF (Indri) | Pseudo-relevance feedback | Generic query expansion control | **Not reported** (n.s. vs baseline, p. 15). Readers cannot check it |
| FCG6/12/22 | Generative inflection (query side) | Established Tampere method for Finnish (pp. 9, 16) | **Partly.** Case forms from modern statistics; no historical/OCR handling, by design |
| SG_CCI{1,2,3}_{5,20,30,50} | s-gram expansion | Main method | Yes, all CCIs at four levels are reported (five other levels are not) |
| FCG{6,12}_CCI2_{20,30} | Combination | Precision + coverage | **Favoured by selection.** Best two of several configurations chosen on the test topics |
| Index stemming / lemmatization | — | Rejected a priori (OCR noise) | **Not run.** Only a vocabulary conflation rate is reported, not retrieval effectiveness |

## 8. Metrics

Two "scenarios" (pp. 18–19):

| Metric | Definition as given | Simple meaning | Appropriate? |
|---|---|---|---|
| nDCG@10, nDCG@50 with log base 10 (Scenario 1, "high recall") | Graded gains; discount with log₁₀ to model "patient users" | How good the top 10 / 50 are, with little penalty for lower positions | Yes, but see the gain values below |
| MAP (Scenario 1) | Binary (levels 2–3 relevant), trec_eval 9.0 | Average precision over all relevant documents, averaged over topics | Yes |
| nDCG@10 with log base 2 (Scenario 2, "high precision") | Strict discounting for "impatient users" | Top-10 quality with a strong position penalty | Yes |
| P@10 (Scenario 2) | Binary, trec_eval 9.0; described in the text as "average precision at rank 10" | Share of relevant documents among the first 10 | Yes |

- **nDCG gains** (p. 19): level 0 and 1 → 0, level 2 → 10, level 3 → 100, computed with the Tampere tool Vectora. This makes highly relevant documents count 10× more than relevant ones, which is a strong weighting choice.
- Context (not from the paper): in the original DCG definition (Järvelin & Kekäläinen 2002), the log-b discount is applied only from rank b onwards. If Vectora follows it, nDCG@10 with log₁₀ is effectively undiscounted within the top 10. The paper does not state this.
- No recall metric is reported for "Scenario 1"; MAP and nDCG@50 play that role. Footnote 7 (p. 32), attached to the discussion of translation precision, states that "Reporting e.g. recall values would not have been possible in our study due to the extent of variation in the collection".
- **Variant-level metric (RQ1):** "translation precision" = share of the top-20 s-gram candidates in categories 1 or 2 (p. 18).

## 9. Results

### Table 4: s-gram variant categories, top-20 candidates for 100 words (p. 20)

| Category | Count | % |
|---|---:|---:|
| 1 VARIANT (total) | 1,239 | 62% |
| 1a exact match | 82 | 4.1% |
| 1b spelling variant | 77 | 3.9% |
| 1c inflectional variant | 372 | 18.6% |
| 1d OCR variant | 191 | 9.6% |
| 1e multiple, surface only | 517 | 25.9% |
| 2 RELATED (total) | 328 | 16% |
| 2a synonym / 2b cross-lingual / 2c derivative / 2d related meaning | 5 / 8 / 50 / 28 | 0.3 / 0.4 / 2.5 / 1.4% |
| 2e multiple, related | 237 | 11.9% |
| 3 NOISE (3a noise 425; 3b unclear 8) | 433 | 22% |

- "Translation precision" = 78% (62% + 16%) (p. 20). Subtotals and the grand total of 2,000 = 100 × 20 add up **[computed ✓]**.
- In the multiple-variation categories 1e + 2e, 316 of 754 variants (42%) contained historical variation, 216 of them also OCR errors (p. 21) **[computed: 517 + 237 = 754 ✓; 316/754 = 41.9% ✓]**.
- Minor unreconciled detail: the text says 36 historical + 39 spelling-error variants (p. 21) = 75, while category 1b has 77. The 2 remaining are plausibly abbreviations (1b-ii), but the paper does not say so.
- **Table 5 (p. 21):** the historical or OCR form can be more frequent than the modern form, e.g. `kansanvalistusseuran` 155 vs historical 329 vs OCR `kansanmalistusseuran` 634; `vaimo` 2,054 vs `waimo` 3,376.

### Table 6: query-word length × variant category (p. 22)

| Word length | 1a | 1b–1e | 2 | 3 (noise) |
|---|---:|---:|---:|---:|
| Short, 2–6 chars (27 words, n = 540) | 4.4% | 36.9% | 11.3% | **47.4%** |
| Medium, 7–11 chars (44 words, n = 880) | 4.8% | **72.3%** | 8.5% | 14.4% |
| Long, 12–20 chars (29 words, n = 580) | 2.8% | 55.5% | **33.1%** | 8.6% |
| Total (n = 2,000) | 4.1% | 57.9% | 16.4% | 21.7% |

- Pearson χ²(6) = 449.7, p = 0.000 (p. 22). **[computed: counts reconstructed from the percentages sum exactly to the category totals 82 / 1,157 / 328 / 433; χ² = 449.7 ✓]**
- Short words mostly produce noise; long words (often compounds) produce related words and compound parts.

### Table 7: Scenario 1, "high recall" (p. 23; 20 runs)

| Run | nDCG@10 (log10) | nDCG@50 (log10) | MAP |
|---|---:|---:|---:|
| Baseline | 0.221 | 0.248 | 0.128 |
| FCG6 | 0.279 (+26%) | 0.290 (+17%) | 0.171 (+34%) |
| FCG12 | 0.286 (+29%) | 0.301 (+21%) | 0.180 (+41%*) |
| FCG22 | 0.281 (+27%) | 0.300 (+21%) | 0.188 (+47%*) |
| SG_CCI1_5 | 0.309 (+40%) | 0.333 (+34%) | 0.195 (**+52%\***) |
| SG_CCI2_5 / CCI3_5 | 0.303 / 0.302 | 0.317 / 0.316 | 0.183 / 0.184 |
| SG_CCI1_20 / CCI2_20 / CCI3_20 | 0.371* / 0.398* / 0.385* | 0.393* / 0.401* / 0.394* | 0.246* / 0.253* / 0.251* |
| SG_CCI1_30 | **0.426\*** (rank 1) | 0.430* | 0.276* |
| SG_CCI2_30 / CCI3_30 | 0.417* / 0.418* | 0.421* / 0.429* | 0.267* / 0.275* |
| SG_CCI1_50 / CCI3_50 | 0.411* / 0.411* | 0.436* / 0.436* | 0.277* / 0.275* |
| SG_CCI2_50 | 0.422* | 0.440* | **0.279\*** (rank 1, +118%) |
| FCG6_CCI2_20 / FCG6_CCI2_30 | 0.420* / 0.420* | 0.430* / 0.438* | 0.269* / 0.270* |
| FCG12_CCI2_20 / FCG12_CCI2_30 | 0.414* / 0.414* | 0.435* / **0.443\*** (rank 1) | 0.268* / 0.269* |

\* = difference to the baseline statistically significant (caption). All printed Diff-% values and ranks were recomputed **[computed ✓, no mismatch]**.

### Table 8: Scenario 2, "high precision" (pp. 24–25)

| Run | nDCG@10 (log2) | P@10 |
|---|---:|---:|
| Baseline | 0.243 | 0.294 |
| FCG6 / FCG12 / FCG22 | 0.305 / 0.317 / 0.308 | 0.336 / 0.358 / 0.376 |
| SG_*_5 (CCI1 / 2 / 3) | 0.331 / 0.328 / 0.325 | 0.436 / 0.418 / 0.426 |
| SG_*_20 | 0.395* / 0.418* / 0.406* | 0.488* / 0.498* / 0.494* |
| SG_*_30 | 0.438* / 0.437* / 0.440* | **0.506\*** / 0.498* / 0.504* |
| SG_*_50 | 0.435* / 0.442* / 0.432* | 0.484* / 0.490* / 0.486* |
| FCG6_CCI2_20 | **0.451\*** (rank 1) | **0.508\*** (rank 1) |
| FCG6_CCI2_30 / FCG12_CCI2_20 / FCG12_CCI2_30 | 0.445* / 0.449* / 0.442* | 0.498* / 0.504* / 0.496* |

**Reading Tables 7–8** (all differences **[computed]** from the printed values):

- **Raw → FCG (inflection only):** +0.043 to +0.060 MAP, +0.042 to +0.082 P@10. Significant vs baseline only for MAP of FCG12 and FCG22. FCG6 vs FCG12 vs FCG22 are not significantly different (p. 23).
- **FCG → s-gram:** SG_CCI1_30 is 49.0% / 42.9% / 46.8% above the best FCG run on nDCG@10 / nDCG@50 / MAP (Table 7), and 38.2% / 34.6% on nDCG@10 (log2) / P@10 (Table 8). Absolute: MAP 0.276 vs 0.188 (+0.088); P@10 0.506 vs 0.376 (+0.130). **No direct significance test of s-gram vs FCG is reported**; the claim "clearly more effective" (p. 24) rests on the baseline-referenced asterisks and the size of the gap.
- **Expansion level:** gains rise up to about 30 variants and then level off. P@10 is lower at 50 than at 30 for all three CCIs (e.g. CCI1 0.506 → 0.484).
- **Combination vs plain s-gram:**
  - at matched settings (CCI2, same level), the combinations are mostly higher: FCG6_CCI2_20 vs SG_CCI2_20 = +0.022 / +0.029 / +0.016 (Table 7), +0.033 / +0.010 (Table 8). FCG12_CCI2_30 vs SG_CCI2_30 is slightly lower on nDCG@10 (log10) (−0.003) and P@10 (−0.002);
  - against the **best** plain s-gram run the combinations are not higher in Scenario 1: MAP 0.270 vs 0.279, nDCG@10 0.420 vs 0.426; only nDCG@50 0.443 vs 0.440;
  - in Scenario 2 the best combination is top on both measures (0.451 / 0.508 vs 0.442 / 0.506);
  - none of these differences is significant (p. 24).

### Table 9: topic-level analysis, SG_CCI1_30 vs baseline, by query length and baseline P@10 (p. 25)

| Query length | Baseline P@10 ≤ 0.1 (+ / = / −) | 0.2–0.4 | ≥ 0.5 | Total (+ / = / −) |
|---|---|---|---|---|
| 1 word (n = 17) | 6 / 1 / 0 | 7 / 1 / 0 | 2 / 0 / 0 | **15 / 2 / 0** |
| 2 words (n = 20) | 8 / 3 / 0 | 3 / 0 / 1 | 2 / 2 / 1 | 13 / 5 / 2 |
| 3–5 words (n = 13) | 1 / 2 / 0 | 5 / 0 / 0 | 0 / 1 / 4 | 6 / 3 / **4** |
| Total (N = 50) | 15 / 6 / 0 (N = 21) | 15 / 1 / 1 (N = 17) | 4 / 3 / 5 (N = 12) | **34 / 10 / 6** |

(+ improved, = unaffected, − damaged). All row and column sums check **[computed ✓]**.

- Improved vs not improved × query length: Pearson χ², p = 0.047 (p. 25). **[computed: χ²(2) = 6.13, p = 0.0466 ✓]**. With the three outcome categories kept separate, χ²(4) = 8.77, p = 0.067 **[computed]**; the authors' merging of "unaffected" and "damaged" is what brings p under 0.05.
- The criterion for "improved/unaffected/damaged" is not defined beyond "based on the P@10 results" (p. 19). It is presumably any change in P@10; no threshold is stated.
- Qualitative analysis (pp. 26–27):
  - one-word queries were long (11 of 17 were compounds; compound query words averaged 12.7 characters vs 9.7 overall) and rare: of the 17 words, 5 had zero collection frequency, 11 were low-frequency (fewer than 100 occurrences) and 1 had medium frequency (232 occurrences). s-grams helped by adding compound parts (`Imatra`, `diakonissa`);
  - in two-word and longer queries, expanding the constituents of fixed phrases is described as "problematic" (e.g. "Suezin kanava", "Työmiehen vaimo"; the paper does not say which of these topics were damaged). Damage is attributed to vocabulary/concept mismatch and query drift (topic 52 "Maanalaiset rautatiet", whose performance decreased: `maalaiset`, "peasants", entered via `maanalaiset`);
  - vocabulary change (topic 44, weather forecasting: `ilman`, `ennustus` used historically) is a mismatch that string-level variant expansion does not address.

### Table 10: distribution of topics by P@10, baseline vs SG_CCI1_30 (pp. 30–31)

| P@10 level | Baseline | s-gram |
|---|---:|---:|
| P@10 = 0 | 10 (20%) | 4 (8%) |
| P@10 = 0.1 | 11 (22%) | 4 (8%) |
| 0.2–0.4 | 17 (34%) | 15 (30%) |
| ≥ 0.5 | 12 (24%) | 27 (54%) |

- "At most one relevant document in the top 10": 42% → 16%; "at least five": 24% → 54% (p. 30) **[computed ✓]**.

## 10. Statistical evidence

- **Significance tests:** "the Friedman's test and Pearson's chi-squared test" (p. 19). Asterisks in Tables 7–8 mark differences to the baseline. The post-hoc / multiple-comparison procedure after Friedman, the α level and the raw p-values for the runs are **NOT_REPORTED** (p = 0.047 is treated as significant, so α = 0.05 is implied).
- **Internal inconsistency:** the text (p. 24) states "The performance difference between the low expansion level s-grams and the baseline were not statistically significant", but Table 7 (p. 23, checked on the page image) marks SG_CCI1_5 MAP "+52 % \*". The rest of the text agrees with the tables: FCG significant only for MAP of FCG12/FCG22; all s-grams at 20–50 significant in both scenarios.
- **Confidence intervals:** NOT_REPORTED.
- **Runs / seeds:** deterministic runs; no variance applicable. The effect of topic sampling is not quantified.
- **Ablation / sensitivity:** yes, informally. 3 CCIs × 9 expansion levels (4 reported); FCG at 3 levels; combinations over 7 levels × 2 CCIs × 2 FCG levels (2 reported per FCG level). The PRF grid was run but not reported.
- **Per-query analysis:** **yes, partial.** Table 9 (one expanded run vs baseline, by query length × baseline P@10 bin) with χ²; Table 10; qualitative case analyses. **NOT_REPORTED:**
  - per-topic comparison of FCG vs s-gram, or of combination vs s-gram;
  - relevant documents retrieved only by one method (unique hits), overlap, or oracle union of methods;
  - per-topic scores (no per-topic table or plot is given).
- **Variant-level statistics:** Pearson χ²(6) = 449.7 for word length × variant category (Table 6).

## 11. Strengths

- A real historical collection with **graded, intellectually assessed** relevance for 56 topics, a recall base averaging 52 documents per topic, and a clear graded-to-binary protocol.
- Explicit separation of **precision-oriented** vs **coverage-oriented** variant handling, with inflection-only (FCG) as a controlled contrast to all-variation (s-gram).
- A careful **qualitative variant analysis** (8,431 documents checked against page images) that explains *what* the expansion adds.
- **Topic-level analysis** tied to query features (length, compounds, collection frequency, baseline difficulty), with a significance test and honest reporting of damaged topics.
- Pre-testing topics held out from the evaluation set (6 of 56).
- The authors state explicitly that results may not transfer to known-item search (p. 31).
- All reported percentage gains and ranks are arithmetically consistent with the scores.

## 12. Limitations

### Stated by the authors

- OCR noise makes index-side conflation "infeasible"; stemming was not used (p. 13).
- FCG case forms come from **modern** Finnish statistics; the 19th-century case distribution may differ (p. 16).
- s-gram expansion is noisy (22% noise in the top 20), and short words produce mostly noise (pp. 20–22).
- Left padding favours inflectional variants over historical and OCR variants; the s-gram set-up determines which variants are found (pp. 21, 30).
- Long, multi-word queries are damaged by drift; Pirkola's query structure did not solve the ambiguity (p. 28).
- Vocabulary and concept change are not handled by string methods (the study "focused on string level variation", p. 4; string matching "cannot handle vocabulary change", citing Braun et al. 2002, p. 11; topic examples pp. 26–27).
- New relevant documents found for two topics were not used (p. 14).
- The results are for informational search; applicability to known-item search is uncertain (p. 31).
- Combination queries can become very long: nearly 1,300 words for one query with FCG12 + 50 variants (p. 17; stated as a fact, not discussed as a limitation).

### Inferred from the experimental design

1. **Pool bias of unknown direction.** Each topic's pool was built by **one** complex, variant-rich query (<500 documents), and the evaluated runs were not pooled. Documents found only by an expansion run are counted as non-relevant. This can under- or over-state the expansion methods; MAP and nDCG@50 are the most exposed.
2. **Configuration selection on the test topics.** Four of nine expansion levels are shown "for clarity", and only the best two combinations per FCG level are reported (CCI1 combinations omitted as "marginally weaker", p. 17). This slightly favours the combination runs in any comparison with the plain s-gram runs.
3. **No reductive baseline in retrieval.** Stemming was excluded on the basis of a vocabulary conflation rate (69.3%), not a retrieval run. We therefore do not know how an index-stemmed (or n-gram-indexed) run compares with FCG or s-gram expansion here.
4. **Retrieval model under-specified.** Only "Lemur Indri" and its synonym operator are named; the ranking model settings (e.g. smoothing) are NOT_REPORTED.
5. **Multiple-comparison control unclear.** 19 runs are compared with the baseline across 5 measures; the Friedman post-hoc procedure is not described.
6. **Per-topic criterion undefined.** "Improved/unaffected/damaged" is based on P@10 without a stated threshold. The p = 0.047 result depends on merging "unaffected" and "damaged" (three-category p = 0.067 **[computed]**). Only one run (SG_CCI1_30) is analysed per topic.
7. **Unusual nDCG gains** (0 / 10 / 100) and log₁₀ discounting make the nDCG values hard to compare with other studies.
8. **Short title queries only** (about 2 words on average **[computed: 100 unique words / 50 topics; approximate, since repeated words across topics are not counted]**); the query-length effect is estimated from 17 / 20 / 13 topics.
9. Assessor numbers and agreement are not reported.

## 13. What the work proves

- In this Finnish historical OCR collection, with an unnormalized index and short title queries, **all tested query-side variant-handling methods beat the raw query** on all five measures (Tables 7–8). The s-gram runs with 20–50 variants are significant vs the baseline in both scenarios.
- **Coverage-oriented fuzzy expansion is much stronger than inflection-only generation here:** best FCG MAP 0.188 vs s-gram 0.276–0.279; P@10 0.376 vs 0.506 (Tables 7–8). The size of the gap makes the direction robust, although no direct s-gram vs FCG test is reported.
- **Expansion depth matters more than the CCI choice:** about 30 variants per word is needed; gains level off after that (Tables 7–8; no significant differences among CCIs).
- **Adding FCG to s-grams gives at most small, non-significant gains** over s-grams alone (p. 24; §9).
- **The benefit of variant handling depends on query properties:** one-word (long, compound, rare) queries are almost always improved (15/17, none damaged), while all 6 damaged topics have 2+ words and a relatively good baseline (baseline P@10 ≥ 0.2; 5 of the 6 at ≥ 0.5). Four of them are three-to-five-word queries (4 of 13), all with baseline P@10 ≥ 0.5. The length × improved association is significant at p = 0.047 in the authors' merged-category test (Table 9).
- **Word length strongly shapes what string similarity returns:** short words give noise, long words give related words and compound parts (Table 6, χ² = 449.7).
- In this collection, historical and OCR forms can be **more frequent than the modern form** (Table 5), so raw modern queries miss a large share of occurrences.

## 14. What the work does NOT prove

- **Anything about BM25.** The engine is Indri; no BM25 run exists.
- **Anything about index-side stemming or lemmatization effectiveness.** Neither was run as a retrieval condition; the Snowball result is a vocabulary conflation rate only. The study cannot rank raw vs stem vs lemma.
- **That "variant recall beats precision" in clean modern text.** The evidence comes from OCR-noisy 19th-century text where most variation is non-inflectional. In clean text FCG targets the main source of variation, and the gap may be much smaller.
- **Anything about dense retrieval, hybrid retrieval or lexical–semantic complementarity.** None was tested. The FCG + s-gram combination is a query-term union, not a fusion of rankings.
- **Which documents each method uniquely retrieves.** No overlap, unique-hit or oracle-union analysis exists, so it is unknown whether FCG finds relevant documents that s-grams miss.
- **That query length causes the damage.** Length is confounded with baseline performance (the damaged long queries were those with P@10 ≥ 0.5) and with compoundness and word frequency. The authors themselves say no single feature explains the effect (p. 29).
- **That the per-topic pattern holds for the other runs** (FCG or combinations); only SG_CCI1_30 was analysed.
- **Generalization** to known-item search, to longer queries, or to other languages; the authors' claim about other compounding languages (p. 29) is a hypothesis, not a result.

## 15. Relationship to current Uzbek evidence

- **No Uzbek data.** Finnish (Uralic) is agglutinative and suffixing like Uzbek (Turkic). The paper's point that inflection changes mainly word endings (motivating left padding, p. 15) applies to Uzbek in principle. Finnish closed compounding is much more prominent than in Uzbek (context, not from the paper), so the strong compound effects here may not transfer.
- **Graphic variation analogue.** The historical `w`/`v` spelling and OCR confusions play a role similar to Uzbek graphic variation: Latin/Cyrillic script, and the apostrophe forms in `o‘`/`g‘` (see the exemplar card §17). The finding that the "wrong" form can be the most frequent one (Table 5) is a warning that, in Uzbek web or legal text, a non-standard apostrophe form may dominate. This needs checking on our corpus (context, not from the paper).
- **Relation to existing cards:**
  - Kettunen, Kunttu & Järvelin 2005 (`CR000452`): in clean modern Finnish news, lemmatization ≈ inflectional stem generation > Snowball > plain word forms. Read together, this paper shows that in noisy text the generative inflection approach (FCG) is far weaker than coverage-oriented fuzzy matching. The **best lexical representation depends on the text condition**.
  - Can et al. 2008 (MORPH-001): query length changes the observed stemming effect in Turkish. This paper gives a parallel query-length interaction for query-side variant handling in Finnish.
  - Airio 2006 (`CR000491`): Finnish normalization and decompounding.
- Nothing here touches the national Uzbek evidence boundary (Bakaev, Xusainova, Elov etc.).

## 16. Relationship to CURRENT_GAP

**Classification:** *supports* (query-feature dimension) + *no material effect* on the residual core.

- **Supports:** v0.8 lists candidate query characteristics: morphological variability, affixal forms, rare terms, query length, graphic (Latin/Cyrillic, Unicode/apostrophe) variation, lexical overlap. This paper provides peer-reviewed lexical-only evidence that the **effect of changing the lexical word-form representation is heterogeneous across queries** and associated with:
  - query length;
  - baseline difficulty;
  - compound and low-frequency query words;
  - graphic (historical/OCR) variation.
  It also shows that **no single feature** explains the effect (p. 29). That supports treating query features as candidates, not predetermined causes, as v0.8 already does.
- **Already occupied (consistent with existing "non-claims"):** "query-type analysis of lexical retrieval effects" and "morphology handling in lexical IR for an agglutinative language" are not new. This paper adds a further example.
- **No material effect on the residual core.** The core chain is: raw/stem/lemma BM25 → change in lexical relevant set → overlap/unique hits versus the **same fixed dense D** → incremental hybrid gain → relation to Uzbek query features. The paper has:
  - no BM25;
  - no stem/lemma retrieval condition (it compares raw vs query-side inflection generation vs fuzzy expansion);
  - no dense model, no fusion;
  - no relevant-set overlap or unique-hit analysis, even between its own lexical variants.
- **Mechanism hint (hypothesis only):** coverage-oriented variant handling raised P@10 from 0.294 to 0.506 and cut the number of topics with no relevant document in the top 10 (P@10 = 0) from 10 to 4. A broader lexical representation may therefore change *which* relevant documents the lexical channel finds, and not only how many. That is exactly what our overlap/unique-hit measurements would test against D. The paper itself provides no such evidence.

**Proposal:** keep v0.8 refined unchanged. Optionally cite this paper in the evidence boundary as Finnish evidence that the effect of lexical word-form handling varies per query with length, compounding, frequency and graphic variation. This is a proposal only; `CURRENT_GAP.md` has not been edited.

## 17. Implications for our research design

- **Lexical variants (secondary controls, researcher's decision):**
  - The primary design stays `BM25_raw / stem / lemma` over the index.
  - This paper suggests two optional secondary conditions:
    1. a **query-side generative** variant (Uzbek analogue of FCG: generate frequent case/possessive forms of query nouns over a raw index);
    2. a **character n-gram / fuzzy** variant robust to graphic noise.
  - They should be reported separately and must not replace the primary matrix.
  - The `BM25_simple-normalization` control already in v0.8 should include apostrophe and script normalization, since graphic variation was a major source of misses here.
- **Do not reject a condition on vocabulary statistics alone.** The authors dropped stemming because of the conflation rate, not a retrieval result. For Uzbek, every morphology condition in the matrix should be run, not pre-screened.
- **Qrels / pooling:**
  - build pools from the **union of runs**: every lexical variant, D and the hybrids, at sufficient depth;
  - do not rely on one expert "complex query" per topic;
  - report assessor numbers and agreement;
  - add documents found later in a versioned qrels release rather than silently.
- **Query taxonomy:** add or keep:
  - query length in words;
  - presence of compounds / multi-word names or fixed phrases (Uzbek: multi-word terms, proper-name phrases);
  - collection frequency of query terms (zero / low / medium);
  - baseline difficulty (per-query effectiveness of `BM25_raw`, used only as a *descriptive* stratum, since it is outcome-dependent);
  - graphic variants of query words in the corpus.
  The paper's damage cases (fixed phrases expanded constituent-wise; drift in multi-word queries) suggest a hypothesis for Uzbek lemmatization: lemmatizing parts of fixed names may hurt.
- **Per-query protocol:**
  - adopt the improved/unaffected/damaged tabulation, but define the change threshold in advance (e.g. |ΔnDCG@10| ≥ 0.05, or any change in the unique-hit count);
  - keep all three categories in the tests;
  - use paired per-query tests (Wilcoxon / randomization) plus a Friedman test with a named post-hoc procedure (e.g. Holm) for multi-run comparisons;
  - analyse **every** condition per query, not only the best run.
- **Configuration selection:** hold out dev topics (as the authors did with 6 of 56) and select expansion levels, fusion α and candidate depth only there. Report all pre-registered configurations on the test set, not the best two.
- **Metrics:** report standard nDCG@10 (log₂, gains 1/2 or 1/3 for graded levels) plus MAP and Recall@100. If a user-model variant is used, state the discount base and gains explicitly.
- **Hypothesis link:** "coverage over precision" suggests that stem (more aggressive) vs lemma (more precise) may differ more in *unique lexical hits* than in averages, especially on noisy or variant-rich Uzbek text. This is a testable hypothesis, not evidence.

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| OCR (optical character recognition) | Software that turns a scanned page image into text; old pages give many misread letters | Image-to-text conversion; errors = character substitutions, insertions, deletions |
| Historical document retrieval (HDR) | Searching old texts with modern query words | Retrieval across diachronic language variants, treated as a CLIR-like problem (p. 3) |
| Query expansion | Adding extra words to the user's query to catch more relevant documents | Reformulating q into q′ ⊃ q |
| Reductive vs generative morphology handling | Reductive: shrink all word forms to one index form (stemming, lemmatization). Generative: keep the index as-is and add the word forms to the query | Index-side conflation vs query-side form generation (p. 9) |
| FCG (Frequent Case Generation) | Add only the most common case forms of each query noun | Generative, corpus-statistics-based inflection of query terms (Kettunen & Airio 2006) |
| n-gram / s-gram | Cut a word into 2-letter pieces; s-grams also allow skipping letters between the two | Character bigrams with skip length k; gram classes combine skips |
| CCI (Character Combination Index) | The recipe of which skip lengths are used | Set of s-gram classes, e.g. {{0},{1,2}} |
| Padding | Extra marker characters at word edges so beginnings count more | (n−1)(k+1) pad characters; here left only |
| Dice coefficient | Similarity = shared pieces relative to total pieces | 2\|A∩B\| / (\|A\|+\|B\|) over s-gram sets |
| Translation precision | Share of suggested variants that really are variants or related words | Categories 1 + 2 among the top 20 |
| Synonym operator / Pirkola's method | Treat all variants of one query word as one word for weighting | Indri `#syn`-type structured query |
| PRF (pseudo-relevance feedback) | Assume the top results are relevant and take new query words from them | Automatic feedback-based expansion |
| Recall base | All documents judged relevant for a topic | Here graded levels 2–3 |
| nDCG with log base b | Graded top-k quality; a larger b means a milder penalty for lower ranks | Järvelin & Kekäläinen 2002 DCG, normalized by ideal DCG |
| Friedman test | Non-parametric test whether several systems differ across the same topics | Rank-based repeated-measures test |
| Query drift | Expansion pulls the query toward a different topic | Topic shift caused by expansion terms |
| Complementarity (project term) | Each channel finds some relevant documents the other misses | Unique relevant hits, overlap, oracle-union gain |

## 19. Open questions / verification needed

1. **SG_CCI1_5 MAP significance:** Table 7 marks it significant; the text says low-level s-grams were not significant. Only the authors or the typeset version can resolve this. Check the published version.
2. **Post-hoc procedure after Friedman,** α level and raw p-values: NOT_REPORTED.
3. **Indri ranking settings** (model, smoothing, stop-word handling in the index): NOT_REPORTED.
4. **"Improved/unaffected/damaged" threshold** in Table 9: NOT_REPORTED.
5. **Recall-base averages (52 / 36 / 16):** computed over 56 or 50 topics? NOT_REPORTED.
6. **Category 1b breakdown:** 36 historical + 39 spelling errors = 75 vs 77 in Table 4 (2 presumably abbreviations; not stated).
7. **Minor manuscript issues:** Holley is cited as 2008 in the text (p. 3) but 2009 in the references; FCG22 lists a "transitive" case (presumably translative). Check the typeset version.
8. **Typeset version:** confirm that the tables and the significance marks are unchanged in JASIST 67(12).
9. Related record flagged at triage: **CR000519** (Kettunen overview). Check it for any Finnish per-query overlap evidence between reductive and generative variants.

## 20. Decision after deep dive

- **Keep current gap?** Yes. v0.8 refined remains valid (§16).
- **Modify gap?** No change proposed. Optionally add the paper to the evidence boundary as lexical-only, per-query evidence on query-feature heterogeneity (researcher's decision).
- **Add decision?** Proposed for `decisions/DECISIONS.md` (researcher's decision):
  - "Qrels pools are built from the union of all evaluated runs (all lexical variants, D, hybrids), not from a single expert query";
  - "per-query outcome categories (improved/unaffected/damaged) use a pre-registered change threshold and are tested without merging categories";
  - "no morphology condition is excluded on vocabulary-conflation statistics alone".
- **Add experiment?** Optional secondary conditions: a query-side generative inflection variant and a character n-gram lexical variant over the raw index, reported separately from the primary raw/stem/lemma matrix. Also include "graphic variant count of query terms in the corpus" as a query feature in the pilot.
- **Add citation to Chapter I?** Yes:
  - §1.1: reductive vs generative handling of morphological variation; coverage vs precision of variant handling in noisy text; query-length/compound/frequency interaction;
  - optionally §1.3, as background for query-feature-based analysis (lexical only).
- **Proposed `MASTER_INDEX.md` row** (to add after approval):

| MORPH-030 | Järvelin, Keskustalo, Sormunen, Saastamoinen, Kettunen — *Information retrieval from historical newspaper collections in highly inflectional languages: A query expansion approach* (*JASIST* 67(12), 2928–2946) — [deep dive](deep-dives/2016_Jarvelin_Keskustalo_Finnish_Historical_Newspaper_Query_Expansion.md) | 2016 | A | HIGH | Finnish OCR historical newspapers (180,468 docs; 50 title queries; graded qrels from single-query pools), Indri over an unstemmed index: raw query vs FCG inflection generation vs s-gram fuzzy expansion vs FCG+s-gram. MAP 0.128 → FCG ≤0.188 → s-gram ≤0.279 (combination 0.270); P@10 0.294 → 0.376 → 0.506 (0.508). Topic-level: 34/50 improved, 6 damaged (all multi-word, relatively good baseline P@10 ≥ 0.2); query length × improved χ² p = 0.047. No BM25, no stem/lemma retrieval run, no dense, no fusion, no overlap/unique-hit analysis. Text vs Table 7 significance inconsistency (SG_CCI1_5 MAP). |
