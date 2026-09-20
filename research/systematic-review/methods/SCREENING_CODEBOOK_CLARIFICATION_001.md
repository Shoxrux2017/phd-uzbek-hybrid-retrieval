# SCREENING_CODEBOOK_CLARIFICATION_001

Date: 2026-09-20. Status: PROPOSED clarification; the frozen codebook is unchanged.
This clarifies existing eligibility rules and high-recall handling. It does not
expand or narrow eligibility scope and introduces no new review line.

## A. Retrieval alone does not establish INCLUDE

For INCLUDE, metadata must support in-scope corpus-level text retrieval (or a
relevant review/survey) and a meaningful morphology-related intervention,
problem, representation or analysis. Retrieval metrics, a morphologically rich
language, a neural encoder, lexical/dense comparison, hybrid gains or routine
subwords alone do not establish that link. If morphology relevance is possible
but unestablished, use UNCERTAIN TA8. Use EXCLUDE TA2 only when its absence is
confidently established. A meaningful morphology-related problem or analysis
does not require inventing a new stemmer or reporting a morphology ablation.

## B. The downstream task alone does not establish EXCLUDE

Inspect retrieval within QA, RAG, MT, classification, generation, extraction
and other pipelines separately. An independently evaluated document/passage/text
retrieval stage with possible morphology relevance must not be dismissed just
because the final task differs from IR. Distinguish actual retrieval use from
IR mentioned only as a possible future application. End-task accuracy, BLEU,
fluency or image-ranking metrics are not substitutes for retrieval evidence,
but their presence in an abstract does not prove absence of separate retrieval
measurement. Apply the existing TA1/TA3/TA5 rules to established evidence.

## C. Unresolved metadata require UNCERTAIN, not guessing

If the morphology link, retrieved unit, corpus-level evidence or separability
cannot be determined and relevant retrieval remains reasonably possible, use
UNCERTAIN TA8. Do not infer either eligibility or exclusion from missing detail.
This does not make every auxiliary retriever eligible. Final eligibility and
unreported experiments must not be invented from a title or model name.

## Examples and status

- A: CR000017, CR000061-CR000064, CR000073, CR000089, CR000097-CR000100.
- B/C: CR000044, CR000049, CR000057, CR000059, CR000066, CR000072,
  CR000077, CR000088 and CR000094.
- CR000019 describes stemming accuracy and generic IR motivation; CR000093
  explicitly reports use of the morphology model in IR setups.

The clarification is recorded separately for explicit adoption/versioning.
No amendment to the frozen codebook or new blind pass was performed. Stability
of its future application has not been demonstrated by this adjudication alone.
