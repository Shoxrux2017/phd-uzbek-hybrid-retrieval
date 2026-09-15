# Sheng-Chieh Lin (2024) — Building a Robust Retrieval System with Dense Retrieval Models

**Targeted deep-dive status:** COMPLETED  
**Completed:** 2026-09-15  
**Literature ID:** PHD-INT-001  
**Project role:** main international PhD structural/reference anchor for dense retrieval robustness and lexical–semantic integration  
**Reliability:** A — officially defended PhD, University of Waterloo

## 1. Bibliographic record

Sheng-Chieh Lin.  
**Building a Robust Retrieval System with Dense Retrieval Models.**  
Doctor of Philosophy in Computer Science, David R. Cheriton School of Computer Science, University of Waterloo, Canada, 2024.  
Supervisor: Jimmy Lin.  
Defense: 2024-12-02.  
Repository record date: 2024-12-17.  
Persistent handle: `https://hdl.handle.net/10012/21253`.

The University of Waterloo repository, official defense announcement and convocation record independently establish the dissertation and degree.

## 2. Why this dissertation matters to the current PhD

This dissertation is one of the closest structural references for the Uzbek hybrid-retrieval PhD because it is not simply a dissertation about “using BERT for search”.

Its central scientific logic is:

`strong lexical baseline`
→ `dense retrieval addresses term mismatch`
→ `dense retrieval has robustness/training limitations`
→ `hybrid/multi-vector systems recover lexical + semantic evidence but increase system complexity`
→ `develop methods that improve robustness and efficiency`.

This is useful for the current Uzbek project because our argument should follow the same evidence-driven principle:

`Uzbek morphology changes lexical representation`
→ `lexical and semantic retrieval are already established`
→ `the unresolved issue is their morphology-conditioned complementarity`
→ `experiment first`
→ `only then choose a method`.

The dissertation therefore supports the project's existing rule:
**gap first, method second**.

## 3. Central problem of the dissertation

The dissertation focuses on **first-stage retrieval**: retrieving a relatively small candidate set from a very large corpus before downstream reranking, QA, fact checking, or RAG.

It starts from three observations.

### 3.1 BM25 remains important

Lexical retrieval such as BM25 is:
- simple;
- efficient;
- training-free;
- robust across many domains/tasks.

### 3.2 Dense retrieval solves part of vocabulary mismatch

Dense retrievers allow a query and a relevant document to match even when they do not share the same exact terms.

### 3.3 Dense retrieval is not universally robust

Dense retrievers:
- require relevance labels and substantial compute;
- can generalize poorly to unseen domains/tasks/languages;
- can still lag behind BM25 in robustness;
- are often outperformed by hybrid or multi-vector systems that retain more lexical/fine-grained evidence.

But hybrid and multi-vector systems may require:
- more storage;
- more query latency;
- multiple indexes;
- more complex retrieval pipelines.

The dissertation therefore seeks **robust yet efficient first-stage retrieval**.

## 4. Two high-level contribution directions

The official dissertation abstract organizes the work into two broad directions.

### Direction A — improve dense retrieval training efficiently

Key lines:
- TCT-ColBERT;
- DRAGON.

### Direction B — improve representation and lexical–semantic integration efficiently

Key lines:
- DHR / Dense Representation Framework;
- Aggretriever;
- mAggretriever.

This is an important structural lesson: the dissertation has one overarching problem, while individual chapters/papers attack different bottlenecks.

## 5. TCT-ColBERT — efficient knowledge distillation

### Problem

ColBERT preserves token-level interactions and uses a fine-grained `MaxSim` matching function, but multi-vector retrieval is more expensive than a single-vector dense retriever.

### Idea

Use ColBERT as a **teacher** and train a student dense retriever whose final relevance score is only a simple dot product.

In simple terms:

`expensive fine-grained teacher`
→ teaches →
`cheap single-vector student`.

The dissertation calls this **TCT-ColBERT**.

### Important mechanism

The teacher and student are “tightly coupled”, allowing efficient in-batch negatives during distillation.

The goal is to transfer ColBERT's fine-grained ranking knowledge while retaining one-step approximate nearest-neighbor retrieval.

### Verified supporting result

The public Castorini reproduction reports approximately:

- TCT-ColBERT dense retrieval MS MARCO Dev MRR@10: `0.335`;
- TCT-ColBERT + bag-of-words BM25: MRR@10 about `0.353`.

