# ARTICLE_RESEARCH_PROTOCOL_v1.0_FROZEN

**Project:** PhD — Uzbek Hybrid Information Retrieval  
**Repository:** `Shoxrux2017/phd-uzbek-hybrid-retrieval`  
**Protocol version:** `v1.0 FROZEN`  
**Freeze date:** 2026-09-17  
**Article type:** systematic literature review / systematic evidence synthesis  
**Primary target journal:** ACM Transactions on Asian and Low-Resource Language Information Processing (TALLIP)  
**Fallback target:** Natural Language Processing (Cambridge University Press)  
**Primary review period:** 2000–2026 inclusive  
**Reporting standards:** PRISMA 2020 + PRISMA-S  
**PhD research-gap status:** `research/CURRENT_GAP.md` v0.8 refined remains **provisional**; freezing this review protocol does **not** freeze the dissertation gap, hypotheses, method, or novelty.

---

## 0. Freeze declaration

This document freezes the methodology of the systematic review before full cross-source screening and evidence synthesis.

From this point onward:

1. accepted source-specific search strategies must not be silently changed;
2. raw exports must be preserved unchanged;
3. every protocol deviation must be dated and documented;
4. additional sources such as Scopus or Web of Science may be added only through a protocol amendment;
5. an update search before manuscript submission is allowed and expected, but must reuse the same frozen conceptual logic unless an amendment is justified;
6. no absence or novelty claim may be strengthened merely because a pilot failed to identify a competing study;
7. the dissertation research gap remains falsifiable and may be revised after the completed review.

The review is therefore frozen at the level of **method**, not at the level of **scientific conclusion**.

---

# 1. Review objective

The review examines how **explicit morphological representation or normalization** has been evaluated in corpus-level information retrieval, and how the evidence changes across:

- classical lexical retrieval;
- learned sparse retrieval;
- dense retrieval;
- late-interaction / multi-vector retrieval;
- lexical–dense hybrid retrieval;
- reranking;
- retrieval stages of RAG when retrieval is separately evaluable.

The review is not another general stemmer catalogue and not another broad low-resource IR survey.

Its central analytical chain is:

`morphological representation/intervention`
→ `retrieval paradigm`
→ `experimental design`
→ `retrieval evidence`
→ `component interaction / complementarity evidence`.

---

# 2. Working article title

**Morphological Representation in Information Retrieval for Morphologically Rich Languages: A Systematic Review of Lexical, Dense, and Hybrid Retrieval with an Uzbek Perspective**

Alternative wording may be used at manuscript stage, but the scope must not be broadened beyond this protocol without an amendment.

Do **not** use “first systematic review” unless the completed review justifies that wording.

---

# 3. Review questions

## RQ1 — Morphological representation

Which explicit morphological representations and normalization strategies have been evaluated in corpus-level information retrieval for morphologically rich and/or low-resource languages?

Extract, where applicable:

- raw / surface form;
- stemming;
- lemmatization;
- root extraction;
- morpheme segmentation;
- fixed-prefix / character truncation;
- subword processing;
- morphology-aware expansion;
- orthographic normalization;
- script normalization / transliteration.

## RQ2 — Lexical retrieval effect

What evidence exists that morphological representation changes lexical retrieval:

- effectiveness;
- efficiency;
- index/vocabulary size;
- query-level behavior;
- composition of retrieved relevant documents?

No ordering such as `lemma > stem > raw` is assumed.

## RQ3 — Dense and hybrid interaction

How has explicit morphology been handled when dense, multi-vector, or hybrid lexical–semantic retrieval is introduced?

Determine in particular:

- whether the dense comparator is retrieval-trained;
- whether the same dense model is retained across morphology conditions;
- whether dense input preprocessing is fixed;
- whether fusion parameters are controlled;
- whether morphology is isolated from other simultaneous changes.

## RQ4 — Complementarity evidence

To what extent does existing literature measure morphology-induced changes in lexical–dense complementarity rather than only aggregate retrieval effectiveness?

Search specifically for:

- lexical-only relevant hits;
- dense-only relevant hits;
- intersection / overlap;
- union coverage;
- oracle union;
- incremental hybrid gain;
- per-query analysis;
- query-feature interaction.

## RQ5 — Evaluation quality

How reliable and reproducible are morphology-aware retrieval experiments with respect to:

- corpus transparency;
- query construction;
- qrels;
- pooling;
- assessors;
- baselines;
- controlled parameters;
- metrics;
- statistics;
- ablation;
- reproducibility?

