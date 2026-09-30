# Iqbal, Amjad, Tahir & Mehmood (2020/2021): CURE: Collection for Urdu Information Retrieval Evaluation and Ranking

**Targeted deep-dive status:** COMPLETED (AI-assisted, pending researcher review)
**Completed:** 2026-09-28
**Verification:** independent AI verifier pass 2026-09-28; 9 findings addressed.
**Literature ID:** `MORPH-039` (assigned 2026-09-28, approved by researcher)
**Systematic-review record:** `CR002024`. Full-text triage: include, reading priority HIGH, reading tier "2 — важно", `carries_complementarity_evidence = YES`. We qualify that flag (§10, §16). The paper has **no dense or semantic channel**. Its per-query evidence is a qualitative error analysis of a lexical pipeline (Sec. 5.3), with counts of failing queries by cause; the full per-query analysis is in an external deliverable that we did not consult (footnote 17). It is not overlap, unique-hit or lexical–dense evidence.
**Provenance:** AI-assisted deep dive (Claude). The whole text (18 pages, references included) was read from the pdftotext extraction. **The analysed PDF is the arXiv preprint** (arXiv:2011.00565v1, 1 Nov 2020, ACM `acmart` template, "1, 1 (November 2020), 18 pages" on p. 1). The assignment metadata points to the **ICoDT2 2021 IEEE proceedings version**, which we did **not** see (§1). All locations are printed page numbers of the preprint, which equal PDF pages. Page images were checked at 110 dpi for pp. 2 (contributions), 4 (Table 1), 5 (Fig. 1, query guidelines), 6 (Figs. 2–3), 7 (Figs. 4–5, pooling), 9 (Fig. 8, Table 2), 10 (Tables 3–4, kappa), 11–12 (Eqs. 2–7, BM25 k1/b, stop-word text), 13 (Fig. 9, lemmatization/QE resources, ranking), 14 (Sec. 5.1–5.3), 15 (Table 5) and 16 (Figs. 10–11). Numbers computed by us are marked **[computed]** and were recomputed with Python.
**Source rule:** **the paper is the primary and only authoritative source.** No code, dataset download, website, later paper or background knowledge is used as evidence about what the authors did. The error-analysis deliverable (footnote 17) and the dataset page (footnote 18) were **not** consulted. Only the bibliographic record was checked on the web (bibliographic check: arXiv abstract page 2011.00565; doi.org resolves `10.1109/ICoDT252288.2021.9441510` to IEEE Xplore document 9441510, and a web search lists that document under this exact title as an "IEEE Conference Publication"). The IEEE page itself and its text could not be fetched; the Crossref record for the DOI (verifier bibliographic check) lists three authors (Muntaha Iqbal, Bilal Tahir, Muhammad Amir Mehmood), pages 1–6, published 20 May 2021.
**Reliability:** **B (conditional).** The work has a verifiable peer-reviewed IEEE conference record (ICoDT2 2021), but:
- we read the 2020 arXiv preprint (18 pages), whose correspondence to the proceedings text (6 pages per Crossref, so substantially condensed) is unverified (if it cannot be confirmed, treat the numbers below as **C**, preprint-level);
- the IR evidence is thin: 50 queries, one small pooled collection, differences of 0.01–0.05 (mostly 0.01–0.02; the largest is VSM P@10 baseline → lemma +0.05) with no significance tests;
- several text statements do not match the paper's own tables (§9, §19).

---

## Кратко для исследователя (RU)

- **Что сделано.** Авторы построили **CURE**, первую, по их словам, стандартную тестовую коллекцию для поиска на урду (Sec. 3):
  - 50 запросов от трёх носителей языка, 2–7 слов, в среднем 4.38 слова (Fig. 3, p. 6);
  - пул: топ-20 документов от **двух лексических моделей (VSM и BM25 в Apache Solr)** из 0.5 млн обойдённых веб-документов. Из 2 000 позиций пула после удаления дубликатов осталось **1 096 документов** из 254 доменов (Sec. 3.3, pp. 6–7);
  - бинарная разметка двумя разметчиками. Каппа по тексту «70%»; по Table 4 **[computed]** 0.689. Третий разметчик разрешил 143 конфликта. Итог: **793 релевантных документа**, т.е. в среднем 15.86 на запрос **[computed]** (Sec. 3.4, p. 10).
- **Затем** на CURE оценены четыре **лексические** модели (TF-IDF VSM, BM25 с k1 = 1.2 и b = 0.75, LM с дирихле-сглаживанием μ = 2000, LM Jelinek–Mercer с λ = 0.7) в четырёх режимах: baseline, удаление стоп-слов, **словарная лемматизация** (3 000 пар «слово–лемма», запрос и индекс) и **расширение запроса словоформами** (2 280 вариантов для 642 слов) (Sec. 4, Table 5, p. 15).
- **Главные числа (Table 5, p. 15), BM25:**
  - baseline: P@10 0.73, MAP@50 0.73, R@50 0.97;
  - лемматизация + SWR: P@10 0.74, MAP@50 0.75;
  - у всех четырёх моделей лемматизация даёт **+0.01…+0.02 MAP@50** к режиму «только SWR» **[computed]**. Расширение запроса поверх этого почти ничего не добавляет: ±0.01.
  - Тестов значимости нет.
- **Морфологические варианты лексического представления есть:** словоформы (с SWR и без) → леммы (словарь) → расширение запроса вариантами. Стемминга как отдельного условия нет. Лемматизация затронула только **24 из 50 запросов** (p. 13).
- **Нет плотного поиска, нет гибрида, нет анализа взаимодополняемости:**
  - нет fusion;
  - нет перекрытия результатов и уникально найденных релевантных документов;
  - нет oracle union.
