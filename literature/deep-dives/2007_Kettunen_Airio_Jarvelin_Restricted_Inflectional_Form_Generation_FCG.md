# Kettunen, Airio & Järvelin (2007): Restricted inflectional form generation in management of morphological keyword variation

**Targeted deep-dive status:** COMPLETED (AI-assisted, pending researcher review)
**Completed:** 2026-09-28
**Literature ID:** `MORPH-042` (assigned 2026-09-28, approved by researcher)
**Systematic-review record:** `CR000504`. Full-text triage: INCLUDE, reading priority HIGH, tier "2 — важно", `carries_complementarity_evidence = YES` (see §10 and §16: the evidence is per-query win/loss counts between lexical representations, not set-level overlap).
**Provenance:** AI-assisted deep dive (Claude). The whole paper (30 pp., printed pp. 415–444, including the Appendix) was read from the pdftotext extraction. Page images were checked for every table and figure whose numbers are reported below: PDF pp. 5–8, 10–24, 26–27 = printed pp. 419–422, 424–438, 440–441 (Tables 1–16, A1–A5; Figs. 1–12). Numbers computed by us are marked **[computed]** and were recomputed with Python. Readings of bar heights in the query-by-query figures are approximate and marked as such.
**Source rule:** **the paper is the primary and only authoritative source.** The web was used only to verify the bibliographic record (Crossref). Nothing is concluded about the earlier Finnish study (Kettunen & Airio 2006) beyond what this paper states about it.
**Verification:** independent AI verifier pass 2026-09-28; 8 findings addressed.
**Reliability:** **A** (peer-reviewed journal article, *Information Retrieval*, Springer). Caveats: the FCG queries were built partly by hand ("simulated"), the Russian collection is very small, and several Discussion/Appendix figures do not match the tables (§9, §19).

---

## Кратко для исследователя (RU)

- **Что сделано.** Авторы предлагают FCG (Frequent Case (form) Generation): индекс **не нормализуется** (словоформы как есть), а в запросе каждое существительное и прилагательное заменяется набором из нескольких **самых частотных падежных форм** (по корпусной статистике). Формы объединяются оператором синонимии `#syn` в InQuery/Lemur.
- **Сравнение представлений лексического канала** на коллекциях CLEF для четырёх языков: необработанные словоформы (inflected), стемминг Snowball, лемматизация TWOL (с разбиением композитов в индексе и без него), FCG. Для русского лемматизатора не было — только словоформы / Snowball / FCG. Длинные (title+description) и короткие (title) запросы.
- **Главные числа (MAP):**
  - финский, короткие запросы: FINTWOL 42.8 / Snowball 41.3 / FCG_12 38.1 / словоформы 22.6 (Table 2, p. 420);
  - шведский, короткие: SWETWOL 32.6 / Sv-FCG_4 30.6 / стемминг 28.5 / словоформы 24.0 (Table 9, p. 428);
  - немецкий, короткие: Snowball 30.9 / De-FCG_4 29.9 / GERTWOL 29.6 / словоформы 25.4 (Table 12, p. 431);
  - русский, короткие: Ru-FCG_6 32.0 / Snowball 27.2 / словоформы 25.1 (Table 15, p. 433) — различия **незначимы**, коллекция крошечная (34 темы, 123 релевантных документа).
- **Вывод авторов:** FCG даёт ≈89–97% качества лучшей нормализации [computed по таблицам], значимо лучше необработанных словоформ хотя бы в одной конфигурации для финского, шведского и немецкого; для русского результат неоднозначен.
- **Есть анализ по запросам** (короткие запросы): гистограммы разности AP «лучший FCG − лучшая нормализация» и «лучший FCG − словоформы» с подсчётом побед/поражений/ничьих (Figs. 1–8). Пример: финский, FCG хуже лемматизации в 23 запросах, лучше в 15, ничья в 7 — при разнице средних 4.7 п.п. Это единственное, что относится к «взаимодополняемости»: **разные представления выигрывают на разных запросах**. Перекрытия множеств релевантных документов, уникальных находок, oracle union — **нет**.
- **Чего нет:** BM25 (используются InQuery и Lemur/LM с Dirichlet), плотного поиска, гибрида/fusion, признаков запроса кроме длины (длинные vs короткие).
- **Внутренние несоответствия:** в Discussion (p. 435) разница «словоформы → лучшая нормализация» дана как 20.4 / 4.1 / 5.7 / 6.9 п.п., а по таблицам 20.2 / 8.6 / 5.5 / 2.1 (для русского 6.9 — это разница с лучшим FCG); в Table A2 сумма SG+PL для аккузатива 47 255 ≠ 47 215; в Conclusions «так же хорошо или лучше» стемминга/лемматизации, а в abstract и таблицах — «почти так же хорошо».
- **Для нашего gap:** работа — классическое свидетельство того, что морфологическое представление лексического канала меняет результаты **по-разному для разных запросов** и, для шведского и немецкого, сильнее для коротких запросов (для финского разрыв большой при обеих длинах; для русского выигрыш Snowball над словоформами в коротких запросах меньше: 4.9 → 2.1 п.п.). Ядро v0.8 (raw/stem/lemma BM25 × фиксированная D → перекрытие/уникальные находки → прирост гибрида) **не затрагивает**. Предложение: gap не менять.
- **Практическая польза:**
  1. «Морфологическое представление» задаётся **и индексом, и запросом**: нормализация на стороне запроса (FCG) — отдельная ось; для нашего дизайна её надо явно зафиксировать (обе стороны одинаково) и, возможно, добавить FCG-подобный вариант как дополнительный контроль.
  2. Длина запроса (короткие vs длинные) — обязательный признак в таксономии запросов.
  3. Конфигурация лемматизатора (обработка композитов / неизвестных слов) может менять результат сильнее, чем выбор «stem vs lemma» — нужно документировать.

