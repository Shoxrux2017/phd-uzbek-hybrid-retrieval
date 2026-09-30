# PROTOCOL COMPLIANCE AUDIT — systematic review v1.0 against ARTICLE_RESEARCH_PROTOCOL_v1.0_FROZEN

Audit date: 2026-09-30. Prepared with AI assistance (Claude) for the researcher; nothing here has been approved yet.
Frozen protocol: `research/systematic-review/protocol/ARTICLE_RESEARCH_PROTOCOL_v1.0_FROZEN.md`. Its freeze time is 2026-09-17 19:09:01 UTC+05:00 (14:09:01 UTC), taken from `CHAT_TIMESTAMPS.md`.
Evidence examined: the files listed in §7 of this audit. Everything else is marked **unknown** / **undocumented**. No value in this audit was inferred from memory.

Path abbreviations: `SR/` = `/mnt/user-data/uploads/phd-uzbek-hybrid-retrieval/artifacts/systematic-review-v1.0/`; `RS/` = `/mnt/user-data/uploads/phd-uzbek-hybrid-retrieval/research/`; `HC/` = `/home/claude/`.

---

## 0. Summary

| Status | Rows | Protocol sections |
|---|---:|---|
| COMPLIED | 4 | §5, §14, §15, §16.1 |
| DEVIATION | 11 | §0, §3, §6.1–6.3/6.5, §7–8, §10+§12, §16.2, §16.3, §18, §19, §20, §32 |
| NOT YET DONE (repairable before submission) | 11 | §4, §6.4, §9, §11, §13, §17, §21, §22, §23, §24, §26 |
| NOT DONE (cannot be repaired) | 1 | §25 (no contemporaneous amendment log; a retrospective log only mitigates) |
| **Total rows** | **27** | Sections §6 and §16 are split because their parts have different statuses. |

**Chronology conclusion.** Every canonical dataset that entered the review was produced on 2026-09-18, after the freeze. These are EBSCO ASP/STC/LISTA (10:03–10:16 +05), PQDT (10:41–10:45 +05), IEEE (13:35–13:39 +05) and the ACL canonical export (18 Sep, time not recorded). No canonical export predates the freeze. Only the query-development pilots (16–17 Sep) did, and they are the origin of the frozen strategies. The single qualification is ACL: its canonical file is a byte-identical deterministic regeneration of pilot hit files computed on 17 Sep, and the clock time of that computation is not recorded.

**The most consequential gaps** are five:
1. There is no amendment log (§25), although at least 20 post-freeze changes exist (see `PROTOCOL_AMENDMENT_LOG_DRAFT.md`).
2. Reviewer reliability falls short of §16.3. Full text had a single AI pass plus a 10% retest, and 194 records entered full text on one AI pass.
3. The review questions were reduced from 6 to 4, and the evidence ladder (§13), the ten-domain appraisal (§19) and the morphology × paradigm and language matrices (§20.2–20.3) are all missing.
4. The national Uzbek searches (§9), supplementary discovery/citation chaining (§6.4) and the contextual layer (§11) have not been done. As a result RQ6 cannot be answered as the protocol specifies.
5. For the closest-work set (§23): three families have no record in the corpus (GreekBarRetrieval, Aboasal et al., the Uzbek USHRA/O-RAG/Urinov/Sharifbaev works), and two priority records were never retrieved (Korean CR000873 and Amharic CR001059).

---

## 1. Chronology of search and export events

Times are given as printed in the source, followed by a conversion. The reference zone is Asia/Tashkent (UTC+05:00, no DST).

| # | Date–time (UTC+05) | UTC | Source / event | Pilot vs canonical | Count | Evidence |
|---|---|---|---|---|---:|---|
| a | 2026-09-10 | – | Gap-killer literature search (project, pre-protocol) | Not a review search | – | `RS/CURRENT_GAP.md` |
| b | 2026-09-11 → 14 | – | National Uzbek deep dives (Bakaev … Urinov, USHRA, O-RAG) | Not a review search; no dated search log | – | `PROJECT_STATE.md` |
| c | 2026-09-16 11:19 → 20:02 | 06:19 → 15:02 | Protocol v0.1 → v0.9 | – | – | `CHAT_TIMESTAMPS.md` |
| d | 2026-09-16, time unrecorded | ? | EBSCO S4 "exact tested" (`S4_EXACT_TESTED_2026-09-16.txt`) | PILOT (query development) | 527 | EBSCO manifests |
| e | 2026-09-16 18:43 | 13:43 | PQDT P2 = Search History S6 (P1 = S1) | PILOT | 126 | `PQDT_P2_RAW_EXPORT_MANIFEST.md` |
| f | date/time not in available files | ? | IEEE I1 pilot (first-50 native CSV/RIS, `audit/IEEE-I1-first50-native.*`) | PILOT | 1,256 | IEEE manifest; `IEEE_I1_QUERY_PROVENANCE.md` not in upload |
| g | 2026-09-17, time unrecorded | ? | EBSCO S4-clean check (not validated; not used) | PILOT | – | protocol §6.1; EBSCO manifest |
| h | 2026-09-17, time unrecorded | ? | ACL A1/A2R pilot on snapshot `f27fde6…` | PILOT (becomes canonical content, see q) | A1 83; A2R 255 | ACL manifest ("search date (frozen pilot) = 2026-09-17") |
| i | 2026-09-17 10:08 | 05:08 | Protocol v0.11 | – | – | `CHAT_TIMESTAMPS.md` |
| **F** | **2026-09-17 19:09:01** | **14:09:01** | **PROTOCOL v1.0 FROZEN** | – | – | `CHAT_TIMESTAMPS.md` |
| j | 2026-09-17 19:47:49 | 14:47:49 | EBSCO combined S4 search (ASP+STC+LISTA jointly) | Post-freeze, **NON-CANONICAL** | 527 header | `EBSCO_S4_RAW_EXPORT_MANIFEST.md`, `EXPORT_SESSION_EVIDENCE.json` |
| k | 2026-09-17 19:49:32 → 20:14:16 | 14:49 → 15:14 | EBSCO combined batches: RIS 1–250, CSV 1–200, plus 3 repeated-range technical attempts | NON-CANONICAL | 250 / 200 | same |
| l | 2026-09-17 ≈20:17 | ≈15:17 | EBSCO institutional session expired | – | – | same |
| m | 2026-09-17 21:32:01 → 21:41:23 | 16:32 → 16:41 | EBSCO resume: count re-confirmed 527; UI ends at "323 unique"; technical attempt 251–300 (21:33:37) | NON-CANONICAL | 50 | same |
| n | 2026-09-18, before 10:03, time unrecorded | ? | EBSCO per-database attempts stopped at personal sign-in; no files | – | 0 | per-database manifest, `audit_history/` |
| o1 | 2026-09-18 10:03:11 (CSV 10:05:48; RIS 10:06:51) | 05:03 | EBSCO Academic Search Premier, S4 | **CANONICAL** | 268 | `EBSCO_PER_DATABASE_EXPORT_MANIFEST.md` |
| o2 | 2026-09-18 10:08:39 (CSV 10:10:34; RIS 10:11:27) | 05:08 | EBSCO Science & Technology Collection, S4 | **CANONICAL** | 126 | same |
| o3 | 2026-09-18 10:12:58 (CSV 10:14:36; RIS 10:16:27); query check 10:18:47 | 05:12 | EBSCO LISTA, S4 | **CANONICAL** | 133 | same; `EXACT_QUERY_VERIFICATION_2026-09-18.json` |
| p | 2026-09-18 10:41:44 (RIS 10:43:56; XLS 10:45:17) | 05:41:44 | PQDT P2 (fresh session S1 = P2) | **CANONICAL** | 126 | PQDT manifest |
| q | 2026-09-18, time unrecorded ("Asia/Tashkent") | ? | ACL canonical export A1 ∪ A2R (∩ 23), regenerated deterministically from pinned snapshot plus frozen pilot hit files; byte-identical second run | **CANONICAL** | 315 | ACL manifest |
| r1 | 2026-09-18 13:35:06 (count); partition 2000–2019 export 13:35:53, file 13:36:09 | 08:35 | IEEE I1 | **CANONICAL** | 1,256 (792) | `IEEE_I1_RAW_EXPORT_MANIFEST.md`, `IEEE_I1_EXPORT_SESSION.json` |
| r2 | 2026-09-18 13:39:16 (count); export 13:39:22, file 13:39:35 | 08:39 | IEEE I1, partition 2020–2026 | **CANONICAL** | 464 | same |
| s | 2026-09-28 / 29 (date of receipt not exact) | – | Two El Mahdaouy et al. 2018 papers sent by an author, not found by the search | Supplementary ("other sources"); held unscreened | 2 | `RS/SYSTEMATIC_REVIEW_STATE.md` (2026-09-29 update) |
| t | – | – | National EN/RU/UZ searches (§9), citation chaining (§6.4), update search (§24) | **Not performed** | – | none found |

