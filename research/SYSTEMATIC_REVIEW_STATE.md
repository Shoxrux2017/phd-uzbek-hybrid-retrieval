# Systematic Review State

**Last updated:** 2026-09-28

**Status:** primary title/abstract screening complete; second review not started; full-text stage not started.

This state records the primary-screening milestone before the second-review stage. It does not certify or advance any existing local preparation work.

## Update 2026-09-28 — full-text stage (supersedes the "NOT STARTED" statements below)

- Title/abstract stage finished (second review and adjudication completed); **509** records sought for full text (P1 265, P2 244).
- Full texts obtained: **281** of 509; the remaining **228** (mostly paywalled IEEE) are pending library access. Unretrieved records will be coded FT7 and characterised per protocol §4.
- **Tier 1 triage** (281 full texts, AI-assisted, 10% blind retest): 124 INCLUDE / 157 EXCLUDE. After Tier 2, three records were recoded as FT8 duplicate studies, giving **121 INCLUDE / 160 EXCLUDE**. Revisions are logged in `07_full_text/triage/FULL_TEXT_TRIAGE_REVISIONS_2026-09-28.csv`.
- **Tier 2 extraction** (AI-assisted): **121 studies**, using the 60-field schema and frozen codebook v1.0 plus Extraction Clarification 001. Blind retest on 13 studies: 91.9% agreement over 38 categorical fields and 95.9% on core fields. Files are in `07_full_text/extraction/`.
- **Descriptive observation (not synthesis):** no included study reports lexical ↔ dense complementarity decomposition (unique relevant hits / overlap / oracle union). Dense channel: 13 studies. Lexical + dense hybrid: 4 studies.
- **Deep dives:** 41 cards (see `literature/DEEP_DIVES_BATCH_2026-09-28_SUMMARY.md`).
- **Not yet done:** FT7 characterisation of unretrieved records, retrieval of the 228 pending full texts (triage/extraction for those that arrive), and the synthesis protocol and synthesis.
- Provenance: all stages are AI-assisted; none is human full-text review.

## Article

**Title:** “Morphological Representation in Information Retrieval for Morphologically Rich Languages: A Systematic Review of Lexical, Dense, and Hybrid Retrieval with an Uzbek Perspective”

**Primary target:** ACM TALLIP

## Identification

- Raw records: **2224**.
- Duplicates removed: **214**.
- Records entering title/abstract screening: **2010**.

## Primary screening

- INCLUDE: **256**.
- EXCLUDE: **1111**.
- UNCERTAIN: **643**.
- Coverage: **2010/2010**.
- Unique IDs: **2010**; missing decisions: **0**; invariant violations: **0**.

## Screening provenance

Primary screening: **AI-assisted**.

**This is NOT independent dual-human screening.** Calibration, drift checks and corrections within the primary workflow do not establish two independent human reviewers.

## Screening rules

- [TITLE_ABSTRACT_SCREENING_CODEBOOK.md](systematic-review/methods/TITLE_ABSTRACT_SCREENING_CODEBOOK.md)
- [SCREENING_CODEBOOK_CLARIFICATION_001.md](systematic-review/methods/SCREENING_CODEBOOK_CLARIFICATION_001.md)
- [SCREENING_CODEBOOK_CLARIFICATION_002.md](systematic-review/methods/SCREENING_CODEBOOK_CLARIFICATION_002.md)

Clarification 001:

- Retrieval alone does not establish INCLUDE.
- Meaningful morphology relevance is required.
- A pipeline endpoint alone does not establish EXCLUDE; inspect separately evaluated retrieval.
- An unclear relation requires UNCERTAIN.

Clarification 002:

- Speech/audio/ASR origin does not automatically justify TA1.
- Determine the retrieval object and task.
- Clearly non-text retrieval may justify TA1.
- Unclear modality requires UNCERTAIN.
- Word/subword retrieval does not automatically establish INCLUDE.

The original Clarification 001 retains its historical PROPOSED heading; the primary final manifest records its operational authorization. Copies preserve the original files.

## Primary correction overlay

**CR000691:** one explicit correction changes the historical INCLUDE decision to **UNCERTAIN / TA8**. The historical batch artifact remains intact.

Decision precedence:

`latest correction overlay > finalized batch artifact > older preliminary artifact`

The correction is part of the same AI-assisted primary workflow, not an independent second review.

