# ARTICLE RESEARCH PROTOCOL v0.8

**Project:** PhD — Uzbek Hybrid Information Retrieval  
**Protocol date:** 2026-09-16  
**Status:** WORKING / EBSCO S4 ACCEPTED; PQDT P2 ACCEPTED; ACM/IEEE/ACL PILOTS PENDING  
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

A focused novelty audit was conducted on 2026-09-16 before freezing the review protocol.

The audit distinguishes **four neighboring review traditions**:

1. morphology/stemming in classical IR;
2. stemmer surveys across languages;
3. broad low-resource document retrieval surveys;
4. dense/hybrid retrieval surveys.

The proposed article must sit **between** these traditions rather than duplicate any one of them.

### 3.1 Pirkola (2001) — morphological typology for IR

**Work:** Ari Pirkola, *Morphological Typology of Languages for IR*, *Journal of Documentation* 57(3), 330–348.  
**DOI:** `10.1108/EUM0000000007085`.

**Scope:**

- theoretical morphological typology from an IR perspective;
- synthesis/fusion dimensions;
- review of morphology/stemming effects across languages;
- mono- and cross-language IR motivation.

**Boundary relative to our review:**

- foundational morphology-for-IR framing;
- pre-dense, pre-neural, pre-modern hybrid retrieval;
- no systematic evidence ladder from lexical morphology to fixed-dense complementarity.

This work should be treated as an early conceptual anchor, not as a competing modern systematic review.

---

### 3.2 Kettunen (2009) — morphological variation in monolingual IR

**Work:** Kimmo Kettunen, *Reductive and generative approaches to management of morphological variation of keywords in monolingual information retrieval: An overview*, *Journal of Documentation* 65(2).  
**DOI:** `10.1108/00220410910937615`.

**Scope:**

- overview of methods for managing morphological keyword variation;
- results compiled across 11 mostly European languages;
- reductive and generative morphological strategies;
- retrieval-effectiveness comparison in classical monolingual IR.

**Boundary relative to our review:**

This is one of the closest historical predecessors, but:

- its evidence landscape predates modern dense retrieval;
- it does not study sparse–dense/hybrid retrieval;
- it does not organize evidence around morphology-conditioned lexical–dense complementarity;
- it cannot address modern retrieval-trained multilingual encoders, late interaction or modern fusion.

The proposed review should explicitly describe itself as extending the morphology–IR evidence question into the dense/hybrid era rather than rediscovering the classical morphology literature.

---

### 3.3 Moral et al. (2014) — stemming algorithms in IR

**Work:** Cristian Moral, Angélica de Antonio, Ricardo Imbert & Jaime Ramírez, *A survey of stemming algorithms in information retrieval*, *Information Research* 19(1).

The paper reviews:

- major stemming algorithms;
- stemmer-evaluation measures;
- non-English stemmers;
- historical effects of stemming in IR.

A crucial scope boundary in the paper is that **lemmatization is explicitly treated as a separate field and is not addressed**.

**Boundary relative to our review:**

- stemmer-centric rather than representation-centric;
- pre-dense retrieval;
- does not compare raw/stem/lemma/root/morpheme choices across modern retrieval paradigms;
- no dense/hybrid/complementarity synthesis.

---

### 3.4 Dave, Mehta & Kotecha (2024) — TALLIP systematic stemmer review

**Work:** Nakul R. Dave, Mayuri A. Mehta & Ketan Kotecha, *A Systematic Review of Stemmers of Indian and Non-Indian Vernacular Languages*, *ACM Transactions on Asian and Low-Resource Language Information Processing* 23(1).  
**DOI:** `10.1145/3604612`.

This is especially important because it was published in the **primary target journal, TALLIP**.

**Scope:**

- systematic catalogue of stemmers;
- 15 Indian and 17 non-Indian languages;
- more than 100 stemming approaches according to associated summaries;
- language-wise comparison;
- dictionaries, WordNets and datasets;
- over-/under-stemming problems and future directions.

**Boundary relative to our review:**

The unit of analysis is the **stemmer**.

The unit of analysis in the proposed article is the **retrieval experiment and the evidence produced when morphological representation changes**.

Therefore our review must not become another catalogue of stemming algorithms.

It must extract:

`morphological representation`
→ `retrieval paradigm`
→ `evaluation design`
→ `retrieval effect`
→ `component interaction / complementarity evidence`.

This distinction must be made explicitly in the TALLIP cover letter.

---

### 3.5 Kazi, Khoja & Daud (2025) — broad low-resource document retrieval SLR

**Work:** Samreen Kazi, Shakeel Khoja & Ali Daud, *Bridging the gap: A survey of document retrieval techniques for high-resource and low-resource languages*, *Computer Science Review* 57, 100756.  
**DOI:** `10.1016/j.cosrev.2025.100756`.

This is the closest **broad modern retrieval review**.

It uses a systematic-literature-review methodology following PRISMA and covers:

- traditional/sparse retrieval;
- neural/dense retrieval;
- hybrid retrieval;
- datasets and benchmarks;
- low-resource challenges;
- especially Arabic, Urdu and Hindi in its LRL-focused analysis.

Morphological complexity and orthographic variation are important LRL challenges in that paper, but morphology is not the organizing experimental axis of the review.

**Boundary relative to our review:**

Our article must not ask:

> What retrieval methods exist for low-resource languages?

It instead asks:

> When an explicit morphological representation or normalization intervention is made, what retrieval evidence is produced, and how does that evidence change as the field moves from lexical to dense and hybrid retrieval?

