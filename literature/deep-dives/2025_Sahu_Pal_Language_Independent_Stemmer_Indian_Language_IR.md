# Sahu & Pal (2025): A Study on Language-Independent Stemmer in the Indian Language IR

**Targeted deep-dive status:** COMPLETED (AI-assisted, pending researcher review)
**Completed:** 2026-09-28
**Literature ID:** `MORPH-037` (assigned 2026-09-28, approved by researcher)
**Systematic-review record:** `CR000161`. Full-text triage: include ("включить"), reading priority HIGH, reading tier "2 — важно", `carries_complementarity_evidence = YES`. We qualify that flag (§10, §16). The per-query evidence compares **two lexical runs** (a stemmed run vs the unstemmed run) by the per-query change in average precision. It is a helped/hurt count, not a relevant-set overlap. No dense or semantic channel exists in the paper.
**Provenance:** AI-assisted deep dive (Claude). The whole paper (9 PDF pages = printed pp. 181–189) was read from the pdftotext extraction. Page images were checked at 110 dpi for pp. 181 (abstract, venue footer, DOI), 183 (Algorithm 1, YASS D3 formula), 184 (Algorithms 2–3), 185 (Algorithm 4, Table 1, Table 2), 186 (Table 3, Figs. 1–2), 187 (Tables 4–5, the result paragraph, Conclusion) and 188 (Fig. 3). Figs. 1–3 were also checked on 300-dpi crops to count bars. Printed page = PDF page + 180. Numbers computed by us are marked **[computed]** and were recomputed with Python. Bar counts read from the figures are marked **[visual count, approximate]**.
**Source rule:** **the paper is the primary and only authoritative source.** No code, website, later paper or background knowledge is used as evidence about what the authors did. Only the bibliographic record was checked on the web: ACL Anthology gives the ID, editors, publisher, pages and date (bibliographic check: aclanthology.org/2025.globalnlp-1.20). The DOI printed on p. 181 could not be resolved (doi.org unreachable through the proxy, HTTP 403), and the ACL Anthology page does not list a DOI.
**Verification:** independent AI verifier pass 2026-09-28; 14 findings addressed.
**Reliability:** **B**. The paper is a peer-reviewed workshop paper (RANLP 2025 workshop, ACL Anthology) and it is verifiable. Its evidential strength is limited: 50 title queries per language, no significance testing, stemmer parameters tuned on the test queries, and several text claims that do not match its own tables (§9, §19).

---

## Кратко для исследователя (RU)

- **Что сделано.** На коллекциях FIRE 2011 для хинди, гуджарати и английского (по 50 запросов, только поле title, ~0.3–0.4 млн новостных документов) авторы сравнили:
  - **без стемминга** (базовый вариант);
  - 4 языково-независимых (статистических) стеммера: **YASS, FCB, SNS, GRAS**;
  - **усечение слова до первых n символов** (Trunc-n, n = 5/5/6).
  Каждый вариант прогнан в **6 моделях Terrier**: BM25, TF-IDF, BB2, InL2, IFB2 и языковая модель Хиемстры. Метрики: MAP и число найденных релевантных документов (Rel.Ret) (Tables 3–5, pp. 186–187).
- **Главные числа (MAP, BM25):**
  - хинди 0.4444 → лучший стеммер GRAS 0.4495, Trunc-5 0.4543;
  - гуджарати 0.2400 → SNS 0.2647 (+10.3% **[computed]**);
  - английский 0.2975 → GRAS 0.3145, Trunc-6 0.3155.
  - Проценты из аннотации (+2.98% хинди, +20.78% гуджарати, +5.83% английский) взяты из **разных моделей** (TF-IDF, InL2, TF-IDF). +20.78% получено на InL2, которую сами авторы называют слабой. На BM25 для гуджарати прирост +10.3% **[computed]**.
- **Эффект стемминга зависит от языка и от модели.**
  - В хинди 9 из 30 ячеек «стеммер/Trunc-n × модель» **ниже** базового варианта (YASS — BM25, InL2, IFB2, LM; GRAS — BB2, InL2, IFB2, LM; Trunc-5 — InL2) **[computed]**;
  - в гуджарати и английском все стеммеры выше базового варианта во всех моделях.
- **Простое усечение (Trunc-n) близко к лучшему стеммеру.** В английском оно выше лучшего стеммера (GRAS) во всех 6 моделях. В хинди на BM25 оно лучше всех (0.4543). Но в гуджарати оно ниже SNS во всех 6 моделях (BM25 0.2579 vs 0.2647), в хинди — ниже SNS в 5 из 6; разрыв ≤ ~0.01 MAP **[computed]**. Утверждения «лучший стеммер» в статье молча исключают Trunc-n.
- **Есть разбор по запросам, но только «стемминг vs без стемминга» внутри лексического поиска** (Figs. 1–3, pp. 186, 188): стемминг помогает / вредит в 35/15 (хинди), 38/8 (гуджарати), 32/12 (английский) запросах из 50.
  - Даже у лучшего варианта вредит 16–30% запросов **[computed]**.
  - Причины не анализируются, признаки запросов не рассматриваются, значимость не проверяется.
- **Rel.Ret почти всегда растёт при стемминге, даже когда MAP падает.** Пример: хинди, YASS, BM25: Rel.Ret +81 при MAP −0.5% **[computed]**. Это только суммарные числа: пересечение и уникальные релевантные документы между вариантами не приводятся.
- **Чего нет** (по измерениям нашего gap):
  - лемматизации;
  - плотного или семантического поиска;
  - гибрида / fusion;
  - перекрытия результатов, уникальных находок, oracle union;
  - тестов значимости;
  - отдельной dev-выборки: параметры стеммеров подобраны по лучшему MAP на тех же 50 запросах.
- **Внутренние несоответствия.**
  - «GRAS performed best in different Indian languages» (p. 187) противоречит «SNS лучший в хинди и гуджарати» (там же и в аннотации).
  - Для анализа по запросам заявлены «лучшие модели», но для гуджарати взята InL2.
  - Счёт по запросам в тексте не совпадает с числом видимых столбцов на рисунках.
  - Параметры SNS/GRAS в Table 1 расходятся с алгоритмами 3–4.
