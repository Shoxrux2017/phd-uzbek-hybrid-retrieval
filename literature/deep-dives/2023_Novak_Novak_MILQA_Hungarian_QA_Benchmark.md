# Novák, Novák, Zombori, Szabó, Szántó & Farkas (2023): A Question Answering Benchmark Database for Hungarian

**Targeted deep-dive status:** COMPLETED (AI-assisted, pending researcher review)
**Completed:** 2026-09-28
**Literature ID:** `MORPH-006` (assigned 2026-09-28, approved by researcher)
**Systematic-review record:** `CR000073`. Full-text triage: INCLUDE, reading priority HIGH, tier "1 — прямо по теме пробела", `carries_complementarity_evidence = NO`
**Provenance:** AI-assisted deep dive (Claude). The whole paper (11 pp., printed pp. 188–198) was read from the pdftotext extraction. Page images were checked for printed pp. 192 (Table 1), 193 (Sec. 4.1 text), 194 (Table 2 and the retrieval text), 195 (Tables 3–4) and 196 (Table 5). Every number below gives its table/section and printed page. Numbers computed by us are marked **[computed]** and were recomputed with Python.
**Source rule:** **the paper is the primary and only authoritative source.** The web was used only to check the bibliographic record (ACL Anthology). No code repository, dataset card or later paper was used to describe what the authors did.
**Verification:** independent AI verifier pass 2026-09-28; 8 findings addressed.
**Reliability:** **B** (proposed). The paper is peer-reviewed and appears in an ACL workshop proceedings volume (LAW-XVII; bibliographic check: ACL Anthology). Retrieval is only a secondary baseline section in a dataset paper: the BM25 configuration, the pool size and the question set of Table 4 are not reported, and there are no significance tests. The researcher may upgrade the record to A- if workshop papers are treated as equivalent to main ACL venues.

---

## Кратко для исследователя (RU)

- **Что сделано.** Создан венгерский QA-бенчмарк MILQA: 23 708 вопросов (16 992 с ответом, 6 716 без ответа) по 142 статьям венгерской Википедии (Table 1, p. 192). Устроен в духе SQuAD 2.0, дополнительно есть yes/no-вопросы, списочные, длинные и неэкстрактивные ответы. Для поиска параграфов и для извлечения ответа (reader) даны базовые модели.
- **Морфологические варианты лексического канала есть:** BM25 в Elasticsearch в четырёх вариантах (Table 2, p. 194). Base: без лемматизации. PoS: из запроса убираются вопросительные слова по частеречному фильтру. Lemma: лемматизация HuSpaCy. PoSLemma: оба приёма. **Стемминга нет.**
- **Главные числа** (Table 2; критерий «найден именно золотой параграф»):
  - R@1: 0.438 (Base), 0.647 (Lemma), 0.656 (PoSLemma);
  - MRR@300: 0.538 → 0.740 → 0.748;
  - R@300: 0.896 → 0.984 (доля пропущенных в топ-300 падает с 10.4% до 1.6% **[computed]**).
  - Лемматизация даёт основной выигрыш (+0.209 R@1 абсолютно, +47.7% относительно **[computed]**). PoS-фильтр добавляет около 0.01. Без лемматизации он немного снижает R@300 (0.896 → 0.878), с лемматизацией R@300 не меняется (0.984).
- **Плотный поиск есть, но слабый и в неравных условиях** (Table 4, p. 195). Пять готовых моделей; обучение ретриверов на MILQA не описано, то есть они, по всей видимости, использованы без дообучения (zero-shot, **[inferred]**, в статье так не названо): английская QA-модель mpnet, многоязычные paraphrase/USE-модели и многоязычный DPR. Их сравнивают с **нелемматизированным** BM25 из Haystack:
  - BM25: R@10 0.817, MRR@10 0.626;
  - лучшая плотная модель (distiluse-v2): 0.589 / 0.326;
  - DPR: 0.281 / 0.123.
  - Лемматизированный BM25 с плотными моделями **напрямую не сравнивался**.
- **Нет гибрида и анализа взаимодополняемости:** нет fusion, нет перекрытия и уникально найденных параграфов, нет oracle union, нет разбора по запросам или типам вопросов. Статистических тестов нет, хотя в тексте несколько раз сказано «significantly».
- **Два разных критерия релевантности.** Table 2 считает попадание только в золотой параграф. Tables 3–4 засчитывают любой результат, где ответ встречается «в точности» (p. 194). Поэтому числа Table 2 и Tables 3–4 напрямую не сравнимы. Конфигурация BM25 в Table 3, параметры k1/b, анализатор Elasticsearch и размер пула параграфов в статье не указаны (NOT_REPORTED).
- **Внутренние несоответствия:**
  - в Table 1 и Sec. 3.2 доля yes/no-вопросов указана как 9.20%, а 1621/16992 = 9.54% **[computed]**; все остальные доли подтипов пересчитываются точно;
  - пул расширен «30 fold» добавлением 4927 статей, но (142+4927)/142 = 35.7× **[computed]**, если считать в статьях;
  - напряжение (не доказанное противоречие): в Sec. 3 сказано, что вопросы перефразированы и «in most cases the answer cannot be found using a lexical search», однако лемматизированный BM25 ставит золотой *параграф* на первое место примерно в 65% случаев (R@1 0.647–0.656). Фраза авторов может относиться к поиску самого *ответа*, а не параграфа, поэтому это не обязательно несоответствие (§19.3).