The dedicated Uzbek/Turkic evidence boundary and the set-complementarity layer are additional differentiators.

---

### 3.6 Zhao et al. (2024) — dense retrieval survey

**Work:** Wayne Xin Zhao et al., *Dense Text Retrieval Based on Pretrained Language Models: A Survey*, *ACM Transactions on Information Systems* 42(4), Article 89.  
**DOI:** `10.1145/3637870`.

It organizes PLM-based dense retrieval around:

- architecture;
- training;
- indexing;
- integration.

It also covers sparse–dense integration.

**Boundary relative to our review:**

- dense retrieval itself is the unit of analysis;
- morphology-rich/low-resource representation is not the review axis;
- no raw/stem/lemma evidence synthesis;
- no morphology-conditioned complementarity analysis.

This paper is a terminology/architecture source, not a competing morphology review.

---

### 3.7 Sparse–dense / hybrid surveys

Recent reviews and theses also synthesize sparse, dense and hybrid retrieval, including a 2025 survey by Mustafa et al. on sparse–dense retrieval and a 2025 taxonomy-oriented thesis by Boghara.

These sources matter for hybrid terminology but do not replace the proposed morphology-centered synthesis.

The proposed review must distinguish:

- **representation hybrid** — e.g. RAW + LEMMA representations;
- **retrieval hybrid** — e.g. BM25/sparse + dense retrieval.

---

### 3.8 Roy, Anas & Kandasamy (2026) — resource-poor stemming review

**Work:** *Stemming Techniques for Resource-Poor Languages: A Review of Methods, Challenges, and Applications*, *Frontiers in Artificial Intelligence* 9 (2026).  
**DOI:** `10.3389/frai.2026.1875268`.

It covers:

- rule-based;
- statistical;
- unsupervised;
- hybrid;
- neural-assisted stemming;
- multiple language families including Turkic;
- applications including IR, classification, sentiment, topic modeling and semantic similarity.

**Boundary relative to our review:**

This is a **stemming-method survey across NLP applications**.

Our article is a **corpus-level retrieval evidence synthesis** spanning multiple morphology representations, including but not limited to stemming.

---

### 3.9 Preliminary novelty-audit conclusion

The audit found substantial overlap around individual components, but **did not identify a review with the same combined analytical unit**:

> explicit morphological representation/intervention  
> × retrieval paradigm  
> × corpus-level experimental evidence  
> × morphology-conditioned lexical–dense interaction/complementarity.

Therefore the article remains viable.

However, the strongest safe claim before the database searches are complete is:

> **The preliminary novelty audit did not identify an existing review that systematically traces explicit morphological representation from lexical retrieval through dense and hybrid corpus-level retrieval while separately analyzing aggregate effectiveness and component complementarity evidence.**

Do **not** use “first systematic review” until the final systematic search is complete.

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

The database plan is now based on **verified institutional access through the Alisher Navoi National Library of Uzbekistan**.

The review will separate:

1. **peer-reviewed article/conference retrieval databases**;
2. **doctoral/grey-literature evidence**;
3. **discipline-native publisher indexes**;
4. **supplementary discovery/snowballing sources**.

This separation is important because not every available subscription should be treated as an equal primary systematic-search database.

### 7.1 Core bibliographic search sources — FIXED

#### EBSCOhost

Search these three databases together in the same EBSCOhost session:

- **Academic Search Premier**
- **Science & Technology Collection**
- **Library, Information Science & Technology Abstracts (LISTA)**

Rationale:

- Academic Search Premier provides broad multidisciplinary journal coverage;
- Science & Technology Collection increases technical/computing coverage;
- LISTA is directly relevant to information retrieval / information science.

These three form the **verified multidisciplinary/article-index layer** currently available to the project.

EBSCOhost deduplicates many duplicate records across simultaneously searched databases using citation metadata, but the project must still perform an independent deduplication after combining exports from all platforms.

#### Discipline-native search sources

The review must also search:

- **ACM Digital Library**
- **IEEE Xplore**
- **ACL Anthology**

Rationale:

IR/NLP evidence is strongly conference-driven. A review based only on multidisciplinary databases risks missing SIGIR, ACL/EMNLP, SIGTURK and IEEE proceedings evidence.

These are not optional background sources; they are part of the core search architecture.

---

### 7.2 Doctoral / grey-literature search source — FIXED

#### ProQuest Dissertations & Theses Global (PQDT Global)

Use PQDT Global as a **separate doctoral-evidence search**, not as a substitute for a journal/conference bibliographic database.

Purpose:

- identify defended dissertations closely related to morphology-aware IR;
- recover detailed methodology that may not appear in short conference papers;
- inspect research lines, references and experimental designs;
- reduce publication-channel bias.

Dissertations must be tagged separately in extraction and not pooled uncritically with peer-reviewed journal/conference evidence.

---

### 7.3 Available databases NOT used as core systematic-search sources

The following verified subscriptions are available but should **not** be included in the main search merely because access exists.

#### ProQuest

- Education Research Index — not aligned with the retrieval topic;
- Coronavirus Research Database — irrelevant;
- Publicly Available Content Database — broad/open-web style discovery; use only if a missing full text or bibliographic lead is needed.

#### EBSCO

