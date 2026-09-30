# Can, Kocberber, Balcik, Kaynak, Ocalan & Vursavas (2006): First Large-Scale Information Retrieval Experiments on Turkish Texts

**Targeted deep-dive status:** COMPLETED (AI-assisted, pending researcher review)
**Completed:** 2026-09-28
**Literature ID:** `MORPH-013` (assigned 2026-09-28, approved by researcher) (preliminary version of MORPH-001; excluded from the review as duplicate study FT8)
**Systematic-review record:** `CR000651`. Full-text triage: INCLUDE, reading priority HIGH, reading tier 1, `carries_complementarity_evidence = NO`. Triage note: preliminary version of the study extended in CR000502 (JASIST 2008 = `MORPH-001`), likely FT8 duplicate for the coordinator.
**Provenance:** AI-assisted deep dive (Claude). The whole paper (2 pages, printed pp. 627–628) was read from the text extraction and from page images. Pages checked visually: p. 627 (whole page) and p. 628 (Table I, Sec. 4 text, Sec. 5, at 200 dpi). Every Table I value below was compared with the page image. Numbers computed by us are marked **[computed]**. Statements about the 2008 journal version come only from the existing project card of `MORPH-001` and are marked **[MORPH-001 card]**; they were not re-verified against the 2008 PDF here.
**Source rule:** **the paper is the primary and only authoritative source** for what the authors did and found. The web was used only to check the bibliographic record.
**Reliability:** **A** by venue (peer-reviewed ACM SIGIR 2006 proceedings, 2-page paper). Its evidential weight is narrow: it is a short preliminary report, the prefix and lemma-length choices are described without numbers, and it is superseded by the full journal version (`MORPH-001`).
**Verification:** independent AI verifier pass 2026-09-28; 7 findings addressed.

---

## Кратко для исследователя (RU)

- **Что сделано.** Двухстраничная (pp. 627–628) предварительная публикация группы Bilkent на SIGIR 2006. Первая крупная турецкая тестовая коллекция в стиле TREC: Milliyet 2001–2005, 408 305 документов, 72 запроса, бинарная разметка 33 носителями языка, пулинг top-100 из 24 прогонов.
- **Варианты лексического представления есть:** без стемминга (NS), усечение до префикса (F3–F7, в финал попал F5), статистический стемминг successor variety (SV), лемматизатор (LM5/LM6) и гибрид LV = LM5 + SV для слов, которые лемматизатор не разбирает (около 40% различных словоформ).
- **Модели сопоставления:** 8 функций векторной модели (MF1–MF8, схемы весов SMART). **BM25 нет.**
- **Главные числа** (Table I, p. 628, bpref, среднее по 8 функциям): NS 0.2793, SV 0.3591, F5 0.3603, LM5 0.3715, LV 0.3781. Для лучшей функции MF8: NS 0.3142, SV 0.4134, F5 0.4146, LM5 0.4265, LV 0.4319. Любая нормализация даёт около +29–35% к NS **[computed]**; LV лучше F5/SV всего на ≈5% относительных.
- **Значимость.** LV > SV и LV > F5 проверены односторонним парным t-тестом (p < .001), но парами служат 8 функций сопоставления, а не запросы. Тест по отдельным запросам для MF8 даёт p < .05; он приведён только после исключения двух запросов-«выбросов» (критерий и результат без исключения не описаны). LM5 vs LV, F5 vs SV, NS vs остальные и «MF8 значимо лучше» тестами не подкреплены.
- **Нет:** плотного (dense) поиска, гибрида/fusion, BM25, анализа перекрытия, уникально найденных релевантных документов, oracle union, анализа по характеристикам запросов (анализа длины запроса, в отличие от журнальной версии, здесь нет).
- **Что добавляет к MORPH-001 (по карточке MORPH-001):** полную таблицу 5 представлений × 8 функций, включая LM5. Видно, что порядок F5 vs SV меняется в зависимости от функции весов (F5 > SV в 5 из 8). Больше ничего существенного.
- **Расхождение с журнальной версией:** значения MF8 здесь ниже, чем в MORPH-001 (например, LV 0.4319 vs 0.4504), и здесь заявлено значимое LV > F5 на MF8, а в журнальной версии, по карточке MORPH-001, это различие не значимо. Цитировать как основной источник следует 2008 г.; этот постер — только как исторически первую публикацию коллекции.
- **Библиографическая ошибка в метаданных обзора:** в записи указано «SIGIR Forum / JOUR», а PDF и Crossref дают труды конференции SIGIR 2006, pp. 627–628, DOI 10.1145/1148170.1148288.
- **Для нашего gap:** не влияет на ядро v0.8 (raw/stem/lemma BM25 × фиксированный D → overlap/unique hits → прирост гибрида). Только подкрепляет уже занятый тезис «морфологическая нормализация сильно помогает лексическому поиску в тюркском языке».
- **Практическая польза:** (1) эффект морфологии зависит от схемы весов, поэтому BM25 k1/b и нормализацию надо фиксировать одинаково для raw/stem/lemma; (2) пул разметки должен включать все сравниваемые представления и dense/hybrid (здесь F5/LM5/LV в пул не входили); (3) длину префикса и параметры лемматизатора не выбирать на тестовых запросах.

