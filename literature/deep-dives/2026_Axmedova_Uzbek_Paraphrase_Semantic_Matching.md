# Axmedova X.X. — Uzbek paraphrasing and semantic matching

**Deep-dive status:** COMPLETED  
**Completed:** 2026-09-11  
**Suggested ID:** UZ-SEM-008  
**Reliability:** B pending final-defense protocol verification

## 1. Bibliographic record
- Author: Axmedova Xusniya Xusanovna / Akhmedova Khusniya Khusanovna
- Title: *O‘zbek tilidagi matnlarni perefraz qilish jarayonlari va axborot tizimini ishlab chiqish*
- Degree sought: PhD, technical sciences
- Specialty: 05.01.10 — Information retrieval systems and processes
- Institution: TUIT
- Supervisor: Sultanov Djamshid Baxodirovich
- Registration: B2025.1.PhD/T5316
- Supplied author abstract: 2026, 24 pages
- Official status verified: TUIT seminar 2026-06-24; OAK defense announcement 2026-07-23
- Final defense protocol/outcome: not recovered as of 2026-09-11

## 2. Why it matters
This work proves that modern semantic-text processing for Uzbek already uses:
- Multilingual E5 embeddings;
- Jina embeddings;
- cosine similarity;
- transformer paraphrase generation;
- a fine-tuned Gemma-based model;
- automatic semantic-duplicate/paraphrase detection in documents.

Therefore we cannot claim that modern Uzbek semantic matching is absent.

## 3. What problem it solves
The work addresses:
1. automatic Uzbek paraphrase generation;
2. detection of sentences that express nearly the same meaning.

This is primarily **paraphrase / semantic similarity**, not query-to-corpus document ranking.

## 4. Main method
### Paraphrase detection
`sentence -> Multilingual E5 embedding -> cosine similarity -> threshold`

Uploaded `.txt/.doc/.docx` files are split into sentences; each sentence is encoded and compared with other sentences. Pairs with reported semantic similarity above 85% are treated as paraphrase candidates.

### Dataset construction
Jina embeddings are used to select semantically equivalent candidate sentences from web-scraped Uzbek news texts.

### Paraphrase generation
A Gemma3-4B-PT-based model is fine-tuned to generate Uzbek paraphrases.

## 5. Data
Final-description figures:
- 375,000 triplets;
- 194 MB;
- about 35,000 root/base words and synonym pairs;
- more than 3,500 phrases and semantic equivalents;
- source texts from about fifteen Uzbek news sites.

Another section reports:
- >3,000 synonym words;
- about 250 phrase synonyms;
- 250K sentence/paraphrase pairs;
- testing on 5K sentences;
- 88.3% system accuracy.

**Caution:** the abstract does not reconcile the 250K/5K/88.3% description with the later 375K/91.3% description. Preserve both as separate reported stages until the full dissertation is checked.

The abstract also states that Jina embeddings helped select semantically equivalent examples. It does not clearly document independent human validation for the full 375K resource, so label quality needs further verification.

## 6. Main numerical results
Reported model comparison:

| Model | Precision | Recall | Accuracy | F1 |
|---|---:|---:|---:|---:|
| google-bert/bert-large-cased | 0.85 | 0.75 | 0.81 | 0.80 |
| google/flan-t5-large | 0.75 | 0.66 | 0.75 | 0.70 |
| Gemma3-based | **0.954** | **0.955** | **0.913** | **0.954** |

The prose rounds this to about 91% accuracy and F1≈0.95.

Reported Gemma training:
- 4 × RTX 4090;
- 11 days;
- 5 epochs;
- 375K triplets.

A separate section reports 88.3% system accuracy for an earlier/different setup.

## 7. Important distinction: this is not corpus-level IR
Axmedova asks roughly:

> Which sentences inside a document say the same thing?

Our PhD asks:

> Given a user query and a large collection, which documents/passages should be ranked as relevant?

So:

`semantic similarity / paraphrase detection != corpus-level ad-hoc retrieval`

Using the same embedding family does not make the tasks equivalent.

## 8. What the work establishes
- modern multilingual embeddings are already used for Uzbek;
- Multilingual E5 can represent Uzbek sentences for semantic matching in this application;
- Uzbek paraphrase generation with a transformer model is feasible;
- paraphrastic variation and semantic duplicates are already modeled nationally.

## 9. What it does NOT establish
- BM25 vs dense retrieval;
- `BM25_raw/stem/lemma`;
- full-corpus dense retrieval effectiveness;
- lexical+dense hybrid retrieval;
- qrels-based MAP/nDCG/Recall@k;
- lexical-only vs dense-only relevant hits;
- overlap/oracle union;
- morphology-induced complementarity;
- incremental hybrid gain.

## 10. Relation to CURRENT_GAP v0.8
**Supports/narrows broad claims; does not close v0.8.**

Axmedova kills broad claims such as:
- “modern semantic embeddings are absent for Uzbek”;
- “paraphrastic variation has not been modeled”;
- “E5-style semantic matching has not been used”.

But the residual question remains:

`raw/stem/lemma lexical representation`
→ `change in BM25 relevant set`
→ `change in overlap/unique hits with the same dense retriever`
→ `change in incremental hybrid gain`
→ `relation to Uzbek query features`.

## 11. Implications for our research design
1. Do not make E5 usage itself a novelty.
2. A multilingual E5-family retriever can still be a candidate dense baseline, but it must be evaluated as a **retriever**.
3. Paraphrastic/descriptive query formulation is a reasonable candidate query feature.
4. The paraphrase resource might later help query-reformulation or robustness experiments, but this is secondary.
5. Our core benchmark must use query-document relevance judgments.

## 12. Status / metadata
TUIT officially announced seminar discussion on 2026-06-24. OAK officially announced the defense on 2026-07-23 and confirms registration number B2025.1.PhD/T5316. A final protocol awarding the degree has not yet been recovered, so keep reliability at **B pending final-defense verification**, not A.

## 13. Open questions
- Verify final defense outcome/protocol.
- Obtain full dissertation.
- Reconcile 250K/5K/88.3% vs 375K/91.3%/F1 0.954.
- Verify train/dev/test split and leakage controls.
- Verify human validation level of the 375K triplets.
- Verify exact E5 and Jina checkpoints.
- Verify how the 85% cosine threshold was chosen.

## 14. Decision
- Keep CURRENT_GAP v0.8: **yes**
- Modify gap/history/decisions: **no**
- Add to national semantic map: **yes**
- Main role: strong national evidence for modern Uzbek semantic matching, with the boundary `paraphrase/STS != corpus-level IR`.
