# Structural Rules Validation — Annotation Guide

## Important

Annotate **only `validation_blind.csv`**.

Do **not** open `validation_key.csv` until every row is annotated.  
Otherwise the audit is no longer blind.

## Allowed human labels

Enter exactly one of:

- `PROSE_LIKE`
- `CLEANABLE_MARKUP`
- `SEVERE_STRUCTURAL`
- `UNCERTAIN`

## How to decide

### PROSE_LIKE

The unit is essentially normal readable text.

It may contain ordinary:
- dates;
- numbers;
- names;
- citations;
- abbreviations.

The text should still read as coherent prose or a naturally readable text unit.

### CLEANABLE_MARKUP

The useful text is largely normal/readable, but it contains obvious removable technical residue such as:

- `thumb|300x300px|`
- `link=Fayl:...`
- image/layout markers;
- raw URL strings.

Ask:

> If the obvious markup is removed, is the remaining text still a useful coherent retrieval unit?

If yes, use `CLEANABLE_MARKUP`.

### SEVERE_STRUCTURAL

The unit is substantially damaged or dominated by collapsed structure, for example:

- table columns glued together;
- sports/statistical rows collapsed into one string;
- identifiers/codes concatenated with names;
- large infobox fields glued together;
- extremely long technical strings;
- simple markup removal would **not** recover a normal coherent unit.

Use this label only when the structural problem is material, not merely because one image marker exists.

### UNCERTAIN

Use when you genuinely cannot decide between classes.

Do not force an uncertain example into another class.

## What NOT to use in judgment

Do not consider:

- E5 token counts;
- BGE-M3 token counts;
- BM25;
- retrieval scores;
- qrels;
- nDCG/Recall;
- whether a document would help the expected hypothesis.

This audit is only about surface/structural data quality.

## Pilot interpretation

This first audit is a **pilot**.

It is meant to reveal whether the rules have systematic false positives or false negatives. Even excellent pilot results do not immediately authorize automatic deletion; a larger confirmation sample follows before freeze.
