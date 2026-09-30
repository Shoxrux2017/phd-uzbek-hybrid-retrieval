# Alemayehu & Willett (2003): The Effectiveness of Stemming for Information Retrieval in Amharic

**Targeted deep-dive status:** COMPLETED (AI-assisted, pending researcher review)
**Completed:** 2026-09-28
**Literature ID:** `MORPH-026` (assigned 2026-09-28, approved by researcher)
**Systematic-review record:** `CR000354`. Full-text triage: INCLUDE, reading priority HIGH, tier "2 — важно", `carries_complementarity_evidence = YES` (see §10 and §16 for how far this holds).
**Provenance:** AI-assisted deep dive (Claude). The whole paper (6 pages, pp. 254–259, a "Short communication") was read in the text extraction. All six pages were rendered at 110 dpi and viewed. The pages checked visually for the numbers reported below are pp. 254 (bibliographic block), 255 (method), 256 (judging and statistics), 257 (Figure 1, Figure 2, Table I, ANOVA/t-tests) and 258 (Sign tests, Query-2 root-vs-stem analysis, Figures 3–4). Every number comes with its location and printed page. Numbers computed by us are marked **[computed]** and were recomputed with Python.
**Source rule:** **the paper is the primary and only authoritative source.** The web was used only for a bibliographic check (Emerald record and White Rose eprint listing found through web search; a direct Crossref lookup was refused by the proxy, so the DOI was matched against the search result and the DOI printed on p. 254). Background knowledge appears only as clearly labelled "Context (not from the paper)".
**Verification:** independent AI verifier pass 2026-09-28; 8 findings addressed.
**Reliability:** **B.** Peer-reviewed journal article (*Program: electronic library and information systems*, Emerald/MCB UP), but a 6-page **short communication**. The evidence is narrow: one small collection (548 title+abstract surrogates, 40 queries), relative recall on a top-20 pool only, the retrieval weighting function inside OKAPI is not named, and "full details" are deferred to the first author's PhD thesis (Alemayehu, 1999; p. 256).

---

## Кратко для исследователя (RU)

- **Что сделано.** Для амхарского языка (семитский, корне-шаблонная морфология) сравнены три варианта лексического представления документов и запросов: исходные словоформы, стеммы (стеммер авторов 2002 г.) и корни (стеммы без гласных, т.е. консонантный скелет). Поиск — система OKAPI; коллекция 548 документов (только заголовок + краткая аннотация), 40 запросов по 3–9 слов (Sec. 2, p. 255).
- **Разметка.** Судили top-20 каждого из трёх ранжирований; релевантные документы трёх выдач объединялись в общий пул, от которого считалась **относительная полнота** (relative recall) (p. 256). То есть знаменатель метрики — это фактически объединение (oracle union) трёх представлений.
- **Главные числа** (Table I, p. 257), средняя относительная полнота при отсечении 20: словоформы **49.07%**, стеммы **64.09%**, корни **62.83%**; всего найдено релевантных: 396 / 517 / 507. При отсечении 5: 15.6 / 20.1 / 20.1.
- **Статистика** (pp. 257–258): ANOVA F = 16.25, p = 0.0001; стеммы и корни значимо лучше словоформ (t-тест, оба p = 0.0001, односторонний; Sign test p = 0.00003 и 0.0011); стеммы vs корни — **различие незначимо** (t-тест p = 0.296; Sign test p = 0.581). Тесты — только для отсечения 20.
- **По запросам.** Лишь в 3 из 40 запросов словоформы нашли больше релевантных, чем стеммы или корни, и всего на 1–2 документа (p. 256). Для Query-2 найдены 4 нерелевантных документа, выданных только через корни; подробно разобраны 2 из них (док. 275 и 380) (гиперконфляция, «over-conflation»; p. 258).
- **Что это даёт для взаимодополняемости.** Явно перекрытие и уникальные находки **не** считаются. Но **по нашему выводу** (не заявлено авторами) числа Table I согласуются с общим пулом ≈807 релевантных документов (396/0.4907 ≈ 517/0.6409 ≈ 507/0.6283 ≈ 807) **[computed]**. Тогда даже лучшее представление (стеммы) не находит в top-20 около 290 документов пула, которые нашли словоформы и/или корни. Часть этого эффекта — просто ограничение отсечением 20 при ~20 релевантных на запрос в пуле. Поэтому это слабое, агрегатное свидетельство взаимодополняемости **между лексическими представлениями**, а не между лексическим и плотным поиском.
- **Чего нет:** BM25 не назван (только «OKAPI», «best-match search»; весовая функция не указана); нет плотного/нейросетевого поиска, нет fusion/гибрида, нет подсчёта перекрытия/уникальных находок, нет анализа признаков запросов; стоп-слова и нормализация письма не описаны.
- **Внутренние несоответствия / неточности:** (1) в разборе документа 380 объединение слов по консонантам «msr» приписано «стеммеру», хотя речь о документах, найденных только через **корни**; (2) «8 + 1 = 9 документов» складывает постинги двух терминов (Figure 2), т.е. это верхняя граница; (3) «happened for the four queries» — неясно, 4 показанных запроса или 4 запроса вообще; (4) вывод «стеммер необходим и достаточен» сильнее доказательств (стем vs корень незначимо, over-conflation показан на одном запросе).
- **Для нашего gap:** работа подтверждает уже занятую границу («raw/stem/root сравнивались в морфологически богатом языке с ограниченными ресурсами»); ядро v0.8 (raw/stem/lemma × фиксированный D → overlap/unique hits → прирост гибрида → признаки запросов) **не затрагивает**. Предложение: gap не менять.
- **Практическая польза для нас:** (1) пул из всех вариантов представления как знаменатель — правильная идея, но нужно явно публиковать размер пула и уникальные находки каждого канала; (2) глубина суждения должна превышать глубину оценки, иначе relative recall упирается в потолок отсечения; (3) полезна метрика «уникальные **нерелевантные** находки варианта нормализации» — цена гиперконфляции; (4) простая таблица побед/поражений по запросам (здесь 3/40) — минимальный обязательный отчёт.

