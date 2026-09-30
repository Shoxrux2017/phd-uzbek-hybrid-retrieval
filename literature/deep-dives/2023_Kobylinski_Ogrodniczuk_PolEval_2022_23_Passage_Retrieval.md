# Kobyliński, Ogrodniczuk, Rybak et al. (2023): PolEval 2022/23 Challenge Tasks and Results (Task 3: Passage Retrieval)

**Targeted deep-dive status:** COMPLETED (AI-assisted, pending researcher review)
**Completed:** 2026-09-28
**Literature ID:** `MORPH-015` (assigned 2026-09-28, approved by researcher)
**Systematic-review record:** `CR000913`. Full-text triage: INCLUDE as a **BORDERLINE** case, reading priority HIGH, tier "1 — прямо по теме пробела", `carries_complementarity_evidence = NO`
**Provenance:** AI-assisted deep dive (Claude). The whole paper (8 printed pages, pp. 1243–1250) was read from the pdftotext extraction. Tasks 1 (punctuation) and 2 (abbreviations) were read only to confirm they are out of scope. Task 3 (Sec. IV, pp. 1246–1249) was read closely. Page images of **p. 1243** (byline, DOI, venue header), **p. 1247** (Sec. IV.A–E: task, datasets, NDCG@10 definition), **p. 1248** (Table IX and all participant descriptions, Sec. IV.F start) and **p. 1249** (rest of Sec. IV.F) were checked visually. Every number and quote below was compared against them. Numbers computed by us are marked **[computed]** (recomputed with Python).
**Source rule:** **the paper is the primary and only authoritative source.** The participants' own system papers, the PolEval website and the footnoted model/tool links were not used to describe what the participants did. The web was used only to verify the bibliographic record (marked "bibliographic check").
**Verification:** independent AI verifier pass 2026-09-28; 6 findings addressed (2 IMPRECISE, 4 NOTE; none rejected).
**Reliability:** **B**. It is a verifiable, peer-reviewed conference paper (FedCSIS 2023, ACSIS vol. 35), written by the organisers. Its evidential strength for our questions is limited: it is a **shared-task overview**. It reports one final score per team for end-to-end retriever + reranker systems. It has no controlled comparison, no ablation and no per-domain scores, and the systems are described in one short paragraph each.

---

## Кратко для исследователя (RU)

- **Что это.** Обзорная статья организаторов соревнования PolEval 2022/23 (польский язык). В нём три задачи; для нас важна только **Task 3: поиск пассажей (passage retrieval) для вопросно-ответных систем**. Остальные задачи (пунктуация, аббревиатуры) к теме не относятся.
- **Постановка Task 3** (Sec. IV.B–D, p. 1247):
  - обучающий набор: 5,000 вопросов-викторин PolQA, 16,389 пар «вопрос–пассаж», корпус Википедии 7,097,322 пассажа;
  - три тестовых домена: викторина (1,291 вопрос), e-commerce Allegro (900 вопросов, 921 пассаж), право («более 700» вопросов, ≈26,000 пассажей);
  - метрика: NDCG@10.
- **Результаты — одна итоговая NDCG@10 на команду** (Table IX, p. 1248), 7 команд: от **69.36** (Pokrywka: BM25 + mt5-3B/13B) до **51.71** (Karaś: гибрид + mBERT). Разбивки по доменам **нет**, способ усреднения по трём доменам не описан.
- **Морфология здесь — только как проектные решения участников, без контролируемого сравнения.** По описаниям (pp. 1247–1248):
  - стемминг «с Polimorf» (Pokrywka, сноска на pystempel);
  - лемматизация Morfologik в Elasticsearch (Kozlowski);
  - BM25 по лемматизированному тексту + признаки «BM25 по нелемматизированным данным / по биграммам», объединённые логистической регрессией (Pacanowska);
  - словарь словоформ sjp.pl (Kazuła);
  - у трёх команд (Wojtasik, Ropiak, Karaś) нормализация **не описана**.
