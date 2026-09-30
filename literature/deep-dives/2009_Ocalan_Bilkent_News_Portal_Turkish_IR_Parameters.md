# Öcalan (2009): Bilkent News Portal: A System with New Event Detection and Tracking Capabilities (M.S. thesis, Bilkent University)

**Targeted deep-dive status:** COMPLETED (AI-assisted, pending researcher review)
**Completed:** 2026-09-28
**Verification:** independent AI verifier pass 2026-09-28; 14 findings addressed.
**Literature ID:** `MORPH-022` (assigned 2026-09-28, approved by researcher)
**Systematic-review record:** `CR002158` (metadata: PQDT – Global, THES, 89 pages). Full-text triage: INCLUDE, reading priority HIGH, reading tier 1, `carries_complementarity_evidence = YES` (triage basis: "breakdown by query-length and document-length characteristics"). This card proposes re-coding it to **NO** (§16).
**Provenance:** AI-assisted deep dive (Claude). What was read:
- the front matter, abstract, table of contents, Ch. 1, Sec. 3.2.2–3.2.5, Sec. 4.1 and 4.3, Ch. 5 (skimmed, BilCol2005/TDT), **Ch. 6 in full** (the retrieval experiments, printed pp. 43–56), Ch. 8 and the reference list, all from the text extraction.
- Pages checked visually (printed page = PDF page − 13): **p. 17** (Sec. 3.2.4), **p. 23** (Sec. 4.1), **pp. 47–56** (MF8 formula, Tables 6.1–6.5, Figures 6.1–6.5, Sec. 6.7).
- Figures 6.1, 6.2 and 6.5 have **no printed values**. We read them from 300-dpi crops by pixel measurement against the gridlines, precision about ±0.005 bpref. These readings are marked **[visual reading]**. For Fig. 6.1 they agree to about 0.001 (at most 0.0012) with values back-derived from the percentages printed in Sec. 6.4.
- Numbers computed by us are marked **[computed]**, all recomputed with Python.
- Statements about the 2008 journal article come only from the existing project card of `MORPH-001` and are marked **[MORPH-001 card]**. They were not re-verified against the 2008 PDF.

**Source rule:** **the thesis is the primary and only authoritative source** for what the author did and found. The web was used only for the bibliographic check.
**Reliability:** **A** by source type: an approved M.S. thesis with a signed committee page. Its evidential weight for IR claims is narrower than MORPH-001:
- Chapter 6 reuses the collection and, in part, the results of CAN2008a (MORPH-001), and is explicitly described as such (p. 17, p. 43).
- Relevance pooling and the query construction are not described in the thesis; the statistical test is named only for the stop-word experiment (two-tailed t-tests, p. 48).
- None of the three bpref result figures (6.1, 6.2, 6.5) carries printed values.
- The IR-relevant chapter is a secondary presentation. Cite MORPH-001 as the primary source for these Turkish findings.

---

## Кратко для исследователя (RU)

- **Что это.** Магистерская диссертация (M.S., Computer Engineering, Bilkent University, май 2009; руководитель Fazlı Can, соруководитель Seyit Koçberber). Основная часть посвящена архитектуре новостного портала и TDT-коллекции BilCol2005 (209 305 новостей 2005 г., 80 размеченных событий). **Экспериментальный IR есть только в главе 6** (pp. 43–56).
- **Глава 6 повторяет часть CAN2008a (MORPH-001).**
  - Та же коллекция: 408 305 документов, 72 запроса (газета в диссертации не названа; Milliyet — по MORPH-001 card **[MORPH-001 card]**).
  - Та же функция сопоставления MF8 (tf-idf-подобная векторная модель).
  - Те же значения bpref для NS/F5/LV на QM: 0.3255 / 0.4322 / 0.4504 (Table 6.1, p. 48). В MORPH-001 это ключевое сравнение.
  - Автор сам пишет, что результаты [CAN2008a] «partly presented in Chapter 6» (p. 17).
- **Варианты лексического представления:**
  - NS: без стемминга;
  - F5/F6: усечение до префикса длиной 5/6 символов; в результатах показан только F5;
  - LV: лемматизатор + successor variety для неразобранных слов.
  - SV отдельно не тестируется («not considered», p. 45).
  - **BM25 нет.** Плотного (dense) поиска нет. Гибрида/fusion нет.
- **Главные числа.**
  - Стемминг vs NS на QM: F5 +32.8%, LV +38.4% **[computed]**. LV − F5 = +0.018 bpref; по тексту различие незначимо на всех длинах запросов, документов и размерах коллекции.
  - Стоп-слова: NS 0.3255 → 0.3287 без списка, F5 0.4322 → 0.4330, LV 0.4504 → 0.4524; незначимо (Table 6.1).
- **Разбивка по длине запроса** (Sec. 6.4, Fig. 6.1).
  - QS→QM: F5 +14.4%, LV +13.5% (p < 0.01); NS +6.23%.
  - QM→QL: NS +14.59% (p < 0.01); F5/LV незначимо.
  - По Fig. 6.1 **[visual reading]**: short 0.306 / 0.377 / 0.398, long 0.373 / 0.447 / 0.461.
  - Длинные запросы частично компенсируют отсутствие стемминга. Но и на длинных запросах F5/LV > NS (p < 0.001).
- **Разбивка по длине документа** (Sec. 6.5, Table 6.4, Fig. 6.2). Три подколлекции: короткие ≤100 слов, 101–300, >300.
  - bpref растёт с длиной документа (p < 0.001).
  - По Fig. 6.2 **[visual reading]**: для коротких документов NS 0.211 vs F5 0.295 (относительно +40%); для длинных 0.482 vs 0.593 (+23%).
  - Абсолютный выигрыш, наоборот, больше у длинных (+0.111 vs +0.084). Сами авторы этого контраста не обсуждают.
