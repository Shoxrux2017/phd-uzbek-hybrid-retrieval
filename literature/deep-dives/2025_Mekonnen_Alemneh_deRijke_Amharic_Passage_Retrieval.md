# Mekonnen, Alemneh & de Rijke (2025): Optimized Text Embedding Models and Benchmarks for Amharic Passage Retrieval

**Targeted deep-dive status:** COMPLETED (pilot, reviewed by researcher 2026-09-28)
**Completed:** 2026-09-28
**Literature ID:** `MORPH-005` (assigned 2026-09-28, approved by researcher)
**Systematic-review record:** `CR000149`. Full-text triage: INCLUDE, reading priority HIGH, `carries_complementarity_evidence = NO`
**Provenance:** AI-assisted deep dive (Claude). The paper was read in full: text plus page images of pp. 10433–10435 for Tables 1–2 and Figures 1–3. Every number below comes with its table/figure and printed page. Numbers computed by us are marked **[computed]**. A separate agent that had not seen the drafting checked all numbers and quotes against the paper; its corrections are included.
**Source rule:** **the paper is the primary and only authoritative source.**
- The public code repository was consulted only as supplementary context. Such items are marked **[repo, supplementary]**.
- The repository may be outdated or may not contain the final code. Nothing is concluded about what the authors did or did not do from the repository's content or its absence, and no repository item is used to contradict the paper.
**Reliability:** **A** (peer-reviewed, Findings of ACL 2025).

---

## Кратко для исследователя (RU)

- **Что сделано.** Для амхарского языка (семитский, корне-шаблонная морфология, письмо геэз) авторы:
  - дообучили три небольших амхарских энкодера как bi-encoder-ретриверы и одну ColBERT-модель;
  - сравнили их с BM25 и четырьмя многоязычными эмбеддинг-моделями на псевдо-бенчмарке «заголовок новости → её статья».
- **Главные числа** (Table 1–2, pp. 10433, 10435):
  - BM25 MRR@10 = 0.657;
  - лучший bi-encoder = 0.775;
  - ColBERT = 0.843;
  - Recall@100: BM25 0.871, dense 0.979.
- **BM25 без описанной морфологической обработки.** В статье сказано только «BM25Retriever из LlamaIndex» (Sec. 5.2). Стемминг, лемматизация, корни, нормализация и параметры k1/b не упоминаются. Работа не даёт морфологических вариантов лексического канала.
  - Фраза авторов «морфологических анализаторов и лемматизаторов не использовали» (Limitations, p. 10437) относится к их плотным моделям.
- **Нет гибрида и анализа взаимодополняемости:**
  - нет fusion BM25 + dense;
  - нет перекрытия результатов и уникально найденных документов;
  - нет oracle union и разбора по запросам.
  - Есть только качественные наблюдения (Sec. 6.6, App. B.2).
- **Морфология в работе — это токенизация плотных моделей** (subword fertility), а не вариант лексического представления. Связь «fertility → качество» корреляционная и смешана с тем, что амхарские модели дообучены in-domain, а многоязычные — нет.
- **Внутренние несоответствия в самой статье:**
  - fertility RoBERTa-Base: в тексте 1.46, на Fig. 1 — 1.55;
  - в методике 4 эпохи, но строка RoBERTa-Medium в Table 1 совпадает с ячейкой «5 эпох» в App. C;
  - отдельной dev-выборки не описано, подбор шёл на той же отложенной выборке.
- **На 2AIRTC** (коллекция с ручной разметкой) среди zero-shot bi-encoder'ов лучшая многоязычная E5, а не амхарские модели. Выше E5 только амхарский ColBERT.
- **Для нашего gap:**
  - работа закрывает широкие утверждения вида «BM25 vs dense для морфологически богатого low-resource языка не сравнивали»;
  - ядро v0.8 (raw/stem/lemma BM25 × фиксированный D → overlap/unique hits → прирост гибрида) **не затрагивает**.
  - Предложение: gap не менять.
- **Практическая польза для нас:**
  1. Если BM25 из Python-библиотек (bm25s / LlamaIndex) запускать с настройками по умолчанию, он разрезает узбекские слова с o‘/g‘, когда апостроф записан как ' ‘ ’ (сохраняется только ʻ), и применяет английский стеммер. Конфигурацию BM25 надо фиксировать явно (проверено нами на самой библиотеке, см. §17).
  2. Пары «заголовок–статья» — дешёвый источник обучающих/dev-данных для узбекского, но не замена экспертным qrels.
  3. Fertility запроса под токенизатором D — кандидат в признаки запроса.

---

## 1. Bibliographic record

- **Authors:** Kidist Amde Mekonnen*, Yosef Worku Alemneh*, Maarten de Rijke (*equal contribution)
- **Affiliations:** University of Amsterdam (Mekonnen, de Rijke); independent researcher (Alemneh)
- **Year:** 2025
- **Venue:** *Findings of the Association for Computational Linguistics: ACL 2025*, Vienna, Austria, 27 July – 1 August 2025
- **Editors:** Wanxiang Che, Joyce Nabende, Ekaterina Shutova, Mohammad Taher Pilehvar
- **Pages:** 10428–10445
- **Publisher:** Association for Computational Linguistics
- **ISBN:** 979-8-89176-256-5
- **ACL Anthology ID:** `2025.findings-acl.543`
- **DOI:** `10.18653/v1/2025.findings-acl.543`
- **Official record:** https://aclanthology.org/2025.findings-acl.543/
- **Preprint:** arXiv:2505.19356
- **Code (stated in paper, footnote 1):** https://github.com/kidist-amde/amharic-ir-benchmarks
- **Data (stated in paper, footnote 2):** Hugging Face `rasyosef/amharic-news-retrieval-dataset`
- **Source type:** peer-reviewed conference paper (Findings track)
- **Reliability:** A
- **Full text available:** yes (`07_full_text/pdfs/CR000149.pdf`, 18 pages including appendices)

