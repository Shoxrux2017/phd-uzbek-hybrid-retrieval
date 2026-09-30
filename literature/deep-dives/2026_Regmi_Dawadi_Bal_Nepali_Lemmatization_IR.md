# Regmi, Dawadi & Bal (2026): Nepali Lemmatization with Multilingual Transformers: Intrinsic and Extrinsic Evaluation in a Low-Resource Setting

**Targeted deep-dive status:** COMPLETED (AI-assisted, pending researcher review)
**Completed:** 2026-09-28
**Literature ID:** `MORPH-009` (assigned 2026-09-28, approved by researcher)
**Systematic-review record:** `CR000218`. Full-text triage: INCLUDE, reading priority STANDARD, reading tier 1, `carries_complementarity_evidence = NO`
**Provenance:** AI-assisted deep dive (Claude). The whole 8-page paper was read (text extraction, pp. 3462–3469). Page images were checked for p. 3462 (Table 1, abstract), p. 3465 (Table 2, zoomed), p. 3466 (Table 3, Secs. 5.2.2–5.2.3) and p. 3467 (Tables 4 and 5, Table 5 zoomed). Every number below has its table/section and printed page. Numbers computed by us are marked **[computed]** (Python, 2026-09-28).
**Source rule:** **the paper is the primary and only authoritative source.** The code repository and Hugging Face models named in Sec. 9 were **not** consulted. Web access was used only to check the bibliographic record (ACL Anthology). Such items are marked "(bibliographic check: ACL Anthology)".
**Verification:** independent AI verifier pass 2026-09-28; 9 findings addressed.
**Reliability:** **B**. The venue is peer-reviewed (LREC 2026 main proceedings, ACL Anthology), so the source *type* is A-level. We grade it B for the retrieval claims this project uses, because:
- retrieval is a small secondary extrinsic evaluation (one subsection, one table);
- the retrieval protocol is underspecified;
- the abstract and Table 5 disagree on the metric name;
- the printed accuracies do not fit the stated 600 queries (§9, §19).
The researcher may prefer A for the venue with a scope note, as in the MORPH-004 card.

---

## Кратко для исследователя (RU)

- **Что сделано.** Для непальского (индоарийский язык, письмо деванагари, богатая словоизменительная морфология) авторы:
  - дообучили три многоязычные модели «последовательность → последовательность» (mT5-base, mT5-small, mBART-large-50) как **лемматизаторы на уровне отдельных слов**, без контекста; набор из 8 000 пар «словоформа–лемма» (обучение на 80 %, ≈6 400 пар [вычислено]);
  - проверили их внутренне (CER, accuracy, символьный BLEU, «морфологическое покрытие»);
  - проверили их внешне на двух задачах: межъязыковое сопоставление слов хинди–непали и информационный поиск «заголовок новости → фрагмент статьи».
- **Лемматизаторы** (Table 2, p. 3465): точность 96,1 % (mT5-base), 96,0 % (mBART), 95,2 % (mT5-small). На отдельном наборе из 700 словарных (базовых) форм, по 100 на 7 частей речи, модель ошибается в 23,8 % случаев. Какая из трёх моделей, не указано («The model»). 63,4 % ошибок приходятся на слова с нулевой частотой в корпусе. По примерам в Table 3 модель «перетягивает» редкие слова к частым леммам; доля ошибок каждого типа не приводится (Sec. 5.1, Table 3).
- **Поиск (Table 5, p. 3467).** Лексические модели: только TF-IDF и «бинарный индекс». Два варианта представления: исходные словоформы и леммы (двумя лемматизаторами).
  - Бинарный индекс: Acc@1 0,6317 → 0,8574 (mBART), +35,7 % отн. [пересчитано ✓]; MAP@5 0,7159 → 0,9064.
  - TF-IDF: Acc@1 0,4984 → 0,5533; MAP@5 0,6243 → 0,6594. Acc@5 для mBART не изменился (0,7821 = 0,7821).
  - Эффект лемматизации сильно зависит от лексической модели: для бинарного индекса он в 4–5 раз больше, чем для TF-IDF (по Acc@1) [вычислено].
- **Чего нет** (все измерения нашего gap):
  - **нет BM25**;
  - нет стемминга (лемматизацию называют «альтернативой стеммингу», но стеммер не сравнивается);
  - нет плотного поиска и гибрида;
  - нет перекрытия результатов, уникально найденных документов, oracle union;
  - нет разбора по запросам и признакам запросов;
  - нет проверки статистической значимости.
- **Протокол поиска описан слабо** (NOT_REPORTED):
  - функция ранжирования для TF-IDF и формула «бинарного индекса»;
  - размер коллекции и определение релевантности (по смыслу — один «свой» фрагмент на заголовок, т.е. known-item);
  - лемматизировались ли и запросы, и документы;
  - список стоп-слов.
- **Внутренние несоответствия:**
  - в аннотации «MAP@1 0,71 → 0,90», но в Table 5 MAP@1 нет: 0,7159 → 0,9064 — это **MAP@5**;
  - все 12 значений Acc@1/Acc@5 в Table 5 (6 строк) точно ложатся на знаменатель **638**, а не на 600 заявленных заголовков. Для Table 4 аналогично выходит 3 189, а не 3 000 [вычислено, вывод наш];
  - фраза «лемматизация стабильно улучшает» не выполняется для TF-IDF/mBART по Acc@5;
  - контрольная точка выбиралась по evaluation loss, отдельной dev-выборки не описано.
