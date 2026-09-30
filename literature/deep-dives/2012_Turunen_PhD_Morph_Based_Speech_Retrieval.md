# Turunen (2012): Morph-Based Speech Retrieval: Indexing Methods and Evaluations of Unsupervised Morphological Analysis (doctoral dissertation, Aalto University)

**Targeted deep-dive status:** COMPLETED (AI-assisted, pending researcher review)
**Completed:** 2026-09-28
**Literature ID:** `MORPH-025` (assigned 2026-09-28, approved by researcher)
**Systematic-review record:** `CR002216`. Full-text triage: INCLUDE, reading priority HIGH, reading tier 1 ("прямо по теме пробела"), `carries_complementarity_evidence = YES`
**Provenance:** AI-assisted deep dive (Claude). The supplied PDF (120 pages) contains **only the overview ("introduction") part** of this article-based dissertation: front matter, Chapters 1–8 and the bibliography (printed pp. 1–116). **Publications I–VII are not included in the PDF** (the printed record gives 228 pages in total). Everything below therefore comes from the overview, which itself says that "Full details of the experimental setups and results are given only in the publications" (Sec. 1.4, p. 26). Read in full: abstract, Chapters 1–3 (IR models, metrics, morphology, Morfessor), Sec. 4.6–4.7, Chapters 5–8. Chapter 4 (ASR internals) was skimmed. Page images checked visually (110 dpi; Fig. 7.1 also at 250 dpi): printed pp. 70 (Table 5.2), 72 (Table 5.3), 76 (Table 5.4), 83 (Table 6.1), 86 (Table 6.2), 95 (Fig. 7.1). PDF page = printed page + 2. Numbers computed by us are marked **[computed]**.
**Source rule:** **the dissertation (its overview part as supplied) is the primary and only authoritative source.** Nothing is claimed about what Publications I–VII contain beyond what the overview states. The bibliographic record was checked only against the Aalto repository listing (bibliographic check: aaltodoc.aalto.fi handle 123456789/4430, search-result title match).
**Verification:** independent AI verifier pass 2026-09-28; 8 findings addressed.
**Reliability:** **A** (officially defended doctoral dissertation, Aalto University School of Science, public examination 24 Aug 2012; pre-examiners G. J. F. Jones and K. Järvelin; component papers in Interspeech, SIGIR 2007, ACM TSLP, TAL). Evidence-strength caveat: very small speech test collections (17 and 25 queries), overview-level reporting of results, significance tests mostly not reported.

---

## Кратко для исследователя (RU)

- **Что это.** Докторская диссертация (Doctor of Science in Technology, Aalto University, 2012; руководитель проф. E. Oja, научный консультант д-р M. Kurimo) по поиску в финской речи (spoken document retrieval). Морфы — сегменты слов, найденные алгоритмом **Morfessor Baseline** без учителя, — используются как единицы распознавания речи (языковая модель ASR), как индексные термины и как единицы сегментации аудио на сюжеты. Диссертация по статьям (Publications I–VII), но **в PDF есть только обзорная часть**, самих статей нет.
- **Главное для нас — сравнение трёх вариантов лексического представления индекса** (Sec. 5.2.2, Table 5.3, p. 72):
  1. морфы (Morfessor);
  2. базовые формы, то есть леммы от правилового анализатора TWOL;
  3. их комбинация — единый индекс (combined) или чередование ранжированных списков (interleaved, простое объединение на уровне рангов).
- **Числа** (Podcast, MGAP; Tables 5.3 и 6.1):
  - на длинных запросах морфы ≈ базовые формы (43.0–43.8 vs 43.8);
  - на коротких запросах базовые формы лучше (34.7 vs 30.4–31.8);
  - комбинация лучше обоих во всех условиях: 46.0 / 37.3 (normal), 40.3 / 26.1 (high Q-OOV);
  - прирост комбинации над лучшим одиночным представлением больше всего для **коротких запросов при высокой доле невиденных слов в запросах**: +4.8 MGAP, +22.5% отн. **[computed]**.
  - Вывод автора: «Morphs and base forms both capture different features that neither of them can capture alone» (Ch. 8, p. 99).
- **Это прямое свидетельство взаимодополняемости двух морфологических представлений одного лексического канала**, и её размер зависит от характеристик запроса: длины и доли внесловарных (OOV) слов. Однако:
  - она показана **только агрегатными MAP/MGAP**;
  - **нет** перекрытия результатов, уникально найденных релевантных документов, oracle union и анализа по отдельным запросам;
  - условия high Q-OOV созданы искусственно (из обучающего корпуса удалены предложения с выбранными словами запросов).
- **BM25:** есть, но только как проверка чувствительности (Sec. 6.3.1, Table 6.2, p. 86; k1 = 1.2, b = 0.75). Основная модель — векторная модель с косинусом и сырым TF. BM25 улучшает 1-best на Podcast (морфы: 45.0–45.5 vs 43.4–43.8). На Tampere для морф-индекса лучше косинус с IDF Eq. 6.4 (84.4 vs 81.7).
- **Плотного/нейросетевого поиска нет** (2012 г.). Единственный «семантический» метод — **LSI** (Publication III): MAP 77.7 → 82.7 (морфы), 75.7 → 82.9 (базовые формы). LSI применяется вместо обычного индекса, а не в гибриде с ним.
- **Нет «сырого» (словоформенного) индекса** в экспериментах SDR: базовая линия уже лемматизирована. Сравнение «словоформы vs морфы vs леммы vs стемминг vs n-граммы» есть только в текстовых экспериментах Morpho Challenge (Ch. 7). Они пересказаны качественно со ссылкой на Kurimo et al. (2010a), без чисел: лучший — правиловый анализатор (финский, немецкий) или Porter (английский); лучшие методы без учителя «very close» к нему, Morfessor Baseline работает «reasonably well» (явно лучше несегментированных слов, но хуже лучших правиловых методов, p. 50); буквенные n-граммы «excellent» даже для финского.
- **Внутренние несоответствия** (подробно §9, §19):
  - Pod(N) в Table 5.3 (морфы 43.0/30.4, comb 46.0/37.3, interl 46.6/35.1) расходится с Tables 5.4, 6.1, 6.2 (43.8/31.8, 46.2/37.9, 46.8/36.1), хотя везде указана Publication VI;
  - значение comb 87.5 в столбце PII взято из другой работы (Kurimo et al., 2005);
  - для query expansion (Publication II) базовые значения в тексте равны столбцу PIII (77.7/75.7), а не PII (79.2/78.0);
  - «balanced F-score at β = 0» вместо β = 1;
  - на Fig. 7.1 есть CoMMA-A0/A1, которые в тексте не определены.
