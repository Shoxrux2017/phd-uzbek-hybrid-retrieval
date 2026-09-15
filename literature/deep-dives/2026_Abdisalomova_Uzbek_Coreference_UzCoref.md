# Abdisalomova Sh.A. — Uzbek coreference resolution and UzCoref

**Deep-dive status:** COMPLETED  
**Completed:** 2026-09-11  
**Suggested literature ID:** UZ-SEM-009  
**Reliability:** B pending final-defense verification

## 1. Bibliographic record

- **Author:** Abdisalomova Shahlo Abdimurod qizi
- **Title:** *O‘zbek tilidagi matnlar koreferensiyasini avtomatik aniqlashning lingvistik va dasturiy ta’minoti*
- **English title:** *Linguistic bases and software of the Coreference Resolution in Uzbek texts*
- **Degree sought:** PhD in Philology
- **Specialty:** 10.00.11 — Applied and computational linguistics
- **Institution:** Alisher Navoiy Tashkent State University of Uzbek Language and Literature
- **Scientific adviser:** Elov Botir Boltayevich
- **Registration number:** B2025.1.PhD/Fil3658
- **Author abstract:** 2026
- **Source type:** user-supplied author abstract + official OAK registration evidence + official university discussion notice
- **Reliability:** **B** until final defense/result is verified

### Official status verification

Verified:
- the OAK bulletin lists Abdisalomova with registration number `B2025.1.PhD/Fil3658`;
- the university officially announced departmental discussion of the dissertation for 2025-06-25.

The supplied 2026 abstract still contains blank fields for official opponents, leading organization, defense date/time and abstract distribution date. No final defense protocol/result was recovered during this deep dive.

Therefore the work is real and institutionally verified, but should not yet be treated as an A-level defended PhD.

## 2. Why this work matters to our PhD

This work shows that Uzbek semantic/contextual NLP already includes:

- a manually checked coreference corpus;
- rule-based, statistical, neural and hybrid coreference approaches;
- multilingual transformer baselines;
- an Uzbek-adapted RoBERTa variant;
- semantic/contextual vector representations;
- a real software system (`UzCoref`) with web UI, CLI and REST API;
- direct use of Uzbek-specific morphology/syntax features in semantic/contextual analysis.

This closes broad claims that Uzbek lacks contextual semantic analysis or transformer-based discourse processing.

However, coreference resolution is **not information retrieval**. The dissertation does not rank documents for user queries.

## 3. Coreference explained simply

Coreference means recognizing that different expressions in a text refer to the same entity.

Example:

`Zaynab opasi bilan kinoga bordi. ... u kitobxonlikni yaxshi ko‘rardi.`

The system must determine who `u` refers to.

Another simple example:

`Alisher Navoiy buyuk shoir edi. U ko‘plab asarlar yozgan.`

A coreference system links:

`Alisher Navoiy ↔ U`

This improves machine understanding of a document, but it does not by itself retrieve documents from a collection.

## 4. Research goal

The stated goal is to develop the linguistic resources and software required to automatically resolve coreference in Uzbek texts.

Main tasks include:

- studying coreference/anaphora for agglutinative languages;
- collecting and annotating Uzbek text fragments with coreference relations;
- designing an Uzbek coreference algorithm;
- building the hybrid `UzCoref` system.

## 5. Data / corpus

The dissertation reports a dedicated Uzbek coreference corpus:

- **1,020 documents**
- **820 train**
- **100 validation**
- **100 test**
- approximately **320,000 tokens**
- **18,451 annotated mentions**
- **5,326 coreference chains**
- average chain length about **3.5 mentions**

Sources include:
- school textbooks;
- literary works;
- Constitution articles;
- medicine instructions;
- Wikipedia;
- Bilimlar.uz and other materials.

### Annotation quality

The corpus uses a two-stage annotation process:

1. automatic pre-annotation;
2. manual checking and correction by linguist experts.

This is stronger annotation evidence than a purely model-generated dataset.

The corpus uses CoNLL-style annotation conventions.

## 6. What is annotated

The work focuses mainly on nominal/reference coreference:

- nouns;
- noun phrases;
- pronouns;
- some action nouns / referential structures.

The annotation explicitly defines special treatment for:

- coordinated mentions;
- nested mentions;
- demonstratives;
- synonymic names;
- discourse references.

Some phenomena are excluded or only partially covered, so the corpus is not universal for all possible reference relations.

## 7. Models and algorithm

### 7.1 Hybrid approach

The work compares:

- rule-based;
- statistical ML;
- transformer neural network;
- hybrid `rule + ML + neural`.

Reported table:

| Approach | MUC F1 | B³ F1 | CEAF-e F1 | CoNLL F1 |
|---|---:|---:|---:|---:|
| Rule-based | 48.5 | 52.1 | 50.0 | 50.2 |
| Statistical ML | 55.0 | 57.8 | 54.5 | 55.8 |
| Transformer NN | 61.2 | 63.0 | 59.7 | 61.3 |
| Hybrid rule+ML+NN | **64.0** | **66.5** | **62.3** | **64.3** |

Here “hybrid” means hybrid **coreference resolution**, not hybrid information retrieval.

### 7.2 Transformer comparison

The dissertation also compares:

| Model | MUC F1 | B³ F1 | CEAF-e F1 | CoNLL F1 |
|---|---:|---:|---:|---:|
| mBERT | 65.4 | 58.1 | 56.7 | 60.1 |
| XLM-RoBERTa | 68.9 | 62.3 | 61.0 | 64.1 |
| UzRoBERTa | **72.5** | **66.0** | **64.8** | **67.8** |

The model produces 768-dimensional token representations, extracts mention candidates, scores antecedent pairs and clusters references.

## 8. Result consistency caution

The source reports several close but not identical headline results:

- hybrid rule+ML+NN: **CoNLL F1 64.3**
- UzRoBERTa table: **CoNLL F1 67.8**
- practical-results prose: **CoNLL F1 70%**
- conclusion: RoBERTa model about **68% F1**

These values are not necessarily contradictory because they may refer to:
- different model families;
- rounded values;
- different system versions or evaluation stages.

But the supplied abstract does not fully reconcile them. Therefore preserve each number with its context rather than writing simply “UzCoref = 70%”.

## 9. UzCoref software

The system provides:

- web interface;
- command-line interface;
- REST API;
- file upload;
- JSON output;
- external-application integration.

This is a real implemented NLP system, not only a theoretical model.

## 10. Relation to search systems

This is the most important boundary for our project.

The dissertation reports that its results were used in:

1. a multilingual electronic platform for Uzbek literature, where the source says the search system and translation quality were optimized;
2. the IL-402104209 morpholexicon/morphological-analyzer project for information-retrieval systems;
3. semantic/contextual analysis applications.

However, the source does **not** report a controlled retrieval experiment showing:

- retrieval benchmark queries;
- qrels;
- BM25;
- dense retrieval;
- MAP/nDCG/Recall@k;
- before/after search effectiveness caused specifically by coreference;
- lexical/dense hybrid gain.

Therefore:

> “used in a search-related platform” is not the same as “proved retrieval effectiveness”.

## 11. Why this is not our retrieval task

### Abdisalomova task
Input:
`one text/document`

Output:
`which words/phrases refer to the same entity`

### Our task
Input:
`user query + large document collection`

Output:
`ranked relevant documents/passages`

So:

`coreference resolution != document retrieval`

Coreference may later help retrieval, but it is an auxiliary NLP feature, not a replacement for BM25 or dense retrieval.

## 12. What the work establishes

The work supports that:

- Uzbek contextual/discourse analysis is already computationally developed;
- a dedicated Uzbek coreference corpus exists;
- Uzbek-specific morphological and syntactic features are useful in a modern contextual NLP task;
- multilingual transformers and Uzbek-adapted RoBERTa have been evaluated for Uzbek coreference;
- a practical UzCoref system exists.

## 13. What the work does NOT establish

It does not prove:

- that coreference improves BM25;
- that coreference improves dense retrieval;
- that coreference improves hybrid search;
- that `raw/stem/lemma` affects coreference-based search;
- that morphology changes lexical–dense overlap;
- that a search engine using UzCoref has higher MAP/nDCG/Recall;
- that the current v0.8 retrieval gap is closed.

## 14. Relationship to CURRENT_GAP v0.8

**Status:** background/national semantic evidence; does not close the gap.

The current residual chain remains:

`raw/stem/lemma lexical representation`
→ `change in BM25 relevant set`
→ `change in overlap/unique hits with fixed dense retriever`
→ `change in incremental hybrid gain`
→ `relation to Uzbek query characteristics`.

Abdisalomova works on a different level:

`within-document reference resolution`.

Therefore no modification to `CURRENT_GAP v0.8` is required.

## 15. Practical importance for our National Library system

Potentially useful later:
- resolving pronouns and repeated entity references inside books/articles;
- improving snippets, entity linking, QA or document understanding;
- supporting semantic indexing.

But for a PhD-level project aimed at a fast, focused completion, this should **not** be added to the core retrieval method unless experiments later show a clear need.

It is more appropriate as:
- optional future enhancement;
- DSc/future research direction;
- auxiliary NLP service.

## 16. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| Coreference | Different expressions refer to the same thing | Linking mentions to the same referent/entity |
| Antecedent | Earlier expression that a later word refers to | Candidate referential source |
| Mention | A word/phrase referring to an entity | Span participating in a coreference chain |
| Coreference chain | All mentions of one entity | Cluster of mentions sharing a referent |
| CoNLL F1 | Standard combined coreference score | Average of MUC, B³ and CEAF-style metrics |
| RoBERTa | Transformer language model | Contextual encoder architecture |
| Hybrid coreference | Rules + ML + neural methods | Not lexical+dense retrieval fusion |

## 17. Open questions / verification needed

1. Verify final defense/protocol.
2. Obtain the final dissertation if available.
3. Reconcile CoNLL F1 64.3 / 67.8 / ~68 / 70% contexts.
4. Verify exactly which version of Uzbek RoBERTa was used and how it was adapted.
5. Verify whether the reported search-system optimization in the multilingual literature platform was measured quantitatively.
6. Determine public/research licensing and availability of the 1,020-document coreference corpus.
7. Do not add coreference to our core retrieval architecture unless a later experiment motivates it.

## 18. Decision after deep dive

- **Keep v0.8?** Yes.
- **Modify research gap?** No.
- **Add to national map?** Yes.
- **Role:** contextual/semantic Uzbek NLP evidence, not direct IR evidence.
- **Priority for current PhD method:** low/secondary.
- **Potential future role:** optional semantic enrichment for the final library search system, not required for the minimum PhD contribution.
