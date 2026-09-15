# Turayev B.Sh. — Neural/hybrid morphological and syntactic analysis of Uzbek

**Deep-dive status:** COMPLETED  
**Completed:** 2026-09-11  
**Suggested literature ID:** MORPH-UZ-008  
**Status note:** official dissertation work is independently verified at TUIT seminar level; final defense not verified as of 2026-09-11.

## 1. Bibliographic record

- **Author:** Turayev Boburxon Shuhrat o‘g‘li
- **Title in supplied abstract:** *Neyron tarmoq asosida o‘zbek tilini morfologik va sintaktik tahlil qilish algoritmlari va dasturiy majmuasi*
- **Russian title in supplied abstract:** «Алгоритмы и программные комплексы для морфологического и синтаксического анализа узбекского языка на основе нейронных сетей»
- **Degree sought:** Doctor of Philosophy (PhD), technical sciences
- **Specialty in supplied abstract:** 05.01.04 — mathematical and software support of computers, complexes and computer networks
- **Institution:** Tashkent University of Information Technologies named after Muhammad al-Khwarizmi (TUIT)
- **Scientific adviser:** Musayev Muhammadjon Maxmudovich, DSc, professor
- **Year on supplied abstract:** 2026
- **Source type:** user-supplied dissertation abstract + current official TUIT seminar verification
- **Reliability:** **B / candidate PhD evidence; do not treat as defended PhD yet**
- **Full dissertation:** not supplied; abstract supplied (26 parsed pages)

### Current official verification

A current TUIT announcement confirms that Turayev Boburxon Shuhrat o‘g‘li presented/discussed a PhD dissertation at the scientific seminar on **2026-07-11**. The TUIT title is:

> *O‘zbek tili matnlarini morfologik va sintaktik tahlil qilish algoritmlari va dasturiy majmuasi*

This verifies the existence and institutional progress of the dissertation work, but does **not** by itself verify successful final defense.

Official TUIT seminar record:
https://tuit.uz/post/hurmatli-professor-oqituvchilar-doktorantlar-va-mustaqil-izlanuvchi

### Metadata conflict that must be preserved

The supplied abstract states dissertation registration number:

`B2025.3.PhD/T5887`.

However, the current official OAK defense-announcement index assigns that registration number to a **different dissertation**, by Xoldorov Shohruhmirzo Imomali o‘g‘li, on muscle biosignal processing for athlete training.

This is a major metadata inconsistency. In addition, the supplied abstract has blank fields for:

- official opponents;
- leading organization;
- defense date/time;
- dissertation registration in the information-resource center;
- abstract distribution date.

Therefore the supplied file should be treated as a **draft / pre-defense abstract** rather than a final defended-author-abstract record until the discrepancy is resolved.

## 2. Why this work matters to the PhD

Turayev is important for the national evidence boundary because it further closes any broad claim that Uzbek lacks:

- text normalization;
- a sizable lemma/base-form lexicon;
- lemmatization algorithms;
- statistical/neural POS tagging;
- hybrid morphology-oriented processing;
- large tagged corpora;
- software complexes for morphosyntactic processing.

For our retrieval PhD, the most relevant result is the explicit construction of **more than 32 thousand base forms** and a lemmatization algorithm that maps grammatical word forms to a common base form.

However, the work is **not** an information-retrieval ranking benchmark and does not test BM25, dense retrieval or lexical–semantic hybrid search under qrels.

## 3. Research problem

### Simple explanation

Uzbek is agglutinative: a word can contain a base plus several suffixes. A computer system processing Uzbek documents must therefore normalize forms, identify word classes and understand sentence structure.

Turayev’s main problem is not “which documents should be retrieved for a query?” It is:

> how to automatically preprocess, morphologically tag, syntactically analyze and correct Uzbek official-style text.

### Formal formulation

The dissertation combines:

- preprocessing/normalization;
- lemmatization;
- POS tagging;
- syntactic parsing;
- corpus construction;
- neural sequence modeling;
- automatic syntactic correction.

The work treats these as a pipeline for Uzbek NLP and document-processing systems.

## 4. Main idea

### Simple explanation

The author does not rely on one model.

For POS tagging, several components are combined:

- **BiLSTM** — reads context in both directions;
- **CRF** — chooses a globally consistent sequence of grammatical tags;
- **maximum-entropy features** — add probabilistic linguistic features.

For syntactic analysis, a hybrid `RNN + CYK` approach is proposed.

For correction, a reverse corpus of correct/incorrect sentence pairs is used to train sequence-to-sequence models.

### Concrete example

The lemmatization component collects more than 32k base forms and maps different grammatical forms to the same basic form. This is directly relevant to our future `BM25_lemma` condition, but Turayev does not evaluate that lemma representation inside BM25.

## 5. Architecture / algorithm

