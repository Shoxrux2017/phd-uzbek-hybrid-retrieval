# Arısoy, Can, Parlak, Sak & Saraçlar (2009): Turkish Broadcast News Transcription and Retrieval

**Targeted deep-dive status:** COMPLETED (AI-assisted, pending researcher review)
**Completed:** 2026-09-28
**Literature ID:** `MORPH-017` (assigned 2026-09-28, approved by researcher)
**Systematic-review record:** `CR001390`. Full-text triage: INCLUDE, reading priority HIGH, reading tier 1, `carries_complementarity_evidence = YES`. Triage boundary note: the retrieval task is spoken term detection (STD), which finds term occurrences in a lattice index rather than ranking documents; it was included under Clarification 002 Rule E. The YES flag rests on the IV/OOV query split and the word+morph index cascade (Table VII). That evidence is **class-level and partly structural** (see §10, §16).
**Provenance:** AI-assisted deep dive (Claude). The whole paper was read (10 pages, pdftotext text). Page images of **all 10 pages** were rendered at 110 dpi. Pages 1–8 were checked visually, including Tables I–II (ms. p. 3), Fig. 2 (ms. p. 4), Sec. VI (ms. p. 5), Tables III–IV (ms. p. 6) and Table V (ms. p. 7). Table VI, **Table VII** and Fig. 3 (ms. p. 8) were checked visually, and Table VII also on 250-dpi crops. Numbers computed by us are marked **[computed]** and were computed in Python.
**Important:** the PDF is a **pre-publication author manuscript**, not the typeset IEEE version. It is IEEEtran `bare_jrnl` with "PLACE PHOTO HERE" placeholders, pages numbered 1–10, no journal header, volume or DOI, and a PDF creation date of 2009-03-09. Page references below are **manuscript pages ("ms. p.")**. We did not compare it with the published version, whose numbers could differ.
**Source rule:** **the paper is the primary and only authoritative source.** Web lookup was used only for the bibliographic record (see §1). The related SIGIR '09 paper by two of the same authors (CR000691) is mentioned only to relate the records. Nothing is concluded about this paper from that one.
**Reliability:** **A for the venue** (peer-reviewed IEEE Transactions journal). The text we read is an author manuscript, and **the retrieval evidence is narrow**: one STD section, no document retrieval, no significance tests for the retrieval results.
**Verification:** independent AI verifier pass 2026-09-28; 8 findings addressed.

---

## Кратко для исследователя (RU)

- **Что сделано.** Журнальная статья группы Boğaziçi. Она обобщает их систему **распознавания речи (ASR) и поиска** по турецким новостным передачам. Основной объём — ASR:
  - единицы языковой модели: слова, stem+ending от морфологического парсера, статистические морфы Morfessor;
  - дискриминативное обучение акустической и языковой модели.
  Поиск представлен **только обнаружением терминов в речи** (spoken term detection, STD). Система находит, в каких фрагментах записи (utterances) произнесён термин запроса, по индексу взвешенных автоматов над решётками ASR (Sec. VI, VII-D).
- **Поиска документов (SDR) в статье нет.** SDR упоминается лишь как определение во введении (ms. p. 1). Экспериментов с ранжированием новостных сюжетов, qrels, BPref/MAP нет. Этим подтверждается открытый вопрос из карточки CR000691: стемминговые SDR-результаты группы есть только в 2-страничной статье SIGIR '09.
- **Морфологические варианты есть, но как единицы распознавания и индекса, а не как нормализация сопоставления.** Индексы строятся из слов (200K), stem+endings (76K) и морфов (76K). Поиск по подсловному индексу специально ограничен: вхождение засчитывается, только если «после запроса не видно суффикса» (Sec. VI-B, ms. p. 5). Значит, словоформы запроса **не склеиваются** по основе, в отличие от stem matching в CR000691. Выигрыш подслов идёт от покрытия словаря (OOV), а не от сопоставления словоформ.
- **Главные числа** (Table VII, ms. p. 8; MTWV ×100; 1627 запросов, выбранных NIST Term Selection Tool):
  - глобальный порог: Words 65.1 → Stem+endings 68.6 → Morphs 71.1 → каскад Word+Morph 72.6;
  - термин-специфичный порог: 70.0 / 74.8 / 76.9 / 79.4;
  - доля OOV-запросов: 21.1% для слов, 4.6% для stem+endings, 0% для морфов.
  Итог: от 65.1 до 79.4, то есть +14.3 пункта (+22.0% отн.) **[computed]**.
- **IV/OOV.**
  - На словарных (IV) запросах лучше словный индекс: 77.6 против 76.3–76.6.
  - На внесловарных (OOV) запросах лучше морфы: 49.9 против 34.9 у stem+endings; словный индекс их не находит вовсе («-»).
  - Каскад: сначала поиск по словам, при пустом результате — по морфам. Он лучше обоих индексов, в том числе на IV (+1.1 / +1.7 к словам) **[computed]**.
