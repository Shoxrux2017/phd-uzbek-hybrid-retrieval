# Xusainova Z.Y. — Uzbek tokenization, stemming, lemmatization and search/corpus optimization

**Deep-dive status:** COMPLETED
**Completed:** 2026-09-11
**Suggested IDs:** PHD-UZ-003 / MORPH-UZ-003 / MORPH-UZ-004
**Reliability:** A
**Priority:** CRITICAL national boundary

## 1. Bibliographic record
- Author: Zilola Yuldashevna Xusainova
- Title: *O‘zbek tili birliklarini tokenlash, stemlash, lemmalashning lingvistik asoslari va dasturiy ta’minoti*
- Degree: PhD in Philological Sciences
- Specialty: 10.00.11 — Language Theory. Applied and Computational Linguistics
- Institution: Alisher Navoiy Tashkent State University of Uzbek Language and Literature
- Supervisor: Botir Boltayevich Elov
- Registration: B2023.2.PhD/Fil3688
- Author abstract: Tashkent, 2024, 53 pages
- Official OAK defense announcement: https://oak.uz/pages/17441
- Later 2026 publications identify Xusainova as PhD and acting associate professor.

## 2. Why this work is critical
Xusainova directly studies tokenization, stemming and lemmatization and explicitly connects them to Uzbek National Corpus search and multilingual electronic-platform search. Therefore novelty cannot be claimed from merely introducing Uzbek stemming/lemmatization into search.

However, the work does not provide a modern qrels-based retrieval benchmark comparing raw/stem/lemma under BM25 and a fixed dense retriever.

## 3. Main research tasks
- Uzbek-specific tokenization;
- theoretical foundations of stemming and lemmatization;
- stemming problems for agglutinative languages;
- linguistic rules for Uzbek stemming/lemmatization;
- optimization of Uzbek National Corpus search;
- BPE tokenization;
- affix-removal-based UzbStemming;
- software: Uzbek tokenizer, stemmer and lemmatizer.

## 4. Tokenization
The dissertation discusses Bag of Words and BPE and implements an Uzbek tokenizer at `uznatcorpara.uz/uz/Tokenizer`.

## 5. UzbStemmer
The proposed stemmer uses:
- corpus data;
- affix database;
- Uzbek morpholexicon;
- roots/stems database;
- POS information;
- two-stage affix-removal logic.

Reported evaluation:
- applied to **more than 100,000 sentences** of the Uzbek educational corpus;
- reported **97.5% accuracy**.

This is stemming/base-identification accuracy, not document-retrieval effectiveness.

## 6. Lemmatization
The dissertation distinguishes:
- stemming = remove affixes to obtain a stem;
- lemmatization = determine the dictionary/canonical form with lexical/morphological knowledge.

Rules are developed for simple, derived, compound, repeated and paired words, compound verbs, multi-token constructions, phraseological units, NERs, neologisms and abbreviations.

A lemmatizer is implemented at `uznatcorpara.uz/uz/Lemmatizer`.

## 7. Lexical resources
Implementation evidence reports:
- more than **32,000 simple lexemes**;
- more than **7,500 compound lexemes**.

## 8. Search-system claims
The dissertation and official OAK summary state that stemming/lemmatization:
- optimized Uzbek National Corpus search;
- improved search quality in a multilingual Uzbek-literature platform;
- improved a Turkic-language educational platform search indicator.

But the inspected author abstract does not report:
- fixed query benchmark;
- qrels;
- raw/stem/lemma retrieval baselines;
- MAP, nDCG, MRR, Recall@k, Precision@k;
- statistical significance;
- BM25.

Therefore the search-improvement statements are implementation/deployment claims, not controlled modern IR evidence.

## 9. Important terminology warning: IR vs SEO
A section on search optimization partly discusses **SEO**, website keywords, page optimization and ranking factors. This should not be equated with ad-hoc IR evaluation.

Our PhD task is:
`query -> ranked relevant documents/passages`

using qrels.

## 10. Evidence matrix
| Question | Xusainova |
|---|---|
| Uzbek tokenization | ✅ |
| BPE tokenizer | ✅ |
| Uzbek stemming | ✅ |
| Uzbek lemmatization | ✅ |
| 32k+ simple / 7.5k+ compound lexemes | ✅ |
| UzbStemmer evaluation | ✅ 97.5% analyzer-level accuracy |
| Corpus/search optimization | ✅ applied/claimed |
| Controlled raw vs stem vs lemma retrieval | ❌ |
| BM25 | ❌ |
| Query-document qrels | ❌ |
| MAP/nDCG/MRR/Recall@k | ❌ |
| Dense retrieval | ❌ |
| BM25 + dense | ❌ |
| lexical-only/dense-only hits | ❌ |
| overlap/oracle union | ❌ |
| morphology-induced hybrid gain | ❌ |

## 11. What the work proves
1. Uzbek tokenizer, stemmer and lemmatizer software already exist.
2. Uzbek stemming has been evaluated at analyzer level.
3. Linguistic rules exist for structurally diverse Uzbek lexical units.
4. Morphological preprocessing is already used in national corpus/search-related systems.
5. Search optimization through stemming/lemmatization is not a new general idea for Uzbek.

## 12. What it does not prove
It does not establish:
- `BM25_lemma > BM25_stem > BM25_raw`;
- that lemmatization improves BM25;
- that stemming improves BM25;
- which morphology variant gives best retrieval effectiveness;
- dense retrieval effectiveness;
- lexical+dense complementarity;
- morphology-induced changes in overlap/unique relevant hits;
- incremental hybrid gain;
- query-feature effects on hybrid gain.

## 13. Relation to Bakaev
Bakaev shows earlier morphology-aware Uzbek search and library/full-text applications. Xusainova adds explicit tokenizer/stemmer/lemmatizer software and corpus/search applications. Together they eliminate any broad novelty claim based on simply adding morphological normalization to Uzbek search.

Neither performs the controlled interaction experiment required by v0.8.

## 14. Relation to CURRENT_GAP v0.8
**Status: strongly supports national boundary; does not close v0.8.**

Residual chain remains:
`raw/stem/lemma`
→ `BM25 relevant-set change`
→ `overlap/unique hits with fixed dense retriever`
→ `incremental hybrid gain`
→ `relation to Uzbek query characteristics`.

## 15. Implications for our design
1. Do not build a new stemmer/lemmatizer as the main contribution.
2. Evaluate existing Xusainova/related resources for reuse.
3. Keep raw/stem/lemma as controlled lexical representations.
4. Use the same BM25 protocol for all variants.
5. Hold the dense retriever fixed.
6. Evaluate with qrels and standard IR metrics.
7. Separate analyzer accuracy (97.5%) from search quality.
8. Analyze compounds, NERs, neologisms, script/spelling variation and multi-token lexical units as possible query features.

## 16. Practical relevance to the National Library
The tokenizer, stemmer, lemmatizer and morpholexicon are useful engineering candidates. The final library system should use whichever representation wins our controlled retrieval experiment; lemmatization should not be assumed best a priori.

## 17. Open questions
- Obtain the full 153-page dissertation if possible.
- Check whether the full dissertation contains numerical search experiments omitted from the abstract.
- Verify current access/licensing for tokenizer, stemmer, lemmatizer and morpholexicon.
- Clarify exact ground truth behind 97.5% stemming accuracy.
- Verify whether platform search improvements were measured quantitatively in project reports.
- Keep SEO discussion separate from IR evaluation.

## 18. Decision
- Keep CURRENT_GAP v0.8: yes.
- Deep-dive role: CRITICAL national morphology/search boundary.
- Change gap/history/decisions: no.
