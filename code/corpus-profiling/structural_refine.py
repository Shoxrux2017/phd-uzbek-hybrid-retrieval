#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Refined structural-quality audit for the Uzbek hybrid retrieval corpus.

Purpose
-------
Separate three different situations without using qrels or retrieval effectiveness:

1) CLEANABLE_MARKUP:
   mostly usable prose containing removable technical wiki/URL/image markup;

2) SEVERE_STRUCTURAL:
   collapsed tables / glued fields / abnormally long technical surface tokens;

3) PROSE_LIKE:
   no severe surface-structure signal.

The classification uses only surface-format features. E5 is used afterwards
only to measure whether token overflow remains after deterministic markup cleanup.

This script does NOT modify source files.
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import Counter
from pathlib import Path
from typing import Dict, Any, List

import corpus_profile as cp



def normalize_for_structure_audit(text: str) -> tuple[str, bool]:
    """Remove obvious technical residue before judging severe structure.

    This is model-independent and does not use retrieval outcomes.
    """
    s = text or ""
    original = s

    # URLs and raw web links.
    s = re.sub(r"(?i)https?://\S+", " ", s)
    s = re.sub(r"(?i)\bwww\.\S+", " ", s)

    # Wikimedia/image/layout residue.
    s = re.sub(r"(?i)\blink=//upload\.wikimedia\.org/\S+", " ", s)
    s = re.sub(r"(?i)\blink=Fayl:[^\s]+", " ", s)
    s = re.sub(r"(?i)\bFayl:[^\s]+", " ", s)
    s = re.sub(
        r"(?i)\b(?:right|left|center)\|thumb\|[0-9]{2,4}x[0-9]{2,4}px\|",
        " ",
        s,
    )
    s = re.sub(r"(?i)\bthumb\|[0-9]{2,4}x[0-9]{2,4}px\|", " ", s)
    s = re.sub(r"(?i)\b(?:frameless|thumb|right|left|center)\|", " ", s)
    s = re.sub(r"(?i)\balt=[^|\s]*\|", " ", s)
    s = re.sub(r"(?i)\b[0-9]{2,4}x[0-9]{2,4}px\|", " ", s)

    # Long form blanks are placeholders, not structural corruption.
    s = re.sub(r"[_＿]{8,}", " ", s)

    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n{3,}", "\n\n", s).strip()

    return s, (s != original.strip())


def _token_glue_features(token: str) -> Dict[str, Any]:
    t = token or ""
    transitions = len(
        re.findall(
            r"(?i)(?:[A-Za-zÀ-žʻʼ‘’'`][0-9]|[0-9][A-Za-zÀ-žʻʼ‘’'`])",
            t,
        )
    )
    digit_ratio = sum(ch.isdigit() for ch in t) / max(1, len(t))
    return {
        "len": len(t),
        "transitions": transitions,
        "digit_ratio": digit_ratio,
    }


