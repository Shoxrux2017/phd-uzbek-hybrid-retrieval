# Elov B.B. — NLP-based automatic analysis and processing of Uzbek texts

**Deep-dive status:** COMPLETED  
**Completed:** 2026-09-11  
**Suggested literature ID:** PHD-UZ-004 / MORPH-UZ-007

## 1. Bibliographic record

- **Author:** Botir Boltayevich Elov
- **Title:** *NLP texnologiyasiga asoslangan o‘zbek tilidagi matnlarni avtomatik tahlil qilish va ishlov berishning lingvistik usullari, modellari va axborot tizimi*
- **Russian sense of title:** «Лингвистические методы, модели и информационная система автоматического анализа и обработки узбекских текстов на основе NLP-технологий»
- **Degree:** Doctor of Science (DSc), technical sciences
- **Specialty:** 05.01.10 — Information retrieval systems and processes / «Axborot olish tizimlari va jarayonlari»
- **Institution/council:** Tashkent University of Information Technologies named after Muhammad al-Khwarizmi
- **Scientific adviser/consultant shown in supplied manuscript:** Utkir Khamdamov
- **Year on supplied full manuscript:** 2025
- **Official defense date:** 2026-02-05
- **Official OAK record:** https://www.interaktiv.oak.uz/independentCouncil/dissertation/3aOf2299417263O.asp
- **Official abstract record:** https://www.interaktiv.oak.uz/avtoreferat/3aO22994fO1.file
- **Source type:** officially defended DSc dissertation; user-supplied full manuscript plus official OAK verification
- **Reliability:** **A**
- **Full text available for project analysis:** yes, user-supplied 387-page PDF

### Date handling

The supplied manuscript itself is dated **Tashkent–2025**, while the official OAK record confirms the defense on **2026-02-05**. For project chronology, treat this as a **2026 defended DSc** and preserve 2025 as the manuscript date.

## 2. Why this work matters to the PhD

This is strong national evidence for what is already mature in Uzbek NLP and what must **not** be claimed as new in the present dissertation.

Directly relevant points:

- Uzbek morphology is modeled computationally at substantial depth;
- lemmatization and morphological normalization are explicitly connected to search/indexing;
- a hybrid morphological analyzer combines linguistic rules, statistical methods and neural/ML components;
- the resulting lexical-processing pipeline prepares lemma-based inverted indexes using SQL Server full-text search / Elasticsearch infrastructure;
- morphology, syntax, semantic-role analysis and NER are integrated in one Uzbek NLP information system (`UzNLP`);
- the work is explicitly connected to the national project IL-402104209 for a Uzbek morpholexicon and morphological analyzer intended for information-retrieval / language-processing systems.

However, the work is **not** a controlled modern document-retrieval study of BM25 versus dense retrieval, and its use of the word “hybrid” refers mainly to combining analysis methods inside NLP modules rather than lexical–semantic retrieval fusion.

## 3. Research problem

### Simple explanation

Uzbek words can have many suffixes. The same lexical item can appear in many forms, and a computer must determine the base form, grammatical information and context before higher-level processing becomes reliable.

Example:

`kitoblarimizdan`

is analyzed into a structure corresponding to:

`kitob + noun + plural + first-person possessive + ablative`.

The dissertation studies how to automate this kind of analysis together with POS tagging, syntax, semantic roles and named entities, and how to expose the resulting analysis through an integrated information system.

### Formal formulation

The dissertation treats morphology, syntax and semantics as linked levels of automatic Uzbek text processing. For morphological analysis, candidate analyses are generated and then disambiguated using contextual/statistical/neural methods. The output is subsequently used for normalization, lexical processing and indexing.

This is a language-analysis and information-system problem, not primarily a qrels-based ad-hoc retrieval-ranking problem.

## 4. Main idea

### Simple explanation

Do not rely on only one technique for Uzbek morphology.

- Rules are good for known grammatical patterns.
- Statistical/neural models help when a form is ambiguous or not completely covered by rules.
- Combining them gives a more robust analyzer.

The normalized output can then be reused by search, indexing, translation and other NLP applications.

### Concrete example

For forms such as `borayotgan` and `borgan`, the lexical-processing stage maps forms to a common lemma/base representation so that different grammatical forms can be treated as related during indexing/search-oriented processing.

### Formal method

The dissertation describes a hybrid morphology pipeline approximately as:

`text`
→ tokenization
→ orthographic/script normalization
→ FST/rule-based candidate analyses
→ CRF/BiLSTM-CRF/Transformer-style contextual disambiguation
→ lemma + POS + grammatical features
→ stop-word filtering
→ synonym mapping with UzWordNet
→ lexical indexing.

## 5. Architecture / algorithm

### 5.1 Morphological analysis

The proposed analyzer combines:

1. **rule/FST component** — generates possible root/lemma and affix analyses;
2. **statistical / neural disambiguation** — selects the most contextually appropriate analysis;
3. **lexical database / lemma mechanism** — returns base forms;
4. **grammatical feature output** — POS and morphological attributes.

The manuscript also discusses BiLSTM-CRF and sequence-to-sequence formulations for morphology.

### 5.2 Lexical-processing stage

The morphological result is then used for:

1. lemma normalization;
2. filtering selected function words with `UzbStopWordsList` and POS information;
3. synonym mapping using UzWordNet;
4. building inverted indexes over lemmas / grammatical attributes.

The text explicitly names SQL Server full-text search and Elasticsearch as indexing/search infrastructure.

### 5.3 Integrated UzNLP system

Beyond morphology, the system combines modules for:

- morphology;
- POS tagging;
- dependency/syntactic analysis;
- semantic-role analysis;
- NER;
- corpus ingestion/ETL;
- REST/API-based integration with external applications.

Important distinction for our PhD:

> integrating morphology + syntax + semantic analysis modules is **not the same experiment** as fusing a lexical document retriever with a dense semantic retriever.

## 6. Data

The dissertation contains several dataset/corpus descriptions that must not be collapsed into one number without qualification.

### 6.1 Morphological-model training/evaluation

- a linguistically tagged part of `UzbCorpus` is reported at approximately **38 million words** for ML/seq2seq morphology training;
- elsewhere, a neural morphology subsection reports about **80k training words** and **20k test words** for a particular model setup;
- a dedicated morphology evaluation uses a manually/previously tagged test set of approximately **5,000 words** from different styles/topics.

### 6.2 National/integrated corpus counts

The introductory/practical-results section reports approximately:

- `~50 billion sentences`;
- `~380 million words`;
- 10% linguistically tagged.

But a later database/implementation section reports:

- approximately **124 million tokens**;
- approximately **2.5 million unique lemmas**.

### 6.3 Data-count caution

The stated `~50 billion sentences` together with `~380 million words` is internally implausible as written because the sentence count exceeds the word count by two orders of magnitude. The full text also reports 124M tokens elsewhere.

Therefore the project must **not repeat the corpus-size headline uncritically**. Before final dissertation citation of corpus scale, verify the official abstract/final dissertation wording or obtain clarification from the underlying corpus documentation.

## 7. Baselines

### Morphological analyzer comparison

The key morphology table compares:

- rule-based approach;
- machine-learning approach;
- proposed hybrid approach.

This comparison is useful for showing that Uzbek morphological processing has already moved beyond simple suffix stripping.

### Retrieval baselines

No controlled retrieval baseline family comparable to the present PhD design was identified in the supplied full text:

- no verified `BM25_raw`;
- no verified `BM25_stem`;
- no verified `BM25_lemma`;
- no modern dense retriever held fixed across morphology variants;
- no lexical+dense fusion comparison.

The dissertation discusses TF-IDF conceptually and uses full-text/inverted indexing infrastructure, but this should not be upgraded into a BM25 retrieval experiment without source evidence.

## 8. Metrics

### Precision

Simple meaning: among analyses produced by the module, how many are correct.

### Recall

Simple meaning: among correct analysis elements that should have been found, how many were found.

### F1

Harmonic mean of precision and recall; balances both.

### Accuracy / complete-analysis accuracy

For the morphology experiment, this is described as the share of words whose complete morphological analysis matches the reference.

### Critical metric distinction

These are **NLP module-quality metrics**, not standard document-retrieval effectiveness evidence such as MAP, nDCG, Recall@k on qrels.

Therefore a 96% morphology score cannot be interpreted as 96% search quality.

## 9. Results

### 9.1 Morphological analyzer — core comparison

| Approach | Precision | Recall | F1 | Accuracy / fully correct analysis |
|---|---:|---:|---:|---:|
| Rule-based | 78.0% | 75.0% | 76.5% | 80% |
| Machine learning | 88.5% | 85.0% | 86.7% | 85% |
| Hybrid | **93.0%** | **91.0%** | **92.0%** | **94%** |

