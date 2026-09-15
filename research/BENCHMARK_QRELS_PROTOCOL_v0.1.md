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

## 2.1 Decisions and planning targets in v0.1

The following are protocol decisions unless a later protocol version explicitly revises them **before test-label exposure and experiment lock**. Query counts are planning targets pending Section 5.1 sensitivity analysis; they are not frozen sample-size claims.

| Item | v0.1 decision |
|---|---|
| Main task | Uzbek ad-hoc text retrieval |
| Main evaluation unit | Prefer source documents; any common canonical section units must be declared as such (Section 4) |
| Query target | Planning target: 180 total, pending prospective power/sensitivity analysis |
| Development queries | Planning target: 60 |
| Held-out test queries | Planning target: 120; final N and confirmatory scope require prospective justification |
| Primary relevance scale | graded `0 / 1 / 2` |
| Assessors | 2 independent assessors per pooled pair |
| Adjudication | all assessor disagreements |
| Primary ranking metric | `nDCG@10` |
| Primary coverage metric | `Recall@100` |
| Primary set-analysis depth | `k_set = 50` |
| Primary fusion candidate depth | `k_cand = 100` per component |
| Initial pooling depth | Target `p = 50` per contributor; DEV-1 must cover every tuning candidate's top 10 |
| Pool extension | to satisfy judged-coverage gates through top 100 |
| Dense comparator | one retrieval-trained semantic dense retriever selected on dev, then frozen |
| Primary fusion | normalized convex score combination |
| Primary alpha | one global interior alpha from `{0.05, 0.10, ..., 0.95}` for all three morphology conditions |
| Alpha selection | dev only, after DEV-1–DEV-4 coverage gates; endpoints are standalone references |
| Secondary fusion robustness | RRF with fixed `η = 60` |
| Test tuning | prohibited |
| Test query labels | held out until experiment/configuration lock |
| Latin↔Cyrillic transliteration | not enabled as part of primary morphology intervention |
| Stop-word removal | off by default in the primary experiment unless a pre-test protocol revision justifies otherwise |

---

## 2.2 Must be frozen before test-label exposure

The following require resource inspection or prospective design work. They must be filled in and frozen in a later protocol revision (v0.2 or an experiment-lock manifest) **before the investigator/research-tuning side can access any held-out test relevance labels**, with lock-before-test-annotation as the default:

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
- source-document vs section-level evaluation scope and any segmentation rule;
- final query count/split, prospective power/sensitivity report and confirmatory/exploratory status per hypothesis;
- scientifically justified final SESOI/equivalence margins;
- zero-relevant-topic review trigger and any outcome-independent replacement policy;
- exact pool-only diversity retriever;
- final assessor roster;
- final annotation interface;
- random seed for dev/test stratification.

No such item may be selected using held-out test effectiveness or relevance labels. Primary morphology processors must be frozen independently of comparative dev IR outcomes (Section 9.6).

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

The preferred primary design ranks **source-document-level units** when their lengths permit fair representation across all selected systems. This is the design that directly matches the current document-ranking research claim.

Every lexical, dense and hybrid system must rank the **same retrieval-unit IDs**.

It is prohibited to compare:

- BM25 over full articles

against

- dense retrieval over unrelated passage/chunk IDs

and interpret the difference as lexical vs semantic retrieval.

The unit boundary itself must be system-independent.

---

## 4.2 Long documents

If long source documents cannot be represented fairly across the preregistered candidate systems, they must be segmented **before indexing** using one deterministic model-independent rule, identical for every system. The decision must follow resource/length inspection before DEV-1, not comparative retrieval effectiveness.

Preferred procedure:

- preserve natural paragraph/section boundaries;
- combine adjacent paragraphs into bounded retrieval units;
- do not use model-specific semantic chunking;
- do not create overlapping chunks in the primary benchmark unless a later protocol revision justifies it;
- retain the original source-document ID as metadata.

Each resulting section/passage becomes a **benchmark retrieval unit with a stable unique ID** and a mapping to its original source-document ID.

All systems index and retrieve exactly this same text unit.

The final segmentation rule, ID mapping and length statistics must be frozen before test. Report both original-document counts and retrieval-unit counts, including the proportion of source documents split.

If segmentation is used, evaluation is explicitly **retrieval-unit/section-level evaluation**, including any retained short unsplit units. It is not automatically evidence of full original-document retrieval. In this protocol, subsequent uses of "document", `doc_id` and relevant-document counts refer to the declared benchmark unit.

The dissertation, tables and conclusions must name the actual unit. Do not silently convert the document-ranking claim into passage retrieval. Full original-document claims would require a separately specified aggregation/evaluation design; Section 27 Gate A and Section 29 enforce this reporting boundary.

---

# 5. Query/topic design

## 5.1 Target size

Current **planning target**, pending mandatory prospective power/sensitivity analysis:

- **180 independent information needs**.

Split:

- **60 development topics**;
- **120 held-out test topics**.

The design `180 = 60 dev + 120 test` is retained for planning and annotation estimates. It does **not** establish that 120 held-out queries are scientifically sufficient for any hypothesis.

Before final query-count freeze, complete and archive a **prospective power / sensitivity analysis** for at least:

- paired `nDCG@10` differences across the required morphology contrasts;
- H1 `LexSetChange@50`, including sensitivity to distinguish meaningful from negligible set change;
- H2a `ComplementaritySetShift@50` under the corresponding decision rule;
- H2b paired `ΔG_lex`;
- RQ3 feature associations, including the candidate practical association `|rho| >= 0.20`.

