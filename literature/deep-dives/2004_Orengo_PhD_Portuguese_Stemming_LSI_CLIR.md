# Orengo (2004): Assessing Relevance Using Automatically Translated Documents for Cross-Language Information Retrieval (PhD thesis, Middlesex University)

**Targeted deep-dive status:** COMPLETED (AI-assisted, pending researcher review)
**Completed:** 2026-09-28
**Literature ID:** `MORPH-020` (assigned 2026-09-28, approved by researcher)
**Systematic-review record:** `CR002114`. Full-text triage: INCLUDE, reading priority HIGH, reading tier 1, `carries_complementarity_evidence = YES`. Triage note: "Complementarity YES refers to topic-by-topic relevance-feedback results in Ch. 5, not to the stemming comparison"; the RSLP stemmer is also published separately (Orengo & Huyck 2001).
**Provenance:** AI-assisted deep dive (Claude). The 268-page PDF was navigated through the table of contents and grep. Read in full: abstract, Ch. 1 objectives, Ch. 2.1.2 (evaluation), 2.3–2.4 (LSI, CLIR with LSI), 2.5.2.4 and 2.5.3 (RF on LSI, residual collection), **Ch. 3 (stemmer, pp. 48–61), Ch. 4 (CLIR–LSI experiments, pp. 62–74), Ch. 5 (RF user experiment, pp. 75–106)**, Ch. 6–7 (pp. 107–121), Appendix E header and E5.1. Appendix A (199 stemming rules) and Appendices B–D (questionnaires, documents, CLEF judgements) were not read line by line. **Pages checked visually** (printed page / PDF page): 56/65, 58/67, 59/68, 60/69 (stemmer evaluation, Tables 3.1–3.3, UI/OI); 64/73 (Table 4.1); 68/77 (Table 4.2); 70/79 (Table 4.3); 71/80 (Figure 4.7); 79/88 (Figure 5.1); 94/103 (Table 5.10); 100/109 (Table 5.15); 249/258 (Appendix E5.1 correlation matrix). Every number from these tables was compared with the page image. Printed page = PDF page − 9. Numbers computed by us are marked **[computed]** (recomputed with Python).
**Source rule:** **the thesis is the primary and only authoritative source** for what the author did and found. The web was used only to check the bibliographic record. Background knowledge appears only as labelled "Context (not from the thesis)".
**Verification:** independent AI verifier pass 2026-09-28; 10 findings addressed.
**Reliability:** **A** by source type (doctoral thesis, Middlesex University, March 2004; record in PQDT – UK & Ireland per the assignment metadata). Evidential weight for this project is **narrow**: a 2004 LSI-based CLIR system, stemming effects reported as single aggregate numbers per collection with no significance test, and several internal numerical inconsistencies (§9, §19).

---

## Кратко для исследователя (RU)

- **Что это.** PhD (Middlesex University, 2004; руководитель — Dr. Christian Huyck, по благодарностям). Три блока: (1) стеммер RSLP для португальского (Гл. 3); (2) португальско-английский межъязыковой поиск (CLIR) на основе латентно-семантического индексирования (LSI) на четырёх коллекциях (Гл. 4); (3) пользовательский эксперимент с relevance feedback (RF): 27 носителей португальского оценивают английские, машинно- и вручную переведённые документы (Гл. 5).
- **Морфологические варианты есть, но входят не в лексический канал, а во вход LSI.** Три условия (Sec. 4.4.4, Table 4.3, p. 70): RSLP для португальского текста (+ Porter для английского), португальский Porter (+ Porter для английского) и «без стемминга ни в одном языке». Лемматизации нет. Метрика — одно число «average precision» на коллекцию и число найденных релевантных в top-100.
- **Главные числа (Table 4.3, p. 70):** Time 34.16 / 33.06 / 31.61; Cranfield 26.60 / 25.97 / 23.83; CISI 12.56 / 12.29 / 10.72; LA Times 20.85 / 16.46 / 18.93 (RSLP / Porter / без стемминга, %). Стемминг RSLP против отсутствия стемминга: +8.1…+17.2% относительно **[computed]** — совпадает с «8–17%» автора.
- **Внутренние несоответствия (проверены по изображениям страниц):**
  - автор пишет о среднем +12% RSLP над Porter на малых коллекциях, а по Table 4.3 выходит +2.2…+3.3% (в среднем 2.65%) **[computed]**; 12.3% — это среднее RSLP против «без стемминга»;
  - «RSLP лучше во всех экспериментах, в том числе по числу найденных релевантных» — неверно для Time (299 против 306 у Porter и 301 без стемминга);
  - на LA Times португальский Porter **хуже**, чем отсутствие стемминга (16.46 против 18.93);
  - пример расчёта OI Пайса: 12/156 = 0.077, а напечатано 0.083 **[computed]**;
  - в Table 4.2 для Time напечатано то же число терминов, что для Cranfield (2629/1979), вопреки Table 4.1 (7596);
  - Bilingual для LA Times: 17.09% (Table 4.2) против 20.85% (Table 4.3) при одинаковых 69 996 терминах — разница не объяснена;
  - r = −0.40 между исходной точностью и приростом от RF (p. 99, «see page 249»), а в Appendix E5.1 на p. 249 стоит r = −0.219.
- **Нет:** BM25 или другой отдельной лексической модели в экспериментах со стеммингом, современного dense retrieval (LSI — ранняя латентная, «плотная» модель без обучения на релевантности), fusion/гибрида, перекрытия результатов между каналами, уникально найденных релевантных документов, oracle union между каналами, тестов значимости для стемминга, анализа по запросам для стемминга.
- **Что есть по запросам (Гл. 5, не про стемминг):** прирост от RF сильно зависит от темы (−52%…+128%, Table 5.15, p. 100); выбор для каждой темы набора оценок, давшего лучший результат («Optimal»; входят ли официальные оценки CLEF в число кандидатов, не сказано) даёт +85.4% против +12.6% у официальных оценок CLEF (Table 5.10, p. 94). Это oracle-выбор среди источников обратной связи, а **не** взаимодополняемость каналов поиска. Всего 6 тем; сам автор пишет, что для анализа характеристик тем их слишком мало. Флаг триажа «complementarity YES» предлагается понизить до «косвенно».
- **Для нашего gap:** работа исторически показывает, что стемминг перед семантической моделью (LSI) уже изучался в 2004 г. Ядро v0.8 (raw/stem/lemma BM25 × фиксированная D → перекрытие / уникальные попадания → прирост гибрида → признаки запросов) **не затрагивает**. Предложение: gap не менять.
- **Практическая польза:**
  1. В LSI стемминг меняет само семантическое пространство, поэтому эффект морфологии и эффект семантической модели там неразделимы. Это аргумент за наше решение держать D фиксированной на исходном тексте.
  2. Внутренняя оценка стеммера по Пайсу (индексы UI/OI на концептуальных группах) полезна для выбора узбекского стеммера/лемматизатора до IR-экспериментов.
  3. Выбор стеммера может перевернуть знак эффекта на отдельной коллекции (Porter на LA Times) — нужны несколько коллекций/доменов и потапросный анализ.
  4. Относительные приросты надо пересчитывать самим: у автора смешаны знаменатели.