---

## 1. Bibliographic record

- **Authors:** Nega Alemayehu, Peter Willett
- **Affiliation:** Department of Information Studies, University of Sheffield, UK (p. 254)
- **Year:** 2003
- **Venue:** *Program: electronic library and information systems*, Vol. 37, No. 4, pp. 254–259 (p. 254 footer and running heads)
- **Article type:** "Short communication" (p. 254)
- **Publisher:** MCB UP Limited (Emerald); ISSN 0033-0337 (p. 254)
- **DOI:** `10.1108/00330330310500748` (printed on p. 254)
- **Bibliographic check (web search):** the Emerald record lists the article at vol. 37, issue 4, first page 254, under the journal's current name *Data Technologies and Applications*; the DOI URL `emerald.com/insight/content/doi/10.1108/00330330310500748` matches the printed DOI; an open eprint is listed at White Rose Research Online (eprints.whiterose.ac.uk/145/). (bibliographic check: Emerald and White Rose search results; the Crossref API lookup was refused by the proxy, so month of issue was not verified.)
- **Funding / acknowledgement:** Canadian International Development Research Centre; OKAPI package provided by the Centre for Interactive Systems Research, City University London (p. 254).
- **Related sources named in the paper:** stemmer: Alemayehu & Willett (2002), *Literary and Linguistic Computing* 17(1):1–17; full experimental details: Alemayehu (1999), PhD thesis, University of Sheffield (p. 256, p. 259).
- **Source type:** peer-reviewed journal short communication
- **Reliability:** B
- **Full text available:** yes (`07_full_text/pdfs/CR000354.pdf`, 6 pages)

## 2. Why this work matters to the PhD

It is, to the authors' knowledge, the **first retrieval experiment on Amharic** (the authors' own claim: "There have, to our knowledge, been no previous IR experiments done on Amharic language text", p. 255) and an early, compact example of the exact lexical-side design our project uses: the **same queries and collection indexed under several morphological representations** (word / stem / root), with a **judging pool formed from all representations**.

| Axis | Relation |
|---|---|
| Lexical retrieval | Direct: OKAPI best-match retrieval over word, stem and root surrogates. The weighting function (e.g., BM25) is **not named** |
| Semantic retrieval | Absent |
| Hybrid retrieval | Absent: no fusion of representations or channels |
| Uzbek morphology | Indirect: Amharic is Semitic (vowel infixing + affixes); Uzbek is Turkic (suffixing). The stem level transfers in spirit; the consonantal root level has no Uzbek analogue |
| Low-resource retrieval | Direct: no prior Amharic test collection existed; the authors built one |
| Current gap | Supports the already-occupied boundary "raw/stem/root compared in a morphologically rich low-resource language"; contributes a pooled-union evaluation design and a per-query over-conflation example; does not touch the lexical–dense core (§16) |

