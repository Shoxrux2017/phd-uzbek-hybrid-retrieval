# BENCHMARK_QRELS_PROTOCOL_v0.1

**Project:** PhD — Uzbek Hybrid Information Retrieval  
**Topic:** «Гибридный подход к поиску информации на узбекском языке на основе интеграции лексических и семантических методов»  
**Protocol version:** v0.1  
**Date:** 2026-09-15  
**Status:** WORKING / PROVISIONAL — protocol design before benchmark construction and controlled pilot  
**Research gap:** `v0.8 refined` — unchanged / provisional  
**RQ/H basis:** `research/OPEN_QUESTIONS.md`, working RQ/H v0.2  
**Decision basis:** `decisions/DECISIONS.md`, especially D-017–D-022  

---

## 0. Purpose and protocol role

This document defines the benchmark, relevance-judgment (`qrels`) and evaluation protocol required to test the current working research chain:

`morphological representation change`  
→ `lexical relevant-set change`  
→ `change in complementarity vs the SAME fixed dense retriever D`  
→ `change in incremental hybrid gain`  
→ `relation to interpretable Uzbek query characteristics`.

The protocol is designed to make the current research gap **falsifiable**. It must permit all of the following outcomes:

- morphology materially changes lexical retrieval and lexical–dense complementarity;
- morphology changes lexical relevant sets but does not materially change hybrid gain;
- morphology changes aggregate effectiveness but not the identity/composition of relevant hits;
- morphology produces weak, unstable or practically negligible changes;
- query features do not reliably explain the observed changes.

None of the following is assumed in advance:

- `lemma > stem > raw`;
- `hybrid > best standalone`;
- `dense > BM25`;
- morphology necessarily changes complementarity;
- query characteristics necessarily predict a useful morphology-induced effect.

This protocol is **not** a proposal for a new retrieval architecture. Its purpose is to obtain evidence before any method/novelty claim is made.

---

# 1. Scientific questions covered by the benchmark

## 1.1 RQ1 / H1

The benchmark must support a controlled comparison of:

- `BM25_raw`;
- `BM25_stem`;
- `BM25_lemma`.

The same corpus, query set, BM25 implementation and non-morphological preprocessing must be used.

The benchmark must allow two distinct outcomes to be measured:

1. **retrieval effectiveness**;
2. **composition of the relevant documents retrieved**.

These outcomes must not be conflated. Similar aggregate nDCG/MAP/Recall does not imply that the same relevant documents were found.

---

## 1.2 RQ2 / H2 — central experiment

The benchmark must support the following controlled design:

`L_raw = BM25_raw`  
`L_stem = BM25_stem`  
`L_lemma = BM25_lemma`

with one fixed semantic dense retriever:

`D`

and three corresponding hybrid conditions:

`H_raw = fusion(L_raw, D)`  
`H_stem = fusion(L_stem, D)`  
`H_lemma = fusion(L_lemma, D)`.

The following must remain fixed across `raw/stem/lemma`:

- dense model `D`;
- dense checkpoint;
- dense retrieval mode;
- dense input preprocessing;
- fusion formula;
- score normalization;
- one global `alpha`;
- candidate depth;
- BM25 implementation and parameters;
- all non-morphological preprocessing.

RQ2 must distinguish:

### H2a — candidate/relevant-set complementarity

Does changing lexical morphology change:

- lexical-only relevant hits;
- dense-only relevant hits;
- relevant-set intersection;
- relevant-set overlap;
- identity of uniquely contributed relevant documents;
- oracle union / candidate-set headroom?

### H2b — incremental hybrid gain

Does the morphology-induced complementarity change translate into a reproducible change in the additional effectiveness of hybrid retrieval?

H2a and H2b are evaluated separately.

---

## 1.3 RQ3 / H3

RQ3 is limited to:

> associations between **predefined interpretable Uzbek query characteristics** and the **morphology-induced change in lexical–dense complementarity**.

RQ3 is **not**:

- dynamic `alpha(q)` prediction;
- generic query-adaptive fusion;
- query routing;
- per-query selection of the best retriever;
- a learned strategy-selection problem.

Features for RQ3 must be computed independently of the compared systems' relevance outcomes.

---

# 2. Protocol status: fixed now vs to be frozen before test

## 2.1 Fixed in v0.1

The following are fixed protocol decisions unless a later protocol version explicitly revises them **before test evaluation**:

| Item | v0.1 decision |
|---|---|
| Main task | Uzbek ad-hoc text retrieval |
| Main evaluation unit | One common retrieval-document unit for all systems |
| Query target | 180 total |
| Development queries | 60 |
| Held-out test queries | 120 |
| Primary relevance scale | graded `0 / 1 / 2` |
| Assessors | 2 independent assessors per pooled pair |
| Adjudication | all assessor disagreements |
| Primary ranking metric | `nDCG@10` |
| Primary coverage metric | `Recall@100` |
| Primary set-analysis depth | `k_set = 50` |
| Primary fusion candidate depth | `k_cand = 100` per component |
| Initial pooling depth | `p = 50` per contributor |
| Pool extension | to satisfy judged-coverage gates through top 100 |
| Dense comparator | one retrieval-trained semantic dense retriever selected on dev, then frozen |
| Primary fusion | normalized convex score combination |
| Primary alpha | one global alpha for all three morphology conditions |
| Alpha selection | dev only |
| Secondary fusion robustness | RRF with fixed `η = 60` |
| Test tuning | prohibited |
| Test query labels | held out until experiment/configuration lock |
| Latin↔Cyrillic transliteration | not enabled as part of primary morphology intervention |
| Stop-word removal | off by default in the primary experiment unless a pre-test protocol revision justifies otherwise |

---

## 2.2 Must be frozen before test evaluation

The following cannot be invented before resources are inspected. They must be filled in and frozen in a later protocol revision (v0.2 or an experiment-lock manifest) **before held-out test qrels are used for analysis**:

- exact corpus sources and licenses;
- final corpus snapshot/hash;
- exact Uzbek tokenizer;
- exact Uzbek stemmer implementation/version;
- exact Uzbek lemmatizer implementation/version;
- exact canonical apostrophe normalization mapping;
- exact dense E5 checkpoint;
- optional third dense pilot candidate, if any;
- exact vector-index implementation and search settings;
- exact corpus-size after cleaning;
- exact pool-only diversity retriever;
- final assessor roster;
- final annotation interface;
- random seed for dev/test stratification.