- **Внутреннее несоответствие (наш расчёт по Eq. 1 самой статьи):** при 21.1% OOV-запросов, которые словный индекс найти не может, MTWV «all» для слов не может превышать 61.2 (глобальный порог) и 65.8 (термин-специфичный). Напечатано 65.1 и 70.0. Все четыре строки с термин-специфичным порогом согласуются с долей OOV ≈16.1%, а не 21.1% **[computed]**. Причина из статьи не устанавливается. Возможно, доля OOV и среднее TWV считаются по разным наборам запросов.
- **Чего нет:**
  - **BM25 и вообще ранжирующей модели документов** (ранжирование фрагментов по ожидаемому числу вхождений, затем порог);
  - **плотного/нейросетевого поиска**;
  - **гибрида лексического и семантического каналов** («hybrid» у авторов — это комбинация словного и подсловного индексов);
  - **перекрытия, уникально найденных релевантных объектов, oracle union**;
  - **разбора по отдельным запросам**, кроме агрегатов по IV/OOV;
  - тестов значимости для STD. Для ASR есть NIST MAPSSWE.
- **Для нашего gap:** работа **поддерживает** уже занятые положения:
  - подсловное/морфологическое представление индекса важно для поиска в тюркском языке;
  - комбинирование двух представлений по классу запроса — старая идея (каскад 2009 г. и ссылки [39]–[41]).
  Ядро v0.8 (raw/stem/lemma BM25 × фиксированный D → overlap/unique hits → прирост гибрида → признаки запроса) **не затрагивает**. Предложение: gap не менять.
- **Практическая польза для нас:**
  1. Признак запроса «термин вне словаря raw-индекса» (текстовый аналог IV/OOV) — кандидат для per-query анализа. Здесь переход word → stem+ending → morph снижает долю OOV-запросов 21.1 → 4.6 → 0%.
  2. Покрытие морфоанализатора нужно сообщать явно. Здесь парсер разбирает 96.7% токенов, но лишь 52.2% типов (Table II). Неразобранные слова остаются сырыми и размывают условия stem/lemma.
  3. Политику снятия неоднозначности разбора надо фиксировать: выбор разбора меняет результат (Table IV, WER 35.0–36.6).
  4. При разбиении на подмножества запросов надо публиковать их размеры, чтобы средние по подмножествам сверялись с общим.

---

## 1. Bibliographic record

- **Authors (as printed, ms. p. 1):** Ebru Arısoy, Doğan Can, Sıddıka Parlak, Haşim Sak, Murat Saraçlar.
- **Affiliations (ms. p. 1):**
  - Arısoy, Can, Parlak, Saraçlar: Department of Electrical and Electronics Engineering, Boğaziçi University, Istanbul;
  - Sak: Department of Computer Engineering (Boğaziçi).
- **Year:** 2009 (systematic-review metadata; consistent with the bibliographic check below).
- **Venue:** *IEEE Transactions on Audio, Speech, and Language Processing*. The venue comes from the systematic-review record and the bibliographic check below; the manuscript itself carries no journal header.
- **Volume / first page:** vol. 17, first page 874. Bibliographic check: NASA ADS bibcode `2009ITASL..17..874A`, seen in a web-search result listing; the ADS page itself could not be fetched (robots).
- **Issue / last page:** **not verified.** The systematic-review record gives 10 pages. An IEEE Xplore record exists (document 5071138, seen in a web-search result listing), but the page returned no content to our fetch.
- **DOI:** `10.1109/TASL.2008.2012313`. **Only partly verified** (bibliographic check: an ACM Digital Library URL `dl.acm.org/doi/abs/10.1109/TASL.2008.2012313` titled "Turkish Broadcast News Transcription and Retrieval", seen in a web-search result listing). The ACM page returned HTTP 403, and Crossref, OpenAlex and Semantic Scholar were blocked or rate-limited, so the DOI was not confirmed on an official landing page.
- **Funding (ms. p. 1):**
  - TUBITAK projects 105E102 and 107E261;
  - Boğaziçi University Research Fund (BAP) 05HA202 and 07HA201D;
  - TUBITAK BDP and BIDEB student support.
- **Prior conference versions (stated, ms. p. 1):** "Parts of this study were presented in conferences [1], [2], [3], [4]." [4] = Parlak & Saraçlar, "Spoken term detection for Turkish broadcast news", ICASSP 2008, which is the earlier STD system extended here (Sec. II).
- **Source type:** peer-reviewed journal article. The version read is an author manuscript.
- **Reliability:** A (venue); narrow retrieval evidence.
- **Full text available:** yes (`07_full_text/pdfs/CR001390.pdf`, 10-page manuscript).

## 2. Why this work matters to the PhD

| Axis | Relation |
|---|---|
| Lexical retrieval | Indirect. STD over lattice indexes of **words, grammatical stem+endings, and Morfessor morphs**. Utterances are ranked by the expected count of the exact query term, then thresholded. No document ranking model (no BM25/VSM) |
| Semantic retrieval | Absent. "Semantic" appears only in the related work on LM features (Sec. II-B) |
| Hybrid retrieval | Absent for lexical + semantic. The authors' "hybrid" / "cascade" combines **two lexical/subword indexes** (word → morph fallback) |
| Uzbek morphology | Indirect but close: Turkish is the nearest well-studied agglutinative Turkic relative. The paper documents OOV growth (735K word types per 40M tokens vs < 200K for English; Sec. IV-A) |
| Low-resource retrieval | Moderate: in-house broadcast-news audio and a 184M-word web corpus |
| Current gap | Supports already-occupied premises (the representation unit matters in Turkic retrieval; query-class routing between representations). Does not touch the lexical–dense complementarity core (§16) |

## 3. Research problem

### Simple explanation

Turkish words take many suffixes, so a speech recognizer with a fixed word list meets many words it has never seen. It then writes something else, and a later search for that word fails. The authors try smaller units (stems plus endings, or statistically learned word pieces) to make the recognizer and the search index cover more words. They then test how well each index can **find where a query term was spoken**.

