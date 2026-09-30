# Airio (2006): Word normalization and decompounding in mono- and bilingual IR

**Targeted deep-dive status:** COMPLETED (AI-assisted, pending researcher review)
**Completed:** 2026-09-28
**Literature ID:** `MORPH-027` (assigned 2026-09-28, approved by researcher)
**Systematic-review record:** `CR000491`. Full-text triage: INCLUDE, reading priority HIGH, reading tier "2 — важно", `carries_complementarity_evidence = YES` (see §10 and §16: in this card we qualify this as *qualitative, lexical-vs-lexical per-topic variation only*).
**Provenance:** AI-assisted deep dive (Claude). The paper (23 PDF pages, printed pp. 249–271) was read in full from the pdftotext extraction. Page images were checked for every table, figure and appendix number reported here: printed pp. 256 (Table 1), 258 (Table 2, Fig. 1), 259 (Figs. 2–3), 262 (Table 3, Fig. 4), 263 (Figs. 5–6), 264 (Fig. 7), 266–270 (Conclusions, Appendix Examples 1–18) = PDF pp. 8, 10, 11, 14, 15, 16, 18–22. Every number below comes with its table/section and printed page. Numbers computed by us are marked **[computed]** (recomputed with Python).
**Source rule:** **the paper is the primary and only authoritative source.** No code, website or later paper was used for claims about the author's work. The record below is taken from the PDF's own running header and first page; the issue number (3) and publication dates were later verified via the Crossref record for the DOI (verifier pass).
**Verification:** independent AI verifier pass 2026-09-28; 10 findings addressed.
**Reliability:** **A** (peer-reviewed journal article, *Information Retrieval*, Springer, 2006; received 11 June 2004, revised 3 January 2005, accepted 1 February 2005, p. 249).

---

## Кратко для исследователя (RU)

- **Что сделано.** Классическое контролируемое сравнение вариантов лексического представления на CLEF 2003 (60 тем, система InQuery, MAP):
  - индексы: словоформы (inflected), стемминг Snowball, лемматизация TWOL без разбиения композитов, лемматизация TWOL с разбиением композитов (decompounding);
  - одноязычный поиск для английского, финского, шведского, немецкого (15 прогонов) и двуязычный словарный поиск EN→FI/SV/DE (9 прогонов).
- **Главные числа, одноязычный поиск** (Table 3, p. 262; MAP в %):
  - финский: словоформы 31.0 → лемма+split 50.5 (+62.9%), стемминг 48.5 (+56.5%), лемма без split 47.0 (+51.6%);
  - шведский: 30.2 → 38.8 / 33.5 / 31.4; немецкий: 30.2 → 36.2 / 35.7 / 31.9;
  - английский: 43.4 → стемминг 46.3, лемма 45.6 (различия незначимы).
- **Главные числа, двуязычный поиск** (Table 2, p. 258): лемма+split лучше везде (FI 35.5, SV 27.1, DE 31.0); стемминг FI 20.8 (−41.4% от лемма+split).
- **Стемминг ≈ лемматизация** (без разбиения композитов) в одноязычном поиске: стемминг даже чуть лучше во всех 4 языках. Основной выигрыш лемматизатора даёт именно decompounding, т.е. расширение индекса частями композитов.
- **Есть разбор по отдельным запросам, но только качественный:** автор пишет, что «худший» в среднем прогон может быть лучшим на отдельной теме; все темы, где стемминг обошёл лемматизацию, содержали слова, не распознанные лемматизатором (например, иностранные имена; утверждение относится к одноязычным прогонам, p. 265). Нет подсчёта выигрышей/проигрышей, нет перекрытия найденных релевантных документов, нет oracle union.
- **Чего нет (измерения gap):** BM25 нет (InQuery); плотного/нейросетевого поиска нет; fusion/гибрида нет (ни лексико-семантического, ни между вариантами морфологии); overlap/unique hits нет; признаки запросов только в виде примеров.
- **Внутренние несоответствия в статье:**
  - Выводы (p. 266) и Discussion (p. 265) утверждают, что без decompounding стемминг и лемматизация работают «почти одинаково во всех двуязычных прогонах», но в EN→FI 29.0 vs 20.8 (−28.3%), и сам автор называет это различие значимым (p. 258);
  - вывод «decompounding значимо лучше в двуязычном поиске» (p. 266) не выполняется для EN→FI (35.5 vs 29.0 названо незначимым, p. 258);
  - аннотация «почти так же хорошо» для лемма без split vs лемма+split в одноязычном поиске, хотя для немецкого различие значимо, а для шведского −19.1%;
  - в тексте p. 265 ссылка на «Examples 11 and 12» для шведской темы 197 (правильно — 13 и 14); мелкое расхождение округления (−7.0 vs −6.9 [computed] из округлённых MAP; может объясняться неокруглёнными значениями, т.е. не обязательно ошибка); «2.0% better» — это процентные пункты, а не проценты.
- **Для нашего gap:** работа поддерживает фон (морфологическое представление меняет результаты по-разному для разных запросов; значимы признаки «композит», «нераспознанное слово/имя», ошибки стемминга), но ядро v0.8 (raw/stem/lemma BM25 × фиксированный D → overlap/unique hits → прирост гибрида) **не затрагивает**. Предложение: gap не менять.
- **Практическая польза для нас:**
  1. для BM25_lemma заранее зафиксировать политику для слов, не распознанных анализатором (оставить как есть / стеммировать), и считать долю таких слов в запросе как признак запроса;
  2. стоп-слова применять одинаково во всех условиях: по примерам в приложении видно, что в финских стеммированных запросах остаются служебные слова, отсутствующие в лемматизированных (наш вывод);
  3. различать «замещающее» представление (stem/lemma вместо словоформы) и «расширяющее» (словоформа + части/лемма), как decompounding здесь;
  4. явно фиксировать правило токенизации для апострофов и дефисов (у автора «punctuation marks were deleted»).

