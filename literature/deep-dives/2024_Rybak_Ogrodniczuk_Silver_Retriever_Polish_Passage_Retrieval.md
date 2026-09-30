# Rybak & Ogrodniczuk (2024): Silver Retriever: Advancing Neural Passage Retrieval for Polish Question Answering

**Targeted deep-dive status:** COMPLETED (AI-assisted, pending researcher review)
**Completed:** 2026-09-28
**Literature ID:** `MORPH-007` (assigned 2026-09-28, approved by researcher)
**Systematic-review record:** `CR000100`. Full-text triage: INCLUDE, reading priority HIGH, tier "1 — прямо по теме пробела", `carries_complementarity_evidence = NO`
**Provenance:** AI-assisted deep dive (Claude). The paper (6 printed pages, pp. 14826–14831) was read in full from the pdftotext extraction. Page images of pp. 14827 (Table 1), 14828 (Sections 3.2–4.4, footnote 9) and 14829 (Tables 2–3, Sections 4.4–5) were checked visually, and every table number below was compared against them. Numbers computed by us are marked **[computed]** (recomputed with Python).
**Source rule:** **the paper is the primary and only authoritative source.** The model/dataset/filtering-script links in the paper's footnotes were not opened. The web was used only to verify the bibliographic record (marked "bibliographic check").
**Verification:** independent AI verifier pass 2026-09-28; 10 findings addressed.
**Reliability:** **A** (peer-reviewed main-conference paper, LREC-COLING 2024, ACL Anthology). Caveat: the part that matters most for us (BM25 on word forms vs BM25 on lemmas) is a secondary baseline. It is under-specified (no lemmatizer, BM25 implementation or parameters named) and is reported without significance tests; the number of runs/seeds is not reported (§10, §12).

---

## Кратко для исследователя (RU)

- **Что сделано.** Авторы обучили польский плотный ретривер Silver Retriever: HerBERT Base в архитектуре DPR, обучен на ≈1 млн вопросов из 9 наборов с ручной или «слабой» (автоматической) разметкой. Его сравнили с двумя вариантами BM25 и семью другими нейросетевыми моделями (4 многоязычные + 3 польские) на трёх тестовых наборах: PolQA (вопросы-викторины по Википедии), Allegro FAQ (e-commerce) и Legal Questions (право). Метрики: Acc@10 и NDCG@10 (Table 2, p. 14829).
- **Морфологические варианты лексического канала есть, но только два:** `BM25` (словоформы) и `BM25 (lemma)`. Стемминга нет. Лемматизатор, реализация BM25, токенизация и k1/b **не указаны** (NOT_REPORTED).
- **Главные числа** (Table 2, p. 14829), Acc@10 / NDCG@10, %:
  - PolQA: BM25 61.35 / 24.51 → BM25 (lemma) 71.49 / 31.97; Silver 87.24 / 43.40; E5-Base 86.61 / 46.08.
  - Allegro FAQ: BM25 66.89 / 48.71 → lemma 75.33 / 55.70; Silver 94.56 / 79.66.
  - Legal Questions: BM25 **96.38 / 82.21** (лучший результат среди всех моделей) → lemma 94.57 / 78.65; Silver 95.54 / 77.10.
- **Эффект лемматизации меняет знак в зависимости от набора** **[computed]**: +10.14 / +7.46 п.п. на PolQA, +8.44 / +6.99 п.п. на Allegro FAQ, но −1.81 / −3.56 п.п. на Legal Questions. Это прямой аргумент «не предполагать lemma > raw — измерять».
- **Плотный поиск vs BM25.** В среднем по трём наборам Silver (92.45 / 66.72) и E5-Base (91.58 / 66.56) значительно выше BM25 (lemma) (80.46 / 55.44). На юридических вопросах лексический поиск по словоформам лучше всех нейросетевых моделей. Авторы объясняют это длинными пассажами (>512 токенов) и высоким лексическим перекрытием вопрос–пассаж. Это объяснение не проверено экспериментом.
- **Нет:** гибрида/fusion для оценки; перекрытия результатов BM25 и плотных моделей; уникально найденных пассажей; oracle union; анализа по запросам; тестов значимости и доверительных интервалов; число запусков/seed не указано. Абляция (Table 3) касается только обучения ретривера, а не лексического представления.
- **Важная методическая деталь для qrels** (footnote 9, p. 14828): в исходной разметке PolQA все выдачи BM25 проверялись вручную, а выдачи нейросетевых моделей нет. Авторы прямо предупреждают, что это может завышать результаты BM25. Для нашей задачи смещение пула разметки в пользу одного канала напрямую искажает подсчёт уникальных релевантных документов.
- **Лемматизированный BM25 используется внутри обучения** плотной модели: им подбираются hard negatives (Sec. 3.2) и кандидаты для нового набора 1z10 (Sec. 3.1.2). Значит, плотная модель частично обучена «против» лемма-канала. Это наша интерпретация, в статье она не обсуждается.
- **Внутренние несоответствия** (текст vs Table 2, p. 14829): NDCG E5-Base на Allegro FAQ — 76.02 в тексте и 75.90 в таблице; на Legal — 77.79 и 77.69; средние E5 — 91.63 / 66.63 и 91.58 / 66.56. В Table 1 (p. 14827) итог столбца «Negative questions» равен 823,490, а сумма строк — 990,404 **[computed]**. Утверждение «BM25 лучше LaBSE и MiniLM-L12-v2» на Allegro FAQ верно только для BM25 (lemma).
- **Для нашего gap:** работа — ещё один пример того, что raw vs lemma BM25 и современный плотный поиск уже сравнивались на одних и тех же тестовых наборах морфологически богатого (флективного) языка. Ядро v0.8 (изменение взаимодополняемости с фиксированной D при переходе raw → stem → lemma; уникальные находки, перекрытие, прирост гибрида, признаки запросов) **не затрагивает**. Предложение: gap не менять.
- **Практическая польза для нас:**
  1. Пул для разметки строить из всех каналов (BM25_raw / stem / lemma, D, гибриды) с одинаковой глубиной.
  2. Проверять знак эффекта лемматизации отдельно по доменам и типам запросов.
  3. Не обучать и не дообучать D на hard negatives, найденных одним из лексических вариантов, — иначе сравнение raw / stem / lemma становится несимметричным.
  4. Явно фиксировать лемматизатор, BM25 и поля документа: заголовок в Legal Questions ухудшал все модели.

