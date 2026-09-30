# Braschler & Ripplinger (2004): How Effective is Stemming and Decompounding for German Text Retrieval?

**Targeted deep-dive status:** COMPLETED (AI-assisted, pending researcher review)
**Completed:** 2026-09-28
**Literature ID:** `MORPH-041` (assigned 2026-09-28, approved by researcher)
**Systematic-review record:** `CR000561`. Full-text triage: INCLUDE, reading priority HIGH, reading tier "2 — важно", `carries_complementarity_evidence = YES`. In this card we qualify the flag: the paper's per-query evidence is **qualitative and lexical-vs-lexical only**. It compares morphological representations of one lexical system on nine hand-picked topics. There is no second retrieval channel, and no counts of unique hits or overlap are reported (§10, §16).
**Provenance:** AI-assisted deep dive (Claude). The paper (26 PDF pages, printed pp. 291–316) was read in full from the pdftotext extraction. Page images were checked for every table and every significance listing reported here. Pages checked visually: printed pp. 296 (Table 1), 300 (Table 2 and Sec. 7 text), 305 (Table 3), 306 (Table 4), 307 (Sec. 8, Table 5 and T-query groupings), 308 (Table 6 and groupings), 309 (Table 7 and groupings), 310 (P@10 TDN groupings, start of Sec. 9), 312 (Sec. 9.6–9.9) and 313 (Sec. 9 summary, Conclusions). These are PDF pp. 6, 10, 15, 16, 17, 18, 19, 20, 22 and 23. Numbers computed by us are marked **[computed]** and were recomputed with Python. The recall/precision curves (Figs. 1–8) are not read numerically; no numbers are taken from them.
**Source rule:** **the paper is the primary and only authoritative source.** No code, website or later paper was used for claims about the authors' work. The DOI and issue number come only from a bibliographic check of the Springer article page (see §1).
**Verification:** independent AI verifier pass 2026-09-28; 9 findings addressed.
**Reliability:** **A** (peer-reviewed journal article, *Information Retrieval* 7, 291–316, 2004, Kluwer; received 20 Jan 2003, revised 14 May 2003, accepted 10 Sep 2003, p. 291). It is a primary controlled experimental study on a standard CLEF test collection with a formal statistical analysis.

---

## Кратко для исследователя (RU)

- **Что сделано.** Для немецкого языка на тестовой коллекции CLEF авторы сравнили 13 вариантов лексического индексирования (153 694 документа, 85 тем; Table 1, p. 296):
  - без стемминга;
  - слова + символьные 6-граммы;
  - самообучаемая сегментация Linguistica;
  - правиловый стеммер NIST;
  - коммерческий стеммер Spider (словарь + правила);
  - морфологический анализатор MPRO: лемма (lu) или деривационный корень (ls).
  NIST, Spider и MPRO проверены также в вариантах с декомпаундингом (разбиением сложных слов). Всё остальное (токенизация, стоп-слова, модель ранжирования) фиксировано (Sec. 5–6, pp. 295, 299).
- **Модель ранжирования не BM25**, а векторная схема Lnu.ltn с pivoted-нормализацией длины, slope = 0.15 (Sec. 6, p. 299). Плотного поиска, гибрида и объединения ранжированных списков нет (работа 2004 года).
- **Главные числа** (MAP, Table 2, p. 300):
  - короткие запросы (T): без стемминга 0.2275, лучший стемминг без декомпаундинга (NIST) 0.2792 (+22.7%), лучший с декомпаундингом (Spider FS) 0.3650 (+60.4%);
  - длинные запросы (TDN): 0.3321 → 0.3682 (+10.9%) → 0.4471 (+34.6%).
  - Все проценты в Tables 2–4 пересчитаны нами и сходятся (одно расхождение 0.1 п.п., §9).
- **Статистика:** ANOVA (13 прогонов × 85 тем) с группировкой по Тьюки (Sec. 8, pp. 307–310). Значимые различия получены только в пользу прогонов с декомпаундингом. **Ни один прогон «только стемминг» в опубликованных группировках значимо не превосходит прогон без стемминга**, ни по MAP, ни по P@10. Вывод авторов «стемминг полезен» опирается на средние значения. Это наш вывод из группировок, авторы его так не формулируют.
- **Длина запроса меняет эффект морфологии:** прирост от нормализации для TDN примерно вдвое меньше, чем для T. По P@10 на TDN ни один вариант значимо не лучше прогона без стемминга, а несколько вариантов даже ниже его (Table 4, p. 306; Sec. 8, p. 309).
- **Лемма не лучше «грубых» методов автоматически:** простой NIST-стеммер ≈ лемма MPRO (0.2792 vs 0.2682 для T). Деривационный корень MPRO (ls) хуже леммы без декомпаундинга, но лучше в сочетании с декомпаундингом (Table 2).
- **Разбор по запросам (Sec. 9)** — 9 тем, отобранных как «заметные», только качественно. Разные представления выигрывают на разных запросах:
  - без стемминга лучше, если ключевые слова уже в базовой форме или являются именами собственными;
  - декомпаундинг решающий, если составное слово в документах передаётся словосочетанием;
  - декомпаундинг вреден для «ложных» составных слов (Mitgliedschaft).
  В критериях отбора тем упомянуты «уникально найденные релевантные документы», но **их числа не приводятся**.
- **Внутренние несоответствия в статье** (§9, §19):
  - в тексте на p. 300 перепутаны половины Table 2 (декомпаундинг назван «нижней половиной»);
  - заголовок Sec. 9.8 указывает тему «CLEF 2002», хотя коллекция включает только темы 2000–2001;
  - в группировке на p. 308 фигурирует несуществующий код прогона «ls».