---

## 1. Bibliographic record

- **Authors:** Kimmo Kettunen, Eija Airio, Kalervo Järvelin
- **Affiliation:** Department of Information Studies, University of Tampere, Finland (p. 415)
- **Year:** 2007
- **Venue:** *Information Retrieval*, vol. 10, issue 4–5, pp. 415–444
- **Dates:** received 5 December 2006; accepted 28 June 2007; published online 10 August 2007 (p. 415); print issue October 2007 (bibliographic check: Crossref)
- **Publisher:** Springer Science+Business Media
- **DOI:** `10.1007/s10791-007-9030-z` (printed on p. 415; confirmed by bibliographic check: Crossref)
- **Funding:** Academy of Finland Grant No. 204978 (p. 440)
- **Source type:** peer-reviewed journal article
- **Reliability:** A
- **Full text available:** yes (`07_full_text/pdfs/CR000504.pdf`, 30 pages)

## 2. Why this work matters to the PhD

It is a controlled comparison of **several morphological representations of the lexical channel** (raw word forms, rule-based stems, lexicon-based lemmas, query-side generation of frequent inflected forms) on standard CLEF collections, for four languages of different morphological complexity, with long vs short queries and **query-by-query** win/loss analysis.

| Axis | Relation |
|---|---|
| Lexical retrieval | Main focus. InQuery (Swedish, German; system for Finnish not restated in this paper) and Lemur with Dirichlet LM (Russian); strongly structured `#sum(#syn …)` queries. **No BM25** |
| Semantic retrieval | Absent |
| Hybrid retrieval | Absent. `#syn` merges variant forms inside one lexical query; it is not fusion of two channels |
| Uzbek morphology | Indirect. Finnish is agglutinative (like Uzbek); Swedish/German/Russian are fusional/Indo-European. The FCG idea rests on skewed case-form frequencies, which is language-general in principle |
| Low-resource retrieval | Motivational: FCG is proposed for "languages poor in morphological resources" (p. 415, p. 439), but all four tested languages have resources |
| Current gap | Background support for the claim that representation choice reshuffles per-query outcomes; no dense, no fusion, no set-level overlap (§16) |

## 3. Research problem

### Simple explanation

In languages where one noun has many forms, a search for the exact word misses documents that use another form. The usual fix is to reduce all forms to one stem or lemma, in the index and in the query. That needs a stemmer or a lemmatizer and re-processing of the whole index. The authors ask whether it is enough to leave the index as it is and add to the query only the few most frequent forms of each noun and adjective.

### Formal formulation

Research questions (pp. 416–417, verbatim numbering):

- **(1)** "Is the FCG approach viable across languages of varying morphological complexity?"
  - (1a) performance of FCG in Swedish, German, Russian and Finnish;
  - (1b) "How many morphological surface forms are needed to achieve reasonable performance?"
  - (1c) "How does this performance compare to doing nothing at all, stemming and lemmatization?"
- **(2)** "What is the effect of topic length on the performance of FCG as compared to doing nothing at all, stemming or lemmatization?"

Evaluation stance (p. 417): comparisons "should be made with respect to the state of the art or gold standard, not with respect to the worst possible result, as now is done many times in IR."

## 4. Main idea

### Simple explanation

Corpus counts show that a few case forms cover most noun occurrences (e.g., Swedish: 4 forms ≈ 81% of noun occurrences, Table A1). So instead of normalizing, generate just those forms for each query noun/adjective and treat them as synonyms of one query term.

### Concrete example

The paper's own Swedish query #142, Sv-FCG_4, short version (p. 422):

`#q142 = #sum(#syn(christo) #syn(paketerar) #syn(det) #syn(tyska tyskt) #syn(riksdagshuset riksdagshus riksdagshusen));`

- The noun *riksdagshuset* ('the Reichstag building') is expanded to three forms, the adjective *tyska* to two;
- the verb *paketerar* and the proper name *christo* stay as in the topic.

### Formal method

For each query term t that is a noun or adjective, replace t with `#syn(g₁(t), …, g_k(t))`, where g₁…g_k generate the k most frequent inflectional forms for the language (from corpus statistics). Other terms stay unchanged. Retrieve over the **un-normalized** (inflected) index. InQuery "treats them as instances of one key" (p. 422).

Context (not from the paper): in InQuery-style structured queries, `#syn` pools the term statistics of its arguments as if they were one term, so the variants share one document-frequency / term-frequency estimate rather than each receiving separate weight.

## 5. Architecture / algorithm

1. **Corpus analysis of form frequencies** (Sec. 2.1, 4; Appendix):
   - Swedish: SWETWOL analysis of Helsingborgs Dagblad + Göteborgs-Posten 1994, 161,336 articles → 633,058 noun interpretations (p. 423; Table A1);
   - German: Tiger corpus (Frankfurter Rundschau 1995–1997, ≈900,000 tokens) → 178,834 common nouns, 48,946 proper nouns, 49,076 attributive positive adjectives (pp. 424–425; Tables A2–A3);
   - Russian: Russian National Corpus, 5 M-word hand-tagged sub-corpus → ≈1.3 M noun forms (p. 426; Tables A4–A5);
   - Finnish: from Kettunen & Airio (2006): six of 14 cases cover 84–88% of noun case-form tokens (p. 417).
