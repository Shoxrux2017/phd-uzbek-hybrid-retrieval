# Absalamova, Muminov & Absalamova — USHRA legal chatbot / hybrid semantic retrieval

**Deep-dive status:** COMPLETED AT VERIFIED-ABSTRACT LEVEL  
**Completed:** 2026-09-14  
**Suggested literature ID:** UZ-HYB-001  
**Reliability:** B  
**Priority for current PhD:** CRITICAL national hybrid/RAG boundary

## 1. Bibliographic record

- **Authors:** Diyora Absalamova, Bahodir Muminov, Gozal Absalamova
- **Title:** *Developing A Semantic Search-Based Chatbot For Legal Queries In Uzbek Language Using Big Data Resources*
- **Venue:** *Proceedings of the 9th International Conference on Future Networks and Distributed Systems (ICFNDS ’25)*
- **Publisher:** Association for Computing Machinery (ACM)
- **Publication year:** 2025
- **Pages:** 1036–1042
- **DOI:** 10.1145/3789692.3789825
- **Primary indexing evidence:** ACM DOI record referenced by J-GLOBAL / library catalogs
- **Full text status in this deep dive:** not recovered; ACM page returned access denial and ResearchGate exposes metadata only
- **Reliability:** **B** — verified ACM proceedings paper, but the current analysis is constrained to verified bibliographic metadata and abstract-level content

### Metadata caution

ResearchGate currently displays a May 2026 date, but independent bibliographic catalogs and the ICFNDS proceedings identify the publication as **2025**. For the project, use `2025` as the publication year and note that some databases surfaced/indexed the paper in 2026.

## 2. Why this work matters to our PhD

USHRA is critical because it closes the broad national claim:

> “Uzbek hybrid retrieval / hybrid RAG does not exist.”

The paper explicitly presents an algorithm called:

**Uzbek-Specific Hybrid Semantic Retrieval Algorithm (USHRA)**

for Uzbek legal question answering.

The verified abstract also states that the system uses:

- multilingual embeddings;
- semantic search;
- retrieval-augmented generation (RAG);
- a hybrid retrieval algorithm;
- the national legal-information portal `Lex.uz`.

Therefore hybrid/semantic retrieval is already part of published Uzbek legal-AI research.

However, the verified public evidence does **not** establish our current `v0.8` interaction question.

## 3. Scientific problem

### Simple explanation

A user asks a legal question in Uzbek.

Traditional keyword search can fail when:
- the user does not know the exact legal wording;
- the query and law use different expressions;
- Uzbek morphology changes surface word forms.

The proposed chatbot attempts to retrieve semantically appropriate legal information and then generate an answer grounded in retrieved legal material.

### Formal task

At verified abstract level:

`Uzbek legal query`
→ `semantic/hybrid retrieval over legal data`
→ `retrieved legal context`
→ `RAG answer`.

The main source is `Lex.uz`, described as containing laws, decrees and court/legal materials.

## 4. Main idea

The paper combines three broad components:

1. **multilingual semantic embeddings**;
2. **USHRA hybrid retrieval**;
3. **retrieval-augmented generation**.

This is enough to establish that published Uzbek research already integrates retrieval and semantic representation in a hybrid/RAG pipeline.

### Critical evidence boundary

The accessible abstract does **not** specify enough detail to determine safely:

- whether the lexical component is BM25, TF-IDF or another keyword mechanism;
- whether the hybrid algorithm is score fusion, rank fusion, routing, filtering or another strategy;
- which embedding model is used;
- whether FAISS/Milvus/Elasticsearch or another index is used;
- the exact top-k protocol;
- the exact normalization/fusion formula.

These details must remain **unknown** until the full ACM paper is inspected.

## 5. Data source

Verified:
- principal source: `Lex.uz`, Uzbekistan’s national legal-information portal;
- the abstract mentions laws, decrees and court decisions/legal records;
- evaluation uses **200 criminal-law queries**.

Not verified from accessible evidence:
- total number of legal documents;
- total number of passages/chunks;
- chunking unit;
- corpus date/version;
- train/dev/test partition;
- whether all 200 queries are independent held-out test queries.

## 6. Evaluation

The verified abstract reports:

- **200 criminal-law queries**
- chatbot answer accuracy: **85%**

This is the paper’s most visible numerical result.

### Very important distinction

`85% chatbot answer accuracy != 85% retrieval accuracy`

The observed answer depends on several stages:

`retrieval`
+
`context construction`
+
`LLM/generator`
+
`prompting`
+
`answer evaluation`.

Therefore the 85% result cannot be used as:
- Precision@k;
- Recall@k;
- MAP;
- nDCG;
- MRR;
- retrieval hit rate

unless the full paper explicitly defines it that way.

The abstract describes it as accuracy of the **chatbot in answering user questions**.

## 7. Baselines

The accessible abstract contrasts the proposed semantic understanding with “traditional keyword search”.

However, the current verified evidence is insufficient to identify a controlled baseline table with:

- BM25;
- TF-IDF;
- keyword search;
- dense-only retrieval;
- hybrid retrieval;
- RAG variants

and their exact retrieval metrics.

Therefore the project must not write:

> “USHRA significantly outperforms BM25”

or any similar claim without the full paper.

## 8. Retrieval metrics

At the current evidence level, standard pure-IR metrics are **not verified**.

