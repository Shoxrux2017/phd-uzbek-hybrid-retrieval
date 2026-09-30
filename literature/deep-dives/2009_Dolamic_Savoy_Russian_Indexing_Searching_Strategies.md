# Dolamic & Savoy (2009): Indexing and Searching Strategies for the Russian Language

**Targeted deep-dive status:** COMPLETED (AI-assisted, pending researcher review)
**Completed:** 2026-09-28
**Literature ID:** `MORPH-040` (assigned 2026-09-28, approved by researcher)
**Systematic-review record:** `CR000529`. Full-text triage: INCLUDE, reading priority HIGH, reading tier "2 — важно", `carries_complementarity_evidence = YES`. In this card we qualify that flag: the paper has **per-query win/loss counts between two lexical representations (light or aggressive stemming vs no stemming) for one model (DFR-I(ne)B2), plus three topic anecdotes** (§10, §16). There is no document-level overlap, unique-hit or oracle-union evidence, and no second retrieval channel.
**Provenance:** AI-assisted deep dive (Claude). The paper (8 PDF pages = printed pp. 2540–2547) was read in full from the pdftotext extraction (the Cyrillic examples are garbled in the extraction, so they were read from the images). Page images at 110 dpi were checked for PDF pp. 1–7 (= pp. 2540–2546): p. 2540 (abstract, dates, DOI), p. 2541 (Table 1), p. 2542 (stemmer rules, stop-word list), p. 2543 (Tables 2–4), p. 2544 (Table 5, Eqs. 1–8, parameters), p. 2545 (Table 6, also as a 250-dpi crop to read the bold values and asterisks), p. 2546 (query-by-query analysis and Conclusion, also as a 220-dpi crop for the Cyrillic terms). PDF p. 8 (= p. 2547) contains only references and was read from the text. Page references below are the journal's printed page numbers. Numbers computed by us are marked **[computed]** (recomputed with Python).
**Source rule:** **the paper is the primary and only authoritative source.** No code, website, later paper or background knowledge is used as evidence about what the authors did. Bibliographic check: a web search returned the IDEAS/RePEc record `ideas.repec.org/a/bla/jamist/v60y2009i12p2540-2547.html` and the University of Neuchâtel repository copy under the same title. Both agree with the PDF's own header (JASIST 60(12):2540–2547, 2009) (bibliographic check: IDEAS/RePEc, libra.unine.ch). The DOI was not resolved online; it is taken from the PDF (p. 2540).
**Reliability:** **A** (peer-reviewed journal article, *JASIST* 60(12), 2009, ASIS&T / Wiley). The experimental scope is narrow: one collection family, MAP only, and the test design compares each model with the best model in its column (§10).
**Verification:** independent AI verifier pass 2026-09-28; 9 findings addressed.

---

## Кратко для исследователя (RU)

- **Что сделано.** Классическое сравнение способов индексирования **для русского языка** (флективный славянский язык, кириллица) на русских коллекциях CLEF Domain-Specific 2005–2008:
  - библиографические записи по социальным наукам: RSSC (94 581 документ) и INION (145 802), документы очень короткие (19 и 15 различных терминов);
  - 94 запроса с оценками релевантности от экспертов CLEF, **только заголовок запроса** (в среднем 3,25 термина).
- **Варианты лексического представления** (Table 6, p. 2545):
  - без стемминга (None);
  - «лёгкий» стеммер авторов: 57 правил + 4 правила нормализации, только словоизменительные окончания существительных и прилагательных;
  - «агрессивный»: лёгкий + 40 правил для частых словообразовательных суффиксов;
  - Snowball (русский);
  - 4-граммы символов (языконезависимый вариант).
  - Лемматизации нет, корней нет.
- **Модели поиска (шесть):** tf-idf, dtu-dtn (векторные), Okapi (по нашему пониманию, не из статьи, — модель семейства BM25; формула и k1/b в статье **не приведены**), DFR-I(ne)B2, DFR-GL2, языковая модель (Hiemstra). Метрика только MAP (trec_eval, 1000 документов).
- **Главные числа** (Table 6, средняя MAP по шести моделям):
  - None 0,0898 → Light 0,1710 (+90,3%), Aggressive 0,1684 (+87,5%), Snowball 0,1650 (+83,6%), 4-gram 0,1644 (+83,0%);
  - Okapi: None 0,0881 → Light 0,1734, Aggressive 0,1735, Snowball 0,1648, 4-gram 0,1710;
  - лучшая ячейка: dtu-dtn + Light = 0,1892.
  - По тексту: стемминг vs None значим всегда; различия между стеммерами и между 4-граммами и стеммерами незначимы (двусторонний t-тест, α = 5%).
- **Анализ по запросам есть, но узкий** (p. 2546, только DFR-I(ne)B2):
  - Light лучше None на 61 запросе, Aggressive — на 67; хуже в обоих случаях на 18; без изменений 15 и 9 **[computed]**;
  - Topic #223: «детьми» в запросе vs «детей»/«дети» в документах. Light 0,6607 vs None 0,01, при этом Snowball 0,0227 и 4-gram 0,0598. То есть **на отдельном запросе разрыв между представлениями на порядок больше, чем в среднем** (запроса, где Snowball или 4-граммы лучше лёгкого стеммера, в статье нет; неоднородность по запросам показана только против None: 18 запросов с ухудшением);
  - Topic #146 «Диабет меллитус»: ни одного найденного документа, так как термины запроса отсутствуют в коллекции.
  - Нет пересечения найденных релевантных документов, уникальных находок, oracle union, признаков запросов.
