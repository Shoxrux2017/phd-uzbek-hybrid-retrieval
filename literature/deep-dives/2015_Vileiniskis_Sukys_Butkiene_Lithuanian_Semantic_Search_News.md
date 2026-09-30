# Vileiniškis, Šukys & Butkienė (2015): An Approach for Semantic Search over Lithuanian News Website Corpus

**Targeted deep-dive status:** COMPLETED (AI-assisted, pending researcher review)
**Completed:** 2026-09-28
**Literature ID:** `MORPH-019` (assigned 2026-09-28, approved by researcher)
**Systematic-review record:** `CR001735`. Full-text triage: INCLUDE (borderline), reading priority STANDARD, reading tier 1, `carries_complementarity_evidence = YES`. The triage note itself says the YES flag "reflects per-query results only". This card finds **no** complementarity evidence in the project's sense: there is only one retrieval system and no second channel to compare with (see §10, §16, §19).
**Provenance:** AI-assisted deep dive (Claude). The whole paper was read (10 pages, printed pp. 57–66): the pdftotext text plus page images of printed pp. 57 (title page and copyright footer), 60 (Figure 1, Rules I–II), 61 (Figure 2, Rule III, alias heuristics), 64 (Figure 3, Tables 1–2) and 65 (Table 3, observations, conclusions). Every number from Tables 1–3 was compared with the page image. Numbers computed by us are marked **[computed]** and were computed in Python.
**Source rule:** **the paper is the primary and only authoritative source.** Web lookup was used only for the bibliographic record (§1). The project website named in the paper (p. 65) was not consulted. Nothing is concluded about the authors' work from outside sources.
**Verification:** independent AI verifier pass 2026-09-28; 3 findings addressed.
**Reliability:** **B.** It is a conference paper in SciTePress proceedings (IC3K 2015, Volume 1: KDIR), as the paper's own copyright footer states (p. 57). The **evidence is very narrow**: an author-judged case study with 4 queries, no baseline, no ranking and no significance testing.

---

## Кратко для исследователя (RU)

- **Что сделано.** Прототип «семантического поиска» по литовским новостям в смысле Semantic Web, а не плотного векторного поиска:
  - конвейер извлечения информации (IE): токенизация и удаление стоп-слов → морфологический анализатор (POS, лемма, число, падеж) → NER по газеттирам → правила, заполняющие онтологию RDF-триплетами;
  - вопрос пользователь пишет на «структурированном литовском» (SBVR), вопрос автоматически переводится в SPARQL;
  - по найденным сущностям строится фрагмент текста (snippet).
  Корпус: более 90 000 документов с 30+ порталов, около 44 млн явных и 49 млн выведенных RDF-триплетов (Sec. 4, p. 63).
- **Где морфология:**
  - варианты имени одной сущности (в том числе падежные: *Daliai Grybauskaitei*, *Dalią Grybauskaitę*) объединяются по общей лемме в одну «доверенную» сущность (Sec. 3.1, p. 61);
  - понятия в вопросе сопоставляются по лемме (Sec. 3.2, p. 62);
  - в одном правиле извлечения проверяется родительный падеж (Rule III, p. 61).
  **Ни один из этих шагов не отключается экспериментально** (нет ablation), поэтому их вклад в результат не измерен.
- **Главные числа** (Table 2, p. 64; точность и полнота фрагментов по каждому запросу):
  - Q1 «Что говорили агенты?»: P = 0.934, R = 0.456;
  - Q2 «Что говорил Владимир Путин?»: P = 0.885, R = 0.486;
  - Q3 «Кто работает в организациях?»: P = 0.971, R = 0.493;
  - Q4 «Кто работает в Европарламенте?»: P = 1.000, R = 0.816.
  Среднее по 4 запросам: P ≈ 0.948, R ≈ 0.563 **[computed]**.
- **Как измерено:**
  - всего 4 запроса; оценивали сами авторы; число асессоров и согласие не указаны;
  - полнота считалась только на «рабочем подмножестве» уже просмотренных статей, так как полный набор ответов неизвестен (p. 64);
  - формула полноты в статье не дана.