## Second review

- Frozen random sample: **402**.
- Primary UNCERTAIN: **643**.
- Planned second-review population: `UNION(frozen random 402, all primary UNCERTAIN 643)`.
- Actual overlap: **NOT YET COMPUTED at this checkpoint**.
- Second review: **NOT STARTED**.

Keep the two cohorts analytically distinct: the frozen random cohort supports agreement/stability analysis; the UNCERTAIN cohort supports targeted uncertainty resolution. Calculate overlap before review. Do not compute one headline agreement statistic on the enriched union.

## Full text

Full-text retrieval/screening: **NOT STARTED**.

## Relation to PhD research gap

Completion of primary screening does **NOT** by itself change CURRENT_GAP **v0.8 refined**, which remains **provisional**. Evidence synthesis and full-text assessment are still pending.

Therefore, [research/CURRENT_GAP.md](CURRENT_GAP.md) remains unchanged, as does GAP_HISTORY.md. Screening counts are workflow information, not scientific evidence revising the gap. Provisional INCLUDE records have not been integrated into MASTER_INDEX as validated evidence by this checkpoint.

## Local data

Operational artifacts remain local under `artifacts/systematic-review-v1.0/`.

They are intentionally not committed because the repository is public and the local dataset contains record-level bibliographic metadata/abstracts from multiple databases. Public release requires a separate audit.

See [PRIMARY_SCREENING_CHECKPOINT_2026-09-20.md](systematic-review/PRIMARY_SCREENING_CHECKPOINT_2026-09-20.md) for the public checkpoint and its quality controls.

## Update 2026-09-29 — acquisition round 3 and synthesis plan

- Round 3 (author requests by e-mail, 25 letters sent 2026-09-28 from the researcher's Gmail by the AI on the researcher's instruction; log in `07_full_text/acquisition_round3/SENT_LETTERS_LOG_2026-09-28.csv`): **9** further full texts obtained (8 from authors, 1 arXiv preprint). Full texts now **290** of 509; **219** not retrieved.
- Tier 1 triage of the 9 (AI-assisted, `FULL_TEXT_TRIAGE_AI_FT_01_ROUND3.csv`): **4 INCLUDE** (CR001997, CR000430, CR001199, CR000550) / **5 EXCLUDE** (CR001186 FT1; CR001174, CR001767, CR002054, CR001060 FT2). Included studies now **125**.
- Tier 2 extraction of the 4 (AI-assisted, `FULL_TEXT_EXTRACTION_AI_EX_01_ROUND3.csv`, validated). CR001199 (Turkish, raw vs lemma under BM25 and dense mE5) is the closest study to the gap design; it reports aggregate comparisons only, no complementarity decomposition.
- Two related 2018 papers by El Mahdaouy et al. were sent by the author but were not identified by the database search; stored in `acquisition_round3/other_sources_not_in_search/`, not screened. Decision pending on "identification via other methods".
- Synthesis plan **frozen** 2026-09-29 (`08_publication/SYNTHESIS_PLAN_v1.0.md`, SHA-256 in `SYNTHESIS_PLAN_FREEZE_SHA256.txt`); written after extraction, before synthesis.
- Provenance: all stages AI-assisted; human verification sample issued 2026-09-28 (`09_human_verification/`), not yet returned.

## Update 2026-10-03 — dual full-text review, national search, new counts
Recorded with AI assistance (Claude).
- **Human verification of title/abstract screening.** The first author blind re-screened 150 records. Result: 0/75 false exclusions (95% CI 0–4.9%); all 38 disagreements were AI over-inclusions, and none reached the included set. See `09_human_verification/results_TA_2026-09-30`.
- **Full text (290).** Second reviewer U.M. Lutfullaev (PhD; ChatGPT-assisted, per his declaration). Agreement with the AI 92.4%, κ = 0.85. The first author adjudicated the 22 disagreements. Result: 113 studies (116 reports). See `07_full_text/final_disposition`.
- **National search (§9).** Two passes: a web subagent and a browser pass (Scholar, CyberLeninka, arXiv, OAK). 130 new records screened, 17 full texts sought; 1 study included (NR0002, Uzbek). See `10_national_search`.
- **Current totals.** 114 studies; dense 12; hybrid 2; Turkic 11; Uzbek 2. PRISMA counts: `08_publication/PRISMA_COUNTS_2026-10-03.md`; synthesis plan Amendment 2.
- **Pending.**
  - citation chasing (§6.4);
  - El Mahdaouy 2018 decision;
  - update of the manuscript draft numbers;
  - Tier 3 effect table (RQ1).