---

## 1. Bibliographic record

- **Author:** Viviane Moreira Orengo
- **Year:** 2004 (title page: "March 2004")
- **Degree / university:** Ph.D., Middlesex University (title page: "A thesis submitted to Middlesex University in partial fulfilment of the requirements for the degree of Ph.D.")
- **Supervisor:** Dr. Christian Huyck (Acknowledgements: "for the excellent supervision"). The PDF does not state the formal supervisory team or the defence date.
- **Length:** 268 PDF pages (121 printed pages of main text + references + Appendices A–E)
- **Venue metadata (assignment):** PQDT – UK & Ireland, document type THES
- **DOI:** none known; NOT_REPORTED in the PDF
- **Repository:** (bibliographic check: web search, 2026-09-28) a web search returned a Middlesex University Research Repository PDF (`repository.mdx.ac.uk/download/.../568474.pdf`) listed under this title; the record page could not be opened (HTTP 405), so the repository item ID, award date and final record fields are **not verified**.
- **Related publications by the author cited in the thesis:** Moreira Orengo & Huyck (2001), *A Stemming Algorithm for the Portuguese Language*, SPIRE 2001 (Ch. 3 is based on it, p. 48; reference list, p. 130); Moreira Orengo & Huyck (2003), *Portuguese-English Cross-Language Information Retrieval Using Latent Semantic Indexing*, CLEF 2002 workshop, LNCS 2785 (reference list, p. 130). Possible overlap with other systematic-review records.
- **Source type:** doctoral thesis
- **Reliability:** A (source type); narrow evidential weight for this project
- **Full text available:** yes (`07_full_text/pdfs/CR002114.pdf`)

## 2. Why this work matters to the PhD

| Axis | Relation |
|---|---|
| Lexical retrieval | Indirect. Stemming is applied to the term-by-document matrix that feeds LSI. No standalone lexical ranking model (VSM, BM25) is evaluated in the stemming experiment |
| Semantic retrieval | LSI (latent semantic indexing, SVD-based) is the retrieval model for all experiments. Context (not from the thesis): LSI is an early unsupervised "semantic" model with dense vectors; it is not a retrieval-trained dense retriever. The thesis itself notes "the vectors generated by LSI are dense" (Sec. 6.4.1, p. 114) |
| Hybrid retrieval | **Absent.** No fusion of lexical and LSI scores |
| Morphology | **Direct but narrow:** a rule-based Portuguese suffix-stripping stemmer (RSLP) with intrinsic evaluation, and a no-stem / Porter / RSLP comparison inside LSI-based CLIR |
| Uzbek / low-resource | Indirect: Portuguese in 2001–2004 is described as under-resourced for IR (Sec. 4.1, p. 63); inflectional morphology (plural, gender, diminutive/augmentative, >50 verb forms) motivates a language-specific stemmer. Portuguese is fusional, not agglutinative |
| Current gap | No material effect on the v0.8 core; it adds a historical data point that "morphological preprocessing + semantic model" is old (§16) |

## 3. Research problem

### Simple explanation

The author wants Portuguese speakers who read little English to search English documents with Portuguese queries. For that she needs (a) Portuguese language tools, above all a stemmer; (b) a cross-language search system; (c) an understanding of whether users can judge the relevance of foreign or machine-translated documents well enough for relevance feedback to work.

### Formal formulation

The thesis states two main research questions (Abstract; Sec. 1.1, pp. 1–3):

1. How well do users assess the relevance of texts in a foreign language, of texts hand-translated into their language and of texts machine-translated into their language?
2. What is the relationship between the accuracy of users' judgements and the improvement achieved by RF?

Supporting contributions (Sec. 7.1, pp. 117–119): a new language pair for CLIR, a Portuguese stemming algorithm, and "several LSI–CLIR experiments", including the stemming experiment. **The stemming experiment is a side experiment, not a research question of the thesis.**

## 4. Main idea

### Simple explanation

- **Stemmer.** Cut Portuguese suffixes by ordered rule steps (plural → feminine → adverb → augmentative/diminutive → noun → verb → final vowel → accents, following the step numbering of Sec. 3.2; Figure 3.1, p. 50, draws augmentative before adverb). Each rule has a minimum stem length and a list of exceptions.
- **CLIR with LSI.** Machine-translate part of an English collection into Portuguese, glue each document to its translation ("dual-language document"), and build one LSI space from these pairs. Words that co-occur across the two halves (e.g., *car* / *carro*) end up close in the space, so a Portuguese query can find English documents.
- **Stemming inside LSI.** Stemming merges word forms, so co-occurrence counts are pooled and cross-language matches are, in the author's words, better supported.

### Concrete example

- The thesis's own example (Sec. 3.2, Step 7, p. 53): *menino, menina, meninice, meninão, menininho* all become the stem *menin*.
- Dual-language document before and after stemming (Figures 4.3–4.4, p. 65): English "branches" → *branch*; SYSTRAN's Portuguese "filiais" (wrong sense: shop branches) → *filial*. The translation error is kept ("no corrections were performed", p. 65).

### Formal method

- Term-by-document matrix entries = log-entropy weights (Eqs. 19–20, p. 66): `L(i,j) = log(tf_ij + 1)`, `G(i) = 1 − Σ_j [p_ij log p_ij / log N]`, `p_ij = tf_ij / gf_i`.
- Truncated SVD `A_k = T S Dᵀ` with k dimensions (Fig. 2.6, p. 26). English-only documents are "folded in" ("placing them at the average of their corresponding terms", pp. 26, 34); queries are pseudo-documents "placed at the weighted sum of its component term vectors" (p. 27); ranking by cosine (Sec. 2.3.1, pp. 26–27; Sec. 5.3.4, p. 83).
- RF (Ch. 5): method RF3 = replace the query by the centroid of the documents judged relevant (Sec. 5.2, p. 78).

## 5. Architecture / algorithm