---

## 1. Bibliographic record

- **Authors:** Piotr Rybak, Maciej Ogrodniczuk
- **Affiliation:** Institute of Computer Science, Polish Academy of Sciences, Warsaw (p. 14826)
- **Year:** 2024
- **Venue:** *Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)*, 20–25 May 2024 (page footer, p. 14826); Torino, Italia (bibliographic check: ACL Anthology)
- **Editors:** Nicoletta Calzolari, Min-Yen Kan, Veronique Hoste, Alessandro Lenci, Sakriani Sakti, Nianwen Xue (bibliographic check: ACL Anthology)
- **Pages:** 14826–14831 (page footer; confirmed by bibliographic check: ACL Anthology)
- **Publisher:** ELRA and ICCL (bibliographic check: ACL Anthology); footer: "© 2024 ELRA Language Resource Association: CC BY-NC 4.0"
- **ACL Anthology ID:** `2024.lrec-main.1291` (bibliographic check: ACL Anthology)
- **DOI:** none listed on the ACL Anthology record (bibliographic check)
- **Official record:** https://aclanthology.org/2024.lrec-main.1291/
- **Preprint:** arXiv:2309.08469 (bibliographic check: web search result only; not compared with the published version)
- **Model / data (stated in paper, footnotes 1–2):** `hf.co/ipipan/silver-retriever-base-v1`; `hf.co/datasets/ipipan/maupqa`; filtering script `github.com/360er0/silver-retriever` (footnote 7); evaluation sets `hf.co/datasets/piotr-rybak/allegro-faq`, `.../legal-questions` (footnotes 10–11). Not consulted.
- **Source type:** peer-reviewed conference paper (resource + model paper)
- **Reliability:** A (see header caveat)
- **Full text available:** yes (`07_full_text/pdfs/CR000100.pdf`, 6 pages)

## 2. Why this work matters to the PhD

It is a compact, modern example of a **morphologically rich, less-resourced European language** (Polish, a fusional Slavic language) in which:

- **two lexical representations**, BM25 over word forms and BM25 over lemmas, and
- **several dense retrievers** (monolingual Polish and multilingual)

are evaluated **on the same test sets with the same metrics**. It also shows the lemma effect **changing sign across datasets**.

| Axis | Relation |
|---|---|
| Lexical retrieval | BM25 (word forms) and BM25 (lemma). Configuration NOT_REPORTED. No stemming variant |
| Semantic retrieval | Main focus: a DPR-type bi-encoder fine-tuned for Polish, compared with 3 Polish and 4 multilingual models |
| Hybrid retrieval | **Absent** in the evaluation. Lemmatized BM25 → cross-encoder cascades are used only to **build training data** (Sec. 3.1.2, 3.2) |
| Uzbek morphology | Indirect: Polish is fusional/inflectional, Uzbek is agglutinative. Both have rich inflection, which motivates lemmatization |
| Low-resource retrieval | Moderate: Polish has few retrieval models (Sec. 2) but large weakly labelled resources (≈1M questions, Table 1) |
| Current gap | Touches the "raw vs lemma BM25 next to modern dense" component (already a non-claim in v0.8). Does **not** touch complementarity structure (§16) |

## 3. Research problem

### Simple explanation

Neural retrievers beat word-matching search in English, but Polish had almost no public neural retrievers. The authors build one from many existing and new, partly automatically labelled, Polish question–passage datasets. They then check whether it beats both older Polish/multilingual models and classic BM25.

### Formal formulation

- Task: first-stage **passage retrieval** for open-domain question answering. Given a question `q` and a passage collection `P`, rank `P` so that at least one relevant passage appears in the top 10.
- No explicit research questions are stated. The implicit claims are in the abstract: "Silver Retriever achieves much better results than other Polish models and is competitive with larger multilingual models" (Abstract, p. 14826).

## 4. Main idea

### Simple explanation

Collect as many Polish question–passage pairs as possible:

- human-labelled sets;
- machine-translated sets;
- LLM-generated questions;
- quiz-show transcripts;
- NLI pairs converted into questions.

Add "hard" wrong answers found by lemmatized BM25, clean noisy pairs, and train a standard dense retriever (DPR) on everything.

### Concrete example

- A PolQA trivia question is encoded as one vector, and every Wikipedia passage as another vector. The top 10 passages by vector similarity are returned.
- **Acc@10 = 1** for this question if any of them is annotated relevant.
- BM25 (lemma) instead reduces the question and passages to lemmas and ranks by term overlap. Different inflected forms of the same word then match.
- The example is illustrative; the paper gives **no worked query example**.

### Formal method

