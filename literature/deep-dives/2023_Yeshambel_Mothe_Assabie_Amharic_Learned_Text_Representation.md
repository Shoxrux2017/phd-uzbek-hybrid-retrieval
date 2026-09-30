# Yeshambel, Mothe & Assabie (2023): Learned Text Representation for Amharic Information Retrieval and Natural Language Processing

**Targeted deep-dive status:** COMPLETED (AI-assisted, pending researcher review)
**Completed:** 2026-09-28
**Literature ID:** `MORPH-010` (assigned 2026-09-28, approved by researcher)
**Systematic-review record:** `CR000427`. Full-text triage: INCLUDE, reading priority HIGH, reading tier 1 («прямо по теме пробела»), `carries_complementarity_evidence = NO`
**Provenance:** AI-assisted deep dive (Claude). The whole 23-page article was read. The pdftotext layer is unusable on pp. 5–8 and 15–18: an earlier draft ("x FOR PEER REVIEW") is overlaid on the final text, so those pages were read only from page images. Pages checked visually (110 dpi): **5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19**. These include Tables 1–13, Figures 1–6 and Equations 1–13. Every number below comes with its table/figure/section and printed page (the printed page number equals the PDF page). Numbers computed by us are marked **[computed]** and were recomputed with Python.
**Verification:** independent AI verifier pass 2026-09-28; 7 findings addressed.
**Source rule:** **the paper is the primary and only authoritative source.** The web was used only to check the bibliographic record (MDPI article page). No code, website or later paper is used as evidence about what the authors did.
**Reliability:** **B**. The paper is peer-reviewed (MDPI *Information*, open-access journal; received 15 Jan 2023, accepted 3 Mar 2023). The evidence is weaker than A for these reasons:
- no significance testing;
- no unexpanded word/stem/root baselines in the paper itself;
- the ranking-model parameters are not reported;
- several internal inconsistencies (§19).

---

## Кратко для исследователя (RU)

- **Что сделано.** Для амхарского языка (семитский, корне-шаблонная морфология) авторы обучили статические эмбеддинги слов (word2vec, GloVe, fastText) и BERT-base модели (MLM, NSP). Каждая модель обучена в трёх вариантах: на **словоформах, стеммах и корнях** тестовой коллекции 2AIRTC (6069 документов, 240 запросов; Sec. 4.2, p. 12).
  - Затем эмбеддинги используются для **расширения запроса** (query expansion): к каждому термину добавляются 10 ближайших по косинусу слов.
  - Поиск выполняется в Lemur: языковая модель, KL-дивергенция, точное совпадение терминов (Sec. 3.4.1, p. 10).
- **Главные числа** (Tables 7–9, pp. 16–17, проверено по изображениям):
  - лучший вариант — fastText skip-gram на словоформах: P@5 0.60, P@10 0.56, nDCG 0.75, R-prec 0.49, bpref 0.47;
  - тот же fastText на стеммах: P@5 0.32, на корнях: 0.37.
  - Во всех пяти конфигурациях эмбеддингов порядок один и тот же: **словоформы > корни > стеммы**.
  - Против «Conventional» без расширения (Table 12, p. 19): MAP 0.43 → 0.51, nDCG 0.65 → 0.75.
- **Чего нет:**
  - BM25 нет (ранжирование — языковая модель Lemur);
  - плотного поиска (dense retrieval) нет: эмбеддинги используются только для добавления терминов в лексический запрос, поиск остаётся лексическим;
  - fusion/гибрида нет;
  - перекрытия, уникально найденных документов, oracle union нет;
  - анализа по запросам и статистических тестов нет.
- **Главный методический изъян для нас.** Базовые запуски **без расширения** для стеммов и корней в статье не приведены. «Conventional» дан одной строкой; из текста следует, что он взят из работы [46], и форма представления для него явно не указана. Поэтому нельзя отделить эффект морфологического представления индекса от эффекта расширения: при смене представления меняются одновременно индекс, словарь эмбеддингов и сами расширения.
- **Интересный механизм (качественно, Tables 10–11, pp. 17–18).** На словоформах ближайшие соседи fastText — в основном **морфологические варианты** термина запроса. Эмбеддинговое расширение, по сути, выполняет роль обучаемой морфологической нормализации. На корнях варианты не возвращаются вовсе. Это прямо касается нашего вопроса о перекрытии «морфологической нормализации» и «семантического» компонента, но количественно не измерено.
- **Внутренние несоответствия:**
  - формула Accuracy (Eq. 7, p. 13) = (TP+FP)/(...) — ошибка;
  - утверждение, что fine-tuned BERT лучше на словоформах, и вывод «word-based лучше во всех задачах» противоречат p. 15: стем/корневые fine-tuned модели не оценивались;
  - утверждение «BERT значимо превзошёл все эмбеддинги в IR» сравнивает F1 классификации с метриками ранжирования, без статистического теста;
  - в Sec. 4.5 50 пар NSP «выбраны случайно», в Sec. 5.1.1 — «вручную»;
  - MAP и recall объявлены как метрики, но в Tables 7–9 их нет.
