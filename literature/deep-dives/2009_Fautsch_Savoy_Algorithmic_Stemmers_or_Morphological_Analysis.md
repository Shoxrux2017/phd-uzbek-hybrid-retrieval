# Fautsch & Savoy (2009): Algorithmic Stemmers or Morphological Analysis? An Evaluation

**Targeted deep-dive status:** COMPLETED (AI-assisted, pending researcher review)
**Completed:** 2026-09-28
**Literature ID:** `MORPH-033` (assigned 2026-09-28, approved by researcher)
**Systematic-review record:** `CR000523`. Full-text triage: INCLUDE, reading priority HIGH, reading tier "2 — важно", `carries_complementarity_evidence = YES`. In this card we qualify that flag as *per-query win/loss counts and anecdotal topic analyses between lexical representations (and between IR models) only* (§10, §16). There is no document-level overlap, unique-hit or oracle-union evidence.
**Provenance:** AI-assisted deep dive (Claude). The paper (9 PDF pages = printed pp. 1616–1624) was read in full from the pdftotext extraction. Page images were checked for every table and every number block reported here: PDF p. 1 (= p. 1616: header, abstract, DOI, dates), p. 3 (= p. 1618: Tables 1–2), p. 4 (= p. 1619: Eqs. 1–5, evaluation protocol), p. 5 (= p. 1620: Table 3, additionally as a 250-dpi crop to read bold/italic/†/‡ marks), p. 7 (= p. 1622: Tables 4–5, additionally as a 250-dpi crop). Page references below are the journal's printed page numbers. Numbers computed by us are marked **[computed]** (recomputed with Python).
**Source rule:** **the paper is the primary and only authoritative source.** No code, website, later paper or background knowledge is used as evidence about what the authors did. Bibliographic check: a web search returned the Wiley Online Library record `onlinelibrary.wiley.com/doi/10.1002/asi.21093` titled "Algorithmic stemmers or morphological analysis? An evaluation – Fautsch – 2009 – Journal of the American Society for Information Science and Technology", consistent with the PDF (bibliographic check: Wiley Online Library search result). A direct Crossref lookup was refused by the proxy (HTTP 403), so volume/issue/pages are taken from the PDF's own running header and were not independently confirmed online; they are corroborated by the PDF metadata (Subject: "Journal of the American Society for Information Science and Technology 2009.60:1616-1624") and the Wiley download stamp ("15322890, 2009, 8") (verifier check).
**Reliability:** **A** (peer-reviewed journal article, *JASIST* 60(8), 2009, ASIS&T / Wiley).
**Verification:** independent AI verifier pass 2026-09-28; 8 findings addressed.

---

## Кратко для исследователя (RU)

- **Что сделано.** Классическое контролируемое сравнение способов нормализации словоформ **для английского языка** на англоязычных коллекциях CLEF 2001–2006 (169 477 газетных статей LA Times 1994 + Glasgow Herald 1995; 284 запроса T+D с экспертными оценками релевантности):
  - без стемминга (None), лёгкий S-стеммер (только множественное число), Porter, Lovins, SMART;
  - лемматизация (лемма из WordNet через JWNL после POS-разметки MXPOST; расширенную версию данных с этой разметкой предоставили организаторы Robust track CLEF 2008, авторы её не строили);
  - надстройки над леммой: лемма + часть речи (POS), лемма + номера синсетов WordNet, всё вместе;
  - списки стоп-слов: SMART (571 слово), без списка, короткий список из 9 слов.
  - Всё это прогнано на **пяти лексических моделях**: Okapi (BM25), DFR-PL2, DFR-I(ne)C2, языковая модель (Jelinek–Mercer), tf–idf. MAP по trec_eval (глубина 1000), бутстреп-тест, двусторонний, α = 5%.
- **Главные числа** (Table 3, p. 1620; средняя MAP по моделям):
  - None 0.4291; S-стеммер 0.4588 (+6.9%); Porter 0.4647 (+8.3%); Lovins 0.4503 (+4.9%); SMART 0.4685 (+9.2%); Lemma 0.4597 (+7.1%);
  - Okapi (BM25): None 0.4345 → S 0.4648, Porter 0.4706, SMART 0.4755, Lemma 0.4663.
  - S/Porter/SMART/Lemma значимо лучше None во всех пяти моделях; между собой (относительно SMART) незначимы; Lovins значимо хуже SMART во всех моделях.
- **Лемматизация не лучше лёгкого стемминга** в английском: 0.4597 vs 0.4588 (S) vs 0.4685 (SMART), различия незначимы. Авторы рекомендуют для английского S-стеммер.
- **POS и синсеты** (Table 4, p. 1622): лемма+POS даёт +1.5% (значимо в 4 из 5 моделей); добавление всех синсетов WordNet даёт −3.4% в среднем и значимо ухудшает Okapi, DFR-PL2, LM.
- **Стоп-слова** (Table 5, p. 1622): без списка стоп-слов Okapi падает с 0.4648 до 0.3403 (−26.8%), DFR-PL2 — на −30.1%; остальные три модели почти не меняются. Список из 9 слов ≈ список из 571 слова (−0.6%).
- **Анализ по запросам есть, но только в виде счётов «лучше/хуже» и примеров:**
  - S-стеммер лучше None на 159 запросах, хуже на 93 (модель не указана; для 32 запросов результат не сообщён **[computed]**);
  - примеры: стемминг помогает (Topic 306 «activities→activity», AP 0.333→1.0; Topic 63 «Antarctic/Antarctica», 0.0286→1.0) и вредит (Topic 180 «Barings→bare», 0.7652→0.0082; Topic 98, 1.0→0.5).
  - Это показывает, что эффект нормализации **разнонаправлен по запросам**, но нет пересечения найденных релевантных документов, уникальных находок, oracle union, объединения прогонов.
- **Чего нет:** плотного (dense) поиска, гибрида/fusion, n-грамм, overlap/unique hits, признаков запросов (кроме анекдотов), морфологически богатого языка. BM25 есть (Okapi), но k1/b не сообщены.
- **Внутренние несоответствия в статье:**
  - строка «Average» в Tables 3–5 — это среднее **четырёх** вероятностных моделей без tf–idf (совпадает до 4-го знака **[computed]**), а в тексте сказано «each of the five retrieval models» (p. 1620);
  - аннотация и заключение: синсеты «не меняют» качество, а Table 4 и текст p. 1622 — значимое ухудшение в трёх моделях;
  - текст: Lovins статистически не отличается от None, но в Table 3 у DFR-PL2/Lovins стоит † (значимо лучше None);
  - заключение: лемма значимо лучше Lovins — такой тест в таблицах не представлен (‡ только относительно SMART).
