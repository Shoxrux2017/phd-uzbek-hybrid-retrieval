# Dorkin & Sirts (2025): GliLem: Leveraging GliNER for Contextualized Lemmatization in Estonian

**Targeted deep-dive status:** COMPLETED (AI-assisted, pending researcher review)
**Completed:** 2026-09-28
**Verification:** independent AI verifier pass 2026-09-28; 10 findings addressed.
**Literature ID:** `MORPH-043` (assigned 2026-09-28, approved by researcher)
**Systematic-review record:** `CR000179`. Full-text triage: INCLUDE, reading priority HIGH, reading tier "2 — важно", `carries_complementarity_evidence = NO` (confirmed in this card: no dense run, no fusion, no overlap analysis; §10, §16).
**Provenance:** AI-assisted deep dive (Claude). The whole paper (12 PDF pages = printed pp. 86–97; pp. 94–97 are mostly references; there is no appendix) was read from the pdftotext extraction. Page images were checked visually at 110 dpi for every table and figure used here: PDF pp. 4–8 = printed pp. 89 (Figure 1), 90 (Table 1, Sec. 4), 91 (Table 2, Sec. 5.1), 92 (Sec. 5.2–5.3, footnotes 9–11), 93 (Table 3, Sec. 5.4). Every number below comes with its table/section and printed page. Numbers computed by us are marked **[computed]** (recomputed with Python).
**Source rule:** **the paper is the primary and only authoritative source.** The released dataset, the demo and the GliNER / bm25s / Lucene code were **not** consulted as evidence about what the authors did. The web was used only to verify the bibliographic record (marked "bibliographic check"). Background knowledge appears only as "Context (not from the paper)". Statements about other works in our corpus come from our own cards and are labelled as such.
**Reliability:** **B** (researcher may upgrade). The source is a peer-reviewed paper in the ACL Anthology-hosted NoDaLiDa/Baltic-HLT 2025 proceedings, which is A-grade for its lemmatization-accuracy claims (bootstrap CIs, standard UD test split). The IR evidence, which is our reason for reading it, is a secondary experiment:
- one machine-translated collection with no quantitative translation-quality check;
- BM25 with default parameters;
- a single run and no significance test.

---

## Кратко для исследователя (RU)

- **Что сделано.** Для эстонского языка (финно-угорский, богатая словоизменительная морфология) авторы:
  - строят GliLem: нейросетевой модуль снятия неоднозначности лемм для правилового морфоанализатора Vabamorf на базе open-vocabulary NER-модели GliNER;
  - затем проверяют, как нормализация токенов влияет на лексический поиск BM25 (библиотека bm25s, параметры по умолчанию) на коллекции DBpedia-Entity v2, машинно переведённой на эстонский (NLLB 3.3B): 467 запросов, ≈4.5 млн документов.
- **Морфологические варианты лексического канала есть: 4 представления** (Sec. 5.2, p. 92):
  - словоформы (Identity, «только токенизация»);
  - стемминг (эстонский стеммер Apache Lucene);
  - леммы Vabamorf с его HMM-снятием неоднозначности;
  - леммы Vabamorf с GliLem-снятием неоднозначности.
- **Точность лемматизации** (Table 2, p. 91, тест UD EDT): Vabamorf-HMM 0.892 → GliLem 0.977 (+8.5 п. **[computed]**); оракул Vabamorf 0.993.
- **Главные числа поиска** (Table 3, p. 93):
  - Recall@100: словоформы 0.2212, стемминг 0.2167, Vabamorf 0.2831, GliLem 0.2935;
  - Success@100: 0.6681 / 0.6767 / 0.7901 / 0.7837;
  - MAP@100: 0.0874 / 0.0856 / 0.1057 / 0.1115.
  - Картина: **словоформы ≈ стемминг < леммы** (при k = 5 и k = 100, а также MAP@1/Success@1; исключение — Recall@1, где леммы Vabamorf ниже обоих: 0.0218 против 0.0269/0.0260). Лемматизация против стемминга: +6.6 п. Recall@100 (+30.6% отн.), +11.3 п. Success@100 **[computed]**.
- **Более точная лемматизация даёт мало:**
  - GliLem против Vabamorf: +1.04 п. Recall@100, +0.58 п. MAP@100;
  - на MAP@5, Success@5 и Success@100 GliLem **хуже** Vabamorf **[computed]**;
  - авторы признают, что рост точности лемматизации «do not easily translate into significantly better IR results» (p. 93), но статистического теста нет.
- **Стемминг фактически не отличается от словоформ.** Авторы объясняют это слабостью стеммера Lucene для эстонского (p. 93). Альтернативный стеммер не проверялся, степень склейки словаря не сообщается. Поэтому «лемма > стем» здесь означает «лемма > слабый стеммер ≈ словоформы».
- **Чего нет (измерения gap):**
  - плотного поиска нет: он упоминается только в мотивации;
  - fusion/гибрида нет;
  - перекрытия, уникально найденных релевантных документов и oracle union нет;
  - разбора по запросам нет, хотя в DBpedia-Entity есть 4 типа запросов (p. 91).
  - Нет тестов значимости для поиска и нескольких прогонов. Градуированные оценки 0/1/2 сведены к бинарным.
- **Неточности в самой статье:**
  - в разделе 4.3 для pattern-based классификатора дано 96.2% (это значение **dev**), тогда как GliLem 97.7% и Vabamorf 89.2% взяты из **test**; тестовое значение классификатора 0.966;
  - во введении «ca 10% improvement» лемматизации над стеммингом не соответствует ни абсолютным (от −0.42 до +11.34 п.), ни относительным (от −16.2% до +30.6%) разницам по Table 3 **[computed]**;
  - дополнительный прирост GliLem «около 1%» по Recall и MAP (p. 93): для MAP@100 это лишь +0.58 п.;
  - доверительный интервал Vabamorf на dev [0.877, 0.883] несимметричен вокруг 0.878.
- **Не сообщается (NOT_REPORTED):**
  - токенизатор и регистр для Identity;
  - какие поля документа индексировались;
  - k1/b;
  - применялся ли анализатор Lucene целиком (с приведением к нижнему регистру и стоп-словами) или только стеммер.
  - Из-за этого варианты могут различаться не только морфологией.