- **Для gap v0.8:** работа **поддерживает** предпосылку «морфологическое представление меняет, что находит лексический канал, и разные представления взаимодополняемы». Она **сужает** возможные притязания на новизну: объединение двух морфологических представлений и зависимость выигрыша от OOV/длины запроса уже показаны в 2005–2012 гг. **Ядро v0.8** (raw/stem/lemma BM25 × фиксированный плотный D → уникальные попадания / перекрытие / прирост гибрида) **не затронуто**. Предложение: gap не менять.
- **Практическая польза:**
  1. добавить к `BM25_raw/stem/lemma` вариант на субсловных единицах (Morfessor или BPE-морфы) как контроль и как «страховку» для слов вне словаря лемматизатора;
  2. в таксономию запросов включить **долю токенов запроса, не разобранных узбекским лемматизатором** (покрытие анализатора), и длину запроса;
  3. рассмотреть контроль `H_stem+lemma` (слияние двух лексических представлений) — чтобы отличить морфологическую взаимодополняемость внутри лексического канала от лексико-семантической.

---

## 1. Bibliographic record

- **Author:** Ville T. Turunen
- **Title:** *Morph-Based Speech Retrieval: Indexing Methods and Evaluations of Unsupervised Morphological Analysis*
- **Degree:** Doctor of Science in Technology (title page, p. 1)
- **University / unit:** Aalto University, School of Science, Department of Information and Computer Science (Adaptive Informatics Research Centre)
- **Supervising professor:** Prof. Erkki Oja. **Thesis advisor:** Dr. Mikko Kurimo.
- **Preliminary examiners:** Dr. Gareth J. F. Jones (Dublin City University), Prof. Kalervo Järvelin (University of Tampere). **Opponent:** Prof. Murat Saraçlar (Boğaziçi University).
- **Defence:** 24 August 2012 (manuscript submitted 24 January 2012; permission to publish 25 June 2012)
- **Series:** Aalto University publication series DOCTORAL DISSERTATIONS 97/2012
- **ISBN:** 978-952-60-4717-1 (printed), 978-952-60-4718-8 (pdf); ISSN-L 1799-4934
- **URN:** http://urn.fi/URN:ISBN:978-952-60-4718-8 (stated in the thesis)
- **Repository:** aaltodoc.aalto.fi/handle/123456789/4430 (bibliographic check: web search listing, title match); current Aaltodoc item page aaltodoc.aalto.fi/items/fe5a209b-5224-4d19-894f-bc97a9715778 confirms author, title, DD 97/2012, defence 24 Aug 2012, 228 pages, supervisor Oja, advisor Kurimo
- **Type:** article dissertation (summary + original articles); total 228 pages per the abstract page; the supplied PDF has 120 pages = overview only
- **Language studied:** Finnish (the Morpho Challenge chapter also covers English and German)
- **Component publications (as listed, pp. 13–14):**
  - I Kurimo, Turunen, Ekman — Interspeech 2004 (ICSLP), pp. 1585–1588;
  - II Kurimo, Turunen — Interspeech 2005, pp. 605–608;
  - III Turunen, Kurimo — Interspeech 2006, pp. 341–344 (LSI);
  - IV Turunen, Kurimo — ACM SIGIR 2007, pp. 631–638 (confusion networks);
  - V Turunen — Interspeech 2008, pp. 2158–2161 (OOV query words);
  - VI Turunen, Kurimo — ACM TSLP 8(1), pp. 1–25, 2011 (unsegmented audio; segmentation, recognition, retrieval);
  - VII Virpioja, Turunen, Spiegler, Kohonen, Kurimo — TAL 52(2), pp. 45–90, 2011 (evaluation metrics).
- **Reliability:** A
- **Full text available:** overview part only (`07_full_text/pdfs/CR002216.pdf`)

## 2. Why this work matters to the PhD

It is an early, defended-PhD-level body of work in an **agglutinative** language (Finnish) that:

- compares **alternative morphological representations of the same lexical index**: unsupervised morphs vs rule-based base forms (lemmas);
- **combines** these representations, both as one index and as rank-level interleaving;
- reports that the combination beats either alone, with the size of the gain depending on **query properties** (length; share of unseen/OOV query words).

| Axis | Relation |
|---|---|
| Lexical retrieval | Central. VSM cosine TF-IDF (main); Okapi BM25 as a sensitivity check (Table 6.2); morph vs base form vs combined indexes |
| Semantic retrieval | Only LSI (Publication III) and pseudo-relevance-feedback query expansion (Publication II). No neural or dense retrieval |
| Hybrid retrieval | Only **lexical–lexical** combination (morph + base form); no lexical–semantic fusion. LSI is not fused with the term index |
| Uzbek morphology | Indirect but close in type: Finnish is agglutinative and suffixing, like Uzbek; it also has stem alternation (consonant gradation) |
| Low-resource retrieval | The motivation for unsupervised morphology is explicitly "less resourced languages" (Sec. 1.2) |
| Current gap | Supports the premise that morphological representation changes what the lexical channel retrieves. Occupies "fusing different morphological representations" and "OOV/length moderates the gain". Does not touch lexical–dense complementarity (§16) |

## 3. Research problem

### Simple explanation

To search recorded speech, the system first converts audio to text with a speech recognizer (ASR), then indexes the text. In Finnish, one word can have thousands of forms. A word-based recognizer can only output words from its fixed vocabulary, so rare query words, often names, are never recognized. The words that *are* recognized must still be normalized (e.g., lemmatized) before matching, and a dictionary-based lemmatizer also fails on unknown words or on words the recognizer got partly wrong. The thesis asks: what if both recognition and indexing use automatically learned word pieces (morphs)?

### Formal formulation

The questions, as they can be read from Chapters 1 and 5–7:

- **Q1:** Do morph-based ASR language models give better spoken document retrieval (SDR) than word-based ones, especially for unseen query words (Publication V)?
- **Q2:** Which **indexing units** give the best retrieval: morphs, base forms, or their combination (Publications III, VI)?
- **Q3:** Can the effect of "unoptimal" morph segmentation or allomorphy be reduced with LSI, query expansion, or alternative query segmentations (Publications II, III, VI)?
- **Q4:** Which segmentation units are best for story segmentation of unsegmented audio (Publication VI)?
- **Q5:** Does adding alternative ASR hypotheses from confusion networks, weighted by posterior or by rank, improve retrieval (Publications IV–VI)?
- **Q6:** Which linguistic metrics for unsupervised morphological analysis correlate with IR performance (Publication VII)?

