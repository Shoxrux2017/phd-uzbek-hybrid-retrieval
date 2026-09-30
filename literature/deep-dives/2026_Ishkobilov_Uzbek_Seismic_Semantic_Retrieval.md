# Ishkobilov, Meyliev, Ortikov, Ibragimov, Turaeva & Jumaev (2026): Semantic Retrieval of Uzbek Seismic Safety Regulations

**Targeted deep-dive status:** COMPLETED (AI-assisted, pending researcher review)
**Completed:** 2026-09-28
**Literature ID:** `UZ-IR-001` (existing ID kept; section G. Uzbek retrieval / hybrid / RAG)
**Revision history:**
- 2026-09-14: first card, written from the publisher abstract and the project record only.
- 2026-09-28: upgraded to a full-text deep dive. All 5 pages were read, and every claim of the earlier card was confirmed or corrected (§0).
**Systematic-review record:** `CR000481`. Full-text triage: include (triage summary: «включить»), reading priority HIGH, tier 1 («прямо по теме пробела»), `carries_complementarity_evidence = NO`.
**Provenance:** AI-assisted deep dive (Claude). The whole paper was read: the pdftotext text plus page images of all 5 pages (pp. 227–231). Table 1 (p. 229), Table 2 (p. 229) and Fig. 1 (p. 228) were also checked on zoomed page crops. Every number below comes with its table/section and printed page. Numbers computed by us are marked **[computed]**. Bibliographic details not printed in the paper are marked "(bibliographic check: …)".
**Source rule:** **the paper is the primary and only authoritative source.** Web look-ups were used only to check the bibliographic record: Crossref and the publisher's journal page. No repository, later paper or background knowledge is used as evidence about what the authors did.
**Verification:** independent AI verifier pass 2026-09-28; 6 findings addressed.
**Reliability:** **B**.
- The paper appears in a verified proceedings volume with a DOI and a stated editor-run peer review (bibliographic check: Crossref; extrica.com journal page).
- It is not an IR venue, and the full text is methodologically thin. The relevance-judgment protocol, the FastText model and the preprocessing are all unreported, and the reported P@5 values cannot be produced by standard P@5 over 100 queries (§9).
- It is good evidence that an Uzbek paragraph-retrieval experiment exists, and weak evidence for the size of any effect.

---

## Кратко для исследователя (RU)

- **Что сделано.** Корпус узбекских нормативных и технических документов по сейсмобезопасности: 120 документов, 8 450 абзацев, 777 400 токенов, словарь 18 000 (Table 1, p. 229). Корпус разбит на абзацы. Сравниваются две модели поиска абзацев (Sec. 2.3, p. 229):
  - TF-IDF;
  - FastText (эмбеддинги «with subword information»). Вектор абзаца = среднее арифметическое векторов токенов (Eq. 1), сходство — косинус (только Fig. 1, p. 228).
- **Главные числа** (Table 2, p. 229; 100 запросов):
  - TF-IDF: P@5 0.6017, R@5 0.5418, MAP 0.573, MRR 0.596, F1 0.570;
  - FastText: 0.7444 / 0.6875 / 0.712 / 0.731 / 0.714;
  - парный t-test: t = 15.1372, p < 0.001 (Sec. 3, p. 229).
  - Относительный прирост FastText +22.7…+26.9 % по всем метрикам **[computed]**.
- **Что уточнено против старой карточки:**
  - точные MAP/MRR теперь известны;
  - F1 в статье действительно есть (Sec. 2.4, Table 2), хотя в аннотации не упомянут;
  - числа корпуса (120 / 8 450) подтверждены по Table 1;
  - слово «combines» в аннотации не означает гибрид: модели только «implemented and compared» (Sec. 2.3).
- **Чего нет (измерения пробела):**
  - BM25;
  - стемминг/лемматизация/любые морфологические варианты лексического представления (слова «stem», «lemma» в тексте отсутствуют);
  - современный обученный для поиска dense-ретривер (XLM-R и mBERT названы только как будущая работа);
  - fusion/гибрид;
  - перекрытие, уникально найденные релевантные абзацы, oracle union;
  - анализ по запросам или по признакам запросов.
