# Performance of Turkish Information Retrieval: Evaluating the Impact of Linguistic Parameters and Compound Nouns

**Deep-dive status:** COMPLETED  
**Completed:** 2026-09-04  
**Literature ID:** MORPH-002

## 1. Bibliographic record

- **Authors:** Hatem Haddad; Chedi Bechikh Ali
- **Year:** 2014
- **Venue:** CICLing 2014, Part II, *Computational Linguistics and Intelligent Text Processing*, Lecture Notes in Computer Science (LNCS) 8404, pp. 381–391
- **Publisher:** Springer-Verlag Berlin Heidelberg
- **DOI:** `10.1007/978-3-642-54903-8_32`
- **Persistent bibliographic record:** DBLP `conf/cicling/HaddadA14`
- **Full text available:** yes (author-uploaded full text is publicly accessible)
- **Source type:** peer-reviewed conference chapter / proceedings paper
- **Reliability:** B
- **Reason for reliability level:** verified primary publication with direct IR experiments, but narrower venue/evidence strength than the project's A-tier anchors; no paired statistical-significance test is reported.

## 2. Why this work matters to the PhD

This paper is the direct methodological follow-up to Can et al. (2008) for the current PhD's morphology-aware lexical retrieval line.

Can et al. established that morphology matters for Turkish lexical IR but did not evaluate BM25. Haddad & Bechikh Ali explicitly evaluate:

- TF-IDF;
- BM25;
- a classical statistical Language Model (LM) retrieval formulation;

while varying several linguistic preprocessing/representation choices.

For the current Uzbek PhD, the most important contribution is therefore not a particular Turkish stemmer, but evidence that:

1. morphology-related preprocessing can materially change BM25 effectiveness in an agglutinative Turkic language;
2. the same preprocessing may affect different retrieval models differently;
3. simple normalization can remain competitive with more linguistically elaborate morphology-aware processing;
4. preprocessing effects depend on the metric and experimental configuration;
5. the paper still does not address modern semantic or lexical–semantic hybrid retrieval.

## 3. Research problem

### Simple explanation

Turkish creates many surface word forms by attaching suffixes to roots. A lexical search system may therefore miss relevant documents when query and document use different inflected forms.

But there is a broader question than in Can et al.:

> If we change the linguistic preprocessing of the same Turkish text, do TF-IDF, BM25 and a classical language-model retrieval formulation benefit in the same way?

The authors additionally ask whether search can improve by using:

- stop-word removal;
- document/query fields;
- simple word truncation;
- Snowball and Zemberek stemming;
- multiword compound-noun candidates.

### Formal formulation

The work evaluates the interaction between:

`linguistic preprocessing / lexical representation × retrieval model`

on the Milliyet Turkish ad-hoc retrieval collection.

The evaluated retrieval models are classical lexical/statistical models, not modern dense semantic retrievers.

## 4. Main idea

### Simple explanation

Instead of testing one stemmer, the authors keep the same retrieval collection and repeatedly change how documents and queries are represented before retrieval.

They then run each representation with three retrieval models.

This allows them to ask not just:

> Does preprocessing help?

but:

> Which preprocessing helps which retrieval model, under which metric?

### Concrete Uzbek example

Suppose a future Uzbek collection contains:

`talaba`, `talabalar`, `talabalarga`, `talabalarning`.

Possible lexical representations include:

- raw words;
- a fixed-prefix form;
- a rule-based stem;
- a morphology-aware stem/lemma.

The Haddad & Bechikh Ali design suggests comparing each representation under the same BM25 implementation rather than assuming the most linguistically sophisticated representation will win.

### Formal method

The paper evaluates controlled configurations in Terrier:

1. raw baseline;
2. stop-word filtering;
3. document/query structural field selection;
4. fixed-prefix truncation;
5. Snowball and Zemberek stemming;
6. compound-noun candidate augmentation.

Effectiveness is measured with P@5, P@10, P@15, 11pt-avg, MAP and `bpref`.

## 5. Architecture / algorithm

### 5.1 Retrieval framework

The experiments use **Terrier**, an open-source information retrieval framework.

Three retrieval models are evaluated:

- **TF-IDF** — lexical term weighting based on within-document term frequency and collection rarity;
- **BM25** — probabilistic lexical ranking with term-frequency saturation and document-length normalization;
- **Language Model (LM)** — a classical statistical language-model retrieval formulation; this is **not** a modern neural language model such as BERT or GPT.

