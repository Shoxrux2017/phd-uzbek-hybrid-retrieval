# Yeshambel, Mothe & Assabie (2024): Construction of Amharic Information Retrieval Resources and Corpora

**Targeted deep-dive status:** COMPLETED (AI-assisted, pending researcher review)
**Completed:** 2026-09-28
**Literature ID:** `MORPH-011` (assigned 2026-09-28, approved by researcher)
**Systematic-review record:** `CR000447`. Full-text triage: INCLUDE, reading priority HIGH, reading tier 1 ("прямо по теме пробела"), `carries_complementarity_evidence = NO`.
**Provenance:** AI-assisted deep dive (Claude). The whole paper was read (pdftotext, 30 PDF pages, including the HAL cover page). The file is the **HAL-deposited "REVISED PROOF"** of the article (HAL `hal-04755851`; watermark "REVISED PROOF" on every page; proof header "Dispatch: 19-6-2024"). The final version of record was **not** checked; small differences from the published text are possible. The proof has **line numbers** but no journal page numbers, so locations below are given as **PDF page + proof line numbers**. PDF p. 2 is the first article page. The article spans journal pp. 1157–1185, so PDF page N ≈ journal page 1155 + N **[inferred mapping]**. Pages checked visually on page images (110 dpi): **PDF pp. 2, 8, 9, 10, 18, 20, 21, 22, 23, 24, 25, 27**. These pages hold Table 1, Fig. 1, Fig. 2, Tables 5–11, Figs. 3–4, and the prose quoted below. Every number below comes with its location. Numbers computed by us are marked **[computed]**. Values read off the figures are marked **[read from figure, approx.]**.
**Source rule:** **the paper is the primary and only authoritative source.**
- Web access was used only to verify the bibliographic record (volume, issue, pages, dates). Those items are marked "(bibliographic check: Crossref)".
- No code, website or later paper is used to claim what the authors did or did not do.
- Background knowledge appears only as explicitly labelled "Context (not from the paper)".
**Reliability:** **A** as a source type: a peer-reviewed Springer journal article in *Language Resources and Evaluation*. The **retrieval experiments inside it, however, are thinly specified** (retrieval model, query field, collection subset, stopword setting and NDCG cutoff are not stated; see §5, §12). Their evidential weight for the word/stem/root comparison is therefore closer to **B**.
**Verification:** independent AI verifier pass 2026-09-28; 6 findings addressed.

---

## Кратко для исследователя (RU)

- **Что сделано.** Это в первую очередь **ресурсная статья** для амхарского языка (семитский, корне-шаблонная морфология, письмо геэз). Авторы построили:
  - тестовую коллекцию 2AIRTC в формате TREC: 12 586 документов, 240 тем, ручная разметка релевантности (Table 1, PDF p. 8);
  - морфологически размеченные корпуса и лексиконы двух видов — **по стеммам** и **по корням**; вручную размечены 170 000 уникальных словоформ, разметка перенесена на 6 069 документов;
  - список стоп-слов из 222 единиц, построенный на уровне корней/морфем;
  - WordNet-подобный ресурс;
  - модели word2vec для исходных слов, стемм и корней.
- **Главные числа** (Table 7, PDF p. 22): поиск по словоформам / стеммам / корням даёт
  - MAP = 0.43 / 0.57 / 0.70;
  - NDCG = 0.47 / 0.71 / 0.86;
  - прирост корней над словоформами +62.8% MAP, +83.0% NDCG **[computed]**.
- **Поисковая модель — не BM25.** Это «Lemur IR system which is based on a language model» (строки 671–672). Тип модели, сглаживание и параметры **NOT_REPORTED**. Стеммер и морфоанализатор для запросов/документов не названы.
- **Плотного поиска нет.** word2vec используется только для **расширения запроса** (query expansion), а не как ретривер.
  - При расширении порядок представлений **обратный**: word 0.70 > root 0.66 > stem 0.55 по NDCG (Table 11, PDF p. 25).
  - Расширение через WordNet ухудшает результат при всех типах связей (Fig. 4).
- **Нет:**
  - гибрида / fusion;
  - перекрытия выдач, уникальных релевантных документов, oracle union;
  - анализа по запросам;
  - тестов значимости, нескольких прогонов, доверительных интервалов.
- **Серьёзные неясности постановки** (выводы наши):
  1. Не сказано, на какой коллекции шёл каждый прогон Table 7. Размеченные корпуса охватывают только 6 069 документов, **отобранных так, чтобы у каждой темы было ≥ 10 релевантных** (строки 303–305). Число документов для каждого прогона не указано нигде: «на 2AIRTC» названы и word-прогон (Table 7), и stem/root-прогоны (подпись Fig. 3). Если word-прогон шёл по полной коллекции, а stem/root — по подмножеству, сравнение смещено.
  2. Условие по стоп-словам для Table 7 не указано, хотя их удаление даёт очень большой эффект (Fig. 3).
  3. Лексическое богатство 0.13 (исходный текст) против 0.106 (стеммы и корни), по-видимому, считается на корпусах разного размера **[inferred, computed]**.
- **Внутренние несоответствия в самой статье:**
  - пул: «top 50» (строка 266) против «top 100» (строка 275);
  - частота корня g-l-ts': 13 250 в тексте (строка 661) против 13 252 в Table 5;
  - сумма частот пяти стемм = 13 150, меньше заявленной частоты корня **[computed]**;
  - в тексте о Fig. 4 цвета синонимов и гипонимов перепутаны относительно легенды;
  - в формуле косинуса (Eq. 1) нет квадратных корней.