## 3. Research problem

### Simple explanation

In Amharic, one verb root yields very many word forms (the paper lists eight forms generated from the three-consonant root of "sing", besides the citation form ዘፈነ "zefene", p. 255). If the search engine matches only exact word forms, a query word and a document word that are "the same word" in different forms do not match. The paper asks whether cutting words down to stems, or even further to consonantal roots, finds more relevant documents.

### Formal formulation

- Three document/query surrogates: words (W), stems (S), roots (R).
- Hypotheses (p. 256): **H0** — "The effectiveness of retrieval is the same for all three types of document surrogate"; **H1** — it is not the same.
- Effectiveness measured by mean relative recall at cut-offs 5, 10, 20 over 40 queries; hypothesis tests on the cut-off-20 values.

## 4. Main idea

### Simple explanation

Index the same small collection three times: as written, after stemming, and after reducing stems to consonant roots. Run the same 40 queries (processed the same way) through the OKAPI engine. Let university staff judge the top 20 results of each run, merge all relevant documents into one pool per query, and see what share of that pool each run finds.

### Concrete example (the paper's own, pp. 255, 257)

- Root ዝፍን "zfn" ("sing"). Words: ዘፈንኩ "I sang", ዘፈናችሁ "you sang (pl.)", ዘፈንሽ, ዘፈንክ, ዘፈኑ, ዘፋፈነ "he sang now and then", አስዘፈናቸው "he made them sing", ዘፍነዋል "they have sung".
- Word surrogate: each form is a separate index term.
- Stem surrogate: all forms except ዘፍነዋል are stemmed to ዘፈን; ዘፍነዋል becomes ዘፍን. So two index terms remain.
- Root surrogate: all forms become one term, ዝፍን.
- Query-2 ("oppression instruments and enterprises, parties"; Figure 2, p. 257): the number of documents containing each query term grows sharply with conflation:

| Query-2 term (original form) | Word | Stem | Root |
|---|---:|---:|---:|
| የጭቆና ("of oppression") | 0 | 22 | 56 |
| መሣሪያዎችና ("instruments and") | 0 | 8 | 59 |
| ድርጅቶች ("enterprises") | 8 | 45 | 62 |
| ፓርቲዎች ("parties") | 1 | 21 | 21 |

(Figure 2, p. 257, checked on the page image.) With words, two of the four query terms occur in no document at all.

### Formal method

- **Relative recall** for a query and surrogate *s* at cut-off *k*: (number of relevant documents in the top *k* of *s*) / (number of documents judged relevant in the merged pool of the top-20 outputs of W, S and R) (p. 256; definition paraphrased from the text).
- The authors note that relative recall "is monotonic with precision at a fixed cut-off as here" (p. 256).

## 5. Architecture / algorithm

1. **Stemming** (Alemayehu & Willett, 2002; described there, not here): an affix-removal stemmer for Amharic. Its internals are NOT_REPORTED in this paper.
2. **Root extraction:** "the roots obtained by elimination of the vowels from those stems" (p. 255). Roots have two to six consonants, three being most common (p. 255).
3. **Dictionary compression** (reported from the 2002 paper, p. 255): 50.3% for stems and 58.6% for roots.
4. **Indexing:** "documents and queries being indexed by means of the original words, the stemmed words, or the resulting roots" (p. 255). So query and document always share one representation.
5. **Retrieval:** OKAPI retrieval system (City University), "best-match search" (pp. 255–256). The weighting function, parameters, stop-word list and any Amharic script normalization are **NOT_REPORTED**.
   - Context (not from the paper): the Okapi system is the platform on which the BM-series weighting functions, including BM25, were developed, so BM25 is a plausible default. The paper does not say which function was used, so this card does **not** treat the runs as BM25.
6. **Cut-off:** top 20 per ranking (p. 255).
7. **Figure 1** (p. 257) lists the word, stem and root forms of Queries 2, 7, 18 and 32 (checked on the page image).