1. **RSLP stemmer** (Sec. 3.2, pp. 49–53): implemented in C; 8 ordered steps; 199 rules (full list in Appendix A). Each rule = suffix, minimum stem length, optional replacement suffix, exception list. Exception lists were built with a 32,000-word Portuguese vocabulary from Snowball; "exceptions list reduce overstemming mistakes by 5%" (p. 51). Verb forms are reduced to the root, not the infinitive, "as it would not be possible to reduce them to their infinitive without dictionary lookups" (p. 53). Proper names are stemmed too (p. 55). The author notes: "the stems do not have to be linguistically meaningful, since they are used to index a database of documents and are not presented to the user" (p. 51).
2. **Comparator stemmer:** the Portuguese version of the Porter algorithm, described as "a translation of the original English version" (Sec. 3.4, p. 55).
3. **CLIR corpora construction** (Sec. 4.3–4.4, pp. 64–66):
   - Small collections (Time, Cranfield, CISI): documents with odd IDs (half) and all queries machine-translated by SYSTRAN.
   - LA Times: 20% of documents translated (one in five daily files); Portuguese topics from CLEF.
   - Stop-word removal with Snowball lists; **English texts stemmed with Porter, Portuguese texts with RSLP; queries stemmed too** (p. 65).
   - Each translated document merged with its original → dual-language document; the LSI space is derived from these; remaining English-only documents folded in.
   - Telcordia LSI software; 100 documents retrieved per query in all runs (p. 66).
   - Terms occurring in only one document discarded (Table 4.1 footnote, p. 64).
4. **Dimensions** (Sec. 4.4.2, p. 67): 100 for the small collections; for LA Times "an optimal number could not be established"; the software could not index the whole collection above 400 dimensions; with only 20% indexed (Ch. 5), 700 dimensions were reached. The stemming experiment used 100 (small) and 700 (LA Times) dimensions (p. 70).
5. **Stemming experiment** (Sec. 4.4.4, p. 70): "(i) Stemming the Portuguese texts using the stemmer proposed here; (ii) Stemming the Portuguese texts using the Portuguese version of the Porter Stemmer; and (iii) no stemming on any texts."
   - In (i) and (ii) the English side is Porter-stemmed (p. 65); in (iii) neither language is stemmed. So (iii) vs (i) changes **both** languages' preprocessing at once **[inferred from pp. 65 and 70]**.
   - The LSI space is re-derived for each condition: the latent space itself changes with the morphological representation **[inferred]**.
6. **RF user experiment** (Ch. 5): LA Times, 20% dual-language, 700 dimensions (Sec. 5.3.2, p. 81); six CLEF 2002 topics; top-10 documents shown per topic; three presentation "systems": S1 original English, S2 SYSTRAN MT, S3 hand translation by the author (p. 84); Latin-square design; "not sure" mapped to non-relevant (p. 86); RF3 feedback; residual-collection evaluation (p. 93).

## 6. Data

### Chapter 4 (stemming and CLIR experiments), Table 4.1, p. 64

| | Time | Cranfield | CISI | LA Times |
|---|---:|---:|---:|---:|
| Documents | 425 | 1,400 | 1,460 | 113,005 |
| Queries | 83 | 225 | 112 | 50 |
| Unique terms (monolingual; terms in only one document discarded) | 7,596 | 2,629 | 3,121 | 91,190 |
| Relevant documents | 324 | 1,838 | 3,114 | 821 |

- **Languages:** English documents; Portuguese queries (SYSTRAN translations for the small collections, CLEF Portuguese topics for LA Times).
- **Domains:** news (Time 1963, LA Times 1994), aeronautics abstracts (Cranfield), library-science abstracts (CISI).
- **Relevance judgements:** the collections' existing qrels (University of Tennessee distribution for the three small collections; CLEF for LA Times).
- **Train/dev/test:** no split. The number of LSI dimensions was chosen by running retrieval evaluations with different values (Sec. 4.4.2, Figure 4.5, p. 67) on the same collections and queries used for evaluation.
- **LA Times query count:** Ch. 5 states that 8 of the 50 CLEF 2002 topics have no relevant documents (p. 79). Whether Ch. 4 averages over 50 or 42 topics is NOT_REPORTED.

### Chapter 3 (intrinsic stemmer evaluation)

- 32,000 distinct Portuguese word forms (Snowball vocabulary) for vocabulary reduction and timing (p. 55).
- 2,800 words with manually assigned stems for rule development (training) and 1,000 further words as a held-out test set (p. 56).
- 1,000 words in 170 concept groups for Paice's evaluation (p. 60). Who built the groups and how is NOT_REPORTED.

### Chapter 5 (user experiment)

- LA Times 1994, 113,005 documents, 69,996 unique bilingual terms, 821 relevant (Table 5.1, p. 81).
- 6 topics randomly selected from 17 of the 50 CLEF 2002 topics that had >10 relevant documents and at least one relevant document in the top 10 (pp. 81–82).
- 27 Portuguese-speaking participants (students/lecturers, UCPel, Brazil), 60 judgements each, 1,620 in total (pp. 80, 84). Extra groups: 6 bilingual Portuguese speakers and 6 native English speakers (Sec. 5.4.4, pp. 91–92).

## 7. Baselines

| Baseline / condition | What it is | Why selected | Fair comparison? |
|---|---|---|---|
| No stemming (Table 4.3) | LSI on unstemmed English and Portuguese text | Reference for the effect of stemming | **Partly.** It removes stemming from both languages, so it does not isolate the Portuguese stemmer's effect |
| Portuguese Porter (Table 4.3) | Translated Porter rules for Portuguese | The "only other Portuguese stemmer publicly available" (p. 48) | Yes for the stemmer-vs-stemmer comparison: same k, same collection, and (by the general procedure on p. 65) the same English Porter stemming **[inferred]**; Sec. 4.4.4 describes only the Portuguese side of run (ii) |
| Porter-PT in intrinsic tests (Ch. 3) | Same | Same | Yes, same word samples. But the rules and exceptions of RSLP were developed on the 2,800-word training set of the same vocabulary; the 1,000-word test set is held out from that training set (p. 56). The exception lists were built with the whole 32,000-word Snowball vocabulary (p. 51), from which the test words were apparently also drawn, so the test set may not be fully independent of the exception lists **[inferred]** |
| Mono-all / Mono-half (Table 4.2) | Monolingual English LSI with all documents in the SVD, or half in the SVD and half folded in | Quantifies the cost of the cross-language setting | Reasonable; Mono-half controls for folding in. The stemming setting of monolingual runs is NOT_REPORTED |
| RF baseline (Ch. 5) | Initial LSI ranking, residual collection | Standard RF evaluation | Yes. RF3 was chosen on the same LA Times collection with the CLEF 2002 topics (32 topics with a relevant document in the top 20; English topic versions and English documents; Sec. 5.2, p. 79), i.e. method selection overlaps the evaluation topics |