- **BM25 есть у всех 7 систем; плотные ретриверы — у 4 «гибридных»** (mContriever, mDPR, LaBSE, дообученные RoBERTa, MiniLM). «Гибрид» здесь означает объединение пулов кандидатов перед переранжированием; способ объединения не описан. Слияния оценок BM25 + dense с оценкой именно первого этапа **нет**.
- **Нет:** сравнения raw / stem / lemma BM25 в одних условиях; оценки ретриверов отдельно от переранжировщика; перекрытия результатов и уникально найденных пассажей; oracle union; анализа по запросам; тестов значимости и доверительных интервалов.
- **Выводы авторов слабо обоснованы (наша оценка):** «ретривер не играл важной роли, так как лучшая система использовала только BM25» (p. 1249). Системы одновременно различаются переранжировщиком, глубиной пула (350–3,000 кандидатов), внешними данными и числом моделей на домен, поэтому вклад ретривера и нормализации из Table IX выделить нельзя.
- **Внутренние несоответствия в статье:**
  - текст (p. 1249): «**три** участника» делали отдельные модели для доменов, а в Table IX (p. 1248) «Model per domain = Yes» только у **двух** (Pokrywka, Ropiak);
  - «Many lemmatised the passages» (p. 1248), но явно лемматизацию описывают только 2 из 7 команд;
  - «ни одна система не использовала learning-to-rank» (p. 1249), хотя у Pacanowska итоговую оценку даёт логистическая регрессия поверх нескольких признаков (p. 1248). Это можно считать поточечным learning-to-rank — наша интерпретация.
- **Для нашего gap:** работа ядро v0.8 **не затрагивает** (предложение: gap не менять). Она показывает, что в польской практике морфологическая нормализация BM25 и объединение BM25 с плотным поиском уже используются вместе. Контролируемых данных о взаимодополняемости нет. Ценность работы — **указатель**:
  - на CR000914 (система Pacanowska, по triage в ней есть сравнение лемматизаторов и слияние);
  - на многодоменный польский бенчмарк PolEval Task 3. Публичная доступность данных в статье не указана: авторы только планируют репозиторий наборов данных (Sec. V, p. 1249). По карточкам проекта (не по этой статье), наборы с теми же названиями доменов используются в CR000100 и CR000103; идентичность тестовых наборов не проверена (§15, §19).
- **Практическая польза для нас:**
  1. Оценивать первый этап отдельно (Recall@k / unique hits ретривера), а не только итоговую метрику после переранжирования.
  2. Приводить метрики по доменам и указывать способ усреднения.
  3. Для каждого варианта BM25 явно документировать инструмент нормализации (стеммер / лемматизатор / словарь словоформ).

---

## 1. Bibliographic record

- **Authors:** Łukasz Kobyliński, Maciej Ogrodniczuk, Piotr Rybak, Piotr Przybyła, Piotr Pęzik, Agnieszka Mikołajczyk, Wojciech Janowski, Michał Marcińczuk, Aleksander Smywiński-Pohl (p. 1243)
- **Affiliations:** Institute of Computer Science, Polish Academy of Sciences (Kobyliński, Ogrodniczuk, Rybak, Przybyła); Universitat Pompeu Fabra (Przybyła); University of Łódź (Pęzik); VoiceLab.AI (Pęzik, Mikołajczyk, Janowski); Wrocław University of Science and Technology (Marcińczuk); AGH University of Krakow (Smywiński-Pohl) (p. 1243)
- **Year:** 2023
- **Venue:** *Proceedings of the 18th Conference on Computer Science and Intelligence Systems* (FedCSIS 2023), Warsaw, Poland. Thematic track "Challenges for Natural Language Processing" (p. 1243 footer; p. 1244 running header)
- **Series:** Annals of Computer Science and Information Systems (ACSIS), Vol. 35, ISSN 2300-5963 (p. 1243)
- **Pages:** 1243–1250 (p. 1243)
- **Publisher:** PTI (©2023, PTI; IEEE Catalog Number CFP2385N-ART, p. 1243)
- **Editors:** M. Ganzha, L. Maciaszek, M. Paprzycki, D. Ślęzak (bibliographic check: annals-csis.org, Volume_35/drp/5627)
- **ISBN:** 978-83-967447-8-4 (bibliographic check: annals-csis.org)
- **DOI:** `10.15439/2023F5627` (p. 1243; resolves to annals-csis.org/Volume_35/drp/5627.html, bibliographic check)
- **IEEE Xplore listing:** the assignment metadata says "IEEE Conferences". We did not verify an IEEE Xplore record; the ACSIS page does not mention one.
- **Source type:** peer-reviewed conference paper; **shared-task overview** written by the organisers
- **Reliability:** B
- **Full text available:** yes (`07_full_text/pdfs/CR000913.pdf`, 8 pages)

## 2. Why this work matters to the PhD

It is the official record of a Polish passage-retrieval shared task. Polish is a highly inflected language. Seven teams built full retrieval pipelines, and the organisers note that they "differed in the way they normalised the text" (p. 1248).

