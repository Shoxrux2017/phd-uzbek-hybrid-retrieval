# Khaltar & Fujii (2008): A Lemmatization Method for Modern Mongolian and its Application to Information Retrieval

**Targeted deep-dive status:** COMPLETED (AI-assisted, pending researcher review)
**Completed:** 2026-09-28
**Verification:** independent AI verifier pass 2026-09-28; 7 findings addressed.
**Literature ID:** `MORPH-036` (assigned 2026-09-28, approved by researcher)
**Systematic-review record:** `CR000251`. Full-text triage: INCLUDE, reading priority HIGH, reading tier 2 ("важно"), `carries_complementarity_evidence = NO`. Triage note: relevance derived from author keywords (automatic judgments); queries with AP = 0 for all methods discarded; results reported separately for keyword vs list queries (query formulation, not a per-query breakdown).
**Provenance:** AI-assisted deep dive (Claude). The whole paper (8 pages, ACL two-column; printed page numbers 1–8, local to the paper, so "p. N" below means printed page N) was read from the text extraction and from page images. **Pages checked visually (110 dpi):** p. 1 (abstract, Sec. 1–2, Figure 1), p. 5 (Figures 5–6, Sec. 4.7–5.2), p. 6 (Table 1, Figure 7, Sec. 5.3), p. 7 (Figure 8, Table 2, Table 3, Sec. 6). Every table value below was compared with the page image. Numbers computed by us are marked **[computed]** and were recomputed with Python.
**Source rule:** **the paper is the primary and only authoritative source** for what the authors did and found. The web was used only to check the bibliographic record (ACL Anthology). Background knowledge appears only in lines marked "Context (not from the paper)".
**Reliability:** **B** — peer-reviewed main-conference paper (IJCNLP 2008, ACL Anthology `I08-1001`), but the IR experiment is a secondary section: automatically derived relevance (author keywords), 1,102 short abstracts, BM25 parameters and query processing not reported, one collection, one run per condition.

---

## Кратко для исследователя (RU)

- **Что сделано.** Для современного монгольского (кириллица, агглютинативный суффиксальный язык) предложен **словарно-правиловой лемматизатор**: словарь 126 глагольных суффиксов + 179 правил сегментации, 35 именных суффиксов + 196 правил (из них 23 новых для заимствований на «-аци/-яци/-ологи»), 12 правил вставки выпавшей гласной, словарь из 1 254 глаголов; словаря существительных нет (Sec. 4, pp. 3–5).
- **Две оценки:** (1) точность лемматизации на 15 478 типах словоформ, размеченных двумя асессорами (κ = 0.96); (2) эффект в **Okapi BM25** на коллекции из 1 102 технических аннотаций (Sec. 5, pp. 5–7).
- **Варианты лексического представления в BM25 (Table 2, p. 7, MAP):** без лемматизации / лемматизатор Sanduijav et al. (2005) / Khaltar et al. (2006) / предложенный метод / **«правильная» (ручная) лемматизация** как верхняя граница (в Sec. 5.3 не описана; что это ответы асессоров из Sec. 5.2 — наш вывод). **Стемминга нет** (хотя во введении он определён).
- **Главные числа (MAP, keyword queries KQ / list queries LQ):** без лемматизации 0.2312 / 0.2766; Sanduijav 0.2882 / 0.2834; Khaltar 2006 0.3134 / 0.3127; предложенный 0.3149 / 0.3114; ручная 0.3268 / 0.3187.
  - Прирост предложенного метода над raw: +0.0837 (+36.2%) для KQ и +0.0348 (+12.6%) для LQ **[computed]**.
  - Метод получает ~88% (KQ) и ~83% (LQ) прироста, доступного при ручной лемматизации **[computed]**.