No such item may be selected using held-out test effectiveness.

---

# 3. Corpus design

## 3.1 Scientific requirement

The primary benchmark should not be a single narrow-domain collection if the dissertation intends to make a general claim about Uzbek retrieval.

The target is a **multi-domain Uzbek corpus** large enough that retrieval is non-trivial and lexical/dense systems can return materially different candidate sets.

### Target corpus size

Preferred target:

- approximately **100,000–250,000 retrieval-document units**.

Minimum acceptable for the main benchmark:

- **50,000 retrieval-document units** after cleaning and deduplication.

If fewer than 50,000 usable units are available, the experiment must be labelled **pilot/domain-limited**, and broad conclusions about Uzbek retrieval must be avoided.

### Domain coverage

The corpus should contain at least **three substantively different domains**.

Suitable domain families include, subject to licensing and data quality:

- news/current affairs;
- public/government information;
- educational/reference material;
- science/technology;
- culture/social information;
- legal/public regulations.

No single domain should dominate the final corpus to the point that RQ3 becomes effectively a single-domain analysis. As a design target, no domain should exceed roughly 50% of the retrieval units unless the corpus source constraints require otherwise and the limitation is documented.

---

## 3.2 Corpus inclusion criteria

Each retrieval unit must:

- contain substantial Uzbek text;
- have a stable unique document ID;
- have recoverable source metadata;
- be legally reusable for the intended research;
- be machine-readable;
- not be an exact duplicate of another retained unit;
- not consist primarily of navigation, advertising, boilerplate, code or tables without usable text.

The benchmark must document:

- source;
- acquisition date;
- licensing basis;
- document counts before/after filtering;
- language-identification rule;
- length distribution;
- script distribution;
- duplicate-removal counts;
- domain distribution.

---

## 3.3 Language and script

The corpus may contain:

- Uzbek Latin script;
- Uzbek Cyrillic script;
- limited natural code-mixing.

The primary benchmark must **not silently transliterate all content to one script**, because script/orthographic characteristics are candidate explanatory features for RQ3.

Uniform normalization that is not the experimental morphology intervention is permitted, for example:

- Unicode normalization;
- case normalization;
- canonicalization of Uzbek apostrophe variants.

The exact rules must be identical for `raw/stem/lemma` and frozen before test.

A separate transliteration experiment may later be conducted as a secondary robustness study, but it must not be mixed into the primary morphology intervention.

---

## 3.4 Deduplication

At minimum:

1. exact duplicates must be removed using a content hash;
2. near-duplicate detection must be applied before corpus freeze;
3. duplicate/near-duplicate clusters must be logged.

Near-duplicate handling must be model-independent and completed before query evaluation.

The same semantic content must not appear repeatedly as multiple “relevant documents” merely because it was syndicated or copied.

---

# 4. Retrieval unit

## 4.1 One common unit for all systems

Every lexical, dense and hybrid system must rank the **same retrieval-unit IDs**.

It is prohibited to compare:

- BM25 over full articles

against

- dense retrieval over unrelated passage/chunk IDs

and interpret the difference as lexical vs semantic retrieval.

The unit boundary itself must be system-independent.

---

## 4.2 Long documents

If source documents are longer than can be represented fairly by all candidate dense retrievers, long documents must be segmented **before indexing** using one deterministic model-independent rule.

Preferred procedure:

- preserve natural paragraph/section boundaries;
- combine adjacent paragraphs into bounded retrieval units;
- do not use model-specific semantic chunking;
- do not create overlapping chunks in the primary benchmark unless a later protocol revision justifies it;
- retain the original source-document ID as metadata.

The resulting unit is the benchmark's **retrieval document**.

All systems index and retrieve exactly this same text unit.

The final segmentation rule and length statistics must be frozen before test.

---

# 5. Query/topic design

## 5.1 Target size

Primary target:

- **180 independent information needs**.

Split:

- **60 development topics**;
- **120 held-out test topics**.

The test set of 120 is chosen to provide a reasonable number of paired query-level observations for morphology comparisons and enough observations for a limited pre-specified RQ3 feature analysis.

A reduction below 180 topics requires an explicit protocol revision.

If the held-out test set falls below 100 valid topics after quality filtering, RQ3 should be treated as exploratory unless a separate power analysis justifies otherwise.

---

## 5.2 Information need vs query string

Each topic must contain:

- `topic_id`;
- short query string used by retrieval systems;
- a fuller information-need description;
- an annotation narrative defining what should count as relevant;
- domain label;
- query-construction provenance;
- predefined query-feature fields.

The retrieval systems receive only the short query field.

The narrative is for assessors and audit only.

---

## 5.3 Preferred query sources

Priority order:

1. privacy-safe real or naturally occurring Uzbek information needs/query logs, if legally available;
2. queries written by native/fluent Uzbek speakers from independently defined information needs;
3. carefully human-validated synthetic assistance only if the first two sources are insufficient.

The held-out test set must not consist primarily of automatically generated LLM queries.

If an LLM is used to assist query creation:

- the final query must be reviewed/revised by a human Uzbek speaker;
- the query must be natural as a search query;
- the model must not be shown the retrieval results;
- the model must not be used as the final relevance assessor;
- the provenance must be recorded.

---

## 5.4 Query leakage prevention

When manually constructing a query, the author should not copy a distinctive phrase from a known target document.

Before corpus retrieval experiments, run a leakage audit for unusually long exact query–document phrase overlap.

A high overlap is not automatically invalid, but suspicious known-item queries should be manually reviewed.

Query creation must occur before inspecting system-specific retrieval success/failure for that query.

---

# 6. Query-feature design for RQ3

RQ3 features must be computed or annotated **without using retrieval effectiveness or qrels-derived outcomes**.

## 6.1 Primary predefined features

The primary confirmatory feature set should remain small.

### F1. Morphological transformation ratio

For a morphology transition `a → b`:

`MorphChangeRatio(q,a,b)`

= proportion of eligible query tokens whose lexical representation changes between the two conditions.

Examples:

- raw → stem;
- raw → lemma;
- stem → lemma.

This is contrast-specific and is expected to be the most direct morphology feature.

### F2. Morphological complexity proxy

A pre-defined query-level measure such as:

- average detected affix count;
- suffix-chain length;
- another analyzer-derived morphology proxy.

The exact implementation must be frozen before test and may not use retrieval outcomes.

### F3. Query length

Number of query tokens after the common non-morphological tokenizer.

### F4. Rare-term ratio

Proportion of query terms whose document-frequency proportion in the frozen corpus is:

`df / N ≤ 0.001`

unless a pre-test calibration justifies a revised fixed threshold.

### F5. Entity / identifier feature

Predefined count or flag for:

- named entities;
- numbers;
- alphanumeric identifiers;
- exact titles/names.

This feature may be produced by manual query annotation if Uzbek NER reliability is insufficient.

### F6. Script / orthographic variation

Predefined indicators such as:

- presence of Cyrillic;
- mixed Latin/Cyrillic;
- non-canonical apostrophe variant in the original query;
- orthographic variant requiring canonicalization.

---

## 6.2 Adjustment / exploratory features

The following may be recorded but must not silently become confirmatory after results are seen:

- domain;
- paraphrastic/descriptive query style;
- code-mixing;
- mean IDF;
- query ambiguity;
- additional linguistic labels.

The confirmatory feature list must be frozen before held-out test analysis.

---

## 6.3 Query-group analysis

If categorical high/medium/low groups are needed, cut points must be determined on development data or by fixed linguistic rules and then applied unchanged to test.

Do not create test groups after observing test retrieval outcomes.

---

# 7. Dev/test split

## 7.1 Split timing

The query split must be performed before:

- dense model selection;
- BM25 parameter selection;
- alpha tuning;
- final query-feature association analysis.

The split must be stratified to preserve reasonable coverage of:

- domains;
- query lengths;
- morphology-sensitive queries;
- script/orthographic variation;
- entity/rare-term queries.

The random seed must be recorded.

---

## 7.2 Development set uses

The 60 dev topics may be used for:

- dense candidate validation;
- one shared BM25 parameter selection;
- global alpha selection;
- normalization sanity checks;
- assessor calibration;
- defining feature-group cut points;
- feasibility/error analysis.

---

## 7.3 Test set prohibition

The 120 test topics may not be used to:

- choose `D`;
- choose BM25 `k1/b`;
- choose stemmer or lemmatizer;
- tune alpha;
- choose candidate depth;
- choose RRF `η`;
- select RQ3 features;
- modify relevance criteria;
- decide which metrics to report as primary.

---

# 8. Common text preprocessing

## 8.1 Common operations

The following must be identical across the three lexical conditions:

- tokenization;
- case folding;
- Unicode normalization;
- apostrophe normalization;
- punctuation policy;
- number/identifier policy;
- script/transliteration policy;
- stop-word policy.

Only the morphological representation changes.

---

## 8.2 Primary stop-word rule

Primary experiment:

**no stop-word removal**.

Reason:

- it avoids adding another language-specific intervention to the causal comparison;
- historical Turkic evidence does not justify assuming stop-word removal will improve ranking;
- any later stop-word experiment can be performed separately.

If resource constraints or the selected engine require a stop-list, this protocol must be revised before test and the exact list must be identical across raw/stem/lemma.

---

## 8.3 Script normalization

Primary experiment:

- canonical Unicode/apostrophe normalization: **enabled uniformly**;
- Latin↔Cyrillic transliteration: **disabled**.

A secondary transliteration sensitivity study may be defined later.

---

# 9. Morphological conditions

## 9.1 Raw

`raw` uses the common preprocessing only.

No stemming or lemmatization is applied.

---

## 9.2 Stem

`stem` applies the frozen Uzbek stemmer to eligible query/document tokens.

The same stemmer version and rules are used for indexing and querying.

---

## 9.3 Lemma

`lemma` applies the frozen Uzbek lemmatizer to eligible query/document tokens.

The same model/rules/resources are used for indexing and querying.

---

## 9.4 Failure behavior

Morphological analyzer failures must not be manually repaired after qrels/results are known.

Default failure policy:

- if the selected stemmer/lemmatizer cannot transform a token, retain the common-preprocessed original token;
- log transformation coverage and failure rates.

Do not silently use a different fallback morphology method in one condition unless this is explicitly part of the frozen algorithm.

---

## 9.5 Morphology audit

Before test analysis, report for queries and corpus:

- percentage of tokens changed by stemming;
- percentage changed by lemmatization;
- analyzer failure rate;
- ambiguous lemma rate if available;
- average vocabulary reduction;
- script-specific failure rates.

These are preprocessing diagnostics, not IR effectiveness results.

---

# 10. BM25 protocol

## 10.1 One implementation

Use one BM25 implementation for all three conditions.

Record:

- library/engine and version;
- exact BM25 formula/variant;
- `k1`;
- `b`;
- field handling;
- tie-breaking.

No BM25 variant may be changed across raw/stem/lemma.

---

## 10.2 Shared `k1/b` selection

If tuning is performed, select **one shared pair** on dev.

Recommended grid:

`k1 ∈ {0.6, 0.9, 1.2, 1.5}`

`b ∈ {0.3, 0.5, 0.75}`.

Selection objective:

1. maximize the macro-average dev `nDCG@10` across `BM25_raw`, `BM25_stem`, `BM25_lemma`;
2. tie-break by macro-average `Recall@100`;
3. if still tied, choose the candidate closest to the conventional pair `(1.2, 0.75)`.

The chosen pair is then frozen for all test runs.

Do not tune separate `k1/b` values for raw, stem and lemma in the primary causal experiment.

---

# 11. Dense-retriever pilot and selection gate

## 11.1 Candidate requirement

A candidate `D` must be:

- retrieval-trained;
- multilingual;
- usable as a semantic dense first-stage retriever;
- capable of Uzbek input;
- reproducible with a fixed checkpoint and scoring rule.

High STS performance, general embedding popularity or English/BEIR results alone are insufficient.

---

## 11.2 Initial candidate families

At minimum, pilot:

1. **BGE-M3 Dense-only mode**;
2. **multilingual E5 retrieval-trained model**.