- **Для нашего gap:** работа поддерживает лексическую половину механизма: морфологическое представление меняет, *какие* запросы успешны, и эффект зависит от длины запроса. Ядро v0.8 (raw/stem/lemma BM25 × фиксированный D → перекрытие / уникальные находки → прирост гибрида) она **не затрагивает**. Предложение: gap не менять.
- **Практическая польза:**
  1. Длину запроса (короткий vs описательный) делать обязательным фактором.
  2. Орфографические варианты (Öl/Oel, Mitglied(s)staaten) — прямой аналог узбекских вариантов апострофа (o‘/o'/oʻ). Их нормализацию выделить в отдельное условие `BM25_simple-normalization`.
  3. Для уникальных находок заранее фиксировать глубину k: в работе глубина для «Recall» не указана.
  4. Для множества попарных сравнений нужен план статистики с поправкой на множественность.

---

## 1. Bibliographic record

- **Authors:** Martin Braschler; Bärbel Ripplinger
- **Affiliations (p. 291):** Eurospider Information Technology AG, Zürich (both); Université de Neuchâtel, Institut Interfacultaire d'Informatique (Braschler)
- **Year:** 2004
- **Venue:** *Information Retrieval*, vol. 7, pp. 291–316 (running header, p. 291)
- **Issue:** 3, September 2004 (bibliographic check: Springer article page, link.springer.com/article/10.1023/B:INRT.0000011208.60754.a1). The PDF itself does not print the issue number.
- **Publisher:** Kluwer Academic Publishers (p. 291; confirmed on the Springer page)
- **DOI:** `10.1023/B:INRT.0000011208.60754.a1` (bibliographic check: Springer article page). The DOI is not printed in the PDF.
- **Official URL:** https://link.springer.com/article/10.1023/B:INRT.0000011208.60754.a1
- **Dates (p. 291):** received 20 January 2003; revised 14 May 2003; accepted 10 September 2003
- **Source type:** peer-reviewed journal research article
- **Reliability:** A
- **Full text available:** yes (`07_full_text/pdfs/CR000561.pdf`, 26 pages)

## 2. Why this work matters to the PhD

It is one of the most-cited controlled studies of **how the morphological representation of the lexical index changes retrieval effectiveness** in a morphologically rich European language. It covers a wide spectrum in one fixed system:

- language-independent: character n-grams, unsupervised segmentation;
- rule-based stemming;
- lexicon-based stemming;
- full morphological analysis: lemma vs derivational root;
- each with and without compound splitting.

| Axis | Relation |
|---|---|
| Lexical retrieval | **Central.** 13 index representations under one vector-space model (Lnu.ltn). Not BM25 |
| Semantic retrieval | **Absent** (pre-neural; no LSI or embeddings either) |
| Hybrid retrieval | **Absent.** The "6gram + word" run combines two lexical feature types in one representation; it is not a lexical–semantic hybrid and not a fusion of separate runs |
| Uzbek morphology | Indirect. German is inflectional-fusional with productive closed compounding; Uzbek is agglutinative with suffix chains and fewer closed compounds. The methodological lessons transfer (representation choice, query length, per-query variation); the size of the effects does not |
| Low-resource retrieval | Not directly. German had CLEF resources in 2003. The paper's language-independent methods (n-grams, Linguistica) are the options available to low-resource languages |
| Current gap | Supports the lexical half of the mechanism (morphological representation → which queries succeed). No effect on the lexical–dense complementarity core (§16) |

## 3. Research problem

### Simple explanation

A word in a query often appears in a different form in relevant documents: another case ending, a derived word, or a compound like *Windenergie* ("wind energy") vs the phrase "Energie aus Wind". Search engines "stem" words to a common form so that the forms match. For German, a second problem is compounds. The authors ask:

- How much does stemming help German retrieval?
- How much does compound splitting help?
- How much linguistic knowledge is needed: is a crude, language-independent method enough, or do you need a full morphological analyzer?

### Formal formulation

For a fixed retrieval model (Lnu.ltn vector space) and a fixed tokenization and stop-word list, vary only the term-conflation function φ that maps word forms to index terms. Measure the effect of φ on MAP, number of relevant documents retrieved, and P@10, for short (T) and long (TDN) automatic queries on 85 CLEF topics. Test the differences between the 13 φ variants with ANOVA and Tukey grouping (Sec. 7–8).

The authors' framing (p. 292): previous studies usually compare one method against no stemming, so "Only an exhaustive comparison can give an indication of the right amount of linguistic knowledge and the right balance of conflation that is necessary."

## 4. Main idea

### Simple explanation

Build 13 versions of the same search index that differ only in how words are reduced before indexing. Run the same queries against each. Compare the averages, test which differences are statistically reliable, and then look closely at nine topics where the methods behave differently to understand *why*.

### Concrete example

The paper's own examples (Sec. 5.5, 5.6, 9.3):

- *Umweltaspekte* (environmental aspects):
  - Spider without decompounding → `umweltaspekt`;
  - Spider full split → `um-welt-aspekt`;
  - MPRO → `umwelt aspekt`.
- Topic "Nutzung von Windenergie" (CLEF 2000, topic 26): splitting *Windenergie* into *Wind* + *Energie* "results in the retrieval of nearly twice as many relevant documents" (Sec. 9.3, p. 311).
- Topic "Mitgliedschaft in der Europäischen Union" (CLEF 2000, topic 5): splitting hurts. Spider decompounding runs are "between 48% and 66%" worse than runs without decompounding (Sec. 9.2, p. 311), because "the core concept of 'member state' gets diluted".

### Formal method

- Index-term representation φ ∈ {none, word+6-gram, Linguistica, NIST, NIST+dec, Spider, Spider+dec×3, MPRO-lu, MPRO-ls, MPRO-lu+dec, MPRO-ls+dec}. That is 13 runs per query length.
- Ranking: Lnu.ltn weighting (Singhal et al. 1996) for documents (Lnu) and queries (ltn). "L" is a log-average term-frequency normalization, "u" is pivoted unique-term length normalization with slope 0.15 (Sec. 6, p. 299). *Context (not from the paper): this is the standard SMART reading of the Lnu.ltn codes; the paper gives only the name and the slope.*
- There is **no special weight for compound constituents** (Sec. 6, p. 299).

## 5. Architecture / algorithm

The 13 runs and their codes (Sec. 5, pp. 296–299). Lower-case code = stemming only; capitalized = with decompounding.

| Code | Name | What it does | Knowledge type |
|---|---|---|---|
| `n` | nostem | Surface word forms (the paper's baseline) | none |
| `6` | 6gram + word | Unstemmed words **plus** character 6-grams over unstemmed words; 6-grams may span word boundaries; index ≈ 3× the unstemmed word index | language-independent. The paper treats it as a "decompounding run" because 6-grams match compound parts (p. 301) |
| `l` | Linguistica | Unsupervised stem+suffix segmentation learned from the collection (Goldsmith 2001); lexicon ≈ 123,000 entries from ≈ 1.4 million unique terms. Causes "accidental decompounding": *Datenbank* → *Daten* | language-independent, statistical |
| `t` | NIST stem | Porter-like iterative rule-based suffix stripping (NIST ZPrise 2). Example: *glücklicherweise* → *gluck* | rule-based |
| `T` | NIST dec | `t` + corpus-based decompounding via constituent co-occurrence; "rather conservative" | rules + corpus statistics |
| `sn` | Spider NS | Commercial Eurospider stemmer: lexicon + rules; no decompounding | lexicon + rules |
| `Ss` | Spider SS | Split only if all parts share the compound's part of speech (conservative) | lexicon + rules |
| `Sc` | Spider CS | At least one part must match the compound's part of speech | lexicon + rules |
| `Sf` | Spider FS | "split whenever possible" (aggressive) | lexicon + rules |
| `mu` | MPRO lu | Lemma ("lexical unit") from the MPRO morpho-syntactic analyzer (IAI) | full morphology |
| `ms` | MPRO ls | Derivational root ("more aggressive"), e.g. *Kollisionen* → *kollidieren* | full morphology |
| `Mu` | MPRO lu dec | Compound split into lemma constituents | full morphology |
| `Ms` | MPRO ls dec | Compound split into derivational-root constituents | full morphology |

Fixed across runs (Sec. 5, p. 295): "apart from using different stemming and decompounding methods, all other indexing parameters remain constant (tokenization, stopword list, etc.)". **The tokenizer and the stop-word list are not described: NOT_REPORTED.**

Retrieval system: the commercial Eurospider "relevancy" system. Resources from each approach are plugged into its indexing module (Sec. 6, p. 299).

How the words and 6-grams of run `6` are combined (one mixed index or merged runs; relative weights): **NOT_REPORTED** beyond "we chose to combine 6-grams and unstemmed words" (p. 296).

## 6. Data

- **Dataset / corpus:** German part of CLEF 2000/2001 without the SDA newswire, i.e. *Frankfurter Rundschau* 1994 and *Der Spiegel* 1994–1995 (Sec. 4, p. 295; Table 1, p. 296)
- **Language / domain:** German; newspaper and news-magazine articles
- **Size (Table 1, p. 296):**
  - 153,694 documents, 383 MB;
  - indexing tokens per document (after stop-word removal): mean 156.09, median 128, min 1, max 2,885.
- **Queries:**
  - 90 CLEF topics (40 from 2000, 50 from 2001), minus 5 topics with no relevant documents in this subset, gives **85 topics** (Table 1, footnote a).
  - Each topic has title (T; "one to three keywords"), description (D; one sentence) and narrative (N; several sentences) fields (Sec. 7, p. 300).
  - Queries are built automatically, "without manual intervention", by indexing all or part of the topic text (Note 1, p. 314).
  - Two query lengths are reported: T and TDN.
- **Relevance judgments (Table 1):**
  - 20,980 assessments; 1,790 relevant documents;
  - relevant per topic: mean 21.06, median 12, min 1, max 109;
  - mean = 1790/85 = 21.06 **[computed ✓]**.
- **How the labels were produced:** the official CLEF relevance assessments. **The pooling procedure, the pool depth and the effect of removing the SDA documents on pool coverage are not described in this paper: NOT_REPORTED.**
- **Train / dev / test:** none. There is no learning component except Linguistica (unsupervised, run on the collection itself) and the NIST corpus-based decompounder. The Lnu slope 0.15 was "determined empirically to be the optimal value" (p. 299). **On which data it was chosen: NOT_REPORTED.**

## 7. Baselines

| Baseline | What it is | Why selected | Fair comparison? |
|---|---|---|---|
| `n` nostem | Surface-form indexing | Reference for all relative gains | Yes: same system, tokenizer, stop-words and weighting |
| `6` 6gram + word | Language-independent n-gram representation, following Mayfield et al. 1999 and Savoy 2003 | Represents the "no linguistic knowledge" end of the spectrum | Mostly. Index ≈ 3× larger; one slope (0.15, "determined empirically") is used for all runs, including this mixed word/6-gram index; on which run(s) it was optimized and any per-run tuning: NOT_REPORTED |
| Stemming-only runs `l`, `t`, `sn`, `mu`, `ms` | Increasing linguistic knowledge | Spectrum | Yes within the design. Spider and MPRO are proprietary tools; the Spider stemmer belongs to the authors' employer (see §12) |
| Decompounding runs `T`, `Ss`, `Sc`, `Sf`, `Mu`, `Ms` | Same stemmers + compound splitting | Isolates decompounding | Yes. Each has a stemming-only counterpart (`t`, `sn`, `mu`/`ms`), which makes the pairs natural ablations **[inferred]** |

The retrieval model is fixed to Lnu.ltn for all runs. The authors themselves warn that the scheme's document-length normalization is "a factor influenced by stemming", so "some caution may be appropriate when generalizing the results to approaches that use vastly different collection statistics for weighting" (Sec. 6, p. 299). That would include BM25 **[inferred; the paper does not name BM25]**.

## 8. Metrics

| Metric | Definition | Simple meaning | Appropriate? |
|---|---|---|---|
| MAP | Mean over topics of non-interpolated average precision over all relevant documents (p. 300) | "How high, on average, are all relevant documents ranked?" | Yes for ad hoc retrieval with pooled qrels |
| Number of relevant documents retrieved (Table 3, labelled "Recall") | Total relevant documents retrieved over all 85 topics, out of 1,790 | Coverage of relevant documents | Yes, but **the retrieval depth (cutoff) is NOT_REPORTED** |
| P@10 | Share of relevant documents in the top 10 | "Is the first result page good?" | Yes. The authors note that two systems may tie on topics with very few relevant documents although they rank them differently, "not necessarily a drawback" at cutoff 10 (p. 306) |
| Query-by-query measures (Sec. 9, p. 310) | AP, mean of P@5/10/15, mean of P@10/20/30, P@100, uniquely retrieved relevant documents, plus their standard deviations | Used only to **select** interesting topics | Values not reported |

## 9. Results

### Table 2: MAP (p. 300; checked on page image)

| Run | MAP T | Δ vs `n` (T) | Run | MAP TDN | Δ vs `n` (TDN) |
|---|---:|---:|---|---:|---:|
| `Sf` Spider FS | **0.3650** | +60.4% | `Sf` Spider FS | **0.4471** | +34.6% |
| `Ss` Spider SS | 0.3586 | +57.6% | `Ms` MPRO ls dec | 0.4440 | +33.7% |
| `Ms` MPRO ls dec | 0.3547 | +55.9% | `Ss` Spider SS | 0.4431 | +33.4% |
| `Sc` Spider CS | 0.3546 | +55.9% | `Sc` Spider CS | 0.4415 | +32.9% |
| `Mu` MPRO lu dec | 0.3385 | +48.8% | `Mu` MPRO lu dec | 0.4234 | +27.5% |
| `T` NIST dec | 0.3240 | +42.4% | `T` NIST dec | 0.4022 | +21.1% |
| `6` 6gram + word | 0.2757 | +21.2% | `6` 6gram + word | 0.3219 | **−3.1%** |
| `t` NIST stem | 0.2792 | +22.7% | `t` NIST stem | 0.3682 | +10.9% |
| `sn` Spider NS | 0.2722 | +19.6% | `sn` Spider NS | 0.3616 | +8.9% |
| `mu` MPRO lu | 0.2682 | +17.9% | `mu` MPRO lu | 0.3461 | +4.2% |
| `ms` MPRO ls | 0.2353 | +3.4% | `l` Linguistica | 0.3435 | +3.4% |
| `l` Linguistica | 0.2302 | +1.2% | `ms` MPRO ls | 0.3396 | +2.3% |
| `n` nostem | 0.2275 | — | `n` nostem | 0.3321 | — |

**[computed]** checks:
- All 24 printed relative gains in Table 2 recompute exactly from the printed MAPs.
- Text (p. 301): "Sf" outperforms "t" by 30.7% (T) and 21.4% (TDN) **[computed: 30.7% ✓, 21.4% ✓]**.
- Text (p. 301): the best variants of the two top methods gain "between 33% and 60%" **[computed: Sf/Ms range 33.7–60.4% ✓]**.
- Absolute gains: `Sf` − `n` = +0.1375 (T), +0.1150 (TDN); `t` − `n` = +0.0517 (T), +0.0361 (TDN) **[computed]**.
- **Query length:** no stemming already gains +46.0% MAP by moving from T to TDN (0.2275 → 0.3321) **[computed]**. The relative benefit of the best representation shrinks from +60.4% to +34.6%.
- **Conclusions' "decompounding contributes … 16% to 34% for short and 9% to 28% for long queries"** (p. 313). The paper does not say how this was computed. It is reproduced **[computed]** if each decompounding run is compared with its own system's stemming-only run, using `mu` (the better MPRO stemming-only run) as the MPRO reference:
  - T: `T`/`t` +16.0% … `Sf`/`sn` +34.1% (`Ss` 31.7, `Sc` 30.3, `Ms`/`mu` 32.3, `Mu`/`mu` 26.2);
  - TDN: `T`/`t` +9.2% … `Ms`/`mu` +28.3% (`Sf` 23.6, `Ss` 22.5, `Sc` 22.1, `Mu`/`mu` 22.3).
  - If `ms` is the reference for `Ms`, the T value would be +50.7%, outside the stated range. This is our reconstruction, not the authors' stated method.
- Conclusions' stemming gains "up to 23% for short (T) and up to 11% for long queries" = `t` +22.7% / +10.9% ✓.

**Internal inconsistency (p. 300).** Sec. 7 first says tables are divided into "approaches using decompounding (top half) and those using stemming only (lower half)". The Table 2 caption says the same, and the values confirm it. Yet the next paragraph says: "methods that use decompounding (lower half of Table 2) perform better than methods that do not split compound words (upper half of Table 2)". The halves are swapped in that sentence. The substance (decompounding > stemming only) is unaffected.

### Table 3: number of relevant documents retrieved, out of 1,790 (p. 305; checked on page image)

| Run | T | Δ (T) | Run | TDN | Δ (TDN) |
|---|---:|---:|---|---:|---:|
| `Sf` | **1669** | +30.3% | `Ms` | **1704** | +11.0% |
| `Sc` | 1665 | +30.0% | `Mu` | 1696 | +10.5% |
| `Ss` | 1657 | +29.4% | `Ss` | 1694 | +10.4% |
| `Ms` | 1625 | +26.9% | `Sc` | 1693 | +10.3% |
| `Mu` | 1624 | +26.8% | `Sf` | 1690 | +10.1% |
| `T` | 1577 | +23.1% | `T` | 1632 | +6.3% |
| `6` | 1551 | +21.1% | `6` | 1594 | +3.8% |
| `sn` | 1434 | +11.9% | `sn` | 1595 | +3.9% |
| `mu` | 1433 | +11.9% | `t` | 1595 | +3.9% |
| `t` | 1427 | +11.4% | `ms` | 1568 | +2.1% |
| `ms` | 1398 | +9.1% | `mu` | 1547 | +0.8% |
| `l` | 1300 | +1.5% | `l` | 1538 | +0.2% |
| `n` | 1281 | — | `n` | 1535 | — |

- All printed gains recompute exactly **[computed]**.
- Coverage **[computed]**:
  - `n` retrieves 71.6% (T) / 85.8% (TDN) of all relevant documents;
  - the best runs retrieve 93.2% (`Sf`, T) / 95.2% (`Ms`, TDN);
  - relevant documents never retrieved: 509 → 121 (T) and 255 → 86 (TDN).
  - In absolute terms, `Sf` adds 388 relevant documents over `n` for T queries, and `t` adds 146.
  - These are **aggregate** differences in counts. They do not show which documents are new, because no set overlap is reported.
- The cutoff depth for "retrieved" is **NOT_REPORTED**.
- Small tension (p. 305–306): the text says the 6-gram run "favorably compares to the stemming methods that do not use decompounding". That holds for T (1551 vs ≤ 1434), but for TDN it is 1 document below `sn` and `t` (1594 vs 1595).

### Table 4: P@10 (p. 306; checked on page image)

| Run | T | Δ (T) | Run | TDN | Δ (TDN) |
|---|---:|---:|---|---:|---:|
| `Sf` | **0.3835** | +30.9% | `Ss` | **0.4435** | +13.9% |
| `Ss` | 0.3824 | +30.6% | `Sf` | 0.4388 | +12.7% |
| `Sc` | 0.3824 | +30.6% | `Sc` | 0.4341 | +11.5% |
| `Ms` | 0.3800 | +29.7% | `Ms` | 0.4306 | +10.6% |
| `Mu` | 0.3706 | +26.5% | `Mu` | 0.4247 | +9.1% |
| `T` | 0.3553 | +21.3% | `T` | 0.3800 | −2.4% |
| `6` | 0.3047 | +4.0% | `6` | 0.3412 | −12.4% |
| `sn` | 0.3400 | +16.1% | `sn` | 0.3965 | +1.8% |
| `mu` | 0.3271 | +11.7% | `l` | 0.3847 | −1.2% |
| `t` | 0.3259 | +11.3% | `mu` | 0.3835 | −1.5% |
| `l` | 0.2929 | +0.0% | `t` | 0.3835 | −1.5% |
| `ms` | 0.2906 | −0.7% | `ms` | 0.3777 | −3.0% |
| `n` | 0.2929 | — | `n` | 0.3894 | — |

- All printed gains recompute to ±0.05 points, except `ms` (T): printed −0.7%, computed −0.79% **[computed]**. That looks like truncation or unrounded source values; it is immaterial.
- For **TDN**, no stemming (0.3894) is above 6 of the 7 runs outside the Spider/MPRO decompounding group: `T`, `6`, `l`, `mu`, `t`, `ms` **[computed]**. Only `sn` (0.3965) is above it.

### Sec. 9: query-by-query analysis (pp. 310–313), qualitative

Nine topics (≈ 10% of 85; 9/85 = 10.6% **[computed]**) were "selected for showing conspicuous behavior". Selection used AP, several early-precision averages, P@100 and "uniquely retrieved relevant documents", with their standard deviations (p. 310). None of these per-topic values is printed.

| Topic (as printed) | Winners | Mechanism the authors give |
|---|---|---|
| 2000/1 "Architektur in Berlin" | `Sf`, `Sc`, `Ss`, `Ms`, `l` | Conflating *Architektur*/*Architekt* "pulls in approximately 10% more relevant documents" |
| 2000/5 "Mitgliedschaft in der EU" | `n`, `l`, `t`, `sn`, `mu`, `Mu` | Decompounding dilutes "member state"; *-schaft* is a derivational suffix, not a compound part. Spelling variants *Mitglied(s)staaten* |
| 2000/26 "Nutzung von Windenergie" | all decompounding | *Wind* + *Energie*: "nearly twice as many relevant documents" |
| 2000/34 "Alkoholkonsum in Europa" | all decompounding | "50% additional relevant documents on average" |
| 2000/35 "Wölfe in Italien" | no clear picture | Only 1 relevant document; AP fluctuates with its rank |
| 2001/6 "Embargo gegen den Irak" | `n`, `l` | Keywords already in base form; stemming "only introducing further noise" |
| 2001/21 "Ölkatastrophe in Sibirien" | `Sf`, `Sc`, `Ss` | Decompounding absorbs writing-style variants (*Ölpipeline*/*Ölleitung*). MPRO splits *Oelleitung* but not *Ölleitung* (umlaut handling) |
| "2002"/25 "Schatzsucher" | decompounding + `t` | *Schatzsucher*/*Schatzsuche* must be related, via the constituent *Schatz* or the NIST stem *Schatzsu*. Accidental Spider conflation *finde*/*Fund* helps |
| 2001/27 "Schiffskollisionen" | `Sf`, `Sc`, `Ss` | Only Spider splits the compound; this matters for T. For TDN, the constituents appear in the narrative |

**Internal inconsistency:** Sec. 9.8 is headed "CLEF 2002 Campaign, Topic 25" (p. 312, checked on image). Sec. 4 builds the topic set from CLEF 2000 and 2001 only (p. 295). Either the heading is a typo or the topic is not part of the 85; the paper does not allow us to decide which.

Authors' summary of the per-query findings (p. 313, verbatim):
- "Cases where no stemming outperforms most or all of the stemming methods exist when all the keywords are already present in their base forms (and occur rarely in inflected forms) and represent simple concepts (no compound nouns) … Furthermore, queries consisting of proper names show such effects, especially in short queries."
- "An interesting line of research may be to consider how to automatically infer from corpus statistics how well compounds are represented by their constituents, and use this as a factor in the decision of whether to apply compound splitting or not."

## 10. Statistical evidence

- **Test:**
  - IR-STAT-PAK (Blustein 1998): two-way ANOVA with runs × queries, followed by Tukey grouping (Sec. 8, p. 307).
  - The Hartley test is used to check equality of variances, and "indicates that the assumption is satisfied".
  - Both raw and arcsine-transformed (arcsin √x) scores are analysed.
  - Done for MAP (Tables 5–6) and P@10 (Tables 7–8). Not done for the relevant-retrieved counts.
- **ANOVA tables (pp. 307–309; checked on images):**
  - Runs F: MAP T 17.577 (raw) / 17.393 (arcsine); MAP TDN 12.801 / 13.749; P@10 T 10.168 / 10.640; P@10 TDN 5.209 / 5.343. Critical value 1.7618.
  - Query F: 54.852–112.200, critical 1.2818. The topic effect is far larger than the run effect in every table.
  - DF: runs 12, query 84, error 1008, total 1104 = 13 × 85 − 1 **[computed ✓]**.
- **Significance level:** "The '≻' symbol denotes a statistically significant difference between two runs with probability p = 0.95" (p. 308). This presumably means 95% confidence; exact p-values: NOT_REPORTED.
- **Significant differences (verbatim listings, pp. 307–310):**
  - MAP, T and TDN: the Spider decompounding runs and `Ms` ≻ all stemming-only runs, `6` and `n`. `Mu` and `T` ≻ subsets. `Sf`/`Ss`/`Sc`/`Ms` vs `Mu`/`T` is **not significant** (p. 308).
  - P@10 T: decompounding runs ≻ several stemming-only runs, `6` and `n`.
  - P@10 TDN: only ≻ `6` (and `ms` for `Ss` in raw data). The authors: "no approach or variant outperforms the baseline of not using stemming at all in this scenario" (p. 309).
  - **Observation [inferred from the listings]:** in all eight listings no stemming-only run (`l`, `t`, `sn`, `mu`, `ms`) ever appears on the left of "≻". So no stemming-only run is shown to be significantly better than `n`, or than any other run. The Conclusions' "stemming is useful for German text retrieval in most cases" (p. 313) therefore rests on mean differences (+17.9% to +22.7% MAP for T for the top three stemmers `mu`, `sn`, `t`; +1.2% to +22.7% across all five stemming-only runs), not on significance. The Conclusions do add that "The different stemming methods show only weak significant differences, mainly in the high recall range" (p. 313). That sentence is not backed by any listed stemming-only difference and may refer to the P/R curves.
  - **Typo:** in the T arcsine MAP listing, "'T' ≻ 'ls', 'l', 'n'" (p. 308). There is no run "ls"; it is probably `ms`, but that cannot be decided from the paper.
- **Confidence intervals:** NOT_REPORTED.
- **Runs / seeds:** single deterministic run per configuration. Not applicable in the usual sense: lexical indexing is deterministic.
- **Ablation:** no formal ablation section. The design contains natural ablations **[inferred]**: decompounding on/off within NIST, Spider and MPRO; three decompounding aggressiveness levels (Spider); lemma vs derivational root (MPRO).
- **Per-query analysis:** yes, but **qualitative** and on a **non-random, hand-selected** subset of nine topics. There are:
  - no per-topic win/loss counts over all 85 topics;
  - no unique-relevant-document counts or overlap between representations (the measure was used for selection only);
  - no oracle union across representations;
  - no systematic query-feature analysis beyond T vs TDN.
  Query length is the only systematically varied query characteristic.

## 11. Strengths

- A **wide, controlled spectrum** of index representations: surface, n-gram, unsupervised, rule-based, lexicon-based, lemma, derivational root, and three decompounding strengths. Everything else is held fixed.
- Paired decompounding / no-decompounding variants isolate the contribution of compound handling.
- 85 topics with CLEF pooled judgments on long newspaper documents. That was large for the time, and the authors argue that it is "not immediately obvious" whether stemming gains measured on short-document collections transfer to large collections with long documents (pp. 292–293).
- Two query lengths throughout: a systematic query-feature dimension.
- A formal multi-system test (ANOVA + Tukey) with variance checking and a transformation robustness check. They report negative results honestly (P@10 TDN).
- The query-by-query section explains mechanisms (over/under-conflation, false compounds, spelling variants, proper names) rather than only averages.
- Recall-oriented (relevant retrieved) and precision-oriented (P@10) views are both reported.

## 12. Limitations

### Stated by the authors

- The results may not generalize to weighting schemes with "vastly different collection statistics", because Lnu length normalization is affected by stemming (Sec. 6, p. 299).
- No different weight for compound constituents (Sec. 6).
- With P@10, two systems may obtain the same score on topics with very few relevant documents even though they rank those documents differently (p. 306); the authors add that this is "not necessarily a drawback" at cutoff 10, but matters more for larger cutoffs such as P@100. AP fluctuates wildly on single-relevant topics (Sec. 9.5, p. 311).
- Some good results are due to "erroneous conflations, which turned out to produce good matches by chance" (p. 313).
- Domain-specific terminology (medical, chemical) is untested (Sec. 10, p. 314).
- The n-gram run is storage-intensive: index ≈ 3× (p. 296).

### Inferred from the experimental design

1. **Not BM25.** One vector-space model (Lnu.ltn) with one slope (0.15). The slope was "determined empirically to be the optimal value", on data NOT_REPORTED, possibly the same test topics. It is the same for all 13 representations, although vocabulary size and document-length statistics change with φ. Per-representation tuning may change the ranking of close runs.
2. **Stemming-only gains are not shown to be significant** in the published Tukey groupings (§10). The claim "stemming is beneficial even when using a simple approach" (abstract) is descriptively true but not statistically established here.
3. **Tukey HSD over 78 pairs** is conservative. Some real differences between close runs may be missed; a paired per-query test between a few planned contrasts would have more power.
4. **Proprietary components.** The Spider stemmer is the commercial product of the authors' employer (Eurospider, p. 291); MPRO is licensed. Its variants win most comparisons. No bias is shown, but reproducibility is limited and there is a potential conflict of interest (not declared as such in the paper).
5. **Query-by-query analysis is selective and non-quantitative.** Nine hand-picked "conspicuous" topics, with no reported per-topic numbers. Qualitative percentages ("≈ 10%", "nearly twice", "50%", "48%–66%") cannot be verified.
6. **Unique hits were measured but not reported.** The authors had "uniquely retrieved relevant documents" per method (p. 310) but give no counts. The set-level complementarity between representations therefore remains unknown.
7. **Pool bias is unaddressed.** CLEF pools were built from participants' runs. Representations that retrieve very different documents (6-grams, aggressive splitting) may be disadvantaged by unjudged documents. The paper does not discuss this. Removing SDA documents also changes the collection relative to the pooled runs.
8. **Retrieval depth for "Recall" (Table 3) is not stated.**
9. **Internal inconsistencies:**
   - swapped halves in the Table 2 text (p. 300);
   - "CLEF 2002" topic heading (p. 312);
   - "ls" run code in a significance listing (p. 308);
   - minor rounding in Table 4.
   None changes the main conclusions.

## 13. What the work proves

- **Morphological representation of the lexical index strongly changes effectiveness** in German news retrieval under Lnu.ltn:
  - MAP from 0.2275 (surface) to 0.3650 (best) for short queries;
  - from 0.3321 to 0.4471 for long queries (Table 2).
- **Good compound splitting adds significantly on top of stemming:** the Spider decompounding variants and `Ms` significantly beat every stemming-only run for MAP, T and TDN (Tukey, pp. 307–308). This does not hold for every decompounder: `T` (NIST dec) is significant only against `ms`, `l`, `n` (T raw), `ls`[sic], `l`, `n` (T arcsine), `n`, `6` (TDN raw) and `l`, `n`, `6` (TDN arcsine), never against its own stemming-only run `t`; `Mu` is not significant against `t` for MAP.
- **More linguistic knowledge is not monotonically better:**
  - simple NIST suffix stripping ≈ Spider ≈ MPRO lemma without decompounding (0.2792 / 0.2722 / 0.2682 T; Table 2), with no significant differences among them;
  - the MPRO derivational root is worse than the MPRO lemma without decompounding but better with it (mean differences only; neither `mu` vs `ms` nor `Ms` vs `Mu` appears as significant in the Tukey listings).
  - Aggressive (`Sf`) and linguistically careful (`Ms`) splitting reach almost the same MAP (0.4471 vs 0.4440, TDN).
- **Query length moderates the morphology effect:** relative MAP gains over `n` are roughly halved for TDN vs T (Table 2; e.g. `Sf` +60.4% → +34.6%, `t` +22.7% → +10.9%). For TDN P@10, no representation significantly beats surface forms (Sec. 8, p. 309).
- **Purely language-independent methods are not competitive for German here:**
  - Linguistica is +1.2% / +3.4% (T / TDN);
  - 6-gram + word is +21.2% (T) but −3.1% (TDN) (Table 2) and is significantly below the good decompounding runs.
- **Representations win on different queries** (qualitative, Sec. 9): surface forms win on proper-name / base-form topics; decompounding wins on phrasal-paraphrase compound topics and loses on "false" compounds.

## 14. What the work does NOT prove

- **Anything about BM25.** The authors themselves caution against transferring results to other weighting schemes.
- **Anything about dense / semantic retrieval, hybrid fusion or lexical–semantic complementarity.** None was run.
- **That stemming alone (without decompounding) is significantly better than no stemming.** It is not shown in the published significance listings.
- **How much the relevant sets of different representations overlap**, or how many relevant documents each representation finds uniquely. That was measured for selection but not reported; there is no oracle union.
- **Which query features systematically predict the best representation.** Only nine selected topics were analysed qualitatively, plus query length. The proper-name and base-form patterns are hypotheses, not tested effects.
- **That the ranking of close runs is stable** under a different weighting, slope, collection or judgment pool.
- **Anything about agglutinative languages or Uzbek.**

## 15. Relationship to current Uzbek evidence

- **No Uzbek data.** German (fusional inflection, productive closed compounds) differs from Uzbek (agglutinative suffix chains, vowel harmony, limited closed compounding). *Context (not from the paper): Uzbek has closed compounds such as* temiryo‘l *(temir + yo‘l, "railway"), but compounding is much less central to vocabulary mismatch than suffixation.* Decompounding is therefore a secondary issue for Uzbek; stemming vs lemma vs root is the primary one.
- **Consistent with the Turkic evidence in the index:**
  - MORPH-001 (Can et al. 2008): query length changes the stemming effect; elaborate lemmatization is not guaranteed to win.
  - MORPH-002 (Haddad & Bechikh Ali 2014): simple prefix truncation stays competitive with Zemberek.
  - Here, likewise, the simple NIST stemmer ≈ lemma, and T vs TDN changes the effect size.
- **Same classic CLEF cluster** (cards in `/home/claude/dd/cards/`):
  - CR000338 Hollink et al. 2004: eight languages, stem/lemma/decompounding/n-grams, CLEF 2002;
  - CR000491 Airio 2006: word normalization and decompounding, mono- and bilingual; it cites this paper.
  Together they establish that representation effects are language- and query-dependent. None of them has a dense channel.
- National Uzbek morphology resources (MORPH-UZ-001…008: Bakaev, Xusainova, Elov, Turayev) provide stemmers and lemmatizers but no controlled qrels-based comparison of representations. This paper is the kind of experiment those resources have not yet been put through for Uzbek. The dense-channel dimension is missing in both.

## 16. Relationship to CURRENT_GAP

**Classification:** *supports* (the lexical half of the mechanism) + *no material effect* on the residual core.

- **Supports:**
  - Changing the lexical representation changes **which queries succeed**, not only the average. Different representations win on different topics (Sec. 9).
  - The effect depends on a query characteristic: length (T vs TDN).
  This is the lexical-side precondition for our hypothesis that raw → stem → lemma changes the *set* of relevant documents that the lexical channel contributes, and hence its complementarity with D.
  The authors' own suggestion to decide compound splitting from corpus statistics per term or query (p. 313) is an early instance of "query-dependent representation choice". It reinforces the existing v0.8 non-claim that query-dependent strategies are not new.
- **Already covered non-claims:** "raw/stem/lemma have not been compared in morphologically rich IR" was already rejected (UPERF, Can, Haddad). This paper is another A-level classic for that boundary.
- **No material effect on the core:**
  - no BM25;
  - no dense retriever D;
  - no fusion;
  - no unique-hit/overlap/oracle numbers, even between the lexical representations themselves;
  - no query-feature analysis beyond length.
  The v0.8 elements "unique relevant hits", "overlap with a fixed D", "incremental hybrid gain" and "link to query features" are untouched.
- **Triage flag qualification:** `carries_complementarity_evidence = YES` should be read as "qualitative per-topic variation between lexical representations". It is not lexical–dense complementarity.

**Proposal:** keep v0.8 refined unchanged. Optionally cite this paper in the evidence boundary as a classic controlled, significance-tested study: morphological representation (including decompounding and n-grams) changes lexical effectiveness per query and interacts with query length, with no BM25, dense or fusion component. This is a proposal only; `CURRENT_GAP.md` has not been edited.

## 17. Implications for our research design

- **Lexical variants.**
  - Keep `BM25_raw / BM25_stem / BM25_lemma` as the core.
  - This paper suggests two optional controls that are cheap and interpretable:
    1. **`BM25_simple-normalization`** (orthographic only). The paper's umlaut (*Öl*/*Oel*) and binding-*s* (*Mitglied(s)staaten*) cases show that spelling-variant conflation is a separate effect from morphology. For Uzbek, the analogues are the apostrophe variants of o‘/g‘ (ʻ ‘ ’ ') and Latin/Cyrillic script.
    2. **A language-independent control:** character n-grams (+ words) or a truncation stemmer. It tests whether any gain requires linguistic knowledge. This paper found that purely language-independent methods were not competitive (Linguistica +1.2% / +3.4%; 6-gram + word competitive only for T and still significantly below the good decompounding runs), that a simple rule-based stemmer (NIST) suffices for stemming, and that decompounding needs lexical coverage or linguistic knowledge (Conclusions, p. 314).
  - Do not assume lemma > stem; test it. MPRO-lu ≈ NIST here.