- **Для нашего gap:** поддерживает фон (эффект морфологического представления лексического канала неоднороден по запросам и зависит от языка и модели). Ядро v0.8 не затрагивает. **Предложение: gap не менять.**
- **Практическая польза для нас:**
  1. Добавить Trunc-n как языково-независимый контроль рядом с raw/stem/lemma.
  2. Подбирать параметры стеммеров только на dev.
  3. Вместо суммарного Rel.Ret считать по запросам уникальные релевантные документы каждого варианта и тестировать значимость.

---

## 1. Bibliographic record

- **Authors:** Siba Sankar Sahu (Dept. of CSE, Sardar Vallabhbhai National Institute of Technology, Surat, India); Sukomal Pal (Dept. of CSE, Indian Institute of Technology (BHU), Varanasi, India) (p. 181)
- **Year:** 2025
- **Title as printed on p. 181:** "A study on language-independent stemmer in the Indian language IR". ACL Anthology and the PDF metadata give "A study on **the** language **independent** stemmer in the Indian language IR" (bibliographic check: aclanthology.org).
- **Venue:** *Proceedings of the Workshop on Beyond English: Natural Language Processing for all Languages in an Era of Large Language Models* (GlobalNLP 2025) (full name: bibliographic check, aclanthology.org; the p. 181 footer prints the abbreviated form "Beyond English: NLP for all Languages in an Era of LLM from Texts associated with RANLP 2025"), Varna, Bulgaria, Sep 12, 2025 (p. 181 footer)
- **Editors:** Sudhansu Bala Das, Pruthwik Mishra, Alok Singh, Shamsuddeen Hassan Muhammad, Asif Ekbal, Uday Kumar Das (bibliographic check: aclanthology.org)
- **Publisher:** INCOMA Ltd., Shoumen, Bulgaria (bibliographic check: aclanthology.org)
- **Pages:** 181–189
- **ACL Anthology ID:** `2025.globalnlp-1.20`
- **Official URL:** https://aclanthology.org/2025.globalnlp-1.20/
- **DOI:** printed on p. 181 as `10.26615/978-954-452-105-9-020`. **Not verified**: doi.org was unreachable (proxy 403), and the ACL Anthology page shows no DOI.
- **Source type:** peer-reviewed workshop paper (short/regular workshop paper; 8 pages of text plus references)
- **Reliability:** B
- **Full text available:** yes (`07_full_text/pdfs/CR000161.pdf`, 9 pages)
- **Funding / resources (p. 188):** IIT (BHU) Varanasi; PARAM Shivay supercomputing facility

## 2. Why this work matters to the PhD

It is a recent (2025) controlled comparison of **several lexical representations** (no stemming, four unsupervised corpus-based stemmers, prefix truncation) across **six lexical ranking models, including BM25**, in low-resource, morphologically inflected languages. It also reports a **per-query** helped/hurt analysis of the representation change. Those are two of the ingredients of our design. The dense and hybrid half is absent.

| Axis | Relation |
|---|---|
| Lexical retrieval | Central. BM25, TF-IDF, three DFR models (BB2, InL2, IFB2) and the Hiemstra language model, all in Terrier (Sec. 4, p. 185) |
| Morphological representation of the lexical channel | Central. No stemming vs YASS, FCB, SNS, GRAS (unsupervised, corpus-based) vs Trunc-n. **No lemmatization, no rule-based stemmer, no character n-grams** |
| Semantic retrieval | **Absent** |
| Hybrid retrieval | **Absent**: no fusion of any kind, not even between stemmed and unstemmed lexical runs |
| Uzbek morphology | Indirect. Hindi, Gujarati (Indo-Aryan, inflectional) and English; no agglutinative or Turkic language |
| Low-resource retrieval | Direct: language-independent stemming is motivated by the lack of linguistic resources (Sec. 1, p. 181) |
| Current gap | Supports the background claim that the lexical representation's effect is query-, language- and model-dependent. **No** lexical–dense complementarity (§16) |

## 3. Research problem

### Simple explanation

Words change form: Hindi and Gujarati add endings to show case, number and so on. A search engine that matches exact forms misses documents that use another form of the query word. A *stemmer* cuts words down to a common part so that the forms match. Hand-written stemmers need linguistic knowledge that many Indian languages lack. *Language-independent* stemmers learn which endings to cut from the document collection itself. The authors ask whether such stemmers help retrieval in Indian languages, and which one works best.

### Formal formulation

Two research questions (Sec. 1, p. 182; quoted verbatim):

- **RQ1:** "Does language-independent stemmer improve retrieval performance in different Indian languages IR? If yes, to what extent?"
- **RQ2:** "Which language-independent stemmer is the most suitable for different Indian languages? Whether to use Yet another suffix stripper (YASS) or fast-corpus-based (FCB) or co-occurrence-based (SNS) or graph-based (GRAS), or Trunc-n-based indexing?"

Task: monolingual ad hoc document retrieval (FIRE collections, title queries). The factors are the index-term representation (6 levels) × the ranking model (6 levels) × the language (3). The response is MAP and relevant-retrieved count.

## 4. Main idea

### Simple explanation

Take each collection. Build six versions of the index: no stemming; one per stemmer (YASS, FCB, SNS, GRAS); and one where every word is cut to its first n letters. Search each index with six standard ranking formulas and see which combination gives the best average precision.

### Concrete example

- The paper's only morphological example is English: "'education', 'educating', 'educated', and 'educational' map to their root word 'educate'" (Sec. 1, p. 181), and "'educated' provides 'educ'" under Trunc-4 (Sec. 3.4, p. 185).
- Illustration of the retrieval effect (ours, not from the paper): a title query containing *educated* matches a document that only says *education* once both are indexed as *educ*. Without stemming the document is not matched on that term.
- The per-query figures show that the same conflation can also hurt a query. For example, the bars for Hindi queries 23 and 6 are clipped at −0.5 in Fig. 1 (p. 186); if the axis is read as a fraction (units ambiguous, §8), their AP drops by at least half. The paper gives no examples of which words caused this.

### Formal method

Stemmers as described by the authors (Algorithms 1–4, pp. 183–185; paraphrased, formulas as printed):

