# Chapter I Status

**Working version:** v0.9  
**Date:** 2026-08-31

## Title

> **АНАЛИЗ МЕТОДОВ И МОДЕЛЕЙ ЛЕКСИЧЕСКОГО, СЕМАНТИЧЕСКОГО И ГИБРИДНОГО ИНФОРМАЦИОННОГО ПОИСКА**

## Sections

### 1.1
Теоретические основы и модели лексического информационного поиска.

Status: working final text created.

Core conclusions:

- lexical retrieval remains relevant;
- BM25 strong baseline;
- learned sparse matters;
- Uzbek morphology/script variation affect lexical representation;
- morphology normalization reduces form mismatch but not semantic mismatch.

### 1.2
Современные методы и модели семантического поиска текстовой информации.

Status: working final text created and updated with 2026 Uzbek retrieval evidence.

Core conclusions:

- semantic representation does not equal retriever;
- cross-encoder / bi-encoder / late interaction differ by interaction/scalability;
- dense retrieval solves part of vocabulary mismatch but has exact/rare-detail limitations;
- Uzbek semantic infrastructure exists;
- Uzbek semantic retrieval has direct IR evaluation in some 2026 specialized tasks;
- pure semantic retrieval cannot be assumed optimal without comparison.

### 1.3
Методы интеграции лексических и семантических моделей в гибридном поиске текстов на узбекском языке.

Status: working final text created.

Core conclusions:

- hybrid methods exist at score/rank/learned/representation/query-adaptive levels;
- RRF/fixed fusion/dynamic alpha are known methods;
- Uzbek hybrid/RAG exists;
- gap must concern missing understanding of complementarity, not absence of hybrid search.

## Current volume

Word layout used:

- A4;
- Times New Roman 14;
- 1.5 spacing;
- margins 30/15/20/20 mm.

Approximate pages:

- 1.1: 9
- 1.2: 13
- 1.3: 10
- conclusions: 3
- total without bibliography: ~35.

## Decision

Do **not** perform page-count compression yet.

Reason:

Before shortening, deeply re-check the closest scientific works. The gap and chapter content may change.

## Next chapter-I maintenance after deep dives

- update claims that are narrowed/contradicted;
- reduce repeated explanation;
- citation/metadata audit;
- terminology normalization;
- only then decide final page target.