### 5.2 Baseline (BL)

Original documents and queries are used without:

- stop-word removal;
- stemming.

This is the main raw baseline.

### 5.3 Stop words (SW)

The authors use the **Turkish Stop Word List 1.1** containing **223 stop words**.

The comparison is:

`BL ↔ SW`.

### 5.4 Document and query structure

Milliyet documents have XML fields including:

- `HEADLINE`;
- `TEXT`;

and several metadata fields.

Queries use a TREC-like format with:

- `title`;
- `description`;
- `narrative`.

The best tested structural configuration uses:

- documents: `HEADLINE + TEXT`;
- queries: `title + description`.

This run is denoted **ST**.

The same structure plus stop-word filtering is **ST SW**.

### 5.5 Fixed-prefix truncation

Three pseudo-stemming variants are evaluated:

- 3-prefix;
- 4-prefix;
- 5-prefix.

A fixed-prefix method does not identify a linguistic lemma. It simply retains the first `n` characters.

This creates a trade-off:

- too short → over-normalization / false merging;
- too long → insufficient normalization of inflected forms.

### 5.6 Snowball

Snowball Turkish stemming uses rule-based **affix stripping** and does not require dictionary lookup.

It is a language-specific rule-based stemmer, but it is less linguistically resource-intensive than Zemberek.

### 5.7 Zemberek

Zemberek is designed for Turkish and uses a **root-dictionary-based parser** plus Turkish NLP/morphological rules.

The paper describes it as capable of handling suffix special cases and using it as a **lemmatizer-based stemmer**.

For the purposes of this PhD, the safe interpretation is:

> Zemberek is a more morphology-aware and lexicon-supported Turkish normalization method than Snowball.

It should not be treated as proof that dictionary lookup alone causes the observed gain.

### 5.8 Compound nouns

The authors attempt to enrich the lexical representation beyond isolated words.

Zemberek is used to tag words with syntactic/POS categories. Candidate compound nouns are then extracted with three patterns:

- `<Noun, Noun>`;
- `<Noun, Adjective>`;
- `<Adjective, Noun>`.

Reported extracted occurrences/candidates:

- Noun + Noun: 21,353,529;
- Noun + Adjective: 1,388,429;
- Adjective + Noun: 1,430,866.

Compound nouns are added **in addition to simple keywords** for both queries and documents.

Configurations:

- **CN** — compound nouns added to the baseline;
- **CN S** — compound nouns + structural fields;
- **CN S I** — CN S plus Terrier's `ignore.low.idf` option.

This remains lexical representation enrichment; it is **not semantic retrieval**.

## 6. Data

- **Dataset/corpus:** Bilkent Information Retrieval Group Milliyet test collection
- **Language:** Turkish
- **Domain:** newspaper articles and columns
- **Period:** 2001–2005
- **Documents:** 408,305
- **Collection size:** approximately 800 MB
- **Words before stop-word removal:** approximately 95.5 million
- **Average document length before stop-word removal:** approximately 234 words
- **Queries:** TREC-style Milliyet query set; the 2014 paper describes the same established Milliyet collection but does not restate the total query count in its dataset subsection. The underlying collection is the 72-query set documented by Can et al. (2008).
- **Assessors:** 33 native Turkish speakers
- **Relevance judgments:** binary
- **Judgment protocol:** pooling; pooled documents are shown in random order to assessors
- **Unjudged documents:** the paper describes the remainder of the collection as assumed irrelevant in the collection construction
- **Train/dev/test separation:** no modern explicit train/dev/test split or held-out tuning protocol is reported

Document-length categories inherited from the Milliyet analysis:

- short: ≤100 words;
- medium: 101–300;
- long: >300.

## 7. Baselines and comparison families

### Raw baseline

`BL` is the primary baseline:

- no stemming;
- no stop-word removal.

### Retrieval-model baseline comparison

The same BL representation is evaluated with:

- TF-IDF;
- BM25;
- LM.

This establishes whether one retrieval model is intrinsically stronger before adding linguistic preprocessing.

### Preprocessing comparisons

The authors then compare:

- BL vs SW;
- BL/ST variants;
- 3/4/5-prefix;
- Snowball vs Zemberek;
- CN vs CN S vs CN S I.

