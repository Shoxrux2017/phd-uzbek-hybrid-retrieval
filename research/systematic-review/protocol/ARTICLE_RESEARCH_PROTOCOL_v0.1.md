# ARTICLE RESEARCH PROTOCOL v0.1

**Project:** PhD — Uzbek Hybrid Information Retrieval  
**Protocol date:** 2026-09-16  
**Status:** WORKING / PRE-SEARCH PROTOCOL  
**Primary target journal:** ACM Transactions on Asian and Low-Resource Language Information Processing (TALLIP)  
**Fallback target:** Natural Language Processing (Cambridge University Press)  
**Article type:** Systematic review / systematic evidence synthesis  
**Relationship to PhD:** Independent review article supporting, but not duplicating, the dissertation literature chapter and the future controlled Uzbek retrieval experiment.

---

## 1. Working article concept

### Recommended working title

**Morphological Representation in Information Retrieval for Morphologically Rich Languages: A Systematic Review of Lexical, Dense, and Hybrid Retrieval with an Uzbek Perspective**

### Strong alternative

**From Morphological Normalization to Lexical–Dense Complementarity: A Systematic Review of Information Retrieval in Morphologically Rich and Low-Resource Languages**

### More TALLIP-oriented alternative

**Morphology-Aware Information Retrieval for Asian and Low-Resource Languages: Evidence from Lexical, Dense, and Hybrid Retrieval with an Uzbek Perspective**

### Title decision

Use the first title during the review.  
Do **not** finalize a claim such as “the first systematic review” until the full systematic search and novelty audit have been completed.

---

## 2. Why this article is scientifically justified

The PhD repository already establishes a narrower residual research problem than a generic “low-resource information retrieval” problem.

The current PhD gap is not:

- whether stemming or lemmatization can improve retrieval;
- whether BM25 or dense retrieval is better;
- whether sparse+dense hybrid retrieval exists;
- whether query-adaptive fusion exists.

Instead, the surviving research question concerns whether changing the morphological representation of the lexical channel changes:

1. the relevant documents retrieved by lexical search;
2. its overlap with a fixed dense retriever;
3. the lexical-only and dense-only relevant documents;
4. the candidate-set headroom / oracle union;
5. the incremental gain of the hybrid condition.

The review article should therefore examine **how existing research has actually connected morphology to retrieval evidence**, rather than merely cataloguing stemmers, language models, or retrieval architectures.

---

## 3. Positioning against existing reviews

### 3.1 Kazi, Khoja & Daud (2025)

**Work:** *Bridging the gap: A survey of document retrieval techniques for high-resource and low-resource languages*, Computer Science Review 57, 100756.  
**DOI:** 10.1016/j.cosrev.2025.100756.

This is the closest recent broad review. It covers:

- traditional retrieval;
- neural/dense retrieval;
- hybrid retrieval;
- low-resource retrieval challenges;
- datasets and benchmarks;
- mainly Arabic, Urdu and Hindi in the low-resource part.

Our article must **not** repeat this scope.

### Difference of the proposed article

The proposed review is centered on:

> explicit morphological representation/intervention × corpus-level retrieval paradigm × evidence type.

It will ask whether morphology is treated as:

- raw surface forms;
- stems;
- lemmas;
- roots;
- morphemes;
- morphological segmentation;
- morphology-aware expansion;
- orthographic/script normalization;
- subword-aware representation,

and how those choices interact with:

- classical lexical retrieval;
- learned sparse retrieval;
- dense bi-encoder retrieval;
- late interaction / multi-vector retrieval;
- hybrid lexical–dense retrieval;
- reranking/RAG retrieval when retrieval itself is separately evaluated.

The article also includes a dedicated Uzbek/Turkic evidence layer, which is absent from the core focus of the Kazi et al. review.

---

### 3.2 Roy, Anas & Kandasamy (2026)

**Work:** *Stemming Techniques for Resource-Poor Languages: A Review of Methods, Challenges, and Applications*, Frontiers in Artificial Intelligence, 2026.  
**DOI:** 10.3389/frai.2026.1875268.

This review is centered on stemming methods and their applications across NLP tasks.

### Difference of the proposed article

Our unit of analysis is not the stemmer.

Our unit of analysis is:

> **retrieval evidence produced when morphological representation is changed.**

Therefore, a stemming paper is relevant only when it evaluates or materially specifies an information-retrieval condition.

The proposed article also compares stemming with lemmatization, raw forms and other representations, and explicitly follows the transition from lexical to dense and hybrid retrieval.

---

### 3.3 Older stemming-in-IR surveys