- **YASS** (Majumder et al. 2007). String distance D3 between words X and Y. As printed: `D3(X,Y) = ((x − y + 1)/y) · Σ_{i=y..x} 1/2^{i−x}`, where x is the maximum length of X and Y and y is the index of the first mismatch. Complete-linkage clustering of the lexicon at threshold θ; each cluster becomes one stem class.
- **FCB** (Paik & Parui 2011). Words are grouped into equivalence classes by a common prefix of length k. A suffix is a "potential suffix" if its frequency exceeds a cut-off α. The longest common prefix of a class is a candidate stem. It is accepted if the ratio "potential class size / generated class size" exceeds δ; otherwise the process is repeated iteratively (k1 = initial prefix length, k2 = final prefix length).
- **SNS** (Paik et al. 2011b). Co-occurrence `CO(a,b) = Σ_{d∈C} min(tf_{a,d}, tf_{b,d})`. Graph edges (weight CO) are added if a pair satisfies "at least one of these two conditions: (i) CO(w1, w2) > 0; and (ii)" a common prefix of at least L1 (with a suffix condition involving L2) (Algorithm 3, step 6, p. 184; the wording mixes "at least one of" and "and", so whether the conditions are disjunctive or conjunctive is ambiguous). The strength is recomputed through common neighbours: `RCO(a,b) = CO(a,b) + Σ_{c∈N_{a,b}} min(CO(a,c), CO(c,b)) · 0.5`. Weak edges are removed, and the stem is the longest prefix within a connected component.
- **GRAS** (Paik et al. 2011a). Words sharing an L-long prefix (L = "average word length of the language") are partitioned. η-frequent suffix pairs are collected (η = 1). A graph of morphological links is built, pivot nodes with many edges become stems, and class membership is decided by cohesion δ.
- **Trunc-n.** Keep the first n characters of each word.

## 5. Architecture / algorithm

1. **Collections**: FIRE 2011 Hindi, Gujarati and English (Table 2, p. 185; table captions "2011 text collection", pp. 186–187). Only the query title (T) field is used (Sec. 5, p. 185).
2. **Stemmer induction** from each collection (Sec. 3). The paper implies the lexicon is taken from the collection but does not state the exact vocabulary.
3. **Parameter choice** (Table 1, p. 185): "The best MAP score obtained by stemming techniques for different languages with different parameters and 'n' values is shown in Table 1" (p. 185). YASS: "we experimented with different threshold values (θ), and the best MAP score obtained at a particular threshold value is noted down" (Algorithm 1, step 7, p. 183). **No separate tuning query set is mentioned, so parameters were evidently selected by MAP on the same 50 test queries (our inference).** Which ranking model was used for that selection is **NOT_REPORTED**. Table 1 gives one parameter set per stemmer per language, reproduced below.

| Stemmer | Hindi | Gujarati | English |
|---|---|---|---|
| YASS | θ = 1.5 | θ = 0.6 | θ = 1.55 |
| FCB V-1 | k1 = 4, k2 = 2, δ = 0.7 | k1 = 4, k2 = 2, δ = 0.6 | k1 = 7, k2 = 2, δ = 0.6 |
| SNS | L1 = 4, L2 = 6 | L1 = 5, L2 = 7 | L1 = 3, L2 = 5 |
| GRAS | L = 6, α = 4 | L = 7, α = 4 | L = 8, α = 6 |
| Trunc-n | 5 | 5 | 6 |

   - Tensions with the algorithm boxes: Algorithm 3 says "Here L1=3" and "Here L2 > 5" (p. 184), but Table 1 uses other values for Hindi and Gujarati (L1 = 4/5), and English L2 = 5 does not satisfy "L2 > 5". Algorithm 4 uses η = 1 and δ (p. 185), but Table 1 lists α for GRAS, which is not defined in Algorithm 4. The legend only says "θ, α, δ : Threshold taken by different stemmers".
4. **Indexing and ranking** in Terrier (Sec. 4, p. 185): BM25, TF-IDF, BB2, InL2, IFB2 and the Hiemstra LM.
   - **NOT_REPORTED:** Terrier version; BM25 k1/b and the other model parameters; tokenization; stop-word removal; lowercasing (for English); retrieval depth for Rel.Ret; the evaluation tool.
5. **Evaluation**: MAP and Rel.Ret for each (representation, model) cell (Tables 3–5). A per-query "% gain in MAP" is given for one configuration per language (Figs. 1–3).

## 6. Data

- **Collections (Table 2, p. 185):**

| Collection | Size | Documents | Queries |
|---|---|---:|---:|
| Hindi | 1.3 GB | 331,608 | 50 |
| Gujarati | 2.2 GB | 313,163 | 50 |
| English | 1.1 GB | 392,577 | 50 |

- **Source:** "part of the FIRE evaluation campaign"; "mainly consist of news articles extracted from different archives"; UTF-8 (Sec. 5, p. 185). The year 2011 is given only in the table captions (Tables 3–5).
- **Domain:** news.
- **Queries:** FIRE topics, title field only. Topic numbers are **NOT_REPORTED**: the figures label them 1–50.
- **Relevance judgments:** FIRE qrels, implied by the use of the FIRE collections. Pooling, grading and the number of relevant documents per language are **NOT_REPORTED**. Recall therefore cannot be derived from Rel.Ret.
- **Train/dev/test:** no split. The unsupervised stemmers are induced from the collection, and their parameters are tuned by MAP on the evaluation queries (§5).
- **"Indian languages":** the paper treats English as one of the "Indian languages" (Abstract, p. 181; Conclusion, p. 187).

## 7. Baselines

| Baseline | What it is | Why selected | Fair comparison? |
|---|---|---|---|
| No stemming ("Base line") | Surface-form index, same ranking model | Reference for RQ1 | **Partly.** The stemmers get parameters tuned on the test queries, while the baseline has no free parameters. Part of a small gain (e.g. Hindi BM25 +0.7–1.2%) may be tuning optimism |
| Trunc-n | Prefix truncation, n tuned per language | Language-independent indexing alternative (RQ2) | Yes, same tuning status as the stemmers. It is, however, excluded from the "best stemmer" statements and the boldface |
| Across ranking models | BM25, TF-IDF, BB2, InL2, IFB2, LM | Robustness of the stemming effect across models | Yes (same indexes). Model parameters are not reported and presumably not tuned |
| Rule-based stemmers | — | Not tested. The paper states that prior work found language-independent stemmers comparable to rule-based ones (Sec. 1, p. 182) | Missing comparator; RQ2 is limited to unsupervised methods |