- **Для нашего gap:** работа — ещё один пример сравнения «словоформа vs стемма vs корень» в морфологически богатом языке с ограниченными ресурсами, но **только для лексического канала и без BM25**. Ядро v0.8 (raw/stem/lemma BM25 × фиксированная модель D → перекрытие / уникальные попадания → прирост гибрида → признаки запросов) **не затрагивает**. Предложение: gap не менять.
- **Практическая польза для нас:**
  1. Схема «вручную разметить словарь типов → автоматически перенести разметку на корпус» — дешёвый способ получить «эталонную» (oracle) лемматизацию для узбекского контроля.
  2. Обработку стоп-слов и аффиксов надо фиксировать одинаково для raw/stem/lemma: здесь она, по-видимому, влияет сильнее самой морфологии.
  3. Пулы 2AIRTC собраны только лексическими системами (Lemur + Google, top-50). Для наших qrels пул должен включать и плотный канал, иначе уникальные находки D будут занижены.
  4. 2AIRTC с корпусами по стеммам и корням, по словам авторов, публичны (irit.fr). Это возможный дешёвый амхарский пилот нашего измерения перекрытия.

---

## 1. Bibliographic record

- **Authors:** Tilahun Yeshambel, Josiane Mothe, Yaregal Assabie
- **Affiliations (from the paper, lines A7–A9):**
  - Yeshambel: IT PhD Program, Addis Ababa University, Ethiopia;
  - Mothe: INSPE, Univ. de Toulouse, IRIT, UMR5505, CNRS, France;
  - Assabie: Department of Computer Science, Addis Ababa University.
- **Year:** 2024. Accepted 8 January 2024 (PDF p. 2, line 5). Published online 2 July 2024; print issue December 2024 (bibliographic check: Crossref).
- **Venue:** *Language Resources and Evaluation*, **58**(4), pp. **1157–1185** (bibliographic check: Crossref; volume and pages also on the HAL cover, PDF p. 1). The issue number (4) comes from Crossref only.
- **Publisher:** Springer Nature ("© The Author(s), under exclusive licence to Springer Nature B.V. 2024", line 6)
- **DOI:** `10.1007/s10579-024-09719-x`
- **Official URL:** https://doi.org/10.1007/s10579-024-09719-x ; HAL: https://hal.science/hal-04755851v1
- **ISSN:** 1574-020X (print), 1574-0218 (online) (bibliographic check: Crossref)
- **Data / code (stated in paper, lines 818–819, 839, 844):** https://www.irit.fr/AmharicResources/. Availability was not checked by us.
- **Source type:** peer-reviewed journal article (resource paper with an evaluation section)
- **Reliability:** A (venue). The retrieval-experiment evidence is weaker; see header.
- **Full text available:** yes (`07_full_text/pdfs/CR000447.pdf`, HAL revised proof, 30 PDF pages)

## 2. Why this work matters to the PhD

It is a peer-reviewed, TREC-style resource for a **morphologically rich low-resource language**. It offers an explicit **word vs stem vs root** lexical-representation comparison, and the same collection (2AIRTC) is used later by modern dense-retrieval work (CR000149, exemplar card).

| Axis | Relation |
|---|---|
| Lexical retrieval | Direct: word-, stem- and root-based indexing with a Lemur language-model retrieval system; stopword effect |
| Semantic retrieval | Only as **query expansion** with static word2vec and a WordNet-like resource. **No dense retriever** |
| Hybrid retrieval | **Absent** |
| Uzbek morphology | Indirect. Amharic is Semitic (root-and-pattern plus affixation); Uzbek is Turkic (agglutinative, suffixing). "Root" has no direct Uzbek analogue; stem/lemma do |
| Low-resource retrieval | Direct: construction of the first public Amharic ad hoc test collection, per the authors |
| Current gap | Adds one more instance of "morphological variants of the lexical channel compared". Touches none of the complementarity elements (§16) |

## 3. Research problem

### Simple explanation

Amharic had no public test collection (documents + queries + human relevance judgments) for testing search systems. Its words are built from roots and stems with many prefixes and suffixes, so a search engine that matches exact word forms misses many relevant documents. The authors build the missing resources, all designed around Amharic morphology, and check whether they are usable for retrieval.

### Formal formulation

Contributions stated by the authors (lines 86–92):

- "(i) Evaluation of the usability of the existing Amharic resources and corpora for IR;"
- "(ii) Construction of Amharic IR resources and corpora by considering linguistic features; and"
- "(iii) Evaluation and benchmarking of the usability of our resources and corpora in IR task."

There are no formal research questions or hypotheses. The retrieval question is implicit: **which index-term representation (surface word, stem, root) gives the best ad hoc retrieval effectiveness**, and do the stopword list and the expansion resources help?

## 4. Main idea

### Simple explanation

1. Collect about 12.6K Amharic documents, write 240 search topics, and have groups of five assessors judge relevance.
2. Take all distinct words from part of the collection and have people split each word into prefixes, stem or root, and suffixes. Linguists check this.
3. Replace every word in the documents with its stem-based or root-based analysis.
4. Search each version of the collection and compare MAP/NDCG.

### Concrete example

- The paper's own example (lines 656–661, PDF p. 21; Table 5, PDF p. 20):
  - the verbal stem *siri* ('work') occurs 8,911 times;
  - its root *s-r* occurs 24,035 times.
- Five different stems of the verb *g-l-ts'* ('explain') have frequencies 3, 668, 780, 5,765 and 5,934. All share one root with frequency 13,250.
- A query in root form therefore matches all these variants; a stem-form query matches one stem; a word-form query matches one surface form.

### Formal method

- **Annotation scheme** (line 312): a word `W` is represented as `[p_]* w [_s]*`, with prefixes `p`, base `w` (stem or root) and suffixes `s`.
  - Ambiguous (homonymous) words get multiple annotations: `[p_]*w[_s]*[{[pi_]*wi[_si]*}]*` (line 362).
  - How multiple annotations are indexed at retrieval time is **NOT_REPORTED**.
