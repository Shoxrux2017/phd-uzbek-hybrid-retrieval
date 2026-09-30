# McNamee, Nicholas & Mayfield (2009): Addressing Morphological Variation in Alphabetic Languages

**Targeted deep-dive status:** COMPLETED (AI-assisted, pending researcher review)
**Completed:** 2026-09-28
**Literature ID:** `MORPH-035` (assigned 2026-09-28, approved by researcher)
**Systematic-review record:** `CR000688`. Full-text triage: INCLUDE, reading priority HIGH, reading tier "2 — важно", `carries_complementarity_evidence = NO` (we agree: the analysis is per language, not per query; §10). Two corrections to the review metadata:
- The record gives the venue as *SIGIR Forum* (JOUR). The PDF itself is the **SIGIR '09 conference paper** (first-page footer: "SIGIR'09, July 19–23, 2009, Boston, Massachusetts, USA. Copyright 2009 ACM 978-1-60558-483-6/09/07"; printed pp. 75–82). See §1.
- The triage language list leaves out Arabic, Hindi and Marathi. The paper's 18 languages are in Table 2 (p. 77).
**Provenance:** AI-assisted deep dive (Claude). The whole paper (8 PDF pages = printed pp. 75–82) was read from the pdftotext extraction. Page images were checked for:
- p. 75 (header, abstract, venue footer);
- p. 76 (Table 1);
- p. 77 (Table 2, Eq. 1, footnote 6);
- p. 78 (Table 3, 200-dpi render);
- p. 79 (Tables 4–5, 200-dpi render, to read the ▲/△ significance marks);
- p. 80 (Tables 6–7, 200-dpi render);
- p. 81 (Figure 1, 220-dpi crop).
Page references below are the printed page numbers. Numbers computed by us are marked **[computed]** and were recomputed with Python. Values read off Figure 1 by pixel measurement are marked **[computed, approximate]**.
**Source rule:** **the paper is the primary and only authoritative source.** No code, website, later paper or background knowledge is used as evidence about what the authors did. Background knowledge appears only as labelled "Context (not from the paper)". Web use was limited to the bibliographic record (§1).
**Reliability:** **A** (peer-reviewed full paper, ACM SIGIR 2009, the main IR conference).
**Verification:** independent AI verifier pass 2026-09-28; 6 findings addressed.

---

## Кратко для исследователя (RU)

- **Что сделано.** Крупное контролируемое сравнение **18 вариантов формирования индексных терминов** на 18 языках, 5 системах письма (латиница, кириллица, арабское письмо, бенгальское письмо, деванагари), тестовые коллекции TREC / CLEF / FIRE (Table 2, p. 77). Всего 2 431 запрос и ≈2,87 млн документов **[computed]**. Варианты:
  - словоформы без нормализации (`words`);
  - стемминг Snowball (только 8 языков);
  - статистическая сегментация Morfessor;
  - фонетические преобразования (devowel, soundex);
  - усечение до 4/5 первых символов (trun4/trun5);
  - «наименее частая подстрока» (lfs4/lfs5);
  - символьные n-граммы n = 3…7, внутрисловные n-граммы, скипграммы.
- **Модель поиска одна для всех условий:** языковая модель с линейным сглаживанием, λ = 0.5 (Eq. 1, p. 77). **BM25 нет.** Запросы title+description, без relevance feedback, метрика MAP, парный t-тест (p. 77).
- **Главные числа** (Tables 3–4, pp. 78–79):
  - среднее по 18 языкам: words 0.3072; 4-граммы 0.3778 (+23.0%); 5-граммы 0.3742 (+21.8%); trun5 0.3571 (+16.2%); Morfessor 0.3409 (+11.0%);
  - среднее по 8 языкам со Snowball: words 0.3719; Snowball 0.4146 (+11.5%); 5-граммы 0.4310 (+15.9%); trun5 0.4103 (+10.3%);
  - венгерский: 4-граммы 0.3746 против 0.1976 (+89.6%); маратхи: +60.0%; финский: 5-граммы +49.1%;
  - английский: лучший Snowball (+7.7%), 4-граммы −1.7%;
  - значимые улучшения над words (p < 0.05): 5-граммы в 16/18 языках, 4-граммы и trun5 — в 14/18.
- **Главный вывод авторов:** выигрыш от n-грамм растёт с морфологической сложностью языка. Для английского и романских языков Snowball не хуже или лучше n-грамм, для германских, уральских, славянских и индийских языков n-граммы сильнее. trun5 даёт ≈2/3 выигрыша 4-грамм без затрат на индекс.
  - Table 5 (p. 79): индекс 5-грамм в 6,5 раза больше, запрос в 8,7 раза медленнее **[computed]**.
- **Эксперимент с перестановкой букв** (Sec. 5.2, Fig. 1, p. 81) — пример интервенции на представлении:
  - внутри каждого слова буквы переставляются случайно;
  - MAP для words, по словам авторов, не меняется;
  - 4-граммы падают в среднем на 28% и становятся хуже words почти во всех языках (по нашему считыванию графика ≈ −11% к words в среднем **[computed, approximate]**).
  - Вывод авторов: выигрыш n-грамм обусловлен регулярностью внутри морфологически связанных словоформ.
- **Чего в работе нет:**
  - лемматизации (есть только стемминг и суррогаты);
  - BM25;
  - плотного / нейросетевого поиска;
  - гибрида / fusion;
  - перекрытия результатов, уникально найденных документов, oracle union;
  - анализа по запросам.
  Корреляция со сложностью языка считается **на уровне языков** (Table 6: 13 европейских языков; для меры Juola — 5 языков), а не на уровне запросов.
- **Внутренние несоответствия статьи:**
  1. Сноска 6 (p. 77) относит к языкам Snowball **португальский**, а в Tables 3–4 Snowball есть для **шведского**, а не для португальского. Средние «snow langs» воспроизводятся только со шведским: 0.3719, с португальским было бы 0.3691 **[computed]**.
  2. Коэффициенты Спирмена в Table 6 (0.7771 / 0.9054 / 0.6761) **не воспроизводятся** по напечатанным данным: у нас 0.8088 / 0.9000 / 0.8273 **[computed]**. Значение 0.9054 невозможно для коэффициента Спирмена при 5 языках без совпадающих рангов. Направление связи при этом сохраняется.
  3. В тексте сказано, что при перестановке букв «n = 4 и n = 5» резко ухудшаются, но Fig. 1 показывает только 4-граммы; результаты для 5-грамм не приведены.
- **Для нашего gap:**
  - работа подтверждает давно занятую границу: морфологическое представление лексического канала сильно и по-разному по языкам влияет на эффективность, а языконезависимые n-граммы и усечение — сильные базовые методы;
  - ядро v0.8 (raw/stem/lemma BM25 × фиксированный D → overlap / unique hits → прирост гибрида → признаки запросов) **не затрагивает**.
  - Предложение: gap не менять.