- **Предложенный метод ≈ своему предшественнику Khaltar 2006 в поиске:** разница не значима ни для KQ, ни для LQ (Table 3, p. 7), а для LQ численно ниже (0.3114 vs 0.3127). Рост точности лемматизации на +5.9 п.п. (72.3 → 78.2%, Table 1) почти не отразился на MAP (+0.0015 KQ) **[computed]**. Вывод «улучшили точность поиска» (Sec. 6) верен относительно raw, но не относительно Khaltar 2006.
- **Форма запроса модулирует эффект морфологии:** для коротких запросов (одно ключевое слово) выигрыш лемматизации примерно в 2.4 раза больше по абсолютной MAP, чем для длинных (список ключевых слов ≈ 6.1 слова) **[computed]**; для LQ разница raw vs Sanduijav не значима. Это агрегатное сравнение двух наборов запросов, а не анализ по отдельным запросам.
- **Статистика:** парный t-test (уровни 5% / 1%), только знаки «<», «<<», «―», без p-значений; доверительных интервалов, анализа по запросам, перекрытия результатов нет.
- **Чего нет (измерения нашего gap):** плотного/нейросетевого поиска нет; гибрида/fusion нет; перекрытия, уникально найденных релевантных документов и oracle union между вариантами нет; признаков запросов нет (кроме деления KQ/LQ). Параметры BM25 (k1, b), обработка запросов, стоп-слова — NOT_REPORTED.
- **Внутреннее несоответствие:** строка «Total» в Table 1 (63.2 / 72.3 / 78.2%) не воспроизводится как среднее по строкам, взвешенное числом типов (у нас 54.7 / 80.1 / 84.2%) **[computed]**; сумма ошибок в Figure 7 (2 154) не совпадает ни с 3 374 (из 78.2%), ни с 2 442 (из взвешенного среднего) **[computed]**.
- **Для нашего gap:** работа подтверждает уже занятую позицию «raw vs lemma в BM25 для агглютинативного языка сравнивали» и даёт полезный приём — **ручная (gold) лемматизация как верхняя граница**. Ядро v0.8 (raw/stem/lemma × фиксированная D → overlap/unique hits → прирост гибрида) не затрагивает. Предложение: gap не менять.
- **Практическая польза:** (1) точность морфоанализатора ≠ эффективность поиска — нужна отдельная оценка в поиске; (2) gold-лемматизация небольшого подмножества отделяет «ошибки лемматизатора» от «эффекта представления»; (3) длина/форма запроса — кандидат-модератор эффекта морфологии; (4) правила для заимствований в кириллице (русские/западные слова) — аналогичная проблема есть в узбекском.

---

## 1. Bibliographic record