- **Retrieval:** "Lemur IR system which is based on a language model" (lines 671–672).
  - Context (not from the paper): Lemur's standard language-model retrieval is query likelihood with a smoothing method. Which variant and parameters were used here is not stated.
- **Metrics:** MAP (Eq. 3) and NDCG (Eq. 4, PDF p. 22–23); P@5 / P@10 in Table 11; interpolated recall–precision curves (Figs. 3–4).

## 5. Architecture / algorithm

1. **Test collection 2AIRTC** (Sec. 3.1): documents, topics and pooled human judgments (details in §6).
2. **Morphological annotation** (Sec. 3.2, Fig. 2 on PDF p. 10). The process is semi-automatic:
   - extract unique words from 6,069 selected documents, giving 170,000 unique surface words (lines 302–307);
   - annotate them **manually**, and have linguists evaluate the annotation (lines 292–294, 336–337);
   - annotate each word in the documents **automatically** by replacing it with its annotated form (lines 294–296): "A total of 1,592,351 words from 6,069 documents have been morphologically annotated."
   - The root-based lexicon is built from the stem-based lexicon (lines 297–299).
   - The focus is on **basic stems**, which are shorter and conflate more variants than derived stems (lines 426–429).
3. **Character normalization** (lines 547–557): homophone Ge'ez characters are mapped to one representative character. It is described under stopword preprocessing (Sec. 3.3.2.1). Sec. 4.1 (lines 648–650) says the word-, stem- and root-based corpora are generated after "tag removal, character normalization, and punctuation removal".
4. **Stopwords** (Sec. 3.3):
   - 44 semantic-based stopwords from an Amharic grammar (line 528);
   - 180 corpus-based **morphemes**, from the intersection of the top of four lists ranked by frequency, mean, variance and entropy, computed on 5,737 documents (lines 541, 563–570);
   - final list: "222 general terms" (lines 571–572), described as "222 root-based unique terms" (line 782). 44 + 180 = 224, so 2 items presumably overlap **[computed; overlap not stated]**.
5. **WordNet-like resource** (Sec. 3.4): built manually only for the topic titles. English translations of the title words are looked up in English WordNet for synonyms, hyponyms and hypernyms, and the results are translated back. It is organized by roots (lines 586–604).
6. **word2vec** (Sec. 3.5): three CBOW and three skip-gram models, one per corpus (word / stem / root). The top-10 cosine-similar terms are added as expansion terms (lines 617–626).
   - Training hyperparameters (dimension, window, epochs, corpus used): **NOT_REPORTED**.
   - Eq. 1 as printed has no square roots in the denominator (PDF p. 20, line 622), a typesetting or formula error.
7. **Retrieval evaluation** (Sec. 4.2): the "Amharic IR system developed by Yeshambel et al. (2020)", run on Lemur (lines 667–672).
   - Stem-based runs: "both queries and documents are morphologically processed using the same stemmer".
   - Root-based runs: they are processed "using the same Amharic morphological analyzer" (lines 697–700).
   - Which stemmer or analyzer, and whether it is the manually annotated lexicon or an automatic tool: **NOT_REPORTED**. This is in tension with step 2 (see §12).
   - **Not reported:** query field (title / description / narrative), number of topics used, retrieval depth, LM smoothing, and the stopword setting for Table 7.

## 6. Data

- **Dataset:** 2AIRTC (Amharic ad hoc IR test collection), built by the authors.
- **Language / domain:** Amharic. Mixed domains: news agencies (Walta, Fana, Amhara Mass Media Agency), Facebook, a personal blog and Amharic Wikipedia (lines 225–228). Topics cover business, sport, entertainment, education, religion, politics, technology, health and culture (lines 233–234).
- **Documents** (Table 1, PDF p. 8; lines 223–233):
  - 12,586 documents, 121,040 sentences, 4,784,469 words, 618,537 unique words;
  - words per document: min 15, avg 380, median 254, max 74,804.
  - Collected in two phases. The second phase added 2,880 Web documents retrieved by running the topic titles (max 50 per topic), "to enrich the collection and avoid topics with either no or very few relevant documents".
  - Check **[computed]**: 4,784,469 / 12,586 = 380.1 words per document, consistent with Table 1.
- **Topics** (Sec. 3.1.2, Table 1, Fig. 1):
  - 240 manually created topics, in Amharic with manual English translations;
  - fields: title, description, narrative;
  - "# words per topic": min 1, avg 4, median 3, max 7 (Table 1). We read these as **title** length **[inferred]**: Table 1 says "per topic", not "per title"; the Fig. 1 example title has 5 words.
- **Relevance judgments** (Sec. 3.1.3, PDF p. 9):
  - groups of **five assessors** with IR background, one group per topic;
  - "all assessors in the group need to agree to decide the relevance of each document" (lines 279–280);
  - pooling from the **Google Web search** and **Lemur** on the initial corpus, top 50 per topic (lines 264–266);
  - plus exhaustive judgment for some topics.
  - Relevant documents per topic: avg 22, min 10, max 172 (Table 1). The total is ≈ 5,280 **[computed, approximate: 22 × 240]**.
  - Relevance grades (binary or graded): **NOT_REPORTED**, although Eq. 4 is written for graded relevance. Inter-assessor agreement statistics: not reported; consensus was required.
- **Morphologically annotated subset:**
  - 6,069 documents (48.2% of 2AIRTC **[computed]**), "selected systematically in such a way that each topic in the test collection has at least 10 relevant documents" (lines 303–305);
  - 1,592,351 annotated words (line 296);
  - after preprocessing, each of the word-, stem- and root-based corpora has 1,585,364 tokens (lines 647–648);
  - 170,000 unique words in each lexicon, of which 88,293 (51.9% **[computed]**) are derived from verbal roots (lines 644–646).