- **Для нашего gap:** работа подтверждает уже зафиксированные не-утверждения v0.8 («raw vs lemma BM25 в морфологически богатом агглютинативном языке уже сравнивали»; «BM25 vs dense уже сравнивали»). Ядро v0.8 (raw/stem/lemma × фиксированный D → overlap/unique hits → прирост гибрида → признаки запроса) **не затрагивает**. Предложение: gap не менять.
- **Практическая польза для нас:**
  1. В агглютинативном языке переход raw → lemma может менять лексический канал очень сильно (R@1 +0.21), так что изменение взаимодополняемости с D вполне правдоподобно и измеримо.
  2. Фильтр вопросительных слов в запросе полезен как простой контроль (`BM25_simple-normalization`) для узбекских вопросов (nima, qachon, qaysi, -mi).
  3. Критерий релевантности, единица поиска (параграф/секция/статья) и размер пула сильно меняют числа (Table 3). Их нужно фиксировать для всех условий.
  4. MILQA публично доступна (footnote 1): это дешёвый пилот нашего протокола overlap/unique hits на агглютинативном языке (raw/lemma BM25 × современный D).

---

## 1. Bibliographic record

- **Authors:** Attila Novák, Borbála Novák (Pázmány Péter Catholic University, Faculty of Information Technology and Bionics, Budapest); Tamás Zombori, Gergő Szabó, Zsolt Szántó, Richárd Farkas (University of Szeged, Institute of Informatics) (p. 188)
- **Year:** 2023
- **Venue:** *Proceedings of the 17th Linguistic Annotation Workshop (LAW-XVII)*, pages 188–198, July 13, 2023 (p. 188 footer)
- **Editors / place / publisher:** Jakob Prange, Annemarie Friedrich; Toronto, Canada; Association for Computational Linguistics (bibliographic check: ACL Anthology)
- **ACL Anthology ID:** `2023.law-1.19` (bibliographic check: ACL Anthology)
- **DOI:** `10.18653/v1/2023.law-1.19` (bibliographic check: ACL Anthology)
- **Official record:** https://aclanthology.org/2023.law-1.19/
- **Data / models (stated in paper, footnote 1, p. 188):** "The dataset and trained models can be found on GitHub and the Hugging Face Model Hub searching for the term MILQA." No URL is given.
- **Funding:** grant FK 125217 of the National Research, Development and Innovation Office of Hungary, FK 17 funding scheme; RRF-2.3.1-21-2022-00004, Artificial Intelligence National Laboratory Program (Acknowledgements, p. 196)
- **Source type:** peer-reviewed workshop paper (dataset / resource paper with baseline experiments)
- **Reliability:** B (see header)
- **Full text available:** yes (`07_full_text/pdfs/CR000073.pdf`, 11 pages)

## 2. Why this work matters to the PhD

It is a peer-reviewed study in an **agglutinative, case-marking language**. The paper calls Hungarian "a morphologically rich language" (p. 193) and "a niche agglutinating language" (p. 196). In one setting it:

- compares **surface-form BM25 with lemmatized BM25**, together with a query-side PoS (part-of-speech) filter;
- compares **BM25 with dense / embedding retrievers**.

| Axis | Relation |
|---|---|
| Lexical retrieval | BM25 (Elasticsearch) in a 2×2 design: lemmatization {no, yes} × query wh-word PoS filter {no, yes}. A second BM25 implementation (Haystack, no lemmatization) is used against the dense models |
| Semantic retrieval | Five off-the-shelf models, sentence-transformers and multilingual DPR. No retriever training on MILQA is described, so they were apparently used zero-shot **[inferred]**. None is trained for Hungarian retrieval |
| Hybrid retrieval | **Absent** |
| Uzbek morphology | Indirect. Context (not from the paper): Hungarian is Uralic, agglutinative and suffixing, with rich case marking, so it is typologically closer to Uzbek than Semitic Amharic is. It is not Turkic |
| Low-resource retrieval | Moderate: the authors state that no dense model "specifically trained for Hungarian" exists (p. 194) |
| Current gap | It gives evidence for the already-occupied components (raw vs lemma BM25; BM25 vs dense). It does **not** touch the morphology → complementarity interaction (§16) |

## 3. Research problem

### Simple explanation

There was no public Hungarian dataset for training and testing question-answering (QA) systems. The authors built one. As a baseline they also asked two retrieval questions:

- Does reducing Hungarian words to their dictionary form (lemmatization) help a word-matching search engine find the paragraph that answers a question?
- Do ready-made neural embedding models find it better than word matching?

### Formal formulation

- Primary contribution: construction and description of MILQA, an extractive (plus partly generative-ready) Hungarian QA benchmark following SQuAD 2.0 principles with additional question types (Sec. 3, pp. 191–193).
- Retrieval sub-task (Sec. 4.1, pp. 193–194): given a question `q` and a pool of passages `P`, rank `P`. Hits are defined in two ways:
  - Table 2: hit = the gold paragraph;
  - Tables 3–4: hit = any passage in which the gold answer string occurs exactly.
- Stated research question for the lexical part (p. 193): "to what extent traditional preprocessing steps like lemmatization or part-of-speech-based term filtering can improve retrieval performance."
- Reader sub-task (Sec. 4.2): answer-span extraction, F1 / exact match. It is outside the gap and summarised only briefly here.

## 4. Main idea

### Simple explanation

Build the dataset by letting annotators read Wikipedia paragraphs and write questions about them. Then search for each question's paragraph among all dataset paragraphs:

1. with BM25 on words as written;
2. with BM25 on lemmas;
3. with or without removing question words from the query;
4. with several neural embedding models.

### Concrete example