### Formal formulation

- **ASR part** (Sec. IV–V, VII-A–C): compare LM units (words 50K–500K, stem+endings 76K/200K, morphs 50K/76K in four word-boundary schemes) by WER. Also compare discriminative AM training (MMIE) and discriminative LM training (perceptron DLM) over word and morph systems.
- **Retrieval part** (Sec. VI, VII-D): spoken term detection. Given a query term `q` and a threshold `θ`, return the utterances in which `q` occurs with an expected count above `θ`; then localize the term by forced alignment. The evaluation uses **TWV** (Eq. 1, ms. p. 8):

`TWV(θ) = 1 − (1/Q) Σ_{k=1..Q} { P_miss(q_k, θ) + β · P_FA(q_k, θ) }`

  **MTWV** is the maximum of TWV over θ. β is "a user defined parameter"; its value for the Table VII MTWVs is **NOT_REPORTED**. For term-specific thresholding the authors varied β to obtain the different operating points of the DET curves (ms. p. 8).
- Factors varied in STD: the index unit (words / stem+endings / morphs / word→morph cascade) × thresholding (global vs term-specific, following [38]).

## 4. Main idea

### Simple explanation

Build three recognizers: one that writes whole words, one that writes stems and endings, and one that writes statistical word pieces. Index everything each recognizer considered likely, not only its single best guess. Then:

- a query the word recognizer has never seen cannot be found in the word index, but can be found in a piece-based index;
- a query the word recognizer knows is found slightly better in the word index.

So search the word index first, and fall back to the piece index when it returns nothing.

### Concrete example (the paper's own, Fig. 2, ms. p. 4)

Phrase "derneklerinin öncülüğünde" (under the leadership of the associations):

| Unit | Segmentation (as printed) |
|---|---|
| Words | derneklerinin öncülüğünde |
| Morphs (Morfessor) | dernek lerinin # öncü lüğü nde |
| Morphemes, lexical | dernek -lArH -NHn öncü -lHk -SH -NDA |
| Morphemes, surface | dernek -leri -nin öncü -lüğ -ü -nde |
| Stem+endings, surface | dernek -leri-nin öncü lüğ-ü-nde |

- In the stem+ending row, the manuscript prints "öncü lüğ-ü-nde" **without** a leading "-" before "lüğ". The surface-morpheme row has "-lüğ". This is probably a typesetting slip; we did not correct it.
- STD consequence (Sec. VI-B, ms. p. 5): with a sub-word index, a query is found only where "no suffix is seen after the query". On our reading of that rule (the paper gives no example), a query `dernek` therefore does **not** match the occurrence "dernek -leri-nin". The sub-word index reproduces whole-word matching; it does not conflate inflected forms.

### Formal method

- **Indexing** (Sec. VI-A, ms. p. 5):
  - alternative ASR hypotheses (lattices) with their probabilities become weighted automata, following Allauzen, Mohri & Saraçlar [55];
  - all substrings are extracted; each utterance's automaton becomes a transducer whose output is the utterance id;
  - the transducers are unioned and determinized;
  - index weights are **expected counts**.
- **Retrieval** (Sec. VI-B): the query automaton is composed with the index. Utterances are ranked by expected count, and those above a threshold are returned. Thresholds are either **global** or **term-specific**; the term-specific ones are chosen "to maximize the TWV metric" [38].
- **Cascade** (Sec. VII-D, ms. p. 8): "First, the query was searched in the word based index. If no results were returned, it was searched in the morph based index [39]."

## 5. Architecture / algorithm

1. **Acoustic model** (Sec. VII-A, ms. p. 5):
   - speaker-independent, decision-tree-clustered cross-word triphones with 10,843 HMM states;
   - **graphemes** instead of phonemes ("Turkish is almost a phonetic language");
   - 11 Gaussians per state (23 for silence), HTK MFCC front end, AT&T decoding tools.
2. **Language models** (Sec. VII-A):
   - SRILM, interpolated Kneser-Ney, entropy pruning;
   - first-pass lattices rescored with unpruned LMs;
   - web and in-domain LMs linearly interpolated, with the interpolation constant and n-gram order tuned on held-out data.
3. **Recognition units** (Sec. IV; Table III, ms. p. 6):
   - **Words:** 50K–500K; 200K was chosen as the baseline.
   - **Stem+endings** (grammatical): the stem from the morphological parser, with the rest of the word as a surface-form ending. There are 901.2K distinct stems and 43.7K endings. The 76K and 200K most frequent units were used, and 76K was chosen as the baseline.
   - **Morphs** (statistical): Baseline-Morfessor with default settings, trained on words occurring ≥ 3 times (50K morphs); other words were segmented by Viterbi. Four word-boundary schemes were tried; the authors' best (on the test set, 22.9) marks non-initial morphs with "-" (76K types). On held-out data the concatenated-endings scheme is slightly better (23.9 vs 24.1; Table III).
4. **Morphological parser** (Sec. III-C, ms. p. 3):
   - two-level morphology (Sak, Güngör & Saraçlar [47]), with rules and lexicon adapted from Oflazer's PC-Kimmo description and a new 54,267-root lexicon;
   - **no disambiguation**: the outputs were "not compatible with the input expected by the available disambiguation tools";
   - the parse with the fewest morphemes was chosen (Table IV).
