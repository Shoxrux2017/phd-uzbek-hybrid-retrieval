# Ahmad (2022): Ontological Approach for Semantic Modelling of Malay Translated Qur'an (PhD thesis, University of Leeds)

**Targeted deep-dive status:** COMPLETED (AI-assisted, pending researcher review)
**Completed:** 2026-09-28
**Literature ID:** `MORPH-023` (assigned 2026-09-28, approved by researcher)
**Systematic-review record:** `CR002168`. Full-text triage: INCLUDE, reading priority HIGH, reading tier 1, `carries_complementarity_evidence = YES`
**Provenance:** AI-assisted deep dive (Claude). The 284-page thesis was navigated through the table of contents and grep. Read in full: Abstract, Ch. 1 (research questions, contributions), Sec. 4.3 (preliminary experiment), Ch. 5 (corpus and morphological pipeline), Sec. 6.1–6.2 (ontology construction, query and searching), Ch. 7 (retrieval evaluation), Ch. 8 (implementation, incl. search methods and limitations), Ch. 9 (conclusions, limitations), Appendices D–E (relevant verses; retrieved/relevant counts for all 30 queries). Chapters 2–3 (literature review, Malay background) were skimmed only. Printed page = PDF page − 16. **Pages checked visually on page images:** printed pp. 69, 78, 81, 85, 89, 90, 134, 136, 140, 141, 142, 144, 145, 148, 149, 158, 159, 249, 251, 255, 256, 258–265. Every number below carries its table/figure/section and printed page. Numbers computed by us are marked **[computed]**.
**Verification:** independent AI verifier pass 2026-09-28; 12 findings addressed.
**Source rule:** **the thesis is the primary and only authoritative source** for what the author did and found. The web was used only to verify the bibliographic record (marked "bibliographic check"). Background knowledge appears only in clearly labelled "Context (not from the thesis)" notes.
**Reliability:** **A** as a source type (PhD awarded by the University of Leeds, deposited in White Rose eTheses). **The evidential weight of the retrieval experiment is low.** Only 10 queries are evaluated, and no significance testing is reported. There are many internal numerical inconsistencies (§9, §19). The relevance judgments may share sources with the ontology that drives the "semantic" system (§12).

---

## Кратко для исследователя (RU)

- **Что сделано.** PhD-диссертация (Лидс, 2022). Автор создала корпус малайского перевода Корана (MyQOS Corpus: 149 654 словоупотребления, 6 236 аятов по Table 5.1) и собственный конвейер морфологической обработки: разделение редупликаций, стоп-слова, стеммер на основе словаря корней и правил отсечения аффиксов. Кроме того, построена OWL-онтология на две темы: «Местоположение» и «Живые творения».
  - Сравниваются три поисковых метода на уровне аятов:
    1. поиск по ключевым словам (SQL);
    2. так называемый «Question Answering Search» — тот же поиск по ключевым словам, но со стеммингом, удалением стоп-слов и редупликаций;
    3. «семантический поиск» — SPARQL-запросы к онтологии.
- **Главные числа** (Table 7.6, p. 148; среднее по 10 запросам):
  - ключевые слова: P = 0.5471, R = 0.5884;
  - вариант со стеммингом: P = 0.4971, R = 0.6027;
  - онтологический поиск: P = 0.8409, R = 0.8043.
  - Англоязычная система Qurany: P = 0.4557, R = 0.6688 (Table 7.4, pp. 140–141).
- **Морфологические варианты лексического представления есть, но очень слабо контролируемые.** Сравниваются «сырые» словоформы и стеммы/корни. При этом стемминг смешан с удалением стоп-слов и с другой реализацией: веб-SQL против Python/Tkinter.
  - По Tables 7.4 и 7.6 стемминг изменил результат лишь в 2 из 10 запросов:
    - Q4: P 1.00 → 0.25;
    - Q10: P 0.75 → 1.00, R 0.4286 → 0.5714.
  - По Appendix E число найденных аятов изменилось в 4 из 30 запросов, иногда в сторону уменьшения (Q23: 214 → 6).
  - Точность самого стеммера не оценивалась.
- **Нет BM25 и вообще нет ранжирующей модели.** Поиск булев или множественный: возвращается множество аятов, по нему считаются P и R. Нет плотного поиска и эмбеддингов, нет fusion.
  - «Семантический поиск» — это не плотный поиск, а поиск по онтологии и базе знаний через SPARQL. Входом служит формальный SPARQL-запрос (p. 122); прототип, по словам автора, «still under development» (p. 161).
- **Взаимодополняемость (overlap / unique hits / oracle union) автор не анализирует.** Есть только таблицы P и R по каждому запросу.
  - Из P, R, |Rel| и числа найденных (Appendix E) мы восстановили число найденных релевантных аятов по каждому запросу **[computed]**. Отсюда получаются только нижние границы уникальных попаданий:
    - только лексический канал: ≥ 2 релевантных аята в Q3 и в Q6 (всего ≥ 4);
    - только онтология: ≥ 49 (в сумме по запросам);
    - стемминг против «сырых» словоформ: ≥ 1 уникальный релевантный аят (Q10).
- **Сильные внутренние противоречия** (§19):
  - строки Q4/Q10 в Table 7.5 противоречат Tables 7.4 и 7.6 и Appendix E;
  - фраза «definite improvement at all retrieval points» о стемминге противоречит собственной таблице (P снизилась);
  - «double» на деле означает ×1.69 (P) и ×1.33 (R);
  - «in all cases» опровергается Q3, Q5, Q6;
  - корней 2 187 или 2 817;
  - сумма в Table 5.6 = 29 940, а напечатан итог 63 191;
  - 6 234 или 6 236 аятов;
  - для Q23 в Appendix D 3 релевантных аята, в Appendix E — 19.
- **Риск цикличности в оценке.** Онтология строится по тематическому указателю той же книги, а тот же указатель назван источником релевантных документов (p. 77). В 18 из 20 запросов Q11–Q30 онтологический поиск возвращает ровно |Rel| аятов (Appendix E) **[computed]**.
- **Для нашего gap:** работа не затрагивает ядро v0.8: нет BM25_raw/stem/lemma × фиксированный D, нет fusion и нет декомпозиции взаимодополняемости. Предложение: gap не менять. Работу можно цитировать как пример ранней малайской (low-resource, аффиксальная морфология) работы, где морфологическая нормализация без ранжирования почти не меняет результаты по 10 запросам.
- **Практическая польза для нас:**
  1. Смешение нормализации с удалением стоп-слов и сменой реализации делает эффект морфологии неинтерпретируемым. Нужна строго однофакторная изоляция `raw → stem → lemma`.
  2. Нельзя строить qrels из того же ресурса, из которого строится один из каналов.
  3. Нужно сообщать число найденных и найденных релевантных по каждому запросу: только так восстанавливаются overlap и unique hits.
  4. Нужны точность стеммера и лемматизатора как отдельная характеристика.

---

## 1. Bibliographic record

