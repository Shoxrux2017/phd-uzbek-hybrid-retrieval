# Mothe & Tanguy (2007): Linguistic Analysis of Users' Queries: Towards an Adaptive Information Retrieval System

**Targeted deep-dive status:** COMPLETED (AI-assisted, pending researcher review)
**Completed:** 2026-09-28
**Verification:** independent AI verifier pass 2026-09-28; 4 findings addressed.
**Literature ID:** `HYB-013` (assigned 2026-09-28, approved by researcher)
**Systematic-review record:** `CR001352`. Full-text triage: INCLUDE, reading priority HIGH, tier "1 — прямо по теме пробела", `carries_complementarity_evidence = YES` (re-assessed below: only in a weak, system-group sense; see §10, §16)
**Provenance:** AI-assisted deep dive (Claude). The paper was read in full from the supplied PDF, which is the **HAL author version** (`halshs-00287776`, 9 PDF pages; PDF p. 1 is the HAL cover sheet, the paper runs PDF pp. 2–9, without printed page numbers). Locations below are given as "PDF p. N". Page images of PDF pp. 2–9 were checked visually, including zoomed crops of Fig. 2 (dendrogram leaves, p. 6) and Fig. 3a (PCA of topics, p. 8); every number from Tables 1–5 was compared against the page images. Numbers computed by us are marked **[computed]**.
**Source rule:** **the paper is the primary and only authoritative source.** No code, later papers or TREC run descriptions were used to say what the authors did. The web was used only for the bibliographic record (marked "bibliographic check").
**Reliability:** **B**. Peer-reviewed IEEE conference paper (SITIS 2007), but a short exploratory study: no significance tests, post-hoc visual grouping, and several internal inconsistencies (§9, §19). Not at the level of the A-category venues in the project scale.

---

## Кратко для исследователя (RU)

- **Что сделано.** Для 49 тем TREC 2002 Novelty (английский язык) авторы:
  - автоматически вычислили 9 лингвистических признаков запроса (заголовок + описание темы): 3 морфологических (средняя длина слова LENGTH, среднее число морфем на слово MORPH по CELEX, доля слов с суффиксами SUFFIX), 5 синтаксических и 1 семантический (многозначность по WordNet);
  - кластеризовали темы по этим признакам (иерархическая агломеративная кластеризация, евклидово расстояние, **без нормализации признаков**) → 6 кластеров;
  - отдельно построили PCA по матрице полноты (recall) «тема × система» для 42 систем/вариантов и визуально выделили две группы систем по 5 прогонов;
  - сопоставили кластеры тем с группами систем (Table 5, PDF p. 8).
- **Главные числа** (Table 5, PDF p. 8), средняя полнота Group 1 / Group 2:
  - «синий» кластер 0.42 / 0.26 (единственный, где выигрывает Group 1);
  - «оранжевый» 0.24 / 0.62; «зелёный» 0.50 / 0.77; «красный» 0.22 / 0.29;
  - все запросы 0.32 / 0.46.
  - То есть есть **перекрёстное взаимодействие** «тип запроса × группа систем», но Group 2 лучше в 3 из 4 показанных кластеров.
- **Морфология здесь — только признаки запроса**, а не варианты лексического представления. Нет raw/stem/lemma-индексов, системы — «чёрные ящики» TREC; их обработка (стемминг и т. п.) в статье не описана.
- **Вклад морфологических признаков в кластеры фактически не выделен.** Авторы сами пишут, что отдельные признаки не коррелируют с кластерами. По 8 темам из Table 3 на MORPH и SUFFIX приходится ≈0.3% суммарной дисперсии, на SYNT DEPTH и POLYSEM — ≈93% **[computed]**; при ненормализованном евклидовом расстоянии кластеры почти целиком определяются синтаксической глубиной и многозначностью.
- **Чего нет:**
  - BM25 (упоминается лишь «вероятностная модель» во введении), плотного поиска, нейросетей;
  - реального fusion — только предложение на будущее (Sec. 4);
  - перекрытия результатов, уникально найденных релевантных предложений, oracle union;
  - тестов значимости, размеров кластеров, двух из шести кластеров в Table 5.