Use a reproducible analytical calculation or simulation appropriate to each planned test/interval and outcome distribution. Predeclare the desired power (planning target: at least 80%), precision and equivalence sensitivity, and evaluate a range of plausible variances, paired correlations, bounded/zero-heavy set outcomes, feature prevalence and annotation reliability. Nuisance estimates may come from independent evidence or dev calibration, with uncertainty/sensitivity ranges; do not substitute favorable observed dev morphology effects for independently justified target effects or SESOI (Section 20).

Account for Holm correction in the primary contrast families, the full RQ3 Benjamini–Hochberg FDR family, dependence between features/contrasts, and loss of usable paired topics through coverage/zero-relevance exclusions. Multiple contrasts from one query do not increase the independent query N. Report assumed effects, nuisance inputs, correction procedure, usable N, detectable effects/interval precision and the resulting decision for each hypothesis.

In particular, **120 test queries may be underpowered for `|rho| = 0.20`, especially after multiple-testing/FDR correction**. The final test N must be justified prospectively. If available N lacks adequate sensitivity for confirmatory H3, label H3 **exploratory before test-label exposure**; a non-significant association must not become evidence of no association. Apply the same sensitivity review to the other confirmatory claims.

Increase N where feasible or narrow/declare the affected analysis exploratory before lock. Any change to the planning count/split requires an explicit pre-test protocol revision. Annotation budget alone cannot establish statistical sufficiency. Record the final N, rationale and claim status in `EXPERIMENT_LOCK`; Section 27 Gate G must pass for each retained confirmatory claim.

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

The dev topics (planning target: 60) may be used for:

- dense candidate validation;
- one shared BM25 parameter selection;
- global alpha selection;
- normalization sanity checks;
- assessor calibration;
- defining feature-group cut points;
- feasibility/error analysis.

Model/parameter/alpha selection must follow the phased coverage requirements in Section 13.2. Dev calibration may inform prospective sensitivity inputs, but comparative morphology effects must not determine favorable SESOI.

---

## 7.3 Test set prohibition

The held-out test topics (planning target: 120, pending prospective justification) may not be used to:

- choose `D`;
- choose BM25 `k1/b`;
- choose stemmer or lemmatizer;
- tune alpha;
- choose candidate depth;
- choose RRF `η`;
- select RQ3 features;
- modify relevance criteria;
- decide which metrics to report as primary.

The investigator/research-tuning side must have no access to test relevance labels before `EXPERIMENT_LOCK`, including informal inspection or assessor feedback revealing relevance (Section 24).

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

## 9.6 Independent processor selection and freeze

Select and freeze the primary stemmer and lemmatizer before comparative IR dev analysis/DEV-1, preferably during resource selection, using independent criteria:

- availability and licensing;
- documented Uzbek linguistic validity;
- reproducibility and versioned resources;
- analyzer-quality evidence from independent linguistic evaluation;
- language/script coverage;
- technical stability.

Archive the selection rationale, implementation/version/hash and fallback policy. Do not search across multiple stemmers/lemmatizers using dev IR effectiveness and present the winner as a neutral `stem` or `lemma` condition. Comparisons of several morphology implementations on IR effectiveness are a separate **secondary experiment**, with the search space and selection reported explicitly.

Any necessary primary processor revision must have an independent documented reason, occur before test-label exposure, and restart affected dev phases under a versioned protocol; it cannot be an opportunity to select a favorable morphology effect.

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

If tuning is performed, select **one shared pair** on dev in DEV-2, only after DEV-1 has judged every participating configuration's top 10 for every comparison topic (Section 13.2).

Recommended grid:

`k1 ∈ {0.6, 0.9, 1.2, 1.5}`

`b ∈ {0.3, 0.5, 0.75}`.

Selection objective:

1. maximize the macro-average dev `nDCG@10` across `BM25_raw`, `BM25_stem`, `BM25_lemma`;
2. use macro-average `Recall@100` only if **all tied configurations across raw/stem/lemma have 100% adjudicated top-100 coverage on every comparison topic**, using the same qrels snapshot and eligible topic set;
3. if that gate is unavailable or Recall remains tied, choose the pair minimizing `(k1 - 1.2)^2 + (b - 0.75)^2`; then smaller `k1`, then smaller `b`.

Freeze numeric score precision/tie tolerance before comparing candidates. The final tie rule is deterministic and does not depend on relevance. Never apply the looser test top-100 coverage gate as permission to use incompletely judged Recall for tuning.

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

Use only the dev queries (planning target: 60), in DEV-2 after every dense candidate satisfies DEV-1 adjudicated top-10 coverage.

Primary selection metric:

`mean nDCG@10`.

Tie rule:

- form the near-tied set of candidates within `< 0.01` of the highest dev `nDCG@10`; this is a selection tolerance, not a SESOI;
- use higher `Recall@100` only if every candidate in that set has **100% adjudicated top-100 coverage on every comparison topic**, with common qrels and eligible topics;
- if the coverage gate fails or Recall remains tied, use a deterministic non-relevance order fixed before dev comparison: lower measured inference cost under a fixed benchmark, then smaller index footprint, then stable checkpoint ID in ascending order.

Also inspect predefined query strata for catastrophic transfer failure.

The selected model does **not** need to outperform BM25 on every query or in every subgroup.

After selection, freeze exactly one `D`.