- **Author:** Nor Diana Binti Ahmad
- **Title:** *Ontological Approach for Semantic Modelling of Malay Translated Qur'an*
- **Degree / institution:** Doctor of Philosophy, The University of Leeds, School of Computing (title page, p. i). The bibliographic check (White Rose eTheses record) adds: Faculty of Engineering.
- **Date:** thesis dated January 2022 (title page). Bibliographic check: deposited 8 June 2022.
- **Supervisors:** Dr Brandon Bennett and Professor Eric Atwell (Acknowledgements, p. v; confirmed by bibliographic check).
- **Funding:** Ministry of Higher Education of Malaysia and Universiti Teknologi MARA (Acknowledgements, p. vi).
- **Official record:** https://etheses.whiterose.ac.uk/30167/ (URI https://etheses.whiterose.ac.uk/id/eprint/30167/; EThOS URN `uk.bl.ethos.855629`), via bibliographic check (White Rose eTheses record page).
- **DOI:** none found in the repository record (bibliographic check).
- **Related publications listed by the author (p. iv):**
  - Ahmad, Bennett & Atwell (2016), IMAN'2016, Khartoum;
  - Ahmad, Bennett & Atwell (2017), "Retrieval Performance for Malay Quran", *IJASAT* 5(2), 13–25.
  - Chapter 6 is marked "PRESENTED: UK Ontology Network 2018" (p. 99).
- **Source type:** doctoral thesis (awarded).
- **Metadata record in the review:** "PQDT – UK & Ireland", 284 pages; this matches the PDF (284 pages).
- **Reliability:** A (source type); low evidential weight for the IR claims (see header).
- **Full text available:** yes (`07_full_text/pdfs/CR002168.pdf`).

## 2. Why this work matters to the PhD

It is a doctoral thesis on a **low-resource language with rich affixal morphology (Malay)**. In one retrieval setting it puts side by side:

- surface-form keyword matching;
- the same matching after a **new morphology pipeline** (reduplication splitting, stop-word removal, dictionary- and rule-based stemming to root words);
- a knowledge-based "semantic" channel (ontology + SPARQL);
- per-query precision/recall with expert relevance judgments.

That is why the triage flagged it as carrying complementarity evidence.

| Axis | Relation |
|---|---|
| Lexical retrieval | Unranked keyword matching (SQL; substring `LIKE` in the Ch. 4 pilot). No BM25, TF-IDF or other scoring model |
| Morphological representation | **Present, but confounded:** raw word forms vs "root word" stems. The stemmed condition also removes stop-words and uses a different implementation |
| Semantic retrieval | "Semantic" = ontology/knowledge-base lookup via SPARQL. **Not** dense or embedding retrieval |
| Hybrid retrieval | Described as "the combination of keyword-based and ontology-based retrieval results" (p. 137). The combination rule is not specified, and the per-query recall pattern is inconsistent with a union (§9) |
| Uzbek morphology | Indirect. Malay (Austronesian: prefixes, suffixes, circumfixes, reduplication) differs typologically from Uzbek (Turkic, suffixing, agglutinative) |
| Low-resource retrieval | Direct: scarce Malay NLP resources are the stated motivation (Abstract; Sec. 5.1) |
| Current gap | Touches "raw vs stem" and "lexical vs non-lexical channel" only in a weak, unranked, 10-query form. It does not touch the v0.8 core (§16) |

## 3. Research problem

### Simple explanation

People search Malay translations of the Qur'an by typing words. Exact word search misses verses that use a different word form: Malay adds many prefixes and suffixes and repeats words for plurals. It also misses verses that express the same idea with another word or a proper name (e.g., *Darussalam* or *Firdaus* for paradise). The thesis asks whether cutting words down to their roots helps, and whether a hand-built ontology of Qur'anic concepts helps more.

### Formal formulation

Two research questions (Sec. 1.2, pp. 5–6):

- **RQ1:** "Can morphological analysis help in retrieving accurate information in the Malay translated Qur'an?"
- **RQ2:** "Can ontology-based IR with semantics improve the query mechanism for Malay Translated Qur'an?"

Chapter 7 restates these as experiment questions (Sec. 7.4, p. 137):

1. "Can semantic annotation improve retrieval quality and accuracy compared to a keyword-based search in Malay Translated Qur'an text?"
2. "What is the effect of using semantic annotation compared to a keyword-based search?"

Task: **verse-level retrieval.** Given a natural-language query, return the **set** of verses (ayat) relevant to it. Evaluation uses set-based precision and recall; no ranking is produced (§5).

## 4. Main idea

### Simple explanation

1. Build a clean digital Malay Qur'an corpus.
2. Write a Malay stemmer that reduces every word to its root, e.g. *pemakanan* → *makan* (p. 86).
3. Build an ontology that links concepts (Paradise, Hell, Jinn, prophets, peoples, places) to the verses discussing them, plus synonyms.
4. Compare three search modes on the same 10 questions: plain word match, word match on roots, and ontology lookup.

### Concrete example

The query *"Ayat berkaitan kaum Nabi Nuh"* ("Verse related to People of Noah") is processed as follows (p. 145):

- The stemmer strips *ber-* and *-an* from *berkaitan*.
- The query is searched as "Ayat kait kaum Nabi Nuh".
- For this query (Q6), stemming changed nothing: P = 0.4375 and R = 0.8235 in both conditions (Tables 7.5 and 7.6).
- The ontology lookup gives P = 1.0000 and R = 0.7059. It is more precise but finds fewer relevant verses than plain keyword search (Table 7.6, p. 148).

### Formal method

- Retrieval function (keyword and stem conditions):
  - `Ret_m(q) = { v ∈ Verses : v matches the terms of q under representation m }`.
  - m ∈ {surface form, root-word stem}.
  - The thesis describes the matching only informally: keyword search "will search only 'Syaitan' or 'enggan' or 'sujud' or 'Adam' separately" (p. 141); QA search "retrieves all verses containing those keywords and merges the results" (p. 145) and "searches for matches … for every keyword found in the user question" (p. 160). This suggests term-by-term matching with merged results, but an exact multi-term rule (OR / AND / phrase) for the Ch. 7 runs is not stated. The very small retrieved sets for some multi-word queries (e.g. Q4 keyword: 3 verses, App. E) are hard to reconcile with a plain any-term OR (our inference).
  - The Ch. 4 pilot uses SQL `lower(a.malay) like '%syurga%'`, i.e. substring matching (Fig. 4.4, p. 69).
  - The Qurany baseline is described as matching any verse with at least one query term (p. 140).
- Semantic condition: a SPARQL graph-pattern query over the OWL knowledge base, e.g. all instances of class `malay:Syurga` and their verse texts (Listing 6.1, p. 124).
- Metrics: per-query `P = tp/(tp+fp)`, `R = tp/(tp+fn)` (Eqs. 7.1–7.2, p. 134), macro-averaged over 10 queries. F1 (Eq. 7.3) is defined but **not reported**.

## 5. Architecture / algorithm

