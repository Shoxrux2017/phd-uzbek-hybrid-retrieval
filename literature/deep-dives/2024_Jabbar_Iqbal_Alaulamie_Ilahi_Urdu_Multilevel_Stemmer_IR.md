# Jabbar, Iqbal, Alaulamie & Ilahi (2024): Building a Multilevel Inflection Handling Stemmer to Improve Search Effectiveness for Urdu Language

**Targeted deep-dive status:** COMPLETED (AI-assisted, pending researcher review)
**Completed:** 2026-09-28
**Literature ID:** `MORPH-038` (assigned 2026-09-28, approved by researcher)
**Systematic-review record:** `CR000935`. Full-text triage: include, reading priority HIGH, reading tier "2 — важно", `carries_complementarity_evidence = YES`. We qualify that flag (§10, §16). The only per-query evidence is a line chart of per-query precision for four **lexical** runs: no stemming and three stemmers, all under BM25 (Fig. 10). It shows stem-vs-raw differences per query. It is not a relevant-set overlap, a unique-hit count or a lexical–dense comparison. The paper has no dense or semantic channel.
**Provenance:** AI-assisted deep dive (Claude). The whole paper (22 PDF pages: main text pp. 1–15, with the Conclusion body and declarations on p. 15; Appendices A–D pp. 15–18; references pp. 19–22) was read from the pdftotext extraction. This PDF is the **accepted author version** ("not been fully edited and content may change prior to final publication", header of every page). It has **no real printed page numbers**: every footer reads "VOLUME XX, 2017" with a placeholder page number. All locations below therefore use **PDF page numbers** ("PDF p. N"). Page images were checked at 110 dpi for PDF pp. 1 (abstract, header), 10 (evaluation criteria, BM25 paragraph, Eqs. 1–9), 11 (Tables 10–12, CURE sentence), 12 (Table 13, Figs. 4–5), 13 (Figs. 6–7, Table 14), 14 (Figs. 8–10) and 17 (Appendix D, tokenization markers). Figs. 9 and 10 were also checked on 300-dpi and 600-dpi crops. Numbers computed by us are marked **[computed]** and were recomputed with Python. Values read from plotted lines are marked **[visual reading, approximate]**.
**Source rule:** **the paper is the primary and only authoritative source.** No code, dataset repository, website, later paper or background knowledge is used as evidence about what the authors did. The GitHub link in the paper's Data Availability Statement (PDF p. 15) was **not** consulted. Only the bibliographic record was checked on the web (bibliographic check: OpenAlex record for DOI 10.1109/ACCESS.2024.3373714; doi.org resolves to IEEE Xplore document 10460562). The final published version may differ from this author version. We did not see it: IEEE Xplore could not be fetched.
**Verification:** independent AI verifier pass 2026-09-28; 12 findings addressed.
**Reliability:** **B**. The paper is a peer-reviewed journal article (IEEE Access) and it is verifiable. Its IR evidence is thin:
- one small collection (50 queries);
- BM25 configuration not reported;
- no significance tests;
- the MAP differences are in the fourth decimal place;
- several text statements do not match the paper's own tables (§9, §19).

---

## Кратко для исследователя (RU)

- **Что сделано.** Авторы предлагают **правиловый стеммер урду UTS** (Urdu Text Stemmer). Он обрабатывает многоуровневые аффиксы, со-суффиксы, префиксы, инфиксы (ломаные мн. ч. арабского типа), сложные слова и «мохмил» — рифмованные слова-«эхо» вроде *roti woti*. Стеммер оценён двумя способами:
  - **внутренне (intrinsic)**, по сравнению с экспертной разметкой: собственный словарный корпус 56 074 слова и текстовый корпус 20 000 слов (Tables 10–12, PDF p. 11);
  - **внешне (extrinsic)**, в поиске: **BM25** на коллекции **CURE**, 1 096 документов, 50 запросов (Sec. V.C, PDF p. 11; Table 13, PDF p. 12).
- **Главные числа поиска** (Table 13, PDF p. 12), варианты «без стемминга → UTS»:
  - R@10: 0.4822 → 0.5194 (+7.7% отн.);
  - P@10: 0.68 → 0.712 (+4.7% отн.);
  - MAP: 0.2585 → 0.2598 (+0.5% отн., **+0.0013 абс.** **[computed]**).
  - Два других стеммера (Assas-Band, Multi-Step) ещё ближе к базовому варианту по MAP: 0.2587 и 0.2590.
- **Морфологические варианты лексического представления есть, но только «сырые словоформы vs стеммы».** Сравниваются без стемминга и три стеммера при одной и той же модели BM25. Это контролируемое сравнение вариантов лексического канала. **Леммы как отдельного условия поиска нет.** Эталон при внутренней оценке авторы называют «human extracted lemma list», но в поиске участвуют только стеммеры.
- **BM25 не описан.** Реализация, k1/b, токенизация индекса, стоп-слова, нормализация и применение стеммера к документам в статье не указаны (NOT_REPORTED). Состав варианта «No stem» тоже не описан.
- **Нет плотного поиска, нет гибрида, нет анализа взаимодополняемости:**
  - нет fusion;
  - нет перекрытия результатов и уникально найденных релевантных документов;
  - нет oracle union.
- **Разбор по запросам есть только в виде графика** (Fig. 10, PDF p. 14): точность (по-видимому, P@10; авторы не уточняют) по 50 запросам для четырёх лексических прогонов.
  - Нет подсчёта выигрышей/проигрышей и нет статистического теста.
  - Авторы пишут, что UTS лучше «на большинстве запросов». По графику этого проверить нельзя: линии в основном совпадают. Видны расхождения в обе стороны: на нескольких запросах вариант без стемминга или другой стеммер выше UTS **[visual reading, approximate]**.