- The paper's own morphology example (Sec. 1, p. 190): context *Péternek az idegeire ment a zaj* "The noise got on Peter's nerves". Here *Péter* is in the dative case (*Péternek*). The question is *Kit idegesített a zaj?* "Who was annoyed by the noise?". The adequate answer is *Pétert*, in the accusative case.
- In retrieval terms (our illustration, **not** from the paper): the same lexeme appears in different case forms (*Péter-nek*, *Péter-t*), so surface-form BM25 does not match them, while lemmatized BM25 maps both to *Péter*.

### Formal method

- BM25 scoring (Robertson & Zaragoza 2009, cited p. 193) over index terms produced by one of four preprocessing configurations (Table 2).
- The dense models score by vector similarity between question and passage embeddings. For DPR, there are separate question and context encoders (p. 194).

## 5. Architecture / algorithm

1. **Lexical retrieval, own implementation** (Sec. 4.1, pp. 193–194):
   - BM25 "using Elasticsearch".
   - Preprocessing uses "components of the HuSpaCy library" (Orosz et al. 2022; Szabó et al. 2023).
   - Configurations (Table 2 caption):
     - **Base:** no lemmatization, no filter;
     - **PoS:** "applying a simple PoS-based filter to eliminate wh-words from the query";
     - **Lemma:** "applying lemmatization";
     - **PoSLemma:** both.
   - NOT_REPORTED:
     - whether lemmatization was applied to both documents and queries (implied, but not stated);
     - the Elasticsearch analyzer / tokenizer for Base;
     - lowercasing and stop-words;
     - k1 and b;
     - HuSpaCy model version.
2. **Lexical retrieval, Haystack BM25** (p. 194): used as the lexical reference in Table 4. The paper says only that it "differs from our own in that it does not involve lemmatization". Its backend and parameters are NOT_REPORTED.
3. **Dense / embedding retrievers** (p. 194, Table 4), run through the retrieval engines implemented in Haystack. No retriever training or fine-tuning on MILQA is described, so they were apparently used zero-shot **[inferred]**; the paper uses the label "zero-shot" only for the readers (Table 5):
   - `multi-qa-mpnet-base-dot-v1`: English only, trained on QA data;
   - `paraphrase-multilingual-MiniLM-L12-v2`: multilingual paraphrase;
   - `distiluse-base-multilingual-cased-v1`: "15 lang USE", which by the paper's text "does not cover Hungarian" (p. 194);
   - `distiluse-base-multilingual-cased-v2`: "50+ lang USE";
   - `dpr-(question/ctx)_encoder-bert-base-multilingual`: m-BERT-based DPR.
   - The paper states that the multilingual models "were trained on semantic similarity/paraphrase rather than QA tasks" (p. 194).
4. **Document-granularity experiment** (Table 3, p. 195): the pool contains paragraphs, sections or whole articles, from in-dataset articles only or with 4,927 random Wikipedia articles added. The preprocessing configuration used here is NOT_REPORTED.
5. **Readers** (Sec. 4.2): huBERT and XLM-R models, zero-shot from SQuAD 2.0, fine-tuned on MILQA, and Retro-Reader. Outside our scope.

## 6. Data

- **Dataset:** MILQA (Hungarian QA benchmark), built by the authors.
- **Language / domain:** Hungarian; Wikipedia, restricted to articles marked featured or high quality and ranked by page views 2016–2021 (Sec. 3.1, p. 191).
- **Documents:** 142 articles (Sec. 3.2, p. 192). For each article, the first section plus at most 10 random sections of ≥500 characters. Paragraphs <500 characters were merged, and those >~1200 characters were omitted (pp. 191–192).
- **Number of paragraphs in the retrieval pool: NOT_REPORTED.**
- **Questions** (Table 1, p. 192):
  - 23,708 total: 16,992 answerable (71.67%) and 6,716 unanswerable (28.33%);
  - subtypes of answerable questions: yes-no 1,621; not extractive 4,452 (26.20%); arithmetic 427 (2.51%); list 1,455 (8.56%); not SQuAD-compatible 5,203 (30.62%);
  - tricky unanswerable questions: 629 (9.37% of unanswerable).
  - All subtype ratios recompute exactly **[computed]** except yes-no: printed 9.20%, but 1,621/16,992 = 9.54% **[computed]** (see §19).
- **Question word distribution** (p. 193): subject >17%, dates/times >10%, reasons >8%, quantities >7%, places ~7%.
- **Annotation:**
  - five annotators; Label Studio 1.4; ~85 s per question (p. 192);
  - annotators chose articles "based on their personal interests" (p. 191);
  - questions were written *while looking at the paragraph*. The paper states: "when formulating the questions, we paraphrased the original text, so in most cases the answer cannot be found using a lexical search" (Sec. 3, p. 191).
- **Test/tuning split:**
  - 2,391 questions (1,751 answerable) from 36 articles, "roughly 10% of the corpus" (p. 192);
  - by questions this is 10.1%, by articles 25.4% **[computed]**;
  - this part was annotated twice independently; inter-annotator agreement is NOT_REPORTED.
- **Relevance for retrieval:**
  - Table 2: one gold paragraph per answerable question (the paragraph the question was written from), evaluated "on all answerable questions" (caption). This implies 16,992 queries **[inferred from Table 1; not stated as a number]**. Retrieval is therefore evaluated on the whole dataset, not only on the test split. That is unproblematic for BM25 and for the dense models, for which no training on MILQA is described **[inferred zero-shot]**.
  - Tables 3–4: a hit is any result containing the gold answer "exactly in the form given in the dataset" (p. 194). The paper states this for "the follow-up retrieval experiments", i.e. those after Table 2. How yes-no and non-extractive answers are handled under this criterion is NOT_REPORTED. The question set for Table 4 is not stated beyond "base in-dataset-passages-only pool".

