# Paik, Parui, Pal & Robertson (2013): Effective and Robust Query-Based Stemming

**Targeted deep-dive status:** COMPLETED (AI-assisted, pending researcher review)
**Completed:** 2026-09-28
**Literature ID:** `MORPH-034` (assigned 2026-09-28, approved by researcher)
**Systematic-review record:** `CR000566`. Full-text triage: INCLUDE, reading priority HIGH, reading tier "2 — важно", `carries_complementarity_evidence = YES`. We qualify that flag (§10, §16). The "robustness index" (RI) is a **net** count: queries helped by a stemmer minus queries hurt, relative to no stemming, with both runs lexical. The separate helped and hurt counts are not reported, and there is no relevant-set overlap evidence.
**Provenance:** AI-assisted deep dive (Claude). The paper (29 pages, printed pp. 18:1–18:29 = PDF pp. 1–29) was read in full from the pdftotext extraction. Page images were checked for every table and figure whose numbers are reported here: pp. 18:12 (Fig. 2 and the `#wsyn` example), 18:14 (Table I), 18:16 (Figs. 3–4), 18:17–18:24 (Tables III–XII, Fig. 5), 18:26–18:28 (Tables XIII–XVI). Tables XIII and XIV were also checked on 250-dpi crops to read the significance superscripts and subscripts. Page references below are the printed article pages "18:N". Numbers computed by us are marked **[computed]** and were recomputed with Python. Values read from bar charts are marked **[approximate]**.
**Source rule:** **the paper is the primary and only authoritative source.** No code, website, later paper or background knowledge is used as evidence about what the authors did. The bibliographic record was checked against the IR Anthology record (authors, TOIS 31(4), pp. 18:1–18:29, 2013, DOI `10.1145/2536736.2536738`), and a web search returned the ACM DL landing page for the same DOI (bibliographic check: ir.webis.de IR Anthology; ACM DL search result). Crossref was not reachable (proxy HTTP 403).
**Reliability:** **A** (peer-reviewed journal article, *ACM Transactions on Information Systems*).
**Verification:** independent AI verifier pass 2026-09-28; 11 findings addressed.

---

## Кратко для исследователя (RU)

- **Что сделано.** Предложены корпусные полностью автоматические стеммеры, у которых морфологические варианты слова **взвешиваются в зависимости от запроса**. Вес зависит от того, насколько вариант совместно встречается (co-occurrence) с остальными словами запроса («тематическая согласованность»). Три метода:
  - QIS: запросонезависимая группировка вариантов по общему префиксу, общим «остаткам»-суффиксам и совместной встречаемости;
  - QBS-WMA и QBS-ART: запросозависимое взвешивание вариантов оператором Indri `#wsyn`.
- **Постановка.** Только лексический поиск: Indri, языковая модель с дирихле-сглаживанием (μ = 1000), **не BM25** (Sec. 4.2, p. 18:14).
  - Данные: 12 наборов тем TREC на 6 коллекциях (новости TIPSTER/TREC disks, ROBUST, веб-коллекция GOV2 с ≈25 млн документов) и три неанглийские коллекции: маратхи и бенгальский (FIRE), чешский (CLEF).
  - Сравнение: без стемминга (NO), Porter / языковой rule-based стеммер (RBS), XU, SNS, GRAS.
- **Главные числа (MAP; NPMI-вариант QBS-ART):**
  - TREC 1–3: 0.192 → 0.249 (+29.7%), лучший базовый стеммер SNS 0.229 (Table III, p. 18:17);
  - TREC 6–8: 0.183 → 0.242 (Table VI, p. 18:20);
  - ROBUST: 0.268 → 0.313, базовые стеммеры лишь 0.280–0.283 (Table VII, p. 18:21);
  - GOV2: 0.268 → 0.313 (Table VIII, p. 18:22);
  - чешский: 0.214 → 0.318 (RC-вариант QBS-ART: 0.325);
  - маратхи: 0.213 → 0.286;
  - бенгальский: QBS не лучше GRAS/SNS (Tables XIII–XV, pp. 18:26–27).
- **Анализ по запросам есть, но только в агрегированном виде.** RI = (n₊ − n₋)/|Q| относительно NO, запросы с разницей < 5% исключаются (Sec. 5.2, p. 18:20).
  - QBS-ART: RI 0.72 на TREC 1–3 (чистый выигрыш ≈108 из 150 запросов **[computed]**); Porter: 0.28; на ROBUST у всех базовых стеммеров RI ≤ 0.08 (Table IX, p. 18:22).
  - **Отдельные n₊ и n₋ не приводятся.** Посчитать, сколько запросов стемминг ухудшил, нельзя.
- **Нет:** BM25, лемматизации, плотного поиска, гибрида/fusion, перекрытия (overlap) или уникально найденных релевантных документов, oracle union, систематического анализа признаков запросов. Есть только качественный разбор ≈5 запросов (Sec. 5.6, 3.3, 5.4).
- **Главная идея, полезная для нас:** ценность морфологического варианта **зависит от запроса**. Частый вариант уводит запрос от темы (legal в «drug legalization benefits»), а для другого запроса тот же вариант полезен (Sec. 1, 3.3, pp. 18:2, 18:10). Это концептуальная опора для связи «морфологическое представление → эффект по запросам → признаки запроса» в v0.8. Эффекта для гибридного поиска работа не показывает.
- **Внутренние несоответствия в статье:**
  - строка «SNS+QBS» вместо QBS-WMA в Table VII;
  - заявления «>10% / >15% лучше базовых» сходятся с таблицами только как разница процентных приростов над NO, а не как относительный прирост;
  - Table XIII противоречит тексту о значимости QIS на маратхи;
  - «Porter хуже всех по RI во всех коллекциях» не подтверждается Table IX;
  - на чешском QBS-ART по RI хуже GRAS (0.57 vs 0.63), хотя текст говорит обратное;
  - RI для наборов из 50 запросов не согласуется с |Q| = 50 (подробно в §9, §19).
- **Для gap:** поддерживает фон и уточняет дизайн; **ядро v0.8 не затрагивает**. Предложение: gap не менять. Идея «запросозависимый / селективный стемминг» — занятая территория (см. §16).
- **Практически для нас:**
  1. Для BM25_stem и BM25_lemma относительно BM25_raw отчитываться по запросам: helped / hurt / unchanged **раздельно**, с явным порогом и знаменателем. Одного RI недостаточно.
  2. Кандидатные признаки запроса: размер семейства вариантов, частота варианта в коллекции, его совместная встречаемость с другими словами запроса, длина запроса.
  3. Явно фиксировать, где происходит склейка словоформ: в индексе (index-side) или в запросе (query-side, как `#syn`).

---

## 1. Bibliographic record