No raw/stem/lemma-specific dense retriever is allowed in the primary experiment.

---

## 11.5 Dense retrieval implementation fidelity

At the planned corpus scale, prefer **exact vector search** for the primary confirmatory experiment when computationally practical. Exactness here concerns searching the frozen embedding collection, not semantic relevance.

If approximate nearest-neighbor (ANN) retrieval is used:

- freeze index construction, distance function, all build/search parameters, seeds and numerical precision;
- before relying on ANN candidate sets, compare against exact search with the same vectors/scoring on a predefined dev subset or independently sampled queries, selected without relevance outcomes;
- measure per-query `ANNRecall@100 = |Top100_ANN(q) ∩ Top100_exact(q)| / |Top100_exact(q)|` (use the available exact-list length when fewer than 100 exist); report the mean, distribution and worst-case/stratum failures;
- require very high fidelity: the planning acceptance target is mean top-100 ANN recall `>= 0.99`, plus a pre-frozen lower-tail acceptance rule; justify and freeze any alternative threshold and the sample before the fidelity check;
- if fidelity fails, use exact search or revise ANN settings on dev and revalidate before lock; freeze and record the final settings and validation report.

Use deterministic score/ID tie handling in the exact reference and ANN outputs. Apply this control to dense candidates used for selection and to the fixed `D` used for complementarity analysis. Otherwise ANN misses could be mistaken for lexical–dense complementarity. This is **retrieval implementation fidelity, not relevance `Recall@100`**.

---

# 12. Fusion protocol

## 12.1 Candidate union

For each query and morphology condition:

`U_m(q) = Top100(L_m,q) ∪ Top100(D,q)`.

Primary fusion candidate depth:

`k_cand = 100` from each component.

The union contains at most 200 unique documents and may contain fewer because the component rankings overlap (or because fewer than 100 candidates are available).

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

The **primary hybrid** must use `0 < alpha < 1`, selected from the interior grid in Section 12.4. Endpoints are standalone references: `alpha=0` is lexical standalone and `alpha=1` is dense standalone. Evaluate them on dev as sanity/reference points, preserving the standalone rankings with the same deterministic tie rules.

For convex fusion and RRF, rank by descending final score, then ascending stable retrieval-unit ID for exact score ties (fixed bytewise ID ordering, independent of locale). Freeze score precision and use the same rule in candidate generation, component rankings and reruns. Do not break fusion ties by source system, relevance or pool order.

---

## 12.4 One global alpha

Eligible primary hybrid alpha grid on dev:

`{0.05, 0.10, ..., 0.95}`.

For every interior alpha, generate the following runs, then evaluate them only after DEV-4 coverage is met:

- `H_raw`;
- `H_stem`;
- `H_lemma`.

Choose the interior alpha that maximizes the **macro-average dev nDCG@10 across the three morphology conditions**. Every candidate's top 10 must be adjudicated before comparison; use the same qrels snapshot and eligible topics for all candidates.

This makes alpha selection morphology-neutral for the main causal comparison.

Tie rule:

1. higher macro-average `Recall@100` only if every tied hybrid candidate in all three morphology conditions has **100% adjudicated top-100 coverage on every comparison topic**;
2. if that gate fails or Recall remains tied, choose alpha closest to `0.50`;
3. if still tied, choose the smaller alpha.

Freeze this single **interior** alpha for all test conditions.

Also evaluate `alpha=0` and `alpha=1` on dev as standalone sanity/reference points, outside the primary selection grid and on the same comparison topics. If the best endpoint exceeds every interior alpha under the same morphology-neutral macro-average objective, retain the best interior alpha as the predefined primary hybrid control and record explicitly: **dev provides no evidence that score fusion improves over the strongest endpoint**. Report per-morphology endpoint comparisons as well. Do not redefine the hybrid to an endpoint or force a positive result: `G_lex`, `G_best` and H2b's `ΔG_lex` may legitimately be zero or negative on test.

---

## 12.5 Secondary RRF baseline

Secondary robustness fusion:

`RRF(d) = contribution_L(d) + contribution_D(d)`, where `contribution_o(d) = 1 / (60 + rank_o(d))` if `d` occurs in component `o`'s top-100 list, and `0` otherwise.

Ranks are one-based. A missing document contributes zero from that component: do not invent rank 101, retrieve a deeper rank or recompute a rank outside the frozen list. Rank the component union with the deterministic fusion tie rule in Section 12.3.

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

may be tuned only in a later **secondary practical experiment**, with the same coverage safeguards. Any condition called hybrid must use an interior alpha; endpoints remain standalone references.

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

Dev pooling and tuning must follow these phases in order. Register candidate IDs/configurations before scoring, retain a coverage matrix by phase/query/run/depth, and archive each phase's run files and adjudicated qrels snapshot. All candidates within a comparison use the same qrels snapshot and common eligible topics; no candidate-specific topic deletion is allowed.

> parameter/model tuning must never interpret unjudged tuning documents as evidence of non-relevance.

This rule includes alpha and standalone-comparator selection. `U`/unjudgeable is unresolved, not judged coverage or relevance grade 0 (Sections 13.4 and 14.1).

### Phase DEV-1 — candidate generation

Before choosing shared BM25 parameters or dense `D`, generate:

- **every BM25 configuration actually participating in the `k1/b` grid**, separately for raw/stem/lemma (the recommended grid gives 12 pairs × 3 representations = 36 lexical runs);
- every registered dense candidate;
- every predefined diversity run (include at least one if feasible).