### Fairness and limitations of the comparison

Strengths:

- same corpus;
- same relevance judgments;
- same retrieval framework;
- multiple retrieval models;
- multiple effectiveness metrics.

Limitations:

- no held-out tuning set is reported;
- no paired significance test is reported;
- not every configuration changes only one independent factor;
- Zemberek vs Snowball differs in multiple implementation/morphological properties, not only dictionary access;
- the structure result partly exploits features specific to the Milliyet test collection.

## 8. Metrics

### P@5, P@10, P@15

**Simple meaning:** proportion of relevant documents among the top 5, 10 or 15 retrieved results.

These metrics emphasize the top of the ranking.

### 11pt-avg

Traditional 11-point interpolated average precision.

It summarizes precision at standard recall levels and reflects historical IR evaluation practice.

### MAP

**Mean Average Precision** averages Average Precision across queries.

It rewards systems that rank relevant documents early throughout the ranked list.

### bpref

`bpref` compares the relative ranks of judged relevant and judged non-relevant documents.

It is especially useful when relevance judgments are incomplete.

The authors explicitly treat `bpref` as particularly appropriate for Milliyet because the collection was built with incomplete relevance judgments.

## 9. Results

### 9.1 Baseline vs stop words

| Configuration | Model | P@5 | P@10 | P@15 | 11pt-avg | MAP | bpref |
|---|---|---:|---:|---:|---:|---:|---:|
| BL | TF-IDF | 0.5806 | 0.5278 | 0.5019 | 0.2598 | 0.2361 | 0.3899 |
| BL | BM25 | **0.5944** | **0.5444** | **0.5139** | **0.2757** | **0.2522** | **0.4041** |
| BL | LM | 0.5306 | 0.5000 | 0.4676 | 0.2561 | 0.2306 | 0.3769 |
| SW | TF-IDF | 0.6056 | 0.5250 | 0.5111 | 0.2673 | 0.2424 | 0.3963 |
| SW | BM25 | 0.6000 | 0.5389 | 0.5148 | 0.2799 | 0.2567 | 0.4081 |
| SW | LM | 0.5306 | 0.5181 | 0.4796 | 0.2614 | 0.2353 | 0.3799 |

Interpretation:

- BM25 is the strongest raw baseline among the three models.
- Stop-word removal changes results only modestly.
- Different metrics do not always move in the same direction.

### 9.2 Structure

| Configuration | Model | P@5 | P@10 | P@15 | 11pt-avg | MAP | bpref |
|---|---|---:|---:|---:|---:|---:|---:|
| ST | TF-IDF | 0.5861 | 0.5625 | 0.5565 | 0.3259 | 0.3044 | 0.3981 |
| ST | BM25 | 0.5833 | **0.5819** | **0.5620** | **0.3357** | **0.3149** | 0.4039 |
| ST | LM | 0.5417 | 0.5139 | 0.5000 | 0.3016 | 0.2779 | 0.3612 |
| ST SW | TF-IDF | 0.6056 | 0.5736 | 0.5565 | 0.3311 | 0.3102 | 0.4028 |
| ST SW | BM25 | **0.6111** | **0.5833** | 0.5583 | **0.3379** | **0.3186** | **0.4075** |
| ST SW | LM | 0.5556 | 0.5222 | 0.5000 | 0.3047 | 0.2813 | 0.3651 |

Interpretation:

- structure increases MAP and several precision measures;
- `bpref` changes much less;
- the authors explicitly warn that this gain is an inherent characteristic of the test collection.

### 9.3 Fixed-prefix truncation

| Prefix | Model | P@5 | P@10 | P@15 | 11pt-avg | MAP | bpref |
|---|---|---:|---:|---:|---:|---:|---:|
| 3 | TF-IDF | 0.3594 | 0.4639 | 0.4306 | 0.2180 | 0.1912 | 0.3972 |
| 3 | BM25 | 0.4389 | 0.4208 | 0.4019 | 0.2223 | 0.1989 | 0.3634 |
| 3 | LM | 0.3244 | 0.4194 | 0.3667 | 0.2161 | 0.1953 | 0.3426 |
| 4 | TF-IDF | 0.6111 | 0.5667 | 0.5407 | 0.3225 | 0.3032 | 0.4364 |
| 4 | BM25 | **0.6194** | **0.5917** | **0.5537** | 0.3385 | 0.3213 | **0.4462** |
| 4 | LM | 0.5583 | 0.5333 | 0.5009 | **0.3389** | **0.3242** | 0.4058 |
| 5 | TF-IDF | **0.6361** | **0.6083** | 0.5639 | 0.3451 | 0.3278 | 0.4374 |
| 5 | BM25 | 0.6333 | 0.6014 | **0.5704** | 0.3566 | 0.3396 | **0.4439** |
| 5 | LM | 0.5722 | 0.5292 | 0.5231 | **0.3605** | **0.3411** | 0.4024 |

