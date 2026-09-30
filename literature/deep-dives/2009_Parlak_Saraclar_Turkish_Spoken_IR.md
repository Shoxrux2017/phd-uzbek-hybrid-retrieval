# Parlak & Saraçlar (2009): Spoken Information Retrieval for Turkish Broadcast News

**Targeted deep-dive status:** COMPLETED (AI-assisted, pending researcher review)
**Completed:** 2026-09-28
**Literature ID:** `MORPH-014` (assigned 2026-09-28, approved by researcher)
**Systematic-review record:** `CR000691`. Full-text triage: INCLUDE, reading priority HIGH, reading tier 1, `carries_complementarity_evidence = YES`. The YES flag comes from the IV/OOV query split and the word+morph cascade, and both belong to the **spoken term detection** part, not to document retrieval (see §10, §16).
**Provenance:** AI-assisted deep dive (Claude). The whole paper was read (2 pages, printed pp. 782–783): the pdftotext text plus page images of **both** pages. Tables 1 and 2 (p. 783) were also checked on a 250-dpi crop. Every number below comes with its table/section and printed page. Numbers computed by us are marked **[computed]** and were computed in Python.
**Source rule:** **the paper is the primary and only authoritative source.** Web lookup was used only for the bibliographic record (see §1). The related journal paper by the same group (CR001390; ref. [1] of this paper) is mentioned only as a corpus relation. Nothing is concluded about this paper from it.
**Verification:** independent AI verifier pass 2026-09-28; 7 findings addressed.
**Reliability:** **A for the venue:** peer-reviewed, ACM SIGIR '09 proceedings, as the paper's own copyright block states. **Narrow evidence strength:** it is a 2-page paper with no stated query counts, retrieval-model settings or test details.

---

## Кратко для исследователя (RU)

- **Что сделано.** Поиск по турецким новостным радио- и телепередачам на двух задачах:
  - **обнаружение терминов в речи** (spoken term detection, STD): найти, где в записи произнесено слово запроса;
  - **поиск речевых документов** (spoken document retrieval, SDR): ранжирование 2 425 новостных сюжетов по запросу.
  Документы индексируются по ручным (reference) транскриптам и по выходу ASR. ASR (автоматическое распознавание речи) использует разные единицы языковой модели: слово, морфологические stem+ending (G-SE), морфы Morfessor (Morph), статистические stem+ending (S-SE).
- **Морфологические варианты лексического представления в SDR есть.** Сравниваются четыре единицы индексирования:
  - NS — словоформа без стемминга;
  - FP — первые 5 символов слова;
  - G-Stem — основа от морфологического парсера;
  - S-Stem — первый морф Morfessor.
  Поисковая модель — векторная модель (VSM), метрика — BPref (Sec. 5, Table 2, p. 783).
- **Главные числа SDR** (Table 2, p. 783; BPref ×100, только пользовательские запросы):
  - reference-транскрипты: NS 38.85 → FP 43.15 / G-Stem 43.73 / S-Stem 43.66;
  - ASR с word-LM: NS 37.64 → 41.73 / 41.89 / 42.66;
  - любой стемминг даёт +3.5…+5.3 пункта (+9…+14% отн.) **[computed]**.
- **Основа от парсера ≈ основа Morfessor:** разница незначима (со слов авторов). Обе лишь на 0.2–1.6 пункта выше простого префикса FP **[computed]**, и авторы предпочитают FP «из-за простоты». Эффект стемминга (~4–5 пунктов) больше, чем потеря от ошибок ASR (~0.7–1.8) **[computed]**.
- **Главные числа STD** (Table 1, p. 783; MTWV ×100): word 56.71; подсловные единицы (Morph, S-SE, G-SE) 60.62–62.74. Каскад «слово для словарных (IV) запросов + морф для внесловарных (OOV)» даёт 64.75. Сопоставление по основе (stem matching) поднимает G-SE с 62.74 до 65.71.
- **Чего нет:**
  - **BM25 нет** (только VSM, настройки весов не описаны);
  - **плотного/нейросетевого поиска нет**;
  - **гибрида лексического и семантического каналов нет**;
  - **перекрытия, уникально найденных релевантных документов, oracle union нет**;
  - **разбора по запросам в SDR нет**.
  Разбиение запросов на IV/OOV и каскад есть только для STD. Это поиск вхождений термина по решётке ASR, а не ранжирование документов.