Task: ad hoc spoken document retrieval. Rank documents (Tampere) or replay points in unsegmented audio (Podcast) for a text query, evaluated by MAP / MGAP.

## 4. Main idea

### Simple explanation

Train Morfessor on a large text corpus so that it learns frequent word pieces. Use those pieces:

1. as the recognizer's vocabulary, so any word can be spelled out as a sequence of pieces;
2. as the index terms;
3. to split query words the same way.

A query word the recognizer never saw can still match if some of its pieces are recognized. Because morphs sometimes split different forms of the same word differently, combine the morph index with a classical lemma index.

### Concrete example (Table 5.1, p. 69)

- Unseen query word *Iliescun* ("Iliescu's") → morph query `ili escu n`.
  - The morph recognizer produced `n ilja escu` / `ili a s kun`, so some query morphs still match.
  - The word recognizer produced *lieskoja* / *eli eskon*, lemmatized to "flame", "or / live / Esko": nothing matches.
  - Additionally, "Iliescu" was not in the analyzer lexicon, so the word query was left unprocessed.
- Another case (Sec. 5.2.2, p. 71): the name "Eero Heinäluoma" was recognized as morphs `vir heinä <w> luoma`. The lemmatizer turned it into "virhe" (mistake) + "luoda" (to create), but the query morphs "heinä" and "luoma" still match in the morph index.

### Formal method

- **Morfessor Baseline** (Sec. 3.4.1, pp. 47–50) chooses a morph lexicon θ minimizing the MDL cost `L(x, θ) = L(x|θ) + L(θ)` (Eq. 3.1) by greedy recursive binary splitting. New words are segmented by Viterbi search over the morph lexicon, so no word is OOV.
- **Retrieval** (Sec. 2.3.1, 6.2, 6.3.1):
  - vector space model with cosine similarity (Eq. 2.3);
  - raw TF (chosen on Tampere over log variants);
  - IDF `log(N / Σ_i o(t,D_i))` (Eq. 6.4; Publications IV, V) or `log(O / O_t)` over expected counts (Eq. 6.5; Publication VI).
- **Confusion networks (CN)** (Sec. 6.2):
  - CL method: `TF(t,D) = Σ_occ P(t|c,D)` (Eq. 6.1);
  - rank method: `TF(t,D) = Σ_occ 1/rank(t|c,D)` (Eq. 6.2).
- **Okapi BM25** (Eq. 2.10, IDF Eq. 2.11 floored at zero) with k1 = 1.2, b = 0.75 appears in the speech experiments only in Table 6.2 (it is also the ranking function of the cited Morpho Challenge text-IR evaluation, Sec. 7.2.1).

## 5. Architecture / algorithm

1. **Morfessor training** on a text corpus; the same model segments the LM training corpus and the queries (Fig. 5.1, p. 68).
2. **ASR:**
   - morph LM, about 19,000 morphs, with a word-break symbol; effective OOV rate 0%;
   - vs a word LM of about 490,000 word forms, leaving about 4.7% of training-set words OOV (Sec. 5.2.1, p. 69).
3. **Story segmentation** (Podcast only):
   - TextTiling over fixed-length time windows, threshold `μ − ασ`;
   - α tuned for MGAP on a text corpus with document structure removed;
   - optimum at about 50% more boundaries than documents (Sec. 5.2.4, p. 75).
4. **Indexing options** (Sec. 5.2.2, pp. 70–72). The options are verbatim in substance:
   1. morph index, with query words segmented by Morfessor;
   2. morphs joined into words and lemmatized by a rule-based analyzer (TWOL, Koskenniemi 1983), giving a **base form index**;
   3. **combined:** morph and base-form transcriptions concatenated into one index, with queries in both forms;
   4. **interleaved:** the two indexes are queried separately; "the final ranked list was constructed by picking items in order, alternating between the two lists, and removing duplicates" (p. 72).
   - The author notes that the combined index may give "unoptimal" term weights, because base-form and morph terms sometimes coincide (p. 71).
5. **Robustness add-ons:**
   - LSI with 150 dimensions (Publication III);
   - parallel blind relevance feedback query expansion on a newspaper corpus, using offer weight (Eq. 2.15; Publication II);
   - 2-best Morfessor segmentations of query words (Publication VI);
   - CN expansion with CL or rank weighting (Publications IV–VI).
6. **Evaluation:** MAP (Tampere, text corpus); MGAP with triangular relevance functions around replay points (Podcast; Sec. 2.5.2).

## 6. Data

| Collection | Content | Queries | Relevance | Used in |
|---|---|---|---|---|
| **Tampere** (Ekman 2003) | 288 news stories read by a single speaker in a quiet environment | 17 | Each story matches **exactly one** of the 17 queries (≈16.9 relevant stories per query **[computed]**) | Publications III, IV, V (Sec. 2.2); also Publication II per Table 5.3. The overview does not state which corpus Publication I used |
| **Podcast** (built for Publication VI) | 136 h of Finnish YLE radio podcasts, **unsegmented** | 25 topic descriptions from metadata; long and short versions | 451 relevant replay points located by human assessors (≈18 per topic **[computed]**) | Publication VI |
| **CLEF Finnish text** | 55,000 newspaper documents, 4.6M words | 50 topics | 23,000 binary judgments, 413 relevant documents | Reference text experiments, Publications VI and VII |

- Source: Sec. 2.2, p. 29.
- **"High Q-OOV" scenario** (Sec. 5.2.1, p. 69): "a few descriptive words were selected from each query" and every training sentence containing any of these words "in any inflected form was excluded".
  - This *simulates* unseen query words.
  - The resulting Q-OOV rates are **NOT_REPORTED** in the overview.
  - Podcast high-Q-OOV results are "previously unpublished" (captions of Tables 5.3 and 6.1).
- **Train/dev/test:** no separate dev collection is described. TF variant selection was done on Tampere ("initial testing", p. 84). Segmentation α was tuned on the text corpus.
- Relevance window width for MGAP on Podcast, stop-list use in the speech experiments, and exact query lengths: **NOT_REPORTED** in the overview.

## 7. Baselines

| Baseline | What it is | Fair? |
|---|---|---|
| Word LM (≈490k forms) + lemmatized index | Conventional LVCSR + rule-based base forms (Publication V) | Reasonable: very large vocabulary. The RT-factor is *worse* than the morph LM's (2.17 vs 1.23), so the morph advantage does not come from a slower system |
| Base form index on morph-LM transcripts | "The standard in IR of agglutinative languages" (p. 71) | Yes: the same transcripts, differing only in index units |
| 1-best transcripts | Reference for CN expansion | Yes |
| Cosine raw-TF VSM | Main retrieval model | The author acknowledges that it may be weak and repeats some runs with BM25 (Sec. 6.3.1) |
| **Missing** | Unnormalized word-form index, stemmer, character n-grams in SDR | Not tested in SDR; only in Morpho Challenge text IR (Ch. 7, reported qualitatively) |