- **Для нашего gap:** работа — ещё один свежий пример сравнения raw/stem/lemma для BM25 в морфологически богатом языке (такая новизна уже отвергнута в v0.8). Ядро v0.8 (raw/stem/lemma × фиксированная D → overlap / уникальные находки → прирост гибрида → признаки запросов) **не затрагивает**.
  - Ценно, что авторы **прямо формулируют как непроверенную гипотезу**, что лемматизация может помочь именно в гибридном поиске на большой глубине k (p. 93–94). Это поддерживает актуальность нашего вопроса.
  - Предложение: gap не менять.
- **Практическая польза для нас:**
  1. Вариант «стем» надо проверять на реальную склейку словаря (размер словаря индекса, доля склеенных форм), иначе он совпадает с raw.
  2. Неморфологическую предобработку (токенизатор, регистр, апострофы, стоп-слова) держать одинаковой во всех вариантах.
  3. Точность лемматизатора — вторичный фактор. Можно добавить вариант «lemma_alt» (другой узбекский лемматизатор) как проверку чувствительности.
  4. Переведённая коллекция — только пилот, не замена узбекским qrels.
  5. Лемматизация большого корпуса дорога (>50 ч × ~30 процессов CPU на 4.5 млн документов, p. 94): лемматизировать один раз и кешировать.

---

## 1. Bibliographic record

- **Authors:** Aleksei Dorkin, Kairit Sirts
- **Affiliation:** Institute of Computer Science, University of Tartu (both)
- **Year:** 2025
- **Venue:** *Proceedings of the Joint 25th Nordic Conference on Computational Linguistics and 11th Baltic Conference on Human Language Technologies (NoDaLiDa/Baltic-HLT 2025)*, March 3–4, 2025 (printed on p. 86)
- **Pages:** 86–97 (printed on p. 86)
- **Publisher:** University of Tartu Library (printed on p. 86: "©2025 University of Tartu Library")
- **Editors:** Richard Johansson, Sara Stymne (bibliographic check: ACL Anthology record)
- **Place:** Tallinn, Estonia (bibliographic check: ACL Anthology record)
- **ISBN:** 978-9908-53-109-0 (bibliographic check: ACL Anthology record)
- **ACL Anthology ID:** `2025.nodalida-1.10`; official record https://aclanthology.org/2025.nodalida-1.10/ (bibliographic check: ACL Anthology record). **DOI:** none listed on the Anthology page.
- **Preprint:** arXiv:2412.20597 (bibliographic check: web search result; the arXiv version was not compared with the proceedings version)
- **Released resources (stated in the paper):**
  - demo: `huggingface.co/spaces/adorkin/GliLem` (footnote 1, p. 86);
  - Estonian IR dataset: `huggingface.co/datasets/adorkin/dbpedia-entity-est` (footnote 3, p. 87).
- **Funding:** Estonian Research Council Grant PSG721 (Acknowledgments, p. 94)
- **Source type:** peer-reviewed regional conference paper (12 pages including references; the paper type, long or short, is not stated in the paper or the Anthology record)
- **Reliability:** B (see header)
- **Full text available:** yes (`07_full_text/pdfs/CR000179.pdf`, 12 pages)

## 2. Why this work matters to the PhD

It is a **recent (2025) controlled comparison of lexical representations for BM25** in a morphologically rich, lower-resource European language. It has two features that most older raw/stem/lemma studies lack:

1. **Two lemmatizers of different accuracy** built on the same analyzer (Vabamorf-HMM 89.2% vs Vabamorf+GliLem 97.7%). This lets one ask how much *lemmatizer quality*, rather than lemmatization as such, matters for retrieval.
2. An **explicit hybrid-retrieval motivation**. The authors argue that lemmatization helps most at high k, "typical in hybrid IR systems" (p. 93). They then stop short of running a dense or hybrid system.

How it relates to each project axis:

| Axis | Relation |
|---|---|
| Lexical retrieval | Direct: BM25 (bm25s) over four token representations (Identity, Lucene stem, Vabamorf lemma, GliLem lemma) |
| Semantic retrieval | **Absent.** Dense retrieval appears only in the introduction and motivation (pp. 86, 91, 92) |
| Hybrid retrieval | **Absent.** Only argued as a use case for high-k lexical recall (pp. 93–94) |
| Uzbek morphology | Indirect. Estonian is Uralic (Finnic), not Turkic, but shares rich suffixal inflection. The typological comparison is our context, not from the paper |
| Low-resource retrieval | Direct: no native Estonian IR benchmark existed, so the authors built one by machine translation (p. 91) |
| Current gap | Background / supporting. It occupies "raw/stem/lemma BM25 in a morphologically rich language" again, but not the morphology → complementarity core (§16) |

## 3. Research problem

### Simple explanation

A lemmatizer turns each word into its dictionary form ("running" → "run"). In Estonian, one word can have many forms, and the rule-based analyzer Vabamorf often proposes several possible dictionary forms for one word. Its built-in chooser only looks at the neighbouring word and often picks the wrong one. The authors ask two questions:

1. Can a modern neural model choose the right candidate better?
2. Does better lemmatization make keyword search (BM25) find more relevant documents?

### Formal formulation

Two research questions (Introduction, p. 87; paraphrased):

- **RQ1 (lemmatization):** can a GliNER-based span-labelling model disambiguate Vabamorf's lemma candidates better than Vabamorf's HMM disambiguator? This is measured as token-level lemmatization accuracy on Estonian UD EDT.
- **RQ2 (downstream IR):** what is the impact of improved lemma disambiguation accuracy on BM25 retrieval effectiveness, compared with no normalization and stemming?

The IR task is **entity search**. Given a query, rank DBpedia entity documents (title plus description) from a ≈4.5M-document collection (Sec. 5.1, p. 91).

## 4. Main idea

### Simple explanation

Vabamorf lists possible lemmas for each word. Each candidate is rewritten as a small "edit rule" (for example, "remove the last letter"). GliNER, a model built to match text spans with free-text labels, is trained to pick, for each word, the rule that fits the sentence. Applying the chosen rule gives the lemma. Then the whole translated collection and its queries are lemmatized, and BM25 is run over the lemmas instead of the original word forms.

### Concrete example

