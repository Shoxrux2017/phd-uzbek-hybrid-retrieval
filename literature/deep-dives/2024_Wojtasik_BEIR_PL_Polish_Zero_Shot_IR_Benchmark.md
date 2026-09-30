# Wojtasik, Shishkin, Wołowiec, Janz & Piasecki (2024): BEIR-PL: Zero Shot Information Retrieval Benchmark for the Polish Language

**Targeted deep-dive status:** COMPLETED (AI-assisted, pending researcher review)
**Completed:** 2026-09-28
**Literature ID:** `MORPH-008` (assigned 2026-09-28, approved by researcher)
**Systematic-review record:** `CR000103`. Full-text triage: INCLUDE (BORDERLINE on the morphology criterion q2), reading priority HIGH, tier "1 — прямо по теме пробела", `carries_complementarity_evidence = NO`
**Provenance:** AI-assisted deep dive (Claude). The paper was read in full (pdftotext, 12 pages, pp. 2149–2160). Page images were checked for every table and figure whose numbers are reported here: PDF pages 1, 3, 4, 5, 6, 7, 8 = printed pp. 2149 (byline), 2151 (Table 1), 2152 (Table 2, Sec. 3.2), 2153 (Figure 2, Secs. 3.2.1–3.4), 2154 (Table 3, Secs. 3.5–4), 2155 (Tables 4–5), 2156 (Table 6). Tables 4–6 and Figure 2 were re-rendered at 200–250 dpi and compared cell by cell. Numbers computed by us are marked **[computed]** (script re-run 2026-09-28).
**Verification:** independent AI verifier pass 2026-09-28; 8 findings addressed.
**Source rule:** **the paper is the primary and only authoritative source.** The web was used only to check the bibliographic record (marked "bibliographic check"). Statements about the related Polish works (CR000100, CR000913, CR000914) come from our systematic-review triage records, not from reading those papers, and are marked as such. Background knowledge appears only as labelled "Context (not from the paper)".
**Reliability:** **A** (peer-reviewed main-conference paper, LREC-COLING 2024, ACL Anthology). Caveat: the paper has several internal reporting inconsistencies (§9, §19). They lower confidence in individual table cells and in some prose claims, not in the venue level.

---

## Кратко для исследователя (RU)

- **Что сделано.** Авторы машинно перевели (Google Translate) все 13 открытых наборов BEIR на польский и получили бенчмарк BEIR-PL. На нём они сравнили:
  - BM25 (Elasticsearch + польский стеммер Stempel);
  - два слабых би-энкодера: HerBERT, дообученный без учителя на задаче ICT, и LaBSE;
  - шесть переранжировщиков поверх BM25: mMiniLM, HerBERT-base/large, plT5-base/large (MonoT5) и ColBERT, который использован **как переранжировщик, а не как ретривер**.
  - Дополнительно переранжировщики проверены на трёх исходно польских наборах PolEval 2022 (Table 6).
- **Главные числа** (Tables 3–4, pp. 2154–2155):
  - BM25 на польском хуже, чем на английском, на всех 11 наборах Table 3 **[computed]**:
    - средний nDCG@10 35.67 против 42.41: разница средних −15.9%, среднее относительных падений по наборам −17.3%;
    - средний Recall@100 48.85 против 56.53: разница средних −13.6%, среднее относительных падений −14.5%;
  - BM25 обходит оба би-энкодера на 12 из 13 наборов (исключение — Quora). Средний nDCG@10: BM25 37.64, ICT 19.84, LaBSE 22.51 **[computed]**;
  - переранжировщики в среднем лишь немного выше BM25 (лучший средний nDCG@10: HerBERT-large 41.46) **[computed]**. На ArguAna и Touche-2020 все шесть ниже BM25.
- **Морфология только как объяснение.** Разрыв PL–EN авторы приписывают флективности польского («Polish is a highly inflected language…», Sec. 4, p. 2154). Проверки нет:
  - BM25 запускался в одной конфигурации (со Stempel); варианта без стемминга или с лемматизацией нет, параметры k1/b не сообщаются;
  - разрыв PL–EN смешан с машинным переводом (сами авторы отмечают ошибки перевода именованных сущностей), с разными анализаторами и с неизвестным происхождением английских чисел;
  - на Fig. 2 китайский (не флективный) так же низок, как польский (MRR@10 0.12).
- **Плотный поиск слабый и не обучен на задаче поиска.** ICT — это предобучение без учителя, LaBSE — модель для эмбеддингов предложений/перевода. Вывод «BM25 сильнее плотного поиска» относится только к этим моделям, не к современным плотным ретриверам.
- **Нет гибрида и анализа взаимодополняемости:**
  - переранжирование поверх BM25 top-100 — это каскад, а не fusion: полнота ограничена полнотой BM25;
  - нет объединения оценок BM25 и плотного поиска;
  - нет перекрытия результатов, уникально найденных документов, oracle union и анализа по запросам. Есть только разбивка по наборам данных.
- **Внутренние несоответствия в статье** (подробно в §9 и §19):
  - Fig. 2 приписан mMARCO (Bonifacio et al.), хотя авторы сами пишут, что польского в mMARCO нет (Sec. 2, p. 2150; Sec. 3.1, p. 2152);
  - MRR@10 BM25 на MS MARCO: 0.12 на Fig. 2 против 68.09 в Table 4;
  - ось Fig. 2(b) подписана «MRR@1K», подпись — «MRR@10»;
  - заявлено «три» би-энкодера, описано два;
  - в тексте ссылка на «Figure 1» вместо таблицы с результатами;
  - ICT на SciFact: nDCG@10 38.17 при MRR@10 6.12. При бинарной релевантности это невозможно: nDCG@10/MRR@10 ≤ 3.40 **[computed]**;
  - в Table 5 у HerBERT-base и HerBERT-large совпадают значения в трёх столбцах;
  - порядок авторов в PDF и в ACL Anthology различается.
- **Для нашего gap:** не затрагивает остаточное ядро v0.8 (raw/stem/lemma BM25 × фиксированный D → overlap/unique hits → прирост гибрида). Даёт лишь ещё один пример того, что влияние морфологии на BM25 объясняют задним числом, но не измеряют. **Предложение: gap не менять.**
- **Практическая польза для нас:**
  1. Сравнение BM25 между языками (PL vs EN) не позволяет выделить эффект морфологии. Нужен наш дизайн: варианты raw/stem/lemma на одних и тех же узбекских запросах и qrels.
  2. LaBSE как ретривер слабый (к слову, LaBSE используется в рукописи Sharifbaev, UNVER-002). D должна быть моделью, обученной на задаче поиска и проверенной на узбекском пилоте.
  3. Переранжирование и fusion в главе I нужно разводить явно.
  4. В конвейер оценки стоит добавить автоматическую проверку согласованности метрик.