- **Практическая польза для нас (предложения):**
  1. Рассмотреть `BM25_trun5` (усечение до префикса) и `BM25_char-4/5gram` как дополнительные языконезависимые контроли лексического канала рядом с raw/stem/lemma.
  2. Идею интервенции «разрушить внутрисловную регулярность» можно использовать как проверку того, что эффект связан именно с морфологией.
  3. Предобработку (апостроф в o‘/g‘, регистр, пунктуация) надо фиксировать явно: в статье «удаление пунктуации» применяется ко всем условиям, и для узбекского это меняет сами словоформы (наш вывод, §17).

---

## 1. Bibliographic record

- **Authors:** Paul McNamee (Human Language Technology Center of Excellence, Johns Hopkins University), Charles Nicholas (Dept. of Computer Science and Electrical Engineering, UMBC), James Mayfield (HLTCOE, Johns Hopkins University). Source: the paper's header, p. 75.
- **Year:** 2009
- **Venue:** *Proceedings of the 32nd Annual International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR '09)*, Boston, Massachusetts, USA, July 19–23, 2009. Source: first-page footer, p. 75.
- **Pages:** 75–82. Source: printed page numbers of the PDF.
- **Publisher:** ACM. **ISBN:** 978-1-60558-483-6. Source: first-page footer, p. 75.
- **DOI:** `10.1145/1571941.1571957`. This is not printed in the PDF. (bibliographic check: Paul McNamee's publications page, pmcnamee.net, which lists "SIGIR-2009, Boston, MA, pp. 75-82, http://doi.acm.org/10.1145/1571941.1571957"). The ACM Digital Library page returned HTTP 403 and a Crossref lookup was refused by the proxy, so the DOI is **not** confirmed on the publisher's own page. It is, however, confirmed by the OpenAlex record for this DOI (verifier's bibliographic check, api.openalex.org: title, the three authors, *Proceedings of the 32nd international ACM SIGIR conference*, 2009, pp. 75–82). The IR Anthology SIGIR 2009 proceedings listing contains the title with the same three authors (bibliographic check: ir.webis.de), but it shows no pages or DOI.
- **Official URL:** https://doi.org/10.1145/1571941.1571957 (from the bibliographic check above; not opened).
- **Metadata discrepancy:** the systematic-review record says *SIGIR Forum* / JOUR. The PDF and the author's publication list both identify the SIGIR '09 conference proceedings. We propose correcting the record to conference paper (CONF), SIGIR '09.
- **Keywords (paper):** Tokenization, Stemming, Morphology, Character N-grams, CLIR.
- **Source type:** peer-reviewed conference full paper.
- **Reliability:** A.
- **Full text available:** yes (`07_full_text/pdfs/CR000688.pdf`, 8 pages).

## 2. Why this work matters to the PhD

It is one of the widest classical controlled studies of **how the lexical representation of documents and queries changes retrieval effectiveness across languages**. Everything except the indexing terms is held fixed: the same retrieval model, the same smoothing, the same query fields, no feedback. It also offers a clear **intervention experiment** (scrambling letters within words) that tries to isolate *why* one representation helps.

| Axis | Relation |
|---|---|
| Lexical retrieval | Central. 18 lexical representations (words, Snowball stems, Morfessor segments, phonetic codes, truncation, least-frequent substrings, character n-grams, skipgrams) under one language-model retrieval function. **No BM25** |
| Semantic retrieval | Absent |
| Hybrid retrieval | Absent. No fusion of representations and no combined runs |
| Uzbek morphology | Indirect. No Turkic language. The closest agglutinative proxies are Hungarian and Finnish (Uralic), which show the largest n-gram gains |
| Low-resource retrieval | Partial. Bengali, Hindi and Marathi (FIRE '08) are outside "the eight languages supported by the Snowball stemmer" (p. 77), so no Snowball run exists for them, and the paper's motivation is exactly the situation where "rule-based stemmers are not available for every language" (Abstract, p. 75) |
| Current gap | Background / boundary evidence: representation effects are large and language-dependent, and language-independent representations are strong baselines. No lexical–dense complementarity evidence (§16) |

## 3. Research problem

### Simple explanation

Search engines that match whole words miss documents that use a different form of the same word (*swimmer / swimming*). Stemmers fix this, but good stemmers do not exist for every language, and nobody knew which of the many alternatives works best in which language. The authors try 18 ways of cutting text into index terms, in 18 languages, and ask:
- which one wins;
- why character n-grams in particular work so well.

### Formal formulation

- **Task:** monolingual ad hoc document retrieval on newswire test collections (TREC, CLEF, FIRE; Sec. 3.1, p. 77).
- **Independent variable:** the tokenization / term-formation function τ applied to both documents and queries: "we wanted the experiment to reflect only changes in the indexing representation for documents (and queries)" (Sec. 3.2, p. 77).
- **Controlled factors:** retrieval model (Eq. 1), smoothing λ = 0.5, query fields (title + description), no relevance feedback, common preprocessing (case folding, punctuation removal, numbers truncated to ≤ 6 digits; Sec. 2, p. 76).
- **Dependent variable:** MAP per language.
- **Secondary questions (Sec. 5):**
  - Does the n-gram gain correlate with language-level morphological complexity (Table 6)?
  - Does the n-gram advantage survive when within-word morphological regularity is destroyed (Fig. 1)?

## 4. Main idea

### Simple explanation

Represent every word not by itself but by overlapping pieces of 4 or 5 letters. Related word forms (*doctor, doctors*) share most of their pieces, so they match partly even if their endings differ, with no language knowledge needed. Compare this with ordinary words, stemmers and other tricks, language by language.

### Concrete example

The paper's own Table 1 (p. 76) for the phrase *medical doctors*:

| Method | Index terms (as printed) |
|---|---|
| words | medical, doctors |
| snow (Snowball) | medic, doctor |
| morf (Morfessor) | medical, doctor, s |
| trun5 | medic, docto |
| 4-grams | _med, medi, edic, dica, ical, cal_, al_d, l_do, _doc, doct, … |
| win4 (word-internal 4-grams) | _med, medi, edic, …, _doc, doct, octo, ctor, tors, ors_ |

A query containing *doctor* matches a document containing *doctors* under snow, trun5 and n-grams, but not under words.

### Formal method

Retrieval model (Sec. 3.3, Eq. 1, p. 77), used unchanged for every representation:

`P(D|Q) ∝ Π_{t∈Q} [ λ·P(t|D) + (1 − λ)·P(t|C) ]`, with λ = 0.5.

- `P(t|D)` is the relative term frequency in the document.
- `P(t|C)` is "the mean relative document term frequency from documents in the collection".
- The "terms" t are whatever the representation produces: words, stems, n-grams, and so on.

## 5. Architecture / algorithm

1. **Common preprocessing** for all conditions (Sec. 2, p. 76): case folding; punctuation removal; long numbers truncated to at most six digits.
   - Stop-word handling: **NOT_REPORTED**.
   - Diacritic handling: **NOT_REPORTED**.
   - Tokenizer details beyond "tokens delimited by spaces" for `words`: **NOT_REPORTED**.
2. **The 18 representations** (Sec. 2.1–2.4, pp. 76–77; count verified: 9 + 5 + 4 = 18 **[computed]**):
   - `words`: space-delimited tokens. This is the baseline.
   - `snow`: Snowball rule-based stemmer, available for 8 languages.
   - `morf`: Morfessor, an unsupervised segmentation based on the minimum description length principle. "all of a word's segments were included in the inverted file". The word list and training settings for Morfessor are **NOT_REPORTED**.
   - `devowel`: every vowel is replaced by '.', and adjacent vowels are collapsed.
   - `soundex`: a modified Soundex. Whole words are converted to digits, and non-English letters map to '7'. Applied only to Latin-script languages (11 of 18, as the Table 3 cells show).
   - `trun4`, `trun5`: the word truncated to at most its first 4 or 5 characters.
   - `lfs4`, `lfs5`: the least frequent substring of length 4 or 5 in the corpus, "might coincide with the root morpheme".
   - `3-gram` … `7-gram`: word-spanning character n-grams.
   - `win4`, `win5`: word-internal n-grams.
   - `sk41`, `wisk41`: 4-grams plus 5-character skipgrams with one internal letter replaced by '.' (word-spanning and word-internal respectively).
3. **Retrieval:** the language model with λ = 0.5 (Eq. 1). Title + description queries, no relevance feedback. The authors' reason: feedback "might conflate issues of expansion methods and term weighting with the selection of indexing terms" (Sec. 3.2, p. 77).
4. **Evaluation:** MAP over the queries in Table 2; queries without known relevant documents are ignored. Paired t-test, pooling "the available queries from multiple years to increase the sensitivity" (Sec. 3.2, p. 77).
5. **Diagnostic analyses (Sec. 5):**
   - Language-level correlation (Table 6) between the 5-gram gain and three complexity proxies:
     - mean word length by token;
     - Juola's compression ratio;
     - Kettunen et al.'s compression ratio (both ratios are taken from the literature).
   - **Letter-scrambling intervention** (Table 7, Fig. 1): "we randomly shuffle the order of the characters in each word" across the corpus, then re-run words and 4-grams (Sec. 5.2, pp. 80–81).
     - The text describes "a method of altering every word in the lexicon", i.e. a per-type mapping.
     - Whether the same mapping was applied to queries is not stated explicitly. It must have been for the words run to be "unaffected", so this is our inference.

## 6. Data

- **Collections:** 18 TREC / CLEF / FIRE test collections, "generally comprised of newswire articles" (Sec. 3.1, p. 77; Table 2).
- **Languages / scripts:** AR, BG, BN, CS, DE, EN, ES, FA, FI, FR, HI, HU, IT, MR, NL, PT, RU, SV. Scripts: Latin, Cyrillic (BG, RU), Arabic (AR, FA), Bengali (BN), Devanagari (HI, MR). The paper says "five different writing systems" (Abstract).
- **Size (Table 2, p. 77):**
  - queries per language range from 45 (HI) to 367 (EN); 2,431 in total **[computed]**;
  - documents range from 16,715 (RU) to 454,041 (ES); ≈2.87M in total **[computed]**.

| Lang | Queries | Documents | Evaluation |
|---|---:|---:|---|
| AR | 75 | 383,872 | TREC '01–'02 |
| BG | 149 | 85,427 | CLEF '05–'07 |
| BN | 50 | 123,040 | FIRE '08 |
| CS | 50 | 81,735 | CLEF '07 |
| DE | 192 | 294,805 | CLEF '00–'03 |
| EN | 367 | 87,653 | CLEF '00–'07 |
| ES | 156 | 454,041 | CLEF '01–'03 |
| FA | 50 | 166,774 | CLEF '08 |
| FI | 120 | 55,344 | CLEF '02–'04 |
| FR | 333 | 177,450 | CLEF '00–'06 |
| HI | 45 | 95,213 | FIRE '08 |
| HU | 148 | 49,530 | CLEF '05–'07 |
| IT | 181 | 157,558 | CLEF '00–'03 |
| MR | 49 | 99,359 | FIRE '08 |
| NL | 156 | 190,605 | CLEF '01–'03 |
| PT | 146 | 210,734 | CLEF '04–'06 |
| RU | 62 | 16,715 | CLEF '03–'04 |
| SV | 102 | 142,819 | CLEF '02–'03 |

- **Relevance judgments:** the official pooled judgments of the evaluation campaigns. The authors note that "post-hoc use of these benchmarks for comparative evaluation is believed to be reliable" (p. 77). Pool depth and whether any of these runs contributed to the pools: **NOT_REPORTED**.
- **Train/dev/test:** not applicable in the usual sense. Nothing is trained on the queries; Morfessor and lfs are unsupervised and corpus-based. λ = 0.5 is fixed, not tuned.
- **Number of queries evaluated:** the paper states MAP was measured "based on the number of queries shown in Table 2" and that "Queries with no known relevant documents did not affect the calculation" (Sec. 3.2, p. 77). Whether any of the Table 2 queries actually lacked relevant documents (i.e., whether the effective count is lower): **NOT_REPORTED**.

## 7. Baselines

| Baseline | What it is | Why selected | Fair comparison? |
|---|---|---|---|
| `words` | Unnormalized space-delimited tokens | "Plain words are commonly used in web search"; "well justified in languages with little morphological complexity" (p. 76) | Yes. It is the reference for all relative figures. Note that punctuation removal and case folding are applied even here |
| `snow` | Snowball stemmer | Standard rule-based stemming | Yes, but only in 8 languages, so it cannot be compared across all 18 (authors state this, p. 79) |
| `morf` | Unsupervised morph segmentation, all segments indexed | Language-neutral statistical stemming | Partly. Morfessor settings and training word list are NOT_REPORTED, and indexing *all* segments (rather than a stem) is one design choice among several |
| Retrieval model | Language model, λ = 0.5 | Held constant | Fair across representations. A single untuned λ may favour some representations over others (e.g., n-gram indexes have very different term statistics); not tested (§12) |

There is no lemmatization baseline, no BM25, and no other retrieval model.

## 8. Metrics

| Metric | Definition | Simple meaning | Appropriate? |
|---|---|---|---|
| MAP | Mean over queries of average precision (mean of precision at each rank where a relevant document appears, divided by the number of relevant documents) | "On average, how early and how completely are relevant documents ranked?" | Yes, the standard for pooled TREC/CLEF ad hoc collections of that era |
| Relative change vs `words` | (MAP_x − MAP_words) / MAP_words | "How many percent better than plain words?" | Yes, but percentages from low baselines (HU words 0.1976) look larger |
| Spearman ρ (Table 6) | Rank correlation over languages | "Do languages with higher complexity scores also gain more from 5-grams?" | Only as language-level description. n = 13 / 5 / 11 languages; the printed values do not reproduce (§9) |
| Storage / time (Table 5) | Dictionary MB, inverted file MB, mean query seconds on CLEF 2003 English | Cost of each representation | Yes, English only |

Depth of the ranked lists (e.g., 1000) and the evaluation tool: **NOT_REPORTED**.

## 9. Results

### Table 3: all 18 representations, averages (p. 78; page image checked)

Relative change is vs `words` on the same language set, as printed. We recomputed every average and relative figure from the per-language cells; all reproduce to ±0.0001 **[computed]**.

| Representation | Avg MAP, 8 Snowball langs | Δ vs words | Avg MAP, 18 langs | Δ vs words |
|---|---:|---:|---:|---:|
| words | 0.3719 | — | 0.3072 | — |
| snow | 0.4146 | +11.5% | — | — |
| morf | 0.3928 | +5.6% | 0.3409 | +11.0% |
| devowel | 0.3621 | −2.6% | 0.3089 | +0.6% |
| soundex | 0.2900 | −22.0% | — | — |
| lfs4 | 0.3902 | +4.9% | 0.3336 | +8.6% |
| lfs5 | 0.3883 | +4.4% | 0.3260 | +6.1% |
| trun4 | 0.3658 | −1.7% | 0.3260 | +6.1% |
| trun5 | 0.4103 | +10.3% | 0.3571 | +16.2% |
| 3-gram | 0.2959 | −20.4% | 0.2871 | −6.5% |
| **4-gram** | 0.4214 | +13.3% | **0.3778** | **+23.0%** |
| **5-gram** | **0.4310** | **+15.9%** | 0.3742 | +21.8% |
| 6-gram | 0.4013 | +7.9% | 0.3420 | +11.3% |
| 7-gram | 0.3616 | −2.8% | 0.3038 | −1.1% |
| sk41 | 0.4202 | +13.0% | 0.3712 | +20.8% |
| wisk41 | 0.4152 | +11.6% | 0.3604 | +17.3% |
| win4 | 0.4164 | +12.0% | 0.3716 | +21.0% |
| win5 | 0.4242 | +14.1% | 0.3619 | +17.8% |

Notes:
- The "snow langs" set in the table is DE, EN, ES, FI, FR, IT, NL, **SV**. Footnote 6 (p. 77) lists Portuguese instead of Swedish (inconsistency, §19).
- Per-language points worth noting (Table 3):
  - Morfessor beats Snowball only in German (0.3994 vs 0.3695) and Dutch (0.4053 vs 0.4003).
  - trun4 collapses in Arabic (0.1453 vs words 0.2054).
  - devowel helps Hindi strongly (0.3054 vs 0.2429).

### Table 4: best methods vs `words`, with significance (p. 79; 200-dpi image checked)

▲ = significant improvement over words at p < 0.01; △ = p < 0.05 (paired t-test). The "Top method" MAP is printed without its name; we identified the method by matching the value in Table 3 **[inferred]**.

| Lang | words | snow | trun5 | 4-grams | 5-grams | Top method |
|---|---:|---:|---:|---:|---:|---|
| AR | 0.2054 | — | 0.2148 +4.6% | 0.2731▲ +33.0% | 0.2356△ +14.7% | 4-gram +33.0% |
| BG | 0.2164 | — | 0.2959▲ +36.7% | 0.3105▲ +43.5% | 0.2820▲ +30.3% | 4-gram +43.5% |
| BN | 0.2630 | — | 0.3058△ +16.3% | 0.3247△ +23.5% | 0.3173△ +20.6% | 4-gram +23.5% |
| CS | 0.2270 | — | 0.3005▲ +32.4% | 0.3294▲ +45.1% | 0.3223▲ +42.0% | win4 0.3329▲ +46.7% |
| DE | 0.3303 | 0.3695▲ +11.9% | 0.3656▲ +10.7% | 0.4098▲ +24.1% | 0.4201▲ +27.2% | 5-gram +27.2% |
| EN | 0.4060 | 0.4373▲ +7.7% | 0.4216△ +3.8% | 0.3990 −1.7% | 0.4152 +2.3% | snow +7.7% |
| ES | 0.4396 | 0.4846▲ +10.2% | 0.4666△ +6.1% | 0.4597 +4.6% | 0.4609△ +4.8% | snow +10.2% |
| FA | 0.3617 | — | 0.3645 +0.8% | 0.3986△ +10.2% | 0.3821 +5.6% | 4-gram +10.2% |
| FI | 0.3406 | 0.4296▲ +26.1% | 0.4652▲ +36.6% | 0.4989▲ +46.5% | 0.5078▲ +49.1% | 5-gram +49.1% |
| FR | 0.3638 | 0.4019▲ +10.5% | 0.3953▲ +8.7% | 0.3844△ +5.7% | 0.3930▲ +8.0% | snow +10.5% |
| HI | 0.2429 | — | 0.2914▲ +20.0% | 0.3305▲ +36.1% | 0.3271▲ +34.7% | 4-gram +36.1% |
| HU | 0.1976 | — | 0.3082▲ +56.0% | 0.3746▲ +89.6% | 0.3624▲ +83.4% | 4-gram +89.6% |
| IT | 0.3749 | 0.4178▲ +11.4% | 0.3963 +5.7% | 0.3738 −0.3% | 0.3997△ +6.6% | snow +11.4% |
| MR | 0.2572 | — | 0.3477▲ +35.2% | 0.4114▲ +60.0% | 0.3739▲ +45.4% | win4 0.4164▲ +61.8% |
| NL | 0.3813 | 0.4003△ +5.0% | 0.3946 +3.5% | 0.4219▲ +10.6% | 0.4243▲ +11.3% | 5-gram +11.3% |
| PT | 0.3162 | — | 0.3423△ +8.3% | 0.3358 +6.2% | 0.3524▲ +11.4% | 5-gram +11.4% |
| RU | 0.2671 | — | 0.3739▲ +40.0% | 0.3406▲ +27.5% | 0.3330△ +24.7% | trun5 +40.0% |
| SV | 0.3387 | 0.3756▲ +10.9% | 0.3770△ +11.3% | 0.4236▲ +25.1% | 0.4271▲ +26.1% | 5-gram +26.1% |

Checks of the authors' claims (all **[computed]** from the table):

| Claim (location) | Check |
|---|---|
| "Gains with 5-grams are statistically significant in 16/18 cases; 4-grams and trun5 each lead to significant improvements for 14 of the 18 languages" (p. 79) | ✓. Counted from the marks: 5-grams not significant in EN and FA; 4-grams not in EN, ES, IT, PT; trun5 not in AR, FA, IT, NL |
| "5-grams attain higher MAP in all 18 languages compared to plain words" (p. 79) | ✓ (smallest gain: EN +2.3%, not significant) |
| trun5 "improves on words for all 18 languages" (p. 79) | ✓ (smallest gain: FA +0.8%) |
| 4-grams "score lower than words in English and Italian" (p. 79) | ✓ (−1.7%, −0.3%) |
| trun5 "gives two-thirds of the benefit of 4-grams" (p. 79) | 16.2 / 23.0 = 0.70 ✓ |
| Abstract: "In half of the languages examined n-grams outperform unnormalized words by more than 25%" | With the better of 4-/5-grams: 10/18 languages ≥ 25% (AR, BG, CS, DE, FI, HI, HU, MR, RU, SV) ✓. This matches the list in Sec. 5.1 (p. 79) |
| Abstract: "in highly inflective languages relative improvements over 50%" | HU +89.6%, MR +60.0% ✓ |
| "In Hungarian 4- and 5-grams were 80% more effective than words" (p. 79) | +89.6% / +83.4% ✓ |
| Snowball on all 8 languages | Significant in all 8 (▲ in 7, △ in NL) |
| "Snowball is significantly better [than n-grams] in English and Spanish (both), and in French and Italian (4-grams)"; n-grams "statistically better in German, Finnish, and Swedish" (p. 79) | These n-gram-vs-Snowball tests are reported **in the text only**; no p-values or marks. Direction checks: snow > 5-gram in EN, ES, FR, IT; 5-gram > snow in DE, FI, NL, SV |

### Table 5: cost, CLEF 2003 English (p. 79; page image checked)

| | Dict (MB) | Inverted file (MB) | Query (sec) |
|---|---:|---:|---:|
| words | 4.7 | 60.0 | 0.51 |
| snow | 3.5 (−26%) | 50.4 (−16%) | 0.65 (+27%) |
| trun5 | 1.6 (−66%) | 47.0 (−22%) | 0.90 (+77%) |
| 4-grams | 1.8 (−62%) | 232 (+287%) | 4.08 (+700%) |
| 5-grams | 10.9 (+131%) | 391 (+552%) | 4.42 (+767%) |

- The percentages reproduce **[computed]**. The 5-gram dictionary is +131.9%, printed as +131% (truncated rather than rounded; trivial).
- Text: n-grams "can consume 6 times as much storage and queries can take 8 times as long" (p. 79). We get 391/60 = 6.5× and 4.42/0.51 = 8.7× **[computed]** ✓.
- trun5 queries are slower than words (+77%) despite the smaller index. The paper does not comment on this.

### Table 6: 5-gram gain vs language complexity (p. 80; 200-dpi image checked)

| Lang | Mean word length | Juola ratio | Kettunen ratio | 5-gram gain |
|---|---:|---:|---:|---:|
| HU | 5.99 | — | 1.1421 | 83.40% |
| FI | 7.23 | 1.1253 | 1.1637 | 49.09% |
| CS | 5.38 | — | 1.0867 | 41.98% |
| BG | 5.02 | — | — | 30.31% |
| DE | 5.98 | — | 1.1660 | 27.19% |
| SV | 5.26 | — | 1.1252 | 26.10% |
| RU | 5.93 | 1.0456 | — | 24.67% |
| PT | 4.89 | — | 1.0676 | 11.45% |
| NL | 5.17 | 0.9949 | 1.1189 | 11.28% |
| FR | 4.79 | 1.0117 | 1.0622 | 8.03% |
| IT | 5.08 | — | 1.0518 | 6.62% |
| ES | 4.89 | — | 1.0624 | 4.85% |
| EN | 4.68 | 0.9717 | 1.0529 | 2.27% |
| **printed ρ** | **0.7771** | **0.9054** | **0.6761** | |

- The table covers **13** European languages. The caption says "European languages"; AR, BN, FA, HI and MR are excluded, and the paper does not say why.
- The 5-gram gains equal Table 4's 5-gram column to two decimals **[computed]** ✓.
- **Our recomputation of Spearman ρ from the printed data** (scipy, average ranks for ties) **[computed]**:
  - word length: n = 13, ρ = 0.8088 (printed 0.7771);
  - Juola: n = 5, ρ = 0.9000 (printed 0.9054);
  - Kettunen: n = 11, ρ = 0.8273 (printed 0.6761).
  - With 5 untied pairs, Spearman ρ can only take values in steps of 0.1, so 0.9054 cannot be a Spearman coefficient over these five rows.
  - The printed Kettunen value is close to the *Pearson* r (0.6746), but the word-length and Juola values match neither Pearson (0.670, 0.985) nor Kendall τ.
  - The paper may have used unrounded data or a different language set. This cannot be decided from the paper. **All variants give a clearly positive association**, so the qualitative claim ("moderate to large correlations", p. 80) holds.

### Figure 1 / Sec. 5.2: letter-scrambling intervention (p. 81; 220-dpi crop checked)

- The figure plots, for each language, the relative MAP change of 4-grams vs words:
  - triangles = ordinary text; they match Table 4's 4-gram column;
  - circles = text with the letters of every word permuted.
- No numbers are printed for the circles. Our pixel read-off **[computed, approximate, ±1 pt]**:
  - HI ≈ 0%, FA ≈ −1%;
  - HU ≈ −6%, CS ≈ −7%, FI ≈ −8%, AR ≈ −9%;
  - IT ≈ −10%, EN ≈ −10%, FR ≈ −11%;
  - ES ≈ −13%, NL ≈ −14%, DE ≈ −14%, SV ≈ −14%, PT ≈ −15%, RU ≈ −16%, BN ≈ −17%;
  - MR ≈ −19%, BG ≈ −21%;
  - mean ≈ −11% relative to words.
- Authors' statements (p. 81):
  - "No change occurs when using space-separated words as indexing terms". Footnote 8: "for words MAP was unaffected by the letter scrambling". No number is given.
  - "N-grams of lengths n = 4 and n = 5 perform markedly worse, suffering a 28% decline in mean average precision, averaged over all languages. Performance falls appreciably below that of word-based indexing."
- **Check of the 28%:** the mean over languages of (MAP_4gram,permuted / MAP_4gram,ordinary − 1) from our read-off is −28.2% **[computed, approximate]**. That is consistent with the printed 28%, so the base of the "28% decline" is the *ordinary 4-gram* run, not words.
- **5-gram permuted results are not shown** anywhere, although the text claims them.
- Authors' conclusion: "These results give strong evidence that it is the ability of overlapping character n-grams to capture regularity across morphologically related words forms that gives them their primary advantage" (p. 81).

### Table 7: illustration of scrambling (p. 80; page image checked)

CLEF 2000 English examples:
- *ate* (df 613) and *tea* (df 741) both become *aet* (df 1316), an artificial conflation;
- *team / meat* stay separate;
- *lull* is unchanged;
- *golfer / golfed / golfing / golfball* lose all resemblance.

## 10. Statistical evidence

- **Significance test:** paired t-test (citing Cormack & Lynam, 2007) on per-query AP, with queries pooled across campaign years (p. 77). Two levels, p < 0.01 (▲) and p < 0.05 (△). Tests are only against `words` (Table 4).
  - n-gram vs Snowball tests are mentioned in the text only (p. 79).
  - Raw p-values, t statistics and effect-size CIs: **NOT_REPORTED**.
- **Multiple-comparison correction:** none. Table 4 alone contains 62 tests against words (8 Snowball + 3 × 18 for trun5 / 4-grams / 5-grams) **[computed]**.
- **Confidence intervals:** NOT_REPORTED.
- **Runs / seeds:** deterministic pipeline, one run per condition. The letter-scrambling experiment uses **one random permutation**; its variance across permutations is NOT_REPORTED.
- **Ablation:**
  - the word-internal vs word-spanning comparison (4-gram vs win4; 5-gram vs win5) is a partial ablation of cross-word phrasal information. The authors conclude that phrasal cues "would not explain what is occurring" (p. 80);
  - the letter-scrambling experiment is an intervention ablation of within-word character order.
- **Per-query analysis:** **none.** There are no per-query win/loss counts, no query-feature analysis, and no overlap or unique-relevant-document analysis between representations. The only "explanatory" analysis is **per language** (Table 6, n = 13 or fewer).
- **Sensitivity to the retrieval model / λ:** not tested. λ = 0.5 is fixed for all conditions.

## 11. Strengths

- **Very wide and controlled:** 18 representations × 18 languages × 5 scripts under one fixed retrieval function, no feedback, no tuning. The representation is the only thing that changes.
- **Includes lower-resourced languages** (Bengali, Hindi, Marathi) outside "the eight languages supported by the Snowball stemmer" (p. 77), i.e. the realistic situation for many languages.
- **Significance marks per language and method**, with query sets pooled across years for power.
- **Reports cost** (Table 5), not only effectiveness. This is rare and practical.
- **An explicit intervention experiment** (scrambling) that tests a mechanism instead of only correlating. It is a methodological template for "change one factor, observe the effect".
- Clear, reproducible descriptions of the language-independent methods (Table 1 examples).

## 12. Limitations

### Stated by the authors

- n-gram indexing costs up to ~6× storage and ~8× query time (Table 5, p. 79).
- Snowball is available for only 8 of 18 languages, so "direct comparisons to Snowball cannot be made" over all languages (p. 79).
- Soundex was applied only to Latin-script languages (a design choice stated on p. 76, not argued as a limitation).
- Complexity measures "are not without controversy among linguists" (p. 79).
- The scrambling experiment "will not distinguish between morphological processes such as inflection and compounding" (p. 80).
- Scrambling can create artificial conflations (anagrams, e.g. *ate/tea → aet*) and short or repetitive words "will bear a strong resemblance to their original forms", occasionally remaining unchanged (e.g., *lull*); "No constraint was imposed to ensure that shuffled forms differed from their original strings" (Table 7, pp. 80–81).
- The effect of spelling normalization "is somewhat difficult to quantify" (p. 80).

### Inferred from the experimental design

1. **One retrieval model, one untuned λ.** The ranking of representations may depend on the model: BM25 or other smoothing, and n-gram-specific λ, were not tested. The conclusion "n-grams are best" is conditional on this language model.
2. **No lemmatization condition and no BM25.** The raw/stem/**lemma** axis central to our design is represented only by raw and stem (8 languages) plus surrogates.
3. **Pooling bias is possible.** The qrels come from campaign pools. n-gram runs may retrieve relevant documents that were never judged (or the reverse). Pool depth and pool contributors are not reported. This matters for any conclusion about *which* documents a representation finds.
4. **Language-level correlation, not query-level.** Table 6 has n = 13 (word length), 5 (Juola) and 11 (Kettunen) languages, the complexity values come from other corpora, and the printed ρ values do not reproduce (§9). Collections also differ in size, number of queries, years and genre, so language complexity is confounded with collection properties.
5. **The scrambling intervention is not specific to morphology.** Permuting letters also destroys:
   - spelling-variant robustness;
   - transliteration variants;
   - cognate or compound-part overlap;
   - any sub-word regularity at all.
   What the experiment shows is that n-gram gains need **within-word character order**. That this order matters *because of morphology* is an interpretation. The abstract's "causal relationship between the morphological complexity of a language and n-gram effectiveness" (p. 75) is stronger than the design supports: the intervention is within each language, and language complexity itself was never manipulated.
6. **A single random permutation, and the 5-gram permuted results are not shown**, despite the claim in the text.
7. **"Punctuation removal" for all conditions** interacts with orthographies that use apostrophe-like letters. This does not affect the paper's languages much, but it matters for Uzbek (§17).
8. **No multiple-comparison correction;** many tests.
9. **Queries per language vary 45–367** (Table 2). Small-query languages (HI, MR, BN, FA, CS) have less power, which can explain some non-significant cells (e.g., FA).

## 13. What the work proves

Within one language-model retrieval function (λ = 0.5), on 18 newswire test collections:

- **The lexical representation matters a lot, and its effect is strongly language-dependent.** Averaged over all 18 languages, 4-grams reach MAP 0.3778 vs 0.3072 for words (+23.0%, Table 3). In individual languages the best representation gives from +7.7% (EN, Snowball) to +89.6% (HU, 4-grams) (Table 4).
- **Character 4-/5-grams are a strong language-independent default.**
  - 5-grams improve on words in all 18 languages, significantly in 16 (Table 4).
  - 4-grams improve significantly in 14 of 18.
- **In English and Romance languages, rule-based stemming is at least as good as n-grams.** Snowball is the top method in EN, ES, FR and IT. Per the text (p. 79), it is significantly better than both 4- and 5-grams in EN and ES, and than 4-grams in FR and IT (no p-values are shown). In German, Finnish and Swedish, n-grams are significantly better than Snowball per the text.
- **Simple prefix truncation (trun5) captures most of the n-gram benefit at no index cost.** It gives +16.2% on average and improves every language (significant in 14/18), and it is the top method in Russian (+40.0%) (Tables 3–4).
- **Destroying within-word character order removes the n-gram advantage.** 4-grams on scrambled text fall about 28% below ordinary 4-grams, and below words in essentially every language (Fig. 1). Words are reported unaffected. Longer (6-, 7-) and shorter (3-) n-grams are weaker than 4/5 (Table 3).
- **At the language level, larger n-gram gains go with longer words and higher compression-based complexity** (positive rank association in Table 6, even though the printed coefficients do not reproduce exactly).

## 14. What the work does NOT prove

- **That n-grams are the best representation in general.** Only one retrieval model with a fixed λ was tested: no BM25, no DFR, no tuned smoothing.
- **Anything about lemmatization.** No lemma condition exists. The paper cannot rank raw < stem < lemma or similar.
- **That morphological complexity *causes* n-gram gains across languages.** The cross-language evidence is correlational (n ≤ 13, confounded with collection differences). The scrambling experiment shows dependence on within-word character order, not on morphology specifically, and not across languages.
- **Which queries benefit from which representation.** There is no per-query analysis, no query features, and no win/loss counts.
- **Anything about complementarity:** whether n-gram and word (or stem) runs retrieve different relevant documents, how much they overlap, or whether fusing them helps. There is no fusion, no oracle union and no unique-hit analysis.
- **Anything about semantic/dense retrieval or hybrids.** None were evaluated. (A 2009 paper predates modern dense retrieval; this is noted as context, not criticism.)
- **Transfer to Turkic/Uzbek.** No Turkic language is included. Hungarian and Finnish are the nearest agglutinative analogues, but orthography, collection genre and morphology differ.

## 15. Relationship to current Uzbek evidence

- **No Uzbek or Turkic data.** The pattern "the more agglutinative, the larger the gain from sub-word or truncation representations" is consistent with the Turkish evidence already in the index:
  - MORPH-001 (Can et al., 2008): morphology materially affects lexical retrieval in Turkish;
  - MORPH-002 (Haddad & Bechikh Ali, 2014): simple 4/5-prefix truncation remains highly competitive with Zemberek-based BM25.
  This paper adds cross-linguistic breadth: trun5 improves all 18 languages.
- **Same cluster of classical European lexical-representation studies** already carded:
  - `CR000338` Hollink et al. 2004 (cited here as [9]; the authors say the results "are consistent with those in this study", p. 81);
  - `CR000523` Fautsch & Savoy 2009;
  - `CR000491` Airio 2006;
  - `CR000452` Kettunen et al. 2005 (Finnish stem vs lemma);
  - `CR000490` Ahlgren & Kekäläinen (Swedish indexing strategies; the paper cites an Ahlgren & Kekäläinen IPM 2007 article as [1]. Whether it is the same work as the carded record should be checked).
  Unlike most of these, this paper lacks lemmatization but covers non-European and low-resource languages.
- **National Uzbek work** (Bakaev, Xusainova, Elov; `MASTER_INDEX` A/C) builds stemmers and lemmatizers, but none reports a qrels-based comparison against language-independent baselines such as n-grams or truncation. This paper argues such baselines "should be measured against" (p. 82). That is an argument for including them in the Uzbek design (§17), not evidence about Uzbek.
- Morpho Challenge (cited [16]) and Turunen's PhD (`CR002216`, morph-based speech retrieval) are the related unsupervised-segmentation line; `morf` here is the same family (Morfessor).

## 16. Relationship to CURRENT_GAP

**Classification:** *supports (background)* + *no material effect on the residual core*.

- **Supports / occupies the background boundary:**
  - Controlled comparisons of lexical representation variants across many morphologically diverse languages, including lower-resourced ones without stemmers, are long established (2009, SIGIR). The effect of a representation is language-dependent and can be very large.
  - This strengthens the v0.8 non-claims "raw/stem/lemma [lexical representations] have not been compared in low-resource IR" and "morphology has not been applied to search", which were already rejected.
  - It also shows that the representation space is **wider than raw/stem/lemma**: character n-grams and prefix truncation are strong, language-independent competitors.
- **Methodological support:** the paper exemplifies the design principle v0.8 relies on. It changes only the lexical representation and holds everything else fixed, and it uses an intervention (scrambling) to test a mechanism.
- **No material effect on the residual core.** None of the v0.8 elements is present:
  - morphological representation → change in complementarity with a **fixed** dense retriever D;
  - unique relevant hits / overlap / oracle union;
  - incremental hybrid gain;
  - link to query features at the **query** level.
  Its "explanatory" analysis is at the language level. The paper does not even compare the relevant-document *sets* of different lexical representations.

**Proposal:** keep v0.8 refined unchanged. Optionally list this paper in the evidence boundary as the classical multi-language reference for "lexical-representation effects are large, language-dependent, and language-independent n-gram/truncation baselines are strong". A possible design refinement (not a gap change) is in §17. This is a proposal only; `CURRENT_GAP.md` has not been edited.

## 17. Implications for our research design

- **Baselines / lexical variants (proposal):**
  - Keep `BM25_raw / BM25_stem / BM25_lemma` as the primary factor.
  - Consider **`BM25_trun5`** (prefix truncation; the optional `BM25_simple-normalization` control in v0.8 could take this form) and **`BM25_char-4gram` or `-5gram`** as secondary, language-independent controls.
  - Rationale from this paper: trun5 and n-grams gave the largest gains in agglutinative languages, need no Uzbek morphological tools, and "n-gram indexing is a strong default method that other approaches should be measured against" (p. 82).
  - If they are added, they must be fused with the same fixed D and analysed with the same overlap / unique-hit measures. Otherwise the dissertation cannot say whether lemma-specific complementarity differs from what cheap sub-word matching gives.
  - Cost note: n-gram inverted files are ≈3.9× (4-grams) to ≈6.5× (5-grams) larger and queries ≈8.0–8.7× slower **[computed]** (Table 5; English only).
- **Retrieval model:** the paper's ranking of representations holds under a language model with λ = 0.5. It must not be assumed to carry over to BM25. Our BM25 k1/b must be fixed or validated **per representation on dev**, because n-gram and stem vocabularies change term statistics.
- **Preprocessing (our inference, not from the paper):**
  - The paper applies "punctuation removal" and case folding to every condition. For Uzbek Latin script, removing apostrophe-like characters turns `o‘`/`g‘` and the tutuq belgisi (ʼ) into different strings: `O‘zbekiston` → `ozbekiston`, while `sa'y` and `say` merge.
  - It also shifts the 5-character window of trun5 and every n-gram.
  - Apostrophe normalization must therefore be fixed identically for all lexical variants and reported (same point as in the exemplar card's §17).
- **Mechanism test (optional experiment idea):** an intervention like the letter scrambling could serve as a sanity check. Applying a consistent per-type character permutation to queries and documents leaves `BM25_raw` unchanged but destroys what stemming, n-grams or truncation can exploit. If the complementarity change we observe for stem/lemma vanishes under a matched "destroyed-morphology" control, that supports a morphological explanation. This must be designed carefully: D cannot be applied to scrambled text, so the check applies to the lexical side only.
- **Query taxonomy:** mean word length and compression ratios work as *language*-level complexity proxies here. At the query level we can compute analogous features: mean query-word length, number of suffixes per query word, OOV rate, share of words changed by the stemmer or lemmatizer. The paper gives no evidence that such features predict per-query effects; they remain candidates.
- **Metrics / statistics:**
  - Report MAP (comparability with this classical literature) together with nDCG / Recall@k.
  - Use paired tests per query with a multiple-comparison correction, since this paper runs dozens of uncorrected tests.
  - Report the number of evaluated queries.
- **Qrels:** avoid relying on pools built from a single representation. Pool from raw, stem, lemma, the n-gram controls (if used) and D, so that unique hits of any representation have a chance of being judged (compare the pooling concern in §12).

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| Indexing term / tokenization | The units a search engine stores and matches: words, stems, pieces of words | Function τ mapping text to a bag of terms for the inverted index |
| Stemming (Snowball) | Cutting word endings by hand-written rules so related forms become one stem | Rule-based suffix stripping; Snowball = Porter's stemmer-rule compiler |
| Lemmatization | Mapping each word to its dictionary form using language knowledge | Morphological analysis → lemma. **Not tested in this paper** |
| Morfessor | Learns word pieces (morphs) from a word list without supervision | MDL-based unsupervised morphological segmentation |
| Character n-gram | Overlapping letter sequences of fixed length n | Sliding window of n characters, here spanning word boundaries (with `_` for the space) |
| Word-internal n-gram | n-grams that do not cross word boundaries | Window restricted to within a word (plus boundary markers) |
| Skipgram | An n-gram with a letter replaced by a wildcard | Here: 5-character strings with one internal letter replaced by '.' |
| Truncation (trun5) | Keep only the first 5 letters of every word | Fixed-length prefix stemming |
| Least frequent substring (lfs) | Keep the rarest 4/5-letter piece of a word, hoping it is the root | argmin corpus frequency over the word's length-k substrings |
| Soundex / devowel | Encodings that ignore some spelling detail (vowels, similar consonants) | Phonetic or orthographic normalization |
| Language-model retrieval (Eq. 1) | Rank documents by how likely they are to "generate" the query, mixing document and collection statistics | Query likelihood with Jelinek–Mercer-style linear interpolation, λ = 0.5 |
| MAP | Average over queries of how early and how completely relevant documents are ranked | Mean of per-query average precision |
| Paired t-test | Checks whether per-query score differences between two runs are reliably non-zero | t-test on per-query AP differences |
| Spearman ρ | Do two rankings of languages agree? | Rank correlation coefficient |
| Letter-scrambling intervention | Shuffle the letters inside each word everywhere, so related word forms no longer look alike | Consistent random permutation per word type; removes within-word character order |
| Pooling | Only documents retrieved by the systems in an evaluation campaign are judged | Qrels built from the union of top-k results of submitted runs |
| Complementarity (project term) | Each channel finds relevant documents the other misses | Unique relevant hits, overlap, oracle-union gain. **Not measured here** |

## 19. Open questions / verification needed

1. **Snowball language set.** Footnote 6 (p. 77) lists Portuguese; Tables 3–4 show Swedish. The averages reproduce only with Swedish (0.3719 vs 0.3691 with Portuguese **[computed]**), so the footnote is most likely a typo. Still, cite "8 Snowball languages = DE, EN, ES, FI, FR, IT, NL, SV" from the tables.
2. **Table 6 correlation values** do not reproduce as Spearman from the printed data (0.8088 / 0.9000 / 0.8273 vs printed 0.7771 / 0.9054 / 0.6761 **[computed]**). Do not quote the printed ρ values as exact; say "positive, moderate-to-strong rank association".
3. **Permuted 5-grams:** claimed in the text (p. 81), not shown. The printed 28% decline is consistent with 4-grams only (base = ordinary 4-grams) **[computed, approximate]**.
4. **The abstract's "causal relationship … was demonstrated"** should not be repeated in Chapter I without the qualification in §12, item 5.
5. **DOI 10.1145/1571941.1571957** comes from the first author's publication list and is confirmed by the OpenAlex record (verifier's bibliographic check: title, three authors, SIGIR '09 proceedings, pp. 75–82). The ACM DL page itself was not reachable (403); a final check there is optional. Correct the systematic-review venue from *SIGIR Forum* / JOUR to the SIGIR '09 proceedings.
6. NOT_REPORTED details: stop-words, diacritics, Morfessor training data and parameters, pool depth, run depth, and whether any Table 2 queries lacked relevant documents (MAP is stated to be based on the Table 2 query counts, p. 77).
7. Check whether `CR000490` (Ahlgren & Kekäläinen) is the same work as reference [1] (IPM 43(1), 2007).
8. **Whether n-gram vs stem vs word runs retrieve different relevant documents** (complementarity at the representation level) cannot be answered from this paper. It would need the original runs.

## 20. Decision after deep dive

- **Keep current gap?** Yes. v0.8 refined remains valid (§16).
- **Modify gap?** No change proposed. Optionally add this paper to the evidence-boundary list as the classical multi-language reference for large, language-dependent lexical-representation effects and strong n-gram/truncation baselines (researcher's decision).
- **Add decision?** Proposed for `decisions/DECISIONS.md` (researcher's decision):
  - "Language-independent lexical controls (prefix truncation trun5 and/or character 4/5-grams under BM25) are considered as secondary lexical variants, fused with the same fixed D and analysed with the same overlap/unique-hit measures";
  - "Apostrophe/punctuation handling is fixed identically across all lexical variants and reported".
- **Add experiment?** Optional:
  1. `BM25_trun5` and `BM25_char-4gram` controls in the pilot;
  2. an optional lexical-side "scrambled-morphology" sanity check (§17).
  Both are proposals, to be decided after the pilot benchmark exists.
- **Add citation to Chapter I?** Yes:
  - §1.1 (lexical representation / indexing units: stemming vs n-grams vs truncation; language-dependence; cost);
  - Выводы по главе I (as evidence that morphology-related representation choices were long studied at the aggregate level, but not in terms of complementarity with semantic retrieval).
  Avoid quoting the printed ρ values or the "causal" wording without qualification.
- **Proposed `MASTER_INDEX.md` row** (to add after approval):

| MORPH-035 | McNamee, Nicholas, Mayfield — *Addressing Morphological Variation in Alphabetic Languages* (SIGIR '09, pp. 75–82) — [deep dive](deep-dives/2009_McNamee_Nicholas_Mayfield_Morphological_Variation_Alphabetic_Languages.md) | 2009 | A | HIGH | 18 lexical representations (words, Snowball [8 langs], Morfessor, devowel/soundex, trun4/5, lfs4/5, char 3–7-grams, word-internal n-grams, skipgrams) × 18 TREC/CLEF/FIRE languages in 5 scripts, one LM retrieval model (λ=0.5), T+D queries, MAP, paired t-test. 4-grams +23.0% / 5-grams +21.8% / trun5 +16.2% over words on average (Table 3); gains largest in HU (+89.6%), MR, FI, CS, BG; Snowball best in EN/ES/FR/IT. Letter-scrambling intervention removes the n-gram advantage (−28% vs ordinary 4-grams, Fig. 1). Language-level complexity correlation only (Table 6; printed ρ not reproducible; footnote 6 vs tables Snowball-language mismatch). No lemma, no BM25, no dense, no fusion, no per-query/overlap/unique-hit analysis. |