An optional third candidate may be added only before dev evaluation and with written justification.

**BGE-M3 All must not be the primary causal comparator**, because it mixes dense, sparse and/or multi-vector signals.

It may be used as a **pool-only diversity system**.

---

## 11.3 Dense input protocol

For each dense candidate, freeze:

- checkpoint;
- query/document prefixes/templates;
- tokenizer;
- max sequence length;
- truncation/segmentation handling;
- embedding pooling;
- vector normalization;
- similarity function;
- index/search implementation;
- ANN parameters, if approximate search is used.

For the primary `D`, prefer L2-normalized embeddings and cosine/dot-product-equivalent scoring when supported by the model.

---

## 11.4 Selection rule

Use only the 60 dev queries.

Primary selection metric:

`mean nDCG@10`.

Tie rule:

- if the absolute dev `nDCG@10` difference between the top two candidates is `< 0.01`, use higher `Recall@100`;
- if still tied, prefer the candidate with lower reproducible inference/index resource cost, provided effectiveness is not materially worse.

Also inspect predefined query strata for catastrophic transfer failure.

The selected model does **not** need to outperform BM25 on every query or in every subgroup.

After selection, freeze exactly one `D`.

No raw/stem/lemma-specific dense retriever is allowed in the primary experiment.

---

# 12. Fusion protocol

## 12.1 Candidate union

For each query and morphology condition:

`U_m(q) = Top100(L_m,q) ∪ Top100(D,q)`.

Primary fusion candidate depth:

`k_cand = 100` from each component.

The union may contain fewer or more than 200 unique documents because rankings can overlap.

For every document in the union, compute **both** the lexical score and dense score.

Do not assign a fake “missing” component score merely because the document was absent from one component's top 100 if its actual score can be computed.

---

## 12.2 Primary normalization

Provisional primary normalization:

**theoretical-minimum / observed-maximum linear normalization**, following the design logic of Bruch, Gai & Ingber.

For component `o`:

`norm_o(q,d) = (s_o(q,d) - lower_o) / (max_q(s_o) - lower_o)`.

Default theoretical lower bounds when the actual score definitions support them:

- BM25: `lower_lex = 0`;
- cosine dense similarity: `lower_dense = -1`.

Degenerate denominator handling:

- if `max_q(s_o) == lower_o`, all normalized scores for that component/query are set to `0`.

If the final dense scoring function does not have the assumed bound, the lower-bound rule must be revised and frozen before test.

---

## 12.3 Primary convex fusion

Define alpha as the **dense weight**:

`S_H(q,d) = alpha * norm_D(q,d) + (1 - alpha) * norm_L(q,d)`.

`0 ≤ alpha ≤ 1`.

Alpha extremes are allowed during dev tuning. The protocol must not force the optimum to be “hybrid”.

---

## 12.4 One global alpha

Alpha grid on dev:

`{0.00, 0.05, 0.10, ..., 1.00}`.

For every alpha, evaluate:

- `H_raw`;
- `H_stem`;
- `H_lemma`.

Choose the alpha that maximizes the **macro-average dev nDCG@10 across the three morphology conditions**.

This makes alpha selection morphology-neutral for the main causal comparison.

Tie rule:

1. higher macro-average `Recall@100`;
2. if still tied, choose alpha closest to `0.50`;
3. if still tied, choose the smaller alpha.

Freeze this single alpha for all test conditions.

---

## 12.5 Secondary RRF baseline

Secondary robustness fusion:

`RRF(d) = 1 / (60 + rank_L(d)) + 1 / (60 + rank_D(d))`.

Use:

`η = 60`

and the same component candidate depth `k_cand = 100`.

RRF is a robustness baseline, not novelty.

Optional tuned/asymmetric RRF may be studied later, but must be clearly separated from the primary causal experiment.

---

## 12.6 Secondary morphology-specific alpha

Independent:

- `alpha_raw`;
- `alpha_stem`;
- `alpha_lemma`

may be tuned only in a later **secondary practical experiment**.

Those results cannot be used as the primary evidence for morphology-induced causal change because both morphology and fusion weight change simultaneously.

---

# 13. Pooling protocol

## 13.1 Why deep multi-system pooling is required

The central claims depend on:

- unique relevant hits;
- overlap;
- oracle union;
- Recall;
- candidate-set headroom.

A shallow top-10 pool is insufficient for these analyses.

The protocol therefore uses staged pooling.

---

## 13.2 Development pool

Before selecting `D`, dev pooling must include:

- `BM25_raw`;
- `BM25_stem`;
- `BM25_lemma`;
- every dense pilot candidate;
- at least one additional diversity run if feasible.

Initial depth:

`top 50` per contributing run.

The dev qrels are then used for dense-model and parameter selection.

---

## 13.3 Test initial pool

After `D`, BM25 parameters and global alpha are frozen using dev, the initial test pool must include at least:

### Core evaluated runs

- `BM25_raw`;
- `BM25_stem`;
- `BM25_lemma`;
- fixed `D`;
- `H_raw`;
- `H_stem`;
- `H_lemma`.

### Secondary robustness runs

- `RRF_raw`;
- `RRF_stem`;
- `RRF_lemma`.

### Diversity runs

At least one:

- runner-up dense pilot model; and/or
- BGE-M3 All / sparse / multi-vector mode as **pool-only diversity evidence**; and/or
- another justified heterogeneous retriever.

Pool-only systems do not become primary experimental comparators.

Initial pooling depth:

`p = 50` per contributing run.

Duplicate document IDs are removed before assessment.

---

## 13.4 Residual pool extension

After initial judgments, compute judged coverage for each **primary core run**.

Required minimum judged coverage:

- top 10: **100%**;
- top 50: **≥98%**;
- top 100: **≥95%**.

If any core run fails a gate, add the unjudged documents needed from its top 100 to a residual pool and judge them.

Repeat until the gates are satisfied or a documented resource stop is triggered.

If the top-50 judged-coverage gate cannot be reached, confirmatory set-based analysis at `k_set=50` is not permitted for the affected query/run.

---

## 13.5 Pool blindness

Assessors must not see:

- contributing system name;
- score;
- rank;
- whether a document came from lexical/dense/hybrid retrieval.