- The paper's own illustration is Figure 1 (p. 89), an English example: input "running man studies" with candidate labels `remove_ning` and `replace_ies_y`.
- GliNER scores every (span, label) pair: "running" × `remove_ning` = 0.9, "studies" × `replace_ies_y` = 0.8 (highlighted); "man" scores only 0.1 / 0.2. Our reading (not stated in the figure): "running" → "run", "studies" → "study", and "man" receives no rule, i.e. stays in the default "do nothing" state (Sec. 4.1, p. 90).
- In retrieval terms: a query containing an inflected form can match a document containing another inflected form of the same lemma, once both are reduced to the lemma.

### Formal method

- **Lemma as transformation rule** (Sec. 3, p. 88): following Straka (2018), each form → lemma pair is encoded as a *shortest edit script* over characters, i.e. a string label. Examples are in Table 1, p. 90: `↓0;d¦` "Do nothing" (49.6% of train tokens), `↓0;d¦-` "Remove the last letter" (7.0%), `↑0¦↓1;d¦` "Upper case the first letter" (3.7%).
- **Candidate restriction** (Sec. 3, p. 89): at inference, only the rules corresponding to Vabamorf's lemma candidates for the current text are passed to GliNER as "entity types". This bounds the label set by the text rather than by the full rule vocabulary.
- **GliNER scoring** (Sec. 2.2, p. 88): a BERT-like encoder processes `[ENT] label₁ [ENT] label₂ … [SEP] text` jointly ("in a cross-encoder fashion"). Span and entity heads (feed-forward layers) produce embeddings, and spans are assigned labels by similarity scores.
- **"Do nothing" as the default class** (Sec. 4.1, p. 90): it is not used as a label. Tokens whose lemma equals the surface form are left unlabelled.

## 5. Architecture / algorithm

1. **Vabamorf analysis** (Sec. 2.1, p. 88): a rule-based Estonian analyzer, used via EstNLTK. It outputs one or more analyses per token. The token "can be a word or a punctuation mark" (p. 86). Its built-in HMM disambiguator conditions only on the previous word's analysis (p. 88).
2. **GliLem training** (Sec. 4.1, p. 90):
   - data: Estonian UD EDT v2.14 with its predefined splits;
   - **Vabamorf is not used during training**: gold token/lemma pairs are converted into rule labels;
   - model: the official GliNER training script with **default parameters**, starting from "the multilingual version of the pretrained model" (the exact checkpoint name is NOT_REPORTED).
3. **GliLem inference:** Vabamorf candidates → rule strings → GliNER scores the spans → apply the best rule. The score threshold and tie handling are NOT_REPORTED.
4. **Comparison systems for lemmatization** (Sec. 4, pp. 89–90):
   - Vabamorf + HMM;
   - Oracle Vabamorf (correct if the gold lemma is among the candidates; "unusable in a practical scenario", footnote 2, p. 87);
   - pattern-based token classification with adapter fine-tuning (Houlsby et al., 2019), which does not use Vabamorf. Its encoder and training details are NOT_REPORTED beyond "adapter-based parameter efficient fine-tuning".
5. **Collection translation** (Sec. 5.1, p. 91):
   - documents and queries of DBpedia-Entity v2 both translated (presumably separately; the paper does not say) with NLLB-200 3.3B (footnote 6; the text says "NLLB 3B") via CTranslate2;
   - ≈2 days on one A100.
   - How long documents were segmented or truncated for MT: NOT_REPORTED.
6. **Four lexical representations** (Sec. 5.2, p. 92):
   1. Identity ("only tokenization is applied"). The tokenizer is NOT_REPORTED.
   2. Stemming with "the Estonian Stemmer available in Apache Lucene". Footnote 10 links the Lucene `EstonianAnalyzer` class page, so whether the full analyzer or only its stemmer was applied is ambiguous.
   3. Vabamorf lemmas (HMM disambiguation).
   4. Vabamorf lemmas (GliLem disambiguation).
   - The token-classification lemmatizer is excluded from IR (footnote 9, p. 92).
   - Context (not from the paper): Lucene documents `EstonianAnalyzer` as a chain of standard tokenization, lowercasing, Estonian stop-word removal and a Snowball Estonian stemmer. If the whole analyzer was used, the Stemming condition would differ from Identity in lowercasing and stop-words as well as stemming. The paper does not say which was used.
7. **BM25 indexing / retrieval** (Sec. 5.2, p. 92):
   - bm25s library, "default parameters";
   - library preprocessing is bypassed: "we input the corpus preprocessed by us directly";
   - tokens are joined with whitespace and indexed (≈3 min per variant);
   - queries get the same preprocessing; the top **100** documents are retrieved per query.
   - k1, b and the BM25 variant: NOT_REPORTED. Context (not from the paper): the bm25s defaults are k1 = 1.5, b = 0.75, "lucene" scoring variant; these may have been the values, but the paper does not say.
8. **Qrels:** the original English DBpedia-Entity judgments are reused, keeping "only the documents deemed relevant or highly relevant" (p. 92), i.e. binarized at ≥1.
9. **Cost** (Sec. 5.4, p. 94): applying either disambiguator to the 4.5M documents "took over 50 hours for each", with about 30 concurrent CPU processes. GliNER batching cannot use per-example label sets, so GPU acceleration is hard; the Vabamorf disambiguator "cannot be accelerated at all".

## 6. Data

### Lemmatization: Estonian UD EDT v2.14 (Sec. 4.1, p. 90)

- **Language / domain:** Estonian treebank (EDT). The domain composition is not described in the paper.
- **Split:** the predefined UD train/dev/test.
- **Split sizes: NOT_REPORTED.**
- **Preprocessing relative to Dorkin & Sirts (2023):** no lowercasing; derivational symbols in lemmas are kept; UD version 2.10 → 2.14 (Sec. 4.2, p. 90).
- **Minor inconsistency in the paper:** the text says UD v2.14 (p. 90), but the cited reference (Zeman et al., 2023, p. 97) is "Universal dependencies 2.12".
- **Rule distribution:** "do nothing" covers 49.6% of train tokens; the top 6 rules cover 71.6% **[computed]** (Table 1, p. 90).

### IR: DBpedia-Entity v2, machine-translated to Estonian (Sec. 5.1–5.2, pp. 91–92)

- **Source:** DBpedia-Entity v2 (Hasibi et al., 2017), an English entity-search test collection over the DBpedia 2015-10 dump.
- **Queries:** 467. There are four query types (p. 91):
  1. short ambiguous named-entity queries;
  2. IR-style keyword queries;
  3. list-of-entities queries;
  4. natural-language questions.
  Whether all 467 queries were evaluated is not stated explicitly; "for each query" (p. 92) suggests so.