---

## 1. Bibliographic record

- **Authors:** Fazli Can, Seyit Kocberber, Erman Balcik, Cihan Kaynak, H. Cagdas Ocalan, Onur M. Vursavas
- **Affiliation:** Bilkent Information Retrieval Group, Bilkent University, Ankara, Turkey (p. 627)
- **Year:** 2006
- **Venue (from the PDF, p. 627 footer):** "SIGIR'06, August 6–11, 2006, Seattle, Washington, USA. ACM 1-59593-369-7/06/0008."
- **Proceedings (bibliographic check: Crossref record for the DOI, via api.crossref.org):** *Proceedings of the 29th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval*, pp. 627–628, ACM, issued 2006-08-06, type proceedings-article.
- **DOI:** `10.1145/1148170.1148288` (bibliographic check: Crossref; ACM DL page returned 403 and could not be opened)
- **Official URL:** https://dl.acm.org/doi/10.1145/1148170.1148288
- **Source type:** 2-page peer-reviewed conference paper (poster-length). The PDF itself does not use the word "poster"; the acknowledgments thank "the anonymous referees".
- **Metadata discrepancy:** the systematic-review record gives venue "SIGIR Forum" and type JOUR. Both the PDF footer and Crossref identify the SIGIR 2006 conference proceedings. The record should be corrected.
- **Reliability:** A (venue); narrow evidential weight (see header).
- **Full text available:** yes (`07_full_text/pdfs/CR000651.pdf`, 2 pages)
- **Relation to other records:** preliminary version of `MORPH-001` (Can et al., JASIST 2008, CR000502), same authors and collection (triage note; confirmed by identical authors and collection figures).

## 2. Why this work matters to the PhD

It is the first publication of the Milliyet Turkish test collection that later supports `MORPH-001` and `MORPH-002`. It gives a controlled comparison of lexical representations (raw / prefix / statistical stem / lemma / lemma+fallback) in an agglutinative Turkic language.

| Axis | Relation |
|---|---|
| Lexical retrieval | Direct: 5 representations × 8 vector-space weighting schemes; **no BM25** |
| Semantic retrieval | Absent |
| Hybrid retrieval | Absent (LV is a hybrid *stemmer*, not a hybrid retrieval system) |
| Uzbek morphology | Indirect: Turkish, same family (Turkic, agglutinative, suffixing) |
| Low-resource retrieval | Historical: Turkish IR had only 500–2,500-document collections before this (Sec. 1) |
| Current gap | Supports an already occupied boundary claim; does not touch morphology-induced complementarity |

## 3. Research problem

### Simple explanation

In Turkish one word can take many suffixes, so a query word and the same word in a document often look different. Does collapsing these forms help search, and does a real morphological analyzer beat simply cutting words to their first few letters?

### Formal formulation

Compare the retrieval effectiveness (bpref) of term representations {NS, F5, SV, LM5, LV} across eight vector-space query–document matching functions on a large Turkish ad hoc test collection (Sec. 1, 4). No explicit research questions or hypotheses are stated.

## 4. Main idea

### Simple explanation

Build the same index several times, each time turning words into index terms differently. Run the same 72 queries against each index with eight classic weighting formulas and compare the scores.

### Concrete example

Context (not from the paper; illustrative Turkish word chosen by us): *kitaplarımızdan* ("from our books").
- NS keeps `kitaplarımızdan`;
- F5 keeps `kitap`;
- SV cuts at the prefix after which the corpus shows the most distinct next letters;
- LM5 asks the morphological analyzer for the lemma `kitap`;
- LV uses LM5 but falls back to SV when the analyzer fails (misspelled or foreign words).
The paper gives no worked word example.