Older reviews such as *A survey of stemming algorithms in information retrieval* are important historical references but predate the modern dense/hybrid retrieval landscape.

The proposed review will connect the classical morphology-aware IR literature with the post-2020 dense/hybrid retrieval era.

---

## 4. Planned scientific contribution

The article should make five contributions.

### C1. Morphology–retrieval taxonomy

Create a taxonomy crossing three dimensions:

**A. Morphological representation**

- raw / surface form;
- stem;
- lemma;
- root;
- morpheme segmentation;
- character/prefix truncation;
- subword representation;
- morphology-aware expansion;
- orthographic normalization;
- script transliteration.

**B. Retrieval paradigm**

- lexical/statistical;
- learned sparse;
- dense bi-encoder;
- late interaction / multi-vector;
- hybrid lexical–semantic;
- reranking;
- RAG retrieval, only where the retrieval stage is separately evaluable.

**C. Evidence target**

- aggregate retrieval effectiveness;
- index/storage efficiency;
- per-query behavior;
- relevant-set composition;
- lexical–dense overlap;
- unique relevant hits;
- oracle union;
- fusion gain;
- query-characteristic interaction.

---

### C2. Evidence ladder for morphology-aware retrieval

Each included study will be classified by the strongest level of retrieval evidence it provides.

**Level 0 — Contextual morphology evidence**

Morphological analyzer/resource/search infrastructure is described, but there is no corpus-level IR effectiveness experiment.

Examples may include analyzer accuracy, language-resource construction, indexing infrastructure or workflow improvements.

**Level 1 — Morphology-aware lexical retrieval**

At least two morphological representations or preprocessing variants are evaluated with a lexical/statistical retriever.

Example pattern:

`raw BM25 ↔ stem BM25 ↔ lemma BM25`

or equivalent classical retrieval comparisons.

**Level 2 — Lexical and semantic/dense retrieval compared**

The study evaluates lexical and dense/semantic retrieval in the same benchmark, but does not perform a controlled morphology-conditioned hybrid analysis.

**Level 3 — Morphology-aware hybrid retrieval**

A morphology-aware lexical condition participates in a lexical+dense/semantic hybrid or reranking pipeline and the retrieval stage is evaluated.

**Level 4 — Controlled morphology × fixed semantic comparator**

Multiple lexical morphology variants are compared while the same dense/semantic retriever and substantially the same fusion protocol are held constant.

**Level 5 — Morphology-conditioned complementarity analysis**

The study directly measures how changing morphology alters lexical–dense complementarity, such as:

- lexical-only relevant hits;
- dense-only relevant hits;
- relevant-set intersection;
- overlap;
- unique relevant-document identity;
- candidate union / oracle union;
- morphology-conditioned incremental hybrid gain.

### Important

The review must not assume in advance that Level 5 is empty.  
Whether any Level 5 study exists is an empirical result of the systematic search.

---

## 5. Review questions

### RQ1 — Morphological representation

**Which explicit morphological representations and normalization strategies have been evaluated in corpus-level information retrieval for morphologically rich and/or low-resource languages?**

Subquestions:

- Which languages and language families are represented?
- Which forms are compared: raw, stem, lemma, root, morphemes, subwords, character truncation, normalization?
- How often are morphology choices applied to documents, queries, or both?

---

### RQ2 — Lexical retrieval effect

**What evidence exists that morphological representation changes lexical retrieval effectiveness, efficiency, or the composition of retrieved relevant documents?**

Extract:

- MAP;
- nDCG;
- Recall;
- Precision;
- MRR;
- bpref;
- index size;
- vocabulary size;
- latency where available;
- query-level effects;
- statistical significance.

No global assumption such as `lemma > stem > raw` is permitted.

---

### RQ3 — Dense and hybrid interaction

**How has explicit morphology been handled when dense, multi-vector, or hybrid lexical–semantic retrieval is introduced?**

Specifically determine:

- whether the dense comparator is retrieval-trained;
- whether the same dense model is retained across morphology conditions;
- whether fusion parameters are fixed;
- whether morphology is applied only to the lexical branch or also to dense input;
- whether observed gains can actually be attributed to morphology.

---

### RQ4 — Complementarity evidence

**To what extent does existing literature measure morphology-induced changes in lexical–dense complementarity rather than only aggregate effectiveness?**

Look specifically for:

- overlap/intersection;
- lexical-only relevant hits;
- dense-only relevant hits;
- union coverage;
- oracle union;
- incremental hybrid gain;
- per-query analysis;
- query-type or query-feature interaction.

This RQ is the direct bridge to the current PhD gap.

---