## 8. Metrics

| Metric | Definition | Simple meaning | Remark |
|---|---|---|---|
| MAP | Mean over queries of AP = (1/S) Σ_{relevant ranks k} p_k (Eq. 2.18) | Average precision at each relevant document found, averaged over queries | With 17 queries (Tampere), very noisy |
| MGAP | Mean of GAP = (1/N) Σ_{R_k≠0} p_k, with p_k = (1/k) Σ R_i, where R is a triangular relevance function around each ground-truth replay point (Eqs. 2.19–2.20) | Like MAP, but a returned time point gets partial credit the closer it is to the true start of a relevant segment; repeats score zero | Window width w for Podcast NOT_REPORTED |
| WER / LER / RT-factor | ASR error rates; processing time relative to audio length | Recognition quality and speed | ASR-side only |
| Spearman ρ | Rank correlation between morphology-metric F-scores and IR MAP across ≈20 methods (Ch. 7) | Does the linguistic metric order methods the same way IR does? | Not a retrieval metric |

## 9. Results

### Table 5.2 — morph vs word LM, Tampere (p. 70; Publication V)

| | morph (N) | morph (H) | word (N) | word (H) |
|---|---:|---:|---:|---:|
| WER (%) | 26.01 | 29.62 | 28.63 | 34.74 |
| LER (%) | 7.50 | 8.50 | 8.30 | 10.10 |
| RT-factor | 1.23 | 1.27 | 2.17 | 2.34 |
| MAP (%) | 84.4 | 64.2 | 77.9 | 48.0 |

- Morph over word: +6.5 MAP (normal), +16.2 MAP (high Q-OOV); +8.3% and +33.8% relative **[computed]**.
- Drop from normal to high Q-OOV: −20.2 (morph) vs −29.9 (word) **[computed]**.
- Note: the word system here also uses lemmatized indexing, so LM units and index units change together.

### Table 5.3 — indexing units (p. 72)

| Corpus | Tam. (PII) | Tam. (PIII) | Pod. (N) long | Pod. (N) short | Pod. (H) long | Pod. (H) short |
|---|---:|---:|---:|---:|---:|---:|
| WER / LER | 30.4 / 7.1 | 34.0 / 11.2 | – | – | – | – |
| num. morphs | 65k | 26k | 19k | 19k | 19k | 19k |
| morph | 79.2 | 77.7 | 43.0 | 30.4 | 34.2 | 19.0 |
| base form | 78.0 | 75.7 | 43.8 | 34.7 | 36.9 | 21.3 |
| comb. | 87.5¹ | – | 46.0 | 37.3 | 40.3 | 26.1 |
| interl. | – | – | 46.6 | 35.1 | 38.9 | 22.6 |

¹ Footnote: "(Kurimo et al., 2005)". Tampere columns: MAP; Podcast: MGAP.

**Combination vs best single representation [computed]:**

| Condition | Best single | comb. | Δ abs | Δ rel | interl. Δ abs |
|---|---:|---:|---:|---:|---:|
| Pod N long | 43.8 (base) | 46.0 | +2.2 | +5.0% | +2.8 |
| Pod N short | 34.7 (base) | 37.3 | +2.6 | +7.5% | +0.4 |
| Pod H long | 36.9 (base) | 40.3 | +3.4 | +9.2% | +2.0 |
| Pod H short | 21.3 (base) | 26.1 | +4.8 | +22.5% | +1.3 |

- **Morph − base form** on Podcast **[computed]**: −0.8 / −4.3 (N long / short), −2.7 / −2.3 (H long / short). In this table, base forms are never worse than morphs.
- The author's claim that the combination gain in high Q-OOV "is greater than in any other case" (p. 73) holds **within Podcast** (+3.4 / +4.8 vs +2.2 / +2.6). The Tampere comb gain (+8.3 over morph) is larger in absolute terms but comes from a different source (footnote 1).
- The author notes setup changes between publications (Morfessor/LM corpus, analyzer updates), so the results "are indeed somewhat mixed" (p. 72).

### Sec. 5.2.3 — allomorphy remedies (pp. 74–75; text only, no table)

| Method (publication) | morph index MAP | base form index MAP |
|---|---|---|
| LSI, 150 dims (Publication III) | 77.7 → 82.7 (+5.0; +6.4% **[computed]**) | 75.7 → 82.9 (+7.2; +9.5% **[computed]**) |
| Parallel blind-RF query expansion (Publication II) | 77.7 → 91.8 (+14.1) | 75.7 → 86.6 (+10.9) |
| 2-best query segmentations (Publication VI) | "at best … relative improvement of MGAP was 4.69%" (morph index, short queries); absolute values NOT_REPORTED | — |

- **Inconsistency:** the query-expansion baselines are quoted as 77.7 / 75.7, the Publication III column of Table 5.3, although query expansion is attributed to Publication II, whose Table 5.3 column is 79.2 / 78.0.

### Table 5.4 — segmentation × index units, Podcast MGAP (p. 76)

| index \ segmentation | morph | base form | combined |
|---|---:|---:|---:|
| morph | 43.8 | 40.9 | 42.1 |
| base form | 44.7 | 43.8 | 45.4 |
| combined | 47.0 | 45.7 | 46.2 |

- "statistically significant differences only in one case": with the morph index, base-form segmentation is significantly worse than morph segmentation (p. 75).
- The test is NOT_REPORTED.

### Table 6.1 — 1-best vs confusion networks (p. 83)

Podcast MGAP (long / short):

| Index | Weighting | Pod N long | Pod N short | Pod H long | Pod H short |
|---|---|---:|---:|---:|---:|
| morph | 1-best | 43.8 | 31.8 | 34.2 | 19.0 |
| morph | CL | 43.7 | 32.7 | 36.1 | 20.9 |
| morph | rank | 46.0 | 34.6 | 41.3 | 26.9 |
| base form | 1-best | 43.8 | 34.7 | 36.9 | 21.3 |
| base form | CL | 40.3 | 32.2 | 37.8 | 22.7 |
| base form | rank | 44.3 | 35.4 | 38.5 | 23.5 |
| combined | 1-best | 46.2 | 37.9 | 40.3 | 26.1 |
| combined | CL | 45.2 | 36.1 | 41.4 | 26.5 |
| combined | rank | 46.1 | 37.9 | 43.8 | 29.0 |
| interleaved | 1-best | 46.8 | 36.1 | 38.9 | 22.6 |
| interleaved | CL | 46.2 | 36.1 | 40.1 | 23.4 |
| interleaved | rank | **49.2** | 37.3 | 42.4 | 27.4 |