- **Внутренняя точность стеммера ≠ эффективность поиска.** CSWF (доля правильно выделенных стемов) растёт с 89.32% (Assas-Band) до 95.59% (UTS) (Table 12). При этом MAP в поиске меняется на 0.0011 (0.2587 → 0.2598) **[computed]**. Это прямая иллюстрация различия, которое мы уже фиксируем для узбекских работ (Xusainova, Bakaev).
- **Внутренние несоответствия в статье** (подробно §9, §19), например:
  - в тексте UTS приписана точность 93.95%, а Multi-Step — 95.586%, тогда как по Table 11 у UTS 95.58, у Multi-Step 93.57 (значения переставлены);
  - ICF конкурентов в тексте «55% и 51%», в Table 12 — 55 и 53;
  - «~5% average precision» в Sec. V.E на самом деле относится к P@10;
  - ссылки на стеммеры перепутаны ([13] вместо [11], [62] вместо [60]).
- **Для нашего gap:** работа подтверждает, что вариант «raw vs stem» BM25 уже изучался для урду. Это давно занятый элемент. **Ядро v0.8** (raw/stem/lemma × фиксированный D → уникальные релевантные документы / перекрытие → прирост гибрида → признаки запросов) **не затрагивается**. Предложение: gap не менять.
- **Практическая польза для нас:**
  1. Стеммер/лемматизатор для узбекского выбирать по результатам поиска на dev-выборке, а не по внутренней точности.
  2. Сдвиги R@10/P@10 могут не отражаться в MAP. Нужны абсолютные разности, таблица «выигрыш/ничья/проигрыш» по запросам и парный тест, а не линейный график.
  3. Урду-стеммер режет персидско-арабские аффиксы (*khana*, *dar*, *na-*, *be-/ba-*, *-mand*). Близкие аффиксы есть и в узбекском: *-xona*, *-dor*, *no-*, *be-*, *-mand* (контекст, не из статьи). Надо заранее решить, снимает ли узбекский «stem»-вариант словообразовательные аффиксы.
  4. Ложное усечение имён собственных (*Irshad → rushad*) поддерживает признак «именованные сущности» в таксономии запросов.

---

## 1. Bibliographic record

- **Authors:** Abdul Jabbar, Sajid Iqbal, Abdullah A. Alaulamie, Manzoor Ilahi
  - The PDF prints "Abdullah Alaulamie"; OpenAlex gives "Abdullah A. Alaulamie".
- **Affiliations** (PDF p. 1):
  - COMSATS University Islamabad (Jabbar, Ilahi);
  - King Faisal University, Saudi Arabia (Iqbal, Alaulamie);
  - Bahauddin Zakariya University, Multan (Iqbal).
  - Corresponding author: S. Iqbal. The PDF prints the template placeholder "Second A. Author" next to his e-mail.
- **Year:** 2024
- **Venue:** *IEEE Access*, vol. 12, pp. 39313–39329 (bibliographic check: OpenAlex). The volume and pages are not printed in the author-version PDF.
- **DOI:** `10.1109/ACCESS.2024.3373714`. It is printed in the PDF header and resolves to IEEE Xplore document 10460562 (bibliographic check: doi.org redirect). The PDF also carries a leftover template DOI, "10.1109/ACCESS.2017.Doi Number" (PDF p. 1).
- **Official record:** https://ieeexplore.ieee.org/document/10460562 (not fetched; bibliographic check via OpenAlex only)
- **Funding:** Deanship of Scientific Research, King Faisal University, Grant No. 5428 (PDF p. 15)
- **Data (stated in paper, PDF p. 15):** https://github.com/abduljabbar2017/Urdu-stemmer-dataset (not consulted)
- **Source type:** peer-reviewed open-access journal article; the PDF analysed is the accepted author version (22 pages including appendices)
- **Reliability:** B
- **Full text available:** yes (`07_full_text/pdfs/CR000935.pdf`)

## 2. Why this work matters to the PhD

It is a recent, peer-reviewed example of a **morphology-specific normalizer** for a morphologically complex, low-resource language. The normalizer is evaluated **both intrinsically and extrinsically, inside BM25 retrieval**, against a no-stemming baseline on a standard test collection. This is the lexical half of our design (`BM25_raw` vs `BM25_stem`) in another language.

| Axis | Relation |
|---|---|
| Lexical retrieval | BM25 only, one unreported configuration; four lexical representations: no stem + 3 stemmers (Table 13) |
| Semantic retrieval | **Absent** |
| Hybrid retrieval | **Absent** |
| Uzbek morphology | Indirect. Urdu is Indo-Aryan, Perso-Arabic script, with Arabic broken plurals and Persian derivational affixes. Uzbek is Turkic, agglutinative and suffixing. They share Persian/Arabic loan affixes and echo/pair-word formation (context, §15) |
| Low-resource retrieval | Direct: Urdu, small test collection (CURE, 50 queries) |
| Current gap | Adds one more "raw vs stem under BM25" data point (already occupied). Does **not** touch the morphology → lexical–dense complementarity core (§16) |

## 3. Research problem

### Simple explanation

Urdu words change their form in many ways:
- endings pile up (several suffixes in a row);
- Arabic-style plurals change letters inside the word (*marz* "disease" → *amraaz* "diseases");
- compounds are written as two or three space-separated words (*jail khanah jaat* "prisons");
- nonsense "echo" words are attached for emphasis (*roti woti*, "bread and such").

Existing Urdu stemmers handle only some of these, so different forms of the same word stay different, and search misses documents. The authors build a stemmer that handles all of them. They then check that (a) it cuts words correctly and (b) it makes search better.

### Formal formulation

The paper states no formal research questions. The contribution list (PDF pp. 1–2) claims:
1. UTS handles multi-level inflections;
2. it handles co-suffixes;
3. it removes Mohmil words;
4. affix lists and rules are provided;
5. it is "the first effort to handle multi-levels inflections and derivations in the Urdu language";
6. it is evaluated by "both direct and indirect evaluation techniques".