1. **Corpus construction** (Sec. 5.2, pp. 76–79):
   - Source: *Al-Qur'an Amazing* (Karya Bestari, 6th ed., 2016), a JAKIM-verified Malay translation.
   - The text was extracted manually and validated by comparison with English and Arabic versions and by two Qur'anic-studies experts.
   - It was stored in Oracle 11g.
   - Table 5.1 (p. 78): 114 chapters, 6,236 verses, 149,654 words. The text on the same page says 6,234 verses (§19).
2. **Pre-processing / morphological pipeline** (Sec. 5.2.3, pp. 79–91; Python 3.4):
   - lowercasing and punctuation removal (regex);
   - **reduplication splitting:** 1,587 reduplicated words, handled semi-automatically — Python split, then manual root check (p. 82);
   - tokenization: 149,654 tokens (Sketch Engine, NVivo 10; p. 84);
   - **stop-words:** 356 from Ahmad (1995), reduced to 318 (p. 84; list in App. A);
   - **stemming:** seven steps (pp. 88–89; Fig. 5.7). Step 1 iterates over the words; Steps 2–7 are:
     1. reduplication check;
     2. **dictionary check (root found → stop)**;
     3. prefix removal;
     4. suffix removal;
     5. spelling restoration after prefix removal;
     6. final "-i" removal.
     - The affix inventory follows "Alkhawarizmi's Rule" (Table 5.4, pp. 87–88).
     - Algorithm 1 (Fig. 5.3, p. 81) is simpler: it removes a prefix *or* a suffix (`else if`).
     - The thesis calls the output "root words". In our taxonomy this is **dictionary-assisted affix stripping to a base/root form**: closer to a stem/root normalization than to a POS-aware lemmatizer.
     - **Stemmer accuracy is not evaluated anywhere in the thesis** (NOT_REPORTED).
   - **root-word annotation:** every word is annotated with root, synonyms and antonyms (DBP Malay Thesaurus, Malay Dictionary, WordNet; pp. 91–92).
3. **Ontology** (Ch. 6):
   - OWL in Protégé, served via Apache Jena Fuseki.
   - Classes: Chapter, Verse, Location (World: cities, mountains, rivers, seas, historical places; Afterlife: Paradise, Hell), Living Creation (angels, animals, jinn, plants, humans: groups, prophets, historical people) (pp. 106–107).
   - Concepts and instances come from the **thematic index of the same Malay Qur'an book** plus three existing ontologies: Qurany concepts (Abbas 2009), Hakkoum & Raghay (2016), Dukes (2013) (pp. 105, 116).
   - "Each of the concepts in the ontology is assigned a corresponding verse from the Qur'an that discusses such concepts" (p. 116).
   - Instances (Tables 6.3 / 7.2, pp. 116 / 136): Chapter 114, Verse 6,236, Location 86, Living Creation 1,762; total 8,198.
4. **Three search methods** (Sec. 7.4, p. 137; Sec. 8.3.3, pp. 157–160):
   - **Keyword-based search:** "a conventional keyword-based retrieval model" (pp. 137, 157), "developed using SQL query" (p. 158); web interface (JSP/Java).
   - **Question Answering (QA) search:** "a conventional keyword-based retrieval model using text processing algorithm" (p. 137).
     - Implemented in "Python 3.4.3 Tkinter GUI" (p. 159).
     - Query and text are both stemmed.
     - "MyQOS QA search sequentially executes each query, concatenating the results (after the morphological analysis is done) until a result has been achieved" (p. 158).
     - Ch. 7 lists "stemming, stopword removal, tokenization, and reduplication algorithm" (p. 144), and Sec. 9.6 says "it only uses tokenization, removing reduplication, removing stopword and stemming" (p. 173). Ch. 8 says "At this time, the searching process only uses tokenization, stop word removal and stemming techniques" (p. 159).
     - Despite its name this is **not** question answering: it returns verse sets. The triage note says the same.
   - **Semantic-based search:** "the semantic retrieval model including the combination of keyword-based and ontology-based retrieval results" (p. 137).
     - Input: "Our system takes as input as a formal SPARQL query" (p. 122).
     - "Terms in the ontology were used to query" (p. 147).
     - Status: "the prototype of the semantic search is still under development" (p. 161); "At this time, we only use the SPARQL query to query the contents in the OWL file" (p. 165).
     - Sec. 6.2.4 (pp. 123–124) describes generic SPARQL generation from a triple pattern with a "?" variable (e.g. `?hasBirthMother, Maryam`) answered by the Jena inference engine, but not how the Ch. 7 natural-language queries were turned into such patterns.
     - **How the evaluation's natural-language queries were mapped to SPARQL (manually or automatically) and how keyword and ontology results were combined: NOT_REPORTED.**
5. **Ranking:** none. Results are unranked sets. Ranking is listed as future work: "MyQOS prototype also can be improved in the area of ranking the search results according to the user needs" (p. 174).

## 6. Data

- **Collection:** Malay translation of the Qur'an (*Al-Qur'an Amazing*); the retrieval unit is the verse. 6,236 verses per Tables 5.1 / 7.2; 6,234 per the text on pp. 35, 68, 78, 156.
- **Language / domain:** Malay (evaluation). The Qurany baseline runs on an English translation. Religious text.
- **Queries** (Sec. 7.1, pp. 132–134; Table 7.3, pp. 138–139):
  - Malay natural-language queries taken from **Pouzi's collection** (Mohd Pouzi Hamzah, 2006, PhD thesis, UKM); English versions are translations.
  - 40 queries → 10 removed "because the queries are not clear in term of the level of difficulty" → **30 queries**.
  - Table 7.1: 136 words in total, 2–9 words per query, mean 4.5333 (= 136/30 **[computed ✓]**).
  - **Only the first 10 queries (Q1–Q10) are evaluated with P/R** (p. 137). For Q11–Q30 only counts of relevant and retrieved verses are given (App. E).
- **Relevance judgments** (Sec. 7.2, pp. 134–135):
  - Pouzi's collection, whose relevant documents were formulated "with the assistance of two Muslim religious experts";
  - plus "additional checks with another two experts in Quranic studies from Malaysia University", for queries not in Pouzi's collection.
  - Procedure: "Subjects then conducted searches and reviewed documents returned from their searches" (p. 135).
  - Binary relevance.
  - **Pooling from the evaluated systems, number of judges per query, agreement statistics and adjudication: NOT_REPORTED.**
- **Competing descriptions of the relevance source:**
  - Sec. 5.2.1 says the book "has a list of topic indices that can be used as relevant documents in the evaluation phase" (p. 77), and that relevance "is based on Tafseer Jalalain and not just a word match" (p. 78).
  - The Ch. 4 pilot used Tafsir Ibn Kathir, Abbas's concept list and a thematic index (p. 69).
  - Which source produced the Ch. 7 qrels for each query is not stated unambiguously.
- **Relevant-set sizes** (App. E, pp. 255–265):
  - Q1–Q10: 49, 81, 37, 8, 4, 17, 5, 10, 17, 7. Total 235 **[computed]**.
  - All 30 queries: 489 relevant verses **[computed]**.
  - App. D (pp. 248–253) lists verse IDs per query. It totals 473 because it lists only 3 verses for Q23 vs 19 in App. E **[computed]** (§19).