### Relevance to current PhD

TCT-ColBERT reinforces that:
- dense quality depends strongly on training;
- hybrid gains are not automatically attributable to “semantic meaning” alone;
- the chosen fixed dense comparator `D` must be a serious retrieval-trained model, not merely a generic sentence embedding model.

It does **not** address morphology-induced complementarity.

## 6. DRAGON — robustness through diverse augmentation

Full paper:
**How to Train Your Dragon: Diverse Augmentation Towards Generalizable Dense Retrieval**, Findings of EMNLP 2023.

### Problem

Dense retrievers often show a tradeoff:

`high in-domain effectiveness`
vs
`good zero-shot/generalization`.

One explanation in earlier work was insufficient model capacity.

### Main finding

Lin et al. argue that **data diversity**, especially diversity in both:
- query generation/selection;
- relevance supervision/labels,

is a critical factor.

### DRAGON

DRAGON = **Dense Retriever trained with diverse AuGmentatiON**.

The authors progressively train with supervision from multiple teacher/retrieval signals.

The resulting model uses a BERT-base-sized backbone of roughly **110M parameters**.

The dissertation highlights that DRAGON can compete with:
- much larger GTR-XXL (~4.8B parameters, ~40× larger);
- strong multi-vector/learned-sparse systems;

in supervised and zero-shot retrieval.

Crucially, the augmentation is generated using the **8.8M MS MARCO passages** rather than requiring billion-scale additional web crawling.

### Scientific lesson

Robustness is not simply:

`larger model = better transfer`.

Training-data/query/label diversity can matter strongly.

### Relevance to Uzbek

This is highly relevant to selection of `D`.

A dense retriever that performs well on English/MS MARCO may not necessarily be a strong Uzbek retriever.

Therefore the Uzbek experiment should not select `D` only because a model is popular or strong on BEIR.

A preliminary Uzbek validation/pilot is needed before freezing `D`.

## 7. DHR — unified lexical–semantic representation

This dissertation contains the work already analyzed separately as:

**A Dense Representation Framework for Lexical and Semantic Matching**.

Core contribution:
- Dense Lexical Representation (DLR);
- Gated Inner Product (GIP);
- Dense Hybrid Representation (DHR);
- unified vector retrieval for lexical + semantic matching.

The key conceptual result for the current project is:

`dense representation ≠ necessarily semantic matching`.

A lexical signal can be numerically represented densely.

Therefore the main Uzbek comparator should be described precisely as:

> **a fixed retrieval-trained semantic dense retriever**

rather than simply “a dense model”.

DHR itself does not test `raw/stem/lemma × same semantic D`.

## 8. Aggretriever — combining semantic and lexical features inside one dense vector

Full paper:
**Aggretriever: A Simple Approach to Aggregate Textual Representations for Robust Dense Passage Retrieval**, TACL 2023.

### Problem

Standard dense retrievers commonly rely on:
- `[CLS]`;
- average pooling.

The dissertation argues that pretrained language models contain additional lexical information in their masked-language-modeling machinery that ordinary dense pooling underuses.

### Main idea

Aggretriever combines:

1. semantic information from `[CLS]`;
2. aggregated lexical/MLM-derived token information (`agg*`);

into one fixed-length dense vector.

Thus it remains a dense retriever at inference time while internally incorporating a stronger lexical component.

### Representative results

Using MS MARCO fine-tuning:

- DistilBERT `[CLS]`: MS MARCO RR@10 `0.308`;
- DistilBERT Aggretriever: `0.341`.

On BEIR zero-shot average nDCG@10:

- BM25: `0.430`;
- DistilBERT `[CLS]` fine-tuned on MS MARCO: `0.364`;
- DistilBERT Aggretriever: `0.450`.

Comparable gains occur with BERT/Condenser/coCondenser backbones.

### Important ablation

The TACL paper shows that `[CLS]` and `agg*` encode different useful information.

For one dimensionality experiment:

- `[CLS]` alone: BEIR-small nDCG@10 about `0.259`;
- `agg*` alone: about `0.328`;
- combined `[CLS]+agg*`: about `0.358`.

This supports a recurring theme of the dissertation:

> robust retrieval often benefits from preserving both semantic and lexical information.

### Relevance to v0.8

Aggretriever shows that lexical evidence can be embedded inside a dense retriever itself.

Therefore a “dense” comparator may not be semantically pure in a philosophical sense.