---

## 1. Bibliographic record

- **Author:** Eija Airio
- **Affiliation:** Department of Information Studies, University of Tampere, Finland (p. 249)
- **Year:** 2006
- **Venue:** *Information Retrieval* (Springer; running header "Inf Retrieval (2006) 9:249–271")
- **Volume / pages:** 9, pp. 249–271
- **Issue:** 3 (print June 2006; online 5 June 2006); not printed in the PDF, verified via Crossref record for the DOI
- **DOI:** `10.1007/s10791-006-0884-2` (printed on p. 249)
- **Official URL:** https://doi.org/10.1007/s10791-006-0884-2 (constructed from the printed DOI; not opened)
- **Publisher:** Springer Science + Business Media, LLC 2006
- **Dates:** received 11 June 2004; revised 3 January 2005; accepted 1 February 2005 (p. 249)
- **Source type:** peer-reviewed journal article
- **Reliability:** A
- **Full text available:** yes (`07_full_text/pdfs/CR000491.pdf`, 23 pages)

## 2. Why this work matters to the PhD

A clean, older, peer-reviewed example of the **lexical-representation axis** of our design: the same collection, the same retrieval engine and the same topics are indexed in several morphological representations (inflected / stem / lemma / lemma + decompounding), and the results are compared by MAP with a paired test, plus a qualitative per-topic analysis of *why* representations win or lose on individual topics.

| Axis | Relation |
|---|---|
| Lexical retrieval | **Central.** Four index representations in InQuery; stemming (Snowball) vs lemmatization (TWOL) vs decompounding |
| Semantic retrieval | **Absent** |
| Hybrid retrieval | **Absent.** No fusion of any kind (not even across the morphological variants) |
| Uzbek morphology | Indirect. Finnish is the closest analogue among the four languages (see §15); no Turkic language |
| Low-resource retrieval | No. All four languages had commercial lemmatizers and CLEF test collections in 2003 |
| Current gap | Touches the `raw → stem → lemma` element and (qualitatively) query features; does not touch dense D, fusion, overlap/unique hits or hybrid gain (§16) |

## 3. Research problem

### Simple explanation

A word can appear in many inflected forms; if the query has one form and the document another, exact matching fails. Two families of tools reduce forms to a common one: **stemmers** (cut endings by rules; the result need not be a real word) and **lemmatizers** (use a dictionary and rules to return the dictionary form). Lemmatizers can also split compound words (Finnish *tiedonhaku* → *tieto* + *haku*). The paper asks which of these gives better retrieval, in one's own language and when English queries are translated into another language by dictionary.

### Formal formulation

Research questions (Sec. 5.1, p. 255, verbatim):

1. "Does monolingual retrieval with normalization give significantly better results than retrieval without normalization?"
2. "Which gives better results in monolingual runs, retrieval with stemming in the stemmed index, retrieval with lemmatization in the lemmatized compound index or retrieval with lemmatization in the lemmatized decompounded index?"
3. "Which gives better results in bilingual runs, retrieval with stemming in the stemmed index, retrieval with lemmatization in the lemmatized compound index or retrieval with lemmatization in the lemmatized decompounded index?"

Task: ad hoc document retrieval, CLEF 2003 newspaper collections; effectiveness = non-interpolated average precision averaged over topics (MAP).

## 4. Main idea

### Simple explanation

Build four versions of each newspaper index (word forms as written; Snowball stems; TWOL lemmas; TWOL lemmas plus the parts of compounds), process the queries the same way, run the same search engine, and compare the average precision. For cross-language runs, English topics are lemmatized, translated word by word with a dictionary, then stemmed or lemmatized to match the target index.

### Concrete example

From the paper (Sec. 6.2, pp. 263–264; Appendix Examples 11–12, p. 269):

- Finnish topic 147 contains *lintu* ("bird"). Some relevant documents contain "bird" only inside compounds: *lintuparvi* ("a flock of birds"), *lintuvahinko* ("a bird accident").
- The lemmatized **decompounded** index holds *lintuparvi*, *lintu* and *parvi*, so the query word *lintu* matches: AP = 41.8%.
- The lemmatized compound index holds only *lintuparvi*: AP = 2.0%.
- The stemmed index: AP = 16.8%; the author attributes the stemmed run's advantage over the compound index to under-stemming "which happens to be advantageous in this topic" (p. 264).

A counter-example (Examples 17–18, p. 270): Finnish topic 185 contains *Srebrenicasta*, *Srebrenicassa*. The lemmatizer does not recognize the name and leaves the inflected strings as such, so they do not match *Srebrenica* in documents (lemmatized AP 50.0% with and without decompounding). The stemmer reduces all forms to *srebrenic*: AP = 100.0%.

### Formal method

- Retrieval engine: InQuery (p. 256). Queries are structured with `#sum` over `#syn` groups (Appendix; Sec. 5.3, p. 257: "target words derived from the same source word are grouped into the same synonym group").
- Context (not from the paper): InQuery is an inference-network retrieval system; `#syn` treats its arguments as one term, `#sum` averages the beliefs of its arguments. The paper gives no ranking formula or parameters.
- Representation variants per language `L` (Sec. 5.3, p. 256): `I_infl(L)`, `I_stem(L)`, `I_lemma-nosplit(L)`, `I_lemma-split(L)` (no split index for English). Query words are processed with the same tool as the index.