## 6. Data

- **Collection:** 548 documents from *A Catalogue of Clandestine Literature on Ethiopia* (Institute of Ethiopian Studies, 1995): anti-government propaganda during military rule, 1974–1991. Originals are letters, pamphlets, reports and books; **only the title and a short abstract** of each document were used (p. 255).
- **Language / domain:** Amharic; political/historical documents.
- **Queries:** 40, constructed by the authors ("We constructed"), each of 3–9 words, "each designed to retrieve at least some relevant documents from the collection" (p. 255). Examples: Queries 2, 7, 18, 32 (p. 256).
- **Relevance judgments** (p. 256):
  - judges: academic staff of Addis Ababa University from the Institute of Ethiopian Studies, Faculty of Law, Institute of Language Studies, Institute of Development Research, and the departments of Geography, History, Library and Information Science, Political Science and International Relations, and Sociology;
  - "Each judge was given a query and the top-ranked documents from a best-match search using each of the three types of document surrogate", with written and verbal instructions;
  - relevant documents from the three sets were merged into a pool per query.
  - NOT_REPORTED: number of judges, judges per query, whether judges knew which surrogate produced which document, relevance scale (binary is implied but not stated), agreement.
- **Pool size:** NOT_REPORTED. Our inference: ≈807 relevant documents in total, ≈20 per query (§9) **[computed, inferred]**.
- **Train/dev/test:** not applicable (no learned components); no tuning described.

## 7. Baselines

| Condition | What it is | Why selected | Fair comparison? |
|---|---|---|---|
| Words | Unprocessed word forms | Conventional word-based searching (abstract) | Yes within the design; the weighting function is shared but unnamed |
| Stems | Authors' 2002 stemmer | The method under evaluation | Same engine, queries, cut-off and pool |
| Roots | Stems with vowels removed | Arabic literature reports root ≥ stem (Al-Kharashi & Evens, 1994, as cited on p. 255) | Same as above |

No other stemmer, no truncation (n-prefix) baseline, and no second retrieval model is compared.

## 8. Metrics

| Metric | Definition | Simple meaning here | Appropriate? |
|---|---|---|---|
| Relative recall @ k (k = 5, 10, 20) | relevant found in top k / relevant documents in the merged top-20 pool of W, S, R | "What share of all relevant documents that any of the three runs found does this run find in its top k?" | Reasonable for a new collection without exhaustive judgments. Its **ceiling** is below 100% whenever the pool of a query holds more than k relevant documents |
| Total relevant retrieved | Sum over 40 queries of relevant documents in the top 20 | Raw count | Yes, descriptive |

Context (not from the paper): relative recall against a union pool is the same quantity as coverage of an **oracle union** of the compared runs; it is an early form of the measurement our project wants, but only in aggregate.

## 9. Results

### Table I (p. 257, checked on the page image)

| Surrogate | RR@5 (%) | RR@10 (%) | RR@20 (%) | Total relevant retrieved (top 20) |
|---|---:|---:|---:|---:|
| Words | 15.6 | 30.25 | 49.07 | 396 |
| Stems | 20.1 | 35.40 | 64.09 | 517 |
| Roots | 20.1 | 33.40 | 62.83 | 507 |

