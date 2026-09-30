# Corpus Profiling Report

**Status:** screening / pre-freeze evidence only

This report profiles source-document lengths and candidate canonical retrieval-unit limits. It does not use qrels or retrieval effectiveness and must not be treated as an experiment result.

## Run configuration

- Sample per source: `10000`
- Seed: `20260916`
- Candidate word limits: `150, 180, 200, 220`
- E5 model: `intfloat/multilingual-e5-large` (max `512` tokens)
- BGE-M3 model: `BAAI/bge-m3` (max `8192` tokens)
- Tokenizer profiling skipped: `True`

## Source-document profile

| Source | Seen | Sample | Words P50 | P90 | P95 | P99 | Max | Exact dup % | Mixed script % |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| wikipedia | 2 | 2 | 371.00 | 652.60 | 687.80 | 715.96 | 723 | 0.00 | 0.00 |
| news | 2 | 2 | 152.00 | 253.60 | 266.30 | 276.46 | 279 | 0.00 | 0.00 |
| legal | 2 | 2 | 416.50 | 729.70 | 768.85 | 800.17 | 808 | 0.00 | 0.00 |

## Candidate segmentation profile

| Source | Limit words | Units | Mean units/doc | Whole doc % | Unit words P99 | E5 P99 | E5 overflow % | BGE-M3 P99 | BGE overflow % |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| wikipedia | 150 | 6 | 3.00 | 50.00 | 147.00 | NA | NA | NA | NA |
| wikipedia | 180 | 6 | 3.00 | 50.00 | 179.90 | NA | NA | NA | NA |
| wikipedia | 200 | 5 | 2.50 | 50.00 | 197.92 | NA | NA | NA | NA |
| wikipedia | 220 | 5 | 2.50 | 50.00 | 219.00 | NA | NA | NA | NA |
| news | 150 | 3 | 1.50 | 50.00 | 141.00 | NA | NA | NA | NA |
| news | 180 | 3 | 1.50 | 50.00 | 174.60 | NA | NA | NA | NA |
| news | 200 | 3 | 1.50 | 50.00 | 196.68 | NA | NA | NA | NA |
| news | 220 | 3 | 1.50 | 50.00 | 207.24 | NA | NA | NA | NA |
| legal | 150 | 7 | 3.50 | 50.00 | 147.58 | NA | NA | NA | NA |
| legal | 180 | 6 | 3.00 | 50.00 | 180.00 | NA | NA | NA | NA |
| legal | 200 | 6 | 3.00 | 50.00 | 193.65 | NA | NA | NA | NA |
| legal | 220 | 5 | 2.50 | 50.00 | 216.72 | NA | NA | NA | NA |

## Mechanical screening recommendation

**No retrieval-unit limit is frozen.** Run with the exact E5 tokenizer (or local SentencePiece model) before freezing a limit.

## Required interpretation checks before freeze

1. Prefer a limit with effectively zero E5 truncation risk on every source, not only on the pooled average.
2. Inspect P95/P99 and worst cases separately for Wikipedia, News and Legal.
3. Keep the same canonical retrieval-unit text/IDs for BM25_raw, BM25_stem, BM25_lemma and dense retrieval.
4. Do not introduce overlap in the primary segmentation without a separate methodological justification.
5. Exact duplicates in this report are sample diagnostics; full cross-source/near-duplicate resolution is a separate corpus-freeze task.
6. Re-run the final candidate segmentation over the full corpus before Corpus v0.1 is frozen.
