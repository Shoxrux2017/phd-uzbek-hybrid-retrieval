# Hollink, Kamps, Monz & de Rijke (2004): Monolingual Document Retrieval for European Languages

**Targeted deep-dive status:** COMPLETED (AI-assisted, pending researcher review)
**Completed:** 2026-09-28
**Literature ID:** `MORPH-032` (assigned 2026-09-28, approved by researcher)
**Systematic-review record:** `CR000338`. Full-text triage: INCLUDE, reading priority HIGH, reading tier "2 — важно", `carries_complementarity_evidence = YES`. In this card we qualify this flag: the paper has **no** complementarity evidence in the project's sense. Its per-topic table covers only the word-based run across languages, not different representations or channels (§10, §16).
**Provenance:** AI-assisted deep dive (Claude). The paper (20 PDF pages, printed pp. 33–52) was read in full from the pdftotext extraction. The extraction loses all significance markers, so every table was re-read on page images. Pages checked visually: printed pp. 33 (header), 35 (Sec. 2, Table 1), 36 (significance-marker legend, Table 2), 38 (Table 3), 41 (Fig. 1), 42 (Table 4), 43 (Table 5), 44 (Table 6), 45 (Tables 7–8), 46 (Table 9) and 48 (Table 10). These are PDF pp. 1, 3, 4, 6, 9, 10, 11, 12, 13, 14 and 16. Tables 3, 4, 6, 7 and 8 were also checked on 250-dpi crops. Numbers computed by us are marked **[computed]** and were recomputed with Python.
**Source rule:** **the paper is the primary and only authoritative source.** No code, website or later paper was used for claims about the authors' work. The DOI and issue come from a bibliographic check of the Springer article page only (see §1).
**Verification:** independent AI verifier pass 2026-09-28; 8 findings addressed.
**Reliability:** **A**. This is a peer-reviewed journal article in *Information Retrieval* (Kluwer), vol. 7, pp. 33–52, 2004 (received 5 Dec 2002, revised 13 May 2003, accepted 14 May 2003, p. 33). It is a primary controlled experimental study, although the authors frame it as a survey of techniques.

---

## Кратко для исследователя (RU)

- **Что сделано.** Контролируемое сравнение способов формирования лексического представления для 8 европейских языков (нидерландский, английский, финский, французский, немецкий, итальянский, испанский, шведский). Условия эксперимента:
  - CLEF 2002, темы 91–140, поля T+D;
  - одна система FlexIR: векторная модель Lnu.ltc с псевдорелевантной обратной связью Роккио во всех прогонах;
  - метрика MAP; значимость проверялась бутстрепом.
- **Варианты представления:**
  - словоформы с диакритикой и без неё;
  - стемминг Snowball (8 языков);
  - лемматизация TreeTagger (только EN/FR/DE/IT);
  - разбиение композитов (NL/FI/DE/SV) и разбиение + стемминг;
  - символьные n-граммы: 4 и 5 внутри слова, 6 через границу слов; n-граммы строились от словоформ, стемов и лемм.
- **Главные числа** (MAP; Tables 2–8, pp. 36–45):
  - удаление диакритики улучшает все 8 языков, значимо в 5 (например, FR 0.3627→0.4296);
  - стемминг улучшает все 8 языков, значимо только FI (0.2545→0.3308, +30.0%), ES (+10.5%) и DE (+7.3%);
  - лемматизация хуже стемминга во всех 4 языках, где есть обе (EN 0.4003 vs 0.4639);
  - 4-граммы словоформ улучшают все 8 языков, значимо FI, DE, IT, SV;
  - лучший финский прогон — стем + 5-граммы, 0.3935 (+54.6% к словоформам **[computed]**).
- **Общий вывод авторов:** «нет единой лучшей комбинации настроек» (p. 49). Лучший вариант зависит от языка и не следует языковой семье. Гипотеза «4-граммы всегда лучшие» опровергнута для испанского; гипотеза «разбиение + стемминг» не опровергнута.
- **Чего нет (измерения нашего gap):**
  - BM25 нет (модель Lnu.ltc);
  - плотного и нейросетевого поиска нет;
  - fusion/гибрида нет: комбинации «стем → n-граммы» — это последовательная обработка в одном индексе, а не объединение прогонов;
  - нет перекрытия результатов, уникально найденных релевантных документов и oracle union;
  - разбор по темам только для словоформенного прогона между языками (Table 9, 10 тем), а не между вариантами представления.
- **Внутренние несоответствия в статье:**
  - в 4 ячейках столбец «% change» не согласуется с приведёнными MAP ни при каком округлении: Table 6 EN 4-gram 7.3 vs 7.47 **[computed]**, FI 4-gram 37.4 vs 38.94, Table 7 FI 5-gram-stem 20.8 vs 18.95, FR 4-gram-stem −6.4 vs −6.67;
  - Sec. 4.2 называет столбец лемматизации «четвёртым», хотя по нумерации Sec. 4.1 это пятый;
  - в Sec. 6.1 написано «CLEF 2003 languages» при темах CLEF 2002.
- **Методические оговорки:**
  - PRF Роккио включена во все прогоны, а для «некоторых» n-граммных прогонов разрешено до 100 добавленных терминов вместо 20; какие это прогоны, не сказано;
  - число оцениваемых тем по языкам не приведено, кроме финского (30 из 50 тем);
  - размеры коллекций в статье не даны: авторы ссылаются на вводную статью выпуска.
- **Для нашего gap:** работа поддерживает фон: эффект морфологического представления зависит от языка, а лемматизация не обязательно лучше стемминга. Ядро v0.8 (raw/stem/lemma BM25 × фиксированный D → overlap/unique hits → прирост гибрида) **не затрагивает**. Предложение: gap не менять.
- **Практическая польза для нас:**
  1. Нормализацию графики (у авторов диакритика; у нас апостроф в oʻ/gʻ и латиница/кириллица) делать отдельным контрольным условием: у авторов она сама даёт до +23.4% MAP (FI, незначимо; значимо до +19.3%, SV).
  2. Добавить символьные n-граммы как языконезависимый контрольный вариант лексического канала (BM25_ngram): для агглютинативного финского это сильнейший тип представления.
  3. PRF либо отключить, либо применять одинаково во всех условиях, иначе эффект представления смешивается с эффектом расширения запроса.
  4. Не предполагать `lemma > stem > raw`: это измеряется.