- **Documents:** ≈4.5 million entity documents. Each has an ID, a title and a variable-length description (p. 91). **Which fields were indexed: NOT_REPORTED.**
- **Relevance judgments:** graded (2 highly relevant, 1 relevant, 0 irrelevant) in the original English collection, **binarized** here (≥1 = relevant). No Estonian re-judging: relevance is assumed to survive translation. The number of relevant documents per query is NOT_REPORTED.
- **Train/dev/test:** none. The IR part is evaluation-only (no training, no tuning reported).
- **Translation quality:** "At this time, we did not perform any quantitative quality evaluation of the resulting translations" (p. 91). A "small sample" was manually examined; its size is NOT_REPORTED. The authors report:
  - noisy source entries (empty entries, long listings, mixed scripts);
  - query translation errors, "such as the presence of non-existent words" (p. 93).
- **Release:** `adorkin/dbpedia-entity-est` (footnote 3, p. 87). The authors call it "the first IR dataset for Estonian" (p. 87).

## 7. Baselines

| Baseline | What it is | Why selected | Fair comparison? |
|---|---|---|---|
| Vabamorf + HMM (lemmatization) | The existing default disambiguator | Direct target of improvement | Yes: same candidates, same test set |
| Oracle Vabamorf | Upper bound: correct if any candidate is correct | Shows the headroom for disambiguation | Not a system, a ceiling |
| Pattern-based token classification (adapters) | Neural lemmatizer that does not use Vabamorf | "a simple, efficient, and computationally cheap baseline" (p. 90) | Reasonable, but **not** the strongest prior system: the generative model reported best by Dorkin & Sirts (2023) is deliberately not reproduced because it needs disambiguated morphology as input (p. 90) |
| BM25 Identity | BM25 over word forms | "Baseline" in Table 3 | Tokenizer, case and punctuation handling are NOT_REPORTED |
| BM25 + Lucene Estonian stemming | Algorithmic stemming | Standard cheap normalization | **Weak.** The authors themselves call the stemmer "very weak for Estonian" (p. 93). No second stemmer and no conflation statistics. Possibly also differs from Identity in case/stop-words (§5) |
| BM25 + Vabamorf-HMM lemmas | Lemmatized index | Reference for the GliLem effect | Yes: same analyzer and candidates; only the disambiguator differs |

No dense, learned-sparse or hybrid baseline is included, although the introduction cites dense–lexical complementarity (Gao et al., 2021; Lee et al., 2023; p. 86).

## 8. Metrics