- Business Source Premier — not core;
- Regional Business News — not core;
- eBook Collection — background only;
- eBook Academic Collection — background/theoretical books only;
- eBook Business Collection — not core;
- Legal Source — targeted supplementary use only if needed for legal-retrieval evidence;
- Art Source — not core;
- GreenFILE — not core;
- MasterFILE Premier — too broad for core search;
- ERIC — not core;
- Education Research Complete — not core;
- MEDLINE with Full Text — optional targeted supplementary search for biomedical retrieval only;
- reference eBook subscription — background only;
- European Views of the Americas — irrelevant;
- OpenDissertations — redundant with stronger PQDT Global doctoral access;
- eBook Open Access Collection — background/discovery only.

This restriction improves methodological specificity and prevents the PRISMA search from being inflated by databases with low topical yield.

---

### 7.4 Desired major citation indexes — OPTIONAL ENHANCERS

#### Web of Science Core Collection

If official access is obtained, add WoS as a major multidisciplinary citation-index search and report it separately.

#### Scopus

If official access is obtained, add Scopus as a second major multidisciplinary citation-index search.

### Critical decision

**Neither Scopus nor Web of Science is now a hard prerequisite for beginning or completing the systematic review.**

The minimum viable primary search architecture is:

`EBSCOhost (ASP + Science & Technology + LISTA)`
+
`ACM DL`
+
`IEEE Xplore`
+
`ACL Anthology`
+
`PQDT Global doctoral search`
+
`snowballing / citation chaining`.

If WoS and/or Scopus become available before protocol freeze or before the final update search, they should be added and fully documented.

---

### 7.5 Supplementary discovery / sensitivity sources

Use only as supplementary sources:

- SciSpace;
- Google Scholar, if needed for forward citation discovery;
- publisher searches;
- official university/national repositories;
- Uzbek/Russian/Uzbek-language national searches;
- reference lists of included papers and closest reviews.

Records discovered only through supplementary channels must be labelled by discovery source.

---

### 7.6 Database/platform reporting rule

In the manuscript report the **database name and platform separately**, for example:

- Academic Search Premier (**EBSCOhost**)
- Science & Technology Collection (**EBSCOhost**)
- Library, Information Science & Technology Abstracts (**EBSCOhost**)
- ProQuest Dissertations & Theses Global (**ProQuest**)

Do not write only “EBSCO” or only “ProQuest” in the Methods section.

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

The search strategy is revised after a seed-recall audit.

### 9.1 Design principle

The primary search must **not require a low-resource-language block**.

Reason:

- some important morphology-aware IR work is conducted in Finnish, Greek or other morphologically rich languages that may not be labelled “low-resource”;
- papers may not self-describe the language as “morphologically rich” in title/abstract/keywords;
- requiring a language/resource-status block would reduce recall.

Language/resource status will therefore be coded during screening and extraction, not used as a mandatory eligibility keyword in the main query.

---

### 9.2 Block A — Retrieval

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
```

**Do not use the bare acronym `RAG` in the core query**, because it can introduce unrelated acronym matches.

---

### 9.3 Block B — Explicit morphology / representation intervention

```text
morpholog*
OR stemm*
OR lemmat*
OR "morphological normalization"
OR "morphological analysis"
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
```

Avoid an unrestricted `root*` term because it creates substantial non-linguistic noise.

---

### 9.4 Block C — Language/resource sensitivity terms

This block is **supplementary**, not mandatory in the primary search:

```text
"low-resource"
OR "low resource"
OR "under-resourced"
OR "morphologically rich"
OR "morphologically complex"
OR agglutinative
OR Uzbek
OR Turkish
OR Turkic
OR Greek
OR Finnish
OR Hungarian
OR Basque
OR Urdu
OR Arabic
OR Persian
OR Bengali
OR Marathi
OR Hindi
OR Kazakh
OR Kyrgyz
OR Azerbaijani
OR Uyghur
OR Shona
```

The list is a discovery aid, not the definition of eligible languages.

---

### 9.5 Why multiple search layers are required

A crucial pilot finding is that **GreekBarRetrieval (2026)** is a relevant morphology-sensitive study, because its full experiment contains stemming/lemmatization-oriented BM25 variants, yet its title and abstract mainly say “three BM25 variants” and do not necessarily expose the morphology terms required by the core Boolean query.

Therefore a single `retrieval AND morphology` query is not sufficiently sensitive.

The final search must use:

1. core retrieval × morphology search;
2. targeted language/retrieval sensitivity searches;
3. backward citation chaining;
4. forward citation chaining;
5. known-review reference mining;
6. targeted searches around newly found Level 2–5 studies.

This is a methodological requirement, not an optional convenience.

## 10. Proposed Scopus search

### 10.1 Primary high-recall Scopus query — candidate v0.3

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
)
AND PUBYEAR > 1999
AND PUBYEAR < 2027
```

### 10.2 Why this version changed

The pre-authenticated pilot added:

- `"semantic search"` — some modern papers use this term instead of `semantic retrieval`;
- `"vector search"` — captures modern embedding retrieval terminology;
- `"morphological processing"` / `"morphological preprocessing"` — common wording in IR papers;
- `"term conflation"` — captures older morphology-aware IR terminology.

The query deliberately does **not** use a large `NOT` block. Screening is safer than aggressive Boolean exclusion because exclusion terms may remove relevant retrieval studies.

### 10.3 Supplemental language-sensitive query family

A second query family must combine retrieval terms with language/resource terms **without requiring an explicit morphology keyword**, then screen the results for morphology-sensitive experimental conditions.