---

## 1. Bibliographic record

- **Authors:** Vera Hollink, Jaap Kamps, Christof Monz, Maarten de Rijke
- **Affiliation:** Language & Inference Technology Group, ILLC, University of Amsterdam (p. 33); Hollink's later address: Social Science Informatics, Dept. of Psychology, University of Amsterdam (footnote, p. 33)
- **Year:** 2004
- **Venue:** *Information Retrieval*, vol. 7, pp. 33–52 (running header p. 33: "Information Retrieval, 7, 33–52, 2004")
- **Publisher:** Kluwer Academic Publishers (p. 33)
- **Dates:** received 5 Dec 2002; revised 13 May 2003; accepted 14 May 2003 (p. 33)
- **Issue:** not printed in the PDF. The paper refers to "the editors' introduction" and "Braschler and Peters (this volume)" (p. 34), which indicates a CLEF special issue. A ResearchGate record title in the search results reads "…Special Issue on CLEF" (bibliographic check: web search). The Springer article page (opened by the verifier, 2026-09-28) gives **vol. 7, issue 1, January 2004, pp. 33–52**.
- **DOI:** `10.1023/B:INRT.0000009439.19151.4c`, confirmed on the opened Springer article page (verifier bibliographic check, 2026-09-28). Crossref remained blocked by the proxy.
- **Official URL:** https://link.springer.com/article/10.1023/B:INRT.0000009439.19151.4c. Springer lists the journal under its later name "Discover Computing".
- **Source type:** peer-reviewed journal article (experimental study framed as a survey)
- **Reliability:** A
- **Full text available:** yes (`07_full_text/pdfs/CR000338.pdf`, 20 pages)

## 2. Why this work matters to the PhD

This is a classic, peer-reviewed, **multi-language controlled comparison of lexical representations**. It uses one retrieval engine, one topic set translated into eight languages, a common sanitizing pipeline, and one set of stop-word lists where possible. Inside that setting, only the index-term representation is varied:

- raw word forms (with and without diacritics);
- Snowball stems;
- TreeTagger lemmas;
- compound splitting;
- character n-grams, built from words, stems or lemmas.

| Axis | Relation |
|---|---|
| Lexical retrieval | **Main focus.** Vector space Lnu.ltc with blind feedback; many representation variants. Not BM25 |
| Semantic retrieval | **Absent** |
| Hybrid retrieval | **Absent.** No run fusion; the "combinations" are sequential processing pipelines inside one index |
| Uzbek morphology | Indirect. The closest language typologically is Finnish (agglutinative [context, not from the paper]; Finno-Ugric, p. 47; average word length 7.3, Table 5, p. 43), where normalization and n-grams give the largest gains |
| Low-resource retrieval | Partly. Motivated by "small European languages" with costly tooling (pp. 33–34); knowledge-poor n-grams as an alternative to language tools |
| Current gap | Supports the background claim that the effect of the lexical representation is language-dependent and not predictable from language family. It does **not** touch morphology-induced lexical–dense complementarity (§16) |

## 3. Research problem

### Simple explanation

Search engines match the words of a query against the words of documents. In many European languages one word appears in many forms (endings, compounds, accents), so exact matching misses relevant documents. There are two families of fixes:

- **linguistic tools**: stemmers, lemmatizers, compound splitters;
- **language-independent tricks**: cutting words into overlapping character pieces (n-grams).

The authors ask which fixes help, for which languages, and whether a single strategy works for all.

### Formal formulation

The paper states no numbered research questions. The stated aim is "to survey the current state of the art in monolingual retrieval for European languages", with a focus on "language-specific versus language-independent techniques" (p. 34). Operationally:

- For each language `L` ∈ {NL, EN, FI, FR, DE, IT, ES, SV} and each index-term representation `R`, measure MAP(`L`, `R`) on the CLEF 2002 topics under a fixed retrieval model.
- Test `R` against a reference representation with a one-tailed bootstrap test.
- Finally test two uniform hypotheses (Sec. 6.3, p. 49): "split, then stem is best" and "4-gramming of words is best".

## 4. Main idea

### Simple explanation

Keep everything fixed except how words are turned into index terms, then compare mean average precision language by language.

### Concrete example (from the paper)

- **Raw with diacritic mapping:** German *Raststätte* is indexed as *raststatte* (p. 36).
- **Stemming:** the Dutch description of Topic 95, after case folding, stopping and Snowball stemming, becomes "palestijn conflict artikel ∗gewap conflict palestijn gebied betrok ∗del bevolk geweld". The asterisks mark non-words produced by the stemmer (*gewap*, *del*) (p. 39; asterisk placement checked on the page image).
- **Compound splitting:** *bahnhof* → *bahn+hof*; the index keeps *bahnhof* and adds *bahn* and *hof* (pp. 40–41).
- **6-grams across word boundaries:** the Dutch *maatschappelijke gevolgen* becomes "maatsc aatsch atscha … lijke_ ijke_g jke_ge ke_gev e_gevo _gevol gevolg …" (p. 44).

### Formal method

- **Retrieval model:** the vector space model with the Lnu.ltc weighting scheme (pivoted document-length normalization, slope 0.2, pivot = average number of unique words per document) (p. 35).
- **Query expansion:** Rocchio blind feedback. The top 10 documents are treated as relevant and the bottom 500 as non-relevant. At most 20 expansion terms are added, and "in some of the n-gram-based runs … as many as 100" (p. 35).
- **Evaluation:** MAP per language; one-tailed bootstrap confidence interval on the improvement (1,000 bootstrap samples); significance marked at 95% and 99% (pp. 35–36).

## 5. Architecture / algorithm

1. **Topic processing** (p. 35):
   - title and description fields only;
   - stop phrases such as "Relevant documents report…" and "Find documents…" removed automatically in all eight languages.