**No standalone lexical model (VSM or BM25) is run anywhere in the retrieval experiments**, so there is no lexical-vs-LSI comparison.

## 8. Metrics

| Metric | Definition in the thesis | Simple meaning | Comment |
|---|---|---|---|
| "Average Precision" (Tables 4.2, 4.3, 5.10) | Sec. 2.1.2 (pp. 11–13) defines interpolated precision at 11 recall points and averaging over queries (Eq. 6), but not the exact single-number summary used in the tables | "How high the relevant documents are ranked, averaged over queries" | Whether it is non-interpolated MAP or an 11-point average is **NOT_REPORTED**; the evaluation software is not named ("the evaluation software", p. 86). Ranking depth is 100 (p. 66) |
| Relevant Retrieved | Total number of relevant documents in the top 100 summed over all queries (Tables 4.2–4.3) | A recall-like count at depth 100 | Only totals; no per-query breakdown |
| Number of Terms | Index vocabulary size after preprocessing | How much stemming shrinks the vocabulary | Descriptive |
| Recall–precision curves | Figures 4.6, 4.7, 5.1, 5.8 | Precision at each recall level | Figures only |
| Paice UI / OI | Understemming index = GUMT/GDMT; overstemming index = GWMT/GDNT (Eqs. 15–18, pp. 57–58) | UI: how often forms of the same concept are *not* merged; OI: how often forms of different concepts *are* merged | Intrinsic stemmer quality, not retrieval quality |
| Stem accuracy | Share of words given the manually assigned correct stem (p. 56) | Plain accuracy against a gold stem | Intrinsic |
| Overlap (Ch. 5) | Lesk & Salton: intersection / union of the relevant sets of two judges, on the 10 shown documents (Sec. 5.4.2, p. 87) | Agreement between a participant and CLEF assessors | **Not** retrieval-channel overlap in our sense |
| Change in precision (Ch. 5) | Residual-collection average precision after RF vs before | Gain from RF per participant/topic | Residual collection removes judged documents from evaluation (Sec. 2.5.3, p. 45) |

## 9. Results

### Intrinsic stemmer evaluation (Ch. 3; pages 55–60 checked visually)

| Measure | Porter-PT | RSLP | Location |
|---|---:|---:|---|
| Vocabulary reduction on 32,000 words | 44% | 51% | Sec. 3.4.1, pp. 55–56 |
| Correct stem, training set (2,800 words) | — | 98% | Sec. 3.4.2, p. 56 |
| Correct stem, held-out test set (1,000 words) | 71% | 96% | Sec. 3.4.2, p. 56 |
| Understemming index UI (1,000 words, 170 groups) | 0.215 | 0.034 | Sec. 3.4.3.2, p. 60 |
| Overstemming index OI | 2.11 × 10⁻⁴ | 9.85 × 10⁻⁵ | Sec. 3.4.3.2, p. 60 |

- Stemming the 32,000 words took 12 seconds "on a low end PC" (p. 55).
- **Paice worked example (Tables 3.1–3.3, pp. 58–59):** GDMT = 34, GDNT = 156, GUMT = 3, GWMT = 12 — all confirmed **[computed]**. UI = 3/34 = 0.088 ✓. **OI = 12/156 = 0.077 [computed], but the thesis prints 0.083** (p. 59). 0.083 would equal 12/144 or 13/156; the source of the difference is not explained. This affects only the illustrative example, not the RSLP vs Porter-PT comparison.
- The chapter says RSLP "performs significantly better" than Porter-PT (p. 48). **No statistical test is reported** for any of these comparisons; "significantly" is used informally.

### Table 4.3 — stemming experiment inside LSI-based CLIR (p. 70; checked visually)

"Bilingual" = RSLP on Portuguese + Porter on English (p. 65); "Bilingual-Porter" = Porter-PT on Portuguese + Porter on English (English side **[inferred]** from the general procedure on p. 65; Sec. 4.4.4 names only the Portuguese stemmer); "No Stemming" = no stemming on any texts. k = 100 (small collections), 700 (LA Times).

| Collection | Measure | RSLP | Porter-PT | No stemming |
|---|---|---:|---:|---:|
| Time | Number of terms | 8,779 | 8,854 | 12,049 |
| | Average precision | **34.16%** | 33.06% | 31.61% |
| | Relevant retrieved (of 324) | 299 | **306** | 301 |
| Cranfield | Number of terms | 3,429 | 3,624 | 5,660 |
| | Average precision | **26.60%** | 25.97% | 23.83% |
| | Relevant retrieved (of 1,838) | **1,382** | 1,368 | 1,366 |
| CISI | Number of terms | 3,875 | 4,116 | 6,791 |
| | Average precision | **12.56%** | 12.29% | 10.72% |
| | Relevant retrieved (of 3,114) | **1,097** | 1,069 | 950 |
| LA Times | Number of terms | 69,996 | 74,163 | 96,945 |
| | Average precision | **20.85%** | 16.46% | 18.93% |
| | Relevant retrieved (of 821) | **694** | 658 | 671 |

Derived values **[computed]**:

| Collection | RSLP vs no stem (rel. / abs.) | RSLP vs Porter-PT (rel. / abs.) | Porter-PT vs no stem (rel.) | Vocabulary reduction RSLP vs no stem |
|---|---:|---:|---:|---:|
| Time | +8.1% / +2.55 pts | +3.3% / +1.10 pts | +4.6% | 27.1% |
| Cranfield | +11.6% / +2.77 pts | +2.4% / +0.63 pts | +9.0% | 39.4% |
| CISI | +17.2% / +1.84 pts | +2.2% / +0.27 pts | +14.6% | 42.9% |
| LA Times | +10.1% / +1.92 pts | +26.7% / +4.39 pts | **−13.0%** | 27.8% |

Checks of the author's claims:

- "The improvement achieved through stemming ranges between 8% and 17%" (p. 71): **matches** RSLP vs no stemming (8.1–17.2%) ✓.
- "An average of 12% proportional improvement in relation to the Portuguese version of the Porter stemmer was observed in the small test collections, and a greater proportional improvement of 26% was observed in the LA Times collection" (p. 70):
  - LA Times: 26.7% ✓ (approximately).
  - Small collections: the table gives +3.3%, +2.4%, +2.2%, mean **2.65%**, not 12%. With RSLP as denominator the values are 3.2/2.4/2.1%. **The 12% equals the mean of RSLP vs *no stemming* on the small collections (12.3%)** — plausibly a mislabelled comparison. **Internal inconsistency.**
