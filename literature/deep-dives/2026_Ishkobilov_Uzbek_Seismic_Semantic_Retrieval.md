# Ishkobilov et al. (2026) — Semantic Retrieval of Uzbek Seismic Safety Regulations

**Deep-dive status:** COMPLETED  
**Completed:** 2026-09-14  
**Suggested literature ID:** UZ-IR-001  
**Reliability:** B  
**Priority for current PhD:** CRITICAL national semantic-retrieval boundary

## 1. Bibliographic record

- **Authors:** Farrukh Ishkobilov, Abdulatif Meyliev, Mironshoh Ortikov, Javlon Ibragimov, Umida Turaeva, Elmurod Jumaev
- **Title:** *Semantic Retrieval of Uzbek Seismic Safety Regulations*
- **Venue:** *Vibroengineering Procedia*, Vol. 63
- **Year:** 2026
- **Pages:** 227–231
- **Publication date:** 2026-07-16
- **Publication context:** Volume 63 of *Vibroengineering Procedia*, associated with the 77th International Conference on VIBROENGINEERING (Almaty, 11–12 June 2026)
- **Publisher evidence:** Extrica/JVE International; venue states volume-level peer review and is indexed in Scopus and other databases
- **Reliability:** **B** — verified peer-reviewed proceedings article, but not a core IR venue and the accessible public record is short
- **Current project record before this deep dive:** `UZ-IR-001`, priority `CRITICAL`, reliability `B/A-`

## 2. Why this work is important for our PhD

This paper is one of the clearest national sources proving that **real corpus-level semantic retrieval for Uzbek already exists**.

Unlike Uzbek work that only evaluates:
- word similarity,
- sentence similarity,
- paraphrase detection,
- sentiment,
- BERT language modeling,

this paper performs an actual retrieval experiment:

`query -> ranked paragraphs from a corpus`

and evaluates the ranking with standard information-retrieval metrics.

Therefore our dissertation must **not** claim:

> “Uzbek semantic retrieval has not been evaluated.”

That broad gap is closed.

However, the paper does not investigate our current residual question:
- no BM25;
- no raw/stem/lemma intervention;
- no lexical+dense fusion;
- no complementarity decomposition.

## 3. Scientific problem

### Simple explanation

Uzbek technical regulations contain many inflected and derived forms. A purely word-matching method may miss relevant passages when the query and the document use different surface forms or semantically related terms.

The study asks whether a representation that uses **subword information** can retrieve relevant Uzbek regulatory paragraphs better than a classical lexical-frequency baseline.

### Formal formulation

The paper compares:
- **TF-IDF** — lexical/statistical vector-space retrieval;
- **FastText-based semantic retrieval** — subword-aware distributed representation.

Retrieval is performed at paragraph level over Uzbek seismic-safety / engineering documentation.

## 4. Main idea

### TF-IDF channel

TF-IDF rewards paragraphs containing important words that also occur in the query.

Strength:
- simple;
- interpretable;
- strong for direct word overlap.

Weakness:
- surface-form mismatch;
- suffixation can fragment lexical evidence.

### FastText channel

FastText represents words using both word and character-subword information.

Simple meaning:

> even when two Uzbek word forms are not identical, shared subword structure can give them more similar representations.

This is useful for an agglutinative language such as Uzbek.

Important terminology:

> FastText embeddings are **semantic/subword representations**, but this setup is not the same as a modern retrieval-trained Transformer bi-encoder such as multilingual E5/BGE-M3-style dense retrieval.

## 5. Retrieval architecture

At the verified level, the experiment is approximately:

`Uzbek seismic / engineering documents`
→ paragraph segmentation
→ paragraph index
→ user/domain query
→ retrieval with either TF-IDF **or** FastText
→ ranked paragraphs
→ top-k evaluation.

Critical distinction:

> The two models are **compared**. The accessible evidence does not show that TF-IDF and FastText scores are fused into one hybrid ranker.

Therefore this paper is **semantic-vs-lexical comparison**, not hybrid retrieval.

## 6. Corpus and queries

The current project record reports:

- **120 documents**
- **8,450 indexed paragraphs**
- **100 domain-specific queries**

The publisher abstract independently confirms:
- a specialized seismic-safety / engineering corpus;
- paragraph-level segmentation;
- **100 domain-specific queries**.