Merged master (for orientation, not a search event): 2,224 raw records → 2,010 after deduplication. It was built from o1–o3, p, q, r1 and r2 only; the old combined EBSCO batches j–m are explicitly not read (`MASTER_MERGE_DEDUP_MANIFEST.md`).

### 1.1 Freeze placement: conclusion

- **Produced after the freeze (all canonical):** the three EBSCO per-database sets (o1–o3), PQDT (p), IEEE (r1, r2) and the ACL canonical files (q). All date from 2026-09-18, 15–18.5 hours after the freeze.
- **Produced before the freeze:** no canonical dataset. What predates the freeze are the query-development pilots (d–h). These fixed the strategies and baseline counts, and the frozen protocol reports them as such. The canonical counts equal the pilot counts: 527, 126, 1,256, 83/255.
- **Qualification (ACL):** the canonical ACL data are not a new search. They re-read "frozen unscreened hit files" from the 17 Sep pilot and recompute them from the pinned snapshot, with byte-identical results. Because the snapshot is pinned, the content does not depend on when the search ran. Whether the pilot hit files were written before or after 19:09 on 17 Sep is **undocumented**.
- **First post-freeze search** (j, 19:47:49 +05) came 38 minutes after the freeze. It produced only non-canonical partial files.
- The CHAT_TIMESTAMPS note itself says the freeze did not precede all search activity (16–17 Sep pilots). The Methods text should therefore say "strategies frozen after piloting; all final exports run after the freeze". It should not say "protocol frozen before any search".

### 1.2 Time-zone pitfalls

1. **The freeze time exists in two notations.** It is 19:09:01 +05 = 14:09:01 UTC, and the protocol header gives only the date. If 19:09 were read as UTC (00:09 +05 on 18 Sep), the 17-Sep EBSCO combined search (19:47 +05 = 14:47 UTC) would falsely appear to precede the freeze.
2. **The PQDT pilot time is in UTC** (13:43 UTC = 18:43 +05 on 16 Sep), but the PQDT canonical time is given in both zones. Do not compare the pilot "13:43" directly with +05 times.
3. **IEEE native download filenames** (`export2026.09.18-04.36.04.csv`, `…04.39.29.csv`) use another zone: 04:36 corresponds to 13:36 +05, which is UTC−4 (probably US Eastern). The manifest correctly does not use them as search times. Any audit that reads them as local time would place IEEE before EBSCO.
4. **EBSCO filenames** (`EBSCO-Export-09_17_2026…`) carry a local MM_DD_YYYY date without a time. EBSCO download times are filesystem LastWriteTime values; they are not server time.
5. **Several events are date-only:** ACL pilot and canonical, S4 test and S4-clean, the IEEE pilot, and the per-database failed attempts. These cannot be ordered relative to 19:09 on 17 Sep.
6. **Uzbekistan has no DST**, so +05 is constant. Anthology and IEEE metadata years are unaffected.
7. **Recommendation.** Report every search date in the Methods as "YYYY-MM-DD (UTC+05)", and keep UTC equivalents in Supplementary S1.

---

## 2. Section-by-section compliance

Legend: **C** = COMPLIED; **DEV** = DEVIATION; **NYD** = NOT YET DONE (still possible before submission); **ND** = NOT DONE (cannot be repaired).
Decision dates are taken from file headers. A change that no file announces is marked "undocumented".