| Axis | Relation |
|---|---|
| Lexical retrieval | BM25 in all 7 systems. Normalisation varies across teams (stemming, lemmatisation, word-form dictionary, not described). Not compared in controlled conditions |
| Semantic retrieval | Dense retrievers (mContriever, mDPR, LaBSE, fine-tuned Polish RoBERTa, MiniLM) in 4 "hybrid" systems; cross-encoder / seq2seq rerankers in all |
| Hybrid retrieval | Present as **candidate-pool combination** of BM25 and dense retrievers before reranking. The combination method is not described; the retrieval stage is not scored separately |
| Uzbek morphology | Indirect: Polish is fusional-inflectional (Slavic), Uzbek is agglutinative (Turkic) |
| Low-resource retrieval | Medium-resource language; small in-domain training data (5,000 questions) and three test domains |
| Current gap | No controlled raw/stem/lemma comparison, no complementarity measurement. **No material effect** on v0.8 refined (§16) |

## 3. Research problem

### Simple explanation

Question-answering systems first need to find the text passages that contain the answer. The organisers set up a competition: given a Polish question, return the 10 best passages from a corpus. The question is which systems do this best across three quite different domains (general knowledge, online-shop help pages, law).

### Formal formulation

Task (Sec. IV.B, p. 1247): "cross-domain question-answering retrieval". For each test question `q`, return an ordered list of the 10 passages from corpus `P` most likely to contain the answer. Systems are ranked by NDCG@10 on test questions from three domains (trivia, law, customer support).

The paper itself asks no research question. It reports the task, data, metric and submissions.

## 4. Main idea

### Simple explanation

This is not a method paper. The organisers built training and test data, fixed one metric and collected participants' systems. "All systems followed a similar architecture" (p. 1247), a two-stage shape (Wojtasik adds an intermediate plT5-large filtering step, p. 1248):

1. a **retriever** (fast first-stage search) returns the top N candidate passages;
2. a **ranker** (slower, more accurate model) re-orders them and keeps the final 10.

### Concrete example

The paper gives no Task 3 example. Illustration from its own description (not a real query):

- a legal-domain question was written by hand after randomly choosing a passage from an act of law (p. 1247);
- a BM25 retriever with lemmatisation matches the question's inflected Polish words against lemmatised passage words and returns, e.g., 1,000 candidates;
- a cross-encoder then scores each (question, passage) pair and outputs the top 10;
- NDCG@10 rewards the system if the answer-bearing passage appears near the top.

### Formal method

Metric only (Eqs. 5–7, p. 1247):

`DCG_p = Σ_{i=1..p} rel_i / log2(i+1)`,
`IDCG_p = Σ_{i=1..|REL_p|} rel_i / log2(i+1)`,
`NDCG_p = DCG_p / IDCG_p`, with p = 10.

`rel_i` is "the relevance of the i-th passage". `REL_p` is "the list of relevant passages ordered by their relevance". Whether relevance is binary or graded is **NOT_REPORTED**.

Context (not from the paper): in the usual definition, `REL_p` is cut at position p. The printed text does not say so explicitly; if `REL_p` were not cut, a query with more than 10 relevant passages could never reach NDCG = 1.

## 5. Architecture / algorithm

The participants' systems, as described by the organisers (Sec. IV.E, pp. 1247–1248; Table IX, p. 1248). "NR" = not reported in this paper.