- **Для нашего gap:** работа подтверждает, что сравнение raw/stem/root при добавлении «семантического» компонента для морфологически богатого языка ограниченных ресурсов уже было (**supports / narrows**). Ядро v0.8 (raw/stem/lemma BM25 × фиксированная D → перекрытие / уникальные попадания → прирост гибрида → признаки запросов) **не затрагивает**. Предложение: gap не менять.
- **Практическая польза:**
  1. Всегда давать базовые запуски без семантического компонента для каждого морфологического варианта, иначе интерпретация невозможна.
  2. Не переобучать семантический компонент под каждый вариант: фиксированная D в v0.8 устраняет именно этот конфаунд.
  3. Дешёвый дополнительный контроль для узбекского: «raw + fastText-расширение», чтобы проверить, насколько эмбеддинговое расширение дублирует лемматизацию.
  4. Не делать вывод «нормализация помогает» для узбекского априори: здесь нормализация проиграла.

---

## 1. Bibliographic record

- **Authors:** Tilahun Yeshambel (IT Doctoral Program, Addis Ababa University; corresponding author), Josiane Mothe (IRIT, UMR5505 CNRS, Université de Toulouse Jean-Jaurès), Yaregal Assabie (Dept. of Computer Science, Addis Ababa University) (p. 1)
- **Year:** 2023
- **Venue:** *Information* (MDPI), Vol. 14, Issue 3, Article 195; 23 pages
- **Dates:** Received 15 January 2023; Revised 17 February 2023; Accepted 3 March 2023; Published 20 March 2023 (p. 1)
- **Academic editor:** Kostas Stefanidis (p. 1)
- **DOI:** `10.3390/info14030195`
- **Official record:** https://www.mdpi.com/2078-2489/14/3/195 (bibliographic check: MDPI article page; title, authors, volume 14, issue 3, article 195, DOI and 20 March 2023 publication date confirmed)
- **Resources (stated in paper):** https://www.irit.fr/AmharicResources/ (datasets) and https://www.irit.fr/AmharicResources/amharic-pre-trained-language-models/ (models, tokenizers) (pp. 12, 19)
- **Funding:** none (p. 21)
- **Source type:** peer-reviewed open-access journal article (CC BY 4.0)
- **Reliability:** B
- **Full text available:** yes (`07_full_text/pdfs/CR000427.pdf`, 23 pages)

## 2. Why this work matters to the PhD

It is one of the few studies, in a morphologically rich low-resource language, that hold one test collection fixed and vary the **morphological representation** of the lexical index. It varies **word (surface form) / stem / root** and at the same time adds a **learned-representation component** (static embeddings used for query expansion).