- **Морфология в работе — только мотивация и свойство плотного канала:** subword-информация внутри FastText. Контролируемого сравнения представлений лексического канала нет. Вывод авторов «subword-представление эффективнее чисто лексического сопоставления» смешивает сразу несколько отличий: разреженное vs плотное, предобученная семантика vs её отсутствие, subword vs целое слово.
- **Разметка релевантности не описана полностью:** кто составлял запросы, кто и как оценивал релевантность (бинарно/градуально), сколько релевантных абзацев на запрос, был ли пулинг, согласие асессоров. Известно лишь, что запросы «derived from seismic engineering and regulatory documentation» (Sec. 2.4). Не указаны также модель FastText (предобученная или обученная на корпусе), размерность, препроцессинг, вариант TF-IDF, письмо (латиница/кириллица), обработка апострофа.
- **Внутреннее несоответствие (наша проверка):** при стандартном бинарном P@5 по 100 запросам среднее должно быть кратно 0.002. 0.6017 и 0.7444 не кратны; ни одно число запросов ≤ 233 не даёт оба значения **[computed]**. Из статьи причину установить нельзя. Мелкое: F1 FastText 0.714, а гармоническое среднее P@5 и R@5 из той же таблицы = 0.715 (для TF-IDF совпадает, 0.570) **[computed]**.
- **t-test:** не сказано, по какой метрике он считался и одно- или двусторонний; поправки на множественные сравнения нет; CI нет.
- **Для нашего gap:** работа подтверждает уже зафиксированную в v0.8 границу «семантический поиск для узбекского существует» и **не затрагивает** ядро v0.8: raw/stem/lemma BM25 × фиксированный D → перекрытие / уникальные попадания → прирост гибрида → признаки запросов. Предложение: gap не менять.
- **Практическая польза:**
  1. Данные доступны «on reasonable request» — можно запросить корпус и разметку для пилота нашего конвейера (если qrels действительно существуют).
  2. Пример того, какие параметры протокола разметки и метрик нам надо обязательно документировать.
  3. Поиск на уровне абзацев применим к длинным документам Национальной библиотеки (инженерный вывод, не результат статьи).

---

## 0. Revision check against the 2026-09-14 abstract-level card

| Claim in the earlier card | Status after full text | Evidence |
|---|---|---|
| Authors: Ishkobilov, Meyliev, Ortikov, Ibragimov, Turaeva, Jumaev | **Confirmed** | p. 227 header; Crossref (bibliographic check) |
| Venue *Vibroengineering Procedia* Vol. 63, pp. 227–231, 2026 | **Confirmed** | page footers pp. 227–231; PDF metadata; Crossref |
| Publication date 2026-07-16 | **Confirmed** | p. 227: "Received 7 March 2026; accepted 11 April 2026; published online 16 July 2026" |
| 77th International Conference on Vibroengineering, Almaty, 11–12 June 2026 | **Confirmed** | p. 227 |
| Publisher Extrica / JVE International | **Confirmed, but not printed in the paper** | Crossref publisher "JVE International Ltd." (bibliographic check) |
| Volume-level peer review; Scopus-indexed venue | **Not in the paper.** Confirmed at venue level only | extrica.com journal page: Proceedings Editor(s) "oversee the peer-review process"; Scopus listed (bibliographic check) |
| Real corpus-level Uzbek retrieval, query → ranked paragraphs, standard IR metrics | **Confirmed**, with a qualifier: the "semantic" channel is mean-pooled static FastText vectors with cosine, not a retrieval-trained model | Sec. 2.1, Fig. 1 (p. 228); Sec. 2.3, Eq. 1 (p. 229) |
| No BM25; no raw/stem/lemma; no fusion; no complementarity decomposition | **Confirmed** | whole text; no occurrence of BM25, stem-, lemma-, fusion, hybrid |
| "The two models are compared … not fused" | **Confirmed.** The abstract's "combines … with two retrieval models" is wording about the system, not score fusion | Abstract (p. 227) vs Sec. 2.3 "implemented and compared" and Table 2 (two rows only), p. 229 |
| FastText "uses both word and character-subword information" | **Corrected (attribution).** The paper never mentions character n-grams. It says:<br>• "FastText embeddings with subword information", and "morphologically related forms can share representational components" (Sec. 2.3, citing [3] Mikolov et al. 2013 and [4] Bojanowski et al. 2017);<br>• FastText "incorporates subword information and can preserve semantic similarity across morphologically related forms [4]" (Sec. 1).<br>The "character n-gram" detail is context, not a statement of the paper | Sec. 1, p. 227; Sec. 2.3, p. 229 |
| 120 documents, 8,450 paragraphs, 100 queries | **Confirmed.** Added: 777,400 tokens, vocabulary 18,000 | Table 1 (p. 229); Sec. 2.4 (p. 229) |
| Query creation / relevance-judgment details "need full text" | **Resolved as NOT_REPORTED.** The full text also does not give them; only "derived from seismic engineering and regulatory documentation" | Sec. 2.4, p. 229 |
| No modern retrieval-trained dense model, no learned sparse, no hybrid baseline | **Confirmed.** XLM-R and mBERT appear only as future work | Sec. 3 and Sec. 4, p. 230 |
| F1 listed in RESEARCH_MAP, "check against full paper" | **Confirmed:** F1 = 0.570 (TF-IDF), 0.714 (FastText). The abstract omits F1 and its definition is NOT_REPORTED | Sec. 2.4, Table 2 (p. 229); Sec. 4 (p. 230) |
| P@5 0.6017 → 0.7444; R@5 0.5418 → 0.6875 | **Confirmed** (the abstract and Table 2 agree). **New caveat:** the P@5 values are not attainable with standard binary P@5 over 100 queries | Table 2, p. 229; §9 |
| MAP / MRR values "not recovered" | **Resolved:** MAP 0.573 → 0.712, MRR 0.596 → 0.731 | Table 2, p. 229 |
| Paired t-test t = 15.1372, p < 0.001 | **Confirmed.** The tested quantity, sidedness, assumption checks and multiplicity correction are **NOT_REPORTED** (not merely "unclear from the abstract") | Sec. 3, p. 229; Sec. 4, p. 230 |
| Reliability B | **Kept (B)**, with the reasons in the header | — |
| Priority CRITICAL (national boundary) | **Kept as a boundary role.** It is weak as quantitative or methodological evidence. The final priority is the researcher's decision | §13–§14 |
| Section 18 "National Library" design lesson | **Kept, moved to §17**, where it is labelled as our engineering inference | — |
| Open questions 1–10 | Q2, Q6, Q7, Q9 resolved. Q1 partly resolved. Q3, Q4, Q5, Q8, Q10 remain NOT_REPORTED | §19 |