Tampere MAP (long queries):

| Index | Weighting | PIV (N) | PV (N) | PV (H) |
|---|---|---:|---:|---:|
| morph | 1-best | 76.8 | 84.4 | 64.2 |
| morph | CL | 82.3 | – | – |
| morph | rank | 85.2 | 86.9 | 70.6 |
| base form | 1-best | – | 77.9¹ | 48.0¹ |
| base form | rank | – | 80.0¹ | 49.8¹ |

¹ Produced with a word LM and a word CN.

- Morph 19.0 → 26.9 with rank-CN = +41.6% relative (text: "41.6%", p. 84) **[computed: 41.58% ✓]**.
- Best overall in high Q-OOV short: combined + rank = 29.0, i.e. +7.7 over the base-form 1-best 21.3 **[computed]**.
- Rank weighting beats CL in all 16 Podcast cells and in the one Tampere cell where both are reported (PIV morph: 85.2 vs 82.3) **[computed, reading of Table 6.1]**. This is consistent with the author's statement that rank weighting "produces best results" on both corpora and for all indexing types (p. 82).
- However, rank-CN does **not** beat 1-best for the combined index in the normal Podcast scenario: 46.1 vs 46.2 (long) and 37.9 vs 37.9 (short) **[computed]**.

### Table 6.2 — TF/IDF and BM25 sensitivity (p. 86), selected rows

| Index | TF | IDF | Unit | Tam. MAP | Pod long MGAP | Pod short MGAP |
|---|---|---|---|---:|---:|---:|
| morph | raw | Eq. 6.4 | 1-best | 84.4 | 43.4 | 31.6 |
| morph | raw | Eq. 6.5 | 1-best | 75.4 | 43.8 | 31.8 |
| morph | BM25 | Eq. 2.11 | 1-best | 81.7 | 45.0 | 33.0 |
| morph | BM25 | Eq. 6.5 | 1-best | 76.3 | 45.5 | 32.7 |
| morph | BM25 | Eq. 6.5 | rank CN | 78.5 | 47.4 | 34.2 |
| base form | raw | Eq. 6.4 | 1-best | 77.9 | 41.3 | 31.7 |
| base form | raw | Eq. 6.5 | 1-best | 72.1 | 43.8 | 34.7 |
| base form | BM25 | Eq. 2.11 | 1-best | 78.8 | 43.4 | 35.1 |
| base form | BM25 | Eq. 6.5 | 1-best | 75.7 | 42.9 | 36.3 |
| base form | BM25 | Eq. 6.5 | rank CN | 77.0 | 44.2 | 37.4 |

- BM25: k1 = 1.2, b = 0.75; BM25 IDF floored to zero (p. 85 and caption).
- Text (p. 85): with BM25, CN still improves morph MGAP 45.5 → 47.4 (long; "statistically significant") and 33.0 → 34.2 (short) **[computed: +4.2%, +3.6%]**.
- **Under BM25 1-best on Podcast, base forms beat morphs on short queries** (35.1–36.3 vs 32.7–33.0), and morphs beat base forms on long queries (45.0–45.5 vs 42.9–43.4) **[computed from Table 6.2]**. So the morph-vs-lemma ordering depends on the query length *and* on the weighting scheme.
- The author: "both the corpus and the selection of index terms have an effect on what is the most appropriate weighting of index terms" (p. 85).
- Minor text–table tension: the text says Eq. 6.5 IDF beats BM25 IDF "both for the CN and for the 1-best results" (p. 85). For morph 1-best short queries, Table 6.2 shows 32.7 (Eq. 6.5) < 33.0 (Eq. 2.11); the text adds that the 1-best difference is "very small".

### Morpho Challenge text IR (Ch. 7.2.1, pp. 92–93) — qualitative only

- All words in the corpus and queries are replaced by each algorithm's morphemes.
- Reference methods: unsegmented words, rule-based base forms, stemming.
- Ranking by Okapi BM25 with an automatic stop list of very frequent morphemes; without the stop list, performance "was severely degraded" (negative IDF).
- Best MAP came from a language-specific reference method in each language (two-level analyzer for Finnish and German, Porter for English).
- The best unsupervised methods came "very close"; a number of them were not significantly worse.
- "combining results from two different algorithms is a good strategy".
- Letter n-grams "gives excellent IR results, even for … Finnish".
- Numbers: NOT_REPORTED in the overview (cited to Kurimo et al., 2010a).

### Fig. 7.1 — Spearman ρ between linguistic-metric F-score and IR MAP (p. 95; checked at 250 dpi)

| Metric | English | Finnish | German |
|---|---:|---:|---:|
| MC | 0.269 | 0.265 | 0.641 |
| EMMA | 0.814 | 0.656 | 0.547 |
| EMMA-2 | 0.798 | 0.627 | 0.560 |
| CoMMA-B0 / B1 | 0.248 / 0.523 | 0.071 / 0.152 | 0.511 / 0.492 |
| CoMMA-A0 / A1 | 0.529 / 0.797 | 0.184 / 0.299 | 0.576 / 0.558 |
| CoMMA-S0 / S1 | 0.538 / 0.795 | 0.202 / 0.313 | 0.599 / 0.566 |

- About 20 methods or variants were evaluated (Sec. 7.3).
- The author: "EMMA correlates highly in English and Finnish, and moderately in German"; MC and CoMMA perform poorly in Finnish (p. 94).
- Our reading (inferred): in Finnish only EMMA / EMMA-2 exceed ρ = 0.6 (0.656 / 0.627); the other linguistic metrics are weak (0.071–0.313), so the choice of metric matters for predicting IR usefulness.
- These are balanced F-score (β = 1) correlations; the optimal Fβ weighting depends on the metric, and with optimal β MC and CoMMA come "much closer" to EMMA (Fig. 7.2, p. 95).

## 10. Statistical evidence