- **Для нашего gap:** работа подтверждает уже закрытый тезис: «raw vs lemma в поиске на языке с ограниченными ресурсами уже сравнивали». Остаточное ядро v0.8 (raw/stem/lemma BM25 × фиксированный D → overlap/unique hits → прирост гибрида → признаки запросов) **не затрагивает**. Предложение: gap не менять.
- **Практическая польза для нас:**
  1. Нейросетевой лемматизатор может «исправлять» редкие слова и имена в частые леммы. Это ошибки, которые меняют лексические совпадения. Для BM25_lemma надо измерять долю таких замен в запросах и держать её кандидатом в признаки запроса.
  2. Table 4 показывает: лемматизация только одной стороны сравнения **ухудшает** результат (12,86 % → 10,57 %). Анализатор запросов и индекса должен быть строго одинаковым.
  3. Эффект морфологии зависит от модели взвешивания. Выводы для binary/TF-IDF нельзя переносить на BM25; BM25 нужно проверять самим.
  4. Точность лемматизатора (≈96 %) ≠ эффект в поиске. Отчитываться нужно по обоим отдельно.

---

## 1. Bibliographic record

- **Authors:** Sunil Regmi, Sundeep Dawadi, Bal Krishna Bal
- **Affiliations:** Department of Artificial Intelligence, Kathmandu University (Regmi, Dawadi); Information and Language Processing Research Lab, Department of Computer Science & Engineering, Kathmandu University (Bal) (p. 3462)
- **Year:** 2026
- **Venue:** *Proceedings of the Fifteenth Language Resources and Evaluation Conference (LREC 2026)*, 11–16 May 2026 (printed footer, p. 3462); Palma de Mallorca, Spain (bibliographic check: ACL Anthology)
- **Editors:** Stelios Piperidis, Núria Bel, Henk van den Heuvel, Nancy Ide, Simon Krek, Antonio Toral (bibliographic check: ACL Anthology)
- **Pages:** 3462–3469 (printed footer; confirmed by bibliographic check: ACL Anthology)
- **Publisher:** ELRA Language Resources Association (printed footer)
- **ACL Anthology ID:** `2026.lrec-1.275` (bibliographic check: ACL Anthology)
- **DOI:** `10.63317/2o6euz7qakr5` (as given in the ACL Anthology BibTeX; bibliographic check: ACL Anthology. We did not resolve the DOI itself)
- **Official record:** https://aclanthology.org/2026.lrec-1.275/
- **Code / models (stated in paper, Sec. 9):** https://github.com/sunilRegmi-ai/Nepali-Lemmatizer; https://huggingface.co/sunilregmi/nepali-lemmatizerV1-mT5-base (not consulted)
- **IR data source (stated in paper, Sec. 12):** Disisbig (2025), *Nepali News Dataset*, Kaggle
- **Source type:** peer-reviewed conference paper (8 printed pages, including references, ethics and data-availability sections)
- **Reliability:** B (see header)
- **Full text available:** yes (`07_full_text/pdfs/CR000218.pdf`, 8 pages)

## 2. Why this work matters to the PhD

It is a recent (2026) peer-reviewed example where a **neural lemmatizer is evaluated extrinsically on retrieval** in a morphologically rich, low-resource language. It compares an unlemmatized and a lemmatized lexical representation on the same queries and documents.

| Axis | Relation |
|---|---|
| Lexical retrieval | TF-IDF and "binary term indexing" only; **no BM25**. Ranking functions not specified |
| Morphological representation | Raw (whitespace tokens after stop-word removal) vs lemma (mT5-base lemmatizer; mBART-large-50 lemmatizer). **No stem condition** |
| Semantic retrieval | **Absent** from the IR task. The mT5/mBART models are used only as lemmatizers, not as retrievers. FastText embeddings appear only in the separate cross-lingual word-alignment task |
| Hybrid retrieval | **Absent** |
| Uzbek morphology | Indirect. Nepali is Indo-Aryan, with inflection and postpositional suffixation (e.g., घरमा *gharamā* 'in the house' → घर *ghara*, p. 3462). Uzbek is Turkic and agglutinative. Both are mainly suffixing |
| Low-resource retrieval | Direct: small data, 600-headline known-item style task |
| Current gap | Touches only the already-occupied "raw vs lemma in low-resource IR" element; nothing on complementarity (§16) |

## 3. Research problem

### Simple explanation

Nepali words change form a lot: one verb has many inflected forms, and nouns attach case endings. Older Nepali lemmatizers rely on rules and dictionaries, and they fail on unknown or misspelled words. The authors ask whether large multilingual text-to-text models can learn to turn any word form into its dictionary form, and whether doing so helps two applications, one of which is search.

### Formal formulation

- **Lemmatization as sequence-to-sequence generation:** learn `g: w → l`, mapping an inflected word `w` to its lemma `l` from input "lemmatize: <word>" (Sec. 3.2, p. 3464).
- The paper lists three contributions (p. 3463):
  1. systematic evaluation of multilingual encoder–decoder models for Nepali lemmatization;
  2. mT5 vs mBART comparison;
  3. "An extrinsic evaluation via cross-lingual alignment and information retrieval improvements".