- DPR bi-encoder (Sec. 3.4, p. 14828): "We use a standard dense passage retriever (DPR, Karpukhin et al., 2020) architecture implemented in the Tevatron library". Scoring function, pooling, shared or separate encoders and loss are NOT_REPORTED beyond this citation.
- Context (not from the paper): in DPR, relevance is the dot product of query and passage embeddings, trained with a contrastive loss over positives and negatives.

## 5. Architecture / algorithm

1. **Training data** (Sec. 3.1, Table 1, p. 14827). Four existing and five new datasets:
   - Existing: PolQA (train split), MAUPQA (7 weakly labelled sets), PoQuAD (train split), PolEval 2021 Pairs.
   - New:
     - **1z10**: 333 TV-quiz episodes transcribed with Whisper; question–answer pairs extracted with GPT-3.5; passages matched by spaCy lemmatization + **BM25 top-100** → mMiniLM-L6-v2 cross-encoder rerank → top 5 verified by GPT-3.5.
     - **GPT-3.5-CC / GPT-3.5-Wiki**: generated questions.
     - **Polish MS MARCO**: machine-translated.
     - **Multilingual-NLI**: premise prefixed with "Czy" turned into a question; entailment/contradiction count as relevant.
2. **Hard negatives** (Sec. 3.2, p. 14828): "we lemmatize the questions and the corpus of passages and use the BM25 to select the top 10 candidate passages for each question. Then, we score them using the mMiniLM-L6-v2 cross-encoder and keep only the irrelevant passages." Applied to all datasets except PolQA. The lemmatizer here is not named.
3. **Denoising** (Sec. 3.3):
   - length filters, passages relevant to too many questions, passages too similar to their questions;
   - scoring pairs with **E5-Base** (bi-encoder) and mT5-3B (cross-encoder): relevant pairs scoring < 10% and negative pairs scoring > 90% are removed;
   - a manual blacklist.
   - Result: "we discard 14% of the relevant question-passage pairs".
4. **Training** (Sec. 3.4): fine-tune HerBERT Base in DPR/Tevatron for **15,000 steps, batch size 1,024, lr 2·10⁻⁵**; "We leave the rest of the hyperparameters at their default values". Questions without relevant passages are dropped.
5. **BM25 baselines** (Table 2 only): "BM25" and "BM25 (lemma)". The implementation, tokenizer, lowercasing, stop-words, k1/b and the **lemmatizer used for the evaluation runs** are **NOT_REPORTED**.
   - spaCy is named only for building 1z10 (Sec. 3.1.2).
   - We therefore treat "BM25" as a surface-form lexical configuration and "BM25 (lemma)" as a lemma-level one, **without knowing their exact preprocessing**.
6. **Neural baselines** (Sec. 2, Table 2):
   - multilingual: MiniLM-L12-v2 (paraphrase-multilingual, footnote 3), LaBSE, mContriever-Base, E5-Base;
   - Polish: ST-DistilRoBERTa, ST-MPNet (sentence-similarity models, Dadas 2022), HerBERT-QA (Rybak 2023).
   - Exact E5 checkpoint and any query/passage prefixes: NOT_REPORTED.

## 6. Data

### Evaluation sets (Sec. 4.1–4.3, p. 14828)

| Set | Domain | Size stated | Relevance judgments | Notes |
|---|---|---|---|---|
| PolQA (test split) | Trivia questions, Wikipedia passages | PolQA overall: 7,000 questions, 87,525 manually matched passages (Sec. 3.1.1). **Test-split size NOT_REPORTED** | Human-annotated. The authors use "all passages annotated as relevant (not just those found by human annotators)"; questions without relevant passages are ignored | Footnote 9: original passages "were found either by human annotators or by the BM25. As a result, all BM25 predictions were manually verified which is not the case for other models." The authors warn this "may overestimate the results for the BM25 baselines" |
| Allegro FAQ | E-commerce help (Allegro.com) | 900 questions, 921 help articles | "Each question-passage pair is manually checked and edited if necessary" | Introduced in PolEval 2022 (Kobylinski et al., 2023 = CR000913) |
| Legal Questions | Law (acts of law) | 718 questions, 26,000 passages from >1,000 acts | NOT_REPORTED in this paper | Passage titles ignored "because it degrades performance on all tested models". Introduced in PolEval 2022 |

- Only test sets exist for Allegro FAQ and Legal Questions (Sec. 5). The ablation therefore uses the PolQA validation set.
- Relevance grades (binary or graded) for NDCG: NOT_REPORTED.
- Train/test overlap control (e.g., 1z10 or PolQA-train passages vs PolQA test): NOT_REPORTED. 1z10 uses "a corpus of Wikipedia passages distributed with the PolQA dataset" (Sec. 3.1.2), i.e., the same passage source as the PolQA test.

### Training sets (Table 1, p. 14827; checked visually)

| Dataset | Questions total | Passages total |
|---|---:|---:|
| PolQA | 5,000 | 62,035 |
| MAUPQA | 385,895 | 2,824,978 |
| PoQuAD | 56,588 | 346,052 |
| PolevalPairs2021 | 1,977 | 19,690 |
| 1z10 | 22,835 | 160,850 |
| GPT3.5-CC | 29,591 | 281,679 |
| GPT3.5-Wiki | 29,674 | 145,312 |
| MS MARCO (PL) | 389,987 | 3,422,436 |
| Multilingual-NLI | 100,752 | 811,884 |
| **Total** | **1,022,299** | **8,074,916** |

- Column sums for total questions, positive questions and all passage columns match the printed totals **[computed]**.
- **Inconsistency:** the "Negative" questions column sums to **990,404**, not the printed **823,490** **[computed]**, although the caption says "Total represents the concatenation of all datasets".
- "Five new datasets ... over 500,000 questions" (p. 14826): the five new sets total 572,839 questions **[computed]**, consistent.