- **Significance tests:** mentioned for only a few findings:
  - morph LM vs word LM retrieval: "the morph-based approach is significantly better (Publication V)" (Sec. 3.4.1, p. 50); on p. 70 it is the morph system's RT-factor that is called "significantly better";
  - Table 5.4: one significant difference;
  - BM25 + CN long-query gain "statistically significant" (p. 85);
  - Tampere "significantly better" for Eq. 6.4 IDF (p. 85);
  - (Morpho Challenge text IR, cited: several unsupervised methods "not significantly worse" than the reference methods, p. 93.)
  - The test type, p-values and α: **NOT_REPORTED** in the overview.
  - The central claims (morph vs base form; combination > each; CN gains in Tables 5.3 and 6.1) are given **without significance statements**.
- **Confidence intervals:** NOT_REPORTED.
- **Runs / seeds:** NOT_REPORTED. Morfessor training uses random word order (Sec. 3.4.1), but seed variance is not reported.
- **Ablation / sensitivity:** present in several forms:
  - LM units × index units (Table 5.2 changes both);
  - index units × segmentation units (Table 5.4);
  - TF/IDF/BM25 grid (Table 6.2);
  - CN weighting (Table 6.1).
- **Per-query analysis:** **none quantitative.** Query effects appear only as **condition-level splits**: long vs short queries, normal vs simulated high Q-OOV. There are two anecdotal examples (Table 5.1; "Heinäluoma").
- **Overlap / unique relevant hits / oracle union between morph and base-form runs: NOT_REPORTED.** The complementarity claim rests on aggregate combination gains only.
- **Sample size:** 17 queries (Tampere) and 25 topics (Podcast). The author himself calls the Tampere corpus's small size a reliability problem (Sec. 2.2) and cites Morpho Challenge's "limited number of queries" (p. 93).

## 11. Strengths

- Clean controlled contrast of **index representations on identical transcripts**: morph vs base form vs combined vs interleaved.
- Explicit, reasoned mechanism for why the two representations are complementary: the analyzer's lexicon limits and its sensitivity to recognition errors vs Morfessor's inconsistent stems under allomorphy (pp. 71, 73).
- Query conditions that moderate the effect (length, simulated OOV) are designed into the evaluation.
- Sensitivity to the ranking function checked (BM25 vs cosine; three IDF variants), with honest reporting that conclusions change with the corpus.
- New unsegmented-audio test collection with human-assessed replay points (Podcast).
- Chapter 7 directly questions whether intrinsic morphology metrics predict IR usefulness, a useful caution for choosing a Uzbek stemmer or lemmatizer by accuracy alone.

## 12. Limitations

### Stated by the author

- Setups changed between publications, so comparisons are "slightly more difficult" and results "somewhat mixed" (p. 72).
- Tampere is small and artificial (read speech, clean audio), which makes conclusions "less reliable than desired" (p. 29) and explains weighting differences (p. 85).
- A simple VSM ignores proximity, which matters more for short subword units; a language-model approach might be better (pp. 34, 100–101).
- The same morph set serves recognition and retrieval, though the set that works best for recognition "will not necessarily work best" for retrieval (p. 100).
- "The full effect of the ranking function, its parameters, and the IDF function is a question that still warrants further research" (p. 85).
- Morpho Challenge IR significance is hard to reach with the limited number of queries (p. 93).

### Inferred from the experimental design

1. **Very few queries** (17 / 25), without reported significance for the main index-unit and fusion claims (only the morph-vs-word LM comparison is stated as significant, p. 50). Differences of 1–3 MGAP points (e.g., interleaved vs combined) are probably within noise.
2. **The high-Q-OOV scenario is simulated** by deleting training sentences. It inflates the unseen-word effect in a controlled but artificial way; its Q-OOV rate is not given.
3. **No raw word-form index in SDR.** The baseline is already lemmatized, so the "raw → normalized" step of our design is not measured for speech.
4. **Tampere is a partition** (each story relevant to exactly one query). That is closer to topic classification than to typical ad hoc retrieval and favours recall-oriented methods such as query expansion (which reaches 91.8 MAP).
5. **Complementarity is inferred from fusion gains only**: no overlap, unique relevant hits, oracle union or per-query win/loss. A gain from the combined index could come partly from term-weight effects (the author notes that combined weights may be "unoptimal").
6. **Several numbers are not mutually consistent** across tables (§19). The overview mixes values from different publications and setups. Table 5.3's footnoted 87.5 comes from a third source.
7. The **overview only** was available; details in Publications I–VII (topic lengths, test type, stop lists) could not be checked.

## 13. What the work proves

Within Finnish SDR on these small collections:

- **Morph-based ASR language models give much better retrieval than a large word LM**, especially when query words are unseen: MAP 84.4 vs 77.9 and 64.2 vs 48.0 (Table 5.2); stated as "significantly better" (p. 50; test NOT_REPORTED). The morph system is also faster.
- **Unsupervised morphs and rule-based lemmas are roughly equivalent index units on long queries.** Lemmas are better on short queries (Table 5.3; Pod N short 34.7 vs 30.4).
- **Combining the two lexical representations beats either alone in every reported Podcast condition** (Table 5.3; also Table 6.1 and Table 5.4 diagonals). The gain is largest (+4.8 MGAP, +22.5% relative **[computed]**) for short queries with simulated unseen words.
  - This is **direct evidence that two morphological representations of the lexical channel retrieve partly different relevant material**, and that the value of combining them depends on query properties.
  - Caveat: this is shown by aggregate gains only, without significance tests.
- **Rank-weighted confusion-network expansion** improves morph-index retrieval most where recognition misses unseen words (19.0 → 26.9 MGAP, Table 6.1).
- **The morph-vs-lemma ordering depends on the ranking function and IDF**, not just on the representation (Table 6.2).
- In the Morpho Challenge meta-analysis, **linguistic evaluation metrics differ strongly in how well they predict IR MAP**: in Finnish, EMMA ρ = 0.656 (described by the author as a high correlation) and EMMA-2 0.627, while MC and CoMMA variants are poor (0.071–0.313) (Fig. 7.1, p. 94).

## 14. What the work does NOT prove

- **Anything about lexical–dense (semantic) complementarity or hybrids.** There is no neural or dense retriever. LSI is used as a replacement index, not fused with the term index.
- **How morphological representation changes complementarity with a fixed second channel.** Morph vs lemma are the two *fused* channels themselves; there is no third, fixed channel against which raw/stem/lemma variants are compared.
- **Which relevant documents each representation uniquely retrieves**, or the overlap. Only fused-run averages are reported.
- **A raw → stem → lemma progression.** No raw word-form index and no stemmer in the speech experiments. The text-IR comparison with raw words and stemming is only summarized qualitatively from another paper.
- **Statistical reliability of the main representation and fusion claims.** No tests are reported for them, and the query sets are small.
- **Transfer to real (non-simulated) OOV distributions or to text retrieval.** On clean text, base forms beat morphs (Kurimo et al. 2010a as cited, p. 73).
- **That combination is universally better**: on Tampere with the word-LM/word-CN setting only single representations are shown; interleaving is sometimes below the combined index (Table 5.3).