- **IR sub-question (implicit, Sec. 5.2.3):** for a fixed lexical model M ∈ {TF-IDF, binary index}, does replacing tokens by predicted lemmas raise Acc@1, Acc@5 and MAP@5 on headline → snippet matching?

## 4. Main idea

### Simple explanation

Teach a multilingual translation-style model to "translate" a Nepali word into its lemma, using a dataset of 8,000 word–lemma pairs, of which 80% (≈6,400 **[computed]**) are used for training. Then run the lemmatizer over search text and check whether a news headline finds its own article more often.

### Concrete example

- Paper's morphology example (Table 1, p. 3462): गर्छ *garchha* 'does', गरेको *gareko* 'did/done' and गर्दै *gardai* 'doing' all map to गर्नु *garnu*.
- IR example: the paper gives no concrete IR query. Its motivation is that "headlines often use abbreviated or inflected forms that need to be matched against the differently-inflected forms in the main text body" (Sec. 5.2.3.1, p. 3466).
- Illustration (ours, not from the paper): if a headline contains an inflected form of गर्नु and the article uses a different inflected form of the same verb, raw exact matching sees no shared term, while lemmatized matching does.

### Formal method

- Fine-tune pretrained encoder–decoder models on (prompt, lemma) pairs. The loss function is not named. The paper says only that padding token IDs were set to −100 "to exclude them from loss computation" (Sec. 3.2, p. 3464). Context (not from the paper): −100 is the ignore index of the Hugging Face default token-level cross-entropy.
- **IR step:**
  - tokens `t` in text x (query/document) → `g(t)`;
  - index with model M;
  - rank the snippets for each headline.
- Whether `g` is applied to queries, documents or both is not stated explicitly: "compared the IR performance on the original (unlemmatized) text and the lemmatized text" (Sec. 5.2.3.2, p. 3466).

## 5. Architecture / algorithm

1. **Data preparation** (Sec. 3.2, p. 3464):
   - instruction-style prompt "lemmatize: <word>";
   - SentencePiece boundary marker inserted;
   - Unicode NFC normalization of Devanagari;
   - SentencePiece tokenization;
   - maximum sequence length 32.
2. **Models** (Sec. 3.3, p. 3464):
   - mT5-base (∼580M parameters);
   - mT5-small (∼300M);
   - mBART-large-50 (∼610M).
   - Hugging Face Transformers. The text says "two multilingual sequence-to-sequence models were employed" and then lists three checkpoints of two architectures (minor wording issue).
3. **Training** (Sec. 4, p. 3465):
   - NVIDIA Tesla T4 GPUs;
   - grid: learning rate {1e-5, 5e-5, 1e-4, 5e-4} × batch {2, 4, 8, 16}, 5–20 epochs;
   - AdamW, weight decay 0.01, gradient clipping.
   - "The best checkpoint was selected by the lowest evaluation loss."
   - Reported best settings: mT5-base lr 5e-4, batch 16; mBART lr 1e-5 (Sec. 5, p. 3465).
   - Primary metric: CER.
4. **IR pipeline** (Sec. 5.2.3.2, p. 3466):
   - "a standard stopword removal" (list NOT_REPORTED);
   - whitespace tokenization;
   - two "IR baselines": TF-IDF vectorization and binary term indexing.
   - NOT_REPORTED: scoring/similarity function, library, term weighting variant, how ties are broken, and BM25 parameters (no BM25 is used).
   - Lemmatizers used in IR: mT5-base and mBART-large-50; mT5-small is not used in IR.
5. **Cross-lingual alignment** (Sec. 5.2.2, pp. 3466–3467):
   - VecMap over FastText Hindi and Nepali word vectors;
   - candidate Nepali words compared with a gold Nepali word, raw or lemmatized on one or both sides.
   - This is word translation retrieval, **not** document retrieval.

## 6. Data

### Lemmatization data (Sec. 3.1, p. 3464)

- **Sources:**
  - 5,000 gold word–lemma pairs from the public NepaliLemmatizer dataset (dpakpdl, 2025);
  - plus 3,000 pairs "based on common Nepali morphological transformation rules and suffix variations", manually verified by one native speaker with a linguistic background.
- **Total:** 8,000 unique pairs.
- **Split:** 80/20 train/evaluation, with no overlap. This gives ≈6,400 / 1,600 pairs **[computed]**.
- No separate dev split is described.
- **Error-analysis set:** 700 dictionary words (100 per each of 7 POS) from *Pragya Nepali Brihat Shabdakosh*, where the input is its own gold lemma. Frequencies come from FineWeb2.

### IR data (Sec. 5.2.3.1, p. 3466)

- **Dataset / corpus:** "600 randomly selected Nepali news headlines and their corresponding article snippets", from the Kaggle Nepali News Dataset (Disisbig, 2025).
- **Language / domain:** Nepali; open-domain news.
- **Queries:** headlines; 600 stated. The printed Table 5 accuracies are consistent with 638, not 600, evaluated items (§9) **[computed]**.
- **Documents:** article snippets. Collection size NOT_REPORTED (presumably the 600 snippets). Snippet length NOT_REPORTED.
- **Relevance judgments:** NOT_REPORTED explicitly. By construction ("headline-to-content matching") each headline's own snippet is the target, i.e., a single positive per query, known-item style. No human qrels.
- **Train/dev/test:** the task is used only for evaluation: "These tasks were used exclusively for extrinsic evaluation and did not influence lemmatizer training" (Sec. 5.2.1, p. 3466). No IR parameters are tuned.