- **Задача — не ad hoc поиск документов:** выбор релевантных *предложений* внутри заранее данных релевантных документов (TREC Novelty, в среднем 22.3 документа и 1321 предложение на тему, Table 1). Метрика — только полнота множества, без точности.
- **Внутренние несоответствия:** 50 тем в аннотации vs 49 в Table 1 / Sec. 4; «6 кластеров» vs 4 в Table 5 (на Fig. 3a видны ещё пурпурные ромбы и оранжевый перевёрнутый треугольник); «первые 10 тем» vs 8 строк Table 3; ссылка на «section 4» вместо Sec. 3; колонка «R*P» в Table 2 не равна ни произведению R·P, ни F; примеры в тексте (темы 314, 317, 363) относятся к кластеру, которого нет в Table 5.
- **Для нашего gap:** ранний (2007) пример идеи «лингвистические, в т.ч. морфологические, признаки запроса связаны с тем, какая система/группа систем выигрывает, → основа для fusion». Подтверждает, что «анализ типов запросов» и «query-dependent выбор системы» не новы (уже в v0.8 как non-claims). Ядро v0.8 (raw/stem/lemma × фиксированный D → перекрытие / уникальные попадания → прирост гибрида) **не затрагивает**. Предложение: gap не менять.
- **Практическая польза для нас:**
  1. MORPH (морфем на слово) и SUFFIX (доля аффиксированных слов) — готовые прототипы узбекских признаков запроса (для узбекского — через морфоанализатор: число аффиксов на слово).
  2. Признаки запроса перед кластеризацией/регрессией нормализовать (z-score), иначе «морфологические» признаки растворяются в масштабе других.
  3. Не выбирать группы систем/условия визуально по тем же данным, на которых затем проверяется эффект; проверять взаимодействие «признак запроса × условие» статистически на уровне запросов.

---

## 1. Bibliographic record

- **Authors:** Josiane Mothe (IRIT, UMR 5505, Université de Toulouse; IUFM Toulouse), Ludovic Tanguy (CLLE-ERSS, UMR 5263, CNRS & Université de Toulouse) (PDF p. 2)
- **Year:** 2007
- **Venue:** *2007 Third International IEEE Conference on Signal-Image Technologies and Internet-Based System (SITIS 2007)*, Shanghai, China, 16–18 December 2007 (bibliographic check: Crossref)
- **Pages:** 77–84 (bibliographic check: Crossref); the assignment metadata gives "9" pages, which corresponds to the HAL PDF including its cover sheet
- **Publisher:** IEEE
- **DOI:** `10.1109/SITIS.2007.81` (bibliographic check: Crossref)
- **Official record:** https://ieeexplore.ieee.org/document/4618761/ (bibliographic check: web search result; the page itself could not be rendered)
- **Version read:** HAL `halshs-00287776` v1, submitted 12 June 2008 (PDF p. 1). The version of record was not compared.
- **Funding (stated):** EU FP6 project WS-Talk (COOP-006026) (PDF p. 9)
- **Source type:** peer-reviewed conference paper (IEEE)
- **Reliability:** B
- **Full text available:** yes (`07_full_text/pdfs/CR001352.pdf`)

## 2. Why this work matters to the PhD

It is an early, explicit statement of the idea behind query-dependent fusion: **linguistic features of a query, including morphological ones, may predict which kind of system succeeds on it**, so a fusion method could be driven by query type (Sec. 4, PDF pp. 8–9). It builds on the authors' own earlier work on linguistic features and query difficulty (ref. [12], Mothe & Tanguy 2005, cited as showing that the average polysemy of query terms is correlated with recall; PDF p. 3).

| Axis | Relation |
|---|---|
| Lexical retrieval | Indirect. 42 TREC Novelty 2002 runs are analysed as black boxes; their retrieval models and preprocessing are **not described** |
| Semantic retrieval | Absent (2007; no neural or dense retrieval). "Semantic" here means a WordNet polysemy feature of the query |
| Hybrid retrieval | **Proposed only.** Fusion is future work; no fused run is built or evaluated |
| Uzbek morphology | Indirect: English queries; morphological complexity measured by morphemes per word and suffixation, which are natural analogues for agglutinative Uzbek |
| Low-resource retrieval | Not relevant (English, TREC) |
| Current gap | Historical precedent for query-feature analysis and query-type-driven system selection (already non-claims in v0.8). Does not touch morphology-induced complementarity (§16) |

## 3. Research problem

### Simple explanation

Standard IR evaluation averages results over ~50 queries, which hides the fact that different systems fail on different queries. The authors ask whether cheap, automatically computed linguistic properties of a query (long or complex words, complex syntax, ambiguous words) can explain those differences, and so tell us in advance which system to use for which query.

### Formal formulation

Given a set of topics T (|T| = 49) and runs S (|S| = 42) with per-topic recall R(s, t):
1. describe each topic t by a feature vector f(t) ∈ ℝ⁹ (Sec. 2.5);
2. partition T into clusters C₁…C_k from f(t) alone, without performance data (Sec. 3.1);
3. analyse the matrix R(s, t) by PCA to find groups of systems (Sec. 3.2);
4. check whether mean recall of system groups differs by topic cluster (Table 5).

Authors' stated aim (Sec. 1, PDF p. 3): "can we identify some characteristics in users' queries that can explain the variations between systems".

