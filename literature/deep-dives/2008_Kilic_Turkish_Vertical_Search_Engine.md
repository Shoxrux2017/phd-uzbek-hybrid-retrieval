# Kılıç (2008): Türkçe dokümanlar için özelleştirilebilir web tabanlı dikey arama motoru (Web-based customizable vertical search engine for Turkish documents)

**Targeted deep-dive status:** COMPLETED (AI-assisted, pending researcher review)
**Completed:** 2026-09-28
**Literature ID:** `MORPH-021` (assigned 2026-09-28, approved by researcher)
**Systematic-review record:** `CR002145`. Full-text triage: INCLUDE, reading priority HIGH, reading tier 1 ("прямо по теме пробела"), `carries_complementarity_evidence = NO`. Triage evidence location: Sec. 4.2, Tables 4.3–4.4.
**Provenance:** AI-assisted deep dive (Claude). The thesis is in Turkish (84 PDF pages; the abstract states "2008, 81 sayfa"). What was read: title and approval pages, Turkish and English abstracts, table of contents, Ch. 1 (skimmed), Sec. 2.2–2.3 (language identification and stemming background), Sec. 3.1–3.3 and 3.6–3.7 (architecture, language identification, Turkish analysis/stemmer, indexer, query processor), all of Ch. 4 (experiments), Ch. 5 (conclusions) and the reference list. Sec. 2.1 and 3.4–3.5 (Heritrix crawler configuration, web UI) were only skimmed because they contain no retrieval evaluation. **Pages checked visually** (110 dpi page images; PDF page = printed page + 9): PDF p. 2 (jury approval page), PDF pp. 49–52 (printed pp. 40–43: stemmer description, Tables 3.2–3.3, worked example), PDF pp. 73–79 (printed pp. 64–70: Tables 4.1–4.9, Fig. 4.1). Every number of Tables 4.1–4.8 reported below was compared with the page image. Numbers computed by us are marked **[computed]** and were computed in Python.
**Source rule:** **the thesis is the primary and only authoritative source** for what the author did and found. The web was used only to try to verify the bibliographic record; this failed (see §1). Statements about the Milliyet collection that come from other project cards are marked **[CR000651 card]** or **[MORPH-001 card]** and are not used as evidence about this thesis.
**Verification:** independent AI verifier pass 2026-09-28; 10 findings addressed.
**Reliability:** **B.** It is a Master's thesis (Yüksek Lisans Tezi) with a jury approval page giving acceptance on 13.08.2008 at Anadolu University. It is not a peer-reviewed publication and not a doctoral thesis. The Institute board approval fields on the same page are blank. The record could not be verified externally. The evidence itself is narrow: one unreplicated comparison of two Lucene analyzers, with no significance test and several unreported settings.

---

## Кратко для исследователя (RU)