- **Нет анализа взаимодополняемости:** нет перекрытия выдач NS/F5/LV, уникально найденных релевантных документов, oracle union, анализа по отдельным запросам. Есть только средние по группам. Поэтому предлагаем исправить `carries_complementarity_evidence` с YES на NO: это модерация эффекта морфологии условиями, а не complementarity.
- **Внутренние несоответствия.**
  1. Стоп-слова в портале: p. 17 — «It uses a stopword list», p. 56 — «we did not perform stopword list elimination».
  2. Table 6.5: среднее число релевантных на запрос для 50–200 тыс. документов меньше, чем «unique relevant docs / active queries», то есть среднее, по-видимому, считалось по всем 72 запросам (с этим согласуются все строки) **[computed]**.
  3. Описание правила выбора леммы (p. 47: длина, ближайшая к средней длине основы) по MORPH-001 card похоже на LM6, тогда как LV там основан на LM5.
  4. В портале применяется «tf-idf model of Lemur» (p. 23), а не проверенная MF8.
- **Для нашего gap:** ядро v0.8 не затрагивает (raw/stem/lemma × фиксированный D → overlap/unique hits → прирост гибрида). Только подкрепляет занятые тезисы: морфология помогает лексическому поиску в тюркском языке; эффект зависит от длины запроса.
- **Практическая польза:**
  1. Длину запроса варьировать **внутри одной темы** (title / title+description), а не сравнивать разные запросы.
  2. Стратифицировать результаты по длине документа и давать и абсолютный, и относительный прирост.
  3. Пилоты на подколлекциях могут завышать эффект стемминга (на 50 тыс. документов F5/NS ≈ +52% vs ≈ +33% на полной коллекции **[visual reading]**).
  4. ETracker — полезный шаблон search-guided разметки. Но пул из одного лексического F5-поисковика смещён в пользу лексики; наш пул должен включать dense.

---

## 1. Bibliographic record

