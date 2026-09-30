# Hadımlı (2011): Processing Turkish Radiology Reports (M.Sc. thesis, METU)

**Targeted deep-dive status:** COMPLETED (AI-assisted, pending researcher review)
**Completed:** 2026-09-28
**Verification:** independent AI verifier pass 2026-09-28; 10 findings addressed.
**Literature ID:** `MORPH-028` (assigned 2026-09-28, approved by researcher)
**Systematic-review record:** `CR002211`. Full-text triage: INCLUDE, reading priority HIGH, reading tier 1 ("прямо по теме пробела"), `carries_complementarity_evidence = NO`. Triage evidence location: Ch. 5.1 (5.1.1–5.1.2), Table 5.1; Sec. 4.2.1.
**Provenance:** AI-assisted deep dive (Claude). The thesis is in English (100 PDF pages; the abstract states "May 2011, 86 pages"). PDF page = printed arabic page + 13. What was read in full: title and approval pages, abstract and Öz, table of contents, Ch. 1 (Introduction), Ch. 3 (Background, incl. 3.5 Utilized Tools), Ch. 4.1–4.2 (data, rule-based method, morphological analysis and workarounds), Sec. 4.3.1–4.3.3 and 4.3.6 (data-driven method: morphology, disambiguation, parsing, variations), all of Ch. 5 (evaluation: 5.1 retrieval, 5.2 extraction, 5.3 discussion) and Ch. 6 (conclusion and future work). Ch. 2 (literature survey) and Sec. 4.3.4–4.3.5 (simulated annealing and SVM internals) were read quickly because they contain no retrieval evaluation. Appendices A–B (sample reports, extraction data subset) were not read. **Pages checked visually** (110 dpi page images): PDF p. 3 (approval page); PDF pp. 31–32 (printed pp. 18–19: Tables 4.1–4.2); PDF p. 34 (p. 21: Fig. 4.1 and the Zemberek workaround); PDF pp. 56–57 (pp. 43–44: Sec. 5.1.1–5.1.2, Table 5.1); PDF p. 61 (p. 48: Table 5.4); PDF p. 66 (p. 53: Table 5.9); PDF p. 70 (p. 57: Table 5.13); PDF pp. 74–77 (pp. 61–64: Tables 5.16–5.20); PDF p. 79 (p. 66); PDF pp. 82–84 (pp. 69–71: conclusions). Every number of Tables 5.1, 5.4, 5.9, 5.13, 5.16, 5.17, 5.19 and 5.20 reported below was compared with the page image. Numbers computed by us are marked **[computed]** and were computed in Python.
**Source rule:** **the thesis is the primary and only authoritative source** for what the author did and found. The web was used only to try to verify the bibliographic record (see §1). Statements about other Turkish IR works come from other project cards and are marked as such; they are not evidence about this thesis.
**Reliability:** **B.** Master's thesis (M.Sc., Computer Engineering, Middle East Technical University). Not peer-reviewed and not doctoral. In the supplied copy the approval page carries names but no signatures and no date (PDF p. 3). The official METU record could not be opened. The retrieval evidence is very narrow: one small test set (53 reports, 100 queries, one physician), unranked set-matching, recall/precision only, no significance test.

---

## Кратко для исследователя (RU)

- **Что это.** Магистерская диссертация (M.Sc., METU, май 2011; руководитель Prof. Dr. Göktürk Üçoluk, соруководитель Dr. Meltem Turhan Yöndem). Часть проекта TÜBİTAK 3080179 по поиску в турецких радиологических отчётах. **Основная часть работы — извлечение информации** (information extraction): правила и обучаемые правила строят концептуальные графы (отношения «локализация», «модификатор», «измерение»). Поиск по документам занимает около 2,5 страницы (Sec. 5.1, pp. 42–44).
- **Поисковый эксперимент.** 53 отчёта на разные темы, 100 запросов (фрагменты предложений в стиле отчёта), отметки релевантности сделал **один врач**, 5300 пар «запрос–отчёт». Сравниваются:
  - базовый метод: пересечение множеств **корневых лексем** (root lexemes) запроса и документа, т.е. булев поиск по корням;
  - метод на правилах: пересечение множеств извлечённых отношений («individual meanings») запроса и документа.
  Ранжирования нет: документ либо возвращается, либо нет.
- **Главные числа** (Table 5.1, p. 44):
  - базовый метод: recall 96.05%, precision 5.15–5.46%;
  - метод на правилах: recall 65.78–67.10%, precision 28.65–31.84%.
  - F1 **[computed]**: ≈0.10 (базовый) против ≈0.40–0.43 (правила).
- **Наша проверка** **[computed]**: все проценты Table 5.1 точно воспроизводятся, если усреднять по парам (micro) и число релевантных пар R = 76, 152 или 228 (например, 73/76, 51/76, 50/76). Значит, в среднем всего 0.76–2.28 релевантных отчёта на запрос. Автор число релевантных пар и способ усреднения **не сообщает**.
- **Морфология в поиске:**
  - есть только одно лексическое представление — корни. **Сравнения raw / stem / root в поиске нет**;
  - какой анализатор даёт корни для базового метода и что делается со словами, которые анализатор не разобрал, **не сказано** (NOT_REPORTED);
  - в методе на правилах используется Zemberek; для медицинских терминов вне словаря — откат к сопоставлению поверхностных суффиксов (Sec. 4.2.1, p. 21).