## 7. Baselines

| Baseline | What it is | Why selected | Fair comparison? |
|---|---|---|---|
| BM25 Base (Elasticsearch) | Surface-form lexical ranking | Reference for the preprocessing experiment | Yes within Table 2: same engine, pool and criterion; only preprocessing changes. The Base analyzer settings are unknown |
| BM25 PoS / Lemma / PoSLemma | Same engine with query wh-word filter and/or HuSpaCy lemmatization | Test of "traditional preprocessing" for a morphologically rich language | Yes (controlled 2×2 within Table 2). No stemming variant |
| Haystack BM25 (no lemmatization) | A second BM25 implementation | Reference for the dense models in the same framework | **Partly.** It is a different implementation from Table 2, with unreported settings. The strongest lexical configuration (PoSLemma) is not compared with the dense models |
| multi-qa-mpnet-base-dot-v1 | English-only QA-trained bi-encoder | QA-trained dense retriever | **No** for Hungarian: English-only model |
| paraphrase-multilingual-MiniLM-L12-v2; distiluse v1/v2 | Multilingual sentence-similarity encoders | "There is no such model specifically trained for Hungarian" (p. 194) | **No** as retrieval baselines: not retrieval-trained; v1 does not cover Hungarian |
| m-BERT DPR | Multilingual DPR question/context encoders | Multilingual QA-retrieval model | Weak: its training data are not reported in the paper; it is not trained on Hungarian retrieval data |

Summary: the dense side is a set of apparently zero-shot **[inferred: no retriever training is described]**, mostly non-retrieval-trained encoders. Context (not from the paper): these are roughly 2019–2021-era models, and modern retrieval-trained multilingual models such as multilingual E5 or BGE-M3 are absent. Most were released after or near the paper's time, so this is not a criticism of the authors, but it limits what the comparison says about present-day dense retrieval.

## 8. Metrics

| Metric | Definition | Simple meaning here | Appropriate? |
|---|---|---|---|
| R@k (k = 1, 3, 4, 5, 10, 300) | "Recall/match with a cutoff at position k" (Table 2 caption). With one gold paragraph, 1 if the gold paragraph is in the top k, averaged over queries (= hit rate / success@k) | "In what share of questions is the right paragraph among the first k?" | Yes for single-target retrieval. R@300 is the candidate-coverage view relevant to hybrids |
| R@k in Tables 3–4 | 1 if any of the top k contains the gold answer string exactly | "Does any retrieved passage contain the answer?" (like DPR top-k accuracy) | Reasonable for a QA pipeline, but more lenient and not comparable with Table 2 |
| MRR@300 / MRR@10 | Mean of 1/r (rank of the first hit) if r ≤ cutoff, else 0 | "How high is the first correct result, on average?" | Yes |
| "@300-w-time" | **Not defined in the paper.** Values are in seconds | Plausibly wall-clock time for the run at depth 300 (our reading) | Efficiency only |
| Reader: F1, EM | Token-overlap F1 and exact match of answer spans | Answer quality | Outside retrieval |

Significance: **no statistical test** is reported. "Significantly" in the text (pp. 193–194) is used descriptively.

## 9. Results

### Table 2: effect of preprocessing on BM25 (p. 194; gold-paragraph criterion; all answerable questions; pool = all dataset paragraphs)

| Preprocessing | R@1 | R@3 | R@4 | R@5 | R@10 | R@300 | MRR@300 | @300-w-time |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Base | 0.438 | 0.595 | 0.627 | 0.655 | 0.729 | 0.896 | 0.538 | 466.17 s |
| PoS | 0.448 | 0.603 | 0.636 | 0.665 | 0.741 | 0.878 | 0.547 | 262.25 s |
| Lemma | 0.647 | 0.807 | 0.835 | 0.858 | 0.908 | 0.984 | 0.740 | 505.53 s |
| PoSLemma | 0.656 | 0.814 | 0.844 | 0.866 | 0.916 | 0.984 | 0.748 | 385.31 s |

(No bold in the printed table; PoSLemma is best on every recall/MRR column, tied with Lemma on R@300.)

Derived **[computed]**:
- **Lemma vs Base:** R@1 +0.209 (+47.7% relative); R@10 +0.179 (+24.6%); R@300 +0.088 (+9.8%); MRR@300 +0.202 (+37.5%).
- **PoSLemma vs Base:** R@1 +0.218 (+49.8%); MRR@300 +0.210 (+39.0%).
- **PoS filter:**
  - on top of Lemma it adds only +0.007 to +0.009 on R@1–R@10 and MRR, and nothing on R@300;
  - on top of Base it gives about +0.01 at the top ranks but **lowers R@300** (0.896 → 0.878, −0.018).
- **Misses in the top 300:** 10.4% of questions (Base) vs 1.6% (Lemma / PoSLemma). **Misses in the top 10:** 27.1% (Base) vs 9.2% (Lemma), a 66% reduction, or 8.4% (PoSLemma).
- Timing: the PoS filter reduces the time column (Base 466 s → PoS 262 s, ×0.56). Lemmatization increases it slightly (505 s).

### Table 3: document entity type and pool size (p. 195; answer-string criterion; all answerable questions)