def surface_features(text: str) -> Dict[str, Any]:
    raw = text or ""
    cleaned, had_cleanable_markup = normalize_for_structure_audit(raw)

    words = cleaned.split()
    chars = max(1, len(cleaned))
    longest = max(words, key=len) if words else ""

    digit_ratio = sum(ch.isdigit() for ch in cleaned) / chars
    alpha_ratio = sum(ch.isalpha() for ch in cleaned) / chars

    token_feats = [_token_glue_features(w) for w in words]
    transitions = sum(f["transitions"] for f in token_feats)
    long_digit_runs = len(re.findall(r"\d{8,}", cleaned))

    # Conservative precision-first severe evidence.
    suspicious_glued = [
        f for f in token_feats
        if (
            (f["len"] >= 50 and f["transitions"] >= 3)
            or (f["len"] >= 40 and f["digit_ratio"] >= 0.35 and f["transitions"] >= 2)
        )
    ]
    very_long_residual = [f for f in token_feats if f["len"] >= 80]
    long_residual = [f for f in token_feats if f["len"] >= 40]

    severe = bool(
        very_long_residual
        or suspicious_glued
        or (
            len(long_residual) >= 2
            and digit_ratio >= 0.08
        )
        or (
            long_digit_runs >= 2
            and any(f["len"] >= 30 and f["transitions"] >= 2 for f in token_feats)
        )
    )

    raw_markup = bool(
        re.search(
            r"(?i)(?:\blink=|\bFayl:|upload\.wikimedia|wikimedia\.org|"
            r"\bframeless\b|\bthumb\b|\balt=|[0-9]{2,4}x[0-9]{2,4}px|"
            r"https?://|\bwww\.|[_＿]{8,})",
            raw,
        )
    )
    markup = bool(raw_markup or had_cleanable_markup)

    if severe:
        label = "SEVERE_STRUCTURAL"
    elif markup:
        label = "CLEANABLE_MARKUP"
    else:
        label = "PROSE_LIKE"

    return {
        "label": label,
        "severe": severe,
        "markup": markup,
        "words": len(words),
        "max_word_len": len(longest),
        "digit_ratio": digit_ratio,
        "alpha_ratio": alpha_ratio,
        "alpha_digit_transitions": transitions,
        "long_digit_runs": long_digit_runs,
        "long40": len(long_residual),
        "long80": len(very_long_residual),
        "file_markup_count": len(re.findall(r"(?i)\blink=Fayl:", raw)),
        "thumb_markup_count": len(re.findall(r"(?i)\bthumb\b", raw)),
        "px_markup_count": len(re.findall(r"(?i)[0-9]{2,4}x[0-9]{2,4}px", raw)),
        "repeated_markup_structure": False,
        "suspicious_glued_token_count": len(suspicious_glued),
        "longest": longest,
    }


def clean_inline_markup(text: str) -> str:
    """Deterministic cleanup of obvious technical markup/placeholders only."""
    cleaned, _ = normalize_for_structure_audit(text)
    return cleaned


