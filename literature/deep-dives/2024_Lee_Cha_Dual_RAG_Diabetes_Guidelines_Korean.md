# Lee, Cha, Hwangbo & Cheon (2024): Enhancing Large Language Model Reliability: Minimizing Hallucinations with Dual Retrieval-Augmented Generation Based on the Latest Diabetes Guidelines

**Targeted deep-dive status:** COMPLETED (AI-assisted, pending researcher review)
**Completed:** 2026-09-28
**Literature ID:** `MORPH-012` (assigned 2026-09-28, approved by researcher)
**Systematic-review record:** `CR000448`. Full-text triage: INCLUDE, reading priority HIGH, reading tier "1 — прямо по теме пробела", `carries_complementarity_evidence = NO`
**Provenance:** AI-assisted deep dive (Claude). The paper (14 pages) was read in full from the pdftotext extraction. Page images were checked for Tables 1–6 and Figures 1–2 (pp. 3, 4, 5, 6, 7, 8, 9, 10, 11); Figure 2 (p. 9) was additionally inspected at 300 dpi (f1, recall, MAP and NDCG panels). Every number below comes with its table/figure/section and printed page. Numbers computed by us are marked **[computed]** (recomputed with Python).
**Source rule:** **the paper is the primary and only authoritative source.** No code repository, website or later paper was used for claims about what the authors did. The web was used only to verify the bibliographic record, marked "(bibliographic check: …)". Background knowledge appears only as labelled "Context (not from the paper)".
**Verification:** independent AI verifier pass 2026-09-28; 10 findings addressed.
**Reliability:** **B.** Peer-reviewed journal article (MDPI, *Journal of Personalized Medicine*), but a medical-domain venue, a very small evaluation set (≈49/48 queries, inferred), no statistics, several internal inconsistencies, and the ensemble/hallucination claims are not backed by any reported numbers. For those claims the evidential value is closer to C.

---

## Кратко для исследователя (RU)

- **Что сделано.** Система RAG по двум клиническим рекомендациям 2023 г. по диабету: корейской (KDA, текст на корейском) и американской (ADA, текст на английском). Отдельно оценён этап поиска:
  - 11 моделей плотного поиска (OpenAI, Upstage Solar, корейские, многоязычные), Tables 3–4;
  - BM25 с двумя токенизаторами: `ko_kiwi` (морфологический анализ корейского) и `porter_stemmer`, оба применены к обоим корпусам, Tables 5–6;
  - k = 1, 3, 5, 10, 50; метрики F1, Recall, Precision, MAP, MRR, NDCG.
- **Данные крошечные.** Фрагменты по 1000 символов (перекрытие 200), вопросы сгенерированы ChatGPT-4o по корпусу («generated from the extracted corpus data», Table 2) и одобрены экспертами; ровно один релевантный фрагмент на вопрос (вывод из P = R/k и MAP = MRR). Что каждый вопрос порождён именно из своего `retrieval_gt`-фрагмента, прямо не сказано (наш вывод). В 2 из 3 примеров статьи (Tables 1–2) эталонный фрагмент не очевидно отвечает на вопрос. Число вопросов в статье **не указано**; по значениям Recall это 49 (KDA) и 48 (ADA) **[computed, inferred]**.
- **Морфологический вариант лексического канала есть, но только для корейского и в минимальной форме:** Kiwi vs Porter.
  - KDA: Recall@1 0.306 vs 0.245 (15 vs 12 из 49 запросов), Recall@50 0.98 vs 0.898 (48 vs 44), MRR@50 0.425 vs 0.386 (Table 5, p. 10).
  - Но при k = 5 и 10 Porter выше по Recall/Precision/F1 (напр. R@10 0.694 vs 0.633), что противоречит тексту авторов «Kiwi лучше по всем метрикам».
  - ADA (английский): оба варианта близки (Table 6).
  - Нет условия «raw»; что Porter делает с хангылем, не описано; k1/b, стоп-слова не указаны; значимость не проверялась.
- **Плотный поиск vs BM25.** На KDA при k = 1 лучший плотный (Upstage 0.429) выше BM25-Kiwi (0.306), но многие плотные модели ниже. На ADA BM25 близок к лучшим плотным при k = 1 (0.542 vs 0.583/0.563) и k ≥ 10 (R@10 0.979 у Porter vs 0.979/1.000), но заметно ниже при k = 3–5 (R@3 0.729 vs 0.917; R@5 0.854 vs 0.958).
- **Гибрид = простое объединение результатов (union), без каких-либо чисел.** KDA: Upstage top-3 ∪ BM25-Kiwi top-50; ADA: text-embedding-3-large top-1 ∪ BM25-Porter top-10 (Sec. 3.3, p. 11). Таблицы для ансамбля нет; утверждения об «улучшении recall и качества ранжирования при сохранении precision» и о «снижении галлюцинаций» ничем не подкреплены (генерация не оценивалась).
- **Наш расчёт:** поскольку BM25 в ансамбле уже находит 48/49 (KDA) и 47/48 (ADA), плотный канал может добавить **не более одного запроса** с уникальным попаданием в каждом корпусе **[computed]**. Перекрытие/уникальные попадания/oracle union авторы не считали.
- **Внутренние несоответствия:**
  1. text-embedding-3-large, ADA, k = 1: Table 4 = 0.583, а текст (Sec. 3.3) = 0.563; средние в Sec. 3.1 и Fig. 2 согласуются с 0.563, а Fig. 2 показывает 0.583 у gte-multilingual-base (похоже на перестановку строк).
  2. В плотных таблицах MAP/MRR/NDCG **убывают** с ростом k (напр. Upstage KDA MRR 0.429 → 0.021), что невозможно при стандартных определениях; в таблицах BM25 они растут. Сравнивать MAP/MRR/NDCG между плотными и BM25-таблицами при k > 1 нельзя.
  3. «Upstage лучше по всем метрикам при k = 3» (Sec. 3.3), но MAP/MRR у e5 выше (0.384 vs 0.367, Table 3).
  4. «Kiwi лучше Porter по всем метрикам» на KDA (Sec. 3.2), но при k = 5 и 10 Porter выше по Recall/Precision/F1 (Table 5).
  (Та же нумерация 1–4 используется в §8–§9.)