Derived values **[computed]**:
- RR@20: stems − words = +15.02 points (+30.6% relative); roots − words = +13.76 points (+28.0%); stems − roots = +1.26 points (+2.0%).
- Totals: stems/words +30.6%; roots/words +28.0%; stems/roots +2.0%.
- RR@5: stems = roots = 20.1, both +28.8% over words. RR@10: stems +17.0%, roots +10.4% over words.
- Approximate micro P@20 = total/(40 × 20): words 49.5% (a lower bound for the word runs' precision, since they returned fewer than 20 documents for some queries), stems 64.6%, roots 63.4%.

### Implied pool size (our inference, not stated by the authors)

- total / (RR@20 / 100): words 396/0.4907 = 807.0; stems 517/0.6409 = 806.7; roots 507/0.6283 = 806.9 **[computed]**.
- The three agree to within 0.4 documents. This suggests that the "mean relative recall" in Table I behaves like a **ratio of totals over a pool of ≈807 relevant documents** (≈20.2 per query), rather than a mean of per-query ratios, or that the two happen to coincide. The caption says "averaged over the set of 40 queries", so this remains an inference.
- If U ≈ 807: stems miss ≈290, roots ≈300, words ≈411 pooled relevant documents in their top 20; the sum of the three totals is 1,420, so pairwise overlaps (minus the triple overlap) total ≈613 **[computed]**. Unique relevant hits per surrogate **cannot** be derived from the paper.
- Caveat: with ≈20 relevant documents per query in the pool and a 20-document cut-off, no single run can reach 100% for many queries even with perfect precision. Low RR@20 is therefore partly a **cut-off ceiling**, not only non-overlap.

### Per-query statements (p. 256)

- Only three queries had the word-based search retrieve more relevant documents than the stem-based or root-based searches, each by "just one relevant or two relevant documents more in the cut-off 20 searches" (pp. 256–257). The number of tied queries is not reported.
- The word-based search retrieved fewer than 20 documents for Query-2 (nine, "8 + 1 = 9") and this "happened for the four queries"; for the rest all three runs returned more than 20 documents, with the word-based run always retrieving the fewest.
- "The same pattern of behaviour is seen at all three cut-off values" (p. 257).

### Root vs stem, Query-2 (p. 258, Figures 3–4 checked on the page image)

- Four non-relevant documents were retrieved in the top 20 by roots but not by stems; the paper details two of them (documents 275 and 380).
- Document 275: ደረጃ "dereja" ("stage") and ድርጅት "drjt" ("enterprise") are conflated under roots (only the latter matches under stems); ጭቁን "Cqun" ("oppressed") is conflated with the query word የጭቆና "yeCqona" ("of oppression").
- Document 380: እንዲመሠረት "Indimeseret" ("... establish") matches መሣሪያዎችና "me'sariyawoc" ("instruments and") through the shared consonants "msr"; in addition, the document word ፓርቲ "party" is related to a query word (ፓርቲዎች "parties").
- The authors attribute the slightly higher absolute score of stems to such over-conflation by roots (p. 258).

## 10. Statistical evidence

- **Tests** (pp. 256–258), on cut-off-20 relative recall only:
  - ANOVA: F = 16.25, "at two degrees of freedom", p = 0.0001; H0 rejected.
    - The denominator degrees of freedom and whether the ANOVA was repeated-measures (paired by query) are NOT_REPORTED. **[computed]** p for F = 16.25 is ≈1.3 × 10⁻⁶ with df (2, 78) and ≈5.9 × 10⁻⁷ with df (2, 117); the reported 0.0001 is therefore conservative (likely a rounding floor), not contradictory.
  - Pairwise t-tests: stems vs words and roots vs words both p = 0.0001 (one-tailed); stems vs roots p = 0.296 (not significant at 0.05). Paired or unpaired: NOT_REPORTED.
  - Kendall's coefficient of concordance W: H0 rejected "at the 0.001 level"; the W value is NOT_REPORTED.
  - Sign tests: stems vs words p = 0.00003; roots vs words p = 0.0011; stems vs roots p = 0.581.
    - **[computed]** p-values of this order are one-sided binomial tails for plausible counts of untied queries (e.g., 2 losses of 23 gives 3.3 × 10⁻⁵; 2 of 17 or 3 of 20 give ≈0.0012–0.0013), compatible with the "only three queries" statement; the paper does not give the win/loss/tie counts, so the tests cannot be reproduced exactly.
- **No correction** for multiple comparisons; not needed for the conclusions given the p-values, but not discussed.
- **Confidence intervals:** NOT_REPORTED.
- **Runs / seeds:** not applicable (deterministic retrieval), single configuration per surrogate.
- **Ablation:** none (no variation of stop-words, weighting, cut-off pool depth, or query/document side processing separately).
- **Per-query analysis:** partial and qualitative: the count of queries where words beat stems/roots (3 of 40), and the Query-2 over-conflation analysis. There is **no** per-query table, no unique-hit or overlap count between surrogates, and no query-feature analysis.
- **Complementarity (project dimensions):**
  - morphological variants of the lexical representation: **yes** (word / stem / root);
  - BM25: **not named** (OKAPI best-match; function unreported);
  - dense/neural retrieval: **no**;
  - fusion/hybrid: **no**;
  - overlap / unique relevant hits / oracle union: **only implicitly** — the relative-recall denominator is the union pool of the three surrogates, but no overlap or unique-hit counts are reported;
  - per-query / query-feature analysis: **anecdotal only** (Query-2; 3 of 40 queries where words win).

## 11. Strengths

- Clean within-subject design: same collection, queries, engine, cut-off and pool across three representations.
- Pooling from all compared representations avoids the bias of judging only one system's output.
- Both parametric and non-parametric tests, with the same conclusions.
- A concrete failure analysis of aggressive normalization (roots conflating unrelated words through shared consonants), not just averages.
- Independent judges from many disciplines rather than the authors.

## 12. Limitations

### Stated by the authors

- "Even with the small set of documents used here we have found many examples where the use of roots results in over-conflation" and such problems "would be much greater with larger files of text" (p. 258).
- Reported facts bearing on limitations (the authors do not frame them as limitations; that framing is ours):
  - the judges were new to this kind of task, so they received written and verbal instructions (p. 256);
  - full details and additional results are only in the PhD thesis (p. 256).

### Inferred from the experimental design

1. **Small, short documents.** 548 documents represented only by title + short abstract. Short texts magnify vocabulary mismatch, so the morphology effect may be larger than on full texts.
2. **Retrieval function unknown.** "OKAPI" and "best-match" only; weighting, parameters, stop-words and script normalization (Amharic has homophone Fidel characters — context, not from the paper) are not reported.
3. **Author-built queries,** "designed to retrieve at least some relevant documents" — possible selection toward the collection's vocabulary; construction procedure otherwise unreported.
4. **Shallow pool and cut-off ceiling.** Judging depth equals evaluation depth (20). With an inferred ≈20 relevant documents per query, RR@20 cannot reach 100% for many queries; documents ranked 21+ by one surrogate count as "missed" even if retrieved lower.
5. **Relative recall is pool-dependent:** adding a fourth surrogate would change every score.
6. **Judging protocol under-specified:** number of judges, blinding to surrogate, relevance scale and agreement are not reported.
7. **The conclusion "necessary and sufficient" (p. 258) overreaches:** stems vs roots is not significant, over-conflation is shown for one query, and no alternative stemmer or truncation baseline is tested.
8. **Aggregate only for the key comparison;** per-query data are not published.

## 13. What the work proves

- On this Amharic collection (548 title+abstract surrogates, 40 queries, OKAPI), **stem-based and root-based indexing retrieve significantly more relevant documents than word-based indexing**: RR@20 64.09% and 62.83% vs 49.07%; 517 and 507 vs 396 relevant documents (Table I, p. 257); ANOVA, t-tests, Kendall W and Sign tests agree (pp. 257–258).
- The advantage is **rarely reversed at query level**: words beat stems/roots on only 3 of 40 queries, by 1–2 documents (pp. 256–257); the number of ties is not reported, so this does not show that conflation helped on most of the remaining 37 queries.
- **Stems and roots do not differ significantly** (t-test p = 0.296; Sign test p = 0.581).
- Root conflation can **introduce false matches** between unrelated words sharing consonants, demonstrated for Query-2 (four root-only non-relevant documents; p. 258).

## 14. What the work does NOT prove

- **That the stemmer is "sufficient"** or better than roots: the stem–root difference is not significant, and although the authors say they found "many examples" of over-conflation (p. 258), they quantify none and illustrate only one query (Query-2, two documents detailed).
- **Anything about BM25 specifically:** the weighting function is not reported.
- **Anything about dense/semantic retrieval, fusion, or lexical–dense complementarity:** none are tested.
- **How much the three representations overlap or which relevant documents are unique to each:** only the union-pool denominator exists; unique hits are not reported, and our ≈807 pool estimate is an inference.
- **Which query characteristics make conflation help or hurt:** no query-feature analysis.
- **Generalization to full-text documents, larger collections or other domains.**

## 15. Relationship to current Uzbek evidence

- **No Uzbek data.** Transfer is limited: Amharic stems (affix removal) correspond roughly to Uzbek suffix stripping; Amharic consonantal roots have no Uzbek counterpart, although the "aggressive normalization creates false conflations" lesson applies to aggressive Uzbek stemming or truncation.
- In the same family of evidence as Can et al. (Turkish, MORPH-001) and Haddad & Bechikh Ali (Turkish BM25, MORPH-002): lexical normalization helps in a morphologically rich language, and more aggressive normalization is not automatically better (here stem ≥ root in absolute terms, not significantly).
- **Amharic cluster** (relations drawn from the sibling cards, not from this paper):
  - **CR000149** (Mekonnen et al. 2025, exemplar card): modern BM25 vs dense for Amharic, with no morphological processing of BM25 reported. This paper supplies the missing lexical-morphology side, but on a different, tiny collection and 22 years earlier.
  - **CR000447** (Yeshambel et al. 2024, 2AIRTC): per that card, Lemur LM MAP word/stem/root 0.43/0.57/0.70 — **root best**, unlike here, where stem ≥ root (not significant). Different collection, model and metric; the contrast shows the stem-vs-root order is not stable across settings.
  - **CR000427** (Yeshambel et al. 2023): per that card, with embedding-based query expansion the order reverses (word > root > stem). Together the three papers show that the effect of morphological representation depends on what it is combined with — which is the premise of our gap, but none of them measures lexical–dense complementarity.

## 16. Relationship to CURRENT_GAP

**Classification:** *supports (the existing boundary)* + *no material effect on the residual core*.

- **Supports / already occupied:** "raw/stem/lemma(root) have not been compared in low-resource IR" was already rejected in v0.8 (UPERF, Turkish studies). This paper is an additional, early Amharic citation for that rejected claim.
- **Touches, weakly, one v0.8 measurement element:** its relative recall uses the union of relevant documents found by all representations as denominator, i.e., oracle-union coverage **across lexical representations**. It does not report unique hits or overlap, and it has no dense component, so it does not touch "overlap/unique hits with a fixed dense retriever D".
- **Does not touch:** fixed modern dense D; fusion H_raw/H_stem/H_lemma; incremental hybrid gain; per-query relation to query features.
- **Triage flag `carries_complementarity_evidence = YES`:** accurate only in the narrow sense above (between lexical representations, aggregate, inferred). It should not be cited as lexical–semantic complementarity evidence.

**Proposal:** keep v0.8 refined unchanged; optionally add this paper to the evidence boundary as the earliest Amharic word/stem/root study. This is a proposal only; `CURRENT_GAP.md` has not been edited.

## 17. Implications for our research design

- **Pooling and qrels.**
  - Pool from **all** conditions (BM25_raw, BM25_stem, BM25_lemma, D, and hybrids), as this paper does for its three surrogates.
  - Judge **deeper than the evaluation cut-off** (e.g., judge top-30/50, evaluate at 10/20), so coverage metrics are not capped by the cut-off ceiling seen here.
  - **Publish the pool size per query** and per-condition unique relevant hits; the paper's omission forced us to reverse-engineer ≈807.
  - Record judge count, blinding to condition, relevance scale and agreement.
- **New metric proposal: unique non-relevant hits of a normalization variant** (documents a stemmed/lemmatized run retrieves in its top k that the raw run does not, and that are non-relevant). This operationalizes the over-conflation cost the authors show for Query-2 and complements unique relevant hits.
- **Per-query win/loss table** for raw vs stem vs lemma (here 3/40 losses) as a minimal required report, before any query-feature modelling.
- **Query taxonomy:** candidate features suggested by the Query-2 case: number of query terms with zero document frequency in raw form (two of four here, Figure 2); document-frequency growth under normalization (df ratio stem/raw) as a proxy of conflation aggressiveness.
- **Document representation:** document length (title+abstract vs full text) is a likely moderator of the morphology effect; keep the Uzbek document unit fixed and report it.
- **Statistics:** use a repeated-measures design with paired per-query tests (paired t-test or Wilcoxon, plus sign counts) and report test statistics and degrees of freedom — the paper's unreported df and pairing illustrate what to avoid.
- **Baselines:** include a simple truncation (n-prefix) control next to stem/lemma, which this paper lacks and which Turkish studies found competitive.
- **Hypothesis:** no evidence for or against the lexical–dense hypothesis; consistent with the expectation that raw → stem changes which relevant documents the lexical channel finds (517 vs 396 relevant, with an estimated ≈613 pairwise-overlap mass among three surrogates), which is the precondition for a complementarity shift.

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| Stemming | Cutting prefixes/suffixes so different forms of a word become one index term | Affix removal mapping word forms to a stem |
| Root (Amharic) | The consonant skeleton shared by many related words | Stem with vowels removed; 2–6 consonants (p. 255) |
| Conflation / over-conflation | Treating different word forms as the same term; over-conflation = merging unrelated words | Many-to-one term mapping; false merges |
| Document surrogate | The text actually indexed for a document | Here: title + short abstract in word, stem or root form |
| OKAPI | A research retrieval system from City University London | Best-match probabilistic ranking platform; function used here not stated |
| Pool / pooling | The set of documents shown to judges, gathered from several systems' top results | Union of top-k outputs of all compared runs |
| Relative recall | Share of all relevant documents found by any compared run that this run finds | relevant retrieved@k / relevant in merged pool |
| Oracle union (project term) | The set of relevant documents found by at least one of the compared channels | Union of relevant retrieved sets |
| ANOVA | Test of whether several group means differ | F-test on between- vs within-condition variance |
| Kendall's W | Agreement of rankings across queries | Coefficient of concordance, 0–1 |
| Sign test | Counts per query which system won, ignoring the size of the difference | Binomial test on win/loss counts |
| Unique relevant hit (project term) | A relevant document found by one channel but not the other | Relevant ∩ retrieved_A \ retrieved_B |

## 19. Open questions / verification needed

1. Which OKAPI weighting function (BM1/BM11/BM15/BM25 or other) and parameters were used? NOT_REPORTED; the PhD thesis (Alemayehu, 1999) may say.
2. Is Table I's "mean relative recall" a mean of per-query ratios or a ratio of totals? The totals imply a consistent pool of ≈807 (§9); needs the thesis or per-query data.
3. Pool size, judges per query, blinding, relevance scale and agreement: NOT_REPORTED.
4. "This happened for the four queries" (p. 256): the four illustrative queries or four queries in total?
5. Document 380 (p. 258): the "msr" conflation is attributed to "the stemmer" in a passage about root-only retrieval; Figure 1 shows the stem መሳር and the root ምስር for "me'sariyawocna", so the conflation is plausibly root-level. Wording inconsistency in the paper; not resolvable here.
6. "8 + 1 = 9 documents" (p. 256) adds postings of two terms (Figure 2); the true number of distinct documents is ≤ 9.
7. ANOVA denominator df and whether it was repeated-measures; pairing of the t-tests.
8. Does the Alemayehu (1999) thesis contain per-query results or overlap data between surrogates? It is not in our record set as far as the assignment shows; check the corpus.

## 20. Decision after deep dive

- **Keep current gap?** Yes; v0.8 refined remains valid (§16).
- **Modify gap?** No. Optionally list this paper in the evidence boundary as an early Amharic word/stem/root study (researcher's decision).
- **Add decision?** Proposed for `decisions/DECISIONS.md` (researcher's decision):
  - "Qrels pool depth must exceed the evaluation cut-off; report pool size and per-condition unique relevant hits";
  - "Report per-query win/loss counts for raw vs stem vs lemma".
- **Add experiment?** Add "unique non-relevant hits of a normalization variant" (over-conflation cost) to the per-query measurement set, next to unique relevant hits.
- **Add citation to Chapter I?** Yes, briefly: §1.1 (morphological normalization in lexical IR for morphologically rich, low-resource languages; stem vs root; over-conflation), together with CR000447 and CR000427 as the Amharic line.
- **Proposed `MASTER_INDEX.md` row** (to add after approval):

| MORPH-026 | Alemayehu & Willett — *The effectiveness of stemming for information retrieval in Amharic* (*Program* 37(4), 254–259, short communication) — [deep dive](deep-dives/2003_Alemayehu_Willett_Amharic_Stemming_IR.md) | 2003 | B | MEDIUM | First Amharic IR experiment (to the authors' knowledge): 548 title+abstract docs, 40 queries, OKAPI (weighting function not named) over word / stem / root surrogates; top-20 pooled judgments, relative recall. RR@20 words/stems/roots 49.07/64.09/62.83% (396/517/507 relevant); stem and root > word (ANOVA F=16.25; t and Sign tests p≤0.0011), stem vs root n.s. (p=0.296/0.581); words win on 3/40 queries; root over-conflation shown for Query-2. Union-pool denominator only; no unique-hit/overlap counts, no BM25 named, no dense, no fusion, no query-feature analysis. |