- "The RSLP stemmer achieved the highest results in all experiments: the average precision was higher and so was the number of relevant documents retrieved" (p. 70): true for average precision; **false for relevant retrieved on Time** (RSLP 299 < no stem 301 < Porter-PT 306).
- "No stemming performed the worst with the small collections and retrieved the least relevant documents in two out of the four collections" (p. 71): consistent with the table (Cranfield, CISI).
- Not commented on by the author: on LA Times the **Porter-PT run is worse than no stemming** (16.46% vs 18.93%; 658 vs 671 relevant retrieved). A poor stemmer can do worse than none.
- Figure 4.7 (p. 71, checked visually): the three curves nearly coincide on Time, Cranfield and CISI; on LA Times the RSLP curve is visibly above the other two at low recall.

### Table 4.2 — monolingual vs bilingual LSI (p. 68; checked visually)

| Collection | Mono-all AP | Mono-half AP | Bilingual AP | Bilingual / Mono-half **[computed]** |
|---|---:|---:|---:|---:|
| Time | 59.90% | 38.13% | 34.16% | 89.6% |
| Cranfield | 29.53% | 27.75% | 26.60% | 95.9% |
| CISI | 15.31% | 13.80% | 12.56% | 91.0% |
| LA Times | 21.16% | 20.34 (printed without %) | 17.09% | 84.0% |

- The author's "84 to 96% of the performance of the monolingual run" (Sec. 4.5, p. 73) matches Bilingual/Mono-half ✓.
- Loss percentages in the text mix denominators **[computed]**: "11% (Cranfield)" = (29.53−26.60)/26.60 (bilingual as denominator), but "42% (Time)" ≈ (59.90−34.16)/59.90 = 43.0% (monolingual as denominator); "5% (Cranfield) to 19% (LA Times)" for Mono-half vs Bilingual computes to 4.1–4.3% and 16.0% (/Mono-half) or 19.0% (/Bilingual). Minor.
- **Copy error:** the Time block of Table 4.2 prints "Number of Terms" 2,629 (Mono-all) and 1,979 (Mono-half), identical to the Cranfield block, while Table 4.1 gives 7,596 unique monolingual terms for Time.
- **Unexplained difference:** LA Times "Bilingual" = 17.09% AP, 663 relevant retrieved (Table 4.2) vs 20.85%, 694 (Table 4.3), with the same 69,996 terms. The number of dimensions for Table 4.2 is not stated per collection; Table 4.3 used 700. The small-collection Bilingual values are identical in both tables.

### Table 4.4 — cross-language term similarity in the LSI space (p. 72)

A sample of 18 of 50 word pairs, e.g., baby–bebê 99.67%, England–Inglaterra 99.24%, train–trem 12.30% vs train–treinar 84.97%, match–fósforo 96.72% vs match–jogo 36.28%. The author concludes that polysemy lowers similarity, proper names map almost perfectly, and verbs are worst (p. 72). Values for all 50 pairs are not reported.

### Chapter 5 — RF user experiment (key numbers; pages 94 and 100 checked visually)

- **Choice of RF method** (Figure 5.1, p. 79): baseline 0.24; RF1 0.35; RF2 0.36; RF3 (centroid) 0.38; RF4 0.26 ("improvement of 8%" ✓, 8.3% **[computed]**). Even RF3 made 4 of 32 topics worse (p. 79).
- **Judgement accuracy** (Table 5.4, p. 87; Table 5.6, p. 88): overlap with CLEF assessors 0.40 (hand translation), 0.41 (MT), 0.16 (original English); ANOVA HT vs MT p = 0.85. Native English speakers: 0.46 (Table 5.8, p. 92).
- **RF gains** (Table 5.10, p. 94), mean residual-collection AP over the 6 topics:

| Run | Mean AP | Change vs baseline (printed) | Recomputed from topic values |
|---|---:|---:|---:|
| Baseline | 0.2553 | — | 0.2553 ✓ |
| Official CLEF judgements | 0.2875 | +12.64% | +12.64% ✓ |
| Best participant | 0.3947 | +54.62% | +54.63% ✓ |
| Worst participant | 0.1986 | −22.20% | −22.21% ✓ |
| Optimal (best judgement set per topic) | 0.4732 | +85.38% | +85.39% ✓ |
| Average of participants | 0.2873 | +12.53% | +12.56% (mean of Table 5.11 per-participant changes = 12.55%) ✓ |

- 21 of 27 participants improved (77%), 6 got worse, 10 beat the official judgements (Table 5.11, p. 96; counts re-derived ✓).
- **By topic** (Table 5.15, p. 100): +41%, −52%, +18%, +128%, +22%, +2% (recomputed +40.7, −51.7, +18.0, +128.0, +21.7, +2.1 ✓).
- **Correlations over 162 participant-topic units** (Table 5.12, p. 96; Appendix E5.1, p. 249, Pearson, SPSS 11): change vs missed −0.24, false alarm −0.27, missed+false −0.51, overlap +0.33 (all match the appendix ✓).
- **By topic** the signs flip (Table 5.14, p. 98): e.g., overlap vs change +0.86 (Topic 1) but −0.52 (Topic 2).
- **Query features:** number of proper names in the topic vs RF improvement r = 0.35; vs baseline AP r = −0.23 (Sec. 5.6.5, pp. 104–105) — computed over 6 topics.
- **Inconsistency:** "A moderate negative correlation (r=-0.40 – see page 249) was found between initial average precision of the queried and the improvement" (p. 99). Appendix E5.1 on p. 249 (checked visually) gives Residual Initial vs Change = **−0.219** (p = .005, N = 162). No −0.40 value appears in that matrix.

## 10. Statistical evidence

- **Stemming experiment (Ch. 4): no significance test, no confidence intervals, one run per condition, no per-query results.** Only per-collection aggregate AP and relevant-retrieved totals. The "8–17%" differences may or may not be significant; the thesis gives no basis to judge.
- **Stemmer intrinsic tests (Ch. 3):** no statistical test; single samples of 1,000 words.
- **LSI dimensions:** chosen by inspecting retrieval results on the evaluation collections (Figure 4.5, p. 67); no separate tuning set.
- **Ch. 5:** ANOVA (α = 0.05) for judgement-accuracy comparisons; Pearson correlations with two-tailed p-values in Appendix E (SPSS v. 11). Sample: 27 participants × 6 topics; 162 participant-topic units in the correlation analysis are not independent (each participant contributes 6, each topic 27) **[inferred]**.
- **Ablation:** the no-stem / Porter-PT / RSLP comparison is itself a preprocessing ablation; there is no ablation of RSLP steps (e.g., without exception lists, except the unquantified "reduce overstemming mistakes by 5%", p. 51).
- **Per-query analysis:** for stemming, **none**. For RF, per-topic tables and per-topic correlations (Tables 5.10, 5.14, 5.15).
- **Overlap / unique hits / oracle union between retrieval channels or representations:** **none.** The "overlap" of Ch. 5 is inter-assessor agreement; the "Optimal" run is an oracle choice, per topic, of "the set of judgements that yielded the best result" (p. 94; whether the official CLEF set is among the candidates is not stated; for Topic 2 the optimum equals the baseline), not a union of results from different retrieval representations.