Not recovered:
- Precision@k;
- Recall@k;
- MAP;
- MRR;
- nDCG;
- Hit Rate for retrieval;
- qrels-based evaluation.

The only verified headline measure is 85% answer accuracy over 200 criminal-law queries.

## 9. Statistical evidence

No verified statistical significance test was recovered from the accessible abstract-level evidence.

Do not assume:
- confidence intervals;
- paired tests;
- bootstrap;
- repeated runs

without the full paper.

## 10. What USHRA establishes

Safe conclusions:

1. A published ACM proceedings paper exists on Uzbek legal semantic/hybrid retrieval.
2. The authors explicitly name a hybrid algorithm `USHRA`.
3. Multilingual embeddings and RAG are part of the approach.
4. `Lex.uz` is used as the main legal information source.
5. The prototype is evaluated on 200 criminal-law queries.
6. The authors report 85% answer accuracy.
7. Therefore **Uzbek hybrid/RAG research already exists**.

## 11. What USHRA does NOT establish at current evidence level

It does not currently establish for our project:

- exact BM25 use;
- exact lexical model;
- exact dense embedding model;
- exact hybrid fusion rule;
- controlled lexical-vs-dense-vs-hybrid IR metrics;
- raw/stem/lemma comparison;
- explicit morphological preprocessing;
- morphology-conditioned lexical–semantic overlap;
- unique relevant hits;
- oracle union;
- incremental hybrid gain;
- per-query complementarity decomposition.

## 12. Why this is not yet enough to close v0.8

USHRA answers a broad engineering question:

> Can an Uzbek legal chatbot use semantic/hybrid retrieval and RAG?

Our current PhD asks a narrower explanatory question:

> If we alter only the morphological representation of the Uzbek lexical channel (`raw/stem/lemma`) while keeping the semantic retriever fixed, how does the structure of lexical–semantic complementarity change?

These are different levels of analysis.

USHRA does not provide verified evidence for:

`BM25_raw`
`BM25_stem`
`BM25_lemma`

with the same `D`, nor for:

`unique lexical`
`unique dense`
`intersection`
`oracle union`
`incremental hybrid gain`.

Therefore `CURRENT_GAP v0.8` remains open.

## 13. Important IR vs RAG distinction

### Pure retrieval question

> Did the system retrieve the relevant legal articles/passages?

This requires retrieval judgments and metrics.

### RAG/QA question

> Did the chatbot ultimately answer the user correctly?

A chatbot can:
- retrieve a partially relevant passage and still generate a correct answer;
- retrieve the correct passage but generate a wrong answer;
- mix information incorrectly.

Therefore answer accuracy cannot be treated as direct evidence about the retriever.

This distinction is especially important when comparing USHRA with our future National Library search engine, where retrieval itself is the primary object.

## 14. Relationship to Ishkobilov

The national evidence now separates clearly:

### Ishkobilov et al.
- actual ranked paragraph retrieval;
- TF-IDF vs FastText;
- standard IR metrics.

### USHRA
- hybrid/semantic RAG chatbot;
- multilingual embeddings;
- Lex.uz;
- 200 legal queries;
- answer-level accuracy.

Thus:
- Ishkobilov is stronger evidence for **pure retrieval evaluation**;
- USHRA is stronger evidence that **Uzbek hybrid/RAG architecture already exists**.

Neither closes the morphology × complementarity interaction of v0.8.

## 15. Relationship to CURRENT_GAP v0.8

**Status:** kills broad “no Uzbek hybrid retrieval” claim; does not alter the residual gap.

Current residual chain remains:

`raw/stem/lemma lexical representation`
→ `change in BM25 relevant set`
→ `change in overlap/unique hits with fixed dense retriever`
→ `change in incremental hybrid gain`
→ `relation to Uzbek query characteristics`.

No change to `CURRENT_GAP.md` is required.

## 16. Implications for our PhD design

1. We must **not** present `BM25 + semantic + RAG` itself as novelty.
2. We should evaluate retrieval separately from any future chatbot/generation layer.
3. The PhD core can remain simpler than USHRA:
   - lexical retrieval;
   - dense retrieval;
   - simple controlled fusion;
   - qrels-based analysis.
4. A chatbot can be added to the final software later, but it is not necessary for proving the PhD retrieval contribution.
5. For National Library deployment, our first practical milestone should be a reliable ranked search engine; RAG can remain a later layer.

## 17. Open questions requiring the full ACM paper

Before making stronger claims, verify:

1. exact definition of USHRA;
2. lexical component, if any;
3. exact embedding model;
4. retrieval index/database;
5. preprocessing / Uzbek normalization;
6. whether stemming/lemmatization is used;
7. chunking and top-k;
8. fusion/routing formula;
9. detailed baseline table;
10. definition of “85% accuracy”;
11. who judged answer correctness;
12. qrels/retrieval metrics, if any;
13. statistical significance;
14. corpus size and exact Lex.uz subset.

## 18. Decision after deep dive

- **Keep CURRENT_GAP v0.8:** yes.
- **Modify GAP_HISTORY / DECISIONS:** no.
- **National role:** CRITICAL proof that Uzbek hybrid/RAG exists.
- **Reliability:** B, ACM publication verified, but methods remain abstract-level until full text is recovered.
- **Use in Chapter I:** yes, especially section 1.3, with explicit `RAG answer accuracy != retrieval effectiveness` caution.
