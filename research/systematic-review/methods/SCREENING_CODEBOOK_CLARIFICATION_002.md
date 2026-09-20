# SCREENING CODEBOOK CLARIFICATION 002

Date: 2026-09-20. Status: operational clarification adopted for the authorized
modality guard audit and completion of Batch 012.

This is an operational clarification of the existing high-recall rule, not a
change to eligibility scope. The frozen `TITLE_ABSTRACT_SCREENING_CODEBOOK.md`
and `results/batch_001/SCREENING_CODEBOOK_CLARIFICATION_001.md` remain unchanged.
Rules C–G below are local to Clarification 002; references to Clarification 001 C
continue to mean its existing uncertainty rule.

## RULE C — SOURCE MODALITY ≠ RETRIEVAL MODALITY

The presence of speech, audio, spoken language, ASR, acoustic features or voice
does not by itself justify EXCLUDE / TA1 — NOT_TEXT_RETRIEVAL. First identify
the retrieval object and task, including any separately evaluated textual stage.
The modality of the source or user interface does not determine the modality
of retrieval. Part-of-speech, hate speech and grammatical voice can also be
incidental matches rather than descriptions of an acoustic task.

## RULE D — CLEAR NON-TEXT RETRIEVAL

EXCLUDE / TA1 remains correct when metadata clearly establish retrieval directly
over acoustic signals, audio segments, spoken recordings or speech events, with
no text/document/passage/lexical corpus retrieval or relevant textual
indexing/retrieval stage. Establish the mismatch from the stated task and units;
do not infer it from a speech-related keyword or absent methodological detail.

## RULE E — TEXTUAL / LEXICAL REPRESENTATION INSIDE SPEECH PIPELINE

Speech/audio pipelines may use transcripts, word forms, stems, lemmas,
morphemes, subwords, lexical indexes, morphological variants or textual query
representations. If metadata clearly show corpus-level text/word/passage/document
retrieval evaluation, speech origin alone is not an exclusion reason.

If Q1 = YES (in-scope corpus-level textual retrieval evidence) and Q2 = YES
(meaningful morphology-related intervention, problem, representation or analysis),
use INCLUDE. Apply Clarification 001 to component separability and the morphology
gate. The presence of transcripts, subwords or retrieval metrics by itself does
not establish both gates. Existing documented review/context exceptions remain
available; they do not become primary experimental evidence.

## RULE F — MODALITY UNCLEAR

If metadata mention spoken term retrieval, word retrieval, subword retrieval,
lexical retrieval within speech/ASR or morphology-aware speech indexing, but do
not establish whether retrieval is text/document/passage retrieval or purely
acoustic/speech retrieval, use UNCERTAIN / TA8. Do not guess TA1. Leave Q1
UNCLEAR when the retrieved unit or the relevant textual evaluation is unresolved.
Apply this guard to current INCLUDE and UNCERTAIN records as well as EXCLUDE.

## RULE G — WORD/SUBWORD RETRIEVAL IS NOT AUTOMATIC INCLUDE

The phrases word retrieval, subword retrieval and term retrieval do not
automatically establish relevant corpus-level text IR. Clearly established
psycholinguistic lexical access, cognitive word retrieval, speech-event retrieval
or non-text matching remain EXCLUDE under the appropriate existing code.
If the modality/task is unclear and relevant retrieval remains reasonably
possible, use UNCERTAIN / TA8.

Distinguish word-form search in a transcribed text corpus from dictionary-entry
lookup, word translation matching, lexical-resource access and word production
in people. Lexical labels or a large dictionary do not alone establish Q1.
This applies the existing task/unit boundary and introduces no new exclusion code.

## No scope expansion

This clarification does not expand the review to general speech retrieval.
Primary scope remains text/document/passage corpus-level retrieval and separately
evaluated textual retrieval stages. Its purpose is to prevent false EXCLUDE
decisions based only on data origin. It neither admits all speech papers nor
forces unresolved cases into INCLUDE or EXCLUDE.

## Operational use and discovery

Use case-insensitive search of already screened title, abstract, keywords and
subject terms for speech, spoken, audio, acoustic, ASR, automatic speech recognition,
voice, spoken term, speech retrieval, audio retrieval, word retrieval and subword
retrieval. Obvious variants are permitted. Matches only select candidates for
manual inspection of all these fields and the existing rationale. They never
assign a scientific decision. Search rationales/notes as an additional conservative
discovery check, recording any rationale-only matches.

For every candidate, independently inspect Q1 and Q2 within this same primary
screening workflow. Downgrade an unsupported current INCLUDE to UNCERTAIN;
correct an unsupported EXCLUDE to UNCERTAIN. Preserve uncertainty when the
metadata do not settle the issue. This is not an independent second review,
blind recalibration, or an agreement-metric exercise.

## Canonical decision precedence and immutable history

For a future merged screening master, use:

**latest explicit correction ledger > batch final screening file > older preliminary file**.

Correction ledgers are overlays keyed by unchanged canonical_id, not edits to
historical artifacts. For any corrected finalized record, preserve its old label
and code, record its new label/code and evidence basis, date and clarification.
Use explicit ledger version/order as well as date if several ledgers share a date;
do not infer precedence from filesystem modification time.

`SCREENING_CORRECTIONS_CLARIFICATION_002.csv` is immutable once issued. Later
corrections require a new explicit ledger. Batch 012 gets a separate final file;
its preliminary file and the original STOP report remain historical evidence.

## Audit examples

- CR000271: explicit search for word-form variants in transcribed Estonian text;
  the speech source does not prevent INCLUDE.
- CR001374: heart-sound audio-envelope matching is clearly NON_TEXT; retain TA1.
- CR000042: human naming/recall is cognitive word retrieval; retain TA1.
- CR000153: ASR decoder states retrieve keyword-dictionary entries for biasing;
  textual keywords and recall were considered, but the explicitly defined unit
  remains dictionary entries rather than a textual corpus retrieval stage.
- CR000691: text indexes and segmentation are present, but the retrieved units
  and retrieval types are insufficiently specified; use UNCERTAIN / TA8.
- CR001338, CR001388 and CR001390: morphology-sensitive word/subword retrieval
  is plausible, while the text-versus-speech-event boundary is unresolved;
  retain UNCERTAIN / TA8.