### Formal method

Two factors are crossed: term representation (5 levels in the final analysis) × matching function (8 levels). Effectiveness is bpref (Sec. 4), presumably averaged over the 72 queries; the paper does not state the averaging explicitly.

## 5. Architecture / algorithm

1. **Stemming options, stage 1** (Sec. 2, p. 627): NS; F6 (first six characters); SV (successor variety, Hafer & Weiss [3]). The Turkish SV adaptation "chooses the longest prefix corresponding to the highest SV value".
2. **Stage 2** (Sec. 2): prefixes F3, F4, F5, F7, and a lemmatizer-based stemmer using a morphological analyzer [1].
   - When the analyzer returns several lemmas, the one closest to the average lemma length (6.58 characters) is chosen (LM6), or closest to 5 characters (LM5, "since F5 gives good retrieval results"). Ties are broken by the most frequent part of speech.
   - The authors state this choice is "more than 90% accurate", citing their own paper [1], listed as "resubmitted after rev.".
   - About 40% of distinct words cannot be analyzed; LV applies SV to them.
3. **Selection of representatives** (Sec. 4, p. 628): using 11-point recall–precision graphs under MF8 ("an inexact comparison approach"), F3 and F7 are "definite losers", then F6 < F4 < F5, with the caveat that "The difference especially between the last two is insignificant, but F5 is slightly better than F4" (no test; informal graphs). LM5 is "slightly better" than LM6. **The numbers for this selection are NOT_REPORTED.** Final set: NS, SV, F5, LM5, LV.
4. **Matching functions** (Sec. 3, pp. 627–628): SMART-notation schemes from Salton & Buckley [4]:
   - MF1 txc.txx (cosine, no idf);
   - MF2–MF7 tfc.nfx, tfc.tfx, tfc.bfx, nfc.nfx, nfc.tfx, nfc.bfx;
   - MF8, from Witten, Moffat & Bell [8, p. 187], puts the idf effect into query term weights, so document weights need no update when the collection changes.
   - Context (not from the paper): in SMART notation, the three letters give the term-frequency, collection-frequency (idf) and normalization components for documents (before the dot) and queries (after the dot).
5. **Stop words:** 320-word list (no numbers), covering 15% of collection tokens; stop-word removal applied (Sec. 3).
6. **BM25 / probabilistic or language-model retrieval:** not used.

## 6. Data

- **Collection:** Milliyet newspaper, 2001–2005, news articles including columns (Sec. 3, p. 627).
- **Language / domain:** Turkish; news.
- **Size:** 408,305 documents; about 800 MB; about 95.5 million tokens including numbers before stop-word removal; average article 234 tokens.
- **Index statistics** (Sec. 3):

| | NS | F6 | SV |
|---|---:|---:|---:|
| Avg unique words (types) per document | 150 | 134 | 120 |
| Avg type length (characters) | 9.88 | 5.66 | 7.23 |
| Posting-list entries (million) | ≈61 | ≈55 | ≈49 |

  Statistics for F5, LM5 and LV are NOT_REPORTED.
- **Queries:** 72 ad hoc queries written "according to the TREC ad hoc query tradition" by 33 native speakers; "about 11 distinct words" each (Sec. 3, p. 628). Which topic fields (title/description/narrative) were used is **NOT_REPORTED**.
- **Query filtering:** "about 20" queries were eliminated for having too few (≤ 5% of the pool) or too many (≥ 90%) relevant documents. (The page image shows ≤ and ≥; the text extraction gives < and >.) So about 92 queries were originally created **[computed, approximate]**.
- **Relevance judgments:** binary; pool = union of top-100 documents from 24 runs (8 MFs × NS/F6/SV). Average pool size 466 documents, average 104 relevant per query, i.e. ≈22% of the pool **[computed]**.
- **Train/dev/test:** none; all choices (prefix length, LM5 length target) were made on the same queries.
- **Pool coverage:** F5, LM5 and LV did not contribute to the pool; bpref was chosen "to prevent any possible bias effect on the runs not involved in query pool construction" (Sec. 4).

## 7. Baselines