- **Train / dev / test:** not applicable; no learned components. The ontology and stemmer were built on the same collection that is evaluated.

## 7. Baselines

| Baseline / condition | What it is | Why selected | Fair comparison? |
|---|---|---|---|
| Qurany keyword search (English) | Existing English Qur'an search tool (Abbas 2009), any-term matching (p. 140) | "To carry out a fair comparison" with an existing system (p. 139) | **No.** Different language, different translation text and a different system. The Qurany concept list is also one of the ontology's sources (p. 105) |
| MyQOS keyword search (raw) | SQL keyword matching on Malay surface forms | Reference for the morphology condition | Partly. The matching semantics for multi-word queries are described only informally ("separately", p. 141) and not as an exact rule |
| MyQOS "QA search" (stem) | Keyword matching after reduplication splitting (per Ch. 7 only), stop-word removal and root stemming, applied to query and text | Tests RQ1 (morphology) | **Confounded.** Stemming, stop-word removal and a different implementation (Python/Tkinter vs SQL/JSP) change together. The "sequential … concatenating … until a result has been achieved" logic may also differ from the raw condition |
| MyQOS semantic search | SPARQL over an OWL ontology whose concepts are linked to verses (plus a keyword component whose combination rule is not described) | Tests RQ2 | **Not comparable as a retrieval model.** The query input is a formal SPARQL query / ontology terms, not the natural-language query. The knowledge base was hand-curated from sources overlapping with the qrels (§12) |

## 8. Metrics

| Metric | Definition | Simple meaning here | Appropriate? |
|---|---|---|---|
| Precision (per query) | \|Ret ∩ Rel\| / \|Ret\| (Eq. 7.1) | Share of returned verses that experts judged relevant | Acceptable for unranked sets. It rewards returning few verses |
| Recall (per query) | \|Ret ∩ Rel\| / \|Rel\| (Eq. 7.2) | Share of all relevant verses that were returned | Acceptable, but depends on qrels completeness (non-pooled) |
| Average P / R | Arithmetic mean over Q1–Q10 (macro) | — | Very small sample; no dispersion reported |
| F1 | Eq. 7.3 | Harmonic mean of P and R | Defined but **not reported** |
| "Precision vs recall plot" (Figs. 7.1–7.4) | One point per query, sorted by recall (checked on the page images, pp. 142, 149) | — | **Not** an interpolated precision–recall curve. The reading "upper-right portion → performs well" (p. 141) is not meaningful for this plot type |

No rank-based metrics (MAP, nDCG, MRR, P@k) are used, because no system produces a ranking.

## 9. Results

### Preliminary experiment: Table 4.1 (p. 69), Surah Al-Baqarah only, SQL substring search

| Language | Keyword | Relevant | Retrieved | Missed |
|---|---|---:|---:|---:|
| Malay | Syurga | 12 | 10 | 2 |
| English | Heaven | 15 | 11 | 4 |
| English | Paradise | 11 | 1 | 10 |
| English | Hell | 18 | 1 | 17 |
| Malay | Neraka | 18 | 16 | 2 |

- The "missed" column equals relevant − retrieved. This implicitly assumes every retrieved verse is relevant, which is not stated.
- The text calls this "Table 4.2" (p. 69).
- The two Malay misses for *syurga* are attributed to proper names (*Darussalam*, *Firdaus*) (p. 70). This is vocabulary, not inflection.

### Table 7.4: keyword search, Qurany (English) vs MyQOS (Malay), Q1–Q10 (pp. 140–141)

| Query | P Qurany | P MyQOS | R Qurany | R MyQOS |
|---|---:|---:|---:|---:|
| Q1 What is Paradise? | 0.1345 | 0.1751 | 0.6531 | 0.6327 |
| Q2 What is Hell? | 0.2115 | 0.2379 | 0.8148 | 0.7901 |
| Q3 What is Jinn? | 0.1974 | 0.5556 | 0.8108 | 0.9459 |
| Q4 Satan refused to bow to Adam | 0.5333 | 1.0000 | 1.0000 | 0.3750 |
| Q5 Story about Qarun | 0.8000 | 0.5000 | 1.0000 | 0.5000 |
| Q6 People of Noah | 0.2273 | 0.4375 | 0.8824 | 0.8235 |
| Q7 Old man of Madian | 1.0000 | 0.5000 | 0.2000 | 0.2000 |
| Q8 Human creation | 0.0244 | 0.5455 | 0.1000 | 0.6000 |
| Q9 The Trumpet is blown | 0.7619 | 0.7692 | 0.9412 | 0.5882 |
| Q10 Man with Joseph in prison | 0.6667 | 0.7500 | 0.2857 | 0.4286 |
| **Average** | **0.4557** | **0.5471** | **0.6688** | **0.5884** |

All four averages were recomputed from the rows **[computed ✓]**. MyQOS vs Qurany: +0.091 P, −0.080 R **[computed]**. These are different languages, texts and systems, so the comparison says little about methods.

### Table 7.6: three MyQOS methods, Q1–Q10 (p. 148)

"QA" = keyword + stemming/stop-word pipeline.

| Query | P kw | P QA (stem) | P sem | R kw | R QA (stem) | R sem |
|---|---:|---:|---:|---:|---:|---:|
| Q1 | 0.1751 | 0.1751 | 0.9800 | 0.6327 | 0.6327 | 1.0000 |
| Q2 | 0.2379 | 0.2379 | 0.9878 | 0.7901 | 0.7901 | 1.0000 |
| Q3 | 0.5556 | 0.5556 | 1.0000 | 0.9459 | 0.9459 | 0.8919 |
| Q4 | 1.0000 | 0.2500 | 0.8571 | 0.3750 | 0.3750 | 0.7500 |
| Q5 | 0.5000 | 0.5000 | 0.4000 | 0.5000 | 0.5000 | 0.5000 |
| Q6 | 0.4375 | 0.4375 | 1.0000 | 0.8235 | 0.8235 | 0.7059 |
| Q7 | 0.5000 | 0.5000 | 0.8333 | 0.2000 | 0.2000 | 1.0000 |
| Q8 | 0.5455 | 0.5455 | 0.7273 | 0.6000 | 0.6000 | 0.8000 |
| Q9 | 0.7692 | 0.7692 | 0.8235 | 0.5882 | 0.5882 | 0.8235 |
| Q10 | 0.7500 | 1.0000 | 0.8000 | 0.4286 | 0.5714 | 0.5714 |
| **Average** | **0.5471** | **0.4971** | **0.8409** | **0.5884** | **0.6027** | **0.8043** |

All six averages were recomputed from the rows **[computed ✓]**.

**Morphology effect (raw → stem), our reading of Table 7.6:**