- **Морфология в извлечении (не в поиске):** добавление корневой лексемы в правила повышает precision (+8.9…+20.1 п.п.), но снижает recall на 25.9–31.5 п.п. (переобучение); 2–3-буквенные концы корней дают +3.5…+13.6 п.п. precision при −4.5…−5.5 п.п. recall (Tables 5.9, 5.13 **[computed]**).
- **Чего нет:** BM25 или любой ранжирующей модели; плотного поиска; гибрида/fusion; перекрытия выдач двух методов, уникальных релевантных документов, oracle union; анализа по запросам; тестов значимости.
- **Внутренние несоответствия:**
  - p. 66: precision на экспертном наборе «37.0% to 64.3%», в Table 5.20 (MC = 1) и p. 72 — до 65.3% (при MC = 2 в Table 5.20 — 67.0%);
  - падение precision из-за автоматического парсинга: «8 points in average» (p. 63) и «6%» (p. 71); по таблице в среднем 8.85 п.п. **[computed]**;
  - Table 5.16 ставит рядом метод на правилах (TP+FN = 426) и методы на данных (TP+FN = 528), т.е. знаменатели разные; в Table 5.17 знаменатели 447 / 442 / 396;
  - Test-4: при MC = 2 (фильтрация правил) TP больше, чем при MC = 1 (401 против 361).
- **Для нашего gap:** работа на ядро v0.8 **не влияет**. Она только качественно показывает типичную проблему турецких специализированных текстов (медицинские заимствования вне словаря анализатора, разное написание терминов у разных врачей). Предложение: gap не менять.
- **Практическая польза для узбекского:**
  1. Для лемма/корень-канала заранее задать правило отката для слов, которые анализатор не разбирает, и сообщать долю таких слов (кандидат в признаки запроса).
  2. Вариативность написания заимствованных терминов — аналог латиница/кириллица и апострофов в узбекском; это признак запроса.
  3. Запросы в стиле документа (фрагменты предложений) завышают recall пословного сопоставления — тип формулировки запроса надо фиксировать в таксономии.
  4. Всегда сообщать число релевантных на запрос и способ усреднения (micro/macro).

---

## 1. Bibliographic record

- **Author:** Kerem Hadımlı
- **Title:** *Processing Turkish Radiology Reports*. Turkish title (Öz): *Türkçe Radyoloji Raporlarının İşlenmesi*.
- **Degree:** Master of Science in Computer Engineering (Öz: "Yüksek Lisans, Bilgisayar Mühendisliği Bölümü")
- **University:** Middle East Technical University (METU), Graduate School of Natural and Applied Sciences
- **Date:** May 2011 (title page; abstract: "May 2011, 86 pages")
- **Supervisor:** Prof. Dr. Göktürk Üçoluk (METU). **Co-supervisor:** Dr. Meltem Turhan Yöndem (Sabancı University).
- **Examining committee (approval page):** Dr. Ayşenur Birtürk, Prof. Dr. Göktürk Üçoluk, Dr. Onur Tolga Şehitoğlu, Dr. Cevat Şener, Dr. Meltem Turhan Yöndem. In the supplied PDF the signature lines and the date are blank (PDF p. 3).
- **Funding:** TÜBİTAK project 3080179; data from the Radiology Department of Hacettepe University Hospital (Acknowledgments, p. vi).
- **DOI:** none found.
- **Related publication (bibliographic check only; not read and not used as a source):** K. Hadımlı, M. Turhan Yöndem, "Information Retrieval from Turkish Radiology Reports without Medical Knowledge", Lecture Notes in Computer Science vol. 7022, Springer, 2011 (doi 10.1007/978-3-642-24764-4_19; Springer chapter page).
- **Official URL:** not verified. (Bibliographic check: a web search returned only a CiteSeerX listing titled "Approval of the thesis: PROCESSING TURKISH RADIOLOGY REPORTS" (doi 10.1.1.634.1967); the page could not be opened (blocked). No METU OpenMETU record was found.)
- **Systematic-review metadata:** venue "PQDT - Global", document type THES, 100 pages.
- **Source type:** Master's thesis
- **Reliability:** B (see header)
- **Full text available:** yes (`07_full_text/pdfs/CR002211.pdf`, 100 PDF pages)

## 2. Why this work matters to the PhD

It is one of the few Turkish (Turkic, agglutinative) works in the corpus that evaluates **domain-specific document retrieval** with a **morphologically normalized lexical representation** (root lexemes). But the retrieval part is small and the lexical representation is never varied.