```text
TITLE-ABS-KEY(
  (
    "information retrieval"
    OR "document retrieval"
    OR "text retrieval"
    OR "passage retrieval"
    OR "dense retrieval"
    OR "semantic retrieval"
    OR "semantic search"
    OR "vector search"
    OR "hybrid retrieval"
    OR BM25
    OR "retrieval augmented generation"
  )
  AND
  (
    <LANGUAGE OR LANGUAGE-FAMILY TERMS>
  )
)
AND PUBYEAR > 1999
AND PUBYEAR < 2027
```

Priority batches: Uzbek/Turkic; Finnish/Hungarian/Basque; Arabic/Persian/Urdu; Bengali/Marathi/Hindi; Greek; Shona and newly discovered morphology-rich languages.

### 10.4 Pre-authenticated seed-recall audit — 2026-09-16

**Important:** direct Scopus web access from the current environment returned HTTP `403 Forbidden`, so this is **not an authenticated Scopus result-count run**.

Title/abstract/keyword content was instead checked via publisher pages, ACL Anthology, institutional repositories and bibliographic records.

| Seed study | Core query expected? | Why |
|---|---|---|
| Pirkola 2001 — Morphological Typology of Languages for IR | YES | title/abstract: morphology + IR |
| Kettunen et al. 2005 — Finnish stem vs lemma | YES | title: stem / lemmatize + IR |
| Semmar et al. 2006 — Arabic | YES | stemming + morphological analysis + IR |
| Kadri & Nie 2006 — Arabic | YES | stemming + IR |
| Can et al. 2008 — Turkish | YES | abstract: IR + stemming + lemmatizer |
| Kettunen 2009 — morphology variation overview | YES | morphology + monolingual IR |
| Haddad & Bechikh Ali 2014 — Turkish | YES | abstract: IR + stemming |
| selective stemming / classical IR studies | YES | explicit stemming + IR |
| UPERF 2024 — Urdu | YES | morphology/stemmed preprocessing + retrieval |
| Aboasal et al. 2026 — Arabic legal IR | YES | morphological segmentation + IR |
| Munetsi et al. 2026 — Shona SIGIR | YES | title: morphology-aware retrieval |
| Sunay & Yigit-Sert 2026 — Turkish RAG | YES | morphological normalization + retrieval |
| GreekBarRetrieval 2026 | **NOT GUARANTEED** | morphology appears in system details rather than abstract wording |
| Kazi & Khoja 2026 — U-RR² Urdu | **NOT GUARANTEED** | abstract says script/word variation without explicit morphology terms |

Pre-authenticated conceptual core recall: **12/14 = 85.7%**.

Both non-guaranteed studies motivate the supplemental language-sensitive search and citation chaining.

### 10.5 Precision/noise observations

The core query will intentionally retrieve some contextual studies that mention IR as an application but do not evaluate corpus-level retrieval, including lemmatizer-development and generic preprocessing papers. This is acceptable.

**Decision:** optimize for recall and enforce corpus-level retrieval eligibility during screening. Do not add aggressive exclusions before the authenticated pilot provides actual result counts and false-positive categories.

### 10.6 Query recall vs Scopus coverage

Do not conflate:

1. **query recall** — would the Boolean expression retrieve an indexed study from its searchable metadata?;
2. **database coverage** — is the study/venue actually indexed by Scopus for that year/document type?

The current audit tests mainly query recall. Authenticated Scopus must verify coverage separately.

### 10.7 Authenticated Scopus freeze gate

Before `v1.0 FROZEN`, record:

- exact search date/time;
- exact query;
- total result count;
- filters;
- document-type and year distributions;
- top source titles;
- main irrelevant-result categories;
- seed studies retrieved;
- seed studies absent;
- whether each absence is a coverage miss or query miss.

Recommended export fields:

- Authors
- Title
- Year
- Source title
- DOI
- Abstract
- Author keywords
- Index keywords
- Document type
- Affiliations
- EID / Scopus identifier
- References if available

Saved-search name:

`MORPH_IR_REVIEW_CORE_v0_3_2026-09-16`

### 10.8 Web of Science replication

Repeat the conceptual query in Web of Science Core Collection using database-specific syntax. Record result counts and seed recall separately.

### 10.9 Search-query change control

After `v1.0` freeze, syntax adaptations preserving the same concepts are allowed and logged. New concept blocks require a documented amendment. Do not add a term merely because it selectively retrieves a desired paper.

## 10A. Independent academic-index validation — SciSpace, 2026-09-16

An independent semantic-search validation was run in SciSpace after the pre-authenticated Scopus audit.

This does **not** replace Scopus or Web of Science in the PRISMA protocol. Its role is:

- discover additional candidate studies;
- stress-test the review taxonomy;
- identify terminology not captured by the Boolean query;
- check whether an obvious Level-5 gap killer exists.

### 10A.1 Search A — explicit morphology × corpus-level retrieval

Natural-language query:

> Which peer-reviewed studies since 2000 evaluate explicit morphological normalization, stemming, lemmatization, morphological segmentation, or other morphology-aware text representations in corpus-level information retrieval, including lexical, dense, semantic, neural, or hybrid retrieval for morphologically rich or low-resource languages?

Important additional candidate studies returned:

#### Fautsch & Savoy (2009)

**Algorithmic Stemmers or Morphological Analysis? An Evaluation**  
DOI: `10.1002/asi.21093`

Relevance:

- direct stemming vs morphological-analysis comparison;
- CLEF test collections;
- 284 queries;
- multiple IR models;
- reported MAP improvement from stemming;
- useful classical evidence that more linguistically elaborate processing does not automatically outperform algorithmic stemming.