- **Для нашего gap:** работа подтверждает уже занятую границу («raw/stem/lemma ранее сравнивались», в т.ч. с BM25) для английского; ядро v0.8 (raw/stem/lemma BM25 × фиксированный D → overlap/unique hits → прирост гибрида) **не затрагивает**. Предложение: gap не менять.
- **Практическая польза для нас:**
  1. Конфигурацию стоп-слов BM25 фиксировать и сообщать явно: BM25 крайне чувствителен к её отсутствию.
  2. Условие «stem» нужно специфицировать (лёгкий vs агрессивный стеммер); ошибки агрессивного стемминга на именах собственных («Barings→bare») — кандидат в признаки запросов (named entities).
  3. Счёты win/tie/loss по запросам между вариантами — дешёвое дополнение к нашим document-level unique hits.

---

## 1. Bibliographic record

- **Authors:** Claire Fautsch, Jacques Savoy
- **Affiliation:** Computer Science Department, University of Neuchâtel, Switzerland (p. 1616)
- **Year:** 2009
- **Venue:** *Journal of the American Society for Information Science and Technology* (JASIST), 60(8), 1616–1624, August 2009 (running header / footer of every page)
- **Dates:** received January 28, 2009; revised March 16, 2009; accepted March 17, 2009; published online 6 May 2009 in Wiley InterScience (p. 1616 footnote)
- **Publisher:** ASIS&T / Wiley (© 2009 ASIS&T)
- **DOI:** `10.1002/asi.21093` (p. 1616; bibliographic check: Wiley Online Library search result)
- **Official record:** https://onlinelibrary.wiley.com/doi/10.1002/asi.21093
- **Funding:** Swiss NSF, Grant 200021–113273 (Acknowledgment, p. 1623)
- **Source type:** peer-reviewed journal article (full paper)
- **Reliability:** A
- **Full text available:** yes (`07_full_text/pdfs/CR000523.pdf`, 9 pages)

## 2. Why this work matters to the PhD

It is a **clean, peer-reviewed, statistically tested comparison of lexical representations** (none / light stem / aggressive stems / lemma / lemma+POS / lemma+synset) crossed with **five lexical retrieval models including Okapi BM25**, on a large human-judged query set (284). For our project it is a methodological and background reference for the *lexical-representation* axis only.

| Axis | Relation |
|---|---|
| Lexical retrieval | Direct: Okapi BM25, two DFR models, LM, tf–idf; stop-word variants |
| Semantic retrieval | Only in the old sense of WordNet synset codes added as index terms. **No dense / neural retrieval** |
| Hybrid retrieval | **Absent**: no run fusion; "Lemma, POS & Synset" is one combined index representation, not a fusion of retrieval channels |
| Uzbek morphology | Indirect only: English is morphologically poor; the authors themselves say gains are larger in richer languages (citing others) |
| Low-resource retrieval | None: English, large CLEF collection |
| Current gap | Supports already-listed non-claims (raw/stem/lemma already compared, with BM25). No effect on the morphology → complementarity core (§16) |

## 3. Research problem

### Simple explanation

When a query says "horses", should the system also find "horse"? One can cut word endings with simple rules (a *stemmer*) or look each word up in a dictionary to get its base form (*lemmatization*, "morphological analysis"). Lemmatization is more expensive. The authors ask whether it is worth it for English, whether the choice of stemmer matters, and whether extra linguistic information (part of speech, WordNet synonym-set codes) or stop-word lists change the picture, checking this across several retrieval models so that the conclusion does not depend on one model.

### Formal formulation

Four questions (p. 1617, verbatim ordering (a)–(d)):

- (a) "With a large set of queries (∼300), is suffixing really better than a nonstemming approach?"
- (b) "Is it possible to obtain improved retrieval effectiveness when applying a morphological analysis instead of an algorithmic stemmer?"
- (c) "Is it possible to obtain statistically significant differences between various algorithmic stemmers?"
- (d) "Does the use of thesaurus class numbers or simple POS information prove useful in increasing retrieval effectiveness?"

A fifth question, stop-word lists, is addressed in a separate section (p. 1622–1623) but not listed among (a)–(d).

Task: ad hoc document retrieval; for each query `q`, rank documents; effectiveness = MAP over 284 queries.

## 4. Main idea

### Simple explanation

Keep everything fixed (collection, queries, relevance judgments, retrieval model) and change only how words are normalized before indexing and querying. Repeat with five retrieval models. Test every difference with a bootstrap significance test, then look at individual queries where normalization helped or hurt to explain why.

### Concrete example (the paper's own)

- Topic 306 "ETA Activities in France" (DFR-I(ne)C2): without stemming AP = 0.333; with the S-stemmer AP = 1.0, because "activities" → "activity", and the single relevant document contains "activity" three times and "activities" twice (p. 1621).
- Topic 180 "Bankruptcy of Barings": with the SMART stemmer "Barings" is stemmed to "bare"; AP drops from 0.7652 (no stemming) to 0.0082 (p. 1621).
- Topic 98 "Films by the Kaurismäkis": the Lovins stemmer produces stems "ak" and "mik" from the names Aki and Mika, which match unrelated terms; AP 0.1429 (Lovins) vs 1.0 (SMART) (p. 1621).

### Formal method