- **Train/dev/test:** not applicable; no learned ranker. word2vec training data are presumably the corpora (lines 617–619), but not specified exactly.
- **Collection used for each retrieval run: NOT_REPORTED** (see §12).

## 7. Baselines

| Condition | What it is | Why selected | Fair comparison? |
|---|---|---|---|
| Word-based (2AIRTC) | Surface-form indexing, Lemur LM | Reference representation | **Unclear.** The paper never states whether this run used the full 12,586 documents or the 6,069-document subset. The "(2AIRTC)" label is weak evidence, since stem/root runs are also called "on the 2AIRTC collection" (Fig. 3 caption). Its stopword setting is not stated |
| Stem-based | Basic stems, via "the same stemmer" for queries and documents | Conflates inflectional variants | Unclear: stemmer not named; stopword and affix handling not stated |
| Root-based | Consonantal roots, via "the same Amharic morphological analyzer" | Conflates all variants of a root | Same issues as stem-based |
| ± stopwords (Fig. 3) | Stem- and root-based runs with and without the 222-item list | Tests the stopword resource | Word-based run not shown. What "with stopwords" means for segmented affixes is not explained |
| Query expansion (WordNet, word2vec) | Expanded vs "normal" retrieval | Tests the semantic resources | Fig. 4 includes an unexpanded baseline; **Table 11 does not** |

No external lexical baseline (BM25, another IR toolkit) and no dense or neural baseline is included.

## 8. Metrics

| Metric | Definition | Simple meaning | Appropriate? |
|---|---|---|---|
| MAP (Eq. 3) | Mean over queries of the average precision at the ranks of relevant documents | "How early, on average, do all relevant documents appear?" | Yes for ad hoc TREC-style collections. The paper's verbal definition ("MAP specifies the number of relevant documents…", line 673) is imprecise; the equation is standard |
| NDCG (Eq. 4) | DCG at cutoff k with gain `2^R − 1` and log₂ discount, normalized by the ideal ranking | "Graded, rank-discounted quality" | Yes. **The cutoff k used in Tables 7 and 11 is NOT_REPORTED** |
| P@5, P@10 (Table 11) | Share of relevant documents among the top 5 / 10 | "Top-of-list precision" | Yes, but not reported for Table 7, so the two tables cannot be compared on these metrics |
| Interpolated recall–precision curves (Figs. 3–4) | Interpolated precision at 11 recall levels | Whole-ranking view | Yes. In the printed figures **precision is on the x-axis and recall on the y-axis**, the reverse of the usual convention; we read them as printed |

No significance test is reported (§10).

## 9. Results

### Table 7: word vs stem vs root (PDF p. 22, checked on image)

| Corpus | MAP | NDCG |
|---|---:|---:|
| Word-based (2AIRTC) | 0.43 | 0.47 |
| Stem-based | 0.57 | 0.71 |
| Root-based | **0.70** | **0.86** |

**[computed]**:
- Stem vs word: +0.14 MAP (+32.6%), +0.24 NDCG (+51.1%).
- Root vs word: +0.27 MAP (+62.8%), +0.39 NDCG (+83.0%).
- Root vs stem: +0.13 MAP (+22.8%), +0.15 NDCG (+21.1%).

The authors report no relative percentages. Their verbal claim is "root-based retrieval was found to be the most effective" (lines 693–694).

### Figure 3: stopword effect, stem- and root-based (PDF p. 22, checked on image)

Interpolated precision at the recall extremes **[read from figure, approx. ±0.02]**:

| Run | Precision at recall 0.0 | Precision at recall 1.0 |
|---|---:|---:|
| Root-based, stopwords removed (red) | ≈ 0.85 | ≈ 0.30 |
| Stem-based, stopwords removed (blue) | ≈ 0.80 | ≈ 0.14 |
| Root-based, stopwords kept (green) | ≈ 0.50 | ≈ 0.01 |
| Stem-based, stopwords kept (pink) | ≈ 0.33 | ≈ 0.01 |

- Authors: "removing stopwords improves the results of both root-based and stem-based retrievals. The best results are obtained for root-based retrieval after stopwords have been removed" (lines 708–710).
- The color mapping in the text (lines 705–708) matches the legend.
- The stopword effect (≈ +0.35 to +0.47 in precision at low recall) is **as large as or larger than** the stem → root difference (≈ +0.05) **[computed from approx. readings]**.
- No word-based curve is shown.

### Table 8: index size (PDF p. 23, checked on image)

| Index type | Corpus size (MB) | Index size (MB) |
|---|---:|---:|
| With stopwords | 33.0 | 25.1 |
| Without stopwords | 24.1 | 15.1 |

Stopword removal reduces the index by 39.8% and the corpus by 27.0% **[computed]**. Which representation (word / stem / root) these sizes refer to is not stated.

### Figure 4: WordNet query expansion (PDF p. 24, checked on image)

- For both stem-based (a) and root-based (b) retrieval, every expansion type lies **below** "normal retrieval".
- Precision at recall 0.0 **[read from figure, approx.]**:
  - (a) normal ≈ 0.85, hypernym ≈ 0.62, pink ≈ 0.55, green ≈ 0.42;
  - (b) normal ≈ 0.89, hypernym ≈ 0.50, pink ≈ 0.45, green ≈ 0.43.
- Authors: "Query expansion using WordNet is performing less than without query expansion" (line 735). They attribute this to missing term disambiguation (lines 736–737).
- **Internal inconsistency (color mapping):**
  - The text says "The blue, green and pink lines are hypernym, synonym and hyponym retrievals, respectively" (lines 729–730).
  - The printed legend assigns **pink = synonym** and **green = hyponym**.
  - The authors' ranking, "retrieval effectiveness obtained by adding hypernyms is better than the result obtained by adding synonyms, which in turn is better than the result obtained by adding hyponyms" (lines 732–734), agrees with the figure only under the **legend** mapping.