**Systematic-review category:** Level 1 morphology-aware lexical retrieval.

---

#### Hahn, Honeck & Schulz (2003)

**Subword-based text retrieval**  
DOI: `10.1109/HICSS.2003.1174249`

Relevance:

- replaces word-level matching with morphologically segmented subwords;
- stems/prefixes/suffixes become indexing/retrieval units;
- large biomedical collection;
- extends taxonomy beyond stem/lemma/root.

**Taxonomy consequence:** retain explicit `morpheme/subword segmentation` category.

---

#### Schultz, Honeck & Hahn (2002)

**Biomedical text retrieval in languages with a complex morphology**  
DOI: `10.3115/1118149.1118158`

Relevance:

- morphology-rich retrieval;
- subword indexing;
- early evidence that morphology-aware representation can alter the retrieval unit itself.

---

#### Yeshambel, Mothe & Assabie (2020)

**Amharic Document Representation for Adhoc Retrieval**  
DOI: `10.5220/0010177301180128`

Relevance:

- Amharic ad-hoc retrieval;
- stem-based vs root-based representations;
- TREC-like evaluation;
- root-based representation reported stronger than stem-based representation.

**Systematic-review category:** Level 1.

**Taxonomy consequence:** `root-based representation` must remain distinct from stemming.

---

#### MORSE-QE (2026)

**MORSE-QE: A Morphology-Aware, Embedding-Driven Framework with Root Extraction for Arabic Dialectal Query Expansion**  
DOI reported by SciSpace: `10.31449/inf.v49i20.9628`

Relevance:

- morphology-aware Arabic retrieval;
- dialect-to-MSA normalization;
- root extraction;
- embedding-based expansion;
- TREC Arabic corpus;
- MAP / P@10 / root-recall reporting;
- ablation evidence reported in the indexed abstract.

**Important:** full bibliographic and methods verification is required before this study is treated as established evidence.

**Likely category:** Level 2/3 boundary depending on exact retrieval architecture.

---

### 10A.2 Search B — closest reviews and morphology/dense boundary

Natural-language query:

> Which peer-reviewed surveys or systematic reviews since 2000 synthesize the effects of stemming, lemmatization, morphological normalization, morphological segmentation, or morphology-aware representations specifically for information retrieval, and which surveys cover dense, semantic, or hybrid retrieval in low-resource or morphologically rich languages?

The search did not reveal an obvious review duplicating the proposed analytical unit.

It surfaced:

- computational-morphology surveys;
- embedding reviews for morphologically rich languages;
- dense retrieval studies in low-resource languages;
- morphology-aware primary IR studies.

These are adjacent rather than duplicative.

### 10A.3 Search C — direct Level-5 gap-killer query

Natural-language query:

> Are there peer-reviewed information retrieval studies that explicitly compare multiple morphological representations such as raw, stemmed, lemmatized, root-based, or morphologically segmented lexical retrieval against the same fixed dense or semantic retriever, and then analyze overlap, unique relevant hits, union coverage, oracle union, or morphology-conditioned hybrid gain?

Returned results were mostly:

- learned sparse lexical representations;
- generic sparse–dense complementarity;
- morphology-aware lexical retrieval;
- stemming/lemmatization comparisons;
- dense retrievers designed to imitate sparse behavior.

No returned record clearly satisfied the full pattern:

`multiple lexical morphology conditions`
× `same fixed dense retriever`
× `controlled fusion`
× `relevant-set overlap/unique-hit/oracle-union analysis`.

### Interpretation

This is **supporting evidence only**, not proof of absence.

The review and PhD must still phrase the claim conservatively:

> The searches conducted so far have not identified a study that clearly reports the complete controlled morphology-conditioned lexical–dense complementarity design.

Do not write:

> No such study exists.

---

### 10A.4 New retrieval-evidence categories confirmed by SciSpace

The systematic extraction taxonomy should preserve at least:

- raw/surface form;
- stemming;
- lemmatization;
- root extraction;
- morpheme/subword segmentation;
- character/prefix truncation;
- morphology-aware query expansion;
- orthographic/script normalization;
- dense-side morphological normalization;
- representation hybrid;
- retrieval hybrid.

---

### 10A.5 Candidate papers to add to the review screening seed set

Add to the mandatory seed/known-study list:

1. Fautsch & Savoy (2009) — DOI `10.1002/asi.21093`
2. Schultz, Honeck & Hahn (2002) — DOI `10.3115/1118149.1118158`
3. Hahn, Honeck & Schulz (2003) — DOI `10.1109/HICSS.2003.1174249`
4. Yeshambel, Mothe & Assabie (2020) — DOI `10.5220/0010177301180128`
5. Kurimo, Creutz & Turunen (2008) — *Morpho Challenge Evaluation by Information Retrieval Experiments*, DOI `10.1007/978-3-642-04447-2_131`
6. Balakrishnan & Lloyd-Yemoh (2014) — *Stemming and Lemmatization: A Comparison of Retrieval Performances*, DOI `10.7763/LNSE.2014.V2.134`
7. Darwish, Ali & Abdelali (2014) — morphology-equivalence query expansion study
8. MORSE-QE (2026) — pending independent verification

These studies should not all be assumed eligible until full-text screening, but they are useful seed-recall controls.

---

### 10A.6 Protocol consequence

The independent academic-index validation **supports proceeding**.

It does not justify freezing the protocol yet because:

- SciSpace is not one of the designated primary bibliographic databases;
- actual Scopus/WoS result counts remain unavailable;
- Scopus indexing coverage of the newest 2026 sources still needs direct confirmation.