| Pool | Unit | R@1 | R@3 | R@4 | R@5 | R@10 | R@300 | MRR@300 | @300-w-time |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| In-dataset articles only | Base (in-dataset paragraphs only) | 0.662 | 0.816 | 0.846 | 0.868 | 0.919 | 0.984 | 0.753 | 453.48 s |
| | Paragraphs (all paragraphs of the articles) | 0.475 | 0.621 | 0.651 | 0.675 | 0.736 | 0.872 | 0.567 | 502.12 s |
| | Sections | 0.577 | 0.741 | 0.772 | 0.791 | 0.837 | 0.896 | 0.671 | 839.22 s |
| | Articles | 0.824 | 0.879 | 0.885 | 0.888 | 0.896 | – | – | – |
| + 4,927 random articles | Paragraphs | 0.412 | 0.562 | 0.593 | 0.618 | 0.682 | 0.860 | 0.506 | 486.17 s |
| | Sections | 0.485 | 0.664 | 0.704 | 0.729 | 0.792 | 0.891 | 0.593 | 708.12 s |
| | Articles | 0.617 | 0.733 | 0.754 | 0.768 | 0.804 | 0.904 | 0.686 | 20188.95 s |

Reading the table:
- The preprocessing configuration of Table 3 is NOT_REPORTED. The Base row (0.662 / 0.919 / 0.984 / 0.753) is close to, but not identical with, Table 2 PoSLemma (0.656 / 0.916 / 0.984 / 0.748). It is also close to Table 2 Lemma (0.647 / 0.908 / 0.984 / 0.740). The row is consistent with either Lemma or PoSLemma under the more lenient answer-string criterion **[inferred, not stated]**.
- Adding all (non-selected) paragraphs of the same articles lowers R@1 from 0.662 to 0.475. Adding ~4.9K distractor articles lowers paragraph-level R@1 further to 0.412 (−0.063) and MRR@300 to 0.506 (−0.061) **[computed]**.
- For the in-dataset article pool, "–" at @300 is plausibly because the pool has only 142 articles, fewer than 300 **[inferred]**.
- Text: "we increased the size of the document pool 30 fold by adding further 4927 randomly selected Wikipedia articles" (p. 194). In articles, (142 + 4,927)/142 = 35.7× **[computed]**. The paper may count in another unit; see §19.

### Table 4: dense / embedding models vs Haystack BM25 (p. 195; base in-dataset-passages-only pool; answer-string criterion, stated for "the follow-up retrieval experiments" after Table 2, p. 194)

| Model | Lang/training (as printed) | R@10 | MRR@10 |
|---|---|---:|---:|
| haystack BM25 (no lemmatization, p. 194) | – | **0.817** | **0.626** |
| multi-qa-mpnet-base-dot-v1 | English only QA | 0.483 | 0.285 |
| paraphrase-multilingual-MiniLM-L12-v2 | multiling. paraphrase | 0.566 | 0.315 |
| distiluse-base-multilingual-cased-v1 | 15 lang USE | 0.299 | 0.150 |
| distiluse-base-multilingual-cased-v2 | 50+ lang USE | **0.589** | **0.326** |
| dpr-encoder-bert-base-multilingual | m-BERT-based DPR | 0.281 | 0.123 |

- BM25 (without lemmatization) vs the best dense model (distiluse-v2) **[computed]**: +0.228 R@10 (+38.7% relative), +0.300 MRR@10 (+92.0%).
- DPR is weakest (MRR@10 0.123). English-only mpnet (0.285) beats distiluse-v1 (0.150), which does not cover Hungarian. This matches the authors' text (p. 194).
- Cross-reading (not a controlled comparison) **[computed]**: Table 3 Base (own BM25, probably Lemma or PoSLemma **[inferred]**) has R@10 0.919 vs Haystack BM25 (no lemmatization) R@10 0.817, a difference of 0.102. This hints at a lemmatization effect under the answer-string criterion as well, but implementation, configuration and possibly the query set differ.
- **The strongest lexical configuration (lemmatized BM25) was never compared with the dense models in the same table.**

### Table 5: readers (p. 196), brief

- Best short-answer reader: xlmR-large-squad2-RR, F1 0.724 / EM 0.623 (with multispan). The authors call Retro-Reader results "preliminary".
- Best long-answer reader: xlmR-large-squad2-T, F1 0.766 / EM 0.436 (with multispan).
- Outside the gap. It is mentioned only to show that the dataset supports an end-to-end retrieval + reader pipeline.

## 10. Statistical evidence

- **Significance test:** NOT_REPORTED. The claims "improves retrieval performance significantly" (pp. 193–194) and "All embedding-based models performed significantly worse than the simple and fast BM25 model" (p. 194) have no test.
  - The Lemma vs Base differences (+0.2 on R@1 / MRR over an implied ~17K queries) are very large, so the direction is very likely robust.
  - The PoS-filter differences (≈0.01) are not established.
- **Confidence intervals:** NOT_REPORTED.
- **Runs / seeds:** not applicable to BM25 (deterministic). The dense models are used off-the-shelf; one run each is implied.
- **Ablation:** Table 2 is itself a small 2×2 factorial ablation (lemmatization × PoS filter). There is no stemming, no stop-word variant and no BM25 parameter variation.
- **Per-query analysis:** **none.** In particular:
  - no per-question-type retrieval breakdown, although question types are annotated (Table 1);
  - no win/loss analysis between Base and Lemma;
  - no BM25–dense overlap or unique-hit analysis;
  - no oracle union;
  - no query-feature analysis.

## 11. Strengths