| § | Operative requirement | Status | What was done / what differs | Decided / documented where |
|---|---|---|---|---|
| **0** | Strategies not silently changed; raw exports immutable; every deviation dated and documented; Scopus/WoS only by amendment; update search; no strengthened absence claims | **DEV** | Raw exports are preserved with SHA-256 (C). Scopus/WoS were not added (C). But several post-freeze changes were adopted without an amendment: EBSCO joint → per-database, the PQDT string reconstruction, FT codes, reviewer-reliability design, extraction schema, RoB domains and RQs. No dated deviation log exists. The absence observation in `SYSTEMATIC_REVIEW_STATE.md` 2026-09-28 ("no included study reports … decomposition") is qualified as descriptive, but it is not bounded by the 219 FT7 records or the unsearched national and closest-work sources. | Changes are scattered across stage manifests (2026-09-18 → 29). No §25 log. |
| **3** | RQ1–RQ6 | **DEV** | Synthesis plan v1.0 has 4 RQs (see §3 of this audit). Protocol RQ2 (efficiency, index/vocabulary size, composition of retrieved relevant documents) is only partly covered, through the headline metric. RQ3's five control checks (retrieval-trained comparator, same dense model, fixed dense preprocessing, controlled fusion, morphology isolated) are not specified. RQ5 is reduced to 4 RoB domains. RQ6 (Uzbek boundary across 7 evidence types) is reduced to a Turkic/Uzbek narrative over 11 Turkic studies, 1 of them Uzbek. The plan does not mention the protocol RQs. | `08_publication/SYNTHESIS_PLAN_v1.0.md`, frozen 2026-09-29. Not logged as an amendment. |
| **4** | PRISMA 2020 + PRISMA-S; flow with all listed boxes | **NYD** | Title/abstract flow exists (`06_final_disposition/PRISMA_TITLE_ABSTRACT_FLOW.md`), and full-text counts can be derived: sought 509, not retrieved 219, assessed 290, excluded 165 by code, included 125. Missing: the "other methods" arm (the 2 El Mahdaouy papers, and any national or chaining records), the final flow diagram, and the PRISMA-S checklist. `PRISMA_IDENTIFICATION_COUNTS.json` is quoted in `MASTER_DEDUP_FINAL_MANIFEST.md`, but the file itself is absent from the upload. | – |
| **5** | 2000-01-01 → 2026-12-31 | **C** | Date limits were applied in every source (EBSCO `DT1:2000-01-01/2026-12-31`; PQDT 01.01.2000–31.12.2026; IEEE 2000–2026; ACL 2000–2026). The completeness of 2026 depends on §24. | Source manifests |
| **6.1–6.3, 6.5** | EBSCO: ASP+STC+LISTA searched **jointly** with exact S4; IEEE I1; ACL A1/A2R; PQDT P2; ACM supplementary only; Scopus/WoS optional | **DEV** | EBSCO was re-run **separately in each database** (268+126+133 = 527). The reason was that the joint export exposed only 323/527 records and its order drifted. The logic and settings are unchanged, and the old joint files are non-canonical. IEEE, ACL and PQDT were run as frozen (PQDT caveat in §7–8). ACM and Crossref were not used; this is permitted. | Per-database manifest 2026-09-18, which calls it "this amendment". No amendment entry. |
| **6.4** | Supplementary discovery (SciSpace, Scholar forward chaining, publisher pages, repositories, national sources, backward/forward chaining, references of included studies and closest reviews) with provenance | **NYD** | No chaining or supplementary search was performed. Two author-supplied papers are held unscreened (`acquisition_round3/other_sources_not_in_search/`, a folder not in the upload). The `CONTEXT_REVIEW` flag was introduced "for citation chasing" (FT-CLAR-001), but no chasing followed. | `SYSTEMATIC_REVIEW_STATE.md` 2026-09-29: "Decision pending" |
| **7–8** | Conceptual blocks; exact source strings (S4 artifact wins; "use the archived exact P2 string"); IEEE All Metadata 2000–2026; ACL A1/A2R rules | **DEV** (minor) | S4 was byte-checked against its artifact (SHA `61bf92…`, 1,246 chars). I1 matched its artifact. ACL used the frozen A2R pattern on the pinned snapshot. **PQDT:** `PQDT_P2_EXACT_QUERY_2026-09-16.txt` was unavailable. P2 was instead rebuilt from the quoted P1 string plus the two recorded `lemmat[*10]` substitutions. The count is unchanged (126) and the documentary derivation is recorded, but byte identity is unverified. A known-item retention check was reported for IEEE (7/7), PQDT (7/7) and ACL (4/4), but not for EBSCO. | PQDT manifest 2026-09-18 |
| **9** | Separate national Uzbek searches in EN/RU/UZ, with apostrophe variants | **NYD** | No search strings, dates, sources or counts were found in any review artifact. The national deep dives of 11–14 Sep predate the protocol and are not a documented systematic search. | – |
| **10 + 12** | Eligibility conditions 1–7; exclusion list | **DEV** | Conditions 1–3 and 5–7 were applied through the T/A codebook, Clarifications 001/002 and the FT codebook. **Condition 4** ("language whose morphological or low-resource characteristics are relevant", E3) was never operationalised. The FT codebook has no language-relevance code, and **21 included studies are METHODOLOGICAL_ONLY** (English- or Chinese-only; e.g., CR000248, CR000503, CR000604, CR002102, CR002218). Condition 5 requires preprints to sit in a clearly marked provisional tier; there is 1 PREPRINT among the 125 and no tier flag. Surveys were excluded as FT6 by FT-CLAR-001 (2026-09-27). This is consistent with "primary source" but not written in the FT codebook. | Undocumented for condition 4. FT-CLAR-001 in `HC/triage/TRIAGE_INSTRUCTIONS.md`. |
| **11** | Contextual evidence layer kept separately (not pooled) | **NYD** | No contextual layer exists. Morphology resources and search infrastructure without IR evaluation were simply excluded (TA3/FT3). So were lexical-vs-dense work in MRLs where morphology is only motivational, e.g. CR000477, CR000226, CR000239, CR000220 (FT2). Only surveys carry a `CONTEXT_REVIEW` note. | – |
| **13** | Evidence level 0–5 per retained work | **NYD** | Not extracted, and absent from the synthesis plan. It can be derived deterministically for L1–L3 and L5 (see §4 of this audit and the appendix). L4 needs two fields the schema lacks: "same dense model across morphology variants" and "fusion held constant/controlled". These must be read for the 4 hybrid studies (CR000103, CR000108, CR000448, CR000913). L0 applies only to the missing contextual layer. A rule is needed on whether LSI/LDA/LSA count as "semantic/dense" (4 studies). Tentative levels: L1 110, L2 10 (4 latent, 3 without a lexical channel), L3 4, L4 0, L5 0, unclassifiable 1 (CR001735, ontology/SPARQL). | – |
| **14** | Provenance fields per record; immutable raw files; SHA-256 | **C** | The master keeps sources, source databases, native IDs, source files, search strategies, DOI, title, authors, year and all per-record variants, plus raw hashes. Search and export dates are held at file level (manifests and filenames), not as per-record columns. This is acceptable, but add a per-source date table to S1. | `MASTER_MERGE_DEDUP_MANIFEST.md`, `MASTER_DEDUP_FINAL_MANIFEST.md` |
| **15** | Dedup order DOI → native ID → exact title → title+author+year → fuzzy; keep extensions; record vs study; dedup log | **C** | D1 DOI, D2 exact title (+year or author), D3 compact title+author+year, then fuzzy candidates reviewed manually (0 auto-merges). Native-ID uniqueness was verified within sources. Extensions and theses were kept separate. Logs are `DEDUPLICATION_LOG*.csv`. Record vs study is handled at full text (FT8). Limitation to disclose: the manual review was done by one AI (Codex) and not double-checked. | 2026-09-18/19 manifests |
| **16.1** | T/A labels INCLUDE / EXCLUDE / UNCERTAIN; pilot R1/R2/X labels not reused | **C** | 256/1,111/643 primary. Pilot labels were not exposed (preparation manifest). | `PRIMARY_SCREENING_FINAL_MANIFEST.md` |
| **16.2** | One primary FT exclusion code E1–E9 | **DEV** | FT1–FT9 were used with different semantics (mapping in §5 and log AMD-R06). There is no equivalent of E3 (language), E6 (insufficient methods: such studies stay included with NOT_REPORTED) or E9 (period). FT7 (not retrieved) and FT9 (language barrier) are new. Actual use: FT1 27, FT2 54, FT3 42, FT4 20, FT6 19, FT8 3 (165), plus FT7 219. FT5 and FT9 were never used. | `07_full_text/FULL_TEXT_PROTOCOL_v1.0.md` §5, frozen 2026-09-21 |
| **16.3** | Second independent reviewer on (a) random 20% T/A, (b) all UNCERTAIN, (c) **all records entering FT screening**. Otherwise disclose single-reviewer status **and** run an independently repeated verification pass for **all borderline/full-text decisions** | **DEV** | (a) Done: 402, frozen seed. (b) Done: 643. Both by a *blinded AI-assisted* second pass, not an independent human, with AI adjudication of 557 disagreements. (c) **Not met: 194 PRIMARY_ONLY_INCLUDE records entered FT on one AI pass.** At full text, one AI pass (AI_FT_01) plus a 10% blinded retest (28/281; 26/28 agree). Extraction had one AI pass plus a 13-study retest (454/494 = 91.9%). This meets neither branch of §16.3. T/A κ = 0.476 on the 402. There is no documented decision under step 5 ("if disagreement unexpectedly high, expand"). A human verification sample (150 T/A + 60 FT) was issued 2026-09-28 and has not been returned. It does not cover the 9 round-3 records. | `04_second_review/SECOND_REVIEW_PROTOCOL_v1.0.md` (2026-09-20); `05_adjudication/ADJUDICATION_PROTOCOL_v1.0.md` (2026-09-21); FT protocol §8 (2026-09-21); `09_human_verification/SAMPLING_PLAN.md` (2026-09-28) |
| **17** | Publisher first → institutional → author/repositories; no automatic exclusion without documented attempts; track retrieved / unavailable / reason / access path | **NYD** | 290/509 retrieved (57%). 219 are FT7, which PRISMA reports separately and does not treat as an exclusion (C). Attempts are partly documented: `NOT_FOUND_FULL_TEXTS_2026-09-27.xlsx` records "where already searched" for 218/228, and 10 are marked "не проверялось" (not checked). The "Результат" column is empty for all 228. The per-record log is inconsistent: `FULL_TEXT_RETRIEVAL_WORKLIST.csv` acquisition columns are blank for all 509, and the CLEAN.xlsx is stale (152 RETRIEVED / 340 PENDING). Round 3 sent 25 author letters with undocumented selection. Library/ILL for 183 DOI records (151 IEEE) is still pending. The round-3 log folder is not in the upload. FT7 characterisation (required because FT7 > 10%) is pending. | FT protocol §4; `SYSTEMATIC_REVIEW_STATE.md` |
| **18** | Study-level extraction matrix with the listed items | **DEV** | A 60-field schema was used. Of 104 protocol items: 42 present, 15 partial, 3 held only in the bibliographic master, and **44 absent** (table in §6). Absent groups include retrieval task/unit, scripts/orthographic and transliteration issues, query source/type/human-synthetic, assessors/agreement, orthographic/script normalisation, query/document side, retrieval-trained vs generic, reranker, candidate depth, same-dense-model/same-preprocessing/same-fusion flags, CI/effect size/ablation, incremental hybrid gain, supports/does-not-support, and **evidence level 0–5**. Extraction ran once per record (124 rows), and 3 rows were merged afterwards. | `07_full_text/FULL_TEXT_STAGE_MANIFEST.md` (schema, 2026-09-21); `HC/ex/FULL_TEXT_EXTRACTION_CODEBOOK_v1.0.md` (2026-09-28) |
| **19** | 10 independent domains, rated LOW / SOME / HIGH CONCERN / NOT APPLICABLE; no summed score; A/B/C/D tier separate | **DEV** | Four domains were rated (qrels validity, baseline fairness, tuning fairness, reporting completeness) on the scale LOW / SOME_CONCERNS / HIGH / NOT_ASSESSABLE. Not rated: source reliability, corpus transparency (only inside "reporting"), query validity, morphology-specific confounders, metric appropriateness, statistical evidence, reproducibility (only as availability fields) and strength of causal interpretation. There is no A/B/C/D tier field. No summed score was made (C). | Same schema and codebook |
| **20** | Descriptive map; morphology × paradigm matrix; language evidence matrix; direction-of-effect synthesis; no meta-analysis without amendment; complementarity synthesis for L3–5 | **DEV** (plan) + NYD (execution) | The plan contains 20.4 (SWiM direction and relative change, C) and 20.5 (no meta-analysis, C). The sign test is a vote-count test, not a meta-analysis, but should be stated explicitly. Partly present: 20.1 (proportions with qrels, testing and public data are in RQ4; studies per language is not explicit). **Missing: 20.2 (morphology × lexical/learned-sparse/dense/late-interaction/hybrid/complementarity matrix), 20.3 (per-language evidence matrix) and the L3–5 framing of 20.6.** The synthesis has not been executed. | Synthesis plan 2026-09-29 |
| **21** | Uzbek section keeps 7 categories separate; no conversion of analyzer/STS/answer accuracy into IR claims | **NYD** | Not yet designed. There is 1 DIRECT_UZBEK study (CR000481) and no contextual layer. National evidence (Bakaev, Xusainova, Elov, Ishkobilov, USHRA, O-RAG, Urinov, Sharifbaev) is outside the review corpus. | – |
| **22** | Gap-killer audit during FT screening/extraction; deep dive and CURRENT_GAP re-evaluation for a direct analogue; "do not wait until manuscript writing" | **NYD** | Partly done informally: the triage flag `carries_complementarity_evidence`, the extraction complementarity fields and the 2026-09-29 note on CR001199. There is no formal 6-criterion audit record, and CURRENT_GAP has no audit-triggered re-evaluation entry. Methods drafting began on 29 Sep, so the timing clause is under strain. This audit's §4 supplies a draft of the formal audit. | – |
| **23** | Careful FT verification of the priority families | **NYD** | See §5 below. Of the families: 3 are included, 2 have key records not retrieved (CR000873, CR001059), 4 have records excluded FT2 (RAGTurk CR000239, Persian CR000220, Arabic CR000162, Amharic CR000226), and 3 have no record in the corpus (Aboasal; GreekBarRetrieval; USHRA/O-RAG/Urinov/Sharifbaev), plus the Kazakh family is uncertain. | – |
| **24** | Update search before submission (rerun all strategies; new ACL commit; screen only new records) | **NYD** | Not yet due. Mandatory, because submission will fall in 2026 or later. | – |
| **25** | Amendment log with ID, date, trigger, old/new rule, reason, sources, reruns, records affected | **ND** | No log exists. The only amendment file is `HC/plan/SYNTHESIS_PLAN_AMENDMENTS.md`, which amends the synthesis plan and not the protocol. Contemporaneous dating cannot be recovered. The retrospective draft `PROTOCOL_AMENDMENT_LOG_DRAFT.md` mitigates this. | – |
| **26** | Preserve the listed data files | **NYD** | Present: frozen protocol, exact queries (the S4 artifact is referenced at a G:/ path), raw exports + hashes, ACL snapshot ID, master, dedup log, T/A log, FT triage log, extraction matrix. **Missing or incomplete in the audited set:** amendment log; a consolidated full-text screening log including FT7 (round-3 triage lives in `HC/triage/out_round3.csv`, and the round-3 extraction in `HC/ex/out/X14.csv` is not merged into `SR/07_full_text/extraction/`); a separate quality-appraisal table; included-study bibliography; final PRISMA counts; synthesis tables; update-search files. Also not in the upload: the ACL search script folder `artifacts/acl-anthology-pilot-2026-09-17/`, `IEEE_I1_QUERY_PROVENANCE.md`, `PRISMA_IDENTIFICATION_COUNTS.json` and `acquisition_round3/`. | – |
| **32** | Frozen execution sequence | **DEV** | Phases 1–2 were followed. In Phase 3, step 11 was done with an AI second pass, and full text was retrieved and screened with a single AI pass (see §16.3). In Phase 4, **study-level merge (step 14) came after extraction**, as FT8 via Clarification 001. **Evidence-level classification (step 16) was skipped.** Appraisal (step 17) is partial. **The gap-killer audit (step 18) was not recorded** before the synthesis plan. Phase 5 has not started. | – |