- Minor: the unexpanded curves in Fig. 4 do not coincide exactly with the "stopwords removed" curves in Fig. 3 (≈ 0.85 vs ≈ 0.80 for stem; ≈ 0.89 vs ≈ 0.85 for root at recall 0) **[read from figure, approx.]**. The settings of "normal retrieval" are not stated.

### Table 11: word2vec query expansion (PDF p. 25, checked on image)

| Model | CBOW P@5 | CBOW P@10 | CBOW NDCG | Skip-gram P@5 | Skip-gram P@10 | Skip-gram NDCG |
|---|---:|---:|---:|---:|---:|---:|
| Word-based | **0.53** | **0.51** | **0.70** | **0.53** | **0.51** | **0.70** |
| Stem-based | 0.40 | 0.35 | 0.55 | 0.40 | 0.35 | 0.55 |
| Root-based | 0.45 | 0.40 | 0.66 | 0.44 | 0.38 | 0.66 |

- With expansion the ordering is **word > root > stem**, the reverse of Table 7 for word vs the others. The authors state it (lines 744–746, 823–825) and explain that word-based neighbours include inflected variants of the query term (lines 747–761).
- **Cross-table reading [computed; comparability NOT established by the paper]:**
  - word-based NDCG 0.47 (Table 7, no expansion) → 0.70 (Table 11, expansion): +0.23;
  - stem-based 0.71 → 0.55: −0.16;
  - root-based 0.86 → 0.66: −0.20.
  - Table 11 has no unexpanded baseline, and the NDCG cutoff and settings of the two tables are not stated. So "word2vec expansion helps word-based and hurts stem/root retrieval" is a **possible reading, not a reported result**.

### Corpus analysis (Sec. 4.1, PDF pp. 20–21, checked on image)

- **Lexical richness** (type/token ratio, Eq. 2): 2AIRTC 0.13, stem-based 0.106, root-based 0.106 (lines 637–638).
- Check **[computed]**: 618,537 / 4,784,469 = 0.129, so 0.13 is the **full** collection. 0.106 × 1,585,364 ≈ 168,049 types, while 170,000 / 1,585,364 = 0.107.
  - The stem/root values therefore appear to be computed on the 6,069-document subset.
  - They are numerically almost equal to the subset's **surface**-vocabulary ratio.
  - That stem and root give the same value is also unexpected, since roots conflate more than stems (lines 598–599, 653–654).
  - Because type/token ratio falls as corpus size grows, the reported 0.13 → 0.106 "reduction" cannot be attributed to morphology from these numbers **[inferred]**.
- **Frequencies** (lines 656–661; Table 5):
  - stem *siri* 8,911 vs root *s-r* 24,035 (Table 5 agrees);
  - root *g-l-ts'*: **13,250 in the text vs 13,252 in Table 5**;
  - the five listed stems sum to **13,150 [computed]**, 100 less than the text's root frequency. This is not necessarily an error, since the list may be incomplete, but it is not explained.
  - The "Word-based" column of Table 5 is not sorted by frequency (e.g., 3,284 first, 3,332 sixth), although it is titled "Top 10".

## 10. Statistical evidence

- **Significance tests:** NOT_REPORTED (none for Table 7, Fig. 3, Fig. 4 or Table 11).
- **Confidence intervals:** NOT_REPORTED.
- **Runs / seeds:** NOT_REPORTED. Presumably single deterministic runs; the word2vec training seeds are not reported.
- **Ablation:** only one-factor comparisons: representation (Table 7), stopwords (Fig. 3), expansion source and relation type (Fig. 4, Table 11). No factorial design (e.g., representation × stopwords × expansion). Word-based ± stopwords is not reported.
- **Per-query analysis:** **none quantitative.** There are qualitative expansion-term examples (Table 4, lines 750–761). There is:
  - no per-topic breakdown;
  - no overlap or unique-hit analysis between representations;
  - no oracle union;
  - no link to topic properties, although topic titles are said to vary in length and in simple vs complex words (lines 245–251).

## 11. Strengths

- A public TREC-style Amharic collection (documents, topics, qrels), per the authors, with **consensus judgments by five-assessor groups** and description/narrative-based relevance criteria. Relevance "should not simply contain words from the query" (lines 269–272).
- **Linguistically validated, manually built stem and root lexicons** covering 170,000 word types. This is closer to gold morphology than typical automatic stemmers.
- Word, stem and root are compared on the same topics.
- Stopwords are treated as a morphology problem (root/morpheme-level list), and index-size effects are reported.
- Negative results are reported honestly: WordNet expansion hurts; word2vec expansion favours surface forms.

## 12. Limitations

### Stated by the authors

- The WordNet-like resource covers only topic-title terms, and expansion without term disambiguation hurts. "further evaluation should be conducted, including the number of terms to add" (lines 735–738).
- Root- and stem-based expansion returns "a higher number of syntactic words for some queries which negatively affects retrieval performance" (lines 825–827).
- Existing morphological analyzers (HornMorpho) generate derived rather than basic stems, and roots with vowels (lines 793–800). This motivates the manual annotation.

### Inferred from the experimental design

1. **The collection used for each Table 7 run is unspecified, and a plausible reading is confounded.**
   - The annotated corpora cover 6,069 documents, selected so that every topic keeps ≥ 10 relevant documents.
   - The word-based row is labelled "(2AIRTC)". The label carries little weight, because the paper also describes the stem- and root-based runs as being on 2AIRTC:
     - the Fig. 3 caption reads "Recall/Precision curves with and without stopwords on the 2AIRTC collection" (PDF p. 22);
     - Sec. 4.2.1 refers to stem/root results "using this collection" (lines 695–697).
   - The paper also describes the source of the annotated corpora in different ways:
     - the stem- and root-based corpora are "created automatically using the initial documents in which every word in the initial corpus is replaced" by its annotation (lines 457–458; similarly 497–499);
     - "initial corpus" is the paper's term for the phase-1 collection (line 224);
     - lines 296 and 302–305 instead speak of 6,069 selected documents.
   - If word-based retrieval ran on 12,586 documents and stem/root on the 6,069-document subset, the latter searched a collection about half the size with nearly the same relevant documents. That alone would raise MAP/NDCG.
   - Sec. 4.1 says the word-, stem- and root-based corpora have equal token counts (1,585,364), which supports a same-subset reading. The paper never states the document count per run, so the question stays open.