## 7. Baselines

| Baseline | What it is | Why selected | Fair comparison? |
|---|---|---|---|
| BM25 | Lexical ranking over word forms | Standard lexical reference | **Partly.** Configuration unreported. On PolQA, qrels were built from a pool that included (unspecified) BM25 output, which favours BM25 (footnote 9) |
| BM25 (lemma) | BM25 over lemmatized text | Rationale NOT_REPORTED. The only author remark (Sec. 4.4) is PolQA-specific: BM25, "especially when using lemmas instead of word forms", achieves "competitive performance on PolQA" | As above. Lemmatizer unknown. The only morphological variant; **no stemming** |
| MiniLM-L12-v2, LaBSE | Multilingual sentence-similarity / translation-pair encoders | Available multilingual models | Yes as reference, but not retrieval-trained in the DPR sense (LaBSE: bilingual pairs, Sec. 2) |
| mContriever-Base, E5-Base | Multilingual retrieval-trained dense models | Strongest available multilingual retrievers | Largely fair as reported: used as released, with no fine-tuning on the paper's Polish training data described. Their own training data (Sec. 2: mContriever "fine-tuned on the MS MARCO dataset"; E5 trained on weakly labelled pairs, then "fine-tuned on labeled datasets") and whether it includes Polish are NOT_REPORTED; the E5 checkpoint is not named. Note: **E5-Base was also used to filter Silver Retriever's training data** (Sec. 3.3) |
| ST-DistilRoBERTa, ST-MPNet | Polish sentence transformers trained on paraphrases | Only Polish sentence encoders | Not retrieval-trained; expected to be weak |
| HerBERT-QA | Previous Polish retriever trained on MAUPQA | Only public Polish neural retriever (Sec. 2) | Yes; the first author's earlier model (Rybak, 2023, single-author) |

- The abstract says Silver Retriever is "competitive with larger multilingual models". Model parameter counts are NOT_REPORTED in the paper.

## 8. Metrics

| Metric | Definition (paper, Sec. 4, p. 14828) | Simple meaning | Appropriate? |
|---|---|---|---|
| Accuracy@10 | "there is at least one relevant passage within the top 10 retrieved passages" | Share of questions for which the top 10 contains *any* correct passage (= success@10 / hit@10) | Suits QA (a reader needs one good passage). Coarse: blind to how many relevant passages are found and to their order |
| NDCG@10 | "the score of each relevant passage within the top 10 retrieved passages depends descendingly on its position" (Järvelin & Kekäläinen, 2002) | Rewards putting relevant passages high; counts several relevant passages | Standard. Relevance grades NOT_REPORTED |

- No recall at deeper cut-offs (e.g., Recall@100), so candidate-coverage for hybrid use cannot be judged.
- Values are percentages.

## 9. Results

### Table 2: passage retrieval, Acc@10 / NDCG@10 (%) on the test splits (p. 14829; checked visually)

| Group | Model | PolQA Acc | PolQA NDCG | Allegro Acc | Allegro NDCG | Legal Acc | Legal NDCG | Avg Acc | Avg NDCG |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Lexical | BM25 | 61.35 | 24.51 | 66.89 | 48.71 | **96.38** | **82.21** | 74.87 | 51.81 |
| Lexical | BM25 (lemma) | 71.49 | 31.97 | 75.33 | 55.70 | 94.57 | 78.65 | 80.46 | 55.44 |
| Multilingual | MiniLM-L12-v2 | 37.24 | 11.93 | 71.67 | 51.25 | 78.97 | 54.44 | 62.62 | 39.21 |
| Multilingual | LaBSE | 46.23 | 15.53 | 67.11 | 46.71 | 81.34 | 56.16 | 64.89 | 39.47 |
| Multilingual | mContriever-Base | 78.66 | 36.30 | 84.44 | 67.38 | 95.82 | 77.42 | 86.31 | 60.37 |
| Multilingual | E5-Base | 86.61 | **46.08** | 91.89 | 75.90 | 96.24 | 77.69 | 91.58 | 66.56 |
| Polish | ST-DistilRoBERTa | 48.43 | 16.73 | 84.89 | 64.39 | 88.02 | 63.76 | 73.78 | 48.29 |
| Polish | ST-MPNet | 56.80 | 21.55 | 86.00 | 65.44 | 87.19 | 62.99 | 76.66 | 49.99 |
| Polish | HerBERT-QA | 75.84 | 32.52 | 85.78 | 63.58 | 91.09 | 66.99 | 84.23 | 54.36 |
| Polish | Silver Retriever | **87.24** | 43.40 | **94.56** | **79.66** | 95.54 | 77.10 | **92.45** | **66.72** |

Bold as printed (highest per column). The "Average" columns equal the mean of the three datasets for every row within ±0.01 rounding (MiniLM Acc 62.63, HerBERT-QA Acc 84.24) **[computed]**.

**Lemma vs word-form BM25** **[computed]**:

| Dataset | ΔAcc@10 (pp) | ΔNDCG@10 (pp) | Relative ΔAcc | Relative ΔNDCG |
|---|---:|---:|---:|---:|
| PolQA | +10.14 | +7.46 | +16.5% | +30.4% |
| Allegro FAQ | +8.44 | +6.99 | +12.6% | +14.4% |
| Legal Questions | −1.81 | −3.56 | −1.9% | −4.3% |
| Average | +5.59 | +3.63 | +7.5% | +7.0% |