| Axis | Relation |
|---|---|
| Lexical retrieval | Only a Boolean set-intersection baseline over root lexemes (any-word or ≥50% of query words). No term weighting, no ranking, no BM25 |
| Semantic retrieval | None in the modern sense. The "rule-based" retriever matches extracted relation structures (a structured/symbolic representation), not embeddings |
| Hybrid retrieval | **Absent**: the two methods are never combined, and their result sets are never compared |
| Uzbek morphology | Indirect: Turkish is a close Turkic relative. Useful qualitative points on analyzer coverage of domain loanwords and surface-suffix fallback (Sec. 4.2.1) |
| Low-resource retrieval | Domain-level scarcity (no Turkish medical lexicon/ontology used, by design) |
| Current gap | No material effect (§16) |

## 3. Research problem

### Simple explanation

Turkish radiology reports are free text. Doctors want to find reports that describe a finding at a location ("cyst in the liver"). Searching for the words alone returns almost every report, because words like *cyst*, *liver* and *lesion* appear everywhere. The author asks whether understanding the **relations** between words, using only Turkish grammar and no medical dictionary, gives more precise results. The main goal of the thesis is extracting such relations; retrieval is one application.

### Formal formulation

- **Aim (abstract, p. iv):** "to measure baseline performance Turkish language can provide for medical information extraction and retrieval, in isolation of other factors".
- **Retrieval task (Sec. 5.1):** unranked set retrieval. For query `q` and report `d`, return `d` if `|S(q) ∩ S(d)| / |S(q)| ≥ θ` (or `≥ 1` element for "single match"; the thesis says "greater than a threshold ratio" but also that a baseline threshold of one returns documents containing all query words, so strict vs non-strict inequality is not specified consistently, p. 43), where `S(·)` is either the set of root lexemes (baseline) or the set of extracted relations (rule-based). A sentence-level variant computes the intersection per sentence of `d`.
- **Extraction task (Sec. 5.2):** extract typed relations (location, modifier, locative modifier, measurement) with labelled concept phrases, evaluated by TP/FN/FP.

## 4. Main idea

### Simple explanation

Represent every sentence as a small graph of relations: *where* something is, *what* it is, how it is qualified. Build the graph with hand-written templates that look at Turkish suffixes (for example, the locative *-de/-da* marks a location). Then retrieve reports whose graph shares relations with the query's graph.

### Concrete example

The thesis's own example (Fig. 4.1, Fig. 4.2, Tables 4.5–4.6, pp. 21–26):

- Sentence: "Hemaperitonium, mesane lümeninde hematom ve hava." (English, p. 21: "Hematoma and air in urinary bladder's cavity, hemoperitoneum.")
- The locative suffix in *lümen-in-de* triggers a LOCATION template: (where) *mesane lümen* → (what) *hematom*.
- *ve* ("and") triggers CONJUNCTION: *hematom* – *hava*.
- A second-phase rule distributes the location over the conjunction: (where) *mesane lümen* → (what) *hava*.
- Two wrong relations are also produced, because without medical knowledge the system treats *Hemaperitonium* as a location (marked * in Table 4.6).
- A bag-of-roots baseline would match any report containing *mesane*, *lümen*, *hematom*, *hava*; the relation-based method matches only reports that contain the same relations.

### Formal method

- **Rule-based extraction (Sec. 4.2):** local templates (sequences of word patterns: any word, surface suffix, morpheme name, prefix, root, number, end-of-sentence, literal; Sec. 4.2.2) produce concept–relation pairs. Three non-local rules (left/right distributivity of LOCATION over CONJUNCTION, qualification chaining; Sec. 4.2.4) are applied until no new relation appears.
- **Retrieval (Sec. 5.1):** set intersection of relation sets (the author calls it "a method similar to vector-space model", p. 43, but describes no weighting or ranking), with three decision variants (whole report + single match; whole report + threshold ratio; single sentence + threshold).
- **Baseline (Sec. 5.1.1):** "The baseline algorithms makes a set intersection based search like the rule-based algorithm, but the sets consist of individual query and document words (root lexemes), not *conceptual relations*" (p. 43).

## 5. Architecture / algorithm

1. **Morphological analysis for the rule-based method** (Sec. 4.2.1, pp. 20–21):
   - Zemberek, which "analyzes a given word string by trying to regenerate it from a known list of roots, morphemes, and rules governing agglutination" (p. 20–21).
   - Problem: medical terms missing from Zemberek's lexicon are still inflected in the reports.
   - Workaround: templates exist in two forms, one matching a Zemberek morpheme and one matching "the common surface representation of the morpheme". If Zemberek analyzes a word, only morpheme rules apply; otherwise "rules with surface forms allows us fallback to string suffix matching" (p. 21).
   - Only morphemes of the last inflectional group are needed (p. 20). Morphological disambiguation for this method is not described.