The next freeze gate remains:

`authenticated Scopus`
→ `authenticated WoS`
→ `seed recall + coverage audit`
→ `v1.0 FROZEN`.


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

A fresh publication was discovered and audited during protocol preparation:

**Muhammed Berkay Sunay & Sevgi Yigit-Sert (2026)**  
*The Effect of Morphological Normalization on Retrieval Performance and Answer Accuracy in Turkish RAG Systems*  
34th Signal Processing and Communications Applications Conference (SIU 2026).  
**DOI:** `10.1109/SIU71813.2026.11636534`.

### Current verification status

- conference/program provenance verified;
- IEEE bibliographic record verified;
- base RAGTurk benchmark independently checked;
- indexed method/result summary inspected;
- **full IEEE PDF not yet recovered**.

### Currently supported experimental description

The study compares:

- `RAW`;
- `LEMMA`;
- `HYBRID` representation combining raw and lemma information,

in a Turkish dense/RAG retrieval setup.

Available evidence reports retrieval evaluation with Recall/MRR and downstream generation evaluation with ROUGE/BERTScore.

The available summary reports that full lemmatization did not improve the tested multilingual dense retrieval setup and that RAW performed best.

### Critical distinction

`HYBRID` in this paper should **not** be treated as lexical+sparse/dense hybrid retrieval unless the full paper explicitly establishes that.

Current evidence indicates a **representation hybrid**:

`RAW + LEMMA`

rather than a retrieval hybrid:

`BM25/sparse + dense`.

### Relation to current PhD gap

This paper kills a broad claim such as:

> morphology normalization has not been experimentally evaluated with modern dense retrieval for a Turkic language.

It does **not** currently kill the refined question:

> how changing only the lexical morphology representation changes complementarity with the same fixed dense retriever and the incremental gain from lexical–dense hybrid retrieval.

### Protocol consequence

The article taxonomy must distinguish:

1. morphology applied to the lexical branch;
2. morphology applied to the dense branch input;
3. representation hybrids such as raw+lemma;
4. retrieval hybrids such as lexical+dense fusion.

### Remaining action

Recover the full IEEE paper before using:

- exact numerical values;
- exact embedding checkpoint;
- exact lemmatizer;
- exact `HYBRID` construction;
- significance claims;
- exact query subset;
- any claim about absence/presence of BM25 or true sparse–dense fusion.

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

### Phase A — Complete protocol validation

1. Treat the Sunay & Yigit-Sert deep dive as **partial pending IEEE full text**; do not block the systematic search on this if the PDF remains unavailable.
2. Preserve the completed preliminary novelty audit against:
   - Pirkola 2001;
   - Kettunen 2009;
   - Moral et al. 2014;
   - Dave et al. 2024;
   - Zhao et al. 2024;
   - Kazi et al. 2025;
   - Roy et al. 2026;
   - modern hybrid/sparse–dense surveys.
3. Execute the first live pilot in **EBSCOhost** with exactly:
   - Academic Search Premier;
   - Science & Technology Collection;
   - LISTA.
4. Execute the separate **PQDT Global** doctoral search.
5. Pilot equivalent searches in ACM Digital Library, IEEE Xplore and ACL Anthology.
6. Record result counts, seed recall, noise categories and export capability for every platform.
7. If WoS becomes available, add a WoS pilot.
8. If Scopus becomes available, add a Scopus pilot.
9. Amend search syntax only if live result counts/noise/seed recall justify it.
10. Freeze `ARTICLE_RESEARCH_PROTOCOL_v1.0` once the accessible core-platform pilots are reproducible; do not delay the freeze solely because Scopus is unavailable.

### Phase B — Systematic search

9. Search Scopus.
10. Search Web of Science.
11. Search ACM DL.
12. Search IEEE Xplore.
13. Search ACL Anthology.
14. Perform Uzbek/Russian/Uzbek-language supplementary searches.
15. Mine reference lists of the closest reviews.
16. Perform backward and forward citation chaining from all critical Level 2–5 studies.
17. Export all records with exact search dates.
18. Deduplicate.

### Phase C — Screening

19. Title/abstract screening.
20. Full-text screening.
21. Record exclusion reasons.
22. Produce PRISMA counts.

### Phase D — Extraction

23. Build the extraction matrix.
24. Complete critical-paper deep dives.
25. Apply quality appraisal.
26. Classify each study by evidence level 0–5.
27. Add a separate field for:
   - lexical morphology;
   - dense-side morphology;
   - representation hybrid;
   - retrieval hybrid.

### Phase E — Synthesis

28. Build taxonomy.
29. Build language and method evidence maps.
30. Synthesize classical lexical morphology findings.
31. Synthesize dense-side morphology findings.
32. Synthesize true lexical–dense hybrid findings.
33. Analyze complementarity evidence.
34. Write Uzbek/Turkic evidence boundary.
35. Derive benchmark/research-design implications.

### Phase F — Manuscript

36. Draft Results from extracted data first.
37. Draft Discussion.
38. Draft Introduction after Results/Discussion stabilize.
39. Write abstract last.
40. Prepare a TALLIP cover letter explicitly distinguishing the paper from Dave et al. 2024 and Kazi et al. 2025.
41. Run a final literature-update search immediately before submission.

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

**Current decision: ACCESS SUFFICIENT TO PROCEED; START LIVE EBSCO/PQDT/ACM/IEEE/ACL PILOTS.**