### 5.1 Preprocessing

The abstract describes a chain including:

- encoding/script standardization;
- normalization of non-standard units;
- abbreviation handling;
- removal of unnecessary symbols;
- tokenization;
- contextual completion with RoBERTa/MLM-style models;
- spelling correction.

### 5.2 Lemmatization / lexical base

The conclusion states:

- more than **32,000 base forms** were collected;
- a lemmatization algorithm was developed on this basis;
- it maps grammatical word forms to a unified base form.

A corpus table gives the more precise value:

- **32,225 lemmas/base forms**.

This is strong national evidence that lemmatization is not a missing Uzbek capability.

### 5.3 POS tagging

The proposed model combines:

`maximum entropy + BiLSTM + CRF`.

Simple interpretation:

- BiLSTM captures contextual information;
- maximum-entropy features incorporate linguistic/probabilistic properties;
- CRF optimizes the output tag sequence jointly.

### 5.4 Syntactic analysis

The dissertation proposes a hybrid:

`RNN encoder + CYK decoder/parser`.

The RNN represents contextual/sequential information and CYK applies grammar-based structured decoding.

### 5.5 Reverse corpus and syntactic correction

A “reverse corpus” is constructed from correct and incorrect sentence pairs. A sequence-to-sequence model learns to transform an incorrect sentence into a corrected sentence.

### 5.6 Software complex

The system architecture includes:

- speech-to-text input;
- normalization;
- tokenization/morphological analysis;
- syntactic analysis;
- syntactic editing;
- rules/dictionaries;
- document generation;
- workflow and integration infrastructure.

Again, this is a document/NLP processing system, not a ranked document-retrieval architecture.

## 6. Data

The abstract reports several data families.

### 6.1 General corpus split

A table on page 10 reports:

| Split | Words | Sentences | Share |
|---|---:|---:|---:|
| Training | 345,120,139 | 90,135,045 | 85% |
| Testing | 60,903,554 | 15,906,184 | 15% |

The source does not provide enough detail in the abstract to independently verify provenance, deduplication, annotation coverage or how these very large counts were produced.

### 6.2 POS knowledge-base statistics

A separate table reports:

| Split | Sentences | Tokens | POS-tagged sentences | POS-tagged tokens |
|---|---:|---:|---:|---:|
| Training | 801,315 | 2,950,011 | 789,362 | 2,117,272 |
| Validation | 1,699 | 40,068 | not separated | not separated |
| Test | 2,415 | 56,671 | 2,012 | 47,377 |

The relationship between this POS dataset and the much larger corpus counts above is not explained sufficiently in the abstract.

### 6.3 Corpus resources for downstream processing

The later corpus table reports:

| Resource | Tokens | Sentences |
|---|---:|---:|
| Mixed collected corpora (POS) | 406,023,693 | 106,041,229 |
| Lemma set | 32,225 | — |
| NER corpus | 785 | — |
| Syntactically tagged corpus | 97,451,541 | 34,578,785 |

### 6.4 Data caution

The abstract contains very large corpus values in several different tables without enough methodological detail to reconcile them.

For our project:

- preserve the numbers as **reported**;
- do not use them to claim corpus scale without final-source verification;
- do not infer that all hundreds of millions of tokens are manually annotated;
- do not treat the corpus automatically as an IR benchmark, because it has no retrieval queries/qrels.

## 7. Baselines

### POS/morphology-oriented comparison

The abstract reports comparisons among:

- HMM;
- CRF;
- LSTM;
- BiLSTM;
- LSTM+CRF;
- BiLSTM+CRF;
- MaxEnt+BiLSTM+CRF.

These are POS/morphological sequence-labeling models.

### Syntactic comparison

The abstract reports:

- HMM;
- BERT;
- RoBERTa;
- LLaMA;
- DeBERTa;
- RNN.

### Retrieval baselines

For our current PhD question, the crucial absence is:

- no `BM25_raw`;
- no `BM25_stem`;
- no `BM25_lemma`;
- no modern dense retriever;
- no lexical+dense hybrid retrieval;
- no RRF/score fusion;
- no qrels-based ranking evaluation.

## 8. Metrics

The abstract reports:

- “accuracy” (`Aniqlik`);
- BLEU (printed as `BLUE` in tables);
- ROUGE-L;
- ROUGE-W;
- METEOR;
- ChrF/ChrF++.

These are then used not only for generation/correction but also in tables describing POS and syntactic analysis.

### Methodological caution

BLEU, ROUGE, METEOR and ChrF are mainly string/generation overlap metrics. They are **not standard primary metrics for POS tagging** in the same sense as token accuracy, precision/recall/F1.

Therefore the table values can be reported as author-reported evaluation, but the present PhD should not treat them as a standard comparable POS benchmark without the full dissertation’s exact metric definitions.