2. **Sanitizing** (p. 35):
   - lowercasing (for lemmatized runs, after lemmatizing);
   - mapping diacritic characters to unmarked ones (except in the "kept" runs of Table 2).
3. **Stop-words** (p. 35, Table 1):
   - Snowball lists for seven languages; Savoy's list for Finnish;
   - list lengths: NL 101, EN 119, FI 1,134, FR 155, DE 231, IT 279, ES 313, SV 114;
   - stop-words removed at indexing time and before stemming and n-gramming.
4. **Representations:**
   - **Word-based:** surface forms after sanitizing (Sec. 3).
   - **Stemmed:** Snowball stemmers for all eight languages (Sec. 4.1). The authors note that rule sets "may differ in quality between the languages" (p. 38).
   - **Lemmatized:** TreeTagger lemmas for EN/FR/DE/IT only. Part-of-speech output is not used, and "mainly number, case, and tense information is removed" (pp. 39–40). The handling of unknown words is **NOT_REPORTED**.
   - **Compound split:** recursive splitter (Fig. 1, p. 41; from Monz & de Rijke 2002). The splitter works as follows:
     - the collection vocabulary with collection frequencies serves as the lexicon;
     - parts must be at least 4 characters, so a compound has at least 8 characters;
     - parts must have a higher collection frequency than the compound;
     - linking elements: NL -s-, -e-, -en-; DE -s-, -n-, -e-, -en-; SV -s-, -e-, -u-, -o-;
     - splits without a linker are preferred, and a 1-character linker is preferred over a 2-character one;
     - documents and queries keep the compound **and** add its minimal parts (an expanding, not a replacing, representation);
     - compound and parts are weighted independently (pp. 40–42).
   - **Split + stem:** split first, then stem (Table 4).
   - **Character n-grams:** 4- and 5-grams within word boundaries; 6-grams across word boundaries (Sec. 5.1). They are built from words (Table 6), stems (Table 7) or lemmas (Table 8). The authors cite a 5–6× larger index for n-grams (McNamee & Mayfield 2002a, p. 43); they did not measure index size themselves.
5. **Retrieval:** Lnu.ltc + Rocchio PRF for every run (p. 35).

## 6. Data

- **Dataset / corpus:** CLEF 2002 monolingual collections for eight languages. The paper does not describe the collections: "We refer to Braschler and Peters (this volume) for details" (p. 34). **Collection sizes, sources and periods: NOT_REPORTED in this paper.**
- **Language(s):** Dutch, English, Finnish, French, German, Italian, Spanish, Swedish.
- **Domain:** NOT_REPORTED in this paper. Context (not from the paper): the CLEF collections are newspaper and news-agency text.
- **Queries:** the 50 CLEF 2002 topics (91–140), translated into all languages by native speakers (p. 46); T+D fields (p. 35).
- **Topics actually evaluated per language:** NOT_REPORTED, except that "The Finnish collection covers only 30 of the 50 CLEF 2002 topics" and two further topics have no relevant documents in the English collection (p. 46). MAP values are therefore presumably computed over different topic sets per language (our inference; the paper does not say which topics enter each MAP). The exact counts are not given.
- **Relevance judgments:** CLEF qrels. The pooling and assessment procedure are not described in this paper (NOT_REPORTED).
- **Train/dev/test:** no learning. The parameters (slope 0.2, 10/500 feedback documents, 20/100 expansion terms, splitter thresholds) are stated as fixed. How they were chosen is NOT_REPORTED. All results are on the same CLEF 2002 topic set.

## 7. Baselines

| Baseline | What it is | Why selected | Fair comparison? |
|---|---|---|---|
| Word-based, diacritics kept | Surface forms as they occur | Reference for the diacritics experiment (Table 2) | Yes; only the diacritic mapping differs |
| Word-based, diacritics removed ("naive baseline") | Lowercased surface forms, diacritics mapped | Reference for stemming, lemmatization, splitting and word n-grams (Tables 3, 4, 6) | Yes within a language; all runs share the model, stop-words and PRF |
| Stemmed run | Snowball stems | Reference for split+stem (Table 4) and stem n-grams (Table 7) | Yes |
| Lemmatized run | TreeTagger lemmas | Reference for lemma n-grams (Table 8) | Yes, but lemmatizers exist for only 4 languages, and the lemmatized run is weaker than the stemmed run in all 4 |

Additional fairness notes:

- **PRF parameters vary.** At most 20 expansion terms in "most runs", up to 100 in "some of the n-gram-based runs" (p. 35). Which runs used 100 is **NOT_REPORTED**, so some n-gram gains may partly reflect a different feedback budget.
- **Different tool families.** Snowball stems and TreeTagger lemmas are not "the same normalization at different depths". TreeTagger removes "mainly number, case, and tense information … leaving other morphological processes intact" (p. 40). Snowball stemmers "can be very aggressive, and may produce non-words" (p. 39). The lemma < stem result therefore compares two specific tools, not "lemmatization" vs "stemming" in general.

## 8. Metrics

| Metric | Definition | Simple meaning | Appropriate? |
|---|---|---|---|
| Average precision (AP) per topic | mean of precision at the rank of each relevant document | "How early, on average, the relevant documents appear for one topic" | Standard for TREC-style ad hoc retrieval |
| MAP | mean of AP over topics | Overall ranking quality over the topic set | Yes; the only effectiveness metric in the paper |
| Relative change (%) | (MAP_b − MAP_a) / MAP_a × 100 | Relative gain over the reference run | Yes, but inconsistent in 4 cells (§9) |

Not reported: Recall@k, P@k, nDCG, the number of relevant documents retrieved, and per-topic results for any run other than word-based.

Significance (pp. 35–36):

- one-tailed bootstrap, 1,000 samples;
- an improvement is significant if the left limit of the confidence interval is > 0 (a decrease: right limit < 0);
- markers: △ = improvement at 95%, ▲ = improvement at 99%, ▽ = decrease at 95%, ▼ = decrease at 99%.