Pool a common `top 50` per contributor where feasible, or use a deeper common depth. The mandatory minimum is **100% adjudicated top-10 coverage for every candidate whose `nDCG@10` will be compared, on every comparison topic**. Add residual judgments for all missing top-10 items before any selection. An initially selected/default BM25 run cannot stand in for the entire tuning grid. No tuning candidate may be artificially disadvantaged by unjudged top-10 documents.

Resolve `U` cases through recovery/adjudication. If required coverage cannot be obtained, pause the affected selection and apply only the predefined common eligibility/quality rules; do not score missing tuning labels as 0 or silently drop a disadvantaged candidate.

### Phase DEV-2 — model/parameter selection

Only after DEV-1 coverage is satisfied:

1. select one shared BM25 configuration using Section 10.2;
2. select one fixed dense `D` using Section 11.4.

`Recall@100` may break a tie **only when every compared candidate has 100% adjudicated top-100 coverage on every eligible comparison topic**, with common qrels and topic denominators. Otherwise skip Recall and apply the deterministic non-relevance tie rule in the relevant selection section. The Section 13.4 test threshold of 95% is insufficient for a tuning tie-break.

Archive the selection decisions and their qrels version. Later dev pool extensions must not be used for opportunistic reselection; any necessary redesign requires a documented pre-test revision and consistent repetition of the affected phases.

### Phase DEV-3 — selected-component extension

After the shared BM25 configuration and fixed `D` are selected, extend judgments through the selected `L_raw`, `L_stem`, `L_lemma` and `D` top-100 candidate sets. Prefer **complete adjudication of the union of all four lists for each dev query**. This covers every candidate available to the three hybrids and supports both alpha tuning and pooled-qrels `Recall@100`.

If complete union adjudication is infeasible, document residual unknowns, satisfy at least the per-query component coverage gates in Section 13.4, and complete every interior hybrid's top 10 in DEV-4. Recall with residual unknown top-100 items is only a qualified descriptive pooled-qrels result; it cannot be used for model/parameter/alpha selection. If even these gates fail, pause alpha selection and extend/review the pool.

### Phase DEV-4 — alpha tuning

Generate **all interior-alpha hybrid candidates** for raw/stem/lemma from the selected top-100 component unions. Before comparing by `nDCG@10`, require **100% adjudicated top-10 coverage for every candidate and topic**; judge any residual items, including unresolved `U` cases. Recheck coverage against the common final alpha-tuning qrels snapshot.

Complete adjudication of the selected-component union remains preferred where feasible. If it is incomplete, alpha Recall tie-breaks require the separate strict 100% top-100 gate; otherwise use the non-relevance tie rule in Section 12.4. Evaluate endpoints as standalone dev references with fully adjudicated top 10, and choose the global **interior** alpha using the morphology-neutral rule. Select `B_m` (Section 19.3) only with the same top-10 coverage safeguards.

---

## 13.3 Test initial pool

**After `EXPERIMENT_LOCK` has been created**, generate held-out test runs and their initial pool. The lock includes `D`, BM25 parameters, global interior alpha, metrics, features, SESOI, tests and all retrieval settings (Sections 24 and 31). The default workflow locks before test annotation; a separate assessor team's logistical exception requires the label-access barrier in Section 24.2. The test pool must include at least:

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

After initial judgments, compute judged coverage for each **query and primary core run**, not just aggregate coverage.

For a run returning `n_k = min(k, number of available returned candidates)` unique IDs, define `judged@k` as the number of those IDs with a final adjudicated `0/1/2` label divided by `n_k`. Report list length/shortfalls separately; if `n_k=0`, coverage is `NA` and requires audit, not an automatic pass. `U`/unjudgeable and absent/unresolved labels remain in the returned-list denominator but **do not count in the judged numerator**. Report `U` separately from never-assessed items; neither may be removed from the denominator to inflate coverage.

Required minimum judged coverage:

- top 10: **100%**;
- top 50: **≥98%**;
- top 100: **≥95%**.

If any core run fails a gate, add the unjudged documents needed from its top 100 to a residual pool and judge them.

Repeat until the gates are satisfied or a documented resource stop is triggered.

If the top-50 judged-coverage gate cannot be reached, confirmatory set-based analysis at `k_set=50` is not permitted for the affected query/run.

Apply required metric eligibility to a common paired topic set across compared runs and report exclusions and effective N. Top-10 failure prohibits the affected confirmatory `nDCG@10` comparison; top-100 failure prohibits confirmatory `Recall@100` for the affected comparison. Partial top-50/top-100 coverage remains a pooled-qrels limitation even when a gate passes. Secondary runs need the same gates for any corresponding inferential claim. Dev selection uses the **stricter metric-specific gates in DEV-1–DEV-4**; these test minima never authorize tuning on unjudged documents.

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

It does not count as a judged item for any coverage gate. Recover assessable source text or seek adjudication where possible; otherwise retain `U` in the audit and as unresolved coverage. Do not selectively remove unjudgeable returned IDs to make a run pass a gate. Any corpus-wide eligibility repair must be documented and applied consistently under the lock/change-control rules.

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

## 14.8 Topics with zero known relevant units

After sufficiently deep, adjudicated pooling and residual extension, a topic with `|Rel(q)| = 0` must be flagged **`NO_KNOWN_RELEVANT`**. This means no relevant unit is known in the pooled qrels; it does not establish that the corpus contains none. Unresolved `U` items or shallow coverage cannot be used to certify topic quality.