2. **Template construction** (Sec. 4.2, p. 19): hand-crafted from phrases tagged by physicians of Hacettepe University Hospital, using frequencies of morphemes and string suffixes, including 2 words before and after each tagged phrase. The number of templates is NOT_REPORTED. Whether the tagged reports overlap the retrieval test set is NOT_REPORTED.
3. **Indexing for retrieval** (Sec. 5.1, p. 43): every test report is parsed; its relation sets are stored in a database. Each query is parsed as one sentence. How concept phrases are compared (exact string, root form) is NOT_REPORTED; the worked example shows concept phrases stored with the matched suffix removed (*mesane lümen* from *mesane lümeninde*, Table 4.5).
4. **Baseline indexing** (Sec. 5.1.1): sets of root lexemes of query and document words. **NOT_REPORTED:** which analyzer produces the roots (Zemberek is plausible because Table 3.1 lists it for the rule-based line, but the thesis does not say so for the baseline); how ambiguous analyses are resolved; what is done with words the analyzer cannot analyze; stop-words; case folding.
5. **Data-driven extraction** (Sec. 4.3; not used for retrieval): TRMorph (two-level analyzer) with post-processing of derivational boundaries; the Yuret & Türe disambiguator (training failed on the small dataset, p. 66); MaltParser with IG-to-IG links; rules learned by a covering algorithm with simulated annealing, or by linear SVMs (LIBLINEAR). Variations: root lexeme in rules (L), extra parent node (A), disallowing zero-error rules (0), 2–3-letter string suffixes of the root (S).

## 6. Data

### Master collection (Sec. 4.1, Tables 4.1–4.2, pp. 17–19)

- 4,634 anonymized reports from Hacettepe University Hospital; 287 unique report types, 45 types with more than 10 reports.
- Coarse groups: abdominal 840, thoracic 944, head/neck/brain/spinal 1,942, joints/bones 252, others 656 (sum 4,634 **[computed]** ✓).
- Language: Turkish; domain: radiology (medical).

### Retrieval test set (Sec. 5 intro, p. 42; Sec. 5.1.2, p. 44)

- 53 reports "on different topics" and 100 queries; "forming 5300 data points".
- Queries: free text, "not full sentences, but partial sentences", each with "only a few conceptual relations such as a finding, a location, and qualifiers" (p. 42).
- Relevance: "Each query has a defined set of reports it should return. This dataset was prepared by a medical doctor" (p. 42). Binary; exhaustive over the 53 reports (every unmarked report counts as an error if returned, p. 44).
- **NOT_REPORTED:** number of relevant reports per query; whether any query has zero relevant reports; how queries were created (from the reports? independently?); agreement or second assessor; sampling of the 53 reports.
- **[computed] inference:** under micro-averaging over pairs, Table 5.1 is reproduced exactly only if the total number of relevant pairs R is 76, 152 or 228 (R ≥ 304 would require the baseline to return more than 5,300 pairs). With R = 76: baseline TP = 73 of about 1,416 returned pairs; rule-based TP = 51 of 178 (single match) and 50 of 157 (50%). This is 0.76–2.28 relevant reports per query on average. The printed values are truncated rather than rounded (51/76 = 67.105% printed 67.10%; 50/76 = 65.789% printed 65.78%).

### Extraction datasets (Sec. 5.2, 5.2.6; not used for retrieval)

- Second dataset: abdominal reports; 506 sentences, 251 after removing sentences that have exact duplicates (all copies removed) (Table 5.2, p. 45); 566 tagged relations (Table 5.5). After low-coverage filtering on the **whole** dataset: 528 (k = 2) or 447 (k = 10) instances (Table 5.6).
- Third ("expert") dataset: 7 abdominal reports, 34 sentences, 117 relations, tagged by two domain experts (p. 64). Agreement NOT_REPORTED.

## 7. Baselines

| Baseline | What it is | Why selected | Fair comparison? |
|---|---|---|---|
| Root-lexeme set match (whole report, any word) | Boolean OR over query roots | Simplest "do the words occur" reference | Weak baseline: no term weighting, no ranking, no IDF. A 2011 Turkish IR baseline would normally be a ranked tf-idf/BM25 model |
| Root-lexeme set match (whole report / single sentence, ≥50% of query words) | Boolean partial-AND | Tightens matching | Same caveat; the 100% (all words) threshold defined on p. 43 is not reported in Table 5.1 |

- The comparison is between two **unranked** representations (bag of roots vs bag of relations), so it measures a precision/recall trade-off at one operating point per configuration. No ranked baseline exists to show whether a weighted lexical model would reach similar precision.
- Only the rule-based method was tested for retrieval ("Only the rule based algorithm is tested in information retrieval context", p. 42). The better-performing data-driven extractor was never used for retrieval.

## 8. Metrics

| Metric | Definition | Simple meaning here | Appropriate? |
|---|---|---|---|
| Recall | relevant returned / all relevant | Share of the marked (query, report) pairs that are returned | Yes for set retrieval; averaging (micro vs macro) NOT_REPORTED; micro is consistent with the numbers (§6) |
| Precision | relevant returned / all returned | Share of returned pairs that are marked relevant | Yes for set retrieval; very sensitive to the small number of relevant pairs |
| Extraction TP / FN / FP (CWA, CCA, CRA) | Exact relation match; three definitions of false positive (closed-world, closed-concepts, closed-relations) | Strict to lenient error counting when the gold tagging is incomplete | Reasonable for extraction; not retrieval metrics |

No ranked metric (MAP, nDCG, MRR, P@k) is used; F1 is deliberately not reported ("Additional measures such as F1-score will not be reported in order to not confuse the reader", p. 47).