- **Чего нет:** плотного (dense) поиска, гибрида/fusion, лемматизации, overlap/unique hits, разбивки по коллекциям, других метрик кроме MAP.
- **Внутренние несоответствия в статье:**
  - аннотация: отказ от стемминга «снижает MAP более чем на 50%», но по Table 6 снижение 43,2–49,2% по моделям и 47,5% по среднему **[computed]**;
  - аннотация: лёгкий стеммер «tends to perform best»; заключение: «for most IR models» (формулировка двусмысленна); по Table 6 он лучший только в 2 из 6 моделей (dtu-dtn, LM), лучший только по среднему;
  - аннотация: dtu-dtn и DFR лучше Okapi и LM. По Table 6 LM на втором месте в 4 из 5 столбцов, а DFR-GL2 ниже Okapi в 4 из 5;
  - аннотация и заключение: значимые отличия только у tf-idf и LM, «для Okapi значимых различий нет». Но в столбце None у Okapi и DFR-GL2 стоит звёздочка (значимо хуже лучшей модели);
  - авторы цитируют Buckley & Voorhees: сравнивать баллы можно только на одной коллекции. Затем сравнивают свой +90% с приростами для других языков из Tomlinson (2004) на других коллекциях.
- **Для нашего gap:** подтверждает уже занятую границу («стемминг vs без стемминга с Okapi/BM25 в морфологически богатом языке сравнивали», «n-граммы как альтернатива»). Ядро v0.8 (raw/stem/lemma BM25 × фиксированный D → overlap/unique hits → прирост гибрида) **не затрагивает**. Предложение: gap не менять.
- **Практическая польза для нас:**
  1. Для коротких запросов и коротких документов эффект нормализации может быть огромным (почти ×2 MAP). Длину запроса и документа нужно фиксировать и учитывать как признаки.
  2. Условие «stem» нужно специфицировать: лёгкий (только словоизменение) vs агрессивный (с деривацией); выбор существенно меняет результат на отдельных запросах.
  3. 4-граммы — дешёвый языконезависимый контроль, почти равный стеммерам в среднем.
  4. Запросы с нулевой выдачей из-за транслитерации заимствований (#146) — кандидат в признаки запроса для узбекского (кириллица/латиница, русские заимствования).

---

## 1. Bibliographic record

- **Authors:** Ljiljana Dolamic, Jacques Savoy
- **Affiliation:** Computer Science Department, University of Neuchâtel, Switzerland (p. 2540)
- **Year:** 2009
- **Venue:** *Journal of the American Society for Information Science and Technology* (JASIST), 60(12), 2540–2547, December 2009 (running header / footer, p. 2540; bibliographic check: IDEAS/RePEc)
- **Dates:** received March 18, 2009; revised June 11, 2009; accepted June 29, 2009; published online 7 August 2009 in Wiley InterScience (p. 2540 footnote)
- **Publisher:** ASIS&T / Wiley (© 2009 ASIS&T)
- **DOI:** `10.1002/asi.21191` (p. 2540)
- **Official record:** https://doi.org/10.1002/asi.21191 (not resolved online by us; see header)
- **Resources stated in paper:** stemmers and stop-word list at http://www.unine.ch/info/clef/ (pp. 2542, 2546). Not consulted.
- **Funding:** Swiss NSF, Grant #200021-113273 (Acknowledgment, p. 2546)
- **Source type:** peer-reviewed journal article (full paper, 8 pages)
- **Reliability:** A
- **Full text available:** yes (`07_full_text/pdfs/CR000529.pdf`, 8 pages)

## 2. Why this work matters to the PhD

It is a classical, controlled study of **lexical representation variants** (no stemming / light stemming / aggressive stemming / Snowball / character 4-grams) across **six lexical retrieval models including Okapi**, for a **morphologically rich language written in Cyrillic** with **human relevance judgments**. Russian matters indirectly for Uzbek: Uzbek text contains many Russian loanwords, and much Uzbek text is still in Cyrillic (Context, not from the paper).

| Axis | Relation |
|---|---|
| Lexical retrieval | **Direct.** Six models × five indexing strategies; Okapi is included, but its formula and parameters are not given |
| Semantic retrieval | **Absent** |
| Hybrid retrieval | **Absent**: no fusion of models or of representations |
| Uzbek morphology | Indirect: Russian is Slavic and fusional (case/number/gender endings, stem alternations such as fleeting vowels), not Turkic and agglutinative |
| Low-resource retrieval | Partly: the authors note that few Russian test collections were available in 2009 (pp. 2540–2541) |
| Current gap | Confirms already-occupied claims (stem vs none with BM25-family models in a morphologically rich language; n-gram alternatives). No effect on the residual core (§16) |

## 3. Research problem

### Simple explanation

In Russian, one noun can appear in many forms: "дети", "детей", "детьми" all mean "children". If the search engine indexes words exactly as written, a query with one form will not match documents with another form. The authors ask which way of reducing words to a common form works best for Russian search, and whether the answer depends on the ranking model.

### Formal formulation

- Objective (p. 2540): "to propose, compare, and evaluate various stemming, indexing, and search strategies" for Russian.
- Stated plan (p. 2541): "analyze stemmer effectiveness for Russian, and suggest which one would be the most effective. We also address the comparative retrieval effectiveness of an n-gram scheme, a language-independent approach, and compare them to a word-based scheme."
- Design: a factorial comparison, indexing strategy ∈ {None, Light, Aggressive, Snowball, 4-gram} × retrieval model ∈ {tf-idf, dtu-dtn, Okapi, DFR-I(ne)B2, DFR-GL2, LM}. The measure is MAP over 94 topics.
- Note: the introduction also describes the CLEF Domain-Specific track's objective (full-text vs manual indexing, usefulness of a thesaurus; p. 2540). This paper does **not** evaluate manual indexing or the thesaurus separately (§12).

## 4. Main idea

### Simple explanation

Write two rule-based Russian stemmers:
- a "light" one that cuts off only case/number endings of nouns and adjectives;
- an "aggressive" one that also cuts some word-building suffixes.

Compare them with no stemming, with the public Snowball stemmer and with splitting words into overlapping 4-letter pieces. Run every variant through six classical ranking models and measure MAP.

### Concrete example

The paper's own example (Topic #223 "Media in the preschool age", p. 2546):
- The query contains "детьми" (children, instrumental case).
- The relevant documents contain "детей" (genitive/accusative) or "дети" (nominative).
- Without stemming these do not match: AP = 0.01.
- The authors' light and aggressive stemmers reduce all three to the same stem. With the light stemmer AP = 0.6607.
- Snowball does not conflate them (AP 0.0227), and the 4-grams do not match either (AP 0.0598).
- The retrieval model for these AP values is not stated explicitly. The query-by-query analysis in the same paragraph uses DFR-I(ne)B2.

### Formal method

- **Light stemmer** (p. 2542): "light" stemmers "apply 57 rules in order to remove only the inflectional suffixes from nouns and adjectives (to normalize the resulting stems, we added four more rules)". The design policy is to focus on nouns and adjectives and "to avoid verb forms" (p. 2541).
- **Aggressive stemmer** (p. 2542): "to remove certain derivational suffixes, 40 rules were added to the light stemmer version". It concentrates on adjectival qualitative and relational suffixes (e.g., "кровь" → "кровавый"). Prefixes are not removed: the authors "completely ignored any prefixes we thought might change the base word's meaning" (p. 2542).
- **Snowball** (p. 2545): "the available Snowball stemmer (http://snowball.tartarus.org/)". The version is not stated.
- **4-gram** (p. 2545): overlapping 4-letter sequences, e.g. "prime minister" → {"prim", "rime", "mini", "inis", …, "ster"}. "the value 4 was selected because it produced the best IR performance". The data used for this selection are not stated.
- **Stop-word list:** 412 Russian word forms (pronouns, prepositions, conjunctions, etc.; p. 2542). It is used in all Table 6 runs (p. 2545).

## 5. Architecture / algorithm

1. **Document representation** (p. 2543). RSSC: `<title>` + `<text>`. INION: `<title-ru>` + `<keywords-ru>` + `<abstract-ru>`. `<keywords-ru>` holds "terms extracted manually from INION Thesaurus"; abstracts exist for "around 27% of the documents". Author names and classification tags are ignored.
2. **Query representation** (p. 2543). Title field only ("to more closely reflect queries sent to commercial search engines"); mean 3.25 search terms.
3. **Stop-word removal** (412 forms), then one of the five indexing strategies (§4).
4. **Ranking models** (pp. 2543–2545). The text says "two vector-space schemes and three probabilistic models" (p. 2543), but six models are described and reported: the three probabilistic families contain four models (§19).
   - **tf-idf**: tf × idf with cosine normalization, inner product.
   - **dtu-dtn** (Singhal et al., 1999; Eqs. 1–2): pivoted length normalization, slope = 0.25, pivot = 15 ("corresponding to the average document length").
   - **Okapi** (Robertson, Walker & Beaulieu, 2000): **no formula and no parameter values are given in the paper.** Context (not from the paper): the Okapi weighting in that reference is BM25 with parameters k1, b (and k3); we treat "Okapi" here as a BM25-family model with unknown settings.
   - **DFR-GL2** (Eqs. 3–5) and **DFR-I(ne)B2** (Eqs. 3, 6–7): mean dl = 15, c = 1.5 ("fixed empirically").
   - **LM** (Hiemstra, 2000; Eq. 8): linear mixture (our characterization: Jelinek–Mercer-type; the corpus estimate is P[t_j|C] = df_j / l_c, document-frequency based) of document and corpus estimates, λ = 0.25 for all terms. The prior P[d_i] is ignored.
5. **Evaluation** (p. 2545): MAP via TREC_EVAL, up to 1,000 retrieved records per query; two-sided t-test, α = 5%.
6. **Extra runs reported only in the text** (p. 2545, no table):
   - stemming + decompounding: "around 5% in average" lower MAP than without decompounding;
   - with vs without the stop-word list: differences "rather small (around 2% on average)".

## 6. Data

- **Dataset/corpus** (Table 2, p. 2543): Russian part of the CLEF Domain-Specific tracks 2005–2008.

| | 2005 | 2006 | 2007 | 2008 |
|---|---|---|---|---|
| Source | RSSC | RSSC + INION | INION | INION |
| Size | 64.6 MB | 145.5 MB | 80.9 MB | 80.9 MB |
| Documents | 94,581 | 240,383 | 145,802 | 145,802 |
| Topics | 25 (#126–#150) | 25 (#151–#175) | 25 (#176–#200) | 25 (#201–#225) |

- Check: 94,581 + 145,802 = 240,383 ✓ and 64.6 + 80.9 = 145.5 MB ✓ **[computed]**.
- **Language / domain:** Russian; social science and economics bibliographic records (RSSC = Russian Social Science Corpus; INION).
- **Documents:** very short: "19 and 15 distinct indexing terms, respectively" (p. 2542). INION records mix free text with manually assigned thesaurus keywords.
- **Queries:** 100 CLEF topics with title/description/narrative (TREC style, Table 5). Only the title is used; mean 3.25 terms.
- **Relevance judgments:** "made by human assessors" (p. 2543). "for six topics no relevant document could be found, leaving 94 topics for the evaluation". Pooling depth, grades and assessor agreement: NOT_REPORTED.
- **Train/dev/test:** no split. Parameters are fixed (§5), and the 4-gram length was "selected because it produced the best IR performance" (the data used for that choice: NOT_REPORTED).
- **Pooling across years:** topics from 2005–2008 are "combined" into one set of 94 (p. 2545). Which collection each topic was searched against is not stated explicitly; Table 2 implies each year's topics use that year's collection. Per-year results: NOT_REPORTED.

## 7. Baselines

| Baseline | What it is | Why selected | Fair comparison? |
|---|---|---|---|
| None (no stemming) | Surface word forms after stop-word removal | Reference for all normalization gains | Yes: same models, stop list and topics |
| Snowball (Russian) | Public algorithmic stemmer | The authors: its performance "tends to reflect the best practice in this field" (p. 2541) | Yes. Version unspecified |
| 4-gram | Language-independent character n-grams (McNamee & Mayfield, 2004) | Alternative that needs no linguistic rules | Mostly. n = 4 was chosen as the best-performing value, apparently on the same topics (not stated) |
| Six retrieval models | tf-idf, dtu-dtn, Okapi, two DFR, LM | "broader perspective" (p. 2543) | Partly. Parameters are fixed by hand ("empirically"); Okapi settings are not reported, so its tuning relative to the others is unknown |

## 8. Metrics

| Metric | Definition | Simple meaning here | Appropriate? |
|---|---|---|---|
| MAP | Mean over topics of average precision: "mean of the precision scores obtained after each relevant document is retrieved, using zero as the precision for relevant documents that are not retrieved" (p. 2545), depth 1,000 | "On average, how early do the relevant records appear, taking all of them into account?" | Yes for ad hoc retrieval with several relevant documents. No early-precision or recall figures are reported, so candidate coverage (important for hybrids) cannot be read from the paper |
| AP (per topic) | Average precision for one topic | Used in the query-by-query analysis | Yes |

Significance: two-sided t-test, α = 5% (Buckley & Voorhees, 2005). Whether the test is paired over topics is not stated explicitly.

## 9. Results

### Table 6: MAP by indexing strategy and model (p. 2545; checked on the 250-dpi crop)

| Model | None | Light | Aggressive | Snowball | 4-gram |
|---|---:|---:|---:|---:|---:|
| tf idf | 0.0739* | 0.1302* | 0.1328* | 0.1282* | 0.1381* |
| dtu-dtn | **0.0999** | **0.1892** | 0.1749 | **0.1847** | 0.1708 |
| Okapi | 0.0881* | 0.1734 | 0.1735 | 0.1648 | 0.1710 |
| DFR-I(ne)B2 | 0.0928 | 0.1802 | **0.1812** | 0.1734 | **0.1741** |
| DFR-GL2 | 0.0879* | 0.1708 | 0.1688 | 0.1624 | 0.1712 |
| LM | 0.0964* | 0.1821 | 0.1793 | 0.1762 | 0.1613* |
| mean | 0.0898 | 0.1710 | 0.1684 | 0.1650 | 0.1644 |
| % change | | +90.3% | +87.5% | +83.6% | +83.0% |

Bold = best model in the column. \* = significantly different from the best model in that column (p. 2545).

Checks and derived values **[computed]**:
- The "mean" row is the mean of the six models: 0.08983 / 0.17098 / 0.16842 / 0.16495 / 0.16442 ✓.
- The "% change" row matches the **unrounded** means: +90.33 / +87.48 / +83.62 / +83.02% ✓. From the printed rounded means one gets +90.4 / +87.5 / +83.7 / +83.1%.
- Relative gain over None per model:

| Model | Light | Aggressive | Snowball | 4-gram |
|---|---:|---:|---:|---:|
| tf idf | +76.2% | +79.7% | +73.5% | +86.9% |
| dtu-dtn | +89.4% | +75.1% | +84.9% | +71.0% |
| Okapi | +96.8% | +96.9% | +87.1% | +94.1% |
| DFR-I(ne)B2 | +94.2% | +95.3% | +86.9% | +87.6% |
| DFR-GL2 | +94.3% | +92.0% | +84.8% | +94.8% |
| LM | +88.9% | +86.0% | +82.8% | +67.3% |

- **MAP reduction when stemming is ignored** (1 − None / Light): 43.2% (tf idf) to 49.2% (Okapi); 47.5% on the mean. Even against the best strategy per model the maximum is 49.2% (Okapi vs Aggressive). The abstract's "more than 50%" is therefore not supported by Table 6 (§19).
- **Which strategy wins per model:** Light in 2 of 6 (dtu-dtn, LM); Aggressive in 2 (Okapi by 0.0001, DFR-I(ne)B2); 4-gram in 2 (tf idf, DFR-GL2). Light is best only on the six-model mean.
- **4-gram vs Light:** −3.84% on the unrounded mean (−3.86% from the printed means; the text says −3.8%, p. 2546 ✓). Per model the difference ranges from +6.1% (tf idf) to −11.4% (LM).
- **Snowball vs Light:** lower in all six models (−1.5% to −5.0%).
- **Model ranking by column:** dtu-dtn is first in None, Light and Snowball; DFR-I(ne)B2 is first in Aggressive and 4-gram. **LM is second in 4 of 5 columns.** DFR-GL2 is below Okapi in 4 of 5 columns (all except 4-gram). tf idf is last everywhere.
- Okapi vs best model: −11.8% (None), −8.4% (Light) relative to dtu-dtn. In the stemmed columns the differences are not marked significant.

### Statements reported only in the text

- Stemming vs no stemming: "always statistically significant" (p. 2546). Per-model test results are not shown in a table.
- 4-gram vs word-based stemming: differences "never statistically significant" (p. 2546).
- Light vs Aggressive vs Snowball: "never statistically significant" (Conclusion, p. 2546).
- Decompounding: about 5% lower MAP; stop-word list: about 2% difference on average (p. 2545).
- Comparison with other languages (p. 2546): the Russian gains are larger than those reported by Tomlinson (2004) for other European languages ("+4% with the English language, +4.1% Dutch, +7% Spanish, +9% French, +15% Italian, +19% German, +29% Swedish, or +40% Finnish"). These figures come from other collections and another system (§12).

### Query-by-query analysis (p. 2546; DFR-I(ne)B2)

| Comparison vs None | Topics improved | Topics worse | Unchanged **[computed]** |
|---|---:|---:|---:|
| Light | 61 | 18 | 15 |
| Aggressive | 67 | 18 | 9 |

- The unchanged counts assume that all 94 topics were counted; the paper does not state it.

Topic examples (AP, p. 2546):

| Topic | None | Light | Snowball | 4-gram | Mechanism given by the authors |
|---|---:|---:|---:|---:|---|
| #223 "Media in the preschool age" | 0.01 | 0.6607 | 0.0227 | 0.0598 | "детьми" (query) vs "детей"/"дети" (documents); conflated by light and aggressive stemmers, not by Snowball or 4-grams |
| #160 "Precarious working conditions" | 0.0093 | 0.6165 | — | — | "опасные" and the printed form "опасньх" (apparently a typo for "опасных") conflated. Improvement "for all stemming procedures" |
| #146 "Diabetes Mellitus" ("Диабет меллитус") | — | — | — | — | "did not retrieve any items, relevant or not, since none of the terms in the topic appeared in the collection" |

- #223 gain: +0.6507 AP absolute, ×66 **[computed]**; #160: +0.6072, ×66 **[computed]**.
- The authors also say that stemming "can diminish retrieval performance, usually through conflating nonrelated terms into the same stem" (p. 2546). No example topic with a loss is given.

## 10. Statistical evidence

- **Significance test:** two-sided t-test, α = 5% (p. 2545). Whether it is paired is not stated explicitly. In Table 6 each cell is tested **only against the best model of the same column**. The tests between indexing strategies (stem vs none, stemmer vs stemmer, 4-gram vs stemmers) are reported only in the text, without per-model marks or p-values.
- **Confidence intervals:** NOT_REPORTED.
- **Runs / seeds:** not applicable (deterministic lexical runs).
- **Ablation:** partial, text-only: decompounding on/off (−5%) and stop list on/off (~2%). The 4-gram length was chosen as the best-performing value (the other lengths tried: NOT_REPORTED).
- **Per-query analysis:** **yes, limited.**
  - Win/loss counts vs None for Light and Aggressive, one model (DFR-I(ne)B2).
  - Three topic anecdotes; one shows a per-topic gap far larger than the mean differences (#223: Light 0.6607 ≫ 4-gram 0.0598 > Snowball 0.0227 > None 0.01). This is the same order as the DFR-I(ne)B2 means in Table 6 (Light > 4-gram > Snowball > None), so it is not a ranking flip; no topic where Snowball or 4-grams beat Light is reported.
  - NOT_REPORTED: pairwise win/loss between Light, Aggressive, Snowball and 4-gram; per-query results for other models; overlap of retrieved relevant documents; unique relevant hits; oracle union / run combination; query features (length, OOV, part of speech) beyond the anecdotes.
- **Breakdown by collection/year:** NOT_REPORTED.

## 11. Strengths

- Clean factorial design: 5 indexing strategies × 6 models on the same 94 human-judged topics and the same stop list.
- Two self-built stemmers of different strength, plus a public stemmer and a language-independent n-gram control. The stemmers and stop list were released (pp. 2542, 2546).
- A model-independent conclusion: normalization raises MAP by +67% to +97% for every model (roughly doubling it in most cells) **[computed]**.
- A per-query view (win/loss counts) and concrete linguistic explanations of the large gains and of Snowball's failure on one topic.
- Clear explanation of Russian morphology (cases, fleeting vowels, derivation, compounding) and of why verbs were excluded from stemming.
- Explicit model parameters for five of the six models.

## 12. Limitations

### Stated by the authors

- Algorithmic stemmers make over-stemming and under-stemming errors (p. 2541). Lexical (dictionary) stemmers must handle out-of-vocabulary words such as names and acronyms and "thus cannot be viewed as error-free approaches" (p. 2541).
- Stemming "can diminish retrieval performance, usually through conflating nonrelated terms into the same stem" (p. 2546).
- Aggressive stemming may return "unexpected results" for the user; the authors recommend the light stemmer partly for understandability (p. 2546).
- Scores are comparable only on the same collection and topics (the quoted Buckley & Voorhees passage, p. 2545).

### Inferred from the experimental design

1. **No lemmatization or morphological analyzer.** The comparison is none vs rule-based stems vs 4-grams. The stem-vs-lemma question for Russian is not addressed.
2. **Okapi is under-specified.** No formula and no k1/b/k3 are reported, while other models get explicit parameters. The BM25-type evidence cannot be reproduced exactly from the paper.
3. **Collection particularity.** Very short bibliographic records (15–19 distinct terms), partly manual thesaurus keywords, title-only queries of about 3 terms, low absolute MAP (≤ 0.19). The authors themselves link the large stemming effect to short documents (Conclusion). Transfer to full-text documents or longer queries is untested.
4. **Pooling of three collections** (RSSC, RSSC+INION, INION) into one 94-topic mean, with no per-collection results. This sits uneasily with the authors' own quote that scores are only comparable on "the exact same collection".
5. **Cross-study comparison.** The "+90% vs +4% (English) … +40% (Finnish)" comparison uses Tomlinson's (2004) results on other collections with another system, which the quoted Buckley & Voorhees principle excludes.
6. **Test design.** Asterisks test each model against the column's best model. The comparisons that matter for the paper's conclusions (strategy vs strategy) are only stated in prose, without per-model detail. Whether the t-test is paired is not stated.
7. **Possible tuning on the test topics.** The 4-gram length and several model constants were chosen "empirically"; no separate dev set is described.
8. **Per-query analysis limited** to one model and to comparisons against None. It is mostly anecdotal and gives no document-level evidence.
9. **Several summary claims are stronger than Table 6** (§19): "more than 50%", "light best for most models", "DFR better than LM/Okapi", "Okapi no significant differences".

## 13. What the work proves

- On the Russian CLEF Domain-Specific collections (short bibliographic records, title queries), **any tested normalization (light, aggressive, Snowball stemming or 4-grams) raises MAP substantially over surface word forms (+67% to +97% per model–strategy cell [computed], +83% to +90% on the six-model mean)**, for all six lexical models. That includes Okapi: 0.0881 → 0.1648–0.1735 (Table 6). The authors report that stem vs none is always significant.
- **The choice among stemmers and 4-grams matters little on average.** Means lie within 0.1644–0.1710; the authors report these differences as non-significant. The best strategy differs by model.
- **The effect is heterogeneous per query.** For DFR-I(ne)B2, stemming improves 61–67 topics but hurts 18 of 94. On individual topics the representations can differ by an order of magnitude (#223: Light 0.6607 vs Snowball 0.0227 vs 4-gram 0.0598).
- Decompounding does not help Russian here (about −5%), and the stop list has little effect (about 2%). Both are stated without tables.

## 14. What the work does NOT prove

- **Anything about lemmatization**, or about stem vs lemma. There is no lemma condition.
- **Anything about dense/semantic retrieval, hybrid fusion or lexical–semantic complementarity.** Only lexical models are used, and no runs are combined.
- **That different representations find different relevant documents.** There is no overlap, unique-hit or oracle-union analysis; per-topic AP differences are not document-level evidence.
- **That the light stemmer is better than the aggressive stemmer, Snowball or 4-grams.** The differences are small, reported as non-significant, and the winner changes by model.
- **That the Russian stemming gain is larger than for other languages.** That comparison crosses collections and systems.
- **That the effect generalizes** to full-text documents, longer queries or other domains. Only one collection family with very short records was tested.
- **Which query characteristics predict gains or losses.** There is no quantitative query-feature analysis.

## 15. Relationship to current Uzbek evidence

- **No Uzbek data.** Russian is Slavic and fusional: one ending carries case, number and gender, and stems alternate (fleeting vowels). Uzbek is Turkic and agglutinative: chains of mostly one-function suffixes. The *size* of the stemming effect does not transfer directly. The design lessons do (light vs aggressive rule sets, noun/adjective focus, n-gram control).
- Context (not from the paper): Uzbek also has stem alternations at suffix boundaries (e.g., *o‘g‘il → o‘g‘li*, *yurak → yuragi*). A suffix-stripping stemmer therefore meets the same kind of irregularity that the authors handle with "normalization" rules.
- Context (not from the paper): Uzbek texts contain many Russian loanwords, and part of Uzbek text is in Cyrillic. Topic #146 ("Диабет меллитус", transliterated Latin terms absent from the collection) is the kind of transliteration/loanword mismatch expected in Uzbek queries.
- Place in our corpus (classical lexical-normalization cluster):
  - **CR000523** Fautsch & Savoy 2009 (same group, same JASIST year): English, same methodology (none / light / algorithmic stemmers / lemma, five models, per-query win/loss). Together they show the same group's finding: light stemming is competitive, and more aggressive or linguistic processing is not clearly better.
  - **CR000688** McNamee, Nicholas & Mayfield 2009: 18 languages including Russian; per our card, trun5 prefix truncation is the top method in Russian (+40.0%). It agrees with this paper's finding that language-independent approaches are close to stemmers, on a different Russian collection.
  - **CR000566** Paik et al. 2013 uses Dolamic & Savoy rule-based stemmers as baselines for other languages.
  - **MORPH-001** Can et al. 2008 and **MORPH-002** Haddad & Bechikh Ali 2014 (Turkish): the same pattern in an agglutinative Turkic language, including simple truncation remaining competitive.
- None of these, including this paper, joins lexical-representation variants with a dense retriever or analyses relevant-set overlap.

## 16. Relationship to CURRENT_GAP

**Classification:** *supports the existing evidence boundary (closes part of the broad gap, already listed as occupied)* + *no material effect on the residual core*.

- **Already-occupied claims it confirms** (v0.8 "what literature no longer allows us to claim"):
  - "raw/stem/… have not been compared in IR for morphologically rich languages";
  - "morphology-aware BM25 is unstudied".
  Here an Okapi (BM25-family) model is compared across none / two stemmers / Snowball / 4-grams on human-judged Russian topics.
- **Partial touch on per-query analysis.** The v0.8 list of measurements includes per-query changes. This paper gives per-query win/loss counts between *lexical* representations for one model, but not the quantities v0.8 is built on:
  - unique relevant documents per channel;
  - overlap with a dense retriever;
  - oracle union;
  - hybrid gain.
  The triage flag `carries_complementarity_evidence = YES` should be read as "lexical-vs-lexical per-query heterogeneity" only.
- **Motivational value.** The 18 topics hurt by stemming (vs 61–67 helped) show that whether normalization helps is query-specific, and Topic #223 shows that per-topic gaps between representations can be far larger than the mean differences (the authors' light stemmer succeeds where Snowball and 4-grams fail). The paper reports no topic where Snowball or 4-grams beat the light stemmer. That supports the premise of v0.8 that changing the representation changes *which* relevant documents are reachable, not just the average. It does not test this at the document level or against a semantic channel.
- **No effect on the residual core:** raw/stem/lemma BM25 × the same fixed D → unique hits / overlap / oracle union / hybrid gain → relation to query features. None of these elements is present.

**Proposal:** keep v0.8 refined unchanged. Optionally cite the paper in the boundary as a classical Slavic/Cyrillic example of large normalization gains with BM25-family models and query-level heterogeneity, without any semantic or hybrid component. This is a proposal only; `CURRENT_GAP.md` has not been edited.

## 17. Implications for our research design

- **Lexical variants.**
  - Specify the stemmer strength explicitly: an inflection-only ("light") vs an inflection+derivation ("aggressive") Uzbek stemmer are different conditions.
  - Consider including both, or justify one. In this paper they tie on average but differ on individual topics (61 vs 67 topics improved).
  - Following the authors' policy, a noun/adjective-focused light stemmer is a defensible "stem" condition. Its behaviour on verbs must be documented.
- **Language-independent control.** Add a character n-gram or prefix-truncation BM25 run as a cheap control (`BM25_simple-normalization` in v0.8). Here 4-grams reach 96% of the light stemmer's mean MAP **[computed: 0.1644/0.1710]**. Fix the n-gram length on dev, not on test.
- **BM25 reporting.** Report the BM25 formula variant and k1/b. This paper's Okapi runs cannot be reproduced for lack of them.
- **Query and document length as moderators.** The very large effect here comes with title queries of about 3 terms and 15–19-term documents. For Uzbek:
  - record query length and document length;
  - analyse the morphology effect and complementarity by these strata;
  - consider short-title vs longer-description query variants if topics allow.
- **Query taxonomy.** Candidate features suggested by the topic examples:
  - case/inflection mismatch between query and documents (#223);
  - loanword/transliteration terms absent from the collection, giving a zero-result query (#146);
  - words where a stemmer over-conflates unrelated terms (the authors' "nonrelated terms" risk).
  These map to the v0.8 candidates "morphological variability", "rare terms" and "Latin/Cyrillic variation".
- **Per-query reporting.** Report win/tie/loss counts between every pair of lexical variants, not only against raw, and for the primary model. Then add the document-level unique-hit/overlap analysis that this paper lacks.
- **Statistical protocol.** Test the *comparisons of interest* directly (variant vs variant, per model), paired over queries. Report p-values or CIs. Do not use only "vs best model in column" marks.
- **Collection hygiene.** Do not average topics over different document collections without also reporting per-collection results.
- **Metrics.** Add Recall@k (candidate coverage) and nDCG@10 to MAP. MAP alone cannot show whether a representation adds reachable relevant documents.

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| Stemming | Cutting word endings so that different forms of a word match | Rule-based mapping of word forms to a (not necessarily linguistic) stem |
| Light stemmer | Removes only grammatical endings (case, number) | Inflectional-suffix removal, here for nouns and adjectives (57 + 4 rules) |
| Aggressive stemmer | Also removes word-building suffixes, so more words are merged | Light rules + 40 derivational-suffix rules |
| Snowball | A public family of algorithmic stemmers for many languages | Porter-style suffix-stripping algorithms |
| Character n-gram (4-gram) indexing | Index overlapping 4-letter pieces instead of words; partial matches still count | Terms = all character substrings of length 4 |
| Decompounding | Splitting compound words into parts | Compound segmentation before indexing |
| tf-idf | Word weight = frequency in the document × rarity in the collection | Vector-space weighting with cosine normalization |
| dtu-dtn | tf-idf variant that dampens repeated terms and corrects for document length | Pivoted length normalization (Singhal et al., 1999) |
| Okapi (BM25) | Classic probabilistic word-matching score with saturation and length normalization | Robertson et al. (2000); parameters not reported in this paper |
| DFR | Scores a term by how far its frequency in a document departs from chance | Divergence-from-Randomness models (Amati & van Rijsbergen, 2002) |
| Language model (LM) | Ranks documents by how likely they are to "generate" the query | Query likelihood with collection smoothing (Hiemstra, 2000) |
| MAP / AP | Average of precision values at each relevant document; MAP averages AP over queries | Standard ad hoc effectiveness measure |
| Two-sided t-test | Checks whether a mean difference is reliably non-zero, in either direction | t-test at α = 5% |
| Complementarity (project term) | Each channel finds some relevant documents the other misses | Unique relevant hits, overlap, oracle-union gain |

## 19. Open questions / verification needed

1. **Abstract vs Table 6 (reduction size).** Abstract (p. 2540): "Ignoring stemming generally reduces the MAP by more than 50%". Table 6 (p. 2545) gives 43.2–49.2% per model and 47.5% on the mean **[computed]**. Wording error or a different base? Not decidable from the paper.
2. **"Light tends to perform best"** (abstract, p. 2540) and "for most IR models ... our light stemming tends to perform better" (Conclusion, p. 2546; the scope of "for most IR models" is ambiguous) vs Table 6: light is the best stemming strategy for only 2 of 6 models (dtu-dtn, LM).
3. **Model ranking claim.** The abstract says dtu-dtn and DFR models are better than Okapi and LM. In Table 6, LM is second in 4 of 5 columns, and DFR-GL2 is below Okapi in 4 of 5.
4. **Significance statements.** The abstract says only LM and tf-idf differ significantly; the Conclusion says "for the Okapi model there are no significant statistical differences". Table 6 marks Okapi (0.0881*) and DFR-GL2 (0.0879*) as significant in the None column. The body text on p. 2545 mentions the None-column exception.
5. **Number of probabilistic models:** "two vector-space schemes and three probabilistic models" (p. 2543) vs four probabilistic rows in Table 6 (Okapi, DFR-I(ne)B2, DFR-GL2, LM). Possibly "three families".
6. **Okapi configuration** (formula variant, k1, b, k3): NOT_REPORTED.
7. **Is the t-test paired?** Which models do the "always significant" stem-vs-none tests cover? NOT_REPORTED.
8. **Which retrieval model produced the topic AP values** (#223, #160): implied DFR-I(ne)B2, not stated. The printed "опасньх" is probably a typo.
9. **Per-collection / per-year results** and the collection each topic was run against: NOT_REPORTED.
10. **4-gram length selection data** (test topics?): NOT_REPORTED.
11. **Topic #146:** under which indexing strategy was nothing retrieved (is the statement meant for all strategies, including 4-grams)? Not stated.

## 20. Decision after deep dive

- **Keep current gap?** Yes. v0.8 refined remains valid (§16).
- **Modify gap?** No change proposed. Optionally add this paper to the classical-boundary list in `GAP_BOUNDARY` next to Fautsch & Savoy 2009 and McNamee et al. 2009 (researcher's decision).
- **Add decision?** Proposed for `decisions/DECISIONS.md` (researcher's decision):
  - "The `stem` condition must state stemmer strength (inflection-only vs inflection+derivation) and part-of-speech coverage";
  - "Pairwise per-query win/tie/loss between all lexical variants is reported alongside document-level unique hits".
- **Add experiment?** Optional low-cost addition: a light vs aggressive Uzbek stemmer pair, if an aggressive variant is available, and a character-n-gram or prefix-truncation BM25 control. Stratify the per-query analysis by query length.
- **Add citation to Chapter I?** Yes, §1.1: classical evidence that normalization strongly affects lexical retrieval in a morphologically rich Cyrillic-script language, across models including Okapi; light stemming and n-grams are close on average but differ per query. Cite with the caveat that the summary claims in the abstract are stronger than Table 6.
- **Proposed `MASTER_INDEX.md` row** (to add after approval):

| MORPH-040 | Dolamic & Savoy — *Indexing and Searching Strategies for the Russian Language* (*JASIST* 60(12), 2540–2547) — [deep dive](deep-dives/2009_Dolamic_Savoy_Russian_Indexing_Searching_Strategies.md) | 2009 | A | MEDIUM | Russian CLEF Domain-Specific 2005–2008 (RSSC/INION short bibliographic records, 94 title-only topics, human qrels); none vs authors' light (inflectional) and aggressive (+derivational) stemmers vs Snowball vs 4-grams × six lexical models incl. Okapi (parameters not reported). Six-model mean MAP 0.0898 → 0.1710 / 0.1684 / 0.1650 / 0.1644 (+83–90%); Okapi 0.0881 → 0.1734 (light); stem vs none always significant, stemmers/4-gram differences not. Per-query (DFR-I(ne)B2): light/aggressive improve 61/67 topics, hurt 18; topic anecdotes show per-topic gaps far larger than mean differences (#223: light 0.6607 vs Snowball 0.0227). No lemma, no dense, no fusion, no overlap/unique-hit analysis. Abstract overstates Table 6 (">50%" reduction vs 43–49%; light best in only 2/6 models). |
