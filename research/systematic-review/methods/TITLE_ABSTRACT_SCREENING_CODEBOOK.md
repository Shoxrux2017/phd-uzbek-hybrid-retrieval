# TITLE/ABSTRACT SCREENING CODEBOOK

Version: 1.0.0. Frozen preparation specification: 2026-09-18.

## Scope and status

Unit: one canonical bibliographic record, keyed by unchanged `canonical_id`.
This preparation assigns no scientific inclusion/exclusion decisions. It performs
no full-text reading, study-level linkage, record deletion or GitHub modification.
All six decision columns start empty. Allowed future labels: `INCLUDE`, `EXCLUDE`,
`UNCERTAIN`. An empty label means not yet screened, not any of those decisions.

## High-recall rule

Если существует разумная вероятность, что full text содержит релевантный
morphology-aware corpus-level retrieval experiment, запись НЕ исключать на
title/abstract stage. В таком случае использовать `UNCERTAIN` или `INCLUDE`
в зависимости от силы metadata. False inclusion на этом этапе лучше false exclusion.

`abstract_available` is `YES` when the canonical abstract contains non-whitespace
text, otherwise `NO`. Abstracts are not fetched, inferred, summarized or replaced.
Missing abstracts do not justify exclusion. Review title plus available metadata;
if insufficient, use `UNCERTAIN` with TA8 in future screening.

## Working reason codes

### TA1 — NOT_TEXT_RETRIEVAL

Работа не исследует text/document/passage retrieval. Примеры: classification,
machine translation, parsing, pure semantic similarity, image retrieval,
biological/material morphology. Use on established task mismatch, not keywords alone.

### TA2 — NO_MORPHOLOGY_RELEVANCE

Есть retrieval, но отсутствует morphology intervention, morphology-sensitive
analysis или meaningful morphology-related representation/problem.
If relevance cannot be determined confidently from metadata, use `UNCERTAIN`.

### TA3 — NLP_RESOURCE_ONLY

Morphology/NLP tool/resource присутствует, но corpus-level retrieval evaluation
отсутствует. Примеры: stemmer accuracy only, lemmatizer accuracy only,
POS/morphological analyzer only. Resource presence by itself is not retrieval evidence.

### TA4 — NO_CORPUS_LEVEL_RETRIEVAL_EVIDENCE

Работа обсуждает search/retrieval, но abstract/title не устанавливает реальный
corpus-level retrieval experiment или relevant evidence. Использовать осторожно.
Failure of an abstract to mention evaluation is not proof that none exists.
Если неясно — `UNCERTAIN`; do not infer exclusion from missing detail.

### TA5 — RAG_QA_RETRIEVAL_NOT_SEPARABLE

RAG/QA paper оценивает только конечный ответ или generation, а retrieval stage
не оценивается отдельно. Если abstract не позволяет установить это уверенно:
`UNCERTAIN`.

### TA6 — OUTSIDE_SCOPE

Явно вне review scope по задаче/предмету. Не использовать только потому, что
язык high-resource. Morphologically rich high-resource languages могут быть релевантны.

### TA7 — NON_PRIMARY_OR_NON_SCHOLARLY

Явно editorial, news, book review или non-scholarly item, если это можно
установить из metadata. Do not infer this from database, publisher or venue prestige.

### TA8 — INSUFFICIENT_METADATA

НЕ является EXCLUDE reason. Использовать только вместе с `UNCERTAIN`, когда
title/abstract/metadata недостаточно. Never pair TA8 with `EXCLUDE` or `INCLUDE`.

TA1–TA7 are working exclusion reasons only when clearly established under the
high-recall rule. No reason code is assigned during preparation. Future reviewers
record the code in `screening_reason_code` and their explanation in
`screening_reason_text`; no automated decisions are derived from metadata.

## Methodological distinctions

НЕ считать retrieval evidence автоматически:

- stemmer accuracy;
- lemmatizer accuracy;
- tokenizer accuracy;
- STS correlation;
- classification accuracy;
- generation quality;
- RAG answer accuracy.

НЕ исключать автоматически:

- RAG paper, если retrieval отдельно измеряется;
- QA paper, если passage/document retrieval отдельно evaluated;
- biomedical paper, если задача — именно text retrieval;
- high-resource language paper, если morphology/retrieval design релевантен.

## Reviewer packets and blinding

Use `batches/TA_BATCH_001.csv` through `TA_BATCH_021.csv`, or their Markdown
counterparts, for initial decisions. The full master is an audit/coordination
dataset: it retains every original field, including raw/alternate metadata and
native IDs. Its audit columns are not the initial reviewer interface.

Reviewer CSVs use a fixed allowlist in the requested field order, followed by
screening order, batch, abstract availability and the six empty decision columns.
Reviewer Markdown includes the same bibliographic context and empty Decision,
Reason and Notes prompts. Metadata is escaped only for safe literal Markdown
display; underlying CSV values remain unchanged.

Prior pilot labels `R1`, `R2`, `X`, pilot judgements, search/audit provenance and
project-membership flags are not imported into reviewer packets. Ordinary
bibliographic text such as author initial X., X-ray, or a mathematical X is
preserved: those are not pilot labels. Blinding is validated by field provenance
and explicit label markers, not by deleting these scientific characters.

Source families (`sources`) and `source_databases` remain visible. Publication
type and database provenance can be useful, but source must not determine relevance.
IEEE records are not automatically stronger or more relevant than EBSCO/PQDT/ACL.

Known prior deep-dive studies follow the same frozen screening criteria. They are
neither excluded nor auto-included because of project MASTER_INDEX membership.
No MASTER_INDEX matching is performed here; the optional `known_project_record`
flag is omitted, rather than inventing YES/NO values or doing study-level linkage.

`dedup_uncertain=true` is bibliographic uncertainty, not scientific relevance or a
screening label. Four records from two pairs remain separate and unchanged. If both
members pass screening, study-level linkage is checked later.

## Fixed order and independent second review

Sort canonical IDs lexicographically ascending; number `screening_order` 1–2010.
No relevance ranking, source order or year priority is applied. Batch numbers are
`TA_BATCH_001`–`TA_BATCH_021`: first twenty contain 100 records, final batch 10.

Before any screening, draw a simple random sample without replacement from all
2010 sorted canonical IDs using Python `random.Random(20260918).sample(ids, 402)`.
No source, language, abstract-availability or other strata/weights are used.
Serialize the selected records in screening order. The master has exactly 402
`second_review_random_sample=YES`; others are `NO`. The flag is omitted from
primary reviewer packets. Runtime and selected-ID hash are recorded in the manifest.

`SECOND_REVIEW_SAMPLE_20_PERCENT.csv` contains only canonical_id, screening_order,
batch, title, abstract, with no primary-review decisions. Second review must remain
independent of primary decisions. After primary screening, all `UNCERTAIN` records
also receive second review independently of random-sample membership; that later
step is not executed now and does not change this frozen random sample.

## Recording future decisions

`screening_label`, `screening_reason_code`, `screening_reason_text`, `reviewer`,
`review_date`, `review_notes` are all blank at preparation. Future dates should use
YYYY-MM-DD. Labels and reasons require reviewer judgement, not automatic inference.
CSV itself does not enforce dropdown validation. Preparation validates emptiness;
any later decision-validation or reconciliation belongs to a separate authorized step.

Stop after preparation. Do not begin Batch 001 or retrieve full texts.