- Do **not** assign `Recall=0`, oracle-union recall 0 or another arbitrary value to an undefined denominator.
- Exclude these topics from metrics requiring at least one known relevant unit, including all Recall depths, `OracleUnionRecall`, recall-based headroom/gains, AP/MAP and nDCG when `IDCG=0`; record the affected values as `NA`.
- Use the same eligible topics for every system in each paired comparison and its derived gain/association analysis; report each metric's effective N. Never let an evaluation library silently supply a zero that enters the average.
- Retain the topic and its known relevant-hit counts/set diagnostics in the audit; any empty-set zeros are descriptive and must not be interpreted as evidence of successful agreement or practical equivalence. For primary H1/H2a inference, use topics with at least one known relevant unit as a common eligibility rule.
- Report the number and proportion among all frozen test topics, plus an audit row containing topic ID, pooling depth/coverage, unresolved counts, adjudication status, affected metrics, exclusion/review reason and action taken.

Predefine a small quality-review trigger before test-label exposure: the **provisional trigger is >5% of frozen test topics** flagged `NO_KNOWN_RELEVANT`. If exceeded, **pause confirmatory analysis** and review query narratives, corpus fit and pooling quality before final claims. Review must remain blind to system identity and cannot tune retrieval settings. Additional pooling follows pre-frozen residual rules; substantive redesign after label exposure requires change control and appropriately exploratory/new-held-out validation, not silent repair.

Default policy: **no post-outcome query replacement**. Any replacement policy must instead be defined before test outcomes are inspected, with independently constructed reserve topics, deterministic order and system-independent eligibility reasons. Never replace/select queries because particular systems failed. Preserve originals in the audit, include all frozen topics in the trigger denominator, and revisit the prospective sensitivity gate using the actual eligible N.

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

Retain a linked topic-level audit for `NO_KNOWN_RELEVANT`, metric eligibility/effective N and any predefined quality review or replacement (Section 14.8).

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

If pooled-qrels `IDCG=0`, nDCG is `NA` and the topic is excluded under Section 14.8, with the same eligible topic set across paired systems.

---

## 16.2 Primary coverage metric

**`Recall@100`**

using binary relevance `grade >= 1`.

Because qrels are pooled and not exhaustive, this is pooled-qrels Recall and must be interpreted together with judgment-coverage statistics.

For `|Rel(q)|=0`, report `NA` and apply Section 14.8; never silently score Recall as 0.

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

`Rel(q)` = set of benchmark retrieval-unit IDs with adjudicated pooled-qrels grade `>=1`; it is not the exhaustive corpus-relevance set. Apply the zero-relevant-topic eligibility rule in Section 14.8.

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

This is a candidate-set upper-bound diagnostic **against the known pooled qrels**, not an estimate of exhaustive corpus relevance. Always report the absolute oracle-union relevant-hit count `OracleUnionHits_m@50 = |OracleUnion_m(q)|` alongside pooled-qrels recall. If `|Rel(q)|=0`, recall is `NA` under Section 14.8.

It is **not** a fused ranking and **not** per-query best alpha.

---

## 18.6 Candidate-set complementarity headroom

`Headroom_m@50 = OracleUnionRecall_m@50 - max(Recall@50(L_m), Recall@50(D))`.

This describes how much **known pooled-qrels** relevant coverage exists in the union beyond the better individual component at the same depth. Also report absolute additional known hits: `|OracleUnion_m(q)| - max(|J_m(q)|, |J_D(q)|)`. Recall-based headroom is `NA` when `|Rel(q)|=0`.

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

is the standalone system with higher mean dev `nDCG@10`, using common qrels/topics and 100% adjudicated top-10 coverage for both systems after DEV-3/DEV-4. On an exact mean-score tie, choose `L_m` deterministically; do not use incompletely judged Recall.

Freeze `B_m`.

Then on test:

`G_best(m,q) = E(H_m,q) - E(B_m,q)`.

This is the primary “best standalone” comparison.

A per-query test oracle:

`max(E(L_m,q), E(D,q))`

may be reported only as a clearly labelled diagnostic and must not be described as a deployable baseline or as the primary H2b comparator.

---

# 20. Practical-effect thresholds / SESOI

The numbers below are **candidate planning thresholds only**. They are **not yet scientifically frozen SESOI or evidence-derived truths**, and cannot support confirmatory meaningful/negligible-effect claims in v0.1.

Before confirmatory test analysis, justify final SESOI and equivalence margins using scientific/practical relevance, measurement reliability and resolution, literature where appropriate, and the prospective sensitivity analysis in Section 5.1. Record the rationale and final values in the pre-test protocol revision and `EXPERIMENT_LOCK`, **before test-label exposure**.

Do not choose margins by inspecting which threshold makes comparative raw/stem/lemma dev differences appear meaningful, negligible or favorable. Comparative dev morphology effects themselves cannot justify the margins. Dev annotation calibration may inform measurement reliability, and prespecified nuisance estimates may inform sensitivity, without tailoring target effects/margins to observed comparative effects. Do not widen/shrink margins or redefine practical relevance to make a desired result detectable within the annotation budget. Freeze any change with its independent rationale before test; never revise margins after seeing test effects.

## 20.1 Ranking effectiveness

For mean paired changes in `nDCG@10`:

- candidate negligible/equivalence band: approximately `[-0.02, +0.02]`;
- candidate minimum practically meaningful absolute mean difference: `>= 0.02`, subject to independent justification.