- A **controlled surface-form vs lemma BM25 comparison** in an agglutinative, case-marking language. It is clean within Table 2: same engine, pool, queries and criterion, with only preprocessing changed.
- A large query set: all answerable questions, implied ~17K. Context (not from the paper): this is far more than typical TREC-style collections.
- Recall is reported down to depth 300, which directly shows candidate coverage (10.4% vs 1.6% misses).
- The granularity and pool-size experiment (Table 3) shows how strongly the retrieval unit and the distractor volume change the numbers.
- Human-written questions with rich type annotation (yes/no, list, arithmetic, non-extractive, tricky unanswerable). These could support per-question-type retrieval analysis in future work.
- Public release of the dataset and models is stated (footnote 1).

## 12. Limitations

### Stated by the authors

- The resource "is also very limited in extent compared to similar English resources both concerning size and the number of parallel annotations" (Limitations, p. 196).
- The baseline experiments do not tackle multispan answers, counting or arithmetic questions, or generative answering (p. 196).
- The reader models "do not currently properly handle multispan answers" (Sec. 4.2, p. 194).
- Retro-Reader training and evaluation are "in progress"; its results are preliminary (p. 195).
- They note an unexplained drop in EM after fine-tuning: "We need to investigate why this happened" (p. 195).
- No dense model "specifically trained for Hungarian" was available (p. 194).

### Inferred from the experimental design

1. **Lexical-overlap bias of the queries.** Annotators wrote each question while reading its paragraph. The authors say they paraphrased, but the high lemmatized BM25 scores (R@1 0.656) suggest substantial lexical overlap remained. This setting favours BM25 over dense models; the size of the bias is unknown.
2. **Weak and mismatched dense comparators.** All appear to be zero-shot: no retriever training is described. Most are not retrieval-trained (paraphrase/USE), one is English-only and one does not cover Hungarian. The result "BM25 > all dense" therefore says little about modern retrieval-trained multilingual dense retrievers.
3. **Dense models are compared only with non-lemmatized Haystack BM25,** not with the best lexical configuration. This is a separate implementation with unreported settings.
4. **Two relevance criteria** (gold paragraph vs answer-string match) and at least two BM25 implementations are used across tables. The Table 3 configuration and the Table 4 question set are not stated. Cross-table comparisons are therefore only indicative.
5. **Single gold paragraph per question** (Table 2). Other paragraphs that also answer the question count as misses. This is known-item-style evaluation, not pooled ad hoc qrels.
6. **Underspecified BM25:** analyzer, lowercasing, stop-words, k1/b and HuSpaCy model version are NOT_REPORTED. It is also not stated whether lemmatization applies to the documents as well as the queries.
7. **No stemming or other normalization variant,** so lemma vs stem cannot be compared.
8. **No significance tests or CIs,** although "significantly" is used.
9. **No per-question-type breakdown of retrieval,** despite the available annotation.

## 13. What the work proves

- In Hungarian paragraph retrieval over MILQA, **lemmatizing the lexical representation strongly improves BM25**. Under the gold-paragraph criterion (Table 2, p. 194):
  - R@1 0.438 → 0.647;
  - MRR@300 0.538 → 0.740;
  - R@300 0.896 → 0.984.
  - Caveat: no significance test is reported, but the effect size and query count make the direction very likely robust.
- A query-side **wh-word PoS filter adds only a small top-rank gain** on top of lemmatization (≈+0.008). Without lemmatization it slightly lowers deep recall (R@300 0.896 → 0.878).
- On this dataset, **non-lemmatized BM25 (Haystack) outperforms five off-the-shelf embedding/DPR models** (apparently used without fine-tuning: no retriever training is described **[inferred]**) by a wide margin (R@10 0.817 vs ≤0.589; MRR@10 0.626 vs ≤0.326; Table 4, p. 195).
- Retrieval effectiveness depends strongly on the **retrieval unit and pool composition** (Table 3). For example, paragraph-level R@1 falls from 0.662 (in-dataset paragraphs) to 0.412 (all paragraphs + 4,927 distractor articles).

## 14. What the work does NOT prove

- **That BM25 beats dense retrieval in Hungarian (or in agglutinative languages) in general.** No retrieval-trained multilingual or Hungarian dense retriever was tested. The queries were written from the gold paragraph, which likely favours lexical matching.
- **That lemmatized BM25 beats dense retrieval.** That pair was never compared directly.
- **Anything about BM25–dense complementarity or hybrid gains.** There is no fusion, no overlap, no unique hits and no oracle union.
- **How lemmatization changes the set of queries or paragraphs that BM25 finds relative to a dense model.** This is exactly the v0.8 core; it is absent.
- **Which questions benefit from lemmatization, or why.** There is no per-query or per-question-type analysis.
- **Lemma vs stem.** No stemming condition.
- **Statistical significance of any difference.** No tests.
- **Generalization** to real user queries, other domains or pooled multi-relevant qrels.

## 15. Relationship to current Uzbek evidence

- **No Uzbek data.**
  - Context (not from the paper): Hungarian and Uzbek are both agglutinative and suffixing, with rich case systems and vowel harmony, but belong to different families (Uralic vs Turkic).
  - The direction of the raw → lemma BM25 effect is plausibly transferable as a hypothesis; the magnitude is not.
- Consistent with the Turkish lexical-IR evidence already in the index:
  - **MORPH-001:** Can et al. 2008, where morphology improves lexical retrieval;
  - **MORPH-002:** Haddad & Bechikh Ali 2014, where BM25 with a Zemberek morphological analyzer is strongest.
  This paper adds a modern (HuSpaCy) lemmatizer, a very large query set and a (weak) dense comparison, but still **no fusion or complementarity**.