More importantly:

> none of these numbers are document-retrieval metrics.

They cannot be interpreted as MAP, nDCG, MRR or Recall@k.

## 9. Main numerical results

### 9.1 POS/morphology-oriented table

The reported table includes two feature groups.

For the strongest reported variant:

| Model | Feature family | Accuracy | BLEU | ROUGE-L | ROUGE-W | METEOR | ChrF/ChrF++ |
|---|---|---:|---:|---:|---:|---:|---:|
| MaxEnt+BiLSTM+CRF | contextual features | **0.89** | **0.87** | 0.79 | 0.85 | **0.93** | **0.91** |

For comparison, `BiLSTM+CRF` under contextual features reports:

- Accuracy 0.86;
- BLEU 0.85;
- ROUGE-L 0.89;
- ROUGE-W 0.86;
- METEOR 0.76;
- ChrF/ChrF++ 0.85.

### 9.2 Syntactic table

The source reports:

| Model | “CYK Accuracy” | BLEU | ROUGE-L | ROUGE-W | METEOR | ChrF/ChrF++ |
|---|---:|---:|---:|---:|---:|---:|
| HMM | 0.71 | 0.73 | 0.70 | 0.69 | 0.69 | 0.73 |
| BERT | 0.74 | 0.76 | 0.837 | 0.83 | 0.837 | 0.767 |
| RoBERTa | 0.685 | 0.725 | 0.836 | 0.837 | 0.837 | 0.69 |
| LLaMA | 0.814 | 0.833 | 0.72 | 0.725 | 0.722 | 0.831 |
| DeBERTa | 0.861 | 0.852 | 0.89 | 0.86 | 0.76 | 0.85 |
| RNN | **0.881** | **0.872** | 0.794 | 0.855 | **0.936** | **0.913** |

The abstract does not give enough detail to determine whether all these systems were trained/evaluated under strictly identical conditions.

### 9.3 Syntactic correction / Seq2Seq

On a reported normalized set of 34,578,785 examples:

| Model | Correct | Incorrect | ChrF++ | Mean output time |
|---|---:|---:|---:|---:|
| BERT | 30,520,000 | 4,058,785 | 0.88 | 45 ms |
| RoBERTa | 30,760,000 | 3,818,785 | 0.88 | 50 ms |
| LLaMA | 30,830,000 | 3,748,785 | 0.89 | 70 ms |
| DeBERTa | 30,870,000 | 3,708,785 | 0.89 | 55 ms |
| Seq2Seq | **30,877,850** | **3,700,935** | **0.893** | **34 ms** |

The conclusion describes this as **89.3% accuracy** and reports `Loss = 0.03%`.

### 9.4 Deployment efficiency

The system was piloted for document creation/editing:

- 21 documents over 10 working days;
- speech-based input compared with keyboard/manual entry;
- reported time-efficiency improvement: **17–23%**.

This is a workflow/productivity result, not search effectiveness.

## 10. Statistical evidence

From the supplied abstract alone, the deep dive did not find:

- statistical significance tests;
- confidence intervals;
- repeated-seed reporting;
- retrieval-level per-query testing;
- qrels;
- a clear ablation isolating the contribution of lemmatization to downstream search.

The work does compare several models numerically, but the abstract is insufficient to establish whether all differences are statistically robust.

## 11. Strengths

1. **Direct Uzbek morphology evidence.**
2. **Explicit lemmatization resource** with more than 32k base forms.
3. **Hybrid POS approach** combines contextual neural and probabilistic sequence information.
4. **Large practical software scope**, not only a conceptual model.
5. **Real implementation context** in administrative/document workflows.
6. **Independent official TUIT evidence** confirms that this dissertation work underwent scientific seminar discussion in 2026.

## 12. Limitations

### Source/status limitations

1. Final defense is not verified.
2. The supplied abstract contains blank final-defense metadata fields.
3. The abstract’s registration number `B2025.3.PhD/T5887` conflicts with the current OAK record, where that number belongs to another dissertation.
4. The current TUIT seminar uses a somewhat different title formulation from the supplied abstract.

### Scientific limitations relative to our IR question

1. **Lemmatization is not evaluated through document retrieval.**
2. **No BM25 experiment.**
3. **No dense retriever.**
4. **No lexical–semantic hybrid retrieval.**
5. **No query/relevance judgments.**
6. **No MAP/nDCG/Recall@k for document ranking.**
7. **No raw/stem/lemma retrieval ablation.**
8. **No lexical-only/dense-only/overlap/oracle analysis.**
9. The use of BLEU/ROUGE/METEOR/ChrF in POS/syntactic tables needs full-method verification before cross-paper comparison.

## 13. What the work proves

At the current evidence level, it strongly supports that:

- Uzbek text normalization and morphosyntactic processing are active, technically developed national research directions;
- a substantial Uzbek lemma/base-form lexicon has been assembled;
- lemmatization is explicitly implemented computationally;
- neural/statistical hybrid POS tagging has been developed and compared against several alternatives;
- corpus and software infrastructure for Uzbek morphological/syntactic processing exists;
- these tools can be integrated into practical document-processing workflows.

## 14. What the work does NOT prove

It does **not** establish that:

- lemmatization improves Uzbek BM25;
- stemming is worse/better than lemmatization for Uzbek retrieval;
- `lemma > stem > raw`;
- BM25+dense is better than either channel alone;
- semantic retrieval benefits from or conflicts with morphology;
- morphology changes lexical–dense complementarity;
- the lemma resource gives incremental hybrid gain;
- National Library search itself was improved.

The National Library implementation described in the abstract concerns **document formation/input and syntactic editing**, not a retrieval benchmark.

## 15. Relationship to current Uzbek evidence

Turayev reinforces a national chain already established by:

- Bakaev — Uzbek morphological analysis and search-oriented processing;
- Xusainova — tokenization/stemming/lemmatization and corpus/search optimization;
- Elov — integrated morphology/syntax/semantics and search-oriented normalization/indexing infrastructure.

Turayev’s distinctive contribution for our evidence map is:

- a concrete 32k+ lemma/base-form resource;
- a neural/statistical hybrid POS/morphosyntactic pipeline;
- large reported corpora;
- practical document-processing implementation.

This further weakens any attempt to claim novelty from “adding Uzbek lemmatization”.

## 16. Relationship to CURRENT_GAP

**Status:** supports the boundary; does not close v0.8.

Turayev addresses:

`Uzbek morphology / lemma resources / POS / syntax / editing`.

Our current residual question remains:

`raw/stem/lemma lexical representation`
→ `change in BM25 relevant set`
→ `change in overlap/unique hits with the same dense retriever`
→ `change in incremental hybrid gain`
→ `relation to Uzbek query features`.

The dissertation abstract provides no experiment covering this chain.

Therefore **CURRENT_GAP v0.8 should remain unchanged**.

## 17. Implications for our research design

1. **Do not make lemmatization itself the novelty.**
2. Investigate whether Turayev’s 32k+ lemma resource/software can be reused or compared with other Uzbek lemmatizers.
3. Treat `BM25_lemma` as one controlled lexical representation, not automatically the “best” representation.
4. Keep `BM25_raw`, `BM25_stem`, `BM25_lemma` under the same retrieval protocol.
5. Evaluate with a real retrieval benchmark and qrels.
6. Keep the dense retriever and fusion fixed when attributing changes to morphology.
7. Do not interpret workflow speed or POS accuracy as search quality.

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| Lemma | Dictionary/base form of a word | Canonical representation of inflected word forms |
| POS tagging | Determine whether a word is a noun, verb, adjective, etc. | Sequence labeling assigning part-of-speech tags |
| BiLSTM | Reads context from left-to-right and right-to-left | Bidirectional Long Short-Term Memory network |
| CRF | Chooses a consistent sequence of tags | Conditional Random Field structured prediction layer |
| Maximum entropy | Uses weighted features probabilistically | Log-linear probabilistic modeling approach |
| CYK | Grammar-based structured parser | Cocke–Younger–Kasami dynamic-programming parsing algorithm |
| Reverse corpus | Pairs wrong and corrected sentences | Training resource for correction/transduction models |
| Qrels | Which documents are truly relevant to each query | Relevance judgments used in information-retrieval evaluation |

## 19. Open questions / verification needed

1. Verify final defense status.
2. Resolve the registration-number conflict `B2025.3.PhD/T5887`.
3. Obtain/fetch the final dissertation or final official author abstract after defense.
4. Verify whether the final title is the supplied “neural-network-based” title or the shorter title used by TUIT’s July seminar.
5. Clarify the origin and annotation process of the very large corpus counts.
6. Verify exact metric definitions in the POS/syntactic tables, especially use of BLEU/ROUGE/METEOR/ChrF.
7. Determine whether the 32,225-lemma resource/software is accessible for research reuse.
8. Confirm exactly what was deployed at the National Library: current evidence supports document input/editing, not search ranking.

## 20. Decision after deep dive

- **Keep current gap?** Yes.
- **Modify v0.8?** No.
- **Reliability upgrade?** No A-level upgrade yet. Keep as **B / official ongoing PhD evidence pending final defense verification**.
- **Add to national map?** Yes.
- **Add citation to Chapter I?** Potentially yes for national lemmatization/morphosyntactic infrastructure, but final dissertation citation should wait for metadata/defense resolution.
- **Add methodological decision?** No.
- **Retrieval implication:** Turayev strengthens the reason to use existing morphology resources rather than making a new analyzer the main PhD contribution.