### RQ5 — Evaluation quality

**How reliable and reproducible are the experimental designs used to support morphology-aware retrieval claims?**

Assess:

- corpus transparency;
- query construction;
- qrels/relevance judgments;
- assessor procedure;
- pooling;
- baseline fairness;
- fixed/controlled parameters;
- evaluation metrics;
- statistical testing;
- ablation;
- source code/data availability.

---

### RQ6 — Uzbek evidence boundary

**What has been established specifically for Uzbek retrieval, and which claims remain unsupported by controlled corpus-level retrieval evidence?**

The synthesis must distinguish:

- morphology/NLP resources;
- search infrastructure;
- semantic similarity;
- corpus-level retrieval;
- hybrid retrieval;
- RAG answer quality.

Analyzer accuracy, STS correlation and RAG answer accuracy must not be presented as retrieval effectiveness.

---

## 6. Review type and reporting standard

The paper will be conducted as a **systematic literature review / systematic evidence synthesis**.

Reporting standards:

- **PRISMA 2020** for the study-selection and reporting process;
- **PRISMA-S** for reproducible reporting of literature searches.

A PRISMA flow diagram will report:

- records identified;
- duplicates removed;
- title/abstract records screened;
- records excluded;
- full texts assessed;
- full texts excluded with reasons;
- studies included in the final synthesis.

### Protocol preservation

Before final database searching begins, freeze this protocol as `v1.0`.

Recommended project path:

`articles/01_morphology_ir_review/ARTICLE_RESEARCH_PROTOCOL_v1.0.md`

Also preserve:

- exact search strings;
- export dates;
- database export files;
- deduplication log;
- screening decisions;
- exclusion reasons;
- extraction sheet.

An OSF registration is optional but scientifically useful after the internal protocol is finalized.

---

## 7. Information sources

### Primary bibliographic databases

1. **Scopus**
2. **Web of Science Core Collection**
3. **ACM Digital Library**
4. **IEEE Xplore**
5. **ACL Anthology**

### Supplementary discovery sources

6. ScienceDirect
7. SpringerLink
8. Google Scholar — citation chasing and missing-source discovery, not the sole primary search database.
9. ProQuest Dissertations & Theses — especially for doctoral evidence where relevant.
10. Official university / national repositories for Uzbek dissertations and research resources.

### Citation chaining

For every critical included paper:

- backward citation search;
- forward citation search;
- related-work search.

Critical seed studies include at minimum:

- Can et al. (2008), Turkish IR;
- Haddad & Bechikh Ali (2014), Turkish lexical IR;
- UPERF (2024), Urdu;
- Kazi & Khoja (2026), Urdu retrieval/reranking;
- Aboasal et al. (2026), Arabic legal retrieval;
- Munetsi et al. (SIGIR 2026), Shona;
- GreekBarRetrieval (2026 preprint);
- Bakaev / Xusainova / Elov Uzbek morphology-search evidence;
- Uzbek semantic/hybrid retrieval works already tracked in the PhD repository.

---

## 8. Search period

### Primary-study time window

**2000–2026**

Reason:

- captures the modern multilingual and language-specific morphology-aware retrieval literature;
- includes the major pre-neural lexical era;
- allows direct comparison with modern dense/hybrid retrieval.

### Pre-2000 works

Important landmark works may be used as **background/theoretical references** through citation chaining but will not automatically belong to the systematic primary-study corpus.

### Search cut-off

The final manuscript must state the exact last-search date.

Protocol rule:

> Repeat all primary database searches shortly before manuscript submission and record the update-search date.

---

## 9. Core search concept blocks

### Block A — Retrieval

```text
"information retrieval"
OR "document retrieval"
OR "text retrieval"
OR "passage retrieval"
OR "ad hoc retrieval"
OR "lexical retrieval"
OR "sparse retrieval"
OR "dense retrieval"
OR "semantic retrieval"
OR "neural retrieval"
OR "hybrid retrieval"
OR "hybrid search"
OR BM25
OR "retrieval augmented generation"
OR RAG
```

### Block B — Morphology

```text
morpholog*
OR stemm*
OR lemmat*
OR "morphological normalization"
OR "morphological analysis"
OR "morphological segmentation"
OR "morpheme segmentation"
OR root*
OR inflection*
OR agglutinat*
OR "surface form"
OR "word form"
```

### Block C — Morphologically rich / low-resource language context