2. **FCG procedures** (Tables 4, 5, 7):
   - **Sv-FCG_2:** indefinite + definite singular nominative; **Sv-FCG_4:** + indefinite + definite plural nominative; adjectives in two forms.
   - **De-FCG_2:** nominative and accusative sg/pl + dative sg for common nouns; sg nominative for proper names; 5 adjective forms. **De-FCG_4:** + genitive sg/pl, plural dative; genitive for proper names.
   - **Ru-FCG_3:** nominative, genitive, accusative, singular only; **Ru-FCG_6:** same cases sg + pl; **Ru-FCG_8:** + instrumental sg + pl. Nouns and adjectives in the same forms.
   - **Finnish FCG_9, FCG_12:** 9 and 12 variant forms; the case composition is **NOT_REPORTED in this paper** (refers to Kettunen & Airio 2006).
   - Note: the suffix is not always the number of forms. De-FCG_4 generates on average 2.98 forms per lexeme in short queries (Table 16). The paper does not explain this figure; it is consistent with the German inflectional homography the authors discuss (pp. 424, 430) (our inference).
3. **Form generation** (Sec. 3.1–3.2, pp. 421–422): "rule-based even if manual". Tools: Lexin + online SWETWOL + web/printed dictionaries (Swedish); Canoo.net generator (German); Multitran + the Gelbukh & Sidorov analyzer (Russian). If a Swedish form could not be verified, the word "was left in the query as it originally appeared in the topic".
4. **Baselines:** query generation for lemmatization, stemming and inflected forms "was automatic"; FCG queries "were formed partly manually from the topics" (p. 422).
5. **Normalizers:** FINTWOL, SWETWOL, GERTWOL lemmatizers (Lingsoft); Snowball stemmers for Finnish, German, Russian, Swedish; "Unfortunately there was no Russian lemmatizer available" (p. 421). Words the lemmatizer cannot analyze are marked `@` and put in a separate index of unknown words (footnote 2, p. 421).
6. **Compound handling:** in the "compounds split" condition, compounds are split in the index but not in the queries; the compound is indexed whole and as its parts (Table 8 footnote a, p. 428; applies to Finnish, Swedish, German).
7. **Retrieval systems** (Table 3, Sec. 3, 5.3):
   - Swedish, German: InQuery;
   - Russian: Lemur ("inference network retrieval model with language models", p. 432), Dirichlet smoothing, no pseudo-relevance feedback (p. 433), UTF-8;
   - Finnish: not restated in this paper (results replicated from Kettunen & Airio 2006) — **NOT_REPORTED here**.
   - Retrieval-model parameters (e.g., Dirichlet μ), stop-word handling in retrieval: **NOT_REPORTED**.

## 6. Data

| Language | Collection | Docs | Topics used | Relevance | Query lengths |
|---|---|---:|---|---|---|
| Finnish | CLEF 2003 | NOT_REPORTED here | 45 (Tables 1–2) | binary (p. 418) | short: mean 2.55 words, stop words omitted (p. 419); long: NOT_REPORTED |
| Swedish | CLEF 2003 | 142,819 | 54 of 60 with relevant docs | CLEF | long 15.62, short 3.17 words with stop words (p. 427–428) |
| German | CLEF 2003 | 294,809 | 56 of 60 | CLEF | long 17.25, short 3.15 with stop words (pp. 430–431) |
| Russian | CLEF 2004 | 16,716 (Izvestia 1995) | 34 of 50 | CLEF; **123 relevant documents in total** | long 16.7 (stop words not omitted), short 3.18 with stop words (p. 433) |

Sources: Table 3 (p. 421), text pp. 418–433. Domain: newspaper articles. No train/dev split: the FCG procedures were designed from **external corpus statistics**, not tuned on the test topics; but "After testing, the best FCG process with respect to normalization is usually distinguished" (p. 418), and the "best FCG" per condition is picked on the test topics (§12).

## 7. Baselines

| Baseline | What it is | Fair comparison? |
|---|---|---|
| Inflected (raw) | Topic words as written, un-normalized index | Yes, but the authors deliberately treat it as the weakest reference (p. 417) |
| Snowball stemmer | Rule-based affix removal, no large lexicon | Yes; automatic |
| TWOL lemmatizer, compounds split in index | Lexicon-based lemmatization + decompounding in the index | Yes; the "gold standard" of the paper. It combines two operations (lemmatization + decompounding), so it is not a pure "lemma" condition |
| TWOL lemmatizer, compounds not split | Lemmatization only | Yes; often **worse than Snowball** and sometimes worse than inflected (Tables 8, 11) |
| FCG (2–12 forms) | Query-side generation over inflected index | **Asymmetric construction:** FCG queries partly manual, baselines automatic (p. 422); "best FCG" chosen post hoc per language and query length |

No Russian lemmatizer, so the Russian comparison is inflected / Snowball / FCG only.

## 8. Metrics

| Metric | Definition | Simple meaning | Appropriate? |
|---|---|---|---|
| Mean average precision (MAP), reported as % | Mean over topics of average precision | Overall ranking quality, rewards finding all relevant documents high | Yes, standard for CLEF ad hoc |
| P–R curves, 11 recall levels (Figs. 9–12) | Interpolated precision at recall 0.0…1.0 | Where along the ranking one method wins | Descriptive |
| Relevant documents returned in top-1000 (Russian only, Tables 14–15) | Count of relevant docs retrieved, out of 123, pooled over topics | Recall at depth 1000, summed over topics | Useful coverage view; pooled counts over 34 topics are dominated by topics with many relevant docs |
| Per-query ΔAP histograms (Figs. 1–8) | AP(best FCG) − AP(baseline) per topic | Win/loss per query | Yes; the only per-query evidence |

## 9. Results

### Finnish CLEF 2003 (Tables 1–2, pp. 419–420; checked on page images)