- **Authors:** Badam-Osor Khaltar, Atsushi Fujii
- **Affiliation (as printed, p. 1):** Graduate School of Library, Information and Media Studies, University of Tsukuba, Japan
- **Year:** 2008
- **Venue:** *Proceedings of the Third International Joint Conference on Natural Language Processing: Volume-I* (IJCNLP 2008) (bibliographic check: ACL Anthology record and BibTeX, https://aclanthology.org/I08-1001/)
- **ACL Anthology ID:** `I08-1001`
- **DOI:** none listed in the ACL Anthology record (bibliographic check: ACL Anthology)
- **Pages:** the Anthology record lists no page range; the PDF carries local page numbers 1–8. Proceedings page range: **not verified**.
- **Conference place/date:** not given in the Anthology record; **not verified**.
- **Official URL:** https://aclanthology.org/I08-1001/
- **Source type:** peer-reviewed conference paper (main volume)
- **Reliability:** B (see header)
- **Full text available:** yes (`07_full_text/pdfs/CR000251.pdf`, 8 pages)

## 2. Why this work matters to the PhD

An early, controlled **raw vs lemma** comparison inside **Okapi BM25** for an agglutinative, suffixing, Cyrillic-script language, with an explicit **gold-lemmatization upper bound** and significance tests.

| Axis | Relation |
|---|---|
| Lexical retrieval | Direct: Okapi BM25 with five index-term representations (raw, three automatic lemmatizers, manual lemmatization) |
| Semantic retrieval | **Absent** |
| Hybrid retrieval | **Absent** |
| Uzbek morphology | Indirect. Context (not from the paper): Mongolian is Mongolic, not Turkic, but shares agglutinative suffixation, stem alternations at suffix boundaries, Cyrillic writing and many Russian/Western loanwords with Uzbek |
| Low-resource retrieval | Direct: no public Mongolian IR test collection existed (Sec. 5.3, p. 6); qrels built from author keywords |
| Current gap | Supports the already-occupied claim "raw vs lemma BM25 compared for agglutinative languages"; no effect on the complementarity core (§16) |

## 3. Research problem

### Simple explanation

In Mongolian a word can change its shape when a suffix is attached (a vowel drops out, a consonant is inserted). A search engine that indexes words as written will not match a query word with its inflected forms. The authors build a tool that recovers the dictionary form ("lemma") and test whether indexing lemmas improves search.

### Formal formulation

- **Task 1:** phrase-level lemmatization: map an inflected phrase (content word + suffixes) to the content word's original form, for nouns, verbs, adjectives and numerals (Sec. 2, 4).
- **Task 2:** ad hoc document retrieval with Okapi BM25 where the index-term representation is varied: `repr ∈ {raw, Sanduijav 2005, Khaltar 2006, proposed, correct}`; effectiveness measured by MAP (Sec. 5.3).
- No research questions are formally numbered; the paper's claims are "lemmatization was effective for information retrieval in Mongolian" and "Our method was more effective than the method of Sanduijav et al. (2005) for both KQ and LQ" (p. 6).

## 4. Main idea

### Simple explanation

Instead of a large dictionary of nouns (which misses new words and technical terms), the method strips known suffixes from the end of the word using rules, repairs the stem (re-inserting a dropped vowel), and handles loanwords with separate rules. Verbs are checked against a small verb dictionary; anything not recognised as a verb is treated as a noun-like phrase.

### Concrete example (from the paper)

- Loanword: "экологийн (ecology's)". The older Khaltar 2006 method outputs "эколог" (wrong); the new loanword rule removes "ийн" and adds "и", giving "экологи" (Sec. 3 p. 2; Sec. 4.6 p. 4; Figure 6 p. 5).
- Vowel elimination: "ажил + аас → ажлаас" (work + ablative); the vowel-insertion rule restores "ажил" (Figure 1, p. 1; Sec. 4.7, p. 5).
- Verb: "шинэчлэв (renew + past)" satisfies rule (ii) of the past-suffix "в"; removing "в" and the preceding vowel "э" gives "шинэчл" (Sec. 4.3, p. 4).

### Formal method

Pipeline (Figure 2, p. 3):

1. **Verb branch:** backward partial matching against the verb suffix dictionary; repeated suffix removal by segmentation rules; vowel insertion; if the result is in the verb dictionary → output as a verb.
2. **Noun branch** (nouns, adjectives, numerals): noun suffix dictionary; loanword identification; loanword-specific or standard segmentation; vowel insertion (skipped for loanwords); if no suffix matches, output the phrase unchanged.

## 5. Architecture / algorithm

| Component | Size / source | Location |
|---|---|---|
| Verb suffix dictionary | 126 suffixes (aspect, participle, mood) — new | Sec. 4.2, p. 4 |
| Verb suffix segmentation rules | 179 rules — new | Sec. 4.3, p. 4 |
| Verb dictionary | 1,254 verbs, from Sanduijav et al. (2005) | Sec. 4.4, p. 4 |
| Noun suffix dictionary | 35 suffixes, from Khaltar et al. (2006) | Sec. 4.5, p. 4 |
| Noun suffix segmentation rules | 196 rules, of which 173 from Khaltar 2006 and 23 new loanword rules ("аци", "яци", "ологи") | Sec. 4.6, p. 4 |
| Vowel insertion rules | 12 rules, from Khaltar 2006 (based on a grammar textbook) | Sec. 4.7, p. 5 |
| Loanword identification | 6 of the 7 conditions of Khaltar 2006 (the "consonants + и" condition dropped after a preliminary study) | Sec. 4.8, p. 5 |

Three enhancements over Khaltar 2006 (p. 3): verb-phrase lemmatization; loanword identification rule; extension to adjectives and numerals.

**Retrieval system (Sec. 5.3, p. 6):**

- Model: "We used Okapi BM25 (Robertson et al., 1995) as the retrieval model."
- Indexed fields: title, abstract, result; the keywords field is **not** indexed.
- Index terms: "content words" extracted by each lemmatization method in Table 2.
- **NOT_REPORTED:** BM25 implementation and parameters (k1, b, k3), whether queries were lemmatized with the same method (presumably, but not stated), tokenization of multi-word keywords, stop-words, case handling, how the "no lemmatization" index terms were formed (inferred: phrases as written), and how "correct lemmatization" was applied to phrase types outside the 15,478 assessor-agreed types (the corpus has 17,709 types; §9).

## 6. Data

### Lemmatization evaluation (Sec. 5.1–5.2, p. 5)

- **Corpus:** 1,102 technical abstracts from "Mongolian IT Park" (footnote 1: http://www.itpark.mn/, October 2007); 178,448 phrase tokens, 17,709 phrase types.
- **Gold standard:** two Mongolian graduate students (not authors) lemmatized and POS-tagged independently; Kappa 0.96 (lemmatization) and 0.94 (POS). Only phrases on which both agreed were used.
- **Evaluated:** 15,478 phrase types (noun 13,016; verb 1,797; adjective 609; numeral 56; Table 1, p. 6). The share of the 17,709 types this covers is 87.4% **[computed]**; the paper does not separate disagreement from non-target (other POS) types.

### IR test collection (Sec. 5.3, pp. 6–7)

- **Documents:** the same 1,102 abstracts. Average length ≈ 162 phrase tokens per abstract **[computed: 178,448 / 1,102]**.
- **Queries:**
  - **KQ (keyword query):** each author keyword used as a query.
  - **LQ (list query):** each abstract's keyword list used as one query; average 6.1 keywords per list.
- **Relevance:** "For each query, we used as the relevant documents the abstracts that were annotated with the query keyword in the keywords field" (p. 6). Binary; no human relevance judgments. **How this rule applies to list queries is not stated** (any keyword? all keywords? the source abstract?).
- **Query filtering:** queries with AP = 0 "in all methods" were discarded, leaving **686 KQ and 273 LQ**. The number of queries before filtering is NOT_REPORTED.
- **Average relevant documents per query:** 2.1 (p. 6); whether this is for KQ, LQ or both is not stated.
- **Train/dev/test:** not applicable (no learned components); rule development and evaluation use the same corpus (inferred; no held-out split is described).

## 7. Baselines

| Baseline | What it is | Why selected | Fair comparison? |
|---|---|---|---|
| No lemmatization | Index terms as written (raw surface forms) | Measures the effect of lemmatization | Yes, same BM25 and collection |
| Sanduijav et al. (2005) | Dictionary-based noun/verb lemmatizer (manual inflection/concatenation rules + dictionary aligned with suffixes) | Prior Mongolian method whose dictionaries were available (p. 5) | Yes; shares the verb dictionary with the proposed method |
| Khaltar et al. (2006) | Dictionary-free noun-phrase lemmatizer (predecessor of the proposed method) | Direct predecessor | Yes; the proposed method reuses its noun suffix dictionary, 173 segmentation rules and 12 vowel-insertion rules and adds to them (but skips vowel insertion for identified loanwords, Sec. 4.1) |
| Correct lemmatization | Manual lemmatization; the paper does not describe it in Sec. 5.3 (inferred: the assessors' answers from Sec. 5.2) | Upper bound for lemmatizer quality | Yes, but its source and coverage for unannotated types are NOT_REPORTED |

No stemming, n-gram or truncation baseline is included, although stemming is defined in the introduction (p. 1). Ehara et al. (2004) is discussed (p. 2) but not compared.

## 8. Metrics

| Metric | Definition | Simple meaning | Appropriate? |
|---|---|---|---|
| Lemmatization accuracy | correctly lemmatized phrases / target phrases (p. 5), computed over phrase **types** | Share of word forms the tool reduces to the right dictionary form | Yes for the tool; says nothing directly about retrieval |
| MAP | mean over queries of average precision | "On average, how high are all relevant abstracts ranked?" | Yes; but with ~2.1 relevant documents per query it behaves close to a reciprocal-rank-like measure |
| Kappa | chance-corrected agreement | Do the two annotators agree beyond chance? | Yes for gold-standard quality |

Significance: paired t-test, 5% and 1% levels (Table 3, p. 7).

## 9. Results

### Table 1: lemmatization accuracy, % (p. 6)

| POS | #Phrase types | Sanduijav 2005 | Khaltar 2006 | Proposed |
|---|---:|---:|---:|---:|
| Noun | 13,016 | 57.6 | 87.7 | 92.5 |
| Verb | 1,797 | 24.5 | 23.8 | 24.5 |
| Adjective | 609 | 82.6 | 83.5 | 83.9 |
| Numeral | 56 | 41.1 | 80.4 | 81.2 |
| **Total (as printed)** | 15,478 | 63.2 | 72.3 | 78.2 |
| Total re-weighted by #types **[computed]** | 15,478 | 54.7 | 80.1 | 84.2 |

- **Internal inconsistency.** The printed "Total" row cannot be reproduced as the type-weighted average of the per-POS rows (last row, **[computed]**). For Sanduijav the printed total (63.2) is 8.5 points above the type-weighted value, although nouns (57.6%) make up 84.1% of the types **[computed]**. The paper does not state how Total was computed (e.g., over tokens, or over a different denominator). The per-POS counts do sum to 15,478 **[computed ✓]**.
- **Figure 7 (p. 6), error analysis of the proposed method:** (a) word ending equals a suffix, 274; (b) irregular noun plural, 244; (c) loanword ending in two consonants, 94; (d) verb not in verb dictionary, 689; (e) word with multiple POS, 853. Sum 2,154 **[computed]**, which matches neither the 3,374 errors implied by 78.2% nor the 2,442 implied by the re-weighted 84.2% **[computed]**. The paper does not say whether Figure 7 is exhaustive.
- Verb accuracy is ~24% for all three methods; the authors attribute it to verbs missing from the dictionary being lemmatized as nouns (p. 5).

### Table 2: MAP of lemmatization methods, Okapi BM25 (p. 7)

| Representation | KQ (n = 686) | LQ (n = 273) | Δ vs raw, KQ **[computed]** | Δ vs raw, LQ **[computed]** |
|---|---:|---:|---:|---:|
| No lemmatization | 0.2312 | 0.2766 | — | — |
| Sanduijav et al. (2005) | 0.2882 | 0.2834 | +0.0570 (+24.7%) | +0.0068 (+2.5%) |
| Khaltar et al. (2006) | 0.3134 | 0.3127 | +0.0822 (+35.6%) | +0.0361 (+13.1%) |
| Proposed | 0.3149 | 0.3114 | +0.0837 (+36.2%) | +0.0348 (+12.6%) |
| Correct lemmatization | 0.3268 | 0.3187 | +0.0956 (+41.3%) | +0.0421 (+15.2%) |

Reading the table **[computed]**:

- Share of the raw → correct-lemma gain obtained: proposed 87.6% (KQ) / 82.7% (LQ); Khaltar 2006 86.0% / 85.7%; Sanduijav 59.6% / 16.2%.
- Proposed vs Khaltar 2006: +0.0015 (KQ), −0.0013 (LQ). The authors explain the LQ reversal by the dominance of conventional-noun queries (p. 7).
- The absolute gain of the proposed method on LQ is 0.416× its gain on KQ. Raw BM25 is already 0.0454 higher on LQ than on KQ; the authors attribute the weaker LQ significance to this higher raw MAP (p. 7). Our interpretation (not computed): longer queries leave less room for, and less need of, conflation; the two query sets and their relevance sets also differ, so this is not a within-query comparison.
- Lemmatizer accuracy vs retrieval: Khaltar 2006 → proposed is +5.9 accuracy points (noun +4.8) but +0.0015 MAP (KQ). Sanduijav → Khaltar 2006 is +9.1 total accuracy points (noun +30.1) and +0.0252 MAP (KQ). Gains in retrieval track noun accuracy more than total accuracy; with only two comparisons this is an observation, not a relationship.

### Table 3: paired t-test on MAP (p. 7)

| Pair | KQ | LQ |
|---|:---:|:---:|
| No lemmatization vs Correct | << | < |
| No lemmatization vs Sanduijav | << | ― |
| No lemmatization vs Khaltar 2006 | << | < |
| No lemmatization vs Proposed | << | < |
| Sanduijav vs Proposed | << | < |
| Khaltar 2006 vs Proposed | ― | ― |
| Proposed vs Correct | < | ― |

"<" = significant at 5%, "<<" = at 1%, "―" = not significant (p. 7). Three pairs are not reported: Sanduijav vs Khaltar 2006, Sanduijav vs Correct, Khaltar 2006 vs Correct.

## 10. Statistical evidence

- **Significance test:** paired t-test (citing Keen, 1992), reported only as significance levels; raw p-values and t statistics **NOT_REPORTED**. No correction for multiple comparisons (7 pairs × 2 query sets).
- **Confidence intervals:** NOT_REPORTED.
- **Runs / seeds:** not applicable (deterministic rule-based systems, single BM25 configuration).
- **Ablation:** none. The three enhancements (verb branch, loanword rules, adjective/numeral coverage) are not evaluated separately in IR; Figure 7 is an error analysis, not an ablation.
- **Per-query analysis:** **NOT_REPORTED.** No per-query wins/losses, no query features, no overlap between the result sets of different representations, no unique relevant hits, no oracle union. The KQ/LQ split is a comparison of two query *formulations* at aggregate level.
- **Query filtering:** discarding queries with AP = 0 under all five methods is applied identically to all conditions, so it does not favour a method, but it raises absolute MAP levels and removes queries that every representation fails on.

## 11. Strengths

- Controlled design: one collection, one ranking model, only the index-term representation varied.
- **Gold-lemmatization upper bound** separates lemmatizer error from the effect of lemma indexing; the proposed method reaches ~83–88% of the achievable gain **[computed]**.
- Intrinsic evaluation with two independent annotators, high Kappa, and only agreed items used.
- Paired significance tests for most pairs, including the negative result vs its predecessor, which the authors report honestly.
- Two query formulations show that the size of the morphology effect depends on query form.
- Explicit handling of loanwords in Cyrillic script as a separate morphological class.

## 12. Limitations

### Stated by the authors

- Verb accuracy is low because many verbs are missing from the verb dictionary (p. 5).
- Error types (a)–(c) have no solution yet; (d) needs a larger verb dictionary; (e) needs POS information / a POS tagger (p. 6; Sec. 6 future work).
- The average number of relevant documents per query (2.1) is small; the authors argue that the large number of queries makes results stable (p. 6).
- No public Mongolian IR test collection exists; the collection was built from author keywords to avoid relevance-judgment cost (p. 6).

### Inferred from the experimental design

1. **Pseudo-qrels from author keywords.** Relevance = "annotated with the query keyword", not a judged information need. Abstracts that discuss the topic without listing the keyword count as non-relevant. Keywords are chosen by authors and likely appear (in some inflected form) in the abstract text, which may favour lexical matching; direction and size of the bias are unknown.
2. **List-query relevance is undefined** in the text, and the 2.1 average is not split by query type.
3. **BM25 and query processing under-specified** (k1/b, query lemmatization, multi-word keyword tokenization, stop-words). The results are one BM25 configuration.
4. **Coverage of "correct lemmatization"** beyond the 15,478 agreed types is not described.
5. **No held-out split for rule development:** rules were developed and evaluated on the same abstracts (inferred; the paper describes no separate development data).
6. **Total accuracy row not reproducible** from the per-POS rows (§9); error counts in Figure 7 do not reconcile.
7. **Small, single-domain collection** (1,102 technical abstracts), single language variety (Cyrillic Modern Mongolian).
8. No stemming or n-gram/truncation baseline, so "lemma vs cheaper conflation" is not tested.
9. Multiple t-tests without correction; no effect sizes beyond MAP differences.

## 13. What the work proves

- On this Mongolian abstract collection with keyword-derived qrels, **lemma indexing in Okapi BM25 improves MAP over raw surface forms**, significantly at 1% for single-keyword queries under every lemmatizer (Tables 2–3, p. 7): +0.057 to +0.096 MAP **[computed]**.
- **The effect is much smaller for long (keyword-list) queries:** +0.007 to +0.042 MAP; not significant for the weakest lemmatizer (Tables 2–3).
- **Among the tested pairs:** proposed > Sanduijav (significant for KQ at 1% and LQ at 5%); proposed ≈ Khaltar 2006 (not significant for either); proposed < manual lemmatization significant for KQ (5%), not for LQ (Table 3). Sanduijav vs Khaltar 2006 and Khaltar 2006 vs manual were not tested, so a full ordering is not established (Khaltar 2006 > Sanduijav only numerically, Table 2).
- The proposed lemmatizer is more accurate than two earlier Mongolian lemmatizers on nouns (92.5% vs 87.7% / 57.6%, Table 1), within the caveat on the Total row; no significance test is reported for accuracy.

## 14. What the work does NOT prove

- **That the proposed method improves retrieval over its predecessor.** Khaltar 2006 vs proposed is not significant for either query type, and numerically lower for LQ (Tables 2–3). The conclusion "improved the retrieval accuracy" (Sec. 6, p. 7) holds only relative to no lemmatization and to Sanduijav.
- **That lemmatization beats stemming or simpler conflation** — no stemming, truncation or n-gram condition was run.
- **Anything about dense/semantic retrieval, hybrid fusion or complementarity** — none were run. There is no overlap, unique-hit or oracle-union analysis between representations.
- **Which queries benefit and why.** Only an aggregate KQ/LQ contrast; no per-query or query-feature analysis.
- **That the effect generalizes** to judged relevance, larger or full-text collections, or other domains.
- **That total lemmatizer accuracy predicts retrieval effectiveness** — two data points, and the printed totals are not internally consistent.

## 15. Relationship to current Uzbek evidence

- **No Uzbek data.** Context (not from the paper): Mongolian (Mongolic) and Uzbek (Turkic) are both agglutinative and suffixing, with stem alternations at suffix boundaries and many Russian/Western loanwords; Uzbek has official Latin script with a large Cyrillic legacy. Transfer of the *design lessons* is reasonable; transfer of the *numbers* is not.
- Parallels with the national evidence (from `MASTER_INDEX.md`): Uzbek morphological analyzers are reported with analyzer accuracy (Bakaev 88.9–96%; Xusainova 97.5%) rather than IR effectiveness. This paper shows, for a comparable language, that analyzer accuracy gains need not carry over to retrieval (+5.9 points accuracy → +0.0015 MAP).
- Consistent with MORPH-001 (Can et al. 2008, Turkish; project card): query length interacts with the effect of morphological normalization. Here, single-keyword vs keyword-list queries show the same direction (larger effect for short queries).
- Related pending card: Ozturkmenoglu & Alpkocak 2012 (CR001537, Turkish lemmatization variants in Terrier tf×idf). Together they show multi-variant lemma comparisons in lexical IR for agglutinative languages are long established.

## 16. Relationship to CURRENT_GAP

**Classification:** *supports* (the already-occupied part) + *no material effect on the residual core*.

- **Supports / confirms as occupied** (already a non-claim in v0.8): "raw/stem/lemma have not been compared in low-resource IR". This paper is an additional, early, peer-reviewed example of raw vs several lemmatizers vs gold lemma in **BM25** for an agglutinative Cyrillic-script language, with significance tests.
- **Touches one v0.8 query-feature element only weakly:** query length/formulation ("длина запроса") moderates the morphology effect in the lexical channel alone, at aggregate level.
- **Does not touch:**
  - a fixed dense retriever D;
  - unique relevant hits / overlap between lexical and dense channels;
  - oracle union or incremental hybrid gain;
  - per-query links between morphology-induced change and query features.

**Proposal:** keep v0.8 refined unchanged. Optionally list this paper in the evidence boundary as an early BM25 raw-vs-lemma study with a gold-lemma upper bound (researcher's decision). This is a proposal only; `CURRENT_GAP.md` has not been edited.

## 17. Implications for our research design

- **Morphology preprocessing — add a gold-lemma control.** Manually lemmatize the queries (and, if feasible, a sample of relevant documents) to create `BM25_lemma-gold` as an upper bound on a small subset. It separates "lemmatizer errors" from "effect of lemma representation" in our raw → stem → lemma comparisons, and can be extended to complementarity: does gold lemmatization change the unique-hit set with D more than the automatic lemmatizer does?
- **Report IR effectiveness, not analyzer accuracy.** Choice of Uzbek lemmatizer/stemmer should be justified by retrieval results on our dev set; this paper shows accuracy gains can vanish in MAP.
- **Query taxonomy.** Keep query length / query form (keyword vs sentence vs keyword list) as a candidate moderator, and test it per query rather than across different query sets.
- **Loanwords and script.** Include loanword handling (Russian/Western loans in Cyrillic and Latin Uzbek) in the lemmatizer error analysis and as a query feature; this paper found loanword-specific inflection behaviour needed separate rules.
- **Qrels.** Keyword-derived relevance is cheap but yields ~2 relevant documents per query and topical false negatives; acceptable for a pilot/dev set, not for the main evaluation where unique-hit/overlap counts need fuller judgments.
- **Protocol.** Report BM25 parameters, query preprocessing and the treatment of multi-word terms explicitly; report which queries were excluded and why (here: AP = 0 for all systems — we should report such "all-fail" queries rather than discard them, since they matter for oracle-union analysis).
- **Statistics.** Report p-values/effect sizes and correct for multiple comparisons across representation pairs.
- **Hypothesis.** No evidence for or against morphology-induced complementarity change; the paper only confirms that the lexical channel itself changes under lemmatization.

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| Agglutinative language | Words are built by attaching a chain of suffixes to a stem | Morphology with concatenated, mostly one-meaning affixes |
| Lemmatization | Reduce a word form to its dictionary form | Map inflected form → lemma (a real word) |
| Stemming | Cut a word down to a common stem, not necessarily a real word | Map inflected form → stem (conflation class) |
| Phrase (in this paper) | One Mongolian word unit: content word + suffixes | Content word followed by one or more suffixes (p. 1) |
| Vowel elimination / insertion | A stem vowel drops when a suffix is added; the rule puts it back | e.g., ажил + аас → ажлаас (Figure 1) |
| Loanword | Word borrowed from a Western language, inflecting differently | Treated by separate identification and segmentation rules |
| Okapi BM25 | Classic word-matching ranking with term-frequency saturation and length normalization | Probabilistic relevance framework scoring (parameters k1, b) |
| MAP | Average of per-query average precision | Mean over queries of Σ precision at relevant ranks / #relevant |
| Pseudo-qrels | Relevance taken from data structure (author keywords), not judged | Automatically constructed relevance judgments |
| Gold (correct) lemmatization | Human-made lemmas used as a best-case representation | Upper bound for lemmatizer quality in IR |
| Kappa | Agreement between two annotators corrected for chance | Kappa coefficient (variant not stated in the paper; two raters) |
| Paired t-test | Tests whether per-query differences between two systems are reliably non-zero | Test on per-query AP differences |
| Complementarity (project term) | Each channel finds some relevant documents the other misses | Unique relevant hits, overlap, oracle-union gain |

## 19. Open questions / verification needed

1. How was the "Total" row of Table 1 computed? It is not the type-weighted mean of the per-POS rows (§9). Is Figure 7 exhaustive?
2. How is relevance defined for list queries, and is the 2.1 relevant documents per query for KQ, LQ or both?
3. How many queries were there before AP = 0 filtering?
4. BM25 parameters, implementation, query lemmatization and multi-word keyword handling: NOT_REPORTED.
5. How was "correct lemmatization" applied to phrase types outside the 15,478 agreed types?
6. Proceedings page range and conference place/date: not verified (ACL Anthology record lists none).
7. Is there a later journal/thesis version by Khaltar with dense or larger-scale IR experiments? (A lead only; not checked, and not part of this paper's evidence.)

## 20. Decision after deep dive

- **Keep current gap?** Yes. v0.8 refined remains valid (§16).
- **Modify gap?** No change proposed. Optionally add to the evidence-boundary list as an early BM25 raw-vs-lemma study with a gold-lemma upper bound (researcher's decision).
- **Add decision?** Proposed for `decisions/DECISIONS.md` (researcher's decision): "Morphological tool selection is justified by retrieval effectiveness on the dev set, not by analyzer accuracy"; "include a gold-lemmatized query subset as an upper-bound control".
- **Add experiment?** Optional low-cost addition to the Uzbek pilot: `BM25_lemma-gold` on manually lemmatized queries, compared with automatic lemma BM25 in both effectiveness and unique hits vs D.
- **Add citation to Chapter I?** Yes, §1.1 (morphological normalization of lexical retrieval in agglutinative languages; gold-lemma upper bound; query-form interaction), as a secondary example alongside Turkish work.
- **Proposed `MASTER_INDEX.md` row** (to add after approval):

| MORPH-036 | Khaltar & Fujii — *A Lemmatization Method for Modern Mongolian and its Application to Information Retrieval* (IJCNLP 2008, ACL Anthology I08-1001) — [deep dive](deep-dives/2008_Khaltar_Fujii_Mongolian_Lemmatization_IR.md) | 2008 | B | MEDIUM | Rule-based dictionary-light Mongolian lemmatizer (Cyrillic, agglutinative) + Okapi BM25 on 1,102 technical abstracts with author-keyword pseudo-qrels (686 keyword / 273 keyword-list queries). MAP raw 0.2312/0.2766 → proposed 0.3149/0.3114 → gold lemma 0.3268/0.3187 (KQ/LQ); lemma > raw significant for KQ; proposed ≈ predecessor Khaltar 2006 (n.s.); effect much smaller for long queries. Table 1 total-accuracy row not reproducible. No stemming, no dense, no fusion, no overlap/unique-hit/per-query analysis. |