## 9. Results

### Table 5.1: retrieval (p. 44; checked on the page image)

| Method | Match target | Threshold | Recall | Precision | F1 **[computed]** |
|---|---|---|---:|---:|---:|
| Baseline (root lexemes) | Whole report | Single match | 96.05% | 5.15% | 0.098 |
| Baseline (root lexemes) | Whole report | 50% | 96.05% | 5.42% | 0.103 |
| Baseline (root lexemes) | Single sentence | 50% | 96.05% | 5.46% | 0.103 |
| Rule-based (relations) | Whole report | Single match | 67.10% | 28.65% | 0.402 |
| Rule-based (relations) | Whole report | 50% | 65.78% | 31.84% | 0.429 |
| Rule-based (relations) | Single sentence | 50% | 65.78% | 31.84% | 0.429 |

Reading the table:
- Rule-based vs baseline (whole report, single match): recall −28.95 points, precision ×5.6 **[computed]**.
- The author's explanation (p. 44): queries are written like report sentences and contain generic words (*cyst*, *liver*, *lesion*) that occur in most sentences, so word matching returns almost everything. Threshold choice barely matters for the rule-based method because queries "mostly contain one or two relations" (so 50% of 1–2 relations ≈ one relation).
- Even the any-word baseline misses 3.95% of relevant pairs (3 of 76 under R = 76) **[computed]**. Those relevant reports share no root lexeme with the query. The thesis does not discuss them; possible causes include spelling variants of medical terms (p. 2) and analyzer failures, but this is our conjecture.
- With R = 76 **[computed]**, the baseline returns about 14 reports per query, the rule-based method about 1.6–1.8, against 0.76 relevant on average.

### Morphology-related variations in extraction (Tables 5.9, 5.10, 5.13, 5.15; pp. 53–60; all rows checked on the page images of Tables 5.9, 5.13 and the summary Table 5.16)

Second dataset, k = 2 filtering, 10-fold cross-validation, **gold** morphology and dependencies. MC = minimum rule coverage.

| Test | Variation | MC | TP | FN | Recall | Prec. CWA | Prec. CCA | Prec. CRA |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Test-1 | base | 1 | 404 | 124 | 76.5% | 31.6% | 51.0% | 63.6% |
| Test-1 | base | 2 | 389 | 139 | 73.7% | 33.2% | 51.9% | 64.9% |
| Test-2 | + root lexeme | 1 | 267 | 261 | 50.6% | 45.9% | 59.9% | 74.2% |
| Test-2 | + root lexeme | 2 | 223 | 305 | 42.2% | 53.3% | 67.4% | 79.4% |
| Test-3 | + root lexeme, no zero-error rules | 1 | 419 | 109 | 79.4% | 32.5% | 48.7% | 63.1% |
| Test-3 | + root lexeme, no zero-error rules | 2 | 406 | 122 | 76.9% | 35.8% | 53.1% | 65.0% |
| Test-5 | + 2–3-letter root suffixes | 1 | 380 | 148 | 72.0% | 40.0% | 54.5% | 69.0% |
| Test-5 | + 2–3-letter root suffixes | 2 | 360 | 168 | 68.2% | 46.8% | 60.7% | 74.1% |
| Test-6 | SVM | – | 221 | 307 | 41.9% | 22.3% | 27.5% | 51.3% |
| Test-7 | SVM + suffixes | – | 165 | 363 | 31.3% | 35.6% | 43.7% | 71.1% |

Recomputed changes vs Test-1 **[computed]** (percentage points):
- **Root lexeme (Test-2):** recall −25.9 / −31.5; precision CWA +14.3 / +20.1, CCA +8.9 / +15.5, CRA +10.6 / +14.5. Text: "precision increases by at least ten percent in all cases" and "recall values drop by 26% and 31%" (p. 52); Conclusion: "an increase of 13% in precision" (p. 70). The recall figures match as points. The p. 52 claim "at least ten percent in all cases" holds as a relative change (+16.7% to +60.5% relative **[computed]**) but not as points (CCA at MC = 1 is +8.9 points); the p. 70 "13%" matches neither reading exactly (mean of the six point gains 14.0, of the three MC = 1 gains 11.3 **[computed]**).
- **Root lexeme + no zero-error rules (Test-3):** recall +2.9 / +3.2 (text "3 points", p. 53 ✓); precision change −2.3 to +2.6 (Conclusion "around 2%", p. 71).
- **Root suffixes (Test-5):** recall −4.5 / −5.5 (text "3 to 5 points", p. 55: slightly understated); precision +3.5 to +13.6 (text "3 to 13 points" ✓).
- **SVM + suffixes (Test-7 vs 6):** recall −10.6 (text "10 points" ✓); precision +13.3 / +16.2 / +19.8 (Conclusion "13% to 20%" ✓).

### Other extraction results (checked on page images)