## 15. Relationship to current Uzbek evidence

- **No Uzbek data.** Typologically, Finnish and Uzbek are both agglutinative and suffixing with long suffix chains.
  - Context (not from the paper): Uzbek stem changes (e.g., final k/g, q/g' alternation before vowel-initial suffixes) are a smaller-scale analogue of Finnish consonant gradation, the very allomorphy that splits Morfessor stems here.
- **Analyzer coverage** is the direct Uzbek parallel. National Uzbek lemmatizers and analyzers (Xusainova: >32k simple + >7.5k compound lexemes; Bakaev Morphoanalyzer; Turayev 32,225 base forms) work over finite lexicons. This thesis shows that lemma indexing fails precisely on names and unseen words outside the lexicon, while subword units still match. This motivates measuring **analyzer coverage per query** in our Uzbek benchmark.
- **Close Turkic spoken-retrieval cards in this batch:**
  - Parlak & Saraçlar 2009 (CR000691; Turkish SDR: no stem vs prefix vs parser stem vs Morfessor stem; word+morph STD cascade);
  - Arısoy et al. 2009 (CR001390; Turkish STD with word / stem+ending / morph indexes; word→morph cascade).
  - This thesis extends that line from *choosing* a unit to *combining* morph and lemma indexes for ranked SDR. Its opponent (Saraçlar) and cited work (Parlak & Saraçlar 2008, p. 81) connect the two lines.
  - Across the three, the recurring finding is that subword/morph units rescue OOV terms and that two lexical representations are complementary. None of them has a dense retriever.
- Consistent with MORPH-001 (Can et al. 2008): query length interacts with the effect of morphological processing. Here, short queries favour lemmas and gain most from combination.

## 16. Relationship to CURRENT_GAP

**Classification:** *supports* + *narrows (novelty boundary)* + *no material effect on the residual core*.

- **Supports** the v0.8 premise that changing the morphological representation of the lexical channel changes *what* it retrieves, not just how well:
  - morph and lemma indexes are complementary;
  - the combination gain depends on query length and unseen-word rate (Tables 5.3, 6.1).
- **Narrows** the claims we can make. Already occupied since 2005–2012 (Finnish SDR):
  - "fusing two different morphological representations of the lexical channel";
  - "query OOV/length moderates the benefit of morphological representation or its combination".
  These are already listed as non-claims in spirit ("query-type analysis … not new"; "raw/stem/lemma compared"). This work adds an agglutinative, defended-PhD citation for them.
- **Does not touch the residual core**:
  - no fixed semantic dense retriever D;
  - no raw/stem/lemma × same-D design;
  - no unique-hit / overlap / oracle-union decomposition;
  - no per-query linkage.
  The complementarity measured is **lexical–lexical**, only as aggregate fusion gain.
- Its design suggests a useful **control condition** for our own study: to attribute a lemma-induced change in lexical–dense complementarity to morphology rather than to "any second representation", report a lexical–lexical fusion (e.g., BM25_stem + BM25_lemma, or BM25_lemma + subword BM25) beside `H_lemma = fusion(BM25_lemma, D)`.

**Proposal:** keep v0.8 refined unchanged. Add this thesis to the evidence boundary as early evidence of **intra-lexical morphological complementarity** in an agglutinative language, measured only by fusion gain. This is a proposal only; `CURRENT_GAP.md` has not been edited.

## 17. Implications for our research design

- **Lexical variants.** Keep `BM25_raw / BM25_stem / BM25_lemma`. Consider adding a **subword variant**, `BM25_morph` (Morfessor trained on Uzbek text) or a character n-gram index, as a secondary control:
  - it does not depend on the lemmatizer's lexicon;
  - the thesis and Morpho Challenge (as cited) show that such units are competitive and complementary.
  Treat it as an optional arm, not a new core claim.
- **Analyzer-coverage query feature.** For each query, record the share of tokens that the Uzbek lemmatizer/stemmer **cannot analyze** (unknown lemma, names, foreign or Russian loans, script/apostrophe variants). This is the direct analogue of Q-OOV here, and a likely moderator of which lexical variant finds unique relevant documents.
- **Query length.** The morph-vs-lemma ordering flips with query length (Tables 5.3, 6.2). Stratify analyses by query length and keep both short (keyword) and long (descriptive) query versions, as Podcast did.
- **Fusion control.** Report a lexical–lexical fusion (stem + lemma, or lemma + subword) as a control, so that the lexical–dense complementarity shift can be separated from generic "two representations" gains. Use the same fusion rule (e.g., RRF / fixed convex) as for `H_x`.
- **Measurement.** The thesis shows what is lost without it: only aggregate fusion gains. We should report, per query:
  - unique relevant hits for each run;
  - the intersection;
  - the oracle union at fixed k;
  - significance at query level.
- **Ranking function and IDF.** Orderings changed between cosine and BM25 and between IDF variants (Table 6.2). Fix BM25 (k1, b, IDF flooring) before comparing representations, and check sensitivity on dev only.
- **Stop-list and IDF pitfall for subword or suffix units.** Suffix-like units occurring in more than half of the documents get negative BM25 IDF; without a stop list, performance "was severely degraded" (p. 93). If we index subwords or keep suffixes, floor the IDF or apply a frequency stop list.
- **Choosing the Uzbek stemmer or lemmatizer.** How well linguistic accuracy predicts IR usefulness depends strongly on the metric (Finnish ρ from 0.071 to 0.656, Fig. 7.1), and even the best metric (EMMA) orders methods only imperfectly. Select morphology tools by retrieval dev results, not by the reported analyzer accuracy (e.g., 97.5%).
- **Hypothesis.** No direct evidence for or against our hypothesis. It gives a plausible mechanism: lemma normalization helps where the analyzer covers the query and hurts or is neutral where it does not. This predicts that the lemma-induced change in unique lexical hits relative to D should depend on analyzer coverage.

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| Spoken document retrieval (SDR) | Finding relevant parts of audio recordings for a typed query | ASR transcription + text IR over spoken documents or replay points |
| ASR / language model (LM) | The speech recognizer and its model of which word (or piece) sequences are likely | n-gram LM over words or morphs, decoded with acoustic models |
| OOV / Q-OOV | A word the recognizer's vocabulary does not contain / the share of such words among query words | Out-of-vocabulary; query OOV rate |
| Morph | A piece of a word learned automatically, e.g. `kirja+sta+ni` | Surface realization of a morpheme; here, Morfessor segments |
| Morfessor Baseline | Unsupervised algorithm that learns word pieces from raw text by balancing lexicon size vs corpus coding length | MDL: argmin L(x|θ)+L(θ) (Eq. 3.1) |
| Base form (lemma) | Dictionary form produced by a rule-based analyzer | TWOL two-level morphology lemmatization |
| Combined index | One index containing both morph terms and base-form terms | Representation-level union of term sets |
| Interleaving | Alternately take the next document from each of two ranked lists, skipping duplicates | Parameter-free rank-level fusion |
| Allomorphy | Same meaning unit spelled differently in different forms (Finnish *vesi / vede- / vet-*) | Surface variation of one morpheme |
| Confusion network (CN) | Compact list of competing recognized alternatives at each position, with probabilities | Sequence of confusion sets (Mangu et al. 2000) |
| CL vs rank weighting | Count alternatives by their probability, or by 1/their rank in the set | Eqs. 6.1, 6.2 |
| MAP / MGAP | Average precision over relevant items; its time-tolerant version for replay points | Eqs. 2.18–2.20 |
| LSI | Compresses the term-document matrix so related terms share dimensions | Rank-k SVD of X (Eqs. 2.12–2.14) |
| Complementarity (project term) | Each representation or channel finds relevant items the other misses | Unique relevant hits, overlap, oracle-union gain (not measured in this work) |

## 19. Open questions / verification needed

1. **Table 5.3 vs Tables 5.4 / 6.1 / 6.2 (Podcast normal):**
   - morph 43.0 / 30.4 vs 43.8 / 31.8 (Table 6.1 1-best and Table 6.2 raw/Eq. 6.5; 43.8 also on the Table 5.4 diagonal);
   - combined 46.0 / 37.3 vs 46.2 / 37.9 (Table 6.1; 46.2 also on the Table 5.4 diagonal);
   - interleaved 46.6 / 35.1 vs 46.8 / 36.1 (Table 6.1 only).
   All are attributed to Publication VI; the base-form values agree (43.8 / 34.7). The source of the difference cannot be determined from the overview; check Publication VI (ACM TSLP 8(1), 2011).
2. **Tampere "comb. 87.5"** in the Publication II column is footnoted to Kurimo et al. (2005), a different paper, so the 87.5 vs 79.2 / 78.0 contrast may mix setups.
3. **Query-expansion baselines** (Sec. 5.2.3: 77.7 / 75.7, attributed to Publication II) equal the Publication III column of Table 5.3, not the Publication II column (79.2 / 78.0).
4. **Sec. 7.3, p. 95:** "the balanced F-score at β = 0" contradicts Eq. 7.1 (β = 1 is balanced; β = 0 is precision only). Probably a typo for β = 1.
5. **Fig. 7.1** shows CoMMA-A0 / A1, which the text does not define (it defines B0, B1, S0, S1). The caption says "IR and SMT evaluations", but the panels show IR/MAP only.
6. The Table 5.3 caption and the Table 6.1 caption mention text-corpus MAP results, but neither table has a text-corpus column.
7. **Not reported in the overview:** the significance test, the Q-OOV rates of the simulated scenario, the MGAP window width for Podcast, query lengths, stop-list use in SDR, and the number of assessors. Publications V and VI should hold these.
8. **Possible duplicates for the coordinator:** Publications IV (SIGIR 2007), V (Interspeech 2008) and VI (ACM TSLP 2011) may exist as separate canonical_ids; the primary numbers should be cited from them. Publication VI is the most relevant (morph / base / combined / interleaved on Podcast).
9. **Morpho Challenge IR numbers** (raw words vs stemming vs base forms vs morphs vs n-grams, BM25): Kurimo, Virpioja & Turunen 2010a, and Kurimo, Creutz & Turunen 2009 ("Morpho Challenge evaluation by information retrieval experiments"). These are worth a check as a multi-representation BM25 text-IR source for Finnish.

## 20. Decision after deep dive

- **Keep current gap?** Yes. v0.8 refined remains valid (§16).
- **Modify gap?** No change proposed. Optionally add to the evidence boundary: "complementarity between two morphological representations of the lexical channel (Finnish morph + lemma, fusion gain larger for short / high-OOV queries) exists since 2005–2012; lexical–dense complementarity under morphological change is not addressed" (researcher's decision).
- **Add decision?** Proposed for `decisions/DECISIONS.md` (researcher's decision):
  - "Record per-query analyzer coverage (share of query tokens the Uzbek lemmatizer cannot analyze) as a query feature";
  - "Report a lexical–lexical fusion control (stem+lemma or lemma+subword) alongside H_raw/H_stem/H_lemma";
  - "Floor BM25 IDF / use a frequency stop list if subword or suffix units are indexed".
- **Add experiment?** Optional arm: `BM25_morph` (Morfessor or BPE trained on Uzbek text) with the same D and the same unique-hit / overlap / oracle-union measurements. It costs little once the pipeline exists.
- **Add citation to Chapter I?** Yes:
  - §1.1 (morphological normalization vs unsupervised subword units in lexical IR for agglutinative languages; analyzer-lexicon limits);
  - §1.3 (early evidence that combining two lexical representations helps and that the gain depends on query properties, without lexical–semantic fusion or complementarity decomposition).
- **Proposed `MASTER_INDEX.md` row** (to add after approval):

| MORPH-025 | Turunen — *Morph-Based Speech Retrieval: Indexing Methods and Evaluations of Unsupervised Morphological Analysis* (PhD, Aalto University, DD 97/2012; overview part read) — [deep dive](deep-dives/2012_Turunen_PhD_Morph_Based_Speech_Retrieval.md) | 2012 | A (small collections; main claims without reported significance) | HIGH | Finnish SDR (Tampere 17 q; Podcast 136 h, 25 topics, MGAP): Morfessor morph LM ≫ 490k word LM (MAP 84.4 vs 77.9; high Q-OOV 64.2 vs 48.0). Index units: morph ≈ lemma on long queries, lemma better on short; morph+lemma combined/interleaved beats both in all Podcast conditions, largest for short high-Q-OOV queries (26.1 vs 21.3). Rank-weighted confusion networks up to +41.6% relative. BM25 only as sensitivity check; LSI and query expansion as the only "semantic" tools. Lexical–lexical complementarity by aggregate fusion gain only: no dense channel, no raw index, no overlap/unique-hit/oracle or per-query analysis. Cross-table inconsistencies (Table 5.3 vs 6.1). |