## Update 2026-10-03 (afternoon) — El Mahdaouy 2018 papers
Recorded with AI assistance (Claude).
- Both papers were reviewed independently by the AI (AI_FT_01, key written first) and the first author: full agreement. Included as **one study, AC0001 (2 reports)**, under "other methods (author contact)". See `07_full_text/acquisition_round3/other_sources_not_in_search/OTHER_SOURCES_FT_FINAL_2026-10-03.csv` and synthesis-plan Amendment 3.
- **Current totals.** 115 studies (119 reports); dense 12; hybrid 2; Turkic 11; Uzbek 2.
- **Pending.**
  - citation chasing (§6.4);
  - update of the manuscript draft numbers;
  - Tier 3 effect table (RQ1).
- AC0001 coding of per-query analysis (robustness index, PRF vs baseline) as QUANTITATIVE with scope SYSTEM_VS_SYSTEM was confirmed by the first author (codebook rule applied literally).

## Update 2026-10-03 (evening) — citation chasing (§6.4) started
Recorded with AI assistance (Claude).
- Seed set: 30 works (`11_citation_chasing/SEED_SET_2026-10-03.csv`), scope approved by the first author.
- Forward and backward via OpenAlex (queried from the researcher's Chrome), plus reference lists from 19 PDFs or publisher pages.
- Totals: 1,788 identified; 206 duplicates; 470 from before 2000; 1,112 screened by AI_CC_01. See `CITATION_CHASING_LOG_2026-10-03.md`.
- The first author's blind check is pending: `CITATION_CHASING_REVIEW_BLIND_2026-10-03.xlsx`, 165 rows.
- 4 closest works (Aboasal, GreekBarRetrieval, Munetsi, U-RR²) go straight to full-text assessment.
- **Time window (option A, 2026-10-03):** the 2000–2026 window is kept, now with an explicit rationale (CLEF 2000; TREC-2001 Arabic). A pre-specified pre-2000 sensitivity check was added (AMD-R24). Of 467 pre-2000 records, the AI advanced 44. Blind file for the first author: `11_citation_chasing/PRE2000_SENSITIVITY_REVIEW_BLIND_2026-10-03.xlsx` (56 rows).

## Update 2026-10-08 — citation chasing: the first author's blind check returned
Recorded with AI assistance (Claude).
- 164 rows were checked. The file the first author used did not include the late-added row CC0406.
- 2 records were not found (CC0238, CP0582). Under the codebook they are treated as UNCERTAIN/TA8 and advanced.
- Binary agreement (advance/exclude): 78.4%, κ 0.54. The κ depends on the sample design, because the sample was enriched with AI-advanced records.
- The first author excluded 33 records that the AI had advanced. Most of these decisions were based on reading the full text.
- In the random sample of 40 AI exclusions, the first author advanced 2:
  - CP0566 is a genuine AI miss (2.5%; 95% CI 0.4–12.9%);
  - CC0323 is a proceedings volume. Inside it the first author found a new candidate, Huang et al., CIKM 2013 (DSSM).
- Title/abstract rule: a record advances to full text if either reviewer advanced it. Result: 126 advanced, 38 excluded by both.
- Files: `11_citation_chasing/results_2026-10-08/`.
- **2026-10-08, decisions by the first author:**
  - **No second AI pass** over the 948 AI-excluded records that were not sampled. Report this as a limitation: the observed AI miss rate is 1/40 (2.5%; 95% CI 0.4–12.9%).
  - **The first author did the blind check himself, without AI assistance.** Record this in the AI-use declaration.
- **2026-10-08 (later):**
  - CC0406 was decided by the first author in chat: EXCLUDE TA2. The title/abstract stage of citation chasing is now complete: 126 records advance, 39 are excluded by both reviewers.
  - The first author declined author reminders for now.
  - The second full-text reviewer for the citation-chasing records is U.M. Lutfullaev.

## Update 2026-10-26 — citation chasing: AI full-text review
Recorded with AI assistance (Claude).
- **Full texts.** Available for 103 of the 131 records (first-author zip, plus 2 PDFs from Downloads); 28 are still missing.
- **AI review.** AI_FT_01 reviewed all 103 under the same frozen triage instructions as the database full texts: INCLUDE 50, EXCLUDE 51 (FT2 26, FT3 15, FT6 6, FT1 2, FT4 2), UNCERTAIN 2.
  - CC0200: the supplied file is slides, not the paper.
  - CP0357: open question whether Turkish TDT counts as retrieval; to be decided consistently with the included CR002158.
- **Linked to included studies:**
  - CC0028 → CR000561;
  - CC0177 → CR002216;
  - CC0248 → CR000452, CR000495, CR000504 and CP0603;
  - possible overlaps to check: CC0203 → CR000502; CC0176 → CR002198; CC0375 → CR000447; CP0500 → CR002215.
- **Files:** decisions in `11_citation_chasing/fulltext/_KEY_do_not_open_before_finishing/AI_FT_01_CC_ALL_2026-10-26.csv`; blind workbook for reviewer 2 in `11_citation_chasing/fulltext/CITATION_CHASING_FT_REVIEW_BLIND_R2_2026-10-26.xlsx` (103 rows).
- **Pre-2000 sensitivity check, title/abstract (2026-10-26).** The first author's blind check of 56 rows agreed with AI_CC_01 on 89.3% of decisions (κ 0.73).
  - Of the 12 AI exclusions in the sample (10 random plus Lovins and Dawson), the first author advanced none.
  - In 6 records the AI said UNCERTAIN and the first author said exclude: Porter 1980, Khoja 1999 and others.
  - Under the either-reviewer rule, 44 pre-2000 records advance to full text. Files: `11_citation_chasing/results_pre2000_2026-10-26/`.
- **Pre-2000 full texts (2026-10-26).** 17 of the 44 advanced records were obtained as open copies. AI_FT_01 reviewed them with the date ignored. Its decisions are sealed in the private data repository (`_KEY_do_not_open_before_finishing`) until reviewer 2 returns the blind workbook `11_citation_chasing/fulltext/pre2000/PRE2000_FT_REVIEW_BLIND_R2_2026-10-26.xlsx`. 27 records still have no full text.
  - *Redacted 2026-11-01:* an earlier unpushed draft of this paragraph named the AI decisions; they were moved to the private repository to keep reviewer 2 blind.
- **Citation chasing, full text, reviewer 2 (2026-10-26).** U.M. Lutfullaev returned 103 rows: 54 include, 45 exclude, 4 wrong file.
  - Against AI_FT_01: 86/98 decided records agree (87.8%), κ 0.76 (95% CI 0.62–0.88).
  - 17 records need adjudication: 12 include/exclude disagreements, 4 wrong files, CP0357. Another 9 differ only in the exclusion code.
  - 8 of the disagreements concern subword indexing units in Chinese or speech retrieval (characters, syllables, phones, letter trigrams). This needs a rule decision.
  - Adjudication workbook: `11_citation_chasing/fulltext/CC_FT_DISAGREEMENTS_FOR_ADJUDICATION_2026-10-26.xlsx`.

## Update 2026-11-01 — adjudication in progress; project moved to a new computer
Recorded with AI assistance (Claude).
- **Adjudication of citation-chasing full-text disagreements (first author), 2026-10-26.** Two of four steps are done. The decisions are in the private log `11_citation_chasing/fulltext/results_2026-10-26/FIRSTAUTHOR_ADJUDICATION_LOG_2026-10-26.csv` (15 lines).
  - **Step 1 — RULE-CC-01:** subword indexing units (characters, syllables, phones, letter n-grams) count as a morphological intervention (gate B) only when used to handle word-form variation. Chinese character/syllable units and speech subword units for segmentation, ASR or OOV are FT2. Applied to 8 records: 7 EXCLUDE FT2, 1 INCLUDE (CCN001, DSSM letter trigrams, weak evidence).
  - **Step 2:** 5 records excluded in agreement with reviewer 2 (CC0008 FT2, CC0177 FT2, CP0279 FT2, CP0505 FT1, CP0357 FT1).
  - **Step 3 (next):** 4 records where reviewer 2 found the wrong file (CC0030, CC0145, CC0200, CP0501). The correct texts must be obtained; if they cannot be obtained, code FT7.
  - **Step 4:** 9 records where both reviewers excluded and only the exclusion code differs.
- **Where the data lives.** Record-level data is in the private repository `Shoxrux2017/phd-uzbek-hybrid-retrieval-data`, cloned into `artifacts/`. Copyrighted full texts (PDF/PS) and large corpora are not in any repository; they were moved by an offline archive (see `HANDOFF.md`). This supersedes the "Local data" section above.
- **Handoff:** `HANDOFF.md` (public, how to resume) and `artifacts/HANDOFF_PRIVATE_2026-11-01.md` (private, record-level next steps).

## Update 2026-11-02 — citation chasing complete; extraction; Clarification 002; pre-2000 check
Recorded with AI assistance (Claude). Record-level files are in the private repository (`artifacts/`), commits `c1f5756` and `1b3f4bf`.
- **Adjudication finished (first author).**
  - Step 3: CC0200 — the open CLEF 2001 Working Notes version was accepted as the full text and re-reviewed by AI_FT_01 and reviewer 2 (both: include). CC0030, CC0145, CP0501 — FT7 (only wrong files/slides obtainable).
  - Step 4: the 9 code-only differences were resolved by the first-failed-gate rule.
- **Citation-chasing result.** 127 reports sought; 27 not retrieved; 100 assessed; 52 excluded (FT1 4, FT2 28, FT3 15, FT6 5); **48 included = 43 new studies + 5 additional reports** of included studies (CC0028→CR000561; CC0176→CR002198; CC0203→CR000502; CC0375→CR000447; CC0248→CR000452/CR000495/CR000504/CP0603). Linkage was checked against tables and numbers (`LINKAGE_CHECK_2026-11-02.md`).
- **Merge found during the linkage check:** CR000688 and CR002185 report the same study (identical tables); CR000688 retained. Database arm: **112 studies**.
- **Extraction** (AI_EX_01, 60 fields, codebook v1.0) of the 43 new studies; blind retest of 5 (AI_EX_RT): core fields 65/65 (100%), all 38 categorical fields 88.9%.
- **Extraction Clarification 002** (post hoc, first author): query-time conflation scored as one term (#syn, synonym sets, equivalence classes) counts as the corresponding representation; separate-term query expansion does not (explicitly including FCG grouped with #syn and Boolean OR/truncation). An AI audit of all 58 studies with query-side processing recoded 9 studies and flagged 7 as mechanism unclear; all changes are logged.
- **Current totals: 157 studies (167 reports).** Dense channel 15; lexical+dense hybrid 2; Turkic 16; Uzbek 2; per-query quantitative analysis 57; unique-hit analysis 2; channel overlap 1; oracle/upper bound 6. Files: `08_publication/PRISMA_COUNTS_2026-11-02.md`, `DESCRIPTIVE_COUNTS_2026-11-02.json`, `07_full_text/extraction/FULL_TEXT_EXTRACTION_FINAL_INCLUDED_2026-11-02.csv`.
- **Pre-2000 sensitivity check (AMD-R24).** Full text of 17 open copies: AI_FT_01 vs reviewer 2 16/17 (94.1%, κ 0.88); PRE0249 adjudicated EXCLUDE FT2. **8 eligible-except-date studies** extracted; draft supplementary table `08_publication/PRE2000_SENSITIVITY_TABLE_2026-11-02.md`. 27 pre-2000 records still without full text. The narrative comparison with RQ1 waits for the Tier 3 effect table.
- **This does not revise CURRENT_GAP v0.8 refined**: no new study reports lexical↔dense complementarity decomposition.
- **Pending.**
  - 4 §23 closest works (no full texts yet);
  - reviewer 2 declaration for the citation-chasing, CC0200 and pre-2000 rounds;
  - RoB table, certainty, gap-killer audit;
  - Tier 3 effect table (RQ1) and synthesis;
  - manuscript numbers; update search (§24) before submission.

## Update 2026-11-03 — Tier 3 effect table (RQ1) built and verified
Recorded with AI assistance (Claude). Record-level files are in the private repository (`artifacts/systematic-review-v1.0/07_full_text/tier3_effects/`; check workbook in `09_human_verification/tier3_effects/`).
- **Reviewer 2 declaration** for the citation-chasing, CC0200 and pre-2000 rounds recorded (`11_citation_chasing/fulltext/results_2026-11-02/REVIEWER_2_DECLARATION_2026-11-02.md`), with an addendum to the 290-round declaration.
- **Closest works (§23):** 3 of 4 full texts obtained (U-RR² not retrievable, FT7); AI_FT_01 and reviewer 2 (blind) both INCLUDE all 3 (CW_ABOASAL, Arabic legal; CW_GREEKBAR, Greek statutes; CW_MUNETSI, Shona — borderline: morphology only through a qualitative error analysis, which criterion B lists). Extracted (AI_EX_01; blind retest of CW_ABOASAL 37/38 fields, core 13/13). **Totals: 160 studies (170 reports)**; dense channel 18; hybrid 4; 38 languages (`PRISMA_COUNTS_2026-11-03.md`, `DESCRIPTIVE_COUNTS_2026-11-03.json`, `FULL_TEXT_EXTRACTION_FINAL_INCLUDED_2026-11-03.csv`).
- **Amendment 4** (counts after citation chasing; operational rules B1–B6 for the effect table) agreed by the first author on 2026-11-03, 13:51 (UTC+5), before any row was built.
- **Effect table** `EFFECT_COMPARISONS_2026-11-03.csv`: 135 studies with ≥ 2 representations, 517 rows (509 comparisons from 127 studies; 8 studies without an eligible pair); the 2 closest works with a representation comparison were added as batch EF12 (4 rows, all verified OK).
  - Extraction by AI_EF_01 (11 batches); independent verification of every row against page images by AI_EF_VER.
  - Verification: 466 of 512 rows (91.0%) without finding; 5 value errors, none in an effect value; 41 rows departed from the written rules and were corrected; 1 missing row added. Effect values changed in 20 rows, direction in 2.
  - Every change is logged (`TIER3_CORRECTIONS_LOG_2026-11-03.csv`); report `TIER3_VERIFICATION_REPORT_2026-11-03.md`.
- **First-author decision (option a):** the lemma run without compound splitting is used where one exists; 34 rows tagged DECOMPOUNDING_IN_LEMMA for a sensitivity analysis; CP0603–CR000491 added as a §3 rule 6 overlap pair.
- Rule applications beyond §3 / Amendment 4 B are recorded as an **addendum to Amendment 4** (`08_publication/SYNTHESIS_PLAN_AMENDMENTS.md`).
- **This does not revise CURRENT_GAP v0.8 refined**: the closest works report aggregate lexical, dense and RRF-hybrid scores; CW_MUNETSI discusses qualitatively that BM25 fails on differing word forms where dense models are partly robust, but no study decomposes lexical↔dense complementarity (unique hits, overlap, per-query wins).
- **Pending.**
  - researcher check of a random 20% of the effect rows (103 rows) → error rate;
  - reviewer 2 declaration for the closest-works round;
  - RoB table, certainty, gap-killer audit;
  - RQ1 synthesis (vote counting, SWiM, sensitivity analyses) and the pre-2000 narrative comparison;
  - manuscript numbers; update search (§24) before submission.

## Update 2026-11-05 — researcher check of the effect table and revision
Recorded with AI assistance (Claude). Files in the private repository: `07_full_text/tier3_effects/` (`EFFECT_COMPARISONS_2026-11-05.csv`,
`TIER3_VERIFICATION_REPORT_2026-11-05.md` §11, `TIER3_REVISION_LOG_2026-11-05.csv`, `revision_2026-11-05/`) and
`09_human_verification/tier3_effects/`.
- **Researcher check (§3 rule 7)** of the random 20% sample: all 103 rows checked; numbers 103/103 correct; **1 error (1.0%, 95% CI
  0.2–5.3%)**, a significance code (CC0412); 18 rows (17.5%) with doubts about the choice rules. AI assistance in this check: to be stated.
- **First-author decisions A1–A6, B7–B11** (2026-11-05): options chosen by score are not MAIN; variants with an extra intervention are
  excluded when a clean one exists; runs on another collection version leave the pools; single n-gram "stemming" = STEM; Khoja in
  CR002173 = MORPHEME; baseline = the light-normalised raw run the processed runs are built on; new flag EXTRA_OPERATION (21 rows).
- **Revision:** 15 studies re-extracted and re-verified on page images (no value errors in revised values); table now **519 rows**
  (135 studies); effect values changed in 45 rows; **13 directions changed** (7 in CP0566 after moving to the clean post-lem variant).
  Tier 2: CR002173 morpheme = YES (morpheme studies 32).
- **This does not revise CURRENT_GAP v0.8 refined.**
- **Pending:** AI-assistance statement for the researcher check; reviewer-2 declaration for the closest-works round; RoB, certainty;
  RQ1 synthesis and pre-2000 comparison; manuscript numbers; update search.

## Update 2026-11-05 (afternoon) — RQ1–RQ3 synthesis
Recorded with AI assistance (Claude). Files: `08_publication/synthesis_rq1/` and `08_publication/synthesis_rq2_rq3/` (private repository);
each analysis follows a specification written and saved before the numbers were computed.
- **RQ1 (SWiM vote counting, monolingual, unit = study × language × pair).** Every processed representation beats raw text in most units:
  stem 93% of decisive votes (123 + / 9 −; median +14%), lemma 87% (+19%), morpheme 84% (+10%), subword 78% (+15%). Gains are largest for
  agglutinative and root-and-pattern languages (stem +26% / +28%; lemma +37% and subword +57% in the agglutinative group) and smallest for
  English. Stem vs lemma: no consistent direction (22 / 19; median +0.3%). Robust in all nine sensitivity analyses; weaker in studies since
  2020 (stem 9 / 3, median +2.8%); CLIR inconsistent. Turkic studies all favour stemming; the Uzbek study: stem +20%, lemma +26%.
- **RQ2 (18 dense/hybrid studies; 13 neural, 5 latent).** Morphology-aware lexical vs off-the-shelf dense: dense better in 5, lexical
  better in 2, not comparable in 6; 4 hybrids (better than both components in 1). Morphology inside the dense channel: preprocessed input in
  4 neural studies, never built into the model.
- **RQ3 (160 studies).** Unique hits 2 studies, channel overlap 1, oracle 6 — all lexical–lexical or dense–dense; none of the 11
  lexical–dense studies reports per-query numbers, unique hits, overlap or an oracle. **Consistent with CURRENT_GAP v0.8 refined; not revised.**
- **Pending:** RQ4 (risk-of-bias summary, evaluation practice, Turkic/Uzbek narrative), certainty statements, pre-2000 comparison,
  manuscript text and numbers, AI-assistance statement for the researcher check, reviewer-2 declaration (closest works), update search.

## Update 2026-11-05 (evening) — RQ4 synthesis
Recorded with AI assistance (Claude). Files: `08_publication/synthesis_rq4/` (private repository); the specification was saved before the
RQ4 numbers were computed (RQ1–RQ3 were already known, which the specification states).
- **Risk of bias (160 studies; no overall score).** HIGH: qrels validity 17%, baseline fairness 5%, tuning fairness 13%, reporting
  completeness 12%; 59 studies (37%) HIGH in at least one domain; 9 (6%) LOW in all four. Reporting is the weakest domain (some concerns 64%).
- **Evaluation practice.** Qrels from a shared benchmark 56%, built for the study 26%, not reported 11%; pool depth not stated 65%;
  no significance test for the representation/channel comparison 49% (74% of studies since 2020); median 50 queries (181.5 since 2020);
  code stated as available 9% (37% since 2020), data 18%.
- **Turkic and Uzbek (16 studies, 2 Uzbek).** All 11 Turkic RAW→STEM units favour stemming; stem vs lemma splits 2 / 2 among the four
  Turkic studies with both; dense channels in 3 (CR000481, CR001199, CC0402), no Turkic hybrid. Transferability rests on typology.
- **Certainty (§9, descriptive; accepted by the first author 2026-11-05 13:09 with two additions: agglutinative stemming gain median +25.9%;
  6 of the 11 Turkic studies share the Milliyet collection).** Strongest: RAW→STEM (84 studies, 93% favourable, robust, 11 Turkic
  studies); RAW→LEMMA consistent but size partly from compound splitting; RAW→MORPHEME and RAW→SUBWORD indirect for Uzbek (no Turkic study);
  STEM→LEMMA undecided, also for Uzbek.
- **Gap-killer audit (CURRENT_GAP conditions 1–3).** Raw vs stem/lemma 109 studies → with a dense channel 9 → with a hybrid 2 → several
  lexical variants fused with the same dense model 0 → lexical–dense unique hits/overlap/oracle 0. **CURRENT_GAP v0.8 refined is not revised.**
- **Pending:** first-author acceptance of the certainty wording; pre-2000 comparison; figures and manuscript text and numbers;
  AI-assistance statement for the researcher check; reviewer-2 declaration (closest works); update search (§24), which repeats the audit.

## Update 2026-11-05 (evening) — pre-2000 sensitivity check (AMD-R24)
Recorded with AI assistance (Claude). Files: `08_publication/synthesis_pre2000/` (private repository); specification saved before the
comparison; replaces the informal draft table of 2026-11-02.
- **Effect rows** for the 8 eligible-except-date studies built with the Tier 3 rules (21 rows; Xu & Croft 1998 has no raw baseline) and
  checked by an independent AI verifier on the page images: all numbers correct; 11 rows corrected (mainly Krovetz 1993: the author's
  algorithm "deriv" is MAIN; one STEM→LEMMA direction 0 → −), 1 row added (Cleverdon 1966, 1400 documents, not determinable).
- **Votes (9 units):** RAW→STEM 5 + / 1 − (English small gains, Italian +128%, Dutch Porter index −3.3% n.s.); RAW→LEMMA 1 +; STEM→LEMMA 1 −;
  RAW→SUBWORD 1 + (figure). **No RQ1 conclusion would change** (what-if only; main counts unchanged).
- **Per-query analyses** (Harman 1987; Jing & Tzoukermann 1999; Kraaij & Pohlmann 1996; Xu & Croft 1998): stemming helps some queries and
  hurts others — documented since 1987, lexical–lexical only. **CURRENT_GAP v0.8 refined is not revised.**
- **Limitation:** mostly English, no agglutinative or root-and-pattern language; the 27 records not retrieved include 9 Arabic studies and
  the only Turkish one (PRE0225, 1994), so the check adds no evidence for agglutinative languages or Uzbek.
- **Accepted by the first author:** RQ4 certainty wording (2026-11-05 13:09) and the pre-2000 comparison text (13:13, one change).
- **Pending:** figures; manuscript text and numbers;
  AI-assistance statement for the researcher check; reviewer-2 declaration (closest works); missing texts; update search (§24).

## Update 2026-11-05 (evening) — figures and tables for the manuscript
Recorded with AI assistance (Claude). Files: `08_publication/figures/` (private repository), list and draft captions in
`FIGURES_AND_TABLES_PLAN_2026-11-05.md`. Built at journal size (12.7–14 cm wide, PDF + 600 dpi PNG): Fig. 1 PRISMA 2020 flow (160 studies,
170 reports), Fig. 2 studies by year and channel, Fig. 3 RQ1 effect direction, Fig. 4 RQ3 evidence map, Fig. 5 RoB summary, Fig. S1 RoB
per study; tables: neural dense/hybrid studies (13), Turkic and Uzbek studies (16), characteristics of the 160 studies (supplement).
- **Found missing:** the characterisation of the reports not retrieved (FT7), required by SYNTHESIS_PLAN §10, has not been done.
- **Done 2026-11-05 (evening):** FT7 characterisation (`08_publication/ft7_characterisation/`; specification saved before computing).
  Database arm, 218 not retrieved vs 291 retrieved: IEEE Xplore-only 69% vs 31% (access, not content); title/abstract label and neural
  vocabulary balanced; at the same inclusion rate about 84 would have been included (116 included). 32 not-retrieved reports from 2020
  onwards use neural vocabulary, incl. two Turkish RAG/embedding studies (CR001149, CR001170) and an Uzbek one (CR001179); 14 not-retrieved
  reports across all arms mention a Turkic language. RQ3 holds for the retrieved literature only. Interpretation: draft for the first author.
- **Academia.edu e-mail check (2026-11-05, first author's request):** 630 notification e-mails read through the Gmail connector;
  239 distinct papers: 19 already in the review (7 included, 12 excluded at full text), none of the FT7 reports, no new eligible study
  (`13_other_sources/academia_emails_2026-11-05/`). PRISMA counts unchanged.
- **Pending:** first-author acceptance of the FT7 interpretation; obtaining priority FT7 reports (2020+ neural, Turkic); reference column of Table S1; PRISMA checklist; manuscript text and numbers; AI-assistance statement
  for the researcher check; reviewer-2 declaration (closest works); missing texts; update search (§24).