- **Польский кластер.** По записям триажа, ближе к нашему вопросу CR000100 (Silver Retriever: BM25 по словоформам и по леммам + плотные модели) и CR000914 (BM25 с разными лемматизаторами + fusion). BEIR-PL для gap вторичен.

---

## 1. Bibliographic record

- **Authors (PDF byline, p. 2149):** Konrad Wojtasik, Vadim Shishkin, Kacper Wołowiec, Arkadiusz Janz, Maciej Piasecki
  - **Order discrepancy:** the PDF's embedded metadata, our systematic-review metadata and the ACL Anthology record list Wołowiec second and Shishkin third (bibliographic check: ACL Anthology). The printed byline lists Shishkin second. For citation, follow the official Anthology record and keep this note.
- **Affiliation:** Wrocław University of Science and Technology (all authors, p. 2149)
- **Year:** 2024
- **Venue:** *Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)*, 20–25 May 2024 (printed footer, p. 2149); Torino, Italia (bibliographic check: ACL Anthology)
- **Pages:** 2149–2160 (printed footer)
- **Publisher:** ELRA and ICCL (bibliographic check: ACL Anthology); footer: "© 2024 ELRA Language Resource Association: CC BY-NC 4.0"
- **Editors:** Nicoletta Calzolari, Min-Yen Kan, Veronique Hoste, Alessandro Lenci, Sakriani Sakti, Nianwen Xue (bibliographic check: ACL Anthology)
- **ACL Anthology ID:** `2024.lrec-main.194`; **Official record:** https://aclanthology.org/2024.lrec-main.194/ (bibliographic check)
- **DOI:** none listed on the Anthology page (bibliographic check); not printed in the paper
- **Preprint:** arXiv:2305.19840 (bibliographic check: web search result; not used as a content source)
- **Resources (stated in the paper, abstract):** BEIR-PL and trained models at https://huggingface.co/clarin-knext; BEIR-PL "is included in MTEB Benchmark"
- **Source type:** peer-reviewed conference paper (resource/benchmark paper)
- **Reliability:** A
- **Full text available:** yes (`07_full_text/pdfs/CR000103.pdf`, 12 pages including references and Appendix A)

## 2. Why this work matters to the PhD

It is a peer-reviewed benchmark paper for a **morphologically rich, less-resourced European language** (Polish: Slavic, fusional, heavily inflected). It puts a **stemmed BM25** next to neural bi-encoders and several neural rerankers, and explicitly **attributes the weaker Polish BM25 to inflection**. That attribution is what brought it into the systematic review.

| Axis | Relation |
|---|---|
| Lexical retrieval | BM25 in Elasticsearch with the Stempel Polish analyzer. One configuration only; k1/b, stop-words and fields are NOT_REPORTED |
| Semantic retrieval | Two weak single-vector bi-encoders: an unsupervised ICT-trained HerBERT and LaBSE. No retrieval-supervised dense retriever |
| Hybrid retrieval | **Absent** as fusion. Present only as a **cascade**: BM25 top-100 → neural reranker |
| Uzbek morphology | Indirect. Polish is fusional Slavic, Uzbek agglutinative Turkic; both have many word forms per lexeme |
| Low-resource retrieval | Direct: machine-translated benchmark as a substitute for native annotated data |
| Current gap | No material effect on the v0.8 core (§16). Useful mainly as a methodological counter-example: a cross-language BM25 comparison cannot isolate morphology |

## 3. Research problem

### Simple explanation

Polish lacked large test collections for search, so neural search models could not be properly trained or compared. The authors translate the English BEIR collections into Polish automatically and use them to measure how a word-matching engine (BM25) and several neural models perform on Polish.

### Formal formulation

The paper states no formal research questions. The stated aims (Sec. 1, pp. 2149–2150) are:

- build a large-scale zero-shot IR benchmark for Polish (BEIR-PL);
- train and evaluate IR models from the literature on it and "establish a baseline for future research";
- show that BEIR-PL, like BEIR, is heterogeneous, so models must be compared per dataset "rather than relying solely on overall averages" (contribution bullet, pp. 2149–2150);
- test the trained rerankers on the PolEval 2022 passage-retrieval test sets.

Tasks: first-stage retrieval (BM25, bi-encoders) and second-stage reranking of BM25 candidates, evaluated by nDCG@10 and MRR@10 (Recall@100 for BM25 only).

## 4. Main idea

### Simple explanation

1. Translate every BEIR query and document into Polish with Google Translate.
2. Keep the original relevance labels.
3. Run BM25 and neural models on the result and compare.

### Concrete example

Figure 1 (p. 2150) is the paper's own schematic (in English):

- Query: "Where is Paris?"
- BM25 ranks "Paris is known for …" first and "Paris is in France" third.
- A reranker re-scores these BM25 candidates and moves "Paris is in France" to rank 1.
- The reranker can only reorder documents that BM25 already returned.

### Formal method

- **BM25 (Elasticsearch + Stempel):** standard lexical scoring over stemmed Polish tokens (Sec. 3.2, p. 2152). No formula or parameters are given.
- **Bi-encoder:** `f(q,d) = cos(E(q), E(d))`, with a precomputed dense index of documents (Sec. 3.2.1, p. 2153).
- **Rerankers:** a cross-encoder (HerBERT, mMiniLM) or a sequence-to-sequence model (plT5 MonoT5, which emits the special tokens `_prawda` 'true' / `_fałsz` 'false') scores each (query, BM25 candidate) pair. ColBERT is used as a late-interaction reranker (Secs. 3.2.2–3.3, p. 2153).

## 5. Architecture / algorithm

1. **Translation** (Sec. 3.1, p. 2152):
   - Google Translate for all queries and corpora. The authors chose it because, during mMARCO, it was "better than" the open Helsinki MT model.
   - Output format is BEIR-compatible: JSONL queries/corpus, TSV qrels.
2. **Translation quality check** (Sec. 3.1, Table 2, p. 2152):
   - "we have selected 100 random queries and passages which were evaluated by a linguist in a Strict setting and a researcher in Semantic setting";
   - plus LaBSE similarity between source and translation.
   - Whether the 100 items are per column or in total is not stated.
3. **Lexical baseline** (Sec. 3.2, p. 2152), verbatim: "The main baseline was computed using lexical matching with the BM25 implementation from Elasticsearch engine with Stempel Polish analysis plugin." (There is a footnote marker after "engine" that points to elastic.co.)
   - NOT_REPORTED: k1, b, stop-words, lowercasing and other analyzer settings, whether titles were indexed.
   - Context (not from the paper): Stempel is a Polish stemmer distributed as an Elasticsearch analysis plugin. In our terms this is a **stem-type** lexical representation, not a raw or lemma one.
4. **Bi-encoders** (Secs. 3.2, 3.2.1, 3.4, pp. 2152–2153):
   - **ICT:** HerBERT-base fine-tuned with the unsupervised Inverse Cloze Task on the BEIR-PL datasets; "For each document, a pseudo-query was generated". Training: 203 h, batch 64, ~1.8M iterations, lr 2e−4 (Sec. 3.5, p. 2154).
   - **LaBSE:** pre-trained multilingual model, "fine-tuned to the sentence embedding task".
   - The text says "We evaluated three BERT-only bi-encoder models" (p. 2152) but describes and reports only two (§19).