- **Для gap v0.8:** работа **не затрагивает ядро** (raw/stem/lemma × фиксированный D → перекрытие/уникальные попадания → прирост гибрида → признаки запроса). Это ещё один пример «морфологический токенизатор BM25 + плотный поиск + ансамбль» **без** анализа взаимодополняемости. Предложение: gap не менять.
- **Практическая польза:**
  1. Предупреждение о протоколе: метрики из AutoML/RAG-фреймворков нужно проверять на монотонность по k и фиксировать определения.
  2. Корейский (агглютинативный) пример: морфологический токенизатор улучшает верх выдачи и глубокое покрытие, но не монотонно по k — у нас эффект тоже надо мерить по глубинам.
  3. При одном релевантном документе и ~50 запросах анализ уникальных попаданий вырождается — нужны больше запросов и пулинг.

---

## 1. Bibliographic record

- **Authors:** Jaedong Lee, Hyosoung Cha, Yul Hwangbo, Wonjoong Cheon (corresponding author: W. Cheon)
- **Affiliations (as printed, p. 1):** Healthcare AI Team, National Cancer Center, Goyang-si, Korea (Lee, Cha, Hwangbo); Department of Cancer AI & Digital Health, Graduate School of Cancer Science and Policy, National Cancer Center (Lee, Hwangbo); Department of Radiation Oncology, Seoul St. Mary's Hospital, The Catholic University of Korea (Cheon)
- **Year:** 2024
- **Venue:** *Journal of Personalized Medicine* 2024, 14(12), article 1131; MDPI, Basel; section "Epidemiology" (bibliographic check: mdpi.com article page)
- **ISSN:** 2075-4426 (bibliographic check: mdpi.com)
- **Dates (p. 1):** received 27 Sep 2024; revised 28 Nov 2024; accepted 28 Nov 2024; published 30 Nov 2024
- **DOI:** `10.3390/jpm14121131`
- **Official record:** https://www.mdpi.com/2075-4426/14/12/1131
- **Funding (p. 13):** Korea Health Technology R&D Project, KHIDI, grant RS-2022-KH125204
- **Data availability (p. 13):** KDA guideline is public; "Additional data presented in this study are available upon reasonable request to the corresponding author." The QA set is not released.
- **Source type:** peer-reviewed journal article (open access, CC BY)
- **Reliability:** B (see header)
- **Full text available:** yes (`07_full_text/pdfs/CR000448.pdf`, 14 pages)

## 2. Why this work matters to the PhD

It is one of the few works in the corpus that, in one setting, puts together:

- an **agglutinative language** (Korean) with a **morphological tokenizer for BM25** (Kiwi) versus a stemmer-based tokenizer (Porter);
- **many dense retrievers** (11, including Korean-specific, multilingual and commercial models);
- an **ensemble** of dense and sparse results.

It is therefore a candidate "gap killer" by its component list. On reading, its evidence is thin for our question.

| Axis | Relation |
|---|---|
| Lexical retrieval | BM25 with two tokenizers (Kiwi, Porter) on both corpora; k1/b, stop-words, normalization NOT_REPORTED |
| Semantic retrieval | 11 embedding models used as dense retrievers, zero-shot (no fine-tuning described) |
| Hybrid retrieval | Union of top-k results from one dense and one BM25 configuration per guideline; **no quantitative evaluation** |
| Uzbek morphology | Indirect: Korean is agglutinative, but Hangul script and Kiwi morpheme analysis differ from Uzbek suffixation/Latin script |
| Low-resource retrieval | Not low-resource in the usual sense (Korean has strong tools and models); small domain corpus |
| Current gap | Touches "morphology-aware BM25 + dense + hybrid coexist" (already a non-claim in v0.8). No overlap / unique hits / oracle union / per-query analysis (§16) |

## 3. Research problem

### Simple explanation

Chatbots based on large language models sometimes invent facts ("hallucinate"). In medicine that is dangerous, and guidelines change every year. Instead of retraining the model, one can let it look up the current guideline text first (retrieval-augmented generation, RAG). The authors want to find which search component finds the right guideline passage best, for a Korean and an English guideline, and then combine a semantic and a keyword search.

### Formal formulation

- Task: first-stage **passage (chunk) retrieval** for a RAG pipeline. Given a question `q` and a chunk collection `C` from one guideline, return top-k chunks; relevance = the single `retrieval_gt` chunk ("ground truth document ID for retrieval", Sec. 2.2, p. 4). The paper says QA pairs were "generated from the extracted corpus data" (Table 2 caption); that each question was generated from exactly its `retrieval_gt` chunk is our inference, not stated.
- Comparisons: 11 dense retrievers × 5 depths (Tables 3–4); BM25 × 2 tokenizers × 5 depths (Tables 5–6); then a per-guideline ensemble (Sec. 3.3).
- Stated aim (Abstract, p. 1): "to develop and evaluate a novel retrieval system to enhance LLM reliability in diabetes management across different languages and guidelines."
- No explicit research questions or hypotheses are stated.

## 4. Main idea

### Simple explanation

Cut each guideline into pieces of 1000 characters. Have ChatGPT-4o write a question for pieces, and have doctors approve the questions. Then check, for each search method, whether the piece the question came from appears among the first k results. Pick the best dense model and the best BM25 variant for each guideline and join their result lists.

### Concrete example