```text
"low-resource"
OR "low resource"
OR "under-resourced"
OR "under-resourced language"
OR "morphologically rich"
OR "morphologically complex"
OR agglutinative
OR Uzbek
OR Turkish
OR Turkic
OR Urdu
OR Arabic
OR Persian
OR Kazakh
OR Kyrgyz
OR Azerbaijani
OR Uyghur
OR Shona
OR Finnish
OR Hungarian
OR Basque
OR Bengali
```

The language list is **not intended as an exhaustive eligibility list**.  
A study can be included if its language is demonstrably morphologically rich and the retrieval/morphology criteria are satisfied.

---

## 10. Proposed Scopus search

### Main query

```text
TITLE-ABS-KEY(
  (
    "information retrieval"
    OR "document retrieval"
    OR "text retrieval"
    OR "passage retrieval"
    OR "ad hoc retrieval"
    OR "lexical retrieval"
    OR "sparse retrieval"
    OR "dense retrieval"
    OR "semantic retrieval"
    OR "neural retrieval"
    OR "hybrid retrieval"
    OR "hybrid search"
    OR BM25
    OR "retrieval augmented generation"
    OR RAG
  )
  AND
  (
    morpholog*
    OR stemm*
    OR lemmat*
    OR "morphological normalization"
    OR "morphological analysis"
    OR "morphological segmentation"
    OR "morpheme segmentation"
    OR inflection*
    OR agglutinat*
    OR "surface form"
    OR "word form"
  )
  AND
  (
    "low-resource"
    OR "low resource"
    OR "under-resourced"
    OR "morphologically rich"
    OR "morphologically complex"
    OR agglutinative
    OR Uzbek
    OR Turkish
    OR Turkic
    OR Urdu
    OR Arabic
    OR Persian
    OR Kazakh
    OR Kyrgyz
    OR Azerbaijani
    OR Uyghur
    OR Shona
    OR Finnish
    OR Hungarian
    OR Basque
    OR Bengali
  )
)
AND PUBYEAR > 1999
```

### Important

The initial query must be tested against the known seed studies.

If it fails to retrieve key known papers, modify the query **before freezing v1.0**, document the change, and rerun the validation.

---

## 11. Uzbek-focused supplementary search

Bibliographic databases often under-index national Uzbek research. Therefore, perform a separate Uzbek evidence search.

### English

```text
Uzbek AND
(retrieval OR "information retrieval" OR BM25 OR "semantic search"
 OR "dense retrieval" OR "hybrid search" OR RAG)
AND
(morphology OR stemming OR lemmatization OR normalization
 OR tokenization OR transliteration)
```

### Russian concepts

```text
узбекский язык информационный поиск морфология
узбекский поиск стемминг лемматизация
морфологическая нормализация узбекский поиск
семантический поиск узбекский язык
гибридный поиск узбекский язык
```

### Uzbek concepts

```text
o'zbek tili axborot qidirish morfologiya
o‘zbek tili qidiruv lemmatizatsiya
o‘zbek tili stemming qidiruv
o‘zbek tili semantik qidiruv
o‘zbek tili gibrid qidiruv
```

Search spelling variants of Uzbek apostrophes where technically possible.

---

## 12. Eligibility criteria

### Include a study in the PRIMARY retrieval evidence corpus when all applicable conditions hold

1. It concerns text/document/passage retrieval or a retrieval stage that can be evaluated separately.
2. It uses or evaluates an explicit morphological representation/intervention, or directly investigates morphology-sensitive retrieval behavior.
3. It reports enough methodological information to determine the retrieval setup.
4. It concerns a morphologically rich and/or low-resource language relevant to the review scope.
5. It is a journal article, conference paper, defended dissertation, or other scientifically traceable primary research source.
6. The publication falls within the primary time window or is admitted as an explicitly justified landmark exception.
7. Full text or sufficient authoritative evidence is available for extraction.

---

## 13. Contextual-evidence category

Some Uzbek sources are scientifically important but do not contain a controlled IR benchmark.

Examples:

- morphology analyzer dissertations;
- lemma-based indexing systems;
- corpus search infrastructure;
- analyzer accuracy studies;
- semantic similarity resources.

These sources may be included in a separate **Uzbek contextual evidence layer** but must not be mixed with controlled retrieval-effectiveness studies.

This distinction is essential.

---

## 14. Exclusion criteria

Exclude from primary retrieval-effectiveness synthesis when the work is only:

- stemming/lemmatization algorithm accuracy with no retrieval task;
- POS tagging;
- morphological analysis with no retrieval evaluation;
- STS / semantic similarity only;
- text classification;
- sentiment analysis;
- NER/coreference only;
- language-model pretraining only;
- question answering with no separable retrieval evidence;
- RAG evaluated only through final answer quality when retrieval quality cannot be isolated;
- web tutorial/blog/product documentation;
- untraceable manuscript/aggregator entry;
- duplicate publication of the same experiment without additional evidence.