Interpretation:

- 3-prefix is too aggressive for BM25 and worsens major metrics relative to BL;
- 4-prefix produces the highest BM25 `bpref` among the prefix variants;
- 5-prefix gives stronger BM25 MAP and top-k precision in several cases;
- the pattern is strikingly similar to Can et al., but both works use the same Milliyet collection.

### 9.4 Snowball vs Zemberek

| Stemmer | Model | P@5 | P@10 | P@15 | 11pt-avg | MAP | bpref |
|---|---|---:|---:|---:|---:|---:|---:|
| Snowball | TF-IDF | 0.5556 | 0.5319 | 0.5065 | 0.2945 | 0.2755 | 0.4039 |
| Snowball | BM25 | 0.5583 | 0.5306 | 0.5083 | 0.3055 | 0.2865 | 0.4104 |
| Snowball | LM | 0.4944 | 0.4667 | 0.4509 | 0.2726 | 0.2520 | 0.3642 |
| Zemberek | TF-IDF | 0.6083 | 0.5903 | **0.5676** | 0.3506 | 0.3336 | 0.4534 |
| Zemberek | BM25 | **0.6167** | **0.5944** | **0.5676** | **0.3585** | **0.3440** | **0.4603** |
| Zemberek | LM | 0.5361 | 0.5278 | 0.5093 | 0.3513 | 0.3350 | 0.4114 |

Interpretation:

- Zemberek is numerically stronger than Snowball across the reported models/metrics;
- BM25 + Zemberek is the strongest BM25 morphology configuration by MAP and `bpref`;
- Snowball gives only a small `bpref` improvement over raw BM25;
- simple 4/5-prefix truncation remains competitive with Zemberek.

### 9.5 Compound nouns

| Configuration | Model | P@5 | P@10 | P@15 | 11pt-avg | MAP | bpref |
|---|---|---:|---:|---:|---:|---:|---:|
| CN | TF-IDF | 0.5278 | 0.4764 | 0.4296 | 0.2206 | 0.1965 | 0.3797 |
| CN | BM25 | 0.5583 | 0.4972 | 0.4583 | 0.2533 | 0.2310 | 0.4144 |
| CN | LM | 0.5389 | **0.5069** | **0.4907** | **0.2952** | **0.2735** | **0.4180** |
| CN S | TF-IDF | **0.5833** | **0.5542** | **0.5241** | 0.3043 | 0.2836 | **0.4383** |
| CN S | BM25 | 0.5500 | 0.5444 | 0.5167 | 0.3143 | 0.2971 | 0.4372 |
| CN S | LM | 0.5639 | 0.5333 | 0.5231 | **0.3518** | **0.3351** | 0.4159 |
| CN S I | TF-IDF | 0.5694 | **0.5556** | 0.5259 | 0.3129 | 0.2934 | 0.4407 |
| CN S I | BM25 | **0.5694** | 0.5486 | **0.5306** | 0.3227 | 0.3030 | **0.4472** |
| CN S I | LM | 0.5194 | 0.5167 | 0.5065 | **0.3411** | **0.3249** | 0.4086 |

Interpretation:

- compound-noun enrichment is not uniformly beneficial;
- plain CN worsens TF-IDF MAP and BM25 MAP relative to their raw baselines, while LM benefits more consistently;
- adding structure improves several compound-noun configurations;
- `ignore.low.idf` improves BM25 `bpref` in this configuration but reduces LM effectiveness relative to CN S;
- the authors conclude that the classical LM formulation is more sensitive to added linguistic analysis.

### 9.6 BM25 summary