- **Разбор по запросам — только качественный** (Sec. 5.3, pp. 14–16):
  - LM-JMS находит ≥ 9 релевантных в топ-10 для 30 из 50 запросов;
  - остальные 20 провалов авторы относят к модели ранжирования (11) и к ошибкам NLP (9: токенизатор 2, лемматизация 2, расширение запроса 5);
  - примеры: «Quaid Azam» vs «Jinnah» (именованная сущность + пробел внутри составного имени), «university» vs «jamia» (синоним), дрейф темы после лемматизации до «Science».
- **Ключевое ограничение для нас: пул только лексический** (Solr VSM + BM25, глубина 20). Судя по ID в Fig. 10, оценочные прогоны ищут в самих 1 096 документах пула (наш вывод). Значит, в CURE **нет размеченных релевантных документов, которые не нашли бы лексические модели**. Такая коллекция систематически не засчитывает «уникальные» находки плотного поиска и **непригодна для измерения lexical–dense complementarity** без дополнительной разметки.
- **Связь с карточкой Jabbar et al. 2024 (CR000935), которая оценивает стеммеры на CURE:**
  - та же коллекция, та же модель BM25, а числа сильно различаются: здесь P@10 0.73 и MAP@50 0.73; у Jabbar без стемминга P@10 0.68 и MAP 0.2585;
  - ни одна статья не сообщает достаточно (глубина MAP, корпус поиска, поля, предобработка), чтобы это согласовать;
  - CURE подтверждает вывод той карточки, что у части запросов > 10 релевантных документов: в среднем 15.86 на запрос.
- **Внутренние несоответствия** (§9, §19):
  - в тексте P@10 BM25/LM-JMS «0.71–0.72», VSM/LM-DS «0.67–0.68», а в Table 5 — 0.73/0.73 и 0.66/0.69;
  - «SWR улучшает LM-JMS», но в Table 5 его строки не выросли, а R@50 упал 0.97 → 0.96;
  - в Table 1 у CURE «500 000 документов, 1 096 релевантных», тогда как в коллекции 1 096 документов и 793 релевантных;
  - P(E) = 0.57 в тексте vs 0.581 по Table 4.
- **Для нашего gap:** подтверждает уже занятый элемент «raw vs lemma под BM25 в low-resource языке» (урду). **Ядро v0.8** (raw/stem/lemma × фиксированный D → уникальные релевантные / перекрытие → прирост гибрида → признаки запросов) **не затрагивается**. Предложение: gap не менять.
- **Практическая польза для нас:**
  1. Пул для узбекских qrels должен включать **все варианты лексического канала и D** (и, желательно, гибриды). Иначе уникальные находки D будут недооценены по построению.
  2. Словарные ресурсы (лемматизатор, варианты) нельзя строить по частотным словам оценочной коллекции. Их источник надо фиксировать отдельно от test.
  3. Долю запросов, которые реально изменила нормализация (здесь 24/50), надо сообщать и анализировать отдельно.
  4. В таксономию запросов стоит добавить многословные имена и синонимию.

---

## 1. Bibliographic record

- **Authors (preprint, p. 1):** Muntaha Iqbal, Kamran Amjad, Bilal Tahir, Muhammad Amir Mehmood. All are at the Al-Khawarizmi Institute of Computer Science (KICS), UET Lahore, Pakistan.
  - The assignment metadata for the proceedings version lists three authors (M. Iqbal; B. Tahir; M. A. Mehmood), without Kamran Amjad. The Crossref record for the DOI confirms this three-author list (bibliographic check by the verifier; IEEE page itself not fetchable).