- **Authors:** Jiaul H. Paik, Swapan K. Parui, Dipasree Pal (Indian Statistical Institute, Kolkata); Stephen E. Robertson (Microsoft Research, Cambridge, UK) (p. 18:1)
- **Year:** 2013 (publication date November 2013; received February 2012, revised January 2013 and March 2013, accepted April 2013; pp. 18:1, 18:29)
- **Venue:** *ACM Transactions on Information Systems* (TOIS), Vol. 31, No. 4, Article 18, 29 pages (p. 18:1)
- **DOI:** `10.1145/2536736.2536738` (printed on p. 18:1; bibliographic check: IR Anthology record)
- **Official URL:** https://dl.acm.org/doi/10.1145/2536736.2536738 (bibliographic check: search result)
- **Source type:** peer-reviewed journal article (ACM TOIS)
- **Reliability:** A
- **Full text available:** yes (`07_full_text/pdfs/CR000566.pdf`, 29 pages, typeset publisher version)

## 2. Why this work matters to the PhD

It is one of the most careful classical studies of **how stemming changes lexical retrieval per query**, rather than only on average. It is also one of the few that treats the usefulness of a morphological variant as **query-dependent**. Coverage: 9 collections, 3 of them non-English collections "for which stemming is known to be beneficial" (Sec. 5.7, p. 18:25). It adds a robustness index next to MAP and runs two significance tests.

| Axis | Relation |
|---|---|
| Lexical retrieval | Central. Indri language model (Dirichlet, μ = 1000). **Not BM25**, despite Robertson being a co-author |
| Lexical representation variants | Central. No stemming vs 4 baseline stemmers (Porter/RBS, XU, SNS, GRAS) vs 3 proposed stemmers (QIS, QBS-WMA, QBS-ART), each proposed stemmer with 2 co-occurrence measures. **No lemmatization**, no n-grams |
| Semantic / dense retrieval | **Absent** |
| Hybrid retrieval | **Absent** (no fusion; QBS is weighted query-side expansion inside one lexical model) |
| Uzbek morphology | Indirect. Suffixing languages (English, Marathi, Bengali, Czech). No Turkic language |
| Low-resource retrieval | Partial. FIRE Marathi/Bengali (2008/2010-era Indian-language IR) |
| Current gap | Supports background: the effect of lexical morphology is query-dependent, and per-query robustness reporting has precedent. No effect on the lexical–dense complementarity core (§16) |

## 3. Research problem

### Simple explanation

Stemming merges word forms (*drug*, *drugs*) so that a query finds documents written with other forms. But merging can hurt. In the query "drug legalization benefits", merging *legalization* with the very common *legal* pulls in many documents about unrelated legal topics. Standard stemmers apply the same merge to every query. The authors ask whether a stemmer can decide, **for each query**, which variants to trust. They also ask whether this makes stemming both better on average and **less likely to hurt individual queries** (robustness).

### Formal formulation

Contributions (p. 18:3):

1. two corpus-based, query-dependent stemming algorithms that use word co-occurrence to decide which variants are useful;
2. a co-occurrence measure based on a randomness model (RC);
3. a fully automatic, query-independent method for forming morphological groups (QIS), usable alone or as input to query-based stemming;
4. experimental comparison with four strong baseline stemmers;
5. robustness evaluation;
6. analysis of the influence of the base stemmer.

The paper identifies three stemming problems (p. 18:2):

- **understemming:** related words are left in separate groups;
- **overstemming:** unrelated words are merged;
- **query-based stemming:** even a linguistically correct merge can hurt a particular query.

Evaluation goals (p. 18:13):

- effectiveness (MAP, GMAP);
- robustness compared with query-independent stemming;
- usefulness of the RC measure;
- QIS as input to the query-based stemmers;
- generalization to non-English collections.

## 4. Main idea

### Simple explanation

1. **Find candidate variants** for each query word from the corpus itself. Candidates are words that share a long enough beginning and differ by endings that recur elsewhere in the corpus as endings. They must also co-occur in the same documents often enough.
2. **Weight each variant for this query.** A variant gets a high weight if it co-occurs with the *other* words of the query, especially rare ones. It also gets weight if it can "stand in" for the query word in documents that lack the original form.
3. **Retrieve with a weighted-synonym query.** The original word gets weight 1.0 and variants get weights between 0 and 1.

### Concrete example (p. 18:12, image-checked)

Input "drug legalization benefits". The QBS-WMA output query:

```
#wsyn(1.0 drug 0.19 drugged 0.15 drugging 0.44 drugs)
#wsyn(1.0 legalization 0.13 legal 0.56 legalize 0.54 legalized 0.40 legalizes 0.60 legalizing 0.27 legally 0.19 legals)
#wsyn(1.0 benefits 0.19 benefit 0.13 benefited 0.18 benefiting)
```

The frequent, topic-diffuse *legal* gets the lowest weight in its class (0.13). *legalizing* and *legalize* get the highest (0.60, 0.56). Contrast (p. 18:10): for "Legality of medically assisted suicide", adding *legal* as a variant of *legality* "increases noticeably" average precision. The paper gives no number for this.

### Formal method

**Co-occurrence measures** (Sec. 3.1, pp. 18:7–8), with document frequencies n₁, n₂, joint count m and collection size N:

- **RC (randomness co-occurrence):** similarity = −log P(df(a,b) = m) under a hypergeometric random-placement model (Eqs. 3–4), approximated with Stirling's formula. Normalized by the maximum possible value at m = min(n₁, n₂) (Eq. 5).
- **NPMI:** PMI(a,b) / (−log₂ P(a,b)) (Eq. 7).

**QIS (query-independent stemming)** (Sec. 3.2, pp. 18:8–10). A pair of words is "weakly related" if:

1. the two words share a common prefix of ≥ 3 letters;
2. each residue (the remaining ending) also occurs as a residue in ≥ 2 word pairs with a common prefix of ≥ 5 letters;
3. NPMI ≥ 0.3.

The class of query word qᵢ is qᵢ plus every weakly related w with S(qᵢ, w) ≥ α, where S is RC or NPMI (Fig. 1). Path length is limited to one, unlike single-link clustering. The class is placed in Indri's `#syn` operator, which sums the tf values of all members.

**QBS-WMA** (Eqs. 8–10, p. 18:11):

`W(t,q) = Σᵢ [idf(qᵢ)/S] · max(npmi(t,qᵢ; qᵢ), 0)`

- npmi is normalized asymmetrically by −log₂ P(qᵢ);
- S = Σ idf(qᵢ);
- original query words get weight 1.0.

**QBS-ART** (Eqs. 11–14, pp. 18:12–13):

`W(v,qᵢ) = λ·AS(v,qᵢ) + (1−λ)·RS(v,qᵢ)`

- AS = NPMI(v, qᵢ) if ≥ α, else 0;
- RS = min(1, RA);
- RA = Σ_{j≠i} idf(q_j)·AS(v,q_j) / Σ_{j≠i} idf(q_j)·AS(qᵢ,q_j).

λ was tuned "by optimizing MAP, following a two fold cross validation approach on TREC 1–50 queries". The paper reports that a good λ lies in [0.6–0.8] and fixes λ = 0.7 (p. 18:13).

## 5. Architecture / algorithm