## 1. Bibliographic record

- **Authors:** Farrukh Ishkobilov, Abdulatif Meyliev (corresponding author), Mironshoh Ortikov, Javlon Ibragimov, Umida Turaeva, Elmurod Jumaev
- **Affiliation (as printed):** University of Information Technologies and Management, Karshi, Uzbekistan (p. 227)
- **Title:** *Semantic retrieval of Uzbek seismic safety regulations*
- **Year:** 2026 (received 7 March, accepted 11 April, published online 16 July 2026; p. 227)
- **Venue:** *Vibroengineering Procedia*, Vol. 63, pp. 227–231; 77th International Conference on Vibroengineering, Almaty, Kazakhstan, 11–12 June 2026 (p. 227)
- **ISSN:** print 2345-0533, online 2538-8479 (page footers)
- **Publisher:** JVE International Ltd. (bibliographic check: Crossref; not printed in the paper)
- **DOI:** `10.21595/vp.2026.26510` (p. 227; confirmed by Crossref)
- **License:** CC BY (p. 227)
- **Funding:** "The authors have not disclosed any funding" (p. 230)
- **Data availability:** "available from the corresponding author on reasonable request" (p. 230)
- **Source type:** conference-proceedings article (Crossref type: journal article). The venue page states editor-run peer review and Scopus/EI Compendex indexing (bibliographic check: extrica.com).
- **Reliability:** B
- **Full text available:** yes (`07_full_text/pdfs/CR000481.pdf`, 5 pages)

## 2. Why this work matters to the PhD

It is the only **full-text-verified** Uzbek work in our index where a **ranked retrieval experiment over a real Uzbek corpus** is evaluated with standard IR metrics (P@k, Recall@k, MAP, MRR) and a paired significance test. This is a project-index statement, not a claim of the paper. Urinov (UZ-IR-003) reports a BM25-like vs vector comparison, but it is verified only at abstract level. It therefore closes any claim that Uzbek retrieval evaluation, or "semantic" retrieval for Uzbek, is absent.

| Axis | Relation |
|---|---|
| Lexical retrieval | TF-IDF only. The variant, tokenization and normalization are unreported; no BM25 |
| Semantic retrieval | FastText static subword embeddings, mean-pooled per paragraph, cosine. Unsupervised, not retrieval-trained |
| Hybrid retrieval | **Absent** |
| Uzbek morphology | Motivation only ("morphologically rich agglutinative language", Sec. 1). Handled implicitly through FastText subwords; no stem/lemma condition |
| Low-resource retrieval | Direct: Uzbek, a specialized domain, a small collection |
| Current gap | Confirms an already-rejected broad claim ("Uzbek semantic retrieval is absent"). No effect on the v0.8 core (§16) |

## 3. Research problem

### Simple explanation

Uzbek words take many suffixes, so the same term appears in many written forms. A keyword method that counts exact words (TF-IDF) may miss a relevant paragraph whose wording differs slightly. The authors ask whether word vectors that know about word pieces (FastText) find the right regulation paragraphs better.

### Formal formulation

The goal is stated as: "to evaluate whether subword-aware semantic representation improves retrieval quality in a domain-specific engineering corpus" (Sec. 1, p. 228).

- **Task:** paragraph-level ad hoc retrieval. Given query `q` and paragraph collection `P` (|P| = 8,450), rank `P` by similarity.
- **Compared systems:** TF-IDF vectors vs mean FastText vectors, each ranked by cosine similarity (Fig. 1, p. 228).

The paper states no explicit research questions or hypotheses.

## 4. Main idea

### Simple explanation

Turn every paragraph and the query into a vector in two ways:
1. **TF-IDF:** a long vector of word weights.
2. **FastText:** the average of the word vectors.

Then rank paragraphs by the angle between the query vector and each paragraph vector (cosine), and compare which method puts relevant paragraphs higher.

### Concrete example

The paper gives no worked example query. **Illustration (ours, not from the paper):**
- A query with *zilzilabardoshlik* ("earthquake resistance") and a paragraph that uses *zilzilabardoshligini* (the same word with added suffixes) share no identical token.
- TF-IDF gives this pair zero overlap on that term.
- FastText vectors of the two forms share subword pieces, so the forms stay close.

This is the mechanism the authors invoke (Sec. 3, p. 229–230): "FastText preserves semantic proximity across related forms through subword modeling".

### Formal method

