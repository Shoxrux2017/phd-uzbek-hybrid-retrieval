#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Score blinded human validation after annotation is complete.

Inputs:
- validation_blind.csv with human_label filled
- validation_key.csv hidden algorithm predictions
"""

from __future__ import annotations

import argparse
import csv
import math
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, List, Tuple


CLASSES = ["PROSE_LIKE", "CLEANABLE_MARKUP", "SEVERE_STRUCTURAL"]


def read_csv(path: Path) -> List[Dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def wilson(successes: int, n: int, z: float = 1.96) -> Tuple[float, float]:
    if n <= 0:
        return (float("nan"), float("nan"))
    p = successes / n
    denom = 1 + z*z/n
    center = (p + z*z/(2*n)) / denom
    half = z * math.sqrt((p*(1-p)/n) + (z*z/(4*n*n))) / denom
    return max(0.0, center-half), min(1.0, center+half)


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--blind", type=Path, required=True)
    p.add_argument("--key", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()

    blind = read_csv(args.blind)
    key = {r["sample_id"]: r for r in read_csv(args.key)}

    pairs = []
    uncertain = 0
    missing = 0

    for r in blind:
        sid = r["sample_id"]
        human = r.get("human_label", "").strip().upper()
        if not human:
            missing += 1
            continue
        if human == "UNCERTAIN":
            uncertain += 1
            continue
        if human not in CLASSES:
            raise SystemExit(
                f"ERROR: invalid human_label '{human}' for sample_id={sid}"
            )
        pred = key[sid]["predicted_label"]
        source = r["source"]
        pairs.append((source, pred, human, sid))

    confusion = {
        pred: {human: 0 for human in CLASSES}
        for pred in CLASSES
    }
    for _, pred, human, _ in pairs:
        confusion[pred][human] += 1

    lines = [
        "# Structural Rules Manual Validation",
        "",
        f"- Scored rows: **{len(pairs)}**",
        f"- UNCERTAIN excluded from metrics: **{uncertain}**",
        f"- Missing human labels: **{missing}**",
        "",
        "## Confusion matrix",
        "",
        "| Predicted \\ Human | PROSE_LIKE | CLEANABLE_MARKUP | SEVERE_STRUCTURAL |",
        "|---|---:|---:|---:|",
    ]

    for pred in CLASSES:
        lines.append(
            f"| {pred} | "
            f"{confusion[pred]['PROSE_LIKE']} | "
            f"{confusion[pred]['CLEANABLE_MARKUP']} | "
            f"{confusion[pred]['SEVERE_STRUCTURAL']} |"
        )

    lines += ["", "## Per-class metrics", ""]

    for cls in CLASSES:
        tp = sum(1 for _, p_, h_, _ in pairs if p_ == cls and h_ == cls)
        fp = sum(1 for _, p_, h_, _ in pairs if p_ == cls and h_ != cls)
        fn = sum(1 for _, p_, h_, _ in pairs if p_ != cls and h_ == cls)

        precision = tp / (tp + fp) if tp + fp else float("nan")
        recall = tp / (tp + fn) if tp + fn else float("nan")
        f1 = (
            2 * precision * recall / (precision + recall)
            if precision == precision and recall == recall and precision + recall
            else float("nan")
        )

        lo, hi = wilson(tp, tp + fp)

        lines += [
            f"### {cls}",
            "",
            f"- Precision: **{precision:.3f}** "
            f"(95% Wilson CI {lo:.3f}–{hi:.3f})",
            f"- Recall: **{recall:.3f}**",
            f"- F1: **{f1:.3f}**",
            f"- TP / FP / FN: `{tp} / {fp} / {fn}`",
            "",
        ]

    severe_pred = [
        (s, h, sid) for s, p_, h, sid in pairs if p_ == "SEVERE_STRUCTURAL"
    ]
    severe_fp = [
        (s, h, sid) for s, h, sid in severe_pred if h != "SEVERE_STRUCTURAL"
    ]

    lines += [
        "## Pilot decision rule",
        "",
        "This pilot does **not** authorize automatic deletion by itself.",
        "",
        "Before the labels were inspected, use this operational interpretation:",
        "",
        "- If `SEVERE_STRUCTURAL` precision < 0.90, revise the rules.",
        "- If precision is 0.90–0.95, inspect false-positive patterns and revise/expand validation.",
        "- If precision >= 0.95 with no recurring false-positive pattern, proceed to a larger confirmation sample before freezing automatic exclusion.",
        "- Any systematic false-positive class (for example normal legal prose repeatedly flagged severe) triggers rule revision regardless of aggregate precision.",
        "",
        f"Observed severe false positives in scored pilot: **{len(severe_fp)}**",
        "",
        "## Source-specific severe diagnostics",
        "",
    ]

    by_source = defaultdict(lambda: Counter())
    for source, pred, human, _ in pairs:
        if pred == "SEVERE_STRUCTURAL":
            by_source[source]["predicted_severe"] += 1
            if human == "SEVERE_STRUCTURAL":
                by_source[source]["correct_severe"] += 1

    lines += [
        "| Source | Predicted severe | Human-agreed severe | Precision |",
        "|---|---:|---:|---:|",
    ]
    for source in sorted(by_source):
        n = by_source[source]["predicted_severe"]
        ok = by_source[source]["correct_severe"]
        pr = ok / n if n else float("nan")
        lines.append(f"| {source} | {n} | {ok} | {pr:.3f} |")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))
    print()
    print("Saved:", args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