### Cross-lingual alignment data (Sec. 5.2.2.1, p. 3466)

- 14,500 Hindi–Nepali dictionary pairs (Shivaramakrishna, 1977) for VecMap supervision.
- 3,000 validation pairs from a synthetic Nepali–Hindi parallel corpus, with exact translation matches excluded.

## 7. Baselines

| Baseline | What it is | Why selected | Fair comparison? |
|---|---|---|---|
| Unlemmatized TF-IDF | Term-weighted vector matching over whitespace tokens after stop-word removal | Standard lexical reference | Within-model yes: same model, only the representation changes. But the similarity function is NOT_REPORTED |
| Unlemmatized binary index | Presence/absence term matching; scoring rule NOT_REPORTED | Exact-match reference, "highly sensitive to morphological variation" (p. 3467) | Within-model yes. Unusually, it outperforms TF-IDF in all three representations (Acc@1 +0.133 to +0.304 **[computed]**). This is atypical and unexplained, and suggests implementation specifics we cannot check |
| mT5-base vs mBART lemmatizer | Two neural lemmatizers | Compare lemmatizers extrinsically | Yes (same IR pipeline) |
| Rule-based / TRIE Nepali stemmers or lemmatizers (cited in Sec. 2) | Prior Nepali tools | — | **Not compared** in IR or in intrinsic tables. The text says "the consistent superiority of neural methods across all metrics" (p. 3465) while admitting "direct comparison is limited by differing evaluation datasets". No prior-method numbers are in any table. The only prior figure is textual: earlier TRIE/hybrid affix-removal approaches "achieved up to 90% accuracy on curated datasets" (Sec. 2, p. 3463), on data not comparable with Table 2 |
| BM25, dense, hybrid | — | — | **Absent** |

## 8. Metrics