Retrieval task (Sec. V.B, V.E; PDF pp. 10, 12): ad hoc document retrieval with BM25. Different stemmers are presumably applied to form the index and/or query terms (not stated; see §5), and the effect on R@10, P@10 and MAP is compared against no stemming.

## 4. Main idea

### Simple explanation

UTS runs each word through a fixed sequence of rule sets:
1. undo compounds and echo words;
2. strip suffixes, fixing the ending if needed;
3. strip prefixes/circumfixes;
4. undo broken plurals using letter patterns;
5. look the word up in an exception table.

When a rule could give several candidate stems, UTS keeps the one found in a stem dictionary.

### Concrete example (paper's own examples)

- `وعدے` [waday/promises]: three suffix rules give three candidates, `وعد` [wad], `وعدا` [wada] and `وعده` [wadah]. Only `وعده` [wadah/promise] is in the stem-word list (SWL), so it is kept (Step 4, PDF pp. 8–9).
- `احکام` [ehkaam/orders] matches infix pattern 509. The rule "remove the first and fourth letter ا [alif]" gives `حکم` [hukum/order] (Table 9, PDF p. 9).
- `چوری چکاری` [chori chakari/theft]: the Mohmil (echo) part is removed and the stem `چور` [chor/thief] is produced. Assas-Band and Multi-Step leave it unchanged (Table 14, PDF p. 13).
- Failure case stated by the authors: the proper noun `ارشاد` [Irshad] is wrongly stemmed to `رشد` [rushad/guidance] (Sec. VI, PDF p. 14).

### Formal method

A deterministic, rule-based pipeline (Algorithm 1, PDF p. 7). The inputs are:
- a prefix list PL and a suffix list SL (Appendices B–C, lists 1–8 by affix length);
- compound-word reduction rules CWR and Mohmil rules (Table 5, Appendix A);
- infix patterns (Table 8);
- a stem-word list SWL and a reference lookup table.

Length constraints (Step 5, PDF p. 9):
- minimum input word length 4 characters;
- minimum output stem length 3 characters; a 2-character stem is accepted only if it is found in SWL;
- affixes up to 8 characters long, matched longest-first.

## 5. Architecture / algorithm

Seven steps (Algorithm 1 and Sec. IV, PDF pp. 7–10):

1. **Preprocessing / tokenization.** The text is split on hard space and on stop-words (`کا` ka, `پر` par, `سے` se). Non-Urdu tokens and stop-words are removed. The token-marker list in Appendix D (PDF pp. 17–18) includes Latin letters, digits, brackets, quotation marks and apostrophes (U+0027, U+2018, U+2019), hyphen and Arabic punctuation.
2. **Compound-word reduction.** Bigrams and trigrams are reduced by the CWR rules, which remove compound affixes and Mohmil words. The output may still need stemming (e.g., `مردانہ وار` → `مردانہ`, which still carries the suffix -ana).
3. **Split into unigrams** by hard space.
4. **Suffix removal and recoding.** If several rules apply, the candidate stems are verified against SWL; exceptions go through table lookup (e.g., `کرائے` → `کرایہ`).
5. **Circumfix, then prefix, then suffix removal** with PL/SL, under the length constraints.
6. **Infix handling.** Pattern IDs encode word length plus pattern number (Table 8). Candidate stems are verified against SWL. Exceptions go through lookup (`احساس` → `حس`, `اعداد` → `عدد`).
7. **Reference lookup** for the remaining words (e.g., `اساتذه` → `استاد`).

The authors state the complexity as O(n) time and linear space, vs O(n²) for the Multi-Step stemmer [11] (PDF pp. 13–14).

**Retrieval model** (Sec. V.B, PDF p. 10): "we have chosen the BM-25 retrieval model based on the probabilistic retrieval framework [5]", with a generic description of BM25's components. The following are **NOT_REPORTED**:
- toolkit or implementation;
- k1 and b;
- index tokenization;
- stop-word handling and diacritic normalization in the IR runs;
- whether stemming was applied to documents, queries or both (Algorithm 1 is written for "query_text");
- which CURE topic fields formed the queries;
- MAP cut-off depth.

## 6. Data

### Intrinsic evaluation: USED (Urdu Stemmer Evaluation Dataset), Sec. V.C, PDF pp. 10–11

- **Word corpus:** 56,074 Urdu words: unigrams, bi-/tri-gram compounds, broken plurals, words with infixes. Sources: four Urdu grammar books, Urdu-morphology resources [80] (a dangling citation: the reference list ends at [78]), an online Urdu encyclopedia, and CLE word lists.
  - Preprocessing: diacritics removed; stop-words, punctuation, numbers and symbols removed; English/French characters deleted.
- **Text corpus:** 20 news texts from BBC Urdu and DAWN, 5 per topic (Table 10, PDF p. 11): politics 6,500 words, literature 4,600, science 5,300, technology 3,600. Total 20,000 **[computed ✓]**. It is fed to the stemmer without preprocessing.
- **Gold standard:** "human experts ... native Urdu speakers with relevant qualifications"; the annotations were "cross validated by each other" (Sec. V.D, PDF p. 11).
  - Number of annotators and agreement: NOT_REPORTED.
  - The same annotations were "used for the rule extraction which leads to the development of stemmer" (PDF p. 11). The rules may therefore have been derived from the evaluation data; no train/test split is described (§12).

### Extrinsic (IR) evaluation: CURE

- The paper's entire description (Sec. V.C, PDF p. 11): "The Urdu retrieval experiments have been carried out on 1096 documents from 254 domains with 50 queries from [77]". [77] is Iqbal et al., "CURE: Collection for Urdu Information Retrieval Evaluation and Ranking", arXiv 2020.
- **Relevance judgments:** the construction, graded/binary scale and number of relevant documents per query are **NOT_REPORTED** in this paper.
- **Inference from the reported numbers [computed]:**
  - If every query had ≤ 10 relevant documents, each query's R@10 would be ≥ its P@10, so mean R@10 ≥ mean P@10.
  - Table 13 has mean R@10 (0.48–0.52) < mean P@10 (0.68–0.71) for every run.
  - So **at least some queries have more than 10 relevant documents**, and R@10 cannot reach 1 for them.