Documents within each query pool must be randomized in the annotation interface.

---

# 14. Relevance judgments

## 14.1 Relevance scale

Use three graded relevance levels:

### Grade 2 — highly relevant

The retrieval document directly and substantially satisfies the information need.

### Grade 1 — partially relevant

The document is clearly on-topic and provides useful information, but is incomplete, indirect or only partially satisfies the information need.

### Grade 0 — not relevant

The document does not meaningfully satisfy the information need.

Optional annotation-state code:

`U` / unjudgeable

for corrupted, inaccessible or genuinely impossible-to-assess cases.

`U` must not be silently mapped to 0.

---

## 14.2 Binary relevance threshold for set analysis

Primary binary relevant definition:

`grade >= 1`.

This threshold is used for:

- relevant-set composition;
- lexical-only hits;
- dense-only hits;
- intersection;
- overlap;
- oracle union;
- Recall;
- MAP/binary analyses.

Robustness analysis:

`grade == 2`

may be used as a stricter relevance threshold.

The strict analysis is secondary and must not replace the primary threshold post hoc.

---

## 14.3 Assessor requirements

Each pooled query-document pair is independently judged by:

**two assessors**.

Assessors should be:

- native or near-native fluent Uzbek speakers;
- trained using the same written guideline;
- able to understand the benchmark domains represented in their assignment.

Domain specialists may be needed for technical/legal topics.

---

## 14.4 Calibration

Before full annotation:

1. select approximately 10 dev topics covering multiple domains/query types;
2. both assessors judge the same pools;
3. discuss the rubric only after independent judgments are completed;
4. revise ambiguous instructions;
5. repeat calibration if needed.

Suggested readiness targets:

- weighted Cohen's kappa approximately `>= 0.65`;
- binary relevant/non-relevant agreement approximately `>= 85%`.

These are quality gates, not claims that lower agreement automatically invalidates all data. If not reached, the rubric and training must be reviewed before scaling annotation.

---

## 14.5 Inter-annotator agreement

Report before adjudication:

- weighted Cohen's kappa for the graded 0/1/2 labels;
- binary agreement for `0` vs `>=1`;
- Krippendorff's alpha if the annotation structure or missing labels makes it preferable;
- 95% uncertainty interval where practical.

Do not report only the adjudicated agreement.

---

## 14.6 Adjudication

All disagreements must be adjudicated.

Preferred procedure:

- third experienced Uzbek assessor/adjudicator;
- adjudicator sees the query, narrative and document;
- adjudicator does not see system identity/score/rank;
- original two labels may be shown only after an independent adjudicator reading if the annotation interface supports it.

Final qrels contain the adjudicated grade.

The project must retain the two original labels separately for reliability analysis.

---

## 14.7 Annotation consistency checks

Recommended:

- silently repeat approximately 5% of judged pairs to estimate intra-annotator consistency;
- audit extremely fast annotation sessions;
- record assessor confidence optionally;
- perform manual review of repeated systematic disagreements by topic/domain.

These checks must not be used to change relevance definitions after test outcomes are known.

---

# 15. Qrels representation and provenance

## 15.1 TREC-style qrels

Primary export:

`topic_id  0  doc_id  relevance_grade`

where `relevance_grade ∈ {0,1,2}`.

Unjudgeable items are stored separately or represented by a documented non-evaluation code.

---

## 15.2 Required audit table

Maintain an additional structured file with:

- `topic_id`;
- `doc_id`;
- assessor 1 label;
- assessor 2 label;
- adjudicated label;
- assessor IDs/pseudonyms;
- adjudication flag;
- timestamp/version;
- optional confidence;
- annotation notes;
- pool provenance hidden from assessors but retained for research audit.

---

# 16. Evaluation depths and metrics

## 16.1 Primary ranking metric

**`nDCG@10`**

Use graded labels.

Recommended gain mapping:

`gain(rel) = 2^rel - 1`

therefore:

- grade 0 → 0;
- grade 1 → 1;
- grade 2 → 3.

This makes grade 2 more valuable without treating grade 1 as irrelevant.

---

## 16.2 Primary coverage metric

**`Recall@100`**

using binary relevance `grade >= 1`.

Because qrels are pooled and not exhaustive, this is pooled-qrels Recall and must be interpreted together with judgment-coverage statistics.

---

## 16.3 Secondary ranking metrics

Report at least:

- `nDCG@5`;
- `nDCG@10`;
- `MAP@100`;
- `MRR@10`;
- `Recall@10`;
- `Recall@50`;
- `Recall@100`.

If incomplete judgments remain substantial, report **bpref** as an additional robustness metric.

Do not promote a secondary metric to primary because it produces a more favorable result.

---

# 17. Set-based measurements

For query `q`, morphology condition `m` and set-analysis depth:

`k = k_set = 50`.

Let:

`Top_m(q)` = top-50 result IDs of `L_m`;

`Top_D(q)` = top-50 result IDs of fixed `D`;

`Rel(q)` = adjudicated qrels with grade `>=1`.

Define:

`J_m(q) = Top_m(q) ∩ Rel(q)`

`J_D(q) = Top_D(q) ∩ Rel(q)`.

---

## 17.1 RQ1 — lexical relevant-set change

For lexical variants `a` and `b`:

### Unique relevant hits

`Unique_a|b = |J_a \ J_b|`

`Unique_b|a = |J_b \ J_a|`.

### Intersection

`Intersection_ab = |J_a ∩ J_b|`.

### Jaccard overlap

If `|J_a ∪ J_b| > 0`:

`Jaccard_ab = |J_a ∩ J_b| / |J_a ∪ J_b|`.

If both sets are empty, Jaccard is reported as `NA` rather than interpreted as perfect successful agreement.

### Normalized symmetric set change

Primary RQ1 composition quantity:

`LexSetChange_ab = |J_a Δ J_b| / max(1, |J_a ∪ J_b|)`.

Range:

`0 ... 1`.

- `0` = no composition change;
- `1` = completely non-overlapping retrieved relevant sets, or one non-empty relevant set vs one empty set.

Required contrasts:

- raw ↔ stem;
- raw ↔ lemma;
- stem ↔ lemma.

---

# 18. RQ2 — lexical–dense complementarity measurements