## 2. Why this work matters to the PhD

It is one of the few **modern, peer-reviewed** IR papers that combines the following in one setting:

- a **low-resource, morphologically rich language**: Amharic (Semitic, root-and-pattern morphology, Ge'ez abugida script);
- a **lexical baseline**: BM25;
- **retrieval-trained dense bi-encoders**, both language-specific and multilingual;
- **late interaction**: ColBERT;
- an explicit research question on **tokenization / subword segmentation vs retrieval effectiveness** (RQ3).

How it relates to each project axis:

| Axis | Relation |
|---|---|
| Lexical retrieval | BM25 only, one configuration; no morphological processing (stemming/lemmatization/roots) is described |
| Semantic retrieval | Main focus: dense bi-encoders and ColBERT, with fine-tuning in the target language |
| Hybrid retrieval | **Absent**: no fusion, no combined run |
| Uzbek morphology | Indirect: different family (Semitic, non-concatenative) vs Uzbek (Turkic, agglutinative) |
| Low-resource retrieval | Direct: data scarcity, tokenization, weak supervision |
| Current gap | It closes broad "BM25 vs dense in a morphologically rich low-resource language" claims. It does **not** touch morphology-induced complementarity (§16) |

## 3. Research problem

### Simple explanation

Search systems that match exact words, like BM25, miss documents where the same idea appears in a different word form. That is common in languages like Amharic, where one root produces many surface forms. Multilingual neural models should help, but their tokenizers split Amharic words into many small pieces, which may hurt quality. The authors ask:

- Do **Amharic-specific** neural retrievers beat large multilingual ones?
- How do they compare with BM25?

### Formal formulation

Four research questions (Sec. 6: RQ1 on p. 10432, RQ2–RQ4 on p. 10433; paraphrased):

- **RQ1:** Do Amharic-optimized embeddings improve ranking vs general-purpose multilingual embedding models?
- **RQ2:** How do retrieval paradigms (sparse / dense bi-encoder / late interaction) compare on Amharic passage retrieval?
- **RQ3:** How does tokenization quality, "particularly subword segmentation", impact retrieval effectiveness in morphologically rich, low-resource languages? The paper operationalizes this as subword fertility.
- **RQ4:** How does base-model size affect ColBERT effectiveness in this low-resource setting?

Task: first-stage **passage retrieval**. Given a query `q` and a collection `P`, rank `P` so that the (single) relevant passage appears as high as possible.

## 4. Main idea

### Simple explanation

Take small BERT/RoBERTa models already pre-trained on Amharic text. Teach them retrieval by showing about 40K pairs of "news headline → its article". During training, other articles in the same batch serve as wrong answers. Then compare them with BM25 and with big multilingual embedding models used as-is.

### Concrete example

- Query (a news headline; the paper's own illustration in Sec. 6.6, p. 10436, in English translation): "Was the planned protest not held?".
- The only passage counted as relevant is the body of that same news article.
- BM25 finds it if the article repeats the headline's word forms.
- A dense model can find it even when the article uses other inflected forms or paraphrases.
- Any *other* article about the same protest counts as **non-relevant** by construction.
- The paper's failure case: a passage stating "The planned protest was held" is ranked highly despite the negation; BM25 matches on "protest" but ignores polarity (Sec. 6.6).

### Formal method

**Bi-encoder** (Sec. 4.1–4.2, pp. 10431–10432):

- Scoring: `f(q,p) = cos(Enc(q), Enc(p))`.
- `Enc` = mean pooling over the last hidden states, then L2 normalization.
- Training uses the multiple-negatives ranking loss (MNRL) with in-batch negatives (Eq. 4):

`L = −(1/B) Σ_i log [ exp f(q_i,p_i⁺) / ( exp f(q_i,p_i⁺) + Σ_{p_j⁻ ∈ N_i} exp f(q_i,p_j⁻) ) ]`

**ColBERT** (Eqs. 2–3): score by token-level maximum similarity,

`f(q,p) = Σ_{i=1..m} max_{j} sim(h_i^q, h_j^p)`

## 5. Architecture / algorithm

1. **Base encoders** (Sec. 4.2, p. 10431), all pre-trained on Amharic (≈300M tokens, Sec. 6.6 / Limitations):
   - RoBERTa-Base-Amharic: 110M parameters, 12 layers, hidden size 768, XLM-RoBERTa architecture.
   - RoBERTa-Medium-Amharic: 42M parameters, 8 layers, hidden size 512.
   - BERT-Medium-Amharic: 40M parameters, 8 layers, hidden size 512.
2. **Bi-encoder fine-tuning** (Sec. 4.2 / 5.2, p. 10432):
   - sentence-transformers trainer, MNRL loss;
   - lr 5e-5, batch 128, cosine schedule, 4 epochs, max length 512;
   - single A100 40GB GPU.
   - In-paper tension: Table 1's RoBERTa-Medium row equals the **5-epoch** cell of the Appendix C grid (§9). No dev split or checkpoint-selection procedure is described.
3. **ColBERT** (Sec. 5.2, p. 10432):
   - PyLate library, lr 1e-5, batch 32;
   - 8 hard negatives drawn from the top-150 of RoBERTa-Medium-Amharic-Embed.
   - Reporting ambiguity: Sec. 5.2 says the model was adapted "using the RoBERTa-Medium-Amharic encoder". The Table 2 caption says the best ColBERT "builds on the RoBERTa-Base-Amharic-Embed encoder". Sec. 6.4 reports three ColBERT backbones.
4. **BM25** (Sec. 5.2, p. 10432):
   - The paper says only "BM25Retriever from the LlamaIndex framework".
   - Tokenization, stemming, stop-words, normalization and k1/b are **NOT_REPORTED**. No Amharic morphological processing (stemming, lemmatization, root extraction) is described for BM25.
   - We therefore treat "BM25-AM" as a single **surface-form-type BM25 configuration**: it is not a morphologically normalized lexical channel.
   - Context (a property of the library, not a claim about the authors' run): LlamaIndex `BM25Retriever` / `bm25s` defaults are an English Snowball stemmer, English stop-words, token pattern `(?u)\b\w\w+\b` (drops one-character tokens), k1 = 1.5, b = 0.75. This is relevant for our own design (§17).
5. **Multilingual baselines**: used **zero-shot**:
   - gte-modernbert-base;
   - gte-multilingual-base;
   - multilingual-e5-large-instruct;
   - snowflake-arctic-embed-l-v2.0.
   Plus one **fine-tuned** variant, Snowflake-AM (hyperparameters in Sec. 5.2, results in Sec. 6.5): lr 2e-5, batch 128, warmup 0.1, weight decay 0.01, 4 epochs.
6. **Tokenization analysis** (Sec. 6.3): average subword fertility on a 10k-passage subset. Fertility means average number of subword tokens per word.

## 6. Data

### Main benchmark: "Amharic Passage Retrieval Dataset" (Sec. 5.1, p. 10432)

- **Source:** Amharic News Text Classification Dataset, AMNEWS (Azime & Mohammed, 2021): 50,706 news articles in 6 categories (Local News, Sports, Politics, International News, Business, Entertainment).
- **Language / domain:** Amharic; news.
- **Queries:** article headlines.
- **Passages:** article bodies, truncated to 512 tokens.
- **Relevance judgments:**
  - heuristic: each headline is relevant **only** to its own article, so there is exactly one positive per query;
  - binary;
  - no human qrels.
  - The authors "manually examined a random subset". The subset size and the agreement procedure are **not reported**.
- **Deduplication:** MD5 hashing, giving "approximately 45K query–passage pairs".
- **Split:** 10% held out for evaluation, stratified by category. No separate dev split is described.
- **Exact sizes: NOT_REPORTED.** The exact number of test queries and the size of the retrieval corpus are not stated; ≈45K pairs × 10% implies ≈4.5K test queries **[computed, approximate]**.

### Secondary benchmark: 2AIRTC (App. A, pp. 10440–10442)

- TREC-style Amharic ad hoc collection (Yeshambel et al., 2020): 12,583 documents, 240 topics, manual relevance judgments.
- The authors state that the judgments are incomplete and sparse.
- Used **zero-shot**: models trained on the news pairs are evaluated here without adaptation.
- **BM25 is not reported on 2AIRTC.**

## 7. Baselines

| Baseline | What it is | Why selected | Fair comparison? |
|---|---|---|---|
| BM25-AM | Lexical probabilistic ranking | Standard sparse reference | **Partly.** A single configuration with no reported tuning or Amharic morphological processing. It is not the strongest lexical baseline possible for Amharic: stem/root indexing exists in prior Amharic IR (CR000354; CR000427; CR000447) |
| gte-modernbert-base | Embedding model (149M) that the paper lists under "Multilingual models". Our outside knowledge: it is essentially English-oriented, and its fertility of 13.80 on Amharic is consistent with that | Included in the "multilingual" group | **No.** Its MRR@10 = 0.019 reflects inability to represent Amharic, not a meaningful competitor |
| gte-multilingual-base (305M), multilingual-e5-large-instruct (560M), snowflake-arctic-embed-l-v2.0 (568M) | Strong general multilingual retrievers | The paper names Arctic Embed 2.0 and Multilingual E5 as top of the MTEB leaderboard at the time (p. 10430) | **Asymmetric.** Used zero-shot, while the Amharic models were fine-tuned **in-domain** on the same headline→article task. Table 1 therefore compares *in-domain supervised* vs *zero-shot* more than *language-specific* vs *multilingual* |
| Snowflake-AM (fine-tuned) | Arctic-Embed fine-tuned on the same Amharic pairs | Controls for in-domain supervision | **Yes, and it matters.** With the same supervision the multilingual model reaches MRR@10 0.827, *above* the best Amharic bi-encoder, 0.775 (Tables 1, 3) |
| RoBERTa-Base-Amharic-Embed (bi-encoder) | Authors' best single-vector model | Reference for ColBERT | Yes (same data) |

Additional note: the "strongest multilingual baseline" used for the † significance marks is Snowflake. On MRR@10 and NDCG@10, however, E5 is higher (0.672 / 0.709 vs 0.659 / 0.701; Table 1). Snowflake is higher only on Recall.

## 8. Metrics

With **exactly one relevant passage per query**, all metrics reduce to functions of a single number: the rank *r* of that passage.

| Metric | Definition | Simple meaning here | Appropriate? |
|---|---|---|---|
| MRR@10 | mean of 1/r if r ≤ 10, else 0 | "How high is the correct article, on average, looking only at the top 10?" | Yes for known-item search |
| NDCG@10 (binary) | 1/log₂(r+1) if r ≤ 10, else 0 (ideal DCG = 1) | Softer version of MRR: rank 2 scores 0.63 instead of 0.5 | Yes, but adds little beyond MRR with one positive |
| Recall@k (k = 10, 50, 100) | 1 if r ≤ k, else 0, averaged | "In what share of queries is the correct article inside the top k?" (= Hit@k / success@k) | Yes. Recall@100 is the candidate-coverage view relevant to hybrids |
| 2AIRTC: MRR@100, NDCG@100, Recall@100/200 | standard, graded/incomplete qrels | — | Weakened by incomplete judgments (authors' own caveat) |

Significance: a paired t-test at p < 0.05 is named in the captions of Tables 1–3. Tables 5–6 say only "statistically significant (p < 0.05)" without naming the test. No confidence intervals.

## 9. Results

### Table 1: bi-encoders on the Amharic Passage Retrieval Dataset (p. 10433)

| Model | Params | MRR@10 | NDCG@10 | R@10 | R@50 | R@100 |
|---|---:|---:|---:|---:|---:|---:|
| gte-modernbert-base (zero-shot) | 149M | 0.019 | 0.023 | 0.033 | 0.051 | 0.067 |
| gte-multilingual-base (zero-shot) | 305M | 0.600 | 0.638 | 0.760 | 0.851 | 0.882 |
| multilingual-e5-large-instruct (zero-shot) | 560M | 0.672 | 0.709 | 0.825 | 0.911 | 0.931 |
| snowflake-arctic-embed-l-v2.0 (zero-shot) | 568M | 0.659 | 0.701 | 0.831 | 0.922 | 0.942 |
| BERT-Medium-Amharic-Embed | 40M | 0.682 | 0.720 | 0.843 | 0.931 | 0.954 |
| RoBERTa-Medium-Amharic-Embed | 42M | 0.735 | 0.771 | 0.884 | 0.955 | 0.971 |
| **RoBERTa-Base-Amharic-Embed** | 110M | **0.775†** | **0.808†** | **0.913†** | **0.964†** | **0.979†** |

† = significant vs "strongest multilingual baseline" (paired t-test, p < 0.05).

How the reported gains are computed:
- **+17.6%** relative MRR@10 = (0.775 − 0.659)/0.659 vs Snowflake **[computed: 17.6% ✓]**.
- Against E5, which has the higher MRR@10, the gain is **+15.3%** **[computed]**.
- Abstract: "+9.86% Recall@10" = (0.913 − 0.831)/0.831 **[computed: 9.87%]**.

### Table 2: sparse vs dense (p. 10435)

| Type | Model | MRR@10 | NDCG@10 | R@10 | R@50 | R@100 |
|---|---|---:|---:|---:|---:|---:|
| Sparse | BM25-AM | 0.657 | 0.682 | 0.774 | 0.847 | 0.871 |
| Dense (bi-encoder) | RoBERTa-Base-Amharic-Embed | 0.775 | 0.808 | 0.913 | 0.964 | 0.979 |
| Dense (late interaction) | ColBERT-RoBERTa-Base-Amharic | **0.843†** | **0.866†** | **0.939†** | **0.972†** | 0.979 |

Reading the table:
- ColBERT vs BM25: +28.31% relative MRR@10 **[computed: (0.843−0.657)/0.657 = 28.31% ✓]**.
- Bi-encoder vs BM25: +0.118 MRR@10 absolute (+18.0% relative) **[computed]**.
- The † marks refer to "the strongest baseline" and appear only on the ColBERT row. The pattern (only R@100, where ColBERT ties the bi-encoder at 0.979, is unmarked) indicates that the reference is the bi-encoder. **Significance of dense vs BM25 is not reported.**
- **BM25 vs zero-shot multilingual dense** (cross-reading Tables 1–2) **[computed]**:
  - **On MRR@10**, BM25 (0.657) is about equal to Snowflake (0.659), 0.015 below E5 (0.672) and above gte-multilingual (0.600).
  - On NDCG@10 it is below E5 and Snowflake (0.682 vs 0.709 / 0.701).
  - On R@10 it is between gte-multilingual and the other two (0.774 vs 0.760 / 0.825 / 0.831).
  - On R@50 and R@100 it is below all three (0.847 / 0.871 vs ≥ 0.851 / 0.882).
  - So BM25 is **competitive at the top of the ranking** with large zero-shot multilingual dense retrievers, but has **lower deep coverage**.
- Coverage **[computed]**:
  - BM25 misses the relevant passage in its top-100 for 12.9% of queries (1 − 0.871);
  - the bi-encoder misses it for 2.1% (1 − 0.979).

### Table 3: effect of in-domain fine-tuning of the multilingual model (p. 10436)

| Model | MRR@10 | NDCG@10 | R@10 | R@50 | R@100 |
|---|---:|---:|---:|---:|---:|
| snowflake-arctic-embed-l-v2.0 (zero-shot) | 0.659 | 0.701 | 0.831 | 0.922 | 0.942 |
| snowflake-arctic-embed-l-v2.0-AM (fine-tuned) | **0.827†** | **0.855†** | **0.942†** | **0.977†** | **0.985†** |

- The text reports "+25.5%" relative MRR@10 **[computed: (0.827−0.659)/0.659 = 25.5% ✓]**.
- The fine-tuned multilingual model (0.827) **exceeds** the best Amharic bi-encoder (0.775) by 0.052 MRR@10 **[computed]**. It is 0.016 below ColBERT (0.843).

### Figure 1: average subword fertility, 10k passages (p. 10434)

| Model | Fig. 1 as printed | MRR@10 (Table 1) |
|---|---:|---:|
| BERT-Medium-Amharic-Embed | 1.46 | 0.682 |
| RoBERTa-Medium-Amharic-Embed | 1.46 | 0.735 |
| RoBERTa-Base-Amharic-Embed | 1.55 | 0.775 |
| gte-multilingual-base | 2.35 | 0.600 |
| multilingual-e5-large-instruct | 2.35 | 0.672 |
| snowflake-arctic-embed-l-v2.0 | 2.35 | 0.659 |
| gte-modernbert-base | 13.80 | 0.019 |

- **Internal inconsistency in the paper.** The text (Sec. 6.3, p. 10434) says RoBERTa-Base-Amharic-Embed has "the lowest fertility (1.46)". The printed Fig. 1 (checked on the page image) shows 1.55 for it and 1.46 for BERT-Medium. Which is correct cannot be decided from the paper; plausibly two figure labels are swapped.
- Fig. 2 compares one sentence: RoBERTa-Base 12 subwords (fertility 1.50) vs Snowflake 19 subwords (2.38).
- Conclusions that hold **under either reading**:
  - Fertility does **not** explain why RoBERTa-Base beats RoBERTa-Medium (0.775 vs 0.735). Under the text's values both are 1.46; under the figure's values RoBERTa-Base is *higher* (1.55). That difference follows model size, not tokenization.
  - Only under the text's reading is the highest-fertility Amharic model (then BERT-Medium, 1.55) also the weakest (0.682).
  - Among the three XLM-R-tokenizer models, fertility is identical (2.35) while MRR@10 ranges 0.600–0.672.
  - The large contrasts (1.46 vs 2.35 vs 13.80) coincide with model family and with in-domain fine-tuning vs zero-shot use.

### Sec. 6.4 / Figure 3: ColBERT backbone size (p. 10435)

| ColBERT backbone | MRR@10 | Other reported values |
|---|---:|---|
| RoBERTa-Base-Amharic (110M) | 0.843 | NDCG@10 0.866, R@10 0.939 |
| RoBERTa-Medium-Amharic (42M) | 0.831 | R@10 0.928 |
| BERT-Medium-Amharic (40M) | 0.806 | — |

- Text: Medium is "a 1.5% relative performance difference" **[computed: 1.4%]**, "62% smaller" **[computed: 1 − 42/110 = 61.8% ✓]**.

### 2AIRTC, zero-shot (App. A; Tables 4–5 on p. 10442, Table 6 on p. 10443)

| Model | MRR@100 | NDCG@100 | R@100 | R@200 |
|---|---:|---:|---:|---:|
| multilingual-e5-large-instruct | 0.905 | 0.808 | 0.853 | 0.911 |
| gte-multilingual-base | 0.879 | 0.749 | 0.790 | 0.865 |
| snowflake-arctic-embed-l-v2.0 | 0.876 | 0.781 | 0.830 | 0.897 |
| RoBERTa-Base-Amharic-embed | 0.861 | 0.770 | 0.830 | 0.910 |
| RoBERTa-Medium-Amharic-embed | 0.853 | 0.735 | 0.798 | 0.878 |
| BERT-Medium-Amharic-embed | 0.805 | 0.667 | 0.727 | 0.828 |
| gte-modernbert-base | 0.046 | 0.017 | 0.021 | 0.033 |
| Snowflake-AM (fine-tuned on news, Table 5) | 0.865 | 0.795† | 0.856† | 0.923† |
| ColBERT-RoBERTa-Base-Amharic (Table 6) | 0.919† | 0.834† | 0.887† | R@200 0.906 |
| ColBERT-BERT-Medium-Amharic (Table 6) | 0.907 | 0.823 (@200: 0.842†) | 0.880 | 0.930† |

- On the collection with human judgments, the Amharic **bi-encoders do not beat** the best zero-shot multilingual bi-encoder: E5 is best among the Table 4 bi-encoders on all four metrics.
- Above E5 are:
  - the Amharic ColBERT models (RoBERTa-Base: MRR@100 0.919†, NDCG@100 0.834†, R@100 0.887†);
  - Snowflake-AM, on recall (R@100 0.856, R@200 0.923).
- So the Amharic advantage on 2AIRTC survives only for the late-interaction models.
- The authors present the 2AIRTC results as "indicative rather than conclusive".
- The text says RoBERTa-Base is "just one point below" E5 on NDCG@100 and R@200 **[computed]**:
  - on R@200 the gap is 0.1 point (0.910 vs 0.911);
  - on NDCG@100 it is 3.8 points (0.770 vs 0.808).

### Appendix C: hyperparameter grid (RoBERTa-Medium, pp. 10443–10445)

- Grid: lr {2e-5, 5e-5} × batch {64, 128, 256} × epochs {3, 5}.
- Best MRR@10 = 0.737 (5e-5 / 256 / 5 epochs); Recall@10 up to 0.887.
- No separate dev set is described, so the grid appears to be evaluated on the same held-out split (§12).
- **In-paper evidence on epochs:** Table 1's RoBERTa-Medium row (0.735 / 0.771 / 0.884) exactly equals the **5-epoch** grid cell for lr 5e-5 / batch 128 (Figs. 5–7, p. 10444). Sec. 4.2 / 5.2 say 4 epochs, so Table 1 appears to come from a 5-epoch run scored on the test split.

## 10. Statistical evidence

- **Significance test:** paired t-test, p < 0.05, against "the strongest baseline" (named in the captions of Tables 1–3). In Table 2 the reference appears to be the bi-encoder (§9). The raw p-values are **NOT_REPORTED**.
- **Confidence intervals:** NOT_REPORTED.
- **Runs / seeds:** the number of runs is NOT_REPORTED. It is presumably a single run, since no variance is shown.
- **Ablation:** there is no ablation of pooling, loss or negatives. The Appendix C grid (lr × batch × epochs) is a sensitivity analysis, not an ablation. The Snowflake-AM experiment acts as a partial control for in-domain supervision.
- **Per-query analysis:** **none quantitative.** Sec. 6.6 and App. B.2 give qualitative examples (negation, temporal shift; BM25 favouring surface overlap). There is:
  - no per-query win/loss analysis;
  - no overlap or unique-hit analysis between BM25 and dense;
  - no oracle union;
  - no breakdown by query characteristics.

## 11. Strengths

- Full paradigm spectrum in one setting: lexical BM25, zero-shot multilingual dense, in-language fine-tuned dense, late interaction, and a fine-tuned multilingual control.
- Explicit research question linking tokenization to retrieval in a morphologically rich language (RQ3).
- Standard IR metrics at several depths, including Recall@100, the relevant depth for first-stage candidate generation.
- A second, human-judged collection (2AIRTC) is reported. It tempers the main claim, and the authors say so.
- Open release of code, dataset and models is announced (footnotes 1–3).
- Honest limitations section: weak supervision, no morphological analyzers, news-only domain, 300M-token pretraining.

## 12. Limitations

### Stated by the authors

- Heuristic headline→article relevance labels. There are no human judgments, which introduces noise (Sec. 6.6, Sec. 8, App. B.1).
- Headlines are editorial, not real information needs (App. B.1).
- Sampled negatives may be topically related, i.e. false negatives (App. B.1).
- News domain only; other domains are untested (Sec. 8).
- Small pretraining corpus (300M tokens) (Sec. 8).
- **"Our models do not incorporate explicit morphological analyzers, lemmatizers, or segmentation tools"** (Sec. 8, p. 10437). This refers to their dense models; nothing is said about normalizing the BM25 baseline.
- 2AIRTC has incomplete judgments, so its results are only indicative (App. A).

### Inferred from the experimental design

1. **Language-specific vs in-domain confound.**
   - Amharic models are fine-tuned on the task, while multilingual models are zero-shot.
   - When the multilingual model gets the same fine-tuning it wins among bi-encoders (0.827 vs 0.775).
   - On 2AIRTC the Amharic advantage disappears for bi-encoders.
2. **BM25 is one configuration with no reported tuning or morphological processing.** Tokenizer, stemming, normalization and k1/b are not reported. No stem/root variants are tested, even though such variants exist in prior Amharic IR work.
3. **Possible tuning on the evaluation split.** Only train/test are described, with no dev split. The Appendix C hyperparameter grid reports scores on the held-out split, and the RoBERTa-Medium row of Table 1 equals the 5-epoch grid cell, while Sec. 4.2 / 5.2 say 4 epochs. If configurations were chosen on the same split, the dense scores may be mildly optimistic. The paper does not state how the final configuration was selected.
4. **Fertility analysis is correlational and confounded.** Fertility co-varies with model family, parameter count, pretraining data and, above all, whether the model was fine-tuned in-domain. Text and Fig. 1 disagree on the Amharic values; under either reading, fertility does not explain the difference between the two RoBERTa models (§9).
5. **Single-positive pseudo-qrels.** Every other relevant article is treated as non-relevant. That penalizes any system retrieving topically correct alternatives. The task is closer to **known-item search** than ad hoc retrieval. Headlines also share vocabulary with their own article, which may favour lexical matching; the direction of the bias is unknown.
6. **The morphological difficulty of queries is never measured.** No query-level morphological features, no inflection-mismatch subsets.
7. Number of runs not reported; no seed variance; no confidence intervals.

## 13. What the work proves

- On a large Amharic headline→article benchmark, **in-language fine-tuned dense retrievers outperform BM25 (no morphological processing reported) by a wide margin**: MRR@10 0.775 (bi-encoder), 0.843 (ColBERT) vs 0.657; Recall@100 0.979 vs 0.871 (Table 2).
  - Caveat: no significance test for dense vs BM25 is reported.
  - The margin is large enough that the direction is very likely robust; the exact size is less certain.
- **At the top of the ranking, BM25 is competitive with large zero-shot multilingual dense retrievers**:
  - MRR@10 0.657 vs 0.659–0.672 (cross-reading Tables 1–2);
  - its deeper coverage is lower: R@100 0.871 vs 0.882–0.942.
- **In-language retrieval supervision is the main driver of dense gains** here. The decisive evidence is the Snowflake control: the same fine-tuning lifts it by +0.168 MRR@10, above the Amharic bi-encoder (Table 3).
- An English-oriented model (gte-modernbert, fertility 13.80) fails almost completely on Amharic (MRR@10 0.019).
- On the news benchmark, ColBERT with an Amharic backbone has the best MRR@10, NDCG@10 and R@10 of all systems. On R@50 and R@100, Snowflake-AM is slightly higher (0.977 / 0.985 vs 0.972 / 0.979; not tested against each other). A 42M backbone is close to 110M (0.831 vs 0.843).

## 14. What the work does NOT prove

- **That language-specific models beat multilingual models as such.** The comparison is confounded with in-domain fine-tuning:
  - the fine-tuned multilingual model beats the Amharic bi-encoder;
  - on 2AIRTC, E5 is the best bi-encoder.
- **That lower subword fertility *causes* better retrieval.** The evidence is correlational and not controlled. Text and Fig. 1 disagree on the values, and fertility does not explain the RoBERTa-Base vs RoBERTa-Medium difference.
- **Anything about morphological normalization of the lexical channel.** No stemming, lemmatization or root-based BM25 variant is reported.
- **That BM25 and dense are complementary, or that a hybrid would help.** Section 6.2 speaks of "complementary strengths" between *encoders and ColBERT*, not between lexical and dense. No fusion, overlap or unique-hit evidence exists.
- **Which queries each channel wins on, or why.** There is no per-query or query-feature analysis; only anecdotes.
- **Generalization to real information needs or other domains.** Pseudo-qrels, news only, and the human-judged 2AIRTC results show a different ordering.

## 15. Relationship to current Uzbek evidence

- **No Uzbek data.** Amharic is Semitic (root-and-pattern, non-concatenative), while Uzbek is Turkic (agglutinative, suffixing). Findings about subword tokenization may transfer in spirit, since both suffer multilingual over-segmentation. Findings about BM25 morphology do not transfer at all, because none were tested.
- Parallel to the Uzbek situation:
  - multilingual models used zero-shot vs a small in-language pre-trained encoder (cf. UzBERT, BERTbek in `MASTER_INDEX` E);
  - lack of human-judged test collections;
  - a news domain as the cheapest source of data.
- Same pattern as Munetsi et al. (Shona, MORPH-004): BM25 < neural in a morphologically rich low-resource language, **without** a morphology-normalized BM25 or any fusion. Together they show a recurring blind spot in modern low-resource IR papers, which our design addresses directly.
- Related Amharic records in our corpus (triage INCLUDE, HIGH) that fill exactly the lexical-morphology side this paper omits:
  - **CR000354**: Alemayehu & Willett, 2003 — word vs stem vs root, Okapi;
  - **CR000447**: Yeshambel et al., 2024 — 2AIRTC resources; word vs stem vs root by MAP/NDCG;
  - **CR000427**: Yeshambel et al., 2023 — learned representations and query expansion on 2AIRTC in word/stem/root variants.
  - For Amharic, the two halves (morphology-normalized lexical IR; modern dense IR) therefore exist **in separate papers on different collections**. None of them joins them in one controlled setting.
- Follow-up by the same authors: **CR000226** (*The Multilingual Curse at the Retrieval Layer: Evidence from Amharic*, MeLLM 2026). It was excluded at triage (FT2: morphology only as motivation), but it is worth a quick check for any BM25/dense overlap numbers.

## 16. Relationship to CURRENT_GAP

**Classification:** *closes part of the broad gap* + *narrows* + *no material effect on the residual core*.

- **Closes / confirms as occupied** (these were already listed as non-claims in v0.8):
  - "BM25 has not been compared with modern dense retrieval in a morphologically rich low-resource language";
  - "tokenization/morphology has not been linked to dense retrieval quality in such languages".
  This paper is a strong A-level citation for both.
- **Narrows:** the paper sets up the exact situation where our question becomes necessary:
  - dense ≫ BM25 on average;
  - no morphologically normalized BM25 variant is reported;
  - it is never fused;
  - the channels' result sets are never compared.
  A reader cannot tell from it whether BM25 contributes any relevant passages the dense model misses: the 12.9% vs 2.1% top-100 miss rates say nothing about overlap. Whether stemming or lemmatization would change that is also unknown.
- **No material effect on the residual core** of v0.8 refined:
  - morphological representation (raw/stem/lemma BM25) → change in complementarity with a **fixed** dense retriever D;
  - unique relevant hits / overlap;
  - incremental hybrid gain;
  - link to query features.
  None of these elements is present.

**Proposal:** keep v0.8 refined unchanged. Add this paper to the evidence boundary as a modern Findings-of-ACL example of "BM25 vs dense in a morphologically rich low-resource language *without* morphology-normalized BM25 or complementarity analysis". This is a proposal only; `CURRENT_GAP.md` has not been edited.

## 17. Implications for our research design

- **Baseline selection / D.**
  - Do not treat "language-specific vs multilingual" as the variable. Supervision dominates.
  - If D is fine-tuned on Uzbek data, it must be *fixed* before the raw/stem/lemma comparison, and the same D used for all lexical variants.
  - Report both a zero-shot and (if used) a fine-tuned D, because the lexical–dense gap, and therefore any complementarity, will differ strongly between them.
- **BM25 configuration must be explicit.** This paper reports none, and popular Python BM25 library defaults are unsafe for Uzbek. We checked the `bm25s` / LlamaIndex default token pattern `(?u)\b\w\w+\b` ourselves, run through Python `re` **[computed, 2026-09-28]**:
  - `O‘zbekiston` → `['zbekiston']`;
  - `qo‘shiq` → `['qo', 'shiq']`;
  - the same split happens with ASCII `'` and `’` (U+2019);
  - only the official modifier letter `ʻ` (U+02BB) keeps words intact, because Python counts it as a word character;
  - real Uzbek text mixes all four variants, so the same word can be indexed differently;
  - one-letter pieces (`o`, `g`) are dropped.
  - The default English Snowball stemmer mostly leaves Uzbek tokens unchanged, but occasionally alters them (`yozing` → `yoze`, tested with PyStemmer). A "raw" run with library defaults is therefore not truly raw.
  For our "raw" condition we must fix and report:
  - the tokenizer;
  - apostrophe normalization;
  - lowercasing;
  - stop-words (none or an Uzbek list);
  - stemmer = none;
  - k1 and b.
- **Dataset / qrels.**
  - Headline→article pairs from Uzbek news sites are a cheap, scalable source of **training / dev** data for D and for pilot runs.
  - They are not a substitute for the main evaluation qrels. Single-positive labels make overlap/unique-hit analysis coarse: each query has one "hit or miss" per channel. Pooled human judgments remain necessary for the main experiment.
- **Query taxonomy.** Add **subword fertility of the query under D's tokenizer** as a candidate query feature, alongside morphological features: number of inflectional suffixes, OOV rate, script/apostrophe variants. It can be tested *per query*, which avoids the between-model confound seen here.
- **Metrics.** Report Recall@100 (candidate coverage) in addition to MRR/nDCG; the ranking picture and the coverage picture differ.
- **Protocol hygiene.**
  - Separate dev and test splits; select checkpoints and fusion weights only on dev.
  - Evaluate all channels on the identical query set.
  - Report seed variance or bootstrap CIs, not only paired t-tests.
- **Hypothesis.** This paper gives no evidence for or against our hypothesis. It motivates it: when dense ≫ unnormalized BM25 on average, whether lemmatized/stemmed BM25 adds *unique* relevant documents is exactly the open question.

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| Passage retrieval | Find the right text fragment in a large collection for a query | Rank collection `P` by `f(q,p)`; first-stage retrieval |
| BM25 | Classic word-matching ranking: rarer shared words and more repetitions give a higher score, with length normalization | Probabilistic relevance framework scoring with parameters k1, b |
| Surface-form (raw) BM25 | BM25 over words exactly as written, no stemming/lemmatization | Index terms = tokenized word forms |
| Bi-encoder (dense retriever) | Turns query and passage into one vector each; similar vectors mean relevant | `f(q,p)=sim(Enc(q),Enc(p))`, pre-computed passage vectors, ANN search |
| Late interaction (ColBERT) | Keeps a vector per token and matches each query token to its best passage token | `Σ_i max_j sim(h_i^q,h_j^p)` |
| Zero-shot | Model used as downloaded, without training on this task/language | No task-specific parameter updates |
| Fine-tuning (in-domain) | Extra training on the same kind of data as the test | Supervised updates on train split of the same distribution |
| MNRL / in-batch negatives | During training, other passages in the batch count as wrong answers | Softmax cross-entropy over positives vs in-batch negatives (Eq. 4) |
| Subword fertility | How many pieces the tokenizer cuts an average word into | mean(#subword tokens / #words) |
| Pseudo-qrels / heuristic relevance | Relevance assumed from data structure (headline ↔ its own article), not judged by people | Automatically constructed qrels |
| Known-item search | The user looks for one specific document that exists | Single target per query |
| Paired t-test | Checks whether the per-query score differences between two systems are reliably non-zero | Test on per-query metric differences |
| Complementarity (project term) | Each channel finds some relevant documents the other misses | Unique relevant hits, overlap, oracle-union gain |

## 19. Open questions / verification needed

1. **BM25 configuration** (tokenizer, stemming, stop-words, k1/b) and exact test-set size: NOT_REPORTED. Only the authors can confirm them.
2. **Fertility of RoBERTa-Base-Amharic:** 1.46 (text) or 1.55 (Fig. 1)? Not decidable from the paper.
3. **Epochs and configuration selection:** 4 epochs (Sec. 4.2 / 5.2) vs the Table 1 = 5-epoch grid match (App. C). The results should not be quoted as a clean held-out estimate without this caveat.
4. **ColBERT backbone for Table 2:** RoBERTa-Base (Table 2, Sec. 6.4) vs RoBERTa-Medium (Sec. 5.2)?
5. **Size of the "manually examined random subset"** of headline–article pairs: NOT_REPORTED.
6. **Is a BM25+dense overlap analysis possible from public resources?** The dataset and models are announced as public. Running BM25 plus the released bi-encoder on the public split would make a cheap Amharic pilot of our overlap/unique-hit measurements, with the single-positive caveat.
7. Check **CR000226** (same authors, 2026) for any lexical–dense overlap or fusion numbers before claiming none exist for Amharic.

## 20. Decision after deep dive

- **Keep current gap?** Yes. v0.8 refined remains valid; see the proposal in §16.
- **Modify gap?** No change proposed. Optionally add this paper to the evidence-boundary list in `CURRENT_GAP.md` / `GAP_BOUNDARY` as an Amharic example (researcher's decision).
- **Add decision?** Proposed for `decisions/DECISIONS.md` (researcher's decision):
  - "BM25 configuration (tokenizer, apostrophe normalization, stop-words, stemmer, k1/b) must be fixed explicitly and reported; library defaults are not allowed";
  - "checkpoint/fusion-weight selection on dev only".
- **Add experiment?** Optional low-cost pilot: run our own raw BM25 + the released Amharic bi-encoder on the public dataset and compute overlap / unique hits / oracle union at k = 10/100. This tests our measurement pipeline on an existing public benchmark before Uzbek data exist.
- **Add citation to Chapter I?** Yes:
  - §1.2 (modern dense retrieval in low-resource, morphologically rich languages; tokenization/fertility);
  - §1.3 (as evidence that modern low-resource studies compare BM25 vs dense but do not normalize the lexical channel or analyse complementarity).
- **Proposed `MASTER_INDEX.md` row** (to add after approval):

| MORPH-005 | Mekonnen, Alemneh, de Rijke — *Optimized Text Embedding Models and Benchmarks for Amharic Passage Retrieval* (Findings of ACL 2025) — [deep dive](deep-dives/2025_Mekonnen_Alemneh_deRijke_Amharic_Passage_Retrieval.md) | 2025 | A | HIGH | Amharic BM25 (single configuration, no morphological processing reported) vs zero-shot multilingual and fine-tuned Amharic bi-encoders and ColBERT; subword-fertility analysis. Dense ≫ BM25 (MRR@10 0.775/0.843 vs 0.657), BM25 ≈ zero-shot multilingual dense on MRR@10. Language-specific advantage confounded with in-domain fine-tuning (fine-tuned Snowflake 0.827; E5 best bi-encoder on 2AIRTC). No stem/lemma BM25, no fusion, no overlap/unique-hit analysis. |
