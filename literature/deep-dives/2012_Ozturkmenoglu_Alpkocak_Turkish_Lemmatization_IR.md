# Ozturkmenoglu & Alpkocak (2012): Comparison of Different Lemmatization Approaches for Information Retrieval on Turkish Text Collection

**Targeted deep-dive status:** COMPLETED (AI-assisted, pending researcher review)
**Completed:** 2026-09-28
**Literature ID:** `MORPH-018` (assigned 2026-09-28, approved by researcher)
**Systematic-review record:** `CR001537`. Full-text triage: INCLUDE, reading priority HIGH, reading tier 1 ("прямо по теме пробела"), `carries_complementarity_evidence = NO`. Triage note: "Turkic language; controlled comparison of several morphological representations."
**Provenance:** AI-assisted deep dive (Claude). The whole paper (5 pages, IEEE two-column; no printed page numbers, so "p. N" below means PDF page N) was read from the text extraction and from page images. **Pages checked visually:** all five pages at 110 dpi; pp. 3–4 again at 220 dpi for Table II (example fragment), Table III (index statistics), Table IV (effectiveness) and Figure 1 (P–R curves). Every table value below was compared with the page image. Numbers computed by us are marked **[computed]** and were recomputed with Python. Statements about other papers on the same collection come only from existing project cards / `MASTER_INDEX.md` and are marked **[MORPH-001 card]** or **[MASTER_INDEX]**; they were not re-verified here.
**Verification:** independent AI verifier pass 2026-09-28; 4 findings addressed.
**Source rule:** **the paper is the primary and only authoritative source** for what the authors did and found. The web was used only to check the bibliographic record.
**Reliability:** **B** — peer-reviewed IEEE conference paper (INISTA 2012), verifiable record, but short, with an under-specified retrieval configuration (tokenizer, stop-word list, exact tf×idf variant not given) and no significance tests. The evidence is a single run per condition on one collection.

---

## Кратко для исследователя (RU)

- **Что сделано.** На турецкой коллекции Milliyet (408 305 новостных документов, 72 запроса; p. 2) сравнили **9 вариантов лексического представления** в одной и той же системе Terrier:
  - без лемматизации (NL);
  - три морфологических инструмента: анализатор Oflazer'а (OMA), словарный лемматизатор DTL на radix-trie, Zemberek (ZEM), каждый в двух режимах: **min** / **max** (самая короткая / самая длинная из альтернативных лемм);
  - усечение слова до префикса 5 и 7 символов (FLT5, FLT7).
- **Модель ранжирования — tf×idf в Terrier, а не BM25** («stop-word list of Turkish language and tf×idf weighting model», p. 3). BM25 нет. Плотного поиска, гибрида/fusion нет.
- **Главные числа** (Table IV, p. 4, MAP): NL 0.3098; DTL-max **0.3486** (лучший по всем 5 метрикам); OMA-max 0.3419; ZEM-max 0.3397; FLT5 0.3365; FLT7 0.3342; **DTL-min 0.1121** (катастрофический провал).
  - DTL-max vs NL: +12.52% MAP, +18.87% bpref (проценты авторов воспроизводятся **[computed]**).
  - DTL-max vs простое FLT5: всего +0.0121 MAP (+3.6%); vs OMA-max: +0.0067 MAP (+1.96%).
- **Выбор между альтернативными леммами — критический параметр:** max лучше min у всех трёх инструментов, а у DTL разница огромная (MAP 0.3486 vs 0.1121; Table IV). DTL-min оставляет лишь 18 684 термина индекса против 531 498 у NL (Table III) — вероятно, сверхсклейка (наш вывод; авторы провал DTL-min не объясняют).
- **Утверждение «лемматизация улучшает поиск» верно не везде:**
  - по MAP и bpref все варианты, кроме DTL-min, выше NL;
  - по P@10 OMA-min и ZEM-min ниже NL; по P@20 ниже NL даже OMA-max (0.5042) и ZEM-max (0.5167) при NL 0.5181 **[computed]**. Выигрыш сосредоточен в MAP/bpref, а не в ранней точности.
- **Нет статистики:** нет тестов значимости, доверительных интервалов, разбора по запросам. Разницы между DTL-max и следующими четырьмя вариантами (OMA-max, ZEM-max, FLT5, FLT7; 0.007–0.014 MAP) на 72 запросах нельзя считать доказанными.
- **Нет ничего из ядра gap:** нет перекрытия результатов между представлениями, уникально найденных релевантных документов, oracle union, per-query анализа и признаков запросов. Table III даёт только суммарное число найденных релевантных документов на вариант (NL 5194, DTL-max 5856) — это не анализ перекрытия.
- **Внутренние несоответствия:**
  - abstract/p. 3 называют DTL-max самым экономным по числу терминов и размеру индекса, но в Table III меньше у DTL-min (18 684 терминов, 81.8 MB vs 51 708, 161 MB);
  - OMA в Sec. I назван «stemmer», в Sec. II — «lemmatizer», при этом берётся «first morpheme» (корень);
  - во всех вариантах «Number retrieved» < 72 000, хотя брались top-1000 на 72 запроса — не объяснено.