Counts: C 4 · DEV 11 · NYD 11 · ND 1 = 27 rows.

---

## 3. RQ reconciliation (protocol RQ1–RQ6 vs synthesis plan RQ1–RQ4)

| Protocol RQ | Synthesis-plan coverage | Gap |
|---|---|---|
| RQ1 Which representations were evaluated (10 types incl. truncation, orthographic and script normalisation, transliteration, morphology-aware expansion) | Plan RQ1, first half | Orthographic and script normalisation, transliteration and morphology-aware expansion are not extracted as representations (expansion is in notes only). Truncation is merged into stem, and root into morpheme. |
| RQ2 Lexical effect on effectiveness, **efficiency, index/vocabulary size, query-level behaviour, composition of retrieved relevant docs** | Plan RQ1, second half (headline-metric direction and relative change only) | Efficiency and index size are not extracted. Query-level behaviour appears only as `per_query_analysis`. Composition of relevant sets is covered only via the unique-hit and overlap flags. |
| RQ3 Dense/hybrid handling with 5 control checks | Plan RQ2 (narrative questions a–c) | Retrieval-trained vs generic, same dense model across variants, fixed dense preprocessing, fusion controlled and morphology isolated are not specified as synthesis items, and 3 of them have no extraction field. |
| RQ4 Complementarity measured vs aggregate only | Plan RQ3 (evidence map analysis-type × channel pair) | Broadly covered. The plan widens this to any channel pair (lexical–lexical etc.), which is acceptable if lexical–dense is reported first. "Incremental hybrid gain" is not a field. |
| RQ5 Evaluation quality: corpus, query construction, qrels, pooling, assessors, baselines, controlled parameters, metrics, statistics, ablation, reproducibility | Plan RQ4 (4 RoB domains, evaluation practice, availability) | Query construction, assessors, ablation, metric appropriateness and statistical evidence are not appraised. |
| RQ6 Uzbek boundary across 7 evidence types (resources, infrastructure, STS, corpus-level retrieval, hybrid, reranking, RAG answer quality) | Plan RQ4, Turkic/Uzbek narrative | This cannot be answered as specified without §9 national searches, the §11 contextual layer and the Uzbek closest-work records (USHRA, O-RAG, Urinov, Sharifbaev, CR001179 FT7). |

Decision date: 2026-09-29, the synthesis-plan freeze. No amendment records the reduction. Either amend the synthesis plan to answer RQ1–RQ6 (preferred: an RQ mapping table plus added outputs), or file a protocol amendment that justifies the merge and states that RQ6 is answered narratively with a contextual layer.

---

## 4. Gap-killer audit (§22): all 125 included studies

Data: `SR/07_full_text/extraction/FULL_TEXT_EXTRACTION_AI_EX_01.csv` (121 rows) plus `HC/ex/out/X14.csv` (4 rows) = 125 studies. Full per-study table in the Appendix.

**Mechanical coding from extracted fields:**
- C1 = `morphological_representations_compared` ≥ 2
- C2 = `dense_channel_present` = YES (a proxy: the schema has no "same fixed dense model across variants" field)
- C3 = `hybrid_present` = YES
- C4 = `channel_overlap_reported` = YES
- C5 = `unique_hits_analysis` or `oracle_or_upper_bound` = YES
- C6 = C1 ∧ C3 (a proxy: the schema has no "morphology-conditioned incremental hybrid gain" field)

Mechanical score distribution: 0 → 22; 1 → 88; 2 → 11; **3 → 1; 4 → 3**; 5–6 → 0.

**Strict reading (from the extraction notes, lexical–dense only):**

