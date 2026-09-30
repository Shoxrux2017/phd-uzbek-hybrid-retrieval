# SYSTEMATIC_REVIEW_EXECUTION_CHECKLIST_v1.0

**Protocol:** `ARTICLE_RESEARCH_PROTOCOL_v1.0_FROZEN.md`  
**Start point:** query refinement is closed.

## Gate A — archive before export

- [ ] Copy exact EBSCO S4 query artifact into the review folder.
- [ ] Copy exact PQDT P2 query artifact into the review folder.
- [ ] Save IEEE I1 exact query and settings.
- [ ] Save ACL script, snapshot commit and A1/A2R dictionaries.
- [ ] Create `PROTOCOL_AMENDMENTS.md` with no amendments initially.
- [ ] Create `RAW_EXPORT_MANIFEST.csv`.

## Gate B — final exports

- [ ] EBSCO S4 full export.
- [ ] PQDT P2 full export.
- [ ] IEEE I1 full export in reproducible batches if required.
- [ ] ACL A1 export.
- [ ] ACL A2R export.
- [ ] Preserve targeted/supplementary records separately.
- [ ] Record exact search/export dates and platform result counts.
- [ ] Hash every raw export.

## Gate C — master merge / dedup

- [ ] Merge records without losing source provenance.
- [ ] Exact DOI dedup.
- [ ] Native-ID dedup.
- [ ] Normalized-title dedup.
- [ ] Title + first-author + year dedup.
- [ ] Fuzzy/manual duplicate review.
- [ ] Preserve conference/journal/dissertation extensions when they may add evidence.
- [ ] Freeze PRISMA identification counts.

## Gate D — title/abstract screening

- [ ] Apply INCLUDE / EXCLUDE / UNCERTAIN only.
- [ ] Do not reuse R1/R2/X as final labels.
- [ ] Double-screen reproducible 20% sample.
- [ ] Double-screen all UNCERTAIN records.
- [ ] Log disagreements/adjudication.
- [ ] Calculate agreement on the double-screened sample.

## Gate E — full-text screening

- [ ] Retrieve lawful full text for all INCLUDE/UNCERTAIN records.
- [ ] Record unavailable full texts separately.
- [ ] Apply E1–E9 exclusion reasons.
- [ ] Independently verify full-text decisions.
- [ ] Produce full-text exclusion table.

## Gate F — extraction

- [ ] Build study-level extraction matrix.
- [ ] Separate multiple records of one study/experiment.
- [ ] Extract morphology intervention.
- [ ] Extract retrieval paradigm.
- [ ] Extract corpus/query/qrels details.
- [ ] Extract metrics/statistics.
- [ ] Extract hybrid controls.
- [ ] Extract complementarity evidence.
- [ ] Assign evidence level 0–5.
- [ ] Keep A/B/C/D source reliability separate.

## Gate G — gap-killer audit

- [ ] Flag fixed-dense + multiple-morphology studies.
- [ ] Check controlled fusion.
- [ ] Check overlap/unique-hit/union/oracle analysis.
- [ ] Check morphology-conditioned hybrid gain.
- [ ] Deep-dive every direct analogue before preserving v0.8.
- [ ] Update CURRENT_GAP/GAP_HISTORY only if evidence requires it.

## Gate H — synthesis

- [ ] Descriptive evidence map.
- [ ] Morphology × retrieval matrix.
- [ ] Language evidence matrix.
- [ ] Quality-domain table.
- [ ] Direction-of-effect synthesis.
- [ ] Complementarity synthesis.
- [ ] Uzbek/Turkic boundary.
- [ ] PRISMA flow.
- [ ] PRISMA-S checklist.

## Gate I — manuscript

- [ ] Results first.
- [ ] Discussion second.
- [ ] Introduction after evidence stabilizes.
- [ ] Abstract last.
- [ ] Final novelty audit.
- [ ] Mandatory update search.
- [ ] Final journal-format adaptation.