Preprints may be retained in a clearly marked provisional evidence tier when highly relevant.

---

## 15. Screening procedure

### Stage 1 — Deduplication

Use DOI, title, authors, year and fuzzy title matching.

Keep a deduplication log.

### Stage 2 — Title/abstract screening

Decision labels:

- INCLUDE;
- EXCLUDE;
- UNCERTAIN.

### Stage 3 — Full-text screening

Record one primary reason for exclusion.

Recommended reason codes:

- E1 — not retrieval;
- E2 — no morphology intervention/evidence;
- E3 — wrong language/scope;
- E4 — no corpus-level evaluation;
- E5 — RAG only, retrieval not separable;
- E6 — no extractable methods/results;
- E7 — duplicate experiment;
- E8 — non-scholarly/unverifiable source;
- E9 — outside period without landmark justification.

### Reviewer reliability

Preferred design:

- two independent reviewers for screening;
- resolve disagreements by discussion/adjudication;
- report inter-reviewer agreement.

If full dual screening is not feasible, transparently document the actual process and use an independent check of a predefined sample plus all borderline decisions.

---

## 16. Data extraction matrix

Create one row per distinct study/experiment.

### A. Bibliography

- Study ID
- Authors
- Year
- Title
- Venue
- DOI
- Publication type
- Peer-reviewed / defended / preprint
- Project reliability level A/B/C/D

### B. Language characteristics

- Language
- Language family
- Morphological type
- Script(s)
- Low-resource status / justification
- Orthographic variation
- Transliteration issue

### C. Retrieval task

- Ad-hoc document retrieval
- Passage retrieval
- Legal retrieval
- Domain search
- RAG retrieval
- Other
- Retrieval unit

### D. Corpus

- Source
- Domain
- Number of documents/passages
- Tokens if reported
- Public/private
- Deduplication
- Language identification

### E. Queries and relevance

- Number of queries
- Query source
- Query length/type
- Human/synthetic
- Number of relevant documents
- Qrels method
- Pooling
- Pool depth
- Number of assessors
- Agreement
- Adjudication

### F. Morphology

- Raw condition
- Stemming
- Lemmatization
- Root extraction
- Morphological analysis
- Morpheme segmentation
- Prefix/character truncation
- Subword processing
- Orthographic normalization
- Script normalization/transliteration
- Applied to query / document / both

### G. Retrieval system

- TF-IDF/VSM
- BM25 / variant
- Language model
- Learned sparse
- Dense retriever
- Dense model/checkpoint
- Retrieval-trained vs generic embedding
- ColBERT/late interaction
- Reranker
- Hybrid system
- RAG system

### H. Hybrid protocol

- Fusion method
- Score normalization
- Alpha/weights
- RRF parameter
- Candidate depth
- Same dense model across morphology variants?
- Same fusion configuration across morphology variants?
- Dev/test tuning separation?

### I. Metrics

- P@k
- Recall@k
- MAP
- MRR
- nDCG@k
- bpref
- Hit@k
- latency
- vocabulary/index size
- other

### J. Statistical evidence

- Paired testing
- Confidence intervals
- Effect size
- Multiple-comparison treatment
- Ablation
- Per-query testing

### K. Complementarity evidence

- lexical-only relevant hits
- dense-only relevant hits
- intersection
- overlap coefficient / Jaccard
- union
- oracle union
- incremental hybrid gain
- query-level morphology effect
- query-characteristic analysis

### L. Results and interpretation

- strongest numerical result
- within-study morphology delta
- what the study actually proves
- what it does not prove
- main limitations
- relevance to Uzbek retrieval
- evidence level 0–5

---

## 17. Quality / risk-of-bias appraisal

Do not collapse all quality into one arbitrary total score.

Assess the following domains separately:

1. **Source reliability**
2. **Corpus transparency**
3. **Query validity**
4. **Relevance-judgment/qrels validity**
5. **Comparator fairness**
6. **Control of morphology-specific confounders**
7. **Metric appropriateness**
8. **Statistical evidence**
9. **Reproducibility**
10. **Strength of causal interpretation**

Possible judgment:

- LOW CONCERN;
- SOME CONCERN;
- HIGH CONCERN;
- NOT APPLICABLE.

Retain the project's A/B/C/D source-reliability scale as a separate field.

---

## 18. Synthesis plan

### 18.1 Descriptive evidence map

Report:

- studies per year;
- studies per language;
- morphology method distribution;
- retrieval paradigm distribution;
- benchmark size distribution;
- proportion with qrels;
- proportion with statistical testing;
- proportion with public data/code.

---

### 18.2 Morphology × retrieval matrix

Create a central table:

| Morphology | Lexical | Learned sparse | Dense | Late interaction | Hybrid | Controlled complementarity |
|---|---|---|---|---|---|---|
| Raw | | | | | | |
| Stem | | | | | | |
| Lemma | | | | | | |
| Root | | | | | | |
| Morpheme | | | | | | |
| Orthographic/script normalization | | | | | | |

Each cell should contain counts and key representative studies.

---

### 18.3 Language evidence map

A second matrix:

| Language | Lexical morphology | Dense retrieval | Hybrid retrieval | Controlled raw/stem/lemma | Complementarity analysis |
|---|---|---|---|---|---|

This makes the Uzbek evidence boundary visually explicit.

---

### 18.4 Direction-of-effect analysis

For comparable within-study contrasts, report:

- morphology better;
- approximately unchanged;
- morphology worse.

Where metrics and experimental setups are sufficiently comparable, report within-study relative deltas.

Do **not** pool MAP/nDCG/MRR across unrelated datasets as though their absolute scales were directly comparable.

A statistical meta-analysis should only be added if the final evidence corpus contains a sufficiently homogeneous subset.

---

### 18.5 Complementarity synthesis

For each Level 3–5 study, extract:

- whether hybrid improvement is observed;
- whether component candidate sets are analyzed;
- whether the morphology change itself is isolated;
- whether the same dense model is used;
- whether the same fusion protocol is used;
- whether unique-hit/overlap/oracle evidence exists.

This is the most important synthesis section for the PhD relationship.

---

## 19. New 2026 paper requiring immediate deep-dive verification

A fresh publication discovered during protocol preparation:

**Berkay Sunay & Sevgi Yigit-Sert (2026)**  
*The Effect of Morphological Normalization on Retrieval Performance and Answer Accuracy in Turkish RAG Systems*  
34th Signal Processing and Communications Applications Conference (SIU 2026).  
**DOI:** 10.1109/SIU71813.2026.11636534.

Available metadata/summary indicates:

- Turkish RAG;
- RAGTURK dataset;
- RAW representation;
- LEMMA representation;
- a HYBRID representation;
- Recall and MRR for retrieval;
- ROUGE and BERTScore for generation;
- dense multilingual embedding retrieval;
- reported degradation from full lemmatization relative to raw text.

### Why this matters

It is directly relevant to the review because it tests morphological normalization in modern neural retrieval.

### Why it does not automatically close the current PhD gap

Based on currently verified metadata, the study appears to change the representation used by the dense/RAG retrieval pipeline rather than perform the required controlled comparison:

`BM25_raw / BM25_stem / BM25_lemma`

against the **same fixed dense retriever D** with a fixed fusion protocol and set-complementarity analysis.

However, this must be confirmed from the full paper before drawing a firm conclusion.

### Action

Add this paper to the PhD literature queue for a dedicated deep dive before finalizing the article's novelty statement.

---

## 20. Proposed manuscript structure

Target a manuscript that can fit both TALLIP and Cambridge NLP without major conceptual restructuring.

### 1. Introduction

- morphology as a retrieval representation problem;
- why aggregate low-resource IR reviews are insufficient for this narrower question;
- transition from lexical to dense/hybrid retrieval;
- Uzbek motivation;
- contributions and RQs.

### 2. Scope and Terminology

- lexical vs sparse;
- dense vs semantic;
- retrieval vs reranking;
- IR vs RAG;
- stemming vs lemmatization vs morphological analysis;
- morphology as representation, not automatically a third retrieval paradigm.

### 3. Review Methodology

- databases;
- search strings;
- PRISMA;
- inclusion/exclusion;
- screening;
- extraction;
- quality appraisal;
- synthesis.

### 4. Morphology in Classical Lexical Retrieval

- historical evidence;
- stemming;
- lemmatization;
- roots;
- simple truncation;
- Turkic evidence;
- efficiency/effectiveness trade-offs.

### 5. Morphology in Dense and Neural Retrieval

- generic embeddings vs retrieval-trained dense models;
- subword handling;
- explicit normalization;
- evidence that preprocessing can help, hurt or be neutral;
- dense robustness in morphologically rich languages.

### 6. Morphology in Hybrid Lexical–Semantic Retrieval

- lexical+dense fusion;
- score fusion and RRF;
- morphology-aware lexical branch;
- reranking;
- RAG retrieval only where retrieval evidence is separable.