For morphology condition `m`:

## 18.1 Lexical-only relevant set

`LexOnly_m(q) = J_m(q) \ J_D(q)`.

Count:

`|LexOnly_m(q)|`.

---

## 18.2 Dense-only relevant set

`DenseOnly_m(q) = J_D(q) \ J_m(q)`.

Count:

`|DenseOnly_m(q)|`.

Although `J_D` itself is fixed, `DenseOnly_m` can change because the lexical set changes.

---

## 18.3 Relevant intersection

`Intersection_m(q) = J_m(q) ∩ J_D(q)`.

---

## 18.4 Relevant-set overlap

If the union is non-empty:

`Overlap_m(q) = |J_m ∩ J_D| / |J_m ∪ J_D|`.

Otherwise report `NA`.

---

## 18.5 Oracle union

`OracleUnion_m(q) = J_m(q) ∪ J_D(q)`.

Oracle-union recall:

`OracleUnionRecall_m@50 = |OracleUnion_m(q)| / |Rel(q)|`.

This is a candidate-set upper-bound diagnostic.

It is **not** a fused ranking and **not** per-query best alpha.

---

## 18.6 Candidate-set complementarity headroom

`Headroom_m@50 = OracleUnionRecall_m@50 - max(Recall@50(L_m), Recall@50(D))`.

This estimates how much relevant coverage exists in the union beyond the better individual component at the same depth.

It does not measure whether the fusion function actually ranks that evidence well.

---

## 18.7 Morphology-induced complementarity set shift

For two morphology conditions `a` and `b`, define the lexical-only sets against the same fixed `D`:

`C_a = LexOnly_a(q)`

`C_b = LexOnly_b(q)`.

Primary H2a set-change quantity:

`ComplementaritySetShift_ab = |C_a Δ C_b| / max(1, |C_a ∪ C_b|)`.

Required contrasts:

- raw ↔ stem;
- raw ↔ lemma;
- stem ↔ lemma.

Supporting H2a diagnostics:

- change in `|LexOnly|`;
- change in `|DenseOnly|`;
- change in `Overlap`;
- change in `OracleUnionRecall`;
- change in `Headroom`.

---

# 19. Incremental hybrid gain

Let `E(s,q)` denote per-query `nDCG@10` unless otherwise specified.

## 19.1 Gain over corresponding lexical system

Primary H2b quantity:

`G_lex(m,q) = E(H_m,q) - E(L_m,q)`.

This answers:

> how much does adding the fixed semantic retriever `D` improve or harm the corresponding lexical condition?

H2b examines whether `G_lex` changes between raw/stem/lemma.

For contrast `a → b`:

`ΔG_lex(a,b,q) = G_lex(b,q) - G_lex(a,q)`.

---

## 19.2 Gain over dense system

Secondary:

`G_dense(m,q) = E(H_m,q) - E(D,q)`.

---

## 19.3 Gain over best standalone system

To avoid turning the test set into a per-query strategy oracle, define the practical standalone comparator on **dev**, not from per-query test relevance.

For each morphology condition `m`, on dev:

`B_m ∈ {L_m, D}`

is the standalone system with higher mean dev `nDCG@10`.

Freeze `B_m`.

Then on test:

`G_best(m,q) = E(H_m,q) - E(B_m,q)`.

This is the primary “best standalone” comparison.

A per-query test oracle:

`max(E(L_m,q), E(D,q))`

may be reported only as a clearly labelled diagnostic and must not be described as a deployable baseline or as the primary H2b comparator.

---

# 20. Practical-effect thresholds / SESOI

These thresholds are **provisional v0.1 defaults**. They must be reviewed on dev/annotation-calibration evidence and then frozen in a protocol revision **before held-out test analysis**. They may not be changed after seeing test effects.

## 20.1 Ranking effectiveness

For mean paired changes in `nDCG@10`:

- practically negligible band: approximately `[-0.02, +0.02]`;
- an absolute mean difference of `>= 0.02` is the default minimum practically meaningful effect.

For `Recall@100` / oracle-union recall:

- default practical band: approximately `[-0.03, +0.03]`.

---

## 20.2 Relevant-set composition

For normalized set-change quantities such as:

- `LexSetChange`;
- `ComplementaritySetShift`;

provisional interpretation:

- `<= 0.05`: small/negligible set change;
- `>= 0.10`: practically meaningful set change;
- `0.05–0.10`: indeterminate/intermediate zone requiring uncertainty analysis.

These are not p-values.

The final frozen thresholds must be version-controlled before test evaluation.

---

# 21. Statistical analysis

## 21.1 Unit of analysis

Primary inferential unit:

**query**.

All primary raw/stem/lemma comparisons are paired because the same query is evaluated under every condition.

---

## 21.2 Pairwise morphology contrasts

Required contrasts:

1. raw vs stem;
2. raw vs lemma;
3. stem vs lemma.

For signed effectiveness outcomes such as `nDCG@10`, `Recall@100`, `ΔG_lex`:

- use a paired randomization/permutation test;
- two-sided unless a later hypothesis explicitly becomes directional before test;
- use at least 10,000 permutations when computationally feasible;
- report paired effect estimate and 95% bootstrap confidence interval.

Correct the three morphology pairwise comparisons using **Holm correction** within each primary outcome family.

---

## 21.3 Equivalence / practically negligible effect

`p > 0.05` does not establish no effect.

When testing H0-style practical equivalence, use:

- equivalence testing / TOST where appropriate; and/or
- confidence-interval inclusion within the pre-frozen SESOI band.

Evidence for negligible effect requires the uncertainty interval to support the equivalence claim, not merely a non-significant superiority test.

---

## 21.4 H1 decision logic

Primary composition outcome:

`LexSetChange@50`.

For each morphology pair, report:

- mean/median set change;
- bootstrap 95% CI;
- raw unique-hit counts;
- percentage of queries with non-zero change.

H1 receives meaningful support only if at least one pre-specified contrast exceeds the frozen practical threshold with uncertainty inconsistent with the negligible range.

If the effect is small or uncertainty spans both negligible and meaningful regions:

**insufficient evidence**.

---

## 21.5 H2a decision logic

Primary:

`ComplementaritySetShift@50`.

Supporting outcomes:

- `LexOnly`;
- `DenseOnly`;
- `Overlap`;
- `OracleUnionRecall`;
- `Headroom`.

H2a is not established merely because BM25 effectiveness changed.

Evidence must show a practically meaningful, reproducible change in the lexical contribution relative to the same fixed `D`.

Convincing evidence that all key H2a changes fall inside the pre-frozen negligible range weakens the central basis of `v0.8 refined` and triggers research-gap review.

---

## 21.6 H2b decision logic

Primary:

change in `G_lex` based on `nDCG@10`.

Supporting:

- `G_best`;
- `G_dense`;
- Recall-based gain.

Interpretation:

- H2a supported + H2b supported → full working chain receives support;
- H2a supported + H2b negligible → complementarity changes, but the fixed fusion does not translate this into a practically meaningful hybrid-gain change;
- H2a negligible → central v0.8 premise is weakened even if some ranking differences appear elsewhere;
- insufficient evidence → no positive or null conclusion.

---

# 22. RQ3 statistical protocol

## 22.1 Confirmatory feature set

Limit the primary RQ3 feature set to the six predefined families in Section 6.

Do not add new confirmatory features after inspecting test outcomes.

---

## 22.2 Primary association analysis

For each pre-specified morphology contrast, examine associations between query features and:

1. morphology-induced complementarity change;
2. `ΔG_lex`.

Primary simple association:

**Spearman rank correlation** for continuous/ordinal features.

For binary/categorical features, use the corresponding pre-specified two-group or regression contrast.

Control multiple RQ3 tests using **Benjamini–Hochberg FDR at q = 0.05** within the RQ3 family.

A candidate relationship should not be described as substantively supported solely because `q < 0.05`.

Default practical association requirement:

`|Spearman rho| >= 0.20`

plus a bootstrap confidence interval that does not indicate an unstable sign.

---

## 22.3 Multivariable robustness analysis

Secondary RQ3 analysis:

- standardized multivariable regression;
- include morphology-transition indicator;
- include the frozen primary query features;
- cluster uncertainty by query if multiple transition observations per query are modeled jointly.

The purpose is to test whether a simple univariate association survives adjustment for correlated query characteristics.

Avoid high-dimensional feature selection or learned routing in this phase.

---

# 23. Incomplete judgments and qrels bias

## 23.1 Unjudged is not non-relevant evidence

For scientific interpretation:

> an unjudged document is not proven irrelevant.

The evaluation scripts may need conventional assumptions for some metrics, but the dissertation must report judged coverage and pooling limitations.

---

## 23.2 Judgment coverage reporting

For every evaluated run report:

- judged@10;
- judged@50;
- judged@100;
- unjudged counts.

Set-based conclusions at `k=50` require the coverage gate in Section 13.

---

## 23.3 Robustness to incomplete qrels

If incomplete judgments remain non-trivial:

- report `bpref`;
- repeat key set analyses on the subset of queries/runs satisfying strict judged-coverage thresholds;
- perform a leave-one-pool-contributor sensitivity analysis if feasible.

Do not make a strong oracle-union claim from a shallow pool.

---

# 24. Leakage controls and experiment lock

## 24.1 Before test qrels are opened for analysis

Freeze an experiment manifest containing:

- corpus snapshot/hash;
- query split and hash;
- tokenizer/preprocessing versions;
- raw/stem/lemma algorithms;
- BM25 implementation and parameters;
- selected `D` checkpoint and dense settings;
- alpha;
- normalization formula;
- `k_set`;
- `k_cand`;
- RRF parameter;
- primary metrics;
- primary statistical tests;
- RQ3 feature list;
- SESOI/equivalence thresholds;
- software/container environment;
- random seeds.

Suggested file later:

`experiments/EXPERIMENT_LOCK_v0.1.json`

or equivalent.

Creating that file is **not** part of this protocol-writing task.

---

## 24.2 Test access rule

After the experiment lock:

- test qrels may be opened/evaluated;
- no configuration may be changed in response to test performance.

If a bug invalidates a configuration:

1. document the bug;
2. fix it;
3. version the protocol/experiment lock;
4. rerun all affected conditions consistently;
5. do not selectively rerun only unfavorable systems.

---

## 24.3 Query-feature leakage

RQ3 features may use:

- raw query text;
- morphology analyzer output;
- frozen corpus statistics;
- pre-retrieval manual query labels.

They may not use:

- system rank;
- nDCG/Recall;
- qrels-derived relevance overlap;
- best alpha;
- system winner identity

as input explanatory features in the confirmatory RQ3 analysis.

---

# 25. Reproducibility requirements

Record at minimum:

- OS/container;
- Python/runtime versions;
- retrieval engine versions;
- BM25 implementation;
- morphology resource versions/hashes;
- dense checkpoint names and hashes;
- tokenizer versions;
- indexing commands/configs;
- corpus hash;
- query hash;
- qrels hash;
- all random seeds;
- ANN parameters;
- hardware used for dense indexing/retrieval;
- run time and index size;
- exact evaluation script version.

Every run must have a stable run ID.

Suggested naming:

- `L_RAW`;
- `L_STEM`;
- `L_LEMMA`;
- `D_FIXED`;
- `H_RAW_CC`;
- `H_STEM_CC`;
- `H_LEMMA_CC`;
- `H_RAW_RRF`;
- `H_STEM_RRF`;
- `H_LEMMA_RRF`.

---

# 26. Required benchmark artifacts

Before the main experiment, the project should eventually contain or generate:

1. corpus manifest;
2. corpus snapshot/hash record;
3. document metadata table;
4. query/topic file;
5. query-feature file;
6. dev/test split file;
7. assessor guideline;
8. raw assessor judgments;
9. adjudication record;
10. final qrels;
11. pooling manifest;
12. dense-pilot results;
13. frozen experiment manifest;
14. run files in TREC-compatible or equivalent format;
15. evaluation tables;
16. statistical-test output;
17. per-query analysis table.

These are future outputs; this v0.1 protocol does not create them.

---

# 27. Benchmark validity gates

The benchmark is ready for the main held-out experiment only if all of the following are satisfied.

## Gate A — corpus