- The two conditions are **identical on 8/10 queries.**
- Q4: P 1.00 → 0.25, R unchanged.
- Q10: P 0.75 → 1.00, R 0.4286 → 0.5714.
- Mean change **[computed]**: ΔP = −0.050, ΔR = +0.014.
- The author states: "The precision for question answering search is lower than keyword search" (p. 144). The same section also claims "definite improvement at all retrieval points … with significant differences" (p. 145; repeated on p. 168). The table does not support the second claim, and no test is reported.

**Ontology vs keyword/stem:**

- Mean P 0.8409 vs 0.4971 and R 0.8043 vs 0.6027 (vs QA): +0.344 P and +0.202 R absolute **[computed]**.
- Relative: ×1.69 P and ×1.33 R **[computed]**. The Abstract and Sec. 7.4.3 / 9.4 call this "double".
- The ontology is **worse** than plain keyword search on:
  - Q5 precision (0.40 vs 0.50);
  - Q3 recall (0.8919 vs 0.9459);
  - Q6 recall (0.7059 vs 0.8235).
  - It is also worse than the stemmed condition on Q10 precision (0.80 vs 1.00).
- This contradicts "enhanced the precision and recall in all cases" (pp. 170–171).

### Table 7.5 (pp. 144–145): discrepancy with Tables 7.4/7.6 and App. E

Table 7.5 prints:
- Q4: keyword P = 0.2500, QA P = 1.0000 — the reverse of Tables 7.4/7.6;
- Q10: keyword P = 1.0000 — Tables 7.4/7.6 give 0.7500.

Its own columns average to 0.4971 (keyword) and 0.5721 (QA) **[computed]**, yet it prints 0.5471 and 0.4971. App. E counts settle the question:
- Q4 keyword returned 3 verses with R = 0.375 of 8, i.e. 3 relevant → P = 1.00;
- Q10 keyword returned 4 verses with R = 0.4286 of 7, i.e. 3 relevant → P = 0.75.

**So Tables 7.4/7.6 are internally consistent and Table 7.5's Q4/Q10 rows are wrong.**

### Derived per-query counts and complementarity bounds [computed]

The author does not report relevant-retrieved counts, overlap or unique hits. We derive them:
- App. E gives |Rel| and |Ret| per method (pp. 255–265, checked on page images).
- Tables 7.4/7.6 give P and R.
- |Ret ∩ Rel| = P·|Ret| = R·|Rel|. Both routes give the same integer for every query/method **[computed]**, which confirms that Tables 7.4/7.6 and App. E agree.

| Q | \|Rel\| | kw: \|Ret\| / rel-ret | stem: \|Ret\| / rel-ret | sem: \|Ret\| / rel-ret | kw-only rel ≥ | sem-only rel ≥ | stem-only (vs kw) rel ≥ |
|---|---:|---:|---:|---:|---:|---:|---:|
| Q1 | 49 | 177 / 31 | 177 / 31 | 50 / 49 | 0 | 18 | 0 |
| Q2 | 81 | 269 / 64 | 269 / 64 | 82 / 81 | 0 | 17 | 0 |
| Q3 | 37 | 63 / 35 | 63 / 35 | 33 / 33 | **2** | 0 | 0 |
| Q4 | 8 | 3 / 3 | 12 / 3 | 7 / 6 | 0 | 3 | 0 |
| Q5 | 4 | 4 / 2 | 4 / 2 | 5 / 2 | 0 | 0 | 0 |
| Q6 | 17 | 32 / 14 | 32 / 14 | 12 / 12 | **2** | 0 | 0 |
| Q7 | 5 | 2 / 1 | 2 / 1 | 6 / 5 | 0 | 4 | 0 |
| Q8 | 10 | 11 / 6 | 11 / 6 | 11 / 8 | 0 | 2 | 0 |
| Q9 | 17 | 13 / 10 | 13 / 10 | 17 / 14 | 0 | 4 | 0 |
| Q10 | 7 | 4 / 3 | 4 / 4 | 5 / 4 | 0 | 1 | **1** |

How to read this table:

- The "≥" columns are **lower bounds only** (e.g. kw-only ≥ rel-ret_kw − rel-ret_sem). Exact unique hits and overlap need the retrieved verse IDs, which the thesis does not list.
- **Lexical-only relevant verses:**
  - at least 4 over Q1–Q10 (Q3, Q6), versus at least 49 ontology-only **[computed]**;
  - on these two queries the "semantic" system (described as including keyword results) misses relevant verses that keyword search finds.
- **Oracle union:** macro recall of the keyword ∪ semantic union is ≥ 0.8214, vs 0.8043 for the semantic system alone, i.e. ≥ +0.017 **[computed]**. The upper bound (1.0) is uninformative.
- **Stem vs raw:**
  - at least 1 relevant verse is found only by the stemmed condition (Q10: the same *number* of verses, 4, is returned, but 4 vs 3 of them are relevant, so the two sets must differ);
  - on Q4 stemming returns 9 more verses (12 vs 3) while the relevant-retrieved count stays at 3, i.e. the net addition is 9 non-relevant verses.
- Micro-averaged over Q1–Q10 **[computed]**:
  - keyword: P 169/578 = 0.292, R 169/235 = 0.719;
  - stem: P 170/587 = 0.290, R 170/235 = 0.723;
  - semantic: P 214/228 = 0.939, R 214/235 = 0.911.

### App. E, Q11–Q30: retrieved-set sizes only (pp. 258–265)

**Stemming vs raw (|Ret|):** stemming changes |Ret| in only 4 of 30 queries **[computed]**:

| Query | Raw | Stemmed |
|---|---:|---:|
| Q4 | 3 | 12 |
| Q12 | 44 | 17 |
| Q20 | 26 | 25 |
| Q23 | 214 | 6 |

- For Q12, Q20 and Q23 the stemmed condition returns **fewer** verses (Q20 only by one). That is unexpected for pure stemming, which merges forms; it suggests the stop-word removal and/or query-execution logic dominate. This is our inference.
- Precision/recall for Q11–Q30 are not reported.

**Semantic search |Ret| vs |Rel|:**

- The semantic search returns **exactly |Rel| verses in 18 of 20 queries Q11–Q30** **[computed]**. The exceptions are Q14 (3 vs 2) and Q21 (25 vs 78).
- Over all 30 queries this happens in 19 cases.
- Equal counts do not imply perfect retrieval (Q9: 17 returned, 14 relevant). The pattern is nonetheless consistent with the ontology's verse lists and the qrels sharing sources (§12). This is an inference, not a finding of the thesis.

### Corpus statistics and their consistency

- Table 5.5 (p. 90): 149,654 words with stop-words; 63,191 without; "2,187" words after stemming.
  - The text says 2,187 root words on p. 89 but 2,817 on pp. 90, 91, 104.
  - Stop-word share: (149,654 − 63,191)/149,654 = 57.8% **[computed]**.
- Table 5.6 (p. 90): prefix 10,415; suffix 7,672; infix 53; circumfix 11,800. They sum to **29,940** **[computed]**, but the printed TOTAL is 63,191.
- Table 5.3 (p. 85, seven longest chapters): the "contains stopwords" column sums to **24,887** **[computed]**, not the printed 28,887. With 24,887, the row identity total = kept + stop-words holds (43,399) **[computed]**.