5. **Rerankers** (Secs. 3.2.2–3.4, 3.5, pp. 2153–2154):
   - **HerBERT-base / HerBERT-large cross-encoders:** trained on BEIR-PL MS MARCO; ≈25 h, batch 32; 20M / 3.2M examples. They rerank "the top 100 search results … retrieved by BM25".
   - **plT5-base / plT5-large (MonoT5):** "pre-trained for Polish language on translated MS-MARCO data"; 20 h, gradient accumulation 16, batch 16; 5M / 645K examples.
   - **ColBERT (HerBERT-base core):** 102 h on one RTX 2080 Ti, batch 8, lr 3e−6; max 180 document tokens, 32 query tokens. Used "as a reranker, which does not require creating enormous indexes" (index for MSMARCO-PL estimated at "at least 200GB"). Its training data is not stated explicitly.
   - **mMiniLM:** an existing multilingual cross-encoder trained on multilingual MS MARCO (80M examples); not trained by the authors.
   - The candidate depth is stated as top-100 BM25 only for the HerBERT rerankers (Sec. 3.2.2). For T5, ColBERT and mMiniLM it is not stated separately.
6. **Hardware:** two RTX 3090 (24 GB) for all models except ColBERT.

## 6. Data

### BEIR-PL (Table 1, p. 2151)

- **Source:** machine translation of 13 BEIR datasets: MSMARCO, TREC-COVID, NFCorpus, NQ, HotpotQA, FiQA, ArguAna, Touche-2020, CQADupstack, Quora, DBPedia, SciDocs, SciFact.
- **Language / domains:** Polish; web QA, bio-medical, finance, argument retrieval, duplicate-question detection, entity search, scientific.
- **Sizes (Table 1):**
  - test queries range from 49 (Touche-2020) and 50 (TREC-COVID) to 13,145 (CQADupstack) and 10,000 (Quora);
  - corpora range from 3.6K (NFCorpus) to 8.8M (MSMARCO) passages;
  - average query length ranges from 3.37 words (NFCorpus) to 168.01 words (ArguAna).
- **Relevance judgments:** no new Polish judgments are described. The paper describes only the qrels format (Sec. 3.1). *Our inference:* the original BEIR qrels were carried over unchanged, assuming relevance survives translation. The paper does not state this explicitly.
- **Train/dev/test:**
  - evaluation is on the BEIR test data (Table 3 caption: "on test data");
  - rerankers are trained on the BEIR-PL MS MARCO training data, so for them MS MARCO is **in-domain**, not zero-shot;
  - ICT is trained without labels on the BEIR-PL corpora themselves.
- **Translation quality (Table 2, p. 2152):**

| | DBPedia Q. | FiQA Q. | HotpotQA Q. | HotpotQA C. | MSMARCO C. | MSMARCO Q. | SciFact Q. | Quora Q. | Quora C. |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| LaBSE | 0.89 | 0.88 | 0.90 | 0.93 | 0.91 | 0.87 | 0.88 | 0.90 | 0.91 |
| Semantic (researcher) | 0.85 | 0.80 | 0.84 | 0.88 | 0.84 | 0.91 | 0.80 | 0.82 | 0.92 |
| Strict (linguist) | 0.61 | 0.52 | 0.72 | 0.70 | 0.52 | 0.77 | 0.72 | 0.72 | 0.78 |

- By the strict criterion, only 52–78% of sampled items are correct translations.
- The authors: "Errors were particularly noticed in the translation of Named Entities and when translated, queries sought the same information but had incorrect phrasing." (p. 2152)

### PolEval 2022 passage retrieval (Table 6, p. 2156)

- Three natively Polish test domains, each with test sets A and B: Allegro-FAQ, Legal Questions, Wiki Trivia.
- Collection sizes, query counts and qrels procedure are NOT_REPORTED in this paper.
- Only BM25 and the rerankers are evaluated here; no bi-encoders.

## 7. Baselines

| System | What it is | Why selected (per paper) | Fair comparison? |
|---|---|---|---|
| BM25 + Stempel (Elasticsearch) | Lexical ranking over stemmed Polish tokens | "standard baseline method used in IR" and typical first stage | **Partly.** A single configuration with nothing reported beyond the analyzer name. No raw or lemma variant and no tuning, so it is not a morphology comparison |
| ICT-HerBERT-base (bi-encoder) | Polish BERT trained with an unsupervised pseudo-query task | Unsupervised dense retrieval for zero-shot | **Weak comparator.** It never sees real query–document supervision, so it is not representative of modern dense retrievers |
| LaBSE (bi-encoder) | Multilingual sentence-embedding model | Pre-existing multilingual comparator | **Weak comparator** for ad hoc retrieval: it is trained for sentence similarity, not query–passage retrieval |
| mMiniLM, HerBERT-b/l, plT5-b/l | Rerankers over BM25 candidates | Recent reranking literature | Comparable with each other. Versus BM25 they are **cascade** systems that include BM25, not alternatives to it |
| ColBERT (HerBERT) | Late-interaction model, used here only as a reranker | Speed/quality trade-off | Same caveat. It does **not** show ColBERT's first-stage retrieval ability, because it was never used as a retriever |
| BM25 English (Table 3) | Original BEIR scores in English | PL vs EN comparison | **Provenance NOT_REPORTED**: the paper does not say whether the numbers were re-run (and with which analyzer) or copied |

## 8. Metrics

Definitions follow Appendix A (pp. 2159–2160).