- **Внутреннее несоответствие (наша реконструкция).** Формула R = A_FC / (A_F + A_NF) точно воспроизводит Q1, Q2 и Q4, но для Q3 даёт 0.531 вместо напечатанных 0.493. Значение 0.493 получилось бы при A_NF = 69, а напечатано 59 **[computed]**. Из статьи не решить, где ошибка.
- **Чего в работе нет:**
  - BM25 или иной ранжирующей лексической модели; есть только SPARQL-запрос с булевой логикой, без ранжирования (p. 63, p. 65);
  - вариантов лексического представления (raw/stem/lemma);
  - плотного или нейронного поиска;
  - гибрида или fusion;
  - перекрытия, уникальных находок или oracle union;
  - сравнения с ключевым поиском, хотя авторы заявляют о преимуществе над ним (качественно, p. 65).
  «Значимые результаты» в аннотации — словесная оценка, статистических тестов нет.
- **Уточнения к триажу:**
  - лемматизатор Lemuoklis в статье упоминается только в обзоре (p. 58); какой анализатор реально использован в конвейере, не сказано;
  - флаг complementarity = YES по сути не подтверждается.
- **Для нашего gap:** **нет существенного влияния.** Работа не касается ни одного элемента ядра v0.8. «Семантический поиск» здесь означает онтологию и SPARQL, это не семантический канал в нашем смысле.
- **Практическая польза:**
  1. Хорошо сформулированная мотивация: падежное словоизменение имён собственных снижает полноту по запросам с именами (утверждение авторов, не измерено). Это поддерживает признак запроса «именованная сущность с падежным аффиксом» в нашей таксономии.
  2. Пример того, чего избегать в оценке: полнота на неполном наборе ответов, формулы метрик не приведены.
  3. Терминологическая осторожность в главе I: «semantic search» в смысле онтологий ≠ плотный поиск.

---

## 1. Bibliographic record