- Question (Table 2, p. 4, English rendering): "What tests should women diagnosed with gestational diabetes undergo after childbirth?"
- Its only relevant chunk: `DOC_UID#9` (Table 1, p. 3), a KDA chunk about the Diabetes Prevention Study and glucose criteria.
- Caveat (inferred): the printed (truncated) chunk does not obviously address postpartum testing after gestational diabetes; see §6 on the quality of the printed QA examples.
- BM25-Kiwi splits the Korean question into morphemes (per the paper, Kiwi "specializes in Korean morphological analysis and word segmentation", Sec. 2.3, p. 4) and matches them with the chunk's morphemes; a dense model compares whole-text vectors.
- The ensemble returns the union of, e.g., Upstage's top 3 and BM25-Kiwi's top 50 chunks (Sec. 3.3, p. 11).

### Formal method

- Dense: `score(q,c) = sim(E(q), E(c))` with a pre-trained embedding model `E` (similarity function NOT_REPORTED).
- Sparse: BM25 over tokens produced by `ko_kiwi` or `porter_stemmer` (BM25 parameters NOT_REPORTED).
- Ensemble (Sec. 3.3, p. 11): "The ensemble method combines retrieved documents from both approaches, merging their unique contributions to create a more comprehensive result set." We read this as a set union `R_ens(q) = top-k_D(q) ∪ top-k_BM25(q)`. The ordering of the merged list, deduplication and any score fusion are NOT_REPORTED.

## 5. Architecture / algorithm

1. **Tooling.** AutoRAG (Markr.AI), "an AutoML tool designed for automatically finding and optimizing RAG pipelines" (Sec. 2.1, p. 2), used for preprocessing and, per p. 3, for "subsequent stages in the AutoRAG pipeline, including the evaluation of generating question-answer (QA) pairs and the evaluation of various retriever models". Metric implementations are therefore AutoRAG's; the paper gives no metric formulas.
2. **Chunking** (Sec. 2.1, p. 3): chunk size 1000 characters, overlap 200 characters; independent pipelines per guideline. Corpus fields: index, doc_id, contents, metadata (Table 1). Number of chunks per guideline: NOT_REPORTED (Table 1 shows an index as high as 306 for KDA).
3. **QA generation** (Sec. 2.2, pp. 3–4): ChatGPT-4o ("ChatGPT-4.o"), few-shot; "Only pairs that received unanimous approval from the expert panel were included in the final dataset." Panel size, number of generated vs approved pairs, and how chunks were sampled: NOT_REPORTED.
4. **Dense retrievers** (Sec. 2.3, p. 4), 11 models:
   - OpenAI: text-embedding-ada-002 (rows "openai"; labelled "OpenAI text-embedding-ada-002" in Figs. 1–2), text-embedding-3-small, text-embedding-3-large;
   - Upstage: Solar Embedding-1-large ("upstage_embed");
   - "Korean-specific": ko-sroberta-multitask, KoSimCSE-roberta;
   - "multilingual": paraphrase-multilingual-mpnet-base-v2, paraphrase-multilingual-MiniLM-L12-v2, multilingual-e5-large-instruct;
   - "task-specific": kf-deberta-multitask, gte-multilingual-base.
   - Note: gte-multilingual-base is called "task-specific" in Sec. 2.3 but "multilingual" in Sec. 3.1 (p. 5). All models are used as downloaded/API; no fine-tuning is described.
5. **Sparse retriever** (Sec. 2.3, p. 4): BM25 "with two distinct tokenizers: ko_kiwi tokenizer specifically designed for Korean text processing, and porter_stemmer tokenizer commonly used for text stemming. We applied both tokenizers to both KDA and ADA guidelines". Lower-casing, stop-words, pre-tokenization for Porter, k1/b: NOT_REPORTED.
   - Context (not from the paper): the Porter stemmer's rules target English suffixes, so on Hangul tokens it is expected to leave tokens essentially unchanged; if the Porter pipeline splits Korean on whitespace, the KDA "porter_stemmer" run would be close to a surface-form (word-unit) BM25. The paper does not describe this, so this is only a plausible reading.
6. **Evaluation depths:** k ∈ {1, 3, 5, 10, 50} (Sec. 2.3, p. 4).
7. **Ensemble configurations** (Sec. 3.3, p. 11):
   - KDA: Solar Embedding-1-large top-3 + BM25-ko_kiwi top-50;
   - ADA: text-embedding-3-large top-1 + BM25-porter_stemmer top-10.
   - Inferred: the paper describes only one QA dataset and no split, so the selection was apparently made on the same query set used for evaluation.

## 6. Data

- **Dataset/corpus:** KDA 2023 Clinical Practice Guidelines (Korean) and ADA Standards of Care in Diabetes—2023 (English) (Sec. 2.1, p. 2).
- **Languages:** Korean (KDA), English (ADA). The language of the KDA questions is not stated explicitly; the Table 1 note says "Korean translated into English", and Table 2 examples refer to KDA chunks.
- **Domain:** clinical practice guidelines (diabetes).
- **Size:** number of chunks NOT_REPORTED; number of questions NOT_REPORTED.
  - Inference **[computed]**: every Recall value (all k) in Tables 3 and 5 (KDA) is a multiple of 1/49 (e.g. Table 3: 0.429 = 21/49; Table 5: 0.306 = 15/49, R@50 0.98 = 48/49), and every Recall value in Tables 4 and 6 (ADA) is a multiple of 1/48 (e.g. Table 4: 0.583 = 28/48; Table 6: 0.542 = 26/48, 0.979 = 47/48). 49/48 is the smallest fitting denominator (98/96 would also fit). So **49 KDA questions and 48 ADA questions**, very likely.