| Team (rank) | Retriever (Table IX) | Lexical normalisation for BM25 | Dense retriever(s) | Candidate pool | Ranker | NDCG@10 |
|---|---|---|---|---|---|---:|
| Jakub Pokrywka (1) | BM25 | "text stemming using Polimorf" (footnote 12: pystempel) | none | 1,500 (Allegro, legal); 3,000 (trivia) | per-domain: mt5-3B + mt5-13B ensemble (Allegro, legal); trivia: mt5-3B "supplemented by a custom-trained cross-encoder models, mDeBERTa, and mmarco-mMiniLMv2-L12-H384-v1" (p. 1248; ambiguous: either one custom cross-encoder plus two public checkpoints (footnotes 15–16 link public HF models), or custom-trained mDeBERTa and mMiniLM) | 69.36 |
| Marek Kozlowski (2) | Hybrid | Elasticsearch + Morfologik analyser "for lemmatisation" | two retrievers fine-tuned from polish-roberta-base-v2 / -large-v2 ("MultipleNegativeRankingLoss" as printed, PolEval train + translated MS MARCO) | NR | mt5-13B | 68.19 |
| Konrad Wojtasik (3) | Hybrid | NR | mContriever, mDPR, LaBSE ("ensemble of several retrieval algorithms, starting with the BM25 algorithm") | ≈350 after a plT5-large filter trained on translated MS MARCO | mT5-13B | 67.44 |
| Norbert Ropiak (4) | Hybrid | NR | mContriever; "combined the results of both for further processing" | NR | ms-marco-MiniLM-L-12-v2, mDeBERTa | 63.27 |
| Anna Pacanowska (5) | BM25 | BM25 "on lemmatised text" for retrieval; BM25 "on unlemmatised data or on bigrams" as extra features | none | 1,000 | passages translated to English (OPUS-MT), English MiniLM-L6 cross-encoder on raw pairs and on pairs with GPT-3-generated answers; **logistic regression** combines all scores | 54.23 |
| Maciej Kazuła (6) | BM25 | "word inflection dictionary" (footnote 23: sjp.pl) "to normalise the text" | none | NR | MiniLM-L6 cross-encoder fine-tuned on translated MS MARCO; "a new tokeniser … to better represent Polish words in terms of word forms" | 51.78 |
| Daniel Karaś (7) | Hybrid | NR | "slightly fine-tuned" MiniLM (multi-qa-MiniLM-L6-cos-v1) | ≈1,000 per retriever; all passages for Allegro | mBERT passage reranker, no additional training | 51.71 |

Notes:

- "Hybrid" in Table IX means that BM25 and neural retrievers both supplied candidates. How candidates were merged (union, score fusion, RRF…) is **NOT_REPORTED** for every team.
- BM25 parameters (k1, b), tokenisation, stop-words and index fields are **NOT_REPORTED** for every team.
- Pokrywka's description names Polimorf but footnotes pystempel. Context (not from the paper): Polimorf is a Polish morphological dictionary, and pystempel is a Python port of the Stempel stemmer, which can use stemming tables derived from it. The paper does not explain the relation, so the exact normalisation (stemming vs dictionary lookup) stays ambiguous.

## 6. Data

Task 3 data (Sec. IV.C, p. 1247):

- **Language:** Polish.
- **Training set:**
  - 5,000 trivia questions from PolQA [19];
  - each with up to five answer-bearing Polish Wikipedia passages;
  - 16,389 question–passage pairs in total.
- **Wikipedia corpus:**
  - 7,097,322 passages;
  - parsed with WikiExtractor;
  - split at paragraph ends or when longer than 500 characters.
  - It is presented with the training set. Its use as the trivia test corpus is implied but not stated.
- **Test set 1 (trivia):** 1,291 questions "similar to those in the training set".
- **Test set 2 (customer support, Allegro):**
  - 900 questions and 921 passages;
  - from Allegro help articles and FAQ lists;
  - "Each question-passage pair was manually checked and edited where necessary".
- **Test set 3 (law):**
  - "over 700" questions;
  - created by randomly selecting a passage and "manually writing a question";
  - corpus of "approximately 26,000 passages extracted from over a thousand acts of laws published between 1993 and 2004".
- **Total test questions:** > 2,891 **[computed: 1,291 + 900 + 700]**.
- **Relevance judgments:** "relevant" = containing the answer (Sec. IV.B).
  - How the trivia test positives were identified (pooling? manual?) is **NOT_REPORTED**.
  - For Allegro and law the pairs are author-constructed (one passage per question is implied, not stated).
  - Graded vs binary relevance: NOT_REPORTED.
- **Dev split:** none is described for Task 3. Tasks 1–2 report Test-A / Test-B; Task 3 reports a single score.

## 7. Baselines

**No organiser baseline is reported** (no official BM25 or dense run). The only comparison is between participant systems.

| Comparison implicit in Table IX | Fair? |
|---|---|
| BM25-only vs hybrid retrievers | **No.** Retriever type is confounded with ranker (mt5-13B vs MiniLM-L6), pool depth (≈350 to 3,000), external data (translated MS MARCO), per-domain models and translation to English |
| Stemming vs lemmatisation vs dictionary normalisation | **No.** Each normalisation appears in a different system with a different ranker; three systems do not report normalisation at all |

## 8. Metrics

| Metric | Definition | Simple meaning | Appropriate? |
|---|---|---|---|
| NDCG@10 | Eqs. 5–7, p. 1247 | How high the passages that contain the answer appear in the returned top 10; higher positions count more | Suitable for the end-to-end output. It says nothing about first-stage candidate coverage (e.g., Recall@1000), which is what matters for hybrid-retrieval analysis |