The paper does not state explicitly that the resampled units are per-topic score differences, although "samples of size N from the original sample of N observations" implies per-topic observations.

## 9. Results

Significance markers below were read from the page images. The text extraction does not contain them.

### Table 2: diacritics (p. 36), MAP

| Language | Kept | Removed | % change (printed) |
|---|---:|---:|---:|
| Dutch | 0.4089 | 0.4482 | +9.6 ▲ |
| English | 0.4370 | 0.4460 | +2.1 |
| Finnish | 0.2061 | 0.2545 | +23.4 |
| French | 0.3627 | 0.4296 | +18.4 ▲ |
| German | 0.3812 | 0.3886 | +1.9 |
| Italian | 0.3764 | 0.4049 | +7.6 △ |
| Spanish | 0.3944 | 0.4537 | +15.0 ▲ |
| Swedish | 0.2684 | 0.3203 | +19.3 ▲ |

- Removing diacritics improves all 8 languages, significantly in 5, as stated in the text (p. 37).
- The Finnish +23.4% is **not** significant; the likely reason is the small topic set (30 topics, our inference).
- The text notes a contradiction with Savoy (1999) for French (p. 37).

### Table 3: stemming and lemmatization vs word-based (p. 38), MAP

| Language | Word-based | Stemmed | % | Lemmatized | % |
|---|---:|---:|---:|---:|---:|
| Dutch | 0.4482 | **0.4535** | +1.2 | – | |
| English | 0.4460 | **0.4639** | +4.0 | 0.4003 | −10.2 |
| Finnish | 0.2545 | **0.3308** | +30.0 ▲ | – | |
| French | 0.4296 | **0.4348** | +1.2 | 0.4116 | −4.2 |
| German | 0.3886 | **0.4171** | +7.3 △ | 0.4118 | +6.0 △ |
| Italian | 0.4049 | **0.4248** | +4.9 | 0.4146 | +2.4 |
| Spanish | 0.4537 | **0.5013** | +10.5 ▲ | – | |
| Swedish | 0.3203 | **0.3256** | +1.7 | – | |

- Stemming improves all 8 languages; the improvement is significant only for FI, DE and ES (p. 38).
- **Lemmatized < stemmed in all 4 languages** where both exist **[computed]**: EN −0.0636, FR −0.0232, DE −0.0053, IT −0.0102 MAP. No significance test between the lemma and stem runs is reported.
- English lemmatization −10.2% vs word-based is not significant (p. 40: "none of these are significant").

### Table 4: compound splitting, compound-rich languages (p. 42), MAP

| Language | Word-based | Split | % | Stemmed | Split + Stem | % vs Stemmed |
|---|---:|---:|---:|---:|---:|---:|
| Dutch | 0.4482 | 0.4662 | +4.0 | 0.4535 | **0.4698** | +3.6 |
| Finnish | 0.2545 | 0.3020 | +18.7 △ | 0.3308 | **0.3633** | +9.8 |
| German | 0.3886 | 0.4360 | +12.2 △ | 0.4171 | **0.4816** | +15.5 ▲ |
| Swedish | 0.3203 | 0.3395 | +6.0 | 0.3256 | **0.4080** | +25.3 ▲ |

- The text's "combined improvement of splitting and stemming over the word-based runs ranges from 5% for Dutch to 43% for Finnish" (p. 42) checks out **[computed: +4.82% NL, +42.75% FI; DE +23.93%, SV +27.38%]**.
- Swedish: stemming alone +1.7% (n.s.), splitting alone +6.0% (n.s.), both together +27.4% over word-based **[computed]**. This is a strong interaction between two representation steps.

### Table 6: character n-grams of words vs word-based (p. 44), MAP (printed % in brackets)

| Language | Word | 4-gram (within) | 5-gram (within) | 6-gram (across) |
|---|---:|---:|---:|---:|
| Dutch | 0.4482 | 0.4495 (+0.3) | 0.4401 (−1.8) | **0.4522** (+0.9) |
| English | 0.4460 | **0.4793** (+7.3)* | 0.4341 (−2.7) | 0.4261 (−4.5) |
| Finnish | 0.2545 | 0.3536 (+37.4)▲* | **0.3762** (+47.8)▲ | 0.3560 (+39.9)△ |
| French | 0.4296 | **0.4583** (+6.7) | 0.4348 (+1.2) | 0.4427 (+3.1) |
| German | 0.3886 | 0.4679 (+20.3)▲ | **0.4699** (+20.9)▲ | 0.4574 (+17.7)▲ |
| Italian | 0.4049 | **0.4355** (+7.6)▲ | 0.4140 (+2.3) | 0.3980 (−1.7) |
| Spanish | 0.4537 | 0.4605 (+1.5) | 0.4648 (+2.5) | **0.4671** (+3.0) |
| Swedish | 0.3203 | **0.4080** (+27.4)▲ | 0.3854 (+20.3)△ | 0.3942 (+23.1)△ |

\* printed % inconsistent with the printed MAPs (see "Internal inconsistencies" below).

- 4-grams of words improve all 8 languages, significantly FI, DE, IT and SV (text: "in 4 of the 8 languages", p. 44).
- The authors see no correlation between average word length (Table 5) and the best n-gram length (p. 44).

### Table 7: n-grams after stemming vs stemmed (p. 45), MAP

| Language | Stemmed | 4-gram-stem | 5-gram-stem | 6-gram-stem |
|---|---:|---:|---:|---:|
| Dutch | **0.4535** | 0.4372 (−3.6) | 0.4462 (−1.6) | 0.4524 (−0.2) |
| English | **0.4639** | 0.4075 (−12.2) | 0.3795 (−18.2)▼ | 0.4245 (−8.5) |
| Finnish | 0.3308 | 0.3644 (+10.2) | **0.3935** (+20.8)△* | 0.3898 (+17.8) |
| French | 0.4348 | 0.4058 (−6.4)* | 0.3876 (−10.9)▽ | **0.4364** (+0.4) |
| German | 0.4171 | 0.4539 (+8.8) | 0.4271 (+2.4) | **0.4702** (+12.7)▲ |
| Italian | **0.4248** | 0.3881 (−8.6) | 0.3605 (−15.1)▼ | 0.3808 (−10.4)▽ |
| Spanish | **0.5013** | 0.4468 (−10.9)▼ | 0.4226 (−15.7)▼ | 0.4586 (−8.5)▽ |
| Swedish | 0.3256 | **0.4010** (+23.2)▲ | 0.3857 (+18.5)△ | 0.3876 (+19.0)△ |