- **Relevance judgments:** one ground-truth chunk per question (`retrieval_gt`, Table 2). Evidence that it is exactly one: Precision@k = Recall@k / k in every row and MAP = MRR everywhere **[computed check]**. Chunks overlapping the gold chunk (200-character overlap) or other chunks containing the same information count as non-relevant.
- **How labels were produced:** automatically: LLM-generated QA pairs "from the extracted corpus data" with a `retrieval_gt` chunk ID (Sec. 2.2, Table 2); that the gold chunk is the generation source is our inference. Expert approval of the QA pair; no pooled relevance assessment.
- **Train/dev/test:** no training; one evaluation set, also used to choose the ensemble configuration.
- A quality observation (inferred, from the paper's own example): for UID#2 ("Why should the HbA1c target be maintained below 6.5%?", Table 2) the gold chunk DOC_UID#25 states that the VERIFY study "does not provide evidence on whether glycemic control lower than HbA1c 6.5% is necessary" (Table 1). The chunk and the generated QA pair do not obviously match. The same holds for UID#1 (gestational-diabetes postpartum testing → DOC_UID#9, a chunk on the Diabetes Prevention Study and fasting/2-h glucose criteria; printed truncated). So 2 of the 3 printed QA examples do not obviously match their gold chunk; only UID#3 (urine volume → DOC_UID#306) clearly does. Three examples cannot establish a rate, and the chunks are truncated in print.

## 7. Baselines

| Baseline | What it is | Why selected | Fair comparison? |
|---|---|---|---|
| 11 dense retrievers | Pre-trained embedding models, used without any described fine-tuning | Span language-specific, multilingual, commercial | **Partly.** Same queries and chunks; but model sizes, max input length (1000-character chunks may exceed some models' limits — not discussed) and API vs local differ; no fine-tuning |
| BM25 + ko_kiwi | BM25 over Kiwi morpheme tokens | Korean morphological analysis | Yes vs Porter (same BM25), but BM25 parameters NOT_REPORTED |
| BM25 + porter_stemmer | BM25 over Porter-stemmed tokens | English stemming | On Korean text this is not a defined "raw" control; what it does to Hangul is not described |
| Ensemble | Union of one dense + one BM25 run | Authors' proposed system | **Not evaluated.** No numbers, no comparison with either component at matched list size |

There is no raw/whitespace BM25 condition, no score-level fusion (RRF, convex combination), and no reranker.

## 8. Metrics

With exactly one relevant chunk per question at rank *r*:

| Metric | Definition (standard) | Simple meaning here | Appropriate? |
|---|---|---|---|
| Recall@k | 1 if r ≤ k, else 0, averaged | "Share of questions whose gold chunk is in the top k" (= Hit@k) | Yes; the main usable metric here |
| Precision@k | (1 if r ≤ k)/k | Recall@k divided by k | Adds nothing with one gold chunk |
| F1@k | 2PR/(P+R) | Mechanically falls with k | Not meaningful for comparing depths |
| MAP@k, MRR@k | 1/r if r ≤ k, else 0 | "How high is the gold chunk?" | Yes, but see below |
| NDCG@k | 1/log₂(r+1) if r ≤ k | Softer version of MRR | Yes, but see below |

- **Internal inconsistency 2. Under the standard definitions MRR@k, MAP@k and NDCG@k cannot decrease as k grows.** Tables 5–6 (BM25) behave this way. Tables 3–4 (dense) do **not**: e.g. Upstage KDA MRR 0.429 (k=1) → 0.367 → 0.229 → 0.130 → 0.021 (k=50) (Table 3, pp. 5–6). Every dense row has MRR@50 below MRR@1. The dense ranking metrics are therefore computed in some undocumented way and are **not comparable** with the BM25 ranking metrics at k > 1. Recall and Precision are internally consistent in both table families (P = R/k **[computed check]**).
- The authors' own statement (Sec. 3.2, p. 10) — "as the top-k value increased, recall, MAP, MRR, and NDCG generally improved, while precision decreased" — holds for Tables 5–6 but not for Tables 3–4.
- Execution time is reported (s), but whether per query or per run is NOT_REPORTED.

## 9. Results

### Table 3 (KDA, Korean) and Table 4 (ADA, English): dense retrievers — Recall@k (pp. 5–7, image-checked)

| Model | KDA R@1 | KDA R@3 | KDA R@10 | KDA R@50 | ADA R@1 | ADA R@3 | ADA R@10 | ADA R@50 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| upstage_embed (Solar Embedding-1-large) | **0.429** | **0.755** | **0.918** | 1.000 | 0.563 | 0.854 | 1.000 | 1.000 |
| gte-multilingual-base | 0.388 | 0.673 | 0.857 | 1.000 | 0.563* | 0.833 | 0.958 | 1.000 |
| openai_embed_3_small | 0.347 | 0.592 | 0.837 | 1.000 | 0.521 | 0.813 | 0.958 | 1.000 |
| openai_embed_3_large | 0.265 | 0.551 | 0.837 | 1.000 | **0.583*** | **0.917** | 0.979 | 1.000 |
| multilingual-e5-large-instruct | 0.265 | 0.653 | 0.878 | 0.959 | 0.521 | 0.813 | 0.917 | 1.000 |
| openai (ada-002) | 0.224 | 0.551 | 0.735 | 0.959 | 0.563 | 0.771 | 0.917 | 1.000 |
| paraphrase-multilingual-mpnet-base-v2 | 0.265 | 0.367 | 0.490 | 0.776 | 0.313 | 0.500 | 0.708 | 0.958 |
| ko-sroberta-multitask | 0.224 | 0.408 | 0.510 | 0.837 | 0.229 | 0.333 | 0.479 | 0.854 |
| kf-deberta-multitask | 0.224 | 0.408 | 0.612 | 0.878 | 0.292 | 0.354 | 0.542 | 0.813 |
| paraphrase-multilingual-MiniLM-L12-v2 | 0.204 | 0.286 | 0.469 | 0.694 | 0.375 | 0.396 | 0.604 | 0.958 |
| KoSimCSE-roberta | 0.143 | 0.286 | 0.551 | 0.898 | 0.188 | 0.375 | 0.583 | 0.958 |

\* See the inconsistency below: Table 4 prints 0.583 for openai_embed_3_large and 0.563 for gte-multilingual-base; the text and Fig. 2 point to the reverse.

Authors' averages over the five k values (Sec. 3.1, p. 7):
- KDA, Upstage: F1 0.258, Recall 0.788, Precision 0.192, MAP = MRR 0.235, NDCG 0.349. **[computed from Table 3: 0.2584 / 0.7878 / 0.192 / 0.2352 / 0.3494 ✓]**
- ADA, text-embedding-3-large: F1 0.312, Recall 0.883, Precision 0.236, MAP = MRR 0.273, NDCG 0.400. **[computed from Table 4: 0.3154 / 0.8874 / 0.2398 / 0.2774 / 0.4046 ✗; with k=1 = 0.563 instead of 0.583: 0.3114 / 0.8834 / 0.2358 / 0.2734 / 0.4006 ✓ within ±0.001: Recall, Precision, MAP/MRR match exactly; F1 and NDCG differ by 0.001, plausibly rounding]**

**Internal inconsistency 1 (ADA, text-embedding-3-large, k = 1):**
- Table 4 (p. 6, image-checked): 0.583 in all six metric columns; gte-multilingual-base 0.563.
- Sec. 3.3 (p. 11): "OpenAI's text-embedding-3-large achieved optimal performance at top-k = 1, with consistent scores of 0.563 across all metrics".
- Sec. 3.1 averages (p. 7) reproduce only with 0.563 **[computed]**.
- Fig. 2 (p. 9, 300 dpi): in the f1, MAP and NDCG panels the upper whisker (maximum, i.e. the k = 1 value) of text-embedding-3-large is at ≈0.563, while gte-multilingual-base reaches ≈0.583. In the recall panel the k = 1 value is the minimum: text-embedding-3-large shows a low outlier at ≈0.56, and gte-multilingual-base's lower whisker is at ≈0.58.
- Most consistent reading: the k = 1 values of the two rows are swapped in Table 4. Not decidable from the paper. If so, at k = 1 on ADA the best model is gte-multilingual-base (0.583), and text-embedding-3-large (0.563) only ties with ada-002 and Upstage; the paper's choice of text-embedding-3-large top-1 for the ADA ensemble would then not follow from its own k = 1 numbers.

**Internal inconsistency 3 ("superior across all metrics"):** Sec. 3.3 (p. 11): Upstage "demonstrated superior performance across all metrics at top-k = 3" on KDA. Table 3 at k = 3: Upstage MAP = MRR 0.367 vs multilingual-e5-large-instruct 0.384. Upstage is highest at k = 3 on F1, Recall, Precision and NDCG only.

**"Multilingual > language-specific" (Abstract; Sec. 3.1, p. 7; Discussion, p. 11).** Holds for the strong multilingual models (gte, e5) and the commercial models; not for all multilingual models: on KDA, paraphrase-multilingual-MiniLM-L12-v2 (R@1 0.204, R@10 0.469) is below ko-sroberta-multitask (0.224, 0.510) (Table 3). Model families also differ in size and training data, so this is not a controlled language-specific vs multilingual comparison.

### Table 5 (KDA) and Table 6 (ADA): BM25 with two tokenizers (p. 10, image-checked)

| Corpus | Tokenizer | R@1 | R@3 | R@5 | R@10 | R@50 | MRR@10 | MRR@50 | NDCG@50 | Time |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| KDA | ko_kiwi | **0.306** | **0.449** | 0.531 | 0.633 | **0.98** | **0.405** | **0.425** | **0.542** | 1.06–1.10 |
| KDA | porter_stemmer | 0.245 | 0.429 | **0.551** | **0.694** | 0.898 | 0.375 | 0.386 | 0.497 | 0.001–0.006 |
| ADA | ko_kiwi | **0.542** | 0.708 | 0.792 | 0.896 | 0.979 | **0.657** | **0.663** | 0.736 | 1.087–1.094 |
| ADA | porter_stemmer | 0.500 | **0.729** | **0.854** | **0.979** | **1.000** | 0.656 | 0.657 | **0.738** | 0.001–0.005 |

Reading the table **[computed]**:
- KDA k = 1: Kiwi 15/49 vs Porter 12/49 questions (+0.061 absolute, +24.9% relative). The difference is **3 questions**; no significance test.
- KDA k = 50: 48/49 vs 44/49 (+0.082); MRR@50 +0.039; NDCG@50 +0.045.
- KDA k = 5 and k = 10: **Porter is higher** on Recall (0.551 vs 0.531; 0.694 vs 0.633), Precision (0.110 vs 0.106; 0.069 vs 0.063) and F1 (0.184 vs 0.177; 0.126 vs 0.115). Kiwi is higher on MAP/MRR/NDCG at every k.
- **Internal inconsistency 4:** the text (Sec. 3.2, p. 10) says: "For KDA guidelines, the ko_kiwi tokenizer demonstrated superior performance compared to the porter_stemmer across all metrics." Table 5 contradicts this at k = 5 and k = 10 for Recall, Precision and F1.
- ADA: Kiwi better at k = 1 (26/48 vs 24/48); Porter better in Recall at k = 3–50 (e.g. R@10 47/48 vs 43/48). The authors call them "comparable" (Sec. 3.2).
- Kiwi's tokenization cost: ≈1.1 s vs ≈0.001–0.006 s (Sec. 3.2, p. 11; unit s stated there).

### BM25 vs dense (cross-reading Tables 3–6; Recall only, since dense ranking metrics are not comparable)

- KDA R@1: BM25-Kiwi 0.306 is below Upstage (0.429), gte (0.388) and 3-small (0.347), and above the other eight dense models.
- KDA R@10: BM25-Kiwi 0.633 / Porter 0.694 vs Upstage 0.918 — dense much better at mid-depth.
- KDA R@50: BM25-Kiwi 0.98 vs four dense models at 1.000.
- ADA R@1: BM25-Kiwi 0.542 vs best dense 0.583 (or 0.563, see above). ADA R@10: BM25-Porter 0.979 = text-embedding-3-large 0.979; Upstage 1.000.

### Sec. 3.3: ensemble retriever (p. 11) — **no numbers reported**

- Configurations: KDA = Upstage top-3 ∪ BM25-Kiwi top-50; ADA = text-embedding-3-large top-1 ∪ BM25-Porter top-10.
- Claim: "The ensemble approach demonstrates significant potential for improved overall performance, particularly in recall and ranking quality, while maintaining precision." No table, figure or value supports it; "significant" is not statistical.
- What can be bounded from the component numbers **[computed]**:
  - Union Recall ≥ max of the components: KDA ≥ 0.98 (BM25-Kiwi@50), ADA ≥ 0.979 (BM25-Porter@10).
  - Therefore the dense component can add a unique hit for **at most 1 of 49** (KDA) and **at most 1 of 48** (ADA) questions. The ensemble's recall is essentially BM25's.
  - Precision: the union returns between 50 and 53 chunks (KDA) or 10–11 (ADA) for one gold chunk, so Precision ≤ 1/50 = 0.020 (KDA) and ≤ 0.10 (ADA) — the same order as BM25 alone at k = 50 / 10 and far below the dense top-3 / top-1 precision (0.252 / 0.583). "Maintaining precision" is true only relative to the BM25 component.
  - How the union is ordered (hence MRR/NDCG of the ensemble) is NOT_REPORTED.

## 10. Statistical evidence

- **Significance tests:** NOT_REPORTED (none).
- **Confidence intervals:** NOT_REPORTED.
- **Runs / seeds:** NOT_REPORTED (deterministic retrieval presumably; LLM question generation is a single draw).
- **Ablation:** only the tokenizer swap for BM25 and the k sweep. No ablation of the ensemble (no ensemble numbers at all).
- **Per-query analysis:** none. No overlap, unique relevant hits, oracle union, win/loss or query-feature breakdown between dense and BM25, or between Kiwi and Porter.
- **Sample size:** ≈49/48 questions (inferred). One question = 0.020/0.021 in Recall, so differences of 1–3 questions dominate most comparisons.

## 11. Strengths

- A single setting with an agglutinative language, a morphological BM25 tokenizer, a stemming tokenizer and 11 dense models, evaluated on the same questions at five depths.
- Two languages/guidelines processed with the same pipeline; both tokenizers applied to both corpora.
- Expert approval of generated QA pairs (unanimity rule).
- Recall reported at k = 50, relevant for candidate generation in a hybrid.
- Execution time reported, showing the cost of morphological tokenization (≈1.1 s vs ≈0.001 s).

## 12. Limitations

### Stated by the authors

- RAG adds inference-time computational and memory cost, "particularly evident in the processing time differences between tokenizers in our sparse retrieval implementation" (Discussion, p. 12).
- GPU memory trade-off between retrieved context length and user input length (p. 12).
- OCR processing of medical documents and conversion of tables/figures to text is challenging (p. 12).
- Future work should explore "advanced ensemble techniques for enhanced retrieval performance" (p. 12).

### Inferred from the experimental design

1. **Tiny, single-positive, synthetic evaluation set.** ≈49/48 questions, apparently generated from the gold chunk (our inference; if so, question wording is drawn from that chunk, which may favour lexical matching — direction not measured). Overlapping neighbour chunks are counted as non-relevant.
2. **No statistics.** All differences (e.g. Kiwi vs Porter, 3 questions at k = 1) are untested.
3. **Selection on the test set.** Best models, k values and tokenizers for the ensemble were chosen on the same questions; no dev split.
4. **Ensemble not evaluated.** Claims about ensemble recall, ranking quality and precision are unsupported; our bound shows the dense channel can add at most one question per corpus.
5. **Hallucination reduction not measured.** No generation, answer-accuracy or hallucination metric is reported, although the title, Discussion and Conclusions (p. 12: "this ensemble approach effectively reduces hallucinations") claim it.
6. **Non-standard dense ranking metrics** (decreasing with k), making cross-table MAP/MRR/NDCG comparisons invalid.
7. **Lexical conditions under-specified.** No raw control; Porter on Hangul is undefined in the paper; BM25 parameters, stop-words and normalization NOT_REPORTED. So "Kiwi vs Porter" is not a clean morphological-representation contrast.
8. **Internal inconsistencies** (Table 4 vs text/Fig. 2; "superior across all metrics" twice contradicted by the tables).
9. **Terminology ambiguity:** "dual RAG" means both "integrating both Korean Diabetes Association and American Diabetes Association 2023 guidelines" (Abstract, p. 1) and "directly combining dense (semantic) and sparse (keyword-based) retrieval" (Discussion, p. 11).
10. The Discussion lists "implementation of robust safeguards to minimize hallucinations" as a contribution (p. 11); no such safeguards are described in Methods.

## 13. What the work proves

Within this very small, single-positive setting (without significance tests):

- On the Korean guideline, **BM25 with Kiwi morpheme tokenization places the gold chunk higher than BM25 with the Porter tokenizer** (MRR/MAP/NDCG higher at all k; R@1 0.306 vs 0.245; R@50 0.98 vs 0.898; Table 5), but **not uniformly**: Porter has higher Recall at k = 5 and 10.
- On the English guideline, the two BM25 tokenizers perform similarly (Table 6).
- Strong dense models, used without any described fine-tuning (Solar Embedding-1-large, gte-multilingual-base, OpenAI 3-small/3-large), retrieve the gold chunk at mid-depths (k = 3–10) more often than BM25 on the Korean guideline (e.g. R@10 0.918 vs 0.633/0.694). On the English guideline BM25 is close to the best dense models at k = 1 (0.542 vs 0.583/0.563) and k ≥ 10 (R@10 0.979 vs 0.979/1.000), but clearly below them at k = 3–5 (R@3 0.729 vs 0.917, ≈9 of 48 questions; R@5 0.854 vs 0.958) (Tables 4, 6).
- Several Korean-specific and older multilingual sentence-embedding models are weaker than the strong multilingual/commercial models on both guidelines (Tables 3–4).
- BM25 with Kiwi is about two to three orders of magnitude slower than with Porter in this implementation (execution time 1.062–1.097 s vs 0.001–0.006 s, ratio ≈180–1100 [computed]; Tables 5–6). The column is total execution time, which the authors attribute to the tokenizer (Sec. 3.2, p. 11).

## 14. What the work does NOT prove

- **That the dense+BM25 ensemble improves retrieval** in recall, ranking quality or precision: no ensemble numbers are reported. From the components, the dense channel can add at most one question's gold chunk per corpus.
- **That the system reduces hallucinations** or improves LLM answers: generation was not evaluated.
- **That dense and BM25 are complementary** in terms of unique relevant chunks: no overlap, unique-hit or oracle-union analysis.
- **That morphological analysis (Kiwi) is better than stemming for agglutinative-language BM25 in general:** two conditions, no raw control, undefined Porter behaviour on Hangul, ≈49 questions, no tests, mixed results across k.
- **That multilingual models beat language-specific ones as a class:** mixed per model, uncontrolled for size/training data.
- **Anything about how the lexical representation changes dense–lexical complementarity** (the v0.8 core).
- Which query types each channel wins on: no per-query or query-feature analysis.

## 15. Relationship to current Uzbek evidence

- **No Uzbek data.** Korean is agglutinative (suffixing particles and endings), which makes the Kiwi vs Porter contrast the most Uzbek-relevant part. But Korean morpheme segmentation of Hangul eojeol differs from Uzbek Latin-script suffixation, and Korean has mature morphological tools (Kiwi), unlike the patchy Uzbek stemmer/lemmatizer landscape (MORPH-UZ-001…008).
- Parallel to the Uzbek RAG works in `MASTER_INDEX` G (USHRA, O-RAG, Urinov): a domain RAG where the retrieval stage is evaluated with small synthetic/QA-derived sets and the hybrid component is not separated from the rest. This paper is somewhat better in that it reports retrieval metrics per component, but it has the same blind spot for the hybrid itself.
- Same pattern as Mekonnen et al. (MORPH-005 proposed) and Munetsi et al. (MORPH-004): BM25 and dense compared, with no complementarity decomposition. Here a morphological tokenizer is present, but the comparison stops at averages.

## 16. Relationship to CURRENT_GAP

**Classification:** *no material effect* on the residual core; weakly *supports* the evidence boundary (another instance of the pattern).

- **Already non-claims in v0.8 that this paper also touches:**
  - "morphology-aware BM25 не сравнивали с semantic embeddings" — here Kiwi-BM25 is compared with 11 embedding models;
  - "morphology-aware lexical + semantic hybrid retrieval отсутствует" — here a Kiwi-BM25 ∪ dense ensemble is built (but not evaluated).
  These were already closed by stronger work (Aboasal, GreekBarRetrieval); this paper adds a Korean/medical example of lower evidential weight.
- **v0.8 core elements and whether they are present:**
  - raw / stem / lemma lexical variants — **partly**: two tokenizers (morpheme analyzer vs Porter), no raw control, only for Korean;
  - fixed dense comparator D across lexical variants — **no**: the ensemble pairs each guideline with a different dense model and a different tokenizer;
  - unique relevant hits / overlap / oracle union — **no**;
  - incremental hybrid gain — **no** (not measured);
  - per-query link to query features — **no**.
- None of the "What can still kill this gap" conditions (CURRENT_GAP §"What can still kill this gap") is met: not Uzbek, not Turkic, no complementarity decomposition.

**Proposal:** keep v0.8 refined unchanged. Optionally list this paper in the evidence boundary as "Korean (agglutinative) BM25 with morphological tokenizer vs stemmer + 11 dense models + union ensemble, without complementarity analysis or ensemble evaluation". This is a proposal only; `CURRENT_GAP.md` has not been edited.

## 17. Implications for our research design

- **Metric definitions (protocol).** Compute metrics with our own documented code or a standard tool (e.g. trec_eval-style definitions) and add a sanity check: MRR@k, MAP@k, nDCG@k and Recall@k must be non-decreasing in k for a fixed ranking. This paper shows how framework-computed metrics can silently break this.
- **Lexical variants.** Always include an explicit `BM25_raw` control and document what each normalizer does to every token class (for Uzbek: apostrophe variants o‘/g‘, Cyrillic/Latin, numbers). A stemmer designed for another language/script (like Porter on Hangul) is not a valid "raw" or "stem" condition.
- **Report the morphology effect per depth.** Kiwi vs Porter flips between k = 1 and k = 5–10 on Recall. For Uzbek, report raw/stem/lemma at several k (e.g. 1, 10, 100) and do not summarise with one "better across all metrics" statement.
- **Fixed D.** The authors paired a different dense model and tokenizer with each corpus, which makes any ensemble effect unattributable. Our design keeps D, fusion rule and k fixed across raw/stem/lemma (GAP_BOUNDARY §6).
- **Union vs fusion.** A union of top-k lists is a candidate-set operation; its recall is bounded by `max(R_lex, R_D)` and `min(1, R_lex + R_D)`. Our analysis should report candidate-union coverage (oracle union) separately from fused ranking quality, and compare at matched list sizes.
- **Qrels and sample size.** QA pairs generated from single chunks give one positive per query and ≈50 queries here; with that, unique-hit analysis collapses to a handful of queries (here ≤1). For Uzbek: several hundred queries if possible, pooled judgments from all channels, and paired per-query tests or bootstrap CIs.
- **Chunk overlap.** With overlapping chunks, define relevance at the passage-content level or deduplicate, otherwise neighbouring chunks are false negatives.
- **Cost.** Report morphological-analysis latency for the Uzbek analyzer; the Kiwi numbers show it can dominate retrieval time.
- **Hypothesis.** No evidence for or against our hypothesis.

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| RAG | The language model first searches a document collection and then writes its answer using what it found | Retrieval step + generation conditioned on retrieved passages |
| Hallucination | The model states something false with confidence | Generated content not supported by sources/facts |
| Chunk | A fixed-length piece of a document used as the retrieval unit | Here 1000 characters with 200-character overlap |
| BM25 | Classic keyword ranking: shared rare words and repeated matches score higher, with length normalization | Probabilistic relevance framework scoring with k1, b |
| Tokenizer (for BM25) | The rule that cuts text into the units BM25 matches | Mapping text → index terms |
| Kiwi (`ko_kiwi`) | A Korean morphological analyzer that splits words into morphemes | Morpheme segmentation/analysis for Korean (paper: "Korean morphological analysis and word segmentation") |
| Porter stemmer | Cuts English suffixes to get a common stem (e.g. "treatments" → "treatment") | Rule-based English suffix stripping |
| Dense retriever | Turns question and chunk into vectors; nearby vectors mean relevant | `sim(E(q), E(c))`, nearest-neighbour search |
| Zero-shot | Model used as downloaded, no training on this task | No task-specific parameter updates |
| Recall@k | Share of questions whose correct chunk is in the top k | Hit@k with one gold chunk |
| MRR / MAP / NDCG | How high the correct chunk is ranked | With one gold chunk: 1/r and 1/log₂(r+1), truncated at k |
| Ensemble (here) | Put the two result lists together | Union of top-k sets; ordering unspecified |
| Oracle union | The best possible recall if we could keep every correct chunk found by either channel | `|Rel ∩ (R_lex ∪ R_D)|` per query |
| Unique relevant hit | A correct chunk found by one channel and missed by the other | `Rel ∩ R_lex \ R_D` and vice versa |

## 19. Open questions / verification needed

1. **Table 4, k = 1:** is text-embedding-3-large 0.583 (table) or 0.563 (text, averages, Fig. 2)? Are the openai_embed_3_large and gte-multilingual-base rows swapped? Only the authors can confirm.
2. **Dense ranking metrics:** how were MAP/MRR/NDCG computed in Tables 3–4, given that they decrease with k? NOT_REPORTED.
3. **Number of questions and chunks** (inferred 49/48 questions): NOT_REPORTED.
4. **What `porter_stemmer` does to Korean text** (pre-tokenization, stemming of Hangul): NOT_REPORTED.
5. **BM25 parameters, stop-words, lower-casing:** NOT_REPORTED.
6. **Ensemble ordering and results:** how the union is ranked and what its metrics are: NOT_REPORTED.
7. **Query language for KDA** (Korean originals or English): not stated explicitly.
8. **Expert panel size and rejection rate** of generated QA pairs: NOT_REPORTED.

## 20. Decision after deep dive

- **Keep current gap?** Yes. v0.8 refined remains valid; see §16.
- **Modify gap?** No change proposed. Optionally add this paper to the evidence-boundary list as a low-weight Korean example (researcher's decision).
- **Add decision?** Proposed for `decisions/DECISIONS.md` (researcher's decision):
  - "Retrieval metrics are computed with documented definitions and checked for monotonicity in k; framework-internal metrics are not reported without verification";
  - "A union/ensemble is evaluated both as candidate coverage (oracle union, at matched list size) and as fused ranking; neither is claimed without numbers".
- **Add experiment?** No new experiment. It reinforces the planned `BM25_raw` control and multi-depth reporting.
- **Add citation to Chapter I?** Optional, low weight:
  - §1.3, as an example of domain RAG studies in an agglutinative language that combine a morphological BM25 tokenizer with dense retrieval but do not evaluate the hybrid or analyse complementarity;
  - not as evidence that hybrids improve retrieval or reduce hallucinations.
- **Proposed `MASTER_INDEX.md` row** (to add after approval):

| MORPH-012 | Lee, Cha, Hwangbo, Cheon — *Enhancing Large Language Model Reliability: Minimizing Hallucinations with Dual Retrieval-Augmented Generation Based on the Latest Diabetes Guidelines* (J. Pers. Med. 14(12):1131) — [deep dive](deep-dives/2024_Lee_Cha_Dual_RAG_Diabetes_Guidelines_Korean.md) | 2024 | B | MEDIUM | Korean (KDA) and English (ADA) guideline RAG; ≈49/48 LLM-generated, expert-approved single-positive questions (inferred). BM25 with Kiwi morpheme tokenizer vs Porter: Kiwi better on KDA ranking metrics and R@1/R@50 (0.306/0.98 vs 0.245/0.898) but not at R@5/R@10; comparable on English. 11 dense models (no fine-tuning described) (Solar Embedding-1-large best on KDA). Dense+BM25 union ensemble with **no reported results**; dense can add ≤1 unique hit per corpus [computed]. No raw control, no statistics, no overlap/unique-hit analysis; dense MAP/MRR/NDCG non-monotone in k; Table 4 vs text inconsistency. |