- **Paragraph vector** (Eq. 1, p. 229): `V_p = (1/n) Σ_{i=1..n} V(w_i)`, where `V(w_i)` is the embedding of the i-th token and `n` is the number of tokens in the paragraph.
- **Query vector:** not stated in the text. Fig. 1 shows the query passing through the same "Vector Representation Layer", so the query is presumably encoded the same way. That is **[inferred from Fig. 1]**.
- **Score:** `cos(q, d)` (Fig. 1, p. 228; not mentioned in the prose).
- **TF-IDF:** "representing paragraphs in a statistical vector space" (Sec. 2.3). The weighting formula and normalization are NOT_REPORTED.

## 5. Architecture / algorithm

From Sec. 2.1 (p. 228) and Fig. 1 (p. 228, checked on the page image):

1. **Document collection:** "Seismic Engineering Documents (PDF/DOCX)" (Fig. 1).
2. **Text cleaning and paragraph segmentation** (Sec. 2.1–2.2). The segmentation rule is NOT_REPORTED.
3. **Query side:** "Query Input • Tokenization • Normalization", then "Preprocessing & Normalization" (Fig. 1). What normalization means is **NOT_REPORTED**: lowercasing, script, apostrophes, stop-words and any stemming are all undefined. No stemming or lemmatization is mentioned anywhere.
4. **Vector representation layer:** "TF-IDF Vectorizer" | "FastText Embeddings" (Fig. 1).
   - FastText model source is **NOT_REPORTED**: pre-trained (which one?) or trained on the corpus. Dimension, n-gram range and training parameters are also NOT_REPORTED.
   - The TF-IDF variant (sublinear tf, idf smoothing, vocabulary cut-off) is **NOT_REPORTED**.
5. **Similarity:** cosine `cos(q, d)` (Fig. 1).
6. **Ranking:** "Top-k Ranking • Precision@k Evaluation" (Fig. 1).
7. **Infrastructure:** "Embedding Store", "Django REST API Backend" (Fig. 1). This is a deployment detail and does not affect evaluation.

- Each model is run separately. **No score or rank fusion** (Sec. 2.3: "Two retrieval models were implemented and compared"; Table 2).
- Minor presentation issue: the layer labels in Fig. 1 repeat. (A), (C) and (D) each appear twice, and "Paragraph Index" appears twice. This does not affect the results.

## 6. Data

- **Dataset / corpus:** "compiled from seismic safety regulations, construction compliance documents, seismic risk mitigation guidelines, and related engineering publications" (Sec. 2.2, p. 228). The specific source documents, their publishers and years are NOT_REPORTED.
- **Language:** Uzbek. The script (Latin / Cyrillic / mixed) is NOT_REPORTED, and so is the presence of Russian-language material.
- **Domain:** seismic safety and engineering regulations.
- **Size** (Table 1, p. 229, checked on the image):

| Parameter | Value |
|---|---:|
| Number of documents | 120 |
| Indexed paragraphs | 8,450 |
| Total tokens | 777,400 |
| Vocabulary size | 18,000 |

  **[computed]**: ≈70.4 paragraphs per document, ≈92.0 tokens per paragraph, type/token ratio ≈0.023.
- **Queries:** 100, "domain-specific queries derived from seismic engineering and regulatory documentation" (Sec. 2.4, p. 229). Who wrote them, whether they were taken from the indexed paragraphs themselves, their length and language form are **NOT_REPORTED**. The query set is not published.
- **Relevance judgments:** **NOT_REPORTED** in full. The paper does not report:
  - who judged relevance;
  - whether judgments were binary or graded;
  - the number of relevant paragraphs per query;
  - pooling, agreement or adjudication.
  The only hint is the future-work phrase "improving annotation robustness" (Sec. 4, p. 230), which implies that some annotation existed.
  - Rough indication **[computed, approximate]**: P@5·5 / R@5 ≈ 5.55 (TF-IDF) and 5.41 (FastText). Per query, #relevant = 5·P@5/R@5 holds when 5 results are returned and R@5's denominator is the total number of relevant paragraphs. The aggregates therefore suggest roughly 5–6 relevant paragraphs per query on average. The estimate is approximate because a mean of ratios is not a ratio of means, and it relies on the P@5 values that are themselves questionable (§9).
- **Train / dev / test:** no split is described. No tuning is reported.
- **Availability:** on request from the corresponding author (p. 230).

## 7. Baselines

| Baseline | What it is | Why selected | Fair comparison? |
|---|---|---|---|
| TF-IDF | Sparse term-weighting vector space + cosine. No citation is given where TF-IDF is defined (Sec. 2.3); Salton & Buckley [1] and Manning et al. [2] are cited only for classical/sparse retrieval generally (Sec. 1, p. 227; Sec. 3, p. 230) | "classical" baseline (Sec. 2.3) | **Weak baseline.** No BM25, no reported tuning, no morphological normalization reported. Fig. 1's "Normalization" is undefined |
| FastText (proposed) | Static subword word vectors, mean-pooled | Suited to agglutinative languages (Sec. 1, 2.3) | Only two systems. There is no word-level embedding control (e.g. Word2Vec without subwords) and no stemmed or lemmatized TF-IDF, so the "subword" effect is not isolated |

There is no modern dense retriever, cross-encoder or learned sparse model. XLM-R and mBERT are mentioned only as future work (Sec. 4, p. 230).

## 8. Metrics