The preliminary novelty audit, seed audit, SciSpace validation, and verified National Library access support the viability of the article. The protocol should **not yet be called frozen v1.0** until the exact search has been piloted on the accessible core platforms (EBSCOhost, PQDT Global, ACM DL, IEEE Xplore and ACL Anthology). Scopus and Web of Science are desirable coverage enhancers, but their absence is no longer a freeze blocker.

The strongest current positioning is:

> **Morphology is treated as an experimental change in retrieval representation, and the review traces its consequences across classical lexical retrieval, dense retrieval, representation hybrids, true lexical–dense hybrid retrieval, and—where evidence exists—relevant-set complementarity.**

The review's central distinction is therefore not simply:

`stemming vs no stemming`

and not simply:

`sparse vs dense`.

It is:

`morphological representation/intervention`
→ `retrieval paradigm`
→ `retrieval evidence`
→ `interaction/complementarity evidence`.

The preliminary audit found no identified review that fully combines those layers, while also showing that several neighboring reviews already occupy broad low-resource retrieval, dense retrieval and stemmer-survey territory.

### Protocol-freeze gate

Promote this file to:

`ARTICLE_RESEARCH_PROTOCOL_v1.0 — FROZEN`

after the accessible core sources have completed reproducible pilots:

- EBSCOhost: Academic Search Premier + Science & Technology Collection + LISTA;
- ProQuest Dissertations & Theses Global;
- ACM Digital Library;
- IEEE Xplore;
- ACL Anthology;
- seed-recall audit and documented query amendments;
- final confirmation that no newly found review duplicates the same analytical unit.

If Web of Science and/or Scopus access is obtained before freeze, include them. If access is obtained later, add them through a documented protocol amendment or final update-search round.

Until then, this document is the authoritative **v0.5 working protocol** for the planned article.

## 31. EBSCOhost controlled query-refinement decision — 2026-09-16

### 31.1 Platform and databases

Platform: **EBSCOhost**

Databases:

1. Academic Search Premier
2. Science & Technology Collection
3. Library, Information Science & Technology Abstracts (LISTA)

Date range: **2000–2026**.

No language, full-text, peer-reviewed, or document-type restriction was used. AI-assisted search, query expansion and `Apply equivalent subjects` were disabled.

### 31.2 Controlled test result

| Metric | S1 | S2 | S3 | S4 |
|---|---:|---:|---:|---:|
| EBSCO result count | 868 | 777 | 623 | **527** |
| Retention controls recovered | 8/8 | 8/8 | 8/8 | **8/8** |
| Can et al. 2008 | FOUND | FOUND | FOUND | FOUND |
| Fautsch & Savoy 2009 | FOUND | FOUND | FOUND | FOUND |
| R1 in ranked sample | 8/50 | 5/30 | 4/30 | 5/30 |
| R2 in ranked sample | 8/50 | 7/30 | 7/30 | 7/30 |
| X in ranked sample | 34/50 | 18/30 | 19/30 | 18/30 |
| R1+R2 share | 32% | **40%** | 36.7% | **40%** |

S4 reduced the platform result count by **341 records (39.3%)** relative to S1 while preserving all tested retention controls.

### 31.3 Decision

**Use S4 as the working EBSCOhost search condition.**

This is an EBSCO-specific decision, not proof that S4 has perfect sensitivity across the literature.

### 31.4 Retention controls are not a gold inclusion set

The eight records initially labelled category `A` are renamed:

**EBSCO RETENTION-CONTROL SET**

They are useful for detecting unexpected record loss during query refinement, but they are **not automatically eligible primary studies** for the systematic review.

Final inclusion requires the protocol's title/abstract and full-text eligibility rules.

### 31.5 Screening-label correction

To avoid conflict with the PhD source-reliability scale `A/B/C/D`, use:

- **R1** — clearly relevant at the current screening stage;
- **R2** — potentially relevant; full-text/further screening needed;
- **X** — clearly outside scope.

Source reliability remains separately coded `A/B/C/D`.

### 31.6 Tested S4 refinements

Replace unrestricted `stemm*` with:

```text
(
 stemmer*
 OR
 (stemm* N3
  (word* OR term* OR token* OR text* OR algorithm*
   OR language* OR document* OR index* OR retriev*))
)
```

Replace unrestricted `morpholog*` with:

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

All other concepts from the prior EBSCO query remain unchanged.

### 31.7 S4-clean verification

Because the tested replacement may duplicate explicit morphology phrases already present in S1, create a **Boolean-equivalent deduplicated `S4-clean`** before final export.

Run it once under the identical EBSCO settings.

Expected platform count: **527**.

If the count differs, preserve the exact tested S4 and investigate EBSCO parsing before bulk export.

### 31.8 Export decision

Do **not** export all 527 records yet.

Proceed first to:

1. PQDT Global pilot;
2. ACM Digital Library pilot;
3. IEEE Xplore pilot;
4. ACL Anthology pilot.

After cross-platform pilots and protocol freeze, perform the final EBSCO export.

## 32. PQDT Global pilot decision — 2026-09-16

### 32.1 Database and access

Database:

**ProQuest Dissertations & Theses Global (PQDT Global)**

Platform:

**ProQuest**

Access:

**National Library of Uzbekistan**

Search field used:

**NOFT — Anywhere except full text**

Date range:

**2000–2026**

The pilot used only PQDT Global; the other available ProQuest databases were not searched.

---

### 32.2 P1 result

The initial PQDT query (`P1`, displayed as `S1` in ProQuest history) returned:

**123 records**

Quick screening of the first 50 ranked by Relevance:

- **R1:** 20
- **R2:** 15
- **X:** 15
- **R1+R2:** 35/50 = **70%**

This is a ranked pilot sample, not an estimate of the full-result prevalence.

Among the exported first 50:

- 36 were doctoral-level records;
- 14 were master's-level records.

---

### 32.3 Coverage check

Exact-title/author checks for three known structural dissertations returned no records:

- Sheng-Chieh Lin (2024) — NOT FOUND
- Minghan Li (2024) — NOT FOUND
- Georgios Sidiropoulos (2025) — NOT FOUND

These misses must be interpreted as **PQDT coverage/discoverability limitations**, not as P1 Boolean-query failures.

Do not calculate P1 query recall using these three works.

---

### 32.4 New dissertation leads from PQDT

The pilot surfaced several high-value dissertation leads not present in the currently checked project master index, including:

1. **Eiman Tamah Al-Shammari (2010)** — *Improving Arabic text processing via stemming with application to text mining and web retrieval*
2. **Paul McNamee (2008)** — *Textual representations for corpus-based bilingual retrieval*
3. **Ibrahim Hassan Abu El-Khair (2003)** — *Effectiveness of document processing techniques for Arabic information retrieval*
4. **Kashif H. Riaz (2018)** — *Improving Search via Named Entity Recognition in Morphologically Rich Languages: A Case Study in Urdu*
5. **Güven Fidan (2012)** — *Identifying the Effectiveness of a Web Search Engine with Turkish Domain Dependent Impacts and Global Scale Information Retrieval Improvements*
6. **Abduelbaset Goweder (2004)** — *Stemming and Arabic information retrieval: The case of broken plurals*

These are **screening/deep-dive leads**, not yet accepted evidence.

---

### 32.5 ProQuest truncation correction

Current ProQuest help states:

- ordinary `*` truncation replaces up to **5 characters**;
- defined truncation `[*n]` replaces up to `n` characters, with a documented maximum of 20.

Therefore:

`lemmat*`

may retrieve forms such as `lemmatizer` but is not guaranteed to retrieve:

- `lemmatization`
- `lemmatisation`

because these require more than five trailing characters after `lemmat`.

### Required refinement

Replace **both occurrences** of:

```text
lemmat*
```

with:

```text
lemmat[*10]
```

Do not change any other P1 concept.

Call the refined query:

**P2**

---

### 32.6 Controlled P1 vs P2 rule

Run P2 under the same:

- database;
- NOFT field;
- date range;
- filter state;
- sorting mode.

Record:

- total result count;
- whether all P1 R1 records remain retrievable;
- whether any newly retrieved records contain `lemmatization/lemmatisation`;
- quick relevance of newly added records;
- any unexpected loss.

### Decision rule

If P2:

- preserves all validated P1 retention records, and
- adds plausible morphology/retrieval records or leaves the result set equivalent,

then **USE P2** as the working PQDT query.

If P2 unexpectedly loses relevant P1 records, investigate ProQuest parsing before acceptance.

---

### 32.7 Doctoral vs master's policy

Do **not** apply a doctoral-only filter during the P2 refinement test.

Reason:

the purpose of P2 is to isolate the truncation change.

After P2 is accepted, decide the evidence policy separately:

- doctoral dissertations may enter the main dissertation evidence layer;
- master's theses may be retained as a separately labelled grey-literature / discovery layer if they contain unique retrieval experiments;
- master's theses must not be assigned the same reliability level as officially defended PhD/DSc dissertations.

This avoids confounding query refinement with evidence-type filtering.

---

### 32.8 Export decision

Do not export all PQDT records yet.

The first 50 pilot records are sufficient for query evaluation.

Perform the final PQDT bulk export only after:

- P2 decision;
- ACM DL pilot;
- IEEE Xplore pilot;
- ACL Anthology pilot;
- cross-platform protocol freeze.

## 33. PQDT P2 final query decision — 2026-09-16

### 33.1 Controlled refinement result

P1:

- 123 records.

P2:

- 126 records.

Only two truncation replacements were made:

`lemmat*` → `lemmat[*10]`

in both occurrences.

Retention:

- P1 R1: **20/20 retained**
- P1 R2: **15/15 retained**
- records lost: **0**
- records added: **3**

The three added records were screened:

- one R1;
- one R2;
- one X.

Therefore the truncation correction improved lexical coverage without observed loss.

### 33.2 Final decision

**USE P2 as the working PQDT Global search query.**

This closes the PQDT query-refinement stage.

### 33.3 Working result count

Current PQDT working count:

**126 records**

This is a platform result count, not the final number of unique or eligible dissertations.

### 33.4 Full export

Do not bulk-export all 126 until the cross-platform protocol is frozen.

The pilot exports and retention logs are sufficient for query validation.

### 33.5 Evidence-type policy remains separate

P2 intentionally retained both doctoral and master's records during query refinement.

Final evidence handling must distinguish:

- defended doctoral dissertations / PhD / DSc;
- master's theses;
- other dissertation/thesis records.

Do not assign the same evidence reliability to all degree types.

### 33.6 Next source

Proceed to an **ACM Digital Library pilot**.

Use the ACM Full-Text Collection rather than the broader Guide to Computing Literature for the primary ACM-source search. The purpose is to capture ACM-published journals/proceedings (e.g. SIGIR/TALLIP and related ACM venues) without importing a second bibliographic index of external publishers into the ACM search layer.