## RQ6 — Uzbek evidence boundary

What has been established specifically for Uzbek retrieval, and which claims remain unsupported by controlled corpus-level IR evidence?

The synthesis must distinguish:

- morphology/NLP resources;
- search infrastructure;
- STS / semantic similarity;
- corpus-level retrieval;
- hybrid retrieval;
- reranking;
- RAG answer quality.

Analyzer accuracy, STS correlation and final-answer accuracy are not retrieval effectiveness.

---

# 4. Reporting framework

The completed review will follow:

- **PRISMA 2020** for selection/reporting;
- **PRISMA-S** for literature-search reporting.

The PRISMA flow must report at minimum:

- records identified by each source;
- records from supplementary methods;
- duplicates removed;
- title/abstract records screened;
- title/abstract exclusions;
- full texts sought;
- full texts not retrieved;
- full texts assessed;
- full-text exclusions by reason;
- studies included in the final synthesis.

---

# 5. Primary time window

Primary-study inclusion window:

**2000-01-01 through 2026-12-31**

The 2026 corpus is necessarily incomplete at the current freeze date and must be updated before submission.

Pre-2000 landmark works may be cited as theoretical/background references through citation chaining but are not automatically part of the primary systematic evidence corpus.

---

# 6. Frozen information-source architecture

## 6.1 Core article/conference search layer

### EBSCOhost

Search jointly:

1. **Academic Search Premier**
2. **Science & Technology Collection**
3. **Library, Information Science & Technology Abstracts (LISTA)**

Frozen working query: **exact tested S4**.

Platform result count at refinement:

**527**

Important freeze decision:

**KEEP EXACT TESTED S4.**

`S4-clean` was logically prepared but was **not empirically validated** because the final count/retention checks were not run under confirmed baseline settings. It must not replace the tested S4.

### IEEE Xplore

Frozen working query:

**I1**

Search mode:

`Advanced Search → Command Search`

Scope:

**All Metadata**

Date filter:

**2000–2026**

Frozen pilot result count:

**1,256**

Original IEEE seed retention:

**3/3**

The I2 field-refinement candidate is rejected.

### ACL Anthology

Use the official ACL Anthology metadata repository rather than web-page scraping.

Frozen snapshot used for pilot:

`f27fde6433cfa53bce6d7e3982a8b0085099d301`

Frozen search layers:

- **A1** — explicit retrieval × morphology metadata search;
- **A2R** — supplemental language-sensitive retrieval search.

Pilot counts:

- A1 = **83**
- A2R = **255**

Do not add these counts together as if they were disjoint. Deduplicate ACL records by Anthology ID before cross-source merging.

## 6.2 Dissertation / grey-literature layer

### ProQuest Dissertations & Theses Global

Database:

**ProQuest Dissertations & Theses Global (PQDT Global)**

Platform:

**ProQuest**

Frozen query:

**P2**

Field:

**NOFT — Anywhere except full text**

Date range:

**2000–2026**

Frozen result count:

**126**

P2 differs from P1 only by replacing both occurrences of:

`lemmat*`

with:

`lemmat[*10]`

P2 retained:

- P1 R1: 20/20
- P1 R2: 15/15

No records were lost in the controlled P1→P2 test.

Doctoral dissertations and master's theses must be tagged separately in extraction.

## 6.3 Supplementary / targeted publisher layer

### ACM Digital Library

Current accessible edition:

**Basic Edition**

Institution recognition:

**No institution identified**

Because Advanced Search, date filtering and bulk export were not available, ACM Digital Library is **not counted as a completed primary systematic database search**.

ACM is retained as a:

**supplementary / targeted publisher source**

Permitted uses include:

- DOI/title verification;
- individual full-text inspection where accessible;
- targeted TALLIP / SIGIR / ICTIR / TOIS discovery;
- backward/forward chaining;
- metadata verification.

Do not report the Basic Edition checks as a completed ACM systematic database search.

### Crossref ACM metadata backstop

If used, report it separately as a supplementary metadata source.

Potential filter:

- DOI prefix `10.1145`;
- years 2000–2026;
- retrieval/morphology bibliographic terms.

Crossref is not a substitute for ACM Advanced Search.

## 6.4 Supplementary discovery

Permitted supplementary channels:

- SciSpace;
- Google Scholar for forward citation discovery if necessary;
- publisher pages;
- official university repositories;
- national Uzbek sources;
- backward reference chaining;
- forward citation chaining;
- references of included studies and closest reviews.