| Metric | Definition (context, not from the paper — the paper gives no formulas) | Simple meaning | Remark for this paper |
|---|---|---|---|
| Precision@5 | share of relevant items among the top 5, averaged over queries | "How many of the first five paragraphs are right?" | With binary relevance and 100 queries, the mean must be a multiple of 0.002; the reported values are not (§9) |
| Recall@5 | relevant items in the top 5 / all relevant items for the query | "What share of all relevant paragraphs is already in the top 5?" | Depends on the unreported number of relevant paragraphs per query |
| MAP | mean over queries of average precision across the ranking | Rewards putting all relevant paragraphs high | Cut-off depth NOT_REPORTED |
| MRR | mean of 1/rank of the first relevant item | "How high is the first correct paragraph?" | Cut-off NOT_REPORTED |
| F1-score | harmonic mean of precision and recall | Balance of P and R | Definition NOT_REPORTED. The values match the harmonic mean of the aggregate P@5 and R@5 within 0.001 (§9) |

Significance: a paired t-test on the 100 queries (Sec. 2.4, Sec. 3). Details are in §10.

## 9. Results

### Table 2: TF-IDF vs FastText, 100 queries (p. 229; checked on the zoomed image)

| Model | P@5 | R@5 | MAP | MRR | F1 |
|---|---:|---:|---:|---:|---:|
| TF-IDF | 0.6017 | 0.5418 | 0.573 | 0.596 | 0.570 |
| FastText | **0.7444** | **0.6875** | **0.712** | **0.731** | **0.714** |
| Δ absolute **[computed]** | +0.1427 | +0.1457 | +0.139 | +0.135 | +0.144 |
| Δ relative **[computed]** | +23.7% | +26.9% | +24.3% | +22.7% | +25.3% |

- The P@5 and R@5 values in the abstract (p. 227) equal Table 2.
- The text states "Precision@5 increased from 0.6017 to 0.7444, while Recall@5 improved from 0.5418 to 0.6875. Similar gains were observed for MAP and MRR" (Sec. 3, p. 229). Consistent with the table.
- The authors report no relative percentages, so there is nothing to recompute.

### Internal consistency checks [computed]

1. **P@5 granularity (internal inconsistency).**
   - With binary relevance, exactly 5 results per query and 100 queries, mean P@5 = (total relevant hits in all top-5 lists) / 500. It must therefore be a multiple of 0.002.
   - The reported values are 0.6017 (= 300.85/500) and 0.7444 (= 372.2/500). Neither is an integer count.
   - No query count from 1 to 233 yields both values as standard P@5 means (checked with Python).
   - Possible explanations: a different query count, fewer than 5 results for some queries, graded relevance, or another averaging scheme. **The paper allows none of these to be confirmed.** We report the inconsistency and do not resolve it.
2. **F1.**
   - The harmonic mean of the aggregate P@5 and R@5 is 0.5702 for TF-IDF (reported 0.570 ✓) and 0.7148 for FastText (reported 0.714; rounding would give 0.715).
   - The difference is tiny. It suggests F1 ≈ F1@5 computed from the aggregate P and R, or per-query F1 averaged. The definition is NOT_REPORTED.
3. **MRR vs P@5 (observation, not an inconsistency).**
   - MRR ≈ P@5 (0.596 vs 0.602 for TF-IDF). On average about 3 of the top 5 are relevant, yet the mean reciprocal rank of the first relevant result is only ≈0.6.
   - That is possible only if per-query outcomes are uneven (many queries with no relevant paragraph near the top, others with many), or if relevant paragraphs tend to sit below rank 1.
   - Per-query data are not reported, so this cannot be checked.

## 10. Statistical evidence

- **Significance test:** paired t-test over the 100 queries: "t = 15.1372 and p < 0.001" (Sec. 3, p. 229; repeated in the Abstract and Sec. 4).
  - **Which metric's per-query values were tested: NOT_REPORTED.** A single t is given for "the observed improvement".
  - One- or two-sided: NOT_REPORTED.
  - Normality or other assumption checks: NOT_REPORTED.
  - Correction for testing several metrics: none reported. Only one test is reported.
  - **[computed]** With n = 100 (df = 99), t = 15.14 corresponds to a standardized paired effect d_z = t/√n ≈ 1.51, i.e. a very consistent per-query advantage. If the tested metric was P@5, the implied SD of per-query differences would be ≈0.094. This is illustrative only, since the metric is unknown.
- **Confidence intervals:** NOT_REPORTED.
- **Runs / seeds:** NOT_REPORTED. TF-IDF is deterministic; FastText training (if any) has seed variance that is not reported.
- **Ablation:** none. There is no word-level vs subword embedding control and no preprocessing variants.
- **Per-query analysis:** none. The paper has:
  - no per-query win/loss;
  - no breakdown by query type;
  - no overlap between the TF-IDF and FastText result sets;
  - no unique relevant hits;
  - no oracle union.

## 11. Strengths

- A real Uzbek **corpus-level ranking experiment** with 100 queries, not word/sentence similarity (Sec. 2.4, Table 2).
- A domain of practical value: normative/regulatory paragraphs, where the unit of retrieval is a coherent clause (Sec. 2.2).
- Five standard metrics are reported for both systems, plus a paired significance test on the same query set (Sec. 2.4).
- Corpus statistics are given (Table 1).
- The morphological motivation is explicit and relevant to Uzbek (Sec. 1).
- The data are declared available on request (p. 230).