- Aggregation over the three test domains (micro over all questions, or macro over domains): **NOT_REPORTED**.
- Per-domain scores: **NOT_REPORTED**.
- Scale: reported as ×100 (e.g., 69.36).
- The organisers name one deficiency themselves: "the lack of consideration for the computational heaviness of the approaches" (p. 1249).

## 9. Results

### Table IX: Passage Retrieval task submissions (p. 1248, checked on the page image)

| Submission | Retriever | Ranker | External datasets | Model per domain | NDCG@10 |
|---|---|---|---|---|---:|
| Jakub Pokrywka | BM25 | mt5-3B, mt5-13B, custom | No | Yes | **69.36** |
| Marek Kozlowski | Hybrid | mt5-13B | Yes | No | 68.19 |
| Konrad Wojtasik | Hybrid | mt5-13B, custom | Yes | No | 67.44 |
| Norbert Ropiak | Hybrid | MiniLM-L12, mDeBERTa | No | Yes | 63.27 |
| Anna Pacanowska | BM25 | MiniLM-L6, custom | No | No | 54.23 |
| Maciej Kazuła | BM25 | MiniLM-L6 | Yes | No | 51.78 |
| Daniel Karaś | Hybrid | mBERT | No | No | 51.71 |

Reading the table **[computed]**:

- Winner vs 2nd: +1.17 points (+1.72% relative); winner vs 3rd: +1.92 points. Whole range: 17.65 points.
- The three mt5-13B systems average 68.33; the three MiniLM-L6/mBERT systems average 52.57. That is the ranker pattern the organisers describe.
- Mean by Table IX retriever label: BM25-only 58.46 (n = 3), Hybrid 62.65 (n = 4). **Not interpretable**: both groups mix strong and weak rankers.
- Nearly equal pairs with different retrievers:
  - Kazuła (BM25 + dictionary normalisation, MiniLM-L6) 51.78 vs Karaś (hybrid, mBERT) 51.71: 0.07 points;
  - Pacanowska (lemmatised BM25, MiniLM-L6 + LR) vs Kazuła (dictionary-normalised BM25, MiniLM-L6): 2.45 points, but they also differ in translation, GPT-3 features, LR combination and external data.

### Organisers' interpretation (Sec. IV.F, pp. 1248–1249), verbatim

- "All submitted systems used the BM25 algorithm as a retriever, but differed in the way they normalised the text. Many lemmatised the passages, while others favoured stemming or using a dictionary of different word forms. In addition, some teams also used the neural retrievers and combined the candidates from these two approaches." (p. 1248)
- "Regarding the results, it is observed that the performance of the systems was very much dependent on the ranker." (p. 1249)
- "It seems that the retriever did not play an important role in the task, since the best system used only BM25 model." (p. 1249)
- "It is also interesting to observe that none of the systems used a learning-to-rank approach." (p. 1249)

### Internal inconsistencies / tensions (checked on page images)

1. **Per-domain models: three vs two.** Text, p. 1249: "Three participants chose this approach, including the winning system." Table IX, p. 1248: "Model per domain = Yes" only for Pokrywka and Ropiak. Karaś selected all passages for Allegro (p. 1248), which is a per-domain candidate setting but not a per-domain model. The paper does not resolve this.
2. **"Many lemmatised."** Only Kozlowski (Morfologik) and Pacanowska explicitly lemmatise. Pokrywka stems, Kazuła uses a word-form dictionary, and Wojtasik, Ropiak and Karaś give no normalisation (p. 1248). So "many" = 2 of 7 explicitly **[computed count]**.
3. **"None … used a learning-to-rank approach"** vs Pacanowska: "logistic regression was used to combine all the results into a final score" (p. 1248). Logistic regression over several ranking features can be read as pointwise learning-to-rank. This is our interpretation; the organisers may mean something narrower.
4. **Pokrywka's normaliser:** "stemming using Polimorf" in the text vs a pystempel link in footnote 12 (p. 1247); see §5.

## 10. Statistical evidence

- **Significance tests:** NOT_REPORTED.
- **Confidence intervals:** NOT_REPORTED.
- **Runs / seeds:** NOT_REPORTED (one final score per team).
- **Ablation:** none. No retriever-only scores, no normalisation ablation, no ranker swap.
- **Per-domain / per-query analysis:** NOT_REPORTED.
- **Overlap / unique relevant hits / oracle union between BM25 and dense candidates:** NOT_REPORTED.
- **Retrieval-stage metrics (Recall@N of the candidate pool):** NOT_REPORTED.

## 11. Strengths