- n-gramming stems helps the compound-rich/agglutinative languages (FI, DE, SV).
- It significantly **hurts** EN, FR, IT and ES in some settings (p. 45).

### Table 8: n-grams after lemmatization vs lemmatized (p. 45), MAP

| Language | Lemmatized | 4-gram-lemma | 5-gram-lemma | 6-gram-lemma |
|---|---:|---:|---:|---:|
| English | 0.4003 | 0.4133 (+3.3) | 0.3845 (−4.0) | **0.4273** (+6.8) |
| French | 0.4116 | **0.4454** (+8.2)△ | 0.4318 (+4.9) | 0.4381 (+6.4) |
| German | 0.4118 | **0.4869** (+18.2)▲ | 0.4548 (+10.4)△ | 0.4759 (+15.6)▲ |
| Italian | **0.4146** | 0.4068 (−1.9) | 0.3877 (−6.5) | 0.3924 (−5.4) |

### Table 10: best run per language (p. 48), with MAP looked up from Tables 3–8 **[computed]**

| Language | Best run (Table 10) | MAP | vs word-based |
|---|---|---:|---:|
| Dutch | Split, then stemmed | 0.4698 | +4.8% |
| English | Words, 4-grammed | 0.4793 | +7.5% |
| Finnish | Stemmed, then 5-grammed | 0.3935 | +54.6% |
| French | Words, 4-grammed | 0.4583 | +6.7% |
| German | Lemmatized, then 4-grammed | 0.4869 | +25.3% |
| Italian | Words, 4-grammed | 0.4355 | +7.6% |
| Spanish | Stemmed | 0.5013 | +10.5% |
| Swedish | Words, 4-grammed / Split, then stemmed (tie) | 0.4080 | +27.4% |

- We checked that each Table 10 entry is the maximum over all runs reported for that language **[computed]** ✓.
- Spread between the best and the worst reported representation per language, excluding the diacritics-kept runs of Table 2: 0.033 (NL) to 0.139 (FI) MAP **[computed]**; including them: 0.061 (NL) to 0.187 (FI) **[computed]**.
- Uniform-strategy tests (p. 49):
  - "4-gramming of words" is significantly beaten only in Spanish, by the stemmed run (99% confidence; 0.5013 vs 0.4605, +8.9% **[computed]**);
  - no language's best run significantly beats "split, then stem".
- Unweighted means over the 8 languages **[computed; crude, because topic sets differ by language]**: word 0.3932; stem 0.4190; 4-gram 0.4391; split+stem (stem for non-compound languages) 0.4434.

### Table 9: per-topic AP, word-based run, 5 best and 5 worst topics (p. 46)

| Topic | NL | EN | FI | FR | DE | IT | ES | SV | Mean |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 94 • | 0.8199 | 0.8324 | 0.0158 | 0.7778 | 0.9315 | 0.5237 | 0.8595 | 0.9500 | 0.7138 |
| 98 • | 0.9444 | 1.0000 | 0.5020 | 0.8166 | 0.5957 | 0.6057 | 0.4645 | 0.8333 | 0.7203 |
| 107 ◦ | 0.0304 | 0.1322 | 0.0000 | 0.1349 | 0.1165 | 0.1117 | 0.0604 | 0.0694 | 0.0819 |
| 109 ◦ | 0.0333 | 0.2100 | 0.0266 | 0.0960 | 0.0037 | 0.1621 | 0.5243 | 0.0629 | 0.1399 |
| 111 ◦ | 0.0001 | 0.5453 | 0.0000 | 0.0164 | 0.0368 | 0.0360 | 0.0236 | 0.0143 | 0.0841 |
| 115 ◦ | 0.0281 | 0.1774 | 0.0000 | 0.0420 | 0.0104 | 0.5366 | 0.2018 | 0.0065 | 0.1253 |
| 119 • | 0.5204 | 0.7693 | 0.1520 | 0.8952 | 0.7486 | 0.7993 | 0.7203 | 0.6820 | 0.6609 |
| 123 • | 0.8434 | 0.5471 | 0.5588 | 1.0000 | 1.0000 | 0.8498 | 0.8783 | 0.9096 | 0.8234 |
| 128 ◦ | 0.0298 | 0.1083 | 0.0193 | 0.2656 | 0.1430 | 0.0618 | 0.3420 | 0.1548 | 0.1406 |
| 130 • | 0.6231 | 0.5042 | 0.6000 | 0.6106 | 0.7617 | 0.3279 | 0.7913 | 0.7196 | 0.6173 |

- All 10 printed means were recomputed from the 8 language values and match **[computed]** ✓.
- The authors' reading (pp. 46–47):
  - the best topics contain proper names;
  - the worst contain general, high-frequency terms;
  - Finnish Topic 94 (0.0158) fails because of inflected name forms: "Solzhenitsyjen, Solzhenitsynia, Solzhenitsynin, Solzhenitsyn, and Solzhenitsyneille".
- Their claim "This is a clear case where techniques like stemming or n-gramming help retrieval effectiveness" (p. 47) is **not backed by a reported per-topic number** for the stemmed or n-gram runs.

### Internal inconsistencies found

1. **Printed relative changes that do not match the printed MAPs.** We computed the range of relative change allowed by 4-decimal rounding of both MAPs **[computed]**:
   - Table 6, English 4-gram: printed +7.3%, allowed 7.44–7.49%;
   - Table 6, Finnish 4-gram: printed +37.4%, allowed 38.89–38.99%;
   - Table 7, Finnish 5-gram-stem: printed +20.8%, allowed 18.92–18.99%;
   - Table 7, French 4-gram-stem: printed −6.4%, allowed −6.69 to −6.65%.
   One further cell (Table 6 German 4-gram +20.3 vs 20.38–20.43) is consistent only with truncation rather than rounding. (Table 2 Finnish +23.4 vs 23.43–23.54 is consistent with rounding at the lower edge of the range, so it is not counted.) Which number (MAP or %) is wrong cannot be decided from the paper. The qualitative conclusions do not change.