- **Splits:** none. There is no tuning described, so no dev set is needed for BM25 as reported. The stemmers are rule-based and were not tuned on CURE, as far as the paper says.

## 7. Baselines

| Baseline | What it is | Why selected (paper) | Fair comparison? |
|---|---|---|---|
| No stem | BM25 over unstemmed terms | Reference for relative improvement | **Partly.** Its preprocessing (stop-words, diacritics, tokenization) is NOT_REPORTED, so it is unclear whether only the stemming step differs |
| Assas-Band [60] (Akram et al., 2009) | Affix + affix-exception-list rule-based stemmer | "high accuracy among the rule-based Urdu stemmer ... representative of Urdu rule-based stemmers" (PDF p. 11) | Yes for IR (same BM25 run). The provenance of its Table 11 accuracy (91.2) is unclear: the text quotes a different figure (92.97% on 21,757 words) for it (§9, inconsistency 3) |
| Multi-Step / "MU" [11] (Jabbar, Iqbal, Akhunzada & Abbas, *J. Exp. Theor. Artif. Intell.*, 2018, as cited on PDF p. 19) | The first author's earlier multi-step hybrid stemmer | "the MU stemmer [13] is better among infixes removal stemmers [65], [69]" (PDF p. 11; [13] is a citation slip for [11]) | Yes for IR. It is the authors' own previous system; all implementations were presumably run by the authors (not stated) |
| Khan et al. [65]; Husain et al. [13] | Template-based infix stemmer; n-gram statistical stemmer | Intrinsic comparison only (Table 11) | **No.** Their Table 11 figures match the values the text quotes from those papers' own corpora (19,351 and 1,200 words), not USED (§9) |

**Not present:** a truncation baseline (first-n characters), a lemmatizer as an IR condition, any statistical or unsupervised stemmer in IR, any dense or semantic retriever, any fusion.

## 8. Metrics

### Intrinsic metrics (Sec. V.A, PDF p. 10)

| Metric | Definition (paper) | Simple meaning |
|---|---|---|
| Accuracy, Precision, Recall, F-score | Eqs. 1–4 over TP/TN/FP/FN against the "human extracted lemma list" | How often the produced stem equals the expert stem. What counts as TP/TN/FP/FN for a stemmer is not defined |
| ICF (Index Compression Factor) | Eq. 5 prints `ICF = n − s`, but it is reported as a percentage; the values equal `(n − s)/n × 100` **[computed ✓]** | How much the vocabulary shrinks after stemming |
| WSF (Words Stemmed Factor) | `WS/TW × 100` (Eq. 6) | Share of words the stemmer changed at all |
| CSWF (Correctly Stemmed Word Factor) | `CSW/SW × 100` (Eq. 7) | Share of changed words that were changed correctly |
| AWCF (Average Words Conflation Factor) | `(CSW − NWC)/CSW × 100` with `NWC = S − CW` (Eqs. 8–9) | How many variant forms are merged correctly. NWC cannot be reproduced from the reported S and SW−CSW (§9) |

### Extrinsic (IR) metrics (Sec. V.B, V.E)

| Metric | Definition | Simple meaning here | Appropriate? |
|---|---|---|---|
| P@10 | relevant in top 10 / 10, averaged over 50 queries | "How many of the first 10 results are relevant?" | Yes, but shallow |
| R@10 | relevant in top 10 / all relevant, averaged | "What share of all relevant documents is in the top 10?" | Shallow. With >10 relevant documents for some queries it cannot reach 1 (§6) |
| MAP | mean of per-query average precision; cut-off NOT_REPORTED | Overall ranking quality over the whole ranked list | Yes; the only deep metric |

Not reported: nDCG, Recall at deeper cut-offs (e.g., R@100/R@1000), number of relevant documents retrieved.

## 9. Results

### Table 13: Urdu IR results on CURE, BM25 (PDF p. 12; verified on page image)

| Stemmer | R@10 (rel. %) | P@10 (rel. %) | MAP (rel. %) |
|---|---|---|---|
| No stem | 0.4822 | 0.68 | 0.2585 |
| Assas Band [60] | 0.5067 (5.1) | 0.704 (3.5) | 0.2587 (0.1) |
| Multi-Step [11] | 0.5088 (5.5) | 0.704 (3.5) | 0.2590 (0.2) |
| **UTS** | **0.5194 (7.7)** | **0.712 (4.71)** | **0.2598 (0.5)** |

Recomputed relative improvements **[computed]**:
- Assas Band: R@10 5.08%, P@10 3.53%, MAP 0.077% (printed 0.1) ✓;
- Multi-Step: 5.52%, 3.53%, 0.19% ✓;
- UTS: 7.71%, 4.71%, 0.50% ✓.

Absolute differences, UTS vs No stem **[computed]**:
- R@10 +0.0372;
- P@10 +0.032, i.e. **16 more relevant documents in the top 10 summed over the 50 queries** (0.032 × 10 × 50);
- MAP **+0.0013**.

UTS vs Multi-Step, the best competitor **[computed]**:
- R@10 +0.0106 (+2.1%);
- P@10 +0.008, i.e. 4 more relevant documents in the top 10 over 50 queries;
- MAP +0.0008 (+0.3%).

Reading:
- All three stemmers beat no stemming on the top-10 metrics by 3.5–7.7% relative.
- On MAP, all four runs lie within 0.0013 of each other.
- The paper does not test whether any difference is statistically significant.
- The text says "UTS improve the performance of retrieval nearly 5% in average precision and 0.5 % MAP" (Sec. V.E, PDF p. 12). The "nearly 5%" matches the **P@10** gain (4.71%), not average precision.

### Figs. 8–9 (PDF p. 14)