- Open, multi-domain Polish passage-retrieval shared task (public availability of the data is not stated; only a planned repository, Sec. V, p. 1249) with a large Wikipedia corpus (7.1M passages) and two hand-built out-of-domain test sets (law, e-commerce).
- One common metric and a common test set for all systems.
- Short but concrete descriptions of each pipeline, including the lexical normalisation tool when the team reported it.
- Honest about a deficiency of the evaluation (compute cost ignored).
- Shows that real-world Polish systems already combine morphologically normalised BM25, dense retrievers and cross-encoders.

## 12. Limitations

### Stated by the authors

- The evaluation ignores "the computational heaviness of the approaches" (p. 1249).
- The rules allowed per-domain systems despite the cross-domain goal: "Although the goal of the task was to create a system for cross-domain passage retrieval, it was allowed to submit different systems for different domains" (p. 1249). The authors state this as a rule, not as a deficiency; we list it here because it limits the cross-domain interpretation.

### Inferred from the design

1. **End-to-end metric only.** Retriever quality, and thus the effect of lexical normalisation or dense retrieval on candidate coverage, cannot be separated from the ranker.
2. **Many confounds between systems:** ranker size, candidate-pool depth (≈350 to 3,000), external training data, translation to English, per-domain models, ensembles. So the organisers' claim that "the retriever did not play an important role" is not supported by a controlled comparison. A strong retriever may still matter when the ranker is fixed.
3. **No per-domain scores** and no stated aggregation. Normalisation effects that differ by domain (as the sibling card CR000100 reports for lemma vs raw BM25) would be invisible here.
4. **Normalisation not reported for 3 of 7 systems**; BM25 parameters not reported for any.
5. **Relevance labelling is under-described** for the trivia test set (how positives were identified). In the author-built domains, relevance appears to be one constructed passage per question (implied, not stated), which penalises other valid answer passages.
6. **Hybrid combination methods are unspecified.**
7. Single score per system; no variance, significance or confidence intervals.

## 13. What the work proves