2. **Column reference:** Sec. 4.1 calls the stemmed MAPs "Column 3 in Table 3" (p. 38), but Sec. 4.2 calls the lemmatized MAPs "the fourth column" (p. 40). Under the same counting they are in column 5.
3. **Year slip:** Sec. 6.1 speaks of "all eight CLEF 2003 languages" (p. 46), while all experiments use the CLEF 2002 topics.
4. **Bold marking:** Table 4's bold marks the best score *within Table 4*, not per language overall (e.g., Finnish 0.3633 is bold, while 0.3935 in Table 7 is higher). This is a presentation issue, not an error.

## 10. Statistical evidence

- **Significance test:** one-tailed bootstrap (1,000 samples), 95% and 99% levels, always against the table's reference run (pp. 35–36). Exact p-values and CI limits: **NOT_REPORTED**. Correction for multiple comparisons: none reported, despite several dozen tests.
- **Confidence intervals:** used internally for the test; **not reported**.
- **Runs / seeds:** deterministic system; single run per condition. Not applicable in the usual sense.
- **Ablation:** the design itself is a factorial-like ablation of representation steps (diacritics; stem; lemma; split; n-gram length; n-grams on words/stems/lemmas). Not ablated: PRF on/off, the expansion-term budget, stop-word removal on/off, and the splitter thresholds.
- **Per-query analysis:** Table 9 only, for the **word-based run**: 10 of 28 eligible topics, compared across **languages**. There is no per-topic comparison between representations. The following are absent:
  - win/loss counts;
  - overlap of retrieved relevant documents between representations;
  - unique relevant hits;
  - oracle union;
  - query-feature regression.
  Query features appear only qualitatively: proper names vs general high-frequency terms, and inflected name variants in Finnish.

## 11. Strengths

- Strong control within a language: the same engine, weighting, PRF settings (up to the n-gram expansion-budget caveat), stop-word source, sanitizing and topics across all representations.
- Broad representation space: raw ± diacritics, stem, lemma, decompounding, split+stem, and 4/5/6-grams over words, stems and lemmas.
- Eight languages with translated identical topics, which allows cross-language comparison of *which* representation wins.
- A significance test at every comparison, with the direction and level marked.
- Explicit testing of two "uniform best strategy" hypotheses, with a clear negative answer for the 4-gram hypothesis in Spanish.
- A clearly specified, reproducible compound-splitting algorithm (Fig. 1 and thresholds).

## 12. Limitations

### Stated by the authors

- Stemmer rule sets "may differ in quality between the languages" and "subtle differences between the runs remain" (p. 38).
- Lemmatizers were available only for EN/FR/DE/IT (pp. 39–40).
- Finnish scores are low, which "may be due to the small size of the Finnish collection" (p. 37). The Finnish collection covers only 30 topics (p. 46).
- The compound-part weighting (independent tf.idf for the compound and its parts) "seems overly simplistic" (p. 42).
- Topic-wise analysis is limited: "A full-fledged exposition of this type of analysis requires a full paper in its own right" (p. 46); "predicting the difficulty of topics is notoriously hard" (p. 47).
- Language-family typology does not predict which method works; finer features are needed, e.g. the extent of compounding and the indices of synthesis/fusion (pp. 47–48).
- n-gram indexes are much larger (cited, p. 43).

### Inferred from the experimental design

1. **PRF confound.** Every run uses Rocchio blind feedback, so each MAP reflects *representation + PRF*. The n-gram runs may additionally use up to 100 expansion terms instead of 20, for unspecified runs (p. 35). Gains of n-grams over words are therefore not purely representational.
2. **Not BM25; single retrieval model.** Lnu.ltc vector space only. Results may not transfer quantitatively to BM25 or language-model retrieval.
3. **Different topic sets per language.** Finnish has 30 topics, English excludes at least 2, and the other counts are not given. Cross-language comparisons of MAP levels, and our unweighted means, are only indicative.
4. **Many tests, no multiplicity control.** Some individual △ marks may be false positives.
5. **Lemma vs stem is tool-specific.** TreeTagger (inflection only, POS unused, unknown-word policy not reported) vs Snowball. It cannot be generalized to "lemmatization < stemming".
6. **No parameter-selection protocol.** The fixed parameters are presumably carried over from the authors' CLEF work; no dev/test separation is described.
7. **The per-topic analysis is descriptive and single-representation.** It cannot show whether different representations retrieve different relevant documents.
8. **The cross-language robustness claim is not quantified.** The authors say per-topic scores "across multiple languages tend to be more robust" (p. 46). Yet Table 9 shows very wide cross-language ranges for the same topic (e.g., Topic 111: 0.0001–0.5453; Topic 94: 0.0158–0.9500 **[computed]**), and no correlation statistic is given.

## 13. What the work proves

Within the setting (CLEF 2002, T+D topics, Lnu.ltc + Rocchio PRF, MAP):

- **Diacritic mapping** improves MAP in all 8 languages, significantly in 5 (NL, FR, IT, ES, SV) (Table 2).
- **Snowball stemming** never hurts MAP here (+1.2% to +30.0%). It is significant for Finnish (▲), Spanish (▲) and German (△) (Table 3).
- **TreeTagger lemmatization** is below Snowball stemming in all 4 languages where both were run, and significantly above the word baseline only for German (Table 3).
- **Compound splitting** (keep the compound + add parts) improves MAP in all four compound-rich languages, significantly only for FI and DE alone and only for DE and SV on top of stemming (Table 4); combined with stemming it gives +4.8% (NL) to +42.8% (FI) **[computed]** over words (Table 4).
- **Word 4-grams** improve MAP in all 8 languages, significantly in FI, DE, IT and SV (Table 6). n-grams over stems help FI, DE and SV but significantly hurt EN, FR, IT and ES in some settings (Table 7).
- **The best representation differs by language** and does not follow language families (Table 10; p. 47). In Finnish (agglutinative: our characterization; the paper classifies it only as Finno-Ugric, p. 47), the gains from normalization and n-grams are the largest (stem+5-gram: 0.3935 vs 0.2545).
- Only "4-gram words is best" is refuted, and only for Spanish; "split, then stem" is never significantly beaten (p. 49).

