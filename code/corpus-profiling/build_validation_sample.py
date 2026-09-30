#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Build a blinded, stratified manual-validation sample for structural rules.

Run beside:
- corpus_profile.py
- structural_refine.py v0.2

Inputs:
- local sample cache previously created by corpus_profile.py

Outputs:
- validation_blind.csv   -> human annotator works ONLY with this file
- validation_key.csv     -> hidden algorithm labels; do not open before annotation
- validation_manifest.json
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import random
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Any

import corpus_profile as cp
import structural_refine as sr


ALLOWED_LABELS = {
    "PROSE_LIKE",
    "CLEANABLE_MARKUP",
    "SEVERE_STRUCTURAL",
    "UNCERTAIN",
}


def stable_id(source: str, doc_id: str, chunk_index: int, text: str) -> str:
    raw = f"{source}\n{doc_id}\n{chunk_index}\n{text}".encode("utf-8")
    return hashlib.sha256(raw).hexdigest()[:16]


def write_csv(path: Path, rows: List[Dict[str, Any]]) -> None:
    if not rows:
        path.write_text("", encoding="utf-8-sig")
        return
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--sample-cache", type=Path, required=True)
    p.add_argument("--word-limit", type=int, default=120)
    p.add_argument("--per-stratum", type=int, default=20)
    p.add_argument("--seed", type=int, default=20260917)
    p.add_argument("--output-dir", type=Path, required=True)
    p.add_argument(
        "--exclude-blind",
        type=Path,
        help="Optional previous validation_blind.csv; its sample_id values are excluded from the new sample",
    )
    args = p.parse_args()

    excluded_ids = set()
    if args.exclude_blind:
        with args.exclude_blind.open(encoding="utf-8-sig", newline="") as f:
            for row in csv.DictReader(f):
                sid = (row.get("sample_id") or "").strip()
                if sid:
                    excluded_ids.add(sid)

    data = cp.read_sample_cache(args.sample_cache)
    rng = random.Random(args.seed)

    strata = defaultdict(list)

    for source in ("wikipedia", "news", "legal"):
        if source not in data:
            continue
        docs, _ = data[source]

        for doc in docs:
            chunks = cp.segment_document(doc.title, doc.text, args.word_limit)
            for idx, chunk in enumerate(chunks, start=1):
                feat = sr.surface_features(chunk)
                pred = feat["label"]
                if pred not in {"PROSE_LIKE", "CLEANABLE_MARKUP", "SEVERE_STRUCTURAL"}:
                    continue

                cleaned = (
                    sr.clean_inline_markup(chunk)
                    if pred == "CLEANABLE_MARKUP"
                    else chunk
                )

                sid = stable_id(source, doc.doc_id, idx, chunk)
                if sid in excluded_ids:
                    continue
                strata[(source, pred)].append({
                    "sample_id": sid,
                    "source": source,
                    "doc_id": doc.doc_id,
                    "category": doc.category,
                    "chunk_index": idx,
                    "title": doc.title,
                    "raw_text": chunk,
                    "cleaned_text_if_markup": cleaned,
                    "predicted_label": pred,
                    "max_word_len": feat["max_word_len"],
                    "digit_ratio": round(feat["digit_ratio"], 4),
                    "alpha_digit_transitions": feat["alpha_digit_transitions"],
                    "file_markup_count": feat.get("file_markup_count", 0),
                    "repeated_markup_structure": feat.get("repeated_markup_structure", False),
                })

    selected = []
    stratum_counts = {}

    for key in sorted(strata):
        rows = strata[key]
        rng.shuffle(rows)
        take = min(args.per_stratum, len(rows))
        chosen = rows[:take]
        selected.extend(chosen)
        stratum_counts[f"{key[0]}::{key[1]}"] = {
            "available": len(rows),
            "selected": take,
        }

    # Blind the annotator to algorithm labels and diagnostics.
    blind_rows = []
    key_rows = []

    for row in selected:
        blind_rows.append({
            "sample_id": row["sample_id"],
            "source": row["source"],
            "title": row["title"],
            "raw_text": row["raw_text"],
            "cleaned_text_if_markup": row["cleaned_text_if_markup"],
            "human_label": "",
            "human_notes": "",
        })

        key_rows.append({
            "sample_id": row["sample_id"],
            "source": row["source"],
            "doc_id": row["doc_id"],
            "category": row["category"],
            "chunk_index": row["chunk_index"],
            "predicted_label": row["predicted_label"],
            "max_word_len": row["max_word_len"],
            "digit_ratio": row["digit_ratio"],
            "alpha_digit_transitions": row["alpha_digit_transitions"],
            "file_markup_count": row["file_markup_count"],
            "repeated_markup_structure": row["repeated_markup_structure"],
        })

    # Randomize global row order after stratified sampling.
    order = list(range(len(blind_rows)))
    rng.shuffle(order)
    blind_rows = [blind_rows[i] for i in order]
    key_by_id = {r["sample_id"]: r for r in key_rows}
    key_rows = [key_by_id[r["sample_id"]] for r in blind_rows]

    args.output_dir.mkdir(parents=True, exist_ok=True)
    write_csv(args.output_dir / "validation_blind.csv", blind_rows)
    write_csv(args.output_dir / "validation_key.csv", key_rows)

    manifest = {
        "status": "pilot_manual_validation",
        "word_limit": args.word_limit,
        "per_stratum_target": args.per_stratum,
        "seed": args.seed,
        "total_selected": len(blind_rows),
        "excluded_previous_sample_ids": len(excluded_ids),
        "strata": stratum_counts,
        "annotation_labels": sorted(ALLOWED_LABELS),
        "important": [
            "Do not open validation_key.csv before human annotation is finished.",
            "Human judgment must not use E5/BGE token counts, qrels, retrieval scores, or effectiveness.",
            "UNCERTAIN is allowed and should not be forced into another class.",
        ],
    }

    (args.output_dir / "validation_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print("Validation sample created.")
    print("Total blinded rows:", len(blind_rows))
    print("Excluded previous sample IDs:", len(excluded_ids))
    print("Blind file:", args.output_dir / "validation_blind.csv")
    print("Hidden key:", args.output_dir / "validation_key.csv")
    print()
    print("IMPORTANT: annotate validation_blind.csv only.")
    print("Do NOT open validation_key.csv until annotation is complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