| Method | Long (45 t+d) MAP | Short (45 title) MAP |
|---|---:|---:|
| FINTWOL, compounds split | **50.8** | **42.8** |
| Stemmed (Snowball) | 49.8 | 41.3 |
| FINTWOL, compounds not split | 48.2 | 40.5 |
| FCG_9 | 46.1 | 37.9 |
| FCG_12 | 45.8 | 38.1 |
| Inflected | 31.1 | 22.6 |

- Long-query results are recomputed from the earlier study for the 45 analysed queries (footnote 1, p. 419).
- Best FCG / FINTWOL-split: 90.7% (long), 89.0% (short) **[computed]**. Text: "about 88% of the maximal retrieval result is achieved with both nine and twelve" forms (p. 419); the 88% matches FCG_9 short (88.6%) **[computed]**.
- "difference between best FCG methods and best achieved results … about 5 absolute per cent" (p. 419): 4.7 in both **[computed ✓]**.
- "the marginal cost of doing nothing … is 15–20 absolute per cent" (p. 419): long 14.7–19.7 (FCG_12 45.8 − 31.1 = 14.7), short 15.3–20.2 **[computed; ≈15–20 ✓]**.
- Best FCG recovers ≈76–77% of the inflected→FINTWOL gap **[computed]**.

### Swedish CLEF 2003 (Tables 8–9, p. 428)

| Method | Long (54) MAP | Short (54) MAP |
|---|---:|---:|
| SWETWOL, compounds split | **38.8** | **32.6** |
| Sv-FCG_4 | 35.2 | 30.6 |
| Sv-FCG_2 | 33.7 | 29.1 |
| Stemmed | 33.5 | 28.5 |
| Inflected | 32.1 | 24.0 |
| SWETWOL, compounds not split | 31.4 | 26.3 |

- Both Sv-FCGs are **above Snowball** in both query sets; SWETWOL without decompounding is below inflected in long queries.
- Sv-FCG_4 / SWETWOL-split: 90.7% long, 93.9% short **[computed]**.

### German CLEF 2003 (Tables 11–12, pp. 430–431)

| Method | Long (56) MAP | Short (56) MAP |
|---|---:|---:|
| GERTWOL, compounds split | **39.7** | 29.6 |
| Stemmed | 39.1 | **30.9** |
| De-FCG_4 | 38.0 | 29.9 |
| De-FCG_2 | 36.8 | 29.0 |
| Inflected | 35.9 | 25.4 |
| GERTWOL, compounds not split | 35.1 | 28.1 |

- Table 11 prints "De-FCG_2 36.8% (−1.9)", but 39.7 − 36.8 = 2.9 **[computed]**: the bracket is inconsistent with the table's own values (the other brackets match).
- Short: De-FCG_4 slightly above GERTWOL-split (+0.3), below Snowball (−1.0).
- Best FCG / best normalization: 95.7% long, 96.8% short **[computed]**.

### Russian CLEF 2004 (Tables 14–15, p. 433)

| Method | Long MAP | Rel. in top-1000 (of 123) | Short MAP | Rel. in top-1000 |
|---|---:|---:|---:|---:|
| Snowball | **34.7** | 90 | 27.2 | 81 |
| Ru-FCG_3 | 32.7 | 76 | 31.2 | 78 |
| Ru-FCG_6 | 29.2 | 88 | **32.0** | 84 |
| Ru-FCG_8 | 28.9 | **95** | 31.7 | **86** |
| Inflected | 29.8 | 78 | 25.1 | 67 |

- Long queries: Snowball best on MAP; Ru-FCG_3 second; inflected is third, above Ru-FCG_6/8.
- Short queries: all FCGs above Snowball on MAP.
- Recall at 1000 rises with more forms in both sets (76→88→95; 78→84→86). "Ru-FCG_8 … is able to find 19 more documents in top-1000" than Ru-FCG_3 (p. 433) **[computed ✓]**.
- Pooled recall@1000 **[computed]**: long Snowball 0.732, Ru-FCG_8 0.772, inflected 0.634; short Ru-FCG_8 0.699, Snowball 0.659, inflected 0.545.
- **No difference is statistically significant** (Friedman, p. 433).

### Per-query results, short (title) queries (Figs. 1–8; text pp. 419, 428, 431, 433)

| Language | Comparison | FCG better | FCG worse | Ties | Total | Sign test p (two-sided, ties dropped) **[computed]** |
|---|---|---:|---:|---:|---:|---:|
| Finnish | best FCG vs best lemmatization (Fig. 1) | 15 | 23 | 7 | 45 ✓ | 0.26 |
| Finnish | best FCG vs inflected (Fig. 2) | 32 | 12 | 1 | 45 ✓ | 0.004 |
| Swedish | best FCG vs best lemmatization (Fig. 3) | 23 | 21 | 10 | 54 ✓ | 0.88 |
| Swedish | best FCG vs inflected (Fig. 4) | 33 | 13 | 8 | 54 ✓ | 0.004 |
| German | best FCG vs best stemming (Fig. 5) | 18 | 30 | 8 | 56 ✓ | 0.11 |
| German | best FCG vs inflected (Fig. 6) | 36 | 13 | 7 | 56 ✓ | 0.001 |
| Russian | best FCG vs stemming (Fig. 7) | 14 | 12 | 8 | 34 ✓ | 0.85 |
| Russian | best FCG vs inflected (Fig. 8) | 15 | 9 | 10 | 34 ✓ | 0.31 |

- Totals equal the numbers of topics **[computed ✓]**. The sign-test p-values are our own illustration, not the authors' test.
- Size of per-query swings (approximate bar readings from the page images): Finnish FCG vs TWOL from about −1.0 to +0.7 AP (Fig. 1); Swedish about −0.38 to +0.21 (Fig. 3); German about −0.17 to +0.32 (Fig. 5); Russian about −0.83 to +1.0 (Fig. 7).
- Reading: against the best normalization, FCG wins on a **large minority or a majority of topics** in every language, even where the mean gap is 2–5 MAP points. The representations differ **per query in both directions**, with single-topic swings much larger than the mean difference.