## 10. Statistical evidence

- **Significance test:** NOT_REPORTED. "Significant difference(s)" / "significant impact" / "results are significant" is used rhetorically (pp. 141, 145, 148, 149, 151, 168, 171) without any test.
- **Confidence intervals / dispersion:** NOT_REPORTED.
- **Runs / seeds:** not applicable (deterministic systems). There is a single evaluation.
- **Sample size:** 10 queries for P/R (Q1–Q10), chosen as "first ten". The thesis itself cites Buckley & Voorhees for a minimum of 25 queries (p. 132).
- **Ablation:** none. Stemming, stop-word removal, reduplication handling and implementation change together in the "QA" condition. The ontology vs keyword contributions inside "semantic search" are not separated.
- **Per-query analysis:** per-query P/R tables exist (Tables 7.4–7.6), with anecdotal discussion of Q4, Q6 and Q10. There is:
  - no win/loss count;
  - no overlap, unique-hit or oracle-union analysis (our bounds in §9 are derived);
  - no query-feature analysis (query length, affix counts, named entities), although Sec. 7.1 discusses query difficulty levels (Sakai et al.).
- **Stemmer intrinsic evaluation:** NOT_REPORTED.
- **Qrels quality:** judge agreement NOT_REPORTED.

## 11. Strengths

- A real, expert-judged verse-level test collection for Malay: 30 queries with relevant-verse lists (App. D) and per-method retrieved counts (App. E). Rare for Malay, and detailed enough to derive relevant-retrieved counts for Q1–Q10.
- Explicit handling of Malay-specific morphology: reduplication (1,587 cases, manually checked), prefixes, suffixes and circumfixes (Table 5.4), and a curated stop-word list (318).
- The lexical and knowledge-based channels are evaluated on the same queries and qrels, with per-query numbers (Table 7.6).
- The author concedes the negative morphology result in one place: "The precision for question answering search is lower than keyword search" (p. 144).
- Candid prototype limitations (Sec. 8.4, Sec. 9.6): ontology coverage restricts which queries can be answered; the semantic search is under development; the stemmer needs improvement and is dictionary-dependent; no ranking.

## 12. Limitations

### Stated by the author

- Queries not covered by the ontology cannot be answered by semantic search (Sec. 8.4, p. 164). The ontology covers only two topics, Location and Living Creation (p. 106).
- The semantic search prototype is "still under development" (p. 161); only SPARQL over the OWL file is used (p. 165).
- The stemmer "needs to be improved"; "it relies on Malay root dictionary to maintain the stemming accuracy" (Sec. 9.6, p. 173).
- No ranking of results (Sec. 9.6, p. 174).
- Speed is out of scope; only precision and recall are used (Sec. 8.4, p. 165).
- Manual extraction of the corpus: "the probability of error is high" (p. 78).
- Keyword and QA precision remain "moderate". Relevant verses that use other terms are not retrieved (pp. 146, 168–169).

### Inferred from the experimental design

1. **Morphology is confounded.** The "QA" condition changes stemming, stop-word removal, (per Ch. 7) reduplication handling and the software implementation together. Its execution logic is also different ("sequentially executes each query, concatenating the results … until a result has been achieved", p. 158). No single-factor raw → stem comparison exists.
2. **No ranking model.** Set-based SQL/Python matching. Results say nothing about BM25-type term weighting, where morphology effects typically act through term statistics (Context, not from the thesis: in BM25, conflating forms changes both tf and df).
3. **Circularity risk in evaluation.**
   - The ontology's concepts and concept→verse assignments come from the book's thematic index and from Qurany, Hakkoum & Raghay, and Dukes (pp. 105, 116).
   - The same thematic index is described as usable "as relevant documents in the evaluation phase" (p. 77).
   - The Ch. 4 pilot's relevance used the Abbas/Qurany concept list and a thematic index (p. 69).
   - The Ch. 7 summary states: "The evaluations presented in this chapter have been verified against the available contents and the domain ontologies presented in chapter 6" (p. 151).
   - For Q11–Q30 the semantic system returns exactly |Rel| verses in 18/20 queries **[computed]**.
   - If the qrels and the ontology share verse lists, the semantic P/R measure agreement between two curated resources, not retrieval quality.
4. **Human query formulation for the semantic channel.**
   - The system "takes as input as a formal SPARQL query" (p. 122), and "Terms in the ontology were used to query" (p. 147).
   - The natural-language → SPARQL step is undocumented and possibly manual. The keyword conditions receive the natural-language query; the semantic condition apparently receives a concept-level query.
5. **Qrels construction is not independent of systems and not pooled.**
   - The experts ran their own searches (p. 135).
   - Three sources of relevance are mentioned (Pouzi's collection, additional experts, the book's topic index / Tafseer Jalalain) without a per-query mapping.
   - Agreement is NOT_REPORTED.
   - App. D vs App. E disagree for Q23 (3 vs 19 relevant).
6. **Small and non-random evaluation sample:** 10 of 30 queries ("first ten"), with no statistics.
7. **Qurany comparison is not controlled:** English vs Malay, different translations, different system, and Qurany concepts feed the ontology.
8. **Reporting errors undermine trust in exact values:** Table 7.5 rows Q4/Q10, root counts, the Table 5.6 total and others (§19).
9. **No stemmer accuracy**, so over- and under-stemming cannot be separated from retrieval effects.

## 13. What the work proves

Only weakly supported claims, within this collection and these 10 queries:

- A **dictionary- and rule-based Malay root stemmer, combined with stop-word removal**, applied to unranked keyword matching over verses, changed retrieval results on **only 2 of 10 evaluated queries**. Mean P fell 0.5471 → 0.4971 and mean R rose 0.5884 → 0.6027 (Table 7.6, p. 148). Retrieved-set sizes changed on 4 of 30 queries (App. E) **[computed]**.
  - So in this setting, morphological normalization of the lexical representation had a **small and mixed** effect: a precision loss on Q4 and a recall/precision gain on Q10.
- A curated OWL ontology queried by SPARQL returns verse sets with much higher P/R than keyword matching against these qrels: 0.8409 / 0.8043 vs 0.5471 / 0.5884 (Table 7.6). This holds **under the caveats of possible resource overlap with the qrels and non-equivalent query input** (§12).
- Derived from the thesis's own numbers **[computed]**: the keyword channel finds at least some relevant verses that the "semantic" system misses (≥ 2 each on Q3 and Q6). A keyword ∪ semantic oracle would reach macro recall ≥ 0.821 vs 0.804 for semantic alone.
- In the Ch. 4 pilot, Malay keyword search misses relevant verses because of **lexical substitution** (proper names such as *Darussalam* and *Firdaus*), not inflection (p. 70).

## 14. What the work does NOT prove