### 7. From Aggregate Effectiveness to Complementarity

- relevant-set identity;
- overlap;
- unique hits;
- candidate union;
- oracle union;
- incremental hybrid gain;
- evidence ladder Levels 0–5.

### 8. Uzbek and Turkic Evidence

- Uzbek morphology resources;
- Uzbek lexical/search infrastructure;
- Uzbek semantic retrieval;
- Uzbek hybrid/RAG evidence;
- Turkish comparative evidence;
- exact boundary between infrastructure and controlled retrieval results.

### 9. Cross-Study Evidence Synthesis

- morphology × retrieval matrix;
- language evidence matrix;
- methodological patterns;
- contradictory findings;
- evidence-strength analysis.

### 10. Evaluation and Benchmarking Gaps

- qrels limitations;
- shallow pooling;
- small query sets;
- lack of statistical tests;
- confounding of morphology, dense model and fusion;
- lack of per-query complementarity analysis.

### 11. Research Agenda

Develop design requirements rather than claiming a predetermined solution:

- controlled raw/stem/lemma lexical baselines;
- fixed semantic comparator;
- fixed fusion;
- deeper pooling;
- per-query set analysis;
- query-feature analysis;
- reproducible Uzbek benchmarks.

### 12. Threats to Validity

- database coverage;
- language/publication bias;
- national literature discoverability;
- heterogeneity;
- incomplete full texts;
- rapid 2026 publication cycle.

### 13. Conclusion

Answer each RQ explicitly.

---

## 21. Planned figures

1. **PRISMA flow diagram**
2. **Conceptual taxonomy:** morphology × retrieval paradigm × evidence target
3. **Timeline:** lexical → dense → hybrid morphology-aware retrieval
4. **Evidence ladder:** Levels 0–5
5. **Language × retrieval heatmap**
6. **Morphology × retrieval paradigm heatmap**
7. Optional: benchmark/evaluation-quality map

---

## 22. Planned tables

1. Definitions and methodological distinctions
2. Existing review comparison table
3. Included-study characteristics
4. Morphology-aware lexical retrieval evidence
5. Dense/hybrid morphology evidence
6. Uzbek/Turkic evidence matrix
7. Evaluation methodology / qrels quality
8. Complementarity evidence table
9. Remaining evidence gaps and experimental requirements

---

## 23. Journal targeting

### Primary: ACM TALLIP

**Why it fits**

- Asian and low-resource language information processing is the journal's core scope.
- Computational morphology and linguistic resources are explicitly relevant.
- TALLIP publishes survey/review articles.
- Review articles must provide substantially different information from prior literature, explain how research strands connect, and offer a view of future directions.
- The Uzbek/Turkic evidence layer creates a strong journal-specific fit.

### Editorial positioning for TALLIP

The cover letter should explicitly compare the manuscript with:

1. Kazi et al. (2025) — broad high-/low-resource document retrieval survey;
2. Roy et al. (2026) — resource-poor stemming review;
3. older stemming-in-IR surveys.

The cover letter should state that this manuscript differs by systematically analyzing the **interaction between explicit morphological representation and retrieval paradigm/evidence**, rather than surveying retrieval generally or stemming generally.

---

### Fallback: Natural Language Processing (Cambridge)

The journal explicitly covers:

- information retrieval;
- multilingual NLP;
- low-resource language research;
- survey papers.

Its current author guidance defines Survey Papers as approximately **10,000–16,000 words** and expects both a comprehensive summary and a perspective on where the field is heading.

For compatibility, target approximately **11,000–14,000 manuscript words** before journal-specific formatting, excluding supplementary extraction tables if allowed.

---

## 24. Publication-cost note

### TALLIP / ACM

ACM moved to a full Open Access publishing model in 2026.  
Before submission, check whether the corresponding author's institution participates in ACM Open and whether any journal APC/waiver applies.

Do not assume conference APC figures apply unchanged to TALLIP journal articles.

### Cambridge NLP

The journal is fully Gold Open Access.

The official 2026 page lists an APC of:

- **£2,610**
- **US$3,655**

when an APC is required.

Cambridge also lists institutional agreements, equity initiatives, and waiver/discount routes.

Do not choose between TALLIP and Cambridge on publication cost until the **journal-specific TALLIP APC or institutional ACM Open coverage** has been verified. Cambridge's current list price is known, while ACM conference subsidy figures must not be treated as the TALLIP journal price.

---

## 25. Manuscript novelty statement — safe working version

Do not use “first” yet.

A safe working statement is:

> Existing reviews have examined document retrieval for low-resource languages and stemming for resource-poor languages, but these literatures do not by themselves provide a focused synthesis of how explicit morphological representation interacts with the transition from lexical to dense and hybrid corpus-level retrieval. This review therefore maps morphology interventions against retrieval paradigms and levels of experimental evidence, with particular attention to whether morphology changes only aggregate retrieval effectiveness or also the composition and complementarity of lexical and semantic retrieval results. Uzbek evidence is analyzed separately to distinguish language-resource and search-infrastructure results from controlled retrieval effectiveness evidence.

After the completed systematic search, this statement may be strengthened if justified.

---

## 26. What must NOT be claimed

The review must not claim in advance that:

- no Uzbek hybrid retrieval exists;
- no Uzbek semantic retrieval exists;
- morphology has not been used in Uzbek search;
- lemmatization is better than stemming;
- morphology always improves retrieval;
- dense retrieval removes the need for morphology;
- hybrid always beats standalone retrieval;
- RRF is novel;
- fixed weighted fusion is novel;
- dynamic alpha is novel;
- no prior morphology+dense study exists;
- no Level 5 complementarity study exists.

Every absence claim must be supported by the completed systematic search.

---

## 27. Relationship to the dissertation

This review paper must remain an independent publication.

It can support the PhD by providing:

1. systematic literature evidence;
2. a validated research boundary;
3. benchmark design requirements;
4. evidence that justifies the controlled experiment.

It must **not** present the planned Uzbek experiment as a completed result.

The current experimental PhD design remains separate:

`BM25_raw`
`BM25_stem`
`BM25_lemma`

versus the same fixed dense retriever `D`, followed by controlled hybrid conditions and per-query complementarity analysis.

---

## 28. Immediate execution sequence

### Phase A — Protocol lock

1. Deep-dive the newly discovered Turkish SIU 2026 paper.
2. Recheck the closest existing reviews.
3. Pilot the main search query against known seed papers.
4. Adjust search terms if seed recall is insufficient.
5. Freeze `ARTICLE_RESEARCH_PROTOCOL_v1.0`.

### Phase B — Systematic search

6. Search Scopus.
7. Search Web of Science.
8. Search ACM DL.
9. Search IEEE Xplore.
10. Search ACL Anthology.
11. Perform Uzbek/Russian/Uzbek-language supplementary searches.
12. Export all records.
13. Deduplicate.

### Phase C — Screening

14. Title/abstract screening.
15. Full-text screening.
16. Record exclusion reasons.
17. Produce PRISMA counts.

### Phase D — Extraction

18. Build the extraction matrix.
19. Complete critical-paper deep dives.
20. Apply quality appraisal.
21. Classify each study by evidence level 0–5.

### Phase E — Synthesis

22. Build taxonomy.
23. Build language and method evidence maps.
24. Synthesize lexical morphology findings.
25. Synthesize dense/hybrid findings.
26. Analyze complementarity evidence.
27. Write Uzbek/Turkic boundary.
28. Derive benchmark/research-design implications.

### Phase F — Manuscript

29. Draft Results from extracted data first.
30. Draft Discussion.
31. Draft Introduction last among main analytical sections.
32. Write abstract after conclusions are stable.
33. Prepare TALLIP cover letter explicitly explaining novelty relative to prior reviews.
34. Run a final literature update search immediately before submission.

---

## 29. Go / no-go criteria before manuscript writing

Proceed to full manuscript writing only if the systematic search confirms at least one of the following:

### GO-A

The literature contains enough morphology-aware IR studies to support a cross-language evidence taxonomy, but modern dense/hybrid interaction remains fragmented.

### GO-B

A meaningful distinction exists between classical lexical morphology evidence and modern neural/hybrid evidence.

### GO-C

Uzbek has substantial morphology/search infrastructure but materially weaker controlled corpus-retrieval evidence than the comparative literature.

### GO-D

Existing reviews do not already perform the same morphology × retrieval-paradigm × complementarity synthesis.

### NO-GO / RESCOPE

Rescope the article if a newly found systematic review already performs essentially the same synthesis with current 2026 evidence.

---

## 30. Current protocol conclusion

**The article is viable, but only if treated as a rigorous systematic evidence synthesis rather than a shortened dissertation literature chapter.**

The strongest positioning is:

> **Morphology is not studied merely as preprocessing; it is studied as a change in retrieval representation whose consequences must be traced from lexical retrieval through dense/hybrid interaction and, where the literature permits, to relevant-set complementarity.**

This framing is sufficiently different from the known broad low-resource retrieval review and the known resource-poor stemming review to justify proceeding to the systematic-search phase, subject to the final novelty audit.