The author explicitly cautions that these values are for the reported test set and may differ on another corpus.

### 9.2 Later integrated-system evaluation

A later system-level table reports:

| Module | Accuracy | Precision | Recall | F1 |
|---|---:|---:|---:|---:|
| Morphological analysis | 96.4% | 96.0% | 97.0% | 96.5% |
| POS tagging | 97.5% | 97.2% | 97.8% | 97.5% |
| Syntactic analysis | 96.0% | 96.5% | 95.5% | 96.0% |
| Semantic analysis | 96.7% | 96.9% | 96.2% | 96.5% |
| NER | 96.1% | 96.4% | 95.8% | 96.1% |

### 9.3 Result-consistency caution

The morphology chapter reports **94% complete-analysis accuracy / 92% F1**, while the later integrated-system evaluation reports **96.4% accuracy / 96.5% F1**.

The inspected text does not provide a sufficiently explicit bridge showing whether these are:

- different model versions;
- different test sets;
- post-deployment improvements;
- or differently defined evaluation conditions.

Therefore both should be retained with context rather than silently merged.

## 10. Statistical evidence

For the main morphology comparison, the inspected text reports point estimates of precision, recall, F1 and accuracy.

The deep dive did **not** identify, for that morphology comparison:

- confidence intervals;
- a statistical significance test between rule/ML/hybrid variants;
- repeated random seeds linked directly to the morphology table.

The dissertation does use repeated/cross-validation procedures in other modules such as POS tagging, but this should not be transferred to the morphology result without explicit evidence.

There is also no per-query retrieval analysis because this is not a query-document retrieval benchmark.

## 11. Strengths

1. **Official defended DSc** — strong national primary evidence.
2. **Large integrated scope** — morphology, POS, syntax, semantic roles, NER and system engineering are treated together.
3. **Explicit search-oriented lexical processing** — lemma normalization, inverted indexing and full-text search infrastructure are connected directly to Uzbek morphological analysis.
4. **Practical system** — `UzNLP` is implemented and integrated through APIs.
5. **Direct relevance to national infrastructure** — work is linked to Uzbek corpus and morpholexicon/morphological-analyzer projects.
6. **Concrete morphology ablation at analyzer level** — rule vs ML vs hybrid processing is compared numerically.

## 12. Limitations

### Stated / visible in the work

- OOV/neologisms and misspellings can cause morphology errors;
- complex compounds can be split incorrectly;
- ambiguity without sufficient context remains difficult;
- corpus/resource growth remains important.

### Inferred from the experimental design for our IR question

1. **No controlled modern IR benchmark.** The dissertation does not evaluate raw/stem/lemma variants under one ranker using qrels.
2. **No dense document retriever comparison.** Semantic analysis here is primarily linguistic/semantic-role processing, not dense query-document retrieval.
3. **No lexical–semantic fusion decomposition.** There are no unique relevant hits, overlap, oracle union or incremental hybrid gain measurements.
4. **No query-level retrieval analysis.** The work does not study how morphology changes retrieval effectiveness by query characteristics.
5. **Internal numerical ambiguity.** Corpus-size counts and morphology-evaluation figures differ across sections and need contextual verification before reuse.

## 13. What the work proves

The work supports the following claims:

- Uzbek morphological analysis and lemmatization are mature enough to be implemented in an integrated national NLP system;
- a rule-only morphology approach is not the only national solution; hybrid rule/statistical/neural processing has been developed and tested;
- morphology outputs are explicitly used for normalization and indexing-oriented lexical processing;
- Uzbek morphology, syntax and semantic analysis infrastructure can be integrated into external applications through an information system;
- national work already treats morphological normalization as useful infrastructure for information retrieval/search applications.

## 14. What the work does NOT prove

It does **not** prove:

- that lemmatization improves BM25 ranking effectiveness over raw or stemming for Uzbek;
- that `lemma > stem > raw` in information retrieval;
- that BM25 is the best lexical model for Uzbek;
- that dense retrieval is inferior or superior to lexical retrieval;
- that a lexical+dense hybrid improves Uzbek document retrieval;
- that morphology changes lexical–dense complementarity;
- that the reported NLP accuracy/F1 values translate into MAP/nDCG/Recall improvements;
- that the current PhD’s `raw/stem/lemma × same dense` question is already answered.