| Metric | Definition | Simple meaning here | Appropriate? |
|---|---|---|---|
| Accuracy (lemmatization) | exact match of predicted and gold lemma | share of words lemmatized exactly right | Yes |
| CER | character edit distance / reference length | how many characters are wrong, on average | Yes (authors' primary metric) |
| BLEU (Char) | character n-gram BLEU | partial-credit similarity | Supplementary |
| Morphological coverage | whether the last three characters of the prediction match the gold lemma (Sec. 3.4, p. 3464) | crude check of the lemma ending | Heuristic; the authors call it "a simple heuristic" |
| Acc@1 / Acc@5 (IR) | share of queries whose target snippet is at rank 1 / in the top 5 | hit rate at 1 and 5 | Yes for known-item search |
| MAP@5 (IR) | mean average precision cut at 5. Context (not from the paper): with one relevant item per query it equals MRR@5, i.e., 1/r if r ≤ 5 | "how high is the right snippet, if in top 5" | Yes, but adds little beyond Acc@k with one positive |
| Acc@1 / Acc@5 / MAP@5 (alignment) | whether the gold word is among the VecMap top-1 / top-5 candidates | word-translation hit rate | Word-level; not document IR |

Consistency check **[computed]**: with a single relevant item, MRR@5 must lie between Acc@1 + (Acc@5 − Acc@1)/5 and Acc@1 + (Acc@5 − Acc@1)/2. All six Table 5 rows satisfy this. This is consistent with (not proof of) a one-target-per-query setup.

Significance testing: **none** (§10).

## 9. Results

### Table 2: intrinsic lemmatization (p. 3465; checked on page image)

| Metric | mBART-large-50 | mT5-small | mT5-base |
|---|---:|---:|---:|
| CER | 0.016 | 0.017 | **0.011** |
| Accuracy | 0.960 | 0.952 | **0.961** |
| BLEU (Char) | **0.986** | 0.983 | 0.980 |
| Morph. Coverage | **0.970** | 0.955 | 0.964 |

- Test set ≈1,600 pairs **[computed]**.
- The difference in accuracy between mT5-base and mBART is 0.001, i.e., ≈2 words out of 1,600 **[computed]**. It cannot be distinguished without a test.

### Sec. 5.1 / Table 3: error analysis (pp. 3465–3466)

- Failure rate "23.8% (167 out of 700 words)" **[computed: 23.86%, which rounds to 23.9%]**.
- "106 of the 167 failed words (63.4%)" had zero corpus frequency **[computed: 63.47%]**.
- The model used for this analysis is not named ("The model").
- Table 3 shows four failure types: Frequency Bias (उसिन्निनु *usinninu* → उनी *unī*, 1.2M), POS Ambiguity, Overstemming (*kaṭagranthi* → *kaṭagra*), Contextual Omission (postposition *khātira* → verb *khānu*).
- The authors' reading is that the model "aggressively overwrites" rare or unseen lemmas with "orthographically similar, high-frequency stems" (p. 3465).

### Table 4: Hindi–Nepali word alignment (p. 3467; checked on page image)

| Condition | Acc@1 (%) | Acc@5 (%) | MAP@5 |
|---|---:|---:|---:|
| Gold Nepali vs Candidates (raw) | 12.86 | 29.60 | 0.2031 |
| L. Gold vs Candidates (mT5-base) | 10.57 | 17.91 | 0.1338 |
| L. Gold vs L. Candidates (mT5-base) | 40.80 | 59.08 | 0.4809 |
| L. Gold vs Candidates (mBART-50) | 10.38 | 17.81 | 0.1318 |
| L. Gold vs L. Candidates (mBART-50) | **41.61** | **59.99** | **0.4883** |

- "more than doubles the MAP@5 score" (Sec. 5.2.2, p. 3466): 0.4883 / 0.2031 = 2.40× **[computed ✓]**.
- Acc@1 rises 3.24× **[computed]**.
- **One-sided lemmatization hurts:** Acc@1 falls 12.86 → 10.57 / 10.38. The authors explain this as "forcing an unnatural comparison between canonical roots and highly inflected candidate vectors" (Sec. 5.2.2, p. 3466).
- The abstract says this improved "significantly", but no test is reported.
- Denominator check **[computed]**: the ten percentages are not all consistent with 3,000 evaluated pairs (e.g., 12.86% × 3,000 = 385.8). The smallest consistent denominator in 100–5,000 is 3,189. This suggests that the evaluated count differs from the stated 3,000.

### Table 5: IR, headline-to-content matching (p. 3467; checked on page image, zoomed)

| IR method | Preprocessing | Acc@1 | Acc@5 | MAP@5 |
|---|---|---:|---:|---:|
| TF-IDF | Lemmatized (mT5-base) | 0.5345 | 0.7884 | 0.6491 |
| TF-IDF | Lemmatized (mBART) | 0.5533 | 0.7821 | 0.6594 |
| TF-IDF | Unlemmatized | 0.4984 | 0.7821 | 0.6243 |
| Binary index | Lemmatized (mT5-base) | 0.8245 | 0.9467 | 0.8779 |
| Binary index | Lemmatized (mBART) | 0.8574 | 0.9702 | 0.9064 |
| Binary index | Unlemmatized | 0.6317 | 0.8166 | 0.7159 |

Gains of lemma over raw **[computed]**, shown as absolute (relative):

| Model | Lemmatizer | ΔAcc@1 | ΔAcc@5 | ΔMAP@5 |
|---|---|---:|---:|---:|
| TF-IDF | mT5-base | +0.0361 (+7.2%) | +0.0063 (+0.8%) | +0.0248 (+4.0%) |
| TF-IDF | mBART | +0.0549 (+11.0%) | **0.0000** | +0.0351 (+5.6%) |
| Binary | mT5-base | +0.1928 (+30.5%) | +0.1301 (+15.9%) | +0.1620 (+22.6%) |
| Binary | mBART | +0.2257 (+35.7%) | +0.1536 (+18.8%) | +0.1905 (+26.6%) |

Reading the table:
- The text's "+35.7%" = (0.8574 − 0.6317)/0.6317 **[computed: 35.73% ✓]**.
- The morphology effect is **model-dependent**. For Acc@1 it is 4.1–5.3× larger for the binary index than for TF-IDF **[computed: 0.2257/0.0549; 0.1928/0.0361]**. The authors attribute the smaller TF-IDF gain to weighting that "partially compensates for inflectional differences" (p. 3467); this is an explanation, not tested.
- "lemmatization consistently improves retrieval performance across both methods" (p. 3467) does **not** hold for TF-IDF/mBART Acc@5, which is unchanged (0.7821 vs 0.7821).
- "Across both methods, mBART-based lemmatization slightly outperforms mT5-based" holds except for TF-IDF Acc@5 (mT5 0.7884 > mBART 0.7821).
- mBART beats mT5-base by 0.019–0.033 Acc@1 **[computed]**. This is opposite to the intrinsic accuracy order (0.960 vs 0.961). The authors link it to mBART's higher morphological coverage (0.970 vs 0.964).

**Internal inconsistencies:**
1. **Metric name in the abstract.** The abstract says: "In information retrieval, the Mean Average Precision (MAP)@1 using binary index increased from 0.71 to 0.90 using mBART model" (p. 3462). Table 5 reports no MAP@1. 0.7159 → 0.9064 are the **MAP@5** values. Context: under a single relevant item, MAP@1 would equal Acc@1, which is 0.6317 → 0.8574.
2. **Query count** **[computed, our inference]**.
   - With 600 queries, every Acc value must be a multiple of 1/600. The printed values are not: e.g., 0.5345 × 600 = 320.7; 0.6317 × 600 = 379.0 fits, but 0.8574 × 600 = 514.4 does not.
   - The smallest denominator for which **all** twelve printed Acc@1/Acc@5 values are exact 4-decimal roundings of k/n is **n = 638**. For example, 0.5345 = 341/638, 0.8574 = 547/638, 0.9702 = 619/638.
   - Other admissible values are only multiples of 638 up to 3,000.
   - Given 4-decimal precision, a chance fit of all twelve values is very unlikely. The evaluation therefore most likely averaged over 638 items, not 600.
   - The cause is not stated. Possibilities include duplicate headlines, multiple snippets per headline, or a different sample. The paper does not allow a decision.

## 10. Statistical evidence

- **Significance test:** NOT_REPORTED, for both the intrinsic and the extrinsic results. The word "significant(ly)" appears without a test in the abstract ("improved significantly", p. 3462), the Table 4 caption ("the most significant gain", p. 3467) and Sec. 6 ("significantly enhance indexing", p. 3467).
- **Confidence intervals:** NOT_REPORTED.
- **Runs / seeds:** NOT_REPORTED. The results appear to be single runs.
- **Ablation:** none. The hyperparameter grid is described, but grid results are not shown. One-sided vs two-sided lemmatization in Table 4 acts as an informative control for the alignment task only.
- **Per-query analysis:** **none** for IR. There is:
  - no per-query win/loss (raw vs lemma);
  - no list of queries helped or hurt;
  - no overlap / unique-hit analysis between representations;
  - no oracle union;
  - no query-feature breakdown.
  - The only qualitative error analysis concerns the lemmatizer (Table 3), not retrieval.

## 11. Strengths

- Extrinsic evaluation of a lemmatizer in retrieval, with the lexical model held fixed while only the representation changes. The comparison is clean within each model.
- Two lexical models are tested. This shows that the size of the morphology effect depends on the weighting scheme.
- Two lemmatizers are compared extrinsically. Their IR order differs from their intrinsic-accuracy order: intrinsic accuracy is not a sufficient proxy.
- A useful error taxonomy for neural lemmatizers on rare words (Table 3).
- The alignment experiment explicitly shows that asymmetric normalization harms matching.
- Code, data-generation scripts and models are announced as public (Sec. 9).

## 12. Limitations

### Stated by the authors

- "The dataset lacks full morphological diversity and should be considered insufficient but it was valuable for our experiment" (Sec. 7, p. 3467).
- The study "focuses only on word-level lemmatization, excluding contextual dependencies that influence meaning and cross part-of-speech morphological transformations" (Sec. 7).
- POS/polysemy awareness, rare dictionary words, named entities, spelling errors and "proper standard evaluation data" are needed (Sec. 7).
- Without sentential context the model shows a "Corpus Frequency Bias" (Sec. 5.1).
- Direct comparison with prior Nepali lemmatizers is "limited by differing evaluation datasets and preprocessing pipelines" (p. 3465).

### Inferred from the experimental design

1. **No BM25 and underspecified lexical models.** TF-IDF scoring and binary-index scoring are not defined. That binary matching beats TF-IDF by a wide margin in all three conditions is atypical, and may reflect implementation or collection specifics that cannot be checked from the paper.
2. **Small, single-positive, known-item task.** 600 (or 638) headlines, one target each, no human qrels, collection size not stated. Headlines share vocabulary with their own article, which favours lexical matching and may inflate the benefit of any normalization. The direction and size of this bias are unknown.
3. **Query count inconsistency** (600 stated vs 638 implied by the numbers, §9).
4. **No significance testing** on a few hundred queries. Some TF-IDF differences, e.g., mT5 vs mBART Acc@5 0.7884 vs 0.7821 (≈4 queries out of 638 **[computed]**), are within what chance could produce.
5. **Checkpoint selection on the evaluation split.** Only an 80/20 split is described, and the best checkpoint was selected by "the lowest evaluation loss". The intrinsic scores may be mildly optimistic. The IR task was not used for selection, so IR numbers are not affected by this.
6. **Synthetic part of the lemma data.** 3,000 of 8,000 pairs were generated from transformation rules and checked by a single annotator. The test split likely contains such rule-generated pairs, which may be easier than natural forms. The paper gives no breakdown.
7. **Lemmatization scope in IR is unstated:** queries, documents, or both. This matters, given Table 4's evidence that one-sided normalization harms matching.
8. **No stemming baseline**, despite the lemmatization being framed "as a stemming alternative" (p. 3466). The paper cannot say whether lemmatization beats a simple suffix stripper, or prefix truncation as in the Turkish evidence (MORPH-002).
9. **Word-level lemmatization of running text** ignores context, and the error analysis shows frequency-driven overwriting of rare words and named-entity-like tokens. Its effect on retrieval of rare-term queries is not measured.

## 13. What the work proves

- On a small Nepali headline → snippet matching task, replacing raw tokens with neural lemmas **raises** top-rank accuracy for both tested lexical models (Table 5, p. 3467):
  - binary index Acc@1 0.6317 → 0.8574 (mBART);
  - TF-IDF Acc@1 0.4984 → 0.5533 (mBART).
  - Caveats: no significance test, and the query count is unclear.
- **The size of the lemmatization effect depends on the lexical model**: it is much larger for exact binary matching than for TF-IDF (§9) **[computed]**.
- Multilingual seq2seq models reach ≈95–96% exact-match lemmatization accuracy on the authors' 8,000-pair Nepali data (Table 2). On a separate set of 700 dictionary base forms (100 per each of 7 POS; Sec. 3.1), the lemmatizer evaluated in Sec. 5.1 (which of the three is not named) fails on 23.8%. 106 of the 167 failures (63.4%) are on zero-corpus-frequency words (Sec. 5.1, p. 3465). The paper illustrates frequency-driven overwriting, POS ambiguity, overstemming and contextual omission with examples (Table 3), but gives no per-type counts. How often each error type occurs is therefore not established.
- In word-level cross-lingual alignment, lemmatizing **both** sides helps greatly (Acc@1 12.86 → 41.61%), while lemmatizing **only one** side hurts (→ 10.38–10.57%) (Table 4).

## 14. What the work does NOT prove

- **Anything about BM25.** BM25 is not used, and the results for binary/TF-IDF cannot be transferred to BM25's saturation and length normalization.
- **That lemmatization beats stemming**, or beats prior rule-based Nepali lemmatizers, in retrieval. Neither is compared.
- **Anything about dense or hybrid retrieval**, or about lexical–semantic complementarity. No dense retriever, no fusion, no overlap/unique-hit/oracle analysis.
- **Which queries benefit or are harmed** by lemmatization, or why. There is no per-query or query-feature analysis.
- **That the improvements are statistically significant.** No test is reported, despite the word "significantly".
- **Generalization to ad hoc retrieval** with multiple relevant documents, real information needs, larger collections or other domains.
- **That mBART is a better lemmatizer than mT5-base.** The intrinsic accuracy order is the opposite (0.960 vs 0.961). The IR advantage is small and untested.

## 15. Relationship to current Uzbek evidence

- **No Uzbek data.** Nepali is Indo-Aryan, in Devanagari script, with inflection plus postpositional suffixation. Uzbek is Turkic and agglutinative, in Latin/Cyrillic script. What they share is suffix-driven surface variation, which makes the general mechanism (normalization increases exact-match overlap) relevant. Morphological details do not transfer.
- **Parallel to the national Uzbek evidence:**
  - Xusainova (MORPH-UZ-004) and Bakaev (MORPH-UZ-002) report analyzer/stemmer accuracy (97.5%, 88.9–96%) without qrels-based IR.
  - This Nepali paper shows the **next step**: lemmatizer accuracy plus an IR effect. It is still without BM25, dense retrieval or complementarity.
  - It also shows that a ≈96% accurate lemmatizer can still systematically distort rare words. This caution applies to Uzbek analyzers too.
- **Relation to international morphology cards:**
  - Like UPERF (MORPH-003, Urdu), it compares raw vs lemma in low-resource retrieval, but more narrowly: no stem, no BM25, no embeddings in IR.
  - Like Haddad & Bechikh Ali (MORPH-002, Turkish), it shows that the preprocessing effect depends on the retrieval model.
  - Like Mekonnen et al. (Amharic, exemplar), it uses a headline → article single-positive task.

## 16. Relationship to CURRENT_GAP

**Classification:** *no material effect* on the residual core; it *supports* already-listed non-claims.

- **Confirms as occupied** (already REJECTED in `GAP_BOUNDARY` §4): "raw/stem/lemma has not been compared in low-resource IR". This paper adds a recent peer-reviewed raw-vs-lemma example (Nepali, 2026), but it is weaker than UPERF, which already establishes the point.
- **Consistent with the boundary's model-dependence observation** (Haddad & Bechikh Ali): the morphology effect differs by lexical weighting model.
- **Does not touch** any element of the v0.8 residual core:
  - no `BM25_raw/stem/lemma`;
  - no fixed dense comparator `D`;
  - no `H_raw/H_stem/H_lemma` fusion;
  - no unique relevant hits, overlap, oracle union or incremental hybrid gain;
  - no per-query change analysis;
  - no link to query features.
- It is not a "gap killer" under any of the four conditions in `CURRENT_GAP.md` ("What can still kill this gap").

**Proposal:** keep v0.8 refined unchanged. Optionally cite this work as a further low-resource example that lemmatization effects are measured only on aggregate lexical metrics, without complementarity analysis. This is a proposal only; `CURRENT_GAP.md` has not been edited.

## 17. Implications for our research design

- **Morphology preprocessing (BM25_lemma):**
  - If a neural or statistical Uzbek lemmatizer is used, log **per-query lemmatizer changes**. Record which query tokens were rewritten, and whether a rare token or named entity was mapped to a frequent lemma.
  - The Nepali error analysis (frequency bias, 63.4% of failures on zero-frequency words) predicts that normalization can create **false lexical matches** on rare-term and entity queries. This can shift which documents are uniquely lexical hits, which is exactly the quantity our gap measures.
  - Add "share of query tokens altered by the lemmatizer/stemmer" and "lemmatizer changes on rare/NE tokens" as candidate query features.
- **Analyzer symmetry.** Apply the identical analyzer to queries and documents, and state it explicitly. Table 4 shows that one-sided normalization is worse than none. For Uzbek, this also covers apostrophe/script normalization.
- **Context vs word-level lemmatization.** Documents allow contextual disambiguation; short queries do not. If contextual lemmatization is used for documents, test whether query-side word-level lemmatization creates a mismatch. Otherwise use the same word-level procedure on both sides.
- **Baselines.**
  - Include a stem condition and a simple-normalization control (per v0.8), because this paper cannot say whether lemmatization beats cheaper stemming.
  - Report BM25 parameters and the tokenizer.
  - Run a sanity check that the lexical baselines behave plausibly: e.g., if binary matching beats weighted models, investigate before interpreting.
- **Metrics / protocol.**
  - Report the exact number of evaluated queries and verify it against the metric granularity. This paper's 600-vs-638 problem shows how easily this slips.
  - Use per-query paired tests or a bootstrap.
  - Report intrinsic lemmatizer/stemmer accuracy **separately** from IR effects, and do not treat one as a proxy for the other.
- **Dataset.** Headline → snippet pairs are a cheap pilot resource but single-positive. Our main evaluation still needs pooled multi-relevant qrels for unique-hit/oracle analysis.
- **Hypothesis.** The finding that the morphology effect depends on the lexical model motivates reporting BM25_raw/stem/lemma **and** at least one simpler exact-match control. The finding gives no evidence on complementarity with dense retrieval.

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| Lemmatization | Turning a word form into its dictionary form (e.g., *garchha* 'does' → *garnu* 'to do') | Mapping w → lemma(w), usually with morphological knowledge |
| Stemming | Cutting off endings by rules; the result need not be a real word | Heuristic affix removal |
| Seq2seq / text-to-text lemmatizer | A model that "writes out" the lemma letter by letter, like translation | Encoder–decoder generation p(l \| w) |
| mT5 / mBART | Large multilingual pretrained encoder–decoder models | Pretrained Transformers (span corruption / denoising objectives) |
| CER | Share of characters that must be edited to fix the output | Edit distance / reference length |
| Morphological coverage (paper's term) | Whether the last three letters of the predicted lemma are right | Suffix-match heuristic (Sec. 3.4) |
| OOV | Word never seen in the corpus/training data | Out-of-vocabulary |
| Frequency bias (paper's term) | Model replaces a rare word by a similar common one | Decoder prior dominates for low-frequency inputs |
| TF-IDF retrieval | Word-matching where rare words count more and repeated words count more | Vector space model, tf × idf weighting |
| Binary term index | Only records whether a word occurs, not how often | Boolean/binary term vectors; scoring unspecified in the paper |
| Acc@k | Share of queries whose right document is in the top k | Success@k / Hit@k |
| MAP@5 | Average precision cut at rank 5, averaged over queries; with one relevant item = MRR@5 | Mean average precision at cutoff 5 |
| Known-item search | Looking for one specific existing document | Single target per query |
| Extrinsic evaluation | Testing a tool by its effect on a downstream task | Task-based evaluation |
| Complementarity (project term) | Each channel finds some relevant documents the other misses | Unique relevant hits, overlap, oracle-union gain |

## 19. Open questions / verification needed

1. **Number of evaluated IR queries:** 600 stated vs 638 implied by the printed Acc values (and 3,000 vs ≈3,189 in Table 4). Only the authors or the released evaluation data can resolve it.
2. **Abstract "MAP@1" vs Table 5 MAP@5:** mislabel in the abstract. Cite Table 5 values with their correct metric name.
3. **IR protocol details:** TF-IDF similarity function, binary scoring rule, collection size, relevance definition, stop-word list, and whether queries and documents were both lemmatized. All NOT_REPORTED.
4. **Which lemmatizer** produced the 700-word error analysis (Sec. 5.1): not stated.
5. **Why binary matching beats TF-IDF** in all conditions: unexplained in the paper.
6. **Optional low-cost check** (if researcher wants): the announced public repository might contain the IR evaluation script and could answer 1 and 3. Per the source rule, any such finding would be supplementary and would not revise what the paper states.

## 20. Decision after deep dive

- **Keep current gap?** Yes. v0.8 refined is unaffected (§16).
- **Modify gap?** No. Optionally add to the evidence-boundary list as a Nepali raw-vs-lemma example with TF-IDF/binary, no BM25/dense/fusion (researcher's decision).
- **Add decision?** Proposed for `decisions/DECISIONS.md` (researcher's decision):
  - "The same analyzer (tokenization, normalization, stemming/lemmatization) is applied to queries and documents in every lexical condition";
  - "per-query log of analyzer rewrites is kept and used as a candidate query feature".
- **Add experiment?** No new experiment. It reinforces two existing plans: a stem and a simple-normalization control next to the lemma condition, and query-level logging of lemmatizer errors on rare/NE tokens.
- **Add citation to Chapter I?** Optional, minor:
  - §1.1, as a recent low-resource example that lemmatization gains in lexical IR depend on the weighting model and that neural lemmatizers show frequency-bias errors;
  - cite with caveats (no BM25, no significance, small known-item task).
- **Proposed `MASTER_INDEX.md` row** (section C; to add after approval):

| MORPH-009 | Regmi, Dawadi, Bal — *Nepali Lemmatization with Multilingual Transformers: Intrinsic and Extrinsic Evaluation in a Low-Resource Setting* (LREC 2026, pp. 3462–3469) — [deep dive](deep-dives/2026_Regmi_Dawadi_Bal_Nepali_Lemmatization_IR.md) | 2026 | B | MEDIUM | Neural (mT5/mBART) word-level Nepali lemmatizers (≈96% accuracy; 23.8% failures on a 700-word dictionary set, illustrated by frequency-bias errors on rare words) evaluated extrinsically on 600-headline→snippet matching: raw vs lemma with TF-IDF and binary index only. Lemma gains large for binary (Acc@1 0.632→0.857), small for TF-IDF (0.498→0.553): effect is model-dependent. No BM25, no stem, no dense/fusion, no overlap/unique-hit or per-query analysis, no significance tests; abstract mislabels MAP@5 as MAP@1; printed accuracies imply 638, not 600, queries. |
