# Allanazarova S.Y. — Uzbek sentiment analysis and SentiUzNet

**Deep-dive status:** COMPLETED  
**Completed:** 2026-09-11  
**Suggested literature ID:** UZ-NLP-001  
**Priority for current retrieval PhD:** LOW / BACKGROUND  
**Reliability:** B pending final-defense verification

## 1. Bibliographic record

- **Author:** Allanazarova Saboxat Yusupboyevna
- **Title:** *O‘zbekcha matnlarning sentiment tahlili va lingvistik ta’minoti (xizmat ko‘rsatish sohasining ijtimoiy tarmoq postlari asosida)*
- **English title:** *Sentiment Analysis and Linguistic Resources for Uzbek Texts (Based on Social Media Posts in the Service Industry)*
- **Degree sought:** PhD in Philology
- **Specialty:** 10.00.11 — Applied and computational linguistics
- **Institution:** Alisher Navoiy Tashkent State University of Uzbek Language and Literature
- **Scientific adviser:** Elova Dilrabo Qudratillayevna
- **Registration number:** B2023.2.PhD/Fil3663
- **Author abstract:** 2026
- **Source type:** user-supplied author abstract + official OAK registration record
- **Reliability:** **B** until final defense/result is verified

### Status note

The official OAK bulletin confirms Allanazarova’s dissertation topic, specialty, registration number `B2023.2.PhD/Fil3663`, supervisor and institution. The supplied author abstract is a 2026 pre-defense-style document: official-opponent, leading-organization, defense-date and abstract-distribution fields are blank. No final defense protocol/result was recovered in the current verification.

## 2. Why this work matters — and why only indirectly

This dissertation is **not an information-retrieval dissertation**.

It is relevant to our national map because it proves that Uzbek NLP already includes:

- manually annotated lexical-semantic resources;
- context-sensitive language analysis;
- machine-learning classification;
- hybrid lexical/statistical/LLM resource construction;
- large real-world social-media datasets;
- explicit handling of Uzbek orthographic/morphological peculiarities.

But its target is:

> positive / negative / neutral sentiment classification,

not:

> query → ranked relevant documents.

Therefore it should be kept as **background Uzbek NLP/semantic-resource evidence**, not as a direct gap-killer for our retrieval PhD.

## 3. Research goal

The stated goal is to develop linguistic resources for sentiment analysis of Uzbek texts.

Main tasks include:

- study sentiment resources in other languages;
- identify Uzbek sentiment-bearing units and context-dependent factors;
- build a sentiment lexicon/tagging system;
- evaluate sentiment models on real Uzbek social-media comments.

## 4. SentiUzNet

The central contribution is `SentiUzNet`.

### Simple explanation

SentiUzNet is a resource that assigns words/synsets sentiment information such as:

- positive;
- negative;
- neutral/objective.

### Construction

The dissertation combines:

- manual linguistic annotation;
- six human annotators;
- GPT-based semantic checking;
- SentiWordNet;
- SenticNet;
- PMI statistics;
- neural network;
- logistic regression;
- Random Forest.

This is called a **hybrid** or semi-automatic approach in the dissertation.

Important:

`hybrid sentiment-resource construction != hybrid information retrieval`

## 5. Annotation

The dissertation reports:

- **3,336 synonymic synsets**;
- manual positive/negative/neutral labeling;
- at least three annotator votes required for a class decision;
- six Uzbek-language expert annotators;
- reported mean **Cohen’s κ = 0.79**.

This is useful national evidence that lexical-semantic Uzbek resources can be expert-annotated with an explicit agreement procedure.

## 6. Data

The dissertation combines several existing/social-media review resources.

A table reports a combined total of:

- **397,227 reviews** before/around preprocessing/integration.

The dissertation also repeatedly refers to:

- **384,000+ Uzbek social-media comments** from the service domain used for the practical sentiment experiment.

These two values should not be silently treated as identical. The source appears to distinguish the merged review pool from the final/service-domain experimental set.

Preprocessing includes:

- normalization of Uzbek apostrophe/letter variants;
- removal of numbers, emoji and special symbols in the described experiment;
- normalization of informal elongations/spellings;
- stop-word filtering;
- frequency-dictionary construction.

## 7. Models

The dissertation states that **11 models** were tested using combinations/variants based on:

- neural networks;
- logistic regression;
- Random Forest.

For final SentiUzNet scoring, three models are described explicitly:

- neural network;
- logistic regression;
- Random Forest.

Their outputs are combined by arithmetic averaging to produce final sentiment scores for synsets.

## 8. Features

For each synset, an 18-dimensional feature vector is described, including:

- POS;
- GPT positive/negative/objective scores;
- SentiWordNet positive/negative/objective scores;
- SenticNet positive/negative/objective scores;
- positive/negative PMI;
- PMI computed over gloss words;
- counts of positive/negative PMI indicators.

This is a meaningful lexical-semantic feature-engineering contribution, but it is not retrieval scoring.

## 9. Results

The dissertation reports:

- model accuracy range: **71–91%**;
- evaluation using Precision, Recall and F1;
- sentiment classification accuracy of **91%** on 384k+ Uzbek comments;
- annotator agreement **κ = 0.79**.

The supplied abstract does not provide enough methodological detail to reconstruct a standard train/dev/test protocol for every one of the 11 model variants or to establish statistical significance between them.

## 10. Linguistic findings

The work identifies Uzbek-specific/context-sensitive sentiment factors such as:

- negation;
- intensifiers/diminishers;
- irrealis modal constructions;
- sarcasm;
- irony;
- dialectal units;
- spelling errors;
- cultural connotation.

It argues that ignoring context reduces sentiment-analysis accuracy.

This is useful general evidence that Uzbek lexical meaning can change with morphology/context, but it is task-specific evidence for **sentiment classification**, not retrieval relevance.

## 11. Transfer from Turkish

The dissertation studies transfer/adaptation from Turkish `SentiTurkNet`.

It concludes that transfer can help enrich low-resource sentiment resources but has limitations, especially where culture/domain affects sentiment values.

This is relevant as general Turkic-resource-transfer evidence, but it does not establish transfer behavior for IR morphology or dense retrieval.

## 12. Practical implementation

Reported uses include:

- Uzbek educational corpus project;
- interactive platform for national names of service-sector objects;
- public-opinion analysis;
- media-content analysis.

The resource is published through `sentiuznet.uz` and associated software/database registrations are reported.

No document-search benchmark is reported.

## 13. What this work establishes

Safe conclusions:

- Uzbek sentiment lexicons/resources are an active national research area;
- expert-annotated lexical-semantic resources exist;
- contextual factors are computationally important in Uzbek;
- hybrid lexical/statistical/LLM resource construction exists;
- large Uzbek real-world text collections have been used for supervised NLP evaluation.

## 14. What this work does NOT establish

It does **not** establish:

- BM25 effectiveness;
- stemming or lemmatization effects on retrieval;
- dense retrieval effectiveness;
- query-document ranking;
- BM25 + dense fusion;
- lexical-only vs dense-only relevant hits;
- overlap / oracle union;
- incremental hybrid gain;
- morphology-induced lexical–dense complementarity.

## 15. Why “hybrid” here must not be confused with our topic

Allanazarova hybrid:

`manual annotation + GPT + lexicons + PMI + ML`

for sentiment-resource construction/classification.

Our hybrid retrieval:

`lexical retriever + semantic/dense retriever`

for document ranking.

Therefore Allanazarova does **not** occupy our hybrid-retrieval novelty space.

## 16. Relationship to CURRENT_GAP v0.8

**Status:** no change.

The work sits outside the central residual chain:

`raw/stem/lemma lexical representation`
→ `BM25 relevant-set change`
→ `overlap/unique hits with fixed dense retriever`
→ `incremental hybrid gain`
→ `Uzbek query characteristics`.

It contributes only broad background evidence that Uzbek lexical, contextual and semantic NLP resources are already developed.

## 17. Role in our literature base

Recommended role:

- **background national NLP evidence**;
- optional support for Chapter I discussion of Uzbek semantic/lexical resources;
- not a CRITICAL gap-killer;
- not required for the core experimental design.

Recommended priority:

**LOW / MEDIUM-BACKGROUND**, not CRITICAL.

## 18. Implications for our PhD

1. Do not add sentiment analysis to the retrieval architecture.
2. Do not use SentiUzNet as a core retrieval component.
3. The work may support a general statement that Uzbek lexical meaning is context-sensitive.
4. For a fast, focused PhD, sentiment resources should remain outside the core method.
5. No change to `BM25_raw/stem/lemma + fixed dense D` is justified by this dissertation.

## 19. Open questions

- Verify final defense status/protocol.
- If cited numerically, clarify the relation between 397,227 merged reviews and the 384k service-domain experiment.
- If needed, inspect the 2025 UBMK SentiUzNet paper for exact model splits/baselines.
- Do not infer retrieval relevance from sentiment-classification accuracy.

## 20. Decision

- **Keep v0.8:** yes.
- **Modify gap/history/decisions:** no.
- **Add to MASTER_INDEX:** optional, as background national NLP.
- **Add full national deep-dive card:** yes, because the source was supplied and analyzed.
- **Core research priority:** low.