| BM25 configuration | MAP | bpref |
|---|---:|---:|
| Baseline | 0.2522 | 0.4041 |
| Stop words | 0.2567 | 0.4081 |
| Structure | 0.3149 | 0.4039 |
| Structure + stop words | 0.3186 | 0.4075 |
| 3-prefix | 0.1989 | 0.3634 |
| 4-prefix | 0.3213 | 0.4462 |
| 5-prefix | 0.3396 | 0.4439 |
| Snowball | 0.2865 | 0.4104 |
| **Zemberek** | **0.3440** | **0.4603** |
| CN | 0.2310 | 0.4144 |
| CN S | 0.2971 | 0.4372 |
| CN S I | 0.3030 | 0.4472 |

The central morphology result for the current PhD is therefore:

> More sophisticated morphology can help BM25 substantially, but simple normalization remains a strong control and must not be dismissed without direct testing.

## 10. Statistical evidence

This section is one of the most important methodological cautions.

- The paper reports metric values but **does not report a paired significance test** for the comparisons.
- In the discussion, the authors use wording such as stop words having “no significant influence”, but they do not report a paired t-test supporting that statement.
- The authors explicitly list using the **paired t-test for statistical significance testing** as future work.
- No confidence intervals are reported.
- No repeated runs/seeds are relevant in the modern neural sense because these are deterministic classical retrieval experiments.
- There is no ablation isolating why Zemberek outperforms Snowball.
- There is no statistical test proving that Zemberek is significantly better than 4-prefix or 5-prefix.
- No per-query error analysis is reported comparable to what would be expected in a modern query-type study.

Therefore all superiority claims in this card are phrased as **numerical / reported effectiveness differences**, not statistically established universal dominance.

## 11. Strengths

1. Directly evaluates BM25 on the large Milliyet Turkish collection.
2. Uses the same collection as Can et al., enabling controlled historical comparison.
3. Compares three retrieval models under multiple linguistic representations.
4. Tests both very simple and language-aware morphology processing.
5. Includes stop words, field structure and phrase/compound enrichment rather than only stemming.
6. Uses `bpref`, appropriate for incomplete relevance judgments.
7. Shows that retrieval-model choice and preprocessing interact.
8. Provides evidence that simple normalization can be a strong baseline even when a more sophisticated morphology-aware tool is available.
9. Explicitly recognizes limits of the stemming-vs-truncation conclusion.

## 12. Limitations

### Limitations stated by the authors

- document/query structure gain is partly inherent to the test collection;
- despite stemming performing better numerically than truncation in their discussion, they do not claim stemming is definitively more adequate for Turkish IR;
- more stemming experiments are needed;
- compound-noun extraction should use more patterns;
- compound-noun informativeness/weights need further study;
- different smoothing methods need evaluation;
- paired t-testing is future work.

### Limitations inferred from the design

1. **One language:** Turkish.
2. **One collection/domain:** Milliyet news.
3. **Same collection as Can et al.:** not an independent cross-dataset replication.
4. **Incomplete relevance judgments:** metric interpretation requires care.
5. **No held-out tuning protocol:** parameter/configuration exploration and final evaluation are not separated in a modern dev/test design.
6. **No paired significance test:** small differences cannot be treated as established superiority.
7. **Zemberek causal attribution is not isolated:** dictionary, morphology rules and implementation all differ from Snowball.
8. **Compound-noun extraction uses only three POS patterns:** candidate quality is not independently validated.
9. **No modern semantic retrieval:** embeddings, dense retrievers and Transformers are outside scope.
10. **No hybrid lexical–semantic retrieval.**
11. **Classical LM terminology:** the LM here is not a modern neural language model/retriever.
12. **Potential model/metric interaction:** conclusions can change depending on MAP, `bpref`, or top-k precision.

## 13. What the work proves

Within the Milliyet/Terrier setting, the work supports the following claims:

1. BM25 is a strong lexical baseline relative to the TF-IDF and classical LM formulations used in the raw configuration.
2. Turkish linguistic preprocessing can materially change BM25 effectiveness.
3. Morphology-related normalization is one of the strongest preprocessing factors in the reported BM25 experiments.
4. 3-prefix truncation is too aggressive in this setting and can reduce retrieval effectiveness.
5. 4/5-prefix truncation provides strong BM25 results and is a meaningful low-cost baseline.
6. Zemberek produces higher reported BM25 MAP and `bpref` than Snowball and the tested prefix variants.
7. More sophisticated linguistic processing does not make simpler baselines irrelevant.
8. Stop-word removal alone changes effectiveness only modestly in the reported runs.
9. Compound-noun augmentation has model/configuration-dependent effects.
10. Preprocessing should be evaluated jointly with the retrieval model rather than assumed to have a model-independent effect.