## 12. Limitations

### Stated by the authors

- The paper has no dedicated limitations section. The only author statement pointing at open work is the future-work sentence: "Future work should focus on expanding the corpus, improving annotation robustness, and integrating contextual multilingual models such as XLM-R and mBERT" (Sec. 4, p. 230). The authors do not call the corpus small or the annotation limited.

### Inferred from the experimental design

0. **Our reading of the future-work sentence** (not stated by the authors): it suggests that the authors see the corpus size and the annotation as improvable, and it confirms that no contextual model was tested.

1. **Relevance judgments are completely undocumented.** The results cannot be interpreted for reliability or bias, or reproduced, without the qrels protocol.
2. **Queries were "derived from" the documentation.** If they were built from indexed paragraphs, their wording may share vocabulary with their target paragraphs. The direction of the bias is unknown: it could favour TF-IDF, or FastText if the queries were paraphrased.
3. **Confounded comparison.** TF-IDF and FastText differ at once in:
   - sparse vs dense representation;
   - pre-learned distributional semantics vs none;
   - subword vs whole-word units.
   The conclusion that "subword-based semantic representation is more effective than purely lexical matching" (Sec. 3, p. 229) cannot attribute the gain to subwords or to morphology specifically.
4. **The lexical baseline is weak and unspecified.** It is TF-IDF, not BM25. Normalization is undefined, and there is no stemmed or lemmatized variant. The lexical channel's morphological representation is therefore unknown, not "raw" by design.
5. **FastText is unspecified:** source, training data and dimension are unknown. The mean-pooled static vectors are unsupervised and are not a modern retrieval-trained dense retriever.
6. **The P@5 values are inconsistent** with standard P@5 over 100 queries (§9). There is also the minor F1 rounding mismatch.
7. **The significance test is under-specified:** metric unknown, no CI, no multiplicity handling (§10).
8. **Single small domain:** 120 documents from one engineering area. Generalization to other genres (library books, journals) is untested.
9. **Vocabulary size.** A vocabulary of 18,000 for 777,400 tokens of agglutinative text (type/token ratio ≈0.023 **[computed]**) is a round figure. It may reflect a frequency cut-off or normalization, but the paper does not say. If a cut-off exists, it defines what TF-IDF can match.
10. **Only one cut-off (k = 5)** is reported for precision and recall. There is no deep-recall view (e.g. R@100) of the kind relevant to candidate generation for hybrids.

## 13. What the work proves

- On the authors' Uzbek seismic-regulation paragraph collection (8,450 paragraphs, 100 queries), mean-pooled FastText vectors with cosine ranking scored higher than a TF-IDF baseline on all five reported metrics: P@5 0.7444 vs 0.6017, MAP 0.712 vs 0.573, MRR 0.731 vs 0.596 (Table 2, p. 229). The authors report the difference as significant (paired t = 15.1372, p < 0.001).
- Uzbek paragraph-level retrieval **has been built and evaluated with standard IR metrics** in a peer-reviewed venue. Peer review is confirmed at venue level only (bibliographic check: extrica.com); the paper itself shows only received/accepted dates (p. 227). This is the boundary fact the project uses.
- Qualifier: because the qrels protocol is absent and the P@5 values are inconsistent, the **size** of the reported advantage should be cited with caution. The **direction** is supported by every metric and by the reported test.

## 14. What the work does NOT prove

- **That subword modelling (or handling morphology) is what causes the gain.** There is no word-level embedding control and no stemmed/lemmatized lexical control. The comparison bundles sparse→dense, no-semantics→distributional semantics and word→subword.
- **Anything about morphological representation of the lexical channel.** There are no raw/stem/lemma variants, and the TF-IDF normalization is undefined.
- **That FastText beats BM25**, or that it beats modern retrieval-trained dense retrievers (E5, BGE-M3, etc.). Neither was tested.
- **That lexical and semantic retrieval are complementary here, or that a hybrid would help.** There is no fusion, no overlap, no unique-hit and no oracle-union analysis.
- **Which queries each method wins on, or why.** There is no per-query or query-feature analysis.
- **That the reported numbers are reproducible.** Queries, qrels and model details are unpublished (data on request only), and the P@5 values are internally inconsistent.
- **Generalization** beyond seismic/engineering regulations (e.g. to National Library collections).

## 15. Relationship to current Uzbek evidence

- **National progression** (from our knowledge base, not from this paper):
  - **Bakaev** (MORPH-UZ-002, PHD-UZ-001) and **Xusainova** (MORPH-UZ-004, PHD-UZ-003) establish Uzbek morphological processing: stemming, lemmatization and search infrastructure. They have no qrels-based IR evaluation.
  - **Ishkobilov et al.** establish a qrels-style ranked evaluation for Uzbek, but with no morphological variants of the lexical channel.
  - The two halves (Uzbek morphology tools; Uzbek ranked retrieval evaluation) therefore exist **in separate works**. No national work joins them in one controlled experiment.