## 8. Metrics

| Metric | Definition | Simple meaning here | Appropriate? |
|---|---|---|---|
| MAP | Mean over queries of average precision (AP). AP is the sum of precision at each rank where a relevant document appears, divided by the number of all relevant documents | One number summarizing both "how many relevant documents" and "how high they are" | Yes, standard for FIRE ad hoc retrieval. With 50 queries, small differences need a significance test, which is not given |
| Rel.Ret | Total number of relevant documents retrieved, summed over the 50 queries, at an unstated depth | "How many relevant documents appear anywhere in the returned list" | Useful recall-type signal. The depth is **NOT_REPORTED**, and it is a net total that hides documents gained and lost |
| Per-query "% gain in MAP" (Figs. 1–3) | Per-query relative change of the stemmed run's score vs the unstemmed run, same model | Which queries stemming helps or hurts | Presumably per-query AP (MAP of one query). The y-axis values (up to 1.0 or 3) look like fractions (1.0 = +100%), but the axis says "%": **units ambiguous**. Extreme bars are clipped by the axis limits |

Significance tests: **none** reported.

## 9. Results

### Tables 3–5: MAP (Rel.Ret) per representation × model (pp. 186–187; checked on page images)

**Hindi (Table 3, p. 186)**

| Representation | BM25 | TF-IDF | BB2 | InL2 | IFB2 | LM |
|---|---:|---:|---:|---:|---:|---:|
| Baseline | 0.4444 (1683) | 0.4455 (1679) | 0.3746 (1659) | 0.3909 (1654) | 0.3724 (1664) | 0.405 (1667) |
| YASS | 0.442 (1764) | 0.446 (1762) | 0.3773 (1729) | 0.3785 (1735) | 0.3675 (1731) | 0.3989 (1730) |
| FCB V-1 | 0.4476 (1725) | 0.4488 (1720) | 0.3767 (1703) | 0.3939 (1700) | 0.3746 (1708) | 0.4081 (1708) |
| SNS | 0.4483 (1745) | **0.4588** (1742) | **0.3798** (1732) | **0.3945** (1724) | **0.3808** (1728) | **0.4092** (1712) |
| GRAS | **0.4495** (1759) | 0.4505 (1755) | 0.3692 (1735) | 0.3815 (1741) | 0.3661 (1740) | 0.3995 (1736) |
| Trunc-n (n = 5) | 0.4543 (1749) | 0.4561 (1744) | 0.376 (1733) | 0.3879 (1725) | 0.3729 (1735) | 0.409 (1706) |

**Gujarati (Table 4, p. 187)**

| Representation | BM25 | TF-IDF | BB2 | InL2 | IFB2 | LM |
|---|---:|---:|---:|---:|---:|---:|
| Baseline | 0.24 (1315) | 0.2399 (1308) | 0.2041 (1278) | 0.1992 (1270) | 0.2021 (1274) | 0.2095 (1289) |
| YASS | 0.2464 (1320) | 0.2463 (1311) | 0.2116 (1280) | 0.2057 (1279) | 0.2077 (1276) | 0.2137 (1287) |
| FCB V-1 | 0.2423 (1337) | 0.2404 (1331) | 0.2056 (1292) | 0.1998 (1290) | 0.2031 (1296) | 0.2105 (1313) |
| SNS | **0.2647** (1359) | **0.2643** (1357) | **0.2385** (1343) | **0.2406** (1325) | **0.2342** (1336) | **0.2335** (1338) |
| GRAS | 0.2443 (1349) | 0.2439 (1342) | 0.2125 (1321) | 0.2167 (1305) | 0.2105 (1314) | 0.2184 (1329) |
| Trunc-n (n = 5) | 0.2579 (1360) | 0.2578 (1356) | 0.2282 (1342) | 0.2331 (1330) | 0.2246 (1333) | 0.2282 (1341) |

**English (Table 5, p. 187)**

| Representation | BM25 | TF-IDF | BB2 | InL2 | IFB2 | LM |
|---|---:|---:|---:|---:|---:|---:|
| Baseline | 0.2975 (2236) | 0.2981 (2232) | 0.2686 (2210) | 0.2633 (2204) | 0.2615 (2210) | 0.2543 (2182) |
| YASS | 0.3122 (2337) | 0.3133 (2337) | 0.2837 (2338) | 0.2769 (2312) | 0.2745 (2338) | 0.2652 (2278) |
| FCB V-1 | 0.3012 (2278) | 0.302 (2277) | 0.2723 (2268) | 0.2662 (2249) | 0.2651 (2269) | 0.257 (2221) |
| SNS | 0.3068 (2278) | 0.3065 (2279) | 0.2753 (2250) | 0.2709 (2240) | 0.2734 (2249) | 0.2611 (2224) |
| GRAS | **0.3145** (2310) | **0.3155** (2311) | **0.2849** (2294) | **0.2796** (2280) | **0.2763** (2290) | **0.2661** (2248) |
| Trunc-n (n = 6) | 0.3155 (2309) | 0.3164 (2310) | 0.2858 (2295) | 0.2818 (2277) | 0.2772 (2290) | 0.267 (2247) |

Boldface is as printed. It marks the best **stemmer** per column and never Trunc-n, even where Trunc-n is higher (Hindi BM25; all English columns).

### Relative MAP change vs no stemming [computed]