1. **Corpus statistics.** Document-level df and co-occurrence (P(a,b) = df(a,b)/N, P(a) = df(a)/N; p. 18:12). Window-based co-occurrence is not used.
2. **Candidate pairs:** the prefix / residue / NPMI ≥ 0.3 conditions above. The authors write: "The choice of parameters in these conditions is partly intuition and partly arbitrary" (p. 18:9). Small variations (prefix 2–3; 5–8 in condition 2) gave "small" differences.
3. **Cut-off α.** Plot the distribution of pairwise similarity and take the peak (Figs. 3–4, p. 18:16). Typical values: [0.02–0.05] for RC, [0.2–0.3] for NPMI. The method is unsupervised and chosen per collection (p. 18:16). The authors checked by hand that pairs below the cut-off are mostly unrelated.
   - *Inferred (ours):* under NPMI, condition 3 already requires NPMI ≥ 0.3 ≥ α, so the α filter in QIS appears non-binding for the NPMI variant. The paper does not comment on this.
4. **Base classes.** QIS is used as the base stemmer for both QBS methods in the main tables (p. 18:16). Table XI also tests Porter and GRAS as base stemmers.
5. **Query-dependent weighting.** WMA or ART; ART uses λ = 0.7.
6. **Retrieval.** Indri/Lemur, LM with Dirichlet smoothing μ = 1000. Queries: TREC **title** field, except TREC 4, which uses the description field because those topics have no title (p. 18:14).
   - **How the conflation is applied.** For QIS/QBS it is **query-side**: the `#syn` / `#wsyn` operators over word forms (pp. 18:9, 18:11). How the baseline stemmers were applied (index-side stemming or query-side synonym classes) is **NOT_REPORTED**. Stop-word handling and the indexed document fields are **NOT_REPORTED**.
7. **Meaning of "RC"/"NPMI" for QBS rows** (our reading). The result tables report every proposed stemmer "for each of the two cooccurrence measures" (p. 18:16). For the QBS rows the label most plausibly refers to the measure used to build the QIS base classes: WMA always uses npmi (Eq. 9), and ART's AS always uses NPMI (Eq. 12). The paper does not state this explicitly.

**Limitation stated in the method:** the candidate-pair analysis is "restricted to languages written in an alphabetic form … and may fail in languages where inflections may be generated using prefixes or infixes" (p. 18:8). QBS itself can use any base stemmer (p. 18:12).

## 6. Data

### English (Table I and Sec. 4.1, p. 18:14; image-checked)

| Task | Collection | # docs | Topics | # queries (table captions) |
|---|---|---:|---|---:|
| TREC 1, 2 & 3 | disks 1 & 2 (TIPSTER) | 741,856 | 51–200 | 150 |
| TREC 4 | disks 2 & 3 | 567,529 | 201–250 (description field) | 50 |
| TREC 5 | disks 2 & 4 | 524,929 | 251–300 | 50 |
| TREC 6, 7 & 8 | disks 4 & 5 (minus Congressional Record) | 528,155 | 301–450 | 150 |
| ROBUST | disks 4 & 5 | 528,155 | 601–700 | 100 |
| TERABYTE | GOV2 (.gov web) | 25,205,179 | 701–850 | 150 |

- "Twelve TREC topic sets" (p. 18:14) = TREC 1–8 (8 sets) + ROBUST (1) + Terabyte 2004–2006 (3), grouped into 6 "collections" in the abstract and conclusion **[inferred]**. The paper does not break the 12 down. The Table I ranges total 650 topics (13 × 50), so the count of 12 holds only if ROBUST 601–700 is counted as one set.
- Domain: news and government documents (WSJ, AP, LA Times, FR, FBIS, DOE abstracts), plus .gov web pages.
- Relevance judgments: standard TREC qrels. Pooling and assessor details are not discussed (standard collections).
- **No train/dev/test split** for the main experiments. λ was tuned on TREC topics 1–50 (not among the test topics). α is chosen without relevance data.

### Non-English (Sec. 5.7, p. 18:25)

| Language | Source | # docs | # queries |
|---|---|---:|---:|
| Marathi | FIRE (2008) | 99,362 | 88 |
| Czech | CLEF 2007 | 81,735 | 50 |
| Bengali | FIRE (2010) | 123,047 | 100 |

- Rule-based stemmers (RBS) for these languages are taken from Dolamic & Savoy (2009, 2010).
- The query field and other settings are described only as "similar to that used in the English experiments": **NOT_REPORTED** in detail.

## 7. Baselines

| Baseline | What it is | Why selected (paper) | Fair comparison? |
|---|---|---|---|
| NO | No stemming | Common reference for RI and p-values | Yes. This is our "raw" analogue, but inside an LM, not BM25 |
| PORT (English) / RBS (Marathi, Czech, Bengali) | Rule-based suffix stripping | Represents the rule-based family | Yes. Mode of application (index or query side) NOT_REPORTED |
| XU (Xu & Croft 1998) | Porter classes refined with the em co-occurrence measure and connected components | Older corpus-analysis stemmer | Parameters (k, window) NOT_REPORTED here |
| SNS (Paik et al. 2011b) | Co-occurrence-based "strongest neighbour" stemmer | Recent corpus-analysis stemmer | **Same first author's prior method.** Parameters NOT_REPORTED |
| GRAS (Paik et al. 2011a) | Lexicon-based graph stemmer (suffix-pair graph) | Recent lexicon-analysis stemmer | **Same first author's prior method.** Parameters NOT_REPORTED |
| BEST / wBEST / 2BEST / w2BEST (Table X) | 1 or 2 top-weighted variants per query word, unweighted or weighted | Ablation of weighting vs cut-off | Yes (internal ablation) |

Missing comparators (inferred):

- no lemmatizer;
- no light/inflectional stemmer for English (e.g., S-stemmer or Krovetz, although Krovetz is cited);
- no character n-gram indexing (cited in related work, p. 18:4);
- no other query-expansion method such as pseudo-relevance feedback. QBS adds weighted terms to the query, so PRF would be a natural competitor.

## 8. Metrics