- **Urinov** (UZ-IR-003, C) is another BM25-like vs vector comparison, verified only at abstract level. Ishkobilov remains the better-documented Uzbek ranked-retrieval evaluation, though its qrels protocol is also missing.
- **USHRA / O-RAG** (UZ-HYB-001/002) are hybrid/RAG systems evaluated by answer or citation accuracy. Ishkobilov evaluates ranking directly, but without a hybrid.
- **Sharifbaev** (manuscript, D) describes lemmatized BM25 + LaBSE + adaptive selection. If verified, it goes further than Ishkobilov on components, but it too lacks a raw/stem/lemma × fixed-D decomposition.
- **UZ-SEM-001** (Mansurov & Mansurov, Uzbek FastText vectors) is a possible source of Uzbek FastText vectors. **The paper does not say which FastText model was used**, so no link can be asserted.
- **International analogue:** UPERF (MORPH-003, Urdu) already includes TF-IDF and FastText **with raw/stemmed/lemmatized preprocessing**. It is a strictly richer design than Ishkobilov on the morphology axis.

## 16. Relationship to CURRENT_GAP

**Classification:** *supports* the existing boundary + *no material effect* on the residual core.

- **Supports / confirms as occupied:**
  - "Uzbek semantic retrieval is absent" is already REJECTED in v0.8 and GAP_BOUNDARY §4, and this paper is one of the reasons.
  - The full text strengthens that status: the metrics are now fully verified.
  - It also clarifies the content: "semantic" here means static FastText mean vectors, not a retrieval-trained dense model.
- **v0.8 elements touched:** only the context "Uzbek semantic retrieval exists" and, in spirit, the motivation that surface-form variation hurts lexical matching in Uzbek. The paper asserts this; it does not test it in a controlled way.
- **v0.8 elements NOT touched:**
  - BM25_raw / BM25_stem / BM25_lemma;
  - a fixed modern dense comparator D;
  - H_raw / H_stem / H_lemma fusion;
  - lexical-only and dense-only relevant hits, overlap and oracle union;
  - incremental hybrid gain;
  - per-query statistics;
  - relation to Uzbek query features (morphological, script/apostrophe, lexical overlap).
  None is present.
- The "What can still kill this gap" criteria 1–2 are **not met**.

**Proposal:** keep v0.8 refined unchanged. Update GAP_BOUNDARY §2.8 and the MASTER_INDEX row from "verified abstract" to "full text read" (row in §20). This is a proposal only; `CURRENT_GAP.md` and `GAP_BOUNDARY` have not been edited.

## 17. Implications for our research design

- **Baselines.**
  - This paper confirms the need for BM25 with explicit configuration, not TF-IDF, as the lexical reference.
  - A mean-pooled FastText model could serve as an **optional secondary control**. It would separate "static subword similarity" from a retrieval-trained D, but it must not replace D.
- **Lexical representation must be fully specified.** Fig. 1's undefined "Normalization" is the kind of ambiguity our design must avoid. For every condition, record:
  - tokenizer;
  - script handling (Latin/Cyrillic);
  - apostrophe variants (o‘/g‘);
  - lowercasing;
  - stop-words;
  - stemmer/lemmatizer (none / which);
  - vocabulary cut-offs;
  - k1 and b.
- **Qrels protocol.** This paper shows the national reporting gap concretely. Our benchmark must state:
  - query source and whether queries were derived from indexed text;
  - assessor count and expertise;
  - relevance scale;
  - pooling depth and systems;
  - agreement and adjudication;
  - the number of relevant items per query.
  Documenting these is itself a contribution relative to the national baseline.
- **Query taxonomy.** Record **query origin**: written independently vs derived from a target paragraph. Also record query–target lexical overlap as a feature, since derivation from documentation can bias lexical vs semantic comparisons.
- **Metrics and statistics.**
  - Report metric definitions and cut-offs (trec_eval conventions).
  - Keep per-query run files.
  - Name the metric used in each paired test.
  - Use paired randomization or bootstrap tests with multiplicity control (e.g. Holm).
  - Report CIs.
  - Sanity-check aggregate values against their possible granularity (the P@5 check in §9 is cheap and catches errors).
  - Add a deep recall cut-off (R@100) for candidate coverage.