5. **Discriminative training** (Sec. V, VII-B–C):
   - MMIE acoustic training with word or morph LMs;
   - perceptron DLM over 50-best lists with word and/or morph unigram+bigram features, 12-fold cross-validation for the LM, oracle-best path as the gold standard, α0 tuned on held-out data.
6. **STD** (Sec. VI, VII-D):
   - word (200K), stem+ending (76K) and morph (76K, "-"-marked) lattice indexes;
   - global vs term-specific thresholds;
   - word→morph cascade.
   - Evaluated with NIST STDEval.
   - **Which partition was indexed for STD is NOT_REPORTED**, presumably the 3.3-hour test set of Table I (our inference).

## 6. Data

- **Acoustic data** (Sec. III-B; Table I, ms. p. 3):
  - ≈194 hours of Boğaziçi Turkish BN speech from VOA radio and the CNN Türk, NTV, TRT1 and TRT2 TV channels;
  - reference transcriptions contain 1.3M words;
  - disjoint splits: train 188 h, held-out 3.1 h, test 3.3 h (sum 194.4 h **[computed ✓]**).
  - Table I has columns f0, f1, f2, f3, f4, fx; the text lists the Hub4 classes f0–f4 and "(f5) other". The column label differs from the text (minor).
- **Text data** (Table II, ms. p. 3):
  - 184M words from the Milliyet (59M), NTV-MSNBC (75M) and Radikal (50M) web portals; 212M tokens;
  - parser coverage: 96.7% of tokens, **52.2% of types** (2.2M types);
  - after normalization: 182.3M tokens, 1.8M types.
- **STD query set** (Sec. VII-D, ms. p. 8):
  - **1627 queries** built with the NIST Term Selection Tool, which "randomly selects terms based on manual transcriptions";
  - single- and multi-word terms, foreign names and acronyms;
  - the number of queries per class (single/multi-word, IV/OOV) is **NOT_REPORTED** except as the percentages in Table VII.
- **Ground truth for STD:** not described explicitly; presumably term occurrences in the manual transcriptions (from which the terms were selected), scored by NIST STDEval (our inference). There are **no human relevance judgments**: correctness is occurrence-based (Context, not from the paper: this is standard for STD).
- **Train/dev/test for retrieval:** the thresholds are tuned per the TWV metric. **MTWV by definition takes the best threshold on the evaluated data** (Eq. 1 text). No separate STD development set is described.

## 7. Baselines

| Baseline | What it is | Fair comparison? |
|---|---|---|
| Word index (200K) | Whole-word lattice index | Yes. By construction it cannot detect OOV queries (Table VII OOV cell "-") |
| Stem+ending index (76K) | Grammatical sub-word index | Yes. Same AM, same real-time factor; vocabulary size matched to morphs |
| Morph index (76K) | Morfessor sub-word index | Yes, as above |
| Global threshold | One θ for all terms | Yes, the standard reference for term-specific thresholding |
| Word LMs 50K–500K (ASR) | Vocabulary-size baselines for WER | Yes. 50K/76K chosen to match the sub-word vocabulary sizes |

There is no ranking model for documents and no BM25/VSM, dense or semantic baseline. Phonetic indexes appear only in the related work.

## 8. Metrics

| Metric | Simple meaning | Notes |
|---|---|---|
| **WER** | Share of words the recognizer gets wrong | For sub-word systems, units are joined back into words before scoring (Sec. IV-C) |
| **Coverage** | Share of test word tokens the unit inventory can produce | For sub-words, a word counts as covered if some stem+ending or morph sequence can generate it (footnote 7, ms. p. 6) |
| **TWV / MTWV** | Term-detection score: 1 minus the average over queries of (miss rate + β × false-alarm rate); MTWV is the best value over thresholds | Eq. 1 (ms. p. 8). β NOT_REPORTED. Context (not from the paper): NIST weights false alarms heavily, so MTWV rewards precision |
| **OOV query percentage** | Share of queries containing at least one unit outside the index vocabulary | Table VII. Such a query "can be neither recognized by the ASR system nor detected by the STD system" (ms. p. 8) |
| **DET curve** | Miss probability vs false-alarm probability across operating points | Fig. 3. Global-threshold curves vary θ; term-specific (+TermTh) curves vary β (ms. p. 8) |

For our project, MTWV is **not** comparable to ranked-retrieval metrics (MAP/nDCG/Recall): it scores detection of exact term occurrences, not topical relevance of documents.

## 9. Results

### Table VII: STD MTWV (%) by index unit and thresholding (ms. p. 8; checked on 250-dpi crop)

| Index | Thresholding | OOV query % | MTWV all | MTWV IV | MTWV OOV |
|---|---|---:|---:|---:|---:|
| Words | global | 21.1 | 65.1 | 77.6 | – |
| Stem+endings | global | 4.6 | 68.6 | 76.3 | 34.9 |
| Morphs | global | 0 | 71.1 | 76.6 | 49.9 |
| Word+Morph Cascade | global | 0 | 72.6 | 78.7 | 49.9 |
| Words | term-specific | 21.1 | 70.0 | 83.4 | – |
| Stem+endings | term-specific | 4.6 | 74.8 | 82.5 | 34.7 |
| Morphs | term-specific | 0 | 76.9 | 82.1 | 49.7 |
| Word+Morph Cascade | term-specific | 0 | **79.4** | **85.1** | 49.7 |

Derived values **[computed]**:

- **Sub-word vs word (all, global):** stem+endings +3.5 (+5.4%); morphs +6.0 (+9.2%).
- **Cost on IV queries:** stem+endings −1.3 (global) / −0.9 (term-specific); morphs −1.0 / −1.3 vs words. The authors call this decrease "very small compared to the gain over the OOV set".
- **Morphs vs stem+endings on OOV queries:** 49.9 vs 34.9 (+15.0, global). Stem+endings still leave 4.6% of queries OOV.
- **Cascade vs best single index (morphs):** +1.5 (global), +2.5 (term-specific). **Cascade vs words on IV queries:** +1.1 / +1.7. This is the only non-structural part of the cascade gain: IV queries for which the word index returned nothing get morph-index results. Cascade OOV = morph OOV (49.9 / 49.7), as expected when OOV queries always fall through to the morph index.
- **Term-specific vs global thresholds:** +4.9 (words), +6.2 (stem+endings), +5.8 (morphs), +6.8 (cascade). The authors' "5–7% absolute increase" holds after rounding (4.9 ≈ 5).
- **Headline claim** (Sec. VII-D, ms. p. 8): "the MTWV increases from 65.1% (Words) to 79.4% (Word+Morph Cascade with term-specific thresholding)". That is +14.3 points, +22.0% relative **[computed ✓]**. It combines two changes (index representation and thresholding).
- **Implicit definition of the IV/OOV subsets.** The morph row has 0% OOV queries but still reports an OOV MTWV (49.9). The IV/OOV partition therefore appears to be defined relative to the **word** vocabulary for all rows. This is our inference; the paper does not state it.

**Internal arithmetic inconsistency (found by us).**

- TWV (Eq. 1) is an average over queries. An OOV query in the word index has P_miss = 1 and P_FA = 0, so it contributes 0.
- With 21.1% OOV queries, the Words "all" MTWV can be at most 0.789 × IV MTWV:
  - ≤ 61.2 (global) **[computed]**, but 65.1 is printed;
  - ≤ 65.8 (term-specific) **[computed]**, but 70.0 is printed.
- Solving `all = (1 − x)·IV + x·OOV` for the OOV share x on the four term-specific rows gives **x = 16.07%, 16.11%, 16.05%, 16.10%** **[computed]**. This is a consistent ≈16.1%, not 21.1%. The global rows are also compatible with x ≤ 16.1%.
- The paper cannot tell us why. Plausibly the "OOV query percentage" is computed over a different query set than the one averaged in TWV (for example, all 1627 selected terms vs the terms scored by STDEval). We do not resolve it. The IV/OOV conclusions are unaffected in direction, but the printed 21.1% should not be used to weight the subsets.

### Fig. 3: DET curves (ms. p. 8)

- It plots Words, Words+TermTh, Morphs, Morphs+TermTh and Cascade+TermTh, with MTWV points marked.
- Stem+endings and the global cascade are **not plotted**.
- Visually, Cascade+TermTh has the lowest miss probability over the false-alarm range where it is plotted (roughly .0005–.01%; the other curves extend further). No numbers were read off the figure.

### ASR results used as context (Tables III–VI, ms. pp. 6–8)

| System | Test WER (%) | Location |
|---|---:|---|
| Words 50K / 76K / 200K / 300K / 500K | 29.4 / 27.0 / 24.1 / 23.9 / 23.7 | Table III |
| Stem+endings 76K / 200K | 23.2 / 23.1 | Table III |
| Morphs, best scheme (non-initials marked, 76K) | 22.9 | Table III |
| MMIE AM, morph LM (trained with morph LMs) | 21.3 | Table V |
| Morph DLM (morph uni+bigram features) | 22.2 (Δ 0.7) | Table VI |