| | BM25 | TF-IDF | BB2 | InL2 | IFB2 | LM |
|---|---:|---:|---:|---:|---:|---:|
| Hindi YASS | −0.54% | +0.11% | +0.72% | −3.17% | −1.32% | −1.51% |
| Hindi FCB | +0.72% | +0.74% | +0.56% | +0.77% | +0.59% | +0.77% |
| Hindi SNS | +0.88% | **+2.99%** | +1.39% | +0.92% | +2.26% | +1.04% |
| Hindi GRAS | +1.15% | +1.12% | −1.44% | −2.40% | −1.69% | −1.36% |
| Hindi Trunc-5 | +2.23% | +2.38% | +0.37% | −0.77% | +0.13% | +0.99% |
| Gujarati YASS | +2.67% | +2.67% | +3.67% | +3.26% | +2.77% | +2.00% |
| Gujarati FCB | +0.96% | +0.21% | +0.73% | +0.30% | +0.49% | +0.48% |
| Gujarati SNS | +10.29% | +10.17% | +16.85% | **+20.78%** | +15.88% | +11.46% |
| Gujarati GRAS | +1.79% | +1.67% | +4.12% | +8.79% | +4.16% | +4.25% |
| Gujarati Trunc-5 | +7.46% | +7.46% | +11.81% | +17.02% | +11.13% | +8.93% |
| English YASS | +4.94% | +5.10% | +5.62% | +5.17% | +4.97% | +4.29% |
| English FCB | +1.24% | +1.31% | +1.38% | +1.10% | +1.38% | +1.06% |
| English SNS | +3.13% | +2.82% | +2.49% | +2.89% | +4.55% | +2.67% |
| English GRAS | +5.71% | **+5.84%** | +6.07% | +6.19% | +5.66% | +4.64% |
| English Trunc-6 | +6.05% | +6.14% | +6.40% | +7.03% | +6.00% | +4.99% |

Recomputing the authors' headline claims (Abstract, p. 181; Sec. 6, p. 187):

- "SNS ... improves ... MAP ... by 2.98% in Hindi": this is SNS **TF-IDF** (0.4455 → 0.4588) **[computed: +2.99%; printed value truncated]**. On BM25, SNS gives +0.88%.
- "20.78% in Gujarati": this is SNS **InL2** (0.1992 → 0.2406) **[computed: +20.78% ✓]**. InL2 is one of the DFR models the authors call poor. On BM25, the best Gujarati model, the gain is +10.29% (0.2400 → 0.2647; +0.0247 absolute) **[computed]**. The paper does not say which model the percentages come from.
- "GRAS ... improves a MAP score by 5.83% in English": GRAS **TF-IDF** (0.2981 → 0.3155) **[computed: +5.84%; printed value truncated]**.
- "The SNS stemmer provides the best MAP score in Hindi and Gujarati" (p. 186): true for all 6 Gujarati columns. In Hindi it holds for 5 of 6 columns among stemmers; in the BM25 column GRAS is higher (0.4495 vs 0.4483, as the boldface shows) **[computed]**.
- "the GRAS stemmer provides the best MAP score in English" (p. 186): true among the four stemmers in all 6 columns. **Trunc-6 is higher than GRAS in all 6 English columns** (e.g. BM25 0.3155 vs 0.3145) **[computed]**. The authors describe Trunc-n as offering "similar performance to the SNS stemmer in Hindi and Gujarati" (p. 186) and as performing "similarly to the best-stemming approaches" (Conclusion, p. 187).
- **Hindi is not uniformly improved:** 9 of 30 (stemmer or Trunc-n) × model cells are below the no-stemming baseline: YASS in 4 models, GRAS in 4, Trunc-5 in InL2 **[computed]**. The authors acknowledge "a relatively poor performance in Hindi" (p. 187). Gujarati and English: 0 of 30 below baseline **[computed]**.
- **Probabilistic models best:** BM25 and TF-IDF have the highest MAP in every row of all three tables, and their baselines differ by ≤ 0.0011 MAP **[computed]**. This supports the authors' statement (p. 186) that BM25/TF-IDF perform best and DFR models "exhibit poor performance".

### Rel.Ret: recall-type effect [computed]

- Every stemmer and Trunc-n **increase Rel.Ret over the baseline in every Hindi and English cell**. In Gujarati, every cell except YASS-LM (1287 vs 1289) is also higher.
- The increase happens even when MAP falls. Example: Hindi YASS BM25 has Rel.Ret 1683 → 1764 (+81, +4.8%) while MAP goes 0.4444 → 0.442 (−0.54%). Similar pattern: Hindi GRAS in the DFR models and LM.
- Interpretation (ours): in Hindi, conflation retrieves additional relevant documents, but ranks them (or displaces others) so that precision-weighted AP does not improve.
- **Inference [computed; assumes the same retrieval depth and qrels for both runs]:** a net Rel.Ret gain of Δ implies that the stemmed run retrieved **at least Δ** relevant (query, document) pairs that the unstemmed run did not. For Hindi YASS BM25 that is ≥ 81 pairs over 50 queries. The paper does not report the actual unique or overlapping relevant sets, so the true number of "swapped" documents is unknown.

### Figures 1–3: per-query analysis (pp. 186, 188)

The configuration shown per language is SNS + TF-IDF for Hindi (Fig. 1), SNS + **InL2** for Gujarati (Fig. 2), and GRAS + TF-IDF for English (Fig. 3). The text says: "we consider the best retrieval models and stemming approaches" (p. 186). For Gujarati the best model is BM25/TF-IDF, not InL2 (Table 4).

| Language (config) | Text (p. 186): improved / reduced | Unchanged implied [computed] | Visible bars in figure: up / flat / down [visual count, approximate] |
|---|---|---:|---|
| Hindi (SNS, TF-IDF) | 35 / 15 | 0 | 31 / 4 / 15 |
| Gujarati (SNS, InL2) | 38 / 8 | 4 | 31 / 11 / 8 |
| English (GRAS, TF-IDF) | 32 / 12 | 6 | 30 / 8 / 12 |

- Hurt shares (text counts): 30% (Hindi), 16% (Gujarati), 24% (English) **[computed]**.
- The "reduced" counts in the text match the negative bars in the figures exactly. The "improved" counts are higher than the visibly positive bars. The difference presumably consists of gains too small to be visible at the plotted scale, but this cannot be confirmed from the paper.
- Extremes are clipped: Hindi queries 23 and 6 reach the −0.5 axis floor, and queries 12 and 37 the +1.0 ceiling (Fig. 1). Gujarati query 6 reaches the +3 ceiling (Fig. 2).
- The largest reductions are about −0.9 in Gujarati (query 23) and about −0.18 in English (query 48) [approximate].
- The authors conclude: "the stemming performs better in Gujarati, and English than in Hindi" (p. 186).

## 10. Statistical evidence

