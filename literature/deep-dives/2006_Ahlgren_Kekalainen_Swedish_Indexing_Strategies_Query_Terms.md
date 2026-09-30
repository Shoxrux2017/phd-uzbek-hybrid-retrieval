# Ahlgren & Kekäläinen (2006): Swedish full text retrieval: Effectiveness of different combinations of indexing strategies with query terms

**Targeted deep-dive status:** COMPLETED (AI-assisted, pending researcher review)
**Completed:** 2026-09-28
**Literature ID:** `MORPH-031` (assigned 2026-09-28, approved by researcher)
**Systematic-review record:** `CR000490`. Full-text triage: INCLUDE, reading priority HIGH, reading tier "2 — важно", `carries_complementarity_evidence = YES`. In this card we qualify that flag as *per-topic AP deviation from the median of seven lexical runs only* (§10, §16); there is no relevant-set overlap, unique-hit or oracle-union evidence, and no dense channel.
**Provenance:** AI-assisted deep dive (Claude). The paper (17 PDF pages, printed pp. 681–697) was read in full from the pdftotext extraction. Page images were checked for every table, figure and appendix item whose numbers are reported here: printed pp. 681 (PDF p. 1: title, abstract, dates), 687 (PDF p. 7: combinations list, test collection), 690 (PDF p. 10: Table 1), 691 (PDF p. 11: Fig. 1, Table 2), 692 (PDF p. 12: Table 3, Friedman test, multiple comparisons), 694 (PDF p. 14: Appendix 1 queries), 695 (PDF p. 15: Appendix 2, Fig. 2). Numbers computed by us are marked **[computed]** (recomputed with Python). Values read off bar charts are marked **[approximate, read from figure]**.
**Source rule:** **the paper is the primary and only authoritative source.** No code, website, later paper or background knowledge is used as evidence about what the authors did. Issue number and issue date were obtained from the publisher's page (bibliographic check: link.springer.com article page for DOI 10.1007/s10791-006-9009-1); Crossref could not be reached from this environment.
**Reliability:** **A** (peer-reviewed journal article, *Information Retrieval*, Springer, 2006; received 6 April 2005, accepted 28 June 2006, p. 681).
**Verification:** independent AI verifier pass 2026-09-28; 5 findings addressed.

---

## Кратко для исследователя (RU)