### P–R curves, short queries (Figs. 9–12, pp. 435–437)

- Finnish: clear separation, FINTWOL > best FCG > inflected at most recall levels; curves meet around recall 0.6–0.7 (approximate reading).
- Swedish: best FCG and SWETWOL nearly overlap; inflected is visibly lower at all recall levels (approximate reading).
- German: the three curves are close; inflected lowest at most recall levels (approximate reading).
- Russian: the curves nearly coincide; Snowball highest at low recall, best FCG around recall 0.4–0.5 (approximate reading).

### Query size (Table 16, p. 438)

Mean generated forms per lexeme, short queries: Finnish 12.27 (FCG_12), 9.35 (FCG_9); German 2.98 (De-FCG_4); Russian 5.34 (Ru-FCG_8), 3.80 (Ru-FCG_6); Swedish 3.29 (Sv-FCG_4). For 1–3 keyword queries: German/Swedish "about 3–10", Russian 5–16 (FCG_8) / 4–12 (FCG_6), Finnish 9–36 keyword forms (p. 438) **[computed ✓]**. Finnish runtime (from the earlier study): 12 variants increase mean CPU time by "only about 20%" (p. 438).

### Form statistics (Appendix, pp. 440–441)

- Swedish: indefinite + definite sg nominative = 57.1%; + the two plural nominatives ≈ 81% (p. 423) **[computed: 57.1% ✓, 81.0% ✓]**.
- Russian nouns: 77% singular **[computed: 77.0% ✓]**; nominative + genitive + accusative (sg + pl) "75.7%" (p. 426) vs **76.2% [computed from Table A4]**.

### Internal inconsistencies found

1. **Discussion (p. 435) vs tables.** "the largest difference between non-processing and best normalization method is in Finnish (20.4%) and smallest in Swedish (4.1%). German and Russian … 5.7% and 6.9%". From Tables 2, 9, 12, 15 **[computed]**: Finnish 20.2, Swedish 8.6 (the text on p. 428 itself says 8.6), German 5.5 (text p. 431 says 5.5), Russian 2.1 (Snowball − inflected). The Russian 6.9 equals best FCG − inflected. The Swedish 4.1 equals SWETWOL − Stemmed. So the Discussion's ranking of languages by "need of morphological processing" is not supported by the tables for Swedish and Russian.
2. **Table 11 bracket:** De-FCG_2 "(−1.9)" should be −2.9 given the printed MAPs.
3. **Table A2:** accusative SG 31,899 + PL 15,356 = 47,255, but the printed total is 47,215; SG 123,529 + PL 55,345 = 178,874 vs printed SUM 178,834 **[computed]**. (The printed case totals do sum to 178,834.)
4. **"No two cases together form more than a 60% share"** (p. 425) vs Table A2 nominative + dative = 30.5 + 31.0 = 61.5% **[computed]**.
5. **German adjective shares** 28.6 + 15.2 + 29.4 + 29.6 = 102.8% (p. 425) **[computed]**.
6. **Table A3 percentages:** nominative 61.2% and dative 26.1% printed vs 61.4% and 25.9% computed from the counts.
7. **Russian adjective text** (p. 427): "Only the frequency of instructive and locative forms is slightly different, instructive being more common for adjectives." Table A5 uses "instrumental" and "prepositional"; there, prepositional (13.3% sg) exceeds instrumental (10.2% sg) for adjectives, whereas for nouns instrumental (9.9%) exceeds prepositional (8.9%) in the singular. The sentence cannot be matched to the tables unambiguously.
8. **Strength of the headline claim:** abstract "almost as good as that delivered by stemming or lemmatization" (p. 415) vs Conclusions "just as good as or better than what stemming or lemmatization provide" (p. 439). The tables show FCG above the *best* method of a condition only for German short (above GERTWOL-split but below Snowball, so not the best) and Russian short (not significant); FCG does exceed the Snowball stemmer in Swedish (both lengths) and Russian short, and TWOL-without-decompounding in Swedish and German, but stays below the best normalization in all Finnish, Swedish and German conditions.
9. **"word form generation of 3–9 most frequent cases or forms is sufficient"** (p. 439; abstract: "surface form generators for the 3–9 most frequent forms") while the best Finnish short-query run is FCG_12 (Table 2) and Table 16 gives 12.27 forms/lexeme for it.
10. **Significance notation differs between tables:** Table 10: "≫ p < 0.01; > p < 0.02"; Table 13: "> p < 0.01, ≫ p < 0.001, >* p < 0.02".
11. Discussion "95% for Swedish" (p. 435) vs 93.9% short-query ratio **[computed]** (approximate; Conclusions give 90–93%).
12. Minor: "Broglio et al. 1997" is cited (p. 422) but only Broglio et al. 1994 is in the reference list.

## 10. Statistical evidence

- **Test:** Friedman two-way analysis of variance by ranks, with pairwise comparisons after a significant omnibus test (Conover 1980) (pp. 428–429). Chosen because several methods are compared and parametric assumptions do not hold.
  - The paper calls Friedman "a generalization of the parametric sign test" (p. 429). Context (not from the paper): the sign test is non-parametric; this is a wording slip, not a methodological one.
  - Methods entered: two TWOLs, Snowball, best FCG, inflected (Swedish, German; p. 429).
- **Swedish (Table 10, p. 430):**
  - long: SWETWOL-split > Stemmed "almost significant" (p < 0.05) and ≫ inflected (p < 0.01); inflected > SWETWOL-no-split (p < 0.02); **Sv-FCG_4 not significantly different from anything**;
  - short: SWETWOL-split ≫ inflected, Stemmed ≫ inflected (p < 0.01), Sv-FCG_4 > inflected (p < 0.02).