def write_csv(path: Path, rows: List[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8-sig")
        return
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--sample-cache", type=Path, required=True)
    p.add_argument("--word-limits", type=int, nargs="+", default=[120, 130, 140])
    p.add_argument("--output-dir", type=Path, required=True)
    p.add_argument("--example-cap", type=int, default=50)
    p.add_argument("--e5-model", default="intfloat/multilingual-e5-large")
    p.add_argument("--e5-max-tokens", type=int, default=512)
    args = p.parse_args()

    data = cp.read_sample_cache(args.sample_cache)
    e5 = cp.TransformersTokenCounter(
        args.e5_model,
        "e5",
        args.e5_max_tokens,
        e5_prefix=True,
    )

    summary_rows: List[Dict[str, Any]] = []
    example_rows: List[Dict[str, Any]] = []
    residual_rows: List[Dict[str, Any]] = []

    for source in ("wikipedia", "news", "legal"):
        if source not in data:
            continue
        docs, total_seen = data[source]

        for limit in args.word_limits:
            records = []
            texts_raw = []
            texts_clean = []

            for doc in docs:
                chunks = cp.segment_document(doc.title, doc.text, limit)
                for chunk_index, chunk in enumerate(chunks, start=1):
                    feat = surface_features(chunk)
                    cleaned = clean_inline_markup(chunk) if feat["markup"] else chunk
                    records.append((doc, chunk_index, chunk, cleaned, feat))
                    texts_raw.append(chunk)
                    texts_clean.append(cleaned)

            raw_counts = e5.count_many(texts_raw, is_document=True)
            clean_counts = e5.count_many(texts_clean, is_document=True)

            c = Counter(r[4]["label"] for r in records)
            raw_over = 0
            residual_nonsevere_over = 0
            nonsevere_n = 0
            severe_n = 0
            markup_n = 0

            per_label_examples = Counter()

            for (doc, chunk_index, raw, cleaned, feat), n_raw, n_clean in zip(
                records, raw_counts, clean_counts
            ):
                if n_raw > args.e5_max_tokens:
                    raw_over += 1

                if feat["severe"]:
                    severe_n += 1
                else:
                    nonsevere_n += 1
                    if n_clean > args.e5_max_tokens:
                        residual_nonsevere_over += 1
                        residual_rows.append({
                            "source": source,
                            "word_limit": limit,
                            "doc_id": doc.doc_id,
                            "category": doc.category,
                            "chunk_index": chunk_index,
                            "label": feat["label"],
                            "words": feat["words"],
                            "raw_e5_tokens": int(n_raw),
                            "clean_e5_tokens": int(n_clean),
                            "max_word_len": feat["max_word_len"],
                            "digit_ratio": round(feat["digit_ratio"], 4),
                            "alpha_digit_transitions": feat["alpha_digit_transitions"],
                            "file_markup_count": feat["file_markup_count"],
                            "repeated_markup_structure": feat["repeated_markup_structure"],
                            "title": doc.title,
                            "snippet": cleaned[:500].replace("\n", " "),
                        })

                if feat["label"] == "CLEANABLE_MARKUP":
                    markup_n += 1

                label = feat["label"]
                if per_label_examples[label] < args.example_cap:
                    example_rows.append({
                        "source": source,
                        "word_limit": limit,
                        "doc_id": doc.doc_id,
                        "category": doc.category,
                        "chunk_index": chunk_index,
                        "label": label,
                        "words": feat["words"],
                        "raw_e5_tokens": int(n_raw),
                        "clean_e5_tokens": int(n_clean),
                        "max_word_len": feat["max_word_len"],
                        "digit_ratio": round(feat["digit_ratio"], 4),
                        "alpha_digit_transitions": feat["alpha_digit_transitions"],
                        "long_digit_runs": feat["long_digit_runs"],
                        "file_markup_count": feat["file_markup_count"],
                        "thumb_markup_count": feat["thumb_markup_count"],
                        "px_markup_count": feat["px_markup_count"],
                        "repeated_markup_structure": feat["repeated_markup_structure"],
                        "title": doc.title,
                        "snippet": raw[:500].replace("\n", " "),
                    })
                    per_label_examples[label] += 1

            total_units = len(records)
            summary_rows.append({
                "source": source,
                "word_limit": limit,
                "source_docs_sampled": len(docs),
                "retrieval_units": total_units,
                "prose_like_units": c["PROSE_LIKE"],
                "cleanable_markup_units": c["CLEANABLE_MARKUP"],
                "severe_structural_units": c["SEVERE_STRUCTURAL"],
                "cleanable_markup_pct": round(100 * c["CLEANABLE_MARKUP"] / max(1, total_units), 4),
                "severe_structural_pct": round(100 * c["SEVERE_STRUCTURAL"] / max(1, total_units), 4),
                "raw_e5_overflow_units": raw_over,
                "raw_e5_overflow_pct": round(100 * raw_over / max(1, total_units), 4),
                "residual_nonsevere_overflow_units_after_markup_clean": residual_nonsevere_over,
                "residual_nonsevere_overflow_pct_after_markup_clean": round(
                    100 * residual_nonsevere_over / max(1, nonsevere_n), 4
                ),
            })

    args.output_dir.mkdir(parents=True, exist_ok=True)
    write_csv(args.output_dir / "refined_structural_summary.csv", summary_rows)
    write_csv(args.output_dir / "refined_structural_examples.csv", example_rows)
    write_csv(args.output_dir / "residual_nonsevere_e5_overflow.csv", residual_rows)

    print("# Refined Structural Audit")
    print()
    print(
        "| Source | Limit | Units | Cleanable markup % | Severe structural % | "
        "Raw E5 overflow % | Residual non-severe overflow % |"
    )
    print("|---|---:|---:|---:|---:|---:|---:|")
    for r in summary_rows:
        print(
            f"| {r['source']} | {r['word_limit']} | {r['retrieval_units']} | "
            f"{r['cleanable_markup_pct']:.2f} | {r['severe_structural_pct']:.2f} | "
            f"{r['raw_e5_overflow_pct']:.2f} | "
            f"{r['residual_nonsevere_overflow_pct_after_markup_clean']:.4f} |"
        )

    print()
    print("Residual non-severe E5 overflow units after markup cleanup:", len(residual_rows))
    print("Outputs:", args.output_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