- Fig. 8 re-plots MAP as bars. The y-axis runs 0.2575–0.26, which visually magnifies differences of about 0.001.
- Fig. 9 re-plots (R@10, P@10) as bubbles. Visual reading matches Table 13.

### Fig. 10: per-query precision, 50 queries (PDF p. 14; 600-dpi crops checked)

- Four lines are plotted: No Stem, Assas Band, Multi-Step, UTS. The y-axis is labelled "Precision"; given its values in steps of 0.1 it is presumably P@10, but the paper does not say.
- The text claims: "UTS achieves higher precision on a majority of queries, as seen in Figure 10" (PDF p. 14; the preceding sentence mistakenly cites "figure 9").
- What the figure shows **[visual reading, approximate]**:
  - on most queries the four lines coincide, so ties dominate and cannot be counted from the chart;
  - UTS is visibly **above** No Stem at roughly query IDs 7, 8, 13, 20, 23, 27, 33 and 49;
  - UTS is visibly **below** at least one other run at roughly query IDs 1 (Assas-Band 1.0 vs UTS 0.9), 6 (Assas-Band 1.0, No Stem 0.9, UTS 0.8), 22 (No Stem 1.0 vs 0.8), 26 (No Stem ≈ 0.9 vs 0.8) and 43 (Assas-Band 0.9 vs 0.8);
  - several queries have P@10 ≤ 0.2 under every run, at roughly query IDs 3, 44, 46 and 48.
- Consequence: the "majority" claim is **not verifiable** from the figure. Stemming visibly hurts some queries while helping others. No win/tie/loss counts are given.

### Intrinsic results: Table 11 (PDF p. 11; verified)

| Stemmer | Acc. | Rec. | Pre. | F-score |
|---|---:|---:|---:|---:|
| UTS (words) | 94.92 | 99 | 95.58 | 97.32 |
| UTS (Text) | 91.8 | 97.48 | 93.88 | 95.65 |
| Multi-Step [11] (words) | 92.97 | 99 | 93.57 | 96.26 |
| Multi-Step [11] (Text) | 90.33 | 97.43 | 92.35 | 94.82 |
| Khan et al. [65] | – | 96.08 | 89.95 | 92.49 |
| Assas Band [60] | 91.2 | – | – | – |
| Husain et al. [13] | 84.27 | – | – | – |

- F recomputed from P and R **[computed]**: UTS (words) 97.26 (printed 97.32); Multi-Step (words) 96.21 (96.26); Khan 92.91 (92.49). The Text rows match exactly.
- **Provenance problem.** The Khan and Husain rows match the figures the text quotes from their original papers (Khan: "corpus consisting of 19351 words ... precision and recall are 89.95% and 96.08" (PDF p. 12); Husain: "84.27% accuracy on a test size of 1200 Urdu words" (PDF p. 12)). They are not results on USED, although the authors write that "The results obtained on the same data set show that UTS achieved better performance (see Figures 4 to 6)" (PDF p. 12), and Fig. 4 includes Husain. Table 11 therefore mixes same-corpus and cross-paper numbers.

### Intrinsic results: Table 12, 56,074-word corpus (PDF p. 11–12; verified)

| Metric | Assas Band [60] | Multi-Step [11] | UTS |
|---|---:|---:|---:|
| Distinct words after stemming (S) | 26,597 | 25,233 | 24,970 |
| ICF | 53 | 55 | **55.47** |
| Words stemmed (SW) | 55,128 | 54,012 | 54,179 |
| WSF | 98.31 | 96.32 | 96.62 |
| Correctly stemmed (CSW) | 49,238 | 50,693 | 51,788 |
| CSWF | 89.32 | 93.86 | **95.59** |
| NWC | 24,079 | 23,795 | 23,532 |
| AWCF | 51.10 | 53.06 | **54.56** |

Checks **[computed]**:
- ICF = (56,074 − S)/56,074 gives 52.57 / 55.00 / 55.47 ✓.
- WSF = SW/56,074 gives 98.31 / 96.32 / 96.62 ✓.
- CSWF = CSW/SW gives 89.32 / 93.86 / 95.59 ✓.
- AWCF from CSW and NWC gives 51.10 / 53.06 / 54.56 ✓.
- NWC = S − CW: if CW = SW − CSW, NWC would be 20,707 / 21,914 / 22,579, not 24,079 / 23,795 / 23,532. The implied CW (S − NWC) is 2,518 / 1,438 / 1,438; Multi-Step and UTS are identical, while their SW − CSW differ (3,319 vs 2,391). **NWC cannot be reproduced from the reported quantities.**
- The caption reads "PERFORMANCE COMPARISON USING A STANDARD DATASET", but the data is the authors' own USED word corpus.

**Intrinsic vs extrinsic [computed]:**
- CSWF rises 6.27 points from Assas-Band to UTS (89.32 → 95.59).
- In retrieval, MAP rises 0.0011 (0.2587 → 0.2598) and P@10 0.008 (0.704 → 0.712).
- Large intrinsic gains translate into very small retrieval differences here.

### Internal inconsistencies (all within the paper)

1. **ICF of competitors.** The text says "higher than competitor that has 55% value and 51 %" (PDF p. 13) vs Table 12's 55 and **53**. (The neighbouring WSF sentence is consistent: "Assas-Band stemmer [60] blindly removed the affixes and achieved the highest WSF [98.31%]", PDF p. 13, matches Table 12; the Conclusion, PDF p. 15, gives UTS "WSF of 96.62%".)
2. **Precision attribution.** The text says "MU stemmer [11] ... recall value of 99% and 95.586% precision ... Whereas UTS achieved recall and precision of 99% and 93.95%" (PDF p. 12) vs Table 11: UTS (words) Pre 95.58, Multi-Step (words) Pre 93.57. The values appear swapped, and 93.95 is in neither row.
3. **Assas-Band accuracy.** "Assas Band stemmer [60] tested their stemmer on a corpus consisting of 21757 Urdu words and achieved 92.97% accuracy" (PDF p. 12) vs Table 11: Assas Band 91.2, while 92.97 is Multi-Step (words).
4. **"Average precision".** "nearly 5% in average precision" (PDF p. 12) is actually the P@10 gain (4.71%).
5. **Citation mix-ups:**
   - "MU stemmer [13]" (PDF pp. 11, 13) vs MU/Multi-Step = [11]; [13] is Husain's n-gram stemmer;
   - "[60] is a statistical stemmer" (PDF p. 11), yet [60] is the rule-based Assas-Band;
   - "Assas-Band stemmer [62]" (PDF p. 13);
   - "evaluation method of Sirsat [11], [65]" (PDF p. 10) vs Sirsat = [71].