## 11. Strengths

- A language-specific stemmer with **both** intrinsic evaluation (held-out stem accuracy; Paice UI/OI, which separate under- and over-stemming) **and** extrinsic IR evaluation on four collections.
- Transparent rule design (suffix, minimum stem length, replacement, exceptions; full list in Appendix A) and an explicit catalogue of failure types: exceptions, homographs, irregular verbs (<1% of errors), root changes, proper names (Sec. 3.3, pp. 53–55).
- Multiple collections of different domains and sizes; vocabulary sizes reported per condition.
- Careful user-experiment design in Ch. 5 (Latin square, three presentation systems, extra user groups), with raw data and statistics in Appendix E.
- The author states limits of generalisation honestly: the topic-level findings "are harder to generalise" and need "a much larger set of topics" (Sec. 6.5, pp. 115–116).

## 12. Limitations

### Stated by the author

- The software could not index the whole LA Times collection above 400 dimensions; an optimal k for LA Times "could not be established" (Sec. 4.4.2, p. 67). SVD indexing took up to 2 days at 400 dimensions (Sec. 6.4.1, p. 114).
- MT errors are kept in the parallel corpus; part of the bilingual loss is plausibly due to MT, but hand translation of thousands of documents was not feasible (Sec. 4.5, p. 73).
- RSLP does not treat irregular verbs or non-orthographic root changes (e.g., *emitir* → *emit* vs *emissão* → *emis*); proper names are stemmed (Sec. 3.3, pp. 54–55).
- Minimum stem lengths were "set by observing lists of words"; "there is no linguistic support for this procedure" (p. 51). Porter's measure could replace absolute minimum lengths (Sec. 7.2.4, p. 120).
- Only 6 topics in the RF experiment; "the characteristics of the topics that determine the relationship between change in performance and the misjudged documents remain unclear" (p. 103); results may depend on the IR system (Sec. 6.5, p. 116).
- Only positive feedback was used (Sec. 6.4.2, p. 115).

### Inferred from the experimental design

1. **Confounded "no stemming" condition.** It switches off stemming in both English and Portuguese (pp. 65, 70). The RSLP-vs-no-stem gain (8–17%) is therefore a joint effect of English Porter stemming and Portuguese stemming; only RSLP vs Porter-PT isolates the Portuguese stemmer.
2. **Morphology and the semantic model are entangled.** The LSI space is re-derived on each preprocessed matrix, so stemming changes the semantic representation itself. The design cannot separate "better lexical matching" from "better latent space".
3. **No lexical-only baseline.** Without a VSM/BM25 run, the thesis cannot say whether stemming helps the latent model more or less than it would help plain term matching, or whether the two find different relevant documents.
4. **Partly monolingual matching.** Half (small collections) or 20% (LA Times) of the indexed documents contain a Portuguese MT half, so Portuguese queries can match Portuguese words of those documents directly. Stemming effects therefore mix monolingual Portuguese matching and cross-language mapping. The breakdown is NOT_REPORTED.
5. **Fold-in vocabulary effect.** Folded-in documents add no new terms (p. 68). Stemming reduces the vocabulary (27–43% **[computed]**) and may increase how many terms of folded-in English documents are represented. The author does not discuss this possible mechanism.
6. **No significance testing and one run per condition** for all Ch. 4 comparisons; the RSLP vs Porter-PT differences on the small collections are 0.27–1.10 AP points.
7. **Tuning on evaluation data:** k chosen on the same collections/queries (Figure 4.5); RF3 chosen on the same LA Times collection and CLEF 2002 topics (English versions, 32 topics) as the main RF experiment (Sec. 5.2, p. 79).
8. **Metric definition not fixed** (interpolated vs non-interpolated AP; evaluation software unnamed); LA Times query count (50 vs 42 with relevant documents) NOT_REPORTED.
9. **Old small collections** (Time, Cranfield, CISI; 83–225 queries, 425–1,460 documents) dominate three of four comparisons.
10. **Intrinsic evaluation designed by the stemmer's author:** gold stems and concept groups were created without a reported second annotator or agreement measure.

## 13. What the work proves

- **Within this LSI-based Portuguese→English CLIR setup**, stemming (RSLP for Portuguese + Porter for English) gives higher aggregate average precision than no stemming on all four collections: +8.1% to +17.2% relative, +1.84 to +2.77 AP points (Table 4.3, p. 70 **[computed]**). Significance is not tested.
- **RSLP beats the translated Porter stemmer** on every intrinsic measure reported (held-out stem accuracy 96% vs 71%; UI 0.034 vs 0.215; OI 9.85×10⁻⁵ vs 2.11×10⁻⁴; pp. 56, 60) and on AP in all four collections (Table 4.3). The AP margin is small on three collections (+0.27 to +1.10 points) and large on LA Times (+4.39 points).
- **In this setup, the choice of stemmer changed the sign of the observed stemming effect on one collection:** Porter-PT is below no stemming on LA Times (16.46% vs 18.93%), while RSLP is above it (Table 4.3). This is a single run per condition with no significance test.
- **Stemming reduces the index vocabulary substantially** (RSLP: 27–43% fewer terms than no stemming; Table 4.3 **[computed]**; 51% on the 32,000-word list, p. 56).
- **Topic identity dominates the RF outcome** in the six-topic user experiment: per-topic changes range from −52% to +128% (Table 5.15), per-topic correlations change sign (Table 5.14), and per-topic oracle selection of judgement sets reaches +85.4% vs +12.6% for the official judgements (Table 5.10).

## 14. What the work does NOT prove