| Baseline | What it is | Why selected | Fair comparison? |
|---|---|---|---|
| NS | Surface word forms | No-normalization reference | Yes; it was a pool contributor |
| F5 | Keep first 5 characters | Prefixes of 5–7 recommended for Turkish IR [6]; best prefix in stage 2 | Mostly; not a pool contributor; length chosen on the test queries |
| SV | Corpus-statistical stemmer | Language-independent "active" stemming | Yes; pool contributor |
| LM5 | Lemmatizer, lemma choice guided by length 5 | Linguistically informed | Not a pool contributor; length target borrowed from F5's test results |
| LV | LM5 + SV fallback | Covers the ~40% unanalyzable words | Not a pool contributor; mixes lemmatization and statistical stemming |

No lexical probabilistic model (BM25) and no semantic or hybrid system.

## 8. Metrics

| Metric | Definition | Simple meaning | Appropriate? |
|---|---|---|---|
| bpref | Context (not from the paper, which cites [2] but gives no definition): for each judged relevant document, penalize by the share of judged non-relevant documents ranked above it; unjudged documents are ignored (Buckley & Voorhees 2004) | "Are the known relevant documents placed above the known non-relevant ones?" | Yes, given that three of the five compared representations did not contribute to the pool |
| 11-point recall–precision graph | Context (not from the paper): interpolated precision at recall 0, 0.1, …, 1 | Used only informally to pick F5 and LM5; values not shown | Informal, as the authors say |

Only bpref is reported; MAP, P@k, nDCG and recall are NOT_REPORTED.

## 9. Results

### Table I: bpref, and % improvement of LV over SV and F5 (p. 628; checked on the page image)

| MF | NS | SV | F5 | LM5 | LV | LV/SV % | LV/F5 % |
|---|---:|---:|---:|---:|---:|---:|---:|
| MF1 | .2262 | .2851 | .2916 | .3089 | .3154 | 10.63 | 8.16 |
| MF2 | .3035 | .3995 | .3843 | .3976 | .4047 | 1.30 | 5.31 |
| MF3 | .2949 | .3790 | .3694 | .3872 | .3933 | 3.77 | 6.47 |
| MF4 | .3002 | .3900 | .3756 | .3910 | .3976 | 1.95 | 5.86 |
| MF5 | .2661 | .3417 | .3533 | .3588 | .3666 | 7.29 | 3.76 |
| MF6 | .2819 | .3438 | .3653 | .3595 | .3657 | 6.37 | 0.11 |
| MF7 | .2471 | .3199 | .3281 | .3426 | .3495 | 9.25 | 6.52 |
| **MF8** | .3142 | .4134 | .4146 | .4265 | **.4319** | 4.48 | 4.17 |
| C. Av. | .2793 | .3591 | .3603 | .3715 | .3781 | 5.63 | 5.05 |

Checks and derived values **[computed, python]**:
- All 16 printed LV/SV and LV/F5 percentages reproduce exactly from the bpref values.
- The "C. Av." row is the arithmetic mean over the 8 MFs (SV mean 0.35905, printed .3591; LV/F5 mean 5.045, printed 5.05). The C. Av. percentages are means of per-MF percentages; the ratio of the averaged bpref values gives LV/SV 5.29% and LV/F5 4.94%.
- **Normalization vs NS** (C. Av.): SV +28.6%, F5 +29.0%, LM5 +33.0%, LV +35.4%. Under MF8: SV +31.6%, F5 +32.0%, LM5 +35.7%, LV +37.5%.
- **LV is the best representation under all 8 MFs.** LV > LM5 in all 8 MFs, by only 1.3–2.2% relative.
- **F5 vs SV depends on the matching function:** F5 > SV under MF1, MF5, MF6, MF7, MF8; SV > F5 under MF2, MF3, MF4. The averages are almost equal (.3603 vs .3591, +0.3%).
- LM5 > F5 in 7 of 8 MFs (not under MF6).
- **MF8 is the best matching function for every representation.**
- Absolute gap LV − F5 under MF8 = 0.0173 bpref, compared with LV − NS = 0.1177.

### Comparison with the 2008 journal version (MORPH-001 card, not re-verified here)

The `MORPH-001` card reports for MF8: NS 0.3255, F5 0.4322, SV 0.4304, LV 0.4504. All four are higher than this paper's MF8 row (by 0.011–0.019 bpref) **[computed]**. The poster does not say which query fields were used, so the difference cannot be explained from this paper; the two versions evidently do not use identical run conditions or qrels. The *ordering* (NS ≪ SV ≈ F5 < LV) is the same.