- **Contrast with the Amharic card** (Mekonnen et al. 2025, CR000149, proposed MORPH-005) and with **MORPH-004** (Shona). There, dense > BM25. Here, BM25 > dense.
  - The difference is explained by dense-model choice (apparently zero-shot **[inferred]** and non-retrieval-trained here vs in-language fine-tuned there) and by dataset construction, not by language typology.
  - Together they show that "BM25 vs dense" outcomes in morphologically rich languages depend strongly on D and on qrels construction. This supports the v0.8 requirement to **fix and validate D** before comparing lexical variants.
- Like the Uzbek national evidence (e.g., Ishkobilov et al., UZ-IR-001), the lexical and semantic channels are compared as competitors, not integrated.

## 16. Relationship to CURRENT_GAP

**Classification:** *supports* (confirms already-listed non-claims) + *no material effect on the residual core*.

- **Confirms as occupied** (already listed in v0.8 under "Что литература уже не позволяет утверждать"):
  - "raw/stem/lemma ранее не сравнивались в low-resource IR": here raw vs lemma BM25 is compared in an agglutinative language, though without stem;
  - "morphology-aware BM25 не сравнивали с semantic embeddings": only partly. Non-lemmatized BM25 is compared with embeddings, and lemmatized BM25 appears only in another table.
  This paper is a further citation for these boundaries, not a new killer.
- **No material effect on the residual core** of v0.8 refined:
  - raw/stem/lemma BM25 × **fixed** D → change in unique relevant hits / overlap;
  - incremental hybrid gain;
  - link to query features.
  None of these elements is present: no fusion, no overlap, no per-query analysis, and the dense comparator is not fixed across lexical variants.
- **Relevant to gap-killer criterion 3** ("very close work for another agglutinative language"): it does **not** meet it, because the interaction mechanism is not studied.
- **Useful motivation:** a +0.21 R@1 shift from lemmatization shows that the lexical channel's ranked output changes substantially under morphological normalization in an agglutinative language. This makes the question "does this change what BM25 contributes *beyond* D?" non-trivial.

**Proposal:** keep v0.8 refined unchanged. Optionally add this paper to the evidence boundary as an agglutinative-language example of "raw vs lemma BM25 + (weak) BM25 vs dense, without fusion or complementarity analysis". This is a proposal only; `CURRENT_GAP.md` has not been edited.

## 17. Implications for our research design

- **Morphology preprocessing.**
  - Expect a large raw → lemma effect for Uzbek BM25 on annotator-written questions. Plan to measure whether it changes *unique* hits relative to D, not only averages.
  - Include `BM25_stem`, which this paper lacks, so that lemma vs stem can be separated.
- **Query-side control.** Test a simple **question-word / interrogative-particle filter** as a `BM25_simple-normalization`-type control:
  - Uzbek question words and particles: *nima, kim, qachon, qayer(da), qaysi, nega, necha, qancha*, the particle *-mi*;
  - report it separately from lemmatization, because it trades deep recall for top-rank precision (Table 2).
- **Baseline selection / D.**
  - Do not use paraphrase/STS encoders or English-only models as D.
  - D must be retrieval-trained and multilingual (candidate choice per HYB-007 / SEM-011, after an Uzbek pilot) and fixed across `raw/stem/lemma`.
  - Compare D against **each** lexical variant under identical conditions; this paper's key omission is the missing lemma-BM25 vs dense comparison.
- **Dataset / qrels.**
  - QA-derived datasets, where questions are written from a paragraph, carry a lexical-overlap bias favouring BM25. If Uzbek qrels are built this way, record the query-creation procedure and include queries written *without* seeing the target passage.
  - Define one relevance criterion (judged passage/document relevance, not answer-string match) and use it for all channels.
- **Retrieval unit and pool.** Fix the unit (paragraph / document) and the pool, including distractors, for all conditions, and report them. Table 3 shows that unit and pool shift R@1 by >0.2.
- **Query taxonomy.** MILQA's question-type annotation (yes/no, list, arithmetic, non-extractive, wh-type) suggests adding **question type / wh-category** as a candidate query feature, alongside morphological features.
- **Metrics.** Report deep recall (R@100 or deeper) together with MRR/nDCG. The coverage effect of lemmatization (misses 10.4% → 1.6% at k = 300) is what matters for union and fusion.
- **Protocol hygiene.** Report the analyzer, lowercasing, stop-words, lemmatizer version and k1/b for every BM25 run. Use paired significance tests or bootstrap CIs.
- **Pilot option.** MILQA is announced as public (footnote 1). A cheap external pilot of our measurement pipeline would run raw vs lemma BM25 plus one modern multilingual D on MILQA and compute overlap, unique hits and oracle union at k = 10/100 (single-positive caveat as in the Amharic card).

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| Extractive QA | The system answers by highlighting a piece of the given text | Predict start/end positions of the answer span in the context |
| SQuAD 2.0 | English benchmark of Wikipedia paragraphs with questions, some unanswerable | Rajpurkar et al. 2016/2018 |
| Retriever / reader | Retriever finds the passage; reader extracts the answer from it | Two-stage open-domain QA pipeline |
| BM25 | Classic word-matching ranking: rarer shared words and more repetitions give a higher score, with length normalization | Probabilistic relevance framework scoring with parameters k1, b |
| Surface-form (raw) BM25 | BM25 on words exactly as written | Index terms = tokenized word forms |
| Lemmatization | Reducing each word form to its dictionary form (e.g., *Pétert*, *Péternek* → *Péter*) | Mapping tokens to lemmas with a morphological analyzer (here HuSpaCy) |
| PoS-based wh-word filter | Removing question words ("who", "when"…) from the query using part-of-speech tags | Query-side term filtering by PoS tag |
| Dense / embedding retriever | Turns question and passage into one vector each; similar vectors mean relevant | `f(q,p)=sim(Enc(q),Enc(p))` |
| DPR | Dense retriever with two encoders, one for questions and one for passages, trained on QA data | Karpukhin et al. 2020 (SEM-007) |
| Paraphrase / USE encoder | Model trained to tell whether two sentences mean the same, not to find answering passages | Sentence-similarity (STS-style) training objective |
| Zero-shot | Model used as downloaded, without training on this dataset | No task-specific parameter updates |
| R@k (hit@k) | Share of questions whose correct passage is among the first k results | Mean of 1[rank ≤ k] with one target |
| MRR@k | Average of 1/rank of the first correct result, 0 if beyond k | Mean reciprocal rank with cutoff |
| Answer-string hit criterion | Any retrieved passage that contains the answer text counts as correct | Lenient relevance used in open-domain QA |
| Complementarity (project term) | Each channel finds some relevant items the other misses | Unique relevant hits, overlap, oracle-union gain |