- at least 50,000 cleaned retrieval units for a general benchmark;
- at least three substantive domains, unless explicitly labelled domain-limited;
- corpus frozen and hashed;
- duplicates/near-duplicates addressed.

## Gate B — query set

- target 180 usable information needs;
- 60 dev / 120 test;
- feature/domain coverage audited;
- query construction provenance recorded.

## Gate C — qrels

- two independent assessors per pooled pair;
- disagreement adjudication complete;
- agreement reported;
- top-50 judged-coverage gate satisfied for primary runs.

## Gate D — dense comparator

- at least BGE-M3 Dense and multilingual E5 compared on dev;
- one `D` selected by the predefined rule;
- `D` frozen before test.

## Gate E — causal controls

The same across morphology conditions:

- BM25 implementation/parameters;
- `D`;
- candidate depth;
- normalization;
- global alpha;
- fusion formula;
- query/document corpus;
- qrels.

## Gate F — experiment lock

All final primary settings and thresholds versioned before held-out test analysis.

If a gate fails, the study must be labelled pilot/partial or the protocol must be revised before confirmatory claims.

---

# 28. Stopping / gap-reassessment rules

The experiment must trigger reassessment of `v0.8 refined` if the held-out evidence convincingly shows that:

- raw/stem/lemma produce only practically negligible lexical relevant-set differences; or
- lexical relevant-set differences exist but complementarity against fixed `D` remains practically negligible across the pre-specified measurements; or
- apparent effects do not reproduce on held-out test queries.

If H2a is supported but H2b is not:

- do **not** claim that morphology-induced complementarity automatically improves hybrid ranking;
- retain the set-level finding if robust;
- narrow/revise the hybrid-gain part of the scientific position.

If H1/H2 are supported but H3 is not:

- do not invent query-adaptive fusion;
- report that the effect exists but is not reliably explained by the predefined query features.

A negative result is a valid outcome.

---

# 29. What this protocol does not establish

Even if the full experiment succeeds, it will not by itself prove:

- universal superiority of lemmatization;
- universal superiority of stemming;
- universal superiority of hybrid retrieval;
- universal superiority of the selected dense retriever;
- transfer to all Uzbek domains;
- causal linguistic mechanisms beyond the controlled intervention and observed associations;
- novelty of normalized fusion, RRF or dynamic weighting.

Any method/novelty proposal must follow the evidence.

---

# 30. Protocol change control

Any substantive modification must create a new version.

Examples requiring version bump:

- changing query count/split;
- changing relevance scale;
- changing `k_set` or `k_cand`;
- changing primary metrics;
- changing morphology algorithms after dev inspection;
- changing `D` after test evaluation;
- changing global alpha using test labels;
- changing SESOI after seeing test effects;
- adding/removing confirmatory RQ3 features after test inspection.

Recommended progression:

`v0.1` — benchmark/qrels design  
`v0.2` — concrete resources/checkpoints/corpus frozen  
`v0.3` — annotation/pooling feasibility corrections, if required  
`EXPERIMENT_LOCK` — final pre-test immutable configuration

After test qrels are opened, any unplanned analysis must be labelled **exploratory**.

---

# 31. Immediate next implementation sequence

After approval of this protocol:

1. identify candidate corpus sources and licenses;
2. decide the exact retrieval-unit segmentation;
3. select/freeze Uzbek tokenizer, stemmer and lemmatizer candidates;
4. define the 180-topic construction procedure and feature quotas;
5. construct the 60-topic dev set first;
6. build dev multi-system pool and qrels;
7. run BGE-M3 Dense vs multilingual E5 pilot;
8. choose/freeze `D`;
9. select one shared BM25 parameter pair;
10. select one global alpha;
11. construct/annotate held-out test pools;
12. create experiment lock;
13. only then run the confirmatory test analysis.

---

# 32. Internal methodological anchors

This protocol is aligned with the current project evidence and decisions:

- [`research/CURRENT_GAP.md`](CURRENT_GAP.md) — current `v0.8 refined`;
- [`research/OPEN_QUESTIONS.md`](OPEN_QUESTIONS.md) — RQ/H v0.2 and measurement logic;
- [`../decisions/DECISIONS.md`](../decisions/DECISIONS.md) — D-017–D-022;
- [`../literature/deep-dives/2008_Can_Information_Retrieval_on_Turkish_Texts.md`](../literature/deep-dives/2008_Can_Information_Retrieval_on_Turkish_Texts.md) — deep pooling / Turkic morphology retrieval precedent and incomplete-qrels lessons;
- [`../literature/deep-dives/2026_Munetsi_Mukande_OConnor_Shona_Morphology_Aware_IR.md`](../literature/deep-dives/2026_Munetsi_Mukande_OConnor_Shona_Morphology_Aware_IR.md) — warning against shallow top-10 pooling and under-specified low-resource annotation;
- [`../literature/deep-dives/2023_Bruch_Gai_Ingber_Fusion_Functions_Hybrid_Retrieval.md`](../literature/deep-dives/2023_Bruch_Gai_Ingber_Fusion_Functions_Hybrid_Retrieval.md) — candidate-union vs fusion-ranking distinction and normalized convex fusion;
- [`../literature/deep-dives/2026_Posokhov_Query_Adaptive_Hybrid_Search.md`](../literature/deep-dives/2026_Posokhov_Query_Adaptive_Hybrid_Search.md) — boundary against generic query-adaptive/dynamic-alpha novelty;
- [`../literature/deep-dives/2024_Kazi_Khoja_UPERF_Urdu_Retrieval.md`](../literature/deep-dives/2024_Kazi_Khoja_UPERF_Urdu_Retrieval.md) — raw/stem/lemma and low-resource morphology/hybrid boundary.

---

# 33. Current protocol verdict

**Benchmark/qrels design is sufficiently specified to begin resource selection and dev-benchmark construction, but not yet to run the held-out confirmatory experiment.**

Before held-out test evaluation, a later frozen revision must fill in the concrete resource fields listed in Section 2.2 and produce an experiment-lock manifest.

The central scientific priority remains:

> test whether changing Uzbek lexical morphology actually changes the unique relevant evidence contributed relative to one fixed semantic dense retriever, and whether that change translates into incremental hybrid gain.

No new retrieval architecture should be proposed before this baseline evidence exists.