- **Author:** Hüseyin Çağdaş Öcalan
- **Title:** *Bilkent News Portal: A System with New Event Detection and Tracking Capabilities* (Turkish title: *Bilkent Haber Portalı: Yeni Olay Belirleme ve İzleme Yetenekleri Olan Bir Sistem*)
- **Degree:** Master of Science in Computer Engineering
- **University:** Bilkent University, Department of Computer Engineering and Institute of Engineering and Science, Ankara
- **Date:** May 2009 (title page and abstract)
- **Advisor:** Prof. Dr. Fazlı Can. **Co-advisor:** Asst. Prof. Dr. Seyit Koçberber. The abstract misspells him as "Koçerber".
- **Committee** (signature pages ii–iii): Prof. Dr. Fabio Crestani (University of Lugano), Asst. Prof. Dr. H. Murat Karamüftüoğlu, Prof. Dr. Özgür Ulusoy. Institute director: Prof. Dr. Mehmet Baray.
- **Funding:** TÜBİTAK grant 106E014 (Acknowledgements, p. vi)
- **Length:** xiii + 75 printed pages (89 PDF pages). The last PDF page is a ProQuest notice: "ProQuest Number: 29047315".
- **Language:** English, with a Turkish abstract (Özet)
- **Database record (systematic review):** PQDT – Global, document type THES. The PDF's last page carries ProQuest Number 29047315.
- **DOI:** none found (NOT_REPORTED in the thesis)
- **Bibliographic check (web search, 2026-09-28):**
  - Search results list a YÖK Açık Bilim record with this title (handle `20.500.12812/35760`, https://acikbilim.yok.gov.tr/handle/20.500.12812/35760) and a Semantic Scholar record.
  - Neither page could be opened (robots/proxy refusal), so thesis number, pages and cataloguing details were **not verified** from an official record.
  - The Semantic Scholar URL slug lists committee member Karamüftüoğlu next to Öcalan, which suggests noisy author metadata there.
- **Related publications named in the thesis:**
  - [CAN2008a] Can, Kocberber, Balcik, Kaynak, **Ocalan**, Vursavas, *Information retrieval on Turkish texts*, JASIST, cited as "59(2), 407-421, 2008" (References, p. 66). The thesis's issue number is wrong: F. Can's publication list gives Vol. 59, No. 3 (February 2008), pp. 407–421, and the Bilkent repository record gives DOI 10.1002/asi.20750 (bibliographic check, 2026-09-28), in agreement with the MORPH-001 card.
  - [CAN2008b] SIGIR'08 demo paper on the portal.
  - [CAN2009b] *Topic detection and tracking in Turkish*, JASIST, "under revision".
- **Source type:** master's thesis
- **Reliability:** A by source type (approved thesis). Narrow weight for IR claims, which are derivative of MORPH-001.
- **Full text available:** yes (`07_full_text/pdfs/CR002158.pdf`)

## 2. Why this work matters to the PhD

Most of the thesis (Chs. 2–5, 7) concerns news-portal system design and the TDT collection BilCol2005. Only **Chapter 6, "Experimental Foundations II: Information Retrieval Parameters"**, contains ranked-retrieval experiments. It opens (p. 43):

> "In this chapter, we investigate information retrieval (IR) on Turkish texts using a large-scale IR test collection that contains 408,305 documents and 72 ad hoc queries [CAN2008a]."

In Sec. 3.2.4 (p. 17) the author says the portal's IR component "is based on the experimental results of our research [CAN2008a], also partly presented in Chapter 6".

| Axis | Relation |
|---|---|
| Lexical retrieval | Direct, but only one tf-idf vector-space function (MF8). **No BM25** |
| Morphological variants of the lexical representation | **Yes:** NS (raw), F5 (and F6, mentioned only) fixed-prefix truncation, LV (lemmatizer + successor-variety fallback) |
| Semantic / dense retrieval | **Absent** |
| Hybrid retrieval / fusion | **Absent as an evaluated condition.** Reciprocal-rank fusion is used only inside the annotation tool ETracker (Sec. 5.2) to merge several lexical queries |
| Overlap / unique hits / oracle union | **Absent** |
| Query / document characteristics | **Yes, at group level:** three query-length forms (QS/QM/QL), three document-length sub-collections, eight collection sizes. No per-query analysis |
| Uzbek / Turkic morphology | Turkish (agglutinative, Turkic); the closest typological relative of Uzbek among the project's lexical-morphology sources |
| Current gap | Supports already-occupied claims; no material effect on the v0.8 core (§16) |

It matters as (a) a second, thesis-level presentation of the MORPH-001 findings with explicit query-length and document-length breakdowns and figures, and (b) a source of methodological cautions (test-collection construction, deployment vs experiment mismatch).

## 3. Research problem

### Simple explanation

A Turkish news portal needs a search engine. Its builders must choose settings:
- whether to cut words down to a common form (and how);
- whether to drop very common words;
- how the chosen setting behaves for short vs long queries, short vs long articles, and a growing archive.

Chapter 6 measures these choices on a large Turkish newspaper test collection so that the portal can use the best-supported settings.

### Formal formulation

For ad hoc retrieval on a Turkish news collection with a fixed matching function (MF8), estimate the effect on bpref of:
- (i) the indexing-term representation: NS vs F5 vs LV;
- (ii) stop-word removal;
- (iii) query length: QS/QM/QL forms of the same 72 topics;
- (iv) document length: three disjoint sub-collections;
- (v) collection size: eight nested temporal prefixes, 50K → 408,305 documents.

Statistical comparisons are across conditions (Sec. 6.3–6.6).

## 4. Main idea

### Simple explanation

Build several indexes of the same newspaper archive, each with a different way of turning words into index terms. Run the same queries. Compare how well each index ranks the documents that human judges marked relevant. Then repeat the comparison on subsets: shorter or longer queries, shorter or longer articles, smaller or larger archives.

### Concrete example

An illustrative example of the representation variants, of our own making (not from the thesis). Take a Turkish inflected form `kitaplarımızdan` ("from our books"):
- **NS** indexes `kitaplarımızdan` as is.
- **F5** keeps the first five characters: `kitap`.
- **LV** asks a lemmatizer for the dictionary form (`kitap`). If the word cannot be analysed (misspelled or foreign), it falls back to successor variety.

A query containing `kitap` matches the document only under F5/LV. The thesis also notes that Turkish has little prefixation (p. 44). It explains the success of fixed prefixes by the claim that "Turkish word roots are not much affected with suffixes [EKM2000]" (p. 46).

### Formal method

MF8 matching function (Sec. 6.2, p. 47; formula checked on the page image):

`score(Q, d_j) = Σ_{t∈Q} [ (1 + ln f_dt) / √D ] · [ f_qt · ln(1 + N / f_t) ]`

where:
- `f_dt` = frequency of t in d_j;
- `D` = total number of term occurrences in d_j;
- `f_qt` = frequency of t in Q;
- `N` = number of documents;
- `f_t` = "frequency of term t in the entire document collection".

The author notes that idf enters through the query weight, which suits dynamic collections.

Context (not from the thesis): this is a log-tf × idf vector-space weighting with √length normalization. It has no BM25-style term-frequency saturation parameter (k1) or tunable length normalization (b).

## 5. Architecture / algorithm

1. **Collection and queries.** Taken from CAN2008a: 408,305 documents, 72 ad hoc queries in three forms QS/QM/QL (Tables 6.2–6.3).
   - The thesis does **not** describe what the three forms contain; it refers to [CAN2008a] (p. 49).
   - Per the MORPH-001 card: QS = topic, QM = topic + description, QL = topic + description + narrative **[MORPH-001 card]**.
2. **Term representations** (Sec. 6.1, pp. 45–47):
   - **NS:** no stemming, the "austrich algorithm". It is the baseline.
   - **Fn (fixed prefix):** "we simply truncate the words and use the first n (Fn) characters of each word as its stem; words with less than or equal to n characters are used with no truncation" (p. 45). F5 and F6 are named as the best-performing prefix lengths from [CAN2008a]. **Only F5 appears in the reported results.**
   - **LV:** a lemmatizer with successor-variety (SV) fallback: "For various items, including misspelled and foreign words, which cannot be analyzed by the lemmatizer, we use the SV method for such words; this crossbreed is referred to as LV" (p. 46).
     - The lemmatizer is not named. Oflazer's two-level Turkish morphology [OFL1994] is cited when lemmatizers are defined.
     - Candidate choice (p. 47): "(1) Select the candidate whose length is closest to the average stem length for distinct words for Turkish; (2) If there is more than one candidate, then select the stem whose word type (POS) is the most frequent among the candidates" [ALT2007].
     - The share of words handled by the SV fallback is NOT_REPORTED in the thesis.
   - **SV alone:** "not considered in this study", because [CAN2008a] found it similar to the prefix and lemmatizer methods (p. 45).
   - Terminology note: the thesis prefers "stemming" as the umbrella word for all these variants (p. 47).
3. **Stop-words:** a semi-manually built list of 147 words (App. B.1). Tested before and after stemming. Automatic lists (288 and 10 most frequent words) are cited from [CAN2008a] (p. 48).
4. **Matching:** MF8 for all Chapter 6 experiments.
5. **Sub-collections:**
   - document length: short ≤ 100 words, medium 101–300, long > 300 (pp. 50–51);
   - collection size: eight nested prefixes in temporal order, in 50,000-document steps (p. 52).
   - Only "active" queries, i.e. those with at least one relevant document in the sub-collection, are evaluated (p. 52).
6. **Deployment** (not evaluated):
   - The portal indexes with Lemur/Indri, extended with F5 (Sec. 3.2.2, 3.2.4, 4.1, 6.7).
   - It uses the "tf-idf model of Lemur Toolkit as the matching function of IR component" (p. 23), not MF8 explicitly.
   - ETracker (the annotation tool) uses "a tf-idf-based matching function and the first five prefix stemmer" (p. 36).

## 6. Data

### IR test collection (Chapter 6; built in CAN2008a)

- **Dataset / corpus:** the "large-scale IR test collection" of [CAN2008a]. The thesis does not name the newspaper. Per the MORPH-001 card it is Milliyet 2001–2005 **[MORPH-001 card]**.
- **Language / domain:** Turkish; news.
- **Size:** 408,305 documents (p. 43; Table 6.5, p. 53).
- **Queries:** 72 ad hoc queries in three forms (Table 6.2, p. 49):

| Form | Min | Max | Median | Avg unique words/query (with stop-words) |
|---|---:|---:|---:|---:|
| QS | 1 | 7 | 3 | 2.89 |
| QM | 5 | 24 | 11 | 12 |
| QL | 6 | 59 | 26 | 26.11 |

- **Query word statistics** (Table 6.3, p. 49): 208 / 1004 / 2498 words; 182 / 657 / 1359 unique words; average word length 7.03 / 7.57 / 7.62 characters.
  - QM queries contain on average 1.74 stop-words (p. 48).
  - Average Turkish news token length is 6.90 characters, citing [CAN2008a] (p. 45).
- **Relevance judgments:**
  - 6,923 unique relevant documents; mean 104.30 and median 93.0 relevant documents per query (Table 6.5, p. 53).
  - Assessors are called "query owners" (p. 48).
  - Pooling procedure, pool depth, judgment scale and number of assessors: **NOT_REPORTED in the thesis**. Per the MORPH-001 card: binary judgments by 33 native speakers on a top-100 pool from 24 runs (8 matching functions × NS/F6/SV) **[MORPH-001 card]**.
- **Train / dev / test:** none. All configurations are evaluated on the same 72 queries.
- **Document-length sub-collections** (Table 6.4, p. 51):

| Sub-collection | Docs (as printed) | Active queries | Unique relevant docs | Avg rel./query | Median rel./query |
|---|---|---:|---:|---:|---:|
| Short (≤100 words) | "139.13" | 72 | 1864 | 27.50 | 18.5 |
| Medium (101–300) | "193.144" | 72 | 3447 | 52.14 | 45.0 |
| Long (>300) | "76.031" | 72 | 1612 | 24.67 | 21.0 |

- The printed counts use "." as a thousands separator with a dropped digit in "139.13". Reading them as 139,130 / 193,144 / 76,031 sums exactly to 408,305 **[computed]**. That is 34.1% / 47.3% / 18.6% of the collection **[computed]**.
- The relevant counts sum to 6,923 and the averages to 104.31, both consistent with Table 6.5 **[computed]**.
- Avg × 72 = 7,510 > 6,923 unique **[computed]**, so about 587 relevance assignments go to documents relevant to more than one query.
- **Collection-size increments:** see Table 6.5 in §9.

### BilCol2005 (Chapter 5; TDT, not ad hoc IR)

- 209,305 stories from five Turkish news sites (CNN Türk, Haber 7, Milliyet, TRT, Zaman) for 2005 (Table 5.2, p. 33).
- 80 annotated events after 21 profiles were deleted in quality control; 39 native-speaker annotators.
- Mean 73 tracking stories per event (median 32, range 5–454) (pp. 39–40, Table 5.4).
- Annotation is **search-guided** with ETracker, in four steps (Table 5.3, p. 38): seed-story query, profile query, on-topic-story queries merged by "reciprocal rank data fusion" [NUR2006], and free queries. Each step has a cap on documents ranked (200/300/400/200) and a recommended time limit.
- Quality control: a senior annotator checks up to 60 documents per event.
- No retrieval-effectiveness experiments are run on BilCol2005 in this thesis. Event detection and tracking are covered in companion theses [BAG2009, KAR2009].

## 7. Baselines

| Baseline / condition | What it is | Why selected | Fair comparison? |
|---|---|---|---|
| NS | Surface-form indexing | Reference for stemming effects | Yes, same queries and collection. Per the MORPH-001 card, NS was a pool-contributing system, whereas F5 and LV were not **[MORPH-001 card]**; that pool bias would, if anything, favour NS |
| F5 | 5-character prefix truncation | Best simple method in [CAN2008a] | Prefix length was chosen on the same test collection ([CAN2008a]); there is no dev split |
| LV | Lemmatizer + SV fallback | Linguistically informed method | Same collection. Lemmatizer identity and fallback share are not reported in the thesis |
| With / without stop-word list | 147-word list vs none | Portal design decision | Yes. Only QM and MF8 are tested in the thesis |
| MF8 only | tf-idf VSM | Best function in [CAN2008a] | A single lexical scorer; conclusions are conditional on it. **No BM25**, no language model, no dense model |

## 8. Metrics

| Metric | Definition | Simple meaning | Appropriate? |
|---|---|---|---|
| bpref [BUC2004] | Context (not from the thesis, which cites [BUC2004] without a definition). Per query: average over judged relevant documents r of 1 − (number of judged non-relevant documents ranked above r) / R, with the normalization of Buckley & Voorhees. Unjudged documents are ignored | "Are the documents judged relevant ranked ahead of those judged non-relevant?" | Suited to incomplete (pooled) judgments. It is the only effectiveness metric reported in the thesis. MAP, P@k and nDCG are **not reported** here |
| Vocabulary size | Number of distinct index terms (Fig. 6.3) | Index dictionary size | Efficiency descriptor |
| Posting tuples | Number of <document, weight> pairs (Fig. 6.4) | Inverted-file size | Efficiency descriptor |

Context (not from the thesis): bpref depends on the number of judged relevant (R) and non-relevant documents per query. Its values are therefore not strictly comparable across sub-collections with different R, which matters for Sec. 6.5–6.6 (§12).

## 9. Results

### Table 6.1: stop-word list, QM, MF8 (p. 48; checked on image)

| | NS | F5 | LV |
|---|---:|---:|---:|
| With stop-word list | 0.3255 | 0.4322 | 0.4504 |
| Without stop-word list (primed) | 0.3287 | 0.4330 | 0.4524 |

- Two-tailed t-tests: "no significant impact" (p. 48). The no-list runs are marginally higher: +0.0032 / +0.0008 / +0.0020 **[computed]**.
- A stop-word list applied after F5 stemming also shows "no statistically significant performance change" (p. 48).
- **Stemming effect on QM with the stop-word list** (these values match the main MF8 comparison of MORPH-001 **[MORPH-001 card]**) **[computed]**:
  - F5 vs NS: +0.1067 (+32.78%);
  - LV vs NS: +0.1249 (+38.37%);
  - LV vs F5: +0.0182 (+4.21%).

### Sec. 6.4 / Figure 6.1: query length (pp. 49–50; bars have no printed values)

| Query form | NS | F5 | LV | Source |
|---|---:|---:|---:|---|
| QS (short) | 0.306 | 0.377 | 0.398 | [visual reading]; back-derived from text %: 0.3064 / 0.3778 / 0.3968 [computed] |
| QM (medium) | 0.3255 | 0.4322 | 0.4504 | Table 6.1 (bars agree) |
| QL (long) | 0.373 | 0.447 | 0.461 | [visual reading]; NS back-derived 0.3730 [computed] |

Text claims (p. 49), checked against the figure:
- **QS→QM:** F5 +14.4%, LV +13.5%, "statistically significant (p < 0.01)". NS +6.23%; significance not stated for this NS step.
- **QM→QL:** F5 and LV increase "statistically insignificant". Visual estimates **[computed from visual reading]**: F5 about +3.4%, LV about +2.4%. NS +14.59%, "statistically significant (p < 0.01)".
- "For all query cases, under the same query form the performance difference of F5 and LV is statistically insignificant. However, the performance difference of these stemmers with respect to NS is statistically significant (p < 0.001)" (p. 49).
- The authors' reading (pp. 49–50): "NS gets more benefit from query length increase. Also, the negative impact of not being stemmed is partly recovered with the increase in query length."
  - This holds for the **QM→QL** step and for **QS→QL overall**: NS +21.7% [computed: 1.0623 × 1.1459] vs F5 about +18.6% and LV about +15.8% [visual reading].
  - It does **not** hold for **QS→QM**, where NS gains less (+6.23%) than F5/LV (+14.4% / +13.5%).
- **Stemming benefit by query form [computed from visual reading]:**

| Query form | F5 − NS | LV − NS | F5 / NS − 1 | LV / NS − 1 |
|---|---:|---:|---:|---:|
| QS | +0.071 | +0.092 | +23% | +30% |
| QM | +0.107 | +0.125 | +33% | +38% |
| QL | +0.074 | +0.088 | +20% | +24% |

The benefit of normalization is **non-monotonic in query length**: largest for medium queries; in relative terms it is smallest for long queries, but in absolute terms F5's benefit is smallest for short queries (+0.071 vs +0.074). The authors do not state this pattern, and it is not tested statistically.

### Sec. 6.5 / Figure 6.2 and Table 6.4: document length (pp. 50–52; bars have no printed values)

| Sub-collection | NS | F5 | LV | F5 / NS − 1 | F5 − NS |
|---|---:|---:|---:|---:|---:|
| Short docs (≤100 words) | 0.211 | 0.295 | 0.297 | +40% | +0.084 |
| Medium (101–300) | 0.345 | 0.432 | 0.450 | +25% | +0.087 |
| Long (>300) | 0.482 | 0.593 | 0.608 | +23% | +0.111 |

(all values [visual reading]; last two columns [computed])

- Text (p. 51): "as the document sizes increase the effectiveness in terms of bpref values significantly increases (p < 0.001) and this is true for all stemming options."
- Text (p. 52): F5 vs LV "statistically insignificant" in all document-length cases; both vs NS significant (p < 0.001).
- The authors attribute the length effect to "better evidence about their contents" and note that most articles cover one topic (an "anecdotal observation", p. 51).
- **Relative** stemming gain is largest for short documents (+40% vs +23%), but the **absolute** gain is largest for long documents (+0.111 vs +0.084) **[computed from visual reading]**. The authors do not discuss this contrast.
- Observation: the medium sub-collection's F5 / LV bars (0.432 / 0.450) are visually indistinguishable from the full-collection QM values (0.4322 / 0.4504). The NS bar (0.345) differs from 0.3255. Whether this is a coincidence cannot be decided from the thesis (§19).

### Sec. 6.6: collection size (Table 6.5 p. 53, Figures 6.3–6.5 pp. 54–55)

| Docs | Active queries | Unique rel. docs | Avg rel./query | Median | NS | F5 | LV |
|---|---:|---:|---:|---:|---:|---:|---:|
| 50,000 | 57 | 719 | 10.72 | 11.0 | 0.291 | 0.442 | 0.443 |
| 100,000 | 62 | 1380 | 21.08 | 21.5 | 0.278 | 0.373 | 0.397 |
| 150,000 | 63 | 2014 | 30.55 | 34.0 | 0.284 | 0.381 | 0.384 |
| 200,000 | 64 | 2944 | 44.33 | 45.5 | 0.307 | 0.415 | 0.422 |
| 250,000 | 68 | 3764 | 56.51 | 56.5 | 0.324 | 0.437 | 0.443 |
| 300,000 | 70 | 4794 | 71.45 | 66.0 | 0.337 | 0.445 | 0.445 |
| 350,000 | 71 | 5725 | 86.29 | 79.0 | 0.329 | 0.439 | 0.442 |
| 408,305 | 72 | 6923 | 104.30 | 93.0 | 0.325 | 0.432 | 0.450 |

(first five columns from Table 6.5; bpref columns [visual reading] of Fig. 6.5)

- Text (p. 55): "LV provides slightly better, but statistically insignificant performance improvement with respect to F5. However, the performance of F5 and LV with respect to NS is statistically significantly different (in all cases p < 0.001)."
- bpref drops from 50K to 100K and is steady from about 250K onward (p. 54).
- **Stemming gain varies with collection size [computed from visual reading]:** F5/NS is about +52% at 50K and about +32–35% from 100K upward.
- **Vocabulary (Fig. 6.3) [visual reading]:** at 408K about 1,440K terms for NS, 435K for LV and 280K for F5, so F5 is about 5× smaller than NS [computed]. "F5 and LV show saturation in the increase of unique words ... more noticeable with F5" (p. 53).
- **Posting tuples (Fig. 6.4) [visual reading]:** about 61M (NS), 50M (F5), 47M (LV) at full size, growing linearly.
- **Arithmetic issue in Table 6.5 [computed]:**
  - For 50K–200K, "Avg. rel./query × active queries" is **smaller** than "Total unique relevant docs" (e.g., 10.72 × 57 = 611 < 719).
  - That is impossible if the average is over active queries.
  - Dividing by all 72 queries (10.72 × 72 = 772 ≥ 719) is consistent in every row.
  - The average column therefore appears to include queries with zero relevant documents, although the text says only active queries are evaluated.

## 10. Statistical evidence

- **Significance tests:**
  - Two-tailed t-tests are named only for the stop-word experiment (p. 48).
  - All other claims give only p thresholds (p < 0.01, p < 0.001) without naming the test or the pairing unit. Presumably the unit is queries, but this is **NOT_REPORTED**.
  - No test statistics or exact p-values are given.
- **Confidence intervals:** NOT_REPORTED.
- **Runs / seeds:** not applicable; the retrieval runs are deterministic.
- **Ablation:** the chapter is a set of controlled one-factor variations (representation × stop-words × query form × document length × collection size), always with MF8. Interactions are not modelled, and **no second matching function** is used in the thesis.
- **Per-query analysis:** **NOT_REPORTED.** Only means over query groups or sub-collections are shown. There is:
  - no per-query win/loss between NS, F5 and LV;
  - no overlap of retrieved or relevant sets between representations;
  - no count of relevant documents found only by one representation;
  - no oracle union;
  - no query-feature regression.
- **Significance of the length effect:** "significantly increases (p < 0.001)" for document length is stated across sub-collections that differ in size and number of relevant documents (§12).

## 11. Strengths

- Several morphological variants of the lexical representation (raw, prefix, lemmatizer + SV) on a large Turkish collection with human judgments. The core results are from the peer-reviewed MORPH-001 study.
- The query-length manipulation is **within-topic**: the same 72 information needs in three lengths, so the effect of length is not confounded with topic. The thesis calls QS/QM/QL "query forms" of the 72 queries and defers their composition to [CAN2008a] (p. 49); the topic/description/narrative construction is **[MORPH-001 card]**.
- Explicit document-length and collection-size stratification with descriptive tables of relevant documents per stratum (Tables 6.4–6.5).
- bpref is chosen for incomplete judgments.
- Efficiency side-effects (vocabulary, postings) are reported alongside effectiveness.
- It documents how the experimental results were turned into a production configuration (Sec. 6.7), including a search-guided TDT annotation protocol with quality control (Ch. 5).

## 12. Limitations

### Stated by the author

- Scope restrictions stated by the author (not framed as limitations): only a partial view of [CAN2008a]: SV is excluded "since" it performed similarly (p. 45); details on the queries are deferred to [CAN2008a] (p. 49).
- No objective analysis of topics per article; the single-topic assumption is "anecdotal" (p. 51).
- Longer documents "could hurt the retrieval performance" beyond some length (p. 51); this is speculative, and no such range is observed.

### Inferred from the experimental design

1. **Derivative evidence.** The central numbers reproduce the CAN2008a MF8 comparison. The thesis is not an independent replication.
2. **Single lexical scorer, no BM25.** All effects are conditional on MF8 (log-tf, √length, idf-in-query). Whether they hold for BM25 is not tested here; MORPH-002 addresses BM25 on the same collection.
3. **No dense, no hybrid, no complementarity.** Nothing about how the representation changes which relevant documents are found, only means.
4. **Group-level moderation only.** Query length is manipulated by form, document length by sub-collection. There is no continuous per-query feature analysis and no morphology-specific query features (affix load, OOV, inflection mismatch).
5. **Sub-collection confounds.** The document-length strata differ in size (76K–193K documents) and in relevant documents per query (24.7–52.1). The scalability results show that collection size, together with the changing active-query and relevant sets, moves bpref (e.g., the 50K → 100K drop, where active queries go 57 → 62 and unique relevant documents 719 → 1380). bpref also depends on R. Part of the "longer documents → higher bpref" effect may reflect these differences and MF8's √D normalization, not document length as such.
6. **Pooling bias** (per the MORPH-001 card, not described in the thesis). F5 and LV were not pool-contributing systems, so their scores are probably conservative relative to NS.
7. **Selection on the test set.** Prefix length (F5/F6) and the lemmatizer configuration were chosen on the same collection, and there is no dev split.
8. **Test unspecified.** Pairing unit and test type are not given for most claims; there are no effect sizes or CIs.
9. **Experiment ≠ deployment.**
   - The portal is described as using Lemur's tf-idf model (p. 23), not MF8.
   - The two stop-word statements contradict each other (p. 17 vs p. 56).
   - The tested configuration and the deployed one are therefore not demonstrably the same.
10. **Figures without values.** Figs. 6.1, 6.2 and 6.5 carry the query-length, document-length and scalability results but no numeric labels. Our readings carry about ±0.005 uncertainty.

## 13. What the work proves

Within its setting (Turkish news, MF8, 72 queries, bpref), and largely by re-presenting CAN2008a:
- **Morphological normalization strongly improves Turkish lexical retrieval over raw word forms.** On QM: NS 0.3255 vs F5 0.4322 vs LV 0.4504 (Table 6.1). Significant vs NS (p < 0.001) in every query-length, document-length and collection-size condition reported (pp. 49, 52, 55).
- **A 5-character prefix is statistically indistinguishable from lemmatizer + SV** in every reported condition (pp. 49, 52, 55). LV is numerically higher by about 0.00–0.02 bpref.
- **Query length appears to moderate the raw-vs-normalized gap (descriptively).** Longer queries (within-topic per the MORPH-001 card) raise NS significantly from QM to QL (+14.59%, p < 0.01) while F5/LV gains are not significant; the negative effect of no stemming is partly, not fully, compensated. No representation × query-length interaction test is reported, and the gap sizes come from visual readings of Fig. 6.1.
- **A stop-word list has no significant effect** on bpref with MF8 (Table 6.1).
- **Longer news documents are retrieved with higher bpref** in this collection and scorer, for all three representations (Fig. 6.2, p < 0.001 as stated). The confounds are noted in §12.
- **F5 cuts the index vocabulary about 5-fold** and postings moderately (Figs. 6.3–6.4).

## 14. What the work does NOT prove

- **Anything about BM25, language-model retrieval or dense retrieval.** Only MF8 is used.
- **That lexical and semantic retrieval are complementary, or how morphology changes that complementarity.** There are no semantic channel, no fusion, no overlap, no unique-hit and no oracle-union measurements.
- **That NS and F5/LV retrieve different relevant documents.** Only mean bpref differences are shown; the degree of overlap between representations is unknown.
- **Which individual queries benefit from normalization, or why.** There is no per-query analysis. Query length is the only query characteristic, and it is manipulated at form level.
- **That document length *causes* higher effectiveness.** The strata differ in size and relevance density, and the scorer's length normalization is fixed.
- **That F5 is optimal for Uzbek, or that lemmatization is unnecessary.** Turkish results with a selected-on-test prefix length do not transfer numerically.
- **That the deployed portal matches the tested configuration.** See the stop-word and matching-function discrepancies.
- **That stop-words are irrelevant for BM25 or for Uzbek.**

## 15. Relationship to current Uzbek evidence

- **No Uzbek data.** The transfer is methodological, not numerical, as for MORPH-001.
- Turkish and Uzbek share agglutinative, suffix-only inflection. The thesis's observation that prefixation is rare (p. 44) and that roots are "not much affected with suffixes" (p. 46) underlies the success of F5. Whether this holds for Uzbek, including vowel and consonant alternations at morpheme boundaries and the apostrophe letters o‘/g‘, is untested. The latter point is our inference.
- Uzbek national sources in the index (MORPH-UZ-002/003/004/007: Bakaev, Xusainova, Elov) supply stemmers and lemmatizers with analyzer-accuracy evaluations, but no qrels-based raw/stem/lemma IR benchmark. This thesis (via MORPH-001) is the Turkic precedent for such a benchmark, and adds the within-topic query-length and document-length breakdowns.
- Relation to other project cards:
  - **MORPH-001** (CAN2008a): primary source; this thesis is a partial re-presentation.
  - **CR000651** (Can et al., SIGIR 2006 poster): earlier version of the same experiments.
  - **MORPH-002** (Haddad & Bechikh Ali, 2014): same collection with BM25.
  - **CR002160 / CR000535** (per triage note): the TDT line on BilCol2005, not ad hoc IR.

## 16. Relationship to CURRENT_GAP

**Classification:** *supports* (already-occupied claims) + *no material effect* on the v0.8 refined core.

- **Supports** existing non-claims in v0.8:
  - "морфология ранее не применялась к ... search" / "raw/stem/lemma ранее не сравнивались": raw vs prefix vs lemmatizer-based representations were compared in a Turkic language, via CAN2008a.
  - "query-type analysis ... новая идея": query length moderating the morphology effect is established here and in MORPH-001.
- **Touches, but does not occupy,** the v0.8 element "как эти изменения связаны с ... характеристиками запросов". It links **one** query characteristic (length, by form) to the **lexical-only effectiveness gap** between representations. It does **not** link it to changes in lexical–semantic complementarity.
- **Does not touch:**
  - a fixed dense retriever D;
  - H_raw / H_stem / H_lemma fusion;
  - unique relevant hits of either channel;
  - overlap;
  - oracle union;
  - incremental hybrid gain;
  - per-query decomposition;
  - Uzbek.
- **Triage coding.** Propose changing `carries_complementarity_evidence` from YES to **NO (condition-level moderation of lexical representation effects only)**. The "breakdown by query length and document length" is a mean-bpref stratification, not complementarity evidence in the project's sense.

**Proposal:** keep v0.8 refined unchanged. No addition to the evidence-boundary list is needed beyond MORPH-001, which already covers this evidence. This is a proposal only; `CURRENT_GAP.md` has not been edited.

## 17. Implications for our research design

- **Query taxonomy / length as a controlled factor.** Where the Uzbek topics have a title and a description, evaluate both forms **for the same topic** (as QS/QM/QL here). This separates the length effect from topic difficulty. It should be done per channel (BM25_raw/stem/lemma, D, hybrids) to test whether the morphology-induced complementarity shift depends on query length. Our reading of Fig. 6.1 suggests the raw-vs-normalized gap is non-monotonic in length (largest for medium queries, §9; **[visual reading]**, not stated or tested in the thesis), so length should be modelled as categorical or non-linear, not assumed linear.
- **Document-length stratification.** Report effects by document-length stratum with **both absolute and relative** deltas. The thesis's figure shows the relative stemming gain is largest for short documents, while the absolute gain is largest for long ones. Strata should be defined on the same collection with per-query pairing; control for stratum size and relevant counts, or use per-query mixed models.
- **Collection size / pilots.** The stemming gain was about +52% at 50K documents vs about +33% at full size [visual reading]. Pilot results on small Uzbek sub-collections may not predict full-collection effects. Report collection size with every pilot number.
- **Morphology preprocessing.**
  - Include a fixed-prefix variant (`BM25_prefix-n`) as the "simple normalization" control already foreseen in v0.8.
  - Choose n on dev queries only.
  - Define the prefix in letters **after** apostrophe/Unicode normalization, so that o‘/g‘ variants do not change the effective prefix length (our inference).
  - For a lemma variant, report the analyzer's coverage and the fallback share. The thesis gives neither, even though its LV depends on a fallback.
- **Stop-words.** Fix the stop-word policy identically across raw/stem/lemma and report it. The null effect here is MF8-specific and should not be assumed for BM25.
- **Pooling / qrels.** ETracker's search-guided, multi-query, fusion-merged annotation with capped depth and senior quality control is a practical template for Uzbek qrels. But its candidate lists come from **one lexical system (F5 + tf-idf)**. For our complementarity measurements the pool must include BM25_raw, BM25_stem, BM25_lemma, D and the hybrid runs. Otherwise dense-only relevant documents are systematically unjudged, and "unique dense hits" is biased downwards.
- **Metrics.** Where judgments are incomplete, report bpref (or condensed-list metrics) alongside nDCG/Recall. Unique-hit counts must be computed on judged documents only, and the judged fraction per channel reported.
- **Protocol hygiene.**
  - Record the exact deployed/evaluated configuration: scorer, stop-words, normalization.
  - Name the significance test and pairing unit.
  - Report effect sizes/CIs.
  - Provide per-query outputs.

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| NS (no stemming) | Index words exactly as written | Surface-form index terms (after tokenization and lowercasing) |
| Fixed-prefix stemming (Fn, F5) | Keep only the first n letters of each word | Pseudo-stemming by truncation to n characters; shorter words unchanged |
| Lemmatizer | A tool that finds the dictionary form of a word | Morphological analysis returning lemma candidates with POS and suffixes |
| Successor variety (SV) | Guess where the stem ends by counting how many different letters follow each prefix in a corpus | Stem = prefix with maximal successor-letter variety (here: the longest such prefix) |
| LV | Lemmatizer, with SV as backup for words it cannot analyse | Hybrid lemmatizer/SV term normalization |
| MF8 | The tf-idf formula used to score documents | Σ_t (1 + ln f_dt)/√D · f_qt · ln(1 + N/f_t) |
| bpref | Checks whether judged relevant documents are ranked above judged non-relevant ones, ignoring unjudged ones | Buckley & Voorhees (2004) preference-based measure for incomplete judgments |
| QS / QM / QL | Short, medium and long versions of the same query | Query forms of the same topic, different length (per MORPH-001 card: T, T+D, T+D+N) |
| Active query | A query with at least one relevant document in the (sub-)collection | Evaluation-set filter for sub-collections |
| Pooling | Only documents returned by some systems are shown to judges | Construction of incomplete relevance judgments |
| Search-guided annotation | Annotators use a search engine to find stories to label instead of reading everything | Iterative, query-driven relevance/topic labeling (TDT practice) |
| Reciprocal-rank fusion (as in ETracker) | Merge several ranked lists by giving points for high ranks | Rank-level fusion of multiple query runs |
| Complementarity (project term) | Each channel finds some relevant documents the other misses | Unique relevant hits, overlap, oracle-union gain (**not measured in this work**) |

## 19. Open questions / verification needed

1. **Stop-words in the portal:** p. 17 says the IR component "uses a stopword list"; p. 56 says "we did not perform stopword list elimination in retrieval and filtering components". The thesis cannot resolve this.
2. **Matching function of the deployed system:** MF8 (Ch. 6) vs "tf-idf model of Lemur Toolkit" (p. 23). Is Lemur's tf-idf equivalent to MF8? NOT_REPORTED.
3. **Lemma-selection rule vs LV of CAN2008a.** The thesis describes choosing the candidate "closest to the average stem length" (p. 47). The MORPH-001 card describes LV as built on LM5 (target ≈ 5 characters), with the average-length rule (≈ 6.58) as LM6 **[MORPH-001 card]**. The LV values here equal the MORPH-001 LV values. Check against the 2008 PDF whether the thesis text describes LM6 while reporting LM5-based LV.
4. **Table 6.5 average column:** the arithmetic implies division by 72 rather than by the active queries (§9). Confirm the definition.
5. **Fig. 6.2, medium sub-collection:** F5/LV bars equal the full-collection QM values to reading precision, while NS does not. Coincidence or a plotting reuse? Undecidable from the thesis.
6. **Test type and pairing unit** for all p < 0.01 / p < 0.001 claims outside Sec. 6.3: NOT_REPORTED.
7. **Pooling, assessors, judgment scale and query forms:** described only in [CAN2008a]; rely on the MORPH-001 card.
8. **Reference detail:** resolved. The thesis cites CAN2008a as JASIST 59(2); the correct issue is 59(3) (F. Can's publication list; DOI 10.1002/asi.20750), as in the MORPH-001 card.
9. **Official catalogue record** (YÖK thesis number, pages): not verified; web pages could not be opened.

## 20. Decision after deep dive

- **Keep current gap?** Yes. v0.8 refined remains valid (§16).
- **Modify gap?** No.
- **Add decision?** Proposed for `decisions/DECISIONS.md` (researcher's decision): "Qrels pools for the Uzbek benchmark must include all lexical variants, the fixed dense model D and the hybrid runs; search-guided annotation must not rely on a single lexical system." This is also motivated by the MORPH-001 pooling note.
- **Add experiment?** Optional, low cost:
  - within-topic query-length conditions (title vs title + description) for all channels;
  - document-length strata in the complementarity analysis.
  Both reuse the main runs.
- **Add citation to Chapter I?** Only as a secondary citation next to MORPH-001 in §1.1 (e.g., "see also Öcalan, 2009, Ch. 6"). The primary citation should remain Can et al. (2008).
- **Triage correction (proposal):** `carries_complementarity_evidence`: YES → NO. Reading priority may be lowered to MEDIUM for future passes, since the IR content is derivative.
- **Proposed `MASTER_INDEX.md` row** (to add after approval, section C):

| MORPH-022 | Öcalan — *Bilkent News Portal: A System with New Event Detection and Tracking Capabilities* (M.S. thesis, Bilkent University, 2009; adv. F. Can) — [deep dive](deep-dives/2009_Ocalan_Bilkent_News_Portal_Turkish_IR_Parameters.md) | 2009 | A (thesis; IR chapter derivative of MORPH-001) | MEDIUM | Ch. 6 re-presents part of CAN2008a on the same Turkish collection (408,305 docs, 72 queries, MF8 tf-idf, bpref): NS 0.3255 vs F5 0.4322 vs LV 0.4504 (QM); F5 ≈ LV (n.s.) and both > NS (p < 0.001) across query-length, document-length and collection-size strata; longer query forms partly compensate for no stemming (descriptive; no interaction test); stop-words n.s. Figures without values; stop-word deployment statements conflict (p. 17 vs p. 56). No BM25, dense, fusion, overlap/unique-hit or per-query analysis. BilCol2005 TDT collection (209,305 stories, 80 events) with search-guided annotation. |