- In PolEval 2022/23 Task 3, **all seven submitted Polish QA-retrieval pipelines used BM25 in the first stage**. At least four also used dense retrievers, whose candidates were combined with BM25's (pp. 1247–1248; Table IX).
- Participants used **different morphological normalisations** of the lexical channel: stemming (Polimorf/pystempel), lemmatisation (Morfologik; Pacanowska's unnamed lemmatiser), a word-form dictionary (sjp.pl). One system also used unlemmatised BM25 scores as features (p. 1248).
- The **final NDCG@10 ranking tracks the reranker**: the three mt5-13B systems scored 67.44–69.36, and the MiniLM-L6/mBERT systems 51.71–54.23 (Table IX). As a descriptive pattern this holds; it is not a causal result.
- A **BM25-only first stage with a strong reranker can win** the task overall (69.36; Table IX).

## 14. What the work does NOT prove

- **That the retriever does not matter.** No retriever-level metric and no fixed-ranker comparison exist.
- **That any normalisation (stemming, lemmatisation, dictionary) is better than another, or better than raw forms**, for Polish BM25. There is no controlled comparison and per-team details are missing.
- **That hybrid BM25 + dense candidate generation helps or does not help.** Hybrid and BM25-only systems differ in everything else.
- **Anything about lexical–dense complementarity:** no overlap, unique relevant hits, oracle union or per-query analysis.
- **Anything per domain or per query type.**
- **Statistical reliability** of the differences between teams (e.g., 69.36 vs 68.19).

## 15. Relationship to current Uzbek evidence

- **No Uzbek data.** Polish is inflectional with rich case morphology; Uzbek is agglutinative. Findings do not transfer directly.
- The practice pattern (morphologically normalised BM25 + dense retriever candidates + cross-encoder) matches what the Uzbek RAG/hybrid literature already reports at the component level (`MASTER_INDEX` G: USHRA, O-RAG; D-level Sharifbaev manuscript). Like those, this paper gives **no controlled evidence** on the morphology × complementarity interaction.
- **Polish cluster** (project cards / assignments, not claims from this paper):
  - **CR000100** (Rybak & Ogrodniczuk 2024, Silver Retriever; card completed 2026-09-28). It evaluates raw vs lemma BM25 and dense models on PolQA, Allegro FAQ and Legal Questions. These are the same three domains as PolEval Task 3, and the lemma effect changes sign by domain. This paper does not say whether those are the identical PolEval test sets. **It is the closest controlled Polish evidence in the cluster so far.**
  - **CR000103** (BEIR-PL; card completed 2026-09-28). A single stemmed BM25 vs weak bi-encoders; its Table 6 reports BM25 on PolEval-named datasets (Allegro-FAQ, Legal, Wiki Trivia).
  - **CR000914** (Pacanowska 2023, FedCSIS; card not yet written). This is the 5th-placed system described here. Per its triage record it compares no lemmatisation / spaCy / Morfeusz2 / hybrid lemmatisation for BM25 by NDCG@10, plus BM25/neural/LR fusion and relevant-passage rank depth per lemmatiser. It is likely the most gap-relevant Polish record and should be checked for overlap/unique-hit data.

## 16. Relationship to CURRENT_GAP

**Classification:** *no material effect* on the residual core; weakly *supports* the motivation. It is a *lead* to closer records.

- **Occupied elements it confirms** (already listed as non-claims in v0.8):
  - "morphology-aware BM25 + dense + hybrid pipelines do not exist" is false for Polish practice as well;
  - morphological normalisation of the lexical channel coexists with dense retrieval and candidate fusion in one evaluation setting.
- **Not touched** (v0.8 core):
  - raw → stem → lemma variation of BM25 against a **fixed** dense retriever D;
  - unique relevant hits / overlap between channels;
  - oracle union;
  - incremental hybrid gain;
  - link to query features.
  None is measured; retrieval-stage outcomes are not even reported.
- **Why it still matters:** a public shared task where different morphological normalisations and hybrid candidate generation coexist, yet the organisers could conclude only "it seems that the retriever did not play an important role". That illustrates the evidential vacuum our design targets: end-to-end leaderboards cannot reveal morphology-induced complementarity.

**Proposal:** keep v0.8 refined unchanged. Optionally list this paper in the evidence boundary as a shared-task example ("normalised BM25 + dense candidates + rerankers in Polish, without controlled or complementarity analysis"). This is a proposal only; `CURRENT_GAP.md` has not been edited.

## 17. Implications for our research design

- **Score the first stage separately.** For every lexical variant (raw/stem/lemma), D and each hybrid, report retrieval-stage metrics (Recall@k, unique relevant hits at depth k) **before** any reranker. If a reranker is used at all, keep it fixed across conditions.
- **Keep the pool depth fixed.** Pool depth varied 350–3,000 across teams here; our comparison must use the same k for all channels.
- **Name the normalisation tool exactly.** This paper shows how "stemming using Polimorf" + a pystempel link leaves the actual transformation ambiguous. For Uzbek, name the stemmer/lemmatiser, its version and its tables/dictionary, and report the apostrophe/script normalisation.
- **Specify the hybrid combination.** "Combined the candidates" is not a method. Report union vs score fusion, normalisation, weights and the tuning split.
- **Per-domain reporting.** If the Uzbek benchmark has several domains (e.g., legal / news / FAQ), report each one and state the aggregation.
- **Qrels.** Author-constructed single-passage relevance (legal, FAQ) under-counts valid alternatives. For unique-hit analysis, pool judgments from all channels.
- **Feature idea (hypothesis only):** Pacanowska's use of both lemmatised and unlemmatised BM25 scores as features suggests a "raw + lemma" multi-representation lexical condition. It could be a secondary condition after the main raw/stem/lemma × fixed-D comparison, not a replacement for it.
- **Candidate follow-up source:** PolEval Task 3 data could serve as a cheap non-Uzbek pilot for our overlap/unique-hit pipeline, if its qrels are released. Availability is not stated in this paper; the organisers only plan a repository of datasets (Sec. V, p. 1249).

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| Shared task / evaluation campaign | A competition: organisers fix data and a metric, teams submit systems | Common benchmark with a leaderboard |
| Passage retrieval | Find short text fragments that contain the answer to a question | Rank corpus passages by relevance to the query |
| Retriever vs ranker (reranker) | Retriever: fast first search returning many candidates. Ranker: slower model re-ordering the candidates | First-stage retrieval vs second-stage reranking |
| BM25 | Word-matching score: shared rare words and repeated words raise the score, with document-length correction | Probabilistic relevance framework with k1, b |
| Stemming | Cutting word endings by rules or statistics (e.g., "domami" → "dom") | Heuristic suffix stripping / statistical stem tables |
| Lemmatisation | Replacing each word form with its dictionary form using a morphological analyser | Mapping inflected forms to lemmas |
| Word-form (inflection) dictionary | A list mapping each inflected form to its base form; used to normalise text | Lexicon-based normalisation |
| Dense retriever | Neural model turning question and passage into vectors; close vectors mean relevant | Bi-encoder `sim(Enc(q), Enc(p))` |
| Cross-encoder | Neural model reading question and passage together and outputting one relevance score; accurate but slow | Joint encoding, used for reranking |
| Hybrid (in this paper) | Candidates come from both BM25 and a dense retriever | Candidate-pool combination; method unspecified |
| Learning-to-rank | Training a model to combine many ranking signals into one score | Pointwise / pairwise / listwise ranking models |
| NDCG@10 | How well the top 10 is ordered, with higher positions counting more | DCG@10 / IDCG@10 (Eqs. 5–7) |
| Complementarity (project term) | Each channel finds relevant passages the other misses | Unique relevant hits, overlap, oracle-union gain |

## 19. Open questions / verification needed

1. **Per-domain NDCG@10 and the aggregation rule** (micro vs macro over domains): NOT_REPORTED. They may exist on the PolEval platform. That would be a source outside this paper; use it only if the researcher accepts it as a separate source.
2. **"Three" vs two per-domain-model participants** (p. 1249 vs Table IX, p. 1248): unresolved in the paper.
3. **Normalisation for Wojtasik, Ropiak, Karaś** and BM25 parameters for all teams: NOT_REPORTED. Participants' own system papers (if any in the corpus) would be separate sources.
4. **Pokrywka's normalisation:** stemming vs Polimorf dictionary (text vs footnote 12).
5. **How trivia test positives were determined**, and whether Allegro/legal questions have exactly one relevant passage.
6. **Are the CR000100 test sets (PolQA, Allegro FAQ, Legal Questions) the PolEval 2022/23 Task 3 test sets?** Check in CR000100's card/paper. If yes, CR000100's raw vs lemma BM25 numbers are per-domain retrieval-stage evidence on this exact benchmark.
7. **CR000914 (Pacanowska):** read in full next. Per triage it has a controlled lemmatiser comparison, fusion and rank-depth tables, so it may contain the retrieval-stage evidence missing here.

## 20. Decision after deep dive

- **Keep current gap?** Yes. v0.8 refined remains valid (§16).
- **Modify gap?** No change proposed. Optionally add this paper to the evidence boundary as a Polish shared-task example (researcher's decision).
- **Add decision?** Proposed for `decisions/DECISIONS.md` (researcher's decision): "Retrieval-stage metrics (Recall@k, unique relevant hits at fixed depth k) are reported for every lexical variant, for D and for every hybrid, separately from any reranker; any reranker used is held fixed across conditions."
- **Add experiment?** No new experiment. Possibly a low-cost pilot on PolEval Task 3 data (via CR000914 / CR000100) if public qrels exist; it would test the overlap/unique-hit pipeline on an inflected language.
- **Add citation to Chapter I?** Yes, briefly:
  - §1.3 as an example of practical Polish hybrid pipelines (morphologically normalised BM25 + dense candidates + cross-encoders) evaluated only end-to-end;
  - optionally §1.1 as an illustration of diverse normalisation choices (stemming / lemmatisation / word-form dictionary) in one benchmark.
  Cite as a shared-task overview (B), not as evidence for any normalisation effect.
- **Proposed `MASTER_INDEX.md` row** (to add after approval):

| MORPH-015 | Kobyliński, Ogrodniczuk, Rybak, Przybyła, Pęzik, Mikołajczyk, Janowski, Marcińczuk, Smywiński-Pohl — *PolEval 2022/23 Challenge Tasks and Results* (FedCSIS 2023, ACSIS 35, pp. 1243–1250) — [deep dive](deep-dives/2023_Kobylinski_Ogrodniczuk_PolEval_2022_23_Passage_Retrieval.md) | 2023 | B | MEDIUM | Shared-task overview; Task 3 = Polish QA passage retrieval (5,000 PolQA training questions; tests: trivia 1,291 q, Allegro 900 q / 921 passages, legal >700 q / ≈26k passages; NDCG@10). 7 end-to-end systems (69.36–51.71): all use BM25 with differing normalisation (stemming via Polimorf/pystempel, Morfologik lemmatisation, sjp.pl word-form dictionary, lemmatised + unlemmatised BM25 features; 3 teams not reported); 4 add dense retrievers to the candidate pool. Scores track the reranker (mt5-13B systems 67.44–69.36). No retrieval-stage or per-domain scores, no controlled normalisation or hybrid comparison, no overlap/unique-hit/per-query analysis, no significance tests. Text/table mismatch on per-domain models (3 vs 2). Lead to CR000914 and CR000100. |