The prefix ordering also differs. This paper says, informally and without numbers, that F5 is "slightly better" than F4 (Sec. 4). The MORPH-001 card reports F4 bpref 0.4382 > F5 0.4322 under MF8 in the 2008 version (while F5 is better there on MAP/P@10/P@20).

## 10. Statistical evidence

- **Test 1** (Sec. 4, p. 628): two one-sided matched-pair t-tests "using the document query matching functions (Table I data)": LV > SV and LV > F5, both p < .001.
  - The pairs are the **8 matching functions**, not queries. Reproduced from Table I: LV > SV t = 5.69, one-sided p = 0.00037; LV > F5 t = 6.40, p = 0.00018 (df = 7) **[computed]**. This confirms the reported p-values.
  - What it shows: LV's advantage is consistent across weighting schemes. It does not show generalization across queries, and the 8 schemes are not independent samples.
- **Test 2:** two one-sided matched-pair t-tests on MF8 per-query results: LV > SV and LV > F5, both p < .05, after eliminating "two queries ... identified as potential outliers". The outlier criterion and the test without removal are **NOT_REPORTED**.
- **One-sided choice:** justified by the authors as testing "LV>SV instead of LV is not equal to SV". The paper does not say when the direction was fixed. There is no pre-registration, and the direction matches the observed results, so a post hoc choice cannot be excluded (our inference).
- **Not tested:** NS vs normalized variants; F5 vs SV; LM5 vs LV; LM5 vs F5; MF8 vs other MFs. The Conclusions nonetheless say MF8 "gives a significantly better retrieval performance". **No test supporting this is reported.**
- **Confidence intervals:** NOT_REPORTED. **Runs/seeds:** not applicable (deterministic retrieval).
- **Ablation:** not in the modern sense; the representation × MF grid is a controlled comparison. LV vs LM5 isolates the SV fallback (+1.3–2.2%, untested).
- **Per-query analysis:** only the per-query t-test above. No win/loss counts, no query-feature analysis, no overlap/unique-hit analysis between representations.

## 11. Strengths

- First large TREC-style Turkish collection (408K documents, human binary judgments by 33 native speakers).
- Representations from trivial (prefix) to linguistic (lemmatizer) on the same queries and qrels.
- 8 weighting schemes, so the morphology conclusion does not rest on one formula (Table I).
- Awareness of pool bias: bpref chosen explicitly because some runs were not pooled.
- Handles analyzer coverage failures explicitly (LV fallback) and reports the coverage rate (~40% of distinct words).

## 12. Limitations

### Stated by the authors

- The prefix and LM5/LM6 selection by 11-point graphs is "an inexact comparison approach" (Sec. 4).
- About 40% of distinct words (misspelled and foreign) cannot be analyzed by the lemmatizer (Sec. 2).
- Only NS, F6 and SV runs formed the pool; bpref used to limit the bias (Sec. 3–4).

### Inferred from the experimental design

1. **No BM25, no probabilistic model, no semantic or hybrid retrieval.**
2. **Weak statistical unit for the main claim.** The p < .001 result pairs matching functions, not queries; the per-query test is limited to MF8 and is reported only after removing two queries as "potential outliers" (Sec. 4). The removal criterion and the result without removal are NOT_REPORTED.
3. **Headline claim broader than the test.** "A lemmatizer-based stemmer provides significantly better effectiveness" (Abstract, Sec. 5) refers to LV, which uses SV for ~40% of distinct words. Pure LM5 was never significance-tested.
4. **Design choices made on the test queries.** F5 and LM5 were chosen on the same 72 queries used for the final comparison; LM5's length target is taken from F5's retrieval result.
5. **Pool bias only partly mitigated.** bpref reduces but does not remove the disadvantage of non-pooled runs (F5, LM5, LV); here the non-pooled LV still wins.
6. **Query set shaped by filtering.** About 20 queries with ≤ 5% or ≥ 90% relevant documents in the pool were removed.
7. **Query formulation NOT_REPORTED** ("about 11 distinct words"; fields unknown).
8. **Only bpref** is reported. The self-cited lemma-selection accuracy (>90%) comes from a paper still under review at the time.

## 13. What the work proves