6. **Metric definitions.** Eq. 5 is printed as a difference but reported as a percentage. The NWC values are not reproducible (above).
7. **Figure numbering.** "The query wise performance of UTS are presented in figure 9" vs Fig. 10 (PDF p. 14).

## 10. Statistical evidence

- **Significance tests:** NOT_REPORTED for either the IR or the intrinsic results. Words like "significantly higher" (CSWF, PDF p. 13) are not backed by a test.
- **Confidence intervals:** NOT_REPORTED.
- **Runs / seeds:** not applicable; deterministic rule-based stemmers and BM25.
- **Ablation:** **none.** The contribution of each of the seven steps (compound reduction, Mohmil removal, infix handling, lookup) to intrinsic accuracy or to retrieval is not isolated.
- **Per-query analysis:** only the Fig. 10 line chart of per-query precision for four lexical runs. There are:
  - no win/tie/loss counts;
  - no per-query test;
  - no breakdown by query characteristics (length, compounds, broken plurals, proper nouns);
  - **no overlap / unique relevant hit / oracle-union analysis**, either between stemmers or between lexical and semantic channels.
- **Power (our inference, not computed):** with 50 queries, a MAP difference of 0.0013 is very likely far below the per-query AP variation, which the paper does not report. Nothing about MAP should be claimed without a paired test.

## 11. Strengths

- A controlled lexical comparison: **four lexical representations under the same BM25** on a public Urdu test collection, with a no-stemming baseline.
- Both intrinsic and extrinsic evaluation of the normalizer. The paper therefore contains, if unintentionally, evidence that intrinsic gains need not become retrieval gains.
- Linguistically detailed treatment of phenomena that simple suffix strippers miss: broken plurals, co-suffixes, loan affixes from Persian/Arabic/Hindi/English, compounds, echo words.
- Full affix lists, Mohmil rules and tokenization markers are published in the appendices (PDF pp. 15–18), which aids reproducibility. Not published in the paper: the full suffix-removal/recoding rules (deferred to "our research work [69]", PDF p. 9, although [69] is Ali et al.), the stem-word list SWL and the reference lookup table.
- The authors state concrete failure modes: proper-noun over-stemming; tokenization errors on hard-space compounds (PDF p. 14).

## 12. Limitations

### Stated by the authors

- Proper nouns can be over-stemmed ("there is no mechanism in the Urdu language to identify the proper nouns"; *Irshad → rushad*) (PDF p. 14).
- Mohmil compounds not split by hard space, "patternless words", and "confusing words that may be used as a root word or as an affix" cause wrong stems. Table lookup mitigates this but depends on its coverage (PDF p. 14).
- Text-corpus accuracy is lower than word-corpus accuracy "due to the improper tokenization and identification of proper nouns"; "a word segmentation system is still needed for Urdu" (PDF p. 14).
- Future work: more infix morphology and more context-sensitive segmentation rules (Conclusion, PDF p. 15).

### Inferred from the experimental design

1. **BM25 configuration and preprocessing NOT_REPORTED**, including for the No-stem run. We cannot confirm that only the stemming step differs between runs.
2. **The IR effect is tiny on MAP** (≤ 0.0013) and untested. The positive claims rest on shallow top-10 metrics on 50 queries.
3. **Possible evaluation–development overlap in the intrinsic results.** The expert annotations were used for rule extraction, and there is no held-out split.
4. **Cross-paper numbers in Table 11** (Khan, Husain) are presented as if comparable; the provenance of the Assas-Band accuracy (91.2) is unclear.
5. **No lemma condition, no truncation baseline, no statistical stemmer in IR.** "Stem" is a single family of rule-based stemmers.
6. **Per-query evidence is only visual**, and the stated "majority of queries" claim is unverifiable.
7. **Many internal inconsistencies** between text and tables (§9). Quote numbers from the tables, not the prose.
8. **Author version only.** The final IEEE version may have corrected some errors (not checked; §19).

## 13. What the work proves

- On CURE (50 queries), with BM25 in an unreported configuration, **all three rule-based stemmers give higher mean top-10 metrics** than no stemming: R@10 0.4822 → 0.507–0.519; P@10 0.68 → 0.704–0.712 (Table 13). It is a small effect with no significance test.
- **MAP is essentially unchanged** by stemming in this setting (0.2585 vs 0.2587–0.2598; Table 13).
- UTS has the highest CSWF, ICF and AWCF among the stemmers run on USED: CSWF 95.59 vs 93.86 / 89.32; ICF 55.47; AWCF 54.56 (Table 12). WSF is highest for Assas-Band (98.31 vs 96.62). Its word-corpus accuracy is 94.92% (Table 11). Caveat: the same expert annotations were used for rule extraction (§6), so these are not held-out scores.
- On the six sample words of Table 14, UTS gives the expected stem for all six. Assas-Band fails on all six. Multi-Step fails on the three Mohmil/multi-level cases (`چوری چکاری`, `بات چیت`, `مردانہ وار`) but is correct on the other three (`نا تجربہ کار` → `تجربہ`, `امراض` → `مرض`, `وجوہات` → `وجہ`).

## 14. What the work does NOT prove