## 4. Main idea

### Simple explanation

Measure each query with nine simple linguistic numbers, group similar queries together, then look at which systems do well on each group. If one family of systems wins on one group and another family on a different group, a meta-system could route each query to the right family, or fuse them.

### Concrete example

- The paper's sample topic 310 (Fig. 1, PDF pp. 3–4): Title "Radio Waves and Brain Cancer"; Description "Evidence that radio waves from radio towers or car phones affect brain cancer occurrence."
- Its features (Table 3, PDF p. 6): LENGTH 4.64, MORPH 1.11, SUFFIX 0.08, CONJ 0.03, PREP 0.13, VERBS 0.14, SYNT DEPTH 4.00, SYNT DIST 1.73, POLYSEM 4.71.
- Worked example from the text (Sec. 3.2, PDF p. 7): on topic 314 run ntu1 has recall 0.72 vs a mean over systems of 0.41; on topic 317 run ntu1 has recall 0.91 (the best for this topic), while the mean over systems is 0.42; on topic 363 run pircs02 has recall 0.9 vs a mean of 0.41.

### Formal method

- Features: occurrence features are proportions of query words (e.g. PREP = 0.12 means 12% of words are prepositions); the others are averages over words or sentences (PDF p. 5).
- Clustering: agglomerative hierarchical clustering (HAC), Euclidean distance, unnormalized features, each feature "considered as equally important" (PDF pp. 5–6). The linkage criterion is **NOT_REPORTED**.
- PCA: "characters" (observations) = topics, "variables" = systems, measure = recall; displayed on axes 1 and 3, which "correspond to 50% of the total inertia" (PDF p. 7).

## 5. Architecture / algorithm

1. **Topic preprocessing** (PDF p. 5): title + description parts only; the narrative is ignored, "as most IR systems do". POS tagging and lemmatization with TreeTagger; dependency parsing with SYNTEX.
2. **Morphological features** (PDF pp. 4–5):
   - LENGTH: average word length in characters;
   - MORPH: average number of morphemes per word from the CELEX database (40,000 base word forms), e.g. "additionally" = add+ition+al+ly. Words missing from CELEX count as mono-morphemic;
   - SUFFIX: "number of suffixed words", detected with a list of the most common English suffixes the authors compiled (e.g. "postmenopausal" → -al). Expressed as a proportion (Table 3 values 0.08–0.19). The suffix list itself is **NOT_REPORTED**.
3. **Syntactic features**: CONJ, PREP, VERBS (proportions); SYNT DEPTH (hierarchical depth of the parse); SYNT DIST (average span of a syntactic link).
4. **Semantic feature**: POLYSEM, the average number of WordNet synsets per word; words absent from WordNet get 1.
5. Authors state they "manually checked each feature detection technique" (PDF p. 5); no error rates are given.
6. **HAC clustering** → dendrogram (Fig. 2, PDF p. 6) → 6-class partition chosen by inter-cluster distance.
7. **PCA of the recall matrix** (42 runs × 49 topics) → two groups of five runs selected **visually** at the periphery of the correlation circle (Fig. 3b, PDF p. 8):
   - Group 1: ntu1, ntu2, ntu3, colmerg, cmuBw;
   - Group 2: pircs01, pircs02, pircs03, thunv2, CIIRNew.
   - "These groups are determined visually and chosen because they are orthogonal considering the first axes" (PDF p. 7).
8. **Projection** of the topic clusters onto the PCA plot (colours/shapes in Fig. 3a) and averaging of recall per cluster × group (Table 5).

No retrieval system is built by the authors. What the 42 runs do (model, stemming, stop-words, expansion) is **NOT_REPORTED**.

## 6. Data

- **Collection:** TREC 2002 Novelty track (Sec. 2.1–2.2, Table 1, PDF pp. 3–4).
- **Language / domain:** English; news-type TREC documents (the paper says only "from previous TREC tasks").
- **Topics:** 49 (Table 1; Sec. 2.2; Sec. 4). The abstract says 50 (PDF p. 2): internal inconsistency.
- **Documents per topic:** avg 22.3 (Table 1). Sec. 2.2 says NIST "selected 25 relevant documents" per topic; Sec. 2.1 says "a maximum of 25": minor inconsistency.
- **Sentences per topic:** avg 1321; relevant sentences avg 27.9; % relevant 2.1; new sentences avg 25.3; % new 90.9 (Table 1).
  - Check: 27.9 / 1321 = 2.11% **[computed ✓]**; 25.3 / 27.9 = 90.7% **[computed]** vs 90.9 printed; a mean of per-topic ratios can differ from a ratio of means, so this is not necessarily an error.