| Axis | Relation |
|---|---|
| Lexical retrieval | Lemur language-model retrieval (KL divergence) with exact term matching over word-, stem- and root-based indexes. **No BM25** |
| Semantic retrieval | **Only indirect.** Static embeddings (word2vec / GloVe / fastText) are used to *add terms* to the lexical query. There is no dense retrieval channel. BERT is used for relevance *classification*, not ranking (authors' own statement, p. 20) |
| Hybrid retrieval | **Absent** as fusion. Embedding-based query expansion is a query-side integration of distributional similarity into lexical retrieval, not a hybrid of two ranked lists |
| Uzbek morphology | Indirect. Amharic is Semitic and non-concatenative; its "root" level has no direct Uzbek analogue. Its word/stem contrast is transferable in spirit |
| Low-resource retrieval | Direct: small corpus (6069 docs), 240 queries. Earlier Amharic embeddings/XLMR exist, but the authors describe most as not publicly accessible or cross-lingual (p. 5); they release word/stem/root-specific embeddings and BERT models |
| Current gap | Supports / narrows. It shows a morphology × learned-representation interaction at the query-expansion level. It does **not** measure lexical–semantic complementarity (§16) |

## 3. Research problem

### Simple explanation

Amharic words appear in many inflected forms, and, according to the authors, "usable pre-trained models for automatic Amharic text processing are not available" (Abstract, p. 1). Earlier models exist, but most are not publicly accessible or were trained for cross-lingual purposes (p. 5). The authors build word embeddings and BERT models for Amharic and ask three questions:

- Do these models help search when used to add related words to the query?
- Do they help a few classification tasks?
- Does it matter whether text is represented as full words, as stems or as roots?

### Formal formulation

The paper has no numbered research questions. Its stated activities (Sec. 1, p. 3) are:

- (i) train Amharic word embeddings, a BERT WordPiece tokenizer and BERT models, and "explore their effects on surface words, stems, and roots";
- (ii) design "an Amharic IR system considering the morphology of the language" and investigate the usability of the trained embeddings for IR (TREC ad hoc framework);
- (iii) verify BERT on language modeling and some NLP tasks.

Contribution (iii) on p. 5 is the "investigation of the effects of roots, stems, and surface words on learned text representations".

The IR task is **ad hoc document retrieval**:
- query Q (240 topics);
- collection D (6069 documents);
- ranking by `KL(Q_θ, D_θ)` after expanding Q with embedding neighbours.

## 4. Main idea

### Simple explanation

Train word vectors on the collection itself, once for each form of the text (words, stems, roots). For each query word, take the 10 most similar words from the vector model and add them to the query. Then run ordinary term-matching search and see which text form and which embedding method gives the best results.

### Concrete example

These are the paper's own examples (Sec. 5.2, pp. 17–18; Tables 10–11, p. 18).

- Query term **የፖለቲካ** /jəpolətika/ 'of politics' (example given in the p. 17 text only). The paper attributes it to "word-based learned text representation" and does not name the embedding model. The expansions include:
  - variants of the same word: 'of politics and', 'politics', ...;
  - forms of the related word **ፓርቲ** 'party': 'the parties', 'by the parties', ...
- In a separate point about fastText specifically, the authors conclude: "Most expanded terms of fastText are morphological variants" (p. 17). Table 10 (p. 18) lists fastText expansions for five other query terms (e.g., በሽታ 'disease').
- In the root-based representation, "none of the expanded terms were variants to one of the query terms" (p. 17).
- Out-of-vocabulary case: the query term **አገልግሎት** 'services' does not occur in the corpus, so word2vec and GloVe return no expansions. fastText does return some, through its character n-grams (p. 18).

### Formal method

- **Cosine similarity for the neighbours** (Eq. 4, p. 10): `cos(x,y) = Σ x_i y_i / (Σ x_i² Σ y_i²)`.
  - As printed, the denominator lacks the square roots of the standard cosine. This is probably a typesetting error, since the text calls it "cosine similarity". Taken literally, it would rank neighbours differently. Which form was actually used is not verifiable from the paper. **[our observation]**
- **Ranking** (Eq. 5, p. 10): `KL(Q_θ, D_θ) = Σ_{w∈V} p(w|Q_θ) log [p(w|Q_θ) / p(w|D_θ)]`, where `p(w|D_θ)` is "the smoothed probability of a term seen in the document". The smoothing method and its parameters are **NOT_REPORTED**.
- **Expansion rule** (p. 10):
  - 10 neighbours per query term;
  - duplicates removed;
  - final query = original terms + expanded terms.
  - Term weighting of expansions vs original terms is **NOT_REPORTED**.

## 5. Architecture / algorithm

1. **Preprocessing** (Sec. 3.2, pp. 5–6):
   - removal of tags, punctuation, function words and non-Amharic characters;
   - normalization of homophonous Amharic characters (e.g., ሐ, ኀ, ኸ → ሀ; ሠ → ሰ; ፀ → ጸ; ዐ → አ, with their orders);
   - sentence segmentation on "።"; whitespace tokenization.
2. **Three parallel corpora** (Sec. 4.2, p. 12):
   - word-based (2AIRTC [50]);
   - stem-based and root-based, "built by [51]" (a SIGIR 2021 resource paper, *Morphologically annotated Amharic text corpora*).
   - How queries were converted to stems/roots is **NOT_REPORTED**. The text says only that "documents and user information needs were morphologically processed before indexing and query expansion" (p. 16).
   - Figure 4 (p. 10) shows "Morphological Analysis" and "Stopword Removal" boxes for both document and query processing. Stop-word lists are stem-based and root-based [46] (p. 10).
   - Yet p. 15 states "there was no usable Amharic stemmer and morphological analyzer to extract stems and roots from labeled dataset" (§19).
3. **Static embeddings** (Sec. 3.3.1 and Table 2, pp. 7–8, checked visually):

   | Model | Vector size | Window | Epochs | Min count | LR |
   |---|---:|---:|---:|---:|---:|
   | word2vec | 300 | 5 | 20 | 3 | 0.05 |
   | GloVe | 100 | 10 | 30 | 5 | 0.05 |
   | fastText | 100 | 5 | 30 | 5 | 0.05 |

   - fastText uses character n-grams of length 3–5 (p. 8).
   - CBOW and skip-gram variants are reported for word2vec and fastText.
   - Libraries: Gensim, GloVe, fastText (p. 12).
   - All models are trained **on the same 6069 documents that form the retrieval collection** (p. 12).
4. **BERT** (Sec. 3.3.2, 4.3–4.4 and Table 3, pp. 8–12):
   - standard BERT-base: 12 layers, hidden size 768, 12 attention heads, 110M parameters, max length 512, batch 16, Adam, LR 1e-5; 5 and 10 epochs;
   - WordPiece vocabularies of 252,605 (word), 49,817 (stem) and 46,995 (root) (p. 12);
   - the "default BERT vocabulary size" of BERT-base-uncased (30,522) was "resized" (p. 9). Whether weights were initialised from English BERT or trained from scratch is **not stated clearly**; Sec. 4 speaks of "existing pre-trained English language models ... adapted for Amharic" (p. 11).
5. **IR pipeline** (Sec. 3.4.1 and Fig. 4, p. 10; Sec. 4.1, pp. 11–12):
   - Lemur toolkit builds word/stem/root indexes;
   - expanded queries are run against the index of the matching representation;
   - evaluation with trec_eval.
   - Retrieval depth (number of documents retrieved per query) is **NOT_REPORTED**.
6. **Classification fine-tuning** (Sec. 3.4.2, p. 11; Sec. 5.1.2, p. 15):
   - word-based MLM + classification head;
   - (a) subject classification: 11 labels, 1189 documents;
   - (b) query–document relevance classification: `[CLS] q [SEP] d [SEP]`, 50 queries, 5514 documents from 2AIRTC qrels;
   - 17 epochs.
   - Train/validation split sizes and whether queries are disjoint between them: **NOT_REPORTED**.

## 6. Data

- **Dataset/corpus:** 2AIRTC (Amharic ad hoc IR test collection [50]), in word-, stem- and root-based versions [51] (Sec. 4.2, p. 12).
- **Language / domain:** Amharic. The domain of the IR collection is not described in this paper. The 1189-document classification set comes from news agencies, the web and Amharic Wikipedia (p. 12).
- **Size:** "Each of these datasets has 6069 documents and 240 queries"; 72,814 sentences; 1,592,351 words (p. 12). That gives ≈262 words per document on average **[computed]**.
  - Figure 2 (p. 7), "Distribution of words in the corpus", has an x-axis "Document length" ranging 0–5000 with a mode near 800–1000 and a spike at 5000. Its unit is not stated. It is hard to reconcile with ≈262 words per document unless the unit is characters or tokens (§19).
- **Queries:** 240 topics. Topic fields used (title/description) are **NOT_REPORTED**.
- **Relevance judgments:** 2AIRTC qrels. Pooling depth, judges and graded vs binary relevance are **NOT_REPORTED here**. The authors use bpref, a metric designed for incomplete judgments, and attribute the P@5 → P@10 drop to "an insufficient relevant number of documents" (p. 17).
- **Train/dev/test:** no split for IR. The embeddings are trained on all documents of the test collection (unsupervised; no qrels used). For the relevance classifier, splits are **NOT_REPORTED**.
- **How labels were produced:** IR qrels from 2AIRTC (not described). The subject labels are "manually labeled" (p. 11).

## 7. Baselines

| Baseline | What it is | Why selected | Fair comparison? |
|---|---|---|---|
| "Conventional" (Table 12, p. 19) | Retrieval without query expansion. The text says fastText skip-gram "outperforms the baseline retrieval performance reported in [46]" (p. 18) | Shows the gain of QE | **Unclear.** The representation (word/stem/root) is not named in the table. It appears to be carried over from an earlier paper [46] (KDIR 2020), so identical settings (index, smoothing, stop-words, topic set) are not demonstrated in this paper |
| Word2vec / GloVe / fastText QE compared with each other | Alternative static embeddings | Most common embedding methods (p. 1) | Partly. Vector sizes differ (300 vs 100) and so do windows and epochs (Table 2); no tuning is reported |
| Word vs stem vs root (each with QE) | Alternative morphological representations | Main controlled contrast | **Confounded.** The index, the stop-word list, the embedding training corpus and vocabulary, and the expansions all change together. **No unexpanded stem/root runs are reported in this paper** |
| BM25, dense retrieval, PRF (pseudo-relevance feedback) expansion | — | — | **Absent.** In particular, no classical PRF query expansion is compared with embedding-based expansion |

## 8. Metrics

| Metric | Definition (paper) | Simple meaning | Appropriate? |
|---|---|---|---|
| P@5, P@10 (P@15, P@20 only in Table 12) | Share of relevant docs in the top k (Eq. 8, p. 13) | "How many of the first k results are relevant?" | Yes, top-heavy |
| R-prec | Precision at rank R = number of relevant docs for the topic (p. 13) | Precision at a query-specific cutoff | Yes |
| nDCG ("ndcg") | Eq. 11, p. 13; **cutoff k NOT_REPORTED** | Rank-discounted gain, normalized | Yes, but k unknown |
| bpref | Eq. 13, p. 14 | Penalizes judged non-relevant docs ranked above relevant ones; ignores unjudged docs | Yes for incomplete qrels |
| MAP | Eq. 10, p. 13 | Mean of per-query average precision | Announced in Secs. 3.4.1 and 4.5, but **reported only in Table 12**, not in Tables 7–9 |
| Recall | Eq. 9, p. 13 | Share of all relevant docs retrieved | Announced but **never reported** |
| Accuracy (NSP) | Eq. 7, p. 13: `(TP+FP)/(TP+FP+TN+FN)` | Share of correct predictions | **The formula as printed is wrong** (the numerator should be TP+TN) |
| F1 (weighted), loss | Eq. 12, p. 14 | Classification quality | For the classification tasks only |

Significance tests: **none** (§10).

## 9. Results

All values below were checked on the page images.

### Table 7: QE with word2vec (p. 16)

| Representation | CBOW P@5 | P@10 | ndcg | R-prec | bpref | Skip-gram P@5 | P@10 | ndcg | R-prec | bpref |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Word-based | 0.53 | 0.51 | 0.70 | 0.45 | 0.43 | 0.53 | 0.51 | 0.70 | 0.45 | 0.43 |
| Stem-based | 0.40 | 0.35 | 0.55 | 0.32 | 0.30 | 0.40 | 0.35 | 0.55 | 0.32 | 0.30 |
| Root-based | 0.45 | 0.40 | 0.66 | 0.38 | 0.36 | 0.44 | 0.38 | 0.66 | 0.36 | 0.35 |

- CBOW and skip-gram rows are **identical to two decimals on all five metrics** for word- and stem-based runs. This is possible but unusual; the paper does not comment on it (§19).

### Table 8: QE with GloVe (p. 16)

| Representation | P@5 | P@10 | ndcg | R-prec | bpref |
|---|---:|---:|---:|---:|---:|
| Word-based | 0.54 | 0.50 | 0.70 | 0.45 | 0.43 |
| Stem-based | 0.36 | 0.34 | 0.55 | 0.32 | 0.29 |
| Root-based | 0.41 | 0.38 | 0.66 | 0.37 | 0.34 |

### Table 9: QE with fastText (p. 17)

| Representation | CBOW P@5 | P@10 | ndcg | R-Prec | bpref | Skip-gram P@5 | P@10 | ndcg | R-Prec | bpref |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Word-based | 0.50 | 0.44 | 0.66 | 0.37 | 0.34 | **0.60** | **0.56** | **0.75** | **0.49** | **0.47** |
| Stem-based | 0.30 | 0.27 | 0.51 | 0.26 | 0.22 | 0.32 | 0.30 | 0.52 | 0.26 | 0.23 |
| Root-based | 0.34 | 0.30 | 0.62 | 0.32 | 0.29 | 0.37 | 0.33 | 0.62 | 0.32 | 0.29 |

### Table 12: without vs with QE (fastText, p. 19)

| Technique | P@5 | P@10 | P@15 | P@20 | MAP | ndcg | R-Prec |
|---|---:|---:|---:|---:|---:|---:|---:|
| Conventional | 0.56 | 0.49 | 0.44 | 0.40 | 0.43 | 0.65 | 0.43 |
| With query expansion | 0.60 | 0.56 | 0.50 | 0.47 | 0.51 | 0.75 | 0.49 |

- The "With query expansion" row equals the Table 9 fastText skip-gram word-based row on the four shared metrics. Table 12 adds P@15, P@20 and MAP.
- Gains **[computed]**:

  | Metric | Absolute gain | Relative gain |
  |---|---:|---:|
  | P@5 | +0.04 | +7.1% |
  | P@10 | +0.07 | +14.3% |
  | MAP | +0.08 | +18.6% |
  | ndcg | +0.10 | +15.4% |
  | R-Prec | +0.06 | +14.0% |

- The paper states no relative gains, so there is nothing to re-check.

### Reading the tables [computed]

- **Order word > root > stem holds in every one of the five embedding configurations and on every metric.** The authors' claim (p. 17) is confirmed.
- Word vs stem gap: from −0.13 to −0.28 P@5 (−24.5% to −46.7% relative). The largest gap is for fastText skip-gram.
- Word vs root gap on ndcg is small for the classical embeddings: −0.04 (−5.7%) for word2vec and GloVe.
- Root vs stem: root is higher by 0.03–0.05 on P@5/P@10 and by 0.10–0.11 on ndcg.
- **"fastText outperforms other word embeddings on word-based corpus"** (Abstract, p. 1; p. 17) holds **only for skip-gram**:
  - fastText CBOW word-based (0.50 / 0.44 / 0.66 / 0.37 / 0.34) is **below** word2vec (0.53 / 0.51 / 0.70 / 0.45 / 0.43) and GloVe (0.54 / 0.50 / 0.70 / 0.45 / 0.43);
  - on stem- and root-based corpora both fastText variants are below word2vec and GloVe (e.g., stem P@5 0.30–0.32 vs 0.36–0.40).
- **Comparison with "Conventional"** (only if Conventional is comparable; see §7) on P@5 / P@10 / ndcg / R-prec:
  - word2vec: −0.03 / +0.02 / +0.05 / +0.02;
  - GloVe: −0.02 / +0.01 / +0.05 / +0.02;
  - fastText CBOW: −0.06 / −0.05 / +0.01 / −0.06, i.e. **worse than no expansion** on three of four metrics.
  - Only fastText skip-gram improves every shared metric. The paper does not discuss this.
- **Whether stem/root QE runs are better or worse than stem/root runs without QE cannot be determined from this paper**: no such baseline is reported.

### BERT and classification results (pp. 14–16)

| Result | Location | Values |
|---|---|---|
| MLM training loss, epoch 5 / epoch 10 | Table 4, p. 14 | word 0.253 / 0.480; stem 0.458 / 0.497; root 0.507 / 0.614 |
| NSP accuracy, epoch 5 / epoch 10 | Table 5, p. 15 | word 0.68 / 0.52; stem 0.66 / 0.64; root 0.64 / 0.60 |
| NSP testing loss, epoch 5 | Table 5, p. 15 | word 0.307; stem 0.652; root 0.654 |
| Subject classification (word-based) | Table 6, p. 16 | F1 0.91, accuracy 0.89 |
| Relevance classification (word-based) | Table 6, p. 16 | F1 0.97, accuracy 0.95 |

- NSP evaluation uses 50 sentence pairs (25 adjacent, 25 non-adjacent; p. 13). One pair is 0.02 accuracy, so word vs stem vs root at epoch 5 differ by **one pair each** (0.68 / 0.66 / 0.64) **[computed]**.
- MLM training losses are compared across vocabularies of very different size (252,605 vs 49,817 vs 46,995; ratio ≈5.1–5.4× **[computed]**). Such losses are not directly comparable measures of representation quality **[our inference]**.
- The MLM training loss *rises* from epoch 5 to epoch 10 for all three corpora. That is unusual for a training loss and is not explained.

## 10. Statistical evidence

- **Significance test:** NOT_REPORTED. No test for any retrieval or classification comparison. The word "significantly" in "On Amharic IR, BERT significantly outperformed all embedding algorithms" (p. 19) is not backed by any test.
- **Confidence intervals:** NOT_REPORTED.
- **Runs / seeds:** NOT_REPORTED (presumably single runs).
- **Ablation:**
  - no unexpanded stem/root runs;
  - no variation of the number of expansion terms (fixed at 10);
  - no expansion-term weighting;
  - no PRF comparison.
  The CBOW vs skip-gram contrast is the only design variation within a model.
- **Per-query analysis:** **none quantitative.** Tables 10–11 (p. 18) give qualitative expansion lists for 5 query terms and for 1 query term respectively. None of the following is reported:
  - per-query win/loss;
  - any query-feature breakdown;
  - overlap or unique relevant documents between representations or between the expanded and unexpanded run;
  - an oracle union.

## 11. Strengths

- **One fixed collection and topic set** (6069 documents, 240 queries) with **three morphological representations** (word / stem / root), each with its own index, stop-word list and embedding/tokenizer. This is a rare, clean *representation* contrast for a Semitic language.
- Three embedding families and two training objectives. The pattern word > root > stem is consistent across all of them.
- Standard TREC tooling (Lemur, trec_eval) and bpref, which suits incomplete judgments.
- Public release of the models: 9 embedding models, WordPiece and BPE tokenizers, MLM and NSP models for each representation (p. 19).
- The qualitative analysis (Tables 10–11) explains the mechanism behind the numbers: surface-form embeddings recover morphological variants, and fastText handles OOV terms.
- The authors acknowledge that BERT was not used for ranking (p. 20).

## 12. Limitations

### Stated by the authors

- The datasets are small for BERT, so only BERT-base was tested (p. 20, item i).
- BERT was evaluated "to identify relevant and non-relevant documents for a query rather than ranking" (p. 20, item ii).
- No usable Amharic stemmer or morphological analyzer existed for the labeled data, so the stem- and root-based MLM versions could not be fine-tuned or evaluated (p. 15).
- The fall from P@5 to P@10 is attributed to "an insufficient relevant number of documents" in the test collection (p. 17).
- NSP training losses of the word/stem/root models come from different random samples, so they are hard to compare directly (p. 14).
- (Context remark, not a limitation of their own study: when introducing Table 13 the authors observe, about other languages, that "the effect of word embedding to the improve retrieval effectiveness of IR systems in many languages is low" (p. 19).)

### Inferred from the experimental design

1. **Confounded representation effect.**
   - Moving from word to stem/root changes, all at once: the index, the stop-word list, the embedding training corpus and vocabulary, and hence the expansions.
   - No unexpanded stem/root baseline is reported.
   - So "word-based QE > stem/root QE" cannot be split into (a) the effect of normalization on lexical matching and (b) the effect of normalization on expansion quality.
2. **The baseline is not reproduced in the paper.** "Conventional" appears to come from [46]; its representation and settings are not stated in Table 12.
3. **Ranking model under-specified:** LM smoothing, Lemur version, expansion-term weights, retrieval depth and the nDCG cutoff are all NOT_REPORTED.
4. **Query-side morphology is not described.** It is not said how the 240 topics were converted to stems and roots (manual annotation? a tool?). The p. 15 statement that no usable analyzer exists makes this more pressing.
5. **Embeddings are trained on the evaluation collection.** This is not qrels leakage, but it makes the expansions collection-specific ("local" embeddings). Generalization to unseen collections is untested.
6. **No significance testing on 240 queries.** Many differences are 0.01–0.05, and their reliability is unknown.
7. **The BERT–IR claim is not commensurable.**
   - Relevance-classification F1 (0.97) is compared with ranking metrics.
   - The train/validation split for the 50 queries and 5514 documents is not described, including whether queries are disjoint.
   - Accuracy Eq. 7 is misprinted.
8. **The Amharic "root" level has no analogue in Uzbek.** Transfer is limited to the word vs stem contrast.

## 13. What the work proves

Scope: on 2AIRTC (6069 docs, 240 queries), with Lemur LM retrieval and 10-term static-embedding query expansion trained on the collection itself.

- **Embedding-based QE over surface word forms outperforms QE over stems and over roots.** This holds for all five embedding configurations and all five reported metrics (Tables 7–9). Root beats stem throughout. No significance test, variance or per-query result is reported. **[our inference]** The word vs stem margins (0.13–0.28 P@5) are large enough that the direction is plausibly robust, but this cannot be verified from the paper.
- **fastText skip-gram on surface forms is the best configuration reported:** P@5 0.60, ndcg 0.75, MAP 0.51 (Tables 9, 12).
- **Qualitatively:** on surface forms, fastText neighbours are mostly **morphological variants** of the query term, in the authors' words (p. 17), and fastText provides expansions for OOV query terms where word2vec and GloVe provide none (Tables 10–11, pp. 17–18).
- A word-based Amharic BERT fine-tuned for relevance classification reaches F1 0.97 on its (undescribed) validation data (Table 6). This is a classification result, not retrieval.

## 14. What the work does NOT prove

- **That surface-form *indexing* is better than stem/root indexing for Amharic lexical retrieval.** Only QE-augmented runs are compared; unexpanded stem/root runs are absent.
- **That embedding QE helps in general.** Against "Conventional" only fastText skip-gram improves every shared metric. fastText CBOW is worse on three of four, and word2vec/GloVe lose on P@5. The comparability of "Conventional" is itself not demonstrated.
- **Anything about BM25, dense retrieval, or lexical–dense hybrid retrieval.** None is present. QE with static embeddings is not a dense retriever (cf. PROJECT_INSTRUCTIONS §8: embedding model ≠ retriever).
- **Anything about complementarity:** no overlap, no unique relevant hits and no oracle union between representations or components.
- **That BERT outperforms embeddings "on Amharic IR"** (p. 19): no BERT ranking run exists, the metrics differ, and there is no test.
- **That word-based superiority holds for fine-tuned BERT or "across all tasks"** (p. 19, p. 20). The stem- and root-based fine-tuned models were not evaluated (p. 15).
- **Which query types benefit.** There is no per-query analysis.

## 15. Relationship to current Uzbek evidence

- **No Uzbek data.** Amharic is Semitic (root-and-pattern), while Uzbek is Turkic (agglutinative, suffixing). The word vs stem contrast is the transferable part; the root level is Amharic-specific.
- Consistent with **MORPH-001** (Can et al. 2008, Turkish): elaborate normalization does not automatically improve retrieval, and the effect must be measured. Here normalization even loses, in combination with QE.
- Parallel to **MORPH-003** (UPERF, Urdu): raw/stem/lemma crossed with lexical and embedding-based representations. This paper adds another low-resource language where representation choice interacts with an embedding component. Neither paper has a modern retrieval-trained dense comparator.
- **Uzbek infrastructure for a direct replication exists:** Uzbek word2vec/GloVe/fastText (UZ-SEM-001) and Uzbek stemmers/lemmatizers (MORPH-UZ-003/004). A "raw/stem/lemma × fastText-QE" run for Uzbek is therefore cheap. It would still not be the v0.8 experiment, which needs a fixed dense D and fusion.
- **Amharic cluster** (per the assignment note; the other cards were not re-read for this card):
  - **CR000149** (Mekonnen et al. 2025, proposed MORPH-005): modern BM25 vs dense for Amharic, but with no morphological variants of BM25.
  - This paper (CR000427): morphological variants and embedding QE, but no BM25 and no dense retrieval.
  - **CR000447** (Yeshambel et al. 2024, 2AIRTC resources, word/stem/root) and **CR000354** (Alemayehu & Willett 2003, stemming in Amharic IR) cover the unexpanded lexical side.
  - So for Amharic the two halves again live in separate papers. No paper joins morphological variants of the lexical channel with a dense channel and a complementarity analysis.
- **Cross-card discrepancy to verify (not from this paper):** the CR000149 card records 2AIRTC as 12,583 documents. This paper uses 6069 documents "in each dataset" (p. 12), possibly the morphologically annotated subset of [51]. To be checked in the CR000447 card.

## 16. Relationship to CURRENT_GAP

**Classification (proposal):** *supports* (motivation) + *narrows* (slightly) + *no material effect on the residual core*.

- **Supports / occupied non-claims.** These were already non-claims in v0.8; this paper adds an Amharic example for both:
  - "raw/stem/lemma have not been compared in low-resource IR";
  - "morphology has not been combined with learned semantic representations for search".
- **Narrows.** The paper gives early evidence that **the morphological representation changes what a learned distributional component contributes**:
  - on surface forms, embedding neighbours are largely morphological variants;
  - on roots, they are not.
  This is a *qualitative* precursor of v0.8's "morphological representation → complementarity change". It suggests that a semantic component may partly **duplicate** morphological normalization on raw forms, i.e. overlap could be highest for raw forms and lower for normalized forms. That is a testable hypothesis for our design, not a finding of the paper.
- **No material effect on the residual core.** The following v0.8 elements are all absent:
  - BM25_raw / stem / lemma;
  - a **fixed** retrieval-trained dense D (here the "semantic" component is re-trained per representation and used only for QE);
  - fusion conditions;
  - unique relevant hits / overlap / oracle union;
  - incremental hybrid gain;
  - query features.
  None of the four "what can still kill this gap" conditions is met.

**Proposal:** keep v0.8 refined unchanged. Optionally list this paper in the evidence boundary as "morphological representation × embedding-based QE (Amharic), without dense retrieval or complementarity decomposition". This is a proposal only; `CURRENT_GAP.md` has not been edited.

## 17. Implications for our research design

- **Baselines.**
  - For every morphological variant (raw/stem/lemma), report the lexical run **alone** before any semantic addition. This paper shows how a missing unexpanded baseline makes the representation effect uninterpretable.
  - Keep **D fixed** across variants. Do not re-train a semantic component per representation; that is exactly the confound here.
- **Optional control condition** (low cost): BM25_raw + fastText-based QE, using an Uzbek fastText model trained outside the test collection. Compare it with BM25_lemma via overlap of relevant retrieved documents. This tests whether distributional expansion on raw forms duplicates lemmatization (the §16 hypothesis). It is a control, not a main condition.
- **Preprocessing.**
  - Document how **queries** are stemmed/lemmatized: tool, version, and manual vs automatic.
  - Use representation-specific stop-word lists only if justified, and report them.
  - Record OOV rates of query terms per representation; OOV was the fastText advantage here and is a candidate query feature.
- **Metrics.**
  - Report MAP, nDCG@k with explicit k, R-prec, bpref (useful with incomplete pooled qrels), and Recall@k at the fusion depth.
  - Report all announced metrics for all runs.
  - Per-query paired tests or bootstrap CIs; 240 queries is enough for per-query testing, which this paper omitted.
- **Query taxonomy.** Candidate features suggested by this paper: OOV status of query terms, and the number of in-collection morphological variants of each query term (derivable from a lemmatizer).
- **Protocol hygiene.**
  - Do not train distributional models on the test collection without also reporting an external-corpus variant.
  - Do not compare classification F1 with ranking metrics.
- **Hypothesis.** The paper motivates an explicit sub-hypothesis for the Uzbek pilot: *lexical–semantic overlap is highest for raw forms and decreases with normalization*. Test it; do not assume it.

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| Query expansion (QE) | Adding related words to the user's query so that documents using other words or forms are also matched | `Q' = Q ∪ {top-k neighbours of each q ∈ Q}` |
| Word / stem / root representation | Index text as full word forms, as forms with affixes removed, or (Semitic) as consonantal roots | Alternative term-normalization functions applied to documents and queries |
| Static word embedding (word2vec, GloVe, fastText) | One fixed vector per word learned from co-occurrence; similar words get similar vectors | Distributed representation; neighbours by cosine similarity |
| CBOW / skip-gram | Two ways to train word2vec/fastText: predict the word from its context, or the context from the word | Training objectives |
| fastText subwords | A word vector is built from its character pieces (3–5 characters here), so unseen words still get vectors | Sum of character n-gram vectors |
| Language-model retrieval (KL divergence) | Rank documents by how well a document's word distribution matches the query's | `score = −KL(Q_θ‖D_θ)` with a smoothed `D_θ` |
| bpref | A score that uses only judged documents; robust when many documents were never judged | Eq. 13, p. 14 |
| R-precision | Precision at a cutoff equal to the number of relevant documents for that query | P@R |
| OOV (out-of-vocabulary) | A query word never seen when the model was trained | Word ∉ training vocabulary |
| MLM / NSP | BERT pre-training tasks: guess masked words; decide whether sentence B follows sentence A | Eqs. 1–3, p. 9 |
| Complementarity (project term) | Each component finds relevant documents the other misses | Unique relevant hits, overlap, oracle-union gain |

## 19. Open questions / verification needed

Internal inconsistencies and gaps in the paper:

1. **Accuracy formula** (Eq. 7, p. 13) is printed as `(TP+FP)/(TP+FP+TN+FN)`. It should be `(TP+TN)/…`. Were the reported accuracies computed correctly? This cannot be checked from the paper.
2. **Word-based superiority "across all tasks"** (p. 19: "pre-trained and fine-tuned ... models performed better on the word-based form ... (see Tables 4–6)"; p. 20, Conclusions) **vs** p. 15: stem- and root-based fine-tuned models "could not" be evaluated. Table 6 is word-based only.
3. **"BERT significantly outperformed all embedding algorithms" on Amharic IR** (p. 19): there is no BERT ranking run (p. 20, item ii) and no significance test.
4. **NSP evaluation pairs:** "selected randomly" (Sec. 4.5, p. 13) vs "manually selected" (Sec. 5.1.1, p. 14).
5. **MAP and recall** are announced as IR metrics (Secs. 3.4.1 and 4.5) but are absent from Tables 7–9. Recall is never reported.
6. **"Conventional" baseline** (Table 12): source ([46]?), representation and settings are not stated. Unexpanded stem/root runs are missing.
7. **Query stemming/rooting method:** not described. There is a tension with "no usable Amharic stemmer and morphological analyzer" (p. 15).
8. **Figure 2 document-length unit:** unstated. A mode near 800–1000 is hard to reconcile with ≈262 words per document computed from p. 12 figures.
9. **Table 7:** CBOW = skip-gram to two decimals on 11 of 15 cells (all word- and stem-based cells, plus root-based ndcg). Genuine, or a copy error?
10. **MLM training loss rises from epoch 5 to epoch 10** (Table 4), while the text says the best training loss is at epoch 5. This is unexplained.
11. **BPE tokenizers** are listed among the released resources (p. 19, item ii) but never described in the method.
12. **BERT initialization** (from English BERT-base-uncased with a resized vocabulary, or from scratch?) is ambiguous (pp. 9, 11).
13. **Cross-card:** 2AIRTC size of 6069 (this paper) vs 12,583 (CR000149 card). Verify in the CR000447 card.

Leads (from this paper's reference list; not read):

- [40] Yeshambel et al., *Appl. Sci.*, "Amharic adhoc information retrieval system based on morphological features". The reference is printed as "2021, *12*, 1294" (p. 22); verify year and volume bibliographically before citing;
- [46] Yeshambel et al., KDIR 2020, "Amharic document representation for adhoc retrieval".

These likely contain the unexpanded word/stem/root baselines and should be checked against the corpus (possibly overlapping with CR000447).

## 20. Decision after deep dive

- **Keep current gap?** Yes. v0.8 refined remains valid (§16).
- **Modify gap?** No. Optionally add this paper to the evidence-boundary list as an Amharic "representation × embedding-QE" example (researcher's decision).
- **Add decision?** Proposed for `decisions/DECISIONS.md` (researcher's decision): "Every morphological variant is reported without any semantic component first; the semantic component D is never re-trained per morphological variant in the main comparison."
- **Add experiment?** Optional low-cost control for the Uzbek pilot: BM25_raw + fastText-QE (external Uzbek fastText) vs BM25_lemma. Measure overlap and unique relevant hits, to test whether distributional expansion on raw forms substitutes for lemmatization.
- **Add citation to Chapter I?** Yes, briefly:
  - §1.1: morphological representation in lexical IR of morphologically rich low-resource languages; the word > stem result as a caution against assuming normalization helps;
  - §1.3: early embedding-based query expansion as a pre-dense form of lexical–semantic integration, without complementarity analysis.
- **Proposed `MASTER_INDEX.md` row** (to add after approval):

| MORPH-010 | Yeshambel, Mothe, Assabie — *Learned Text Representation for Amharic Information Retrieval and Natural Language Processing* (*Information* 14(3):195, MDPI) — [deep dive](deep-dives/2023_Yeshambel_Mothe_Assabie_Amharic_Learned_Text_Representation.md) | 2023 | B | HIGH | Amharic 2AIRTC (6069 docs, 240 queries) in word/stem/root representations; Lemur LM (KL) retrieval with word2vec/GloVe/fastText query expansion trained per representation. Word > root > stem in all 5 embedding configurations; best fastText skip-gram word-based P@5 0.60, MAP 0.51 vs "Conventional" 0.56 / 0.43. Qualitatively, surface-form fastText neighbours are mostly morphological variants. No unexpanded stem/root baselines, no BM25, no dense retrieval, no fusion, no overlap/unique-hit analysis, no significance tests; BERT used only for classification. |