- **German (Table 13, p. 432):**
  - long: GERTWOL-split ≫ inflected (p < 0.001), >* GERTWOL-no-split (p < 0.02); Stemmed ≫ inflected, > GERTWOL-no-split (p < 0.01); De-FCG_4 vs inflected only "almost significant";
  - short: GERTWOL-split, Stemmed, De-FCG_4 all better than inflected (p < 0.02 / < 0.01 / < 0.02); Stemmed vs GERTWOL-no-split and GERTWOL-no-split vs inflected "almost significant".
  - No significant difference between best FCG and the "gold standards" (p. 434).
- **Finnish (p. 419):** long: FINTWOL-split, Snowball and FCG_9 better than inflected (p < 0.0001); short: FINTWOL-split and Snowball (p < 0.0001), FCG_12 (p < 0.01) better than inflected. **FCG vs FINTWOL/Snowball: NOT_REPORTED.** So the Conclusions' "The best FCG method in these languages was never significantly worse than the best lemmatization or stemming method" (p. 439) is not backed by a reported test for Finnish in this paper.
- **Russian:** no significant differences (p. 433).
- **Multiple-comparison correction, exact p-values, effect sizes, confidence intervals:** NOT_REPORTED.
- **Runs/seeds:** not applicable (deterministic systems); one run per condition.
- **Ablation:** number of generated forms (2/4, 3/6/8, 9/12) acts as a dose-response variable; compound split vs no split for TWOL; long vs short queries. No ablation of the noun/adjective-only restriction.
- **Per-query analysis:** **yes**, for short queries: ΔAP histograms and win/loss/tie counts vs best normalization and vs inflected (Figs. 1–8). **Not present:** set-level overlap of retrieved relevant documents between representations, unique relevant hits, oracle union/best-of per query, and any relation of per-query differences to query features (other than the long/short split at the set level).

## 11. Strengths

- Four languages, two query lengths, and several lexical representations evaluated in one design on standard CLEF collections.
- Gold-standard framing: FCG is compared to the best normalization, not only to raw forms (p. 417).
- Per-query win/loss evidence, which shows direction-mixed differences hidden by means.
- Transparent corpus statistics behind the FCG choices (Appendix A1–A5).
- Non-parametric multi-method testing (Friedman) rather than many t-tests.
- Honest caveat on the Russian collection (p. 435, p. 439).

## 12. Limitations

### Stated by the authors

- Russian collection is small with only 123 relevant documents; results "remain uncertain" and "should be retested in a better collection" (pp. 435, 439).
- FCG was **simulated**: generation "rule-based even if manual" (p. 421); FCG queries "formed partly manually" (p. 422).
- Case forms were generated regardless of semantic noun category; category-specific sets might help (p. 437).
- Real multi-user search times "can not be evaluated here" (p. 439).
- Needs testing with more languages and query environments (p. 439).

### Inferred from the experimental design

1. **Manual vs automatic construction.** Only FCG queries involved human work with dictionaries; errors or choices in that step can favour or penalize FCG, and the procedure is not fully reproducible.
2. **Post-hoc "best FCG" selection** on the test topics per language and query length (e.g., FCG_9 long vs FCG_12 short in Finnish; Ru-FCG_3 long vs Ru-FCG_6 short). With 2–3 variants the optimism is small but non-zero.
3. **The noun/adjective-only claim is not tested.** No condition expands verbs or other POS, so "it only matters to cover nouns and adjectives" (abstract) is an assumption of the design, not a finding.
4. **The "lemma" condition bundles decompounding.** The best TWOL runs split compounds in the index; TWOL without splitting is often below Snowball and even below inflected. The paper therefore compares FCG with *lemmatization + decompounding*, and FCG itself does no decompounding.
5. **Different retrieval engines** (InQuery vs Lemur) across languages and different stop-word practice in reported query lengths (Finnish short without stop words; others with). Cross-language comparison of effect sizes is confounded.
6. **Retrieval-model parameters** (InQuery settings, Dirichlet μ) and stop-word handling in retrieval: NOT_REPORTED.
7. **Per-query evidence is shown only for short queries** and only as AP differences; no document-level overlap.
8. **No correction for multiple comparisons** reported; Finnish FCG-vs-lemmatizer significance not reported.
9. **Low topic counts** (34–56) and binary CLEF judgments; the Russian set has 3.6 relevant docs per topic on average (123/34) **[computed]**.
10. Several text/table mismatches (§9), including the Discussion's cross-language comparison.

## 13. What the work proves

- On CLEF collections for Finnish, Swedish and German, **query-side generation of a few frequent inflected forms over an un-normalized index recovers most of the gain of stemming/lemmatization over raw word forms**: best FCG reaches ≈89–97% of the best normalization's MAP and recovers ≈46–82% of the raw→best-normalization gap **[computed from Tables 1–2, 8–9, 11–12]**.
- **Raw word forms are clearly worst for Finnish** (MAP 22.6 vs 42.8 short, 31.1 vs 50.8 long) and significantly worse than normalization in Finnish, Swedish and German at least for short queries (Friedman; Tables 10, 13; p. 419).
- **Morphological processing matters more for short queries** in Swedish (gap 6.7 → 8.6 points) and German (3.8 → 5.5 vs best; Tables 8–9, 11–12). In Finnish the gap is large in both (19.7 / 20.2).
- **Lemmatization without decompounding can be worse than stemming and even raw forms** (Swedish long 31.4 < 32.1; German long 35.1 < 35.9; Tables 8, 11).
- **Different lexical representations win on different queries:** even against the best normalization (for Russian the only one, Snowball, which is below FCG on MAP in short queries), best FCG wins on 15/45 (Fi), 23/54 (Sv), 18/56 (De), 14/34 (Ru) short queries (Figs. 1, 3, 5, 7), with single-topic AP swings far larger than the mean gap.
- **In Russian, adding more forms raises recall@1000 but not MAP consistently** (long MAP 32.7 → 29.2 → 28.9; short 31.2 → 32.0 → 31.7; Tables 14–15), within a statistically non-significant, tiny collection.