- **Что сделано.** Классическое контролируемое сравнение способов учёта морфологии шведского языка в лексическом поиске на коллекции CLEF 2003 (142 819 новостных статей, 54 темы с известными релевантными документами, 1 006 релевантных документов; p. 687), система InQuery 3.1 (сеть вывода, операторы #sum/#syn), MAP при глубине 1000 (p. 690). Семь комбинаций «индекс × обработка запроса»:
  - INFL-orig: индекс словоформ + исходные слова (базовый вариант, raw);
  - INFL-trunc: индекс словоформ + **ручное правостороннее усечение** экспертом, все формы индекса с данным префиксом группируются в #syn;
  - четыре варианта SPLIT: **нормализация (лемматизация) морфоанализатором SWETWOL + разбиение композитов** и в индексе, и в запросе; запросы строятся вручную (int) или автоматически (aut), с правилом Compound Elimination Principle (EL) или без него;
  - STEM-stems: стеммер Snowball для шведского, без разбиения композитов.
- **Главные числа** (Table 1, p. 690; MAP): INFL-orig 0.2742; INFL-trunc 0.3621 (+32.1%); STEM 0.3359 (+22.5%); SPLIT 0.3265–0.3315 (+19.1…+20.9%). Все относительные приросты воспроизводятся **[computed]**.
- **Значимость** (тест Фридмана + множественные сравнения, p. 692): Fr = 24.73, df = 6, p < 0.001. Значимо лучше базового варианта только INFL-trunc, SPLIT-split-int, SPLIT-split-aut. **STEM (+22.5% MAP) значимо от базового варианта не отличается**, как и оба SPLIT-EL. Между шестью «морфологическими» вариантами значимых различий нет.
- **Есть анализ по темам** (Table 2, p. 691; Fig. 2, p. 695): отклонение AP каждого варианта от медианы семи вариантов по каждой теме.
  - SPLIT-варианты почти всегда у медианы (21–27 тем «без эффекта»);
  - INFL-orig: 18 тем выше медианы, 33 ниже; INFL-trunc 29/22; STEM 21/26, но положительные отклонения STEM крупнее отрицательных.
  - Вывод авторов: стемминг «менее устойчив» по темам, чем нормализация, при почти равном MAP.
- **Наше замечание к этому выводу:** медиана считается по семи прогонам, четыре из которых — почти одинаковые SPLIT-прогоны. Поэтому медиана по построению почти совпадает с уровнем SPLIT, и «устойчивость» SPLIT отчасти является артефактом метода (§12).
- **Чего нет (измерения gap):**
  - BM25 нет: InQuery (#sum/#syn), параметры ранжирования не сообщаются;
  - плотного/нейросетевого поиска нет;
  - fusion нет ни между лексическими вариантами, ни с чем-либо другим;
  - перекрытия релевантных документов, уникальных находок, oracle union нет;
  - признаков запросов нет, кроме двух качественных наблюдений (темы 165 и 185 — по одному релевантному документу; тема 152 — 997 форм на префикс *barn*).
  - Чистого варианта «лемма без разбиения композитов» нет: нормализация всегда совмещена с разбиением композитов, поэтому эффект лемматизации и эффект разбиения композитов не разделены.
- **Внутренние несоответствия в статье (мелкие):**
  - в разделе 5.3 (p. 692) базовый вариант назван «SINFL-owqt» (опечатка, из контекста — INFL-orig);
  - на p. 688 упоминаются варианты «SPLIT-base, SPLIT-EL-base», которые нигде не определены (по-видимому, старые названия SPLIT-вариантов);
  - ссылка на «Section 4.3.3» (p. 687), хотя нумерованного подраздела 4.3.3 нет;
  - «STEM-stem» и «STEM-stems» чередуются;
  - в аннотации сказано, что усечение, нормализация и стемминг «enhanced retrieval effectiveness», хотя по собственному тесту авторов значимо лучше базового варианта только 3 из 6 вариантов.
- **Для нашего gap:** работа поддерживает фон (raw → stem → lemma+decompounding резко меняет лексический поиск во флективном языке; при равном MAP варианты по-разному ведут себя на отдельных темах). Ядро v0.8 (raw/stem/lemma BM25 × фиксированный D → overlap/unique hits → прирост гибрида → признаки запросов) **не затрагивает**. Предложение: gap не менять.
- **Практическая польза для нас:**
  1. обработка должна быть симметричной (индекс и запрос одним и тем же способом), а итоговый способ группировки вариантов в запросе (аналог #syn) надо фиксировать: по словам авторов, группировка 584 форм в #syn «essential» (p. 693), хотя усечение без #syn в статье не проверялось;
  2. правостороннее усечение/префикс — сильный контроль; в статье усечение **ручное** (эксперт), автоматическое префиксное усечение здесь не проверялось. Для узбекского (агглютинативный, суффиксальный) автоматический префиксный вариант — наша экстраполяция; его стоит держать рядом с raw/stem/lemma;
  3. при семи и более вариантах тест Фридмана с поправкой на множественные сравнения теряет мощность: для основных контрастов (raw vs stem, raw vs lemma) заранее задать попарные тесты;
  4. анализ «отклонение от медианы» не заменяет анализа уникальных находок; для узбекского нужны попарные разности по запросам и множества релевантных документов.

---

## 1. Bibliographic record

- **Authors:** Per Ahlgren, Jaana Kekäläinen
- **Affiliations:** Swedish School of Library and Information Science, University College of Borås, Sweden (Ahlgren); Department of Information Studies, University of Tampere, Finland (Kekäläinen) (p. 681)
- **Year:** 2006
- **Venue:** *Information Retrieval*, Vol. 9, pp. 681–697 (running header, p. 681). Issue 6, December 2006 (bibliographic check: link.springer.com)
- **Publisher:** Springer Science + Business Media (p. 681)
- **DOI:** `10.1007/s10791-006-9009-1` (p. 681)
- **Dates:** received 6 April 2005; accepted 28 June 2006; published online 1 September 2006 (p. 681)
- **Official URL:** https://link.springer.com/article/10.1007/s10791-006-9009-1
- **Source type:** peer-reviewed journal article
- **Basis:** "This study is based on (Ahlgren, 2004)" — Ahlgren's PhD thesis (University College of Borås and Göteborg University); "some methods tested in this study were not tested in the mentioned work" (p. 682)
- **Reliability:** A
- **Full text available:** yes (`07_full_text/pdfs/CR000490.pdf`, 17 pages)

## 2. Why this work matters to the PhD

It is a clean, controlled example of the lexical half of our design: the same collection, queries and ranking system, with only the morphological representation of index and query changed. It adds two things not common in the corpus: **manual truncation** as a strong reference, and a **topic-by-topic** view of how the representations differ.

| Axis | Relation |
|---|---|
| Lexical retrieval | Direct: inflected-form index (raw), Snowball stem index, SWETWOL base-form index with compound splitting, truncation over the raw index. Ranking by InQuery, **not BM25** |
| Semantic retrieval | **Absent** |
| Hybrid retrieval | **Absent**: no fusion of any kind |
| Uzbek morphology | Indirect: Swedish is inflectional and compounding, with vowel-change forms (*stad/städer*, *ligga/låg/legat*; pp. 682–683). Uzbek is agglutinative and suffixing; compounding is less central |
| Low-resource retrieval | Not low-resource: Swedish CLEF with a mature analyzer (SWETWOL) |
| Current gap | Background support for "representation changes lexical behaviour per topic"; no effect on the lexical–dense complementarity core (§16) |

## 3. Research problem

### Simple explanation

A Swedish word appears in many forms (singular, plural, definite, compounds). If the index stores words exactly as written and the query uses one form, documents with other forms are missed. The authors ask which way of handling this works best: cutting words to stems automatically, reducing them to dictionary forms with a morphological analyzer (and splitting compounds), or letting a search expert truncate query words by hand.

### Formal formulation

"The aim of the study is to generate knowledge of the behavior of the seven combinations of indexing strategies with query terms with respect to Swedish texts and retrieval effectiveness" (p. 682). The independent variable is the combination (index representation × query-term processing); the dependent variable is per-topic uninterpolated AP (and MAP, interpolated precision at 11 recall levels). Stated expectation: conflation should help, and compound splitting at both index and query phase "would be fruitful" (pp. 684–685).

## 4. Main idea

### Simple explanation

Build four indexes of the same news collection: words as written; stems; base forms with compounds split; base forms with compounds split but fewer spurious splits. Pair each with matching queries built from the same topic description words. Run all seven pairings in the same search engine and compare.

### Concrete example

Topic 164, "Europeiska narkotikadomar" (Appendix 1, p. 694). Word list from the description field: *europa för ges narkotikahandel olaglig påföljder*. Queries (verbatim, p. 694):

- INFL-orig: `#sum(europa för ges narkotikahandel olaglig påföljder)`
- SPLIT-split-int / SPLIT-EL-split-int: `#sum(@europa för ge #syn(handel narkotika narkotikahandel) olaglig påföljd)`
- SPLIT-split-aut: `#sum(@europa #syn(för föra) ge #syn(narkotikum hane del han handel narkotika narkotikahandel) olaglig påföljd)`. The automatic query keeps spurious compound readings (*hane*, *del*, *han*).
- SPLIT-EL-split-el-aut: `#sum(@europa #syn(för föra) ge #syn(narkotikum handel narkotika narkotikahandel) olaglig påföljd)`
- STEM-stems: `#sum(europ för ges narkotikahandel olag påföljd)`. The compound is not split.
- INFL-trunc: every index string starting with the expert's truncation stem goes into a `#syn`; the query "originally contains 584 words", 529 of them beginning with *europ* omitted from the printout (p. 694).

`@europa` marks a word not recognized by SWETWOL (p. 687).

### Formal method

- Query form for all combinations: `#sum(Q1, …, Qn)`. InQuery's `#sum` means "the more of its arguments that are satisfied by the document, the better" (p. 688).
- `#syn(...)` treats its arguments "as different expressions for the same concept, i.e., as synonyms" (p. 688). It is used for truncation expansions, compound + components, and ambiguous base forms.
- Compound Elimination Principle (Karlsson, 1992; quoted p. 686): "If a cohort C contains readings with n and m compound boundaries, discard all readings with m compound boundaries if m > n."

## 5. Architecture / algorithm

1. **Collection and topics** (p. 687): Swedish CLEF 2003; 142,819 news articles (352 MB), Tidningarnas Telegrambyrå 1994/1995; topics 141–200; six topics without known relevant documents excluded, so n = 54; 1,006 known relevant documents (mean 18.6 per topic **[computed]**).
2. **Query source** (p. 688): a word list per topic from the **description field** only, with a Swedish stop list applied. Size and content of the stop list: NOT_REPORTED. Our observation: the example word list keeps *för* ("for"), p. 694.
3. **Indexes** (pp. 685–687):
   - **INFL**: inflected word-form index (raw).
   - **SPLIT**: SWETWOL normalization to base forms; compounds split, components normalized (glue *-s* removed by a tuned SWETWOL), and compound + components indexed at the same address. All readings of ambiguous words are indexed (e.g., *marinbiologer* → *bio biolog loge marin marinbiolog marinbiologe*, p. 686).
   - **SPLIT-EL**: as SPLIT, with the Compound Elimination Principle (→ *biolog marin marinbiolog*, p. 687).
   - **STEM**: Snowball stemmer for Swedish (Porter, 2001), p. 687. No compound splitting is described for STEM.
   - Words not recognized by SWETWOL are indexed with an `@` prefix (p. 687).
4. **Query processing per combination** (pp. 688–690):
   - INFL-orig: words as is.
   - INFL-trunc: one search expert right-truncated the words "he found appropriate" (p. 688). InQuery does not support truncation, so it was **simulated**: a Unix script collected every index string with the truncation stem as prefix into `#syn`.
   - SPLIT-*-int: the authors selected "the contextually right reading" by hand (p. 689); compound + components in `#syn`.
   - SPLIT-split-aut: all base forms of all readings in `#syn`, plus compound components.
   - SPLIT-EL-split-el-aut: as aut, after applying the Compound Elimination Principle.
   - STEM-stems: each word stemmed, flat `#sum`.
5. **Ranking system:** InQuery 3.1, inference network model (p. 687). Term weighting parameters: NOT_REPORTED.
6. **Evaluation depth:** m = 1000 (p. 690).

## 6. Data

- **Dataset/corpus:** Swedish CLEF 2003 test collection (p. 687)
- **Language(s):** Swedish
- **Domain:** news (TT news agency, 1994/1995)
- **Size:** 142,819 documents, 352 MB
- **Queries:** 54 topics (141–200 minus six without known relevant documents); description field only
- **Relevance judgments:** CLEF "known relevant documents", 1,006 in total. Binary/graded nature and pooling procedure: NOT_REPORTED in the paper. Context (not from the paper): CLEF qrels are pooled from participants' runs, so strongly expanded new runs (e.g., INFL-trunc with hundreds of terms) may retrieve unjudged documents; the paper does not discuss this.
- **Train/dev/test:** not applicable (no learned components). The truncation expert and the "intellectual" query builders saw the topics; whether they saw relevance information: NOT_REPORTED.

## 7. Baselines

| Baseline / condition | What it is | Why selected | Fair comparison? |
|---|---|---|---|
| INFL-orig | Raw inflected-form index, original query words | "no attempt was made to counteract the problem of morphological variation of query terms in the document database" (p. 690) | Yes, as the raw reference |
| INFL-trunc | Raw index + expert right truncation, expanded via `#syn` | Tests query-side handling by a human | **Partly.** A human decides which words to truncate ("the words he found appropriate", p. 688; in topic 164 *för* and *ges* are left untruncated, p. 694) and where; it is the only condition with very large `#syn` expansions (584 terms in topic 164). Not an automatic method. (Human judgment also enters SPLIT-*-int, where the authors select the contextually right reading, p. 689) |
| SPLIT (4 variants) | SWETWOL base forms + compound splitting in index and query; manual vs automatic reading selection; with/without EL | Grammatical normalization | **Confounded:** normalization and decompounding are always together; the effect of lemmatization alone is not measurable. Query structure also differs (`#syn` grouping) from STEM (flat `#sum`) |
| STEM-stems | Snowball Swedish stemmer on index and query | Non-grammatical conflation | Yes for automatic stemming; but no compound splitting, so SPLIT vs STEM mixes "grammatical vs algorithmic" with "decompounding vs none" |

## 8. Metrics

| Metric | Definition (paper, p. 690) | Simple meaning | Appropriate? |
|---|---|---|---|
| AP (uninterpolated) | Sum of precision values after each known relevant document in the top m = 1000, divided by the number of known relevant documents | How early and how completely the relevant documents appear for one topic | Yes, standard for ad hoc |
| MAP | Mean AP over 54 topics | Overall effectiveness | Yes |
| Interpolated precision at 11 recall levels (Fig. 1) | Standard 0.0–1.0 recall curve | Precision at each recall level | Yes, descriptive |
| Deviation from median AP (Table 2, Fig. 2) | AP of a combination minus the median AP of the seven combinations for the same topic (p. 695) | Does this method do better or worse than "typical" on this topic? | Descriptive only. The threshold for "no effect" is NOT_REPORTED (presumably exact equality) |
| Friedman rank sums (Table 3) | Sum over topics of within-topic ranks of AP (1–7) | Which method tends to rank higher per topic | Yes, non-parametric; chosen because AP distributions were non-normal (p. 692) |

No Recall@k, P@k or nDCG.

## 9. Results

### Table 1: MAP (p. 690, checked on page image)

| Combination | MAP | Paper's % vs INFL-orig | Recomputed **[computed]** | Absolute gain **[computed]** |
|---|---:|---:|---:|---:|
| INFL-trunc | **0.3621** | +32.1% | +32.06% ✓ | +0.0879 |
| STEM-stems | 0.3359 | +22.5% | +22.50% ✓ | +0.0617 |
| SPLIT-split-int | 0.3315 | +20.9% | +20.90% ✓ | +0.0573 |
| SPLIT-EL-split-el-aut | 0.3304 | +20.5% | +20.50% ✓ | +0.0562 |
| SPLIT-EL-split-int | 0.3302 | +20.4% | +20.42% ✓ | +0.0560 |
| SPLIT-split-aut | 0.3265 | +19.1% | +19.07% ✓ | +0.0523 |
| INFL-orig | 0.2742 | — | — | — |

Checks of the authors' derived claims **[computed]**:
- SPLIT-split-int vs SPLIT-split-aut: 0.0050, "less than 1% unit" (p. 690) ✓.
- SPLIT vs STEM: 0.0044–0.0094, "about 0.4 percentage units to 1 percentage unit" (p. 693) ✓.
- INFL-trunc vs STEM: +0.0262 (+7.8% relative); INFL-trunc vs best SPLIT: +0.0306 (+9.2%). This is the size of "not far below truncation" (abstract).

### Figure 1: interpolated precision at 11 recall levels (p. 691, checked on page image)

- Authors: INFL-trunc highest at 10 of 11 levels; at 0.0 STEM "performs slightly better"; SPLIT-split-aut is "a few % units" below the other SPLIT runs and STEM at 0.0–0.3; INFL-orig is below every other curve (p. 691).
- On the page image the INFL-orig curve is visibly lowest at all levels; the other six curves are close together. We do not report read-off values because the markers overlap.

### Table 2: topics above / below / at the median AP (p. 691, checked on page image)

| Combination | # Positive | # Negative | # No effect | Row sum **[computed]** |
|---|---:|---:|---:|---:|
| INFL-orig | 18 | 33 | 3 | 54 |
| INFL-trunc | 29 | 22 | 3 | 54 |
| STEM-stems | 21 | 26 | 7 | 54 |
| SPLIT-split-int | 16 | 14 | 24 | 54 |
| SPLIT-EL-split-int | 18 | 15 | 21 | 54 |
| SPLIT-split-aut | 16 | 12 | 26 | 54 |
| SPLIT-EL-split-el-aut | 14 | 13 | 27 | 54 |

- Every row sums to 54 ✓. Column sums: positive 132, negative 135, no effect 111 **[computed]**. "No effect" ≥ 54 is required because one run is always the median; 111 means many ties at the median (e.g., SPLIT-split-int and SPLIT-EL-split-int share the same query in the Appendix example, p. 694).
- The **unprocessed baseline is above the median on 18 of 54 topics** (33%) **[computed]**, despite having the lowest MAP.

### Figure 2: per-topic deviation from median AP (p. 695, checked at 220 dpi)

**[approximate, read from figure]**, x-axis = topic index 1–54 (not CLEF numbers):
- INFL-orig: large negative bars down to about −0.85 (near index 42) and about −0.8 (near index 23–24); positive bars up to about +0.5 (near index 45–47).
- INFL-trunc: largest negatives about −0.8 (near index 41) and about −0.5 (near index 23). This is consistent with the text's two strongly negative topics, CLEF 165 and 185, each with one known relevant document ranked low (p. 691). The exact index-to-CLEF mapping cannot be reconstructed because the six excluded topics are not named.
- INFL-trunc positives up to about +0.7 (near index 47) and about +0.5 (near index 45).
- STEM-stems: positives up to about +0.7 (near index 47) and +0.5 (near 45); negatives mostly within −0.35.
- All four SPLIT panels: bars mostly within ±0.1, largest about +0.2 (near index 46–48).

### Table 3 and Sec. 5.3: significance (p. 692, checked on page image)

| Combination | Rank sum | Mean rank **[computed]** |
|---|---:|---:|
| INFL-trunc | 258.5 | 4.79 |
| SPLIT-split-aut | 230.5 | 4.27 |
| SPLIT-split-int | 225.5 | 4.18 |
| SPLIT-EL-split-el-aut | 218.5 | 4.05 |
| SPLIT-EL-split-int | 218.0 | 4.04 |
| STEM-stems | 203.0 | 3.76 |
| INFL-orig | 158.0 | 2.93 |

- Friedman: "Fr = 24.73, df = 7 − 1, n = 54, p < 0.001" (p. 692). χ²(6) tail probability for 24.73 = 0.00038 **[computed]** ✓.
- Rank sums total 1,512 = n·k(k+1)/2 = 54·28 ✓ **[computed]**.
- Fr recomputed from the Table 3 rank sums without a tie correction = 22.42 **[computed]**. The reported 24.73 is higher. That is consistent with a correction for tied AP values (half ranks in Table 3 show ties exist), but the paper does not say whether a tie correction was used.
- Multiple comparisons (Siegel & Castellan rank-sum difference vs a critical z, α = 0.05; p. 692):
  - INFL-orig significantly worse than INFL-trunc (difference 100.5), SPLIT-split-aut (72.5) and SPLIT-split-int (67.5) **[computed differences]**;
  - not significantly worse than SPLIT-EL-split-el-aut (60.5), SPLIT-EL-split-int (60.0), STEM-stems (45.0);
  - no significant difference between any two of the six non-baseline combinations.
  - The reported pattern implies a critical rank-sum difference between 60.5 and 67.5. The critical z is NOT_REPORTED. **[computed]** with z at α/[k(k−1)] = 0.05/42 (z = 3.04), the critical difference is 68.2, which would make SPLIT-split-int (67.5) non-significant. With α/[k(k−1)/2] = 0.05/21 (z = 2.82) it is 63.4, which reproduces the paper's pattern exactly. The significance of SPLIT-split-int vs INFL-orig is therefore **borderline** and depends on a choice the paper does not state.
- The authors themselves note: "STEM-stem, which has the next best MAP value, has the next lowest rank sum" (p. 692).

## 10. Statistical evidence

- **Significance test:** Friedman test over 7 combinations × 54 topics, then all-pairs rank-sum multiple comparisons at α = 0.05 (p. 692). The choice is justified by evidence against normality (p. 692). Critical z, correction details and tie handling: NOT_REPORTED (§9).
- **Pairwise tests for specific contrasts** (e.g., STEM vs INFL-orig alone, or SPLIT vs STEM): NOT_REPORTED beyond the all-pairs procedure.
- **Confidence intervals:** NOT_REPORTED.
- **Runs/seeds:** not applicable (deterministic system); one expert for truncation; the "intellectual" queries were built by the authors. Inter-person variation: NOT_REPORTED.
- **Ablation:** partial, by design: with/without Compound Elimination Principle, manual vs automatic reading selection. There is no "normalization without decompounding" condition and no "stemming with decompounding" condition.
- **Per-query analysis:** yes, descriptive. Deviation from the median AP per topic (Table 2, Fig. 2), plus two named topics (165, 185) and one expansion example (topic 152: truncation stem *barn* with 997 index entries, p. 693). There is:
  - no pairwise win/loss table between specific combinations (e.g., STEM vs SPLIT per topic);
  - no overlap of retrieved or relevant documents between representations;
  - no count of relevant documents found only by one representation;
  - no oracle union or per-topic best-representation upper bound;
  - no query features (length, compound count, unrecognized words) linked to the deviations.

## 11. Strengths

- Tight control: same collection, topics, word lists, ranking engine; only the index/query representation changes.
- Symmetric processing of index and query in every automatic condition.
- Includes a **raw** baseline, a **stemmer**, an **analyzer-based lemmatizer**, and **human truncation** as a strong reference.
- Separates effects of spurious compound readings (EL) and of manual vs automatic reading selection; the result that automatic ≈ manual is practically useful.
- Uses a non-parametric test suited to AP distributions and reports the test statistic.
- Goes beyond MAP with a per-topic view and states that stemming and normalization differ in stability despite similar MAP.
- The appendix gives full example queries for every condition, which makes the method reproducible in principle.

## 12. Limitations

### Stated by the authors

- "Although the test was executed in a Swedish collection only, the results may be indicative to indexing and retrieval methods of Internet" (p. 693): single language, single collection.
- Truncation "is bound to expand queries intensively"; its success depends on grouping into synonym sets: "the query structure restrains the retrieval of irrelevant documents" (p. 693).
- SWETWOL's compound mechanism can produce spurious readings that may harm precision (pp. 686–687).

### Inferred from the experimental design

1. **Normalization is confounded with decompounding.** All four SPLIT conditions split compounds; STEM does not. The ranking "SPLIT ≈ STEM" therefore compares *lemma + decompounding* with *stem without decompounding*; the separate contribution of lemmatization is unknown.
2. **Query structure differs between conditions.** SPLIT and INFL-trunc use `#syn` groups; STEM and INFL-orig use flat `#sum`. Part of the differences may come from query structure rather than from the representation itself.
3. **The best condition is manual.** INFL-trunc relies on one expert's decisions and on a simulated truncation with very large expansions. It is an upper-reference for query-side handling, not an automatic method.
4. **The median-based per-topic analysis is structurally biased toward SPLIT.** The median is taken over seven runs, four of which are near-identical SPLIT runs. The per-topic median is therefore usually a SPLIT value, so SPLIT runs will almost automatically show small deviations and many "no effect" topics. The conclusion that normalization is "steadier" than stemming (pp. 693–694) is partly an artefact of the reference point. A pairwise STEM–SPLIT per-topic comparison would be needed.
5. **Rank-based all-pairs testing and key contrasts.** With 7 conditions and an all-pairs correction, STEM's +0.0617 MAP (+22.5%) is not significant against the raw baseline. This is not a borderline power issue: the Friedman procedure uses within-topic ranks, not AP magnitudes, and STEM's rank-sum difference from INFL-orig (45.0) is the smallest of all six, well below either candidate critical value (63.4 / 68.2) **[computed]**; the authors themselves note STEM's low rank sum (p. 692). The significance of SPLIT-split-int against the baseline is borderline (§9). The paper does not report targeted pairwise tests on AP.
6. **Ranking model and parameters not reported.** InQuery weighting is not described; no BM25. Stop-word handling on the index side is not reported; the query stop list apparently keeps *för* (p. 694).
7. **Pooling bias not discussed.** CLEF 2003 qrels come from other systems' runs (context, not from the paper); runs with very different term sets may retrieve unjudged relevant documents.
8. **Unrecognized words** (`@` prefix) are handled differently from recognized ones, but their frequency and effect are NOT_REPORTED.
9. Description-field queries only; query length statistics NOT_REPORTED.

## 13. What the work proves

- On Swedish CLEF 2003 with InQuery, an **inflected-form index queried with original words is the weakest option**: every morphological strategy has higher MAP (+19.1% to +32.1%, Table 1), and INFL-orig has the lowest precision at all 11 recall levels (Fig. 1) and the lowest rank sum (Table 3).
- The raw baseline is **significantly** worse than expert truncation and than SWETWOL normalization + decompounding without EL, by the authors' Friedman multiple comparisons (p. 692). The SPLIT-split-int result is borderline (§9).
- Among automatic strategies, **Snowball stemming and SWETWOL normalization with compound splitting reach nearly the same MAP** (0.3359 vs 0.3265–0.3315); no significant difference among them (p. 692).
- **Manual vs automatic** selection of SWETWOL readings makes little difference in MAP (0.3315 vs 0.3265; 0.3302 vs 0.3304), and removing spurious compound readings (EL) does not change MAP materially (Table 1).
- **Aggregate equivalence hides topic-level differences**: the raw baseline is above the median on 18 of 54 topics, and stemming shows larger topic-level swings (both directions) than the SPLIT runs (Table 2, Fig. 2).

## 14. What the work does NOT prove

- **That stemming improves significantly over raw indexing** in this setting: the authors' own test finds no significant difference between STEM-stems and INFL-orig (p. 692), even though the abstract says stemming "enhanced retrieval effectiveness".
- **That lemmatization alone helps**, or that lemmatization and stemming are equivalent in general: lemmatization is always combined with decompounding; stemming never is.
- **That normalization is intrinsically more stable per topic than stemming**: the median reference is dominated by SPLIT runs (§12, item 4).
- **Anything about BM25, dense retrieval or hybrid fusion**: none are tested.
- **That different representations retrieve different relevant documents**: no set-level overlap, unique-hit or oracle-union analysis. The per-topic AP deviations show that *effectiveness* varies by topic, not which documents each representation contributes.
- **Why some topics favour one representation**: only two topics are explained (single relevant document), and no query features are measured.
- **Generalization** to other languages, to automatic truncation or to non-news domains.

## 15. Relationship to current Uzbek evidence

- **No Uzbek data.** Swedish is inflectional with compounding and vowel-change forms; Uzbek is agglutinative and suffixing, and its Latin orthography adds apostrophe-letter variation (o‘, g‘). Context (not from the paper): since Uzbek suffixes attach to a mostly stable root, right truncation/prefix methods are expected to work comparatively well, unlike Swedish *stad/städer* or *ligga/låg* (pp. 682–683).
- Fits the older lexical-morphology line already in `MASTER_INDEX` C: Can et al. 2008 (MORPH-001; prefix stems competitive in Turkish) and Haddad & Bechikh Ali 2014 (MORPH-002; 4/5-prefix truncation competitive with Zemberek under BM25). Here expert truncation is best. Together they support keeping a **prefix/truncation control** for Uzbek.
- Same CLEF 2003 Swedish collection and InQuery setting as Airio 2006 (`CR000491`, card in this batch), which also compares inflected, Snowball, TWOL lemma with and without decompounding. Cross-card note (not evidence about this paper): Airio reports a Swedish inflected-index MAP of 30.2 vs 0.2742 here, so query construction and topic sets differ and the numbers are not directly comparable.
- Kettunen et al. 2005 (`CR000452`, Finnish) is cited in this paper as finding normalization significantly better than Snowball stemming (p. 693). The authors contrast it with their own Swedish result of stem ≈ normalization. This language-dependence of the stem–lemma ordering is directly relevant to not presupposing `lemma > stem > raw` for Uzbek.
- Uzbek analyzers (Bakaev, Xusainova, Elov; `MASTER_INDEX` C) would face the same problems as SWETWOL: ambiguous readings and unrecognized words. The paper's automatic "all readings in `#syn`" approach is a concrete, reproducible option for them.

## 16. Relationship to CURRENT_GAP

**Classification:** *supports (background)* + *no material effect on the residual core*.

- **Supports (background):** in a morphologically rich language, changing the lexical representation (raw → stem → lemma + decompounding, or truncation) changes lexical effectiveness substantially, and similar MAP can hide different per-topic behaviour. This supports the premise of v0.8 that the representation change could alter *which* queries the lexical channel handles well.
- **Already occupied, confirmed:** "raw/stem/lemma have not been compared" is already a rejected claim in v0.8; this paper is a further, older example (Swedish, not low-resource).
- **No material effect on the core:** the paper has no BM25, no dense retriever D, no fusion, no relevant-document overlap, unique hits or oracle union, and no query-feature analysis. The residual chain `morphological representation → lexical relevant-set change → overlap/unique hits vs the same fixed D → incremental hybrid gain → query features` is untouched.
- **On the triage flag `carries_complementarity_evidence = YES`:** proposal to recode as *partial / lexical-vs-lexical per-topic effectiveness variation only*. The evidence is AP deviation from the median, not complementarity of retrieved relevant sets.

**Proposal:** keep v0.8 refined unchanged. Optionally cite as classic evidence that morphological representation effects are topic-dependent in lexical IR. This is a proposal only; `CURRENT_GAP.md` has not been edited.

## 17. Implications for our research design

- **Lexical variants.**
  - Keep `BM25_raw`, `BM25_stem`, `BM25_lemma` as planned. Add an **automatic prefix/truncation** control (e.g., fixed-length prefix), because truncation was the strongest method here and prefix methods were competitive in Turkish (MORPH-001/002). Note: the truncation tested in this paper is manual (expert-chosen words and cut points); an automatic fixed-length prefix is our extrapolation, not tested here.
  - Process index and query identically for each variant; document where stop-words are removed.
  - Decide explicitly how **ambiguous lemmas** are handled (first reading, all readings, disambiguated). Here "all readings grouped" (aut) ≈ manual disambiguation in MAP; this suggests "all readings" as a defensible automatic default for an Uzbek analyzer. Report the rate of **unrecognized words** per variant.
  - Uzbek compounds are less frequent than in Swedish, but if any decompounding is used, it must not be bundled with lemmatization: otherwise the lemma effect cannot be isolated (limitation 1).
- **Query structure / BM25.** Context (not from the paper): BM25 has no native `#syn`; expanding a query with many surface variants in a flat BM25 query inflates term weights. If a truncation-expansion or "all readings" variant is tested with BM25, use a grouping mechanism (e.g., synonym-style term grouping or BM25F-like pooled statistics) and state it. Otherwise query structure becomes a hidden confound (limitation 2).
- **Per-query analysis.** Do not use "deviation from the median of all runs" as the main per-query tool: it depends on which runs are included. Use pairwise per-query differences (raw vs stem, raw vs lemma, stem vs lemma) and, for the gap, set-level measures: lexical-only relevant hits, D-only relevant hits, intersection, oracle union per variant.
- **Statistics.** Pre-register the primary contrasts and test them pairwise (Wilcoxon or randomization/bootstrap) with a stated correction; report effect sizes and CIs. Here a +22.5% MAP difference (STEM vs raw) is non-significant under the all-pairs, rank-based Friedman procedure, because per-topic ranks ignore the size of STEM's large per-topic gains; a pairwise test on AP differences may or may not agree (not reported).
- **Qrels.** Topics with a single relevant document produce extreme AP swings (topics 165, 185). Report per-query results with the number of relevant documents, and prefer deep multi-system pooling including every lexical variant and D, so that expanded or normalized runs are not penalized for unjudged documents.
- **Hypothesis.** Consistent with our hypothesis that morphology changes per-query behaviour of the lexical channel; gives no evidence about interaction with dense retrieval.

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| Conflation | Grouping different forms of a word so that they match each other | Mapping morphological variants to a common representative (Frakes, 1992; p. 682) |
| Inflected word-form index (raw) | The index stores words exactly as they appear | Index terms = surface tokens |
| Stemming | Cutting words to a common stem with rules, even if the stem is not a real word | Snowball Swedish stemmer (p. 687) |
| Normalization (lemmatization) | Replacing a word with its dictionary form using a morphological analyzer | SWETWOL base forms (p. 685) |
| Compound splitting (decompounding) | Splitting *stålindustri* into *stål* + *industri* and indexing all three | Compound + components indexed at the same address (p. 685) |
| Glue morpheme | A linking letter inside compounds, like *-s-* in *pappersbruk* | Removed before indexing components (pp. 685–686) |
| Cohort / reading | The analyzer's list of possible analyses of one word | Input form + 0..n readings (base form + tags) (p. 685) |
| Compound Elimination Principle | Keep only the analyses with the fewest compound boundaries | Local disambiguation rule (Karlsson, 1992; p. 686) |
| Right-hand truncation | Cutting a query word at some point and matching every word that starts with that prefix | Prefix match, simulated via `#syn` over index strings (p. 688) |
| InQuery `#sum` / `#syn` | `#sum`: more matched parts → higher score; `#syn`: treat terms as one concept | Inference-network query operators (p. 688) |
| MAP / AP | Average precision per topic, averaged over topics | Uninterpolated AP at depth 1000 (p. 690) |
| Friedman test | Ranks all methods within each topic and checks whether some methods systematically rank higher | Non-parametric repeated-measures test (p. 692) |
| Deviation from median AP | How much better or worse a method is than the middle method on each topic | AP − median of seven APs (p. 695) |
| Complementarity (project term) | Each channel finds some relevant documents the other misses | Unique relevant hits, overlap, oracle-union gain |

## 19. Open questions / verification needed

1. **Critical z and tie correction** in the Friedman procedure: which formula gives the reported pattern? The significance of SPLIT-split-int vs INFL-orig is borderline (critical difference 63.4 vs 68.2 depending on the α split, §9); Fr 24.73 vs 22.42 uncorrected.
2. **Naming errors:** "SINFL-owqt" (p. 692) presumably = INFL-orig; "SPLIT-base, SPLIT-EL-base" (p. 688) undefined; "Section 4.3.3" (p. 687) does not exist as a numbered section.
3. **Definition of "no effect"** in Table 2 (exact equality or a threshold): NOT_REPORTED.
4. **Stop-word handling** on the index side, and whether *för* was in the stop list: NOT_REPORTED.
5. **Frequency of words not recognized by SWETWOL** in topics and documents: NOT_REPORTED.
6. **Ahlgren (2004) PhD thesis** (University College of Borås / Göteborg University) is the basis of this study and may contain further per-topic analyses or conditions. Check whether it is in the systematic-review corpus.
7. Would a **pairwise STEM vs SPLIT per-topic comparison** confirm the "stemming is less steady" claim without the median artefact? Not answerable from the paper.

## 20. Decision after deep dive

- **Keep current gap?** Yes. v0.8 refined remains valid (§16).
- **Modify gap?** No. Optionally list this paper among classic evidence that raw/stem/lemma effects in lexical IR are topic-dependent (researcher's decision).
- **Add decision?** Proposed for `decisions/DECISIONS.md` (researcher's decision):
  - "Morphological variants must be applied symmetrically to index and query; ambiguous-reading policy, unrecognized-word handling and query grouping structure are fixed and reported per variant";
  - "Primary lexical contrasts (raw vs stem, raw vs lemma, stem vs lemma) are tested pairwise per query with a stated correction; all-runs median deviation is not used as the main per-query tool".
- **Add experiment?** Add an automatic prefix-truncation lexical control (`BM25_prefix-k`) to the pilot, next to raw/stem/lemma; report its unique relevant hits vs D as well.
- **Add citation to Chapter I?** Yes, §1.1 (lexical IR and morphological conflation: raw vs stemming vs analyzer-based normalization vs truncation; topic-level variability behind similar MAP). Not for §1.2–1.3.
- **Proposed `MASTER_INDEX.md` row** (to add after approval):

| MORPH-031 | Ahlgren & Kekäläinen — *Swedish full text retrieval: Effectiveness of different combinations of indexing strategies with query terms* (Information Retrieval 9(6):681–697) — [deep dive](deep-dives/2006_Ahlgren_Kekalainen_Swedish_Indexing_Strategies_Query_Terms.md) | 2006 | A | HIGH | Swedish CLEF 2003 (142,819 docs, 54 topics), InQuery: raw inflected index vs expert truncation vs Snowball stemming vs SWETWOL normalization + compound splitting (4 variants). MAP 0.2742 raw → 0.3621 truncation, 0.3359 stem, 0.3265–0.3315 SPLIT. Friedman: only truncation and two SPLIT runs significantly beat raw; stem (+22.5%) not significant. Per-topic deviation-from-median analysis: stemming swings more than normalization, raw above median on 18/54 topics (median dominated by SPLIT runs). Lemma always bundled with decompounding. No BM25, dense, fusion or overlap/unique-hit analysis. |