- **Passage/paragraph indexing** (engineering inference, not a result of this paper): long National Library items (books, journals) could be indexed as paragraphs or passages, with results aggregated back to the parent document and the matching fragment shown to the user. Whether to evaluate at paragraph or document level must be decided before building qrels.
- **Possible data source.** The corpus is "available … on reasonable request" (p. 230). Requesting it, together with the queries and qrels if they exist, would allow a cheap pilot of our BM25_raw/stem/lemma × D overlap/unique-hit pipeline on existing Uzbek data. Its value depends on the undisclosed qrels quality.
- **Hypothesis.** The paper gives no evidence for or against morphology-induced complementarity change. It shows only that on this collection a dense semantic channel beat an unspecified lexical channel on average. That is the setting in which our question (does a stemmed or lemmatized lexical channel change which relevant items only it finds?) remains open.

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| TF-IDF | Weights a word higher if it is frequent in this paragraph but rare in the collection | `tf(t,d)·idf(t)`, vector-space model with cosine ranking |
| BM25 | A refined word-matching score with saturation of repeats and length normalization (not used in this paper) | Probabilistic relevance framework, parameters k1, b |
| FastText | Word vectors where each word is built from its pieces, so rare or inflected forms still get sensible vectors | Word embedding = sum of subword (character n-gram) vectors (Context, from Bojanowski et al. 2017; the paper says only "subword information") |
| Mean pooling | Represent a paragraph by the average of its word vectors | `V_p = (1/n) Σ V(w_i)` (Eq. 1) |
| Cosine similarity | How similar the directions of two vectors are | `q·d / (‖q‖‖d‖)` |
| Retrieval-trained dense retriever | A neural encoder trained specifically so that queries land near their relevant documents (not this paper) | Bi-encoder with contrastive training on query–document pairs |
| Paragraph-level retrieval | Returning paragraphs instead of whole documents | Retrieval unit = paragraph |
| P@5 / R@5 | Share of the top 5 that are relevant / share of all relevant items found in the top 5 | See §8 |
| MAP / MRR | Quality of the whole ranking / position of the first relevant hit | See §8 |
| Paired t-test | Checks whether per-query score differences between two systems are reliably non-zero | Test on per-query differences, df = n − 1 |
| Qrels | The list of which documents are relevant to which query | Relevance judgments |
| Complementarity (project term) | Each channel finds some relevant items the other misses | Unique relevant hits, overlap, oracle union |

## 19. Open questions / verification needed

Only the authors can answer the first eight.

1. **Qrels protocol:** assessors, scale, pooling, agreement, number of relevant paragraphs per query. **NOT_REPORTED.**
2. **Query construction:** who wrote the queries; were they derived from indexed paragraphs; length and form. **NOT_REPORTED** beyond "derived from seismic engineering and regulatory documentation".
3. **FastText model:** pre-trained (which model?) or corpus-trained; dimension; n-gram range. **NOT_REPORTED.**
4. **TF-IDF configuration and "Normalization"** (Fig. 1): tokenizer, script, apostrophes, stop-words, any stemming, vocabulary cut-off (is 18,000 a cap?). **NOT_REPORTED.**
5. **P@5 computation:** why are 0.6017 and 0.7444 not multiples of 0.002? Was the query count different from 100, were some result lists shorter than 5, or was relevance graded?
6. **The t-test:** which metric, and one- or two-sided?
7. **F1 definition**, and the cut-off depth for MAP/MRR.
8. **The specific source documents** of the 120 (Sec. 2.2 gives only the categories), and their script and language mix.
9. **Data request:** worth asking the corresponding author for corpus + queries + qrels (see §17)? This is the researcher's decision.

Resolved from the earlier card's list:
- corpus counts (Table 1);
- paragraph vector (Eq. 1);
- similarity function (cosine, Fig. 1);
- exact MAP/MRR/F1 values (Table 2);
- corpus composition by category (Sec. 2.2).

## 20. Decision after deep dive

- **Keep current gap?** Yes. v0.8 refined remains valid (§16).
- **Modify gap?** No. Proposed wording update in `GAP_BOUNDARY` §2.8 (researcher's decision):
  - "verified-abstract" → "full text read 2026-09-28";
  - add MAP 0.573→0.712, MRR 0.596→0.731, F1 0.570→0.714;
  - add: qrels protocol, FastText model and preprocessing NOT_REPORTED; P@5 granularity inconsistency.
- **Add decision?** Proposed for `decisions/DECISIONS.md` (researcher's decision): "Every reported metric must state its definition and cut-off; every paired test must name the metric and sidedness; per-query run files are kept." This directly addresses the reporting gaps seen here.
- **Add experiment?** Optional: request the Ishkobilov corpus/queries/qrels and, if the qrels are usable, run a small pilot of BM25_raw/stem/lemma × D with overlap/unique-hit measurement on it.
- **Add citation to Chapter I?** Yes:
  - §1.2 (national semantic retrieval: static subword embeddings in Uzbek ranked retrieval);
  - §1.3 / national synthesis (Uzbek retrieval evaluated as lexical *vs* semantic, without morphological variants of the lexical channel, without hybrid, and without complementarity analysis).
  - Cite the numbers with the qrels and P@5 caveats.
- **Proposed updated `MASTER_INDEX.md` row** (to replace the current UZ-IR-001 row after approval):

| UZ-IR-001 | Ishkobilov et al. — *Semantic Retrieval of Uzbek Seismic Safety Regulations* (*Vibroengineering Procedia* 63, 227–231) — [deep dive](deep-dives/2026_Ishkobilov_Uzbek_Seismic_Semantic_Retrieval.md) | 2026 | B | CRITICAL | Full text read 2026-09-28. 120 docs / 8,450 paragraphs / 100 queries; TF-IDF vs mean-pooled FastText (cosine). TF-IDF P@5/R@5/MAP/MRR/F1 = 0.6017/0.5418/0.573/0.596/0.570; FastText = 0.7444/0.6875/0.712/0.731/0.714; paired t=15.1372, p<0.001 (metric not stated). Qrels protocol, FastText model and preprocessing NOT_REPORTED; P@5 values not attainable with standard P@5 over 100 queries. No BM25, no stem/lemma variants, no fusion, no overlap/unique-hit or per-query analysis. |