## 14. What the work does NOT prove

- **That FCG is "as good as or better than" stemming/lemmatization in general.** In most conditions it is lower; significance of FCG vs the best method is either not significant or not reported (Finnish).
- **That only nouns and adjectives need to be covered** — never tested.
- **Anything about BM25.** InQuery and Lemur/Dirichlet LM are used; the relative ranking of representations under BM25 is not tested.
- **Anything about dense retrieval, fusion or lexical–semantic complementarity.**
- **Set-level complementarity between representations.** Per-query win/loss counts show that representations differ per topic, but not whether they retrieve *different relevant documents*, how large their union is, or whether combining them helps.
- **Which query properties predict when FCG (or stemming, or lemmatization) wins.** Only the long/short split is analysed.
- **Transfer to an agglutinative language with productive derivation and possessive suffixes** beyond Finnish, or to automatic (non-simulated) generation.
- **The cross-language ranking of "need for morphological processing"** given in the Discussion, because its numbers do not match the tables.

## 15. Relationship to current Uzbek evidence

- **No Uzbek data.** The closest language typologically is Finnish (agglutinative, many cases, possessive suffixes, clitics). Context (not from the paper): Uzbek nouns also stack plural, possessive and case suffixes, so a frequent-form generator for Uzbek would need to decide whether to include possessive combinations; the paper notes that in Finnish clitics and possessives are "almost nonexistent even in a reasonably large textual corpus" (p. 418), which may not hold for Uzbek and would need corpus checking.
- The Finnish result (raw word forms lose ≈20 MAP points against lemmatization) is the strongest classic warning that a "raw" Uzbek lexical channel may be very weak, which would make raw BM25 vs dense complementarity look very different from stem/lemma BM25 vs dense.
- National Uzbek morphology resources (Bakaev, Xusainova, Elov; `MASTER_INDEX` C) include analyzers and lemmatizers but no qrels-based raw/stem/lemma retrieval evaluation. FCG shows a third lexical option that needs only a **form generator + frequency statistics**, not a full analyzer on the index side.
- Same Tampere cluster: CR000452 (Kettunen, Kunttu & Järvelin 2005: plain / Snowball / FINTWOL / inflectional stem generation, TUTK), CR000491 (Airio 2006: normalization + decompounding, CLEF 2003), CR000490 (Ahlgren & Kekäläinen 2006, Swedish). Later use of FCG as one query-side representation next to s-grams in historical Finnish OCR retrieval: CR000342 card (Järvelin & Keskustalo 2016).

## 16. Relationship to CURRENT_GAP

**Classification:** *supports (background)* + *no material effect on the v0.8 core*.

- **Supports:** v0.8 treats morphology as a **variant of the lexical representation**, not a third channel. This paper operates exactly in that frame: raw / stem / lemma / FCG are alternative lexical representations of the same engine. It also shows per-query heterogeneity between representations (wins in both directions, large single-topic swings), which is the precondition for our hypothesis that changing the representation changes *which* relevant documents the lexical channel contributes.
- **Touches (partly) these v0.8 elements:**
  - lexical effectiveness per representation, per query (ΔAP per topic) — yes;
  - query characteristics — only length (long vs short), at the set level;
  - coverage view — only pooled recall@1000 for Russian.
- **Does not touch:**
  - BM25 (none);
  - a fixed dense comparator D (none);
  - unique relevant hits / overlap / oracle union (none, even between lexical representations);
  - incremental hybrid gain (no fusion);
  - morphological/graphic/lexical query features beyond length.
- **Nuance for the gap wording:** v0.8 speaks of "raw → stem → lemma". This paper shows a representation change can be applied on the **query side only**; the gap wording remains valid, but the method section should define each representation by both index-side and query-side processing.

**Proposal:** keep v0.8 refined unchanged. Cite as classic evidence (i) that raw forms can be far worse than normalized forms in an agglutinative language and (ii) that lexical representations differ per query in both directions. This is a proposal only; `CURRENT_GAP.md` has not been edited.

## 17. Implications for our research design