## 5. Architecture / algorithm

1. **Tokenization for all indexes** (Sec. 5.3, p. 256, verbatim): "First, punctuation marks were deleted. Next, strings broken down by the space character were decoded to be indexable words. Capitals were converted into lower case letters before indexing."
2. **Stemmers:** Snowball stemmers (Porter) for English, German, Finnish, Swedish, described as "algorithmic and simple. They do not utilize any dictionaries or exception lists" (p. 256).
3. **Lemmatizers:** Lingsoft TWOL two-level lemmatizers (ENGTWOL, FINTWOL, GERTWOL, SWETWOL). They "give all the possible base forms for a given inflected word and are capable of splitting compounds" (p. 256).
   - Handling of ambiguous lemmas in the index (all readings vs one): **NOT_REPORTED** explicitly. Query-side handling of multiple readings is also not stated; UTACLIR's lemmatizer "produces one or more basic forms for a token" (p. 257). (The `#syn` group "#syn(maalliset jäännökset tähteet)" in Example 7 holds alternative dictionary translations of *remains*, p. 261, not lemma readings.)
   - Unrecognized words: "The simplest approach is to leave the word as such. We applied this approach in our monolingual runs." (p. 264). The Appendix marks such words with `@` (e.g. "#syn( dayton @dayton)", Example 13); the meaning of `@` is not explained (our reading).