| Metric | Definition | Simple meaning | Appropriate? |
|---|---|---|---|
| MAP | Mean over queries of average precision (primary metric; p. 18:14) | Overall ranking quality with graded attention to all relevant docs | Yes |
| GMAP | Geometric mean of AP | Punishes very poor queries more than MAP; the authors use it for "topics having poor average precision" | Yes, for robustness |
| P@5 | Precision in top 5 | Top-of-list quality | Yes |
| R-Prec | Precision at rank R (R = # relevant) | Recall-balanced precision | Yes |
| Rel.Ret | Number of relevant documents retrieved in the top 1000, summed over queries (p. 18:14) | Aggregate recall at depth 1000 | Yes, but it is a **net total**. It does not show which relevant docs were gained or lost |
| RI | (n₊ − n₋)/\|Q\| vs no stemming; queries with differences < 5% ignored (p. 18:20) | Share of queries helped minus share hurt | Useful but coarse. n₊ and n₋ are not given separately. It is unclear whether "5%" is relative or absolute, and which \|Q\| is used after exclusions (§9) |

## 9. Results

### MAP across all collections (Tables III–VIII, XIII–XV; image-checked)

Relative improvement over NO is shown in parentheses as printed by the authors. Best value in each row is **bold**.

| Collection (p.) | NO | PORT/RBS | XU | SNS | GRAS | QIS RC | WMA RC | ART RC | QIS NPMI | WMA NPMI | ART NPMI |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| TREC 1–3 (18:17) | 0.192 | 0.226 | 0.228 | 0.229 | 0.228 | 0.231 | 0.240 | 0.248 | 0.234 | 0.241 | **0.249** (29.7) |
| TREC 4 (18:18) | 0.178 | 0.199 | 0.204 | 0.206 | 0.199 | 0.200 | 0.211 | **0.212** (19.1) | 0.207 | 0.209 | 0.207 |
| TREC 5 (18:19) | 0.131 | 0.148 | 0.150 | 0.145 | 0.152 | 0.138 | 0.148 | 0.150 | 0.153 | 0.155 | **0.157** (19.8) |
| TREC 6–8 (18:20) | 0.183 | 0.211 | 0.209 | 0.221 | 0.221 | 0.213 | 0.228 | 0.237 | 0.218 | 0.230 | **0.242** (32.2) |
| ROBUST (18:21) | 0.268 | 0.280 | 0.283 | 0.282 | 0.283 | 0.272 | 0.295 ("SNS+QBS", see below) | 0.307 | 0.281 | 0.298 | **0.313** (16.8) |
| TERABYTE (18:22) | 0.268 | 0.281 | 0.291 | 0.284 | 0.282 | 0.286 | 0.310 | 0.309 | 0.284 | 0.311 | **0.313** (16.8) |
| Marathi (18:26) | 0.213 | 0.225 (RBS) | 0.219 | 0.275 | 0.268 | 0.277 | **0.287** (34.7) | 0.285 | 0.276 | 0.282 | 0.286 |
| Czech (18:27) | 0.214 | 0.269 (RBS) | 0.262 | 0.284 | 0.292 | 0.295 | 0.310 | **0.325** (51.9) | 0.295 | 0.307 | 0.318 |
| Bengali (18:27) | 0.263 | 0.319 (RBS) | 0.302 | 0.330 | 0.331 | 0.334 | 0.331 | 0.329 | **0.335** (27.4) | 0.331 | 0.332 |

Significance marks on the proposed methods (Wilcoxon superscript / randomization subscript; n = better than NO, p/r = PORT/RBS, x = XU, s = SNS, g = GRAS; image-checked):

- **TREC 1–3:**
  - QIS: n/n;
  - all four QBS rows: npxsg/npxsg.
- **TREC 4:**
  - WMA and ART with RC: npg/n;
  - all other proposed rows: n/n.
- **TREC 5:** every proposed row except QIS-RC: n/n. QIS-RC: no mark.
- **TREC 6–8:**
  - QIS: n/n;
  - WMA-RC: npx/npx;
  - WMA-NPMI and both ART rows: npxsg/npxsg.
- **ROBUST:**
  - both QIS rows: no mark;
  - all QBS rows (including "SNS+QBS"): npxsg/npxsg.
- **TERABYTE:**
  - QIS: no mark;
  - all QBS rows: npxsg/npxsg.
- **Marathi:**
  - QIS (RC and NPMI): nrxg/nrx;
  - RC WMA and ART: nrxsg/nrxsg;
  - NPMI WMA and ART: nrxg/nrxg.
- **Czech:**
  - QIS-RC: nrx/n;
  - WMA-RC: nrxsg/nrxs;
  - ART-RC: nrxsg/nrxsg;
  - QIS-NPMI: nrx/nrx;
  - WMA-NPMI: nrxs/nrxs;
  - ART-NPMI: nrxsg/nrxsg.
- **Bengali:** all proposed rows: nrx/nrx.
- **Baselines never carry marks.** Significance of the baseline stemmers against NO is therefore not shown in Tables III–VIII or XIII–XV. Paired t-test p-values against NO appear only in Tables IX and XVI.

Reading the table **[computed]**:

- **Gain of QBS-ART (NPMI) over the best baseline stemmer:**
  - TREC 1–3: +8.7% (0.249 vs SNS 0.229);
  - TREC 4: +0.5%;
  - TREC 5: +3.3%;
  - TREC 6–8: +9.5%;
  - ROBUST: +10.6%;
  - TERABYTE: +7.6%;
  - Marathi: +4.0%;
  - Czech: +8.9% (the RC variant gives +11.3%);
  - Bengali: +0.3%.
- **ROBUST is the clearest case of query-dependence.** All baseline stemmers give only +4.5% to +5.6% over NO, while QBS-ART gives +14.6% (RC) and +16.8% (NPMI).
- **The QIS base stemmer alone is sometimes worse than baselines.** Examples: TREC 5 RC 0.138 vs NO 0.131 and GRAS 0.152; ROBUST RC 0.272.
- **Robust GMAP.** QIS-NPMI has GMAP 0.155 vs NO 0.181 (printed −14.4; Table VII). The query-independent co-occurrence stemmer hurts the poorest queries there.
- **Relevant documents retrieved** in the top 1000, QBS-ART NPMI vs NO:
  - TREC 1–3: +3,484 (+22.0%);
  - TREC 6–8: +1,421 (+23.2%);
  - TERABYTE: +1,847 (+11.1%);
  - ROBUST: +270 (+9.7%).
  These are **net** totals, not set differences.

### Other metrics, TREC 1–3 (Table III, p. 18:17)

| Method | MAP | GMAP | P@5 | R-Prec | Rel.Ret |
|---|---:|---:|---:|---:|---:|
| NO | 0.192 | 0.091 | 0.503 | 0.254 | 15,836 |
| PORT | 0.226 | 0.114 | 0.500 | 0.285 | 18,592 |
| SNS (best baseline MAP) | 0.229 | 0.112 | 0.504 | 0.287 | 18,738 |
| QBS-ART RC | 0.248 | 0.132 | 0.545 | 0.304 | 19,252 |
| QBS-ART NPMI | 0.249 | 0.132 | 0.541 | 0.304 | 19,320 |

- Baseline stemmers barely change P@5, which Porter reduces slightly (−0.6%). QBS-ART raises it +8.3% (RC) / +7.6% (NPMI) **[computed ✓ matches printed]**.
- GMAP rises +45.1% **[computed ✓]**.
- Minor in-table issue: the P@5 column bolds 0.541 (NPMI), although the RC row shows the higher 0.545.

### Robustness index and paired t-test p vs NO (Table IX, p. 18:22; Table XVI, p. 18:28; image-checked)

| Stemmer | TREC 1–3 | TREC 4 | TREC 5 | TREC 6–8 | ROBUST | TERABYTE | Marathi | Czech | Bengali |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| PORT / RBS | 0.28 | 0.33 | 0.34 | 0.11 | 0.01 | 0.23 | 0.27 | 0.56 | 0.54 |
| XU | 0.45 | 0.61 | 0.41 | 0.25 | 0.08 | 0.31 | 0.49 | 0.48 | 0.60 |
| SNS | 0.30 | 0.35 | 0.37 | 0.12 | 0.02 | 0.40 | 0.37 | 0.43 | 0.53 |
| GRAS | 0.39 | 0.64 | 0.43 | 0.23 | 0.04 | 0.19 | 0.47 | 0.63 | 0.52 |
| QIS | 0.27 | 0.40 | 0.24 | 0.27 | 0.01 | 0.27 | 0.45 | 0.52 | 0.56 |
| QBS-WMA | 0.64 | **0.67** | 0.54 | 0.58 | 0.30 | 0.53 | **0.61** | **0.66** | **0.67** |
| QBS-ART | **0.72** | 0.66 | **0.58** | **0.68** | **0.41** | **0.68** | 0.59 | 0.57 | 0.64 |

Selected paired t-test p-values vs NO:

- Porter/RBS: TREC 5 0.13, ROBUST 0.09, TERABYTE 0.10, Marathi 0.06;
- QBS-ART: TREC 1–3 3.29×10⁻¹², TREC 5 0.06, ROBUST 2.78×10⁻⁴, TERABYTE 4.37×10⁻¹⁰;
- on ROBUST: SNS 0.04, XU 0.05, GRAS 0.08, QIS 0.21.

Which co-occurrence measure (RC or NPMI) underlies the QIS/QBS rows of Tables IX and XVI is **NOT_REPORTED**.

Reading **[computed]**:

- **Net helped-minus-hurt queries** (RI × |Q|; approximate, assuming the stated |Q| is the denominator, which the next bullet shows is not always so):
  - QBS-ART: 108 of 150 (TREC 1–3), 102 of 150 (TREC 6–8), 41 of 100 (ROBUST), 102 of 150 (TERABYTE);
  - Porter on ROBUST: ≈1 of 100, i.e. helped ≈ hurt. The authors describe this as "nearly half of the queries are hurt" (p. 18:21), which cannot be checked from RI alone.
- **RI does not match |Q| = 50.** For the 50-query sets (TREC 4, TREC 5, Czech), several RI values are odd hundredths: 0.33, 0.61, 0.35, 0.67, 0.41, 0.37, 0.43, 0.63, 0.57. With an integer n₊ − n₋ and |Q| = 50, RI must be a multiple of 0.02. So the denominator actually used (e.g., after excluding < 5% queries or queries without relevant documents) is not the stated |Q|. The paper does not say what it is.

### Ablations (Tables X–XII, pp. 18:23–24; image-checked)

| Table | Comparison | TREC 1–3 | TREC 4 | TREC 5 | TREC 6–8 | ROBUST | TERABYTE |
|---|---|---:|---:|---:|---:|---:|---:|
| X | BEST / wBEST | 0.231 / 0.235 | 0.205 / 0.206 | 0.152 / 0.153 | 0.227 / 0.230 | 0.294 / 0.297 | 0.292 / 0.306 |
| X | 2BEST / w2BEST | 0.246 / 0.245 | 0.207 / 0.207 | 0.151 / 0.154 | 0.234 / 0.236 | 0.295 / 0.302 | 0.304 / 0.309 |
| X | QBS-ART (sig. over rows) | 0.249 (1,2) | 0.207 | 0.157 | 0.242 (1,2,3) | 0.313 (1–4) | 0.313 (1) |
| XI | PORT+QBS-ART | 0.240 | 0.207 | 0.149 | 0.230 | 0.304 | 0.308 |
| XI | GRAS+QBS-ART | 0.242 | 0.206 | 0.151 | 0.236 | 0.305 | 0.306 |
| XI | QIS+QBS-ART | 0.249 | 0.207 | 0.157 | 0.242 | 0.313 | 0.313 |

- The QBS-ART values in Tables X–XI equal the **NPMI** QBS-ART cells of Tables III–VIII in every column (TREC 4: 0.207 = NPMI, not RC 0.212). So these ablations use NPMI **[inferred from the numbers]**.
- Full weighted QBS-ART vs w2BEST: +0.000 to +0.011 MAP **[computed]**. It is significant (paired t-test) against w2BEST only on ROBUST.
- Base stemmer: QIS base > Porter base by 0.000–0.012 MAP **[computed]**. Significance is not reported for Table XI.
- **Inter-corpus stemming** (Table XII), with the stemmer built on another collection:

  | Queries | Stemmer built on TREC 1–3 | Stemmer built on TREC 6–8 |
  |---|---:|---:|
  | TREC 1–3 | 0.249 | 0.247 |
  | TREC 6–8 | 0.238 | 0.242 |
  | ROBUST | 0.308 | 0.313 |

  Losses of 0.002–0.005 MAP **[computed]**. The co-occurrence statistics transfer across news corpora.
- **Fig. 5** (p. 18:23), number of variants added per query term by QBS-ART:
  - the mode is 1 on both collections (≈127 and ≈76 query terms) **[approximate]**;
  - a sizeable group gets 0 added terms (≈67 and ≈57) **[approximate]**.

### Internal inconsistencies found (with locations)

1. **Table VII (ROBUST), RC block.** The middle row is labelled "SNS+QBS" (0.295), where every other table has QBS-WMA (image-checked, p. 18:21). The text never mentions "SNS+QBS". Table IX lists QBS-WMA for ROBUST (RI 0.30). It is unclear whether this row is SNS used as base stemmer or a label error.
2. **Size-of-improvement claims** (pp. 18:17, 18:18, 18:20):
   - "more than 10% better than the best baseline (SNS)" on TREC 1–3: the relative gain is 8.3% (RC) / 8.7% (NPMI);
   - "more than 10% MAP improvement over the baselines on TREC 6, 7 & 8": relative 9.5% (NPMI) / 7.2% (RC) vs SNS/GRAS;
   - "more than 15% MAP improvement compared to either of Porter and XU": relative 14.7% vs Porter (NPMI), 12.3% (RC). Against XU the relative gain is 15.8% (NPMI), so the claim holds there, but it is 13.4% for RC **[computed]**.

   Apart from the NPMI-vs-XU case, these claims hold only if read as the difference between the printed improvements over NO. On that reading: 29.7 − 19.3 = 10.4 pp; 32.2 − 20.8 = 11.4 pp; 32.2 − 15.3 = 16.9 pp **[computed]**. The paper does not say which reading is meant. "ART … often more than 10% better compared to the best baseline stemmer" (p. 18:20) holds in relative terms only for ROBUST (NPMI, 10.6%) among the English collections.
3. **TREC 5** (p. 18:19): "Only query-based stemmers managed to provide significant MAP improvement (by both tests) compared to no stemming". But QIS-NPMI (0.153) carries n/n in Table V.
4. **Marathi** (p. 18:25): "The improvements from both QIS and QBSs over all five baselines are found to be statistically significant." In Table XIII (image-checked at 250 dpi), QIS lacks *s* in both tests and *g* in the randomization test. The NPMI QBS rows lack *s*. Only the RC QBS rows are significant against all five.
5. **Robustness of Porter** (p. 18:21): "Porter stemmer performs worst on all the collections". In Table IX Porter has the strictly lowest RI only on TREC 4 and TREC 6–8. It ties QIS on ROBUST (0.01). QIS is lower on TREC 1–3 (0.27 < 0.28) and TREC 5 (0.24 < 0.34), and GRAS is lower on TERABYTE (0.19 < 0.23). If only the four baseline stemmers are compared, Porter is lowest on 5 of the 6 TREC collections; the exception is TERABYTE (GRAS). The mismatch is therefore mainly with the words "on all the collections".
6. **Non-English robustness** (p. 18:26): "robustness of query-based stemmers is observed to be better than their competitors". On Czech, QBS-ART RI 0.57 < GRAS 0.63 (Table XVI). QBS-WMA is higher everywhere. The general conclusion that robustness is "always superior to the strong baselines" (p. 18:28) holds in Table IX (TREC) but not for QBS-ART on Czech.
7. **"ART performs consistently better than WMA"** (p. 18:19). Exceptions: TREC 4 NPMI (0.207 < 0.209) and TERABYTE RC (0.309 < 0.310). The non-English tables add Marathi RC (0.285 < 0.287, Table XIII) and Bengali RC (0.329 < 0.331, Table XV). The authors do note that WMA has better RI on the non-English collections.
8. **ROBUST baselines** (p. 18:18): "none of baseline stemmers are able to provide significant improvement even compared to unstemmed retrieval". The main tables carry no marks on baselines. Table IX's paired t-test gives SNS p = 0.04 vs NO, which contradicts the statement. XU p = 0.05 is borderline and not below 0.05. The text does not say which test the statement refers to.
9. **RI denominator:** see "RI does not match |Q| = 50" above.
10. **Minor typesetting issues:** P@5 bold on 0.541 instead of 0.545 (Table III); the second block of Table XV has no co-occurrence-measure label (presumably NPMI).

## 10. Statistical evidence

- **Significance tests.**
  - Main tables: two-sided Wilcoxon and randomization tests on per-query AP at 95%, each proposed method against each baseline (Sec. 4.3, p. 18:14). The authors ran paired t-tests too and found them "almost always similar" to randomization.
  - Tables IX and XVI: paired t-test p-values against NO only.
  - Table X: paired t-test.
  - **No multiple-comparison correction** is mentioned, although each collection has 6 proposed rows × 5 reference runs (NO + 4 baselines) × 2 tests.
- **Confidence intervals:** NOT_REPORTED.
- **Runs / seeds:** deterministic, single-run pipeline. Variance is not applicable and not reported.
- **Ablations:**
  - co-occurrence measure (RC vs NPMI, throughout);
  - weighted vs unweighted variants (Table X);
  - base stemmer (Table XI);
  - inter-corpus statistics (Table XII);
  - λ range, described verbally only ("[0.6–0.8]", p. 18:13; no table);
  - prefix and residue parameters, described verbally only (p. 18:9).
- **Per-query analysis:**
  - RI: net helped minus hurt vs NO with a 5% threshold, which is the only quantitative per-query summary;
  - qualitative error analysis of TREC queries 173 ("smoking bans"), 93 ("What Backing Does the National Rifle Association Have?"), "genetic engineering" (where QBS is worse than Porter/XU because *gene/genes* are merged with *genetic*), 360 ("drug legalization benefits") and "Antarctica Exploration" (Secs. 1, 5.4, 5.6).
  - **Not reported:**
    - separate n₊ and n₋;
    - per-query plots;
    - any per-query comparison between stemmers other than against NO;
    - any analysis by query feature (length, term frequency, family size);
    - relevant-set overlap or unique relevant hits between representations;
    - oracle union.

## 11. Strengths

- Nine collections, including a 25M-document web collection and three non-English languages. The main findings replicate across most of them.
- **Robustness treated as a first-class outcome** (RI, GMAP), not only MAP. The explicit motivation is that MAP can hide queries that stemming hurts (p. 18:20).
- Two complementary significance tests, with a stated rationale (p. 18:14).
- Strong and diverse baselines: rule-based, lexicon-based and two corpus-based stemmers.
- The ablations isolate the value of weighting (Table X), of the base stemmer (Table XI) and of corpus-specific statistics (Table XII).
- The method needs no relevance data. α is chosen by an unsupervised rule, and λ was tuned on topics outside the test sets.
- Error analysis shows both successes and a failure case (*genetic engineering*).

## 12. Limitations

### Stated by the authors

- The candidate-pair analysis is limited to alphabetic scripts and "may fail" for prefixing or infixing morphology (p. 18:8).
- The QIS parameters are "partly intuition and partly arbitrary" (p. 18:9).
- Query-based stemming cannot repair **understemming** by its base stemmer (pp. 18:2, 18:24).
- Stemming helps little on TREC 5, and no proposed method beats the baseline stemmers significantly there (p. 18:19).
- On Bengali, the QBS methods slightly lower MAP relative to their base QIS; the authors state that "in none of the cases is this reduction statistically significant" (p. 18:26).
- Intra-corpus statistics are "slightly more effective" than inter-corpus statistics (p. 18:24).
- RI ignores the size of differences, which is why the authors add a 5% threshold and p-values (p. 18:20).

### Inferred from the experimental design

1. **One retrieval model, and it is not BM25.** Results are for a Dirichlet LM. Interaction with BM25's tf saturation and length normalization is untested; `#wsyn` weighted tf sums may behave differently under BM25.
2. **Query-side vs index-side conflation is not controlled.** QIS/QBS operate through query operators over word forms. The mode for the baselines is not reported, so "stemmer" and "conflation mechanism" may be confounded.
3. **QBS is weighted query expansion** without an expansion baseline such as pseudo-relevance feedback. Some of its gain may come from expansion or reweighting in general rather than from morphology.
4. **RI is too coarse for set-level conclusions.** It does not give n₊ and n₋ separately, the 5% threshold (relative or absolute?) is not specified, and the denominator is inconsistent (§9).
5. **Multiple comparisons** are uncorrected across many method × baseline × collection tests.
6. **Two of the four baselines (SNS, GRAS) are the first author's own earlier stemmers.** Their configurations are not restated.
7. **Short queries dominate** (title fields; TREC 4 uses descriptions). The effect of query length is not analysed.
   - *Inferred from Eq. 14:* for a one-word query the RS term of ART is undefined (empty sums), and co-occurrence with "other query words" does not exist. Behaviour for single-term queries is not discussed.
8. **No lemmatization condition**, so the paper says nothing about stem vs lemma.
9. **No analysis of which documents** stemming adds or loses. Rel.Ret is a net total.
10. Several text claims do not match the tables (§9, items 1–8).

## 13. What the work proves

Within a Dirichlet-LM lexical system on TREC news/web collections and three FIRE/CLEF languages:

- **Stemming improves MAP over no stemming on every collection tested:**
  - baseline stemmers: +2.8% (XU, Marathi) to +36.4% (GRAS, Czech) (printed values, Tables III–VIII, XIII–XV);
  - among the English collections, baseline-stemmer gains are smallest on ROBUST and TERABYTE (+4.5% to +8.6%);
  - these are point estimates. Significance of the baselines vs NO is not shown in the main tables. The paired t-test does not reach p < 0.05 everywhere: Porter/RBS p = 0.13 (TREC 5), 0.09 (ROBUST), 0.10 (TERABYTE), 0.06 (Marathi) (Tables IX, XVI). The authors state that no baseline is significant vs NO on ROBUST (p. 18:18).
- **Query-dependent weighting of morphological variants outperforms query-independent stemming.** On TREC 1–3, TREC 6–8, ROBUST and TERABYTE, QBS-ART (both measures) and every QBS-WMA row but one beat all baseline stemmers significantly, by both tests (Tables III, VI–VIII). The exception is WMA-RC on TREC 6–8, which beats only NO, Porter and XU. On ROBUST the RC row is labelled "SNS+QBS". The advantage is small or absent on TREC 4, TREC 5 and Bengali.
- **Stemming effects are heterogeneous across queries.** On ROBUST all baselines have net RI 0.01–0.08, i.e., queries helped and hurt by more than 5% roughly balance (Table IX). How many queries are affected cannot be derived from net RI. Only the authors' statement for Porter ("nearly half of the queries are hurt", p. 18:21) speaks to that. QBS achieves higher net RI:
  - 0.41–0.72 on TREC-style sets (QBS-ART), above every baseline in each column, though only narrowly on TREC 4 (0.66–0.67 vs GRAS 0.64);
  - 0.57–0.67 on the non-English sets, but QBS-ART on Czech (0.57) is below GRAS (0.63) (Table XVI).
- **Continuous weights mostly beat a hard cut-off on variants** (Table X), by small margins:
  - vs w2BEST 0.000–0.011 MAP, significant only on ROBUST;
  - vs BEST 0.002–0.021; vs 2BEST 0.000–0.018 **[computed]**;
  - on TREC 4, QBS-ART (0.207) ties 2BEST/w2BEST.
- **The base stemmer's grouping matters.** QIS base ≥ Porter/GRAS base (Table XI); understemming by the base cannot be recovered.
- **Corpus co-occurrence statistics transfer across similar news corpora** with small losses (≤ 0.005 MAP; Table XII).
- The RC and NPMI measures give comparable retrieval effectiveness.

## 14. What the work does NOT prove

- **Anything about BM25.** Only a Dirichlet LM is used.
- **Anything about dense/semantic retrieval or hybrid retrieval.** Neither is present. QBS is a lexical expansion, not a semantic channel.
- **Anything about lemmatization versus stemming.**
- **That stemming changes *which* relevant documents are found** (unique hits, overlap). Only net Rel.Ret totals and net RI are given.
- **How many queries are hurt** by any stemmer. n₋ is not reported; RI is net and thresholded.
- **Which query characteristics predict whether stemming helps.** There is no systematic feature analysis, only anecdotes about frequent variants such as *legal*, *national*, *association* and *gene*.
- **Transfer to agglutinative Turkic languages** (Uzbek, Turkish) with long suffix chains and morphophonemic alternations. Marathi, Bengali and Czech are the only non-English languages.
- **The size-of-improvement claims as relative gains** (§9 item 2), and the claimed QIS significance on Marathi and QBS robustness superiority on Czech (§9 items 4, 6).

## 15. Relationship to current Uzbek evidence

- **No Uzbek or Turkic data.**
- Context (not from the paper): Uzbek is a suffixing agglutinative language written in Latin script with apostrophe letters (o‘, g‘). The QIS assumptions (a shared prefix of ≥ 3 letters and recurring suffix residues) fit suffixing morphology in principle. How well the prefix test works for Uzbek depends on consistent tokenization and apostrophe normalization. Stem-final consonant alternations (e.g., *yurak* → *yuragi*) would break exact common-prefix matching at the last letter. This is our hypothesis, untested.
- **Relation to national evidence:**
  - Uzbek rule/analyzer-based stemmers and lemmatizers exist (Xusainova PhD, UzbStemmer; Bakaev; Elov; see `MASTER_INDEX` C);
  - none has been evaluated with per-query robustness against a raw lexical baseline in a qrels-based benchmark (GAP_BOUNDARY §2).
  - This paper supplies the **evaluation template** (per-query helped/hurt vs raw, GMAP, two tests) that the Uzbek morphology literature lacks.
- **Relation to international cards:**
  - Same conclusion as Can et al. 2008 (MORPH-001) and Kettunen et al. 2005 (`CR000452`): the morphological effect differs by query/topic even when means are similar. This paper adds a *query-adaptive* treatment and robustness metrics.
  - Like MORPH-002 (Haddad & Bechikh Ali) it shows that simpler normalizations can remain competitive in some collections (TREC 5, Bengali).
- **Related record in our corpus** (from our assignment list, not from the paper): `CR000161` (Sahu & Pal 2025), a comparison of language-independent stemmers (including SNS and GRAS) on FIRE Indian-language collections with per-query analysis. It is useful for checking whether GRAS/SNS-type corpus stemmers have been re-evaluated recently.

## 16. Relationship to CURRENT_GAP

**Classification:** *supports (background)* + *closes part of a broad claim* + *no material effect on the residual core*.

- **Supports:**
  - the premise of v0.8 that changing the morphological representation of the lexical channel changes results **query by query**, not uniformly;
  - that frequency and thematic coherence of variants plausibly drive this.

  This supports including per-query analysis and lexical/term-level query features (variant frequency, variant family size, co-occurrence with other query words, query length) among the candidate factors.
- **Closes part of a broad claim** (not in the v0.8 core, but worth recording). Query-dependent or selective stemming, i.e. deciding per query which morphological variants to use, is **occupied** (this paper; also Peng et al. 2007, cited here). Any future method along the lines of "choose the morphological representation per query" must be positioned against it. Such a method would stand beside dynamic α(q), which GAP_BOUNDARY already marks as occupied.
- **No material effect on the residual core.** v0.8 refined asks how raw → stem → lemma changes:
  - unique relevant hits;
  - overlap with a **fixed dense D**;
  - oracle union;
  - incremental hybrid gain;
  - the link of these changes to query features.

  This paper has no BM25, no lemma, no dense D, no fusion and no set-level overlap. It compares lexical representations with each other only through net per-query AP changes.

**Proposal:** keep v0.8 refined unchanged. Optionally add to the claim-status matrix: "Query-dependent / selective morphological normalization (stemming) is new: **REJECTED** (Paik et al. 2013; Peng et al. 2007)". This is a proposal only; `CURRENT_GAP.md` and `GAP_BOUNDARY` have not been edited.

## 17. Implications for our research design

- **Per-query reporting of the raw → stem → lemma change.**
  - Adopt the robustness idea, but report **n₊, n₋ and n₀ separately** for BM25_stem and BM25_lemma vs BM25_raw (and for H_stem, H_lemma vs H_raw).
  - Report the threshold, stating whether it is absolute or relative, and the exact denominator. This avoids the ambiguities found here (§9).
  - Also report GMAP, or another low-tail measure, next to MAP/nDCG.
- **Significance.** Use per-query paired tests, with two tests of different character (sign/Wilcoxon and randomization/bootstrap). Plan a multiple-comparison correction for the representation × condition grid.
- **Set-level measures are still needed.** Net totals such as Rel.Ret can hide gained and lost relevant documents. For each query, record relevant documents found by raw only, by stem only and by both, **within the lexical family**, in addition to lexical vs D. This directly extends the Paik-style analysis to our complementarity question.
- **Morphology preprocessing / definition of "stem".**
  - Fix and report where conflation happens: index-side stemming vs query-side synonym expansion over a raw index. Paik's QBS is query-side and weighted, which is a different representation from an index-side stem field.
  - Primary conditions stay index-side (BM25_raw / _stem / _lemma).
  - A weighted query-side variant expansion could be an *optional secondary* condition only. It confounds morphology with expansion.
- **Query taxonomy (candidate features):**
  - size of the morphological variant family of each query term in the corpus;
  - collection frequency / df of the variants relative to the query term (Paik's drift mechanism);
  - co-occurrence (NPMI) of the variants with the other query terms (thematic coherence);
  - number of query terms (single-term queries cannot use co-occurrence context);
  - query field (title vs description).
- **Illustrative Uzbek risk (ours, not from the paper).** A frequent base form with broad meaning merged with a specific derivative, e.g. *qonun* "law" with *qonuniy* "legal / lawful", mirrors *legal* / *legalization*. Such merges could create lexical "drift" that changes overlap with D in a query-specific way. This is a hypothesis to test, not evidence.
- **Baselines (optional control).** A language-independent corpus-based stemmer (GRAS/YASS-type) could serve as a secondary stem condition next to an Uzbek rule/analyzer-based stemmer. Its assumptions (suffixing, shared prefixes) match Uzbek in principle. This is a secondary control, not a primary condition.
- **Metrics.** MAP, P@k and R-Prec as here; Recall/Rel.Ret at depth (e.g., 1000 or the candidate depth k) is needed for union coverage.
- **Protocol.**
  - Tune any parameters (fusion α, stemmer thresholds) on separate topics, as Paik tuned λ on topics 1–50.
  - Keep the query field fixed across conditions.

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| Stemming | Cutting words down to a shared stem so that different forms match | Map word forms to equivalence classes by suffix removal or grouping |
| Understemming / overstemming | Leaving related words apart / merging unrelated words | Recall loss from split classes / precision loss from merged classes |
| Query-based (query-dependent) stemming | Deciding per query which word variants to use and how much | Variant weights W(v, q) conditioned on the whole query |
| Corpus-based stemmer | A stemmer learned from the text collection instead of hand-written rules | Groups from lexicon statistics and/or co-occurrence |
| Co-occurrence | Two words appearing in the same documents more often than chance | df(a, b) compared with an independence expectation |
| PMI / NPMI | How much more often two words co-occur than chance, scaled to [−1, 1] | log₂ P(a,b)/(P(a)P(b)), normalized by −log₂ P(a,b) |
| RC | The authors' co-occurrence score: how unlikely the observed overlap is under random placement | Normalized −log hypergeometric probability (Eqs. 3–5) |
| `#syn` / `#wsyn` | Query operators that treat several words as one term, optionally with weights | tf and ctf summed (weighted) over class members |
| Dirichlet LM | A probabilistic ranking model that smooths document word probabilities with the collection | Query likelihood with Dirichlet prior μ |
| MAP / GMAP | Average ranking quality over queries; the geometric version penalizes very bad queries | Arithmetic / geometric mean of AP |
| R-Prec | Precision at the rank equal to the number of relevant documents | P@R |
| Robustness index (RI) | Share of queries helped minus share hurt, compared with a reference run | (n₊ − n₋)/\|Q\| |
| Wilcoxon / randomization test | Paired tests on per-query scores: the first mainly counts wins, the second uses the size of differences | Signed-rank test; permutation test |
| Index-side vs query-side conflation | Stem the documents when indexing vs expand the query with variants over an unstemmed index | Different lexical representations with different tf statistics |
| Complementarity (project term) | Each channel or representation finds some relevant documents the other misses | Unique relevant hits, overlap, oracle-union gain |

## 19. Open questions / verification needed

1. **"SNS+QBS" in Table VII:** is it SNS as base stemmer or a mislabelled QBS-WMA? Which run underlies the ROBUST QBS-WMA RI (0.30) in Table IX?
2. **Meaning of the ">10% / >15%" claims** (relative gain or difference of percentage improvements over NO)?
3. **RI:** the separate n₊ and n₋; whether the 5% threshold is relative or absolute; the actual denominator (odd-hundredth RIs for 50-query sets).
4. **Which co-occurrence measure** underlies Tables IX and XVI? (Tables X–XII match NPMI.)
5. **How the baseline stemmers were applied** (index-side vs `#syn` classes), and the stop-word handling. NOT_REPORTED.
6. **Non-English query fields** and settings. NOT_REPORTED beyond "similar".
7. **NPMI-QIS α filter:** is it non-binding because of the NPMI ≥ 0.3 pre-condition (our inference)?
8. **Single-term queries in QBS-ART** (Eq. 14 undefined): how are they handled?
9. For our corpus: check `CR000161` (Sahu & Pal 2025) for recent per-query results of GRAS/SNS-type stemmers before citing them as current evidence.

## 20. Decision after deep dive

- **Keep current gap?** Yes. v0.8 refined remains valid (§16).
- **Modify gap?** No change to the formulation. Optional (researcher's decision): add the claim-status row "query-dependent / selective stemming is new: REJECTED" to `GAP_BOUNDARY`, citing this paper as A-level evidence.
- **Add decision?** Proposed for `decisions/DECISIONS.md`:
  - "Per-query effects of every morphological condition are reported as separate helped / hurt / unchanged counts with a stated threshold and denominator, plus a low-tail metric (e.g., GMAP), not only as a net robustness index";
  - "Conflation is index-side in the primary conditions; any query-side variant expansion is a separately labelled secondary condition".
- **Add experiment?** Optional low-cost addition to the pilot: within the lexical family, compute raw-only / stem-only / both relevant hits per query (lexical-internal complementarity). Relate them to variant-family size, variant df and query length. This precedes and conditions the lexical-vs-D overlap analysis.
- **Add citation to Chapter I?** Yes:
  - §1.1 (morphological normalization in lexical IR: under/overstemming, corpus-based and query-dependent stemming, robustness of stemming effects);
  - §1.3, as evidence that the benefit of a lexical-representation change is query-dependent, which motivates per-query analysis.
- **Proposed `MASTER_INDEX.md` row** (to add after approval):

| MORPH-034 | Paik, Parui, Pal, Robertson — *Effective and Robust Query-Based Stemming* (ACM TOIS 31(4), Article 18, 29 pp.) — [deep dive](deep-dives/2013_Paik_Parui_Pal_Robertson_Query_Based_Stemming.md) | 2013 | A | HIGH | Corpus-based co-occurrence stemmers with query-dependent variant weighting (QIS; QBS-WMA/ART via Indri `#wsyn`) vs no stemming, Porter/RBS, XU, SNS, GRAS on 12 TREC topic sets (6 collections incl. ROBUST, GOV2) plus FIRE Marathi/Bengali and CLEF Czech; Dirichlet LM (**not BM25**). QBS-ART (NPMI) MAP e.g. TREC 1–3 0.192→0.249, ROBUST 0.268→0.313 (baselines ≤0.283), Czech 0.214→0.318; no gain on Bengali. Robustness index vs no stemming (net helped−hurt, 5% threshold): QBS-ART 0.41–0.72 vs baselines 0.01–0.64; n₊/n₋ not reported separately. No lemma, no dense, no fusion, no overlap/unique-hit analysis. Several text claims (>10%/15% gains, Marathi significance, Czech robustness, "SNS+QBS" label) do not match the tables. |