- **Root vs lemma.** MPRO's derivational root (more aggressive) hurts without decompounding but helps with it. If an Uzbek analyzer can output both the lemma and the derivational root, a root variant is an optional aggressiveness level. It should not replace the lemma in the core design.
- **Weighting per representation.** Lnu slope was fixed across representations, and the authors warn that length normalization interacts with stemming. For BM25, **k1 and b should either be fixed a priori or tuned per representation on dev only**, and the choice reported. This is a proposed decision.
- **Query taxonomy.** Make **query length / query form** (keyword title vs sentence description) a mandatory factor. Add features suggested by Sec. 9:
  - share of query terms already in base form;
  - proper names;
  - compounds / multiword expressions;
  - spelling-variant presence.
- **Unique-hit measurements.**
  - Fix and report the depth k for "retrieved" (this paper does not).
  - Report unique relevant hits and overlap **between lexical representations as well as against D**. This paper had the measure but did not publish it; publishing it is cheap.
- **Statistics.**
  - Pre-register a small set of planned paired contrasts (e.g. raw vs stem, stem vs lemma, H_x vs D) with per-query paired tests (randomization/bootstrap) and a multiplicity correction.
  - Do not rely only on an omnibus ANOVA + Tukey over all pairs, which here left stemming-only gains non-significant.
  - Topic variance dominates here (query F ≫ run F), which supports per-query analysis.