- Rule-based extraction (Table 5.4, p. 48): TP 137, FN 289, recall 32.2%, precision 15.4% / 20.3% / 32.5%.
- k = 10 filtering (Table 5.17, p. 62): base recall 88.4%; best SVM + suffixes CRA precision 92.0%.
- Automatic dependency parsing instead of gold (Table 5.19, p. 63): recall 76.5 → 62.9% and 73.7 → 60.2%; precision falls by 5.6–13.4 points, mean 8.85 **[computed]**.
- Expert dataset (Table 5.20, p. 64): recall 65.8% / 60.7%; precision CWA 37.0% / 38.2%, CRA 65.3% / 67.0%.

## 10. Statistical evidence

- **Significance tests:** NOT_REPORTED for retrieval and extraction.
- **Confidence intervals:** NOT_REPORTED.
- **Runs / seeds:** NOT_REPORTED for the reported results (the thesis only says that repeated tests on the same training set were used to choose annealing parameters with less variance between successive runs, p. 35). Simulated annealing is stochastic, and one table pattern suggests separate runs (Test-4: MC = 2 has more TP than MC = 1, 401 vs 361, although MC = 2 is described as post-filtering the learned rules; Table 5.11/5.16). Our inference, not stated by the author.
- **Ablation:** none for retrieval (one lexical representation, one relation extractor). For extraction, the L/A/0/S variations and gold-vs-automatic parsing act as ablations.
- **Per-query analysis:** none. No per-query recall/precision, no list of failed queries, no overlap between the two retrieval methods' returned or relevant sets.
- **Tuning / leakage:** the data filtering for extraction was applied to the whole dataset including test folds, stated as intentional (pp. 40–41, 64). For retrieval, whether the template-building tagged reports overlap the 53 test reports is NOT_REPORTED.

## 11. Strengths

- Real clinical Turkish text from a hospital, with a physician-built retrieval test set with exhaustive judgments over all 53 × 100 pairs.
- Honest, concrete description of a practical morphology problem: a lexicon-based Turkish analyzer fails on inflected medical loanwords, and a surface-suffix fallback is used (Sec. 4.2.1).
- Full TP/FN/FP counts for extraction, under three error definitions, so readers can recompute everything.
- Extraction variations isolate the effect of lexicalized (root) features vs abstract morphological features, with a clear precision/recall trade-off.
- The effect of automatic vs gold dependency parsing is measured separately.

## 12. Limitations

### Stated by the author

- The rule-based retrieval "did not achieve the desired performance", attributed to "the breadth of the test set which contained different kinds of radiology reports, and errors related with manually constructing the rules" (p. 69).
- Rule-based extraction suffers from "incorrect extraction of phrase boundaries" (p. 48, p. 69).
- The small dataset prevented training the morphological disambiguator (p. 66, p. 71).
- Closed-world error counting is too strict for incompletely tagged data (p. 69).
- The expert dataset could not be filtered; lower results are attributed to tagging quality (p. 64, p. 67).
- No medical lexicon or ontology was used, by design; "a medical lexicon or ontology would increase these results significantly" (p. 72).

### Inferred from the experimental design

1. **Tiny retrieval collection:** 53 documents, and (under micro-averaging) only 76–228 relevant pairs in total. One physician built queries and judgments; no agreement.
2. **Unranked Boolean retrieval.** One operating point per configuration; no ranked lexical baseline (tf-idf/BM25). A weighted ranker could reduce the precision problem caused by generic words.
3. **Morphology is not varied in retrieval.** Only root lexemes are used for the baseline. The analyzer, handling of unanalyzable words and ambiguity resolution for the baseline are NOT_REPORTED, so even the one representation is not reproducible.
4. **Query style favours word overlap.** Queries are partial sentences in report style, which gives the bag-of-roots baseline very high recall and very low precision. Results may differ for keyword queries.
5. **Micro vs macro averaging not stated.** With few relevant pairs, a few queries may dominate.
6. **Different denominators inside the comparison tables.** Rule-based extraction TP+FN = 426 vs 528 for data-driven methods in the same Table 5.16; Table 5.17 has 447, 442 and 396 **[computed]**. The rule-based and data-driven rows are not compared on the same gold set, or the reason is not explained.
7. **No per-query analysis and no comparison of what each method finds**, although the two methods are natural "channels".
8. **Possible template–test overlap** in retrieval (not reported).

## 13. What the work proves

- On a tiny Turkish radiology collection with report-style queries, **Boolean matching on root lexemes has near-complete recall (96.05%) but very low precision (5.15–5.46%)**, while **matching extracted relations trades recall (65.78–67.10%) for about 5.6–5.9 times higher precision (28.65–31.84%)** (Table 5.1). Unranked, single assessor, no significance test.
- For relation **extraction** from Turkish radiology text, **adding root lexemes as rule features raises precision but costs a lot of recall** (overfitting, per the author); when zero-error rules are also disallowed, recall recovers (+2.9/+3.2 points vs base) but the precision gain is almost lost (Table 5.10). 2–3-letter root endings give a milder version of the same trade-off in the simulated-annealing learner (Table 5.13); in the SVM learner they cost 10.6 recall points for +13.3 to +19.8 precision points (Table 5.15).
- Automatic dependency parsing lowers extraction recall by about 13.5 points relative to gold parses, measured only for the base simulated-annealing test (Table 5.19).
- Qualitatively: a lexicon-based Turkish analyzer does not cover inflected medical loanwords, and a surface-suffix fallback is needed (Sec. 4.2.1). No coverage rate is reported.

