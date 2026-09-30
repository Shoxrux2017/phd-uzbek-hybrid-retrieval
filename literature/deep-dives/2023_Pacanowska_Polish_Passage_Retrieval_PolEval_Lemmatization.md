# Pacanowska (2023): Passage Retrieval in Question Answering Systems in Polish Language

**Targeted deep-dive status:** COMPLETED (AI-assisted, pending researcher review)
**Completed:** 2026-09-28
**Literature ID:** `MORPH-016` (assigned 2026-09-28, approved by researcher)
**Systematic-review record:** `CR000914`. Full-text triage: INCLUDE, reading priority HIGH, tier 1, `carries_complementarity_evidence = NO`
**Provenance:** AI-assisted deep dive (Claude). The whole paper (6 pages, pp. 1281–1286) was read from the pdftotext extraction and checked against page images. Pages viewed visually: pp. 1281, 1283, 1285, 1286 at 110 dpi; Tables II–VII re-rendered at 250 dpi and cropped (Table II/III p. 1283, Table IV p. 1284, Table V p. 1285, Tables VI–VII p. 1286). Every number below comes with its table and printed page. Numbers computed by us are marked **[computed]**.
**Source rule:** **the paper is the primary and only authoritative source.** The code repository named in footnote 2 was **not** consulted. The web was used only to check the bibliographic record (marked "bibliographic check"). Statements about other Polish works come from our own cards / triage records and are labelled as such. Background knowledge appears only as "Context (not from the paper)".
**Reliability:** **B** — published conference-proceedings paper (FedCSIS 2023, ACSIS Vol. 35, DOI printed on p. 1281), but a single-author shared-task system description derived from a master's thesis: single runs, no significance tests, no query counts, and several internal reporting inconsistencies (§9, §19).
**Verification:** independent AI verifier pass 2026-09-28; 9 findings addressed.

---

## Кратко для исследователя (RU)

- **Что сделано.** Описание системы автора для PolEval 2022, Task 3 (поиск пассажей для вопросно-ответной системы, польский язык). Три предметные области: wiki-trivia (обучение и dev только отсюда), legal-questions и allegro-faq (только в тесте). Метрика — NDCG@10 с бинарной релевантностью.
- **Морфологические варианты лексического канала есть**, и это главное для нас. BM25 (Elasticsearch) без лемматизации и с четырьмя лемматизаторами (Table III, dev, p. 1283):
  - без лемматизации 18.62;
  - spaCy 21.41; Morfeusz2 (все леммы) 21.15;
  - hybrid (spaCy выбирает среди лемм Morfeusz2) 24.47;
  - Morfeusz2-freq (самая частотная в корпусе лемма) **25.24** (+6.62 п., +35.6% отн. к «без лемматизации» **[computed]**).
  - **Способ снятия неоднозначности лемм** дал больший эффект (21.15 → 25.24), чем выбор между словарным и нейросетевым лемматизатором (21.15 vs 21.41).
- **Глубина кандидатов** (Table V, p. 1285, обучающая выборка, 14 448 релевантных пассажей **[computed]**): в top-100 BM25 попадает 39.3% релевантных без лемматизации против 54.9% с Morfeusz2-freq; в top-1000 — 57.6% против 76.3% **[computed]**. Это агрегированные счётчики, а не пересечение по запросам.
- **Стемминга нет.** Кроме «словоформа vs лемма» есть ещё BM25 по биграммам (без лемматизации) — только как признак для объединения оценок.
- **Плотного поиска (bi-encoder) нет.** Нейросетевая часть — это **переранжирование** top-100/1000 кандидатов лемматизированного BM25:
  - кросс-энкодер HerBERT (fine-tuned);
  - кросс-энкодер MiniLM (MS MARCO) на тексте, **машинно переведённом на английский** (OPUS-MT);
  - плюс ответы GPT-3 / ChatGPT + DistilBERT.
- **Объединение оценок есть, но это не гибридный поиск в нашем смысле.** Логистическая регрессия объединяет BM25 (леммы), BM25 (словоформы), BM25 (биграммы) и оценки MiniLM внутри каскада «BM25 → переранжирование». Лучшая система (Table IV row 11) дополнительно использует признаки MiniLM по ответам GPT-3 / DistilBERT и глубину переранжирования 1000. Её результат: test-A 62.51, test-B 54.23 против базового BM25 50.38 / 38.84 (Table VI, p. 1286).
  - Добавление BM25-признаков к MiniLM через LR: +1.57 NDCG@10 на test-A (58.19 → 59.76, Table IV rows 4–5) **[computed]**. Вклад по отдельным признакам не разложен.
- **Предметная область меняет картину** (Table VII, p. 1286): на legal лучшая система **хуже** базового BM25 (77.70 vs 81.10; 79.00 vs 80.32). На wiki +18.51 / +18.66, на allegro +20.80 / +19.87 п. **[computed]**. Эффект лемматизации отдельно по областям **не измерялся**: Table III — только wiki-trivia dev.
- **Чего нет:** стемминга, bi-encoder / плотного поиска первого этапа, RRF / объединения ранжированных списков, анализа перекрытия (overlap), уникально найденных релевантных пассажей и oracle union — ни между вариантами лемматизации, ни между BM25 и нейросетью. Нет разбора по запросам (только качественный анализ ошибок), статистических тестов и числа вопросов.
- **Внутренние несоответствия:**
  - базовый BM25 test-A: 50.76 (Table IV) vs 50.38 (Table VI);
  - подпись Table I обещает число вопросов, но его нет;
  - в подписи Table IV дважды «LR-DEV».
- **Неясности и пропуски (не противоречия):**
  - кандидаты для переранжирования берутся из BM25 с «Morfeusz2» (так последовательно во всём тексте), а не из лучшего на dev Morfeusz2-freq; какой именно вариант Morfeusz2 — не уточнено;
  - настройка лемматизации строки «BM25 (k=1.0, b=0.5)» не указана.