- **That UTS improves retrieval reliably.** No significance tests; MAP differences are about 0.001; the per-query chart shows losses as well as gains.
- **That UTS is better than all prior Urdu stemmers.** Part of Table 11 is cross-corpus, and the prose misattributes several numbers.
- **Anything about lemmatization vs stemming in retrieval.** No lemma run exists.
- **Anything about dense or semantic retrieval, hybrid fusion, or lexical–dense complementarity.** None is present.
- **Which queries benefit from stemming and why.** There is no query-feature analysis and no win/loss count.
- **That the intrinsic metrics predict retrieval gains.** If anything, the paper shows a weak link: +6 points CSWF, ≈ +0.001 MAP.

## 15. Relationship to current Uzbek evidence

- **No Uzbek data.** Transfer is at the level of method and caution only.
- Context (not from the paper), on shared morphology:
  - Uzbek has Persian-origin derivational affixes parallel to those UTS strips: *-xona* (cf. Urdu *khana*), *-dor* (*dar*), *no-* (*na-*), *be-*, *ba-*, *-mand*.
  - Uzbek has echo and pair words (*non-pon*, *choy-poy*), analogous to Urdu Mohmil reduplication, usually written with a hyphen.
  - Uzbek has no productive broken plurals, but some Arabic loan plurals occur in formal/legal register.
  - These parallels matter for defining what the Uzbek `BM25_stem` and `BM25_lemma` variants should conflate.
- **Mirrors the national evidence boundary.** Bakaev and Xusainova report high analyzer or stemmer accuracy (e.g., 97.5%), but no qrels-based retrieval effect (`MASTER_INDEX` MORPH-UZ-002/004). This paper is an external example of the step those works omit, and it shows how small the retrieval effect can be even when the intrinsic gain is large.
- **Urdu cluster in our corpus:**
  - MORPH-003 UPERF (raw/stemmed/lemmatized × BM25/TF-IDF/embeddings; Recall@5);
  - HYB-010 Kazi & Khoja 2026 (CURE among its collections; lexical + embedding features + SVMrank).
  - This paper adds a stemmer-specific BM25 comparison on CURE. The three together make Urdu one of the better-covered low-resource languages for the lexical-morphology side. None of them provides the `raw/stem/lemma × fixed D` overlap decomposition.
- **Reference [5]** (Sahu, Dutta, Pal & Rasheed, "Effect of Stopwords and Stemming Techniques in Urdu IR", *SN Computer Science* 4(5):547, 2023, as cited on PDF p. 19) is a related Urdu IR lead, not yet checked against our corpus.

## 16. Relationship to CURRENT_GAP

**Classification:** *supports (background)* + *no material effect on the residual core*.

- **Already-occupied elements it touches:**
  - "raw/stem/lemma have not been compared in low-resource IR" (already REJECTED in `GAP_BOUNDARY` §4). This paper adds a raw-vs-stem comparison under BM25 for Urdu, without lemma.
  - "Morphology has been applied to low-resource search" (occupied).
- **Supports (background):**
  - The morphological representation changes the lexical channel's behaviour **per query**, in both directions (Fig. 10, visual), while barely moving the aggregate MAP.
  - This is consistent with the v0.8 premise that aggregate metrics can hide representation-induced changes in which relevant documents are retrieved.
  - It also shows that a normalizer's intrinsic accuracy does not predict its retrieval contribution.
- **No material effect on the core of v0.8 refined:**
  - no dense comparator D;
  - no fusion;
  - no unique relevant hits, overlap or oracle union;
  - no hybrid gain;
  - no link to query features.
  None of the elements of `morphological representation change → lexical relevant-set change → overlap/unique-hit change vs the same D → hybrid gain → query features` is present.
- The triage flag `carries_complementarity_evidence = YES` should be read as "per-query stem-vs-raw precision differences within lexical retrieval (visual only)". It is not complementarity evidence in the project's sense.

**Proposal:** keep v0.8 refined unchanged. Optionally list this paper in `GAP_BOUNDARY` next to UPERF as further Urdu evidence for the occupied "raw vs stem under BM25" claim. This is a proposal only; `CURRENT_GAP.md` has not been edited.

## 17. Implications for our research design

- **Choosing the Uzbek stemmer/lemmatizer.**
  - Do not select the morphology tool by analyzer accuracy alone (cf. CSWF +6 points → MAP +0.001 here).
  - Report intrinsic accuracy separately. Select, if several tools exist, by a predefined retrieval criterion on the **dev** split only.
- **Define the variants precisely.** State whether `BM25_stem` removes only inflectional suffixes or also derivational and loan affixes (*-xona*, *-dor*, *-mand*, *no-*, *be-*). The paper's stemmer strips derivational affixes aggressively (*zamindar → zamin*, *aqalmand → aqal*); this increases conflation and the risk of topic drift. Consider an inflection-only stem variant as the primary `BM25_stem`.
- **Hold all non-morphological preprocessing constant** across raw, stem and lemma: tokenization, stop-words, diacritics/apostrophe normalization, script. This paper does not document this for its No-stem run, which weakens attribution.
- **Tokenization caution.** The Appendix D marker list treats apostrophes (U+0027, U+2018, U+2019) and the hyphen as delimiters (PDF pp. 17–18). Applied to Uzbek, such a list would split *o‘/g‘* words and hyphenated pair words. Our tokenizer must protect Uzbek apostrophe letters and make an explicit, reported decision on hyphenated compounds. This is consistent with the apostrophe finding in the Mekonnen card.
- **Query taxonomy.** Add or retain these candidate features:
  - **named entities**: over-stemming of proper nouns is a documented failure;
  - **compound / pair / echo words**;
  - **loan-affix words**.
  Test whether the `raw → stem → lemma` changes in unique lexical hits concentrate on these queries.
- **Metrics and reporting.**
  - Report MAP/nDCG plus Recall at depth (R@100/R@1000), not only top-10 metrics. Here top-10 metrics moved 4–8% while MAP did not.
  - Always report absolute differences next to relative ones.
  - Report per-query **win/tie/loss tables** and a paired test (randomization or Wilcoxon), not line charts.
  - Check whether some queries have more relevant documents than the metric cut-off, since R@k is then capped below 1.