- **Task:** the paper describes task A (find relevant and new sentences in given relevant documents) and task B (find new sentences given relevant sentences), but analyses runs of "Novelty 2002 task 1" (Sec. 2.4, PDF p. 4) without stating how task 1 maps to A/B. The analysed measure is relevant-sentence recall, i.e. goal (1).
- **Relevance judgments:** human (NIST), sentence level (Sec. 2.3).
- **Runs:** 42 "systems or system variants" (Sec. 2.4). Per-topic measures were obtained from the TREC server for participants.
- **Train/dev/test:** not applicable; purely descriptive analysis on all topics.

## 7. Baselines

There are no baselines in the usual sense. The comparison is between clusters of topics and groups of runs.

| Compared unit | What it is | Why selected | Fair comparison? |
|---|---|---|---|
| Group 1 vs Group 2 (5 runs each) | Runs at opposite ends of the PCA correlation circle | Visual choice, "orthogonal considering the first axes" | **Weak.** Chosen post hoc from the same recall matrix used for the comparison. By run name, three of five in each group look like variants of one participant (ntu1–3; pircs01–03) **[inferred from run names; the paper does not say]**. The groups may therefore contrast two participant systems more than two "types" of systems |
| "All systems" | Mean over the 42 runs | Reference | Yes, as a descriptive reference |

## 8. Metrics

| Metric | Definition (Sec. 2.3, PDF p. 4) | Simple meaning here | Appropriate? |
|---|---|---|---|
| Rs (recall) | relevant retrieved sentences / relevant sentences | "What share of the relevant sentences did the run return?" | Only analysed metric. A set measure: a run returning many sentences gains recall at the cost of precision (see Nttcslabnvr2: R 0.60, P 0.10, Table 2) |
| Ps (precision) | relevant retrieved / retrieved sentences | Share of returned sentences that are relevant | Reported only for 5 example runs (Table 2); **not analysed** |
| Fs | 2·Ps·Rs / (Ps + Rs) | Balance of the two | Defined; the text says it "is also used" (Sec. 2.3), but no Fs values are reported or analysed |
| "R*P" | Column in Table 2 | Not defined in the text | Unclear (see §9) |

All measures are computed per query and then averaged over topics (Sec. 2.3). No rank-based metric is used.

## 9. Results

### Table 2: example runs (PDF p. 4)

| Run | Recall | Precision | R*P (printed) | R·P **[computed]** | F **[computed]** |
|---|---:|---:|---:|---:|---:|
| Dubrun | 0.49 | 0.15 | 0.19 | 0.074 | 0.230 |
| Thunv1 | 0.34 | 0.23 | 0.235 | 0.078 | 0.274 |
| Thunv3 | 0.41 | 0.20 | 0.235 | 0.082 | 0.269 |
| Pircs2N01 | 0.49 | 0.16 | 0.209 | 0.078 | 0.241 |
| Nttcslabnvr2 | 0.60 | 0.10 | 0.166 | 0.060 | 0.171 |

- The "R*P" column matches neither the product of the averaged R and P nor F computed from them. It could be a per-topic average of some quantity, but the paper does not define it: **unexplained**.
- Run names differ in spelling across the paper (Table 2 "Dubrun" vs Table 4 "dumbrun"; "Pircs2N01" vs "pircs01/02/03"; "Nttcslabnvr2" vs Fig. 3b "nttcvr2"). Whether these denote the same runs cannot be decided from the paper.

### Table 3: linguistic features for 8 topics (PDF p. 6)

The text says "Table 3 reports these values for the first 10 topics" (PDF p. 5), but the table has **8 rows** (TOP303, 305, 310, 312, 314, 315, 316, 317).

Spread over these 8 topics (population variance; share of the summed variance) **[computed]**:

| Feature | Range | Share of total variance |
|---|---|---:|
| SYNT DEPTH | 2.60–5.60 | 63.1% |
| POLYSEM | 2.86–4.92 | 29.9% |
| LENGTH | 4.45–5.41 | 5.6% |
| SYNT DIST | 1.40–1.81 | 1.0% |
| MORPH | 1.05–1.23 | 0.2% |
| SUFFIX | 0.08–0.19 | 0.1% |
| CONJ, PREP, VERBS | ≤ 0.09 range each | ≤ 0.1% each |

- With unnormalized Euclidean distance, a feature's influence on the clustering grows with its variance. On the visible topics, **MORPH + SUFFIX together carry ≈0.3%** of the variance, SYNT DEPTH + POLYSEM ≈93% **[computed]**. Unless the 41 unseen topics differ strongly, the clusters are shaped mainly by syntactic depth and polysemy, with LENGTH as the only morphological feature of some weight.
- The authors acknowledge the scaling issue: "The fact that features are not equivalent considering the scale of their value is not taken into account in this study; but will be in future works" (PDF p. 6).

### Fig. 2: clustering (PDF p. 6)