| Metric | Definition (paper) | Simple meaning | Appropriate? |
|---|---|---|---|
| MRR@10 | mean over queries of 1/rank of the first relevant passage (formula printed without the @k cut-off) | "How high is the first correct passage?" | Yes for QA-style tasks; ignores further relevant documents |
| nDCG@10 | DCG with "Gain … equal to 1 if passage relevant and 0 otherwise", divided by the ideal DCG | Quality of the top 10, crediting all relevant documents with a log-rank discount | Yes (BEIR's main metric). The paper states binary gain |
| Recall@100 | \|relevant ∩ retrieved@100\| / \|relevant\| | Share of relevant documents inside the top 100 | Yes. This is the candidate-coverage view; reported **only for BM25** (Table 3) |
| Recall@1K, MRR@10 on MS MARCO (Fig. 2) | as above | Cross-language BM25 comparison | Values are attributed to Bonifacio et al. (2021) |

Significance tests: none (§10).

## 9. Results

### Table 3: BM25, Polish vs English, "on test data" (p. 2154)

| Dataset | nDCG@10 PL | nDCG@10 EN | Δ rel. **[computed]** | R@100 PL | R@100 EN | Δ rel. **[computed]** |
|---|---:|---:|---:|---:|---:|---:|
| MSMARCO | 41.9 | 47.7 | −12.2% | 34.6 | 45.0 | −23.1% |
| TREC-COVID | 61.0 | 68.9 | −11.5% | 10.1 | 11.7 | −13.7% |
| NFCorpus | 31.9 | 34.3 | −7.0% | 24.6 | 26.0 | −5.4% |
| NQ | 20.1 | 32.6 | −38.3% | 57.9 | 78.3 | −26.1% |
| HotpotQA | 49.2 | 60.2 | −18.3% | 67.1 | 76.3 | −12.1% |
| FiQA | 19.0 | 25.4 | −25.2% | 44.1 | 54.9 | −19.7% |
| ArguAna | 41.36 | 47.2 | −12.4% | 93.5 | 95.2 | −1.8% |
| CQADupstack | 28.37 | 32.5 | −12.7% | 53.9 | 62.1 | −13.2% |
| DBPedia | 22.9 | 32.1 | −28.7% | 30.1 | 43.5 | −30.8% |
| SciDocs | 14.1 | 16.5 | −14.5% | 33.0 | 36.8 | −10.3% |
| SciFact | 62.5 | 69.1 | −9.6% | 88.4 | 92.0 | −3.9% |
| **Mean (11)** **[computed]** | 35.67 | 42.41 | −15.9% between means; −17.3% mean of per-dataset drops | 48.85 | 56.53 | −13.6% between means; −14.5% mean of per-dataset drops |

- PL < EN on all 11 datasets and both metrics **[computed]**.
- Touche-2020 and Quora are **not** in Table 3 (11 of 13 datasets).
- The PL nDCG@10 values equal Table 4's BM25 row truncated to one decimal (22.98 → 22.9; 62.56 → 62.5; 14.13 → 14.1), except ArguAna and CQADupstack, which keep two decimals. This is cosmetic.

**Authors' interpretation** (Sec. 4, p. 2154, verbatim): "The main cause of such a low performance scores for Polish language is that Polish is a highly inflected language with large number of word forms per lexeme (also Proper Names are inflected) and a complex morphological structure. In such a case, lexical matching is less effective than in the case of other languages."

- This is an **explanation, not a tested result**. There is no ablation (e.g., BM25 without Stempel, or with lemmatization) and no control for translation (§12).

### Figure 2: BM25 on MS MARCO passage retrieval across languages, attributed to Bonifacio et al. (2021) (p. 2153)

| | EN | ES | FR | IT | PT | ID | DE | RU | ZH | PL |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Recall@1K (a) | 0.86 | 0.77 | 0.77 | 0.75 | 0.74 | 0.77 | 0.67 | 0.69 | 0.68 | 0.67 |
| MRR@10 (b) | 0.18 | 0.16 | 0.16 | 0.15 | 0.15 | 0.15 | 0.14 | 0.12 | 0.12 | 0.12 |

- The text says Polish shows "one of the lowest scores". On the figure, Polish is **tied**: with German on Recall@1K (0.67), and with Russian and Chinese on MRR@10 (0.12).
- Our inference: Chinese is not inflectional, yet it is as low as Polish. Low BM25 on a translated collection therefore does not by itself indicate an inflection effect.
- PL vs EN: −22.1% Recall@1K, −33.3% MRR@10 **[computed]**.
- **Internal inconsistencies:**
  - the y-axis of panel (b) reads "MRR@1K", while the caption reads "MRR@10";
  - the figure is attributed to Bonifacio et al. (2021), but the paper itself says that MS MARCO had been translated "into many different languages (Bonifacio et al., 2021), but not to Polish, yet" (Sec. 2, p. 2150). It repeats that Polish was not included in mMARCO (Sec. 3.1, p. 2152), and Sec. 1 (p. 2149) similarly says Polish is not covered by "the original multilingual MS MARCO dataset". The source of the Polish bar is therefore unstated.

### Table 4: all BEIR-PL datasets, nDCG@10 (p. 2155)

✓ = fine-tuned by the authors; ✗ = pre-existing multilingual model.

| Model | MSM | T-COV | NFC | NQ | HQA | FiQA | ArgA | Touche | CQA | Quora | DBP | SciD | SciF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| BM25 ✗ | 41.92 | 61.00 | 31.92 | 20.14 | 49.21 | 19.00 | **41.36** | **32.89** | 28.37 | 63.87 | 22.98 | 14.13 | 62.56 |
| ICT ✓ | 29.02 | 22.48 | 15.05 | 0.79 | 7.97 | 9.61 | 20.82 | 13.07 | 9.98 | 72.61 | 14.74 | 3.60 | 38.17 |
| LaBSE ✗ | 17.55 | 18.52 | 17.45 | 9.62 | 19.74 | 7.66 | 38.56 | 5.16 | 20.01 | 75.00 | 16.08 | 7.47 | 39.79 |
| mMiniLM ✗ | 64.10 | 64.70 | 29.84 | 34.16 | 59.81 | 27.67 | 22.10 | 30.36 | 27.94 | 68.73 | 29.61 | 12.21 | 60.08 |
| HerBERT-base ✓ | 62.45 | 56.63 | 30.17 | 33.53 | 57.44 | 26.33 | 21.09 | 26.76 | 26.85 | 68.74 | 27.67 | 12.01 | 60.31 |
| HerBERT-large ✓ | 64.00 | 58.44 | 27.77 | 36.94 | 61.78 | 28.95 | 33.76 | 27.79 | 28.53 | 73.90 | **30.00** | 13.03 | 54.13 |
| plT5-base ✓ | **64.23** | 68.53 | 32.79 | 35.77 | **63.13** | 25.93 | 15.52 | 23.97 | 30.40 | 49.94 | 18.21 | 14.35 | 68.54 |
| plT5-large ✓ | 62.81 | **73.66** | **35.61** | **39.53** | 62.21 | **30.92** | 13.04 | 26.21 | **32.05** | 50.82 | 18.20 | **14.79** | **69.55** |
| ColBERT ✓ | 60.11 | 64.72 | 31.79 | 31.84 | 51.85 | 25.82 | 37.10 | 26.76 | 27.92 | **75.44** | 26.87 | 11.51 | 55.85 |

Bold follows the paper's bold (best per column).

### Table 4: MRR@10 (p. 2155)

| Model | MSM | T-COV | NFC | NQ | HQA | FiQA | ArgA | Touche | CQA | Quora | DBP | SciD | SciF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| BM25 | 68.09 | 84.03 | 46.44 | 17.50 | 64.18 | 23.73 | **33.17** | **68.18** | 27.90 | 63.75 | 48.56 | 25.59 | 62.56 |
| ICT | 43.91 | 39.39 | 29.81 | 0.72 | 10.46 | 11.63 | 13.53 | 28.88 | 9.52 | 71.77 | 31.05 | 10.23 | 6.12 |
| LaBSE | 40.90 | 39.23 | 31.99 | 8.27 | 27.12 | 9.36 | 31.85 | 13.65 | 19.49 | 74.39 | 36.53 | 13.37 | 36.45 |
| mMiniLM | 91.55 | 85.81 | 44.37 | 31.47 | 77.39 | 35.57 | 17.43 | 60.19 | 27.95 | 66.80 | 56.96 | 22.39 | 56.79 |
| HerBERT-base | 90.11 | 79.66 | 46.78 | 30.74 | 73.98 | 34.28 | 16.31 | 50.54 | 26.42 | 67.04 | 52.02 | 21.34 | 57.37 |
| HerBERT-large | **91.86** | 78.80 | 42.50 | 34.40 | 79.41 | 37.29 | 18.31 | 45.23 | 27.90 | 73.06 | **58.42** | 23.21 | 58.63 |
| plT5-base | 89.53 | 80.40 | 48.62 | **38.63** | **80.60** | 33.77 | 13.11 | 43.20 | 30.03 | 49.32 | 38.22 | 26.50 | 66.62 |
| plT5-large | 89.15 | **90.73** | **51.23** | 36.67 | 79.59 | **39.75** | 11.09 | 46.15 | **31.70** | 50.19 | 39.96 | **26.92** | **67.73** |
| ColBERT | 85.89 | 81.07 | 47.24 | 29.00 | 68.67 | 32.93 | 30.06 | 49.26 | 27.76 | **75.34** | 51.64 | 20.79 | 52.78 |

**Reading Table 4** (all counts and means **[computed]**; the authors report no averages and argue against relying on them):

- **BM25 vs bi-encoders:**
  - BM25 beats *both* ICT and LaBSE on 12 of 13 datasets for both nDCG@10 and MRR@10; the exception is Quora, where LaBSE is 75.00 and ICT 72.61 vs BM25 63.87 nDCG@10.
  - Mean nDCG@10: BM25 37.64, ICT 19.84, LaBSE 22.51. Mean MRR@10: BM25 48.74, ICT 23.62, LaBSE 29.43.
  - This supports the authors' statement (p. 2154) that "BM25 is a better choice for most datasets". The sentence cites "Figure 1", which is the reranking schematic; the evidence is in Table 4 (§19).
- **Rerankers vs BM25 (cascade over BM25):**
  - mean nDCG@10: mMiniLM 40.87, HerBERT-base 39.23, HerBERT-large 41.46, plT5-base 39.33, plT5-large 40.72, ColBERT 40.58 (BM25 37.64);
  - all six rerankers are below BM25 on ArguAna and Touche-2020, as the authors state (p. 2156);
  - however, 4 of 6 rerankers are also below BM25 nDCG@10 on NFCorpus, SciDocs and SciFact, and 3 of 6 on CQADupstack. The authors' "Only in the case of the ArguAna and Touche-2020" is correct only in the sense that *all* rerankers fall below there;
  - on the same page (p. 2156) the authors also note that "the results on Quora dataset are worse after re-ranking than BM25" for T5. Table 4 agrees: T5-base 49.94 and T5-large 50.82 vs BM25 63.87 nDCG@10.
- **ColBERT vs BM25:**
  - ColBERT is above BM25 on 7 of 13 datasets for each metric; the sets differ (nDCG@10 includes TREC-COVID, MRR@10 includes NFCorpus).
  - The authors call this "significant improvements over the BM25 retriever on the majority of datasets" (p. 2156), but no significance test was run (§10).
  - Mean nDCG@10: 40.58 vs 37.64.
- **MS MARCO is in-domain for the rerankers**, which were trained on BEIR-PL MS MARCO. Their MRR@10 there (85.89–91.86 vs BM25 68.09) is not a zero-shot result.
- **Consistency check (passes with one exception):** the CQADupstack cells of Table 4 equal the macro-average of the 12 Table 5 subsets within 0.01 for all MRR@10 rows and all nDCG@10 rows, e.g., BM25 nDCG@10 28.38 **[computed]** vs 28.37 and ColBERT 27.92 vs 27.92.
  - The exception is **HerBERT-base nDCG@10**: 26.825 **[computed]** vs 26.85 in Table 4. This is small, but it is the row that also has the duplicated Table 5 cells (see below).

### Table 5: CQADupstack subsets, nDCG@10 (p. 2155; selected rows)

| Model | android | english | gaming | gis | math | physics | program. | stats | tex | unix | webmasters | wordpress |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| BM25 | 36.29 | 25.34 | 38.58 | 25.95 | 19.06 | 30.97 | 32.21 | 28.42 | 20.94 | 26.86 | 30.61 | 25.29 |
| LaBSE | 30.31 | 15.55 | 31.50 | 17.59 | 13.62 | 22.50 | 19.98 | 17.11 | 13.20 | 21.01 | 22.60 | 15.05 |
| HerBERT-base | 33.99 | 26.80 | 38.20 | 23.09 | 17.29 | 30.92 | 28.22 | 23.42 | 21.24 | 26.25 | 28.13 | 24.35 |
| HerBERT-large | 37.72 | **30.24** | 38.20 | 23.09 | 18.48 | 30.92 | 29.63 | 24.57 | 22.37 | 30.58 | 31.03 | 25.64 |
| plT5-large | **42.05** | 14.54 | **48.30** | **30.75** | **23.02** | **37.68** | **34.68** | **30.90** | **24.78** | **32.08** | **35.66** | **30.18** |

- plT5-large is best on 11 of 12 subsets; the exception is "english", where HerBERT-large leads. This matches the text on p. 2156.
- BM25 > LaBSE on all 12 subsets **[computed]**.
- **Possible copy error:** HerBERT-base and HerBERT-large have identical values in the gaming, gis and physics columns, for both nDCG@10 (38.20 / 23.09 / 30.92) and MRR@10 (37.04 / 21.52 / 30.82). Checked on the page image. It cannot be resolved from the paper.

### Table 6: PolEval 2022, natively Polish data (p. 2156)

| Model | Allegro-FAQ A | Allegro-FAQ B | Legal Q. A | Legal Q. B | Wiki Trivia A | Wiki Trivia B |
|---|---:|---:|---:|---:|---:|---:|
| BM25 nDCG@10 | 61.00 | 58.31 | 79.14 | 81.35 | 26.04 | 24.20 |
| best reranker nDCG@10 | 82.75 (T5-l) | 80.16 (HB-l) | 84.76 (mMiniLM) | 85.89 (HB-l) | 40.07 (HB-l) | 40.74 (HB-l) |
| BM25 MRR@10 | 55.01 | 52.00 | 83.56 | 86.90 | 35.14 | 33.66 |
| best reranker MRR@10 | 79.45 (T5-l) | 76.38 (HB-l) | 92.22 (mMiniLM) | 92.15 (mMiniLM) | 57.23 (HB-l) | 57.68 (HB-l) |

- Best-reranker gain over BM25 in nDCG@10 **[computed]**: +21.75 / +21.85 (Allegro-FAQ), +5.62 / +4.54 (Legal Questions), +14.03 / +16.54 (Wiki Trivia).
- On legal data, BM25 is already strong (nDCG@10 ≈ 79–81), so the reranking gain is smallest there.
  - The BM25 configuration for the PolEval runs is not stated separately. That it is the same Elasticsearch + Stempel baseline is **our assumption**.
- From this table the authors conclude that the translation quality "is sufficient for Information Retrieval task" (p. 2157). That is an indirect argument: models trained on translated data transfer to native data.

### Internal numerical inconsistency: ICT on SciFact (Table 4)

- nDCG@10 = 38.17 but MRR@10 = 6.12, a ratio of 6.24.
- Under the paper's own binary-gain definitions (App. A), per-query nDCG@10 / MRR@10 cannot exceed **3.40** (maximum at 3 relevant documents with the first at rank 8) **[computed]**. The ratio of the means therefore cannot exceed it either.
- One of the two cells is probably mis-transcribed. It cannot be resolved from the paper.
- All other rows pass this check **[computed]**.

## 10. Statistical evidence

- **Significance tests:** NOT_REPORTED. Words like "significant improvement" in Sec. 4 and the Conclusions are not backed by any test.
- **Confidence intervals:** NOT_REPORTED.
- **Runs / seeds:** NOT_REPORTED; apparently a single run per model.
- **Ablation:** none. In particular, there is no BM25 without Stempel, no lemmatized BM25, no ablation of translation vs original, and no analysis of reranking depth.
- **Per-query analysis:** none. Analysis is per dataset (Tables 4–6) and per CQADupstack subset (Table 5), with qualitative explanations: Quora = duplicate-question similarity; NQ/HotpotQA = lexical distance; ArguAna/Touche = counter-arguments; medical sets = keyword overlap.
- **Gap dimensions** (explicit check):
  - morphological variants of the lexical representation: **no** (stem only);
  - BM25: **yes**;
  - dense retrieval: **yes, weak** (unsupervised ICT, LaBSE);
  - fusion / hybrid: **no**; only a BM25 → reranker cascade;
  - overlap / unique relevant hits / oracle union: **no**;
  - per-query or query-feature analysis: **no**.

## 11. Strengths

- A large, BEIR-compatible Polish IR resource (13 datasets), publicly released and included in MTEB (abstract).
- A translation-quality check with two human settings plus an automatic LaBSE score (Table 2). The strict scores (0.52–0.78) are reported honestly.
- Broad family of rerankers (cross-encoder, seq2seq, late interaction; base and large) under one BM25 first stage.
- Validation on natively Polish PolEval data (Table 6), which partially addresses the translation concern for rerankers.
- Methodological stance that models must be compared per dataset, not by averages alone (contribution bullet, pp. 2149–2150).
- The BM25 analyzer is at least named (Stempel), unlike many papers that do not name any.

## 12. Limitations

### Stated by the authors

- Translations are "adequate to the IR task, but not perfect". Errors concern named entities and query phrasing (Sec. 3.1, p. 2152).
- Manual verification of the full resource "would be very laborious". Instead, "100 random queries and passages" were checked (Sec. 3.1, p. 2152).
- ColBERT indexing "requires large disk and memory space" (the MSMARCO-PL index is estimated at "at least 200GB"). "Due to that reason, we decided to use ColBERT as a reranker" (Sec. 3.3, p. 2153). This is a cost-based choice.
- ICT is "an insufficient approach" for NQ and HotpotQA (Sec. 4, p. 2154).
- Training-set sizes differ between the base and large models because of compute cost (Sec. 3.5).

### Inferred from the experimental design

1. **The morphology attribution is untested and confounded.** The PL–EN BM25 gap mixes at least four factors:
   - (a) inflection;
   - (b) machine-translation effects. Query and document are translated independently, so lexical choices may diverge, and named-entity errors are reported by the authors themselves;
   - (c) different analyzers (Stempel vs an unreported English setting);
   - (d) qrels transferred from English without re-judgment.
   No within-Polish morphology manipulation (none / stem / lemma) is reported. Fig. 2 also shows Chinese as low as Polish.
2. **The dense comparators are not retrieval-trained.** "BM25 > bi-encoders" says nothing about supervised or modern multilingual dense retrievers.
3. **Rerankers are not independent of BM25.** They reorder BM25's top-100 (stated for HerBERT), so their recall is capped by BM25 Recall@100, which is as low as 10.1 on TREC-COVID and 30.1 on DBPedia (Table 3). Reranker-vs-BM25 differences are not lexical-vs-neural channel comparisons.
4. **"Zero-shot" is not uniform.** MS MARCO is in-domain for the rerankers, and ICT was trained on the target corpora without labels.
5. **Recall is reported only for BM25** (Table 3). Candidate coverage of the dense models is unknown.
6. **No significance tests, no variance, no per-query analysis** (§10).
7. **Reporting inconsistencies:** Fig. 2 source and axis label; "three" bi-encoders; the "Figure 1" reference; ICT SciFact MRR; duplicated Table 5 cells; author order (§19).
8. BM25 settings other than the analyzer are NOT_REPORTED: k1, b, fields, stop-words.

## 13. What the work proves

- On machine-translated BEIR, BM25 with a Polish stemmer scores **lower than English BM25 on all 11 compared datasets**: mean nDCG@10 35.67 vs 42.41 (−15.9%); mean Recall@100 48.85 vs 56.53 (−13.6%) **[computed from Table 3]**. The *cause* is not established (§14).
- On BEIR-PL, **stemmed BM25 clearly outperforms an unsupervised ICT bi-encoder and LaBSE** on 12 of 13 datasets. Quora is the exception, where the task is duplicate-question similarity (Table 4).
- **Neural reranking of BM25 candidates** gives modest average gains on BEIR-PL (best mean nDCG@10 41.46 vs 37.64 **[computed]**). The effect varies strongly by dataset: all rerankers lose on ArguAna and Touche-2020, and most lose on NFCorpus, SciDocs and SciFact.
- On natively Polish PolEval data, rerankers trained on translated MS MARCO **improve** BM25 on all six test sets (Table 6). The gain is smallest on legal questions, where BM25 is already strong.
- Model rankings on BEIR-PL are **heterogeneous across datasets**. The authors' claim is supported by Tables 4–5.

## 14. What the work does NOT prove

- **That Polish inflection causes the lower BM25 scores.** No morphology manipulation is reported, and translation, analyzer and qrels-transfer confounds are uncontrolled.
- **Anything about raw vs stem vs lemma representations.** Only the stemmed configuration is reported.
- **That BM25 beats dense retrieval in general for Polish.** The dense models are unsupervised or sentence-similarity models, not retrieval-trained.
- **That lexical and dense retrieval are complementary, or that a hybrid helps.** There is no fusion and no overlap, unique-hit or oracle-union analysis. The cascade is not fusion.
- **Which queries favour lexical vs neural matching.** Explanations are post hoc, at dataset level, with no per-query or query-feature evidence.
- **Statistical reliability of any difference.** No tests were run.
- **ColBERT's value as a first-stage retriever.** It was used only as a reranker.

## 15. Relationship to current Uzbek evidence

- **No Uzbek data.** Polish (Slavic, fusional) and Uzbek (Turkic, agglutinative) differ typologically. Both have a large number of word forms per lexeme, which is the property the authors invoke.
- **Methodological lesson for Uzbek:**
  - a cross-language BM25 comparison, especially on machine-translated collections, cannot isolate the morphology effect;
  - our design (raw/stem/lemma BM25 on the *same* Uzbek queries and qrels, with a fixed D) is the proper control that this paper lacks.
- **Parallels with Uzbek work:**
  - LaBSE is the dense component in the Sharifbaev 2026 manuscript (UNVER-002: lemmatized BM25 + LaBSE). Here LaBSE is a weak retriever on 12 of 13 Polish datasets (mean nDCG@10 22.51 vs stemmed BM25 37.64 **[computed]**). This is a caution against LaBSE-like D choices.
  - Machine-translating BEIR / MS MARCO into Uzbek is a tempting shortcut, like BEIR-PL. The strict-quality scores (0.52–0.78, Table 2) and the named-entity errors show why translated data should serve for **training and dev** only, not as the main qrels.
- **Polish cluster** (from our triage records, not read in full here):
  - **CR000100**, Rybak & Ogrodniczuk, *Silver Retriever* (LREC-COLING 2024): per triage, compares BM25 on word forms vs lemmas with dense models on PolQA / Allegro FAQ / Legal Questions. Lemmatized BM25 is better on two datasets and worse on Legal Questions. This is closer to our variable than BEIR-PL.
  - **CR000914**, Pacanowska (FedCSIS 2023): per triage, BM25 without lemmatization and with Morfeusz2 / spaCy / hybrid lemmatizers, neural reranking and score fusion on PolEval 2022.
  - **CR000913**, PolEval 2022/23 overview: per triage, participant systems differ in morphological normalization for BM25; no controlled comparison.
  - The same PolEval test sets appear in BEIR-PL Table 6, where BM25 (configuration not stated separately for PolEval; presumably the same Stempel baseline, our assumption) has nDCG@10 61.00 / 58.31 (Allegro-FAQ) and 79.14 / 81.35 (Legal Questions). Whether these match the BM25 variants in CR000100 / CR000914 should be checked when those cards are written. Differences could reflect different test splits.
  - Leads cited in the paper's references (not evidence): Pokrywka 2023 (Okapi BM25 + ensemble of cross-encoders for Polish passage retrieval); Kozłowski 2023 (hybrid retrievers with generative re-rankers).
- **Consistency with CR000477** (Amharic legal RAG, excluded at triage as FT2), as the triage note requested. In both works morphology appears only as a post hoc explanation of a weaker BM25, with no manipulation. BEIR-PL differs in that its BM25 explicitly uses a stemmer. After full reading, BEIR-PL's inclusion remains **borderline-defensible**, but its evidentiary weight for the gap is low (a proposal for the researcher).

## 16. Relationship to CURRENT_GAP

**Classification:** *no material effect* on the v0.8 refined residual core; weakly *supports* the motivation.

- **Elements of v0.8 touched:**
  - "BM25 vs dense in a morphologically rich language" (already a listed non-claim), in a weak form, because the dense side is not retrieval-trained;
  - use of a morphology-sensitive lexical representation: stemmed BM25, one variant only.
- **Elements not touched:**
  - raw → stem → lemma variation of the lexical channel;
  - a fixed modern dense comparator D;
  - fusion conditions H_raw / H_stem / H_lemma;
  - unique relevant hits, overlap, oracle union, incremental hybrid gain;
  - per-query statistics and query features (morphological, graphic, lexical-structural).
- **Weak support for the motivation:** a peer-reviewed benchmark paper asserts that inflection makes lexical matching less effective, yet does not measure it. This illustrates the gap between assumed and measured morphology effects that the Uzbek design addresses. It is not evidence *for* the hypothesis.
- **Gap-killer check** (CURRENT_GAP "What can still kill this gap"): none of conditions 1–4 is met. The work is not Uzbek or Turkic, has no raw/stem/lemma × fixed-D design, and has no per-query overlap analysis.

**Proposal:** keep v0.8 refined unchanged. Optionally list BEIR-PL in the evidence boundary as an example of "morphology invoked but not manipulated; cascade reranking, not fusion". This is a proposal only; `CURRENT_GAP.md` has not been edited.

## 17. Implications for our research design

- **Baseline selection / D.**
  - Do not use LaBSE or unsupervised-only encoders as D. Choose a retrieval-trained multilingual dense model and validate it on an Uzbek pilot/dev set before freezing it (consistent with PHD-INT-001 and HYB-007 notes).
  - Report dense Recall@k too; this paper reports recall only for BM25.
- **Morphology preprocessing.**
  - Name *and configure* the analyzer. Stemmer name, version, stop-words, lowercasing, apostrophe normalization, k1/b and indexed fields must all be reported.
  - Include a **raw** (no stemming) condition explicitly. A single stemmed BM25 cannot show a morphology effect.
- **Dataset / qrels.**
  - Machine-translated collections (BEIR / MS MARCO → Uzbek) are acceptable for training D, pilot runs or dev, with a translation-quality audit (Strict/Semantic sample, as in Table 2).
  - They are not acceptable as the main qrels, especially for morphology analysis: independent translation of queries and documents injects lexical divergence unrelated to Uzbek morphology.
  - Named entities need special attention. The authors report entity translation errors, and Uzbek named entities also inflect (e.g., case suffixes on proper names).
- **Fusion vs cascade.**
  - In Chapter I (§1.3), keep **cascade reranking** (BM25 top-k → neural reranker) distinct from **fusion** (combining scores or ranks of independent channels).
  - A cascade's recall ceiling is the lexical recall@k, so a morphology change in BM25 would change the reranker's candidate pool. That is a possible secondary analysis, not our core.
- **Query taxonomy.** The paper's dataset-level explanations are useful seeds for Uzbek query features, but must be tested per query:
  - duplicate-question/paraphrase queries favour dense;
  - keyword-heavy medical queries favour lexical;
  - long argumentative queries (ArguAna, 168 words on average) favour BM25.
- **Metrics / pipeline hygiene.**
  - Add automatic sanity checks to our evaluation code, e.g., for binary qrels, per-query nDCG@10 ≤ 3.40 × MRR@10 and nDCG@k ≤ 1.
  - Recompute the macro-averages over sub-collections, as done here for CQADupstack.
  - Report significance (paired tests or bootstrap CIs) and per-query distributions.
- **Hypothesis.** No evidence for or against. The paper shows that a morphology attribution without a controlled representation change remains a conjecture, which is exactly what our raw/stem/lemma × fixed D design is meant to measure.

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| BEIR / zero-shot IR | A collection of many different search test sets; models are tested on them without training on each one | Out-of-domain evaluation across heterogeneous test collections |
| Machine-translated benchmark | Test collection produced by automatically translating an existing one; relevance labels are copied | Qrels transfer under the assumption that relevance is preserved by translation |
| BM25 | Word-matching ranking: shared rare words and more repetitions give a higher score, with length normalization | Probabilistic relevance framework with parameters k1, b |
| Stemmer (Stempel) | Cuts words down to a common stem so that inflected forms match | Many-to-one mapping of word forms to stems before indexing |
| Bi-encoder (dense retriever) | Turns query and document into one vector each; nearby vectors are treated as relevant | `f(q,d)=cos(E(q),E(d))`, precomputed document index |
| Inverse Cloze Task (ICT) | Unsupervised training: a sentence acts as a pseudo-query for the passage it came from | Self-supervised contrastive pre-training for retrieval |
| LaBSE | Multilingual sentence-embedding model built for matching translations | Language-agnostic BERT sentence encoder; not trained for query–passage retrieval |
| Reranker / cross-encoder | Reads query and candidate document together and rescores the top results of a first-stage retriever | Second-stage scoring `g(q,d)` over the top-k of BM25 |
| MonoT5 | A text-to-text model that outputs "true"/"false" for relevance | Seq2seq relevance classification used as a reranking score |
| Late interaction (ColBERT) | Keeps one vector per token and matches each query token to its best document token | `Σ_i max_j sim(h_i^q, h_j^d)` |
| Cascade vs fusion | Cascade: the second model only reorders the first model's list. Fusion: both lists are combined | Pipeline composition vs score- or rank-level combination |
| nDCG@10 / MRR@10 / Recall@100 | Quality of the top 10 with discount / rank of the first correct document / share of relevant documents in the top 100 | App. A definitions (binary gain) |
| Complementarity (project term) | Each channel finds some relevant documents the other misses | Unique relevant hits, overlap, oracle-union gain |

## 19. Open questions / verification needed

1. **BM25 configuration:** k1, b, fields, stop-words, Stempel version: NOT_REPORTED. Is there any unstemmed run?
2. **English BM25 numbers (Table 3):** were they re-run by the authors (with which analyzer) or taken from the original BEIR paper? NOT_REPORTED.
3. **Figure 2:** attributed to Bonifacio et al. (2021), yet the paper states that MS MARCO was translated "into many different languages (Bonifacio et al., 2021), but not to Polish, yet" (Sec. 2, p. 2150). It repeats this in Sec. 3.1 (p. 2152), and Sec. 1 (p. 2149) makes a similar statement. Where does the Polish bar come from? The panel (b) axis reads "MRR@1K", the caption "MRR@10".
4. **MS MARCO BM25 MRR@10:** Fig. 2 shows Polish 0.12; Table 4 shows 68.09. Both are described as BM25 on (Polish) MS MARCO. The paper does not explain the difference (different query set, qrels or cut-off?). Not decidable from the paper.
5. **"Three BERT-only bi-encoder models"** (p. 2152) vs two reported (ICT, LaBSE).
6. **Reference error:** "BM25 is a better choice for most datasets as is presented in Figure 1" (p. 2154). Figure 1 is the reranking schematic; the evidence is in Table 4.
7. **ICT SciFact:** nDCG@10 38.17 vs MRR@10 6.12 is arithmetically infeasible under the paper's binary-gain definitions (max ratio 3.40 **[computed]**).
8. **Table 5:** identical HerBERT-base / HerBERT-large cells in gaming, gis and physics (both metrics). Possible copy error. Related: HerBERT-base's Table 5 nDCG@10 macro-average (26.825 **[computed]**) does not match Table 4's CQADupstack cell (26.85).
9. **Reranking depth** for T5, ColBERT and mMiniLM (stated as top-100 only for HerBERT). **ColBERT training data** not stated.
10. **Author order:** PDF byline (Shishkin 2nd) vs ACL Anthology / PDF metadata (Wołowiec 2nd). Use the Anthology order for citation.
11. **Translation audit sample:** 100 items per column or 100 in total?
12. For the Polish cluster, read **CR000100** and **CR000914** in full. Per triage, they contain the within-language word-form vs lemma BM25 contrasts that BEIR-PL lacks. Check them for any overlap or fusion analysis before making claims about Polish.

## 20. Decision after deep dive

- **Keep current gap?** Yes. v0.8 refined is unaffected (§16).
- **Modify gap?** No change proposed. Optionally, the researcher may add BEIR-PL to the evidence-boundary list as an example of "morphology invoked but not manipulated; cascade reranking ≠ fusion".
- **Add decision?** Proposed for `decisions/DECISIONS.md` (researcher's decision):
  - "Machine-translated collections may be used only for training/dev/pilot, not as main qrels; if used, report a Strict/Semantic translation audit";
  - "D must be a retrieval-trained dense model validated on Uzbek dev data; sentence-similarity encoders such as LaBSE are not acceptable as the primary D";
  - "Evaluation code includes automatic metric-consistency checks".
- **Add experiment?** No new experiment. Optionally, when building the pipeline, run a small replication: BM25 raw vs Stempel on one public BEIR-PL dataset. It would test our raw/stem harness on a public morphologically rich benchmark, with the translation caveat.
- **Add citation to Chapter I?** Yes, briefly:
  - §1.1 (morphology-sensitive BM25 in inflected languages: an example of an assumed but untested effect);
  - §1.3 (cascade reranking vs fusion; BEIR-PL as a low-resource benchmark).
  - Do not cite it as evidence that inflection lowers BM25 effectiveness.
- **Reading priority adjustment (proposal):** for the Polish cluster, raise CR000100 and CR000914 above CR000103 for gap-boundary purposes.
- **Proposed `MASTER_INDEX.md` row** (to add after approval, section C):

| MORPH-008 | Wojtasik, Wołowiec, Shishkin, Janz, Piasecki — *BEIR-PL: Zero Shot Information Retrieval Benchmark for the Polish Language* (LREC-COLING 2024) — [deep dive](deep-dives/2024_Wojtasik_BEIR_PL_Polish_Zero_Shot_IR_Benchmark.md) | 2024 | A | MEDIUM | Machine-translated BEIR for Polish (13 datasets). Single stemmed BM25 (Elasticsearch + Stempel) vs weak bi-encoders (unsupervised ICT-HerBERT, LaBSE) and six rerankers over BM25 top-100. BM25 PL < EN on all 11 compared datasets (mean nDCG@10 35.67 vs 42.41 [computed]), attributed to inflection **without ablation** (confounded with MT, analyzer, qrels transfer). BM25 > both bi-encoders on 12/13 datasets. No raw/lemma BM25, no fusion (cascade only), no overlap/unique-hit/per-query analysis, no significance tests; several internal reporting inconsistencies. |