Any record found only through a supplementary channel must retain its discovery provenance.

## 6.5 Optional coverage enhancers

Scopus and Web of Science are **optional coverage enhancers, not protocol-freeze blockers**.

If access becomes available before manuscript submission:

- add them through a dated amendment;
- preserve exact platform queries;
- report them separately;
- do not rewrite earlier source counts.

---

# 7. Frozen conceptual search blocks

These blocks define the conceptual intent. Platform-specific exact strings remain authoritative in their archived artifacts.

## 7.1 Retrieval concepts

Core concepts include:

- `"information retrieval"`
- `"document retrieval"`
- `"text retrieval"`
- `"passage retrieval"`
- `"ad hoc retrieval"`
- `"lexical retrieval"`
- `"sparse retrieval"`
- `"dense retrieval"`
- `"semantic retrieval"`
- `"semantic search"`
- `"vector search"` where supported/used
- `"neural retrieval"`
- `"hybrid retrieval"`
- `"hybrid search"`
- `BM25`
- `"retrieval augmented generation"`
- `"retrieval-augmented generation"` where platform syntax/search design requires it

The bare acronym `RAG` is not used in the EBSCO/PQDT/IEEE core query unless explicitly frozen by a source-specific script; ACL handles it only as a standalone token in the scripted logic.

## 7.2 Morphology concepts

Core concepts include:

- `morpholog*`
- `stemm*`
- `lemmat*` or platform-correct equivalent
- `"morphological normalization"`
- `"morphological analysis"`
- `"morphological processing"`
- `"morphological preprocessing"`
- `"morphological segmentation"`
- `"morphology-aware"`
- `"morphology aware"`
- `"morpheme segmentation"`
- `"morpheme-based"`
- `inflection*`
- `agglutinat*`
- `"surface form"` / `"surface forms"`
- `"word form"` / `"word forms"`
- `"root extraction"`
- `"light stemming"`
- `"aggressive stemming"`
- `"term conflation"`
- subword terms where included by the source-specific frozen script.

Unrestricted `root*` is not used.

## 7.3 Language-sensitive supplemental concepts

The supplemental layer may include:

- Uzbek
- Turkish
- Turkic
- Kazakh
- Kyrgyz
- Azerbaijani
- Uyghur
- Urdu
- Arabic
- Persian
- Amharic
- Shona
- Finnish
- Hungarian
- Basque
- Greek
- Korean
- Thai
- Polish
- Bengali
- Marathi
- Hindi

The list supports sensitivity/discovery. It does not define eligibility.

---

# 8. Source-specific frozen search decisions

## 8.1 EBSCOhost — S4

Frozen database set:

- Academic Search Premier
- Science & Technology Collection
- LISTA

Settings:

- Boolean/Phrase search;
- 2000–2026;
- no language limit;
- no Full Text limit;
- no peer-reviewed-only limit;
- no publication-type restriction;
- `Apply equivalent subjects = OFF`;
- AI/query expansion = OFF;
- no NOT filters.

Frozen tested refinements include:

```text
(
 stemmer*
 OR
 (stemm* N3
  (word* OR term* OR token* OR text* OR algorithm*
   OR language* OR document* OR index* OR retriev*))
)
```

and:

```text
(
 "morphological normalization"
 OR "morphological analysis"
 OR "morphological processing"
 OR "morphological preprocessing"
 OR "morphological segmentation"
 OR "morphology-aware"
 OR "morphology aware"
 OR
 (morpholog* N5
  (language* OR linguist* OR word* OR term* OR token*
   OR text* OR inflection* OR stemm* OR lemmat*
   OR segment* OR query* OR document* OR retriev*))
)
```

All other concepts remain exactly as in the archived tested S4 string.

Authoritative query artifact:

`S4_EXACT_TESTED_2026-09-16.txt`

If a future transcription differs from that file, the archived exact-tested file wins.

## 8.2 PQDT — P2

Use the archived exact P2 string.

Authoritative artifact:

`PQDT_P2_EXACT_QUERY_2026-09-16.txt`

Frozen changes relative to P1:

- exactly two `lemmat*` occurrences changed to `lemmat[*10]`;
- no other conceptual term changed.

## 8.3 IEEE Xplore — I1

Exact conceptual query:

```text
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
OR "semantic search"
OR "vector search"
OR "neural retrieval"
OR "hybrid retrieval"
OR "hybrid search"
OR BM25
OR "retrieval augmented generation"
)
AND
(
morpholog*
OR stemm*
OR lemmat*
OR "morphological normalization"
OR "morphological analysis"
OR "morphological processing"
OR "morphological preprocessing"
OR "morphological segmentation"
OR "morpheme segmentation"
OR "morpheme-based"
OR inflection*
OR agglutinat*
OR "surface form"
OR "surface forms"
OR "word form"
OR "word forms"
OR "root extraction"
OR "light stemming"
OR "aggressive stemming"
OR "term conflation"
)
```

Frozen scope:

**All Metadata**

Frozen date filter:

**2000–2026**

Frozen sort used for pilot:

**Relevance**

I2 is not used because it reduced top-50 R1+R2 from 38% to 24%, increased morphology-tool noise, and lost relevant retention candidates.

## 8.4 ACL Anthology — A1

A1 is an offline deterministic metadata search over title/abstract.

Preprocessing:

- NFKC normalization;
- lowercase;
- preserve raw metadata separately.

A1 logic:

`Retrieval Block AND Morphology Block`

The implementation additionally recognizes standalone whole words `stem` and `lemma` because prefix patterns `stemm*` / `lemmat*` do not cover those base forms.

A1 pilot total:

**83**

## 8.5 ACL Anthology — A2R

A2R is a supplemental sensitivity layer:

`(A2 Retrieval Block OR standalone whole-word retrieval) AND Language Block`

The standalone token is implemented as:

`(?<!\w)retrieval(?!\w)`

A2R pilot total:

**255**

A2 baseline retention:

**180/180**

UPERF (`2024.paclic-1.96`) is recovered by A2R.

The ACL script and snapshot commit are part of the reproducibility record.

---

# 9. Uzbek-focused supplementary search

Because Uzbek national literature can be under-indexed internationally, run separate national searches in English, Russian and Uzbek.

Examples:

### English

```text
Uzbek AND
(retrieval OR "information retrieval" OR BM25 OR "semantic search"
 OR "dense retrieval" OR "hybrid search" OR RAG)
AND
(morphology OR stemming OR lemmatization OR normalization
 OR tokenization OR transliteration)
```

### Russian

```text
узбекский язык информационный поиск морфология
узбекский поиск стемминг лемматизация
морфологическая нормализация узбекский поиск
семантический поиск узбекский язык
гибридный поиск узбекский язык
```

### Uzbek

```text
o'zbek tili axborot qidirish morfologiya
o‘zbek tili qidiruv lemmatizatsiya
o‘zbek tili stemming qidiruv
o‘zbek tili semantik qidiruv
o‘zbek tili gibrid qidiruv
```

Where technically possible, check common Uzbek apostrophe variants.

National searches are supplementary evidence discovery, not substitutes for the core systematic searches.

---

# 10. Eligibility criteria

A study enters the **primary retrieval evidence corpus** when all applicable conditions are met:

1. It evaluates text, document or passage retrieval, or a retrieval stage that can be separately assessed.
2. It uses/evaluates an explicit morphology-related representation/intervention, or directly investigates morphology-sensitive retrieval behavior.
3. It provides enough methodological information to determine the retrieval setup.
4. It concerns a language whose morphological or low-resource characteristics are relevant to the review question.
5. It is a traceable scholarly primary source such as:
   - peer-reviewed journal article;
   - peer-reviewed conference paper;
   - officially defended dissertation;
   - scientifically traceable preprint retained in a clearly marked provisional tier.
6. It falls in 2000–2026 unless admitted as a justified landmark background exception.
7. Sufficient authoritative evidence/full text is available to extract the variables needed for synthesis.

---

# 11. Contextual evidence layer

Scientifically relevant work that does not contain a controlled corpus-level IR evaluation may be retained separately as **contextual evidence**.

Examples:

- Uzbek morphology dissertations;
- analyzer evaluations;
- lemma-based indexing infrastructure;
- National Corpus search tools;
- STS resources;
- language-model resources;
- search system deployments without qrels.

Contextual evidence must not be pooled with controlled retrieval-effectiveness studies.

---

# 12. Exclusion criteria

Exclude from the primary retrieval-effectiveness synthesis when a record is only:

- stemmer/lemmatizer accuracy without retrieval evaluation;
- morphology/POS analysis without IR;
- parsing only;
- STS / similarity only;
- text classification;
- sentiment analysis;
- NER/coreference only;
- language-model pretraining only;
- QA without a separately evaluable retrieval stage;
- RAG evaluated only on final-answer quality;
- non-text retrieval;
- tutorial/blog/product documentation;
- untraceable or unverifiable manuscript;
- duplicate report of the same experiment without additional evidence;
- outside the time window without landmark justification.