## 14. What the work does NOT prove

The paper does **not** prove that:

- Zemberek is universally better than truncation;
- Zemberek's improvement is caused specifically by the root dictionary;
- morphology-aware stemming is statistically significantly better than 4/5-prefix;
- Snowball is generally ineffective for Turkish IR;
- stop words have statistically proven zero effect;
- 4-prefix or 5-prefix is optimal outside Milliyet;
- fixed-prefix truncation is appropriate for Uzbek;
- Zemberek transfers to Uzbek;
- longer or structured queries are universally better;
- compound nouns always improve BM25;
- the classical LM's sensitivity implies anything about modern neural language models;
- morphology improves dense semantic retrieval;
- morphology improves lexical–semantic hybrid retrieval;
- the results establish how query characteristics should control hybrid fusion;
- the Turkish numerical results can be directly transferred to Uzbek.

## 15. Relationship to current Uzbek evidence

Uzbek research already contains:

- tokenization/stemming/lemmatization studies;
- morphological analyzers and morpholexicons;
- search-oriented morphology processing.

Haddad & Bechikh Ali contributes a missing comparative lesson:

> A morphology resource should not be judged only by linguistic sophistication; its value must be measured in an actual ranking task against raw and simple-normalization baselines.

For Uzbek, the appropriate transfer is therefore methodological:

`raw lexical representation`
vs
`simple normalization`
vs
`stemming`
vs
`lemmatization`

under the **same BM25 implementation and tuning protocol**.

The Turkish results do not justify choosing the Uzbek morphology method in advance.

## 16. Relationship to CURRENT_GAP

**Status:** supports; does not close; does not contradict; suggests experimental controls.

The current gap asks how morphology-aware lexical representation and Uzbek query characteristics affect the relative and joint effectiveness of lexical and semantic retrieval.

This paper strengthens the lexical side by showing that:

- BM25 performance changes materially with morphology-related representation;
- simple and sophisticated morphology variants can be surprisingly close;
- preprocessing effects differ across retrieval models and metrics.

But it does not evaluate:

- Uzbek;
- modern dense semantic retrieval;
- lexical–semantic complementarity;
- hybrid fusion;
- query-type-dependent hybrid behavior.

Therefore:

> **Keep CURRENT_GAP unchanged.**

## 17. Implications for our research design

### 17.1 Lexical baseline family

At minimum:

`BM25_raw`

`BM25_simple-normalization`

`BM25_stem`

`BM25_lemma`

The simple-normalization baseline may be prefix-based or another transparent low-cost normalization appropriate to Uzbek; it should be included as a control, not assumed to be the final method.

### 17.2 Same retrieval model and tuning protocol

Morphology variants must be compared under:

- the same BM25 implementation;
- the same corpus;
- the same query set;
- the same BM25 tuning protocol.

Otherwise morphology and model effects become confounded.

### 17.3 Semantic stage

After the lexical family is established, use one fixed modern semantic retriever to compare:

`Semantic`

`BM25_raw + Semantic`

`BM25_stem + Semantic`

`BM25_lemma + Semantic`.

The purpose is to measure whether morphology changes **complementarity**, not merely standalone BM25 effectiveness.

### 17.4 Query analysis

Report not only overall averages but per-query/category behavior, including candidate factors already present in CURRENT_GAP:

- query length;
- morphological complexity;
- rare terms;
- named entities;
- numeric identifiers;
- Latin/Cyrillic variation;
- lexical overlap;
- paraphrastic wording.

### 17.5 Metrics

Use modern effectiveness metrics such as:

- nDCG@k;
- MAP;
- Recall@k;
- MRR where appropriate.

Also include:

- paired significance testing;
- confidence intervals or robust uncertainty estimates where applicable;
- per-query analysis.

### 17.6 Experimental hygiene

Separate:

- tuning/development data;
- final test data.

Do not choose:

- morphology parameters;
- stem lengths;
- BM25 parameters;
- fusion weights

on the final test set.