For causal clarity, the Uzbek project only requires that the **same frozen comparator** be used in every morphology condition.

## 9. mAggretriever — multilingual zero-shot retrieval

Full paper:
**mAggretriever: A Simple yet Effective Approach to Zero-Shot Multilingual Dense Retrieval**, EMNLP 2023.

### Main problem

Multilingual retrieval labels are expensive to create for every language.

The question is whether a model can be trained primarily on English relevance data and transfer effectively to other languages.

### Method

mAggretriever extends Aggretriever using multilingual pretrained backbones such as:
- mBERT;
- XLM-R.

It again combines semantic `[CLS]` features with lexical/MLM-derived information.

Approximate MLM prediction is introduced to reduce training memory.

The paper reports roughly **70–85% GPU-memory reduction** for this lexical-feature computation.

### Evaluation

The model is evaluated zero-shot on multilingual retrieval benchmarks including:
- MIRACL;
- Mr. TyDi.

In MIRACL, the reported XLM-R Aggretriever variants achieve average nDCG@10 of approximately **52.9–53.3** over the evaluated non-English languages, while the paper reports strong transfer despite fine-tuning only on English retrieval data.

On Mr. TyDi, the authors report that mAggretriever variants outperform previous state of the art in **6 of 10 languages**.

### Critical Uzbek limitation

Uzbek is **not** one of the reported MIRACL/Mr. TyDi evaluation languages.

Therefore this dissertation cannot establish that mAggretriever is effective for Uzbek.

It establishes a transfer principle, not Uzbek retrieval effectiveness.

## 10. The dissertation's main scientific chain

The work can be understood as:

`BM25 is robust but lexical`
→
`dense retrieval solves vocabulary mismatch`
→
`dense retrieval needs better training`
→
`TCT-ColBERT: efficient distillation`
→
`DRAGON: robust training via diverse augmentation`
→
`pure dense representations still lose useful lexical information`
→
`Aggretriever: inject lexical + semantic information into one dense vector`
→
`mAggretriever: transfer this idea across languages`
→
`DHR: unify lexical and semantic retrieval/indexing efficiently`.

This chain is more important for our structural learning than any individual score.

## 11. Why this is a useful structural PhD reference

The dissertation does **not** start with:

> “I want to invent model X.”

Instead it builds a sequence:

1. identify a strong established baseline;
2. identify a specific limitation;
3. test why existing solutions are insufficient;
4. propose a method targeted at that limitation;
5. evaluate in-domain;
6. evaluate robustness/zero-shot transfer;
7. evaluate efficiency;
8. analyze component behavior;
9. refine the next research problem.

This is exactly the type of logic the Uzbek PhD should emulate.

But our dissertation should remain narrower.

Lin's PhD contains several mature research lines and multiple top-tier publications. The Uzbek PhD does **not** need to reproduce that breadth.

## 12. Datasets and evaluation philosophy

Across the dissertation's technical lines, the main evaluation ecosystem includes:

- MS MARCO passage retrieval;
- TREC Deep Learning;
- BEIR zero-shot/domain-transfer datasets;
- Natural Questions / TriviaQA in Aggretriever experiments;
- MIRACL;
- Mr. TyDi;
- multilingual/domain-transfer evaluations.

This reveals a major methodological principle:

> a retriever should not be judged only on one in-domain aggregate score.

Robustness across:
- domains;
- tasks;
- languages;

is a central object of evaluation.

## 13. Critical consequence for the Uzbek dense baseline

This dissertation introduces an important risk for the current v0.8 experiment.

Suppose the chosen semantic dense model performs poorly on Uzbek.

Then we may observe:

- many BM25-only relevant hits;
- low overlap;
- apparent “complementarity”;
- large potential hybrid headroom.

But this may simply mean:

> `D` is a bad Uzbek retriever.

That would weaken the scientific interpretation.

Therefore the dense-baseline protocol should have a **pre-experiment validation gate**:

1. choose a small set of modern retrieval-trained multilingual candidates;
2. validate their Uzbek retrieval effectiveness on a development/pilot split;
3. select the primary `D` using a predefined rule;
4. freeze `D`;
5. only then run the main `raw/stem/lemma` causal experiment on held-out test queries.

Candidate family can include, for example:
- BGE-M3 Dense;
- multilingual E5;
- another justified modern multilingual retriever if evidence supports it.