---

# 13. Evidence ladder

Each retained work receives an evidence level separate from source reliability.

## Level 0 — contextual

Morphology/search infrastructure or NLP resource; no corpus-level retrieval effectiveness evidence.

## Level 1 — morphology-aware lexical IR

Explicit morphology intervention with corpus-level lexical retrieval evaluation.

## Level 2 — lexical vs semantic/dense comparison

Lexical morphology and semantic/dense evidence appear in the same experimental work, but no controlled morphology-conditioned lexical–dense hybrid analysis is established.

## Level 3 — morphology-aware lexical–semantic hybrid

A true lexical + semantic/dense hybrid retrieval condition is evaluated with morphology-relevant processing.

## Level 4 — controlled morphology × fixed semantic comparator

Multiple lexical morphology variants are compared against the same/frozen semantic comparator under a controlled fusion protocol.

## Level 5 — direct morphology-conditioned complementarity

The work directly analyzes morphology-conditioned component complementarity, such as:

- lexical-only relevant hits;
- dense-only relevant hits;
- overlap/intersection;
- union/oracle union;
- morphology-conditioned incremental hybrid gain.

Do not assume Level 5 is empty before full-text synthesis.

---

# 14. Record management and provenance

Every imported record must retain:

- source database;
- platform;
- search ID/query ID;
- search date;
- export date;
- original record identifier;
- DOI if present;
- original title;
- authors;
- year;
- raw source file name.

Raw exports are immutable.

Generate SHA-256 hashes for final raw export files and record them in the review manifest.

---

# 15. Deduplication protocol

Deduplicate in this order:

1. exact DOI;
2. source-native persistent ID where applicable:
   - ACL Anthology ID;
   - IEEE document number;
   - ProQuest document ID;
3. normalized exact title;
4. normalized title + first author + year;
5. fuzzy-title review for unresolved candidates.

Do not automatically delete near-duplicate papers when they may represent:

- conference → journal extensions;
- dissertation → paper;
- preliminary → full study.

At full-text stage, distinguish:

- **record** — bibliographic item;
- **study/experiment** — underlying empirical evidence.

The final extraction matrix is study/experiment oriented, while PRISMA identification counts are record oriented.

Keep a deduplication log containing:

- kept record;
- removed record;
- match basis;
- manual decision when applicable.

---

# 16. Screening protocol

## 16.1 Title/abstract screening

Labels:

- `INCLUDE`
- `EXCLUDE`
- `UNCERTAIN`

A pilot label (`R1/R2/X`) used during query refinement is not the final systematic-screening label.

## 16.2 Full-text screening

Every excluded full text receives one primary exclusion code:

- `E1` — not retrieval;
- `E2` — no morphology intervention/evidence;
- `E3` — outside relevant language/scope;
- `E4` — no corpus-level retrieval evaluation;
- `E5` — RAG/QA only, retrieval not separable;
- `E6` — insufficient extractable methods/results;
- `E7` — duplicate experiment / superseded report;
- `E8` — non-scholarly or unverifiable;
- `E9` — outside period without landmark justification.

## 16.3 Reviewer-reliability procedure

Preferred frozen procedure:

1. one primary reviewer screens all records;
2. a second independent reviewer screens:
   - a reproducible random 20% sample of title/abstract records;
   - all `UNCERTAIN` title/abstract records;
   - all records entering full-text screening;
3. disagreements are adjudicated and logged;
4. calculate agreement on the double-screened title/abstract subset;
5. if disagreement is unexpectedly high, expand double screening before synthesis.

If a second independent reviewer cannot be obtained, the manuscript must transparently report the single-reviewer limitation and use an independently repeated verification pass for all borderline/full-text decisions. It must not falsely claim dual independent screening.

---

# 17. Full-text retrieval policy

For records passing title/abstract screening:

1. seek publisher full text first;
2. use institutional/library access where lawful;
3. use author/institutional repositories where available;
4. do not treat unavailable full text as an automatic scientific exclusion without documenting retrieval attempts;
5. track:
   - full text retrieved;
   - full text unavailable;
   - reason/access path.

When only abstract-level evidence is available, do not extract claims requiring methods/results verification.

---

# 18. Data extraction matrix

Create one row per distinct study/experiment.

## Bibliography

- Study ID
- Record IDs
- Authors
- Year
- Title
- Venue
- DOI
- Publication type
- peer-reviewed / defended / preprint
- project source reliability A/B/C/D