Within its setting (Turkish news, 72 filtered queries, vector-space weighting, bpref):
- Morphological normalization of the index terms strongly improves lexical retrieval over surface forms: +29–35% bpref on the average over 8 MFs (Table I, **[computed]**). This is consistent across all 8 weighting schemes, though no NS-vs-normalized test is reported.
- Simple 5-character truncation (F5) is about as effective as statistical SV stemming on average (.3603 vs .3591), but which of the two wins depends on the weighting scheme.
- LV (lemmatizer + SV fallback) is numerically best under every weighting scheme, by about 4–5% over F5 and SV on average. The advantage is consistent across weighting schemes (p < .001 over MFs) and significant per query under MF8 after removing two outliers (p < .05).

## 14. What the work does NOT prove

- Anything about **BM25**, dense retrieval, or lexical–semantic hybrids.
- That **pure lemmatization** (LM5) beats F5 or SV significantly: untested.
- That **MF8 is significantly better** than the other matching functions: claimed, not tested.
- That LV's advantage over F5 is robust. The per-query result is reported only after removing two queries (criterion and unremoved result NOT_REPORTED). The 2008 journal version, according to the MORPH-001 card, does not find LV vs F5 significant under MF8.
- Anything about **which queries** benefit from which representation, or about query length (not analyzed in this paper).
- Whether different representations retrieve **different relevant documents** (no overlap / unique-hit / union analysis).
- Transfer of the numbers or of F5 to Uzbek.

## 15. Relationship to current Uzbek evidence

- No Uzbek data. Turkish is the closest well-studied relative (Turkic, agglutinative, suffixing), so the *method* transfers: compare representations on real ranked retrieval rather than on analyzer accuracy. This is the same boundary that the national cards (Bakaev, Xusainova, Elov) draw between analyzer accuracy and IR effectiveness.
- The LV design mirrors a practical Uzbek issue: analyzer coverage gaps (loanwords, misspellings, Latin/Cyrillic and apostrophe variants) need an explicit fallback, and the fallback share must be reported.
- Adds nothing beyond `MORPH-001` / `MORPH-002` for Uzbek except the full representation × weighting-scheme table.

## 16. Relationship to CURRENT_GAP

**Classification:** *supports* (already occupied boundary) + *no material effect* on the residual core.

- **Supports** the v0.8 non-claim "raw/stem/lemma were not compared in (Turkic) IR": this is the earliest large-scale Turkish comparison of raw vs prefix vs statistical stem vs lemma representations. It adds the observation that the ranking between representations can change with the term-weighting scheme.
- **No material effect** on the residual core: no fixed dense comparator D, no BM25, no fusion, no unique relevant hits / overlap / oracle union, no incremental hybrid gain, no query-feature link. None of the v0.8 core elements is present.
- It does not affect any of the four "what can still kill this gap" conditions.

**Proposal:** keep v0.8 refined unchanged. In `GAP_BOUNDARY` §3.1, optionally mention this paper as the preliminary version of Can et al. (2008). This is a proposal only; `CURRENT_GAP.md` has not been edited.

## 17. Implications for our research design