## 19. Open questions / verification needed

1. **Yes-no share:** Table 1 and Sec. 3.2 print 9.20%, but 1,621/16,992 = 9.54% (and 1,621/23,708 = 6.84%) **[computed]**. All other subtype ratios recompute exactly. This cannot be resolved from the paper.
2. **Pool size:** "30 fold" (p. 194) vs (142 + 4,927)/142 = 35.7× in articles **[computed]**. The unit of the "30 fold" is unclear, and the number of paragraphs/sections in any pool is NOT_REPORTED.
3. **Paraphrase claim vs results (tension, not an established inconsistency):** Sec. 3 (p. 191) states that "in most cases the answer cannot be found using a lexical search", yet lemmatized BM25 ranks the gold paragraph first for 65.6% of questions (Table 2). The claim concerns finding the *answer*, while Table 2 measures finding the *paragraph*, so the two need not contradict each other; the paper does not clarify.
4. **BM25 configuration:** Elasticsearch analyzer, k1/b, stop-words, lowercasing and HuSpaCy model are NOT_REPORTED. It is also not stated whether lemmatization applies to documents as well as queries.
5. **Table 3 configuration** (which preprocessing?) and the **Table 4 query set**: NOT_REPORTED. The inferred Lemma/PoSLemma configuration for Table 3 is unconfirmed. The answer-string criterion covers Table 4 through the "follow-up retrieval experiments" wording (p. 194), though Table 4 does not restate it.
6. **Meaning of "@300-w-time":** not defined.
7. **Table 4 caption** says "The best model performance is in bold", but two rows are bold (BM25 and distiluse-v2). Presumably these are the overall best and the best vector model; this is minor.
8. **Inter-annotator agreement** on the doubly annotated test/tuning part (2,391 questions): NOT_REPORTED.
9. **Later work** (not checked, source rule): whether the same group later evaluated modern retrieval-trained dense models or fusion on MILQA. It would be worth a targeted search before citing MILQA as having "no dense/hybrid evidence".

## 20. Decision after deep dive

- **Keep current gap?** Yes. v0.8 refined remains valid (§16).
- **Modify gap?** No change proposed. Optionally add this paper to the evidence-boundary list as an agglutinative-language (Hungarian) example of "raw vs lemma BM25 and BM25 vs off-the-shelf embeddings without fusion or complementarity analysis" (researcher's decision).
- **Add decision?** Proposed for `decisions/DECISIONS.md` (researcher's decision):
  - "The fixed D must be compared with *every* lexical variant (raw/stem/lemma) under identical unit, pool, query set and relevance criterion";
  - "Query-construction procedure must be documented; include queries written without viewing the target passage to limit lexical-overlap bias".
- **Add experiment?** Optional low-cost pilot on public MILQA: raw vs lemma (HuSpaCy) BM25 + one modern multilingual D. Compute overlap, unique hits and oracle union at k = 10/100, and break them down by the annotated question types. This tests the measurement pipeline on an agglutinative language before Uzbek qrels exist.
- **Add citation to Chapter I?** Yes, with narrow wording:
  - §1.1: lemmatization effect on BM25 in an agglutinative language;
  - §1.3: example that lexical and embedding retrieval are compared, not integrated, and that dense comparators in such studies are often not retrieval-trained.
- **Proposed `MASTER_INDEX.md` row** (to add after approval):

| MORPH-006 | Novák, Novák, Zombori, Szabó, Szántó, Farkas — *A Question Answering Benchmark Database for Hungarian* (LAW-XVII 2023, pp. 188–198) — [deep dive](deep-dives/2023_Novak_Novak_MILQA_Hungarian_QA_Benchmark.md) | 2023 | B | HIGH | MILQA (23,708 questions, 142 Wikipedia articles). BM25 (Elasticsearch) raw vs HuSpaCy lemma vs wh-word PoS filter: R@1 0.438 → 0.656, MRR@300 0.538 → 0.748, R@300 0.896 → 0.984 (Table 2). Non-lemmatized Haystack BM25 beats five off-the-shelf embedding/DPR models, mostly not retrieval-trained and apparently zero-shot (R@10 0.817 vs ≤ 0.589). No stem variant, no lemma-BM25 vs dense comparison, no fusion, no overlap/unique-hit/per-query analysis, no significance tests. |