For `Recall@100` / oracle-union recall:

- candidate practical band: approximately `[-0.03, +0.03]`.

---

## 20.2 Relevant-set composition

For normalized set-change quantities such as:

- `LexSetChange`;
- `ComplementaritySetShift`;

candidate planning interpretation, pending justification and freeze:

- `<= 0.05`: small/negligible set change;
- `>= 0.10`: practically meaningful set change;
- `0.05–0.10`: indeterminate/intermediate zone requiring uncertainty analysis.

These are not p-values or validated cutoffs. The `|rho| >= 0.20` association value in Section 22.2 is likewise a planning candidate requiring justification and sensitivity validation.

The final frozen thresholds must be version-controlled in the pre-test revision / `EXPERIMENT_LOCK` before the research-tuning side can access test labels. Sections 21–22 refer to those final justified thresholds, not automatically to these planning values.

---

# 21. Statistical analysis

## 21.1 Unit of analysis

Primary inferential unit:

**query**.

All primary raw/stem/lemma comparisons are paired because the same query is evaluated under every condition.

Use the metric-specific common eligible topic sets from Sections 13.4 and 14.8; report exclusions and actual N. The prospective sensitivity report (Section 5.1) must cover the final decision procedures, multiplicity and equivalence claims before query-count freeze. If actual eligibility losses exceed its assumptions, review Gate G before retaining confirmatory scope; low sensitivity cannot become evidence of no effect.

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

Use only independently justified margins locked under Section 20, with the declared multiplicity treatment for the corresponding claim family. The planning candidates are not automatic equivalence limits. Sensitivity to establish equivalence must also be assessed prospectively; a wide interval is insufficient evidence.

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

Confirmatory H3 status is conditional on prospective sensitivity for the final feature/contrast/outcome family and usable test N (Section 5.1 and Gate G). If that gate fails, label H3 and its feature-association analyses **exploratory** before test-label exposure while retaining the predefined analysis/reporting plan.

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

Candidate planning practical association requirement (subject to Section 20 justification and freeze):

`|Spearman rho| >= 0.20`

plus a bootstrap confidence interval that does not indicate an unstable sign.

Do not presume that the planning target of 120 test queries can detect this effect reliably. Prospective analysis must include the full FDR family, correlated features, feature prevalence and query-level dependence. Underpowered or non-significant results are **insufficient evidence**, not evidence of no association; exploratory H3 results cannot support a confirmatory H0₃ claim.

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

Conventional pooled-qrels evaluation assumptions may be reported only with the appropriate coverage gates and limitations. They do not override the tuning rule: **parameter/model/alpha selection must never interpret unjudged tuning documents as evidence of non-relevance**. Complete candidate top-10 judgments before `nDCG@10` tuning and require strict top-100 coverage before any Recall tie-break (Section 13.2).

---

## 23.2 Judgment coverage reporting

For every evaluated run report:

- judged@10;
- judged@50;
- judged@100;
- never-assessed/unresolved counts and separate `U` counts;
- returned-list lengths, metric eligibility and effective query N;
- `NO_KNOWN_RELEVANT` number/proportion and audit reference.

Use the Section 13.4 coverage denominator: `U` remains an unknown returned item and never inflates judged coverage. Set-based conclusions at `k=50` require the coverage gate in Section 13 and the common topic-eligibility rule in Section 14.8.

---

## 23.3 Robustness to incomplete qrels

If incomplete judgments remain non-trivial:

- report `bpref`;
- repeat key set analyses on the subset of queries/runs satisfying strict judged-coverage thresholds;
- perform a leave-one-pool-contributor sensitivity analysis if feasible.

Do not make a strong oracle-union claim from a shallow pool.

---

# 24. Leakage controls and experiment lock

## 24.1 Lock before test-label exposure and, by default, test annotation

After dev phases are complete, freeze and version `EXPERIMENT_LOCK` **before generating the held-out test runs/pool and before test annotation in the default workflow**. The investigator and all research/tuning participants must not inspect any test relevance labels before lock, even without running evaluation. The manifest contains:

- corpus snapshot/hash;
- query split and hash;
- final planned query N, prospective power/sensitivity report and confirmatory/exploratory status per hypothesis;
- declared source-document/section-level scope, unit IDs and any segmentation rule;
- tokenizer/preprocessing versions;
- raw/stem/lemma algorithms and independent processor-selection rationale;
- BM25 implementation and parameters;
- selected `D` checkpoint, exact/ANN settings and any ANN fidelity threshold/sample/report;
- global interior alpha, full selection grid, dev endpoint diagnostic and fixed `B_m` comparators;
- normalization formula;
- deterministic component/fusion tie rules and RRF missing-rank treatment;
- `k_set`;
- `k_cand`;
- RRF parameter;
- primary metrics;
- primary statistical tests;
- RQ3 feature list;
- SESOI/equivalence thresholds;
- scientific/practical rationale for final margins independent of comparative dev morphology effects;
- dev candidate inventory, phase-specific coverage reports and qrels/selection hashes;
- test pool contributors/depths, residual extension rules and metric eligibility gates;
- `U` treatment, `NO_KNOWN_RELEVANT` trigger and any predefined replacement policy;
- assessor rubric, adjudication procedure and test-label access controls;
- software/container environment;
- random seeds.

Suggested file later:

`experiments/EXPERIMENT_LOCK_v0.1.json`

or equivalent.