- **Year:** preprint 2020 (arXiv v1, 1 Nov 2020); proceedings 2021
- **Venue (proceedings):** 2021 International Conference on Digital Futures and Transformative Technologies (ICoDT2), IEEE (assignment metadata; bibliographic check: the DOI below resolves to IEEE Xplore document 9441510, listed under this title as an IEEE Conference Publication)
- **DOI:** `10.1109/ICoDT252288.2021.9441510` (bibliographic check: doi.org 302 redirect to https://ieeexplore.ieee.org/document/9441510). Proceedings pages: 1–6, published 20 May 2021 (Crossref record; bibliographic check). The "18" pages in the metadata correspond to the arXiv preprint.
- **Preprint:** arXiv:2011.00565 (DOI `10.48550/arXiv.2011.00565`; bibliographic check: arXiv abstract page, v1 only, no journal-ref)
- **Data (stated in paper):** "CURE is freely available for the research community online" (p. 2). Footnote 18 (p. 17) gives `http://kics.edu.pk/kics_pms/index.php?r=user/auth`. Not consulted.
- **Source type:** peer-reviewed IEEE conference paper (record verified); the analysed text is the arXiv preprint
- **Reliability:** B (conditional; see header)
- **Full text available:** yes, preprint (`07_full_text/pdfs/CR002024.pdf`, 18 pages)

## 2. Why this work matters to the PhD

It is the **test-collection paper** behind a benchmark that at least two works in our Urdu cluster reuse: Jabbar et al. 2024 (CR000935, stemmers under BM25) and Kazi & Khoja 2026 (HYB-010). It also shows directly how pooling, judging and morphological resources were done for a low-resource, morphologically complex language at the scale an Uzbek pilot can afford (50 queries, ≈ 1K documents).

| Axis | Relation |
|---|---|
| Lexical retrieval | Main content: VSM, BM25, LM-DS, LM-JMS, each under baseline / stop-word removal / dictionary lemmatization / inflectional query expansion (Table 5) |
| Semantic retrieval | **Absent** |
| Hybrid retrieval | **Absent** |
| Uzbek morphology | Indirect. Urdu is Indo-Aryan, Perso-Arabic script, with Persian/Arabic loans; Uzbek is Turkic, agglutinative. The lemmatization is a small lookup dictionary, not a morphological analyzer |
| Low-resource retrieval | Direct: first Urdu test collection by the authors' account; resources built by hand |
| Current gap | Adds a raw vs lemma (plus expansion) comparison under four lexical models (occupied element). Its pooling design is a methodological warning for qrels (§17). Does **not** touch the v0.8 core (§16) |

## 3. Research problem

### Simple explanation

To compare search systems for Urdu you need a fixed set of queries, documents and human judgments of which documents answer which query. The authors say no usable public Urdu collection of this kind existed. The one earlier attempt had 200 documents and 4 queries and was not public (Sec. 2, p. 4). So they build one. They then run standard search models on it, with and without simple language processing, to show it can be used.

### Formal formulation

No formal research questions are stated. The contributions (p. 2) are:
1. **test collection creation:** crawled corpus, 50 queries, pooled top-20 of VSM and BM25, binary judgments;
2. **evaluation of IR models:** P, R, MAP for four models;
3. **evaluation of IR models with NLP techniques:** stop-words, lemmatization, query expansion.

Task: ad hoc document retrieval. For query q, rank the CURE documents d by a lexical score s(q,d), and evaluate with binary qrels at cut-offs 10/20/50.

## 4. Main idea

### Simple explanation

Three native speakers write information needs and short queries. Two classic search engines return 20 documents each for every query from half a million crawled Urdu web pages. Duplicates are removed, people judge each remaining document as relevant or not, and the judged set becomes the collection. Then four classic ranking models are run on it, first on plain words, then after removing stop-words, reducing words to a dictionary form, or adding other forms of each query word.

### Concrete example (paper's own)

- Query "Amarten" (عمارتیں, "buildings"). Lemmatization maps it to "Amart" (عمارت, "building"). Query expansion then retrieves documents containing "Amarten", "Amart" or "Amarton" (Sec. 4.3, p. 13; Fig. 9).
- Failure (Fig. 10, p. 16): a query containing the name "Quaid Azam" (five tokens after tokenization, p. 15) has the name split at the space into "Quaid" and "Azam". Five relevant documents are retrieved (underlined in Fig. 10); relevant documents that say "Jinnah", or write the name without the space, are missed (p. 15).

### Formal method

Candidate generation, then lexical scoring (Sec. 4.2–4.4, pp. 11–13):

- **Candidates:** an OR over the query terms (queries longer than one word): only documents containing at least one query term are ranked (p. 11).
- **Per-term field scoring:** for each query term, the score is taken on the title and the content field separately, and the **maximum** of the two is kept (Sec. 4.4, p. 13).
- **Combination:** term scores are **summed** for VSM and BM25, and **multiplied** for the language models (p. 13).
- **BM25** (Eq. 4, p. 11): `Σ_t log((ND − DF + 0.5)/(DF + 0.5)) · tf·(k1+1) / (tf + k1·(1 − b + b·dL/avgdL))`, with **k1 = 1.2, b = 0.75**.
- **VSM** (Eqs. 2–3): cosine similarity; TF-IDF = `√tf · (1 + log(ND/(DF+1)))`.
- **LM-DS** (Eqs. 5–6): Dirichlet, μ = 2000.
- **LM-JMS** (Eq. 7): Jelinek–Mercer, λ = 0.7.

## 5. Architecture / algorithm

1. **Crawl** (Sec. 3.3, p. 6): Apache Nutch 2.3.1; 0.5 million Urdu web documents, Aug–Nov 2017, mostly news sites; indexed in Apache Solr 6.2.2 with id, title and content.
2. **Queries** (Sec. 3.1–3.2, pp. 4–6):
   - three native speakers, trained with four example needs/queries from history, sports, business and health;
   - 60 queries written (20 each); queries longer than 7 words removed, leaving 50;
   - fields: QID, totalWords, noOfWordsWithSWR, title (the query), description (the information need) (Fig. 2, p. 6).
3. **Pooling** (Sec. 3.3, pp. 6–7): top 20 per query from **VSM and BM25 in Solr** → 2,000 pool entries → 1,096 documents after removing duplicates, 254 domains, 6.7 MB, XML (id, title, body).
   - Whether de-duplication was done within each query or across queries is not stated. See §6 and §19.
4. **Judging** (Sec. 3.4, pp. 8–10): see §6.
5. **Query preprocessing** (Sec. 4.1, p. 11): whitespace tokenization; punctuation removed.
6. **NLP conditions** (Sec. 4.3, pp. 12–13):
   - **Stop-word removal (SWR):** a CLE Urdu closed-class word list, reduced from 402 to 211 words by removing cardinal and ordinal numbers. "We removed stop-words **from the query**" (p. 12), so SWR is query-side only as described.
   - **Lemmatization:** dictionary lookup, 3,000 word–lemma pairs, "applied at the query and index level" together with SWR (p. 13). It changed **24 of the 50 queries** (p. 13). The authors describe lemmatization as "used to find the root or stem of the input word" (p. 12).
   - **Query expansion (QE):** the 1,000 most frequent words of "our index" → 642 unique words after SWR → 2,280 manually written inflectional variants (1–12 per word, mean 3.55 **[computed ✓ 2280/642 = 3.55]**). A query word is mapped to its root form, then the root and its variants are added (p. 13).
   - The abstract says both resources were built "specific to our test collection" (p. 1).
   - **Pipeline order** (p. 14): tokenization → SWR → lemmatization → QE. Fig. 10 shows QE applied after lemmatization. So the "Query-Expansion with SWR" condition probably also includes lemmatization (**our inference**). Whether the index is lemmatized in the QE condition is **NOT_REPORTED**.
7. **Evaluation runs:** the toolkit for the four evaluated models is **NOT_REPORTED**. Solr is named only for pooling. The custom field-max / sum / product ranking of Sec. 4.4 suggests the authors' own scoring layer, but this is not stated.
8. **Formula notation issues (paper):** Eq. 6 and Eq. 7 take products over "t in (q,d)". Under Eq. 6, c(t,d) is glossed as "the document frequency of a term", though in a Dirichlet model it is the term count in d. Neither affects the reported numbers, which cannot be checked.

## 6. Data

- **Dataset:** CURE (Collection for Urdu Retrieval Evaluation)
- **Language / domain:** Urdu; web, about 75% from news sites and 18% general sites, plus blogs, forums and social media (p. 8); 11 topic categories (Table 2; Fig. 4, p. 7)
- **Source corpus:** 0.5 million crawled documents (not the evaluation collection)
- **Collection:** 1,096 documents, 6.7 MB, 859,432 tokens (461,300 after stop-word removal), 15,418 unique tokens; document size 1–143 KB, over 80% within 1–10 KB (Table 2, p. 9; Fig. 6, p. 8)
- **Queries:** 50; 219 tokens, 143 unique (Table 2)
  - Length distribution (Fig. 3, p. 6): 2 words ×2, 3 ×7, 4 ×21, 5 ×12, 6 ×6, 7 ×2. Mean 4.38 **[computed ✓ 219/50]**.
  - 30% of queries are in the national/international news categories (p. 6).
- **Relevance judgments** (Sec. 3.4, pp. 8–10):
  - binary; judged by two of the three query creators (S1, S2) over all 1,096 documents;
  - guidelines: partially relevant counts as relevant; a document with a synonym instead of the query word counts as relevant;
  - Table 4: S1 judged 813 relevant, S2 732, both 701; both non-relevant 252; conflicts 31 + 112 = 143 **[computed ✓]**;
  - S3 resolved the 143 conflicts and marked 92 relevant → **793 relevant** **[computed ✓ 701 + 92]**;
  - relevant per query: **15.86 on average** **[computed, 793/50]**. The per-query distribution is NOT_REPORTED. Judged per query: 21.92 on average **[computed, 1096/50]**; the paper prints "21" (p. 6 text, "On average, 21 documents were retrieved for each query"; Table 2, p. 9). Relevant share of the pool: 72.4% **[computed]**.
  - Qrels format: query ID, document ID, 0/1 (Table 3, p. 10).
- **Agreement:** Cohen's kappa. The text reports "P(A) and P(E) is 0.87 and 0.57 respectively so 'agreement score' is 70%" (p. 10). Recomputed from Table 4 **[computed]**: P(A) = 0.870, P(E) = 0.581, kappa = **0.689**. From the printed rounded values: 0.698.
- **Train/dev/test:** none. All runs use the full collection, and there is no tuning described. The lemmatization and QE resources were derived from the collection's own index (§5).
- **Retrieval corpus for the Table 5 runs:** not stated explicitly. Table 2 and the document IDs retrieved in Figs. 10–11 (four-digit CURE IDs such as 0093–0122, 0219 and 0564–0576, p. 16) indicate that retrieval runs over the **1,096 pooled documents**, not over the 0.5M crawl (**our inference**).
- **How pool membership relates to queries:** the Table 3 and Fig. 10 IDs come mostly in contiguous blocks per query. This suggests each document was pooled, and judged, for one query only. One exception is informative: the tokenizer-error query in Fig. 10 (block 0093–0104) also retrieves 0219, which is not underlined (not relevant), i.e. a document from outside its block, consistent with retrieval over the whole 1,096-document pool. Judgments exist only for the 1,096 pooled pairs, so documents pooled for other queries are presumably treated as non-relevant (**our inference**; not stated).

## 7. Baselines

| System | What it is | Why selected (paper) | Fair comparison? |
|---|---|---|---|
| TF-IDF VSM | Cosine over √tf·idf vectors | Not stated (chosen "for comparison", p. 11) | Same collection and ranking layer. But **VSM was one of the two pooling systems** (in Solr) |
| BM25 (k1 1.2, b 0.75) | Probabilistic lexical ranking | Not stated | Same caveat: **a pooling system** |
| LM-DS (μ = 2000) | Query likelihood, Dirichlet smoothing | Not stated | Not a pooling system. Parameter untuned |
| LM-JMS (λ = 0.7) | Query likelihood, Jelinek–Mercer | Not stated | Not a pooling system. λ is set without reported tuning, although the paper says it "needs to be tuned" (p. 12) |
| Baseline condition | No SWR, no lemma, no QE | Reference for NLP effects | Yes as a reference. The **clean lemma effect** is "Lemmatization with SWR" vs "SWR", since both include SWR |

**Not present:** stemming as an IR condition; character n-grams; any dense, neural or semantic retriever; any fusion.

## 8. Metrics

| Metric | Definition (paper, Sec. 5.1, p. 14) | Simple meaning here | Appropriate? |
|---|---|---|---|
| P@10, P@20 | relevant in top k / k | "How many of the first 10 (20) results are relevant?" | Yes, but capped: with a mean of 15.86 relevant per query, P@20 cannot reach 1 for queries with fewer than 20 relevant documents |
| Recall@50 | relevant in top 50 / all relevant "present in the corpus" | "Share of judged relevant documents found in the top 50" | **Weak here.** If retrieval runs over the 1,096-document pool (§6), the pooling systems nearly exhaust the judged set by construction |
| MAP@50 | Described only as "mean of average precision over all queries" | Rank quality of the top 50 | The **AP normaliser is NOT_REPORTED**: all relevant documents, or only those retrieved within 50. This matters for comparing with other CURE papers (§15) |

No nDCG. No significance test (§10).

## 9. Results

### Table 5: results of retrieval models, 50 queries (p. 15; verified on page image)

| Technique | Model | P@10 | P@20 | R@50 | MAP@50 |
|---|---|---:|---:|---:|---:|
| Baseline | BM25 | 0.73 | 0.62 | 0.97 | 0.73 |
| | VSM | 0.66 | 0.57 | 0.86 | 0.69 |
| | LM-DS | 0.69 | 0.58 | 0.93 | 0.68 |
| | LM-JMS | 0.73 | 0.61 | 0.97 | 0.73 |
| Stop-Words-Removal (SWR) | BM25 | 0.73 | 0.62 | 0.97 | 0.74 |
| | VSM | 0.69 | 0.57 | 0.86 | 0.70 |
| | LM-DS | 0.69 | 0.58 | 0.93 | 0.68 |
| | LM-JMS | 0.73 | 0.61 | 0.96 | 0.73 |
| Lemmatization with SWR | BM25 | 0.74 | 0.63 | 0.97 | 0.75 |
| | VSM | 0.71 | 0.58 | 0.87 | 0.72 |
| | LM-DS | 0.71 | 0.59 | 0.93 | 0.70 |
| | LM-JMS | 0.75 | 0.63 | 0.97 | 0.75 |
| Query-Expansion with SWR | BM25 | 0.74 | 0.63 | 0.98 | 0.75 |
| | VSM | 0.71 | 0.58 | 0.88 | 0.72 |
| | LM-DS | 0.70 | 0.58 | 0.94 | 0.69 |
| | LM-JMS | 0.75 | 0.63 | 0.98 | 0.75 |

Differences **[computed]**, as (P@10, P@20, R@50, MAP@50):

| Model | Lemma+SWR − SWR (clean lemma effect) | Lemma+SWR − Baseline | QE+SWR − Lemma+SWR |
|---|---|---|---|
| BM25 | +0.01, +0.01, 0.00, +0.01 | +0.01, +0.01, 0.00, +0.02 (MAP +2.7% rel.) | 0.00, 0.00, +0.01, 0.00 |
| VSM | +0.02, +0.01, +0.01, +0.02 | +0.05, +0.01, +0.01, +0.03 (+4.3%) | 0.00, 0.00, +0.01, 0.00 |
| LM-DS | +0.02, +0.01, 0.00, +0.02 | +0.02, +0.01, 0.00, +0.02 (+2.9%) | −0.01, −0.01, +0.01, −0.01 |
| LM-JMS | +0.02, +0.02, +0.01, +0.02 | +0.02, +0.02, 0.00, +0.02 (+2.7%) | 0.00, 0.00, +0.01, 0.00 |

Reading:
- Lemmatization raises every model by 0.01–0.02 in P@10 and MAP@50 over SWR alone. A P@10 difference of 0.01 over 50 queries is **5 more relevant documents in the top 10 in total** **[computed: 0.01 × 10 × 50]**. Because both values are rounded to two decimals, a printed 0.01 difference is compatible with a true difference between 0 and 0.02, i.e. 0–10 documents **[computed]**.
- Lemmatization changed only 24 of the 50 queries (p. 13). The per-query effect on those 24 is therefore roughly twice the averaged figure, if the other 26 are unchanged (**our inference**; per-query values not reported).
- QE on top of lemmatization changes nothing beyond ±0.01; it hurts LM-DS slightly.
- BM25 ≈ LM-JMS > LM-DS ≈ VSM in every condition. VSM has the lowest R@50 (0.86–0.88) although it was a pooling system (in its Solr form).
- None of these differences is tested for significance, and most (all Lemma+SWR vs SWR and QE vs Lemma differences) are at the rounding resolution (two decimals); the largest, VSM P@10 baseline → Lemma+SWR (+0.05), is not.

### Sec. 5.3: per-query error analysis (pp. 14–16)

- "LM-JMS (P@10) returned at least nine correct relevant documents for 30 out of 50 total queries" (p. 14). The condition (baseline or NLP pipeline) is not stated.
- For the remaining 20 queries, irrelevant documents came from the retrieval model (11) and from NLP errors (9). The NLP errors break down as word tokenizer 2, lemmatization 2, query expansion 5 (pp. 14–15) **[computed ✓ 11 + 9 = 20; 2 + 2 + 5 = 9]**.
- Examples (Figs. 10–11, p. 16):
  - **Tokenizer:** a multi-word name split at the space; relevant documents use another name ("Jinnah") or no space.
  - **QE:** synonyms such as "jamia/jamiat" for "university" are not in the variant list.
  - **Lemmatization:** the lemma "Science" matched index terms and "less relevant documents were pushed to higher ranks".
  - **Model (LM-JMS):** documents with high frequency of "qadeem" (ancient) dominate.
- Authors' conclusion: "for the baseline case", mostly documents containing the original query words were retrieved; with lemmatization and QE, retrieval "relied on root words and variants". "In our case, most errors were observed for query expansion", and synonyms would help (p. 16).
- The "query-by-query error analysis" for 20 queries is only in an external deliverable (footnote 17). It is not in the paper and was not consulted.

### Internal inconsistencies (all within the paper)

1. **P@10 ranges in the text vs Table 5.** Sec. 5.2 (p. 14): "Precision@10 values for BM25 and LM with Jelenik Mercer smoothing for baseline perform in the range of 0.71 − 0.72 whereas VSM the LM with Dirichlet smoothing shows a lower performance of 0.67 − 0.68". Table 5 baseline: BM25 0.73, LM-JMS 0.73, VSM 0.66, LM-DS 0.69.
2. **SWR effect on LM-JMS.** The contributions (p. 2) say that with stop-word removal "results of BM25, VSM, and LM-JMS are improved slightly". In Table 5, LM-JMS SWR vs baseline is P@10, P@20 and MAP identical, and R@50 **drops** 0.97 → 0.96.
3. **Table 1 row for CURE** (p. 4): "Documents 500,000; Relevant Documents 1,096". The collection has 1,096 documents (Table 2) and 793 judged relevant (p. 10).
4. **Kappa inputs.** The text gives P(E) = 0.57 and "70%". Table 4 gives P(E) = 0.581 and kappa = 0.689 **[computed]**.
5. **Judged documents per query:** "21" (p. 6, Table 2) vs 1,096/50 = 21.92 **[computed]**, i.e. truncated rather than rounded.
6. **Order of procedure.** Sec. 3.2 says queries over 7 words were removed because judges were confused. Sec. 3.4 says the conflict analysis after judging led them to change the guidelines: "we revised our guidelines and restricted query length to a maximum of 7 words" (p. 10). The sequence of judging and query filtering is therefore unclear.
7. **QE "improved performance" (p. 2)** for BM25, VSM and LM-JMS: relative to lemmatization only R@50 changes (+0.01); relative to baseline, LM-DS also improves. The reference condition is not stated.

## 10. Statistical evidence

- **Significance tests:** NOT_REPORTED. The word "significant" is used for LM-JMS vs LM-DS (p. 14) without a test.
- **Confidence intervals:** NOT_REPORTED.
- **Runs / seeds:** not applicable; deterministic lexical models.
- **Ablation:** a partial, cumulative pipeline: baseline → +SWR → +lemma → +QE. The lemma effect is isolated (Lemma+SWR vs SWR); the QE effect probably is not isolated from lemmatization (§5). Parameters (k1, b, μ, λ) are not varied.
- **Per-query analysis:** qualitative only (Sec. 5.3): counts of failing queries by attributed cause, and three illustrative queries. There are:
  - no per-query metric values and no win/tie/loss counts between conditions;
  - no analysis by query length or category, although both are recorded (Figs. 3–4);
  - **no overlap / unique relevant hit / oracle-union analysis** between models or representations, and no semantic channel.
- **Only overlap-like number (our inference, not the authors' framing):** the pool shrank from 2,000 entries to 1,096 documents. If de-duplication was within each query, the VSM and BM25 top-20 lists (in Solr) shared on average **18.1 of 20 documents per query (≈ 90%)** **[computed: (2000 − 1096)/50]**. This is an overlap between two lexical models, and it holds only under that assumption (§19).
- **Agreement:** kappa ≈ 0.69 on 1,096 pairs (§6).

## 11. Strengths

- A documented **public-by-claim Urdu test collection** with queries, descriptions (information needs), binary qrels, two-judge agreement and a third-judge adjudication.
- Clear query-creation guidelines, including the synonym rule for relevance, which is relevant to vocabulary mismatch.
- A **controlled lexical comparison across four models** with explicit parameters (k1, b, μ, λ), and a clean raw-vs-lemma contrast under a constant stop-word setting.
- The error analysis names concrete failure types (tokenization of multi-word names, missing synonyms, lemma-induced drift, term-frequency bias) that map onto candidate query features.
- Reports how many queries the normalization actually touched (24/50), which is rare and useful.

## 12. Limitations

### Stated by the authors

- Most errors come from query expansion. Synonyms are missing from the expansion dictionary (p. 16).
- The Urdu word tokenizer splits multi-word names at spaces (pp. 15–16).
- Lemmatization can promote less relevant documents (p. 15).
- Model behaviour is collection-dependent. The LM-JMS vs LM-DS difference "can be due to the nature of the language or the smoothing values used", left for future work (p. 14).
- Judges were stricter on their own queries than on others', which was the main source of conflicts. Long queries confused judges (p. 10).
- Future work: more documents and queries (p. 17).

### Inferred from the experimental design

1. **Lexical-only, shallow pooling.** VSM and BM25 in Solr, depth 20. If retrieval runs over the pool (§6), no relevant document without lexical overlap with the query can exist in the collection. Two of the four evaluated models, in their Solr forms, built the pool. Any later **dense retriever evaluated on CURE is structurally disadvantaged**, and its unique hits are unjudged or absent.
2. **Tiny effects, no tests.** NLP effects are 0.01–0.05 (mostly 0.01–0.02; the clean lemma effect vs SWR is 0.00–0.02) at two-decimal resolution on 50 queries.
3. **Resources derived from the test collection.** The lemma and variant dictionaries are "specific to our test collection" (p. 1) and were "manually developed ... from most frequent words of indexed documents" (p. 17); QE uses the 1,000 most frequent index words (p. 13). That is favourable to lemmatization and QE; it is not a held-out evaluation.
4. **Judges = query authors**, two of three. Relevance is liberal: "partially relevant" counts as relevant, which is consistent with (but not shown to cause) the 72% relevant share of the pool; per-query pooling from two lexical systems also contributes.
5. **Ambiguous conditions:** whether the QE condition includes index lemmatization; whether the index is stop-word filtered; the MAP@50 normaliser; the evaluation toolkit.
6. **Non-standard ranking layer:** per-term max over title/content fields, then summed or multiplied. This is not standard BM25 over a concatenated document or BM25F, which limits comparability with other CURE results.
7. **Preprint vs proceedings:** we analysed the arXiv v1. The IEEE version may differ.

## 13. What the work proves

- A **1,096-document, 50-query Urdu test collection with binary qrels** exists: 793 relevant, kappa ≈ 0.69 between two judges, adjudicated by a third (Sec. 3, Tables 2–4).
- On this collection, **classic lexical models reach P@10 0.66–0.73 and MAP@50 0.68–0.73 without any processing**. BM25 and LM-JMS are the strongest (Table 5).
- **Dictionary lemmatization (query + index) gives small, consistent gains of +0.01 to +0.02 in P@10 and MAP@50 for all four models** over stop-word removal alone. Inflectional query expansion on top adds nothing measurable (Table 5). No significance test was run.
- Dictionary lemmatization **touched only 24 of 50 queries** (p. 13).
- Qualitatively, remaining failures involve multi-word names, synonymy and lemma-induced topic drift (Sec. 5.3).

## 14. What the work does NOT prove

- **That lemmatization or QE reliably improves Urdu retrieval.** The differences are untested and at rounding resolution, and the resources were built from the test collection.
- **Anything about stemming vs lemmatization.** There is no stemming condition; see Jabbar et al. 2024 (CR000935) for stemmers on CURE.
- **Anything about dense or semantic retrieval, fusion, or lexical–dense complementarity.** None is present, and the pooling design would bias any such comparison (§12).
- **Which queries benefit from lemmatization and why.** No per-query metric values; the error analysis is qualitative and partly external.
- **That CURE supports deep-recall or unique-hit analysis.** The pool is 2 lexical systems × depth 20.
- **That the numbers are comparable with other CURE papers.** The ranking layer and MAP normaliser are non-standard or unreported (§15).

## 15. Relationship to current Uzbek evidence

- **No Uzbek data.** Transfer is at the level of method and caution.
- **Urdu cluster in our corpus:**
  - MORPH-003 UPERF (raw/stemmed/lemmatized × BM25/TF-IDF/embeddings; own large corpus; Recall@5);
  - HYB-010 Kazi & Khoja 2026 (CURE among three benchmarks; lexical + embedding features + SVMrank);
  - Jabbar et al. 2024, CR000935 (raw vs 3 stemmers under BM25 on CURE).
  CURE is the shared benchmark under the last two. Its lexical-only pool therefore also limits any lexical–semantic claims those works make on CURE. This is our inference; we have not checked how HYB-010 handles unjudged documents.
- **Direct comparison with the Jabbar et al. 2024 card (CR000935):**
  - Same collection by description: "1096 documents from 254 domains with 50 queries" citing this paper (CR000935 card §6).
  - Same nominal model (BM25), no stemming:
    - here, baseline P@10 **0.73** and MAP@50 **0.73** (Table 5);
    - there, P@10 **0.68**, MAP **0.2585**, R@10 0.4822 (CR000935 Table 13).
  - The P@10 gap is moderate. The MAP gap, 0.73 vs 0.26, is too large to be noise. Possible sources: different retrieval corpus, AP normaliser (all relevant vs retrieved relevant), MAP depth, field handling or preprocessing. **Neither paper reports enough to reconcile this. Do not cite either paper's CURE numbers as a reference baseline for the other.**
  - CURE confirms that card's inference that some queries have more than 10 relevant documents: the mean is 15.86 per query **[computed]**, so at least one query exceeds 10. This also explains why R@10 there is well below P@10.
  - Morphology effects are small in both: lemma +0.01 P@10 / +0.01 MAP@50 here (BM25, vs SWR); UTS stemmer +0.032 P@10 / +0.0013 MAP there. Neither has significance tests.
- **Parallel for Uzbek:** national morphology work reports analyzer accuracy without qrels (`MASTER_INDEX` MORPH-UZ-002/004). CURE shows what a minimal qrels-based lemma evaluation looks like at pilot scale, and how little it can resolve without paired tests and more queries.
- Context (not from the paper): an Uzbek dictionary lemmatizer with a few thousand entries would, as here, touch only part of the queries. Coverage is a first-order variable for the `BM25_lemma` condition.

## 16. Relationship to CURRENT_GAP

**Classification:** *supports (background)* + *no material effect on the residual core*. It also offers a methodological warning for our qrels design (§17).

- **Already-occupied elements it touches:**
  - "raw/stem/lemma have not been compared in low-resource IR" (already rejected in `GAP_BOUNDARY`): this paper adds raw vs dictionary lemma (and inflectional QE) under four lexical models for Urdu;
  - "morphology has not been applied to low-resource search" (occupied).
- **Supports (background):** normalization changes which documents are retrieved, qualitatively, in both directions: lemma-induced drift vs recovered variants (Sec. 5.3). Aggregate metrics barely move. This is consistent with the v0.8 premise that set-level and per-query decomposition is more informative than MAP.
- **No material effect on the v0.8 refined core:**
  - no dense comparator D;
  - no fusion;
  - no unique relevant hits, overlap or oracle union between channels or representations;
  - no hybrid gain;
  - no quantitative link to query features.
- The triage flag `carries_complementarity_evidence = YES` should be read as "qualitative per-query failure attribution within a lexical pipeline". It is not complementarity evidence in the project's sense.

**Proposal:** keep v0.8 refined unchanged. Optionally list CURE in `GAP_BOUNDARY` §3 as the shared Urdu benchmark behind CR000935 and HYB-010, noting its lexical-only pool. This is a proposal only; `CURRENT_GAP.md` has not been edited.

## 17. Implications for our research design

- **Qrels / pooling (most important).**
  - Build the Uzbek judgment pool from **every system whose unique hits we will measure**: `BM25_raw`, `BM25_stem`, `BM25_lemma`, D, and ideally the hybrids.
  - Use a depth large enough for the reported cut-offs, e.g. ≥ 50–100 if we report Recall@100.
  - A lexical-only pool, as in CURE, makes "dense-unique relevant documents" undercounted by construction. Our core quantity would then be biased.
  - Report the pool contribution of each system: unique pooled documents, and unique relevant documents per system.
  - Search over a realistic corpus, not only the pool. Treat unjudged documents explicitly: report judged@k, or use condensed-list metrics as a sensitivity check.
- **Morphology resources.** Build or choose the stemmer, lemmatizer and any variant lists **independently of the test collection**, for example from a separate corpus or the dev split. Report coverage: the share of query tokens and queries changed by each normalization (cf. 24/50 here).
- **Controlled contrast.** Hold stop-words, tokenization and field handling constant across raw/stem/lemma. Here the clean lemma contrast is "Lemma+SWR vs SWR". State whether normalization is applied to query, index or both. Do not stack QE on lemmatization without a separate condition.
- **Field handling.** Use one documented scoring scheme: a concatenated document, or an explicit BM25F. The CURE per-term max over title/content is non-standard and hampers comparability.
- **Query taxonomy.** Add or retain these features:
  - **multi-word named entities / space-separated names** (tokenization failure);
  - **synonym-dependent needs**, where no morphological normalization can help and D should dominate;
  - **normalization coverage per query** (did the lemmatizer change this query?);
  - query length (CURE: 2–7 words).
- **Metrics and statistics.** Define MAP/AP normalisation and depth explicitly. Report per-query values, win/tie/loss counts and paired tests. With about 50 queries, effects of 0.01–0.02 are not interpretable.
- **Judging protocol.** Judges should not only judge their own queries (the source of conflicts here). Report kappa computed from the contingency table, not rounded components. Keep the information-need description with each query: CURE's "description" field is a good template.
- **Hypothesis.** No evidence for or against. Small aggregate lemma gains with qualitatively two-directional per-query changes are the situation in which our set-level decomposition is informative.

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| Test collection | A fixed set of documents, queries and human relevance labels used to compare search systems | (D, Q, qrels) in Cranfield/TREC-style evaluation |
| Pooling | Only the top results of some systems are judged; everything else is assumed non-relevant | Judged set = ∪ top-k of the pooled runs |
| Pool bias | Systems that did not contribute to the pool are penalised because their unique finds are unjudged | Bias of metrics against non-pooled runs |
| Qrels | The list of (query, document, label) judgments | Relevance judgments file |
| Cohen's kappa | Agreement between two judges beyond chance | (P(A) − P(E)) / (1 − P(E)) |
| VSM / TF-IDF | Documents and queries as weighted word vectors, compared by angle | Cosine over tf·idf weights |
| BM25 | Word-matching score with term-frequency saturation (k1) and length normalization (b) | Okapi BM25 |
| Query-likelihood LM (Dirichlet / Jelinek–Mercer) | Score = how likely the document's word distribution is to produce the query, smoothed with the collection | P(q\|d) with Dirichlet (μ) or linear (λ) smoothing |
| Stop-word removal | Dropping very frequent function words | List-based filtering |
| Dictionary lemmatization | Replacing a word with its dictionary form using a lookup table | Word → lemma mapping from a fixed list |
| Query expansion (inflectional) | Adding other forms of each query word to the query | q' = q ∪ variants(lemma(t)) |
| P@k / Recall@k / MAP@k | Share of relevant in top k / share of all relevant found in top k / average precision averaged over queries | Standard IR metrics |
| Complementarity (project term) | Each channel finds some relevant documents the other misses | Unique relevant hits, overlap, oracle-union gain |

## 19. Open questions / verification needed

1. **Proceedings vs preprint:** does the ICoDT2 2021 version (DOI `10.1109/ICoDT252288.2021.9441510`) match the arXiv v1 text and Table 5? Crossref gives three authors (no Kamran Amjad) and pp. 1–6, so the proceedings text is a condensed 6-page version of the 18-page preprint; its content is still unseen.
2. **Retrieval corpus of the Table 5 runs:** the 1,096 pooled documents (our inference from Figs. 10–11) or the 0.5M crawl? This is NOT_REPORTED.
3. **Pool de-duplication:** within query or across queries? This determines whether the ≈ 90% VSM–BM25 top-20 overlap reading holds. Can a document be relevant to more than one query?
4. **MAP@50 definition** (AP normaliser) and **evaluation toolkit**; whether the QE condition includes index lemmatization; whether SWR is query-only in all conditions.
5. **Reconciling CURE numbers across papers:** here BM25 MAP@50 0.73 vs Jabbar et al. (CR000935) BM25 MAP 0.2585 on nominally the same collection. Before we use CURE as any reference, a reproduction with a standard toolkit would settle it (optional; §20).
6. **Per-query lemma effects** on the 24 affected queries: only the external deliverable (footnote 17) might have them. We did not consult it (source rule).
7. **Dataset availability:** footnote 18 points to a KICS login URL. Public availability without registration is not established from the paper.

## 20. Decision after deep dive

- **Keep current gap?** Yes. v0.8 refined remains valid; see §16.
- **Modify gap?** No change proposed. Optionally add CURE to `GAP_BOUNDARY` §3 as the shared Urdu benchmark behind CR000935 and HYB-010, with the lexical-only pool caveat (researcher's decision).
- **Add decision?** Proposed for `decisions/DECISIONS.md` (researcher's decision):
  - "The Uzbek judgment pool includes all lexical variants (raw/stem/lemma) and the fixed dense model D, at a depth ≥ the deepest reported cut-off. Per-system unique pooled and unique relevant counts are reported";
  - "Morphological resources (stemmer/lemmatizer/variant lists) are fixed before, and independently of, the test collection. Their per-query coverage is reported".
- **Add experiment?** Optional, low cost: if CURE is publicly obtainable, run a standard-toolkit BM25 raw vs lemma plus a multilingual dense model on it. Report judged@10 for the dense run, to quantify how strongly a lexical-only pool penalises dense retrieval. This would give a concrete pool-bias argument for our qrels design.
- **Add citation to Chapter I?** Yes, in two places:
  - §1.1, as a low-resource test-collection example with dictionary lemmatization under classic lexical models;
  - §1.3 or the methodology chapter, as an example of lexical-only pooling that limits lexical–semantic comparisons.
  Cite with care: Table 5 values only, and state that no significance tests were reported.
- **Proposed `MASTER_INDEX.md` row** (to add after approval):

| MORPH-039 | Iqbal, Amjad, Tahir, Mehmood — *CURE: Collection for Urdu Information Retrieval Evaluation and Ranking* (ICoDT2 2021, IEEE; DOI 10.1109/ICoDT252288.2021.9441510; analysed as arXiv:2011.00565 preprint) — [deep dive](deep-dives/2021_Iqbal_Amjad_Tahir_Mehmood_CURE_Urdu_IR_Test_Collection.md) | 2021 | B (conditional; preprint text) | MEDIUM | Urdu test collection: 50 queries, 1,096 documents pooled from Solr VSM+BM25 top-20 over a 0.5M crawl, binary qrels (793 relevant, kappa ≈ 0.69). VSM/BM25/LM-DS/LM-JMS × baseline/SWR/dictionary lemmatization/inflectional QE: BM25 MAP@50 0.73 → 0.75, lemma +0.01–0.02 for all models over SWR alone, QE adds ~0; no significance tests; lemma touched 24/50 queries. Lexical-only pool (unsuitable for lexical–dense unique-hit analysis without new judgments). No dense, no fusion, no overlap analysis. Shared benchmark of CR000935 and HYB-010; CURE numbers not reconcilable across papers (BM25 MAP 0.73 here vs 0.26 in CR000935). Text–table inconsistencies. |