2. **The stopword/affix setting of Table 7 is not stated.** Fig. 3 shows stopword removal changes results more than stem vs root does.
   - The annotated corpora segment words into `prefix_base_suffix`, and the stopword list consists largely of **morphemes** (180 of 222).
   - So "stem-based / root-based" retrieval may also differ from word-based retrieval in whether affix morphemes are indexed or removed. The paper does not describe how segmented affixes are tokenized at indexing.
   - The Discussion says: "Morpheme removal from documents and queries brings relevant documents to the top of search results" (lines 808–809).
3. **Tension between the gold annotation and "the same stemmer / analyzer".**
   - The corpora are produced by lexicon lookup of manual annotations (lines 294–296).
   - Sec. 4.2.1 says queries and documents were processed by "the same stemmer" or "the same Amharic morphological analyzer" (lines 697–700), neither named.
   - Whether results reflect gold morphology or an automatic tool is unclear.
   - Handling of multiple (homonym) annotations at indexing and at query time is also unspecified. The paper presents multiple annotations as a design feature ("We applied multiple annotations for such types of words", line 360), not as a limitation.
4. **The retrieval model is under-specified** ("based on a language model"; smoothing and parameters not given). There is no BM25, so the results are not directly a BM25 morphology effect.
5. **Query formulation is not stated** (title only, or title + description). The number of evaluated topics is not stated.
6. **Pool bias toward lexical systems.** Pools came from Google and Lemur top-50 (plus some exhaustive judging). Systems unlike these, e.g., dense retrievers, may retrieve unjudged relevant documents. Relevant for any later dense evaluation on 2AIRTC.
7. **The NDCG cutoff and the relevance scale are not stated.** Tables 7 and 11 cannot be compared reliably.
8. **No significance testing, variance or per-topic analysis.** The large Table 7 differences are plausible but not statistically established.
9. **Circularity risk in the topic ↔ collection construction.** Phase-2 documents were retrieved with the topic titles, and the annotated subset was selected by relevance. Both shape collection statistics in favour of the evaluation topics. The effect on the representation comparison is unknown.
10. **The source is a revised proof, not the version of record.** Numbers may differ in the final article (not checked).

## 13. What the work proves

- **A public-by-claim Amharic ad hoc test collection exists** with 12,586 documents, 240 bilingual topics and consensus human qrels (avg 22 relevant per topic), plus manually annotated stem and root lexicons for 170,000 word types. This is a resource-existence claim, supported by the description (Table 1, Sec. 3).
- **In the authors' Lemur LM setup, conflating Amharic word forms to stems and especially roots gave much higher MAP/NDCG than surface forms:** 0.43 / 0.57 / 0.70 MAP, 0.47 / 0.71 / 0.86 NDCG (Table 7).
  - This holds only under the unstated settings (collection subset, stopwords, query field).
  - No significance test is reported.
- **Stopword removal with the morpheme/root-level list strongly improves stem- and root-based retrieval** and reduces index size by about 40% (Fig. 3; Table 8, [computed]).
  - Same caveats as Table 7: a single run per condition, no significance test, and the collection subset is unstated.
  - Table 8 does not say which representation its index sizes refer to.
- **The best representation appears to depend on the pipeline.** With word2vec query expansion, word-based retrieval (NDCG 0.70) beats root (0.66) and stem (0.55) (Table 11). WordNet expansion underperforms no expansion (Fig. 4).
  - This rests on comparing orderings across Tables 7 and 11, whose settings (NDCG cutoff, collection, stopwords) are unstated and possibly different (§9).

## 14. What the work does NOT prove

- **That root > stem > word holds under a controlled comparison.** The collection used per run, the stopword/affix setting and the query field are not reported, and one plausible reading compares different collection sizes (§12).
- **Anything about BM25.** The retrieval model is a Lemur language model. No BM25 run is reported.
- **Anything about dense or neural retrieval.** word2vec is used only to expand queries. No dense retriever, no semantic ranking channel.
- **Anything about hybrid retrieval or complementarity.** There is no fusion, no overlap of retrieved or relevant sets between representations or channels, no unique hits and no oracle union.
- **Which topics benefit from stem or root conflation, or why.** There is no per-topic or query-feature analysis.
- **That the root form is "the most appropriate representation" in general** (lines 813–815). Under word2vec expansion the word form is best (Table 11), so the claim is conditional on the pipeline.
- **That stemming or root extraction by an automatic tool** (as opposed to manual lexicon annotation) would give these gains. The tool used is unclear.
- **That the morphology effect exceeds the stopword or affix effect.** The two are not separated.

## 15. Relationship to current Uzbek evidence