- **Не сообщается:** число пользовательских запросов, тип теста значимости, глубина пула, имя морфологического парсера, схема весов VSM. Результаты коротких и сжатых (terse) формулировок тем тоже не приводятся.
- **Для нашего gap:** работа подтверждает (supports) уже занятые утверждения: морфологическое представление заметно меняет лексический поиск в тюркском языке, а простой 5-символьный префикс почти так же хорош, как лингвистическая основа. Это турецкая работа с таким же выводом наряду с Can 2008 и Haddad 2014. Ядро v0.8 (raw/stem/lemma BM25 × фиксированный D → overlap/unique hits → прирост гибрида) **не затрагивает**. Предложение: gap не менять.
- **Практическая польза для нас:**
  1. Добавить **BM25_prefix-n** как дешёвый контроль рядом с raw/stem/lemma. Длину n подбирать на dev: в узбекской латинице диграфы (sh, ch, ng, o‘, g‘) занимают по 2 символа (наш вывод, не из статьи).
  2. Каскад STD — исторический пример того, что разные морфологические представления индекса полезны на разных классах запросов (IV/OOV). Отсюда признак запроса «доля словоформ запроса, отсутствующих в индексе raw» как кандидат для per-query анализа.
  3. Пул для qrels собирать из прогонов всех лексических вариантов и D, чтобы уникальные находки каждого канала были размечены. При неполной разметке BPref остаётся полезной дополнительной метрикой.

---

## 1. Bibliographic record

- **Authors:**
  - Sıddıka Parlak: Rutgers University, Electrical and Computer Engineering Dept.;
  - Murat Saraçlar: Boğaziçi University, Electrical and Electronics Engineering Dept.
  Affiliations as printed on p. 782.