## 14. What the work does NOT prove

- **Anything about BM25.** The retrieval model is Lnu.ltc; effect sizes under BM25 are unknown.
- **Anything about dense/semantic retrieval or hybrid retrieval.** Neither exists in the paper. The "combinations" (stem → n-gram, split → stem) are sequential index pipelines, not the fusion of two retrieval channels.
- **That different representations retrieve different relevant documents** (complementarity between lexical variants). No overlap, unique-hit, oracle-union or per-topic comparison between representations is reported.
- **That lemmatization is inferior to stemming in general.** The result holds for one lemmatizer–stemmer pair, with PRF, on four languages.
- **That n-gram gains are purely representational.** PRF expansion budgets differ for some n-gram runs.
- **That stemming or n-grams fix Finnish Topic 94.** This is asserted (p. 47) without the per-topic number.
- **What predicts which representation wins.** Typology is discussed only as a proposal (Pirkola's synthesis/fusion indices, p. 48); no query-level or language-level predictor is tested.

## 15. Relationship to current Uzbek evidence

- **No Uzbek or Turkic data.** Finnish (agglutinative, rich case morphology, long words) is the closest analogue. Its pattern agrees with the Turkish evidence already in the index:
  - morphological normalization gives large gains over surface forms (MORPH-001 Can et al. 2008; MORPH-002 Haddad & Bechikh Ali 2014);
  - simple length-based or n-gram methods are competitive with linguistic tools (compare MORPH-002: 4/5-prefix truncation is highly competitive).
- **Lemma is not automatically best.** The same conclusion appears in MORPH-001 (Can et al. 2008) and in Airio 2006 (CR000491, stem ≥ lemma without decompounding). This paper adds a multi-language, significance-tested instance.
- **Graphic normalization matters on its own.** Diacritic mapping gives up to +23.4% MAP (FI, not significant); the largest significant gains are +19.3% (SV) and +18.4% (FR) (Table 2). The Uzbek analogue is apostrophe variants in oʻ/gʻ (ʻ ' ‘ ’) and Latin/Cyrillic script. The v0.8 candidate query features and the optional `BM25_simple-normalization` control already point there.
- **Inflected proper names.** The Finnish Solzhenitsyn example (p. 47) mirrors Uzbek case-inflected names (e.g., *Toshkentda*, *Toshkentga*; our example, not from the paper). The v0.8 query-feature list already contains "named entities".
- **Uzbek national works** (Bakaev, Xusainova, Elov; MORPH-UZ-*) provide stemmers and lemmatizers but no qrels-based IR comparison. This paper is the kind of controlled lexical-representation experiment those works lack, but it is for other languages.

## 16. Relationship to CURRENT_GAP

**Classification:** *supports (background)* + *no material effect on the residual core*.

- **Supports** these v0.8 premises:
  - "raw/stem/lemma have already been compared" (listed as a non-claim), here in 8 European languages with a significance test;
  - "do not assume a fixed order of representations": the best representation is language-dependent; lemma < stem here;
  - the motivation for graphic-normalization and named-entity query features.
- **No material effect on the residual core.** None of the following v0.8 elements is present:
  - BM25 variants × a **fixed dense retriever D**;
  - unique relevant hits / overlap between lexical and dense channels;
  - oracle union;
  - incremental hybrid gain;
  - the relation of complementarity changes to query features.
- **Triage flag correction (proposal).** `carries_complementarity_evidence = YES` overstates the paper. Table 9 is per-topic AP of one representation across languages. It is evidence of **topic-difficulty variation**, not of complementarity between representations or channels. We propose recoding it to NO (or "partial: per-topic AP, single representation").
- **Possible new direction (minor, proposal only).** The paper shows that character n-grams are a strong knowledge-poor lexical representation for agglutinative/compounding languages. An open question for our design is whether a `BM25_ngram` channel changes the lexical–dense overlap differently from stem/lemma. Character n-grams are closer in form to the subword units of dense tokenizers (our hypothesis, not from the paper). This would extend, not change, the v0.8 logic `raw → stem → lemma`.

**Proposal:** keep v0.8 refined unchanged. Optionally cite this paper in the evidence boundary as a classic multi-language, significance-tested raw/stem/lemma/decompounding/n-gram comparison with no BM25, dense or fusion. `CURRENT_GAP.md` has not been edited.

## 17. Implications for our research design

- **Lexical variants.** Keep `BM25_raw / BM25_stem / BM25_lemma` as the core. Consider two controls motivated by this paper:
  - `BM25_simple-normalization` (apostrophe/script unification only, the analogue of diacritic mapping);
  - `BM25_char-ngram` (4- or 5-grams within words, the language-independent option).
  Pre-register which n is used, or choose it on dev only, because the best n varies by language (Table 6).
- **Normalization before morphology.** Apply graphic normalization identically in all variants. In the paper, diacritic mapping precedes stemming in every run, so its effect is separated (Table 2). Report the raw-with-original-graphics run separately.
- **PRF / query expansion.** Either disable PRF for the main raw/stem/lemma × D comparison or apply an identical budget to all variants. This paper shows how an unequal budget (20 vs 100 terms) blurs attribution.
- **Lemma vs stem tools.** Document for each Uzbek tool:
  - whether it removes only inflection (as TreeTagger here, p. 40) or also derivational affixes;
  - how unknown words are handled;
  - where lowercasing and apostrophe normalization happen (the paper lowercases *after* lemmatizing; p. 35).
- **Compound handling.** Uzbek has fewer closed compounds than German or Swedish. The paper's "keep original + add parts" expansion design is a useful pattern if we test lemma+surface (expanding) vs lemma-only (replacing) representations.
- **Metrics.** MAP alone hides channel overlap. Keep per-query AP/nDCG plus Recall@k and set-based unique-hit/overlap measures, as v0.8 already requires.
- **Topic set.** Report the number of evaluated queries per condition. Avoid comparing conditions over different query subsets; here Finnish had 30 topics.
- **Significance.** Use per-query paired tests (bootstrap or randomization) with a multiplicity correction or pre-registered primary contrasts. The paper runs dozens of uncorrected tests.
- **Query taxonomy.** Proper names vs general high-frequency terms (Table 9) is a cheap, interpretable query feature. Include it, together with an "inflected named entity" flag, in the v0.8 feature list.

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| Monolingual retrieval | Query and documents are in the same language | Ad hoc retrieval within one language collection |
| CLEF | European evaluation campaign modelled on TREC | Test collections with topics, documents and pooled qrels per language |
| Topic (T/D/N) | A written information need with title, description and narrative | TREC-style topic; this paper uses T+D |
| Vector space model, Lnu.ltc | Documents and queries as weighted word vectors; score = similarity | SMART weighting with pivoted length normalization (slope 0.2) |
| Blind feedback (Rocchio PRF) | Assume the top results are relevant and add their words to the query | Rocchio reweighting using top-10 as relevant and bottom-500 as non-relevant |
| Stemming (Snowball) | Chop word endings by rules; may produce non-words | Rule-based affix stripping |
| Lemmatization (TreeTagger) | Replace a word with its dictionary form | Lexicon-based lemma lookup (inflection only here) |
| Compound splitting | Split *bahnhof* into *bahn* + *hof* and index them too | Lexicon/frequency-based decompounding with linking elements |
| Linking element | A connecting sound/letter between compound parts (German -s-) | Interfix / *Fugenmorphem* |
| Character n-gram | Overlapping letter chunks of length n used as index terms | Sliding window of n characters, within or across word boundaries |
| Diacritic mapping | Treat *ä* as *a* | Character normalization before indexing |
| MAP | Average of how early the relevant documents appear, over topics | Mean of per-topic average precision |
| Bootstrap test | Resample topics many times to see whether an improvement is reliably > 0 | Non-parametric CI-based one-tailed test |
| Complementarity (project term) | Each channel or representation finds relevant documents the other misses | Unique relevant hits, overlap, oracle-union gain |

## 19. Open questions / verification needed

1. ~~Issue number, DOI and page confirmation~~ Resolved by the verifier pass: the Springer page gives vol. 7, issue 1 (Jan 2004), pp. 33–52, DOI as in §1.
2. **Four inconsistent "% change" cells** (Table 6 EN and FI 4-gram; Table 7 FI 5-gram-stem and FR 4-gram-stem): is the MAP or the percentage correct? Not decidable from the paper.
3. **Which n-gram runs used the 100-term expansion budget?** NOT_REPORTED. This affects the attribution of the n-gram gains.
4. **Number of evaluated topics per language** (other than Finnish = 30): NOT_REPORTED.
5. **Collection sizes and qrels procedure:** in Braschler & Peters (same special issue). A separate record may exist in our corpus; check before citing sizes.
6. **TreeTagger unknown-word handling:** NOT_REPORTED. It may explain lemma < stem.
7. **Cross-reference:** the Airio 2006 card (CR000491) asks whether its cited "Hollink et al." is this paper. That should be checked in Airio's reference list, not here.
8. **Per-topic representation comparison:** the authors' FlexIR runs are not public in the paper. Nothing further can be extracted about overlap between representations.

## 20. Decision after deep dive

- **Keep current gap?** Yes. v0.8 refined remains valid (§16).
- **Modify gap?** No change proposed. Optionally add this paper to the evidence-boundary list as a classic, significance-tested multi-language representation comparison without BM25, dense or fusion (researcher's decision).
- **Triage correction (proposal):** recode `carries_complementarity_evidence` for CR000338 from YES to NO / partial (per-topic AP of a single representation only).
- **Add decision?** Proposed for `decisions/DECISIONS.md` (researcher's decision):
  - "Graphic normalization (apostrophe/script) is applied identically before every morphological variant and is also reported as its own control condition";
  - "PRF/query expansion is either disabled in the main morphology × D comparison or applied with an identical budget to all variants".
- **Add experiment?** Optional: a `BM25_char-ngram` lexical variant (n chosen on dev) as a language-independent control in the raw/stem/lemma × D overlap analysis.
- **Add citation to Chapter I?** Yes:
  - §1.1 (lexical retrieval: morphological normalization, decompounding and character n-grams as alternative index-term representations; language-dependent effects; lemma is not automatically better than stem);
  - §1.3 briefly, as an example of classic morphology studies that do not analyse cross-representation or cross-channel complementarity.
- **Proposed `MASTER_INDEX.md` row** (to add after approval):

| MORPH-032 | Hollink, Kamps, Monz, de Rijke — *Monolingual Document Retrieval for European Languages* (*Information Retrieval* 7, 33–52) — [deep dive](deep-dives/2004_Hollink_Kamps_Monz_deRijke_Monolingual_Retrieval_European_Languages.md) | 2004 | A | HIGH | CLEF 2002, 8 European languages, T+D topics, FlexIR Lnu.ltc vector space + Rocchio PRF, MAP with bootstrap tests. Word ± diacritics vs Snowball stem vs TreeTagger lemma (4 langs) vs compound splitting (NL/FI/DE/SV) vs character 4/5/6-grams over words/stems/lemmas. Diacritic mapping and stemming improve all 8 languages (stem significant FI +30.0%, ES, DE); lemma < stem in all 4 languages tested; word 4-grams improve all 8; best run varies by language (Finnish stem+5-gram 0.3935 vs 0.2545). No uniform best strategy. Per-topic AP only for the word-based run across languages. No BM25, no dense, no fusion, no overlap/unique-hit analysis; 4 printed % changes inconsistent with the MAPs. |