### Relevance-judgment caution

The accessible publisher abstract does not explain in enough detail:
- who created the queries;
- who judged relevance;
- whether judgments were binary or graded;
- how many relevant paragraphs existed per query;
- whether pooling was used;
- inter-annotator agreement.

These details must be verified from the full paper before using the benchmark as a model for our own qrels protocol.

## 7. Baselines

The paper compares only two principal retrieval representations:

1. **TF-IDF**
2. **FastText**

Important for our PhD:

- **BM25 is absent**;
- no modern retrieval-trained Transformer dense model is included;
- no learned sparse model is included;
- no hybrid fusion baseline is included.

Thus FastText beating TF-IDF does **not** imply FastText would beat BM25 or a modern dense retriever.

## 8. Metrics

### Precision@5

Simple meaning:

> Among the first five retrieved paragraphs, what fraction are relevant?

### Recall@5

Simple meaning:

> Of the relevant material that should be found, how much is already found in the first five results?

### MAP — Mean Average Precision

Measures how well relevant items are ranked across the whole ranked list, averaged over queries. It rewards systems that place relevant material early and repeatedly.

### MRR — Mean Reciprocal Rank

Focuses strongly on the position of the **first relevant result**. If the first relevant result appears very early, MRR is high.

### F1

The project `RESEARCH_MAP` currently records F1 among the reported metrics. The public publisher abstract explicitly lists Precision@5, Recall@5, MAP and MRR. Exact F1 use/value should be checked against the full paper before citation.

## 9. Main numerical results

Verified from the publisher abstract:

| Model | Precision@5 | Recall@5 |
|---|---:|---:|
| TF-IDF | 0.6017 | 0.5418 |
| **FastText** | **0.7444** | **0.6875** |

The publisher abstract states that FastText also outperformed TF-IDF on the other major reported metrics, including MAP and MRR.

### Important caution

Exact MAP and MRR values were not recovered from the accessible publisher abstract during this deep dive. They should **not be invented or reconstructed**.

## 10. Statistical evidence

The paper reports a paired t-test:

- **t = 15.1372**
- **p < 0.001**

Thus the authors report the observed improvement as statistically significant.

### Caution

From the accessible abstract alone it is not clear:
- exactly which per-query effectiveness quantity was entered into the t-test;
- whether distributional assumptions were checked;
- whether multiple metrics were tested separately;
- whether any correction for multiple testing was applied.

These details require the full paper.

## 11. Strengths

1. **Actual information retrieval**, not merely semantic similarity.
2. **Uzbek corpus-level ranking task**.
3. **Standard IR metrics**, including P@5, R@5, MAP and MRR.
4. **Statistical significance test** is reported.
5. **Paragraph-level retrieval**, which is practically relevant for long technical documents.
6. **Morphologically aware motivation**: FastText subwords are a sensible representation for Uzbek surface variation.

## 12. Limitations

### Dataset / domain

- narrow seismic-safety / engineering domain;
- current project record: 120 documents and 8,450 paragraphs;
- 100 queries is useful but still modest for detailed query-subgroup analysis;
- unknown qrels construction details from the accessible abstract.

### Retrieval models

- TF-IDF is a weaker lexical comparator than the BM25 baseline planned for our PhD;
- FastText is a static/subword embedding approach, not a modern retrieval-trained contextual dense retriever;
- no BM25;
- no contextual bi-encoder;
- no cross-encoder/reranking analysis.

### Morphology

- morphology is part of the motivation;
- FastText subwords implicitly address some surface variation;
- but there is no controlled:
  - raw;
  - stem;
  - lemma
  intervention.

### Hybrid/complementarity

No:
- TF-IDF + FastText fusion;
- BM25 + dense fusion;
- unique relevant hits;
- overlap/intersection;
- oracle union;
- incremental hybrid gain;
- query-level complementarity analysis.

## 13. What this work actually proves

The study supports the following restricted claim:

> In the authors' Uzbek seismic-safety paragraph-retrieval benchmark, the FastText-based subword representation outperformed the tested TF-IDF baseline on the reported retrieval metrics, with a statistically significant overall difference reported by the authors.

It also establishes that:

- Uzbek corpus-level semantic retrieval is already a real national research line;
- standard IR evaluation has already been applied to an Uzbek retrieval task;
- semantic/subword representations can be useful in a morphologically rich Uzbek domain.

## 14. What this work does NOT prove

It does **not** prove that:

- semantic retrieval is always better than lexical retrieval for Uzbek;
- FastText is better than BM25;
- FastText is better than multilingual E5/BGE-M3/modern dense retrievers;
- morphology-aware preprocessing is unnecessary;
- stemming or lemmatization harms/helps FastText;
- hybrid retrieval improves over both channels;
- lexical and semantic retrieval are complementary in this benchmark;
- the result generalizes from seismic regulations to National Library books, journals and general-domain texts.

## 15. Relationship to Bakaev / Xusainova

National evidence now forms a clear progression.

### Bakaev / Xusainova

They establish:

`Uzbek morphology`
→ tokenization/stemming/lemmatization
→ search/corpus processing.

### Ishkobilov et al.

They establish:

`Uzbek corpus`
+ `queries`
→ lexical baseline vs semantic/subword retrieval
→ standard IR metrics.

Together they close two broad gaps:

1. morphology-aware Uzbek search is not absent;
2. Uzbek semantic retrieval evaluation is not absent.

But they still do not answer our interaction question.

## 16. Relationship to CURRENT_GAP v0.8

**Status:** strongly supports the current narrowing; does not close v0.8.

Ishkobilov et al. removes any remaining claim:

> “There is no real Uzbek semantic retrieval benchmark.”

But the paper does not test:

`BM25_raw`
`BM25_stem`
`BM25_lemma`

against the same fixed semantic retriever `D`, nor:

`BM25_raw + D`
`BM25_stem + D`
`BM25_lemma + D`.

It also does not measure:
- lexical-only relevant hits;
- semantic-only relevant hits;
- intersection;
- oracle union;
- morphology-induced change in hybrid gain.

Therefore `CURRENT_GAP v0.8` remains unchanged.

## 17. Implications for our experimental design

1. **Use a stronger lexical baseline than TF-IDF.**
   - BM25 remains appropriate.

2. **Use a modern retrieval-trained semantic comparator.**
   - FastText is useful historical/national evidence, but insufficient as the final state-of-the-art dense comparator.

3. **Paragraph-level indexing is worth considering for the National Library.**
   - Books and journals are long documents; passage/paragraph retrieval can return precise evidence.
   - A later document-level aggregation layer can map passages back to books/articles.

4. **Do not claim that embeddings automatically solve Uzbek morphology.**
   - FastText handles subword variation, but this paper does not compare that behavior against explicit stemming/lemmatization.

5. **Our qrels protocol should be more explicit.**
   - query source;
   - assessor count;
   - relevance scale;
   - pooling;
   - adjudication;
   - inter-annotator agreement;
   - train/validation/test separation if tuning is performed.

## 18. Importance for the future National Library search system

This paper gives a practical design lesson:

> retrieving paragraphs/passages can be more useful than ranking whole long books only.

For a National Library deployment, a reasonable engineering design could be:

`book/journal`
→ paragraph or passage segmentation
→ lexical + semantic passage retrieval
→ merge/aggregate results by source document
→ show the user the relevant fragment and the parent book/article.

This is an **engineering implication**, not a result directly proven by Ishkobilov et al. for the National Library.

## 19. Open questions

Before citing the paper in detail, recover/check the full 5-page article for:

1. exact corpus composition and source documents;
2. exact 120-document / 8,450-paragraph counts;
3. query-generation procedure;
4. qrels/relevance-judgment procedure;
5. exact FastText checkpoint/training corpus;
6. exact paragraph-vector construction;
7. exact similarity function;
8. preprocessing/tokenization;
9. exact MAP/MRR/F1 values;
10. exact quantity used for the paired t-test.

## 20. Decision after deep dive

- **Keep CURRENT_GAP v0.8:** yes.
- **Change gap/history/decisions:** no.
- **National role:** CRITICAL proof that Uzbek corpus-level semantic retrieval with standard IR metrics exists.
- **Use as semantic baseline in our experiment:** no, not as the only/primary modern comparator.
- **Use in Chapter I:** yes, strongly in section 1.2 and in the national boundary synthesis.