- **That morphological analysis improves Malay retrieval.** RQ1 is answered positively in the text (pp. 145, 168), but the thesis's own table shows lower mean precision, a +0.014 recall change, identical results on 8/10 queries and no significance test. Stemming is confounded with stop-word removal and implementation.
- **Anything about BM25 or ranked lexical retrieval.** No scoring model, no rank metrics.
- **Anything about dense / embedding retrieval.** "Semantic" here means ontology lookup. Cosine similarity appears only as future work (p. 173).
- **That hybrid retrieval helps.** The combination rule inside "semantic search" is not described. The recall pattern (Q3, Q6) is inconsistent with a union of keyword and ontology results. No fusion is tested.
- **That lexical and semantic channels are complementary in a measured sense.** No overlap, unique-hit or oracle analysis is reported. Our bounds are derived, coarse and rest on possibly circular qrels.
- **That ontology-based search is "double" as good or better "in all cases".** The ratios are ×1.69 (P) and ×1.33 (R), and Q3, Q5, Q6 (and Q10 vs QA) contradict "all cases".
- **Which query characteristics drive differences.** There is no query-feature analysis.
- **Generalization** beyond one translated religious text, one ontology covering two topics, and 10 queries.

## 15. Relationship to current Uzbek evidence

- **No Uzbek data.** Malay (Austronesian) morphology involves prefixes, circumfixes and reduplication. Uzbek (Turkic) is suffixing and agglutinative, with long suffix chains. Transfer of the specific stemming results is therefore weak.
- Only the general lesson transfers: a morphological analyzer's existence and deployment ≠ measured retrieval gain. The same distinction is drawn for Bakaev (PHD-UZ-001), Xusainova (PHD-UZ-003) and Elov (PHD-UZ-004) in `GAP_BOUNDARY` §2.
- Parallel to the national Uzbek evidence:
  - small expert query sets;
  - an ontology or knowledge base used as the "semantic" component (cf. O-RAG, UZ-HYB-002: ontology + hybrid retrieval);
  - "semantic" ≠ dense retrieval (cf. the `PROJECT_INSTRUCTIONS` §8 distinctions).