- **Significance tests:** NOT_REPORTED (none). Hull (1996) is cited as observing that the stemmer "performs moderately in English and does not produce statistically significant results" (p. 182), but the authors do not test their own differences.
- **Confidence intervals:** NOT_REPORTED.
- **Runs / seeds:** deterministic pipeline, single run. The dependence on the choice of tuning queries is not assessed.
- **Ablation / sensitivity:** parameter sweeps are mentioned (Algorithm 1 step 7; Sec. 3.2) but only the best setting per stemmer and language is reported (Table 1). The sweep results are NOT_REPORTED, so sensitivity to the thresholds cannot be judged. The six ranking models act as a robustness check across models.
- **Per-query analysis:** **present but limited.**
  - Helped/hurt counts and a sorted bar chart of per-query relative change, one configuration per language (Figs. 1–3).
  - The comparison is between two **lexical representations** of the same channel. No reasons for the hurt queries are given, and no query features (length, inflection, named entities, etc.) are analysed.
  - The helped/hurt threshold is not stated; it is presumably any non-zero change.
- **Overlap / unique relevant hits / oracle union** between representations or channels: **NOT_REPORTED**. Only net Rel.Ret totals are given.

## 11. Strengths

- A full representation × model grid (6 × 6) in three languages, which makes the **model dependence** of the stemming effect visible. Examples: Hindi GRAS helps BM25/TF-IDF but hurts the DFR models and LM; Gujarati SNS gains range from +10% (BM25) to +21% (InL2).
- Includes **BM25** and a simple **prefix-truncation** control. Trunc-n turns out to be close to the best stemmer (higher in all English columns and Hindi BM25; within ~0.01 MAP below SNS elsewhere **[computed]**), which is a useful negative-control-type finding.
- Reports Rel.Ret next to MAP, which exposes the recall-up / MAP-flat pattern in Hindi.
- Per-query helped/hurt evidence, with the whole distribution shown in Figs. 1–3.
- Standard, publicly known FIRE test collections of realistic size (~0.3–0.4M documents).
- Algorithms and chosen parameters are stated (Table 1), which gives partial reproducibility.

## 12. Limitations

### Stated by the authors

- Stemming gives "a relatively poor performance in Hindi" (Conclusion, p. 187).
- Framed as future work rather than as a limitation: stemming is "less explored in the Dravidian language family" (Telugu, Tamil, Kannada, Malayalam), which this study (Indo-European languages only) does not cover (p. 188).
- Machine-learning and deep-learning stemmers are not studied (future work, p. 188).
- The authors state no other limitations.

### Inferred from the experimental design

1. **Parameters tuned on the evaluation queries.** Stemmer thresholds and n were chosen by the best MAP on the same 50 queries, while the baseline has nothing to tune. Small gains (Hindi BM25 +0.7% to +2.2%) are therefore not credible without a held-out test.
2. **No significance testing** with 50 queries per language. Most Hindi and English differences (≤ 0.02 MAP) cannot be interpreted as reliable.
3. **Selective headline numbers.** The abstract's percentages come from different ranking models per language, and the Gujarati figure comes from InL2, where the baseline is weakest. The BM25 gains are smaller: +0.9% (Hindi SNS), +10.3% (Gujarati SNS), +5.7% (English GRAS) **[computed]**.
4. **The "best stemmer" claims exclude Trunc-n**, which ties or beats the best stemmer in several columns. RQ2 explicitly includes Trunc-n as an option.
5. **Preprocessing is unreported:** stop-words, tokenization, normalization of Indic scripts, lowercasing, BM25 k1/b and the retrieval depth. The effects cannot be separated from these choices.
6. **Only title queries** (short). The effect of stemming may differ for longer queries; this is not tested.
7. **Per-query analysis for one configuration per language only**, with no explanation of the hurt queries and no query features. The Gujarati configuration (InL2) is not the best model, contrary to the text.
8. **Net totals only.** Rel.Ret is summed over queries and is net of gains and losses, so it cannot show which relevant documents each representation uniquely retrieves.
9. **No lemmatization, no rule-based stemmer, no n-grams, no dense retrieval, no fusion.** RQ2's "most suitable" is limited to unsupervised stemmers and truncation within lexical models.
10. **English is treated as an "Indian language"** and the English collection is FIRE news. English results are not a general English IR finding.

## 13. What the work proves

Within the stated limits (tuned on test queries, no significance tests, 50 title queries):

- On FIRE 2011 **Gujarati**, corpus-based stemming (SNS) and prefix truncation (Trunc-5) consistently raise MAP over no stemming across all six lexical models. On BM25: 0.2400 → 0.2647 (SNS) and 0.2579 (Trunc-5) (Table 4). The size (+7% to +21% relative) and the consistency across models make the direction plausible despite the missing tests.
- On FIRE 2011 **English**, YASS, GRAS and Trunc-6 give consistent gains of about +4% to +7% over no stemming in all models (Table 5).
- On FIRE 2011 **Hindi**, the effect of language-independent stemming on MAP is **small and model-dependent**: −3.2% to +3.0% across cells, and 9 of 30 cells are below baseline (Table 3). Rel.Ret still rises in every cell.
- **Simple prefix truncation is close to the best tested unsupervised stemmer** in all three languages. It is the highest MAP in all English columns and in the Hindi BM25 column; elsewhere it is below SNS by at most ~0.01 MAP (all 6 Gujarati columns, 5 of 6 Hindi columns) **[computed]** (Tables 3–5).
- **The effect of changing the lexical representation is heterogeneous across queries**, even for the best configuration: 15, 8 and 12 of 50 queries are hurt in Hindi, Gujarati and English (p. 186; Figs. 1–3).
- In these collections, **BM25 and Terrier's TF-IDF outperform the DFR models and the Hiemstra LM** under every representation (Tables 3–5).

## 14. What the work does NOT prove