- **Что это.** Магистерская диссертация (Anadolu Üniversitesi, 2008, научный руководитель Yard. Doç. Dr. Özgür Yılmazel). Основная часть — инженерная: вертикальная поисковая система на Heritrix + Lucene с веб-интерфейсом. Эксперимент по информационному поиску занимает около двух страниц (Sec. 4.2, pp. 65–67).
- **Морфология.** Автор разработал собственный словарный стеммер `TurkishPrefixMatchFilter` (Sec. 3.3.1, pp. 40–44). Это не усечение до фиксированной длины префикса. Стеммер ищет **самый длинный префикс слова, который есть в словаре корней**; слова без совпадения индексируются как есть. Перед этим он:
  - отрезает всё после апострофа (турецкое «Atatürk'ün» → «Atatürk»);
  - не трогает слова из списков топонимов и личных имён;
  - затем переводит «искусственные» корни с озвончением и выпадением гласной в исходную форму («boyn» → «boyun»).
  Размер и источник словаря корней и списков имён **не указаны**.
- **Эксперимент.** Коллекция Milliyet (408 314 новостей, 72 темы, неполная разметка), метрики bpref и P@5…P@1000. Сравниваются два анализатора Lucene: `StandardAnalyzer` и `TurkishPrefixMatchAnalyzer`, запросы title+description (T+D) и title-only (T).
- **Главные числа** (Tables 4.3–4.4, p. 67):
  - bpref T+D: 0.3947 → 0.5092 (+29.0% **[computed]**);
  - bpref T: 0.3506 → 0.4538 (+29.4% **[computed]**);
  - P@10 T+D: 0.6042 → 0.6667;
  - сокращение словаря индекса на 77.9% (875 202 → 193 262 терминов, p. 65).
- **Интересная деталь о длине запроса** **[computed]**: для коротких запросов (T) P@5 почти не меняется (0.5583 → 0.5639, это всего 2 дополнительных релевантных документа на все 72 запроса), а на глубоких отсечках прирост больше, чем для T+D (P@100 +27.1% против +17.2%). По средним значениям эффект анализатора (не только стемминга, см. ниже) выглядит зависящим от длины запроса и глубины отсечки. Это только агрегированные числа, без теста значимости.
- **Сравнение не изолирует стемминг.** Анализатор отличается от базового сразу в нескольких местах:
  - турецкий перевод в нижний регистр (`TurkishLowerCaseFilter`);
  - турецкий список стоп-слов;
  - сам стеммер.
  Конфигурация `StandardAnalyzer` не описана.
  Кроме того, 77.9% посчитаны для **другой** цепочки (LetterTokenizer + нижний регистр + фильтр, без стоп-слов), а не для оцененного анализатора.
- **Чего нет:**
  - BM25 (функция ранжирования Lucene вообще не названа);
  - плотного поиска, гибрида/fusion;
  - перекрытия результатов, уникально найденных релевантных документов, oracle union;
  - анализа по отдельным запросам;
  - тестов значимости, других вариантов морфологии (лемма, фиксированный префикс).
- **Внутренние несоответствия:**
  - цепочка обработки в тесте словаря ≠ оцененный анализатор;
  - в пошаговом примере «delegelerin» шаг 1 помечен «нет совпадения», но записан номер буквы 3;
  - в Table 4.9 `tercuman.com.tr` указан дважды (19 строк = 18 сайтов);
  - на Fig. 4.1 ось «2028» вместо 2048;
  - «dokümanlar» (титул) vs «dökümanlar» (страница утверждения).
- **Для нашего gap:** работа только подкрепляет уже занятую границу («морфологическая нормализация сильно помогает лексическому поиску в тюркском языке»). На ядро v0.8 (raw/stem/lemma BM25 × фиксированный D → overlap/unique hits → прирост гибрида → признаки запроса) **не влияет**. Предложение: gap не менять.
- **Практическая польза для узбекского:**
  1. Турецкое правило «отрезать всё после апострофа» для узбекского **опасно**: апостроф там входит в буквы o‘/g‘ и в тутуқ белгиси. Нормализация апострофов должна идти до любого стемминга.
  2. Списки защиты имён собственных и топонимов от стемминга — полезный приём; именованные сущности — признак запроса.
  3. Базовый и морфологические варианты должны различаться **только** морфологией: одинаковые токенизатор, регистр, стоп-слова, модель ранжирования.
  4. Сокращение словаря сообщать для той же конфигурации, что и оценивается.

---

## 1. Bibliographic record

- **Author:** Aydın Kılıç
- **Title (title page):** *Türkçe Dokümanlar İçin Özelleştirilebilir Web Tabanlı Dikey Arama Motoru*. On the jury approval page it is spelled *"Türkçe dökümanlar için özelleştirilebilir web tabanlı dikey arama motoru"*.
- **English title (thesis abstract):** *Web Based Customizable Vertical Search Engine for Turkish Documents*
- **Degree:** Master of Science (Yüksek Lisans Tezi)
- **University / unit:** Anadolu Üniversitesi, Fen Bilimleri Enstitüsü, Bilgisayar Mühendisliği Anabilim Dalı, Bilişim Bilim Dalı
- **Supervisor:** Yard. Doç. Dr. Özgür Yılmazel
- **Jury:** Yard. Doç. Dr. Özgür Yılmazel (supervisor), Prof. Dr. Can Ayday, Yard. Doç. Dr. Cüneyt Akınlar. The approval page states: "Yüksek Lisans Tezi 13.08.2008 tarihinde ... kabul edilmiştir" ("the Master's thesis was accepted on 13.08.2008"). The Institute board decision date and number are left blank in this copy (PDF p. 2).
- **Year:** 2008 (title page: "Eylül, 2008"; defense 13.08.2008)
- **Length:** abstracts say "2008, 81 sayfa / 81 page". The PDF has 84 pages, including front matter and a ProQuest notice page. The last printed page number is 74.
- **Distribution:** ProQuest, "ProQuest Number: 28638778", "Distributed by ProQuest LLC (2021)" (last PDF page).
- **DOI:** none known.
- **Keywords (thesis):** Dikey Arama Motorları, Türkçe Bilgi Erişimi, Heritrix, Lucene, Dil Tanıma
- **Bibliographic check:** two web searches (title + author + university; author + supervisor) returned no matching record: YÖK Ulusal Tez Merkezi was not reached directly, and no ProQuest landing page was found. The record above therefore rests only on the PDF itself. The verifier pass (2026-09-28) ran two further searches (Turkish title + author + university; exact English title) and tried the Anadolu University e-archive (not reachable); none found a record. **Not externally verified.**
- **Source type:** Master's thesis
- **Reliability:** B (see header)
- **Full text available:** yes (`07_full_text/pdfs/CR002145.pdf`, 84 pages, text-based PDF)

## 2. Why this work matters to the PhD

It is a small but **Turkic**, **full-scale test collection** experiment comparing an unstemmed with a stemmed Lucene index, on the same Milliyet collection used in MORPH-001 and MORPH-002. It adds a third, independently built stemmer type to that evidence: dictionary longest-prefix match plus proper-noun protection. It also reports title-only vs title+description queries.

| Axis | Relation |
|---|---|
| Lexical retrieval | Direct but narrow: Lucene index with two analyzers; the ranking function is **not named** (NOT_REPORTED); no BM25 is mentioned anywhere in the thesis |
| Semantic retrieval | Absent |
| Hybrid retrieval | Absent. No fusion; the word "melez" ("hybrid") refers only to the stemmer type (Sec. 2.3.5, 3.3.1) |
| Uzbek morphology | Indirect. Turkish is the closest well-resourced Turkic (agglutinative, suffixing) language; the apostrophe handling, however, is Turkish-specific and conflicts with Uzbek orthography (§17) |
| Low-resource retrieval | Weak. Turkish in 2008 was a medium-resource setting; the stemmer is a hand-built dictionary resource |
| Current gap | Supports the already occupied boundary "morphological normalization improves lexical retrieval in Turkic languages". No material effect on the v0.8 core (§16) |

## 3. Research problem

### Simple explanation

General web search engines treat all languages alike and do not serve narrow topics well. The author builds a "vertical" (topic-focused) search engine for Turkish that:

- crawls user-chosen websites;
- recognizes whether a page is Turkish;
- cuts Turkish words down to a shared root before indexing, so that e.g. *masada, masanın, masadaki* all match *masa* (example from Sec. 2.3, p. 29).

### Formal formulation

The thesis does not state research questions or hypotheses. The stated aim (Özet, p. i):

> "Sayfalardaki Türkçe karakterlerin doğru olarak işlenmesi, dokümanın yazıldığı dilin tanınması, sembolleştirilen metnin köklerinin bulunması sağlanarak Türkçe dokümanların daha etkin olarak indekslenmesi hedeflenmiştir."

Translation: "The aim is to index Turkish documents more effectively by processing Turkish characters correctly, identifying the document language, and finding the roots of the tokenized text."

The only retrieval-effectiveness question tested (Sec. 4.2) is the following. For a Lucene index of Milliyet, does the analyzer `TurkishPrefixMatchAnalyzer` (with stemming) give higher bpref / P@k than `StandardAnalyzer` (without stemming), for T+D and T queries?

## 4. Main idea

### Simple explanation

Keep a table of common Turkish roots. For each word, try longer and longer beginnings of the word (first 3 letters, then 4, 5, …). The **longest beginning that is a known root** becomes the index term. Names of people and places are left untouched, because otherwise a settlement ("yerleşim birimi") name like *Ağaçoba* would be reduced to *ağaç* ("tree") and match every document about trees (p. 41).

### Concrete example

The thesis's own examples:

- *delegelerin* → tries *del, dele, deleg, **delege**, delegel, …, delegelerin*; only *delege* is in the root table, so the stem is *delege* (worked example, p. 42).
- Table 4.2 (p. 66) shows the sentence "Hakem karşılaşma sırasında pozisyonlardaki takdirlerini çoğunlukla Hırvatlar lehine kullandı" ("The referee mostly used his discretion in positions in favour of the Croats during the match"). After tokenization and the filter, it becomes: hakem, karşılaş, sıra, pozisyon, takdir, çoğunluk, hırvat, leh, kullan.

### Formal method

Stemming as a dictionary lookup with longest-prefix match:

`stem(w) = argmax_{p ∈ prefixes(w), |p| ≥ 3, p ∈ R} |p|`, and `stem(w) = w` if no such p exists.

Here R is the root table, extended with "artificial roots" for consonant softening and medial-vowel drop. An artificial root is mapped back to its canonical root: *boyn → boyun*, *adağ → adak* (Table 3.3, p. 43). This formula is **our formalization** of the prose in pp. 41–43. Before the lookup, exception rules for apostrophes and names apply (§5).

The author's own framing (Sec. 2.3, p. 29):

> "Konumuz açısından bulunan kökün morfolojik kök ile aynı olması gerekli değildir. Önemli olan kök gerçekte geçerli olmasa bile birbirleriyle ilişkili kelimelerin aynı köke işaret etmeleridir."

Translation: "For our purposes the root found need not be the morphological root. What matters is that related words point to the same root even if it is not actually valid."

The author calls the method a **hybrid of brute-force (dictionary) and suffix-stripping** approaches (p. 40). In fact, no suffix rules are described. The method is a dictionary-based longest-prefix match with exception lists.

## 5. Architecture / algorithm

1. **Crawler:** Heritrix (Internet Archive), configured through a web UI (Sec. 2.1, 3.4–3.5). Not relevant to retrieval effectiveness.
2. **Language identification** (Sec. 3.2, p. 38): the Nutch `LanguageIdentifierPlugin`, i.e. N-gram profiles, detached from Nutch. A Turkish profile was added, trained on the `<TEXT>` parts of the first 100,000 Milliyet news articles (p. 39; the resulting top N-grams are in Table 3.1, p. 38).
3. **`TurkishPrefixMatchAnalyzer`** (Sec. 3.3.1, pp. 40–44), applied in this order:
   1. Lucene `StandardTokenizer`;
   2. `TurkishLowerCaseFilter`;
   3. removal of very frequent Turkish words ("ve", "veya", "ile", "ise" are the examples given). The full stop-word list is **NOT_REPORTED**;
   4. `TurkishPrefixMatchFilter`, which has four steps:
      - (a) if the token contains an apostrophe, keep only the part before it as a proper noun (*Atatürk'ün → Atatürk*, p. 41);
      - (b) if the token is in the place-name hash table, index it unchanged;
      - (c) if the token is in the table of common Turkish first names, index it unchanged;
      - (d) otherwise apply the longest-prefix lookup in the table of common noun/adjective/verb roots (starting at 3 letters), then map softened/vowel-dropped artificial roots to canonical roots (Table 3.3).
   - Tokens with no root match are indexed unchanged (p. 42).
   - The sizes and sources of the root table, the place-name table and the first-name table are **NOT_REPORTED**. The accuracy of the stemmer is **not evaluated**.
4. **Indexer** (Sec. 3.6, pp. 59–60): Lucene `IndexWriter.updateDocument`. Fields: uid, url, ctype, title, content, host, tstamp, language (Table 3.6). Only title and content are analyzed. Title and body text are concatenated into the `content` field (p. 60).
5. **Query processor** (Sec. 3.7, pp. 60–62):
   - queries are analyzed with the same `TurkishPrefixMatchAnalyzer`;
   - a `VSearchQueryParser` subclass of Lucene `QueryParser` prevents analysis of the `host` field;
   - `IndexSearcher.search(query)` runs the query;
   - results are highlighted.
   - **The scoring/similarity function is not named** (NOT_REPORTED).
   - Context (not from the thesis): Lucene releases of 2008 used a TF-IDF vector-space "DefaultSimilarity" by default; BM25 became Lucene's default only much later. Whether the author changed the similarity is not stated.

## 6. Data

### Retrieval test (Sec. 4.2, pp. 65–67)

- **Collection:** Milliyet test collection, cited as [23] Can et al., SIGIR 2006.
- **Language / domain:** Turkish newspaper news.
- **Size:** "408.314 haber" (p. 65) and "408314 gazete haberi ve 72 bilgi ihtiyacı ve ilgililik değerlendirmelerinden oluşmaktadır" ("consists of 408,314 newspaper articles and 72 information needs with relevance judgments", p. 66).
  - Cross-card note: the CR000651 and MORPH-001 cards record **408,305** documents for the same collection **[CR000651 card; MORPH-001 card]**. The 9-document difference cannot be resolved from this thesis.
- **Queries:** 72 topics with title, description and narrative fields ("başlık, tanım ve hikaye", p. 66). Two query forms are used: title + description (T+D) and title only (T).
  - All 72 topics appear to have been evaluated: every reported P@5–P@100 value × k × 72 is within rounding of an integer count of relevant documents **[computed]**.
- **Relevance judgments:** incomplete ("tam değerlendirme olmadığından", p. 66); binary, by the metric chosen (bpref).
  - Context from another card: the pool was built from the top-100 of 24 vector-space runs of the original study **[CR000651 card]**. This thesis's runs were therefore not part of the pool, which is why bpref is appropriate.
- **Train/dev/test:** none. No parameter tuning is described. Whether the root table was built independently of the topics is NOT_REPORTED.
- **Document preprocessing before indexing** (e.g., which SGML fields were indexed; whether language identification was applied): NOT_REPORTED.

### Vocabulary test (p. 65)

- The whole Milliyet collection indexed twice:
  - (1) `LetterTokenizer` + lowercasing, giving 875,202 unique terms;
  - (2) the same plus `TurkishPrefixMatchFilter`, giving 193,262 unique terms.

### Language identification test (Sec. 4.1, pp. 63–65)

- 650 documents per language.
- Turkish: Milliyet articles longer than 2,048 characters.
- English/French/German/Italian: Europarl v3.
- Prefixes of 8–2,048 characters are classified.

### Crawl test (Sec. 4.3, pp. 67–70)

- 19 listed (18 distinct) Turkish press websites.
- 6 days 13 hours of crawling; 5,961,463 URIs discovered, 5,956,563 processed; 3,046,083 documents indexed.

## 7. Baselines

| Baseline | What it is | Why selected | Fair comparison? |
|---|---|---|---|
| `StandardAnalyzer` ("kök bulma işlemi yapılmadan", i.e. without stemming, p. 66) | Lucene's default analyzer; the thesis gives no configuration | Standard no-stemming reference | **Partly.** It differs from the treatment in more than stemming. The treatment adds Turkish-specific lowercasing and a Turkish stop-word list besides the stemmer. Context (not from the thesis): Lucene's 2008 `StandardAnalyzer` lower-cases with locale-independent rules (so "I" → "i", not the Turkish "ı") and removes an English stop-word list by default. If used unchanged, the baseline mishandled Turkish dotted/dotless I. The thesis does not say whether it did |
| Other stemmers (fixed prefix, Zemberek lemmatizer, statistical stemmers) | — | — | **Not compared.** No alternative Turkish stemmer is run, even though Sec. 2.3 reviews the families and the collection's creators had tested F5 / SV / lemmatizer variants **[CR000651 card]** |

## 8. Metrics

| Metric | Definition | Simple meaning | Appropriate? |
|---|---|---|---|
| bpref (Buckley & Voorhees 2004, ref. [26]) | For each judged relevant document r, penalize by the fraction of judged non-relevant documents ranked above r; unjudged documents are ignored | "How often are judged relevant documents ranked above judged non-relevant ones?" | Yes. It was chosen explicitly because judgments are incomplete (p. 66) |
| P@k (k = 5, 10, 15, 20, 30, 100, 200, 500, 1000) | Share of the top k retrieved documents that are judged relevant; unjudged documents count as non-relevant | "Of the first k results, how many are known to be relevant?" | Usable, but biased against systems that were not in the pool (unjudged = non-relevant). Retrieval depth is at least 1,000 (P@1000 reported) |

- MAP, recall and nDCG are **not reported**.
- The evaluation tool (e.g. trec_eval) is **NOT_REPORTED**.
- Tables 4.3–4.4 are captioned "... Bpref değerleri" ("bpref values") but contain P@k rows as well.

## 9. Results

### Tables 4.3 and 4.4: StandardAnalyzer vs TurkishPrefixMatchAnalyzer (p. 67; checked on the page image)

| Metric | T+D: Standard | T+D: TurkishPM | Δ abs **[computed]** | Δ rel **[computed]** | T: Standard | T: TurkishPM | Δ abs **[computed]** | Δ rel **[computed]** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| bpref | 0.3947 | 0.5092 | +0.1145 | +29.0% | 0.3506 | 0.4538 | +0.1032 | +29.4% |
| P@5 | 0.6278 | 0.6889 | +0.0611 | +9.7% | 0.5583 | 0.5639 | +0.0056 | +1.0% |
| P@10 | 0.6042 | 0.6667 | +0.0625 | +10.3% | 0.5250 | 0.5625 | +0.0375 | +7.1% |
| P@15 | 0.5806 | 0.6556 | +0.0750 | +12.9% | 0.4944 | 0.5444 | +0.0500 | +10.1% |
| P@20 | 0.5688 | 0.6458 | +0.0770 | +13.5% | 0.4708 | 0.5312 | +0.0604 | +12.8% |
| P@30 | 0.5296 | 0.6097 | +0.0801 | +15.1% | 0.4361 | 0.5014 | +0.0653 | +15.0% |
| P@100 | 0.3676 | 0.4310 | +0.0634 | +17.2% | 0.2917 | 0.3707 | +0.0790 | +27.1% |
| P@200 | 0.2531 | 0.3020 | +0.0489 | +19.3% | 0.2080 | 0.2661 | +0.0581 | +27.9% |
| P@500 | 0.1339 | 0.1599 | +0.0260 | +19.4% | 0.1112 | 0.1452 | +0.0340 | +30.6% |
| P@1000 | 0.0760 | 0.0894 | +0.0134 | +17.6% | 0.0659 | 0.0827 | +0.0168 | +25.5% |

(The bpref cell is printed "0. 5092" with a stray space in Table 4.3.)

Reading the tables:

- **The treatment analyzer is higher on every metric in both query forms.** The author gives no relative improvement for retrieval, only the qualitative conclusion (p. 72, quoted in §13).
- **Query-length interaction** **[computed]**:
  - With T-only queries the top-5 gain is almost zero. P@5 0.5583 → 0.5639 corresponds to about 201 → 203 relevant documents in the top 5 summed over 72 queries (0.5583 × 5 × 72 = 200.99; 0.5639 × 5 × 72 = 203.00).
  - With T-only queries the gain at deep cutoffs is larger than with T+D (P@100 +27.1% vs +17.2%; P@500 +30.6% vs +19.4%).
  - The bpref gain is nearly identical (+29.0% vs +29.4%).
  - Our interpretation (not stated by the author): the analyzer mainly adds recall-side matches for short queries. For longer T+D queries it also improves the top ranks.
  - Whether these differences are reliable is unknown: no test, no per-query data.
- **Query form effect** **[computed]**: T+D beats T for both analyzers. The T+D − T difference in bpref is +0.0441 without stemming and +0.0554 with stemming, i.e. longer queries do **not** substitute for stemming here.
  - In relative terms the stemming gain is the same for both query forms (+29.0% vs +29.4%), so bpref here does not show the pattern recorded for MORPH-001, where extra query terms partly compensate for the absence of stemming **[MORPH-001 card]**. The setups differ (vector-space matching functions, query forms, analyzers), so this cannot be treated as a contradiction.

### Vocabulary reduction (p. 65; checked on the page image)

| Index | Unique terms |
|---|---:|
| LetterTokenizer + lowercase | 875,202 |
| + TurkishPrefixMatchFilter | 193,262 |

- The author states a reduction of "77.9%" **[computed: (875,202 − 193,262)/875,202 = 77.92% ✓]**, i.e. 4.53× fewer terms **[computed]**.
- **This is not the vocabulary of the evaluated configuration**:
  - it uses `LetterTokenizer`, which, as the thesis itself says, produces tokens "sadece harflerden oluşan" ("consisting only of letters");
  - the evaluated analyzer uses `StandardTokenizer` plus stop-word removal.
  - With letter-only tokens the apostrophe rule (step a) cannot fire, because an apostrophe can never be inside such a token **[inferred from the thesis's description]**.

### Language identification (Table 4.1 / Fig. 4.1, p. 64; checked)

- Share of correctly identified documents, Turkish: 57.38% (8 chars), 75.08% (16), 86.92% (32), 93.08% (64), 98.77% (128), 100% from 256 characters.
- The other four languages reach ≥ 99.23% from 32 characters and 100% at 128 (German/Italian 99.85% at 64).
- Stated reason for the weaker Turkish result: foreign words and names in news, especially football (pp. 64–65).
- Fig. 4.1's last x-axis tick reads "2028" instead of 2048.

### Crawl test (Tables 4.6–4.8, pp. 69–70; checked)

- HTTP-200: 4,847,110 (83.27%). The six listed codes sum to 5,819,745 **[computed]**. The printed percentages match that sum within ≤ 0.02 percentage points; the denominator is not stated.
- MIME types sum exactly to the HTTP-200 count (4,847,110) **[computed]**.
- Indexed documents: 3,046,083, of which 98.90% identified as Turkish (3,012,754) **[computed sum ✓]**.
- No retrieval effectiveness was measured on the crawled collection.

## 10. Statistical evidence

- **Significance test:** NOT_REPORTED (none performed or mentioned).
- **Confidence intervals:** NOT_REPORTED.
- **Runs / seeds:** one result per configuration is reported; the number of runs is not stated (a deterministic Lucene index/search pipeline has no stochastic components, so a single run is presumed **[inferred]**).
- **Ablation:** **none.** The four components of the treatment analyzer (Turkish lowercasing, stop-words, name/apostrophe exceptions, root lookup) are never evaluated separately. The vocabulary test isolates the filter, but only for term counts, not for effectiveness.
- **Per-query analysis:** **none.** There is:
  - no per-topic table;
  - no win/loss count;
  - no failure analysis beyond the constructed Ağaçoba example (p. 41);
  - no overlap or unique-relevant-hit analysis between the two indexes;
  - no oracle union.
- **Stemmer accuracy:** not evaluated (no gold roots, no over-/under-stemming rates, no share of tokens left unchanged).

## 11. Strengths

- Uses a real TREC-style Turkish test collection with 72 topics and the metric appropriate to incomplete judgments (bpref), not an ad hoc demo.
- Reports **both query forms** (T and T+D) and **many cutoffs** (P@5–P@1000), which exposes the query-length × depth pattern (§9).
- Explicit, step-by-step description of the stemming procedure, with worked examples (pp. 40–44). The procedure is clear, but the stemmer is not reproducible without the unreported root, first-name and place-name tables (§12, item 5). It includes practical exception handling for proper nouns and place names that simple stemmers lack.
- Separates the vocabulary-size argument from effectiveness: "Amaç terim sayısının azaltılması değil bir bilgi erişimin sistemi olan arama motorumuzun etkinliğinin artırılmasıdır" ("the goal is not to reduce the number of terms but to increase the effectiveness of our search engine, an information retrieval system", p. 65).
- Handles morphophonological alternation (consonant softening, medial vowel drop) explicitly (Table 3.3).

## 12. Limitations

### Stated by the author

- Relevance judgments of Milliyet are incomplete, hence bpref (p. 66).
- Turkish language identification is weaker on short texts because of foreign words and names (pp. 64–65).
- Boilerplate on dynamic news pages (menus, ads, "most read" boxes) is indexed and lowers relevance; content extraction is out of scope (Ch. 5, p. 71).
- Domain-specific tokenization and stemming would be needed for other verticals, e.g. automotive vs media monitoring (Ch. 5, p. 71).
- No crawler performance metric exists; the crawler was evaluated only descriptively (p. 67).

### Inferred from the experimental design

1. **Confounded comparison.** `TurkishPrefixMatchAnalyzer` differs from `StandardAnalyzer` in lowercasing, stop-words and stemming at once, and the baseline's configuration is not reported. The +29% bpref cannot be attributed to stemming alone, although the author frames the comparison as "kök bulma işlemi yapılmadan ve ... yapılarak" ("without and with stemming", p. 66).
2. **Unknown ranking function.** The Lucene similarity is not named, so the result cannot be placed relative to BM25-based evidence (MORPH-002).
3. **Vocabulary figure from a different pipeline** (LetterTokenizer, no stop-words, apostrophe step inert) than the evaluated one.
4. **No alternative normalization** (fixed-length prefix, lemmatizer, statistical stemmer) on the same setup. The work shows "this analyzer > default analyzer", not that its stemming method is better than others.
5. **Unreported resources.** The root, first-name and place-name tables are neither sized nor sourced, so the stemmer cannot be reproduced. The share of OOV tokens (indexed unchanged) is unknown.
6. **Name-list blocking may interact with common words** that are also first names or place names (exact-match lookup precedes stemming). This is not examined.
7. **Pool bias.** The thesis's runs were not in the judgment pool **[CR000651 card]**, so P@k (unjudged = non-relevant) may understate both systems and may affect them unequally. bpref mitigates this partly.
8. **No significance test, no per-query analysis**, and a single collection/domain (news).
9. The retrieval experiment is a small part of a primarily engineering thesis (≈ 2 of ~74 printed pages).

## 13. What the work proves

Within its limits (no significance test):

- On Milliyet (72 topics), a Lucene index built with the author's Turkish analyzer (Turkish lowercasing + Turkish stop-words + dictionary longest-prefix stemmer with name protection) scores higher than one built with Lucene's `StandardAnalyzer`, on bpref and on P@5–P@1000, for both T+D and T queries:
  - bpref 0.5092 vs 0.3947 (T+D);
  - bpref 0.4538 vs 0.3506 (T) (Tables 4.3–4.4, p. 67).
- The gain is consistent in direction across all 20 reported metric × query-form cells.
- The filter reduces the unique-term vocabulary of a letter-tokenized, lowercased Milliyet index by 77.9% (875,202 → 193,262; p. 65).
- Descriptively only (aggregate means, no test, no per-query data): for short (title-only) queries the observed gain is concentrated at deeper cutoffs, with almost no change at P@5; for T+D queries it is spread across the ranking (§9, **[computed]**). This is a pattern in the reported means, not an established effect.
- The author's conclusion (p. 72), which is supported in direction by Tables 4.3–4.4:

> "Geliştirilen Türkçe kök bulma yöntemi sayesinde test sonuçlarında da açıkça gördüğümüz gibi Türkçe bilgi erişim performansının artmasına rağmen indekse kaydedilen eşsiz terim sayısında ciddi bir azalma gözlenmektedir."

Translation: "Thanks to the developed Turkish stemming method, as clearly seen in the test results, although Turkish IR performance increases, a serious reduction is observed in the number of unique terms stored in the index."

## 14. What the work does NOT prove

- **That the stemmer itself causes the gain.** Lowercasing and stop-word differences are confounded, and there is no ablation.
- **That the gain is statistically significant**, or how it is distributed over queries.
- **That this stemmer is better than simpler or other normalizations** (fixed prefix, lemmatization, statistical stemming). None was compared.
- **Anything about BM25.** The scoring function is not named, and BM25 is not mentioned.
- **Anything about dense/semantic retrieval, hybrid fusion, or complementarity** between the stemmed and unstemmed indexes (overlap, unique relevant hits, oracle union). None of these is measured, even though two indexes of the same collection existed and such an analysis would have been possible.
- **That the vocabulary reduction applies to the evaluated system** (different pipeline).
- **Stemmer accuracy** or linguistic validity. By design the author does not require valid roots (p. 29).
- **Generalization** beyond Turkish news, and to Uzbek. The apostrophe rule in particular does not transfer (§17).

## 15. Relationship to current Uzbek evidence

- **No Uzbek data.** Turkish and Uzbek are both agglutinative Turkic languages with suffixing morphology and some parallel morphophonology. Turkish consonant softening (k→ğ, p→b), for instance, has partial analogues in Uzbek (e.g. *yurak → yuragi*). This is context from general linguistic knowledge, not from the thesis.
- **Methodological kinship with national Uzbek stemmers.** The dictionary-plus-exceptions approach resembles the dictionary/affix-based Uzbek morphological tools in the national evidence (Bakaev, Xusainova, Elov; MASTER_INDEX C). Like them, it reports no qrels-based comparison of different normalization variants. Here, however, there is at least a qrels-based raw-vs-stemmed comparison, which the national works lack **[MASTER_INDEX / GAP_BOUNDARY summaries]**.
- **Relation to the other Milliyet cards:**
  - MORPH-001 (Can et al. 2008; vector-space MFs; NS / F5 / SV / LV; query length);
  - CR000651 (Can et al. 2006 SIGIR short paper);
  - MORPH-002 (Haddad & Bechikh Ali 2014; TF-IDF / BM25 / LM with Zemberek and prefix truncation).
  This thesis adds an independent 2008 Lucene implementation with a different stemmer type, on the same collection and with the same direction of effect. It does **not** add a new evidence dimension relevant to the v0.8 gap.
- **Apostrophe handling** is a direct warning for Uzbek (§17). The Turkish orthographic rule it exploits (apostrophe separates suffixes from proper nouns) does not hold in Uzbek Latin script, where apostrophe-like characters are part of letters.

## 16. Relationship to CURRENT_GAP

**Classification:** *supports (already occupied boundary)* + *no material effect on the residual core*.

- **Supports an already listed non-claim.** v0.8 already states that one cannot claim "морфология ранее не применялась к поиску" or that raw/stem comparisons are absent in morphologically rich languages. This thesis is one more (weak, B-level) Turkish instance of stemmed > unstemmed lexical retrieval on a test collection.
- **Touches, weakly:** the query-feature dimension. Query length (T vs T+D) changes where in the ranking the normalization gain appears (§9). This is aggregate-only and untested, and it concerns lexical-only effectiveness, not complementarity.
- **Does not touch** any element of the v0.8 residual core:
  - BM25_raw / stem / lemma with the **same fixed dense retriever D**: no BM25, no D, no lemma variant;
  - unique relevant hits / overlap / oracle union: absent;
  - incremental hybrid gain: no fusion;
  - morphology-induced complementarity change linked to query features: absent.
- None of the "What can still kill this gap" conditions (CURRENT_GAP) is met: no Uzbek benchmark, no per-query overlap analysis, no Turkic work closing the interaction mechanism.

**Proposal:** keep v0.8 refined unchanged. Optionally list this thesis as minor supporting Turkish evidence in the lexical-morphology boundary, behind MORPH-001/MORPH-002. This is a proposal only; `CURRENT_GAP.md` has not been edited.

## 17. Implications for our research design

- **Morphology preprocessing: apostrophes.**
  - Step (a) of the filter ("keep only the part before an apostrophe") is correct for Turkish proper-noun suffixes but would destroy Uzbek words. In Uzbek Latin the apostrophe marks the letters o‘/g‘ and the tutuq belgisi (e.g. *ma'no*, *san'at*), and it is not the standard separator of suffixes from proper nouns (context from Uzbek orthography, not from the thesis).
  - Any Turkish-derived or generic stemmer must therefore run **after** a fixed apostrophe normalization (ʻ U+02BB, ' U+0027, ‘ U+2018, ’ U+2019, ` → one canonical form), and must not split on it.
  - Record this in the preprocessing protocol together with the BM25 tokenizer decision already proposed in the Amharic exemplar card.
- **Named-entity protection.** The name/place exception lists are a cheap way to prevent harmful conflation (*Ağaçoba → ağaç*). For Uzbek:
  - consider a proper-noun / toponym exception list in `BM25_stem` and `BM25_lemma`;
  - report its effect separately;
  - keep "named entity in query" as a candidate query feature (already in CURRENT_GAP).
- **One-factor-at-a-time control.** The raw/stem/lemma lexical variants must share:
  - the tokenizer;
  - case folding (Uzbek Latin has no dotted/dotless I problem, but Cyrillic/Latin and case rules must be fixed);
  - the stop-word policy;
  - the ranking function with fixed k1/b.
  Only the morphological step may differ. Otherwise, as here, the "stemming effect" is confounded.
- **Report vocabulary / OOV statistics for the evaluated configuration.** Report the unique-term reduction and the share of tokens the stemmer/lemmatizer leaves unchanged, computed on exactly the index used in the retrieval runs.
- **Query taxonomy and query forms.** Evaluate at least two query lengths or forms (short keyword vs descriptive), and report metrics at both shallow (P@5 / nDCG@10) and deep (Recall@100 / 1000) cutoffs. Here the normalization gain for short queries appears mainly at depth, which is exactly where lexical–dense complementarity (unique hits in the candidate set) matters.
- **Pool construction.** Include every compared representation (raw/stem/lemma BM25, D, hybrids) in the judgment pool. Otherwise report bpref / condensed-list metrics as this thesis did.
- **Statistics.** Per-query paired tests (and per-query deltas) are needed. This thesis shows how easily a consistent-looking table can have no inferential support.
- **Hypothesis.** The thesis gives no evidence for or against the morphology → complementarity hypothesis. The depth pattern (§9) is a weak motivation: stemming may change *which* relevant documents enter the deep candidate set, which is what our overlap/unique-hit analysis would measure.

## 18. Important terms

| Term | Simple explanation | Formal meaning |
|---|---|---|
| Vertical search engine (dikey arama motoru) | A search engine that covers one topic or set of sites, rather than the whole web | Domain-restricted crawling, indexing and ranking |
| Analyzer (Lucene) | The chain that cuts text into index terms: tokenize → lowercase → drop stop-words → stem | Lucene `Analyzer` = Tokenizer + TokenFilters |
| Stemming (kök bulma) | Reducing word forms to a shared base so that *masada* and *masanın* both match *masa* | Mapping w → s(w) for conflation; s(w) need not be a linguistic root |
| Longest-prefix dictionary match | Try longer and longer word beginnings and keep the longest that is in a root list | `argmax |p|` over prefixes p ∈ R |
| Fixed-length prefix truncation (F5) | Cut every word to its first 5 letters, with no dictionary (the method of MORPH-001/002, **not** used here) | s(w) = w[:5] |
| Consonant softening / medial vowel drop (yumuşama / orta hece ünlüsünün düşmesi) | Sound changes that alter the root when a suffix is added; the thesis's examples are *çorap+ı → çorabı* and *boyunum → boynum* (pp. 39–40) | Morphophonological alternations handled by "artificial root" tables |
| Stop-words | Very frequent words (e.g. *ve*, *ile*) removed before indexing | Term filter by list |
| bpref | A score that only uses judged documents: how often relevant ones are ranked above judged non-relevant ones | Buckley & Voorhees 2004 (ref. [26]) |
| P@k | Fraction of the top k results that are known relevant | \|rel ∩ top-k\| / k |
| T vs T+D queries | Query built from the topic title only vs title plus description sentence | Topic field selection |
| Pooling | Only documents retrieved by some reference systems are judged; others are unjudged | Depth-k pool over contributing runs |
| Complementarity (project term) | Each channel or representation finds some relevant documents the other misses | Unique relevant hits, overlap, oracle-union gain (not measured here) |

## 19. Open questions / verification needed

1. **Bibliographic record:** verify in YÖK Ulusal Tez Merkezi (thesis number) and ProQuest (28638778). Confirm the final Institute approval, which is blank on the approval page of this copy.
2. **`StandardAnalyzer` configuration** (Lucene version, stop-word list, lowercasing) and the **similarity function**: NOT_REPORTED. Only the author could confirm.
3. **Root table, first-name table and place-name table:** sizes, sources, coverage (share of tokens left unchanged): NOT_REPORTED.
4. **Evaluated vocabulary:** unique-term count for the actual `TurkishPrefixMatchAnalyzer` index (StandardTokenizer + stop-words) is not given, only the LetterTokenizer variant's.
5. **Collection size:** 408,314 (this thesis, pp. 65–66) vs 408,305 (CR000651 / MORPH-001 cards). Different versions or a count difference?
6. **Worked example inconsistency** (p. 42): step 1 "del" is marked "yok" (no match) but "Kaçıncı harf" = 3. Either the table records the starting length rather than a match, or it is a typo. It does not change the result *delege*.
7. **Minor editorial duplicates:** Table 3.2 (p. 41) lists *Ağadibek* and *Ağalar* twice; Table 4.9 (p. 70) lists `tercuman.com.tr` twice (#16 and #19), so 19 rows = 18 distinct sites; Fig. 4.1 x-axis tick "2028".
8. **Query construction:** how the T+D text was passed to `QueryParser` (default operator, handling of punctuation) is NOT_REPORTED.
9. **Triage note correction (for the coordinator):** the triage note calls the method "Prefix-match (truncation-style) stemming". According to Sec. 3.3.1 it is a **dictionary-based longest-prefix match with name exceptions and morphophonological root mapping**, not fixed-length truncation.

## 20. Decision after deep dive

- **Keep current gap?** Yes. v0.8 refined remains valid (§16).
- **Modify gap?** No. Optionally add the thesis as minor Turkish supporting evidence to the lexical-morphology boundary (researcher's decision).
- **Add decision?** Proposed for `decisions/DECISIONS.md` (researcher's decision):
  - "Morphological variants of the lexical channel differ **only** in the morphological step; tokenizer, apostrophe normalization, case folding, stop-words and BM25 parameters are identical and reported."
  - "Apostrophe variants are normalized before tokenization and stemming; no stemmer may split Uzbek words at apostrophes."
  - "Vocabulary reduction and OOV (unchanged-token) rates are reported for the exact evaluated index."
- **Add experiment?** Low-cost addition to the planned pilot: a proper-noun / toponym exception list as a sub-variant of `BM25_stem`, and reporting of metrics at shallow and deep cutoffs for short vs descriptive queries. No new stand-alone experiment is justified by this thesis.
- **Add citation to Chapter I?** Optional, low priority. In §1.1 (lexical IR and morphology in Turkic languages) it can appear as a supplementary example of a dictionary-based Turkish stemmer in a Lucene system with bpref gains on Milliyet. Primary citations should remain MORPH-001 and MORPH-002. Cite it with its Master's thesis status and the confound caveat.
- **Proposed `MASTER_INDEX.md` row** (to add after approval):

| MORPH-021 | Kılıç — *Türkçe dokümanlar için özelleştirilebilir web tabanlı dikey arama motoru* (MSc thesis, Anadolu Univ., supervisor Ö. Yılmazel) — [deep dive](deep-dives/2008_Kilic_Turkish_Vertical_Search_Engine.md) | 2008 | B | LOW | Lucene vertical search engine with a dictionary longest-prefix Turkish stemmer (apostrophe/place-name/first-name exceptions, softening/vowel-drop root mapping). On Milliyet (72 topics, bpref): TurkishPrefixMatchAnalyzer vs StandardAnalyzer bpref 0.5092 vs 0.3947 (T+D), 0.4538 vs 0.3506 (T); vocabulary −77.9% (different pipeline). Comparison confounded with Turkish lowercasing and stop-words; ranking function not named; no BM25, no significance test, no other normalization variants, no dense/fusion/overlap analysis. |