### 17.7 Compound nouns / multiword terms

Treat compound/multiword lexical units as an optional extension or ablation, not as part of the core method at the outset.

The main PhD question should remain identifiable:

> How does morphology-aware lexical representation change lexical–semantic complementarity?

Adding morphology, phrases, script normalization and semantic fusion simultaneously would make causal interpretation difficult.

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| Preprocessing | Подготовка текста до индексирования | Text normalization/transformation before indexing and retrieval |
| Baseline | Исходный вариант для сравнения | Reference retrieval configuration |
| Fixed-prefix truncation | Оставить первые `n` символов | Deterministic pseudo-stemming by prefix length |
| Overstemming | Слишком сильное объединение разных слов | Excessive stemming that conflates semantically different terms |
| Understemming | Недостаточное объединение форм одного слова | Insufficient normalization of morphological variants |
| Affix stripping | Удаление аффиксов по правилам | Rule-based stripping of inflectional/derivational suffixes |
| Root dictionary | Словарь базовых корневых форм | Lexicon used by morphology-aware analysis |
| Zemberek | Турецкий NLP-инструмент с морфологическим анализом | Root-dictionary-based Turkish NLP/morphology framework used here as a lemmatizer-based stemmer |
| Snowball | Правиловый стеммер без словарного поиска | Affix-stripping stemming implementation |
| Compound noun | Составное именное выражение | Multiword nominal candidate treated as an additional lexical index term |
| POS tagging | Определение части речи каждого слова | Assignment of syntactic/part-of-speech labels |
| bpref | Метрика для неполной разметки | Preference-based IR measure using judged documents |
| Paired t-test | Проверка устойчивости разницы двух систем по одним и тем же запросам | Paired statistical test over per-query effectiveness values |
| Ablation | Убрать один компонент и проверить его вклад | Controlled component-removal experiment |
| Language Model (LM) retrieval | Вероятностная модель документа/запроса | Classical statistical language-model IR formulation, not a modern neural LLM |

## 19. Open questions / verification needed

1. Which Uzbek stemmers/lemmatizers are reproducible and suitable for controlled BM25 evaluation?
2. What should serve as the transparent simple-normalization baseline for Uzbek?
3. Does Uzbek morphology-aware normalization improve BM25 consistently across domains?
4. Are gains concentrated in short or morphologically complex queries?
5. How do Latin/Cyrillic and apostrophe normalization interact with stemming/lemmatization?
6. Does semantic retrieval compensate for morphology-related lexical mismatch?
7. Does stronger lexical normalization reduce or increase lexical–semantic complementarity?
8. Does raw BM25 retain unique exact-match evidence that is lost after morphology normalization?
9. Should multiword Uzbek terms be tested as a later lexical ablation?
10. Can a new Uzbek evaluation avoid Milliyet-style incomplete-pool bias by using a diverse pool containing lexical, morphology-aware, semantic and hybrid systems?

## 20. Decision after deep dive

- **Keep current gap?** Yes.
- **Modify gap?** No.
- **Add decision?** No permanent method choice yet.
- **Add experiment?** Yes:
  - `BM25_raw ↔ BM25_simple-normalization ↔ BM25_stem ↔ BM25_lemma`;
  - paired significance tests;
  - per-query/category analysis;
  - then compare each lexical representation with the same semantic retriever.
- **Add citation to Chapter I?** Yes, section 1.1.
- **Priority after deep dive:** VERY HIGH.
- **Role in literature argument:** direct Turkic-language evidence that morphology-aware lexical representation affects BM25, while simple baselines remain necessary.
- **Does it establish hybrid novelty?** No.
- **Does it close the current Uzbek gap?** No.

### Final retained conclusion

> Haddad & Bechikh Ali extend the Milliyet Turkish IR evidence to BM25 and show that morphology-related preprocessing can materially improve lexical ranking, with Zemberek producing the strongest reported BM25 MAP and `bpref` among the tested variants. At the same time, simple 4/5-prefix normalization remains highly competitive, preprocessing effects differ by retrieval model and metric, and the paper does not provide paired significance testing or any modern semantic/hybrid evaluation. For the Uzbek PhD, the correct consequence is a controlled `raw/simple/stem/lemma` BM25 comparison followed by explicit measurement of how each lexical representation changes complementarity with the same semantic retriever.
