# Kettunen, Kunttu & Järvelin (2005): To stem or lemmatize a highly inflectional language in a probabilistic IR environment?

**Targeted deep-dive status:** COMPLETED (AI-assisted, pending researcher review)
**Completed:** 2026-09-28
**Literature ID:** `MORPH-029` (assigned 2026-09-28, approved by researcher)
**Systematic-review record:** `CR000452`. Full-text triage: INCLUDE, reading priority HIGH, reading tier "2 — важно", `carries_complementarity_evidence = YES`. In this card we qualify that flag as *per-topic effectiveness differences between two lexical representations only* (§10, §16); there is no relevant-set overlap evidence.
**Provenance:** AI-assisted deep dive (Claude). The source is the **self-archived author manuscript** from TamPub (University of Tampere repository): 42 PDF pages = a repository cover page + manuscript pages 1–41. It was read in full from the pdftotext extraction. Page images were checked for every table and figure whose numbers are reported here: PDF pp. 1 (cover/bibliographic block), 7–8 (Table I), 13 (Figure 1), 18–19 (Table V), 20–23 (Table VI, Figures 2–5; Figures 4–5 additionally at 220 dpi crops), 25–28 (Tables VII–X), 29–30 (run-time text, Figure 6), 35–37 (Table XI, Discussion, Conclusion). **Page references below are the manuscript's own printed page numbers ("ms p. N" = PDF page N+1).** The journal pagination (pp. 476–496) cannot be mapped from this file. Numbers computed by us are marked **[computed]** (recomputed with Python); values read from bar charts are marked **[approximate, read from bars]**.
**Source rule:** **the paper is the primary and only authoritative source.** No code, website, later paper or background knowledge is used as evidence about what the authors did. Bibliographic check: a web search returned the Emerald record URL `emerald.com/jd/article-abstract/61/4/476/...` and DOI `10.1108/00220410510607480`, consistent with the cover page (bibliographic check: Emerald search result). Direct DOI resolution and Crossref lookup were refused by the proxy (HTTP 429 / 403), so issue date and final pagination were not opened on the publisher page. Verifier pass: a second web search returned the Emerald records `emerald.com/jd/article/61/4/476/200065/...` and `emerald.com/insight/content/doi/10.1108/00220410510607480/...`, again consistent with the cover page; the Emerald page itself (CAPTCHA) and Crossref (HTTP 403) were still not accessible. The published version may differ in wording from this manuscript (e.g., Emerald structured abstract); this was not checked.
**Reliability:** **A** (peer-reviewed journal article, *Journal of Documentation*, Emerald, 2005). Version caveat: the text analysed is the accepted/author manuscript, not the typeset version.
**Verification:** independent AI verifier pass 2026-09-28; 10 findings addressed.

---

## Кратко для исследователя (RU)

- **Что сделано.** Классическое сравнение способов учёта морфологии финского языка (агглютинативный, флективно богатый) в вероятностной поисковой системе INQUERY 3.1 на коллекции TUTK (53 893 газетные статьи, 30 длинных тем, градуированные оценки релевантности 0–3):
  - «простые слова» (plain words: словоформы без обработки, индекс словоформ);
  - стемминг Snowball (стеммированный индекс);
  - лемматизация FINTWOL (лемматизированный индекс);
  - **генерация основ словоизменения** (inflectional stem generation: MaxStemma / Finstems): индекс словоформ не меняется, а к запросу добавляются все словоформы индекса, начинающиеся с порождённых основ (имитация усечения через grep).
- **Главные числа, Environment One** (Table VI, ms p. 19; средняя точность по 10 уровням полноты, %):
  - строгий порог (только уровень 3): FINTWOL 24.1, MaxStemma 22.6, Snowball 20.0, plain 12.4;
  - обычный порог (уровни 2–3): 35.0 / 34.2 / 27.7 / 18.9.
  - Plain = 51.45% и 54% от FINTWOL (ms pp. 20–21; **[computed]** 51.45 и 54.0 ✓). Любая морфологическая обработка даёт +46.6…+94.4% относительно plain **[computed]**.
- **Лемматизация ≈ генерация основ:** разница ≤1.5 п.п., по тесту Фридмана незначима ни на одном пороге (Table VIII, ms p. 26). Snowball значимо хуже лемматизации (оба порога) и генерации основ (только обычный порог).
- **Environment Two** (Table VII, ms pp. 23–24): разбиение композитов в лемматизированном индексе даёт лучший результат (LEMS2: 23.4 / 33.7 / 35.1 на строгом / обычном / либеральном пороге); добавление производных слов в запрос даёт ≤0.8 п.п.
- **Есть разбор по отдельным темам (Figs. 4–5, ms pp. 21–22), но только FINTWOL vs MaxStemma и только по средней точности:**
  - при почти равных средних отдельные темы расходятся до ≈24 п.п. (T4: ≈46.5 vs ≈22.5 на строгом пороге) **[approximate, read from bars]**;
  - по нашим считываниям столбцов FINTWOL выше на 17 темах, MaxStemma на 10, ≈3 равны (строгий порог) **[computed, approximate]**; эти счёты зависят от допуска «ничьей» и сдвигаются на 1–3 темы при повторном считывании; устойчивы только списки разниц ≥5 пунктов (11 тем на строгом пороге);
  - объяснение авторов только одно: разная обработка дефиса в композитах (T2, T28, T29); для остальных тем «no obvious reason».
  - Группы тем по содержанию (тематические, географические, персоналии, организации; Env. Two) — значимые различия только в географической и организационной группах (Table X, ms p. 27).