- Words 50K → 500K: coverage +7.3 points and WER −5.7 points **[computed ✓]**, matching the text ("increases the coverage by 7.3% and decreases the WER by 5.7%"; the text's "%" are absolute points).
- Morphs vs the word 500K system: −0.8 WER points **[computed]**. The authors: the morph model "yields significant improvements (p < 0.001) over all the word based systems" (NIST MAPSSWE). Stem+endings are "significantly better than 50 K, 76 K and 200 K word models", with no significance statement vs 300K/500K (ms. p. 7).
- Sub-words reduce the WER on OOV words from 100% to 77% (stem+endings) and to 71% on average (morph schemes) (ms. p. 7).
- Parse selection (Table IV, stem+ending LMs from reference transcriptions only):
  - all parses 35.2;
  - fewest morphemes 35.0;
  - random per token 35.8;
  - random per type 36.6.
  The first two do not differ significantly and are significantly better than random (ms. p. 6).
- DLM: no significant gain on the word system (24.1 → 23.8). Morph DLM gains of 0.5–0.7 are significant at p < 0.001 (Table VI, ms. p. 8; text ms. p. 7).
- Consistency checks **[computed ✓]**:
  - 901.2K stems + 43.7K endings = 944.9K ≈ the "945 K surface form stem and ending types" (ms. pp. 4, 6);
  - Table II portal word counts 59 + 75 + 50 = 184M, and tokens 68 + 86 + 58 = 212M.

## 10. Statistical evidence

- **Significance tests:**
  - ASR: NIST MAPSSWE with p-levels (p < 0.001, p < 0.01) for the vocabulary-size, sub-word and DLM comparisons (ms. pp. 6–7). MMIE training with morph LMs "does not introduce any statistically significant improvement over the one with word LMs" (ms. p. 7).
  - **STD: none reported.** No test for sub-word vs word, cascade vs morphs, or term-specific vs global.
- **Confidence intervals:** NOT_REPORTED.
- **Runs / seeds:** not applicable (deterministic decoding); variability NOT_REPORTED.
- **Ablation:** unit × thresholding is a 4 × 2 factorial in Table VII. The cascade is compared with its two components. No cascade of word + stem-ending, and no stem-matching variant.
- **Per-query analysis:** **only aggregates over query classes** (all / IV / OOV). No per-query scores, no breakdown by single vs multi-word terms, foreign names or acronyms (although the query set contains them), and no query-length analysis.
- **Overlap / unique hits / oracle union** between indexes: **none**. The cascade result implies that the morph index finds some occurrences the word index misses (+1.1 / +1.7 on IV queries), but the size of that set is not reported.
- **Operating-point caution:** MTWV takes the best threshold on the evaluated data by definition. Term-specific thresholds follow [38]; whether any of their parameters were tuned on held-out data is **NOT_REPORTED**.

## 11. Strengths

- The same AM, the same real-time factor and matched vocabulary sizes (76K) make the unit comparison controlled on the ASR side (Sec. VII-A, Table III).
- It compares a grammatical (parser) segmentation and an unsupervised (Morfessor) segmentation in both ASR and STD.
- Explicit **query-class analysis** (IV vs OOV) with a simple, interpretable routing rule (cascade) that exploits the class difference.
- A large, randomly selected query set (1627 terms) and the standard NIST STD metric and toolkit.
- Honest reporting of negative ASR results: no DLM gain for words, no significant MMIE difference.
- Documents practical morphology issues: parser type coverage 52.2%, parse ambiguity and its measured effect (Table IV).

## 12. Limitations

### Stated by the authors

- Sub-word indexes lose a little on IV queries; the OOV gain "is strongly dependent on the OOV query percentage" (ms. p. 8).
- Morphological ambiguity could not be resolved with the available disambiguators because of format incompatibility (ms. p. 6).
- Word-boundary-marking choices for morphs change accuracy significantly, and the WB-morph schemes hurt IV words (ms. p. 7).
- No DLM gain over the 200K word model, possibly because of more data and a larger vocabulary (ms. p. 7).

### Inferred from the experimental design

1. **Retrieval = term detection, not document retrieval.** Relevance is the occurrence of the exact term, so no topical relevance, qrels or ranking-quality metric is involved. The findings cannot be read as evidence about ad hoc document ranking.
2. **Sub-word indexes emulate whole-word matching** ("no suffix ... after the query"). The morphological representation acts through **ASR vocabulary coverage**, not through conflating inflected forms. This is a different mechanism from stemming/lemmatization in text IR.
3. **Arithmetic inconsistency** between the OOV query percentage (21.1%) and the MTWV decomposition (≈16.1% implied) (§9). The subset sizes are not reported, so the reader cannot reconcile them.
4. **No significance tests for any STD comparison.** Several differences are 1–2.5 MTWV points.
5. **β, the partition indexed for STD, the query counts per class, and any tuning data for term-specific thresholds are NOT_REPORTED.**
6. **The cascade's advantage on OOV queries is structural:** the word index scores nothing on them. Only the IV improvement (+1.1 / +1.7) is an empirical complementarity signal, and it is not decomposed.
7. **The headline +14.3 conflates two interventions** (index representation and thresholding).
8. **Only an author manuscript was read.** The published numbers could differ; this was not checked.

## 13. What the work proves

- In Turkish BN STD with lattice indexes, **sub-word indexes beat a 200K word index overall** (MTWV 68.6 stem+endings, 71.1 morphs vs 65.1, global thresholds). They achieve this mainly by **making OOV queries detectable**, at a cost of about 1 point on IV queries (Table VII).
- **Unsupervised Morfessor morphs beat parser-based stem+endings** for STD (71.1 vs 68.6 all; 49.9 vs 34.9 OOV). Stem+endings still leave 4.6% of queries OOV.
- A **word→morph cascade** beats both single indexes (72.6 / 79.4). It also gains on IV queries (+1.1 / +1.7 vs words), so the morph index recovers some IV occurrences that the word index misses.
- **Term-specific thresholds add about 5–7 MTWV points** for every index type (Table VII).
- On the ASR side, sub-word LMs (76K units) reach **lower WER than a 500K word vocabulary** (22.9–23.2 vs 23.7). The morph gains are significant vs all word systems (MAPSSWE, p < 0.001; Table III, ms. p. 7). Stem+endings are reported significant only vs the 50K, 76K and 200K word models; no significance is stated vs 300K/500K.
- The authors' conclusions are stated without significance tests for STD; the direction of the STD results is consistent across both thresholding regimes.

## 14. What the work does NOT prove

- **Anything about document retrieval** (SDR): no ranked news-story retrieval, no qrels, no BPref/MAP. The group's SDR stemming evidence is in CR000691, not here.
- **Anything about BM25, VSM or any lexical ranking model**, or about stemming/lemmatization as a *normalization of matching*. Here the sub-words do not conflate inflected forms at query time.
- **Anything about semantic, dense or neural retrieval**, or about lexical–semantic hybrids.
- **That the two representations are complementary at the item level** (unique relevant hits, overlap, oracle union). Only class-level aggregates exist, and the OOV part is guaranteed by construction.
- **That the cascade is significantly better** than the morph index alone: no test is reported.
- **Per-query or query-feature effects** beyond the IV/OOV class. The multi-word, foreign-name and acronym subsets are not analysed.
- **That lemma-level representations would help.** No lemma unit exists; stem+endings use the parser's stem with no disambiguation.

## 15. Relationship to current Uzbek evidence

- No Uzbek data. Turkish is the closest agglutinative Turkic relative, so the **vocabulary-explosion argument transfers directly**: the paper reports 735K Turkish word types per 40M tokens, vs < 200K for English (Sec. IV-A). In Uzbek text IR the analogous problem is **query terms absent from the raw index vocabulary**. Stemming/lemmatization or sub-word units reduce that problem (here 21.1% → 4.6% → 0% OOV queries).
- **The Turkish cluster in our corpus:**
  - Can et al. 2008 (MORPH-001) and Haddad & Bechikh Ali 2014 (MORPH-002): text IR, stemming helps, prefix truncation competitive;
  - Parlak & Saraçlar 2009 (CR000691): SDR with stemming (BPref) plus STD;
  - this paper: STD and ASR only.
  This paper adds the **ASR/index-unit** side and the query-class cascade. It adds no text-IR or document-ranking evidence.
- **Relation to CR000691 (same group, noted in the assignment):**
  - This paper does **not** cite CR000691; CR000691 cites this paper as its ref. [1].
  - Both report word/sub-word STD with an IV/OOV split and a word+morph cascade, but the numbers differ:
    - CR000691 Table 1: Word MTWV 56.71, cascade 64.75, word OOV-q 27.3%, units Word/Morph/S-SE/G-SE;
    - this paper: Words 65.1, cascade 72.6 (global), OOV-q 21.1%, units Words/Stem+endings/Morphs.
  - The setups are evidently different (unit inventories, and query sets or thresholds not stated in comparable form), so the numbers must **not** be pooled or compared across the two papers. We do not reconcile them.
  - CR000691's open issue 8 ("confirm that CR001390 has no SDR experiment") is **confirmed**. SDR appears only as a definition (ms. p. 1) and in cited Finnish SDR work ([43]–[45], ms. p. 2).
- The Uzbek national morphology works (Bakaev, Xusainova, Elov) provide analyzers. This paper's Table II and Table IV show two things our Uzbek pipeline must report: analyzer coverage and the ambiguity-resolution policy.

## 16. Relationship to CURRENT_GAP

**Classification:** *supports* (already-occupied premises) + *no material effect on the residual core*.

- **Supports / confirms as occupied** (already v0.8 non-claims):
  - "morphology / sub-word representation has not been applied to Turkic search";
  - "query-dependent strategy / query-type analysis is new". A 2009 A-venue example routes queries between two index representations by result availability, with an IV/OOV class analysis. It cites earlier word/phone cascades ([39], [41]).
- **Weak precedent relevant to the core idea:**
  - different representations of the **same lexical signal** serve different **query classes**: the word index is best on IV, morphs are best on OOV;
  - combining them helps even on IV queries.
  This motivates, in spirit, our question of *which* queries' relevant items each representation uniquely recovers. However:
  - it compares word vs sub-word **lexical** indexes, not lexical vs dense;
  - it is term-occurrence detection, not relevant documents;
  - it reports class aggregates, not unique hits / overlap / oracle union;
  - the sub-word matching deliberately does not conflate inflected forms.
- **No material effect on the core v0.8 elements:**
  - raw/stem/lemma **BM25** × a **fixed dense D**;
  - unique relevant hits / overlap / oracle union;
  - incremental hybrid gain;
  - the link to Uzbek query features.
  None of these is present. None of the four "What can still kill this gap" conditions is met.

**Proposal:** keep v0.8 refined unchanged. Optionally cite this paper with CR000691 in the Turkish boundary (GAP_BOUNDARY §3.1–3.2) as spoken-retrieval evidence on representation units and query-class routing. This is a proposal only; `CURRENT_GAP.md` has not been edited.

## 17. Implications for our research design

- **Query taxonomy (candidate feature):** "query contains ≥ 1 term absent from the raw BM25 index vocabulary" (raw-OOV), and its share of query terms. Here it is the single strongest class split between representations. For Uzbek we would test *per query* whether raw → stem → lemma changes the lexical channel's unique relevant documents mainly for raw-OOV queries. This is a hypothesis to test, not evidence.
- **Morphology preprocessing — report coverage and ambiguity policy:**
  - Report the Uzbek analyzer's **token and type coverage** on our corpus and queries, as in Table II (96.7% tokens but 52.2% types here). State what happens to unanalysed words; presumably they stay raw.
  - **Fix and report the disambiguation rule** for lemmas: the choice among parses changed WER by up to 1.6 points here (Table IV). A lemma condition without a stated policy is not reproducible.
- **Optional cheap control:** a **fallback (cascade) baseline**: `BM25_raw`, switching to `BM25_stem` / `BM25_lemma` when raw returns fewer than *k* results. This is a representation-routing baseline that is not fusion. It is optional and not required for the core; it helps separate "the stem index recovers missing terms" from "the stem index re-ranks".
- **Metrics / reporting hygiene:**
  - Whenever results are split into query subsets, **publish the subset sizes** and check that the subset averages reconcile with the overall average. This paper's 21.1% vs ≈16.1% mismatch shows the risk.
  - Report significance for every headline comparison.
  - Do not merge two interventions into one headline gain (here: representation + thresholding).
- **Protocol:** thresholds, fusion weights and cut-offs are selected on dev only. MTWV-style best-on-test operating points are optimistic. This reinforces the existing proposed decision from the Mekonnen card.
- **Terminology caution:** in the speech-retrieval literature, "hybrid" often means word + sub-word/phone indexes. When citing such work in Chapter I, do not present it as lexical–semantic hybrid retrieval.
- **Hypothesis:** consistent with (not evidence for) the expectation that changing the morphological representation of an agglutinative lexical index changes *which* queries it serves. Whether this changes its unique contribution relative to a dense D is untested.

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| ASR | Software that turns speech into text | Automatic speech recognition; outputs 1-best text, N-best lists or lattices |
| OOV / IV | A word the system's vocabulary does not / does contain | Out-of-vocabulary / in-vocabulary relative to the unit inventory |
| WER | Share of words the recognizer gets wrong | (substitutions + deletions + insertions) / reference words |
| Lattice | A compact graph of many alternative transcriptions with probabilities | Weighted acyclic automaton of ASR hypotheses |
| Spoken term detection (STD) | Find where a given word or phrase is spoken in a recording archive | Detection of term occurrences with scores and a threshold, via an index |
| Spoken document retrieval (SDR) | Find the relevant recordings (e.g., news stories) for a topic | Ranked retrieval over transcribed documents |
| Weighted automata indexation | Turn every hypothesis graph into a searchable index that stores how often each substring is expected to occur | Factor transducer over lattices, weights = expected counts [55] |
| Stem+ending | A word split by a grammar-based parser into its stem and one combined suffix string | Grammatical sub-word unit |
| Morph (Morfessor) | Word pieces learned automatically from text, without grammar rules | MDL-based unsupervised segmentation |
| MTWV | Term-detection score that penalizes misses and false alarms, at the best threshold | Maximum of TWV(θ) (Eq. 1), NIST STD 2006 |
| Term-specific threshold | A separate detection cut-off for each query term instead of one for all | Per-term θ chosen to maximize expected TWV [38] |
| Cascade (here) | Search the word index first; if nothing is found, search the morph index | Result-availability routing between two indexes |
| DLM / MMIE | Training methods that also learn from the recognizer's mistakes | Discriminative language / acoustic model training |
| Complementarity (project term) | Each channel finds some relevant items the other misses | Unique relevant hits, overlap, oracle-union gain |

## 19. Open questions / verification needed

1. **Published version:** compare the manuscript's Tables III–VII with the typeset IEEE TASLP version, and confirm the issue, page range and DOI `10.1109/TASL.2008.2012313` on an official record. Web checks gave only search-result listings (ADS bibcode `2009ITASL..17..874A`, ACM DL URL).
2. **OOV share inconsistency:** 21.1% (printed) vs ≈16.1% (implied by Table VII and Eq. 1). Which query set does each refer to? How many of the 1627 queries were scored?
3. The value of β; the audio partition indexed for STD; whether any held-out data was used for the term-specific thresholds.
4. Numbers of IV, OOV, multi-word, foreign-name and acronym queries; no per-class results beyond IV/OOV.
5. Significance of the STD differences (cascade vs morphs: +1.5 / +2.5).
6. How large is the set of IV occurrences found only via the morph fallback? Not reported; it would be the paper's only item-level complementarity signal.
7. Relationship to CR000691's STD numbers (different values for similarly named conditions). Do not pool the two papers.

## 20. Decision after deep dive

- **Keep current gap?** Yes. v0.8 refined remains valid (§16).
- **Modify gap?** No. Optionally list this paper with CR000691 in the Turkish evidence boundary as spoken-retrieval evidence on index units and query-class routing (researcher's decision).
- **Add decision?** Proposed for `decisions/DECISIONS.md` (researcher's decision):
  - "Report morphological-analyzer token/type coverage on the corpus and queries, and fix the parse-disambiguation rule for the lemma/stem conditions";
  - "When reporting results on query subsets, publish subset sizes and check that subset averages reconcile with the overall average".
- **Add experiment?** Optional: a raw → stem/lemma **fallback** control, and a per-query raw-OOV feature in the complementarity analysis. Neither is required for the core.
- **Add citation to Chapter I?** Yes, briefly:
  - §1.1, on OOV and vocabulary growth in agglutinative Turkic languages and on sub-word index units;
  - possibly §1.3 as a historical example of query-class routing between two *lexical* representations, with the explicit caveat that it is not lexical–semantic hybrid retrieval.
- **Proposed `MASTER_INDEX.md` row** (to add after approval):

| MORPH-017 | Arısoy, Can, Parlak, Sak, Saraçlar — *Turkish Broadcast News Transcription and Retrieval* (IEEE TASLP 17, 2009; author manuscript read) — [deep dive](deep-dives/2009_Arisoy_Can_Turkish_Broadcast_News_Transcription_Retrieval.md) | 2009 | A (venue; narrow retrieval evidence) | MEDIUM | Turkish BN ASR with word / parser stem+ending / Morfessor morph units (sub-words 22.9–23.2 WER vs 23.7 for 500K words) and spoken term detection (1627 NIST-selected queries, lattice indexes). MTWV: words 65.1, stem+endings 68.6, morphs 71.1, word→morph cascade 72.6; term-specific thresholds up to 79.4. Word index best on IV and morphs best on OOV; cascade gains on IV too. Sub-word matching deliberately does not conflate inflected forms. No SDR/document ranking, BM25, dense, lexical–semantic fusion, overlap/unique-hit or per-query analysis; STD significance not reported; printed OOV share (21.1%) inconsistent with the MTWV decomposition (≈16.1% implied). |