- **Authors:** Tomas Vileiniškis, Algirdas Šukys, Rita Butkienė
- **Affiliation:** Department of Information Systems, Kaunas University of Technology, Kaunas, Lithuania (p. 57)
- **Year:** 2015
- **Venue:** *Proceedings of the 7th International Joint Conference on Knowledge Discovery, Knowledge Engineering and Knowledge Management (IC3K 2015) — Volume 1: KDIR*, pages 57–66 (the paper's own footer, p. 57)
- **Publisher:** SCITEPRESS – Science and Technology Publications, Lda. (footer, p. 57)
- **ISBN:** 978-989-758-158-8 (footer, p. 57)
- **DOI:** `10.5220/0005596800570066` (bibliographic check: SciTePress record and KTU eLABa record, epubl.ktu.edu/object/elaba:17016155; not printed in the paper)
- **Conference location / dates:** Lisbon, Portugal, 12–14 November 2015 (bibliographic check: KTU eLABa record; location also on the SciTePress record)
- **IEEE Xplore:** the assignment metadata lists the record as "IEEE Conferences". A search result shows an IEEE Xplore document 7526903 with this title. Its page could not be retrieved, so the IEEE record details are **not verified** (bibliographic check attempted: ieeexplore.ieee.org).
- **Source type:** conference proceedings paper (full paper, 10 pages)
- **Reliability:** B
- **Full text available:** yes (`07_full_text/pdfs/CR001735.pdf`, 10 pages)

## 2. Why this work matters to the PhD

It is an early example of retrieval over a **highly inflected, resource-poor language** (Lithuanian: Baltic, fusional case morphology) in which lemmatization and grammatical case are used explicitly. The paradigm, however, is **ontology-based, Boolean** data retrieval plus snippet generation, not ranked document retrieval.

| Axis | Relation |
|---|---|
| Lexical retrieval | **Absent** as a ranked model. No BM25, TF-IDF or keyword baseline. The only retrieval step is SPARQL matching over RDF extracted from text (Sec. 3.2) |
| Semantic retrieval | "Semantic search" in the **Semantic Web sense** (ontology, RDF, SPARQL, OWL reasoning). No embeddings, no dense retrieval |
| Hybrid retrieval | **Absent** |
| Uzbek morphology | Indirect. Lithuanian is fusional, Uzbek is agglutinative. Both mark case with suffixes on names, e.g. Lithuanian *Grybauskaitei* (dative); cf. Uzbek *Toshkentda* (locative) — Context (not from the paper) |
| Low-resource retrieval | Direct motivation: few NLP resources for Lithuanian, and no production-ready parser (Sec. 2–3.1) |
| Current gap | No material effect (§16) |

## 3. Research problem

### Simple explanation

Keyword search returns whole documents and cannot answer a question such as "Who works in the European Parliament?" directly. The authors want to extract facts (who said what, who works where) from Lithuanian news into a knowledge base, let users ask structured questions, and return the text fragment that answers each one. Lithuanian makes this hard: names and nouns change their endings by grammatical case, and word order is free.

### Formal formulation

- The paper states no formal research questions.
- The aim is stated in the conclusions: "to show that meaning-based information retrieval methods can be successfully applied even for resource-poor, highly inflected languages like Lithuanian" (Sec. 5, p. 65).
- Task as implemented: a structured natural-language question → a SPARQL query `Q` over the RDF graph `G`. The answer set is the set of bindings of the projection variables `V` that satisfy all triple patterns. Each binding tuple is mapped back to a sentence-level snippet of a document `d`.

## 4. Main idea

### Simple explanation

1. Read every news article with a chain of language tools.
2. Rules turn sentences into facts, e.g. "Person X said Y" or "Person X works in Organization Z".
3. Store the facts in a knowledge graph, each with a link to the exact place in the article where it was found.
4. The user writes a question in a controlled form of Lithuanian, with auto-complete suggestions.
5. The question is translated into a database query. Every matching fact is returned together with the sentence it came from.

### Concrete example

- Question: *Kas dirba Europos Parlamente?* ("Who works in the European Parliament?"; Table 1, Q4, p. 64).
- It becomes a SPARQL query asking for persons linked by the "works in" relation to the trusted entity *European Parliament*. Through `recognized_as_trusted_object` it also matches all merged aliases of that entity (Sec. 3.2, p. 63).
- Figure 3 (p. 64) shows returned snippets in which the organization appears as *Europos Parlamento* (genitive), while the question uses *Europos Parlamente* (locative). This is our reading of the printed figure: matching is across case forms of the entity, because both forms resolve to one trusted instance.
- Example of the case check (Rule III, p. 61): in *Europos Parlamente prezidentė Dalia Grybauskaitė skaitė pranešimą* ("President Dalia Grybauskaitė gave a speech at the European Parliament"), *Parlamente* is locative. Without the genitive check, the rule would wrongly assert *works_in⟨Grybauskaitė, European Parliament⟩*.

### Formal method

- **Extraction rules**: lexico-semantic patterns over token, POS/case and NE annotations, of the form `pattern & constraints ⇒ assert(triples)`. Example (Rule III):
  `<NE1> <PNOUN> <NE2> & type(NE1)=Organization & type(NE2)=Person & caseMark(NE1)=genitive ⇒ assert(c1:Organization, c3:Person, works_in<c3,c1>)`.
- **Query model**: SBVR question → SBVR XMI → (ATL model-to-model transformation) → SPARQL XMI → textual SPARQL (Sec. 3.2, p. 62).
- **Retrieval semantics**: conjunctive basic graph pattern. The authors say the IR phase "operates in a Boolean manner" (Sec. 4, p. 65). There is **no scoring or ranking function**. An ORDER BY by publication date was considered but dropped, because "the ordering cost proved to be too high on a larger dataset" (p. 63).

## 5. Architecture / algorithm

From Figure 1 (p. 60) and Sec. 3.1–3.2:

1. **Web crawling → corpus storage** (Lithuanian news portals).
2. **NLP pipeline** (Sec. 3.1, p. 59):
   - *Lexical analyzer*: "stop word removal and standard text tokenization".
   - *Morphological analyzer*: "assigns part-of-speech (POS) tags to each of the word along with lemma, grammatical number and most importantly grammatical case". **The tool is not named.** Lemuoklis (Zinkevičius, 2000) is cited only in Related Work (p. 58) as "the first Lithuanian lemmatizer and part-of-speech (POS) tagger". The authors say the first three components are "beyond the scope of this paper" (p. 60).
   - *NER*: "based on gazetteer lookups"; types are organizations, locations and persons.
   - *Semantic annotator*: rule-based. The ruleset targets political and economic events, with reporting-verb patterns (Rules I–II), a position/organization pattern (Rule III) and "over 20 patterns for detecting changes of prices, taxes and other abstract objects" (p. 61).
   - Annotations are stored stand-off, in JSON.
3. **Ontology** (Figure 2, p. 61): event ontology with "over 100 classes and nearly 70 relations". Documents are linked to objects by `:refers_to_object`.
4. **Entity alias merging** (Sec. 3.1, p. 61). This is where morphology enters the index. Three heuristics, iterated per NE type:
   - "we find equal entities by a common lemma and abbreviation matches";
   - "we determine the main alias behind the trusted entity by inflecting its nominative case, and then create a new instance T";
   - all corresponding entities are linked to T via `:recognized_as_trusted_object`.
   The ontology is also pre-populated with well-known trusted entities and their main aliases.
5. **Question side** (Sec. 3.2, p. 62):
   - questions are constrained by EBNF with contextual suggestions;
   - the SBVR vocabulary maps to OWL classes and properties;
   - inflection is handled by referring to concepts "by their main grammatical form – lemma";
   - "grammatical case-based matching" lets the user omit the subject;
   - singular and plural forms are managed "similarly".
6. **SPARQL construction** (p. 63): type triple patterns T1/T2 are generated for each projected variable. For proper-name queries, `recognized_as_trusted_object` patterns are added "thus giving higher recall". Each projected variable must be bound to one document `d`, and a document id `k` is projected.
7. **Snippet generation** (p. 63): take the token spans of all bound URIs, compute min(b) and max(e), extend to a full sentence (or to neighbouring sentences), and return the passage.

## 6. Data

- **Corpus:** "over 90.000 domain specific documents from more than 30 news portals" (Sec. 4, p. 63). Domains are politics and economics (Sec. 1, p. 58).
- **Language:** Lithuanian.
- **Knowledge base:** "around 44 million explicit and 49 million implicit RDF triples under OWL-Horst materialization settings" (p. 63).
- **Queries:** 4, chosen by the authors: "2 abstract ones and 2 with proper names involved" (Sec. 4, pp. 63–64; queries listed in Table 1, p. 64). Q1 and Q2 are agent–substance ("say") queries; Q3 and Q4 are person–organization ("works in") queries.
- **Units judged:** text snippets, not documents. "Queries Q1, Q2 and Q3, Q4 were assessed by manually evaluating 61 and 71 snippets respectively" (p. 64). The number of analysed articles "differs per query and ranges from 12 to 65" (p. 64); per-query article counts are **NOT_REPORTED**.
- **Relevance judgments:** two criteria (p. 64):
  1. does the snippet give a correct answer;
  2. are the answer-related entities correctly highlighted.
  The assessors appear to be the authors ("We then judged", p. 64). The number of assessors, guidelines and agreement are **NOT_REPORTED**.
- **Recall ground truth:** "a full set of correct answers to each of the queries is not known in advance. Therefore, we calculated recall only on a working subset of articles, i.e. those that had their snippets evaluated" (p. 64). Missed answers were collected by reading those articles.
- **Train/dev/test:** not applicable; the extraction rules are hand-written. Whether the rules were written on the same articles used for evaluation is **NOT_REPORTED**.
- **Public data release:** NOT_REPORTED (a prototype URL is given, p. 65).

## 7. Baselines

**None.** No keyword/Boolean, TF-IDF, BM25 or other system is run for comparison.

The paper claims an advantage of the "semantic search paradigm when compared to classical pure keyword-based approaches" (p. 65). That claim is qualitative: it rests on one-step answer presentation, not on a measured comparison.

## 8. Metrics

| Metric | Definition in paper | Simple meaning here | Appropriate? |
|---|---|---|---|
| Precision (Table 2) | Not given as a formula. It is reproduced by A_FC / A_F **[computed]** | Share of judged snippets that correctly answer the question | Reasonable for a set-based (Boolean) system; no ranking is evaluated |
| Recall (Table 2) | Not given as a formula. It is computed "only on a working subset of articles" | Share of answers in the examined articles that the system found | **Weak.** The reference set is limited to articles the system already returned, so answers in never-returned articles are invisible. The formula is unstated; see §9 for our reconstruction |
| P_AP, P_SO (Table 3) | A_AP / A_FC and A_SO / A_FC **[computed]** | Correct highlighting of the agent/person and substance/organization entities within correct snippets | Extraction-quality measure, not a retrieval measure |

Column legend (p. 64): A_F = snippets analysed; A_FC = snippets with correct answer; A_NF = not-found snippets; A_AP / A_SO = correctly highlighted agent/person and substance/organization entities. The Table 3 text also calls A_FC "the total number of snippets analysed" (p. 64). In Table 3 this means the correct snippets from Table 2 (same values), which is consistent.

No rank-based metric (MAP, nDCG, MRR, P@k) is used, and none would apply to an unranked Boolean result set.

## 9. Results

### Table 2: text snippet accuracy (p. 64; checked on the page image)

| # | Query (English as given) | A_F | A_FC | A_NF | Recall | Precision |
|---|---|---:|---:|---:|---:|---:|
| Q1 | What did the agents say? | 61 | 57 | 64 | 0.456 | 0.934 |
| Q2 | What did Vladimir Putin say? | 61 | 54 | 50 | 0.486 | 0.885 |
| Q3 | Who work in organizations? | 71 | 69 | 59 | 0.493 | 0.971 |
| Q4 | Who works in the European Parliament? | 71 | 71 | 16 | 0.816 | 1.000 |

**Recomputations [computed]:**
- Precision = A_FC / A_F reproduces all four: 0.9344, 0.8852, 0.9718, 1.000. For Q3 the printed 0.971 is a truncation of 0.9718, not a rounding (0.972).
- **Recall reconstruction and inconsistency.** The formula is not stated. R = A_FC / (A_F + A_NF) reproduces Q1 (57/125 = 0.456), Q2 (54/111 = 0.4865) and Q4 (71/87 = 0.816) exactly.
  - For Q3 it gives 69/130 = **0.531**, not the printed **0.493**.
  - 0.493 = 69/140 would require A_NF = 69 instead of the printed 59. The alternative formula A_FC / (A_FC + A_NF) gives 0.539 for Q3, so it does not explain the value either.
  - Either A_NF or the Q3 recall is misprinted, or a different formula was used for Q3. The paper does not allow a decision.
  - Note: the reconstructed formula puts *incorrect* snippets (A_F − A_FC) into the denominator of recall. This is unusual. We present it as a reconstruction, not as the authors' stated definition.
- Macro-averages over the 4 queries: P = 0.948, R = 0.563. Micro precision = 251/264 = 0.951. The paper reports no averages.

**Authors' interpretation** (p. 64): "most of the queries achieve very high precision rates, Q2 stands out with a bit lower results". The Q2 errors come from indirect-quotation extraction, where patterns "can't differentiate between the reporting agent and other agents contextually related to the reported substance". Also: "Relatively low recall values indicate that our current domain-specific event extraction ruleset is capable of capturing only the most common event expressions."

### Table 3: entity highlighting accuracy (p. 65; checked on the page image)

| # | A_FC | A_AP | A_SO | P_AP | P_SO |
|---|---:|---:|---:|---:|---:|
| Q1 | 57 | 36 | 53 | 0.632 | 0.930 |
| Q2 | 54 | 54 | 51 | 1.000 | 0.944 |
| Q3 | 69 | 69 | 69 | 1.000 | 1.000 |
| Q4 | 71 | 71 | 71 | 1.000 | 1.000 |

- All ratios are reproduced as A_AP / A_FC and A_SO / A_FC **[computed]**: 36/57 = 0.6316, 53/57 = 0.9298, 51/54 = 0.9444.
- Authors' explanation for Q1's low P_AP (p. 65): the abstract *Agent* class is also instantiated by "domain list-guided noun lookups". The remedy they propose is that "noun phrase mining should be improved by taking into account more Lithuanian morphological features".

### Reading the per-query pattern (our inference, not the authors')

- The highest recall (Q4, 0.816) is for the proper-name "works in" query. This is **compatible** with the alias-merging heuristic helping proper-name recall, but it is **not evidence** for it:
  - n = 1 query;
  - there is no run without alias merging;
  - the other proper-name query (Q2) has recall 0.486, below Q3's 0.493;
  - query type (say vs works-in) and name presence are confounded.

## 10. Statistical evidence

- **Significance test:** NOT_REPORTED. The abstract's "significant results" is not a statistical claim.
- **Confidence intervals:** NOT_REPORTED.
- **Runs / seeds:** not applicable (deterministic rule-based system); one evaluation.
- **Ablation:** NOT_REPORTED. None of the following is switched off or varied:
  - lemma-based alias merging;
  - the genitive-case check;
  - lemma-based concept matching;
  - stop-word removal.
  (The project's Clarification 001 A, cited in the triage note, says ablation is not required for inclusion. It is still required before any *effect* of morphology can be claimed.)
- **Per-query analysis:** yes, but only for one system. Tables 2–3 are per query (n = 4), with qualitative error sources. There is:
  - no second channel;
  - no overlap or unique-hit analysis;
  - no oracle union;
  - no query-feature analysis beyond the "abstract vs proper name" labels.

## 11. Strengths

- A complete, working end-to-end prototype at realistic corpus scale (90K+ documents, ~93M triples including inferred ones, 44M + 49M **[computed]**) for a low-resource, inflected language.
- A clear description of **where** inflection breaks a naive pipeline, with concrete Lithuanian examples:
  - case-marked name variants split one entity into many;
  - locative vs genitive changes the extracted relation;
  - verb government changes a concept's surface form in the question (*organizacija* → *organizacijoje*, p. 62).
- Explicit lemma-level normalization at both the index side (entities) and the query side (SBVR concepts).
- Honest error analysis that attributes errors to IE components (indirect quotations, noun-phrase mining, no syntactic parser).
- The authors state openly that recall is computed on a partial reference set (p. 64).

## 12. Limitations

### Stated by the authors

- The recall ground truth is incomplete ("a full set of correct answers … is not known in advance"; p. 64).
- Low recall reflects a ruleset that captures "only the most common event expressions" (p. 64).
- No syntactic parser for Lithuanian; free word order makes pattern-based event extraction hard (p. 65).
- Precision depends on IE quality, because the IR phase is Boolean (p. 65).
- Result ordering by date was too costly (p. 63).
- Porting to other domains needs customized business vocabularies and ontologies (p. 65).
- The evaluation is an "early evaluation" / "case study" and is "summed up on a qualitative note" (pp. 63, 65).

### Inferred from the experimental design

1. **Four queries**, chosen by the authors, judged by the authors. No generalization is possible, and no statistical test would be meaningful.
2. **No baseline at all.** The claimed advantage over keyword search is untested.
3. **Morphology is not isolated.** Lemma alias merging, lemma concept matching and case checks are built in and never ablated. Their contribution to precision or recall is unknown.
4. **Retrieval is unranked set matching.** The results cannot be compared with ranked-retrieval metrics (MAP/nDCG/Recall@k) or with BM25/dense systems.
5. **The recall definition is unstated** and our reconstruction does not fit Q3 (§9). The reference set covers only articles the system already surfaced, so recall is an upper-biased, system-dependent estimate.
6. **Snippet-level judging with unequal unit counts** (61/61/71/71 snippets; 12–65 articles per query). The high values for Q3/Q4 may partly reflect their simpler person–organization structure (our inference). The authors' "strictly following NE tags" (p. 65) explains the near-perfect *entity-highlighting* scores of Q2–Q4 in Table 3, not the Table 2 precision.
7. **Possible overlap between rule development and evaluation material.** Reporting verbs were "collected … from the news articles" (p. 60); whether the evaluated articles were excluded is not reported.
8. The morphological analyzer and the lemma/case accuracy of the pipeline are not reported.

## 13. What the work proves

- An ontology-based, SPARQL-backed question-answering search over a large Lithuanian news corpus **can be built and run**, with lemma-based entity normalization and case-sensitive extraction rules (Sec. 3–4).
- For the 4 author-selected queries, the returned snippets were **mostly correct**: precision 0.885–1.000 (Table 2, p. 64). Recall on the examined articles is **moderate** for three queries (0.456–0.493) and higher for one (0.816).
- For the abstract *Agent* query (Q1), entity highlighting is the weak point (P_AP = 0.632; Table 3, p. 65).

## 14. What the work does NOT prove

- **That lemmatization or case handling improves retrieval.** There is no with/without comparison.
- **That this "semantic search" beats keyword search.** No keyword system was evaluated.
- **Anything about lexical ranking models** (BM25, TF-IDF) or about raw/stem/lemma lexical representations.
- **Anything about dense or embedding-based semantic retrieval.** "Semantic" here means ontology/RDF/SPARQL.
- **Anything about hybrid retrieval or lexical–semantic complementarity.** There is one system, so overlap, unique relevant hits and oracle union are undefined.
- **That proper-name inflection hurts recall by a measurable amount.** The authors state it as motivation (p. 61); it is not measured.
- **General effectiveness.** With n = 4 queries, author judgments and an incomplete recall reference, none of the numbers is a stable estimate. The abstract's "significant results" has no statistical backing.

## 15. Relationship to current Uzbek evidence

- **No Uzbek data.** Lithuanian (Baltic, fusional) and Uzbek (Turkic, agglutinative) differ typologically. They share **case suffixes on proper names and nouns**, which split one entity into many surface forms — the phenomenon the paper handles by lemma-level alias merging.
- **Closest national analogue: ontology-based Uzbek search/RAG.** O-RAG (UZ-HYB-002; ontology + hybrid retrieval + ontology-based reranking) is the closest match. This Lithuanian paper is an older, pre-neural instance of "ontology as the semantic component", with no lexical–dense integration.
- **Uzbek morphology/search infrastructure.** The national works (Bakaev: morphology-based full-text search, MORPH-UZ-001/002; Elov: lemma-based inverted indexing, MORPH-UZ-007) also show morphology **deployed inside** a search system without controlled IR evaluation. This paper follows the same pattern for Lithuanian: morphology is built in, effect not isolated, no qrels-based ranked evaluation.

## 16. Relationship to CURRENT_GAP

**Classification:** *no material effect.*

- v0.8 refined elements touched: **none**. The paper has:
  - no BM25_raw/stem/lemma;
  - no fixed dense comparator D;
  - no fusion;
  - no unique relevant hits, overlap, oracle union or incremental hybrid gain;
  - no link between query features and complementarity change.
- The only point of contact is thematic: morphological normalization (lemma) of **named entities** motivated by recall loss on proper-name queries. This is consistent with keeping "named entities" in the candidate query-feature list of v0.8, but it adds no evidence about complementarity.
- It does not affect any item in "What can still kill this gap" (not Uzbek, not Turkic, not a lexical–dense interaction study).

**Proposal:** keep v0.8 refined unchanged. There is no need to add this paper to the evidence-boundary list, except perhaps as a background example that "semantic search" in the Semantic Web sense ≠ dense semantic retrieval. This is a proposal only; `CURRENT_GAP.md` has not been edited.

## 17. Implications for our research design

- **Query taxonomy.**
  - Keep and operationalize "named entity with case/possessive suffix" as a candidate query feature. For Uzbek this means, e.g., *Toshkentda*, *Mirziyoyevning*, *Oliy Majlisga* (Context, not from the paper).
  - The paper's motivation (inflected names lower recall of name queries, p. 61) is a stated hypothesis we can test **per query**: do stem/lemma BM25 variants recover more unique relevant documents for such queries than raw BM25?
- **Morphology preprocessing (optional idea, not a decision).**
  - Entity-level alias normalization (merging inflected and abbreviated name variants to one canonical form) is a distinct representation from token-level stemming or lemmatization.
  - If Uzbek lemmatizers handle proper names poorly, a check of name lemmatization quality is worth adding to the preprocessing audit.
  - Adding an "entity-normalized" lexical variant would go beyond v0.8's raw/stem/lemma design, so it should only be considered after the pilot.
- **Qrels and metrics.**
  - Avoid this paper's evaluation weaknesses:
    - define every metric formula explicitly;
    - do not compute recall on a reference set built only from the evaluated system's own output;
    - use pooled judgments over **all** channels (raw/stem/lemma BM25, D, hybrids). Otherwise unique-hit counts are biased toward the pooled systems.
  - Judge documents (or fixed passages), not system-generated snippets.
- **Baselines.** Any "semantic" component we cite or use must be classified: ontology/KG-based (as here) vs dense retrieval-trained (D). They are not interchangeable in the v0.8 design.
- **Hypothesis.** No evidence for or against our hypothesis.

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| Semantic search (Semantic Web sense) | Search over facts stored in a knowledge graph instead of over words | Querying RDF/OWL knowledge bases (here with SPARQL) populated from text; ≠ dense semantic retrieval |
| Information extraction (IE) | Automatically turning sentences into structured facts | Mapping text to entities and relations (here RDF triples) |
| Ontology population / A-Box | Adding concrete facts (instances) to a predefined schema | Instance assertions for the T-Box classes and properties |
| RDF triple | A fact of the form subject–predicate–object | ⟨s, p, o⟩ in an RDF graph |
| SPARQL | A query language for knowledge graphs | W3C query language; a basic graph pattern is a conjunction of triple patterns |
| SBVR | A standard for writing business concepts and rules in controlled natural language | OMG metamodel; here used for structured questions transformed to SPARQL |
| Model-to-model (M2M) transformation | Automatic conversion of one formal model into another | ATL transformation SBVR XMI → SPARQL XMI |
| Boolean retrieval | A document or fact either matches all conditions or not; no ranking | Set-based matching without a scoring function |
| Lemma | The dictionary form of a word | Canonical form from morphological analysis (e.g., nominative singular for nouns) |
| Grammatical case | A word's ending shows its role in the sentence (in, of, to…) | Inflectional category (genitive, locative, dative, …) |
| Alias merging / trusted entity | Treating all spellings and inflected forms of a name as one entity | Heuristic entity resolution by common lemma and abbreviation → canonical instance T |
| Gazetteer-based NER | Finding names by looking them up in lists | Dictionary-lookup named-entity recognition |
| Complementarity (project term) | Each channel finds some relevant documents the other misses | Unique relevant hits, overlap, oracle-union gain; not applicable here (one system) |

## 19. Open questions / verification needed

1. **Q3 recall 0.493 vs reconstructed 0.531** (Table 2, p. 64). Is A_NF = 69 (misprint of 59) or is the recall misprinted? Only the authors can confirm. The recall formula itself is NOT_REPORTED.
2. **Which morphological analyzer was used** in the pipeline (not named; Lemuoklis is cited only in Related Work, p. 58)? The triage summary's "lemmatizer Lemuoklis" should be treated as **unverified**.
3. **Triage flag correction (proposal):** `carries_complementarity_evidence` should arguably be **NO** in the project's sense. There is one system and no lexical–semantic channel comparison; the per-query tables do not constitute complementarity evidence.
4. Per-query article counts (12–65), assessor identity and number, and judging guidelines are NOT_REPORTED.
5. Were the evaluated articles disjoint from those used to derive the extraction rules? NOT_REPORTED.
6. IEEE Xplore record (document 7526903) details were not retrievable. The DOI and pages are verified via SciTePress and KTU eLABa only.
7. Did any later work by the same KTU group add a keyword/BM25 baseline, or ablate lemma alias merging? This is for literature search only; it cannot be used to change this card.

## 20. Decision after deep dive

- **Keep current gap?** Yes. v0.8 refined is unaffected (§16).
- **Modify gap?** No.
- **Add decision?** Optional, researcher's decision. "All metrics (especially recall) must have explicit formulas, and the recall reference set must come from pooled judgments across all compared channels, never from a single system's output." This is already implied by existing protocol thinking; this paper is a concrete negative example.
- **Add experiment?** No new experiment. In the planned per-query analysis, include a named-entity-with-case-suffix query subset (already covered by v0.8's candidate features).
- **Add citation to Chapter I?** Optional and minor:
  - §1.2, as an example that "semantic search" in the Semantic Web tradition (ontology/SPARQL) differs from dense semantic retrieval;
  - background on morphology-aware processing for inflected low-resource languages (lemma-based entity normalization motivated by case inflection of names).
  It must not be cited as evidence of retrieval effectiveness.
- **Proposed `MASTER_INDEX.md` row** (to add after approval; section C as LOW-priority background):

| MORPH-019 | Vileiniškis, Šukys, Butkienė — *An Approach for Semantic Search over Lithuanian News Website Corpus* (IC3K/KDIR 2015, SciTePress, pp. 57–66, DOI 10.5220/0005596800570066) — [deep dive](deep-dives/2015_Vileiniskis_Sukys_Butkiene_Lithuanian_Semantic_Search_News.md) | 2015 | B | LOW | Ontology/SPARQL (Semantic Web) search over 90K+ Lithuanian news documents; rule-based IE with POS/lemma/case analysis; inflected name variants merged to one entity by common lemma; lemma-based concept matching in structured questions. Boolean, unranked; no BM25/keyword baseline, no dense retrieval, no fusion, no ablation of morphology. Author-judged 4-query case study: snippet precision 0.885–1.000, recall 0.456–0.816 on a partial reference set (Q3 recall not reproducible from printed counts). "Semantic search" ≠ dense retrieval; no complementarity evidence. |