4. **Decompounded index:** contains "the whole compound as well as parts in their base form" (p. 260). This is **index augmentation**, not replacement.
5. **Stop-word lists** (p. 256): English 429 (from InQuery's default list), Finnish 773 and German 1318 ("created on the basis of the English stop list"), Swedish 499 (created at UTA). When and on which form (surface / stem / lemma) stop-words are removed is **NOT_REPORTED** for monolingual runs; for UTACLIR, "After normalization, stop-words are removed" (p. 257).
6. **Indexes:** 15 in total: 4 each for Finnish, German, Swedish; 3 for English (no English decompounding tool) (p. 256).
7. **Runs:** 24 (p. 257): 15 monolingual (inflected, stemmed, lemmatized-compound for all four languages, plus lemmatized-decompounded for FI/SV/DE); 9 bilingual (EN→FI/SV/DE × {lemma-split, lemma-nosplit, stem}).
8. **Bilingual pipeline (UTACLIR)** (p. 257): English topic words lemmatized → stop-words removed → dictionary translation (Motcom GlobalDix: 44,000 English entries; 26,000 Finnish, 39,000 German, 36,000 Swedish, p. 255) → translations normalized with the target stemmer or lemmatizer → structured query with `#syn`. No English phrase recognition (p. 257).
9. **Topic fields used** (title / description / narrative): **NOT_REPORTED**. The Appendix queries contain phrasing words (Finnish *etsiä*, *kertoa*; Swedish *leta*, *efter*, *rapport*), which suggests more than the title field was used (our inference).

## 6. Data

- **Dataset / corpus:** CLEF 2003 newspaper collections (Table 1, p. 256; checked on page image):

| Language | Source | Documents | Size (MB) |
|---|---|---:|---:|
| English | Los Angeles Times 1994, Glasgow Herald 1995 | 169,477 | 579 |
| Finnish | Aamulehti 1994–1995 | 55,344 | 137 |
| German | Rundschau 1994, Der Spiegel 1994–1995, SDA German 1994–1995 | 294,809 | 668 |
| Swedish | Tidningarnas Telegrambyrå 1994–1995 | 142,819 | 352 |

- **Queries:** "60 CLEF 2003 topics, translated into all the CLEF languages" (p. 256). Topic IDs cited in the paper: 147, 152, 174, 183, 184, 185, 186, 187, 197.
- **Number of topics actually evaluated per language:** **NOT_REPORTED.** Context (not from the paper): in CLEF, topics without relevant documents in a given collection are normally excluded, so the effective count per language may be below 60.
- **Relevance judgments:** CLEF 2003 relevance assessments (p. 256). Pooling depth, grading: NOT_REPORTED (standard CLEF binary judgments — context, not from the paper).
- **Train / dev / test:** none; no parameters are tuned (no tunable parameters are described).
- **Domain:** news.

## 7. Baselines

| Baseline | What it is | Why selected | Fair comparison? |
|---|---|---|---|
| Monolingual: inflected word-form index | No normalization; topic words "added as such into the query" (p. 257) | Standard no-normalization reference (p. 250) | **Mostly yes.** Same engine, topics, tokenization. Stop-word handling across conditions is not documented (see §12) |
| Bilingual: lemmatized + decompounded index | TWOL-lemmatized decompounded index; translated query words lemmatized (p. 257) | Designated baseline (p. 250); inflected retrieval "is not practical" with a base-form dictionary (Sec. 4.3, p. 255) | Yes as a reference; there is no inflected bilingual run by design |
| Stemmed (Snowball) | Rule-based suffix stripping | Most common IR normalization (p. 250) | Yes; a simple generic stemmer vs a commercial lexicon-based lemmatizer, which the author acknowledges (p. 266) |
| Lemmatized, compound index | TWOL lemma, compounds kept whole | Isolates lemmatization from decompounding | Yes; the decompounded vs compound contrast is the cleanest comparison in the paper |

No other retrieval model (e.g., BM25 / Okapi, language models) is compared.

## 8. Metrics

| Metric | Definition | Simple meaning | Appropriate? |
|---|---|---|---|
| Non-interpolated average precision, averaged over topics (MAP), in % | For each topic: mean of precision at the rank of each relevant document (unretrieved relevant documents count 0); then mean over topics | "How high, on average, are all the relevant documents?" | Yes: the standard CLEF measure |
| "Diff. %" (Tables 2–3) | Absolute difference in AP percentage points | Points of MAP | Yes; but the text sometimes calls points "%" (§9) |
| "Change %" (Tables 2–3) | Relative change = Diff / reference MAP × 100 | Relative improvement | Yes |
| PR curves (Figs. 1–7) | Precision at 11 recall levels (0–1 in steps of 0.1, as plotted); interpolation method not stated | Shape of precision over recall | Supporting only; no numbers extracted from figures in this card |
| Wilcoxon signed ranks test, 0.01 level | Paired non-parametric test on per-topic AP differences | "Is one run reliably better across topics?" | Yes |

## 9. Results

### Table 2: bilingual runs, source language English (p. 258; checked on page image)

| Target | Index type | MAP % | Diff. vs lemma+split | Change % vs lemma+split | Diff. vs lemma nosplit | Change % vs lemma nosplit |
|---|---|---:|---:|---:|---:|---:|
| Finnish | lemmatized + split | **35.5** | | | | |
| Finnish | lemmatized, nosplit | 29.0 | −6.5 | −18.3 | | |
| Finnish | stemmed | 20.8 | −14.7 | −41.4 | −8.2 | −28.3 |
| Swedish | lemmatized + split | **27.1** | | | | |
| Swedish | lemmatized, nosplit | 17.4 | −9.7 | −35.8 | | |
| Swedish | stemmed | 19.0 | −8.1 | −29.9 | 1.6 | 9.2 |
| German | lemmatized + split | **31.0** | | | | |
| German | lemmatized, nosplit | 26.4 | −4.6 | −14.8 | | |
| German | stemmed | 25.7 | −5.3 | −17.1 | −0.7 | −2.7 |

All derived columns recomputed **[computed ✓]**: −18.31, −41.41, −28.28; −35.79, −29.89, +9.20; −14.84, −17.10, −2.65.

Significance (Wilcoxon, 0.01 level; p. 258):
- EN→SV and EN→DE: lemma+split vs lemma-nosplit significant; lemma-nosplit vs stemmed **not** significant.
- EN→FI: "the situation is opposite": lemma+split vs lemma-nosplit **not** significant; lemma-nosplit vs stemmed significant.
- All three languages: stemmed vs lemma+split significant.

Other numbers:
- 42 phrases found among the English topics, only one (*fast food*) translatable with the dictionary; 7 "customary" (e.g. *mobile phone*) and 35 ad hoc (p. 257).
- Bilingual as a share of monolingual MAP **[computed]**: lemma+split FI 70.3%, SV 69.8%, DE 85.6%; stemmed FI 42.9%, SV 56.7%, DE 72.0%.

### Table 3: monolingual runs (p. 262; checked on page image)

| Language | Index type | MAP % | Diff. vs inflected | Change % vs inflected | Diff. vs lemma+split | Change % vs lemma+split |
|---|---|---:|---:|---:|---:|---:|
| English | inflected | 43.4 | | | | |
| English | lemmatized, nosplit | 45.6 | +2.2 | +5.1 | | |
| English | stemmed | **46.3** | +2.9 | +6.7 | +0.7 | +1.5 |
| Finnish | inflected | 31.0 | | | | |
| Finnish | lemmatized + split | **50.5** | +19.5 | +62.9 | | |
| Finnish | lemmatized, nosplit | 47.0 | +16.0 | +51.6 | −3.5 | −7.0 |
| Finnish | stemmed | 48.5 | +17.5 | +56.5 | −2.0 | −4.0 |
| Swedish | inflected | 30.2 | | | | |
| Swedish | lemmatized + split | **38.8** | +8.6 | +28.5 | | |
| Swedish | lemmatized, nosplit | 31.4 | +1.2 | +4.0 | −7.4 | −19.1 |
| Swedish | stemmed | 33.5 | +3.3 | +10.9 | −5.3 | −13.7 |
| German | inflected | 30.2 | | | | |
| German | lemmatized + split | **36.2** | +6.0 | +19.9 | | |
| German | lemmatized, nosplit | 31.9 | +1.7 | +5.6 | −4.3 | −11.9 |
| German | stemmed | 35.7 | +5.5 | +18.2 | −0.5 | −1.4 |

Recomputation **[computed]**: all values match to rounding except Finnish lemma-nosplit vs lemma+split: printed −7.0, computed −3.5/50.5 = **−6.93** (rounds to −6.9); the printed −7.0 is consistent with unrounded MAPs, so this is not demonstrably an error. For English, the last two columns are relative to the lemma-nosplit run (45.6), since no split run exists: +0.7 / 45.6 = +1.54 ✓. The column header ("from the lemm. split.run") does not say this.

Significance (p. 261–262):
- All non-English normalized runs vs inflected: significant (Wilcoxon, 0.01), **except** German lemma-nosplit vs inflected.
- English: "no statistically significant differences could be found between the inflected run and the normalized runs" (p. 261).
- Swedish lemma+split vs stemmed: significant (0.01). German lemma+split vs lemma-nosplit: significant.
- "There are no statistically significant differences between the runs with various normalization types in other test languages." (p. 262). Whether Swedish lemma+split vs lemma-nosplit (−7.4 points, larger than the significant −5.3 vs stemmed) was tested is **not stated**.

Summary patterns **[computed from Table 3]**:
- Ordering in every non-English language: lemma+split > stemmed > lemma-nosplit > inflected. Stemmed > lemma-nosplit in all four languages (+0.7 EN, +1.5 FI, +2.1 SV, +3.8 DE points).
- Mean over FI/SV/DE: inflected 30.47, lemma-nosplit 36.77, stemmed 39.23, lemma+split 41.83.
- The normalization effect is largest for Finnish (+16.0 to +19.5 points) and not significant for English.

### Per-topic examples (Appendix, pp. 266–270; checked on page images)

AP % per topic and representation. The selection was not random: "First, we identified clear performance differences between the runs concerning individual topics." (p. 259).

| Topic | Run | Lemma + split | Lemma nosplit | Stemmed | Author's explanation |
|---|---|---:|---:|---:|---|
| 187 (*nuclear transport*) | EN→FI | 100 | 54.4 | 16.7 | compound *ydinjätekuljetus*; under/over-stemming (Ex. 1–2) |
| 186 (*purple cabinet*) | EN→SV | 91.0 | 45.3 | 21.5 | compound *purpurkoalition* (Ex. 3–4) |
| 184 (*maternity leave*) | EN→DE | 67.5 | 47.1 | 2.7 | compound *Mutterschaftsurlaub* (Ex. 5–6) |
| 183 (*remains*) | EN→FI | 50.0 | 66.7 | 0.0 | over-stemming: *tähteet* → *täht* collides with *tähti* "star" (Ex. 7–8) |
| 174 (*Bavarian*) | EN→FI | 70.2 | 68.8 | 8.3 | under-stemming of *baijerilainen* forms (Ex. 9–10) |
| 147 (*lintu*) | FI mono | 41.8 | 2.0 | 16.8 | compounds *lintuparvi*, *lintuvahinko* (Ex. 11–12) |
| 197 (*Dayton*) | SV mono | 59.4 | 0.2 | 60.1 | compounds *Dayton-samtal*; unrecognized names (Ex. 13–14) |
| 152 (children's rights) | FI mono | 76.5 | 75.6 | 13.5 | under-stemming: *lasten* → *last* vs *lapsi* → *lap* (Ex. 15–16) |
| 185 (*Srebrenica*) | FI mono | 50.0 | 50.0 | 100.0 | lemmatizer leaves unrecognized *Srebrenicasta* unnormalized (Ex. 17–18) |

- Across these nine topics **[computed]**, the best representation is lemma+split in 6, lemma-nosplit in 1 (183) and stemmed in 2 (197, 185). The spread between best and worst representation is 39.8–83.3 AP points per topic, versus at most 14.7 points between the means of two normalized representations for the same language and task in Tables 2–3 (EN→FI lemma+split vs stemmed).
- The author's general per-topic statement (p. 259): "We found that performance of various methods differed topic by topic: the run which achieved the worst average precision, could achieve the best result in a single topic."
- And (Sec. 7, p. 265): "All the queries which got better result in the stemmed index than in the lemmatized indexes included unrecognized words (for the lemmatizer)."

## 10. Statistical evidence

- **Significance test:** Wilcoxon signed ranks test at the 0.01 level (pp. 258, 261–262). Only some pairs are reported (§9); p-values are **NOT_REPORTED**; no correction for multiple comparisons is mentioned.
- **Confidence intervals:** NOT_REPORTED.
- **Runs / seeds:** deterministic runs; not applicable.
- **Ablation:** the design itself is an ablation of normalization type and of decompounding (lemma with vs without split). No ablation of stop-words, `#syn` structuring or translation dictionary.
- **Per-query analysis:** **qualitative only.** Topics were selected for "clear performance differences" (p. 259); in some cases the top ~10 retrieved documents were inspected (p. 259). There is:
  - no count of per-topic wins/losses between representations;
  - no overlap of retrieved or relevant documents between representations;
  - no unique relevant hits per representation;
  - no oracle union or per-topic best-representation upper bound;
  - no fusion of representations;
  - no systematic coding of query features (compounds, names, inflection) over all topics.
- **Morphological variants of the lexical representation:** yes: inflected / Snowball stem / TWOL lemma / TWOL lemma + decompounding.
- **BM25 or other lexical model:** InQuery only; **no BM25**.
- **Dense / neural retrieval:** **absent**.
- **Fusion / hybrid:** **absent**.

## 11. Strengths

- Controlled design: same collections, topics, engine and tokenization; only the representation changes.
- Separates lemmatization from decompounding (lemma with vs without split), which shows that most of the lemmatizer's advantage comes from compound splitting.
- Four languages with different morphological profiles, including a highly inflected agglutinative one (Finnish).
- Paired non-parametric significance testing on topic-level AP.
- Full queries printed for 18 examples, so the mechanisms (compound mismatch, over/under-stemming, unrecognized names) can be inspected directly.
- Explicitly identifies the lemmatizer's unrecognized-word problem and its effect on individual topics.

## 12. Limitations

### Stated by the author

- The Finnish Snowball stemmer's quality may explain over-stemming problems (p. 261, p. 266).
- The lemmatizer cannot handle unrecognized words; words were left as such (p. 264–265).
- English as the only source language may affect the bilingual results (p. 266).
- No English phrase recognition; small dictionary coverage of phrases (pp. 257, 266).
- Decompounding "could in some cases add noise in retrieval as well" (p. 266).
- No English decompounding tool (p. 256).

### Inferred from the experimental design

1. **Conclusions overstate the evidence** (internal inconsistencies, all verified on page images):
   - Sec. 7 (p. 265): "The two indexes without decompounding performed almost equally in all the bilingual runs." Table 2: EN→FI 29.0 vs 20.8 (−28.3%), called significant on p. 258.
   - Sec. 8 (p. 266): "This research shows that retrieval in the index without decompounding utilizing stemmers performs as well as retrieval using lemmatizers in monolingual and bilingual IR, even with highly inflected languages." Same EN→FI counter-evidence; also, stemmed vs lemma+split is significant in all bilingual runs (p. 258) and in Swedish monolingual (p. 262).
   - Sec. 8 (p. 266): "retrieval in a decompounded index performs significantly better than retrieval in an index without decompounding in bilingual IR". For EN→FI, lemma+split vs lemma-nosplit is "not statistically significant" (p. 258).
   - Abstract (p. 249): "retrieval in a lemmatized compound index gives almost as good results as retrieval in a decompounded index" (monolingual). Table 3: Swedish −19.1%, German −11.9% (significant, p. 262). Sec. 7 answers RQ2 with "No remarkable differences" (p. 265) while reporting the −19.1% difference two sentences later.
2. **Percentage points vs percent:** "the run with a lemmatized decompounded index was only 2.0% better than that of a stemmed index" (p. 265). 2.0 is the difference in AP points; the relative difference is 4.0% of the split run (Table 3) or 4.1% of the stemmed run **[computed]**.
3. **Wrong cross-reference:** p. 265, Swedish topic 197 under "Unrecognized words" points to "Examples 11 and 12 in the Appendix"; those are Finnish topic 147. The correct examples are 13–14 (as given on p. 264).
4. **Rounding:** Table 3 Finnish lemma-nosplit "Change %" −7.0 vs −6.93 computed from the rounded MAPs (consistent with unrounded values; not demonstrably an error).
5. **Stop-word handling may differ across conditions** (our inference from the Appendix): the Finnish stemmed queries contain function or topic-phrasing words absent from the lemmatized queries of the same topic ("#syn( dokument) #syn( jotk)", Example 12, whereas `et` corresponds to *etsiä*, which is present in Example 11; "#syn( mitä) ... #syn( niil) ... #syn( joita)", Example 18). The Finnish list was built from the English list, plausibly in base forms, so it would match lemmas but not inflected forms or stems. If so, stemmed (and probably inflected) runs contain more noise words, which confounds the stem vs lemma comparison. The paper does not discuss this.
6. **Decompounding is augmentation**, not a different representation: the split index adds compound parts while keeping the whole compound (p. 260). Its gains mix normalization with a form of document expansion, as the author himself notes ("acts like query expansion", p. 263).
7. **Unrecognized-word policy is one fixed choice** (leave as is). No fallback (e.g., stemming unrecognized words) is tested, although the author recommends it (p. 265).
8. **Ambiguous lemmas and topic fields** are not documented (§5).
9. **Topic count per language** not reported; 60 topics is the nominal figure.
10. **Per-topic evidence is cherry-picked** by design (topics with clear differences), so it illustrates mechanisms but cannot estimate how often each mechanism occurs.
11. **Only one generic retrieval engine** (InQuery); no BM25; effects may be model-dependent (cf. MORPH-002, Haddad & Bechikh Ali).
12. Bilingual results mix normalization with dictionary translation quality (42 phrases, 1 translatable).

## 13. What the work proves

- In **monolingual** retrieval with InQuery on CLEF 2003, morphological normalization significantly improves MAP over an inflected word-form index for Finnish (+16.0 to +19.5 points), Swedish and German (except German lemma-nosplit), but not significantly for English (Table 3, pp. 261–262).
- **Without decompounding, Snowball stemming is at least as good as TWOL lemmatization monolingually** in all four languages (stemmed higher by 0.7–3.8 points; stem vs lemma-nosplit differences not reported as significant) (Table 3).
- **Lemmatization with decompounding** is the best monolingual representation in FI/SV/DE; its advantage over stemming is significant only for Swedish (Table 3, p. 262).
- In **English→FI/SV/DE dictionary-based bilingual** retrieval, lemma+split is best in every language and significantly better than stemming in all three (Table 2, p. 258). Its advantage over lemma-nosplit is significant for SV and DE, not FI.
- **The best representation varies by topic** (illustrated on nine hand-picked topics; frequency not established, see §14), and qualitatively identifiable mechanisms explain, in the author's analysis, the variation: compounds (split helps), over-stemming collisions (stemming hurts), under-stemming (stemming hurts or occasionally helps), unrecognized names (lemmatization hurts, stemming helps) (Sec. 6, Appendix).

## 14. What the work does NOT prove

- **Anything about BM25.** The engine is InQuery; no BM25 run exists.
- **Anything about dense or semantic retrieval, or lexical–semantic hybrids.** Neither exists in the paper.
- **That different morphological representations retrieve different relevant documents** (unique hits, overlap) or that combining them would help. Only per-topic AP differences are shown, for hand-picked topics.
- **How often each failure mechanism occurs**, or that query features predict the winning representation. The statement that all stemmed-better queries contained unrecognized words is not backed by counts or a test.
- **That "stemming performs as well as lemmatizers ... even with highly inflected languages" in general** (Sec. 8): contradicted for EN→FI bilingual and for lemma+split in Swedish; and the stemmer–lemmatizer comparison is confounded by the lemmatizer's unrecognized-word policy and possibly by stop-word handling (§12).
- **Anything about Turkic languages or low-resource settings.**
- **Generalization beyond news, CLEF 2003, InQuery and these specific tools** (Snowball, TWOL).

## 15. Relationship to current Uzbek evidence

- **No Uzbek or Turkic data.** Context (not from the paper): Finnish, like Uzbek, is agglutinative and suffixing, so Finnish is the most relevant of the four languages; Uzbek compounding is less central than in Finnish/German/Swedish, so the decompounding findings transfer weakly.
- **Consistent with MORPH-001 (Can et al. 2008, Turkish)** and **MORPH-002 (Haddad & Bechikh Ali 2014, Turkish)**: normalization strongly helps an agglutinative language, and a simple rule-based method (stemmer here, prefix truncation there) is competitive with sophisticated lexicon-based analysis. Together they support the project rule "do not assume lemma > stem > raw; measure it".
- **Unrecognized-word problem is directly relevant to Uzbek lemmatizers** (Bakaev, Xusainova, Elov analyzers in `MASTER_INDEX` C). Context (not from the paper): Uzbek text contains many Russian/international loans, proper names and Latin/Cyrillic variation, so the out-of-lexicon rate of an Uzbek analyzer is a probable driver of stem-vs-lemma differences per query.
- **Tokenization lesson (our inference):** "punctuation marks were deleted" (p. 256) would merge hyphenated compounds such as *Dayton-samtal* (topic 197) if hyphens count as punctuation marks; the paper does not say. This is the kind of silent preprocessing decision that, for Uzbek, would affect the apostrophe letters o‘/g‘ (cf. the exemplar card, MORPH-005 §17).
- **Related records in our corpus (from triage summaries, not verified as identical to the cited works):**
  - CR000561: Braschler & Ripplinger, German stemming and decompounding on CLEF (cited in this paper as Braschler and Ripplinger 2004);
  - CR000452: Finnish lemmatization vs stemming vs word-form generation in INQUERY on TUTK (possibly the cited Kettunen et al.);
  - CR000338: eight European languages, stemming/lemmatization/decompounding and n-grams on CLEF 2002 with per-topic analysis (possibly the cited Hollink et al. 2004);
  - CR000490 (Swedish, SWETWOL + decompounding vs stemming, CLEF 2003, per-topic analysis), CR000504 and CR000681 (FCG word-form generation vs stemming/lemmatization, CLEF, Finnish/Swedish) are from the same CLEF 2003 / Tampere setting.

## 16. Relationship to CURRENT_GAP

**Classification:** *supports* (background for the lexical-representation axis and for query features) + *no material effect on the residual core*.

- **v0.8 elements the work touches:**
  - `Lexical_raw → Lexical_stem → Lexical_lemma` as alternative lexical representations: **yes** (inflected / Snowball / TWOL, plus decompounding), with a paired test on topic-level AP. It is one more item for the already REJECTED claim "raw/stem/lemma has not been compared" (not low-resource, not BM25).
  - Query characteristics: **qualitatively.** Compounds / multi-word concepts, unrecognized words (proper names), over-stemming collisions and under-stemming are shown to change which representation wins on a topic. This supports including "out-of-lexicon / named-entity share" and "compound or hyphenated forms" in our candidate query-feature list.
  - Per-query variation: **qualitatively**: "the run which achieved the worst average precision, could achieve the best result in a single topic" (p. 259). This is per-topic variation *between lexical representations*, the precondition for our question, but measured by AP only on selected topics.
- **v0.8 elements the work does not touch:** BM25; any dense retriever (let alone a fixed D); fusion; unique relevant hits; overlap; oracle union; incremental hybrid gain; systematic per-query statistics.
- **Triage flag:** `carries_complementarity_evidence = YES` is, in our reading, too strong for the project definition (unique hits / overlap / oracle union between channels). Proposed recoding: *partial, qualitative, lexical–lexical only*.

**Proposal:** keep v0.8 refined unchanged. Optionally cite in the evidence boundary as a classic example of per-topic variation across morphological representations without set-level decomposition. This is a proposal only; `CURRENT_GAP.md` has not been edited.

## 17. Implications for our research design

- **Lemmatizer fallback policy (BM25_lemma).** Pre-register what happens to words the Uzbek analyzer does not recognize: (a) keep the surface form (Airio's choice, which lost *Srebrenica* forms) or (b) stem them. Primary `BM25_lemma` should use one fixed policy; a secondary `BM25_lemma+stem-fallback` condition is cheap and directly tests the author's own recommendation (p. 265).
- **Ambiguous analyses.** Fix and report whether all candidate lemmas are indexed/queried (TWOL-style) or one is chosen (disambiguation). This changes the lexical relevant set.
- **Stop-words.** Apply the same stop-word list in the same form across raw/stem/lemma (e.g., remove stop-words on surface forms before normalization, with an inflected-form stop list), or use no stop-words. Otherwise raw/stem runs may keep noise words that lemma runs remove (§12 item 5).
- **Replacement vs augmentation.** Keep the primary conditions as *replacement* representations (raw, stem, lemma). Any "surface + lemma" or compound-split index is augmentation and should be reported as a separate condition, because it mixes normalization with expansion.
- **Tokenization.** Specify handling of hyphens, apostrophes (o‘/g‘ variants) and punctuation, identically across all variants; "delete punctuation" silently merges or splits words.
- **Query taxonomy.** Add or confirm as candidate features: analyzer out-of-lexicon rate of the query; named entities (especially inflected names); compound / hyphenated / multi-word expressions; stemmer collision risk (query stems shared by unrelated words); inflectional distance between query and document forms.
- **Per-query analysis protocol.** Do not select topics by "clear differences" only. Report, for every query, which representation wins, per-query AP differences with a paired test (Wilcoxon or randomization) and p-values, and, beyond this paper, relevant-set overlap and unique hits between `BM25_raw/stem/lemma` themselves as a secondary analysis before adding D.
- **Reporting hygiene.** Distinguish percentage points from percent; report every tested pair and p-value; avoid "no remarkable differences" when some pairs are significant.
- **Hypothesis.** The paper motivates, but does not test, the expectation that the stem and lemma channels differ on identifiable query subsets (names vs regular words) even when their means are close. In our design, that would appear as different unique-hit profiles for `BM25_stem` and `BM25_lemma` against the same D.

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| Inflected (word-form) index | Words indexed exactly as written (after lowercasing) | Index terms = surface tokens (our "raw") |
| Stemming | Cutting word endings by rules; the result may not be a real word | Rule-based suffix stripping (here Snowball) |
| Lemmatization | Returning the dictionary form using a lexicon and morphological rules | Lexicon-based morphological analysis (here TWOL two-level model) |
| Decompounding (compound splitting) | Splitting *tiedonhaku* into *tieto* + *haku* and indexing the parts too | Index augmentation with compound constituents |
| Over-stemming | Removing too much, so unrelated words share a stem (*tähteet*/*tähti* → *täht*) | Precision loss via false conflation |
| Under-stemming | Removing too little, so forms of one word get different stems | Recall loss via missed conflation |
| Unrecognized word | A word the lemmatizer's lexicon does not know (often names, foreign words) | Out-of-lexicon token; here left unnormalized |
| InQuery | The search engine used in all runs | Inference-network retrieval system (UMass CIIR) |
| `#syn` / `#sum` | Query operators: treat several words as one term / average the parts | InQuery structured-query operators (Pirkola 1998 structuring) |
| Dictionary-based CLIR | Translating the query word by word with a bilingual dictionary | Query translation via machine-readable dictionary (UTACLIR) |
| MAP (non-interpolated AP) | Average quality of the whole ranking of relevant documents | Mean over topics of average precision |
| Wilcoxon signed ranks test | Checks whether one run is consistently better across topics | Paired non-parametric test on per-topic differences |
| Percentage points vs percent | 48.5 → 50.5 is +2.0 points but +4.1% | Absolute vs relative difference |
| Complementarity (project term) | Each channel finds some relevant documents the other misses | Unique relevant hits, overlap, oracle-union gain |

## 19. Open questions / verification needed

1. ~~Issue number and official record~~ Resolved in verifier pass: Crossref gives *Information Retrieval* 9(3):249–271, June 2006.
2. **Number of topics evaluated per language** (nominally 60): NOT_REPORTED.
3. **Topic fields** used (title/description/narrative): NOT_REPORTED.
4. **Stop-word handling per condition** and whether the stop lists are in base forms: NOT_REPORTED; the Appendix suggests a difference (§12).
5. **Indexing of ambiguous lemmas** (all readings or one) and the meaning of the `@` prefix in the Appendix: NOT_REPORTED.
6. **Was Swedish monolingual lemma+split vs lemma-nosplit (−7.4 points) tested?** Not stated.
7. **Which cited works correspond to our records** CR000452 (Kettunen et al.?) and CR000338 (Hollink et al.?): verify from their full texts.
8. Is there a later Tampere paper (e.g., CR000490, CR000504, CR000681) on the same CLEF 2003 data that reports per-topic overlap between representations? Worth checking before claiming none exists for this setting.

## 20. Decision after deep dive

- **Keep current gap?** Yes. v0.8 refined remains valid; see §16.
- **Modify gap?** No. Optionally add to the evidence boundary as classic evidence of per-topic variation across lexical morphological representations without set-level decomposition (researcher's decision).
- **Add decision?** Proposed for `decisions/DECISIONS.md` (researcher's decision):
  - "For BM25_lemma, the out-of-lexicon fallback and ambiguous-lemma policy are fixed in advance and reported; a lemma+stem-fallback variant is a secondary condition";
  - "Stop-word removal and tokenization (hyphens, apostrophes, punctuation) are identical across raw/stem/lemma";
  - "Primary lexical variants are replacement representations; augmentation (surface + lemma, compound parts) is reported separately".
- **Add experiment?** Optional low-cost secondary analysis: unique relevant hits and overlap between `BM25_stem` and `BM25_lemma` (without D), stratified by query out-of-lexicon rate. This operationalizes Airio's qualitative observation.
- **Add citation to Chapter I?** Yes, §1.1 (morphological normalization in lexical IR: stemming vs lemmatization vs decompounding; unrecognized-word problem; language-dependent effect, strong for Finnish, none for English). Cite with the caveat that the paper's conclusions are stronger than its tables (§12).
- **Proposed `MASTER_INDEX.md` row** (to add after approval):

| MORPH-027 | Airio — *Word normalization and decompounding in mono- and bilingual IR* (Information Retrieval 9:249–271) — [deep dive](deep-dives/2006_Airio_Word_Normalization_Decompounding_Mono_Bilingual_IR.md) | 2006 | A | HIGH | CLEF 2003, 60 topics, InQuery: inflected vs Snowball stem vs TWOL lemma vs lemma+decompounding for EN/FI/SV/DE monolingual and EN→FI/SV/DE bilingual. Normalization strongly helps Finnish (MAP 31.0 → 48.5 stem / 50.5 lemma+split), not English; stem ≥ lemma without split; decompounding gives most of the lemmatizer's advantage, especially bilingually. Qualitative per-topic analysis: winning representation varies by topic (compounds, over/under-stemming, unrecognized names). No BM25, no dense, no fusion, no overlap/unique-hit analysis. Conclusions overstate stem ≈ lemma (EN→FI contradicts). |