## 14. What the work does NOT prove

- **Anything about which lexical morphological representation is better for retrieval.** There is no raw vs stem vs root/lemma comparison in retrieval.
- **Anything about BM25, ranked lexical retrieval, dense retrieval or hybrid retrieval.** None are evaluated.
- **That the two retrieval methods are complementary**, or that combining them would help. No overlap, unique relevant hits, oracle union or fusion is computed.
- **That relation-based retrieval beats a reasonable lexical baseline.** The baseline is an unweighted Boolean set match; a ranked tf-idf/BM25 model was not tested.
- **Which queries each method fails on, or why.** No per-query or query-feature analysis.
- **Generalization.** 53 reports, 100 queries, one assessor, one hospital.
- **That root features help retrieval.** The root-lexeme results in Ch. 5.2 are extraction features, not retrieval representations.

## 15. Relationship to current Uzbek evidence

- **No Uzbek data.** Turkish is the closest well-studied Turkic relative; the agglutinative morphology problems described (inflected out-of-lexicon loanwords, ambiguity, derivational boundaries) are relevant in spirit to Uzbek.
- Compared with the other Turkish cards:
  - **MORPH-001** (Can et al., 2008) and **MORPH-002** (Haddad & Bechikh Ali, 2014) compare several stemming/lemmatization options on the large Milliyet news collection with ranked models (MORPH-002 includes BM25 and Zemberek; MORPH-001 uses a lemmatizer with a fallback for unanalyzable forms) [project index; MORPH-001 card].
  - This thesis adds only a **domain-specific** (clinical) setting and a qualitative note on analyzer coverage. It has no representation comparison and no ranking.
  - Kılıç (2008, CR002145), Öcalan (2009, CR002158) and Fidan (2012, CR002210) cards are closer to our design on the lexical side [project cards].
- Context (not from the paper): Uzbek domain terms borrowed from Russian/European languages, written in different ways (Latin/Cyrillic, apostrophe variants), are a plausible Uzbek analogue of the radiologists' inconsistent spelling of Western medical terms (p. 2). Uzbek morphological analyzers (Bakaev, Xusainova, Elov; `MASTER_INDEX` PHD-UZ-001/003/004) also rely on lexicons, so the coverage problem is likely to transfer.

## 16. Relationship to CURRENT_GAP

**Classification:** *no material effect* (weakly *supports* the practical motivation).

- v0.8 elements **not touched:** BM25_raw / BM25_stem / BM25_lemma; a fixed dense retriever D; fusion (H_raw/H_stem/H_lemma); unique relevant hits, overlap, oracle union, incremental hybrid gain; per-query links to query features. None are present.
- The work does not affect any "what can still kill this gap" condition: no Uzbek benchmark, no per-query overlap analysis, and no Turkic study of the interaction mechanism.
- Weak support: it shows qualitatively that morphological analysis of Turkic domain text fails on out-of-lexicon terms and needs a fallback. This supports treating analyzer coverage / OOV rate and orthographic variation as **candidate query features** (already listed in CURRENT_GAP: rare terms, Unicode/apostrophe variation, domain).
- The triage coding `carries_complementarity_evidence = NO` is correct: two retrieval representations exist, but their results are never compared per query or combined.

**Proposal:** keep v0.8 refined unchanged. Optionally cite as a Turkic domain-specific example where root-based lexical matching is used without any representation comparison. This is a proposal only; `CURRENT_GAP.md` has not been edited.

## 17. Implications for our research design

- **Lemma/root channel definition.** For BM25_lemma (and BM25_stem), fix and report in advance:
  - the analyzer and its version;
  - how ambiguous analyses are resolved (first analysis, disambiguator, most frequent);
  - the **fallback for unanalyzable words** (keep surface form, apply a rule-based suffix stripper, or truncate). This thesis needed such a fallback for out-of-lexicon domain terms in its rule-based method (Sec. 4.2.1), but it does not measure the fallback's effect, and it leaves the baseline's handling unreported.