- The dendrogram shows six circled groups. The authors chose a 6-class partition by inter-cluster distance.
- "no simple correlation was found between linguistic features (taken individually) and these classes" (PDF p. 6). The paper therefore gives **no feature profile** for any cluster: it never says which cluster is, for example, morphologically complex.
- Cluster sizes: **NOT_REPORTED**. On the zoomed page image the leaf labels are partly illegible, and several leaves appear to lie between the drawn ellipses, so membership cannot be read reliably.

### Table 4: extract of the recall matrix (PDF p. 7)

- 10 topics × 8 runs. Observations **[from the table]**:
  - CIIRkl and CIIRnew columns are identical on all 10 topics; cmurCb, cmurCv and cmurCw are identical on all 10. Near-duplicate runs enter the PCA as separate variables.
  - t312 has recall 0 for all 8 runs shown.
- Only one Group 1 run (cmuBw) and one Group 2 run (CIIRnew) appear in the extract. On the three extract topics that Fig. 3a places in the blue cluster (t305, t315, t322), cmuBw has 0.07 / 0 / 0.18 and CIIRnew 0.33 / 0.36 / 0.26 **[read from Table 4 and Fig. 3a]**. This is the opposite of the cluster-level Table 5 pattern (blue favours Group 1). It is only 2 of 10 runs and 3 topics, so it does not contradict Table 5, but it shows how much the group means hide.

### Fig. 3: PCA (PDF p. 8)