- **Чего нет (измерения gap):**
  - BM25 нет: используется INQUERY (#sum/#syn), параметры не сообщаются;
  - плотного/нейросетевого поиска нет;
  - fusion/гибрида нет;
  - перекрытия найденных релевантных документов, уникальных находок, oracle union нет;
  - признаки запросов — только тематические группы и длина запроса (для времени выполнения).
- **Внутренние несоответствия в статье:**
  - в выводах plain = «48–58%» от лемматизатора (ms p. 36), в результатах 51.45% и 54%;
  - «выигрыш 9.2 п.п.» генерации основ над plain (ms p. 35) не воспроизводится: по Table VI 10.2 и 15.3 п.п. (среднее 12.75) **[computed]**;
  - в Table IX «LEMNS1 > INFL2» (значимо) и «LEMNS1 > LEMNS2» на либеральном пороге, хотя в Table VII LEMNS1 = 31.3 < INFL2 = 32.1 и < LEMNS2 = 31.9;
  - одна и та же конфигурация (FINTWOL, композиты не разбиты, базовый запрос) даёт 24.1 / 35.0 в Env. One и 21.6 / 30.3 в Env. Two — расхождение не объяснено;
  - Snowball назван «реализацией стеммера Портера» (аннотация) и «стеммером в стиле Ловинс» (ms p. 9);
  - средняя длина темы без стоп-слов 15.06 (текст) vs 15.04 (Table I).
- **Для нашего gap:** работа поддерживает фон: raw → stem → lemma в агглютинативном языке, при этом равные средние скрывают сильные расхождения по отдельным запросам. Ядро v0.8 (raw/stem/lemma BM25 × фиксированный D → overlap / unique hits → прирост гибрида) **не затрагивает**. Предложение: gap не менять.
- **Практическая польза для нас:**
  1. обязательно держать базовый вариант «raw/plain» и сообщать результаты при двух порогах градуированной релевантности: разрыв Snowball – лемматизация «заметен» только на обычном пороге;
  2. правила токенизации (дефис, для узбекского также апостроф o‘/g‘) фиксировать одинаково для всех вариантов: у авторов часть расхождений по темам объясняется именно дефисом;
  3. «расширение запроса вариантами над неизменным индексом словоформ» (аналог генерации основ) — возможный дополнительный контроль, отличный от замены индекса на стемы/леммы;
  4. тип запроса по сущностям (персоналии / география / организации) — кандидат в признаки запроса.

---

## 1. Bibliographic record

- **Authors:** Kimmo Kettunen, Tuomas Kunttu, Kalervo Järvelin
- **Affiliation:** Department of Information Studies, University of Tampere, Finland (all three; ms p. 1)
- **Year:** 2005
- **Venue:** *Journal of Documentation*, Vol. 61, No. 4, pp. 476–496 (cover page of the repository PDF; consistent with the Emerald URL path `jd/.../61/4/476` — bibliographic check: Emerald search result)
- **ISSN:** 0022-0418 (cover page)
- **Publisher:** Emerald (bibliographic check: Emerald search result)
- **DOI:** `10.1108/00220410510607480` (cover page)
- **Official URL:** https://doi.org/10.1108/00220410510607480 (not opened: proxy refusal)
- **Repository copy:** TamPub, URN `urn:nbn:uta-3-744` (cover page)
- **Keywords (ms p. 1):** morphological processing, probabilistic IR, comparison of methods
- **Source type:** peer-reviewed journal article; analysed as the self-archived manuscript
- **Reliability:** A
- **Full text available:** yes (`07_full_text/pdfs/CR000452.pdf`, 42 PDF pages)
- **Related thesis cited for Environment Two:** Kunttu, T. (2003), M.Sc. thesis (pro gradu), Dept. of Information Studies, University of Tampere (in Finnish; ms p. 40). Environment Two results are summarised from it.

## 2. Why this work matters to the PhD

It is a peer-reviewed, controlled comparison of **several morphological representations of the lexical channel** in a highly inflectional, agglutinative language, on one collection, one engine and one topic set, with graded relevance, a nonparametric significance test and a per-topic plot. It also introduces a representation type that our design has not yet named: **query-side expansion over an unnormalized index** (inflectional stem generation), as opposed to normalizing the index (stemming/lemmatization).

| Axis | Relation |
|---|---|
| Lexical retrieval | **Central.** Plain word forms vs Snowball stemming vs FINTWOL lemmatization vs inflectional stem generation (MaxStemma, Finstems); compound splitting and derivational query expansion in Environment Two |
| Semantic retrieval | **Absent** |
| Hybrid retrieval | **Absent.** INQUERY's `#syn` groups variants of one query word; it is not fusion of retrieval runs |
| Uzbek morphology | Indirect but close in type: Finnish is agglutinative and suffixing, like Uzbek (different families: Uralic vs Turkic) |
| Low-resource retrieval | No. Finnish had commercial two-level morphology tools and a laboratory test collection |
| Current gap | Touches the `raw → stem → lemma` element and gives per-topic and topic-group variation; does not touch a dense D, fusion, overlap/unique hits or hybrid gain (§16) |

## 3. Research problem

### Simple explanation

In Finnish one noun can in principle have about 2,200 inflected forms (ms p. 3). If the query contains one form and the document another, exact word matching fails. There are several ways to fix this: cut word endings (stemming), map every form to its dictionary form (lemmatization), or, keeping the text as is, add to the query all word forms that begin with any of the word's possible stems (stem generation). The authors ask which of these works best in a ranking (best-match) search engine, and whether an off-the-shelf stemmer is good enough for Finnish.

### Formal formulation

Research problems (ms pp. 4–5, verbatim):

- "How do lemmatization and inflectional stem generation compare in a probabilistic environment?"
- "Is a stemmer a realistic alternative for handling of the morphology of a highly inflectional language, such as Finnish, for IR?"
- "Is simulation of truncation feasible in a best-match system?"
- Sub-problems: "compound splitting, derivational queries, and different types of topics" (ms p. 5).

Task: ad hoc document retrieval over newspaper articles with long natural-language topics; effectiveness measured by average precision over recall levels at several graded-relevance thresholds.

## 4. Main idea

### Simple explanation

Keep everything fixed (collection, topics, search engine, stop-word list) and change only how the morphology of query words, and of the index, is handled. Then compare average precision and test the differences statistically.

### Concrete example (the paper's own, ms pp. 9–10, 13)

- Word *kissa* 'cat'.
- **Lemmatization (FINTWOL):** all inflected forms of *kissa* → one base form *kissa*.
- **Stemming (Snowball):** *kissat, kissojen, kissoihin* → *kis-* and *kiso-*; "singular and plural forms are not conflated to a single stem in this case" (ms p. 10).
- **Stem generation (MaxStemma / Finstems):** from the base form, generate the inflectional stems *kissa, kissoi, kissoj*; grep the word-form index with `grep("kissa"|"kissoi"|"kissoj")`; put every matching index entry into the query as synonyms (ms p. 13).
- **Plain words:** the topic word as written, against the unprocessed word-form index.

The real topic 1 (Bush–Gorbachev summit in Helsinki, Sept. 1990) becomes, after stem generation and grepping, a query with "more than 3500 lines of matching words" (ms p. 16), including false drops such as *bushehrissa* or *georgetown* (ms p. 16).

### Formal method

Queries are INQUERY structured queries of the form (ms p. 15):

`#q1 = #sum( #syn(v_11 v_12 …) #syn(v_21 …) … )`

where each `#syn(...)` holds the variants of one query word: one lemma (lemmatization), one stem (stemming), one word form (plain), or all index word forms matched by the generated stems (stem generation).

Context (not from the paper): in INQUERY, `#syn` treats its arguments as occurrences of one term, and `#sum` averages the beliefs of its arguments. The paper itself describes INQUERY only as "a probabilistic partial match system" (ms p. 5). It gives no term-weighting formula or parameters.

## 5. Architecture / algorithm

**Environment One** (Figure 1, ms p. 12; steps ms p. 13):

1. Lemmatize the topic words with FINTWOL. This "simulates interactive query, where the user gives the words in their base forms" (ms p. 14). Ambiguous analyses are kept, e.g. `#syn(käsitellä käsitellä käsitellä)` (ms p. 15).
2. Build a basic INQUERY query with `#sum` and `#syn`.
3. Remove stop words with a Finnish stop list.
4. Generate inflectional stems with MaxStemma. Compound borders are marked; for compounds with more than two parts only the last border stays marked (ms p. 14).
5. Grep the word-form index with the stems. This "simulates term truncation, which is not supported in INQUERY" (ms p. 13). No filtering: "Misspellings and all other false drops are taken into the final query; no matches from the index are checked in any way during or after this phase in Environment One" (ms p. 17).
6. Run INQUERY retrieval and evaluate.

Which steps each condition uses (ms p. 13) and its index (Table IV, ms p. 14):

| Condition | Steps | Index |
|---|---|---|
| Plain words | 2, 3, 6 | inflected (unprocessed) |
| Stemmed (Snowball) | 1 = stemming of query words, then 2, 3, 6 | stemmed with Snowball |
| Stem generation (MaxStemma) | 1–6 | inflected (unprocessed) |
| Lemmatized (FINTWOL) | 1, 2, 3, 6 | lemmatized with FINTWOL, compounds **not** split |

**Environment Two** (Kunttu 2003; ms p. 17; Table V, ms pp. 17–18):

- FINTWOL lemmatization vs **Finstems** stem generation.
- The grep output was filtered: "the results of the grepping were sifted intellectually or with FINTWOL so that the final query included only the real inflected forms of the query noun" (ms p. 17).
- Two index variants for lemmatization: compounds split (LEMS) vs not split (LEMNS).
- Two query types: basic (…1) and derivational (…2), the latter adding "the most productive derivatives of the query nouns", which "more than doubled the number of the query words" (ms p. 17).
- Six runs: LEMS1, LEMS2, LEMNS1, LEMNS2, INFL1, INFL2. INFL = inflected index (Table V). From the text, the INFL runs are the Finstems stem-generation runs (ms pp. 24–25 compare "FINTWOL with compounds-as-whole (LEMNS1 and LEMNS2)" with "Finstems" using the INFL numbers).

**Tools** (ms pp. 9–11, notes 1–2 on ms p. 37):

- FINTWOL: two-level morphology lemmatizer (Koskenniemi 1983; Lingsoft), rule-based with "a large lexicon with tens of thousands of entries" (ms p. 10).
- Finstems: stem generator (Koskenniemi 1985; Lingsoft).
- MaxStemma: stem generator implemented by the first author "in early 1990's" (ms p. 9).
- Snowball Finnish stemmer: suffix-stripping "according to a suffix list and set of rules" (ms pp. 9–10); footnote 2 says it is "based on linguistic description of Finnish" (ms p. 37). Table III (ms p. 11) does not list Snowball itself; it places Porter- and Lovins-type stemmers in the "no dictionary used" cell, and the text classes Snowball as that type.

**Not reported:** INQUERY term-weighting details and parameters, stop-list size/source, any document-length normalization, how graded levels are used in averaging beyond the thresholds.

## 6. Data

- **Collection:** TUTK (Sormunen 2000; Kekäläinen 1999), Finnish newspaper articles 1988–1992 from Aamulehti, Keskisuomalainen and Kauppalehti (ms p. 5).
- **Size** (Table I, ms pp. 6–7):
  - 53,893 documents;
  - 709,317 inflected word-form types;
  - 11,752,290 word-form tokens;
  - mean 218.06 words per document (11,752,290 / 53,893 = 218.067 **[computed]**; the table truncates rather than rounds);
  - mean length of word-form types 13.14 characters; frequency-weighted token length 8.03.
- **Domain:** mostly economics (~16,000 Kauppalehti articles), foreign and international affairs (~25,000 Aamulehti), all sections of Keskisuomalainen (~13,000) (ms p. 5).
- **Topics:** 30 (Sormunen 2000). They are long: mean 17.4 words; without stop words 15.06 (text, ms pp. 5–6) or 15.04 (Table I, ms p. 6). This is a small internal inconsistency.
- **Relevance judgments:** four-point scale from Sormunen (2000, p. 63) (Table II, ms pp. 7–8):
  - 0 totally off target;
  - 1 marginally relevant;
  - 2 relevant, contains some new facts;
  - 3 highly relevant, main focus on the topic.
- **Thresholds used** (ms p. 8):
  - **stringent** = level 3 only;
  - **normal** = levels 2–3 (Environment One's binary level);
  - **liberal** = levels 1–3 (Environment Two only).
- **NOT_REPORTED in this paper:** pooling method, assessors and agreement, number of relevant documents per topic or level. They are delegated to Sormunen (2000).
- **Train/dev/test:** not applicable (no learned components). Nothing was tuned on the topics, as far as the paper reports.

## 7. Baselines

| Baseline / condition | What it is | Why selected | Fair comparison? |
|---|---|---|---|
| Plain words | Topic words as written, unprocessed index | "To get an independent baseline for all the tests" (ms p. 18) | Yes as a floor. The authors explain plain words' relatively good score by the few case forms that actually occur in text and by the "conjunctional effect of a set of query words" (ms pp. 32–33); that the long TUTK topics amplify this is our inference |
| Snowball stemming | Algorithmic suffix stripping, stemmed index | Question 2: is a stemmer realistic for Finnish? | **Partly.** One stemmer, called "far from optimal" by the authors (abstract, ms p. 1) |
| FINTWOL lemmatization | Dictionary lemmatizer, lemmatized index | Reference method, used before in Boolean IR (Alkula 2000, 2001) | Yes |
| MaxStemma / Finstems stem generation | Query expansion over the word-form index | Main interest of the study | **Asymmetric.** The query side first uses FINTWOL lemmatization (step 1), so the condition is not lexicon-free on the query side. In Environment Two the matched forms were filtered "intellectually or with FINTWOL" (ms p. 17), i.e. partly by hand. Environment One MaxStemma queries reach 934–24,443 query words (ms p. 28), so the conditions also differ strongly in query size |

## 8. Metrics

| Metric | Definition | Simple meaning | Appropriate? |
|---|---|---|---|
| Average precision over recall levels (%) | Precision averaged over 10 recall levels (10%, 20%, …, 100%); "ten point average P-R curves" (ms p. 18; axes of Figs. 2–3) | "How precise is the ranking, averaged across the whole range from finding a few to finding all relevant documents" | Yes for 2005 ad hoc evaluation. Interpolation rule not stated |
| Per-topic "Average precision" (Figs. 4–5) | Not defined separately | Same quantity for one topic | Our bar readings average to 24.18 / 35.02 vs the table's 24.1 / 35.0 **[computed, approximate]**, consistent with the table being the mean of per-topic values |
| Graded-relevance thresholds | Stringent / normal / liberal (§6) | "How strictly do we count a document as relevant?" | Useful: effects change with the threshold (§9) |
| Practical significance (Sparck Jones 1974) | Difference < 5 pp "not noticeable", 5–10 pp "noticeable", > 10 pp "material" (ms p. 30) | Rule of thumb for how big a difference matters | A convention, not a statistic |
| CPU time | Mean of three runs, system + user time (Fig. 6, ms p. 28) | Cost of simulated truncation | Laboratory measure only |

## 9. Results

### Table VI — Environment One (ms p. 19)

Average precision over recall levels (%); in parentheses the authors' absolute differences from FINTWOL in percentage points (pp).

| Threshold | FINTWOL (lemma) | MaxStemma (stem generation) | Snowball (stem) | Plain |
|---|---:|---:|---:|---:|
| Stringent | 24.1 | 22.6 (−1.5) | 20.0 (−4.1) | 12.4 (−11.7) |
| Normal | 35.0 | 34.2 (−0.8) | 27.7 (−7.3) | 18.9 (−16.1) |

All differences in parentheses re-derived **[computed ✓]**. Derived values **[computed]**:

- Relative gain over plain:
  - FINTWOL +94.4% (stringent) / +85.2% (normal);
  - MaxStemma +82.3% / +81.0%;
  - Snowball +61.3% / +46.6%.
- Plain as a share of FINTWOL: 51.45% / 54.0%. This matches the authors' "51.45 %" (ms p. 20) and "54 %" (ms p. 21).
- Snowball as a share of FINTWOL: 83.0% / 79.1%.
- MaxStemma − Snowball: 2.6 pp / 6.5 pp; the authors report 6.5 pp for normal (ms p. 30).

### Figures 2–3 — ten-point P-R curves (ms pp. 19–20)

Authors' reading (ms pp. 20–21), consistent with the page images:

- **Stringent:**
  - FINTWOL and MaxStemma "almost converge from recall level 10 to 40";
  - Snowball is "clearly below"; "only at the recall level 30 it performs almost at the same level" (image: still slightly below, ≈32 vs ≈33–34.5);
  - plain is "ca. 60 − 66 %" of FINTWOL up to recall 30, then "ca. 29 – 44 %".
- **Normal:**
  - MaxStemma "starts better than FINTWOL" at low recall (image: ≈66 vs ≈65.5 at recall 10);
  - FINTWOL is "a few per cent better" from recall 30 to 70;
  - plain is "ca. 45 − 79 %" of FINTWOL until recall 70.

### Figures 4–5 — per-topic average precision, FINTWOL vs MaxStemma only (ms pp. 21–22)

Authors' statements (ms p. 22):

- **Stringent:** FINTWOL clearly better on T4, T7, T15, T19, T28, T29; MaxStemma clearly better on T5, T8, T14, T18, T21.
- **Normal:** FINTWOL clearly better on T2, T4, T7, T19, T29; MaxStemma on T5, T15, T18, T21.
- Explanation: different handling of the compound hyphen "seems to be the most obvious reason" and "at least" affects T2, T28, T29. "Otherwise no obvious reason for differences was found in Environment One, when results per query were compared" (ms pp. 22–23).

Our readings of the bars (220-dpi crops) **[approximate, read from bars; counts computed]**:

| | Stringent | Normal |
|---|---|---|
| Mean of readings (FINTWOL / MaxStemma) | 24.18 / 22.68 (table: 24.1 / 22.6) | 35.02 / 34.22 (table: 35.0 / 34.2) |
| Topics with FINTWOL higher / MaxStemma higher / ≈ tie | 17 / 10 / 3 | 15 / 12 / 3 (counts depend on the tie tolerance; an independent re-reading gave 17 / 9 / 4 and 13 / 10 / 7 at ±0.5, 16 / 12 / 2 at ±0.25 for normal) |
| Differences ≥ 5 AP points | FINTWOL: T4, T7, T15, T19, T28, T29; MaxStemma: T5, T8, T14, T18, T21 (reproduces the authors' lists exactly) | FINTWOL: T4, T7, T19, T29; MaxStemma: T5, T15, T18, T21 (authors also list T2, which we read as ≈6 vs ≈2.5) |
| Topics within ±5 points | 19 of 30 | 22 of 30 |
| Largest differences | T4 ≈ +24 for FINTWOL (≈46.5 vs ≈22.5); T18 ≈ −11 | T4 ≈ +22.5; T21 ≈ −14.5 (≈18.5 vs ≈33) |

Observation (implied by the authors' own lists, ms p. 22, which put T15 among FINTWOL's clear wins at stringent and MaxStemma's clear wins at normal; magnitudes are our readings): **T15 changes direction between thresholds.** FINTWOL is ≈14 points better at stringent (≈34.5 vs ≈20.5), while MaxStemma is ≈5.5 points better at normal (≈48.5 vs ≈54). So the per-topic winner can depend on the relevance threshold as well as on the topic.

### Table VII — Environment Two (ms pp. 23–24)

Average precision (%); in parentheses the authors' differences from LEMS1 in pp.

| Threshold | LEMS1 | LEMS2 | LEMNS1 | LEMNS2 | INFL1 | INFL2 |
|---|---:|---:|---:|---:|---:|---:|
| Stringent | 22.8 | 23.4 (0.6) | 21.6 (−1.2) | 22.0 (−0.8) | 20.6 (−2.2) | 21.1 (−1.7) |
| Normal | 33.0 | 33.7 (0.7) | 30.3 (−2.7) | 30.6 (−2.4) | 29.7 (−3.3) | 29.6 (−3.4) |
| Liberal | 34.3 | 35.1 (0.8) | 31.3 (−3.0) | 31.9 (−2.4) | 32.1 (−2.2) | 32.1 (−2.2) |

All differences re-derived **[computed ✓]**. The authors' summary statements (ms pp. 24–25) were rechecked **[computed ✓]**:

- LEMS vs INFL: 1.7–4.1 pp in favour of LEMS.
- FINTWOL compounds-as-whole vs Finstems:
  - liberal: at most 0.8 pp in favour of Finstems;
  - normal: at most 1.0 pp in favour of FINTWOL;
  - stringent: at most 1.4 pp in favour of FINTWOL.
- Derivational gain: FINTWOL 0.3–0.8 pp; Finstems at most 0.5 pp, "mostly … no difference". INFL2 − INFL1 is +0.5 (stringent), −0.1 (normal) and 0.0 (liberal).
- Compound splitting (LEMS1 − LEMNS1) **[computed]**: +1.2 / +2.7 / +3.0 pp, i.e. +5.6% / +8.9% / +9.6% relative.
- Topic groups (normal threshold only; ms p. 25): the best group result was person-oriented queries, LEMNS1 = 45.2%. Group sizes and other group values are **NOT_REPORTED**.

### Significance — Tables VIII–X (ms pp. 26–27)

Friedman test. Table VIII shows differences significant at 0.01, with bold marking 0.001.

**Environment One (Table VIII):**

| Comparison | Significant at |
|---|---|
| FINTWOL > MaxStemma | none on any level |
| FINTWOL > Snowball | stringent (0.01), **normal (0.001)** |
| FINTWOL > Plain | **stringent, normal (0.001)** |
| MaxStemma > Snowball | **normal (0.001)** only |
| MaxStemma > Plain | **stringent, normal (0.001)** |
| Snowball > Plain | stringent (0.01), **normal (0.001)** |

**Environment Two (Table IX):** "almost significant" p ≤ 0.05, "significant" p ≤ 0.01, "very significant" p ≤ 0.001.

- LEMS2 > INFL1 is significant on all three thresholds.
- LEMS1 > LEMNS1 and LEMS2 > LEMNS1 are very significant on the liberal threshold.
- Stem generation vs lemmatization without compound splitting: only LEMNS2 > INFL1 (normal, significant) and LEMNS1 > INFL2 (liberal, significant; see the direction inconsistency below).

**Environment Two by topic group (Table X, normal):**

- Significant differences appear only for geographically oriented and organizational queries.
- Geographic: LEMS2 > LEMNS1 and LEMS2 > INFL1 very significant.
- Organizational: LEMS1 > LEMNS2 and LEMS1 > INFL2 significant.
- Discussion (ms p. 31): only geographic queries had "noticeable" (≥ 5 pp) differences, LEMS2 vs INFL1 and INFL2. The values are not given.

### Run time of simulated truncation (ms pp. 28–29; Figure 6)

- Final Environment One queries have 934–24,443 query words.
- Mean CPU time is 10–96 s for topics of 6–28 source words; effective response time 20.6 s to 4.15 min (Sun Sparc, two processors, 4 GB).
- Figure 6: lowest ≈10 s (T21, 6 words), highest ≈96 s (T20, 18 words). Time is not monotone in topic length (T11, 28 words, ≈42 s).
- Short 3–5-word topic versions "decreased strongly" run times. No numbers are given.

### Table XI — qualitative benefit scoring (ms pp. 33–34)

- Scores: lemmatization 6 (6), stem generation 5 (5), stemming 3 (4), plain 2 (3).
- Weights: retrieval 3 / ease of use 2 / storage 1; in parentheses ease 3 / retrieval 2 / storage 1.
- The sums are re-derived **[computed ✓]**. Stemming's "improved retrieval" cell is "No?" despite its significant gain over plain.

### Internal inconsistencies (reported with both locations; not resolved)

1. **Plain as a share of lemma:** "48 to 58 %" (Conclusion, ms p. 36) vs "51.45 %" (ms p. 20) and "54 %" (ms p. 21). No other plain-words run exists; Environment Two has none.
2. **"9.2 % units" gain of stem generation over plain words** (Discussion, ms p. 35) cannot be reproduced from Table VI: MaxStemma − Plain = 10.2 pp (stringent) and 15.3 pp (normal), mean 12.75 **[computed]**. No other reported pair gives 9.2; the closest is Snowball − Plain, mean 8.2 **[computed]**.
3. **Direction of significant differences, Table IX (ms p. 26) vs Table VII (ms p. 24), liberal threshold:**
   - "LEMNS1 > INFL2 — significant", yet 31.3 < 32.1;
   - "LEMNS1 > LEMNS2 — almost significant", yet 31.3 < 31.9.
   A rank-based Friedman procedure can in principle order systems differently from mean AP. The paper does not say so.
4. **Environment One vs Two for the same nominal configuration:**
   - FINTWOL, compounds not split, basic query: 24.1 / 35.0 (Table VI) vs LEMNS1 21.6 / 30.3 (Table VII);
   - stem generation: 22.6 / 34.2 (MaxStemma) vs 20.6 / 29.7 (Finstems, INFL1).
   The paper says only that the environments are "partly different" (ms p. 5).
5. **Snowball description:** "a Porter stemmer implementation" (abstract, ms p. 1) vs "a Lovins' style stemmer" (ms p. 9).
6. **Mean topic length without stop words:** 15.06 (ms p. 6 text) vs 15.04 (Table I).
7. **Conclusion overstatement:** "the difference between the stemmer and lemmatization or stem generation was mostly statistically and practically significant" (ms pp. 35–36).
   - Statistically: 3 of 4 comparisons (Table VIII).
   - Practically noticeable (≥ 5 pp): 2 of 4, normal threshold only (4.1 and 2.6 pp at stringent) **[computed]**.
8. **Minor:**
   - "LEM2NS" (Table V, ms p. 18) vs "LEMNS2" (Tables VII, IX, X);
   - run times given as "CPU seconds of system time" (ms p. 28) vs Figure 6 "system time + user time … added together".

## 10. Statistical evidence

- **Significance test:** Friedman test ("original Friedman test, cf. Siegel and Castellan, 1988, modifications used in here in Conover, 1980", ms p. 25). All methods were "evaluated against each other".
  - The pairwise post-hoc procedure is not described. Presumably it is Conover's multiple-comparison procedure, but this is not stated.
  - No correction for multiple comparisons is stated.
  - Exact p-values: **NOT_REPORTED**; only thresholds.
- **Confidence intervals:** NOT_REPORTED.
- **Runs / seeds:** not applicable; deterministic runs. CPU timing uses the mean of three runs.
- **Ablation:** partial. Environment Two varies compound splitting (LEMS vs LEMNS) and derivational expansion (…1 vs …2) factorially for lemmatization; for Finstems it varies derivational expansion only.
- **Power / equivalence:** "not significant" for FINTWOL vs MaxStemma rests on 30 topics. It is not an equivalence test (inferred).
- **Per-query analysis:** **present but limited.**
  - Figures 4–5 plot per-topic AP for FINTWOL vs MaxStemma only; Snowball and plain have no per-topic data.
  - The explanation is qualitative: compound hyphen handling for T2, T28, T29.
  - Topic-group significance appears only in Environment Two (Table X).
  - Not present:
    - per-topic win/loss counts in the paper (ours are approximate readings);
    - overlap of relevant documents between representations;
    - unique relevant hits or oracle union;
    - query-feature regression.

## 11. Strengths

- Controlled design: one collection, one engine, one topic set, one stop list; only the morphological handling changes.
- Four genuinely different representation strategies, including the rarely tested **query-side stem generation over an unnormalized index**.
- Graded relevance evaluated at two or three thresholds, showing that conclusions about Snowball depend on the threshold.
- Nonparametric significance testing plus an explicit practical-significance convention.
- Per-topic plot and a topic-theme breakdown: early evidence that aggregate parity hides per-topic divergence.
- Honest reporting of cost (query size, CPU time) and of false drops in the grep simulation.

## 12. Limitations

### Stated by the authors

- The Snowball stemmer "is far from optimal for a morphologically complex language like Finnish" (abstract, ms p. 1); "a more sophisticated stemmer for Finnish would also perform better" (ms p. 32).
- The grep simulation of truncation is slower than native truncation. TUTK topics are long, so queries become very long; many concurrent queries "may be resource consuming" (ms pp. 28–29, 35).
- False drops (misspellings, unrelated strings) enter Environment One stem-generation queries unchecked (ms p. 17).
- Lemmatization needs a large lexicon that must be updated, fails on unknown words such as proper names, and takes longer to implement (ms p. 34).
- Cross-collection comparison with CLEF results is not possible: "the findings are not comparable across test collections" (ms p. 31).

### Inferred from the experimental design

1. **Only 30 long topics** (17.4 words). Morphological effects in agglutinative languages have been reported to interact with query length (Can et al. 2008, MORPH-001, card in `ctx/`). The ranking of methods may differ for short queries, and the authors themselves explain plain words' surprisingly good score partly by the "conjunctional effect of a set of query words" (ms p. 33).
2. **Stem generation is confounded with query size and with a manual step.** Queries grow to thousands of `#syn` members. In Environment Two the matched forms were filtered "intellectually or with FINTWOL", so the condition is not a fully automatic representation. It also depends on FINTWOL lemmatization of the query (step 1).
3. **Index and query representations change together** for stemming and lemmatization, but only the query changes for stem generation. The comparison therefore mixes "normalize the index" with "expand the query".
4. **One retrieval model (INQUERY), no parameters reported, no BM25.** The effects may not transfer to BM25 term weighting, especially the treatment of large `#syn` groups.
5. **Qrels details delegated** to Sormunen (2000): pooling depth and assessor procedure are unknown from this paper, so Recall-oriented conclusions cannot be assessed here.
6. **Per-topic evidence is partial:** two conditions only, graphical only, and the explanation is found for 3 topics.
7. **Unreconciled numbers** (§9: items 1–4) weaken the precision of the Discussion and Conclusion. The core tables themselves are internally consistent.
8. **Thematic topic groups** have unreported sizes (30 topics over 4 groups means small groups), so Table X significance is fragile.

## 13. What the work proves

Within Finnish newspaper retrieval with 30 long topics in INQUERY:

- **Morphological processing substantially improves over unprocessed word forms.**
  - FINTWOL and MaxStemma beat plain by 10.2–16.1 pp (+81…+94% relative), significant at 0.001 (Tables VI, VIII).
  - Snowball beats plain by 7.6–8.8 pp (+47…+61%), significant at 0.01 / 0.001.
- **Plain words still retain about half of the lemmatizer's effectiveness**: 51.45% / 54.0% (Table VI **[computed ✓]**).
- **Lemmatization and inflectional stem generation are statistically indistinguishable in Environment One** on aggregate: ≤1.5 pp, not significant at any threshold (Tables VI, VIII). In Environment Two this holds only partly: lemmatization without compound splitting vs Finstems differs by ≤1.4 pp, but LEMNS2 > INFL1 (normal) and LEMNS1 > INFL2 (liberal) are significant, and lemmatization with compound splitting (LEMS2) is significantly better than INFL1 on all thresholds (Table IX). The abstract itself says "not statistically significant in most of the tested settings".
- **The off-the-shelf Snowball stemmer is below both:**
  - significantly and noticeably at the normal threshold (−7.3 / −6.5 pp);
  - at the stringent threshold the gap vs FINTWOL is 4.1 pp (significant at 0.01, not "noticeable"), and vs MaxStemma 2.6 pp (not significant).
- **Compound splitting helps lemmatization** (+1.2 to +3.0 pp; LEMS1 > LEMNS1 very significant on the liberal threshold only, not significant at normal or stringent; LEMS2 > LEMNS1 very significant at liberal and almost significant at normal); derivational expansion adds ≤0.8 pp (Tables VII, IX).
- **Aggregate parity hides per-topic divergence:** FINTWOL and MaxStemma differ by ≥5 AP points on 11 of 30 topics (stringent), by up to ≈24 points **[approximate, read from bars]**. The direction varies by topic and, for T15, by relevance threshold.

## 14. What the work does NOT prove

- **Anything about BM25.** The engine is INQUERY; no BM25 or other named weighting scheme is reported.
- **Anything about dense/semantic retrieval or lexical–semantic hybrids.** Neither exists in the study.
- **That different representations retrieve different relevant documents.** Per-topic AP differences are compatible with the same relevant documents at different ranks. No overlap, unique-hit or union analysis exists. The triage flag "complementarity evidence = YES" should be read in this narrow sense.
- **That lemmatization and stem generation are equivalent.** Non-significance with 30 topics is not an equivalence test, and per-topic differences are large.
- **Why a representation wins on a topic**, except for compound-hyphen handling on three topics. Topic-theme groups show where differences are significant, not why.
- **That stemming is inherently inferior for Finnish.** Only one stemmer was tested; the authors themselves expect better ones to perform better.
- **Transfer to short queries, other domains or other languages.**
- **The exact size of the plain-word gap or the stem-generation gain as stated in the Discussion and Conclusion** (48–58%, 9.2 pp). These do not match the tables (§9).

## 15. Relationship to current Uzbek evidence

- **No Uzbek data.** Finnish (Uralic) and Uzbek (Turkic) are both agglutinative and suffixing.
  - Context (not from the paper): Finnish stem alternation (consonant gradation, e.g. *kissa → kissoi-*) is what makes stem generation attractive. Uzbek has fewer stem alternations (e.g. final *k/q → g/g‘* before vowel-initial suffixes), so the relative value of stem generation vs suffix stripping may differ for Uzbek. This must be tested, not assumed.
- **Uzbek tools exist** for all main representations studied here:
  - stemmer and lemmatizer (Bakaev PhD; Xusainova PhD, UzbStemmer; Elov DSc lemma-based indexing; MASTER_INDEX C);
  - none of them has a qrels-based raw/stem/lemma retrieval comparison.
  This paper is the kind of controlled evaluation missing for those Uzbek tools.
- **Relation to existing cards:**
  - **Airio 2006 (`CR000491`, same Tampere group, InQuery, CLEF 2003).** Airio found Snowball stemming ≈ lemmatization without decompounding for Finnish monolingual retrieval (MAP 48.5 vs 47.0). Here Snowball is 4.1–7.3 pp below FINTWOL on TUTK. The stem-vs-lemma ordering is therefore collection- or setting-dependent; the collections and metrics differ, so this is a cross-paper observation only. This paper itself cites the CLEF 2003 UTA experiments (Airio et al. 2003), where stemmed Finnish indexes were "about 15 % units lower" than lemmatization in a CLIR setting (ms pp. 31–32).
  - **Can et al. 2008 (MORPH-001, Turkish)** and **Haddad & Bechikh Ali 2014 (MORPH-002):** in Turkish, sophisticated lemmatization does not guarantee superiority, and simple prefix truncation is competitive. Here, simulated truncation via stem generation is equal to lemmatization. Both point the same way: for agglutinative languages, cheap conflation can match dictionary lemmatization on average.
  - **Alemayehu & Willett 2003 (`CR000354`)** is cited by this paper (ms p. 3) as another morphologically interesting language in stemming research.

## 16. Relationship to CURRENT_GAP

**Classification:** *supports (background)* + *no material effect on the residual core*.

**Touches (v0.8 elements):**

- `Lexical_raw → Lexical_stem → Lexical_lemma`: the full raw/stem/lemma family is evaluated, plus a fourth variant (query-side stem generation), in an agglutinative language. This is another instance of the already-rejected claim "raw/stem/lemma have not been compared" (GAP_BOUNDARY §4), though outside the low-resource setting.
- Per-query variation: per-topic divergence between two lexical representations with equal means, and topic-type (person / geographic / organizational / topical) differences in significance. This supports the premise behind measuring per-query quantities, not only aggregate metrics.

**Does not touch:**

- a fixed dense retriever D;
- fusion or hybrid conditions;
- unique relevant lexical or semantic hits, overlap, oracle union;
- incremental hybrid gain;
- the link of any of these to Uzbek query features.

The per-topic evidence concerns effectiveness differences **within the lexical channel**, not relevant-set complementarity with a semantic channel.

**Proposal:** keep v0.8 refined unchanged. Optionally cite this paper in the evidence boundary as a classic, peer-reviewed controlled raw/stem/lemma (+ stem generation) study in an agglutinative language showing aggregate parity with per-topic divergence and no semantic/hybrid component. This is a proposal only; `CURRENT_GAP.md` has not been edited.

## 17. Implications for our research design

- **Baselines / lexical variants.**
  - Keep `BM25_raw` as a mandatory floor. Here plain words still reach about half of the best lexical effectiveness, so raw is weak but not degenerate in an agglutinative language, and it may retrieve different documents (untested here).
  - Optional control: **query-side variant expansion over the raw index** (an analogue of stem generation). It holds the index constant while changing only the query, which separates "normalize index" from "expand query".
    - Context (not from the paper): with BM25 the variants would have to be scored as one pseudo-term (synonym/`#syn`-style grouping) rather than as independent OR terms, otherwise idf and term-frequency saturation change the weighting. This makes it a secondary condition, not part of the primary raw/stem/lemma × D matrix.
- **Preprocessing control.**
  - Per-topic differences here are traced to compound **hyphen** handling. For Uzbek, fix and report identically across raw/stem/lemma:
    - hyphens;
    - apostrophe variants in o‘/g‘ and the tutuq belgisi;
    - Latin/Cyrillic script;
    - lowercasing.
  - Also fix a policy for words the analyzer does not recognize (the authors list proper names as a lemmatizer weakness, ms p. 34).
- **Qrels / metrics.**
  - Collect **graded** relevance (e.g. 0–3) and report results at two thresholds (e.g. ≥2 and =3). Here the size and significance of the stemmer gap, and even a per-topic winner (T15), change with the threshold.
  - Document pooling depth and assessor procedure explicitly; this paper cannot be assessed on them.
- **Query taxonomy.**
  - Add the **entity-type of the query** (person / place / organization / general topic) as a candidate feature. Here significant representation differences appeared only in geographic and organizational groups.
  - Keep **query length** as a feature and include short queries. TUTK topics are long, which may favour raw word forms (the authors' "conjunctional effect").
- **Statistics.**
  - Use per-query paired tests with correction and report effect sizes and per-query distributions.
  - A multi-system Friedman test is acceptable as an omnibus test, but directions must be checked against means (cf. the Table IX inconsistency).
  - Sparck Jones's 5 / 10-pp thresholds can serve as a secondary "practical significance" description.
- **Per-query analysis.**
  - Reproduce the per-topic difference plot for raw/stem/lemma, but extend it to **relevant-set overlap and unique hits**, which this paper lacks.
  - Consider also measuring **overlap among the lexical variants themselves** (BM25_stem vs BM25_lemma). Equal means with large per-topic divergence suggest they may retrieve partly different relevant documents. This is a hypothesis, not a result of this paper.
- **Hypothesis.** The paper motivates, but does not test, the premise that changing the lexical representation changes *which* queries (and possibly which documents) the lexical channel serves well even when the mean is unchanged. That is a precondition for any morphology-induced change in lexical–dense complementarity.

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| Best-match / probabilistic IR | Search that ranks documents by estimated relevance instead of returning an exact Boolean set | Partial-match ranking by a probabilistic (here inference-network) model |
| INQUERY | The 1990s search engine used here; queries are built from operators | Inference-network retrieval system (Callan et al. 1992); `#sum`, `#syn` operators |
| `#syn` operator | "Treat all these words as the same word" | Synonym grouping: members counted as one term |
| Plain words | Query words exactly as written, index unchanged | Surface-form (raw) representation |
| Stemming | Cut word endings by rules; the result need not be a real word | Suffix stripping (Snowball Finnish), index and query stemmed |
| Lemmatization | Replace each word form by its dictionary form using a lexicon | FINTWOL two-level morphological analysis; lemmatized index |
| Inflectional stem generation | From the dictionary form, produce all the stems to which endings attach; find all index words starting with them | Query-side expansion: base form → stems → prefix match over the word-form index (MaxStemma, Finstems) |
| Truncation | Search by the beginning of a word (`kiss*`) | Prefix matching; simulated here with grep |
| False drops | Wrong words caught by truncation (e.g. *georgetown* for *george*) | Non-variant index terms matched by a prefix |
| Compound splitting | Index the parts of compound words as well | Decompounded lemmatized index (LEMS) |
| Derivational query | Add related derived words (not just inflected forms) | Query expansion with productive derivatives |
| Graded relevance; stringent / normal / liberal | Relevance on a 0–3 scale; different cut-offs for what counts as relevant | Thresholds =3 / ≥2 / ≥1 |
| Average precision over recall levels | Precision averaged across 10 recall points | 10-point average precision (whether and how precision is interpolated is not stated) |
| Friedman test | Compares several systems on the same queries using per-query ranks | Nonparametric repeated-measures test with pairwise comparisons |
| Practical significance (Sparck Jones) | Whether a difference is big enough to matter | < 5 pp not noticeable; 5–10 noticeable; > 10 material |
| Complementarity (project term) | Each channel finds relevant documents the other misses | Unique relevant hits, overlap, oracle-union gain; **not measured here** |

## 19. Open questions / verification needed

1. **TUTK qrels:** pooling depth, assessors and number of relevant documents per level. They are only in Sormunen (2000); check whether it is in the record set before using TUTK-based numbers for recall-type claims.
2. **"48 to 58 %" and "9.2 % units"** (ms pp. 35–36) do not follow from Table VI. The published Emerald version should be checked for corrected values.
3. **Environment One vs Two discrepancy** for the same FINTWOL / compounds-not-split / basic-query configuration (24.1 / 35.0 vs 21.6 / 30.3): is it caused by query construction, stop list or evaluation differences? Not stated.
4. **Table IX direction** for LEMNS1 > INFL2 and LEMNS1 > LEMNS2 on the liberal threshold vs Table VII means. Is this due to rank-based ordering, or is it a labelling error?
5. **Post-hoc procedure and multiple-comparison handling** of the Friedman test: not described.
6. **Topic-group sizes and per-group AP values** (Env. Two): NOT_REPORTED except LEMNS1 = 45.2% for person-oriented queries.
7. **Kunttu (2003) M.Sc. thesis** (Finnish) holds the full Environment Two analysis, including pp. 67–70 on the hyphen effect. It is worth checking only if the thematic-group evidence becomes important.
8. **Published vs manuscript version:** pagination and possible textual changes are not verified (the publisher page was not reachable).

## 20. Decision after deep dive

- **Keep current gap?** Yes. v0.8 refined remains valid (§16).
- **Modify gap?** No change proposed. Optionally add to the GAP_BOUNDARY evidence list as a classic agglutinative-language raw/stem/lemma (+ stem generation) study without a semantic or hybrid component (researcher's decision).
- **Add decision?** Proposed for `decisions/DECISIONS.md` (researcher's decision):
  - "Uzbek qrels are graded; primary results are reported at two relevance thresholds";
  - "tokenization rules for hyphens / apostrophes / script are fixed and identical across raw / stem / lemma conditions".
- **Add experiment?** Optional secondary control: `BM25_raw + query-side variant expansion` (index unchanged), to separate index normalization from query expansion. Also a cheap extra analysis: relevant-set overlap between `BM25_stem` and `BM25_lemma` themselves, alongside the lexical–dense overlap.
- **Add citation to Chapter I?** Yes, §1.1: morphological processing of the lexical channel in highly inflectional languages; lemmatization ≈ stem generation > Snowball > plain in Finnish; aggregate parity with per-topic divergence. Also a short mention in the Conclusions to Chapter I as an example of classical studies that stop at lexical-only comparisons.
- **Proposed `MASTER_INDEX.md` row** (to add after approval):

| MORPH-029 | Kettunen, Kunttu, Järvelin — *To stem or lemmatize a highly inflectional language in a probabilistic IR environment?* (*Journal of Documentation* 61(4), 476–496) — [deep dive](deep-dives/2005_Kettunen_Kunttu_Jarvelin_Finnish_Stem_or_Lemmatize_Probabilistic_IR.md) | 2005 | A | HIGH | Finnish TUTK (53,893 news articles, 30 long topics, graded 0–3 relevance), INQUERY: plain word forms vs Snowball stemming vs FINTWOL lemmatization vs inflectional stem generation (query-side expansion over the unnormalized index). Avg. precision stringent/normal: lemma 24.1/35.0, stem generation 22.6/34.2, Snowball 20.0/27.7, plain 12.4/18.9; lemma ≈ stem generation in Env. One (n.s., Friedman), Snowball significantly lower at the normal threshold; compound splitting adds up to 3 pp. Per-topic plot: equal means but ≥5-point differences on 11/30 topics; significance differences by topic type (geographic/organizational). No BM25, no dense, no fusion, no overlap/unique-hit analysis. Discussion/Conclusion figures (48–58%, 9.2 pp) do not match the tables. |