- **Benchmark size.** CURE-scale (≈ 50 queries, ≈ 1K documents) is similar to what an Uzbek pilot can afford. Effects of the size seen here would be undetectable, so the Uzbek main benchmark needs more queries, and effect sizes should be anticipated before choosing the query count.
- **Hypothesis.** No evidence for or against the complementarity hypothesis. The pattern "tiny aggregate change, visible per-query changes" is exactly the situation where set-level decomposition (unique hits, overlap) is more informative than MAP.

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| Stemming | Cutting a word down to a common base so that different forms match | Mapping of word forms to a stem by affix removal/rewrite rules |
| Lemmatization | Mapping a word to its dictionary form | Mapping to a lemma using a lexicon/morphological analysis |
| Affix stripping | Removing known prefixes/suffixes by rules | Rule-based stemming with affix lists |
| Circumfix | A prefix and suffix that together form one unit | Discontinuous affix |
| Infix / broken plural | A plural formed by changing letters inside the word (Arabic type) | Non-concatenative morphology |
| Co-suffix | A second, word-like suffix in a compound (*dar* in *rishte dar*) | Suffix-like element of a compound |
| Mohmil word | A meaningless rhyming "echo" word added for emphasis (*roti woti*) | Echo reduplication element |
| Over-/under-/mis-stemming | Merging unrelated words / failing to merge related words / removing letters that belong to the root | Conflation errors |
| Intrinsic (direct) evaluation | Checking stems against expert answers | Accuracy/P/R/F, ICF/WSF/CSWF/AWCF |
| Extrinsic (indirect) evaluation | Checking whether the stemmer improves a downstream task, e.g. search | IR metrics on a test collection |
| ICF | How much the vocabulary shrinks after stemming | `(n − s)/n × 100` (as reported) |
| CSWF | Share of changed words that were changed correctly | `CSW/SW × 100` |
| BM25 | Classic word-matching ranking (term frequency, rarity, length normalization) | Probabilistic relevance framework, parameters k1, b |
| P@10 / R@10 | Relevant share of the top 10 / share of all relevant documents found in the top 10 | Precision/Recall at cut-off 10 |
| MAP | Average of the per-query average precision over the whole ranking | Mean Average Precision |
| Complementarity (project term) | Each channel finds some relevant documents the other misses | Unique relevant hits, overlap, oracle-union gain |

## 19. Open questions / verification needed

1. **BM25 configuration and preprocessing:** implementation, k1/b, stop-words and normalization in the IR runs, stemming of documents vs queries, CURE topic fields, MAP depth. All NOT_REPORTED.
2. **Final published version:** does IEEE Access vol. 12, pp. 39313–39329 correct the text–table inconsistencies (§9: ICF 51, precision 93.95/95.586, Assas-Band 92.97, citation numbers)? The author version is all we have.
3. **NWC in Table 12** is not reproducible from S, SW and CSW (Multi-Step and UTS imply the same CW = 1,438). Is this an error or an undocumented definition of CW?
4. **Table 11 provenance:** which rows were measured on USED and which were copied from the original papers?
5. **Fig. 10:** exact per-query values and win/tie/loss counts for UTS vs No stem. They are not decidable from the chart; only the authors' data could answer this.
6. **Annotation protocol for USED:** number of annotators, agreement, and whether rule development and evaluation used disjoint word sets.
7. Check reference **[5]** (Sahu et al., 2023, Urdu stop-words and stemming in IR) against the systematic-review corpus as a possible further Urdu lexical-morphology record.

## 20. Decision after deep dive

- **Keep current gap?** Yes. v0.8 refined remains valid; see the proposal in §16.
- **Modify gap?** No change proposed. Optionally add this paper to the `GAP_BOUNDARY` Urdu evidence (next to UPERF) as a "raw vs stem under BM25, no dense, no complementarity" example (researcher's decision).
- **Add decision?** Proposed for `decisions/DECISIONS.md` (researcher's decision):
  - "The Uzbek stemmer/lemmatizer for the lexical variants is chosen by a predefined retrieval criterion on dev data; analyzer (intrinsic) accuracy is reported but is not a selection criterion";
  - "Per-query results are reported as win/tie/loss counts with a paired test, alongside absolute metric differences".
- **Add experiment?** No new experiment. Reinforce the planned design:
  - an inflection-only vs inflection+derivation stem variant as a possible sub-condition of `BM25_stem`;
  - explicit handling of Uzbek apostrophe letters and hyphenated pair words, held constant across variants.
- **Add citation to Chapter I?** Yes, as supporting evidence in §1.1:
  - morphological normalization in lexical IR for low-resource, morphologically complex languages;
  - the intrinsic vs extrinsic stemmer evaluation gap.
  Cite with care: quote only Table 13 values and state that no significance test was reported.
- **Proposed `MASTER_INDEX.md` row** (to add after approval):

| MORPH-038 | Jabbar, Iqbal, Alaulamie, Ilahi — *Building a Multilevel Inflection Handling Stemmer to Improve Search Effectiveness for Urdu Language* (IEEE Access 12, 2024, pp. 39313–39329) — [deep dive](deep-dives/2024_Jabbar_Iqbal_Alaulamie_Ilahi_Urdu_Multilevel_Stemmer_IR.md) | 2024 | B | MEDIUM | Rule-based Urdu stemmer UTS (multi-level affixes, broken plurals, compounds, echo words). Intrinsic: CSWF 95.59 vs 93.86/89.32. Extrinsic on CURE (1,096 docs, 50 queries) under BM25 (configuration not reported): no stem → UTS R@10 0.4822→0.5194, P@10 0.68→0.712, MAP 0.2585→0.2598 (+0.0013); no significance tests; per-query only as a line chart. Raw vs stem only; no lemma run, no dense, no fusion, no overlap/unique-hit analysis. Several text–table inconsistencies. |