- **Qrels / pooling.** Include all lexical variants (and D and the hybrids) in the pool. This paper's reliance on external CLEF pools means that very different representations can be penalized by unjudged documents.
- **Metrics.** Keep MAP / nDCG plus a recall-type coverage count at a stated depth plus an early-precision metric. The early-precision picture differed here, especially for long queries.
- **Hypothesis.** Consistent with, but not evidence for, our hypothesis. If representation changes which queries the lexical channel wins, the lexical channel's unique contribution relative to D may also change with representation. That remains to be measured.

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| Stemming | Cutting word endings so that related forms match (*informierte* → *informier*) | Conflation function φ mapping word forms to a stem; often not a linguistic word |
| Lemmatization | Mapping a word form to its dictionary form (*Kollisionen* → *Kollision*) | φ based on morphological analysis + lexicon |
| Derivational root | An even more general base covering derived words (*Kollision* → *kollidieren*) | MPRO "ls" feature |
| Decompounding | Splitting a compound into parts (*Windenergie* → *Wind* + *Energie*) | Adding or replacing index terms with compound constituents |
| Conservative vs aggressive splitting | Split only when safe vs whenever possible | Part-of-speech constraints on constituents (Spider SS / CS / FS) |
| Over-/understemming | Merging unrelated words vs failing to merge related ones | Conflation precision/recall trade-off |
| Character n-gram (6-gram) | Overlapping 6-letter pieces of text used as index terms | Language-independent sub-word representation |
| Linguistica | A program that learns stem+suffix splits from raw text without a dictionary | Unsupervised morphology (Goldsmith 2001) |
| Lnu.ltn | A classic vector-space weighting with document-length normalization | SMART weighting; pivoted unique normalization, slope 0.15 |
| T / TDN queries | Short title-only query vs long title + description + narrative query | Automatic query formulation from topic fields |
| MAP | Average of how high all relevant documents are ranked, per topic, then averaged | Mean of non-interpolated AP |
| P@10 | Share of relevant documents among the first 10 | Precision at cutoff 10 |
| ANOVA + Tukey | Tests whether systems differ at all, then which pairs differ, while controlling for many comparisons | Two-way ANOVA (runs × topics), Tukey HSD grouping |
| Arcsine transformation | A rescaling that makes precision scores closer to normally distributed | f(x) = arcsin(√x) |
| Pooling (CLEF) | Judging only documents that some participating systems retrieved | Qrels from the union of top-k of submitted runs |
| Unique relevant hits (project term) | Relevant documents found by one representation/channel but not the other | \|Rel ∩ (A \ B)\| at depth k |