Creating that file is **not** part of this protocol-writing task.

---

## 24.2 Test access rule

Default sequence after `EXPERIMENT_LOCK`:

1. generate held-out test runs and the test pool using locked settings;
2. annotate and adjudicate test qrels under the locked rubric;
3. complete predefined coverage/quality checks and freeze the test qrels version;
4. release labels to the research/evaluation side and run confirmatory evaluation for the hypotheses passing the validity gates.

No configuration may be changed in response to test relevance labels or performance. Record lock, run-generation, annotation, qrels-release and evaluation timestamps/hashes.

**Logistical exception:** a separate assessor team may annotate test material before lock only if a documented access barrier keeps **all test relevance labels, label summaries and relevance-bearing feedback inaccessible to the investigator/research-tuning side until after lock**. Use separate permissions/storage and an access/release log; the investigator must not act as an early test assessor. Before the final lock, only label-blind logistics metadata may be shared. After lock, generate the final locked runs/pool and judge any additional required candidates without revising settings. Prefer lock-before-test-annotation; this exception does not authorize tuning with early test labels.

If a bug invalidates a configuration:

1. document the bug;
2. fix it;
3. version the protocol/experiment lock;
4. rerun all affected conditions consistently;
5. do not selectively rerun only unfavorable systems.

Once test labels have been exposed, a revised configuration cannot retroactively restore an untouched confirmatory test; label affected analyses exploratory or obtain a new independent held-out validation as appropriate. A version bump does not legitimize test-driven model, alpha, feature or SESOI selection.

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
- exact-search/ANN fidelity reference, sample, acceptance rule and results;
- deterministic tie order/score precision and RRF missing-component policy;
- dev candidate/phase coverage manifests, qrels versions and selection decisions;
- retrieval-unit/source-document mapping and scope;
- power/sensitivity assumptions, code/seeds, final N and SESOI rationale;
- experiment-lock/test-label access and release timestamps;
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

Across the dev, lock, test-annotation and evaluation stages in Section 31, the project should eventually contain or generate:

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

The artifact set must also include prospective power/sensitivity results, justified SESOI, phase-specific dev coverage/selection records, any ANN fidelity report, a retrieval-unit/source-document map, the zero-relevant-topic audit and test-label access logs. Only dev qrels are available during tuning; final test qrels belong to the post-lock annotation/evaluation stage (Section 31).

These are future outputs; this v0.1 protocol does not create them.

---

# 27. Benchmark validity gates

Pre-lock gates must pass before generating the main held-out runs; test-qrels gates are checked after locked annotation and before confirmatory evaluation. Test-qrels inspection is never a pre-lock prerequisite. Retained confirmatory claims require all applicable gates below.

## Gate A — corpus

- at least 50,000 cleaned retrieval units for a general benchmark;
- at least three substantive domains, unless explicitly labelled domain-limited;
- corpus frozen and hashed;
- duplicates/near-duplicates addressed;
- source-document units preferred where fair; any deterministic common segmentation and stable IDs documented;
- evaluation/dissertation scope explicitly matches source-document vs retrieval-unit/section-level evidence.

## Gate B — query set

- current planning target: 180 information needs, 60 dev / 120 test;
- final N/split justified prospectively and frozen, rather than presumed sufficient from budget;
- feature/domain coverage audited;
- query construction provenance recorded.

## Gate C — qrels

- two independent assessors per pooled pair;
- disagreement adjudication complete;
- agreement reported;
- DEV-1–DEV-4 metric-specific coverage gates satisfied before each dev selection;
- post-lock test top-10/top-50/top-100 gates satisfied for the corresponding primary claims;
- `U` excluded from judged numerators and retained in coverage denominators;
- `NO_KNOWN_RELEVANT` audit complete, undefined metrics excluded consistently, and the pre-frozen zero-relevant-topic trigger reviewed (provisional pause trigger: >5%).

## Gate D — dense comparator

- at least BGE-M3 Dense and multilingual E5 compared on dev;
- one `D` selected by the predefined rule;
- `D` frozen before test;
- exact vector search used where practical, or ANN fidelity passes its pre-frozen gate against exact search (planning mean top-100 target `>= 0.99`).

## Gate E — causal controls

The same across morphology conditions:

- BM25 implementation/parameters;
- `D`;
- candidate depth;
- normalization;
- global interior alpha from `{0.05, 0.10, ..., 0.95}`;
- fusion formula;
- query/document corpus;
- qrels.

Primary morphology processors must have an independently documented pre-comparison selection/freeze. Endpoints remain standalone references even when they outperform all interior alphas.

## Gate F — experiment lock

All final primary settings, features, tests and independently justified thresholds are versioned in `EXPERIMENT_LOCK` **before any test relevance-label access by the research/tuning side**, and before test runs/pooling/annotation in the default workflow. Any separate-assessor logistical exception must demonstrate the Section 24.2 access barrier.

## Gate G — statistical sensitivity / power

- prospective analysis completed before final query-count freeze for paired `nDCG@10`, H1 set change, H2a complementarity-set shift, H2b `ΔG_lex` and RQ3 associations;
- final N, target power/precision, independently justified effects/margins, multiplicity and plausible eligibility losses documented;
- each retained confirmatory claim has adequate sensitivity under its planned decision procedure; budget alone is insufficient;
- H3 explicitly exploratory if available N cannot adequately assess the practical association, including `|rho| = 0.20` as the current planning candidate under FDR;
- actual metric-specific eligible N checked after locked annotation; unexpected losses require sensitivity/scope review, without choosing new favorable margins or treating non-significance as no effect.

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
- distinguish adequately sensitive confirmatory evidence from exploratory/underpowered H3;
- report insufficient evidence about the predefined associations when sensitivity is inadequate; do not claim no association from a small N or non-significant result.