- Authors' reading (Sec. 4.4, p. 14828): "The BM25 retrievers, especially when using lemmas instead of word forms, achieve competitive performance on PolQA and outperform many neural models." The Legal Questions reversal is visible in the table but **not discussed** by the authors.

**Lexical vs dense** **[computed]**:

- On PolQA and Allegro FAQ, the best dense model exceeds BM25 (lemma) by a wide margin:
  - Silver − BM25 (lemma): +15.75 / +11.43 pp on PolQA; +19.23 / +23.96 pp on Allegro FAQ.
  - E5 − BM25 (lemma): +15.12 / +14.11 pp on PolQA; +16.56 / +20.20 pp on Allegro FAQ.
- On Legal Questions, word-form BM25 ranks 1st of 10 on both metrics and BM25 (lemma) ranks 2nd on NDCG@10.
  - Silver is −0.84 Acc / −5.11 NDCG pp vs BM25.
  - E5 is −0.14 / −4.52 pp vs BM25.
  - Accuracy is near ceiling for the five best systems (94.57–96.38: BM25, E5-Base, mContriever, Silver, BM25 (lemma)).
- On average NDCG@10, BM25 (lemma) at 55.44 is above the previous Polish retriever HerBERT-QA (54.36) and all non-retrieval-trained encoders.
- Authors' explanation for Legal Questions (Sec. 4.4, p. 14829): "This is not surprising since the passage length is often longer than 512 tokens and there is a high lexical overlap between questions and passages." This is **not tested** (no length or overlap analysis).

**Silver Retriever vs E5-Base** **[computed]**:

| Dataset | ΔAcc@10 (pp) | ΔNDCG@10 (pp) |
|---|---:|---:|
| PolQA | +0.63 | −2.68 |
| Allegro FAQ | +2.67 | +3.76 |
| Legal Questions | −0.70 | −0.59 |
| Average | +0.87 | +0.16 |

No significance test is reported. The average advantage over E5 (+0.16 NDCG pp) is small.

**Text vs Table 2 discrepancies** (all on p. 14829):

| Item | Text | Table 2 |
|---|---|---|
| E5-Base NDCG, Allegro FAQ | "79.66% vs 76.02%" | 75.90 |
| E5-Base NDCG, Legal Questions | "96.24% vs 96.38%) but ... much lower NDCG (77.79% vs 82.21%)" | 77.69 |
| E5-Base average | "(91.63% and 66.63% respectively)" | 91.58 / 66.56 |

- Allegro FAQ: "The BM25 performs better than LaBSE, and MiniLM-L12-v2". This holds for **BM25 (lemma)** (75.33 / 55.70). Word-form BM25 (66.89 / 48.71) is **below** MiniLM-L12-v2 on both metrics and below LaBSE on Acc@10.
- None of these changes a ranking conclusion. The text values may come from a different run or version; this cannot be decided from the paper.

### Table 3: ablation on the PolQA validation set (p. 14829; checked visually)

Short training: 5,000 steps, batch 256 (Sec. 5). Rows are cumulative.

| Variant | Acc@10 | NDCG@10 | Δ vs previous row **[computed]** |
|---|---:|---:|---|
| base | 79.09 | 35.51 | — |
| + hard negatives | 79.20 | 36.64 | +0.11 / +1.13 |
| + denoising | 80.89 | 38.28 | +1.69 / +1.64 |
| + batch size of 1024 | **81.31** | **39.13** | +0.42 / +0.85 |

- Text: "Denoising improves both accuracy and NDCG by 1.6 p.p." **[computed: 1.69 / 1.64, consistent]**. Hard negatives: "positive but minimal (probably due to the short training)".
- Minor cross-reference slip: Sec. 5 says "Compared to the main training (see Section 3.3)", but training is described in Sec. 3.4 (3.3 is Denoising).

## 10. Statistical evidence

- **Significance tests:** NOT_REPORTED. No p-values anywhere.
- **Confidence intervals:** NOT_REPORTED.
- **Runs / seeds:** NOT_REPORTED; apparently single runs.
- **Ablation:** Table 3 covers training choices (hard negatives, denoising, batch size), cumulative and on validation only. There is **no ablation of the lexical representation** beyond the two BM25 rows, and no ablation of the training-data mixture.
- **Per-query analysis:** **none.** No per-query wins/losses between BM25 variants or between BM25 and dense; no overlap or unique-hit analysis; no oracle union; no query-feature breakdown; no error examples.
- Context (our note): from aggregate Acc@10 alone, the oracle-union Acc@10 of two systems is only bounded between max(a, b) and min(100, a + b), a range too wide to infer complementarity from Table 2.

## 11. Strengths

- Two lexical representations (word forms, lemmas) and ten systems on **identical test sets and metrics**, over three domains.
- Honest note on qrels pooling bias favouring BM25 on PolQA (footnote 9).
- Domain diversity exposes the **sign change** of the lemma effect and a domain (legal) where lexical retrieval beats every dense model.
- Strong multilingual retrieval-trained baselines (mContriever, E5) are included.
- Model, data and filtering scripts released (footnotes 1, 2, 7, 10, 11).
- The ablation is on a validation split, not the test split (Sec. 5).

## 12. Limitations

### Stated by the authors

- PolQA evaluation with all annotated passages "may overestimate the results for the BM25 baselines", because only BM25 predictions were fully verified in the original annotation (Sec. 4.1, footnote 9).
- Legal Questions: passages are often longer than 512 tokens and lexical overlap is high (Sec. 4.4). Offered as the reason BM25 wins; not framed as a limitation of the dense models' setup.
- Ablation only on PolQA because the other two sets have no validation split (Sec. 5); short training may understate the hard-negative effect.
- No explicit Limitations section.