| Study | Mechanical | C1 | C2 same fixed dense | C3 controlled fusion | C4 | C5 | C6 | Strict score | Verdict |
|---|---:|---|---|---|---|---|---|---:|---|
| CR000108 UPERF (Urdu, 2024) | 4 | YES (raw/stem/lemma) | UNCLEAR (dense models also receive the raw/stem/lemma input; whether the same trained Word2Vec is used across variants is not stated) | PARTIAL (linear α,β,γ, grid-searched on test = TUNED_ON_TEST) | NO | NO | UNCLEAR (hybrid reported for weight settings, not per morphology variant) | 1 + 3 unclear/partial | Closest §23 family in corpus; **not** a direct analogue |
| CR000448 Korean medical (2024) | 4 | YES (Porter vs Kiwi) | PARTIAL (dense independent of morphology, but ensemble uses a different stemmer per dataset) | NO (candidate union, TUNED_ON_TEST, no ensemble results reported) | NO | NO | NO | 1–2 | Not an analogue |
| CR000913 PolEval 2023 Task 3 (Polish) | 4 | PARTIAL (variants belong to different teams' systems, not controlled) | NO | NO (merge undescribed) | NO | NO | NO | 0–1 | Not an analogue |
| CR002201 Arabic root-search thesis (2001) | 3 | YES | NO (no dense) | NO | YES (lexical–lexical) | YES (lexical–lexical unique hits) | NO | 1 on lexical–dense criteria | Lexical-only complementarity precedent; not an analogue |
| **CR001199 Sunay & Yigit-Sert (Turkish, 2026)** | 2 | YES (RAW, 2 LEMMA, 2 RAW+LEMMA) | YES (mE5-base constant; also fed lemmatised input) | NO (the "HYBRID" is a raw+lemma index, not lexical–dense fusion) | NO | NO | NO | **2** | Closest to the PhD design (BM25 raw vs lemma + same dense model, Turkic), aggregate only. **Does not meet ≥3.** |

**Conclusion (draft, for researcher confirmation).**
- No included study meets ≥3 of the six criteria when they are read strictly as lexical–dense criteria.
- None meets "most or all" (≥4) even mechanically once the notes are read. The 4-point mechanical scores come from the C6 proxy (hybrid + ≥2 variants), and the notes show the hybrid was not run per morphology variant.
- No "direct analogue" trigger under §22 therefore arises from the 125 included studies.

**Caveats that stop this from being a gap-closing conclusion:**
1. 219 FT7 records are unaudited, including §23 priority records CR000873 (Korean tokenisation × BM25/DPR) and CR001059 (Amharic lexical/neural).
2. GreekBarRetrieval, which the project's own `CURRENT_GAP.md` and MASTER_INDEX HYB-012 call the "closest global gap killer found", is **not in the review corpus**. Neither is Aboasal et al. (HYB-011).
3. National Uzbek sources were not searched.
4. The extraction schema lacks fields for C2 and C6, so those two criteria must be read manually for the 10 non-latent dense studies (6 L2 + 4 hybrid).

Required record: add a dated entry to `research/GAP_HISTORY.md` / CURRENT_GAP ("§22 audit 2026-09-30: no direct analogue among 125 included; boundary conditions …"), with **no change** to v0.8 refined.

---

## 5. Closest-work priority set (§23)

Status notation: route at T/A → full-text outcome. "Single pass" means the record advanced on one AI pass only.

| Family (protocol §23) | canonical_id(s) | Status |
|---|---|---|
| UPERF and related Urdu retrieval | **CR000108** UPERF (ACL 2024.paclic-1.96) | T/A PERSISTENT_UNCERTAIN → FT INCLUDE → extracted (tentative L3) |
| | CR000935 Urdu multilevel stemmer (IEEE Access 2024) | INCLUDE → INCLUDE, extracted |
| | CR002024 CURE (2021); CR002126 Riaz 2018 (PQDT) | INCLUDE → INCLUDE, extracted |
| | CR000197 DR-RAG Urdu (2026) | INCLUDE → INCLUDE, extracted (retest said FT2; coordinator kept INCLUDE) |
| | CR001865 Urdu query expansion; CR000301 Soundex Urdu–English CLIR | Excluded FT2 |
| | CR000167 Roman Urdu IR dataset & baseline (2025) | Excluded TA2 (adjudicated) |
| | Kazi & Khoja, Computer Speech & Language 2026 | **Not found in search** |
| Morphology-aware Arabic hybrid / legal IR | Aboasal et al. 2026 (project card HYB-011) | **Not found in search** |
| | CR001189 Lawsuit AraRAG (2026) | INCLUDE (single pass) → **FT7 not retrieved** |
| | CR001202 Arabic RAG evaluation framework (2026) | UNCERTAIN → **FT7** |
| | CR001869 hybrid Arabic morpho-semantic retrieval (2018) | INCLUDE → **FT7** |
| | CR000162 Enhancing Arabic RAG through language processing (2025) | → Excluded FT2 (OCR preprocessing, no morphology) |
| | CR000110 RAG pipelines for Arabic lexical IR (2025) | Excluded TA1 (adjudicated) |
| GreekBarRetrieval | – (arXiv preprint; none of the 4 sources indexes arXiv) | **Not found in search**. Related CR000221 Gretino excluded FT2 |
| Sunay & Yigit-Sert Turkish RAG morphology normalisation | **CR001199** (IEEE SIU 2026) | INCLUDE (single pass) → FT INCLUDE → extracted (round 3; L2) |
| Korean tokenisation × BM25/DPR | **CR000873** (IEEE ICACI 2023, DOI 10.1109/ICACI58115.2023.10146145) | INCLUDE (single pass) → **FT7 not retrieved** |
| | Related: CR000448 Korean medical | Included (L3) |
| Amharic lexical/neural comparisons | **CR001059** Yeshambel et al. 2025 (IEEE ICICT, 10.1109/ICICT64582.2025.00041) | INCLUDE (single pass) → **FT7 not retrieved** |
| | CR000149 Mekonnen et al. 2025 (Findings ACL) | Included (L2) |
| | CR000427, CR000447, CR000354, CR001471 | Included |
| | CR000226 "Multilingual curse … Amharic" (2026) | Excluded FT2 (BM25 vs dense, morphology only motivational) |
| | CR000477 Amharic legal RAG (2026) | Excluded FT2, flagged BORDERLINE by triage |
| | CR000236 | Excluded FT4 |
| Kazakh morphology + lexical/embedding retrieval | **No record identified with certainty** | Nearest: CR001903 "Lexicon-free stemming for Kazakh language IR" (IEEE 2018), **excluded TA3 on a single primary pass** (possible false exclusion). CR001191 Kazakh legal RAG (2026) → FT7. CR000104 KazQAD → excluded TA2 (adjudicated) |
| ACL P12-2043 Arabic Retrieval Revisited | **CR000288** | INCLUDE (single pass) → FT INCLUDE → extracted |
| Morphology-aware RAG (Turkish, Urdu, Persian, Arabic) | Turkish: CR000239 RAGTurk | → **Excluded FT2** ("lemma-aware retrieval listed as future work") |
| | Turkish: CR001199 | Included |
| | Turkish: CR001149, CR001170 | FT7 |
| | Urdu: CR000197 | Included |
| | Persian: CR000220 | Excluded FT2 |
| | Arabic: CR000162 | FT2 |
| | Arabic: CR001189, CR001202 | FT7 |
| | Arabic: CR000110 | TA1 |
| Uzbek hybrid/RAG (USHRA, O-RAG, Urinov, newer) | USHRA (ACM 10.1145/3789692.3789825), O-RAG (ACM 10.1145/3789692.3789782), Urinov (Zenodo 10.5281/zenodo.17341315), Sharifbaev (manuscript) | **Not found in search**. ACM DL, Zenodo and national sources were not searched |
| | CR000481 Ishkobilov et al. 2026, Uzbek semantic retrieval (TF-IDF vs FastText) | UNCERTAIN → FT INCLUDE → extracted (DIRECT_UZBEK, L2) |
| | CR001179 Uzbek labour-law chatbot (2026) | UNCERTAIN → **FT7** |

Several §23-relevant full texts (CR000239, CR000220, CR000226, CR000477) were excluded FT2 by a single AI pass. Meanwhile, comparable lexical-vs-dense MRL papers where morphology enters only as a stemmed BM25 baseline were included (CR000103 BEIR-PL, CR000100). This borderline boundary is exactly what §16.3's repeated-verification fallback is meant to check. These records are also natural members of the §11 contextual layer.

---

## 6. §18 extraction items vs the 60-field schema

P = present field; Pa = partial (merged, free text or proxy); M = only in the bibliographic master; A = absent.

| Group (items) | P | Pa | M | A | Absent / partial items |
|---|---:|---:|---:|---:|---|
| Bibliography (10) | 5 | 1 | 3 | 1 | Pa: peer-reviewed / defended / preprint (publication_type only). M: authors, title, DOI. **A: source reliability A/B/C/D** |
| Language (7) | 3 | 0 | 0 | 4 | A: scripts, low-resource justification, orthographic variation, transliteration issue |
| Retrieval task (6) | 0 | 0 | 0 | 6 | A: ad-hoc document / passage / legal-domain / RAG retrieval / other; retrieval unit |
| Corpus (7) | 1 | 2 | 0 | 4 | Pa: source (collection_name), public/private (data_available). A: domain, token count, corpus dedup, language identification |
| Queries / qrels (11) | 3 | 1 | 0 | 7 | Pa: pooling. A: query source, query type/length, human/synthetic, number of relevant items, assessors, agreement, adjudication |
| Morphology intervention (11) | 5 | 3 | 0 | 3 | Pa: root (merged into morpheme), morphological analysis (tool name), truncation (merged into stem). A: orthographic normalisation, script normalisation/transliteration, query/document/both |
| Retrieval system (11) | 7 | 1 | 0 | 3 | Pa: late interaction (inside dense). A: retrieval-trained vs generic embedding, reranker, RAG system |
| Hybrid protocol (9) | 3 | 2 | 0 | 4 | Pa: α/weights and RRF parameter (free text). A: candidate depth, same dense model across variants, same dense preprocessing, same fusion configuration |
| Metrics (10) | 8 | 0 | 0 | 2 | A: latency, index/vocabulary size |
| Statistical evidence (6) | 2 | 0 | 0 | 4 | A: confidence intervals, effect size, multiple-comparison control, ablation |
| Complementarity (9) | 4 | 4 | 0 | 1 | Pa: lexical-only and dense-only hits (one merged field, channel pair only in scope text), union (merged with oracle), query-level morphology effect. A: incremental hybrid gain |
| Interpretation (7) | 1 | 1 | 0 | 5 | Pa: strongest result. A: within-study morphology delta (planned Tier 3), supports, does not support, limitations (notes only), **evidence level 0–5** |
| **Total (104)** | **42** | **15** | **3** | **44** | |

The following items are RQ-critical and should be supplemented first:
- evidence level;
- same dense model, same dense preprocessing and same fusion configuration (10 non-latent dense studies: 6 L2 + 4 hybrid);
- retrieval-trained vs generic;
- incremental hybrid gain;
- query/document side of morphology;
- orthographic/script normalisation;
- retrieval task and unit;
- efficiency and index size (for protocol RQ2);
- source-reliability tier.

---

## 7. Evidence files read

- Protocol and timestamps: `RS/systematic-review/protocol/ARTICLE_RESEARCH_PROTOCOL_v1.0_FROZEN.md`, `CHAT_TIMESTAMPS.md`.
- State and gap: `RS/SYSTEMATIC_REVIEW_STATE.md` (updates 2026-09-28 and 2026-09-29), `RS/CURRENT_GAP.md`, `PROJECT_STATE.md`, `literature/MASTER_INDEX.md` (closest-work identifiers only).
- Raw exports (`SR/01_raw_exports/`):
  - `acl/ACL_CANONICAL_RAW_EXPORT_MANIFEST.md`
  - `pqdt/PQDT_P2_RAW_EXPORT_MANIFEST.md`
  - `ebsco/EBSCO_S4_RAW_EXPORT_MANIFEST.md`, `ebsco/EXPORT_SESSION_EVIDENCE.json`
  - `ebsco/per_database/EBSCO_PER_DATABASE_EXPORT_MANIFEST.md`, `…/audit_history/EXACT_QUERY_VERIFICATION_2026-09-18.json`
  - `ieee/IEEE_I1_RAW_EXPORT_MANIFEST.md`, `ieee/audit/IEEE_I1_EXPORT_SESSION.json`, `ieee/audit/IEEE_I1_EXACT_QUERY.txt`
- Merge and deduplication: `SR/02_merge_dedup/MASTER_MERGE_DEDUP_MANIFEST.md`, `MASTER_DEDUP_FINAL_MANIFEST.md`, `MASTER_DEDUPLICATED_FINAL.csv`.
- Title/abstract screening, second review and adjudication:
  - `SR/03_…/TITLE_ABSTRACT_SCREENING_PREPARATION_MANIFEST.md`, `PRIMARY_SCREENING_FINAL_MANIFEST.md`, `PRODUCTION_DRIFT_CHECKPOINT_004.md`
  - `SR/04_…/SECOND_REVIEW_PROTOCOL_v1.0.md`, `SECOND_REVIEW_PACKAGE_MANIFEST.md`
  - `SR/05_…/ADJUDICATION_PROTOCOL_v1.0.md`, `run_AI_ADJ_01/ADJUDICATION_FREEZE_RECORD.json`, `ADJUDICATION_DRIFT_HOLD_001.md`
- Final disposition: `SR/06_…/FINAL_DISPOSITION_MANIFEST.md`, `FINAL_TITLE_ABSTRACT_COUNTS.json`, `FINAL_TITLE_ABSTRACT_DISPOSITION.csv`, `PRISMA_TITLE_ABSTRACT_FLOW.md`.
- Full text (`SR/07_full_text/`):
  - `FULL_TEXT_PROTOCOL_v1.0.md`, `FULL_TEXT_STAGE_MANIFEST.md`
  - `FULL_TEXT_RETRIEVAL_WORKLIST.csv`, `FULL_TEXT_RETRIEVAL_WORKLIST_CLEAN.xlsx`, `NOT_FOUND_FULL_TEXTS_2026-09-27.xlsx`
  - `triage/FULL_TEXT_TRIAGE_AI_FT_01.csv`, `triage/FULL_TEXT_TRIAGE_2026-09-27.xlsx` (retest sheet)
  - `extraction/FULL_TEXT_EXTRACTION_AI_EX_01.csv`, `extraction/RETEST_AGREEMENT.json`
- Synthesis and verification: `SR/08_publication/SYNTHESIS_PLAN_v1.0.md`, `SR/09_human_verification/SAMPLING_PLAN.md`.
- Working files under `HC/`:
  - `HC/ex/FULL_TEXT_EXTRACTION_CODEBOOK_v1.0.md`, `EXTRACTION_CLARIFICATION_001.md`, `out/X14.csv`
  - `HC/triage/out_round3.csv`, `TRIAGE_INSTRUCTIONS.md`, `TITLE_ABSTRACT_SCREENING_CODEBOOK.md`
  - `HC/plan/SYNTHESIS_PLAN_AMENDMENTS.md`
  - `HC/plan/methods/METHODS_DRAFT_v0.2.md`, `METHODS_VERIFY.md`, `OPEN_QUESTIONS.md`
- Referenced but **not available** to this audit:
  - `IEEE_I1_QUERY_PROVENANCE.md`, `PRISMA_IDENTIFICATION_COUNTS.json`
  - `07_full_text/acquisition_round3/` (letters log, other-sources papers)
  - `FULL_TEXT_TRIAGE_REVISIONS_2026-09-28.csv`, `FULL_TEXT_EXTRACTION_REVISIONS_2026-09-28.csv`
  - the ACL pilot script folder, and the S4 artifact at its G:/ path.

---

## 8. Actions before submission (prioritised)

Effort assumes AI-assisted execution with researcher checking. Human-only effort is shown where it matters.

| # | Priority | Action | Removes / reduces | Effort |
|---:|---|---|---|---|
| 1 | MUST | Review, correct and sign `PROTOCOL_AMENDMENT_LOG_DRAFT.md`. Store it next to the frozen protocol as `PROTOCOL_AMENDMENT_LOG.md`, cite it in Methods and Supplementary S16, and mark every entry "retrospectively documented 2026-09-30". | §25 (mitigates), §0 | 3–4 h |
| 2 | MUST | Independently repeated verification of **all 290 full-text decisions** (blinded second pass, different session and model or a human). Prioritise all FT2/FT3 borderlines and all §23 records (CR000239, CR000220, CR000226, CR000477, CR000162). Then adjudicate and report agreement. Finish the issued human-verification sample (150 T/A + 60 FT) and extend it to the 9 round-3 records. | §16.3 (fallback branch), §32 | AI pass ~1 day + adjudication 0.5 day. Human sample 15–20 h. Human pass on all 290 ≈ 50–70 h |
| 3 | MUST | Run the §9 national Uzbek searches in EN/RU/UZ, with apostrophe variants, over national and regional sources (national library, university repositories, Uzbek journals, Google Scholar, CyberLeninka/eLibrary). Log strings, dates (UTC+05) and counts, screen with the same codebooks, and report them as "other methods". | §9, §21, RQ6 | 1.5–2.5 days |
| 4 | MUST | Supplementary identification (§6.4, §23): backward/forward chaining from included core studies (at least L2–L3 and Turkic) and from CONTEXT_REVIEW surveys. Targeted retrieval of the closest-work records not in the corpus: GreekBarRetrieval, Aboasal 2026, USHRA, O-RAG, Urinov, Kazi & Khoja 2026, Munetsi 2026. Screen the 2 El Mahdaouy papers. Keep discovery provenance. | §6.4, §23, §4 PRISMA "other methods" | 2–4 days |
| 5 | MUST | Retrieve the §23 FT7 records through library/ILL/author requests: CR000873, CR001059, CR001189, CR001202, CR001191, CR001179, CR001149, CR001170, CR001869. Complete §17 attempts (the 10 "not checked"; library request for the 183 DOI records), consolidate one per-record acquisition log, and produce the FT7 characterisation. Triage and extract whatever arrives. | §17, §23, §22 caveat | 1 day work + waiting time |
| 6 | MUST | Add `evidence_level` (L0–L5) by deterministic rules (appendix). Read the missing L4 and §20.6 fields (same dense model, same preprocessing, fusion held constant, morphology isolated, incremental hybrid gain) for the 10 non-latent dense studies (6 L2 + 4 hybrid). Amend the synthesis plan to map to protocol RQ1–RQ6 and add §20.2 (morphology × paradigm) and §20.3 (language) matrices plus an L3–5 complementarity section. Decide by amendment whether LSI/LDA/LSA count as "semantic". | §13, §3, §20, §32 step 16 | 1–1.5 days |
| 7 | MUST (timed) | Update search immediately before submission: re-run S4 ×3, P2, I1 (year-partitioned) and ACL on the then-current commit; screen only new records; merge into PRISMA. | §24, §5 (2026 completeness) | 1–2 days |
| 8 | SHOULD | Supplementary appraisal of the 6 missing §19 domains plus the A/B/C/D tier. Several can be derived from existing fields (statistical evidence, reproducibility, source tier from publication_type/venue); the others need a pass over 125 studies. Map existing labels to the protocol scale (LOW/SOME/HIGH CONCERN/NOT APPLICABLE). | §19, RQ5 | 1–2 days |
| 9 | SHOULD | Decide the status of the 21 METHODOLOGICAL_ONLY (English/Chinese-only) studies under §10.4, by amendment. Options: retain as a separately analysed "non-MRL methodological" tier, or exclude with a sensitivity analysis. Mark the 1 preprint as a provisional tier. | §10, §16.2 (E3) | 2–3 h |
| 10 | SHOULD | Build the §11 contextual evidence layer as a table kept apart from effectiveness studies. It should hold MRL lexical-vs-dense or RAG works excluded FT2 for motivational-only morphology, Uzbek resources and infrastructure, and the national deep-dive works. | §11, §21, RQ6 | 1 day |
| 11 | SHOULD | Record the §22 gap-killer audit (from this document's §4, once confirmed) in GAP_HISTORY/CURRENT_GAP with a date. Repeat it after actions 4–5. | §22 | 2 h + repeat 1 h |
| 12 | SHOULD | Supplement the RQ-critical §18 items listed in §6: retrieval task/unit, query/document side, orthographic/script normalisation, retrieval-trained vs generic, reranker, efficiency and index size. | §18, protocol RQ1–RQ3 | 1–2 days |
| 13 | SHOULD | Produce the PRISMA 2020 flow (both arms), the PRISMA-S checklist and the S1 search appendix with UTC+05 and UTC times. | §4 | 0.5–1 day |
| 14 | SHOULD | Document the §16.3 step-5 decision on κ = 0.476. Either justify not expanding double screening, or run a second pass on a random sample of the 892 PRIMARY_ONLY_EXCLUDE records, including CR001903 (Kazakh IR stemming, TA3). | §16.3 | 2 h (decision) / 1 day (sample) |
| 15 | COULD | Complete the §26 archive: ACL script folder, IEEE provenance, PRISMA_IDENTIFICATION_COUNTS.json, round-3 folder, merged 125-row extraction, separate RoB table, included-study bibliography, hash list. | §26 | 3–4 h |
| 16 | COULD | Register the frozen protocol and the amendment log retrospectively (e.g. OSF) and cite the identifier. | Transparency | 1–2 h |

---

## Appendix. Six gap-killer criteria (mechanical) and tentative evidence level: all 125 studies

C1 = ≥2 morphological representations; C2 = dense channel present; C3 = lexical+dense hybrid present; C4 = overlap reported; C5 = unique hits or oracle reported; C6 = C1 ∧ C3.
Tentative ladder rules:
- L5: C4/C5 = YES and complementarity scope LEXICAL_VS_DENSE.
- L4 (check): hybrid + ≥2 variants + fusion FIXED_A_PRIORI/TUNED_ON_DEV.
- L3: hybrid.
- L2: dense channel. "[latent]" marks LSI/LSA/LDA.
- L1: lexical channel only.

"Scope" is the prefix of `complementarity_finding`. These are proxies, not final values. See §4 for the strict reading of the top candidates.

| study_id | year | languages | C1 ≥2 morph variants | C2 dense channel | C3 lex+dense hybrid | C4 overlap | C5 unique hits/oracle | C6 hybrid × ≥2 variants | mech. score | scope of complementarity_finding | tentative ladder level |
|---|---|---|---|---|---|---|---|---|---:|---|---|
| CR000004 | 2006 | Arabic | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR000007 | 2006 | Arabic; English; French | Y | · | · | · | · | · | 1 | NONE | L1 |
| CR000073 | 2023 | Hungarian | Y | Y | · | · | · | · | 2 | LEXICAL_VS_DENSE | L2 |
| CR000100 | 2024 | Polish | Y | Y | · | · | · | · | 2 | LEXICAL_VS_DENSE | L2 |
| CR000103 | 2024 | Polish | · | Y | Y | · | · | · | 2 | LEXICAL_VS_DENSE | L3 |
| CR000108 | 2024 | Urdu | Y | Y | Y | · | · | Y | 4 | LEXICAL_VS_DENSE | L3 |
| CR000149 | 2025 | Amharic | · | Y | · | · | · | · | 1 | LEXICAL_VS_DENSE | L2 |
| CR000161 | 2025 | Hindi; Gujarati; English | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR000179 | 2025 | Estonian | Y | · | · | · | · | · | 1 | NONE | L1 |
| CR000197 | 2026 | Urdu; English | · | Y | · | · | · | · | 1 | DENSE_VS_DENSE | L2 (no lexical channel) |
| CR000218 | 2026 | Nepali | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR000248 | 2012 | English | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR000251 | 2008 | Mongolian | Y | · | · | · | Y | · | 2 | LEXICAL_VS_LEXICAL | L1 |
| CR000288 | 2012 | Arabic | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR000292 | 2001 | Swedish | Y | · | · | · | · | · | 1 | NONE | L1 |
| CR000293 | 2002 | German | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR000295 | 2005 | Arabic | Y | · | · | · | · | · | 1 | NONE | L1 |
| CR000299 | 2007 | Finnish | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR000302 | 2014 | Arabic | · | · | · | · | · | · | 0 | SYSTEM_VS_SYSTEM | L1 |
| CR000334 | 2016 | Persian | Y | · | · | · | · | · | 1 | NONE | L1 |
| CR000338 | 2004 | Dutch; English; Finnish; French; German; | Y | · | · | · | · | · | 1 | NONE | L1 |
| CR000342 | 2015 | Finnish | · | · | · | · | · | · | 0 | LEXICAL_VS_LEXICAL | L1 |
| CR000354 | 2003 | Amharic | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR000362 | 2017 | Kurdish (Sorani) | Y | · | · | · | · | · | 1 | NONE | L1 |
| CR000363 | 2018 | Portuguese | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR000367 | 2018 | Tamil; English | · | · | · | · | · | · | 0 | SYSTEM_VS_SYSTEM | L1 |
| CR000371 | 2018 | Arabic | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR000427 | 2023 | Amharic | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR000430 | 2023 | Sanskrit | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR000447 | 2024 | Amharic | Y | · | · | · | · | · | 1 | NONE | L1 |
| CR000448 | 2024 | Korean; English | Y | Y | Y | · | · | Y | 4 | LEXICAL_VS_DENSE | L3 |
| CR000452 | 2005 | Finnish | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR000481 | 2026 | Uzbek | · | Y | · | · | · | · | 1 | LEXICAL_VS_DENSE | L2 |
| CR000484 | 2006 | Finnish | · | · | · | · | · | · | 0 | SYSTEM_VS_SYSTEM | L1 |
| CR000490 | 2006 | Swedish | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR000491 | 2006 | English; Finnish; German; Swedish | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR000495 | 2006 | Finnish | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR000499 | 2007 | English; French; Bengali | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR000502 | 2008 | Turkish | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR000503 | 2007 | English | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR000504 | 2007 | Finnish; Swedish; German; Russian | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR000505 | 2007 | Bulgarian | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR000518 | 2009 | Arabic | · | · | · | · | · | · | 0 | LEXICAL_VS_LEXICAL | L1 |
| CR000520 | 2000 | Spanish | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR000522 | 2009 | Arabic | Y | · | · | · | Y | · | 2 | LEXICAL_VS_LEXICAL | L1 |
| CR000523 | 2009 | English | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR000529 | 2009 | Russian | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR000539 | 2010 | Persian; English | · | · | · | · | · | · | 0 | NONE | L1 |
| CR000546 | 2011 | Swedish | · | · | · | · | · | · | 0 | NONE | L1 |
| CR000550 | 2012 | Turkish | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR000559 | 2002 | German; English | Y | · | · | · | · | · | 1 | NONE | L1 |
| CR000561 | 2004 | German | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR000566 | 2013 | English; Marathi; Czech; Bengali | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR000578 | 2014 | Czech; German; French; English | · | · | · | · | · | · | 0 | SYSTEM_VS_SYSTEM | L1 |
| CR000581 | 2014 | French; German; English | · | · | · | · | · | · | 0 | LEXICAL_VS_LEXICAL | L1 |
| CR000604 | 2018 | English | Y | · | · | · | · | · | 1 | NONE | L1 |
| CR000609 | 2019 | Serbian; German | · | · | · | · | · | · | 0 | LEXICAL_VS_LEXICAL | L1 |
| CR000613 | 2004 | Japanese | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR000618 | 2004 | Arabic | Y | · | · | · | · | · | 1 | NONE | L1 |
| CR000627 | 2001 | Finnish | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR000681 | 2009 | English; Finnish; Swedish | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR000682 | 2009 | Czech | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR000688 | 2009 | Arabic; Bulgarian; Bengali; Czech; Germa | Y | · | · | · | · | · | 1 | NONE | L1 |
| CR000690 | 2009 | Hindi; Bengali; Marathi | · | · | · | · | · | · | 0 | NONE | L1 |
| CR000691 | 2009 | Turkish | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR000913 | 2023 | Polish | Y | Y | Y | · | · | Y | 4 | SYSTEM_VS_SYSTEM | L3 |
| CR000914 | 2023 | Polish | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR000935 | 2024 | Urdu | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR001121 | 2025 | Indonesian | Y | · | · | · | · | · | 1 | NONE | L1 |
| CR001199 | 2026 | Turkish | Y | Y | · | · | · | · | 2 | LEXICAL_VS_DENSE | L2 |
| CR001209 | 2003 | English; Chinese | · | · | · | · | · | · | 0 | LEXICAL_VS_LEXICAL | L1 |
| CR001261 | 2005 | Persian | Y | · | · | · | · | · | 1 | NONE | L1 |
| CR001309 | 2007 | Arabic; English | Y | · | · | · | · | · | 1 | NONE | L1 |
| CR001348 | 2008 | English | Y | · | · | · | · | · | 1 | NONE | L1 |
| CR001352 | 2007 | English | · | · | · | · | · | · | 0 | SYSTEM_VS_SYSTEM | L1 |
| CR001390 | 2009 | Turkish | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR001454 | 2010 | Arabic | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR001471 | 2009 | Amharic | · | · | · | · | · | · | 0 | NONE | L1 |
| CR001477 | 2010 | English | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR001505 | 2011 | Hungarian | · | · | · | · | · | · | 0 | SYSTEM_VS_SYSTEM | L1 |
| CR001508 | 2011 | Malay | Y | · | · | · | · | · | 1 | NONE | L1 |
| CR001514 | 2011 | Arabic | · | · | · | · | · | · | 0 | LEXICAL_VS_LEXICAL | L1 |
| CR001515 | 2011 | English | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR001537 | 2012 | Turkish | Y | · | · | · | · | · | 1 | NONE | L1 |
| CR001557 | 2012 | English | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR001585 | 2013 | Kurdish (Sorani); English | Y | · | · | · | · | · | 1 | NONE | L1 |
| CR001612 | 2014 | English | Y | · | · | · | · | · | 1 | SYSTEM_VS_SYSTEM | L1 |
| CR001646 | 2014 | Arabic | Y | · | · | · | · | · | 1 | NONE | L1 |
| CR001654 | 2014 | Arabic | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR001735 | 2015 | Lithuanian | · | · | · | · | · | · | 0 | NONE | unclassifiable (no lexical/dense channel) |
| CR001813 | 2017 | Indonesian | Y | · | · | · | · | · | 1 | NONE | L1 |
| CR001840 | 2018 | English | · | · | · | · | · | · | 0 | NONE | L1 |
| CR001888 | 2000 | Chinese | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR001964 | 2020 | English | Y | · | · | · | · | · | 1 | NONE | L1 |
| CR001997 | 2020 | Arabic | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR002024 | 2020 | Urdu | Y | · | · | · | · | · | 1 | NONE | L1 |
| CR002078 | 2001 | English | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR002102 | 2012 | English | Y | Y | · | · | · | · | 2 | DENSE_VS_DENSE | L2 (no lexical channel) [latent] |
| CR002104 | 2011 | Chinese; English | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR002114 | 2004 | Portuguese; English | Y | Y | · | · | · | · | 2 | SYSTEM_VS_SYSTEM | L2 (no lexical channel) [latent] |
| CR002124 | 2017 | English | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR002126 | 2018 | Urdu; Russian; Arabic; English | Y | Y | · | · | · | · | 2 | LEXICAL_VS_LEXICAL | L2 [latent] |
| CR002131 | 2016 | English | · | · | · | · | · | · | 0 | NONE | L1 |
| CR002141 | 2001 | Arabic; English | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR002145 | 2008 | Turkish | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR002156 | 2016 | Hindi; Bengali | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR002158 | 2009 | Turkish | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR002168 | 2022 | Malay; English | Y | · | · | · | · | · | 1 | SYSTEM_VS_SYSTEM | L1 |
| CR002173 | 2014 | English; Arabic; Malay | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR002184 | 2008 | English | · | · | · | · | · | · | 0 | LEXICAL_VS_LEXICAL | L1 |
| CR002185 | 2008 | Bulgarian; Czech; German; English; Spani | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR002188 | 2008 | Arabic; English | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR002192 | 2004 | Arabic | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR002194 | 2004 | Dutch | Y | · | · | · | Y | · | 2 | LEXICAL_VS_LEXICAL | L1 |
| CR002195 | 2003 | Persian | Y | · | · | · | · | · | 1 | NONE | L1 |
| CR002196 | 2003 | Arabic | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR002198 | 2003 | Arabic; English | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR002201 | 2001 | Arabic | Y | · | · | Y | Y | · | 3 | LEXICAL_VS_LEXICAL | L1 |
| CR002203 | 2002 | Arabic; English | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR002210 | 2012 | Turkish | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR002211 | 2011 | Turkish | · | · | · | · | · | · | 0 | NONE | L1 |
| CR002215 | 2012 | English; Finnish; German | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |
| CR002216 | 2012 | Finnish | Y | Y | · | · | · | · | 2 | LEXICAL_VS_LEXICAL | L2 [latent] |
| CR002218 | 2004 | English | · | · | · | · | · | · | 0 | LEXICAL_VS_LEXICAL | L1 |
| CR002221 | 2010 | Arabic | Y | · | · | · | · | · | 1 | LEXICAL_VS_LEXICAL | L1 |

Mechanical score distribution: {0: 22, 1: 88, 2: 11, 3: 1, 4: 3}

Tentative ladder distribution: {'L1': 110, 'L2': 5, 'L3': 4, 'L2 (no lexical channel)': 1, 'unclassifiable (no lexical/dense channel)': 1, 'L2 (no lexical channel) [latent]': 2, 'L2 [latent]': 2}