- **Для нашего gap:** работа поддерживает мотивацию (выбор морфологического представления сильно меняет эффективность BM25 и полноту кандидатов в морфологически богатом языке) и немного сужает её. Ядро v0.8 (raw/stem/lemma × фиксированная D → overlap / уникальные попадания / прирост гибрида / признаки запросов) **не затронуто**. Предложение: gap не менять.
- **Практическая польза:**
  1. Стратегию снятия неоднозначности лемм (все леммы / первая / самая частотная / контекстная) фиксировать и описывать как часть условия `BM25_lemma`, возможно как под-вариант.
  2. Отчитываться о полноте кандидатов по глубине (Recall@100/1000) для каждого варианта.
  3. Сохранять `BM25_raw` как отдельный сигнал в объединении.
  4. Проверять эффект по предметным областям.
  5. Имена собственные — кандидат в признаки запроса (автор отмечает ошибки лемматизации имён).

---

## 1. Bibliographic record

- **Author:** Anna Pacanowska (no affiliation printed in the byline; Sec. VI says the paper is taken from her master's thesis "written under the direction of dr Paweł Rychlikowski at the University of Wrocław", p. 1286)
- **Year:** 2023
- **Venue:** *Proceedings of the 18th Conference on Computer Science and Intelligence Systems* (FedCSIS 2023), Warsaw, Poland; thematic track "Challenges for Natural Language Processing" (p. 1281 footer)
- **Series:** Annals of Computer Science and Information Systems (ACSIS), Vol. 35, ISSN 2300-5963 (printed, p. 1281)
- **Pages:** 1281–1286
- **DOI:** `10.15439/2023F586` (printed, p. 1281)
- **Editors / publisher / ISBN:** M. Ganzha, L. Maciaszek, M. Paprzycki, D. Ślęzak (eds.); PTI / ACSIS; ISBN 978-83-967447-8-4 (bibliographic check: annals-csis.org/Volume_35/drp/586.html, reached via doi.org redirect, 2026-09-28)
- **IEEE:** "IEEE Catalog Number: CFP2385N-ART ©2023, PTI" printed on p. 1281; systematic-review metadata lists document type "IEEE Conferences". The IEEE Xplore record itself was not checked.
- **Official URL:** https://annals-csis.org/Volume_35/drp/586.html
- **Code (stated, footnote 2):** https://github.com/aniapacanowska/passage-retrieval — not consulted.
- **Source type:** conference paper; shared-task (PolEval 2022, Task 3) system description, derived from a master's thesis
- **Reliability:** B. Peer-review status is not stated on the ACSIS record page (bibliographic check).
- **Full text available:** yes (`07_full_text/pdfs/CR000914.pdf`, 6 pages)

## 2. Why this work matters to the PhD

It is one of the few works in our corpus that reports, **in one language and on one dev set**, BM25 without lemmatization against BM25 with several lemmatizers. It also shows how the **lemma-ambiguity strategy** changes both effectiveness and candidate recall. The lexical scores are then combined with neural relevance scores.

| Axis | Relation |
|---|---|
| Lexical retrieval | Central. Elasticsearch BM25 on word forms, on lemmas (4 lemmatizers) and on word bigrams |
| Semantic retrieval | Partial. Only **cross-encoder reranking** (HerBERT; MiniLM on machine-translated English). **No dense / bi-encoder first-stage retrieval** |
| Hybrid retrieval | Partial. Logistic-regression **score-level fusion** of BM25 features and cross-encoder scores inside a BM25 → rerank cascade. Not a parallel lexical + dense hybrid |
| Uzbek morphology | Indirect. Polish is fusional (Slavic), Uzbek agglutinative (Turkic). The lemma-ambiguity problem (analyzer returns several lemmas) is common to both |
| Low-resource retrieval | Medium. the author "could not find a good model for passage retrieval in Polish" (Sec. III.E, p. 1282); the author uses translate-to-English as a workaround |
| Current gap | Supports the motivation (representation choice matters a lot for BM25). Does not touch the complementarity decomposition (§16) |

## 3. Research problem

### Simple explanation

A question-answering system first has to find the text fragments (passages) that contain the answer. In Polish a word appears in many inflected forms, so a word-matching engine like BM25 misses passages that use another form of the question's words. Lemmatization (reducing each word to its dictionary form) should help, but lemmatizers disagree, and one word form can belong to several lemmas. The author also asks whether neural rerankers trained on Wikipedia-style trivia still work on legal texts and e-commerce FAQs.

### Formal formulation

- **Task** (Sec. II.A, p. 1281): given a Polish question, return the 10 most relevant passages from a domain-specific corpus.
- **Evaluation** (Sec. II.C, p. 1282): mean over questions of NDCG@10 with binary relevance.
- **Generalization constraint:** training and dev data come only from wiki-trivia; legal-questions and allegro-faq appear only in the test sets (Sec. II.A).
- The paper states no formal research questions. Its implicit questions:
  1. Which lemmatizer / ambiguity strategy best improves BM25?
  2. Does neural reranking (native Polish, or translated) beat BM25 across domains?
  3. Does combining scores help?

## 4. Main idea

### Simple explanation

Two stages:

1. Find 100 or 1000 candidate passages with BM25 over **lemmatized** text.
2. Re-score each candidate with several signals and combine them with logistic regression:
   - BM25 scores (on lemmas, on word forms, on word pairs);
   - an English cross-encoder (MiniLM) applied after translating the Polish texts to English;
   - optionally, similarity between a GPT-generated answer and an answer extracted from the passage.

### Concrete example

- The author's lemmatization failure case (Sec. IV.A, p. 1283): "Bilbo Baggins" and "Bilba Bagginsa" (the same name in two grammatical cases) receive different lemmas, because no lemmatizer knows every proper name. A lemma-based BM25 then fails to match them.
- The author's retrieval error case (Sec. IV.J, p. 1285): for a question about the host of the show "Zrób to sam", the system returns passages about hosts of "Sam tego nie rób". The words overlap, the answer is absent.

### Formal method

- **Lemma-ambiguity strategies** for BM25 indexing (Sec. III.A, p. 1282):
  - **Morfeusz2 (all lemmas):** index every lemma the dictionary analyzer returns. The author's rationale: identical inflected forms share the whole lemma set and so produce several matches, while different forms of one word match on only one lemma. Exact-form matches therefore count more than cross-form matches. The cost is "many false matches".
  - **spaCy:** one contextual lemma, sometimes wrong or not a valid Polish word.
  - **hybrid:** take spaCy's lemma if Morfeusz2 also proposes it; otherwise take the corpus-most-frequent Morfeusz2 lemma (frequency measured on the Morfeusz2-lemmatized corpus).
  - **Morfeusz2-freq** (called "modified Morfeusz2" in Sec. III.A): always take the most frequent Morfeusz2 lemma, without spaCy.
- **Score fusion** (Sec. III.H, IV.F): logistic regression (scikit-learn) over the features of Table II (p. 1283). The ranking score is presumably the predicted relevance probability; the exact scoring rule is **NOT_REPORTED**.

## 5. Architecture / algorithm

1. **Indexing** (Sec. IV.A, p. 1283): one Elasticsearch index per lemmatizer (Morfeusz2, spaCy, hybrid, Morfeusz2-freq), plus the unlemmatized text. The question is lemmatized the same way as the corpus.
   - BM25 parameters: Table IV row 2 names "BM25 (k=1.0, b=0.5)". Parameters for the Table III runs are **NOT_REPORTED** (Context, not from the paper: the Elasticsearch default is k1 = 1.2, b = 0.75).
   - Elasticsearch analyzer, tokenization, lowercasing and stop-words: **NOT_REPORTED**.
2. **Bigram BM25** (Sec. III.B, p. 1282): BM25 where terms are word bigrams (unlemmatized). The author states it is "not a sufficient method on its own"; it is used only as a fusion feature. Its standalone score is **NOT_REPORTED**.
3. **Candidate generation for reranking** (Sec. III.C, p. 1282; Sec. IV.B, p. 1283): top-100 (later top-1000, Sec. IV.I) from BM25 "on texts lemmatized with Morfeusz2 lemmatizer (the basic approach)".
   - This is named "Morfeusz2", **not** the dev-best Morfeusz2-freq. The paper does not say whether "Morfeusz2" here means the all-lemmas variant of Table III. We read it literally (§19).
4. **BERT reranker** (Sec. IV.C, p. 1283): HerBERT-base cross-encoder (query [SEP] passage → CLS → classification head), fine-tuned one epoch on the wiki-trivia train set.
5. **Translation** (Sec. IV.D, p. 1284): OPUS-MT pl→en. Passages are split into pieces of "at most 0.3*512" (unit not stated; the 512 limit mentioned just before is in tokens, while the MiniLM windows in Sec. IV.E are counted in words), because OPUS-MT dropped content on long inputs; the translated pieces are rejoined.
6. **MiniLM reranker** (Sec. IV.E, p. 1284; footnote 4): `cross-encoder/ms-marco-MiniLM-L-6-v2`, applied to the English translations. No further fine-tuning on PolEval data is mentioned, so we read it as zero-shot (our inference).
   - Passages are split into overlapping windows of at most 0.7 × 512 words; the passage score is the maximum over windows.
   - Context (not from the paper): this is a cross-encoder reranker, not a dense bi-encoder; it scores each (query, passage) pair jointly and cannot index a corpus.
7. **Answer generation features** (Sec. III.G, IV.G, pp. 1283–1285):
   - generative answers from GPT-3 (`davinci`, temperature 0.1, prompt suffix "Shortest answer. NOT unknown.") and from ChatGPT;
   - extractive answers from DistilBERT fine-tuned on SQuAD;
   - MiniLM scores on (answer + question, answer + passage) and on (answer, answer) pairs.
   - Answers were generated only for dev and test questions (free-quota limit).
8. **Fusion** (Sec. IV.F, IV.H, pp. 1284–1285):
   - logistic regression trained either on the train set ("lr-train") or on the dev set ("lr-dev");
   - a two-layer neural network was also tried (Table IV row 9).

## 6. Data

PolEval 2022 Task 3 data as described in Sec. II and Table I (p. 1281):

| Domain | Questions source | Passages source | Avg length (unit NOT_REPORTED) | Corpus size (passages) | Author's characterization |
|---|---|---|---:|---:|---|
| wiki-trivia | "Jeden z dziesięciu" ("classical trivia questions") | Polish Wikipedia (WikiExtractor) | 44 | 7,097,322 | Questions written first, passages matched later, so answers are often worded differently; usually several relevant passages per question |
| legal-questions | generated from passages by volunteers | Polish legal acts | 153 | 26,287 | Wording similar to the passage; specialist vocabulary; some questions ambiguous out of context |
| allegro-faq | FAQ | Allegro help articles | 48 | 921 | Many "how to" questions; mostly one matching passage |

- **Language:** Polish.
- **Queries / test sizes:** **NOT_REPORTED.** Table I's caption says "Dataset sizes and number of questions from each domain", but the printed table has no question counts (checked on the page image, p. 1281).
- **Splits:** train and dev (wiki-trivia only); test-A (answers hidden during the contest, Sec. II.C); test-B (appeared in the last two weeks, Sec. IV.B).
  - Test-B has a majority of wiki passages (author, Sec. IV.K, p. 1286).
  - The train set is "over 7 times larger" than dev (Sec. IV.F, p. 1284); absolute sizes are **NOT_REPORTED**.
- **Test domain mix [computed, inferred]:** assuming the overall score is the question-weighted mean of the domain scores, Tables VI–VII give domain shares of about 0.32 / 0.33 / 0.36 (wiki / legal / allegro) for test-A and 0.51 / 0.18 / 0.31 for test-B. The test-B figure is consistent with the author's "majority … wiki" remark. Caveat: three equations with three unknowns always have an exact solution, so the fit itself is not independent support. The only checks are that all shares fall in [0, 1] and that test-B comes out wiki-majority.
- **Relevance judgments:** binary. How labels were produced is described only per domain (above).
  - The author observes annotation errors: relevant passages not marked, and marked passages without the answer or without the needed context (Sec. IV.J, p. 1285).
  - Allegro passages "were verified manually" (Sec. IV.J).
- **Training data for Table V:** "the training dataset" (wiki-trivia); 14,448 relevant passages in total **[computed: identical row sums in Table V]**.

## 7. Baselines

| Baseline | What it is | Why selected | Fair comparison? |
|---|---|---|---|
| "Baseline (from PolEval)" / "baseline BM25 (Elasticsearch)" | Organizers' BM25 | Official task baseline (Sec. II.C) | Its configuration (lemmatization, k1/b) is **NOT_REPORTED**, so it is unclear how it differs from the author's BM25 runs |
| BM25 without lemmatization (Table III) | Word-form BM25, Elasticsearch | Within-paper reference for the lemmatizers | Yes within Table III (same engine, same dev set). Dev set is wiki-trivia only |
| BM25 (k=1.0, b=0.5) (Table IV row 2) | Author's BM25 with changed parameters | Attempt to improve the baseline | Lemmatization **NOT_REPORTED**; dev 19.59 matches no Table III row; test-A 48.82 is **below** the organizers' baseline 50.76 |
| HerBERT cross-encoder (row 3) | Native Polish reranker, fine-tuned on wiki | Test of in-language fine-tuning | Yes as a reranker over the same candidates. It collapses out of domain (test-A 17.03) |
| MiniLM cross-encoder (row 4) | English MS MARCO reranker on translated text | Best results "for most IR tasks according to the BEIR paper" (author, Sec. III.F) | Same candidate set as the other rerankers. It differs from the BM25 runs in stage (reranking vs retrieval) and in language (translated English) |
| PolEval best solution (Table VI) | Winning team's system | Upper reference | Numbers only; method not described in this paper |

## 8. Metrics

| Metric | Definition | Simple meaning | Appropriate? |
|---|---|---|---|
| NDCG@10 (binary) | DCG@10 / ideal DCG@10 with gain 1 for relevant passages, averaged over questions (Sec. II.C) | "How many relevant passages are in the top 10, and how high?" Reported ×100 | Yes for top-10 QA retrieval. It says nothing about candidate coverage beyond rank 10 |
| Relevant passages by rank bucket (Table V) | Counts of relevant passages at ranks 1–10, 11–100, 101–1000, 1001–10000, >10000 in BM25 rankings, summed over training questions | A recall-by-depth profile for each lemmatizer | Useful for first-stage design; aggregated over questions, so not a per-query measure |

- **Scoring discrepancy stated by the author** (Sec. IV.B, p. 1283): submissions were scored on the PolEval website, other scores by the author's script; they differ by "around 0.5" because of questions where the correct passage is repeated.

## 9. Results

### Table III: BM25 with different lemmatization methods, dev set (wiki-trivia), p. 1283

| Method | NDCG@10 | Δ vs no lemmatization **[computed]** |
|---|---:|---:|
| no lemmatization | 18.62 | — |
| spaCy | 21.41 | +2.79 (+15.0%) |
| Morfeusz2 (all lemmas) | 21.15 | +2.53 (+13.6%) |
| hybrid (spaCy ∩ Morfeusz2, else most frequent) | 24.47 | +5.85 (+31.4%) |
| **Morfeusz2-freq** (most frequent Morfeusz2 lemma) | **25.24** | +6.62 (+35.6%) |

- Author: lemmatization "significantly improved the results"; the impact "considerably depended on the chosen model" (Sec. IV.A). No significance test was run; "significantly" is not statistical.
- spaCy vs Morfeusz2: +0.26 **[computed]**. The author notes Morfeusz2 is "even 20 times faster (on CPU)" (Sec. IV.A); no timing data are shown.
- Morfeusz2-freq vs hybrid: +0.77 **[computed]**. Author: "spaCy was not necessary at all in the hybrid approach" (p. 1283).

### Table V: relevant passages by BM25 rank bucket, training set, p. 1285

| Lemmatization | 1–10 | 11–100 | 101–1000 | 1001–10000 | >10000 | Share in top-100 **[computed]** | Share in top-1000 **[computed]** |
|---|---:|---:|---:|---:|---:|---:|---:|
| none | 2918 | 2755 | 2648 | 2078 | 4049 | 39.3% | 57.6% |
| spaCy | 3447 | 3476 | 2930 | 2023 | 2572 | 47.9% | 68.2% |
| Morfeusz2 | 3385 | 3341 | 3044 | 2181 | 2497 | 46.6% | 67.6% |
| hybrid | 3952 | 3841 | 3064 | 1897 | 1694 | 53.9% | 75.1% |
| Morfeusz2-freq | 4073 | 3863 | 3091 | 1839 | 1582 | 54.9% | 76.3% |

- Every row sums to 14,448 **[computed]**.
- The ordering of lemmatizers on the training set matches Table III on dev.
- Morfeusz2-freq vs none **[computed]**: +39.6% relevant passages in the top-10, +39.9% in the top-100, +32.5% in the top-1000.
- **Inference (ours):** the reranking pipeline takes its candidates from "Morfeusz2" BM25. On the training set that variant places 67.6% of relevant passages in the top-1000, against 76.3% for Morfeusz2-freq. If "Morfeusz2" means the all-lemmas index, the reranker's candidate recall was lower than the paper's own best lemmatizer would have given.

### Table IV: submissions to PolEval, NDCG@10, p. 1284

| id | Models | Combination | Rerank depth | dev | test-A | test-B |
|---:|---|---|---:|---:|---:|---:|
| 1 | Baseline (from PolEval) | – | – | – | 50.76 | – |
| 2 | BM25 (k=1.0, b=0.5) | – | – | 19.59 | 48.82 | – |
| 3 | BERT (HerBERT cross-encoder) | – | 100 | 24.5 | 17.03 | – |
| 4 | miniLM | – | 100 | 31.36 | 58.19 | – |
| 5 | miniLM | lr-train | 100 | 31.97 | 59.76 | – |
| 6 | miniLM | lr-dev | 100 | – | 60.17 | 51.55 |
| 7 | miniLM, GPT3 | lr-dev | 100 | – | 60.97 | 52.15 |
| 8 | miniLM, GPT3, chatGPT | lr-dev | 100 | – | 56.18 | 48.69 |
| 9 | miniLM, GPT3 | neural network | 100 | – | 53.64 | – |
| 10 | miniLM, GPT3 | – | 100 | – | 58.45 | – |
| 11 | miniLM, GPT3 | lr-dev | 1000 | – | **62.51** | **54.23** |
| 12 | miniLM, GPT3 (selected) | lr-dev | 1000 | – | – | 54.15 |
| 13 | miniLM, GPT3, chatGPT | lr-dev | 1000 | – | – | 51.82 |
| 14 | miniLM | lr-dev | 1000 | – | – | 53.20 |

Reading the table **[computed]**:
- **Adding BM25 features to MiniLM via LR (row 4 → 5):** +1.57 test-A, +0.61 dev. This is the closest thing to a "hybrid gain" in the paper. By Sec. IV.F the LR features are BM25-lemma, BM25-raw, BM25-bigram and the MiniLM score. The gain is not decomposed by feature.
- LR trained on dev instead of train (row 5 → 6): +0.41 test-A. The author suspects the LR "started overfitting to the wiki-trivia domain" when trained on the 7× larger train set (Sec. IV.F).
- GPT-3 answer features (row 6 → 7): +0.80 test-A, +0.60 test-B. Adding ChatGPT (row 7 → 8): −4.79 / −3.46.
- LR vs no fusion with the same neural signals (row 10 → 7): +2.52 test-A. The LR row also adds the BM25 and plain MiniLM features, so this is not a clean fusion ablation.
- LR vs two-layer neural network (row 7 vs 9): −7.33 for the NN.
- Rerank depth 100 → 1000 (row 7 → 11): +1.54 test-A, +2.08 test-B. Row 6 → 14: +1.65 test-B.
- "Selected" features (row 12) vs all (row 11), test-B: −0.08. "Selected" = unlemmatized BM25, bigram BM25, MiniLM, MiniLM on answer-concatenated pairs (Sec. IV.I, p. 1285). **The lemmatized-BM25 feature is dropped together with the (answer, answer) MiniLM feature**, so its individual contribution is not identified. The first stage remains lemmatized BM25.
- MiniLM reranking vs organizers' baseline (row 4 vs 1): +7.43 test-A (+14.6%).
- HerBERT: baseline/BERT = 50.76/17.03 = 2.98, matching the author's "dropped three times" (Sec. IV.C).
- The author says HerBERT "did better than the previous methods on the dev dataset" (24.5). That holds against Table IV row 2 (19.59), but not against Morfeusz2-freq BM25 in Table III (25.24). The two tables may not use the same scorer.

### Tables VI–VII: final and per-domain results, p. 1286

| Model | test-A | test-B | test-A wiki / legal / allegro | test-B wiki / legal / allegro |
|---|---:|---:|---|---|
| baseline BM25 (Elasticsearch) | 50.38 | 38.84 | 19.76 / 81.10 / 49.16 | 18.45 / 80.32 / 48.05 |
| my best model (= Table IV row 11, inferred from identical scores and Sec. IV.I) | 62.51 | 54.23 | 38.27 / 77.70 / 69.96 | 37.11 / 79.00 / 67.92 |
| PolEval best solution | 75.40 | 69.36 | NOT_REPORTED | NOT_REPORTED |

- **[computed]** Best model vs baseline: +12.13 test-A (+24.1%), +15.39 test-B (+39.6%).
- Per domain **[computed]**: wiki +18.51 / +18.66; legal **−3.40 / −1.32**; allegro +20.80 / +19.87.
- "Around the middle" between baseline and PolEval best: the midpoints are 62.89 / 54.10, against 62.51 / 54.23 **[computed ✓]**.
- The author attributes legal's high BM25 score to questions generated from the passages ("wording was usually very similar", "unique words") (Sec. IV.K).
- **Internal inconsistency:** the organizers' BM25 on test-A is 50.76 in Table IV (row 1) and 50.38 in Table VI. The 0.38 difference **[computed]** may reflect the website-vs-script discrepancy the author mentions, but the paper does not say which is which.

## 10. Statistical evidence

- **Significance tests:** NOT_REPORTED. Words like "significantly" and "considerably" are descriptive.
- **Confidence intervals:** NOT_REPORTED.
- **Runs / seeds:** NOT_REPORTED. Apparently single runs (e.g., HerBERT fine-tuned for one epoch, no variance shown).
- **Ablation:** partial and confounded.
  - Table III is a clean one-factor comparison of lexical representations, on dev only.
  - Table IV adds or removes features in steps. Rows 4→5 and 11→12 are the closest to fusion ablations, but each changes more than one thing. No leave-one-feature-out analysis for BM25-raw vs BM25-lemma vs bigram.
- **Per-query analysis:** none quantitative. Sec. IV.J gives qualitative error observations. Table V is aggregated over questions. There is **no overlap / unique-relevant-hit / oracle-union** analysis between lemmatizers, or between BM25 and the neural rerankers. There is **no breakdown by query features**; the proper-name observation (Sec. IV.A) is anecdotal.
- **Per-domain analysis:** Table VII only (baseline vs final system). The lemmatizers were not evaluated per domain.

## 11. Strengths

- Controlled within-engine comparison of **five lexical representations** (word form + four lemmatization strategies) on one dev set (Table III).
- Isolates the **ambiguity-resolution strategy** as a factor: all lemmas vs contextual vs dictionary-constrained contextual vs corpus frequency.
- **Recall-by-depth profile** per lemmatizer (Table V). This is directly relevant to first-stage candidate generation and is rarely reported.
- Out-of-domain test design (train on wiki, test on legal and FAQ) exposes domain fragility of fine-tuned rerankers (HerBERT) and of the fused system on legal.
- Uses the unlemmatized and bigram BM25 scores as separate fusion signals next to the lemmatized one.
- Candid reporting of failures (ChatGPT features, NN fusion, HerBERT) and of annotation problems.
- Code link provided (footnote 2).

## 12. Limitations

### Stated by the author

- Lemmatizers fail on proper names (Sec. IV.A).
- Morfeusz2 all-lemmas produces "many false matches"; spaCy can return invalid lemmas (Sec. III.A).
- HerBERT reranking "generalizes very poorly to other domains" (Sec. IV.C).
- OPUS-MT drops content on long inputs, which forced chunking (Sec. IV.D).
- LR trained on train may overfit wiki-trivia (Sec. IV.F).
- Large computational cost of top-1000 reranking, mostly translation (Sec. IV.I).
- Elasticsearch sometimes returns fewer passages than requested, especially for allegro-faq (Sec. IV.I).
- Annotation errors in the datasets (Sec. IV.J).
- Not all models were evaluated on dev, to save resources (Sec. IV.B).

### Inferred from the experimental design

1. **The lemmatizer comparison is wiki-trivia only.** The dev set comes only from that domain. The conclusion "the choice of the lemmatizer largely impacts the performance" and the claim that statistical methods "don't have a problem with generalizability, because they are independent of the domain" (Sec. V, p. 1286) were not tested per domain. Other Polish evidence (CR000100 card, legal questions) shows the lemma effect can reverse sign there.
2. **Pipeline does not use the dev-best lemmatizer.** Reranking candidates come from "Morfeusz2" BM25, while Morfeusz2-freq was best on dev (Table III) and in candidate recall (Table V). The downstream effect of that choice is untested.
3. **No dense retrieval.** The neural channel is a cross-encoder reranker over lexical candidates, so every "hybrid" result is bounded by lexical candidate recall. It cannot show what a semantic retriever finds that BM25 does not.
4. **Translation confound.** MiniLM works on OPUS-MT English, where Polish inflection is largely removed by translation. Neural–lexical differences therefore mix translation and model effects.
5. **Fusion not decomposed.** The contribution of BM25-lemma vs BM25-raw vs bigram inside the LR is not identified (§9).
6. **Tuning on dev, reporting on test.** LR trained on dev is legitimate for test-A/B, but dev is in-domain for wiki only. Selection among the 14 submissions used test-A feedback ("I tried only the models that did well on test-A", Sec. IV.B), so test-B is the cleaner estimate.
7. **Missing configuration and sizes.** BM25 parameters and analyzers for Table III, question counts, and the baseline configuration are NOT_REPORTED.
8. No significance tests, no CIs, single runs.

## 13. What the work proves

Within its setting (Polish, Elasticsearch BM25, PolEval 2022 wiki-trivia dev/train):

- **Lemmatization improves BM25 over word forms**, and the size of the gain depends strongly on the lemmatization strategy: +2.53 to +6.62 NDCG@10 over 18.62 (Table III).
  - Caveats: single dev set, no significance test. The Table V training-set counts show the same ordering, which adds some robustness.
- **Ambiguity resolution matters more than analyzer family here.** Choosing the corpus-most-frequent Morfeusz2 lemma (25.24) beats indexing all Morfeusz2 lemmas (21.15) and beats spaCy's contextual lemma (21.41) (Table III).
- **Lexical representation changes deep candidate coverage.** Among relevant training passages, 39.3% vs 54.9% are in the top-100 and 57.6% vs 76.3% in the top-1000 (none vs Morfeusz2-freq, Table V **[computed]**).
- **Cross-encoder reranking of Morfeusz2-BM25 top-1000 candidates, with an LR fusing BM25 scores, MiniLM scores and GPT-3/DistilBERT answer-based MiniLM features, beats the BM25 baseline overall** (62.51 vs 50.38; 54.23 vs 38.84, Table VI). It does **not** beat it on the legal domain (Table VII).
- An English MS MARCO MiniLM reranker (no PolEval fine-tuning mentioned) on machine-translated text generalized across domains better than a HerBERT reranker fine-tuned on wiki-trivia (58.19 vs 17.03 test-A, Table IV).

## 14. What the work does NOT prove

- **Anything about dense (bi-encoder) retrieval or lexical–dense hybrid retrieval.** No first-stage dense retriever is used.
- **That BM25 and the neural channel are complementary in the project's sense.** There are no unique relevant hits, overlap or oracle union. The +1.57 NDCG@10 fusion gain (rows 4→5) is aggregate and not decomposed.
- **How lemmatization changes complementarity.** The lexical variant was never varied while the neural component was held fixed and their overlap measured. The first stage is always "Morfeusz2" BM25.
- **That lemmatization helps in every domain.** Only wiki-trivia was tested; the legal-domain results hint otherwise for the full system.
- **That stemming is better or worse than lemmatization.** No stemmer was tested.
- **Which queries benefit and why.** There is no per-query or query-feature analysis; proper names are an anecdote.
- **Statistical reliability of any difference.** There are no tests; several dev differences are below 1 point (e.g., spaCy vs Morfeusz2 0.26; freq vs hybrid 0.77).

## 15. Relationship to current Uzbek evidence

- **No Uzbek data.** Polish is fusional (Slavic) with rich case inflection; Uzbek is agglutinative (Turkic).
- **The mechanism studied here transfers conceptually.** Uzbek morphological analyzers (Bakaev, Xusainova, Elov: `MASTER_INDEX` C) also produce ambiguous analyses. For Uzbek the question "all lemmas vs one lemma, chosen how" is as real as for Polish, and none of the national cards reports a retrieval evaluation of that choice.
- **Polish cluster (from our own cards, not from this paper):**
  - **CR000100** (Rybak & Ogrodniczuk 2024, Silver Retriever): word-form vs lemma BM25 next to dense retrievers on PolQA, Allegro FAQ and Legal Questions. The lemma helps on PolQA/Allegro but hurts on Legal; lemmatizer not reported. The present paper supplies the lemmatizer-strategy dimension that CR000100 lacks, on the wiki-trivia/PolQA-type domain only.
  - **CR000103** (BEIR-PL 2024): a single stemmed BM25 (Stempel) plus rerankers; its PolEval 2022 Table 6 gives BM25 Legal 79.14 / 81.35 and Allegro 61.00 / 58.31 (from that card). Those numbers differ from the baseline here (legal 81.10 / 80.32; allegro 49.16 / 48.05). Different BM25 configurations and possibly scoring scripts; not directly comparable.
  - **CR000913** (PolEval 2022/23 overview): per its triage record, participants differed in BM25 normalization. The present paper is one such participant; its "PolEval best solution" (75.40 / 69.36) would be described there.
- Together with Mekonnen et al. (Amharic, proposed MORPH-005) and Munetsi et al. (Shona, MORPH-004), this adds to a recurring pattern: morphology-varied BM25 and neural models appear in the same study, but **the lexical–neural result sets are never decomposed**.

## 16. Relationship to CURRENT_GAP

**Classification:** *supports* (motivation) + *narrows slightly* + *no material effect on the residual core*.

- **Supports:**
  - Changing the morphological representation of the lexical channel changes not only top-10 effectiveness but also **which relevant passages enter deep candidate lists** (Table V).
  - The same representation is used as the candidate generator for the neural stage.
  - This is exactly the mechanism by which the representation could alter lexical–semantic complementarity. The paper shows the precondition (large representation-induced shifts in candidate recall) but not the consequence.
- **Narrows / refines (proposal):** "lemma" is not a single condition. The ambiguity strategy alone moved dev NDCG@10 by +4.09 (21.15 → 25.24) **[computed]**, larger than the lemmatizer-family difference. A v0.8 design that treats `BM25_lemma` as one condition without specifying the disambiguation rule would leave an uncontrolled factor. This refines the experimental control, not the gap wording.
- **Confirms as occupied (already non-claims in v0.8):**
  - "raw vs lemma BM25 was not compared in a morphologically rich language";
  - "lexical and neural scores have not been combined with morphology-varied BM25 features".
  This paper is a (B-level) Polish instance of both.
- **No effect on the residual core:**
  - no fixed dense retriever D;
  - no unique relevant hits, overlap or oracle union;
  - no incremental hybrid gain per representation;
  - no query-feature link.

**Proposal:** keep v0.8 refined unchanged. Optionally cite this paper with CR000100 in the evidence boundary as the Polish example of "lemmatizer strategy changes BM25 effectiveness and candidate recall; lexical scores fused with neural rerankers; no complementarity decomposition". This is a proposal only; `CURRENT_GAP.md` has not been edited.

## 17. Implications for our research design

- **Morphology preprocessing:**
  - Define `BM25_lemma` precisely: analyzer, and the rule for ambiguous forms (all analyses / first analysis / most frequent lemma in corpus / contextual disambiguation / contextual constrained by the analyzer).
  - Consider a small pilot sub-comparison of two ambiguity rules on dev before freezing the main `BM25_lemma` condition. Report the rule chosen.
  - Record analyzer coverage failures (unknown words, proper names) per query as a feature.
- **Candidate coverage metric:** report per-variant Recall@100 / Recall@1000 (Table V style, but per query) for raw / stem / lemma. The union of relevant passages across channels is only meaningful at a fixed depth k.
- **Fusion:**
  - Keep `BM25_raw` available as a separate signal even in the lemma condition; this paper and CR000100 both suggest raw forms carry information (exact-form matches, legal-style wording).
  - Fit fusion weights on dev only. Beware domain mismatch between dev and test (the author's LR train-vs-dev observation).
- **Baselines / D:** this paper gives no guidance on D, since it has no dense retriever. Its translate-then-rerank approach is a pragmatic low-resource workaround, not a candidate for our fixed semantic comparator.
- **Query taxonomy:** add *proper name present / analyzer-unknown tokens* and *query-passage wording similarity* (the legal-domain effect) as candidate query features.
- **Dataset:** if the Uzbek benchmark mixes domains, analyse the morphology effect per domain; the lemma effect can reverse in domains where queries copy passage wording.
- **Protocol hygiene:**
  - fix and report BM25 parameters and analyzers for every variant;
  - report the number of queries per split;
  - use one scoring script for all runs (cf. the 50.76 / 50.38 discrepancy).

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| Passage retrieval | Find the short text fragments that contain the answer to a question | Rank passages of a corpus for query q; here top-10 |
| BM25 | Word-matching ranking: shared rare words and repeated matches raise the score, with length normalization | Probabilistic relevance scoring with parameters k1, b |
| Lemmatization | Replace each word form by its dictionary form ("Bagginsa" → "Baggins") | Mapping token → lemma using a morphological analyzer / model |
| Lemma ambiguity | One written form can belong to several dictionary words; the analyzer returns several candidates | Set-valued analyzer output requiring disambiguation |
| Morfeusz2 | Dictionary-based Polish morphological analyzer; returns all possible lemmas | Analyzer (Kieraś & Woliński 2017, ref. [3]) |
| Morfeusz2-freq | Pick the lemma that is most frequent in the corpus analyzed by Morfeusz2 | Frequency-based disambiguation |
| Bigram BM25 | BM25 where the "words" are pairs of adjacent words | BM25 over word 2-gram terms |
| Cross-encoder reranker | A model reads query and passage together and outputs a relevance score; used only on a short candidate list | Joint encoding f(q,p) = head(Enc([q;p])) |
| Dense retriever (bi-encoder) | Encodes query and passage separately into vectors; can search the whole corpus. **Not used in this paper** | f(q,p) = sim(Enc(q), Enc(p)) |
| Score-level fusion | Combining several numeric relevance scores into one | Here: logistic regression over score features |
| NDCG@10 (binary) | How many relevant passages are in the top 10 and how high | DCG@10 / IDCG@10 with gain ∈ {0,1} |
| Complementarity (project term) | Each channel finds relevant items the other misses | Unique relevant hits, overlap, oracle-union gain |

## 19. Open questions / verification needed

1. **Question counts** per domain and split (the Table I caption promises them): NOT_REPORTED. Check CR000913 (the PolEval overview), which likely gives them.
2. **Which "Morfeusz2"** generated the reranking candidates: the all-lemmas index of Table III, or another variant? Not decidable from the paper.
3. **Lemmatization and analyzer of Table IV row 2** "BM25 (k=1.0, b=0.5)", and BM25 parameters of Table III: NOT_REPORTED.
4. **Baseline discrepancy** 50.76 (Table IV) vs 50.38 (Table VI) on test-A: which is the website score and which the script score?
5. **Table IV caption** defines "LR-DEV" twice (the second should presumably read "LR-TRAIN", given the "lr-train" rows); a typo, noted for accurate citation.
6. **Per-domain lemma effect:** could be computed from the released test answers (published after the contest, Sec. IV.K) with raw vs Morfeusz2-freq BM25. It would be a cheap external check of the domain-reversal pattern seen in CR000100.
7. **Overlap pilot:** Table V's per-lemmatizer rankings on the training set could, if rerun per query, give the raw-vs-lemma unique-hit / overlap numbers at k = 100/1000 that the paper does not report. Useful as a Polish sanity check of our measurement pipeline.
8. Whether the PolEval best solution (75.40 / 69.36) used dense retrieval or fusion: see CR000913, not this paper.

## 20. Decision after deep dive

- **Keep current gap?** Yes; v0.8 refined remains valid (§16).
- **Modify gap?** No change to the wording proposed. Optionally add this paper to the evidence-boundary list together with CR000100 (Polish cluster), as a researcher's decision.
- **Add decision?** Proposed for `decisions/DECISIONS.md` (researcher's decision): "The `BM25_lemma` condition must specify the analyzer and the lemma-ambiguity rule (all analyses / most frequent / contextual). If a pilot shows a large effect of the rule, treat the rule as a controlled sub-variant rather than a hidden implementation detail."
- **Add experiment?** Optional pilot:
  - on Uzbek dev data, compare two ambiguity rules for `BM25_lemma` (all lemmas vs most frequent lemma) on nDCG@10 and Recall@100/1000;
  - compute per-query unique relevant hits vs `BM25_raw` at k = 100/1000.
- **Add citation to Chapter I?** Yes, briefly:
  - §1.1 (morphological normalization in lexical retrieval: lemmatizer and ambiguity strategy change BM25 effectiveness and candidate recall in a morphologically rich language);
  - §1.3 (score-level fusion of morphology-varied BM25 features with neural rerankers exists, without complementarity decomposition). Cite as B-level shared-task evidence.
- **Proposed `MASTER_INDEX.md` row** (to add after approval):

| MORPH-016 | Pacanowska — *Passage Retrieval in Question Answering Systems in Polish Language* (FedCSIS 2023, ACSIS 35, pp. 1281–1286, DOI 10.15439/2023F586) — [deep dive](deep-dives/2023_Pacanowska_Polish_Passage_Retrieval_PolEval_Lemmatization.md) | 2023 | B | HIGH | PolEval 2022 Task 3 system description (MSc-thesis based). Elasticsearch BM25 on word forms vs four lemmatization strategies (dev, wiki-trivia only): 18.62 → 21.15 (Morfeusz2 all lemmas) / 21.41 (spaCy) / 24.47 (hybrid) / 25.24 (most-frequent Morfeusz2 lemma) NDCG@10; top-1000 candidate recall 57.6% → 76.3% (Table V, computed). Cross-encoder reranking (HerBERT; MiniLM on OPUS-MT English) + logistic-regression fusion with raw/lemma/bigram BM25 scores and GPT-3/DistilBERT answer-based features (top-1000 rerank): 62.51/54.23 vs BM25 baseline 50.38/38.84, but below BM25 on legal. No dense retrieval, no stemming, no overlap/unique-hit/oracle/per-query analysis, no significance tests. |