- Axes 1 and 3 shown; together 50% of the total inertia (PDF p. 7). The share of axis 2, and why it is skipped, is **NOT_REPORTED**.
- Claim: "the queries of each cluster resulting from the HAC on linguistic features are situated close each other on the PCA visualization" (PDF p. 7). This is visual; no measure of cluster separation in PCA space is given.
- **Fig. 3a (zoomed) shows six marker types** **[read from page image]**:
  - cyan triangles (the text's "blue" cluster: t305, t315, t322, t330, t345, t362, t388, t410, t445);
  - red squares (many topics, crowded);
  - green circles (t326, t365, t382, t406, t409, t416 and one clipped at the edge);
  - orange ovals (t339, t364, t377, t440, t449);
  - **magenta diamonds** (t314, t317, t358, t363, t368, t397, t433);
  - one orange inverted triangle (t427).
  Only the first four appear in Table 5. The text's worked examples (topics 314 and 317 for ntu1, 363 for pircs02; PDF p. 7) are all magenta-diamond topics, i.e. from a cluster whose group means are not reported.

### Table 5: mean recall by topic cluster × system group (PDF p. 8)

| | Blue (triangle) | Orange (oval) | Green (circle) | Red (square) | All queries |
|---|---:|---:|---:|---:|---:|
| Group 1 (5 runs) | **0.42** | 0.24 | 0.50 | 0.22 | 0.32 |
| Group 2 (5 runs) | 0.26 | **0.62** | **0.77** | 0.29 | 0.46 |
| All systems (42) | 0.29 | 0.38 | 0.53 | 0.22 | 0.34 |
| Group 2 − Group 1 **[computed]** | −0.16 | +0.38 | +0.27 | +0.07 | +0.14 |

- Reading **[computed]**:
  - Blue: Group 1 is +61.5% relative to Group 2 (0.42 vs 0.26) — the only reversal;
  - Orange: Group 2 is +158% relative to Group 1 (0.62 vs 0.24);
  - Green: Group 2 +54% (0.77 vs 0.50). The authors call green "easy for the two groups", which is true relative to the all-systems mean, but the group gap is the second largest;
  - Red: Group 2 +32% (0.29 vs 0.22); "difficult whatever the group".
- So the crossover interaction rests on **one cluster (blue)**; everywhere else Group 2 is ahead.
- A "best group per cluster" oracle cannot be computed: cluster sizes are not reported, and two clusters are missing from the table.
- Values in the text match the table: blue 0.42 / 0.26 / all 0.29 (PDF p. 7) ✓.

### Discussion claim (Sec. 4, PDF pp. 8–9)

"We show that it is possible to decide for each type of queries what would be the best system to use when recall is to optimise." No rule for assigning a *new* query to a cluster is given; the authors state this is future work ("we did not extract the corresponding rules"). Likewise, the abstract's claim that "linguistic features of a query are good indicators to predict systems failure to answer it" (PDF p. 2) is not backed by any prediction experiment: no model predicts failure from features, and individual features are reported not to correlate with the clusters (PDF p. 6).

## 10. Statistical evidence

- **Significance tests:** NOT_REPORTED. The text speaks of "a high significance of these classes with the runs' performance scores" (PDF p. 6), but no test, p-value or effect-size measure is given.
- **Confidence intervals / variance:** NOT_REPORTED.
- **Runs / seeds:** not applicable (analysis of submitted TREC runs).
- **Cluster validity / stability:** NOT_REPORTED (no linkage criterion, no stability check, no alternative k).
- **Ablation:** none (no feature ablation, no normalized-feature variant).
- **Per-query analysis:** **yes, descriptively**: a per-topic recall matrix (Table 4, extract), PCA of topics × runs (Fig. 3), and cluster-level means (Table 5). This is the paper's main contribution.
- **Overlap / unique relevant hits / oracle union between systems:** NOT_REPORTED. The analysis is on per-topic recall *values*, not on *which* relevant sentences each run found.
- **Fusion:** NOT_REPORTED (proposed only).

## 11. Strengths

- Moves beyond averages: explicit per-topic, per-run analysis of 42 runs.
- Features are automatic and cheap, so in principle usable in an adaptive system (a design goal stated on PDF p. 4).
- Separates the definition of query clusters (features only) from the performance analysis (Sec. 3 intro, PDF p. 5), avoiding direct circularity at that step.
- Clearly motivated link from query features to data fusion (Sec. 4).
- Honest about some limits: database coverage of CELEX/WordNet, unnormalized features.

## 12. Limitations

### Stated by the authors

- Feature scales are not normalized in the clustering; to be addressed in future work (PDF p. 6).
- CELEX and WordNet coverage: rare/new/misspelled words count as mono-morphemic / monosemous (PDF p. 5).
- Only title + description are used; the fields are short (1–3 sentences), so some statistical features could not be computed (PDF p. 4).
- NLP tools make errors (PDF p. 5).
- Only recall is analysed; precision is future work (PDF p. 9).
- No rule for assigning new queries to clusters (PDF p. 9).
- Individual features do not correlate with the classes (PDF p. 6).

### Inferred from the experimental design

1. **The morphological contribution is not identifiable.** Morphological features are mixed with syntactic and semantic ones, features are unscaled, and on the visible topics MORPH and SUFFIX carry ≈0.3% of the variance **[computed]**. Nothing in the paper shows that morphology drives any cluster.
2. **Systems are black boxes.** Their stemming, stop-words, models and expansion are not described, so the paper cannot say *which technique* handles which query type. The authors list this as future work ("a given technique (known to be used by a system)", PDF p. 9).
3. **Post-hoc, visual grouping of systems** from the same recall matrix that is then summarized in Table 5; no held-out topics; no test. The reported interaction can be partly a selection effect.
4. **Groups may be participant families** (ntu*, pircs*) rather than technique types **[inferred from run names]**; near-duplicate runs (Table 4) weight some systems more in the PCA.
5. **Recall-only set evaluation.** Group differences in recall can reflect how many sentences a run returns, not better matching; Table 2 shows the recall/precision trade-off.
6. **Incomplete reporting:** 2 of 6 clusters missing from Table 5; no cluster sizes; only 8 of 49 feature rows and 10 × 8 of 49 × 42 recall cells shown.
7. **Task scope:** sentence selection within ~22 given relevant documents per topic, not corpus-level document retrieval; English only.
8. Internal inconsistencies (§19) lower confidence in the reporting.

## 13. What the work proves

Within its descriptive scope:

- On TREC 2002 Novelty (49 English topics, 42 runs), per-topic recall varies strongly across runs; averages hide it (Tables 4–5).
- For the two visually chosen groups of 5 runs, mean recall differs by topic cluster, with one reversal: blue cluster Group 1 0.42 vs Group 2 0.26; other reported clusters favour Group 2 (Table 5). This is a descriptive crossover pattern, not a tested effect.
- Automatic query features (including morphemes-per-word and suffixation) can be computed for short English topics with standard tools (TreeTagger, SYNTEX, CELEX, WordNet).

## 14. What the work does NOT prove

- **That morphological features predict system success.** No feature is linked individually to the clusters (authors' own statement), and the morphological features have negligible weight in the unscaled clustering **[computed]**.
- **That the cluster × group interaction is statistically reliable** or would hold on new topics: no test, no held-out data, post-hoc groups.
- **That fusion or routing by query cluster improves retrieval.** No fused or routed run is evaluated, and no oracle over clusters can be computed from the reported numbers.
- **Anything about morphological normalization of the lexical representation** (raw/stem/lemma): not studied; system preprocessing is unknown.
- **Anything about BM25, dense or semantic retrieval models**, or about lexical–semantic complementarity: none are identified or compared.
- **Which relevant items each group finds uniquely**, or their overlap: not measured.
- Generalization beyond English, beyond sentence-level novelty retrieval, or to precision.

## 15. Relationship to current Uzbek evidence

- **No Uzbek data;** English only.
- Transferable in spirit: the feature design. MORPH (morphemes per word) and SUFFIX (share of suffixed words) measure exactly what is abundant in agglutinative Uzbek. For Uzbek, these could come from a morphological analyzer (cf. Bakaev, Xusainova, Elov in `MASTER_INDEX` C) rather than from a CELEX-type database, which would also avoid the "missing word = mono-morphemic" coverage bias the authors note.
- Methodological parallel with our Amharic cards by the same senior author (Yeshambel, Mothe & Assabie 2023/2024, `CR000427`, `CR000447`): those vary the lexical representation (word/stem/root) but do no per-query analysis; this paper does per-query analysis but does not vary the representation. Neither joins the two, which is what the Uzbek design needs.
- Related to the query-dependent strategy literature already in the index (HYB-008 Arabzadeh et al. 2021; HYB-009 Posokhov et al. 2026) as an earlier, pre-neural example.

## 16. Relationship to CURRENT_GAP

**Classification:** *supports (weakly, as historical precedent)* + *closes part of the broad gap (confirms already-occupied non-claims)* + *no material effect on the residual core*.

- **Confirms as occupied** (already non-claims in v0.8):
  - "query-type analysis lexical vs semantic — new idea": query linguistic features, including morphological complexity, were already related to differential system performance in 2007;
  - "query-dependent strategy / fusion by query type — new idea": explicitly proposed here (Sec. 4).
- **Weak support** for including morphological query features among the v0.8 candidate query characteristics ("количество/тип аффиксальных форм", "proxy морфологической сложности"): the paper shows such features are computable and part of a broader feature set linked to per-query variation. It does **not** show they matter.
- **Re-assessment of the triage flag `carries_complementarity_evidence = YES`:** the only "complementarity" is a cluster-level recall crossover between two groups of black-box runs (Table 5). There is no relevant-set overlap, no unique hits, no oracle union and no fusion. In v0.8 terms it is *per-query performance variation*, not *complementarity of relevant sets*.
- **Untouched v0.8 elements:** raw/stem/lemma lexical representation; fixed dense retriever D; unique relevant hits / overlap; oracle union; incremental hybrid gain; morphology-induced change of any of these; Uzbek.

**Proposal:** keep v0.8 refined unchanged. Optionally cite this paper as an early precedent in the "query-type analysis / query-dependent fusion is not new" part of the evidence boundary. This is a proposal only; `CURRENT_GAP.md` has not been edited.

## 17. Implications for our research design

- **Query taxonomy / features.**
  - Adopt Uzbek analogues of MORPH and SUFFIX: mean number of affixes per word, share of affixed words, from the Uzbek analyzer used for BM25_lemma/stem. Keep LENGTH (characters per word) as a resource-free proxy.
  - Record analyzer coverage per query (share of words the analyzer cannot parse), since unknown words otherwise bias the features toward "simple" (the CELEX problem stated on PDF p. 5).
- **Feature scaling.** Standardize features (z-scores) before any clustering or distance-based analysis, and report per-feature variance; otherwise morphological proportions (range ≈0.1) are swamped by features with range ≈2–3, as in this paper **[computed]**.
- **Analysis protocol.**
  - Predefine the conditions compared (raw/stem/lemma BM25, D, hybrids) instead of choosing groups post hoc from the result matrix.
  - Test the interaction "query feature × condition" at query level (e.g. per-query differences regressed on features, or permutation tests), with held-out queries if clusters or rules are derived.
  - Report cluster sizes and all clusters, not a subset.
- **Metrics.** Do not rely on set recall alone; pair it with rank-based metrics and, for complementarity, with relevant-set overlap / unique hits / oracle union at fixed depth k, so that "retrieves more" is not confused with "finds different relevant items".
- **Systems.** Our design already fixes what this paper lacks: known, controlled lexical variants and a fixed D. This is the main reason the Uzbek experiment can attribute effects to morphology where this paper cannot.
- **Hypothesis.** No evidence for or against the v0.8 hypothesis. It motivates the query-feature part: whether morphology-related query features explain *where* the lexical variant changes complementarity must be tested, not assumed.

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| TREC Novelty track | A 2002 evaluation task: find relevant (and new) sentences inside documents known to be relevant | Sentence-level retrieval and novelty detection over a per-topic document set |
| Topic | A written information need: title, description, narrative | TREC query statement |
| Run | One system's output submitted to TREC | Ranked or unranked result set per topic |
| Set recall (Rs) | Share of the relevant sentences the run returned | relevant retrieved / relevant |
| Morpheme | Smallest meaningful part of a word (add + ition + al + ly) | Morphological unit, here from CELEX |
| Suffixation | Building a word by adding an ending (post-menopaus-al) | Derivational/inflectional suffix detection by list |
| Polysemy | A word having several meanings | Number of WordNet synsets per word |
| HAC (hierarchical agglomerative clustering) | Repeatedly merge the two most similar groups until one remains; cut the tree to get k clusters | Agglomerative partition sequence Pₙ … P₁ |
| Euclidean distance on unnormalized features | Straight-line distance where features with large numbers dominate | ‖f(t) − f(t′)‖₂ without scaling |
| PCA | Rotate the data so the first few axes show most of the variation | Eigen-decomposition of the covariance matrix |
| Inertia (in PCA) | Share of total variation shown by the chosen axes | Sum of the chosen eigenvalues / total |
| Crossover interaction | System A wins on one query type, system B on another | Sign change of the group difference across clusters |
| Data fusion | Combine the results of several systems into one ranking | E.g. score/rank combination |
| Complementarity (project term) | Each channel finds some relevant items the other misses | Unique relevant hits, overlap, oracle-union gain |

## 19. Open questions / verification needed

1. **Number of topics:** 50 (abstract, PDF p. 2) vs 49 (Table 1, Sec. 2.2, Sec. 4). Probably 49 were analysed; not decidable with certainty from the paper.
2. **Missing clusters:** a 6-class partition is chosen (PDF p. 6), but Table 5 reports 4 classes. Fig. 3a shows magenta-diamond topics (including the text's examples 314, 317, 363) and one inverted-triangle topic (t427) with no reported group means.
3. **Cluster sizes and membership:** NOT_REPORTED; the dendrogram leaves are partly illegible.
4. **"R*P" column in Table 2:** matches neither R·P nor F **[computed]**; its definition is not given.
5. **Table 3 caption vs text:** "first 10 topics" vs 8 rows.
6. **Section reference:** runs are "the inputs of the analysis we report in section 4" (PDF p. 4), but the analysis is in Sec. 3.
7. **Task naming:** "task 1" (Sec. 2.4) vs "task A / task B" (Sec. 2.1).
8. **Documents per topic:** "25 relevant documents" (Sec. 2.2) vs "maximum of 25" (Sec. 2.1) vs avg 22.3 (Table 1).
9. **Run naming** differs across Table 2, Table 4 and Fig. 3b (§9).
10. **Linkage criterion, suffix list, PCA axis 2 share:** NOT_REPORTED.
11. The version of record (IEEE, pp. 77–84) was not compared with the HAL version; numbers may differ.
12. Later work by the same group on query difficulty and linguistic features could contain the tested/normalized version (the authors announce it as future work); check the systematic-review record set before citing this paper as the latest word from this line.

## 20. Decision after deep dive

- **Keep current gap?** Yes. v0.8 refined remains valid; see §16.
- **Modify gap?** No change proposed. Optionally add this paper as an early precedent to the evidence-boundary list for "query-type analysis / query-dependent fusion is not new" (researcher's decision).
- **Add decision?** Proposed for `decisions/DECISIONS.md` (researcher's decision):
  - "Query features are standardized before clustering/regression; morphological features come from the Uzbek analyzer, with analyzer coverage recorded per query";
  - "Query-feature × condition effects are tested at query level with predefined conditions, never on groups selected post hoc from the same results".
- **Add experiment?** No new experiment. It supports keeping the planned per-query feature analysis, with morphological features (affixes per word, share of affixed words, word length) in the feature set.
- **Add citation to Chapter I?** Yes, briefly:
  - §1.3 (history of query-dependent / query-type-driven fusion: an early 2007 proposal based on linguistic query features, without evaluation of fusion);
  - optionally §1.1 (query-level variability hidden by averaged evaluation).
- **Proposed `MASTER_INDEX.md` row** (to add after approval):

| HYB-013 | Mothe & Tanguy — *Linguistic Analysis of Users' Queries: Towards an Adaptive Information Retrieval System* (IEEE SITIS 2007, pp. 77–84, DOI 10.1109/SITIS.2007.81) — [deep dive](deep-dives/2007_Mothe_Tanguy_Linguistic_Query_Features_Adaptive_IR.md) | 2007 | B | MEDIUM | TREC 2002 Novelty (49 English topics, 42 black-box runs, sentence-level set recall). 9 automatic query features (morphological: word length, CELEX morphemes/word, suffixed-word share; syntactic; WordNet polysemy) → unnormalized HAC (6 clusters) → PCA of the recall matrix with two visually chosen 5-run groups. Cluster × group recall crossover on one cluster only (blue 0.42 vs 0.26; others favour Group 2, all queries 0.32 vs 0.46). Fusion proposed, not evaluated. No stem/lemma representation variants, no BM25/dense, no overlap/unique hits, no significance tests; morphological features carry ≈0.3% of feature variance in the shown topics [computed]. Early precedent for query-type-driven fusion. |