- **Anything about morphological representation of a lexical ranking channel such as BM25.** No lexical model is evaluated; stemming is tested only as input to LSI.
- **That stemming helps the cross-language mapping specifically.** The author's explanation ("maximises the co-occurrences, providing better correspondence between cross-linguistic matches", p. 71) is not tested; monolingual matching within dual-language documents and fold-in vocabulary effects are not separated.
- **That RSLP is significantly better than Porter-PT in retrieval.** No test; small AP differences on three collections; the "12% on the small collections" claim is not supported by Table 4.3.
- **Lemmatization vs stemming.** No lemmatizer is tested; RSLP deliberately reduces verbs to roots rather than infinitives.
- **Complementarity between retrieval channels or representations.** No overlap of result sets, no unique relevant hits, no oracle union, no fusion. The Ch. 5 "overlap" is assessor agreement, and the "Optimal" oracle chooses among feedback judgement sets.
- **Which query characteristics drive stemming gains.** No per-query stemming analysis exists. The only query-feature evidence (proper names vs RF gain, r = 0.35) is based on 6 topics and concerns RF, not morphology.
- **Anything about modern dense retrievers.** LSI is unsupervised and corpus-specific; results do not transfer to a fixed, pre-trained, retrieval-trained D.

## 15. Relationship to current Uzbek evidence

- **No Uzbek data.** Portuguese is a fusional Romance language with suffixal inflection (plural, gender, diminutive/augmentative, rich verb conjugation). Uzbek is agglutinative with long suffix chains. The engineering lessons (ordered suffix-removal steps, minimum stem length, exception lists, accent/diacritic handling after rules that need them) transfer in spirit to Uzbek stemmers such as UzbStemmer (`MORPH-UZ-004`, Xusainova), but the numbers do not.
- **Diacritics/orthography parallel:** RSLP removes accents as the *last* step because some rules depend on accented forms (e.g., *óis → ol*, p. 53). This is analogous to the Uzbek o‘/g‘ apostrophe issue flagged in `MORPH-005` §17: normalization order matters and should be fixed explicitly.
- **Intrinsic vs extrinsic evaluation:** the Uzbek national theses report analyzer/stemmer accuracy (e.g., Xusainova 97.5%, Bakaev 88.9–96%) without IR effectiveness (`MASTER_INDEX` C). Orengo's thesis shows both kinds of evaluation for one stemmer, and that a 96% vs 71% intrinsic gap became only +0.27 to +1.10 AP points on three of four collections. In this one stemmer pair, analyzer accuracy did not translate proportionally into retrieval gain **[inferred]**; one comparison cannot establish a general rule.
- **Relation to Turkish evidence** (`MORPH-001` Can et al. 2008; `MORPH-002` Haddad & Bechikh Ali 2014): those works test stemming/lemmatization in lexical models (VSM in MORPH-001, BM25 in MORPH-002) on one much larger collection (408,305 documents, 72 queries per the MORPH-001 card); their query sets are not larger than Orengo's (50–225 queries per collection). Orengo tests stemming inside a latent semantic model. Together they show morphology × model interactions were studied in several model families long before dense retrieval, but none decomposes lexical–semantic complementarity.

## 16. Relationship to CURRENT_GAP

**Classification (proposal):** *supports the existing evidence boundary* (historical) + *no material effect on the residual core*.

- **Supports the boundary / non-claims already in v0.8:**
  - "morphology + semantic model is automatically new" — already excluded by the project; this thesis adds a 2004 example of morphological preprocessing (no stem / two stemmers) fed into an LSI semantic model and evaluated by retrieval.
  - "raw/stem comparisons in a less-resourced language have not been done" — also already excluded; this is one more (Portuguese, 2004) instance.
- **Touches, only partially, the v0.8 element "raw → stem → lemma":** raw and two stemmers exist; lemma does not; the variants feed LSI, not a lexical channel.
- **Does not touch:**
  - a **fixed** dense comparator D (here the semantic space is re-derived per morphological condition, the opposite of the v0.8 control);
  - BM25 or any lexical channel;
  - unique relevant hits, overlap, oracle union between channels;
  - hybrid/fusion and incremental hybrid gain;
  - per-query links between morphology-induced changes and query features.
- **On the triage flag `carries_complementarity_evidence = YES`:** the per-topic RF evidence (topic effects, per-topic oracle among feedback sources) is methodologically suggestive (per-query variation, oracle upper bound) but is **not** lexical–semantic complementarity. Proposal: record it as "indirect / per-topic variability only".

**Proposal:** keep v0.8 refined unchanged. This is a proposal only; `CURRENT_GAP.md` has not been edited.

## 17. Implications for our research design

- **Fixed D (supports the existing control).** In LSI, stemming changes the semantic model itself, so morphology and semantics cannot be separated. Our design should keep D fixed and fed with the same text for all lexical variants, and change only the lexical channel. If a stemmed/lemmatized input to D is ever tested, report it as a separate factor, not as part of the raw/stem/lemma lexical comparison.
- **Isolate one factor per contrast.** Orengo's "no stemming" switches off stemming in two languages at once. For Uzbek, the raw/stem/lemma contrast should change only the Uzbek morphological step; tokenization, apostrophe/Unicode normalization, lowercasing and stop-words stay identical across conditions and are reported.
- **Evaluate the stemmer/lemmatizer intrinsically as well.** Adopt Paice-style UI/OI on Uzbek concept groups (families of inflected forms) together with stem/lemma accuracy, so that over- and under-conflation can be linked to changes in unique lexical hits. Use a second annotator and report agreement (absent here).
- **Expect stemmer-dependent and collection-dependent effects.** A weak stemmer can be worse than none (Porter-PT on LA Times). Use more than one Uzbek stemmer/lemmatizer if available, and more than one domain or query set if feasible.
- **Report absolute and relative differences with a fixed denominator**, per-query results and paired tests. The thesis's mixed denominators and a mislabelled "12%" show how aggregate claims drift from the tables.
- **Per-query oracle as an analysis tool.** The Ch. 5 "Optimal" row (+85.4% vs +12.6%) is the RF analogue of our oracle-union / per-query best-choice upper bound. It illustrates why per-query oracles should be reported beside averages, and why their gap to realizable methods must not be read as achievable gain.
- **Query taxonomy and sample size.** The author could not analyse topic characteristics with 6 topics and says a much larger topic set is needed. Our query-feature analysis (morphological, graphic, lexico-structural features) needs enough queries per feature bin; plan the query set size with that in mind.
- **Metric protocol:** name the evaluation tool and the exact metric (e.g., trec_eval MAP / nDCG@k / Recall@k), and fix the retrieval depth (here 100) used for unique-hit counts.
- **Hypothesis:** no evidence for or against the v0.8 hypothesis.

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| Stemming | Cutting endings so that different forms of a word become one index term | Rule-based suffix stripping to a (not necessarily linguistic) stem |
| RSLP | The Portuguese suffix-stripping stemmer built in this thesis ("Removedor de Sufixos da Língua Portuguesa") | 8 ordered steps, 199 rules with minimum stem length, replacement and exceptions |
| Overstemming / understemming | Merging unrelated words / failing to merge related words | Errors measured by Paice's OI and UI |
| Paice UI / OI | Share of word pairs that should be merged but are not (UI), and that should not be merged but are (OI) | UI = GUMT/GDMT; OI = GWMT/GDNT (Eqs. 15–18) |
| CLIR | Searching documents in one language with a query in another | Cross-language information retrieval |
| LSI | Builds a compressed "concept space" from which words appear in which documents; related words end up close | Truncated SVD of a weighted term-by-document matrix; cosine ranking |
| Dual-language document | A document glued to its translation | Training unit for a cross-language LSI space |
| Folding in | Adding new documents to an existing LSI space without recomputing it | Placing a document "at the average of their corresponding terms" (p. 26), i.e. from its (known) term vectors; new terms are not added (p. 68) |
| Log-entropy weighting | Local log term frequency times a global weight that is high for terms concentrated in few documents | Eqs. 19–20 |
| Relevance feedback (RF) | The user marks relevant documents and the system rewrites the query | Here: query replaced by the centroid of judged-relevant documents (RF3) |
| Residual collection | Evaluating the feedback run without the documents the user already judged | Removes judged documents from ranking and qrels |
| Overlap (Lesk & Salton) | Agreement between two judges' relevant sets | |R₁ ∩ R₂| / |R₁ ∪ R₂| |
| Oracle / per-query best choice (project term) | Picking, for each query, whichever option happened to work best; an upper bound, not a method | max over options per query, then averaged |
| Complementarity (project term) | Each retrieval channel finds some relevant documents the other misses | Unique relevant hits, overlap, oracle-union gain |