The choice itself must not be tuned separately for `raw`, `stem`, and `lemma`.

## 14. Why BM25 still remains valid in our experiment

The dissertation explicitly treats BM25 as a serious robust first-stage baseline rather than an obsolete method.

This is valuable for our PhD because BM25's role is not:

> “old algorithm used only for comparison.”

Its role is:

> a strong lexical reference whose strengths and failures can be compared causally with a fixed semantic retriever.

That directly supports the existing project decision to retain BM25 as the primary lexical baseline.

## 15. What this dissertation already closes for novelty

The current Uzbek PhD must not claim novelty from:

- using dense retrieval to solve vocabulary mismatch;
- efficient dense retrieval knowledge distillation;
- diverse augmentation for robust dense retrieval;
- incorporating lexical information into a single dense vector;
- multilingual zero-shot dense transfer;
- unified dense representation of lexical + semantic signals;
- dense–sparse fusion as a general robustness mechanism;
- using one vector index to simplify hybrid retrieval.

All are represented by this dissertation or its component publications.

## 16. What the dissertation does NOT establish

It does not establish:

1. Uzbek retrieval effectiveness;
2. raw/stem/lemma effects for Uzbek BM25;
3. morphology-induced change in a lexical relevant set;
4. `BM25_raw/stem/lemma` against the same frozen semantic dense retriever;
5. morphology-conditioned unique lexical hits;
6. morphology-conditioned unique dense hits;
7. morphology-conditioned overlap/intersection;
8. morphology-conditioned oracle union;
9. morphology-conditioned incremental hybrid gain;
10. relationships between these changes and interpretable Uzbek query morphology/script features.

## 17. Does it kill `v0.8 refined`?

**No.**

It strongly closes generic directions around:
- dense robustness;
- lexical–semantic fusion;
- dense/sparse representation integration;
- multilingual dense transfer.

But it does not conduct the causal intervention central to `v0.8`:

`change Uzbek lexical morphology`
→
`change lexical relevant set`
→
`change overlap/unique hits against SAME D`
→
`change incremental hybrid gain`.

Therefore the residual gap survives.

## 18. Impact on provisional RQ1–RQ3

### RQ1

No change.

The dissertation does not study `raw/stem/lemma` lexical retrieval.

### RQ2

No conceptual change, but a methodological guard is strengthened:

the fixed semantic comparator must first be shown to be **credible for Uzbek**.

Otherwise complementarity can be confounded with a weak dense baseline.

### RQ3

No change.

The dissertation analyzes robustness across datasets/languages, but does not test interpretable morphology-induced Uzbek query features.

## 19. Strongest lesson for our dissertation design

The most useful lesson is not “use DRAGON” or “use Aggretriever”.

It is:

> **Do not confuse a strong model with a scientifically controlled experiment.**

Lin's dissertation evaluates robustness explicitly because model behavior changes by domain/task/language.

For the Uzbek morphology–complementarity question, the same principle means:

- validate `D`;
- then freeze `D`;
- change only the lexical morphology representation;
- use held-out qrels;
- analyze both average effectiveness and query-level set decomposition.

## 20. Potential use in Chapter I

This dissertation is a strong structural and conceptual source for statements such as:

- BM25 remains a robust first-stage lexical retriever;
- dense retrieval addresses vocabulary mismatch;
- dense retrieval requires more training resources and may be less robust across domains/tasks/languages;
- hybrid and multi-vector models can preserve complementary lexical and semantic evidence but introduce efficiency/complexity costs;
- robustness and efficiency are central evaluation dimensions in modern first-stage retrieval.

For detailed model-specific claims, cite the corresponding primary publications (TCT-ColBERT, DRAGON, DHR, Aggretriever, mAggretriever) where possible.

## 21. Final decision

**Role:** main international structural PhD anchor.  
**Gap-killer risk for broad hybrid/dense novelty:** VERY HIGH.  
**Gap-killer risk for `v0.8`:** LOW.  
**Current gap version:** no change required.  
**New experimental implication:** add a pre-experiment Uzbek credibility/validation gate for candidate dense retrievers before freezing the main comparator `D`.  
**Structural implication:** use `problem → evidence of limitation → controlled experiment → method only if justified` as the design logic for the Uzbek dissertation.  
**Scope implication:** do not imitate the breadth of Lin's multiple-model dissertation; the current Uzbek PhD should keep one narrow causal question and one defensible implementation path.