## Language

- language
- family
- morphological type
- script(s)
- low-resource justification
- orthographic variation
- transliteration issue

## Retrieval task

- ad-hoc document retrieval
- passage retrieval
- legal/domain retrieval
- RAG retrieval
- other
- retrieval unit

## Corpus

- source
- domain
- number of documents/passages
- token count if reported
- public/private
- deduplication
- language identification

## Queries / qrels

- number of queries
- query source
- query type/length
- human/synthetic
- number of relevant items if reported
- qrels method
- pooling
- pool depth
- assessors
- agreement
- adjudication

## Morphology intervention

- raw
- stem
- lemma
- root
- morphological analysis
- morpheme segmentation
- character/prefix truncation
- subword processing
- orthographic normalization
- script normalization/transliteration
- query/document/both

## Retrieval system

- TF-IDF / VSM
- BM25 / variant
- language-model retrieval
- learned sparse
- dense retriever
- dense checkpoint
- retrieval-trained vs generic embedding
- late interaction
- reranker
- hybrid system
- RAG system

## Hybrid protocol

- fusion method
- score normalization
- alpha/weights
- RRF parameter
- candidate depth
- same dense model across morphology variants?
- same dense preprocessing?
- same fusion configuration?
- dev/test tuning separation?

## Metrics

- P@k
- Recall@k
- MAP
- MRR
- nDCG@k
- bpref
- Hit@k
- latency
- index/vocabulary size
- other

## Statistical evidence

- paired test
- confidence intervals
- effect size
- multiple-comparison control
- ablation
- per-query analysis

## Complementarity evidence

- lexical-only relevant hits
- dense-only relevant hits
- intersection
- overlap/Jaccard/other
- union
- oracle union
- incremental hybrid gain
- query-level morphology effect
- query-feature analysis

## Interpretation

- strongest numerical result
- within-study morphology delta
- what the study supports
- what it does not support
- limitations
- Uzbek relevance
- evidence level 0–5

---

# 19. Quality / risk-of-bias appraisal

Do not create an arbitrary summed “quality score”.

Assess each domain independently:

1. source reliability;
2. corpus transparency;
3. query validity;
4. qrels/relevance-judgment validity;
5. comparator fairness;
6. control of morphology-specific confounders;
7. metric appropriateness;
8. statistical evidence;
9. reproducibility;
10. strength of causal interpretation.

Domain judgment:

- `LOW CONCERN`
- `SOME CONCERN`
- `HIGH CONCERN`
- `NOT APPLICABLE`

The project A/B/C/D source-reliability tier remains a separate field.

---

# 20. Synthesis plan

## 20.1 Descriptive map

Report:

- studies per year;
- studies per language;
- morphology method distribution;
- retrieval paradigm distribution;
- benchmark-size distribution;
- proportion with qrels;
- proportion with statistical testing;
- proportion with public data/code.

## 20.2 Morphology × retrieval matrix

Build a matrix crossing morphology with:

- lexical;
- learned sparse;
- dense;
- late interaction;
- hybrid;
- controlled complementarity.

## 20.3 Language evidence matrix

For each language report presence/absence of:

- lexical morphology evidence;
- dense retrieval evidence;
- hybrid retrieval;
- controlled raw/stem/lemma comparisons;
- complementarity analysis.

## 20.4 Direction-of-effect synthesis

Within comparable study-level contrasts classify results as:

- morphology improves;
- approximately unchanged;
- morphology worsens;
- mixed/query-dependent.

Report within-study relative deltas when valid.

Do not pool absolute MAP/nDCG/MRR values across unrelated datasets as if directly comparable.

## 20.5 Meta-analysis rule

No statistical meta-analysis is planned by default.

A meta-analysis may be added only if the final evidence corpus contains a sufficiently homogeneous subset with compatible:

- intervention;
- comparator;
- dataset/task;
- metric;
- reported uncertainty or recoverable effect-size information.

Any such addition requires a protocol amendment.

## 20.6 Complementarity synthesis

For every Level 3–5 study determine:

- whether hybrid improvement occurs;
- whether component candidate sets are analyzed;
- whether morphology itself is isolated;
- whether the same dense model is used;
- whether fusion is held constant;
- whether unique-hit/overlap/oracle evidence exists.

This is the central synthesis for linkage to the PhD.

---

# 21. Uzbek/Turkic synthesis rules

The Uzbek evidence section must keep separate:

1. **morphology resources/infrastructure**
2. **semantic similarity / language representations**
3. **corpus-level lexical retrieval**
4. **dense retrieval**
5. **hybrid retrieval**
6. **RAG answer-quality studies**
7. **controlled morphology × fixed-dense complementarity evidence**

Do not convert:

- analyzer accuracy;
- corpus-processing accuracy;
- STS correlation;
- chatbot answer accuracy;
- deployment/productivity gains

into IR effectiveness claims.

---

# 22. Predefined gap-killer audit

During full-text screening/extraction, flag any study that contains most or all of:

1. multiple morphology variants;
2. same fixed dense retriever;
3. controlled lexical+dense fusion;
4. overlap/intersection analysis;
5. unique relevant hits / union / oracle union;
6. morphology-conditioned incremental hybrid gain.

A direct analogue must trigger:

- full deep dive;
- re-evaluation of `research/CURRENT_GAP.md`;
- update of gap history if the gap changes.

Do not wait until manuscript writing to perform this check.

---

# 23. Closest-work priority set

The following families require especially careful full-text verification because they can change the evidence boundary:

- UPERF and related Urdu retrieval work;
- morphology-aware Arabic hybrid/legal IR;
- GreekBarRetrieval;
- Sunay & Yigit-Sert Turkish RAG morphology normalization;
- Korean tokenization × BM25/DPR;
- Amharic lexical/neural retrieval comparisons;
- Kazakh morphology + lexical/embedding retrieval;
- ACL `P12-2043` — *Arabic Retrieval Revisited: Morphological Hole Filling*;
- morphology-aware RAG studies in Turkish, Urdu, Persian, Arabic;
- Uzbek hybrid/RAG studies (USHRA, O-RAG, Urinov, and verified newer work).

This is a prioritization rule, not automatic inclusion.

---

# 24. Review update-search rule

Immediately before manuscript submission:

1. rerun all accessible frozen primary strategies;
2. update the ACL Anthology snapshot to the then-current official commit;
3. record new search/update dates;
4. screen only records newly added since the main search;
5. merge them into the existing PRISMA/extraction workflow;
6. do not silently alter the conceptual search logic.

Because the freeze occurs during 2026, the update search is mandatory if submission occurs later in 2026 or beyond.

---

# 25. Protocol-amendment rule

Any post-freeze change must be written to an amendment log with:

- amendment ID;
- date;
- trigger;
- old rule;
- new rule;
- scientific reason;
- affected sources;
- whether reruns are required;
- whether previously screened records are affected.

Examples requiring amendment:

- adding Scopus/WoS;
- changing eligibility criteria;
- changing source-specific conceptual search logic;
- adding a meta-analysis;
- changing reviewer-reliability procedure;
- changing evidence-level definitions.

Pure correction of a typo that does not change logic should still be logged as editorial, not methodological.

---

# 26. Data files to preserve

At minimum preserve:

- frozen protocol;
- protocol amendment log;
- source-specific exact queries;
- raw exports;
- raw ACL metadata snapshot identifier;
- ACL search script;
- export hashes;
- merged master-record table;
- deduplication log;
- title/abstract screening log;
- full-text screening log;
- exclusion-reason table;
- extraction matrix;
- quality-appraisal table;
- included-study bibliography;
- PRISMA counts;
- synthesis tables/figures;
- update-search files.

---

# 27. Planned manuscript structure

1. Introduction
2. Scope and Terminology
3. Review Methodology
4. Morphology in Classical Lexical Retrieval
5. Morphology in Dense and Neural Retrieval
6. Morphology in Hybrid Lexical–Semantic Retrieval
7. From Aggregate Effectiveness to Complementarity
8. Uzbek and Turkic Evidence
9. Cross-Study Evidence Synthesis
10. Evaluation and Benchmarking Gaps
11. Research Agenda
12. Threats to Validity
13. Conclusion

---

# 28. Planned figures and tables

Core figures:

1. PRISMA flow
2. morphology × retrieval paradigm × evidence-target taxonomy
3. chronology/timeline
4. evidence ladder 0–5
5. language × retrieval heatmap
6. morphology × retrieval heatmap

Core tables:

1. terminology/methodological distinctions
2. comparison with existing reviews
3. included-study characteristics
4. morphology-aware lexical evidence
5. dense/hybrid morphology evidence
6. Uzbek/Turkic evidence matrix
7. evaluation/qrels quality
8. complementarity evidence
9. remaining evidence gaps / design requirements

---

# 29. Safe novelty wording before final synthesis

Use only wording equivalent to:

> Existing reviews have examined document retrieval for low-resource languages and stemming for resource-poor languages, but these literatures do not by themselves provide a focused synthesis of how explicit morphological representation interacts with the transition from lexical to dense and hybrid corpus-level retrieval. This review maps morphology interventions against retrieval paradigms and levels of experimental evidence, with particular attention to whether morphology changes only aggregate effectiveness or also the composition and complementarity of lexical and semantic retrieval results. Uzbek evidence is analyzed separately to distinguish language-resource and search-infrastructure results from controlled retrieval-effectiveness evidence.

Do not use “first” before the final novelty audit.

---

# 30. Claims prohibited before evidence synthesis

Do not claim in advance that:

- Uzbek hybrid retrieval does not exist;
- Uzbek semantic retrieval does not exist;
- morphology has not been used in Uzbek search;
- lemma is better than stem;
- morphology always improves retrieval;
- dense retrieval removes the need for morphology;
- hybrid always beats standalone retrieval;
- RRF/fixed fusion/dynamic alpha is novel;
- no prior morphology+dense study exists;
- no Level-5 complementarity study exists.

---

# 31. Relationship to the PhD

This review is an independent publication that supports the PhD through:

- systematic literature evidence;
- an auditable evidence boundary;
- identification of benchmark/design weaknesses;
- evidence for or against the current residual gap.

It does not present the planned Uzbek experiment as completed.

The current PhD experimental chain remains:

`BM25_raw / BM25_stem / BM25_lemma`
→ same fixed dense retriever `D`
→ controlled hybrid conditions
→ per-query complementarity analysis.

The review may force revision of this design if stronger prior evidence is found.

---

# 32. Frozen execution sequence

## Phase 1 — Final exports

1. EBSCO exact tested S4 — full export.
2. PQDT P2 — full export.
3. IEEE I1 — full export, respecting platform export limits.
4. ACL A1 + A2R — export from deterministic script.
5. Preserve supplementary ACM/SciSpace/national/citation-chaining records separately.

## Phase 2 — Merge and deduplicate

6. Build master record table.
7. Preserve source provenance.
8. Deduplicate according to Section 15.
9. Freeze PRISMA identification counts for the main search date.

## Phase 3 — Screening

10. Title/abstract screening.
11. Independent verification subset/borderline review.
12. Full-text retrieval.
13. Full-text screening with exclusion codes.

## Phase 4 — Extraction / appraisal

14. Study-level merge.
15. Data extraction.
16. Evidence-level classification.
17. Quality/risk-of-bias appraisal.
18. Direct gap-killer audit.

## Phase 5 — Synthesis

19. Descriptive evidence map.
20. morphology × retrieval matrix.
21. language matrix.
22. dense/hybrid/complementarity synthesis.
23. Uzbek/Turkic evidence boundary.
24. update research gap only if evidence requires it.

## Phase 6 — Manuscript

25. Write Results first.
26. Write Discussion.
27. Write Introduction after the evidence structure stabilizes.
28. Write Abstract last.
29. Run mandatory update search before submission.
30. Final PRISMA-S audit.

---

# 33. Freeze decision

**STATUS: FROZEN FOR FULL SYSTEMATIC-REVIEW EXECUTION**

The query-development phase is closed for the currently accessible core sources.

Frozen strategies:

| Source | Frozen strategy | Pilot/result count | Status |
|---|---|---:|---|
| EBSCOhost: ASP + Science & Technology Collection + LISTA | exact tested **S4** | **527** | ACCEPTED |
| PQDT Global | **P2** | **126** | ACCEPTED |
| IEEE Xplore | **I1** | **1,256** | ACCEPTED |
| ACL Anthology | **A1** | **83** | ACCEPTED |
| ACL Anthology supplemental | **A2R** | **255** | ACCEPTED |
| ACM Digital Library | targeted supplementary only | N/A | BASIC ACCESS LIMITATION |
| SciSpace | supplementary discovery only | N/A | SUPPLEMENTARY |
| Scopus / Web of Science | optional amendment if access becomes available | N/A | NOT A FREEZE BLOCKER |

No further query refinement should be performed merely to make result counts smaller or search strings prettier.

The next scientific task is **full systematic-review execution**, beginning with final exports and deduplication.

---

# 34. Final caution

Freezing this protocol does not validate the PhD research gap.

The review must remain capable of finding evidence that:

- narrows the gap;
- changes the gap;
- or invalidates the gap.

The correct logic remains:

`literature → evidence → gap → research questions → hypotheses → experiments → method/novelty`.