- **No Uzbek data.** Amharic root extraction (consonantal roots, non-concatenative templates) has no direct Uzbek counterpart. The Uzbek analogues are stem (suffix stripping) and lemma (dictionary form). The finding that "deeper conflation helps more" is suggestive at most. Can et al. (MORPH-001) already warn that more elaborate normalization does not guarantee better retrieval in Turkish.
- The **manual type-lexicon → corpus projection** approach mirrors what Uzbek analyzers already provide (Bakaev, Xusainova, Elov, Turayev cards: >32k base forms, lemmatizers). Uzbek lacks the IR-evaluation side that this paper supplies for Amharic: a public test collection with human qrels and a word/stem comparison.
- **Amharic cluster in our corpus:**
  - **CR000354** (Alemayehu & Willett 2003, "The effectiveness of stemming for information retrieval in Amharic", cited in this paper's references, lines 869–870): classical word/stem/root comparison with Okapi, per the exemplar card's description.
  - **CR000447** (this paper): collection plus word/stem/root with a Lemur LM.
  - **CR000427** (Yeshambel et al. 2023, per the exemplar card): learned representations / expansion on 2AIRTC in word/stem/root variants.
  - **CR000149** (Mekonnen et al. 2025, exemplar): modern dense retrievers and BM25 on news pairs, dense zero-shot on 2AIRTC. **No BM25 on 2AIRTC, no stem/root BM25, no fusion.**
  - For Amharic, **the lexical-morphology half and the dense half exist on the same collection (2AIRTC) but in separate papers.** None of them fixes a dense retriever and varies the lexical representation.
- **Cross-card note (not a statement about this paper's correctness):**
  - The exemplar card records 2AIRTC as 12,583 documents per Mekonnen et al.'s appendix. This paper reports **12,586** (Table 1; line 223).
  - The Mekonnen authors' caveat (as recorded in the exemplar card) that 2AIRTC judgments are incomplete and sparse is consistent with this paper's lexical-only, top-50 pooling (§12, item 6) **[inferred]**.
- The paper (lines 695–697) points to Yeshambel et al. (2020, KDIR) for "more results on the impact of Amharic stems and roots … using this collection". If that paper is in our record set, it is the natural companion card.

## 16. Relationship to CURRENT_GAP

**Classification:** *supports* (weakly) + *no material effect on the residual core*.

- **Supports / confirms as occupied** (already listed as non-claims in v0.8): "raw/stem/lemma have not been compared in low-resource IR" and "morphology has not been shown to affect lexical retrieval in morphologically rich languages". This paper is one more peer-reviewed instance (word/stem/**root**, Amharic, LM retrieval). It does **not** add BM25, so it does not bear on "morphology-aware BM25 vs modern embeddings".
- **Adds a design warning relevant to the core**, not a gap change: in this setup the stopword/affix treatment has an effect at least as large as the representation change (Fig. 3). A morphology → complementarity study must hold these constant, otherwise a "morphology effect" is confounded.
- **No material effect on the residual core of v0.8 refined.** None of the following is present:
  - a fixed dense retriever D;
  - H_raw / H_stem / H_lemma fusion;
  - unique relevant hits, overlap, oracle union or incremental hybrid gain;
  - per-query changes;
  - a link to query features.
- **Does not kill the gap** under any of the four "what can still kill this gap" criteria in CURRENT_GAP: not Uzbek, not Turkic, no dense comparator, no overlap analysis.

**Proposal:** keep v0.8 refined unchanged. Optionally add this paper to the evidence boundary as the Amharic instance of "lexical morphology variants compared, without dense/fusion/complementarity". This is a proposal only; `CURRENT_GAP.md` has not been edited.

## 17. Implications for our research design

- **Morphology preprocessing (controls).**
  - Hold the non-morphological pipeline constant across BM25_raw / BM25_stem / BM25_lemma: tokenization, apostrophe and script normalization, **stopword list and how it applies to each representation**, and handling of split affixes.
  - This paper shows how a stopword list defined at the base/morpheme level can create a large difference that is easy to misattribute to morphology.
  - Report a ± stopword control for **all** representations, including raw.
- **Oracle morphology condition (optional).** The type-lexicon approach (annotate distinct word types once, project to tokens) is a cheap way to build a **gold-lemma** Uzbek control beside automatic lemmatizers. It separates "lemmatization quality" from "lemma representation" effects. Ambiguous types need an explicit rule (first analysis / all analyses / context), and we must report it; this paper leaves it unspecified.
- **Collection identity.** All representations must be indexed over the **same document set**. Never compare runs on subsets selected by relevance. Report collection size per run.
- **Qrels / pooling.** Pool from **both** lexical variants and the dense model D, at depth > top-10 (see GAP_BOUNDARY on Munetsi). Otherwise dense-only relevant documents are under-judged and unique-hit counts for D are biased downward. 2AIRTC is an example of lexical-only pools (Google + Lemur).
- **Topics.** Adopt the TREC title / description / narrative format with consensus or adjudicated judgments; the narrative-based criterion is a good template. **State which field forms the query.** Title-length variation (1–7 words per topic here, read as title length [inferred]) is a candidate query feature, as in Can et al.
- **Metrics.** State the NDCG cutoff and the relevance scale explicitly. Report MAP, nDCG@10 and Recall@k on the same run set, so that no cross-table comparison is needed.
- **Semantic channel.** Static word2vec expansion is not our D; this paper is not a dense baseline. Its Table 11, however, suggests that **representation × semantic component interact** (the best lexical representation changes when a semantic component is added). That motivates our core measurement, but it is not evidence for it.
- **Low-cost pilot (proposal).** 2AIRTC plus the stem- and root-annotated corpora are, per the authors, public. Running BM25 on word / stem / root × one fixed released Amharic dense model (e.g., from CR000149), and computing overlap / unique hits / oracle union, would exercise our full measurement pipeline on an existing human-judged collection. Caveats: pool bias and a Semitic root representation.

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| Ad hoc test collection | A fixed set of documents, search topics and human relevance labels, used to score search systems | Cranfield/TREC paradigm: (D, Q, qrels) |
| Topic (title / description / narrative) | A written search need: short query words, one or two sentences of description, and rules for what counts as relevant | TREC topic fields |
| Pooling | Only the top results of some systems are shown to assessors; unjudged documents count as non-relevant | Depth-k pool from contributing runs |
| Stem (basic stem) | The part of a word left after removing affixes; in Amharic one verb can have several stems | Morphological base below the surface form |
| Root (Semitic) | The consonant skeleton shared by all stems and words of one verb family, e.g., *s-r* 'work' | Consonantal radicals combined with vowel templates |
| Conflation | Mapping different word forms to one index term | Many-to-one term normalization |
| Stopword | A frequent function word or morpheme with little content, removed before indexing | Removal list applied at indexing and query time |
| Lexical richness | How varied the vocabulary is: distinct words divided by total words | Type/token ratio (Eq. 2); depends on corpus size |
| Language-model retrieval (Lemur) | Ranks documents by how likely the query is to be "generated" by the document's word distribution | Context (not from the paper): query likelihood with smoothing; the variant here is NOT_REPORTED |
| MAP | Average of precision values at each relevant document's rank, then averaged over queries | Eq. 3 |
| NDCG | Rank-discounted gain, normalized so a perfect ranking scores 1 | Eq. 4; cutoff k unstated here |
| P@k | Share of relevant documents among the first k results | Precision at cutoff k |
| Interpolated recall–precision curve | Best precision achievable at or beyond each recall level | 11-point interpolated precision |
| Query expansion | Adding related words to the query to catch more relevant documents | Q' = Q ∪ expansion terms |
| word2vec (CBOW / skip-gram) | Static word vectors learned from context; similar vectors mean related words | Mikolov et al. (2013); used here only for expansion |
| Hypernym / hyponym | More general / more specific word ("vehicle" / "car") | WordNet lexical relations |
| Complementarity (project term) | Each channel finds some relevant documents the other misses | Unique relevant hits, overlap, oracle-union gain |

## 19. Open questions / verification needed

1. **Which document set was each Table 7 run indexed on:** full 2AIRTC (12,586), the phase-1 "initial corpus" (lines 457–458, 497–499) or the 6,069-document annotated subset (lines 296, 302–305)? The paper calls all of the runs "on 2AIRTC" (Table 7 label; Fig. 3 caption). Which topics or query field were used? Not decidable from the paper.
2. **Stopword / affix setting for Table 7,** and how segmented prefixes and suffixes are tokenized and indexed in the stem and root corpora.
3. **Stemmer / analyzer identity** in Sec. 4.2.1 vs the manual lexicon annotation of Sec. 3.2; handling of multiple (homonym) annotations.
4. **Lemur retrieval model details** (query likelihood? smoothing? parameters) and the NDCG cutoff.
5. **Internal inconsistencies** to note when citing:
   - pooling depth "top 50" (line 266) vs "top 100" (line 275);
   - root *g-l-ts'* frequency 13,250 (line 661) vs 13,252 (Table 5); the listed stems sum to 13,150 [computed];
   - Fig. 4 color mapping in the text (lines 729–730) vs the legend;
   - Eq. 1 printed without square roots;
   - lexical richness of stem = root (0.106), apparently on a different corpus from raw (0.13) [computed].
6. **Version of record:** check the final Springer PDF for changes to the numbers above; we read the HAL revised proof.
7. **Companion paper:** Yeshambel et al. (2020, KDIR, "Amharic document representation for ad-hoc retrieval") — is it in our record set? The authors point to it for fuller stem/root results.
8. **Resource availability:** is https://www.irit.fr/AmharicResources/ live with qrels and annotated corpora? Relevant only for the optional pilot; not checked here.

## 20. Decision after deep dive

- **Keep current gap?** Yes. v0.8 refined remains valid (§16).
- **Modify gap?** No change proposed. Optional: add to the evidence boundary as an Amharic word/stem/root lexical-only instance (researcher's decision).
- **Add decision?** Proposed for `decisions/DECISIONS.md` (researcher's decision):
  - "All lexical representation variants are indexed over the identical document set, with identical non-morphological preprocessing (tokenization, normalization, stopword list and its application, affix handling); ± stopword is reported as a separate control for every variant."
  - "Qrels pools must include the dense channel D and all lexical variants."
- **Add experiment?** Optional low-cost pilot on 2AIRTC: BM25 word / stem / root × one fixed released Amharic dense model, measuring overlap, unique hits and oracle union. Also optional: a gold-lexicon lemma condition for Uzbek alongside the automatic lemmatizer.
- **Add citation to Chapter I?** Yes:
  - §1.1 (morphological normalization in lexical IR for morphologically rich low-resource languages; stopwords as a morphology-dependent resource; test-collection construction);
  - Chapter I conclusions / §1.3, as evidence that the Amharic lexical-morphology and dense-retrieval strands exist on the same collection but were never combined or analysed for complementarity.
  - Cite Table 7 with the caveats in §12.
- **Proposed `MASTER_INDEX.md` row** (to add after approval; section C):

| MORPH-011 | Yeshambel, Mothe, Assabie — *Construction of Amharic information retrieval resources and corpora* (*Language Resources and Evaluation* 58(4), 1157–1185) — [deep dive](deep-dives/2024_Yeshambel_Mothe_Assabie_Amharic_IR_Resources_Corpora.md) | 2024 | A (venue); retrieval experiments thinly specified | HIGH | 2AIRTC Amharic ad hoc collection (12,586 docs, 240 topics, five-assessor consensus qrels from Google + Lemur top-50 pools), manually annotated stem/root lexicons (170k types) and corpora (6,069 docs), 222-item morpheme-level stopword list, WordNet-like resource, word2vec. Lemur LM (not BM25): MAP word/stem/root 0.43/0.57/0.70, NDCG 0.47/0.71/0.86 (collection subset, stopword setting, query field unstated; no significance tests). Stopword removal effect ≥ representation effect; word2vec expansion reverses the order (word best). No BM25, dense, fusion, overlap/unique-hit or per-query analysis. |