- **Lexical scoring must be fixed before comparing representations.** Here F5 vs SV flips with the weighting scheme (5 of 8 MFs). For us: one BM25 implementation, one tokenizer and apostrophe normalization, and fixed k1/b (or tuned on dev per variant, with the protocol reported) for raw/stem/lemma. Otherwise the "morphology effect" is partly a weighting-scheme effect.
- **Report the analyzer's coverage and the fallback.** If the Uzbek lemmatizer fails on part of the vocabulary, define `BM25_lemma` explicitly as either lemma-or-raw or lemma-or-stem, report the share of fallback tokens, and consider both variants. LV vs LM5 here shows that the fallback adds a small but consistent gain.
- **Pooling.** Include every compared condition (raw, stem, lemma BM25, D, hybrids) in the pool. Otherwise use a metric robust to incomplete judgments and report the unjudged rate. Here three of the five compared representations were outside the pool.
- **Statistics.** Test per query (paired tests or randomization/bootstrap with CIs) for each planned contrast. Do not use conditions such as weighting schemes as the pairing unit, and do not remove outlier queries post hoc without a pre-stated rule.
- **Dev/test separation.** Prefix length, lemma-selection heuristics, BM25 parameters and fusion weights are chosen only on dev queries.
- **Query filtering.** If queries with too few or too many relevant documents are removed, state the rule beforehand and report the count removed.
- **Metrics.** Report more than one metric (nDCG@10, Recall@100, MAP or bpref), because this paper's single metric limits comparison with its own journal version.
- **Hypothesis.** No evidence for or against morphology-induced complementarity; it only confirms that representation matters for the lexical channel.

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| Stemming | Cut words down to a shared stem so inflected forms match | Heuristic conflation of word forms to a stem |
| Fixed-prefix stemming (F5) | Keep only the first 5 letters | Pseudo-stemming by truncation to n characters |
| Successor variety (SV) | Cut the word where the corpus shows many different possible next letters | Hafer–Weiss corpus-statistical segmentation |
| Lemmatizer | Find the dictionary form of a word | Morphological analysis mapping a form to its lemma |
| LV | Lemmatize when possible, else use SV | LM5 with SV fallback for unanalyzable words |
| Matching function / SMART notation | The formula that weights words and scores documents | Vector-space weighting triple for documents.queries (e.g., tfc.nfx) |
| Pooling | Judge only documents that some tested systems retrieved in their top 100 | Union of top-k from contributing runs; incomplete qrels |
| bpref | Checks that judged relevant documents rank above judged non-relevant ones, ignoring unjudged documents | Buckley & Voorhees (2004) preference-based measure |
| One-sided matched-pair t-test | Tests whether A is better than B on paired observations | Paired t-test with a directional alternative |
| Complementarity (project term) | Each channel finds relevant documents the other misses | Unique relevant hits, overlap, oracle-union gain |

## 19. Open questions / verification needed

1. **Why do the MF8 values differ from the 2008 version** (e.g., LV .4319 vs .4504; MORPH-001 card)? Different query fields, qrels version or index? Not decidable from the poster; check in the 2008 PDF (CR000502) if the difference matters. Unverified clue: the MORPH-001 card lists QS/QM/QL with 2.89/12.00/26.11 unique words, and this paper's "about 11 distinct words" is closest to QM.
2. **Query fields used** ("about 11 distinct words"): NOT_REPORTED.
3. **Outlier criterion** for the two removed queries: NOT_REPORTED.
4. **Prefix-selection and LM5/LM6 numbers:** NOT_REPORTED (only graph-based ordering is described).
5. **Coordinator:** correct the systematic-review venue metadata ("SIGIR Forum / JOUR" → SIGIR 2006 proceedings, pp. 627–628, DOI 10.1145/1148170.1148288), and decide on FT8 (duplicate of CR000502) as the triage note suggests.

## 20. Decision after deep dive

- **Keep current gap?** Yes; v0.8 refined unchanged (§16).
- **Modify gap?** No. Optional: note this paper in `GAP_BOUNDARY` §3.1 as the preliminary version of Can et al. (2008).
- **Add decision?** Proposed for `decisions/DECISIONS.md` (researcher's decision):
  - "Morphology variants are compared under one fixed lexical scoring configuration, and each planned contrast is tested per query";
  - "the lemma variant's fallback rule for unanalyzable words is defined and its coverage is reported".
- **Add experiment?** No new experiment. It reinforces the planned pooling of all raw/stem/lemma/D/hybrid conditions.
- **Add citation to Chapter I?** Only as the first publication of the Milliyet collection in §1.1 (a historical note); cite `MORPH-001` (2008) for the substantive results.
- **Proposed `MASTER_INDEX.md` row** (to add after approval):

| MORPH-013 (preliminary version of MORPH-001) | Can, Kocberber, Balcik, Kaynak, Ocalan, Vursavas — *First Large-Scale Information Retrieval Experiments on Turkish Texts* (SIGIR 2006, pp. 627–628, 2-page paper) — [deep dive](deep-dives/2006_Can_First_Large_Scale_IR_Experiments_Turkish.md) | 2006 | A (narrow; superseded by MORPH-001) | LOW | First report of the Milliyet collection (408,305 docs, 72 queries, pooled binary qrels). bpref for NS/SV/F5/LM5/LV × 8 vector-space matching functions (Table I): normalization +29–35% over NS; LV best in all 8 MFs (C. Av. .3781 vs F5 .3603, SV .3591); F5 vs SV order depends on weighting scheme. Main significance test pairs over MFs, not queries. MF8 values differ from the 2008 version. No BM25, dense, fusion or overlap/unique-hit analysis. |