- **Year:** 2009
- **Venue (from the paper's copyright block, p. 782):** "SIGIR'09, July 19–23, 2009, Boston, Massachusetts, USA", ACM 978-1-60558-483-6/09/07.
- **Pages:** 782–783 (printed page numbers).
- **Publisher:** ACM
- **DOI:** `10.1145/1571941.1572126`, verified (bibliographic check: Crossref record, consulted by the independent verifier on 2026-09-28).
  - The record matches: title "Spoken information retrieval for turkish broadcast news"; authors Siddika Parlak (Rutgers) and Murat Saraclar (Bogazici); pages 782–783; published 2009-07-19.
  - Container: *Proceedings of the 32nd international ACM SIGIR conference on Research and development in information retrieval*.
  - The writer's own lookup reached only an ACM Digital Library URL from a web search; the ACM page returned 403 and Crossref was rate-limited.
- **Track:** not stated in the paper. The 2-page format is consistent with a SIGIR short/poster paper; the triage notes call it a poster (inference, not verified).
- **Metadata discrepancy:** the systematic-review record gives the venue as "SIGIR Forum" (JOUR). The paper itself identifies SIGIR'09 conference proceedings. **Proposed correction:** cite it as SIGIR '09 proceedings (Proceedings of the 32nd international ACM SIGIR conference), pp. 782–783. The Crossref record above confirms this.
- **Funding (p. 783):** TUBITAK project 105E102; Boğaziçi University Research Fund 05HA202.
- **Source type:** peer-reviewed conference short paper (2 pages).
- **Reliability:** A (venue); narrow evidence strength.
- **Full text available:** yes (`07_full_text/pdfs/CR000691.pdf`, 2 pages).

## 2. Why this work matters to the PhD

| Axis | Relation |
|---|---|
| Lexical retrieval | Direct but dated: vector space model (VSM) document retrieval with four indexing units (NS / FP / G-Stem / S-Stem). **No BM25** |
| Semantic retrieval | Absent. "Semantic" appears only in the authors' explanation that "a common stem usually bears semantic relation" (Sec. 6) |
| Hybrid retrieval | Absent for lexical + semantic. The STD part has a **word + morph index cascade**, a combination of two *lexical/subword* representations routed by query class (IV/OOV) |
| Uzbek morphology | Indirect but close: Turkish is the nearest well-studied Turkic, agglutinative relative of Uzbek |
| Low-resource retrieval | Moderate: small in-house collection (2,425 stories) with human judgments; noisy ASR text |
| Current gap | Supports the already-occupied claim that morphological representation matters in Turkic lexical IR. Does not touch the lexical–dense complementarity core (§16) |

## 3. Research problem

### Simple explanation

When news broadcasts are searched through automatic transcripts, two things go wrong in Turkish:

- words that the recognizer does not know (out-of-vocabulary, OOV) are never written down correctly;
- the same word appears in many suffixed forms.

The authors test whether splitting words into smaller pieces, both for the recognizer and for the search index, helps two tasks:

- finding where a query term is spoken (STD);
- finding relevant news stories (SDR).

### Formal formulation

- **STD:** given a query term, return its occurrence times in the audio with scores; detect by thresholding the scores (Sec. 4, p. 783). Evaluated with MTWV.
- **SDR:** given a query, rank the 2,425 news stories; VSM retrieval; evaluated with BPref via trec_eval (Sec. 5, p. 783).
- Factors varied:
  - the **LM unit** of ASR: word / G-SE / S-SE, plus Morph in STD;
  - the **indexing unit** for SDR: NS / FP / G-Stem / S-Stem;
  - the hypothesis representation: 1-best vs confusion networks (CN) in SDR; lattices in STD.

## 4. Main idea

### Simple explanation

Cut Turkish words into a stem and an ending, using either a grammar-based parser or an unsupervised statistical method (Morfessor). Then:

- use these pieces in the recognizer;
- index only the stem (or simply the first 5 letters), so that different suffixed forms of a word match each other.

### Concrete example (the paper's own, Sec. 3, p. 782)

Phrase "dünya kupası finalinde" (in the world cup final):

| Unit | Parse |
|---|---|
| Word | dünya kupası finalinde |
| G-SE (grammatical stem+ending) | dünya kupa +sı final +inde |
| Morph (Morfessor) | dün +ya kupası final +in +de |
| S-SE (statistical stem+ending) | dün +ya kupası final +inde |

- Index terms per unit:
  - **G-Stem** keeps `dünya, kupa, final`;
  - **S-Stem** keeps `dün, kupası, final`;
  - **FP (n = 5)** keeps the first five characters.
- STD example (Sec. 4): a search for *Ankara* should also return *Ankara'+ya* ("to Ankara") and *Ankara'+da* ("in Ankara").
- Context (not from the paper): Morfessor splits "dünya" into "dün +ya" here, and "dün" is also a separate Turkish word ("yesterday"). The statistical stem can therefore conflate unrelated words. "kupası" is left unsplit, so its S-Stem keeps the possessive suffix. The paper shows the parse but does not comment on these errors.

### Formal method

- **SDR:** VSM ranking over the chosen index terms. The term weighting, normalization, stop-word handling and query processing are **NOT_REPORTED**.
- **STD:** lattices indexed and searched with weighted finite-state transducer operations; detection by thresholding the relevance scores (Sec. 4, citing [7]).

## 5. Architecture / algorithm

1. **ASR** (built by colleagues, see the Acknowledgments). Its configuration is **NOT_REPORTED** in this paper. The paper cites [1] only for the BN database (Sec. 2); that the ASR is described in [1] is our inference, not a statement in the paper.
   - LM units: word, Morph (Morfessor), S-SE, G-SE.
   - Recognition output: 1-best, CNs (SDR) or lattices (STD).
2. **Subword units** (Sec. 3):
   - morphemes from "a morphological parser" (**the parser is not named**), merged into 2-piece G-SE;
   - morphs from Morfessor (MDL-based, [3]);
   - S-SE = first morph + all remaining morphs grouped as the ending.
3. **SDR indexing units** (Sec. 3):
   - NS = the whole word;
   - FP = first *n* = 5 characters (following [2], Can et al. 2008 = MORPH-001);
   - G-Stem = first part of G-SE;
   - S-Stem = first part of S-SE.
   - When the LM unit is a subword and the indexing unit is NS, the stems and endings in the ASR output are joined back into words before indexing (Sec. 5).
4. **SDR retrieval:** "the traditional Vector Space Modeling technique" (Sec. 5). No other retrieval model.
5. **STD:** WFST-based lattice index. Additional variants:
   - **stem matching**: match only the stem of the query term;
   - **cascade**: the word index for in-vocabulary (IV) queries and the morph index for OOV queries (Sec. 4).

## 6. Data

- **Corpus:** Boğaziçi Turkish Broadcast News database, collected since March 2006 [1], "approximately 277 hours of transcribed speech" (Sec. 2, p. 782).
- **SDR collection:** a 74-hour portion (135 programmes), manually segmented into **2,425 news stories** and "labeled with a topic" (Sec. 2).
- **Topics:** 27 topics, each in two forms (Sec. 2):
  - **short**: sentence-like, e.g. "Türkiye'de ve dünyada son zamanlarda gerçekleşmiş uçak kaçırma, hava korsanlığı vakalarını bul." (Find the recent skyjacking cases in Turkey and the world.);
  - **terse**: keyword-like, e.g. "Uçak kaçırma hava korsanlığı" (Skyjacking cases).
- **Query sets:** short topics, terse topics, and a third set of **user queries**: keywords that the assessors submitted "to view the news stories related to a given topic" (Sec. 5).
  - **Only the user-query set is reported** (Table 2 caption: "over the user queries").
  - The **number of user queries is NOT_REPORTED**.
- **Relevance judgments:**
  - 8 human assessors;
  - "Search is performed several times (runs) with various methods. The results are pooled and the top documents of the pool are displayed to the assessor [4]" (Sec. 5).
  - **NOT_REPORTED:** pool depth, which runs were pooled, relevance grades, inter-assessor agreement, and the number of judged or relevant documents per topic.
  - How the Sec. 2 topic labels relate to the Sec. 5 assessor judgments is not explained.
- **STD test set:** 3 hours (Sec. 4). The number of STD query terms is **NOT_REPORTED**. By unit, 7.6–27.3% of queries are OOV (Table 1).
- **Train/dev/test for retrieval:** not applicable or **NOT_REPORTED**. No tuning of retrieval parameters is described.

## 7. Baselines

| Baseline | What it is | Fair comparison? |
|---|---|---|
| NS (no stemming) | Surface word forms | Yes, the natural raw baseline. VSM weighting is unreported but presumably shared |
| FP (5-char prefix) | Language-independent truncation stemmer, from [2] | Yes. n = 5 is taken from prior work, not tuned here |
| Reference transcripts | Manual transcripts: an upper bound for ASR-based indexing | Yes, an oracle-text condition |
| Word-LM ASR | Standard recognizer | Yes, the baseline for the subword LMs |
| Word index (STD) | Whole-word lattice index | Yes, but it cannot, by construction, find OOV queries (Table 1: OOV cell "-") |

There is no BM25, language-model or other retrieval model, and no semantic or dense baseline.

## 8. Metrics

| Metric | Simple meaning | Notes |
|---|---|---|
| **BPref** (SDR) | How often the judged relevant documents are ranked above the judged non-relevant ones. Unjudged documents are ignored | Context (not from the paper): Buckley & Voorhees' measure, designed for incomplete judgments; suitable for pooled qrels. The table reports it ×100 |
| **MTWV** (STD) | NIST term-detection score: 1 minus a weighted sum of miss and false-alarm rates, at the best global threshold | Context (not from the paper): TWV weights false alarms heavily; "Maximum" means the best single threshold. The table reports it ×100 |
| WER | Share of words the recognizer gets wrong | Table 1, STD test set only |
| OOV / OOV-q | % of tokens / % of queries that are out of the unit's vocabulary | Table 1 |

The WER of the SDR collection (the 74-hour portion) is **NOT_REPORTED**. The Sec. 5 remark "despite lower OOV rates and WERs" can only be read against Table 1, which uses the 3-hour STD set.

## 9. Results

### Table 2: SDR BPref over the user queries (p. 783; rows = indexing unit, columns = transcript / LM unit)

| Indexing unit | Reference | Word LM | G-SE LM | S-SE LM |
|---|---:|---:|---:|---:|
| No Stemming (NS) | 38.85 | 37.64 | 38.14 | 37.69 |
| Fixed-Prefix (FP, n = 5) | 43.15 | 41.73 | 41.63 | 41.37 |
| G-Stem | 43.73 | 41.89 | 41.98 | – |
| S-Stem | 43.66 | 42.66 | – | 42.94 |

The "–" cells (G-Stem with the S-SE LM, S-Stem with the G-SE LM) are **not explained** in the paper.

Derived values **[computed]**:

- **Stemming vs NS**, absolute BPref points and relative gain:
  - Reference: FP +4.30 (+11.1%), G-Stem +4.88 (+12.6%), S-Stem +4.81 (+12.4%);
  - Word LM: FP +4.09 (+10.9%), G-Stem +4.25 (+11.3%), S-Stem +5.02 (+13.3%);
  - G-SE LM: FP +3.49 (+9.2%), G-Stem +3.84 (+10.1%);
  - S-SE LM: FP +3.68 (+9.8%), S-Stem +5.25 (+13.9%).
- **Linguistic/statistical stem vs FP:** +0.16 to +1.57 points. Reference +0.58 / +0.51; Word LM +0.16 / +0.93; G-SE +0.35; S-SE +1.57.
- **ASR vs reference**, same indexing unit: −0.71 to −1.84 points (−1.6% to −4.2%).
- **Subword LM vs word LM**, same indexing unit: −0.36 to +0.50 points. Subword LMs are numerically higher in 4 of 6 comparable cells. The authors conclude that subword LMs do "not improve the performance", which "Significance tests verify". We read this as "no significant improvement", not "numerically lower".
- The best ASR configuration (S-SE LM + S-Stem, 42.94) is **4.09 points above** NS on the *reference* transcripts (38.85). With these data, the indexing representation matters more than the ASR errors.

Authors' statements (Sec. 5, p. 783):

- "all stemming algorithms provide a considerable improvement". The test used and significance vs NS are not stated explicitly.
- "The difference between the performance of G-Stems and and S-Stems is not statistically significant. They both outperform the FP approach by creating meaningful units. Nevertheless, the difference is small enough to prefer the FP method because of its simplicity." ("and and" is in the original.)
- CN indexing: "We do not notice a significant gain by indexing CNs". **No numbers are reported.**

### Table 1: STD statistics and MTWV (3-hour test set, p. 783)

| Unit | WER | OOV | OOV-q | MTWV all | MTWV IV | MTWV OOV |
|---|---:|---:|---:|---:|---:|---:|
| Word | 26.9 | 1.9 | 27.3 | 56.71 | **72.33** | – |
| Morph | 26.1 | 0.6 | 7.6 | 60.62 | 67.74 | **41.02** |
| S-SE | 25.6 | 1.0 | 11.8 | 60.63 | 69.23 | 35.86 |
| G-SE | 25.7 | 0.9 | 8.1 | **62.74** | 71.88 | 37.52 |

- **Cascade** (word for IV, morph for OOV): MTWV "up to 64.75" (Sec. 4). That is +2.01 over the best single unit (G-SE, +3.2% relative) and +8.04 over word **[computed]**.
- **Stem matching:** G-SE 62.74 → 65.71 (+2.97, +4.7%); Morph 60.62 → 64.15 (+3.53, +5.8%) **[computed]**. No cascade combined with stem matching is reported.
- Subword units lose on IV queries (−0.45 to −4.59 vs word) and gain overall by finding OOV queries **[computed]**.
- Note: the IV/OOV partition depends on the unit (OOV-q ranges from 7.6% to 27.3%), so the IV and OOV columns are not computed over the same query subsets across rows. The partition used for the cascade is **NOT_REPORTED**. We did not try to recompute the cascade score: MTWV uses a global threshold and is not a simple weighted average.

## 10. Statistical evidence

- **Significance test:** mentioned twice without naming the test ("Significance tests verify our observations"; "not statistically significant"). Test type, p-values and alpha are **NOT_REPORTED**. Significance of stemming vs NS and of stems vs FP is not stated explicitly. STD "significant gain" (Sec. 4): test NOT_REPORTED.
- **Confidence intervals:** NOT_REPORTED.
- **Runs / seeds:** not applicable (deterministic VSM); ASR variability NOT_REPORTED.
- **Ablation:** the factorial LM-unit × indexing-unit table serves as a partial ablation of where segmentation helps (index vs ASR).
- **Per-query analysis:**
  - SDR: **none**. No per-topic results, no query-type breakdown, and short/terse topics are not reported.
  - STD: query-class breakdown by IV vs OOV (Table 1) plus the class-routed cascade.
- **Overlap / unique relevant hits / oracle union between representations or channels:** **none**, in SDR or STD.

## 11. Strengths

- A factorial design separates segmentation in the **recognizer** from segmentation in the **index**. It shows that only the latter helps SDR.
- Grammatical vs unsupervised statistical vs trivial prefix stemming are compared on the same collection and judgments.
- Human-assessed relevance with pooling, and a metric designed for incomplete judgments (BPref).
- The IV/OOV query split in STD is an early explicit query-class analysis in which different morphological representations serve different query classes.

## 12. Limitations

### Stated by the authors

- The authors report no explicit limitations. They note that the G-Stem vs S-Stem difference is not significant, and that the small stem-vs-FP difference makes FP preferable for simplicity (Sec. 5).

### Inferred from the experimental design

1. **Retrieval model under-specified:** "traditional" VSM, with weighting, normalization and stop-words NOT_REPORTED. No BM25, so the stemming effect is shown only for one lexical model.
2. **Query and qrels scale unknown:** the number of user queries, the pool depth and the number of relevant documents are not reported, so the precision of the BPref differences cannot be judged.
3. **Only the user-query set is reported.** Short and terse topics were built but their results are not shown, so query formulation and length effects cannot be assessed here.
4. **Significance reporting is minimal** (no test name, no p-values). The "outperform FP" claim is not accompanied by a significance statement.
5. **Unexplained missing cells** in Table 2, and the morphological parser is unnamed.
6. **The contrast "alternative hypotheses help STD but not SDR" (Abstract, Sec. 6) is not measured within this paper.**
   - The STD benefit is supported by citation ([7]), and no 1-best vs lattice STD comparison is shown.
   - SDR used CNs while STD used lattices, so retrieval type is confounded with the hypothesis representation.
   - No CN numbers are given.
7. **The STD cascade is structurally guaranteed to help only relative to the word index.** The word index has no OOV score ("-" in Table 1), so adding a morph index for OOV queries must help it. A gain over the best single unit (G-SE, 62.74) is not guaranteed by construction, because MTWV uses one global threshold; that gain was observed (64.75). Either way the cascade shows class-level complementarity, not measured document-level complementarity.
8. Spoken, noisy-text setting. Results on reference transcripts are the part closest to text IR.

## 13. What the work proves

- On a Turkish broadcast-news SDR collection with human judgments and VSM retrieval, **every tested stemming representation improves BPref over surface word forms by about 3.5–5.3 points (≈9–14% relative)**, on both reference and ASR transcripts (Table 2) **[computed]**.
- **Grammatical (parser) stems and unsupervised Morfessor stems perform about equally** (the difference is "not statistically significant", per the authors). **A 5-character prefix comes within 0.2–1.6 BPref points** of both.
- **Subword LM units in ASR do not improve SDR** despite lower WER/OOV (per the authors' significance tests). Caveat: the only WER/OOV figures come from the 3-hour STD test set (Table 1), not the SDR collection (§8). The benefit of segmentation for document retrieval comes through the index representation.
- In **STD**, subword units recover OOV query terms (OOV MTWV 35.86–41.02; the word index has no OOV score, "-" in Table 1). A word/morph cascade routed by query class reaches MTWV 64.75, above every single unit in Table 1. Separately, stem matching raises single-unit MTWV, up to 65.71 for G-SE (Table 1, Sec. 4).

## 14. What the work does NOT prove

- **Anything about BM25**, or whether the stemming effect holds under BM25 length normalization and saturation.
- **Anything about semantic or dense retrieval**, or about lexical–semantic hybrids.
- **That stemming changes which relevant documents are found** (overlap / unique relevant hits). Only aggregate BPref is reported.
- **That grammatical stems are better than statistical ones or than prefixes in general.** Differences are small, with one collection and one query set.
- **Per-query or query-feature effects in document retrieval.** The IV/OOV analysis concerns term detection, and the classes are defined relative to the ASR vocabulary, not query morphology.
- **That lemmatization helps.** No lemma condition exists. G-Stem is the parser's stem with suffixes stripped, and whether derivational suffixes are removed is not stated.

## 15. Relationship to current Uzbek evidence

- No Uzbek data. Turkish is the closest agglutinative, suffixing Turkic relative, so the finding that suffix normalization helps lexical retrieval plausibly transfers in direction. The size of the effect does not transfer automatically.
- **The Turkish cluster is consistent:**
  - Can et al. 2008 (MORPH-001, the source of FP n = 5);
  - Haddad & Bechikh Ali 2014 (MORPH-002, BM25);
  - this paper, in a noisy spoken-document setting.
  All three find that morphological normalization helps Turkish lexical IR and that simple prefix truncation stays highly competitive with linguistic analysis.
- The Uzbek national evidence (Bakaev, Xusainova, Elov) provides analyzers and stemmers but no qrels-based raw/stem/prefix comparison. This paper is an example of the missing measurement for a sister language.
- **Related record in our corpus:** CR001390 (Arısoy, Can, Parlak, Sak & Saraçlar, 2009) is ref. [1] of this paper, from the same group. Ref. [1] is printed as "IEEE Transactions on Speech and Audio Processing, June 2009" (p. 783). Our corpus metadata gives "IEEE Transactions on Audio, Speech, and Language Processing"; this is a bibliographic difference from the paper's own reference, not resolved here. Per its triage record it covers ASR and STD (MTWV, IV/OOV, word+morph cascade). A keyword search of its extracted text finds no SDR/BPref experiment. Its own card should confirm this. The SDR stemming evidence therefore appears only in the present 2-page paper.

## 16. Relationship to CURRENT_GAP

**Classification:** *supports* (already-occupied premises) + *no material effect on the residual core*.

- **Supports / confirms as occupied** (these are already v0.8 non-claims):
  - "morphology was not applied to Turkic search";
  - "raw vs stem not compared in an agglutinative language".
  A 2009 A-venue example, including an unsupervised (Morfessor) stem variant and a prefix control.
- **Weak precedent relevant to the core idea:** the STD cascade shows that different morphological index representations serve different **query classes** (IV vs OOV). This is a class-level complementarity between *representations*. It motivates our per-query question in spirit.
  - It is **not** lexical–dense complementarity;
  - it is not measured as unique relevant documents;
  - it is not in ranked document retrieval.
- **No material effect on the core v0.8 elements:**
  - raw/stem/lemma **BM25** × a **fixed dense D**;
  - unique relevant hits / overlap / oracle union;
  - incremental hybrid gain;
  - link to Uzbek query features.
  None of these is present.
- None of the four "What can still kill this gap" conditions is met.

**Proposal:** keep v0.8 refined unchanged. Optionally list this paper with Can 2008 and Haddad 2014 in the Turkish boundary (GAP_BOUNDARY §3.1–3.2) as spoken-document evidence. This is a proposal only; `CURRENT_GAP.md` has not been edited.

## 17. Implications for our research design

- **Morphology preprocessing / controls:**
  - Add **BM25_prefix-n** as a low-cost control beside raw/stem/lemma, matching the optional `BM25_simple-normalization` slot in CURRENT_GAP. Three Turkish studies find it close to linguistic stemming.
  - Our inference: in Uzbek Latin script the digraphs `sh`, `ch`, `ng` and `o‘`/`g‘` (with an apostrophe variant) take 2 characters. Choose n on dev after apostrophe normalization, not by copying n = 5.
- **Optional unsupervised stem variant:** a Morfessor-style stem performed on par with the parser stem here. If Uzbek analyzer coverage is uneven, an unsupervised stem is a useful robustness control. It must be reported as a separate representation, not as "lemma".
- **Qrels / pooling:** pool the top-k of **every** lexical variant **and** D (and the hybrids), so that each channel's unique hits get judgments. Report the pool depth and assessor agreement; this paper omits both. Include BPref (or condensed-list metrics) as a secondary metric alongside nDCG/Recall for robustness to unjudged documents.
- **Query taxonomy:** candidate per-query feature: the **share of query word forms absent from the raw index vocabulary** (a text analogue of IV/OOV), plus query formulation (keyword vs sentence). This paper built short and terse topics but reported only user keyword queries. Build both formulations for Uzbek, and report both.
- **Metrics / reporting:** name the significance test, report p-values and per-query distributions. Report the retrieval-model parameters explicitly: this paper leaves VSM weighting unspecified, the same flaw as unconfigured BM25.
- **Hypothesis:** consistent with (not evidence for) our expectation that raw → stem changes lexical-channel behaviour substantially in a Turkic language. Whether it changes the channel's *unique contribution* relative to D is still untested.

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| ASR | Software that turns speech into text | Automatic speech recognition, producing 1-best text, lattices or CNs |
| OOV / IV | A word the recognizer's vocabulary does not / does contain | Out-of-vocabulary / in-vocabulary relative to the LM unit inventory |
| WER | % of words the recognizer gets wrong | (substitutions + deletions + insertions) / reference words |
| Lattice / confusion network (CN) | Instead of one transcript, a compact graph of alternative word guesses with probabilities | Weighted hypothesis graph; a CN is a linearized, aligned version |
| STD | Find where a spoken term occurs in audio | Detection of term occurrences with scores and a threshold |
| SDR | Find the relevant spoken documents (here: news stories) | Ranked retrieval over transcribed documents |
| G-SE / G-Stem | Stem + combined ending from a grammar-based parser / just the stem | Morphological-analyzer segmentation into 2 pieces |
| Morph / S-SE / S-Stem | Pieces found statistically by Morfessor / first morph + rest / just the first morph | Unsupervised MDL segmentation |
| FP (fixed prefix) | Keep only the first 5 letters of each word | Truncation stemmer, n = 5 |
| VSM | Classic ranking: query and document as term-weight vectors, compared by angle | Vector space model (weighting unspecified here) |
| BPref | Are the judged relevant documents ranked above the judged non-relevant ones? Unjudged ones are ignored | Binary-preference measure for incomplete judgments |
| MTWV | Term-detection score that penalizes misses and (heavily) false alarms, at the best threshold | Maximum term-weighted value (NIST STD 2006) |
| Cascade (here) | Use the word index for some queries and the morph index for others | Class-routed combination of two index representations |
| Complementarity (project term) | Each channel finds some relevant items the other misses | Unique relevant hits, overlap, oracle-union gain |

## 19. Open questions / verification needed

1. **Venue metadata:** correct "SIGIR Forum" (systematic-review record) to SIGIR '09 proceedings, pp. 782–783. DOI `10.1145/1571941.1572126` verified via Crossref (independent verifier).
2. Number of user queries, pool depth, number of relevant documents, and assessor agreement: NOT_REPORTED.
3. Significance test type and p-values; whether stemming vs NS and stems vs FP were tested.
4. VSM weighting scheme; the morphological parser used for G-SE.
5. Why the G-Stem × S-SE and S-Stem × G-SE cells are empty.
6. Results for the short and terse topic sets (built but not reported).
7. How the Sec. 2 story topic labels relate to the Sec. 5 pooled assessor judgments.
8. Check the CR001390 card to confirm that it contains no SDR experiment. If it has none, this 2-page paper is the group's only reported SDR stemming result.

## 20. Decision after deep dive

- **Keep current gap?** Yes. v0.8 refined remains valid (§16).
- **Modify gap?** No. Optionally add this paper to the Turkish evidence boundary, next to MORPH-001 and MORPH-002 (researcher's decision).
- **Add decision?** Proposed for `decisions/DECISIONS.md` (researcher's decision):
  - "Include a prefix-truncation BM25 control (n tuned on dev after apostrophe normalization) alongside raw/stem/lemma";
  - "Qrels pool must include the top-k of every lexical variant and of D".
- **Add experiment?** Optional cheap add-on: an unsupervised-stem (Morfessor-type) BM25 variant as a robustness control. Not required for the core.
- **Add citation to Chapter I?** Yes, §1.1: in Turkic lexical IR, stemming helps and prefix truncation is competitive; spoken-document setting. Cite it together with Can 2008 and Haddad 2014, not as a hybrid-retrieval source.
- **Proposed `MASTER_INDEX.md` row** (to add after approval):

| MORPH-014 | Parlak & Saraçlar — *Spoken Information Retrieval for Turkish Broadcast News* (SIGIR '09, pp. 782–783) — [deep dive](deep-dives/2009_Parlak_Saraclar_Turkish_Spoken_IR.md) | 2009 | A (2-page; narrow evidence) | HIGH | Turkish SDR on 2,425 BN stories (VSM, BPref, pooled judgments by 8 assessors, user keyword queries): NS vs 5-char prefix vs parser stem vs Morfessor stem, × reference/ASR transcripts. All stemming +3.5–5.3 BPref over NS; parser ≈ Morfessor stem (n.s.), both only 0.2–1.6 above prefix; subword ASR LMs do not help SDR. STD part: IV/OOV split and word+morph cascade (MTWV 64.75). No BM25, dense, lexical–semantic fusion, overlap/unique-hit or per-query SDR analysis. |