### Inferred from the experimental design

1. **BM25 is under-specified.** The lemmatizer, implementation, tokenization, stop-words and k1/b are not reported for either BM25 row. The lemma-vs-raw difference cannot be attributed to lemmatization alone, and it cannot be reproduced from the paper.
2. **Only two morphological levels.** There is no stemming and no alternative lemmatizer, so the paper cannot tell whether lemmatization or any conflation helps.
3. **Qrels favour BM25 on PolQA; which BM25 is unknown.** If the original pool used one BM25 variant, the raw-vs-lemma comparison on PolQA may also be biased. The paper does not say which.
4. **Dense–lexical coupling in training.** Lemmatized BM25 supplies hard negatives (Sec. 3.2) and candidate passages for 1z10 (Sec. 3.1.2). Silver Retriever is therefore trained partly on the lemma channel's errors. Its comparison with BM25 (lemma) is not independent of that channel.
5. **Baseline also used as a filter.** E5-Base scores were used to denoise Silver Retriever's training data (Sec. 3.3), and E5-Base is the closest competitor.
6. **No significance testing** despite small differences (e.g., Silver vs E5 +0.16 average NDCG pp; Legal Questions differences within 2 pp Acc).
7. **Acc@10 is coarse and near ceiling on Legal Questions** (94.57–96.38 for five systems). No deeper recall is reported.
8. **Possible train–test proximity on PolQA:** training uses the PolQA train split plus 1z10 matched against the same PolQA passage corpus. Deduplication against the PolQA test set is NOT_REPORTED.
9. **Test-set sizes partly unreported** (PolQA test), and Legal Questions relevance-annotation procedure NOT_REPORTED here.
10. **Text–table inconsistencies** (§9) and the Table 1 negative-question total.

## 13. What the work proves

- On three Polish passage-retrieval test sets, **BM25 over lemmas outperforms BM25 over word forms on PolQA and Allegro FAQ** (+10.14 / +8.44 Acc@10 pp) **and underperforms it on Legal Questions** (−1.81 Acc@10, −3.56 NDCG@10 pp) (Table 2) **[computed]**. The benefit of lemmatization for BM25 is dataset-dependent. The configuration is unknown and no significance test is reported, so the size of the Legal Questions reversal is uncertain; its direction is consistent across both metrics. The PolQA gain carries an extra caveat: the authors warn that PolQA qrels favour BM25 because only BM25 predictions were fully verified (Sec. 4.1, footnote 9, p. 14828), and which BM25 variant formed that pool is not stated, so the raw-vs-lemma contrast on PolQA may also be affected (§12, item 3).
- **Retrieval-trained dense models (Silver Retriever, E5-Base) outperform both BM25 variants by large margins on trivia QA and e-commerce FAQ** (≥ +15 Acc@10 pp over BM25 (lemma)), but **not on legal questions**. There, word-form BM25 has the highest scores of all ten systems (Table 2).
- A Polish DPR model trained on ≈1M mostly weakly labelled pairs reaches the **best average scores** (92.45 / 66.72). It is essentially tied with multilingual E5-Base on average (+0.87 / +0.16 pp, untested) and clearly above earlier Polish models (Table 2).
- Encoders not described as retrieval-trained (ST-* "trained for sentence similarity" and LaBSE trained on translation pairs, Sec. 2; MiniLM-L12-v2 identified only by its paraphrase-multilingual checkpoint name, footnote 3) are often worse than BM25 (lemma) (Table 2).
- In a short-training ablation, denoising gives the largest step (+1.69 / +1.64 pp) (Table 3).

## 14. What the work does NOT prove

- **Anything about lexical–dense complementarity.** There is no fusion, overlap, unique-hit, oracle-union or per-query analysis. Legal Questions, where BM25 wins, *suggests* the channels may fail on different queries, but this is not measured.
- **How lemmatization changes the relation between BM25 and a dense model** (the v0.8 core). Only aggregate scores of each system are reported.
- **Why the lemma effect reverses on Legal Questions.** No query- or passage-level analysis; the length/overlap explanation is offered for BM25-vs-dense, not for raw-vs-lemma.
- **That lemmatization beats stemming or other normalization.** Neither was tested.
- **That Silver Retriever is significantly better than E5-Base.** No tests; the average difference is small.
- **That dense retrieval is weaker on long legal passages because of truncation.** Plausible, but not tested (no chunking experiment).
- **Unbiased absolute BM25 scores on PolQA.** The authors themselves flag the pooling bias.

## 15. Relationship to current Uzbek evidence