- **That the stemming gains are statistically significant**, or that they would hold on unseen queries, because parameters were tuned on the test set.
- **That SNS or GRAS is "the best" stemmer** in any strong sense. Trunc-n beats GRAS in all English columns and is within ~0.01 MAP of SNS in Hindi and Gujarati, differences between stemmers are often < 0.005 MAP, and no tests are given. The paper's own text also contradicts itself on GRAS vs SNS (§19).
- **That stemming improves retrieval "in different Indian languages" in general.** Hindi shows mixed effects, and only two Indian languages are tested (plus English).
- **Anything about lemmatization** or linguistically informed normalization.
- **Anything about dense or semantic retrieval, hybrid retrieval, or lexical–dense complementarity.** None is tested.
- **Which relevant documents a representation uniquely contributes.** Only net Rel.Ret totals exist; there are no overlap, unique-hit or oracle-union measurements.
- **Why some queries are hurt.** There is no query-feature or error analysis.
- **Anything about agglutinative or Turkic languages.**

## 15. Relationship to current Uzbek evidence

- **No Uzbek or Turkic data.** Hindi and Gujarati are inflectional Indo-Aryan languages. Uzbek is agglutinative with long suffix chains. Gujarati's much larger gain than Hindi's shows that the size of the benefit is language-specific even among closely related languages. It cannot be transferred to Uzbek; it has to be measured.
- The situation is similar to Uzbek in one respect: stemmers and analyzers for Uzbek exist (Xusainova, Bakaev, Elov; `MASTER_INDEX` A/C), but no qrels-based comparison of them against **language-independent baselines** (corpus-based stemmers, prefix truncation) exists in the index. This paper, like McNamee et al. 2009 (`CR000688`) and Haddad & Bechikh Ali 2014 (MORPH-002, 4/5-prefix truncation competitive in Turkish), shows that such baselines are strong. They should therefore appear in the Uzbek design as controls.
- Related cards in the index:
  - **Paik et al. 2013** (`CR000566`, TOIS; same research line: SNS and GRAS are that group's stemmers): SNS/GRAS on FIRE Marathi/Bengali with a per-query robustness index, but a Dirichlet LM and no BM25.
  - **McNamee et al. 2009** (`CR000688`): truncation and n-grams across 18 languages, including Hindi/Bengali/Marathi (FIRE '08); trun5 is strong.
  - **Regmi et al. 2026** (`CR000218`, Nepali lemmatization IR): another South Asian low-resource lexical-representation study.
  Together they form a consistent "lexical representation matters, is language- and query-dependent, and simple baselines are competitive" cluster. None of them has a dense channel.

## 16. Relationship to CURRENT_GAP

**Classification:** *supports (background)* + *no material effect on the residual core*.

- **Supports** the premise of v0.8 that changing the lexical channel's morphological representation has **heterogeneous, query-level effects**:
  - 16–30% of queries are hurt even by the best stemmer;
  - the effect depends on the ranking model;
  - Rel.Ret rises while MAP stays flat or falls, i.e. the representation change alters *which* relevant documents are retrieved and not only how well they are ranked.
  This is indirect motivation for measuring set-level changes (unique hits) rather than only aggregate MAP.
- **Confirms as occupied** (already non-claims in v0.8): "raw/stem comparisons in a morphologically complex low-resource language have not been done", and "the per-query effect of stemming has not been examined". Both are classical (see also `CR000566`).
- **No material effect on the residual core.** None of the v0.8 core elements is present:
  - lemma variant;
  - a fixed dense retriever D;
  - fusion H_raw/H_stem/H_lemma;
  - unique relevant hits / overlap / oracle union between the lexical and dense channels;
  - change in incremental hybrid gain;
  - link of the changes to query features.
- **Qualification of the triage flag `carries_complementarity_evidence = YES`:** the "complementarity" in this paper is between two lexical representations, measured as per-query AP gain/loss and net Rel.Ret. It is not relevant-set complementarity, and not lexical–semantic complementarity.

**Proposal:** keep v0.8 refined unchanged. Optionally cite the paper in the evidence boundary as a 2025 example showing that "raw vs corpus-based stem vs truncation" is still being studied as lexical-only IR, without a dense channel or set-level decomposition. This is a proposal only; `CURRENT_GAP.md` has not been edited.

## 17. Implications for our research design

- **Lexical representation set.** Consider adding **`BM25_trunc-n`** (n tuned on dev, e.g. from 4–6) as a language-independent control next to `BM25_raw / BM25_stem / BM25_lemma`, and possibly one unsupervised corpus-based stemmer (e.g. GRAS or YASS) as a "no linguistic resources" stem variant. Across this paper (vs unsupervised stemmers), `CR000688` and MORPH-002 (vs linguistic stemmers), truncation keeps coming out as strong or nearly as strong as stemming. A lemma advantage for Uzbek should therefore be shown against it, not only against raw.
- **Tuning protocol.** Any stemmer or truncation parameter must be selected on a **dev query set**, never on the test queries. The same applies to BM25 k1/b and fusion weights. This paper's design shows how test-set tuning inflates small gains.
- **Fix the lexical model.** The stemming effect interacts with the ranking model (Hindi GRAS: + on BM25, − on the DFR models). The primary comparison should fix **one BM25 configuration**, with parameters reported. A second lexical model (e.g. a query-likelihood LM) can serve as a robustness check only.
- **Measure sets, not only totals.** Where this paper reports only net Rel.Ret, our protocol should report per query:
  - relevant documents retrieved by `BM25_stem` but not `BM25_raw` (and vice versa) at k = 100 / 1000;
  - the same against D;
  - how the lexical-unique set with respect to D changes between variants.
  The net Rel.Ret gain is only a lower bound on the stem-unique set (§9).
- **Per-query reporting.** Report helped / hurt / unchanged counts with an explicit threshold (e.g. |ΔAP| ≥ 0.01 or a relative 5%), a paired test (Wilcoxon / randomization) and the full sorted distribution, as in Figs. 1–3 but with units stated and no clipping.
- **Query features.** Add a per-query error analysis for hurt queries: over-conflation (different meanings merged), named entities, short titles. This is exactly what the paper omits and our taxonomy targets.
- **Query length.** The paper uses title-only queries. If our benchmark has both short and descriptive queries, report the morphology effect separately by query length (cf. MORPH-001, Can et al. 2008).
- **Metrics.** Report MAP/nDCG together with **Recall@k at candidate depth**. The Hindi pattern (Rel.Ret up, MAP flat) suggests that the effect of morphology may sit in deep recall, which is where it matters for a hybrid's candidate union.

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| Stemming | Cutting words down to a shared part so that different forms match | Many-to-one mapping from word forms to index terms by affix removal |
| Language-independent (statistical) stemmer | A stemmer that learns what to cut from the collection itself, without grammar rules | Unsupervised induction of conflation classes from corpus statistics (string similarity, suffix frequency, co-occurrence, graphs) |
| YASS | Groups words that look alike from the start of the word | Complete-linkage clustering with prefix-weighted string distance D3 and threshold θ (Majumder et al. 2007) |
| FCB | Finds frequent endings and treats the shared beginning as the stem | Suffix-frequency-based equivalence classes with prefix-strength threshold δ (Paik & Parui 2011) |
| SNS | Words that share a beginning *and* appear in the same documents are merged | Co-occurrence graph (CO, RCO) + prefix constraints; stem = longest prefix of a connected component (Paik et al. 2011b) |
| GRAS | Builds a graph of words linked by common ending pairs; well-connected "pivot" words define the groups | Suffix-pair graph with pivot and cohesion δ (Paik et al. 2011a) |
| Trunc-n | Keep only the first n letters of every word | Prefix truncation of index and query terms |
| Terrier | An open-source research search engine with many ranking models | IR platform (Univ. of Glasgow) |
| BM25 / TF-IDF | Word-matching scores: rare shared words and repeated words count more, with document-length adjustment | Probabilistic / tf·idf term weighting |
| DFR models (BB2, InL2, IFB2) | Scores based on how surprising a word's frequency in a document is compared with chance | Divergence-from-randomness term weighting |
| Hiemstra LM | Ranks documents by how likely they are to "generate" the query | Query-likelihood language model with smoothing |
| MAP | Average of per-query average precision; rewards finding relevant documents early | mean_q AP(q) |
| Rel.Ret | How many relevant documents appear anywhere in the returned lists (all queries together) | Σ_q \|Rel(q) ∩ Ret_k(q)\|, depth k not reported |
| Per-query analysis | Looking at each query separately rather than at the average | Distribution of per-query score differences between two systems |
| Complementarity (project term) | Each channel or representation finds relevant documents the other misses | Unique relevant hits, overlap, oracle-union gain |

## 19. Open questions / verification needed

1. **Internal inconsistency:** "the GRAS stemmer required less computational effort and performed best in different Indian languages" (Sec. 6, p. 187) vs "The SNS stemmer performs best and improves a MAP score of 2.98% in Hindi, 20.78% in Gujarati" (same paragraph), the Abstract, and Sec. 6, p. 186. The claimed lower computational effort of GRAS is not measured anywhere in the paper.
2. **Which model produced the headline percentages?** Not stated. Our recomputation assigns them to TF-IDF (Hindi), InL2 (Gujarati) and TF-IDF (English).
3. **Per-query configuration:** the text says "best retrieval models", but Fig. 2 uses InL2 for Gujarati (Table 4: BM25 is best).
4. **Per-query counts** (text 35/15, 38/8, 32/12) vs visible bars (31/4/15, 31/11/8, 30/8/12) [visual count, approximate]. The threshold for "improves" is not stated. The y-axis unit ("% gain" with values up to 3) is ambiguous.
5. **Parameter mismatches:** Algorithm 3 (L1 = 3, L2 > 5) vs Table 1 SNS for Hindi/Gujarati (and English L2 = 5, not > 5). Algorithm 4 (η = 1, δ) vs Table 1 GRAS (α = 4/4/6). Which model and which query set were used for tuning: NOT_REPORTED.
6. **YASS D3 formula as printed** (exponent `i − x`, p. 183): we do not verify it against Majumder et al. (2007). Anyone implementing YASS should use the original paper.
7. **Retrieval depth for Rel.Ret, number of relevant documents per collection, stop-words, BM25 parameters, FIRE topic numbers:** NOT_REPORTED.
8. **DOI** `10.26615/978-954-452-105-9-020` (printed): not resolvable from here; to confirm.
9. **Title variant:** the printed title differs slightly from the ACL Anthology / PDF-metadata title (§1). Use the ACL Anthology form for citation, or the researcher decides.

## 20. Decision after deep dive

- **Keep current gap?** Yes. v0.8 refined remains valid (§16).
- **Modify gap?** No change proposed. Optionally list the paper in the evidence boundary as a 2025 lexical-only representation study with per-query helped/hurt evidence and no dense channel (researcher's decision).
- **Add decision?** Proposed for `decisions/DECISIONS.md` (researcher's decision):
  - "All lexical-representation parameters (stemmer thresholds, truncation length, BM25 k1/b) are tuned on dev queries only";
  - "Per-query helped/hurt counts are reported with an explicit threshold and a paired significance test";
  - "Set-level unique-hit counts replace net relevant-retrieved totals".
- **Add experiment?** Optional: include `BM25_trunc-n` (n selected on dev) as a language-independent control in the raw/stem/lemma × D design, and report its unique hits with respect to D alongside the other variants.
- **Add citation to Chapter I?** Yes, §1.1 (lexical IR and morphological normalization in low-resource languages: language-independent stemmers, truncation competitive, model- and query-dependent effects). Cite together with `CR000566` and `CR000688`. Not for §1.2/§1.3.
- **Proposed `MASTER_INDEX.md` row** (to add after approval):

| MORPH-037 | Sahu & Pal — *A study on the language independent stemmer in the Indian language IR* (GlobalNLP workshop @ RANLP 2025, pp. 181–189) — [deep dive](deep-dives/2025_Sahu_Pal_Language_Independent_Stemmer_Indian_Language_IR.md) | 2025 | B | MEDIUM | FIRE 2011 Hindi/Gujarati/English (50 title queries each): no stemming vs YASS/FCB/SNS/GRAS vs Trunc-n across 6 Terrier models incl. BM25. BM25 MAP: Gujarati 0.240→0.265 (SNS), English 0.2975→0.3145 (GRAS)/0.3155 (Trunc-6), Hindi 0.444→0.450 (GRAS)/0.454 (Trunc-5); Hindi 9/30 cells below baseline; Trunc-n ≈/≥ best stemmer. Per-query helped/hurt 35/15, 38/8, 32/12 (lexical vs lexical). Parameters tuned on test queries; no significance tests; no lemma, no dense, no fusion, no overlap/unique-hit analysis. Text claims partly inconsistent with tables. |