| Metric | Definition (as described, Sec. 5.3, pp. 92–93) | Simple meaning | Appropriate? |
|---|---|---|---|
| Success@k | 1 if at least one relevant document is in the top k, averaged over queries | "Did the user get at least one useful result in the first k?" | Yes as a lenient view; coarse (authors' own caveat, p. 92) |
| Recall@k | Share of all relevant documents for the query found in the top k, averaged | "What fraction of everything relevant is in the top k?" | Useful for first-stage candidate generation. Bounded by k/\|R\| when a query has many relevant documents (footnote 11, p. 92) |
| MAP@k | Mean average precision truncated at k | Rewards relevant documents ranked high | Standard. MAP@1 = Success@1 by definition here (p. 93), and Table 3 confirms they are identical |

- The authors' rationale for Recall is hard to follow. The text says Recall suits their case "because only a small proportion of the total number of documents is annotated … and therefore the Recall will be upper bounded only with very small k values" (p. 92). The illustrating footnote 11 describes the opposite case (1000 relevant documents, k = 100 → Recall ≤ 0.1). This is a rationale-clarity issue, not a numeric inconsistency.
- **Not used:** nDCG (graded qrels are discarded), MRR, Recall@1000.
- Context (not from the paper): nDCG@10/@100 is the usual headline metric for DBpedia-Entity v2, so the numbers here are not comparable with published English or BEIR DBpedia results.

## 9. Results

### Table 2: lemmatization accuracy, bootstrap estimates with 95% CI (p. 91)

| Method | Dev | Test |
|---|---|---|
| Vabamorf (HMM) | 0.878 [0.877, 0.883] | 0.892 [0.889, 0.895] |
| Oracle Vabamorf | 0.992 [0.992, 0.993] | 0.993 [0.992, 0.994] |
| Pattern-based Token Classification | 0.962 [0.960, 0.964] | 0.966 [0.964, 0.968] |
| **GliLem** | **0.974 [0.973, 0.976]** | **0.977 [0.975, 0.978]** |

Reading the table **[computed]**:
- GliLem vs Vabamorf: +8.5 points on test (+9.5% relative) and +9.6 points on dev (+10.9% relative). This removes 78.7% of Vabamorf's errors on both splits. The abstract's "by 10%" (p. 86) fits the dev figures and is approximate for test.
- Oracle headroom: Vabamorf 10.1 points below the oracle on test (11.4 on dev), consistent with "more than 10% lower" (p. 88). GliLem is 1.6 points below on test, consistent with "less than 2%" (p. 90).
- GliLem vs token classification: +1.1 points on test, +1.2 points on dev. The CIs do not overlap on either split.
- **Internal inconsistency (Sec. 4.3, p. 90 vs Table 2, p. 91):** the text says the token-classification model "reached 96.2% accuracy", which is the **dev** value. In the same paragraph GliLem (97.7%) and Vabamorf (89.2%) are **test** values; the test value for token classification is 0.966. The "ca 1.2% in absolute" difference is likewise the dev difference (test: 1.1).
- **Minor oddity:** Vabamorf dev point estimate 0.878 lies near the lower end of its CI [0.877, 0.883]. The other rows are roughly centred. We cannot tell from the paper whether this is a typo.

### Table 3: BM25 retrieval on translated DBpedia-Entity (p. 93)

| Metric | Baseline (Identity) | Stemming (Lucene) | Vabamorf (HMM) | GliLem |
|---|---:|---:|---:|---:|
| Recall@1 | 0.0269 | 0.0260 | 0.0218 | **0.0278** |
| Recall@5 | 0.0633 | 0.0627 | 0.0702 | **0.0734** |
| Recall@100 | 0.2212 | 0.2167 | 0.2831 | **0.2935** |
| MAP@1 | 0.2077 | 0.2120 | 0.2527 | **0.2591** |
| MAP@5 | 0.1201 | 0.1312 | **0.1596** | 0.1577 |
| MAP@100 | 0.0874 | 0.0856 | 0.1057 | **0.1115** |
| Success@1 | 0.2077 | 0.2120 | 0.2527 | **0.2591** |
| Success@5 | 0.3704 | 0.4004 | **0.4925** | 0.4797 |
| Success@100 | 0.6681 | 0.6767 | **0.7901** | 0.7837 |

Bold as printed. Single run; no significance marks.

Differences **[computed]**, in absolute points (relative %):

| Metric | Stem − Identity | Vabamorf − Stem | GliLem − Stem | GliLem − Vabamorf |
|---|---|---|---|---|
| Recall@1 | −0.09 (−3.3%) | −0.42 (−16.2%) | +0.18 (+6.9%) | +0.60 (+27.5%) |
| Recall@5 | −0.06 (−0.9%) | +0.75 (+12.0%) | +1.07 (+17.1%) | +0.32 (+4.6%) |
| Recall@100 | −0.45 (−2.0%) | +6.64 (+30.6%) | +7.68 (+35.4%) | +1.04 (+3.7%) |
| MAP@1 = Success@1 | +0.43 (+2.1%) | +4.07 (+19.2%) | +4.71 (+22.2%) | +0.64 (+2.5%) |
| MAP@5 | +1.11 (+9.2%) | +2.84 (+21.6%) | +2.65 (+20.2%) | −0.19 (−1.2%) |
| MAP@100 | −0.18 (−2.1%) | +2.01 (+23.5%) | +2.59 (+30.3%) | +0.58 (+5.5%) |
| Success@5 | +3.00 (+8.1%) | +9.21 (+23.0%) | +7.93 (+19.8%) | −1.28 (−2.6%) |
| Success@100 | +0.86 (+1.3%) | +11.34 (+16.8%) | +10.70 (+15.8%) | −0.64 (−0.8%) |

Checking the authors' claims (Sec. 5.4, p. 93):
- "k = 1: MAP and Success improve more than 4% [lemmatization over stemming]": +4.07 points (Vabamorf) and +4.71 (GliLem) ✓. The "%" here means **absolute points**, as in all of Sec. 5.4.
- "k = 5: Recall about 1%, MAP about 3%, Success about 9% [Stemming → Vabamorf]": +0.75 / +2.84 / +9.21 points ✓.
- "k = 100: Recall ca 7%, MAP about 2%, Success about 11%": +6.64 / +2.01 / +11.34 points ✓.
- "GliLem … additional improvement of ca 1% in both Recall and MAP" at k = 100: Recall@100 +1.04 ✓; MAP@100 **+0.58**, so "ca 1%" overstates MAP.
- "small but consistent improvements in Recall for all values of k, with the improvement being the most pronounced in the highest k setting" (GliLem vs Vabamorf): consistent across k ✓. "Most pronounced at the highest k" holds in **absolute** points (+1.04 at k = 100 vs +0.60 / +0.32). In **relative** terms the largest gain is at k = 1 (+27.5%).
- Introduction (p. 87): "ca 10% improvement in retrieval metrics when using Vabamorf lemmatization over stemming, with an additional 1% gain". Neither reading supports "ca 10%" in general. Absolute differences range from −0.42 to +11.34 points; relative from −16.2% to +30.6%. Only Success@5 / Success@100 absolute gains (9.2 / 11.3 points) are near 10. This is imprecise framing, not a table error.
- "the baseline of using word forms is on the same level with stemming on all measures" (p. 93): the largest gap is +3.00 points on Success@5; elsewhere ≤ 1.11 points ✓ (approximately).
- **Pattern worth noting [inference]:** Vabamorf lemmas *lower* Recall@1 (0.0218 vs 0.0260 stem) while *raising* Success@1 (0.2527 vs 0.2120). Recall@k divides by each query's number of relevant documents, so this suggests lemmatization gains at rank 1 come mostly from queries with many relevant documents. Per-query data would be needed to confirm this.
- **Coverage view [computed]:** Success@100 shows that 33.2% of queries have *no* relevant document in the top 100 with Identity, vs 21.0% with Vabamorf lemmas (1 − 0.6681, 1 − 0.7901). Mean Recall@100 is still below 0.30 for all variants.

### Other reported facts

- Indexing took ≈3 minutes per variant (p. 92). Each disambiguator took >50 h on ≈30 CPU processes for 4.5M documents (p. 94), ≈1,500 process-hours per disambiguator **[computed, approximate]**.

## 10. Statistical evidence

- **Significance test:**
  - Lemmatization: none formal, but 95% bootstrap CIs are given (Table 2). The number of bootstrap resamples is NOT_REPORTED.
  - IR: **NOT_REPORTED.** No paired test for any Table 3 comparison. The phrase "do not easily translate into significantly better IR results" (p. 93) is not backed by a test.
- **Confidence intervals:** lemmatization only. **None for IR.**
- **Runs / seeds:** NOT_REPORTED. It is presumably a single run for both GliLem training and IR, since no variance is shown.
- **Ablation:** none for GliLem (e.g., no ablation of candidate restriction, multilingual initialisation or the "do nothing" default). The four IR conditions form a representation comparison, not an ablation of one pipeline.
- **Per-query analysis:** **none.**
  - No per-query wins/losses between representations.
  - No per-query-type results, although the collection has four labelled query types (p. 91).
  - No overlap or unique relevant hits between representations or with any other channel.
  - No oracle union.
  - No link to query features (length, entity presence, inflection).
- **Translation robustness:** the authors *believe* that noise "affects each approach similarly, and thus the relative ranking between the preprocessing methods remains stable" (p. 94). This is untested.

## 11. Strengths

- A clean comparison of **two lemmatizers built on the same analyzer's candidates**, so the IR effect of disambiguation quality is isolated from the analyzer.
- Honest reporting that the large accuracy gain yields only a small IR gain, including metrics where GliLem is worse (MAP@5, Success@5, Success@100).
- A realistic scale: ≈4.5M documents, which is large for a lower-resource-language BM25 study.
- Library preprocessing of bm25s is explicitly bypassed ("we input the corpus preprocessed by us directly", p. 92), so the library's own preprocessing does not alter the representation conditions.
- Bootstrap CIs for the lemmatization accuracies.
- Released dataset and demo (footnotes 1, 3).
- Explicit discussion of compute cost (p. 94), which is relevant to practical deployment of lemmatized indexing.

## 12. Limitations

### Stated by the authors

- No quantitative evaluation of translation quality; the translation is "far from perfect" (pp. 91–92).
- The source DBpedia-Entity corpus is noisy (empty entries, long listings, mixed scripts), and the queries contain translation errors (p. 93).
- The small IR effect of better lemmatization may be partly due to this noise; improving the dataset is future work (pp. 93–94).
- The Lucene Estonian stemmer is "very weak for Estonian" (p. 93).
- Lemmatization accuracy is skewed upwards because most tokens need no change (p. 90). The text says "the majority of corpus tokens"; Table 1 gives 49.6% "do nothing" in the train split, i.e. about half.
- Both disambiguators are computationally intensive, and GliNER batching cannot use per-example label sets (p. 94).
- The generative lemmatizer that was best in prior work is not reproduced (p. 90). The authors present this as a design choice with a rationale (it needs disambiguated input); calling it a limitation is our framing.

### Inferred from the experimental design

1. **Stem ≈ raw.** With one weak stemmer and no conflation statistics (vocabulary size, share of merged forms), "lemma > stem" cannot be generalized to "lemma > stemming" for Estonian.
2. **Possible multi-factor differences between conditions.** The Identity tokenizer, lowercasing, punctuation handling and stop-words are not reported for any condition. Stemming may have used the full Lucene analyzer (§5). Lemmas can keep capital letters (Table 1 includes an "Upper case the first letter" rule; the lemmatization data are not lowercased, p. 90). The conditions may therefore differ in more than morphology.
3. **No IR significance testing and a single run**, so GliLem-vs-Vabamorf differences of 0.2–1.3 points are of unknown reliability on 467 queries.
4. **Machine-translated collection with transferred qrels.** Documents and queries were translated independently, so the same English term may be rendered with different Estonian lemmas or forms. Lemmatization may partly be repairing MT-induced variation rather than natural morphological variation. Relevance is assumed to survive translation. Effects on native Estonian text are untested.
5. **Graded judgments discarded**, and no nDCG. MAP@1 and Success@1 duplicate each other.
6. **Low absolute effectiveness** (Recall@100 < 0.30, MAP@100 < 0.12; maxima 0.2935 and 0.1115). Many relevant documents are never retrieved at depth 100, which limits what the representation comparison can reveal.
7. **Default BM25 parameters** (unspecified k1/b), not tuned per representation. The optimal length normalization may differ between raw and lemma indexes.
8. **The hybrid argument is untested.** The claim that high-k recall gains matter "in hybrid IR systems" (p. 93) and the conclusion that lemmatization "might translate into actual improvements in a hybrid information retrieval setting" (p. 94) are hypotheses. No dense retriever or fusion is run.
9. **No query-level analysis**, despite labelled query types, so it is unknown on which queries lemmatization helps or hurts.

## 13. What the work proves

- **GliLem improves Vabamorf lemma disambiguation substantially** on Estonian UD EDT: test accuracy 0.977 vs 0.892, with non-overlapping 95% bootstrap CIs (Table 2). It also slightly exceeds a pattern-based token-classification lemmatizer (0.977 vs 0.966 test).
- **On this translated DBpedia-Entity collection, with default bm25s, lemmatized BM25 scores higher than both Identity and Lucene-stemmed BM25 at k = 5 and k = 100 and on MAP@1 / Success@1** (Table 3):
  - Recall@100 0.2831–0.2935 vs 0.2167–0.2212;
  - Success@100 0.7837–0.7901 vs 0.6681–0.6767;
  - MAP@100 0.1057–0.1115 vs 0.0856–0.0874.
  - Exception: on Recall@1, Vabamorf lemmas are *below* both (0.0218 vs 0.0269 / 0.0260), and GliLem is only marginally above (0.0278).
  - Caveat: no significance test and a single run. The margins at k = 100 are large (≈6–12 points on Recall@100 / Success@100), but their statistical reliability is untested, and they hold only *for this collection*.
- **The Lucene Estonian stemmer performs at the level of no normalization** in this setting (Table 3).
- **A large gain in lemmatization accuracy (+8.5 points) gives only a small and mixed BM25 gain:**
  - +1.04 points Recall@100 and +0.58 points MAP@100;
  - small losses on MAP@5, Success@5 and Success@100 (Table 3).

## 14. What the work does NOT prove

- **That lemmatization beats stemming in Estonian in general.** Only one stemmer was used, which the authors call very weak and which performs like no normalization.
- **That GliLem's IR gains over Vabamorf are real.** No significance test, single run, and mixed direction across metrics.
- **That the effects hold on native (non-translated) Estonian text** or with native relevance judgments.
- **Anything about dense retrieval, hybrid retrieval or lexical–dense complementarity.** No dense run, no fusion, no overlap / unique-hit / oracle-union analysis. The hybrid statements are motivation and speculation (pp. 86, 93–94).
- **Which queries or query types benefit from lemmatization, or why.** No per-query or per-type analysis.
- **That the representation conditions differ only in morphology.** Tokenization, case and stop-word handling are not reported.
- **That the ranking of preprocessing methods is robust to translation noise.** This is the authors' belief (p. 94), not a tested result.

## 15. Relationship to current Uzbek evidence

- **No Uzbek data.** Estonian (Uralic, Finnic) and Uzbek (Turkic) are unrelated but both are suffix-heavy with many inflected forms per lemma. That is our typological context, not a claim of the paper. Direct transfer of effect sizes is not justified.
- **Parallel to Uzbek resources.** Uzbek also has a rule-based or hybrid morphological analyzer tradition (Bakaev, Xusainova, Elov, Turayev in `MASTER_INDEX` C). The national cards report *analyzer accuracy* (e.g., Xusainova's 97.5%), not retrieval effectiveness. This paper is a clear demonstration that **analyzer or lemmatizer accuracy and IR gain are different quantities**: +8.5 accuracy points became ≈+1 Recall@100 point. That strengthens the project's existing distinction "analyzer accuracy ≠ IR effectiveness" (GAP_BOUNDARY §2.1–2.3).
- **Related entries in our corpus** (from our own cards; summaries, not re-verified here):
  - **CR000452, Kettunen, Kunttu & Järvelin 2005 (Finnish, INQUERY).** Plain words far below Snowball stemming and FINTWOL lemmatization; lemmatization ≈ inflectional stem generation. Finnish is Estonian's closest relative in our corpus. There Snowball stemming clearly beat plain words, unlike Lucene's Estonian stemmer here, which reinforces that "stem" results depend on the specific stemmer.
  - **CR000914, Pacanowska 2023 (Polish, BM25).** There the *disambiguation strategy* of lemmas changed BM25 NDCG@10 by ≈4 points (21.15 → 25.24). Here a much larger accuracy gain changed BM25 by ≈1 point. Together they suggest that the IR impact of lemma disambiguation is setting-dependent.
  - **CR000103, Wojtasik et al. 2024 (BEIR-PL).** Another machine-translated benchmark that includes DBPedia, with BM25 and a Polish stemmer, and similar caveats about translation noise and transferred qrels.
- **Uzbek MT feasibility.** Context (not from the paper): NLLB-200 covers Northern Uzbek (Latin script), so the same translate-DBpedia route is technically available for Uzbek. The limitations above apply, and any such collection would suit only pilots.

## 16. Relationship to CURRENT_GAP

**Classification:** *supports* (motivation) + *no material effect on the residual core*.

- **Already-occupied claims it touches** (all listed as REJECTED novelty claims in GAP_BOUNDARY §4):
  - "raw/stem/lemma has not been compared in low-resource IR";
  - "morphology-aware BM25 is unstudied".
  This paper is one more 2025 citation for them, specifically for a Uralic language and with two lemmatizers of different accuracy.
- **Supports the relevance of the v0.8 question.** The authors explicitly argue:
  - that lemmatization's value lies in **high-k first-stage recall for hybrid systems** (p. 93);
  - that it "might translate into actual improvements in a hybrid information retrieval setting" (p. 94).
  They leave this **untested**. A 2025 peer-reviewed paper thus names, as an open question, the link our core addresses (morphological representation → contribution in a hybrid with a dense channel). It supports the gap's relevance; it does not establish its absence.
- **Elements of v0.8 refined not touched:**
  - a fixed dense comparator D;
  - lexical-only and dense-only unique relevant hits;
  - overlap;
  - oracle union;
  - incremental hybrid gain;
  - per-query changes across raw → stem → lemma;
  - relation to query features.
  None is present.
- **A possible refinement to consider (researcher's decision):** the paper suggests a secondary factor within the "lemma" condition, *lemmatizer quality*. v0.8 treats "lemma" as one condition. The core need not change, but the design could note that "lemma" results are conditional on the chosen Uzbek lemmatizer (§17).

**Proposal:** keep v0.8 refined unchanged. Optionally cite this paper in the evidence boundary as a 2025 example where raw/stem/lemma BM25 is compared and hybrid benefit is *hypothesized but not tested*. This is a proposal only; `CURRENT_GAP.md` has not been edited.

## 17. Implications for our research design

- **Morphology preprocessing.**
  - For each lexical variant, report index vocabulary size, the share of merged forms (conflation rate) and the mean number of distinct query terms. This guards against a "stem" condition that is effectively "raw", as here.
  - If the first Uzbek stemmer barely conflates, add a second stemmer or a fixed-prefix truncation control (cf. Haddad & Bechikh Ali, MORPH-002).
  - Treat **lemmatizer quality** as a secondary, measured factor:
    - report the chosen Uzbek lemmatizer's accuracy on a small gold sample *from our own corpus*, not only published accuracy;
    - optionally add a `BM25_lemma_alt` robustness condition with a second lemmatizer (e.g., from the national analyzers), reported separately from the primary raw/stem/lemma comparison.
- **Hold non-morphological preprocessing constant.** Use one tokenizer, one lowercasing rule, one apostrophe / Unicode normalization (o‘/g‘ variants; see the bm25s default-tokenizer check in the Mekonnen card, `CR000149`), one stop-word policy (none or a fixed Uzbek list) and one punctuation-filtering rule for **all** variants. Only the term-normalization step may differ. Fix and report k1/b. Bypass library preprocessing, as the authors did.
- **Dataset / qrels.**
  - Machine-translating an English collection (e.g., DBpedia-Entity, via NLLB) into Uzbek could give a cheap *pilot* for the pipeline, not the main benchmark:
    - translation can inject or remove morphological variation;
    - qrels are transferred rather than judged;
    - the authors could not quantify translation quality.
  - Keep graded judgments and report nDCG as well as binary metrics.
- **Query taxonomy.** DBpedia-Entity's four query types (named entity, keyword, list, natural-language question) are a ready-made coarse taxonomy. Our Uzbek query set should label comparable types, so that raw → lemma changes can be analysed per type. The paper shows the cost of not doing so.
- **Metrics.**
  - Report Recall@100 and deeper recall (@1000) for candidate coverage.
  - Report Success@k for "any relevant found", and state that Recall@k is bounded by k/|R|.
  - Avoid reporting both MAP@1 and Success@1, which are identical.
  - Use "points" vs "%" consistently: the paper's "%" means absolute points in Sec. 5.4 but is ambiguous in the introduction.
- **Statistics.** Paired per-query tests (or bootstrap CIs) for every lexical-variant comparison. Small lemmatizer-quality effects (≈1 point) will need them.
- **Compute planning.** Lemmatizing 4.5M documents took >50 h × ≈30 CPU processes per disambiguator. Lemmatize the Uzbek corpus once, cache the token streams per variant, and record the lemmatizer version.
- **Hypothesis.** The paper motivates, but does not test, our expectation that morphology effects are most visible at high k in the lexical channel's candidate set. This fits our plan to measure unique relevant hits and oracle union at depth k with a fixed D, where the gains should show if they exist.
- **Optional pilot.** The public Estonian collection (`adorkin/dbpedia-entity-est`) already has the four lexical variants defined. Adding a fixed multilingual dense D and fusion would give a ready testbed for our overlap / unique-hit / oracle-union measurements. Cost caveat: dense-encoding ≈4.5M documents is substantial, and a subsampled corpus would change the task.

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| Lemmatization | Reduce a word to its dictionary form ("studies" → "study") | Map token *w* in context to lemma *l(w)* |
| Stemming | Chop word endings by rules, without a dictionary; the result may not be a real word | Algorithmic suffix stripping (here: Lucene Estonian stemmer) |
| Lemma disambiguation | Pick the right dictionary form when several are possible for a word | Select one of the analyzer's candidate analyses given context |
| Vabamorf | Rule-based Estonian morphological analyzer with a simple HMM chooser | Analyzer + HMM disambiguator (previous-word context), via EstNLTK |
| Oracle mode | Count as correct if *any* candidate is right: an upper bound, not a usable system | Accuracy of candidate-set membership |
| Transformation rule / shortest edit script | A compact recipe for turning a word into its lemma ("remove last letter") | Minimal character-edit sequence, encoded as a label (Straka, 2018) |
| GliNER | A model that matches text spans to labels written in plain language | Encoder with span and label heads, scoring (span, label) similarity (Zaratiana et al., 2024) |
| GliLem | GliNER trained to choose among Vabamorf's candidate rules | Span-labelling disambiguator over candidate transformation rules |
| BM25 / bm25s | Classic keyword ranking; bm25s is a fast Python implementation | Probabilistic relevance scoring with k1, b |
| Identity (raw) representation | Index words exactly as they appear (after tokenization) | Index terms = surface tokens |
| Entity search | Find the knowledge-base entities (e.g., Wikipedia-like entries) that answer a query | Rank entity documents for a query |
| Machine-translated benchmark | An existing test collection automatically translated into another language | Translated queries/documents with transferred qrels |
| Success@k | Did at least one relevant result appear in the top k? | 1[∃ relevant in top k], averaged |
| Recall@k | Share of all relevant documents found in the top k | \|relevant ∩ top k\| / \|relevant\|, averaged |
| MAP@k | Rewards relevant results placed high, up to rank k | Mean of truncated average precision |
| Bootstrap CI | Uncertainty range from resampling the test items | Percentile interval of resampled accuracy |
| Conflation rate (our term) | How many different word forms a normalizer merges into one index term | e.g., 1 − \|normalized vocabulary\| / \|surface vocabulary\| |
| Complementarity (project term) | Each channel finds some relevant documents the other misses | Unique relevant hits, overlap, oracle-union gain |

## 19. Open questions / verification needed

1. **Stemming condition:** was only the Lucene Estonian stemmer applied, or the full `EstonianAnalyzer` (lowercasing, stop-words)? What tokenizer and case handling were used for Identity and the lemma conditions? NOT_REPORTED; only the authors can confirm.
2. **Indexed fields** (title, description or both) and MT segmentation of long descriptions: NOT_REPORTED.
3. **BM25 k1/b and variant** (bm25s defaults assumed, not stated).
4. **Number of evaluated queries** (all 467?) and the number of relevant documents per query after binarization: NOT_REPORTED.
5. **Token-classification accuracy quoted in the text** (96.2%) vs the Table 2 test value (0.966): the text mixes dev and test values (§9).
6. **Vabamorf dev CI** asymmetry (0.878 in [0.877, 0.883]): typo or genuine?
7. **Significance of GliLem vs Vabamorf in IR:** could be computed from the released dataset plus re-running the four BM25 variants, but only if the preprocessing details above are recovered.
8. **The proceedings version vs arXiv:2412.20597** were not compared.
8a. **UD version:** the text says v2.14 (p. 90), the reference list cites UD 2.12 (p. 97). Probably a stale citation; only the authors can confirm.
9. **Lead:** Dorkin & Sirts (2024), *Sõnajaht* (*SEM 2024), cited on p. 91 as dense Estonian retrieval (reverse dictionary). It is not an ad hoc IR benchmark, but worth checking in the systematic-review records for any lexical–dense comparison.

## 20. Decision after deep dive

- **Keep current gap?** Yes. v0.8 refined remains valid (§16).
- **Modify gap?** No change proposed. Optionally (researcher's decision), cite in the evidence boundary as a 2025 example where raw/stem/lemma BM25 is compared and a hybrid benefit of lemmatization is *hypothesized but not tested*.
- **Add decision?** Proposed for `decisions/DECISIONS.md` (researcher's decision):
  - "For every lexical variant, report conflation statistics (index vocabulary size, share of merged forms); all non-morphological preprocessing (tokenizer, case, apostrophe / Unicode normalization, stop-words, punctuation) is identical across variants";
  - "Report the accuracy of the chosen Uzbek lemmatizer on a gold sample from the evaluation corpus; lemmatizer accuracy is not a proxy for IR gain".
- **Add experiment?**
  - Optional secondary condition `BM25_lemma_alt` (a second Uzbek lemmatizer) as a sensitivity check, reported separately from the primary raw/stem/lemma × fixed D comparison.
  - Optional methodology dry run on the public Estonian translated DBpedia-Entity (four lexical variants + fixed multilingual D + fusion + overlap / unique hits), subject to compute cost.
- **Add citation to Chapter I?** Yes:
  - §1.1: morphological normalization for BM25 in a morphologically rich language; lemmatization > weak stemming ≈ raw; lemmatizer accuracy ≠ IR gain;
  - §1.3: as an example of a recent study that motivates lemmatization by hybrid first-stage recall but does not evaluate a hybrid or complementarity.
- **Proposed `MASTER_INDEX.md` row** (to add after approval):

| MORPH-043 | Dorkin & Sirts — *GliLem: Leveraging GliNER for Contextualized Lemmatization in Estonian* (NoDaLiDa/Baltic-HLT 2025, pp. 86–97) — [deep dive](deep-dives/2025_Dorkin_Sirts_GliLem_Estonian_Lemmatization_IR.md) | 2025 | B | HIGH | Estonian: GliNER-based disambiguation of Vabamorf lemmas (UD EDT test accuracy 0.892 → 0.977) and BM25 (bm25s, defaults) on machine-translated DBpedia-Entity (467 queries, ≈4.5M docs) over Identity / Lucene stem / Vabamorf lemma / GliLem lemma. Raw ≈ weak stem < lemma (Recall@100 0.221/0.217 vs 0.283/0.294; Success@100 0.668/0.677 vs 0.790/0.784). A +8.5-point accuracy gain gives only ≈+1 point Recall@100 and mixed MAP/Success. Hybrid benefit argued but not tested. No dense, fusion, overlap/unique-hit or per-query analysis; no IR significance tests; non-morphological preprocessing not reported. |