A negative result is a valid outcome.

---

# 29. What this protocol does not establish

Even if the full experiment succeeds, it will not by itself prove:

- universal superiority of lemmatization;
- universal superiority of stemming;
- universal superiority of hybrid retrieval;
- universal superiority of the selected dense retriever;
- transfer to all Uzbek domains;
- full original-document retrieval if the actual benchmark ranks canonical sections/passages;
- exhaustive corpus relevance from pooled-qrels Recall or oracle-union recall;
- causal linguistic mechanisms beyond the controlled intervention and observed associations;
- novelty of normalized fusion, RRF or dynamic weighting.

Any method/novelty proposal must follow the evidence.

Every report must name the actual benchmark retrieval unit, disclose segmentation and pooling/coverage limitations, show absolute known relevant-hit counts alongside oracle-union recall, and report zero-relevant-topic exclusions and statistical sensitivity. Dissertation wording must match the actual source-document or section-level scope.

---

# 30. Protocol change control

This v0.1 remains an unimplemented, provisional design. The research gap (`v0.8 refined / provisional`) and working RQ/H v0.2 remain unchanged. Once benchmark implementation begins, any substantive protocol modification must create a new version under the rules below.

Examples requiring version bump:

- changing query count/split;
- changing relevance scale;
- changing `k_set` or `k_cand`;
- changing primary metrics;
- changing morphology algorithms after dev inspection;
- changing `D` after test evaluation;
- changing global alpha using test labels;
- changing SESOI, their rationale or confirmatory sensitivity/N assumptions;
- adding/removing confirmatory RQ3 features after test inspection.

Changes selected from test outcomes remain prohibited for the original confirmatory study even with a version bump. Comparative dev morphology effects may not be used to optimize SESOI at any version. Post-exposure unplanned changes require exploratory reporting or new independent held-out validation (Section 24.2).

Recommended progression:

`v0.1` — benchmark/qrels design  
`v0.2` — concrete resources/checkpoints/corpus frozen  
`v0.3` — annotation/pooling feasibility corrections, if required  
`EXPERIMENT_LOCK` — final pre-test immutable configuration

After test qrels are opened, any unplanned analysis must be labelled **exploratory**.

---

# 31. Immediate next implementation sequence

The default implementation order is:

1. **Freeze corpus/resources:** establish licenses, corpus snapshot/hash and source-document or explicitly declared canonical-section units; independently select/freeze tokenizer, stemmer and lemmatizer before comparative dev IR analysis. Register BM25 grid, dense candidates and diversity runs; establish exact/ANN fidelity controls.
2. **Complete the initial dev benchmark/qrels:** start from the `180 = 60 dev + 120 test` planning design, define independent topic construction/stratification and features, construct dev topics, calibrate assessors and complete DEV-1 candidate generation/pooling with all tuning candidates' adjudicated top 10. Complete prospective power/sensitivity analysis before final query-count/split freeze, with no test-label input.
3. **Choose shared BM25 parameters:** apply DEV-2 and its strict Recall tie-break gate or deterministic non-relevance fallback.
4. **Choose fixed dense `D`:** apply the DEV-2 selection rule and fidelity controls; then complete DEV-3 selected-component top-100 judgment extension.
5. **Choose global hybrid alpha:** complete DEV-4 judgments for all interior candidates, choose one alpha from `{0.05, 0.10, ..., 0.95}`, evaluate endpoints as references, and freeze dev-selected `B_m` comparators.
6. **Freeze the complete pre-test design:** final corpus/resources and query split/N, primary metrics, RQ3 features and claim status, independently justified SESOI, tests/multiplicity, all retrieval/fusion settings, test pooling/rubric/access rules, eligibility and zero-relevant-topic policy. Archive dev qrels/coverage/selection evidence and the sensitivity report.
7. **Create and version `EXPERIMENT_LOCK`** with hashes and timestamp. The investigator/research-tuning side has not inspected any test relevance labels.
8. **Generate held-out test runs and test pool** from the locked configuration.
9. **Annotate/adjudicate test qrels**, perform the predefined residual pooling and quality gates, audit zero-relevant topics and effective N, and freeze the qrels release.
10. **Run confirmatory test evaluation** only for claims passing the relevant gates; report prespecified exploratory analyses with that label.

Lock-before-test-annotation is preferred. If a separate assessor team needs earlier annotation for logistics, Section 24.2's label-access barrier is mandatory, and final locked runs/pool coverage must still be verified after lock. Early annotation never permits early investigator access to labels.

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

Before test-label exposure, a later frozen revision must fill in Section 2.2, justify final N and SESOI, complete phased dev selection/coverage and produce `EXPERIMENT_LOCK`. The default workflow generates test runs/pools and annotates test qrels only after that lock. The 180-topic design and numerical effect thresholds remain planning candidates until prospectively justified; confirmatory scope must pass the sensitivity gate.

The central scientific priority remains:

> test whether changing Uzbek lexical morphology actually changes the unique relevant evidence contributed relative to one fixed semantic dense retriever, and whether that change translates into incremental hybrid gain.

No new retrieval architecture should be proposed before this baseline evidence exists.