- **Representations:** a word-normalization function `N ∈ {identity, S, Porter, Lovins, SMART, lemma}` applied to both documents and queries (p. 1620). Lemma variants: `lemma`, `lemma+POS` (term string concatenated with its POS tag, e.g. "alienJJ"), `lemma+synset` (all WordNet synset codes of an article or query added to its surrogate), and both (p. 1621–1622).
- **Models** (p. 1619):
  - tf–idf with cosine normalization, `idf_j = log(n/df_j)`;
  - Okapi / BM25 (Robertson, Walker & Beaulieu, 2000), **parameters NOT_REPORTED**;
  - DFR: `w_ij = −log2[Prob1_ij] · (1 − Prob2_ij)` (Eq. 1); I(ne)C2 with `tfn_ij = tf_ij · ln(1 + c·mean dl / l_i)`, `c = 1.5` ("fixed empirically"), `mean dl = 212` (Eq. 2); PL2 with Poisson `Prob1` and `Prob2 = tfn/(tfn+1)` (Eqs. 3–4);
  - LM (Hiemstra) with Jelinek–Mercer smoothing, `λ_j = 0.35` for all terms, `P(t_j|C) = df_j / lc` (Eq. 5).

## 5. Architecture / algorithm

1. **Collection and topics** (p. 1617–1618): CLEF 2001–2006 English collections, regrouped in the CLEF 2008 Robust track; topics 41–350 (310 topics), of which 26 without any relevant document were removed → 284.
2. **Queries:** title + description (T+D), "corresponding to the official query format in the CLEF evaluation campaigns" (p. 1618).
3. **Linguistic annotation** (p. 1618–1619): supplied by the organizers of the CLEF 2008 Robust track (to test whether WSD improves retrieval) as an "extended version of both documents and topic descriptions":
   - POS by MXPOST (maximum entropy tagger), Penn Treebank variant tag set;
   - lemma extracted with the Java WordNet Library (JWNL);
   - synsets (WordNet 1.6) assigned by the NUS-PT WSD system (the text writes "Vector Support Machine (VSM) approach trained with the SemCor corpus", presumably meaning an SVM; "SVM" is our reading), with a probability score per candidate synset.
   - "Not all of this information is introduced manually." (p. 1618). Lemmatizer/tagger/WSD accuracy on this collection: **NOT_REPORTED**.
4. **Stemmers** (p. 1617, 1620): S-stemmer (Harman 1991; three rules for the plural "-s"); Porter (about 60 suffixes); Lovins (over 260 suffixes); SMART (Salton 1971). Implementations/versions: NOT_REPORTED.
5. **Stop-words** (p. 1622): SMART list of 571 entries; no list; short list of nine words ("an," "and," "by," "for," "from," "of," "the," "to," "with") from the DIALOG search engine (Harter 1986).
   - Which stop-word list was used for the Table 3–4 runs is **not stated explicitly**. The Table 5 "SMART" column (S-stemmer + SMART list) is identical, cell by cell, to the Table 3 S-stemmer column **[checked on page images]**, so we infer that Table 3 (and presumably Table 4) used the SMART 571-word list **[inferred]**.
6. **Lemma+POS implementation ambiguity:** the text says "we increased the document score when lemma common to the query and the retrieved item had the same POS tag" and, in the next sentence, "for each indexing term a string composed of the term and its POS tag" was added (p. 1621–1622). Whether the POS-tagged term was added *alongside* or *instead of* the plain lemma is not fully explicit ("increased the document score" suggests alongside).
7. **Synset use:** "we added all synset numbers attached to an article or a query to its corresponding surrogate" (p. 1622). Whether the WSD probability scores were used (e.g., as weights or a threshold): NOT_REPORTED; the wording suggests all candidates were added.
8. **Retrieval and evaluation:** top 1,000 per query; MAP by trec_eval; paired bootstrap test (Savoy 1997), two-sided, α = 5% (p. 1619).

## 6. Data

- **Dataset/corpus:** CLEF 2001–2006 English ad hoc collections, "regrouped into the Robust track in CLEF 2008" (p. 1617).
- **Language:** English (American and British spellings, p. 1617).
- **Domain:** newspapers: *Los Angeles Times* 1994 and *Glasgow Herald* 1995.
- **Size:** 169,477 documents, ≈579 MB; each article ≈250 content-bearing terms on average (Mdn = 191) (p. 1617).
- **Per-campaign statistics** (Table 1, p. 1618, checked on page image):

| Year | Source | Size (MB) | Documents | Topics used | Topic range |
|---|---|---:|---:|---:|---|
| 2001 | LA Times | 425 | 113,005 | 47 | 41–90 |
| 2002 | LA Times | 425 | 113,005 | 42 | 91–140 |
| 2003 | LA Times + Glasgow Herald | 579 | 169,477 | 54 | 141–200 |
| 2004 | Glasgow Herald | 154 | 56,472 | 42 | 201–250 |
| 2005 | LA Times + Glasgow Herald | 579 | 169,477 | 50 | 251–300 |
| 2006 | LA Times + Glasgow Herald | 579 | 169,477 | 49 | 301–350 |

  - Sum of topics used = 284 **[computed ✓]**; 310 − 284 = 26 removed **[computed ✓]** (removed per year: 3 / 8 / 6 / 8 / 0 / 1 **[computed]** from the 50/50/60/50/50/50 topics in each range).
- **Queries:** 284 T+D topics.
- **Relevance judgments:** by CLEF human assessors (p. 1618); mean 22.46 relevant documents per topic (SD = 28.9, Mdn = 11.5), maximum 229 for Topic 254 "Earthquake Damage" (p. 1618). Graded or binary: NOT_REPORTED (MAP implies binary use).
- **Search scope per topic:** the text says "the entire corpus was not used during all the evaluation campaigns, and thus pertinent articles had to be searched in different parts of the corpus" (p. 1618). Whether each topic was run against its own year's sub-collection or all 284 topics against the full 169,477-document corpus is **not stated unambiguously**.
- **Train/dev/test:** no training; parameters `c = 1.5` "fixed empirically" and `λ = 0.35` fixed, with no separate tuning set described.

## 7. Baselines

| Baseline | What it is | Why selected | Fair comparison? |
|---|---|---|---|
| None (no stemming) | Surface word forms (after stop-word removal, presumably SMART list, §5) | Reference for questions (a), (b) | Yes: same models, queries, qrels |
| SMART stemmer | Stemmer of the SMART system | Best average; used as the ‡ baseline among stemmers | Yes |
| Lemma | WordNet/JWNL lemma after automatic POS tagging | Reference for POS/synset variants (Table 4) | Yes within the paper; but lemma quality is not measured, so "morphological analysis" here means *this* automatic pipeline |
| tf–idf | Classical vector-space model | Earlier stemming studies (Hull 1996, Voorhees 1993) used it | Yes, but it is much weaker (MAP ≈ 0.27–0.29) |
| Okapi, DFR-PL2, DFR-I(ne)C2, LM | Probabilistic models | "to ground our findings on a more solid basis" (p. 1619) | Parameters partly reported (DFR c, LM λ); BM25 k1/b NOT_REPORTED |
| SMART stop list (571 words) | Default in Table 5 | Reference for "None" and "Short" lists | Yes (S-stemmer fixed) |