- **Definition of representations.** Specify for each condition what happens on the index side and on the query side (raw index + raw query; stem/stem; lemma/lemma). Optional extra condition: `BM25_FCG` = raw index + query expanded with the most frequent Uzbek case/number/possessive forms. With BM25, the analogue of `#syn` needs care: Context (not from the paper) — plain OR-expansion scores variants as independent terms; a synonym-style pooled treatment (e.g., BM25F-style or Lucene `SynonymQuery` pooling) should be chosen and reported.
- **Morphology preprocessing.** Report lemmatizer settings that can dominate results: compound/derivation handling, treatment of unknown words (here a separate `@` index), and whether ambiguous analyses return several lemmas.
- **Query taxonomy.** Include query length (title-like vs description-like) as a primary feature; the morphology effect differed by length in Swedish, German and Russian. Candidate additional feature: share of query nouns/adjectives whose surface form is not the citation form.
- **Metrics / analysis.** Replicate the per-query ΔAP / ΔnDCG histograms with win/loss/tie counts for raw vs stem vs lemma, then go beyond them: unique relevant hits and overlap per representation vs the same D, oracle union, hybrid gain. Report Recall@1000 (or @k used for fusion candidates) alongside MAP; the Russian result shows recall and MAP can move in opposite directions when variants are added.
- **Statistics.** Friedman + post-hoc is a reasonable multi-condition test for raw/stem/lemma; specify the post-hoc procedure and correction, and report effect sizes and CIs.
- **Protocol hygiene.** Build all query variants automatically (no manual step for one condition only); fix the variant set (e.g., number of generated forms) on dev, not on test topics.
- **Dataset.** Pool deeply enough to judge documents that only one representation retrieves; the paper's coverage evidence rests on a collection with 123 relevant documents.
- **Hypothesis.** No direct evidence for or against. It predicts that in Uzbek raw BM25 will be much weaker than stem/lemma BM25, especially for short queries, so the raw-vs-D complementarity profile will likely differ strongly from the lemma-vs-D profile — which is exactly what we need to measure.

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| Inflected (raw) index/query | Words exactly as written, no normalization | Index terms = surface word forms |
| Stemming (Snowball) | Cut endings by rules to a common stem | Rule-based affix stripping, many-to-one mapping |
| Lemmatization (TWOL) | Replace each word form by its dictionary base form using a large lexicon | Two-level morphological analysis returning lemma(s) |
| Decompounding (compound splitting) | Index a compound also as its parts (*jazzmusik* → *jazz*, *musik*) | Index-side expansion of compound tokens |
| FCG | Add the few most frequent inflected forms of each query noun/adjective | Query-side generative normalization over an un-normalized index |
| `#syn` / `#sum` (InQuery) | Treat listed forms as one word; combine query terms by averaging | Structured-query operators of the inference-network model |
| Lemur / Dirichlet smoothing | A language-model retrieval engine; smoothing blends document and collection word statistics | Query-likelihood with Dirichlet prior |
| MAP | Average ranking quality over all relevant documents and topics | Mean over topics of average precision |
| Friedman test | Non-parametric test comparing several systems over the same topics by ranks | Two-way ANOVA by ranks, with post-hoc pairwise comparisons |
| Title vs title+description queries | Short, web-like queries vs long, detailed ones | CLEF topic fields used to form queries |
| Per-query (query-by-query) analysis | Look at each topic separately, not only the mean | Distribution of ΔAP per topic, win/loss/tie counts |
| Complementarity (project term) | Each channel/representation finds relevant documents the other misses | Unique relevant hits, overlap, oracle-union gain |

## 19. Open questions / verification needed

1. **Discussion vs table figures** (20.4/4.1/5.7/6.9 vs 20.2/8.6/5.5/2.1; p. 435): which comparison did the authors intend? Not decidable from the paper.
2. **Table 11 bracket** for De-FCG_2 (−1.9 vs −2.9) and **Table A2** accusative / SUM arithmetic (40-token discrepancy).
3. **Finnish setup in this paper:** retrieval system, collection size, FCG_9/FCG_12 case composition — only in Kettunen & Airio (2006) (LNAI 4139), which is not in our record set as far as we know; worth adding to the corpus if the Finnish FCG details are needed.
4. **Finnish FCG vs FINTWOL significance:** not reported; the Conclusions' "never significantly worse" claim relies on it.
5. **Retrieval parameters** (InQuery defaults, Dirichlet μ) and stop-word handling: NOT_REPORTED.
6. **Per-query data** behind Figs. 1–8 are not tabulated; exact ΔAP values can only be read approximately from the bars.
7. Do later Tampere papers (e.g., CR000681, flagged in the Airio 2006 card) report document-level overlap between FCG and lemmatized runs? Check before claiming that no such overlap evidence exists for this setting.

## 20. Decision after deep dive

- **Keep current gap?** Yes; v0.8 refined remains valid (§16).
- **Modify gap?** No change proposed. Optional (researcher's decision): in the method section, define each lexical representation by both index-side and query-side processing.
- **Add decision?** Proposed for `decisions/DECISIONS.md` (researcher's decision):
  - "All lexical representation variants are generated automatically with the same pipeline; no manual query construction for any single condition";
  - "Report per-query win/loss/tie counts and ΔnDCG histograms for raw/stem/lemma, in addition to set-level overlap/unique hits".
- **Add experiment?** Optional secondary condition `BM25_FCG` (raw index + generated frequent Uzbek forms, synonym-pooled), once Uzbek form-frequency statistics are available; secondary to the primary raw/stem/lemma × fixed D design.
- **Add citation to Chapter I?** Yes: §1.1/§1.3 (lexical morphology in IR: raw vs stem vs lemma, query-side generation as an alternative, query-length dependence, per-query heterogeneity between representations).
- **Proposed `MASTER_INDEX.md` row** (to add after approval):

| MORPH-042 | Kettunen, Airio, Järvelin — *Restricted inflectional form generation in management of morphological keyword variation* (*Information Retrieval* 10(4–5), 415–444) — [deep dive](deep-dives/2007_Kettunen_Airio_Jarvelin_Restricted_Inflectional_Form_Generation_FCG.md) | 2007 | A | HIGH | CLEF Finnish/Swedish/German 2003 and Russian 2004 (InQuery; Lemur-Dirichlet for Russian): raw forms vs Snowball vs TWOL lemmatization (± index decompounding) vs FCG (query-side generation of 2–12 frequent case forms over a raw index), long and short queries. Best FCG ≈89–97% of best normalization MAP (e.g., Fi short 38.1 vs 42.8, raw 22.6); normalization matters more for short queries; per-query win/loss shows representations win on different topics (Fi FCG vs TWOL 15/23/7). Russian n.s. (123 rel. docs). No BM25, no dense, no fusion, no overlap/unique-hit analysis. Discussion figures (p. 435) and Table A2 arithmetic do not match the tables. |