- **Для нашего gap:** работа подтверждает уже занятый тезис «варианты морфологического представления лексического канала в тюркском языке сравнивались»; ядро v0.8 (raw/stem/lemma BM25 × фиксированный D → overlap/unique hits → прирост гибрида) **не затрагивает**. Предложение: gap не менять.
- **Практическая польза для нас:**
  1. В условии `BM25_lemma` для узбекского надо явно фиксировать и публиковать правило выбора среди альтернативных разборов (min/max/первый/дизамбигуация) и fallback для нераспознанных слов — от этого результат может меняться в разы.
  2. Для каждого варианта сообщать размер словаря индекса (степень склейки) — кандидат в объясняющую переменную для изменения взаимодополняемости.
  3. Префиксное усечение (5 символов) — дешёвый и сильный контроль (`BM25_simple-normalization`).
  4. Смотреть эффект на нескольких глубинах: здесь морфология помогает MAP/bpref сильнее, чем P@10/P@20.

---

## 1. Bibliographic record

- **Authors:** Okan Ozturkmenoglu (Department of Computer Engineering, The Graduate School of Natural and Applied Sciences, Dokuz Eylül University, Izmir); Adil Alpkocak (Department of Computer Engineering, Engineering Faculty, Dokuz Eylül University, Izmir) (p. 1)
- **Year:** 2012
- **Venue:** 2012 International Symposium on Innovations in Intelligent Systems and Applications (INISTA) — from the assignment metadata; the paper itself carries only the IEEE copyright line.
- **Publisher / ISBN line on the paper:** "978-1-4673-1448-0/12/$31.00 ©2012 IEEE" (p. 1 footer)
- **IEEE Xplore document:** 6246934 (bibliographic check: web search results listing `ieeexplore.ieee.org/document/6246934` for this title)
- **DOI:** `10.1109/INISTA.2012.6246934` — **partially verified** (bibliographic check: a web search for this DOI string returned this paper's ADS, ResearchGate and Semantic Scholar records; the DOI resolver, Crossref and IEEE pages could not be fetched from this environment).
- **Pages in proceedings:** NOT verified. Length: 5 pages. (The ADS bibcode `2012inis.conf...43O` found in the web search may indicate a start page of 43; not confirmed.)
- **Conference place/date:** NOT verified from any source reachable here.
- **Source type:** peer-reviewed conference paper (IEEE)
- **Reliability:** B
- **Full text available:** yes (`07_full_text/pdfs/CR001537.pdf`, 5 pages; PDF metadata: "Certified by IEEE PDFeXpress at 05/17/2012")

## 2. Why this work matters to the PhD

It is a **controlled comparison of several morphological representations of the lexical channel** for an agglutinative Turkic language, on a standard ad hoc test collection:

- one collection, one retrieval engine, one weighting model, one query set;
- only the index-term representation changes (9 conditions).

It is therefore a close methodological relative of our `Lexical_raw → Lexical_stem → Lexical_lemma` design, minus everything on the semantic side.

| Axis | Relation |
|---|---|
| Lexical retrieval | Main and only focus. Terrier with **tf×idf** (not BM25); 9 index-term representations |
| Semantic retrieval | **Absent** |
| Hybrid retrieval | **Absent**. The "hybrid lemmatizer" in the conclusion means combining two lemmatizers, not lexical+semantic fusion |
| Uzbek morphology | Indirect but close: Turkish is a Turkic agglutinative language; morphological tools and dictionaries are Turkish-specific |
| Low-resource retrieval | Weak: Turkish in 2012 had a standard test collection and several analyzers |
| Current gap | Supports an already occupied boundary claim ("raw/stem/lemma compared in Turkic lexical IR"); no effect on morphology-induced lexical–dense complementarity (§16) |

## 3. Research problem

### Simple explanation

A Turkish word can take very many forms, because suffixes are stacked onto a root. A search engine that matches exact word forms misses documents that use a different form of the same word. Reducing words to a base form ("lemma") should help, but there are several tools and several ways to do it. The authors ask: which Turkish lemmatization approach gives the best search results, and is it better than doing nothing or simply cutting words to a fixed length?

### Formal formulation

No explicit research questions or hypotheses are stated. The stated goal (Sec. III, p. 2): "to compare different lemmatization approaches for IR on Turkish text collection". Operationally:

- Hold fixed: collection, queries, qrels, engine (Terrier), weighting model (tf×idf), stop-word list, top-1000 run depth, evaluation tool (trec_eval 8.1).
- Vary: the term-normalization function `g(w)` applied to every token of documents and queries, `g ∈ {identity, OMA-min, OMA-max, DTL-min, DTL-max, ZEM-min, ZEM-max, prefix5, prefix7}`.
- Compare: MAP, R-prec, bpref, P@10, P@20 (Table IV), plus index statistics (Table III).

## 4. Main idea

### Simple explanation

Build the same search index nine times. Each time, turn words into index terms differently: leave them as they are, replace them by the base form from one of three Turkish tools, or cut them to the first 5 or 7 letters. When a tool offers several possible base forms for one word, try both the shortest and the longest. Run the same 72 queries against each index and compare the scores.

### Concrete example

The paper's own example (Table II, p. 3): the phrase "katma değerler ile ödenmesi gereken verginin …" ("the value added and the tax that must be paid …") becomes:

| Variant | Output fragment (verbatim from Table II) |
|---|---|
| NL | "katma değerler ile ödenmesi gereken verginin" |
| OMA-max | "kat değerle ile öde gerek vergi" |
| DTL-max | "katma değer ile ödenme gerek vergin" |
| ZEM-max | "kat değer ile öde gerek vergi" |
| FLT5 | "katma değer ile ödenm gerek vergi" |

What the example shows (our reading of Table II, not stated by the authors):

- the tools disagree on how far to cut: OMA and ZEM reduce "katma" (value-*added*) to "kat", which also merges it with the homographic noun *kat* ("floor/layer"); DTL-max keeps "katma";
- DTL-max keeps some derivational forms as dictionary headwords ("ödenme", "inceleme", "doğruluk"), and also produces "vergin" for "verginin" where the other tools give "vergi";
- casing is not uniform across variants (DTL-max lowercases "gsyih"; ZEM-max keeps "Yurtiçi" and "GSYİH"; FLT5 keeps "Sektö", "Gayri Safi").

### Formal method

For each variant `g`, documents (headline + text fields) and queries (all fields) are mapped token-by-token through `g`, indexed in Terrier, and ranked with a tf×idf weighting model. The exact tf×idf formula is **NOT_REPORTED**.

Lemma selection rule (Sec. III-B, p. 2): "If the lemmatizers contain no lemma for the target word, the original word is returned; if it contains more than one alternative, we use the alternatives with maximum and minimum length."

## 5. Architecture / algorithm

1. **Normalization tools** (Sec. II, p. 2):
   - **OMA** — Oflazer's two-level finite-state morphological analyzer for Turkish (XRCE tools; root lexicon "about 23K roots words"; 22 two-level rules). "In this study, we used the first morpheme of OMA for input word as lemma." The first morpheme is the **root**, so OMA here acts as a root extractor. Sec. I calls it "a morphological analyzer based stemmer".
   - **DTL** — Dictionary-based Turkish Lemmatizer (ref. [8], a 2011 Dokuz Eylül University work by M. Civriz), based on the TDK "Grand Turkish Dictionary", stored in a radix-trie (PATRICIA trie). How it finds candidate lemmas for a word (e.g., prefix lookup) is **NOT_REPORTED**.
   - **Zemberek** — open-source Turkic NLP framework; "a simple dictionary based top-down parser" over a DAWG root dictionary.
   - **FLT5 / FLT7** — keep the first 5 or 7 characters; shorter words unchanged. The choice is justified by Can et al. (5 was best among 3–7, per the authors' citation of [10]) and by an average Turkish word length of 7.07 letters (ref. [17]).
2. **Ambiguity handling:** min-length vs max-length lemma (→ `-min`, `-max` variants). Fallback: the original word when no lemma is found. **How often each tool falls back or returns several alternatives is NOT_REPORTED.**
3. **Preprocessing common to all variants** (Sec. IV, p. 3):
   - "Documents of collection were tokenized with same tokenizer expression." The expression itself is **NOT_REPORTED**.
   - "We removed unwanted characters due to character set encoding and truncated tokens."
   - "We keep the digit characters as is."
   - Same processing applied to queries.
   - Turkish stop-word list: source and size **NOT_REPORTED**; whether it is applied before or after normalization is **NOT_REPORTED**.
   - Lowercasing: **NOT_REPORTED**; Table II shows mixed casing across variants (§4).
4. **Retrieval:** Terrier (ref. [18] points to the v3.5 documentation; the version actually used is not stated), tf×idf weighting, top 1000 documents per query, TREC-format run.
5. **Evaluation:** trec_eval version 8.1.

## 6. Data

- **Dataset/corpus:** Bilkent Milliyet Collection (cited as [10], Can et al. 2008)
- **Language / domain:** Turkish; newspaper articles (Milliyet), 2001–2005
- **Size:** "408,305 documents with 95.5 million words" (Sec. III-B, p. 2)
- **Queries:** "72 ad-hoc queries"; "all fields in queries" were processed. Which fields exist (title/description/narrative) is **NOT_REPORTED** in this paper.
- **Documents:** headline and text fields indexed
- **Relevance judgments:** from the collection; "33 assessors" (p. 2). The authors describe the judgments as incomplete ("when judgments are incomplete like the ones we use", p. 4). Total number of relevant documents, graded vs binary, and pooling procedure: **NOT_REPORTED** in this paper.
  - Context from the project card of the collection paper **[MORPH-001 card]**: pool = union of top-100 of 24 runs built from NS/F6/SV representations. If this is the same qrels version, none of the nine representations here (except NL ≈ NS) contributed to the pool.
- **Train/dev/test:** none. No tuning is described (the prefix lengths 5 and 7 were chosen from prior literature, not on these queries).

## 7. Baselines

| Baseline | What it is | Why selected | Fair comparison? |
|---|---|---|---|
| NL (no lemmatization) | Surface word forms as index terms | "provides a baseline for comparison" (Table I) | Yes: same engine, weighting, stop-words |
| FLT5 / FLT7 | Fixed prefix truncation | Known to work well for Turkish (ref. [10]) | Yes. A strong, cheap control, and it stays close to the best tool |
| OMA / ZEM / DTL, min and max | Three linguistic normalizers × two ambiguity rules | The object of the study | Mostly. DTL comes from the authors' university (ref. [8], M. Civriz, Dokuz Eylül University, 2011; whether it is their own group's tool is not stated), so tool configuration expertise may be uneven (our inference); fallback rates and ambiguity rates per tool are not reported |

No BM25, language-model or other weighting model; no semantic or dense baseline.

## 8. Metrics

| Metric | Definition | Simple meaning here | Appropriate? |
|---|---|---|---|
| MAP | Mean over queries of average precision (precision at each relevant document retrieved) | "How well are *all* relevant documents ranked, on average?" | Yes, standard; sensitive to incomplete judgments (authors' own remark, p. 4) |
| R-prec | Precision after R documents, R = number of relevant documents for the query | "Of the first R results, how many are relevant?" | Yes |
| bpref | Counts how often judged-relevant documents are ranked above judged-non-relevant ones; unjudged documents ignored | Robust to incomplete judgments | Yes, and important here because the normalized runs may retrieve unjudged documents |
| P@10, P@20 | Share of relevant documents in the top 10 / 20 | "What does the user see on the first page?" | Yes |
| Interpolated P–R curve (Fig. 1) | Precision at 11 recall levels | Whole-ranking shape | Descriptive only |
| Table III statistics | Number retrieved, number relevant retrieved (summed over queries, top-1000), indexed term count, index size | Efficiency / conflation and a crude recall proxy | Descriptive; "number relevant retrieved" is a sum over queries, not an overlap measure |

Significance: **none** (§10).

## 9. Results

### Table IV: effectiveness (p. 4; checked on the page image)

| Variant | MAP | R-prec | bpref | P@10 | P@20 |
|---|---:|---:|---:|---:|---:|
| NL | 0.3098 | 0.338 | 0.4 | 0.5417 | 0.5181 |
| OMA-min | 0.328 | 0.3424 | 0.4316 | 0.5264 | 0.4868 |
| OMA-max | 0.3419 | 0.3547 | 0.4491 | 0.5458 | 0.5042 |
| DTL-min | 0.1121 | 0.1308 | 0.2223 | 0.2 | 0.1817 |
| **DTL-max** | **0.3486** | **0.3671** | **0.4755** | **0.5722** | **0.5396** |
| ZEM-min | 0.3253 | 0.3376 | 0.4306 | 0.5278 | 0.4896 |
| ZEM-max | 0.3397 | 0.3518 | 0.4463 | 0.5597 | 0.5167 |
| FLT5 | 0.3365 | 0.3522 | 0.4309 | 0.5472 | 0.5201 |
| FLT7 | 0.3342 | 0.3612 | 0.428 | 0.5583 | 0.5306 |

Values are printed with varying numbers of decimals (e.g., "0.4", "0.2", "0.328"); reproduced as printed.

**Authors' derived claims, recomputed** (Sec. IV, p. 4) **[computed]**:

- MAP, DTL-max vs OMA-max / ZEM-max / FLT5 / FLT7 / NL: 1.96% / 2.62% / 3.60% / 4.31% / 12.52% — all reproduce ✓ (printed "3.6%").
- bpref: 5.88% / 6.54% / 10.35% / 11.10% / 18.87% — all reproduce ✓ (printed "11.1%", "18.88%"; 0.4755/0.4 − 1 = 18.875%).
- P@10 / P@20 vs OMA-max 4.84 / 7.02; ZEM-max 2.23 / 4.43; FLT5 4.57 / 3.75; FLT7 2.49 / 1.70; NL 5.63 / 4.15 — all reproduce ✓.
- R-prec: the text says only that DTL-max is better; against the same five comparators the relative gains are 1.63% (vs FLT7) to 8.61% (vs NL) **[computed]**.

**Absolute differences** (more informative than relative ones) **[computed]**:

- DTL-max − NL: MAP +0.0388, bpref +0.0755, P@10 +0.0305.
- DTL-max − OMA-max: MAP +0.0067; − ZEM-max: +0.0089; − FLT5: +0.0121; − FLT7: +0.0144.

**Every variant vs NL** **[computed]**:

| Variant | ΔMAP | ΔP@10 | ΔP@20 |
|---|---:|---:|---:|
| OMA-min | +0.0182 | −0.0153 | −0.0313 |
| OMA-max | +0.0321 | +0.0041 | −0.0139 |
| DTL-min | −0.1977 | −0.3417 | −0.3364 |
| DTL-max | +0.0388 | +0.0305 | +0.0215 |
| ZEM-min | +0.0155 | −0.0139 | −0.0285 |
| ZEM-max | +0.0299 | +0.0180 | −0.0014 |
| FLT5 | +0.0267 | +0.0055 | +0.0020 |
| FLT7 | +0.0244 | +0.0166 | +0.0125 |

Reading:

- On MAP and bpref, every variant except DTL-min beats NL.
- On early precision the picture is mixed: on P@20, NL (0.5181) ranks 4th of 9, above OMA-max and ZEM-max; the two prefix methods are 2nd and 3rd on P@20.
- **max > min for every tool and every metric** (OMA ΔMAP +0.0139; ZEM +0.0144; DTL +0.2365) **[computed]**, consistent with the authors' second finding.
- Rank order by MAP: DTL-max > OMA-max > ZEM-max > FLT5 > FLT7 > OMA-min > ZEM-min > NL > DTL-min **[computed]**.

### Table III: index statistics (p. 3; checked on the page image)

| Variant | Number retrieved | Number relevant retrieved | Indexed term count | Index size |
|---|---:|---:|---:|---:|
| NL | 70334 | 5194 | 531498 | 269MB |
| OMA-min | 71469 | 5405 | 287251 | 171MB |
| OMA-max | 71400 | 5563 | 288936 | 178MB |
| DTL-min | 71000 | 2792 | 18684 | 81.8MB |
| DTL-max | 71468 | 5856 | 51708 | 161MB |
| ZEM-min | 71027 | 5388 | 265061 | 163MB |
| ZEM-max | 71439 | 5542 | 266468 | 173MB |
| FLT5 | 70803 | 5398 | 132795 | 170MB |
| FLT7 | 70639 | 5500 | 270030 | 216MB |

- Authors' reductions for DTL-max: 90.27% terms / 40.15% index size vs NL; 82.10% / 9.55% vs OMA-max — all reproduce ✓ **[computed]**.
- Term-count reduction vs NL **[computed]**: OMA ≈ 46%, ZEM ≈ 50%, FLT7 49%, FLT5 75%, DTL-max 90%, DTL-min 96.5%.
- Relevant retrieved (top-1000, summed over 72 queries) vs NL **[computed]**: DTL-max +12.75% (5856 vs 5194; ≈ 81.3 vs 72.1 per query); DTL-min −46.25%.
- Recall@1000 cannot be computed: the total number of relevant documents is not reported.
- "Number retrieved" is below 72 × 1000 = 72,000 for every variant (shortfall 531–1666 **[computed]**), i.e., some queries returned fewer than 1000 documents. Not explained in the paper.

### Figure 1: interpolated P–R curves (p. 4; checked on the page image)

- Shows NL, OMA-max, DTL-max, ZEM-max, FLT5, FLT7 (min variants not shown). No numeric table.
- Visual reading (approximate): NL is lowest from recall ≈ 0.1 to ≈ 0.6; DTL-max is highest around recall 0.1–0.3; above recall ≈ 0.6 the curves nearly coincide; at recall 0.0 FLT7 appears highest.
- Authors: "it can be seen that DTL-max is slightly better than both of other approaches" (p. 4).

## 10. Statistical evidence

- **Significance test:** NOT_REPORTED (none performed or reported).
- **Confidence intervals:** NOT_REPORTED.
- **Runs / seeds:** deterministic lexical runs; one run per condition. Not an issue for variance, but there is no query-sampling uncertainty estimate.
- **Ablation:** the 9-condition design itself is a representation ablation (tool × min/max). No ablation of stop-words, casing, fields or weighting model.
- **Per-query analysis:** NOT_REPORTED. No per-query wins/losses, no query-length or query-type breakdown, no failure analysis.
- **Overlap / unique relevant hits / oracle union between representations:** NOT_REPORTED. Table III gives only per-condition totals of relevant retrieved documents.
- **Error analysis of normalizers** (fallback rate, ambiguity rate, lemma accuracy): NOT_REPORTED.

## 11. Strengths

- Clean single-factor design: only the term representation varies; engine, weighting, stop-words and queries are fixed.
- Three different linguistic tools plus two prefix lengths plus a surface baseline on a standard large Turkish test collection.
- Makes the **ambiguity-resolution rule** (min vs max) an explicit experimental factor — rarely reported elsewhere, and shown here to matter a lot.
- Reports index statistics (term count, size) next to effectiveness, which lets the reader relate conflation strength to effectiveness.
- Uses bpref alongside MAP and explicitly notes incomplete judgments.
- All derived percentages in the text reproduce from the tables.

## 12. Limitations

### Stated by the authors

- Relevance judgments are incomplete ("when judgments are incomplete like the ones we use", p. 4), motivating bpref.
- Future work only: a "hybrid lemmatizer, which uses both dictionary-based and morphological analyzer based approaches" (p. 5). No other limitations are stated.

### Inferred from the experimental design

1. **No significance testing** on 72 queries. The differences among the top five (DTL-max, OMA-max, ZEM-max, FLT5, FLT7; MAP spread 0.0144) may not be statistically distinguishable. "DTL is the best word lemmatization method for Turkish IR" (p. 5) is stronger than the evidence.
2. **One weighting model (tf×idf), exact variant unreported.** Other work on the same collection **[MASTER_INDEX, MORPH-002]** reports that preprocessing effects depend on the retrieval model; no BM25 or language model here.
3. **Under-specified preprocessing:** tokenizer expression, stop-word list, casing, handling of Turkish İ/ı and apostrophes (e.g., "Hasıla'nın", "50'sini" in Table II) are not described. Table II shows casing differs across variants, which could itself change matching.
4. **Possible pool bias.** If the qrels are those of the collection paper **[MORPH-001 card]**, none of the tool-based or prefix variants contributed to the pool. bpref mitigates but does not remove this.
5. **DTL-min collapse is unexplained.** 18,684 index terms for 408K documents suggests severe over-conflation (very short dictionary prefixes). This is our inference; the paper gives no fallback/ambiguity statistics.
6. **DTL-max's very small vocabulary** (51,708 terms, vs ≈ 265–289K for OMA/ZEM) despite the stated fallback to the original word for unresolved words implies that DTL assigns *some* dictionary entry to most tokens, including, possibly, names and foreign words. How is not described (our inference).
7. **"Lemma" is used loosely.** OMA's "first morpheme" is a root; FLT is called a "lemmatizer" (Table I). The study compares term-conflation strategies, not lemmatization in the strict sense.
8. **Early-precision caveat not discussed.** The conclusion "using lemmatizer … increases the effectiveness" does not hold for DTL-min on any metric, nor for several variants on P@10/P@20 (§9).
9. **The DTL tool** comes from the authors' own university (ref. [8]); its availability and version are not stated, which limits reproducibility.
10. **No query-level variable** (query length, number of inflected terms, OOV) is analysed, although "all fields" queries are used.

## 13. What the work proves

Within this single setting (Milliyet, 72 queries, Terrier tf×idf, one run per condition, no significance tests):

- **Morphological conflation of index terms raises MAP and bpref over surface forms** for 7 of the 8 normalized conditions (all except DTL-min): MAP from 0.3098 (NL) to 0.3253–0.3486; bpref from 0.4 to 0.428–0.4755 (Table IV).
- **The rule for choosing among alternative analyses matters.** Max-length lemmas beat min-length lemmas for all three tools on all five metrics, and for DTL the wrong rule turns the best condition (MAP 0.3486) into the worst (0.1121), well below no normalization (Table IV).
- **Strength of conflation is not monotonically related to effectiveness.** DTL-max has 90% fewer index terms than NL and is best; DTL-min has 96.5% fewer and is worst (Tables III–IV, **[computed]**).
- **Simple prefix truncation is competitive:** FLT5 is within 0.0121 MAP of the best tool and above both min variants of OMA and ZEM on MAP, R-prec, P@10 and P@20 (on bpref it is marginally below OMA-min, 0.4309 vs 0.4316) (Table IV).
- **Gains are concentrated in the recall-oriented / whole-ranking metrics** (MAP, bpref) more than in P@10/P@20 (Table IV, **[computed]**).

## 14. What the work does NOT prove

- **That DTL is the best Turkish lemmatizer for IR in general.** No significance test; DTL-max leads the next four conditions (OMA-max, ZEM-max, FLT5, FLT7) by only 0.0067–0.0144 MAP; one weighting model; one collection.
- **That lemmatization always helps.** DTL-min is far worse than NL; several variants lose to NL on P@10/P@20.
- **Anything about BM25.** The model is tf×idf; how BM25's length normalization and saturation would interact with these representations is untested here.
- **Anything about semantic/dense retrieval, fusion or hybrid search.** None is present.
- **Anything about complementarity** — between representations or between lexical and semantic channels: no overlap, unique relevant hits, oracle union or per-query analysis.
- **Why** some variants win: no per-query or error analysis, no fallback/ambiguity statistics.
- **Transfer to Uzbek:** the tools, dictionary (TDK) and qrels are Turkish-specific.

## 15. Relationship to current Uzbek evidence

- **No Uzbek data.** Turkish and Uzbek share agglutinative suffixing morphology, so the *design lessons* transfer (ambiguity rule, fallback, conflation strength, prefix control). The *numbers* and the *ranking of tools* do not.
- **Uzbek analogues of the three tool types exist in the project's national evidence** [MASTER_INDEX C]: analyzer-based morphology (Bakaev Morphoanalyzer, MORPH-UZ-002), stemmer + lemmatizer (Xusainova UzbStemmer, MORPH-UZ-004), and dictionary-based lemma indexing (Elov, MORPH-UZ-007). None of those works reports a qrels-based IR comparison like Table IV. This paper shows the kind of controlled comparison that is missing for Uzbek on the *lexical* side.
- **Same collection, other papers:** Milliyet is also the collection of Can et al. 2008 (MORPH-001), its 2006 preliminary poster (CR000651, card pending) and Haddad & Bechikh Ali 2014 (MORPH-002). This paper adds OMA / DTL / Zemberek with min/max rules under tf×idf.
  - Consistent pattern across them: normalization ≫ none, but prefix truncation stays close to linguistic tools **[MORPH-001 card; MASTER_INDEX]**.
  - Difference: MORPH-002 reports Zemberek as the strongest BM25 configuration **[MASTER_INDEX]**; here, under tf×idf, Zemberek-max is third by MAP (0.3397) behind DTL-max and OMA-max. The tool ranking is not stable across weighting models and studies (cross-paper comparison; the configurations differ).
  - Absolute MAP values are not comparable across these papers (different weighting models, query fields and possibly qrels versions).

## 16. Relationship to CURRENT_GAP

**Classification:** *supports an already occupied boundary claim* + *no material effect on the residual core*.

- **Supports / confirms as occupied** (already listed as a non-claim in v0.8): "raw/stem/lemma ранее не сравнивались в low-resource IR" — for Turkic, several conflation variants were already compared in one controlled lexical setting. This paper is an additional B-level citation next to MORPH-001 and MORPH-002 in `GAP_BOUNDARY` §3.1–3.2.
- **Adds one boundary nuance (not a gap change):** the *lemma-selection rule* (which analysis to keep when several exist) is a first-order factor, as large as the choice of tool. This strengthens the need to define `BM25_lemma` precisely, but it does not touch the interaction question.
- **No material effect on the residual core** of v0.8 refined. Absent from the paper:
  - BM25 (tf×idf only);
  - any dense retriever D, fixed or otherwise;
  - fusion / hybrid conditions `H_raw`, `H_stem`, `H_lemma`;
  - unique relevant hits, overlap, oracle union, incremental hybrid gain;
  - per-query analysis and query features.
- It does not meet any of the four "what can still kill this gap" conditions: not Uzbek, no dense model, no per-query overlap, and it is not a full Turkic analogue of the interaction mechanism (condition 3).

**Proposal:** keep v0.8 refined unchanged. Optionally add this paper to `GAP_BOUNDARY` §3 as a Turkish tf×idf example of controlled multi-tool conflation comparison with an explicit min/max ambiguity factor. This is a proposal only; `CURRENT_GAP.md` has not been edited.

## 17. Implications for our research design

- **Morphology preprocessing — define the lemma condition operationally.**
  - For every Uzbek analyzer/lemmatizer, fix and report: which analysis is kept when there are several (shortest / longest / first / POS-disambiguated), what happens to unanalysable tokens (fallback to surface form, to prefix, or dropped), and whether derivational suffixes are kept.
  - Report per variant: fallback rate, ambiguity rate, and index vocabulary size. Here the min/max rule alone moved MAP by 0.24 for one tool.
  - If more than one selection rule is plausible, choose it on a dev query set, not on the test queries.
- **Baselines / controls.** Keep a prefix-truncation control (e.g., 5 characters) as `BM25_simple-normalization`: it is cheap and here stays within 0.012 MAP of the best tool. Compare stem vs lemma against it, not only against raw.
- **Conflation strength as an explanatory variable.** Vocabulary reduction (term count vs raw) differs 46–96% across variants here. For our complementarity analysis, measure conflation at the collection level and per query (how many query terms change under stem/lemma). It is a candidate query feature for `raw → stem → lemma` changes in unique lexical hits.
- **Metrics / depth.** Report MAP/nDCG and Recall at deep cut-offs *and* early precision; here the morphology gain appears mostly in MAP/bpref, i.e., deeper in the ranking — exactly where lexical and dense candidate sets overlap or differ. Compute unique hits at several depths (e.g., k = 10, 100, 1000).
- **Qrels / pooling.** Pool from all lexical variants, D, and hybrid runs; otherwise normalized variants are judged on a pool they did not help build (the risk flagged in §12). Report bpref or condensed-list metrics as a robustness check.
- **Normalization before morphology.** Fix casing and character normalization *before* the analyzer, identically for all variants (Table II shows mixed casing across variants). Uzbek analogues: apostrophe variants (ʻ ’ ' ‘) in o‘/g‘ and the glottal stop, Latin/Cyrillic script. Context (not from the paper): Turkish, like Uzbek Latin, has locale-specific casing issues (İ/ı), which generic lowercasers handle incorrectly.
- **Statistics.** Use per-query paired tests (and bootstrap CIs) for every `raw/stem/lemma` contrast; with ~70 queries, differences of ~0.01 MAP should not be claimed without them.
- **Weighting model.** Use BM25 with fixed k1/b across all variants as the primary lexical model; optionally add tf×idf as a sensitivity check, since tool rankings on Milliyet differ between tf×idf (this paper) and BM25 (MORPH-002, **[MASTER_INDEX]**).
- **Hypothesis.** No evidence for or against morphology-induced complementarity change. Indirect motivation: normalization changes *which* relevant documents the lexical channel retrieves (relevant retrieved 5194 → 5856 at top-1000 for DTL-max), but whether these are the same documents a dense model already finds is exactly the unmeasured question.

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| Lemma / lemmatization | The dictionary form of a word; finding it for each word | Mapping a word form to its canonical headword, usually via a lexicon/analyzer |
| Stem / root | What remains after cutting suffixes; a root is the minimal lexical core | Output of affix stripping / first morpheme of a morphological analysis |
| Conflation | Treating several word forms as one index term | Many-to-one term mapping `g(w)` before indexing |
| Over-conflation (over-stemming) | Merging unrelated words into one term | `g(w₁) = g(w₂)` for semantically unrelated `w₁, w₂` |
| Min / max lemma | When a tool gives several possible base forms, take the shortest / longest | Ambiguity-resolution rule over the analysis set |
| Fixed prefix truncation (FLT5/FLT7) | Keep only the first 5 / 7 letters of each word | `g(w) = w[:n]` |
| Radix-trie (PATRICIA) | A compact tree for fast dictionary lookup of strings with shared beginnings | Trie with single-child nodes merged |
| tf×idf | Classic weighting: a term counts more if frequent in the document and rare in the collection | Term weight ∝ tf · log(N/df) (exact variant in the paper not reported) |
| BM25 | Improved tf×idf with saturation and length normalization (not used in this paper) | Probabilistic relevance framework scoring, parameters k1, b |
| MAP | Average quality of the whole ranking of relevant documents | Mean over queries of average precision |
| bpref | Ranking quality that ignores unjudged documents | Preference-based measure for incomplete qrels |
| R-precision | Precision at rank R, R = number of relevant documents | P@R |
| Pool bias | Systems that did not contribute to the judged pool can be under-rated | Unjudged-as-non-relevant bias |
| Complementarity (project term) | Each channel finds relevant documents the other misses | Unique relevant hits, overlap, oracle-union gain |

## 19. Open questions / verification needed

1. **Exact tf×idf formula, Terrier version, tokenizer expression, stop-word list, casing** — NOT_REPORTED; only the authors could confirm.
2. **Fallback and ambiguity rates per tool**, and how DTL finds candidates (prefix lookup?) — needed to explain the DTL-min collapse and DTL-max's small vocabulary.
3. **Internal inconsistency — index efficiency:** abstract ("it used the minimum number of terms") and p. 3 ("index term count and size of the index built with DTL-max is the most efficient among others") vs Table III, where DTL-min has fewer terms (18,684 vs 51,708) and a smaller index (81.8 MB vs 161 MB). The claims hold only if DTL-min is excluded, or if "DTL" means the tool rather than the DTL-max variant.
4. **Internal inconsistency — terminology:** OMA is "a morphological analyzer based stemmer" (Sec. I, p. 1) but a "lemmatizer" in Sec. II / Table I, and the paper uses its "first morpheme" (root). Minor: the Sec. I roadmap puts the data set in Sec. 3 and the IR system in Sec. 4, but both are in Sec. III; the conclusion lists five "approaches" (including no-lemmatization) whereas the abstract says four.
5. **"Number retrieved" < 72,000** in all conditions — why did some queries return fewer than 1000 documents?
6. **Qrels version and pool composition** — same as Can et al. 2008? Which topic fields ("all fields")? Total relevant documents?
7. **Bibliographic record:** DOI `10.1109/INISTA.2012.6246934`, proceedings pages and conference place/date could not be fully verified from this environment (resolver/IEEE/Crossref blocked); confirm in IEEE Xplore.
8. Is there a later journal/thesis version by Ozturkmenoglu (e.g., a Dokuz Eylül thesis) with BM25 or significance tests? Not searched (source rule); a lead for the coordinator only.

## 20. Decision after deep dive

- **Keep current gap?** Yes. v0.8 refined remains valid (§16).
- **Modify gap?** No change proposed. Optionally list this paper in `GAP_BOUNDARY` §3 next to Can et al. 2008 and Haddad & Bechikh Ali 2014 as a third Milliyet study (tf×idf, three tools × min/max, prefix controls). Researcher's decision.
- **Add decision?** Proposed for `decisions/DECISIONS.md` (researcher's decision): "Each morphological condition (stem, lemma) must specify the analysis-selection rule, the fallback for unanalysable tokens and derivational handling; fallback rate, ambiguity rate and index vocabulary size are reported for every condition; selection rules are chosen on dev queries only."
- **Add experiment?** Low-cost addition to the Uzbek pilot: for the lemma condition, run both a shortest- and a longest-analysis rule (plus a 5-character prefix control) and record how unique lexical hits vs D change. This tests whether the "lemma" effect on complementarity is robust to the selection rule.
- **Add citation to Chapter I?** Yes, briefly:
  - §1.1, as Turkic evidence that the choice of conflation tool and of the ambiguity rule changes lexical retrieval effectiveness, and that prefix truncation remains competitive;
  - §1.3 / conclusions, as an example of a morphology study confined to the lexical channel (no semantic retrieval, no complementarity analysis).
- **Proposed `MASTER_INDEX.md` row** (to add after approval):

| MORPH-018 | Ozturkmenoglu & Alpkocak — *Comparison of Different Lemmatization Approaches for Information Retrieval on Turkish Text Collection* (INISTA 2012, IEEE) — [deep dive](deep-dives/2012_Ozturkmenoglu_Alpkocak_Turkish_Lemmatization_IR.md) | 2012 | B | HIGH | Milliyet (408,305 docs, 72 queries), Terrier **tf×idf** (not BM25): 9 representations = NL, OMA/DTL/Zemberek × min/max-length lemma, prefix-5/7. DTL-max best on all metrics (MAP 0.3486 vs NL 0.3098; bpref 0.4755 vs 0.4), but only +0.0067–0.0144 MAP over OMA-max/ZEM-max/FLT5/FLT7; DTL-min collapses (MAP 0.1121). Max > min for every tool; gains mainly in MAP/bpref, mixed on P@10/P@20. No significance tests, no BM25, no dense/fusion, no overlap/unique-hit/per-query analysis. |