## 8. Metrics

| Metric | Definition | Simple meaning | Appropriate? |
|---|---|---|---|
| AP (per query) | Mean of precision values at the ranks of each relevant document retrieved (top 1,000) | How early *all* relevant documents appear for one query | Yes for ad hoc retrieval with multiple relevant documents |
| MAP | Mean AP over the 284 queries | Overall ranking quality | Standard; each query weighted equally, so single-relevant-document topics (frequent in the paper's examples) can swing AP between 0 and 1 |
| % change | Relative change of the "Average" row vs its baseline column | Size of an effect | Computed on the four-model average, not per model (§9) |

Significance: paired bootstrap test (Savoy 1997), two-sided, α = 5% (p. 1619). No confidence intervals, no effect sizes beyond % change.

**Marking conventions in Tables 3–5** (p. 1620–1623, checked on page images):
- **bold** = best value in a column (i.e., best IR model for that representation);
- *italic* = significantly different from the bold value in the same column (IR-model comparison);
- † = significantly different from the row's baseline column: None (Table 3), Lemma (Table 4), SMART stop list (Table 5);
- ‡ = significantly different from the SMART stemmer in the same row (Table 3 only).

## 9. Results

### Table 3: MAP by IR model and word normalization, 284 T+D queries (p. 1620)

| Model | None | S-stemmer | Porter | Lovins | SMART | Lemma |
|---|---:|---:|---:|---:|---:|---:|
| Okapi | **0.4345** | 0.4648† | 0.4706† | 0.4560‡ | 0.4755† | 0.4663† |
| DFR-PL2 | *0.4251* | *0.4553*† | *0.4604*† | 0.4499†‡ | *0.4634*† | 0.4608† |
| DFR-I(ne)C2 | 0.4329 | **0.4658**† | **0.4721**† | **0.4565**‡ | **0.4783**† | **0.4671**† |
| LM | *0.4240* | *0.4493*† | *0.4555*† | *0.4389*‡ | *0.4568*† | *0.4444*† |
| tf–idf | *0.2669* | *0.2811*† | *0.2839*† | *0.2650*‡ | *0.2860*† | *0.2778*† |
| Average (printed) | 0.4291 | 0.4588 | 0.4647 | 0.4503 | 0.4685 | 0.4597 |
| % change (printed) | | +6.9 | +8.3 | +4.9 | +9.2 | +7.1 |

Reading the table:
- **Stemming/lemmatization vs none.** S, Porter, SMART and Lemma carry † in all five models. Lovins carries † only for DFR-PL2.
- **Stemmers vs SMART.** Only Lovins carries ‡ (all five models). S-stemmer, Porter and Lemma are **not** significantly different from SMART.
- **Lemma vs light stemming:** 0.4597 vs 0.4588 (S-stemmer), +0.0009 on the average **[computed]**; Lemma is below Porter (−0.0050) and SMART (−0.0088, −1.9% relative) **[computed]**. No lemma-vs-S or lemma-vs-Porter test is reported directly; the evidence for "no significant difference" is that neither is ‡ vs SMART.
- **Per-model relative change vs None [computed]:**

| Model | S | Porter | Lovins | SMART | Lemma |
|---|---:|---:|---:|---:|---:|
| Okapi | +7.0% | +8.3% | +4.9% | +9.4% | +7.3% |
| DFR-PL2 | +7.1% | +8.3% | +5.8% | +9.0% | +8.4% |
| DFR-I(ne)C2 | +7.6% | +9.1% | +5.5% | +10.5% | +7.9% |
| LM | +6.0% | +7.4% | +3.5% | +7.7% | +4.8% |
| tf–idf | +5.3% | +6.4% | −0.7% | +7.2% | +4.1% |

  Lemma helps LM and tf–idf less than the light S-stemmer does (+4.8 / +4.1% vs +6.0 / +5.3%).
- **IR models.** DFR-I(ne)C2 is best in every column except None, where Okapi is best (0.4345 vs 0.4329). Okapi is never italic: "the MAP differences between Okapi and DFR-I(ne)C2 are never statistically significant" (p. 1620); their MAP differs by at most 0.0028 **[computed]**. LM and tf–idf are italic in every column.
- **The "Average" row is the mean of the four probabilistic models only (tf–idf excluded)** **[computed]**: four-model means 0.4291 / 0.4588 / 0.4646(5) / 0.4503 / 0.4685 / 0.4596(5) reproduce the printed row; five-model means would be 0.3967 / 0.4233 / 0.4285 / 0.4133 / 0.4320 / 0.4233 (% change +6.7 / +8.0 / +4.2 / +8.9 / +6.7). The text states "we computed the average performance achieved by each of the five retrieval models" (p. 1620). See §19. The printed % changes are correct relative to the printed averages **[computed: 6.92, 8.30, 4.94, 9.18, 7.13 ✓]**.

### Per-query counts reported in the text

| Comparison | Better | Worse | Same | Location |
|---|---:|---:|---:|---|
| DFR-I(ne)C2 vs tf–idf (normalization condition not stated) | 245 | 27 | 12 | p. 1620 |
| S-stemmer vs None (IR model not stated) | 159 | 93 | NOT_REPORTED (284 − 252 = 32 **[computed]**) | p. 1620 |
| Lemma & POS vs Lemma (DFR-I(ne)C2) | 138 | 98 | 48 | p. 1622 |
| SMART stop list vs no list (Okapi, S-stemmer) | 223 | 37 | 24 | p. 1623 |

Sums: 245+27+12 = 284; 138+98+48 = 284; 223+37+24 = 284 **[computed ✓]**.

### Topic-level examples (AP), all from the text

| Topic | Comparison | AP | Explanation given | Page |
|---|---|---|---|---|
| 62 "Northern Japan Earthquake" | DFR-I(ne)C2 vs tf–idf | 1.0 vs 0.0062 | tf–idf favours documents with one query term of very high tf ("Japan" tf = 125 / 85); the relevant document is rank 1 vs rank 213 | 1620 |
| 306 "ETA Activities in France" | None → S-stemmer (DFR-I(ne)C2) | 0.333 → 1.0 | "activities" → "activity" | 1621 |
| 98 "Films by the Kaurismäkis" | None → S-stemmer | 1.0 → 0.5 | "films"/"film" conflation lets a non-relevant document overtake | 1621 |
| 180 "Bankruptcy of Barings" | None → SMART (DFR-I(ne)C2) | 0.7652 → 0.0082 | "Barings" → "bare" (over-stemming of a proper name) | 1621 |
| 63 "Whale Reserve" | None → SMART | 0.0286 → 1.0 (rank 35 → 1) | "Antarctic" → "antarct" matches "Antarctica" | 1621 |
| 198 "Honorary Oscar for Italian Directors" | None → SMART (Okapi) | 0.5 → 1.0 | "Honorary" → "honor", "awarded" → "award" | 1621 |
| 98 (again) | Lovins vs SMART | 0.1429 vs 1.0 | Lovins stems "ak", "mik" too short, match unrelated terms | 1621 |
| 231 "New Portuguese Prime Minister" | Lovins vs SMART | 1.0 vs 0.5 | Lovins conflates "elections" with "electoral" | 1621 |
| 217 "AIDS in Africa" | Lemma → Lemma & POS (DFR-I(ne)C2) | 0.1944 → 0.5526 | "AIDS" → "aid"; the proper-noun tag separates it from "aid"/"aids" | 1622 |
| 76 "Solar Energy" | Lemma → Lemma & Synset (Okapi) | 0.663 → 0.0722 | lemma "be" has 10 synsets, added to the query with frequency 3 | 1622 |
| 136 "Leaning Tower of Pisa" | SMART list vs no list (Okapi) | 1.0 vs 0.0 | many stop words rank non-relevant documents higher | 1623 |
| 104 "Super G Gold medal" | no list vs stop list (Okapi) | 0.6550 vs 0.4525 | "G" is in the stop list and is removed | 1623 |

### Table 4: MAP by IR model and morphological-analysis variant (p. 1622)

| Model | Lemma | Lemma & POS | Lemma & Synset | Lemma, POS & Synset |
|---|---:|---:|---:|---:|
| Okapi | 0.4663 | 0.4720† | *0.4395*† | *0.4482*† |
| DFR-PL2 | 0.4608 | *0.4634* | *0.4365*† | *0.4433*† |
| DFR-I(ne)C2 | **0.4671** | **0.4740**† | **0.4665** | **0.4705** |
| LM | *0.4444* | *0.4562*† | *0.4342*† | *0.4458* |
| tf–idf | *0.2778* | *0.2879*† | *0.2834* | *0.2888*† |
| Average (printed) | 0.4597 | 0.4664 | 0.4442 | 0.4520 |
| % change (printed) | | +1.5 | −3.4 | −1.7 |

- Averages again equal the four-model means (0.4597 / 0.4664 / 0.4442 / 0.4520) **[computed ✓]**; % changes +1.46 / −3.37 / −1.68 **[computed ✓]**.
- Lemma & POS: † (significant gain) for Okapi, DFR-I(ne)C2, LM, tf–idf; not DFR-PL2 (+0.6%) **[computed per-model: +1.2, +0.6, +1.5, +2.7, +3.6%]**.
- Lemma & Synset: significant **decreases** for Okapi (−5.7%), DFR-PL2 (−5.3%), LM (−2.3%) **[computed]**; DFR-I(ne)C2 −0.1% and tf–idf +2.0% not significant.
- All three: significant decrease for Okapi (−3.9%) and DFR-PL2 (−3.8%), significant increase for tf–idf (+4.0%) **[computed]**.
- DFR-I(ne)C2 is barely affected by synsets (0.4671 → 0.4665 / 0.4705). The models most sensitive to synsets (Okapi, DFR-PL2; LM also drops significantly, but only −2.3%) are the same ones sensitive to missing stop-words (Table 5), which is consistent with the authors' Topic 76 explanation (a very frequent lemma, "be", expanded into 10 codes). This link is our observation, not the authors'.

### Table 5: MAP by stop-word list, S-stemmer (p. 1622)

| Model | SMART list (571) | None | Short (9 words) |
|---|---:|---:|---:|
| Okapi | 0.4648 | *0.3403*† | 0.4581 |
| DFR-PL2 | *0.4553* | *0.3185*† | *0.4526* |
| DFR-I(ne)C2 | **0.4658** | **0.4661** | **0.4665** |
| LM | *0.4493* | *0.4433* | *0.4462* |
| tf–idf | *0.2811* | *0.2831* | *0.2830* |
| Average (printed) | 0.4588 | 0.3921 | 0.4559 |
| % change (printed) | | −14.5 | −0.6 |

- Per-model change without a stop list **[computed]**: Okapi −26.8%, DFR-PL2 −30.0% (−30.05% from the printed MAPs; text: "−26.8%" and "−30.1%", p. 1622; the 0.1-point gap is a rounding difference, presumably from unrounded MAPs); DFR-I(ne)C2 +0.1%, LM −1.3%, tf–idf +0.7% (text: "small (∼1%)").
- Short list vs SMART list: −1.4 / −0.6 / +0.2 / −0.7 / +0.7% **[computed]**; none significant (no †).
- Averages again four-model means (0.3921 / 0.4559) **[computed ✓]**.
- The Short-vs-None difference is **not** tested in the table (both are tested against SMART only), although the abstract claims that "including a stop word list, even one containing only around 10 terms, might significantly improve retrieval performance, depending on the IR model".

## 10. Statistical evidence

- **Significance test:** paired bootstrap (Savoy 1997), two-sided, α = 5% (p. 1619). Applied to: IR model vs best model in each column (italics), each representation vs its baseline column (†), each stemmer vs SMART (‡). p-values: NOT_REPORTED.
- **Multiple-comparison correction:** NOT_REPORTED (many pairwise tests across 5 models × 6 + 4 + 3 conditions).
- **Confidence intervals:** NOT_REPORTED.
- **Runs / seeds:** not applicable (deterministic lexical runs); one run per condition.
- **Equivalence testing:** none. "No significant difference" between stemmers and lemma is interpreted as similar performance; no equivalence margin or power analysis is reported.
- **Ablation:** the design is itself a factorial-style comparison of representation × IR model, plus a stop-word ablation for the S-stemmer only. Not ablated: stop-words for other stemmers/lemma; query length (T only vs T+D); BM25 parameters.
- **Per-query analysis:** **partial.** Win/loss/tie counts for four pairwise comparisons (table in §9) and twelve topic-level anecdotes. There is:
  - no per-query distribution plot or table;
  - no document-level overlap, unique relevant documents or oracle union between representations;
  - no fusion of representations (e.g., raw + stem runs);
  - no systematic query-feature analysis (query length, named entities, part of speech are mentioned only in examples).

## 11. Strengths

- Large human-judged query set (284) for its time, explicitly motivated by earlier small-sample stemming studies (p. 1617).
- Five retrieval models, including Okapi BM25, two DFR models and an LM, so that conclusions are not tied to tf–idf (the authors' stated aim, p. 1619).
- Differences against defined baselines (None, SMART, Lemma, SMART stop list, and the best IR model per column) are tested with a bootstrap test; marking conventions are explained. Not every pairwise difference is tested (e.g., Lemma vs S-stemmer, Short vs no stop list).
- Morphological analysis is compared with four stemmers of different aggressiveness in one setting.
- Error analysis with concrete topics explains *why* normalization helps or hurts (over-stemming of proper names, too-short stems, cross-POS conflation, frequent-lemma synset explosion).
- Stop-word sensitivity is quantified per model, which is directly practical for BM25 configurations.

## 12. Limitations

### Stated by the authors

- Findings hold "at least for the English language" (p. 1623); the authors note stemming gains are larger in morphologically richer languages, citing Tomlinson (2004) and Kettunen (2007) (p. 1623). These cited figures are other authors' results, not evidence of this paper.
- The synset result holds "at least as implemented in this article" (p. 1623).
- Stop-word lists "were developed on the basis of certain arbitrary decisions (Fox, 1990)" (p. 1623).
- The ≈7% gain is stated "For medium-sized queries" (p. 1623), i.e. T+D queries.
- User-oriented argument: a light stemmer "is better understood" than an aggressive one (p. 1623); this is an opinion, not tested.

### Inferred from the experimental design

1. **English only.** English inflection is limited; the magnitude of the stemming and lemma effects, and the stem ≈ lemma result, do not transfer to agglutinative languages without new evidence.
2. **Lemmatizer quality not measured.** "Morphological analysis" is an automatic MXPOST + JWNL pipeline supplied by CLEF organizers; its accuracy on this corpus is NOT_REPORTED. "Lemma ≈ stem" is therefore a statement about this pipeline, not about lemmatization in general.
3. **BM25 parameters NOT_REPORTED;** DFR `c = 1.5` "fixed empirically", with no separate tuning set, so it may have been set on the same collection.
4. **Stop-word confound partly undocumented.** The stop list used for Tables 3–4 is inferred (SMART 571) rather than stated; the stop-word study covers only the S-stemmer, so the interaction of stop-words with other stemmers/lemma is unknown.
5. **Non-significance read as equivalence,** with no correction for multiple comparisons and no confidence intervals.
6. **Averages exclude tf–idf while the text says five models** (§9, §19). The headline % changes are therefore four-model figures.
7. **Only T+D queries.** Short (title-only) queries, where normalization effects may differ, are not tested.
8. **Search scope per topic ambiguous** (full 169,477-document corpus vs year-specific sub-collections, §6).
9. **Per-query evidence is counts and anecdotes;** the IR model for the 159/93 count and the representation for the 245/27/12 count are not stated.
10. **No document-level complementarity:** no analysis of which relevant documents each representation finds.

## 13. What the work proves

- On 284 English CLEF T+D queries, **S-stemmer, Porter, SMART and WordNet-based lemmatization each significantly improve MAP over no stemming in all five tested models**, including Okapi BM25 (Table 3). The four-model average gains are +6.9 to +9.2%; for Okapi, +7.0 to +9.4% **[computed]**.
- **The Lovins stemmer is significantly worse than SMART in all five models** and not significantly better than no stemming in four of five (Table 3).
- **Automatic lemmatization is not significantly better than light or standard stemming** in this English setting: none of S, Porter, Lemma differ significantly from SMART; Lemma ≈ S-stemmer on average (0.4597 vs 0.4588). Lemma vs S-stemmer and Lemma vs Porter are not tested directly; the "no significant differences" conclusion (p. 1621) rests on the tests against SMART.
- **Adding POS tags to lemmas gives a small but mostly significant gain** (+1.5% average; significant in 4 of 5 models) (Table 4).
- **Adding all WordNet synset codes lowers MAP on average (−3.4%) and significantly for Okapi, DFR-PL2 and LM** (Table 4), contrary to the abstract's wording (§19).
- **Okapi and DFR-PL2 are highly sensitive to the absence of stop-word removal** (−26.8%, −30.1%); a 9-word list performs statistically like a 571-word list (Table 5).
- **Normalization effects are bidirectional across queries:** e.g., S-stemmer vs None 159 better / 93 worse (p. 1620), with documented failure types (proper-name over-stemming, too-short stems).
- DFR-I(ne)C2 and Okapi perform at the same level in Table 3 (never significantly different, p. 1620). DFR-I(ne)C2 is significantly better than LM and tf–idf in every column of Tables 3–5 where it is the bold reference (all columns except Table 3 "None", where Okapi is bold). Okapi vs LM is tested directly only where Okapi is bold (Table 3, None column); without a stop list Okapi (0.3403) falls far below LM (0.4433) (Table 5). The authors' conclusion states that the probabilistic models "perform significantly better than did the tf–idf approach" (p. 1623).

## 14. What the work does NOT prove

- **Anything about morphologically rich or agglutinative languages** (Uzbek, Turkish, Finnish). English only.
- **That lemmatization and stemming are equivalent in general.** Only non-significance for one automatic WordNet-based pipeline; no equivalence test, no lemmatizer accuracy.
- **That BM25 in a standard configuration behaves as reported here:** k1/b are not reported.
- **Anything about dense/neural retrieval, hybrid retrieval or fusion.** None were tested; WordNet synsets are not semantic retrieval in the modern sense.
- **Lexical–semantic complementarity, or complementarity between representations at the document level.** The win/loss counts show that different representations succeed on different queries, but not which relevant documents are found only by one of them, nor what an oracle union or a fusion would gain.
- **Which query characteristics predict when normalization helps.** Only anecdotes.
- **That short stop lists are significantly better than none:** that comparison is not tested directly.
- **That the synset approach is useless in general:** only "add all synset codes" was tested.

## 15. Relationship to current Uzbek evidence

- **No Uzbek data**; English (Indo-European, weak inflection) vs Uzbek (Turkic, agglutinative). Transfer is methodological, not numerical.
- The paper sits in the classical CLEF lexical-normalization cluster already in our cards:
  - Hollink et al. 2004 (`CR000338`): multi-language stem/lemma/n-gram comparison;
  - Kettunen et al. 2005 (`CR000452`): Finnish stem vs lemma, per-topic divergence under equal means;
  - Airio 2006 (`CR000491`): word normalization and decompounding.
  Fautsch & Savoy add the English end of the spectrum: with weak morphology, stem ≈ lemma and gains are modest (+7–9%).
- Consistent with Can et al. 2008 (MORPH-001, Turkish): an elaborate lemmatizer does not guarantee superiority over simpler conflation. Both works support "measure, do not assume `lemma > stem > raw`".
- Consistent with Haddad & Bechikh Ali 2014 (MORPH-002, Turkish, BM25): preprocessing effects depend on the retrieval model; here the stop-word effect is model-dependent (large for Okapi/PL2, negligible for I(ne)C2/LM/tf–idf).
- Uzbek WordNet (UZWORDNET, UZ-SEM-002) exists; this paper is a caution that naive "add all synsets" indexing can hurt BM25 (Table 4). This is outside our v0.8 core.

## 16. Relationship to CURRENT_GAP

**Classification:** *supports (existing boundary)* + *no material effect on the residual core*.

- **Supports / confirms as occupied** the non-claims already listed in v0.8:
  - "raw/stem/lemma ранее не сравнивались" — they were, here even with BM25 and four other lexical models, in English (and in low-resource languages per UPERF, Urdu);
  - "query-type analysis lexical … — новая идея" — the paper already explains per-query normalization effects by query properties (proper names, POS), anecdotally.
- **Relevant supporting observation:** the bidirectional per-query effect (159 better / 93 worse for S-stemmer vs None) is classical evidence that changing the lexical representation **changes which queries the lexical channel succeeds on**. This is the premise behind our question of whether it also changes *which relevant documents remain unique* relative to a dense retriever. The paper does not measure the latter.
- **No material effect on the residual core** of v0.8 refined:
  - no fixed dense retriever D;
  - no unique relevant hits / overlap / oracle union;
  - no hybrid gain;
  - no systematic query-feature link.
- The triage flag `carries_complementarity_evidence = YES` should be read as *query-level win/loss between lexical variants only*.

**Proposal:** keep v0.8 refined unchanged. Optionally cite as the English, BM25-inclusive classical baseline for the "raw/stem/lemma already compared" boundary. This is a proposal only; `CURRENT_GAP.md` has not been edited.

## 17. Implications for our research design

- **Morphology preprocessing — define "stem" precisely.** The paper shows light vs aggressive stemming can differ significantly (Lovins vs SMART) while light ≈ lemma. For Uzbek, the `BM25_stem` condition must name the stemmer and its aggressiveness (inflection-only vs inflection + derivation). A light inflectional-suffix stripper could serve as the `BM25_simple-normalization` control already foreseen in CURRENT_GAP.
- **Stop-words must be fixed and reported for every BM25 variant.** BM25 lost 26.8% MAP without a stop list here. For our raw/stem/lemma comparison, the stop list (none / short Uzbek list / full list) must be identical across variants and applied at the same pipeline stage (before or after normalization), otherwise the stop-list effect can be confounded with the morphology effect. A small sensitivity check (none vs short list) on the pilot is cheap.
- **Lemmatizer quality must be reported.** Unlike this paper, report the Uzbek lemmatizer's coverage/ambiguity on our corpus (e.g., share of tokens with an analysis, share of ambiguous analyses), so that "lemma ≈ stem" or "lemma > stem" can be interpreted.
- **Query taxonomy.** The failure types documented here are candidate query features, already partly in our list:
  - proper names / named entities that a stemmer over-conflates ("Barings" → "bare");
  - very short stems that collide with unrelated words (Lovins "ak", "mik");
  - cross-POS conflation that helps or hurts ("elections"/"electoral");
  - acronyms colliding with common words ("AIDS" → "aid").
  For Uzbek, suffix-like endings of personal and place names are a direct analogue to test per query.
- **Per-query reporting.** Report win/tie/loss counts between `BM25_raw`, `BM25_stem`, `BM25_lemma` (cheap, comparable with this classical literature), **in addition to** our document-level unique hits, overlap and oracle union, which this paper lacks.
- **Statistics.** Use a paired bootstrap or randomization test as here, but add multiple-comparison control and confidence intervals, and do not read non-significance as equivalence.
- **Robustness across lexical models (optional, secondary).** The paper's lesson that effects can be model-dependent suggests one secondary lexical model (e.g., an LM or DFR run) as a robustness check of the raw/stem/lemma effect. The primary design should stay BM25 × fixed D.
- **Reporting hygiene.** State exactly which runs enter every average (this paper's averages silently exclude tf–idf).
- **Hypothesis.** No direct evidence for or against. It supports expecting heterogeneous per-query normalization effects, which is the precondition for a morphology-induced change in lexical–dense complementarity.

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| Stemming (algorithmic) | Cutting word endings by rules, e.g. "activities" → "activ"/"activity" | Rule-based suffix removal mapping word forms to a (possibly non-word) stem |
| Light stemmer (S-stemmer) | Only removes plural "-s" | Three rules for English plural (Harman 1991) |
| Aggressive stemmer (Lovins) | Removes many endings, including derivational ones; can over-conflate | ≈260+ suffixes, longest-match removal |
| Over-/under-stemming | Merging unrelated words / failing to merge related ones | Conflation errors (e.g., "organization" → "organ"; "European" ≠ "Europe") |
| Lemmatization (morphological analysis) | Replacing a word with its dictionary form | Mapping a token to its lemma, usually using POS and a lexicon (here WordNet via JWNL) |
| POS tag | Word class label: noun, verb, adjective, proper noun | Penn Treebank tags (NN, NNP, JJ, …) |
| Synset (WordNet) | A group of synonyms with one ID code | WordNet 1.6 synonym-set identifier; a word can belong to several |
| Word-sense disambiguation (WSD) | Choosing which meaning of a word is used in context | Assigning a synset (with probability) to each token |
| Stop-word list | Very frequent words ignored during indexing | Terms removed from index and queries |
| Okapi BM25 | Word-matching ranking with saturation of term frequency and length normalization | Probabilistic relevance framework scoring with parameters k1, b |
| DFR (Divergence from Randomness) | Scores a term by how much its frequency in a document deviates from chance | `w = −log2 Prob1 · (1 − Prob2)`; variants I(ne)C2, PL2 |
| Language model (Jelinek–Mercer) | Probability that the document "generates" the query, mixed with collection probabilities | `P(t|d)` smoothed with `P(t|C)`, λ = 0.35 |
| MAP | Average of per-query average precision | Mean over queries of AP@1000 |
| Bootstrap test | Resampling queries to see if a difference could be chance | Paired, two-sided, α = 5% (Savoy 1997) |
| Complementarity (project term) | Each channel finds some relevant documents the other misses | Unique relevant hits, overlap, oracle-union gain |

## 19. Open questions / verification needed

1. **"Average" rows:** text says five models (p. 1620), tables reproduce four-model means (tf–idf excluded) in Tables 3, 4 and 5 **[computed]**. Quote the % changes as four-model averages.
2. **Synsets — abstract/conclusion vs Table 4:** the abstract says thesaurus class numbers "does not modify overall retrieval performances" and the conclusion says they do "not significantly modify mean retrieval performance" (p. 1623), while Table 4 marks significant decreases for Okapi, DFR-PL2 and LM and the text says "For the three IR models, the differences were even statistically significant" (p. 1622). Cite the table, not the abstract.
3. **Lovins vs None:** text says Lovins "tended to produce retrieval performances that were statistically similar to a nonstemming approach" (p. 1621); Table 3 shows † for DFR-PL2/Lovins (0.4499 vs 0.4251).
4. **Lemma vs Lovins:** the conclusion says retrieval performance of the morphological analysis (or of the group of good stemmers) "is significantly better than a nonstemming approach or the Lovins' stemmer" (p. 1623); only SMART vs Lovins (‡) is reported as tested.
5. **Proper nouns and synsets:** the text says proper nouns get no synset (p. 1618), but the Table 2 example shows NNP-tagged "Northern" and "Japan" with synset codes; the text also refers to "our example with the word 'whale'", which is not in Table 2 (example C062). Minor.
6. **Document length:** ≈250 content-bearing terms per article (Mdn 191, p. 1617) vs `mean dl = 212` in the DFR formula (p. 1619). Possibly different counting (after stemming/stop-words); not explained.
7. **Stop list used for Tables 3–4:** inferred SMART 571 from identical values; not stated.
8. **BM25 k1/b, stemmer implementations, and search scope per topic (full corpus vs year sub-collection):** NOT_REPORTED / ambiguous.
9. **IR model behind the 159/93 count and representation behind the 245/27/12 count:** not stated.
10. Minor wording: under the Lemma condition the text says "the stemming converted 'AIDS' into 'aid'" (p. 1622); the NUS-PT classifier is called "Vector Support Machine (VSM)" (p. 1619).

## 20. Decision after deep dive

- **Keep current gap?** Yes. v0.8 refined remains valid; see §16.
- **Modify gap?** No change proposed. Optionally add this paper to the evidence boundary as the classical English, BM25-inclusive example of "raw/stem/lemma already compared" (researcher's decision).
- **Add decision?** Proposed for `decisions/DECISIONS.md` (researcher's decision):
  - "The stop-word configuration (list, stage in the pipeline) is fixed, identical and reported for all BM25 variants; run a none-vs-short-list sensitivity check on the pilot";
  - "The `BM25_stem` condition names the stemmer and its aggressiveness; report lemmatizer coverage/ambiguity on the corpus";
  - "Report per-query win/tie/loss counts between lexical variants alongside document-level unique hits".
- **Add experiment?** Optional, low cost: on the Uzbek pilot, stop-list sensitivity (none / short / full) for `BM25_raw` and `BM25_lemma`, to ensure the stop-list choice does not drive the raw → lemma difference.
- **Add citation to Chapter I?** Yes, §1.1 (theoretical foundations of lexical retrieval): classical evidence that in English stemming gives ≈+7–9% MAP across BM25/DFR/LM, that lemmatization is not better than light stemming, that stop-word handling strongly affects BM25, and that normalization effects vary per query. Use it with the explicit caveat that English is morphologically poor.
- **Proposed `MASTER_INDEX.md` row** (to add after approval):

| MORPH-033 | Fautsch & Savoy — *Algorithmic Stemmers or Morphological Analysis? An Evaluation* (*JASIST* 60(8), 1616–1624) — [deep dive](deep-dives/2009_Fautsch_Savoy_Algorithmic_Stemmers_or_Morphological_Analysis.md) | 2009 | A | MEDIUM | English CLEF 2001–2006 (169,477 news docs, 284 T+D queries, human qrels), 5 lexical models incl. Okapi BM25: none vs S/Porter/Lovins/SMART stemmers vs WordNet lemma (+POS, +synsets), stop-list variants; bootstrap tests. Four-model avg MAP none 0.4291 → S 0.4588 / Porter 0.4647 / SMART 0.4685 / lemma 0.4597 (all significant vs none; not significantly different from each other); Lovins significantly worse than SMART; synsets −3.4% (significant for 3 models); BM25 −26.8% without stop list. Per-query win/loss (S vs none 159/93) and topic anecdotes only. No dense, no fusion, no overlap/unique-hit analysis. "Average" rows exclude tf–idf despite text saying five models. |