- **Query taxonomy.** Add per-query **analyzer coverage** (share of query tokens the analyzer cannot analyze) and **orthographic variant presence** (loanword spelling variants, Latin/Cyrillic, apostrophe forms) as candidate features. Also code **query formulation style** (keyword vs document-style fragment), since document-style queries inflated the recall of word matching here.
- **Qrels and reporting.** Report the number of relevant documents per query and the averaging method; use ranked metrics (nDCG@10, Recall@100, MAP) over pooled judgments; avoid collections where the total number of relevant pairs is in the tens.
- **Baselines.** Any structured or semantic channel must be compared with a **ranked** lexical baseline (BM25), not a Boolean match; otherwise precision gains may reflect missing term weighting.
- **Complementarity measurement.** Even with two very different representations (bag of roots vs relations), this work never computes the relevant-set overlap. Our protocol should compute, per query, relevant-only-in-A, only-in-B, both and the union for every lexical variant vs D.
- **Protocol hygiene.** Keep any resource-building data (templates, dictionaries, tuning) separate from the test queries and documents; do not filter the test set using test labels.
- **Hypothesis.** No evidence for or against our hypothesis.

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| Root lexeme | The dictionary root a word is built from, with all suffixes removed | Root output of a morphological analyzer (here, per the thesis, Zemberek or TRMorph) |
| Morpheme / inflectional group (IG) | Smallest meaningful part of a word; in Turkish, a word can be split at derivational suffixes into IGs, each with its own part of speech | Turkish Treebank sublexical unit separated by derivational boundaries |
| Surface-suffix fallback | If the analyzer cannot parse a word, look at its last letters instead of its analysed morphemes | String-suffix matching used when morphological analysis fails |
| Morphological disambiguation | Choosing the correct analysis when a word has several | Selection among alternative analyses (Yuret & Türe decision lists) |
| Information extraction | Turning free text into structured facts (who/what/where) | Relation extraction into typed, labelled structures |
| Conceptual graph | A small graph of concepts linked by labelled relations | Sowa's bipartite concept/relation graph (Sec. 3.4) |
| Set (Boolean) retrieval | A document is either returned or not, with no ranking | Retrieval by a set predicate, evaluated by precision/recall |
| Micro vs macro averaging | Pooling all query–document pairs vs averaging per query | Micro: ratios of summed counts; macro: mean of per-query ratios |
| CWA / CCA / CRA | Strict to lenient ways of counting wrong extractions when gold tags are incomplete | Closed-world, closed-concepts, closed-relations assumptions (Sec. 5.2.1) |
| Complementarity (project term) | Each channel finds relevant documents the other misses | Unique relevant hits, overlap, oracle-union gain |

## 19. Open questions / verification needed

1. **Baseline lexical representation:** analyzer, ambiguity handling and treatment of unanalyzable words for the root-lexeme baseline: NOT_REPORTED.
2. **Retrieval qrels:** number of relevant reports per query and averaging method. Our reconstruction (R ∈ {76, 152, 228} under micro-averaging) is an inference only.
3. **Template–test overlap** for the rule-based retriever: NOT_REPORTED.
4. **Internal inconsistencies to note when citing:**
   - expert-set precision "37.0% to 64.3%" (p. 66) vs Table 5.20 (MC = 1) and p. 72 (65.3%; 67.0% at MC = 2);
   - parsing-induced precision drop "8 points in average" (p. 63) vs "6%" (p. 71); computed mean 8.85 points;
   - root-lexeme precision gain "at least ten percent in all cases" (p. 52; true only as a relative change) vs "13%" (p. 70) vs table (+8.9 to +20.1 points);
   - suffix recall drop "3 to 5 points" (p. 55) vs table (4.5 and 5.5 points);
   - Table 5.4 labels the middle error definition "CPA", elsewhere "CCA";
   - unequal gold denominators within Tables 5.16–5.17 (426 / 528; 447 / 442 / 396);
   - Test-4 TP higher at MC = 2 than at MC = 1 despite post-filtering;
   - Ch. 5 intro announces "two different datasets" (p. 42) but a third (expert) dataset is used in Sec. 5.2.6.
5. **Bibliographic record:** official METU/YÖK record (thesis number, defense date) not verified; the supplied copy's approval page is unsigned and undated.

## 20. Decision after deep dive

- **Keep current gap?** Yes. v0.8 refined remains valid (§16).
- **Modify gap?** No.
- **Add decision?** Proposed for `decisions/DECISIONS.md` (researcher's decision): "For stem/lemma channels, the analyzer, ambiguity resolution and the fallback for unanalyzable tokens must be fixed and reported, and per-query analyzer coverage logged as a query feature."
- **Add experiment?** No new experiment. Optionally include per-query analyzer coverage in the planned query-feature analysis.
- **Add citation to Chapter I?** Optional, minor: §1.1 (morphological normalization in Turkic lexical retrieval; analyzer coverage problems in specialized domains). Not suitable as evidence for dense or hybrid retrieval.
- **Proposed `MASTER_INDEX.md` row** (to add after approval):

| MORPH-028 | Hadımlı — *Processing Turkish Radiology Reports* (M.Sc. thesis, METU, 2011; sup. G. Üçoluk, co-sup. M. Turhan Yöndem) — [deep dive](deep-dives/2011_Hadimli_Turkish_Radiology_Reports_Retrieval_Extraction.md) | 2011 | B | LOW | Mainly relation extraction from Turkish radiology reports. Retrieval: 53 reports, 100 report-style queries, one physician; unranked set matching. Root-lexeme Boolean baseline R 96.05% / P 5.15–5.46% vs relation-based R 65.78–67.10% / P 28.65–31.84% (Table 5.1). Zemberek with surface-suffix fallback for out-of-lexicon medical terms. No raw/stem/root comparison in retrieval, no BM25, dense, fusion, overlap/unique-hit or per-query analysis. Several internal numeric inconsistencies. |