- **No Uzbek data.** Polish is fusional/Slavic and Uzbek agglutinative/Turkic, so the lemma effect sizes do not transfer. The *pattern* does transfer: normalization helps in some collections and hurts in others. This matches Can et al. 2008 (MORPH-001: "do not assume lemma > stem > raw") and Haddad & Bechikh Ali 2014 (MORPH-002: preprocessing effects depend on model and metric).
- The legal-domain finding (BM25 ≥ dense) is relevant to Uzbek legal-retrieval work in our corpus: USHRA / O-RAG (UZ-HYB-001/002), the Sharifbaev manuscript (UNVER-002) and Aboasal et al. (HYB-011). Before assuming that dense dominates in legal text, a strong BM25 baseline must be run.
- Like Mekonnen et al. (Amharic, proposed MORPH-005) and Munetsi et al. (Shona, MORPH-004), this is a modern paper on a morphologically rich language with BM25 vs dense and no complementarity analysis. Unlike those two, it **does** report a morphological variant (lemma) of BM25.
- **Polish cluster** (relations based only on the triage records of the other works; their full texts were not read for this card):
  - **CR000913** (Kobyliński et al., PolEval 2022/23 overview, FedCSIS 2023): the source of Allegro FAQ and Legal Questions (cited here as Kobylinski et al., 2023). Its participant systems reportedly vary BM25 morphological normalization and combine lexical and dense retrievers, without a controlled comparison (triage note).
  - **CR000914** (Pacanowska, FedCSIS 2023): PolEval 2022 passage retrieval with BM25 without lemmatization and with several lemmatizers (Morfeusz2, spaCy, hybrid) plus neural reranking and score combination (triage note). It likely fills the "which lemmatizer" gap left here and should be read together with this card.
  - **CR000103** (BEIR-PL, Wojtasik et al., LREC-COLING 2024): cited here (Sec. 3.1.2) as the precedent for translating MS MARCO. Per triage: stemmed BM25 (Stempel) vs dense/ColBERT/rerankers, with the weaker Polish BM25 attributed to inflection.
  - Together, the cluster may cover raw / lemma / stem BM25 and dense for Polish, **in separate papers and on partly different test sets**. Whether any of them measures overlap or unique hits must be checked in their own cards.

## 16. Relationship to CURRENT_GAP

**Classification:** *supports (motivation)* + *no material effect on the residual core*.

- **Already occupied, confirmed again.** v0.8 already lists these as non-claims:
  - "raw/stem/lemma ранее не сравнивались в low-resource IR";
  - "morphology-aware BM25 не сравнивали с semantic embeddings".
  This paper is another A-level instance (raw vs lemma BM25 next to retrieval-trained dense models on the same test sets) for a morphologically rich language.
- **Supports the motivation.** The lemma effect changes sign across domains, and BM25 beats all dense models in one domain. Two things follow:
  - the lexical channel's value relative to dense depends on the collection;
  - morphology changes the lexical channel's standing against dense by **aggregate** margins that differ per dataset.
  Whether this reflects a change in *which* relevant passages each channel finds (the v0.8 core) is exactly what aggregate tables cannot show.
- **No material effect on the residual core** (v0.8 refined). The paper has none of these:
  - a controlled raw → stem → lemma change with a fixed D measured by **unique relevant hits / overlap / oracle union**;
  - fusion conditions H_raw / H_lemma;
  - an incremental hybrid gain;
  - a link to query features.
  Its dense model was also trained with lemma-BM25 negatives, so it is not an independent fixed comparator.

**Proposal:** keep v0.8 refined unchanged. Optionally add this paper, with CR000914 and CR000103, to the evidence boundary as the Polish example of "raw vs lemma BM25 + dense on shared test sets, dataset-dependent lemma effect, no complementarity decomposition". This is a proposal only; `CURRENT_GAP.md` has not been edited.

## 17. Implications for our research design

- **Qrels / pooling (most important).**
  - Footnote 9 shows how a pool built from one lexical system inflates that system's scores.
  - For our unique-hit/overlap measurements, pooling bias would directly inflate one channel's "unique" relevant documents.
  - Pool to the same depth from every compared run: BM25_raw, BM25_stem, BM25_lemma, D, and the hybrids.
  - Report judged@k per run, and treat unjudged documents explicitly (e.g., condensed-list metrics as a sensitivity check).
- **Fixed D independence.**
  - Do not train or fine-tune D with hard negatives mined by one lexical variant (as done here with lemma-BM25).
  - If fine-tuning is needed, mine negatives with a neutral method, or with all variants symmetrically, and document it.
  - Otherwise, D is pre-shaped to be complementary to that variant.
- **Morphology baselines.**
  - Include raw and lemma (and stem) and expect the sign to vary by domain/sub-collection.
  - Report the analyzer (name, version, disambiguation policy) and the BM25 implementation with k1/b. This paper shows how a missing configuration blocks interpretation.
- **Domain stratification / query taxonomy.**
  - The legal result suggests adding collection- or query-level features: query–passage lexical overlap, passage length relative to the encoder limit, and domain.
  - Test these per query, not only per dataset.
- **Document representation.**
  - Fix which fields are indexed (the Legal Questions title field hurt every model) and the passage length/chunking.
  - Use identical units for the lexical and dense channels, so that truncation at 512 tokens does not confound the comparison.
- **Metrics.**
  - Success@10 alone is too coarse, and is near ceiling on easy sets.
  - Add Recall@k at depth (e.g., 100) for candidate coverage, and per-query relevant-set measures for overlap/unique hits.
- **Protocol.**
  - Paired significance tests or bootstrap CIs over queries, and multiple seeds for trained models.
  - Separate dev and test splits (this paper had no dev split for two of its three sets).