- Compared with **MORPH-001 (Can et al. 2008, Turkish)** and **MORPH-002 (Haddad & Bechikh Ali 2014)**: those studies isolate stemming/lemmatization effects within ranked lexical models on a large collection. This thesis does not. It confirms the Can et al. caution that more elaborate normalization does not guarantee gains, but only anecdotally.
- Related record in our corpus (per triage note): **CR002173** (Malay Qur'an retrieval, different author and study). It should be checked for a ranked (e.g., TF-IDF/BM25) raw vs stemmed comparison on the same text type.

## 16. Relationship to CURRENT_GAP

**Classification:** *no material effect on the residual core* + *weakly supports the motivation*.

- **Touches (weakly):**
  - "raw vs stem lexical representation" (confounded, unranked);
  - "lexical vs a non-lexical channel on the same qrels, per query" (knowledge-based, not dense);
  - per-query P/R, from which coarse unique-hit bounds can be derived.
- **Does not touch any v0.8 core element:**
  - no BM25_raw / BM25_stem / BM25_lemma;
  - no fixed modern dense retriever D;
  - no fusion condition H_m;
  - no measured unique relevant hits, overlap or oracle union;
  - no incremental hybrid gain;
  - no link to query features.
- **Supports the motivation:** an example where the morphology effect on a lexical channel is small and query-specific (2 of 10 queries), and where a non-lexical channel both adds many relevant items and misses some that the lexical channel finds (Q3, Q6). Measuring *which* relevant items each channel contributes, and how that changes with the lexical representation, is exactly what the thesis leaves unmeasured.
- The "What can still kill this gap" criteria (1–4) in `CURRENT_GAP.md` are not met.

**Proposal:** keep v0.8 refined unchanged. Optionally list this thesis in the evidence boundary as a low-resource (Malay) example of "morphological normalization + knowledge-based semantic channel, unranked, without complementarity analysis". This is a proposal only; `CURRENT_GAP.md` has not been edited.

## 17. Implications for our research design

- **Single-factor morphology control.**
  - `BM25_raw → BM25_stem → BM25_lemma` must differ *only* in the normalization step: same tokenizer, same stop-word handling (either none or the same list in all conditions), same implementation, same query-execution logic.
  - Stop-word removal, if studied, is a separate factor.
  - This thesis shows how bundling them makes the morphology effect uninterpretable.
- **Report per-query |Ret|, |Rel| and |Ret ∩ Rel|, and release run files.** With those counts we could still derive bounds here. With the run files (verse/document IDs per system) overlap, unique hits and oracle union become exact. Our protocol should publish TREC-format runs for every lexical variant, D and each H.
- **Qrels independence.**
  - Relevance judgments must not be derived from a resource that one of the compared channels is built from: thesaurus, ontology, topic index, or a D fine-tuned on the same pairs.
  - Use pooling from all systems (raw/stem/lemma/D/H) to sufficient depth; record assessor agreement.
  - Check the "retrieved count = relevant count" pattern as a leakage diagnostic.
- **Equal query input across channels.** All channels must receive the same query string. No manual reformulation for one channel only (cf. the SPARQL input here).
- **Stemmer/lemmatizer intrinsic accuracy** should be reported next to retrieval effects, so that over- and under-normalization can be distinguished from retrieval-model behaviour.
- **Metrics.**
  - Use ranked metrics (nDCG@k, MAP, Recall@k) plus set-level coverage at fixed depth k for union analysis.
  - Precision/recall of unranked sets reward small outputs and are not comparable across systems with very different |Ret|: here 228 vs 578 verses over Q1–Q10 **[computed]**.
- **Query taxonomy.** This thesis suggests two candidate query features worth coding for Uzbek:
  - *lexical-substitution / proper-name* queries (synonyms and names such as *Darussalam* — not fixable by morphology);
  - *multi-word descriptive* queries (Q4-type), where normalization changes matching breadth.
- **Sample size / statistics.** At least 25–50 queries (the thesis itself cites the 25-query minimum, p. 132), with paired tests or bootstrap CIs at query level.

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| Verse-level retrieval | Returning the Qur'an verses that answer a query | Retrieval unit = ayah; binary relevance per (query, verse) |
| Keyword-based search (here) | Returns every verse containing the query word(s); no ordering | Unranked Boolean/substring matching (SQL `LIKE '%term%'` in the Ch. 4 pilot) |
| Stemming to root (Malay) | Cutting prefixes/suffixes to get the base word, e.g. *pemakanan* → *makan* | Rule-based affix stripping with dictionary check (Fig. 5.7) |
| Reduplication | Repeating a word to mark plural or variety, e.g. *kucing-kucing* 'cats' | Full, partial or rhyming reduplication (Table 5.2) |
| Circumfix | Prefix + suffix added together around the root, e.g. *ke-raja-an* 'kingdom' | Discontinuous affix pair |
| Stop-words | Very frequent function words ignored in matching | 318-word Malay list (App. A) |
| Ontology | A structured map of concepts, their sub-concepts and relations, linked to verses | OWL classes, properties and instances |
| SPARQL | Query language for ontologies / RDF data | Graph-pattern matching over RDF triples |
| Semantic search (in this thesis) | Looking up a concept in the ontology and returning the verses linked to it | Knowledge-based retrieval; **not** dense/embedding retrieval |
| Precision / Recall (set-based) | Share of returned verses that are relevant / share of relevant verses returned | \|Ret∩Rel\|/\|Ret\|, \|Ret∩Rel\|/\|Rel\| |
| Macro vs micro average | Average of per-query scores vs pooled counts across queries | mean_q(P_q) vs Σ\|Ret∩Rel\| / Σ\|Ret\| |
| Unique relevant hit (project term) | A relevant item found by one channel but not the other | \|(Ret_A ∖ Ret_B) ∩ Rel\| |
| Oracle union (project term) | Best-case recall if both channels' outputs were merged | \|(Ret_A ∪ Ret_B) ∩ Rel\| / \|Rel\| |
| Pooling | Building qrels by judging the union of top results from all compared systems | Standard TREC practice to reduce bias against unjudged documents |

## 19. Open questions / verification needed

1. **Table 7.5 vs Tables 7.4/7.6** (pp. 140–148):
   - Q4 keyword/QA precision 0.25/1.00 vs 1.00/0.25; Q10 keyword precision 1.00 vs 0.75.
   - Text p. 141 gives Q4 MyQOS keyword precision as 0.8571, which equals the semantic value.
   - App. E supports Tables 7.4/7.6. Quote Table 7.6 values only.
2. **Claims vs tables:**
   - "definite improvement at all retrieval points" / "significant differences" for stemming (pp. 145, 168);
   - "double" (Abstract; pp. 147, 170) — actual ×1.69 / ×1.33;
   - "in all cases" (p. 171) — contradicted by Q3, Q5, Q6 and Q10.
3. **Corpus counts:**
   - root words 2,187 (p. 89, Table 5.5) vs 2,817 (pp. 90, 91, 104);
   - verses 6,234 (pp. 35, 68, 78, 156) vs 6,236 (Tables 5.1, 6.3, 7.2);
   - Table 5.6 components sum to 29,940 vs printed 63,191;
   - Table 5.3 stop-word column sums to 24,887 vs printed 28,887;
   - Table 6.1 says "144 chapters".
4. **Qrels:**
   - Q23 has 3 relevant verses in App. D (p. 251) vs 19 in App. E (p. 264). App. D totals 473 vs App. E 489 **[computed]**.
   - App. D lists "38:174" for Q8 (p. 249). Context (not from the thesis): Surah 38 has 88 verses, so this is likely a typo.
   - Which relevance source applies to which query (Pouzi's collection / extra experts / book index / Tafseer Jalalain)? How many judges, and with what agreement?
5. **Semantic search mechanics:** how natural-language queries were turned into SPARQL, and how "keyword-based and ontology-based retrieval results" were combined. Why are Q3 and Q6 recall below keyword if keyword results are included?
6. **QA pipeline:** reduplication handling included (pp. 144, 173) or not (p. 159)? Exact multi-term matching and "sequential … until a result has been achieved" logic? Why does stemming *reduce* |Ret| for Q12 (44 → 17) and Q23 (214 → 6)?
7. **Stemming rules:**
   - Step 7 refers to "Step 6" (p. 89) while the flow diagram says Step 5;
   - Algorithm 1 removes prefix *or* suffix (else-if), although circumfixes are frequent (Table 5.6).
8. **Minor text/label errors:**
   - Q4 is called "Who is Jinn" (p. 140), but Jinn is Q3;
   - cross-references to "Table 7.3" for plots (p. 139), "Appendix C" for results (p. 140; Appendix C is the root-word tagging list) and "Table 4.2" (p. 69; no Table 4.2 exists) point to the wrong objects. (The "Appendix E for query list" reference on p. 133 is correct: App. E lists all 30 queries in Malay and English, pp. 255–265.);
   - Table 5.4 (pp. 87–88) labels prefix+suffix pairs (e.g. *per+an*, *me+kan*) as "infix", whereas the text (p. 86) and Table 5.6 call such pairs circumfixes;
   - the Fig. 7.4 caption claims a three-method comparison but plots only semantic search (p. 149);
   - a survey of 50 Malaysians (p. 96) vs 28 Malaysians (p. 173) — possibly different surveys; not reconciled.
9. Check **CR002173** (Malay Qur'an retrieval) and the author's 2017 *IJASAT* paper "Retrieval Performance for Malay Quran" (listed on p. iv) for the same experiment with fuller reporting. That paper could only be used as a separate record, not to correct the thesis.

## 20. Decision after deep dive

- **Keep current gap?** Yes. v0.8 refined remains valid; see §16.
- **Modify gap?** No change proposed. Optionally add to the evidence-boundary list as a Malay example of confounded, unranked raw-vs-stem + knowledge-based "semantic" search without complementarity analysis (researcher's decision).
- **Add decision?** Proposed for `decisions/DECISIONS.md` (researcher's decision):
  - "Morphology conditions differ in exactly one preprocessing step; stop-words, tokenizer and implementation are held constant";
  - "qrels must not be derived from resources used to build any compared channel; pooled judgments with recorded agreement";
  - "release per-query run files for all channels".
- **Add experiment?** No new experiment. It reinforces two planned protocol checks:
  - a qrels-leakage diagnostic (per-query |Ret| vs |Rel| patterns);
  - intrinsic accuracy of the Uzbek stemmer/lemmatizer on a sample, reported alongside retrieval.
- **Add citation to Chapter I?** Optional, low priority:
  - §1.1: morphology-aware lexical processing in a low-resource affixal language, with small and query-specific effects;
  - §1.3: an example where "semantic" means ontology lookup, not dense retrieval, and where lexical–semantic combination is asserted but not specified or measured.
  - Cite only with the caveats in §12.
- **Proposed `MASTER_INDEX.md` row** (to add after approval):

| MORPH-023 | Nor Diana Binti Ahmad — *Ontological Approach for Semantic Modelling of Malay Translated Qur'an* (PhD, University of Leeds) — [deep dive](deep-dives/2022_Ahmad_Malay_Translated_Quran_Ontology_Retrieval.md) | 2022 | A (source type; low evidential weight) | LOW/MEDIUM | Malay Qur'an verse retrieval: unranked SQL keyword matching (raw) vs the same after a new root stemmer + stop-word removal ("QA search") vs SPARQL ontology lookup ("semantic search"); set-based P/R on 10 expert-judged queries. Stemming changed results on 2/10 queries (mean P 0.5471→0.4971, R 0.5884→0.6027); ontology P/R 0.8409/0.8043 (Table 7.6). No BM25/ranking, no dense retrieval, no specified fusion, no overlap/unique-hit analysis (only derivable lower bounds: ≥4 keyword-only vs ≥49 ontology-only relevant verses). Morphology confounded with stop-word removal and implementation; possible qrels–ontology circularity; many internal numerical inconsistencies (Table 7.5, root counts, App. D vs E). |