## 15. Relationship to current Uzbek evidence

Elov strengthens and connects several already known national lines:

- Bakaev — Uzbek morphological analysis/search applications;
- Xusainova — tokenization/stemming/lemmatization/search optimization;
- IL-402104209 — morpholexicon/morphological analyzer for search/NLP systems;
- Akhmedova/Axmedova and related work — semantic processing in Uzbek.

Its distinctive value for the present literature map is that it provides **A-level defended DSc evidence** for an integrated Uzbek morphology–syntax–semantics infrastructure while preserving the important distinction that this integration is not the same as lexical+dense retrieval fusion.

## 16. Relationship to CURRENT_GAP

**Status:** supports and sharpens; does not close v0.8.

Elov eliminates any remaining broad claim that Uzbek lacks:

- serious morphological processing;
- lemmatization/normalization for search-oriented pipelines;
- integrated semantic linguistic processing;
- deployable national NLP infrastructure.

But the dissertation still does not establish the current residual interaction:

`morphological representation change`
→ `change in lexical relevant set`
→ `change in overlap / unique relevant hits with fixed dense retriever`
→ `change in incremental hybrid gain`
→ `relation to Uzbek query characteristics`.

Therefore **CURRENT_GAP v0.8 should not be changed because of this deep dive**.

## 17. Implications for our research design

1. **Do not build a new morphology analyzer as the central PhD contribution.** Existing national infrastructure is already substantial.
2. **Reuse or adapt existing Uzbek morphology resources where legally/technically possible.** The PhD question is retrieval behavior, not reinvention of the analyzer.
3. **Keep morphology as a lexical-representation intervention.** Compare `raw`, `stem`, `lemma` under the same BM25 setup.
4. **Keep the dense retriever fixed** when attributing changes to morphology.
5. **Evaluate retrieval with qrels-based IR metrics**, not analyzer accuracy.
6. **Measure complementarity directly** through unique relevant hits, overlap, union and incremental hybrid gain.
7. **Treat script/orthographic normalization separately** from semantic retrieval so causal interpretation remains clear.

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| Morphological analyzer | Program that breaks a word into its base and grammatical parts | System that maps a word/form in context to lemma/root, POS and morphological features |
| Lemmatization | Bring word forms to a dictionary/base form | Normalization from inflected surface forms to a lemma |
| FST | Rule mechanism for moving through allowed character/morpheme patterns | Finite-state transducer used for morphological analysis/generation |
| Disambiguation | Choose the correct analysis when several are possible | Context-conditioned selection among candidate morphological analyses |
| Inverted index | Structure that says which documents/records contain a term | Core index mapping terms to postings/documents |
| Semantic-role analysis | Determine who did what to whom in a sentence | Predicate–argument semantic labeling (SRL) |
| Hybrid morphology | Combine rule and learned/statistical analysis | Analyzer-level hybridization; **not** lexical+dense retrieval fusion |

## 19. Open questions / verification needed

1. Resolve the corpus-size discrepancy: `~50 billion sentences / ~380M words` vs `~124M tokens` and `~38M tagged words`.
2. Resolve the morphology result discrepancy: chapter-level `94% accuracy / 92% F1` vs later system-level `96.4% accuracy / 96.5% F1`.
3. Determine which exact morphology resources/software components are publicly/reusably available for the present PhD.
4. Verify the precise retrieval/search mechanism used in deployment; the supplied dissertation text names SQL Server full-text search and Elasticsearch but does not establish a controlled BM25 experiment.
5. If citing exact system-scale numbers in Chapter I, prefer the official abstract/final defended version or an independently documented corpus release.

## 20. Decision after deep dive

- **Keep current gap?** Yes — `v0.8 refined` remains intact.
- **Modify gap?** No.
- **Add decision?** No new methodological decision is required; existing rules already separate NLP infrastructure from retrieval effectiveness.
- **Add experiment?** No new experiment beyond the existing controlled `BM25_raw/stem/lemma + same dense D` design.
- **Add citation to Chapter I?** Yes, as strong national evidence for Uzbek morphology/normalization and integrated NLP infrastructure, with explicit warning that module accuracy is not retrieval effectiveness.
- **Update evidence status?** Yes: replace “Elov 2026 screening” with **officially defended DSc, A-level, deep-dive completed 2026-09-11**.