- **Candidate D.** Multilingual retrieval-trained E5-Base was essentially tied with the best monolingual Polish model. This is weak support for a multilingual retrieval-trained D, but Uzbek pilot validation is still required (see PHD-INT-001).
- **Hypothesis.** No evidence for or against. The dataset-dependent lemma effect makes our per-query decomposition more, not less, necessary.

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| Passage retrieval | Find the text fragment that answers a question in a large collection | First-stage ranking of passages `P` for query `q` |
| BM25 | Classic word-matching score: shared rare words and repetitions raise the score, with length normalization | Probabilistic relevance framework scoring, parameters k1, b |
| Word-form (raw) BM25 | BM25 on words exactly as written | Index terms = surface tokens |
| Lemma BM25 | BM25 after reducing each word to its dictionary form (e.g., Polish *domów* → *dom*) | Index terms = lemmas from a morphological analyzer / lemmatizer |
| Dense retriever / DPR | Encodes question and passage as vectors; closer vectors mean more relevant | Bi-encoder, `sim(E_q(q), E_p(p))`, contrastive training (Karpukhin et al., 2020) |
| Hard negative | A wrong passage that looks very similar to the right one, which makes training harder and more useful | Non-relevant high-scoring candidate, here from lemma-BM25 top-10 filtered by a cross-encoder |
| Cross-encoder | Reads question and passage together to score them; accurate but slow | Joint encoding, used here only for data construction |
| Weak labels ("silver" data) | Labels made automatically (by translation, LLMs, retrieval) rather than by people | Noisy supervision |
| Denoising | Removing training pairs that are probably mislabelled | Heuristic and model-score filtering (Sec. 3.3) |
| Accuracy@10 | Did any correct passage appear in the top 10? | Success@10 / hit@10 |
| NDCG@10 | How high the correct passages are ranked in the top 10 | Normalized discounted cumulative gain at 10 |
| Pooling bias | If only some systems' results were checked by annotators, those systems look better | Incomplete-judgment bias favouring pooled runs |
| Complementarity (project term) | Each channel finds relevant passages the other misses | Unique relevant hits, overlap, oracle-union gain |

## 19. Open questions / verification needed

1. **Which lemmatizer and BM25 implementation/parameters** produced the two BM25 rows of Table 2? NOT_REPORTED. Check whether the released code or CR000914 clarifies this (the latter only as context, not as evidence about this paper).
2. **Which BM25 variant formed the original PolQA annotation pool** (footnote 9)? This matters for the raw-vs-lemma comparison on PolQA. It is not stated in this paper; it may be documented in the PolQA paper (Rybak et al., 2022), which was not read for this card.
3. **Text vs Table 2 values for E5-Base** (76.02 vs 75.90; 77.79 vs 77.69; 91.63 / 66.63 vs 91.58 / 66.56): which are correct? The arXiv version (2309.08469) could be compared bibliographically, but not used to "correct" this paper.
4. **Table 1 negative-question total** (823,490 printed vs 990,404 summed).
5. **PolQA test-set size** and relevance-grade scheme for NDCG: NOT_REPORTED.
6. **Train–test deduplication** between 1z10 / PolQA-train and PolQA-test: NOT_REPORTED.
7. **Low-cost pilot possibility.** The Allegro FAQ and Legal Questions sets and the Silver Retriever model are announced as public. Running our own raw/lemma(/stem) BM25 plus a fixed D on Legal Questions would give a cheap non-Uzbek test of the overlap/unique-hit pipeline on a collection where BM25 is strong. Caveat: Silver Retriever itself is not a neutral D (§12, item 4).
8. Cross-check with CR000913, CR000914 and CR000103 cards for any overlap/fusion numbers before stating that none exist for Polish.

## 20. Decision after deep dive

- **Keep current gap?** Yes; v0.8 refined remains valid (proposal in §16).
- **Modify gap?** No change proposed. Optionally add the Polish cluster (this paper, CR000914, CR000103) to the evidence-boundary list (researcher's decision).
- **Add decision?** Proposed for `decisions/DECISIONS.md` (researcher's decision):
  - "Relevance pools are built to equal depth from every compared lexical variant, D and hybrid run; judged@k per run is reported";
  - "D is not trained/fine-tuned on hard negatives mined by a single lexical variant";
  - "the lemmatizer/stemmer identity and version and the BM25 implementation and k1/b are reported for every lexical run".
- **Add experiment?** Optional pilot on the public Polish Legal Questions / Allegro FAQ sets:
  - raw vs lemma (vs stem) BM25 with one fixed multilingual D;
  - per-query overlap / unique hits / oracle union at k = 10 / 100;
  - purpose: test whether the dataset-dependent lemma effect coincides with a change in complementarity.
- **Add citation to Chapter I?** Yes:
  - §1.1 (morphological normalization of lexical retrieval is collection-dependent: lemma helps on two Polish sets and hurts on the legal set);
  - §1.2 (Polish dense retrievers from weakly labelled data; multilingual E5 ≈ monolingual model);
  - §1.3 (evidence that BM25 can beat dense in legal retrieval and that modern studies stop at aggregate comparisons without complementarity analysis).
- **Proposed `MASTER_INDEX.md` row** (to add after approval):

| MORPH-007 | Rybak & Ogrodniczuk — *Silver Retriever: Advancing Neural Passage Retrieval for Polish Question Answering* (LREC-COLING 2024) — [deep dive](deep-dives/2024_Rybak_Ogrodniczuk_Silver_Retriever_Polish_Passage_Retrieval.md) | 2024 | A | HIGH | Polish BM25 on word forms vs lemmas (configuration and lemmatizer not reported) next to 7 neural baselines and a DPR model trained on ≈1M weakly labelled pairs; Acc@10 / NDCG@10 on PolQA, Allegro FAQ, Legal Questions. Lemma helps on PolQA/Allegro (+10.14 / +8.44 Acc pp) but hurts on Legal (−1.81 / −3.56 pp); word-form BM25 beats all dense models on Legal (96.38 / 82.21). Silver ≈ E5-Base on average (92.45 / 66.72 vs 91.58 / 66.56). PolQA qrels favour BM25 (authors' footnote 9). Dense trained with lemma-BM25 hard negatives. No stem, no fusion, no overlap/unique-hit/per-query analysis, no significance tests. |