## 19. Open questions / verification needed

1. **Retrieval depth** for Table 3 ("relevant documents retrieved"): NOT_REPORTED. Only the authors could confirm it.
2. **Tokenizer, stop-word list and data used to set slope = 0.15:** NOT_REPORTED.
3. **Sec. 9.8 "CLEF 2002 Campaign, Topic 25":** a typo, or a topic outside the 85? Not decidable from the paper.
4. **"ls" in the T arcsine MAP grouping (p. 308):** probably `ms`; not decidable.
5. **How the 16–34% / 9–28% decompounding gains were computed:** our reconstruction (each decompounding run vs its own system's stemming-only run, with `mu` as the MPRO reference) matches, but the method is not stated.
6. **Conclusions' "weak significant differences, mainly in the high recall range"** for the stemming methods: no listing supports it. Which analysis does it refer to?
7. **6-gram + word combination mechanism** (single mixed index vs merged runs; weighting): NOT_REPORTED.
8. **Unique relevant documents per method** were computed (p. 310) but not published. Are they reported anywhere else by the authors? This is not checked, under the source rule; checking it would require another source.

## 20. Decision after deep dive

- **Keep current gap?** Yes. v0.8 refined remains valid (see §16).
- **Modify gap?** No change proposed. Optionally add to the evidence-boundary list as a classic German example (researcher's decision).
- **Add decision?** Proposed for `decisions/DECISIONS.md` (researcher's decision):
  - "BM25 k1/b: fixed a priori or tuned per lexical representation on dev only; the choice is reported";
  - "the depth k for 'retrieved' / unique-hit counting is fixed in advance and reported";
  - "query length/form (keyword vs sentence) is a mandatory analysis factor".
- **Add experiment?** Optional low-cost controls in the Uzbek pilot:
  1. `BM25_simple-normalization` (apostrophe/script only) as a separate condition;
  2. a language-independent n-gram or truncation control;
  3. report unique hits and overlap between the lexical variants themselves, in addition to against D.
- **Add citation to Chapter I?** Yes:
  - §1.1: morphological normalization as a design choice of the lexical representation; simple vs linguistic methods; query-length interaction; compound handling; classic evidence that more linguistic knowledge is not monotonically better.
  - Possibly §1.3, as an example of per-query variation between representations with no inter-channel analysis.
- **Proposed `MASTER_INDEX.md` row** (to add after approval):

| MORPH-041 | Braschler & Ripplinger — *How Effective is Stemming and Decompounding for German Text Retrieval?* (*Information Retrieval* 7(3), 291–316, 2004) — [deep dive](deep-dives/2004_Braschler_Ripplinger_German_Stemming_Decompounding.md) | 2004 | A | HIGH | German CLEF (153,694 docs, 85 topics), 13 index representations under Lnu.ltn (not BM25): surface, 6-gram+word, Linguistica, NIST, Spider, MPRO lemma/root, ± decompounding. MAP T 0.2275 → 0.2792 (best stemming) → 0.3650 (Spider FS); TDN 0.3321 → 0.3682 → 0.4471. Spider and MPRO-ls decompounding significantly beat all stemming-only runs (ANOVA/Tukey; NIST dec does not beat its own stemmer); no stemming-only run shown significantly above no stemming; gains halve for long queries. Qualitative 9-topic analysis: representations win on different queries. No BM25, dense, fusion, or unique-hit/overlap numbers. |