## 19. Open questions / verification needed

1. **"12% vs Porter on the small collections"** (p. 70) vs 2.2–3.3% in Table 4.3: mislabelled comparison (RSLP vs no stemming gives 12.3%) or a different, unreported measurement? Not decidable from the thesis.
2. **LA Times Bilingual 17.09% (Table 4.2) vs 20.85% (Table 4.3)** with the same vocabulary: different dimensions (k not stated for Table 4.2)? Not decidable.
3. **Time "Number of Terms" in Table 4.2** duplicates the Cranfield values; the true Time values are NOT_REPORTED.
4. **Paice example OI = 0.083** vs 12/156 = 0.077 **[computed]**.
5. **r = −0.40 (p. 99) vs −0.219 in Appendix E5.1 (p. 249)** for initial precision vs RF change.
6. **Summary claims vs appendix:** Sec. 5.7 says "No relationship was found between the change in performance and the difficulty of the topics or ... the knowledge of the subject" (p. 106), while Appendix E5.1 shows Difficulty vs Change r = −0.182 (p = .020) and Knowledge vs Change r = −0.246 (p = .002). Both are weak but nominally significant; the text's "no relationship" is stronger than the appendix supports. The body itself reports "a weak correlation of 0.18 between the difficulty of the task and the improvement" (Sec. 5.6.4, p. 104; sign not given).
7. **Metric definition** (interpolated vs non-interpolated average precision), evaluation software, stemming of monolingual runs, and number of LA Times topics used in Ch. 4: NOT_REPORTED.
8. **Table numbering:** the List of Tables numbers Ch. 5 tables differently from the body (e.g., body Table 5.10 = LoT Table 5.7). This card uses body numbers with printed pages.
9. **Wording on p. 72:** "Stemming, however, is very important to verbs as it decreases the number of matches across different languages" — "decreases" is probably a slip for "increases", but the thesis does not say.
10. **Overlap with other records:** Orengo & Huyck 2001 (SPIRE, RSLP) and 2003 (CLEF 2002, LSI CLIR) may be separate records in the systematic review; the coordinator should check for duplicates and whether the CLEF paper reports per-topic stemming results.
11. **Bibliographic record:** repository item ID and award date not verified (record page returned HTTP 405).
12. **Step order of RSLP:** the text numbers Adverb Reduction as Step 3 and Augmentative/Diminutive as Step 4 (p. 52), while Figure 3.1 (p. 50) draws Augmentative before Adverb. The implemented order is not decidable from the thesis.

## 20. Decision after deep dive

- **Keep current gap?** Yes. v0.8 refined remains valid (§16).
- **Modify gap?** No change proposed.
- **Triage metadata (proposal for the coordinator):** change `carries_complementarity_evidence` from YES to "indirect (per-topic RF variability; oracle among feedback judgement sets)"; lower reading priority from HIGH to MEDIUM/LOW for the gap (still relevant for the stemmer-evaluation methodology).
- **Add decision?** Proposed for `decisions/DECISIONS.md` (researcher's decision):
  - "Each morphology contrast changes only the Uzbek morphological step; all other preprocessing is identical and reported";
  - "Stemmers/lemmatizers are also evaluated intrinsically (accuracy + Paice-style UI/OI on concept groups) before IR experiments."
- **Add experiment?** Optional and cheap: a Paice UI/OI evaluation of the candidate Uzbek stemmer(s)/lemmatizer(s) on a few hundred inflected-form groups, to be related later to per-query unique lexical hits. No new retrieval experiment is required by this thesis.
- **Add citation to Chapter I?** Optional, minor:
  - §1.1 (morphological normalization in lexical IR for less-resourced inflected languages; intrinsic vs extrinsic stemmer evaluation; the gap between stemmer accuracy and retrieval gain);
  - §1.2, historical note on LSI (morphological preprocessing inside an early latent semantic model), citing it only with the caveats in §12.
  - For the RSLP stemmer itself, the SPIRE 2001 paper may be the more standard citation (not read here).
- **Proposed `MASTER_INDEX.md` row** (to add after approval):

| MORPH-020 | Orengo — *Assessing Relevance Using Automatically Translated Documents for Cross-Language Information Retrieval* (PhD, Middlesex University) — [deep dive](deep-dives/2004_Orengo_PhD_Portuguese_Stemming_LSI_CLIR.md) | 2004 | A (narrow) | LOW | RSLP Portuguese stemmer (199 rules; held-out stem accuracy 96% vs 71% for Porter-PT; Paice UI 0.034 vs 0.215). Stemming tested only as input to LSI-based PT→EN CLIR on Time/Cranfield/CISI/LA Times: RSLP vs no stemming +8–17% AP; RSLP vs Porter-PT +2–3% on small collections (thesis text claims 12%) and +27% on LA Times, where Porter-PT < no stem. No lexical/BM25 model, no significance tests, no fusion or overlap/unique-hit analysis; LSI space re-derived per condition. Ch. 5 RF user study: per-topic effects dominate (−52%…+128%; per-topic oracle +85% vs +13%). |
