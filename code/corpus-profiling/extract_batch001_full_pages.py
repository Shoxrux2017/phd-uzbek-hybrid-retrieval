#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extract full raw wikitext + full extracted text for the 35 calibration cases from
Uzbek Wikipedia batch_001 that were marked NEEDS_FULL_PAGE_REVIEW.

Purpose
-------
This is a read-only evidence extraction step for taxonomy calibration.
It does NOT clean, classify, segment, or modify the Wikipedia dump.

Extraction is intentionally identical to W-DISCOVERY-v0.3:
    mwparserfromhell.parse(raw).strip_code(normalize=True, collapse=True)
followed by NFC and newline normalization.

Python 3.12+
Dependencies:
    pip install lxml mwparserfromhell
"""

from __future__ import annotations

import argparse
import bz2
import hashlib
import importlib.metadata
import json
import platform
import time
import unicodedata
from pathlib import Path
from typing import Any, Dict, Iterator, List, Tuple

SCRIPT_VERSION = "W-FULLPAGE-CALIBRATION-v0.1"
EXPECTED_COUNT = 35

# Exact IDs listed in BATCH_001_FINDINGS.md under NEEDS_FULL_PAGE_REVIEW.
TARGET_PAGE_IDS: Tuple[str, ...] = (
    # Boundaries/context of source-content intrusions
    "739672", "716089",

    # Local damage / table alignment / lost fields
    "907708", "813223", "812737", "956540", "810294", "1254138",
    "827719", "1407389", "1030837", "959863", "1213772", "826666",
    "1084716", "793485", "1267040",

    # Heavy relationship loss in catalogues/tables
    "1219012", "667599", "822957", "667586", "1254567", "818068", "698038",

    # Unshown fields / boundaries of source templates/cards
    "694861", "694769", "694538", "694781", "694772", "694547", "694540", "694851",

    # Preservation of unshown parts of otherwise readable lists
    "1336760", "1027230", "789306",
)


def sha256_text(text: str) -> str:
    return hashlib.sha256((text or "").encode("utf-8")).hexdigest()


def file_sha256(path: Path, block_size: int = 8 * 1024 * 1024) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        while True:
            block = fh.read(block_size)
            if not block:
                break
            h.update(block)
    return h.hexdigest()


def version_or_unknown(dist: str) -> str:
    try:
        return importlib.metadata.version(dist)
    except Exception:
        return "unknown"


def find_child_text(elem: Any, local: str) -> str:
    node = elem.find(f"{{*}}{local}")
    return "" if node is None or node.text is None else node.text


def page_record(elem: Any) -> Dict[str, Any]:
    title = find_child_text(elem, "title")
    ns = find_child_text(elem, "ns")
    page_id = find_child_text(elem, "id") or title

    redirect_node = elem.find("{*}redirect")
    is_redirect = redirect_node is not None
    redirect_title = redirect_node.get("title") if redirect_node is not None else ""

    rev = elem.find("{*}revision")
    has_revision = rev is not None
    text_node = rev.find("{*}text") if rev is not None else None
    has_text_node = text_node is not None
    raw = ""
    if text_node is not None and text_node.text is not None:
        raw = text_node.text

    return {
        "page_id": str(page_id),
        "title": title,
        "namespace": ns,
        "is_redirect": is_redirect,
        "redirect_title": redirect_title or "",
        "has_revision": has_revision,
        "has_text_node": has_text_node,
        "raw": raw,
    }


def iter_pages(path: Path) -> Iterator[Any]:
    try:
        from lxml import etree  # type: ignore
    except ImportError as exc:
        raise RuntimeError("Missing dependency: pip install lxml") from exc

    opener = bz2.open if path.suffix.lower() == ".bz2" else open
    with opener(path, "rb") as fh:  # type: ignore[arg-type]
        context = etree.iterparse(
            fh,
            events=("end",),
            tag="{*}page",
            recover=True,
            huge_tree=True,
        )
        for _, elem in context:
            yield elem
            elem.clear()
            parent = elem.getparent()
            if parent is not None:
                while elem.getprevious() is not None:
                    del parent[0]


def extract_plain_text(raw: str) -> str:
    import mwparserfromhell  # type: ignore

    code = mwparserfromhell.parse(raw or "")
    extracted = code.strip_code(normalize=True, collapse=True)
    extracted = unicodedata.normalize("NFC", extracted or "")
    extracted = extracted.replace("\r\n", "\n").replace("\r", "\n")
    return extracted


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Extract full raw/extracted text for batch_001 full-page calibration cases."
    )
    p.add_argument("--wikipedia", type=Path, required=True)
    p.add_argument("--output-dir", type=Path, required=True)
    p.add_argument("--progress-every", type=int, default=50000)
    return p.parse_args()


def main() -> int:
    args = parse_args()

    if len(TARGET_PAGE_IDS) != EXPECTED_COUNT:
        raise RuntimeError(
            f"Internal target list mismatch: expected {EXPECTED_COUNT}, "
            f"got {len(TARGET_PAGE_IDS)}"
        )
    if len(set(TARGET_PAGE_IDS)) != EXPECTED_COUNT:
        raise RuntimeError("Internal target page-ID list contains duplicates.")

    if not args.wikipedia.exists():
        print(f"ERROR: Wikipedia dump not found: {args.wikipedia}")
        return 2

    try:
        import lxml  # noqa: F401
        import mwparserfromhell  # noqa: F401
    except Exception:
        print("ERROR: install dependencies: pip install lxml mwparserfromhell")
        return 3

    args.output_dir.mkdir(parents=True, exist_ok=True)

    started = time.time()
    print(f"[{SCRIPT_VERSION}] hashing input dump...")
    dump_hash = file_sha256(args.wikipedia)
    print(f"[{SCRIPT_VERSION}] input SHA-256: {dump_hash}")

    targets = set(TARGET_PAGE_IDS)
    found: Dict[str, Dict[str, Any]] = {}
    pages_seen = 0
    extraction_failures: List[Dict[str, str]] = []

    for elem in iter_pages(args.wikipedia):
        pages_seen += 1
        rec = page_record(elem)
        page_id = rec["page_id"]

        if page_id in targets and page_id not in found:
            raw = rec["raw"]
            extracted = ""
            extraction_error = ""
            try:
                extracted = extract_plain_text(raw)
            except Exception as exc:
                extraction_error = f"{type(exc).__name__}: {exc}"
                extraction_failures.append(
                    {"page_id": page_id, "title": rec["title"], "error": extraction_error}
                )

            found[page_id] = {
                "calibration_batch": "batch_001",
                "needs_full_page_review": True,
                "page_id": page_id,
                "title": rec["title"],
                "namespace": rec["namespace"],
                "is_redirect": rec["is_redirect"],
                "redirect_title": rec["redirect_title"],
                "has_revision": rec["has_revision"],
                "has_text_node": rec["has_text_node"],
                "raw_chars": len(raw),
                "extracted_chars": len(extracted),
                "raw_sha256": sha256_text(raw),
                "extracted_sha256": sha256_text(extracted),
                "extraction_error": extraction_error,
                "raw_wikitext_full": raw,
                "extracted_text_full": extracted,
            }

            print(
                f"[{SCRIPT_VERSION}] found {len(found):02d}/{EXPECTED_COUNT}: "
                f"{page_id} | {rec['title']!r} | raw={len(raw):,} "
                f"extracted={len(extracted):,}"
            )

            if len(found) == EXPECTED_COUNT:
                break

        if args.progress_every > 0 and pages_seen % args.progress_every == 0:
            print(
                f"[{SCRIPT_VERSION}] pages={pages_seen:,} "
                f"found={len(found)}/{EXPECTED_COUNT} "
                f"elapsed={time.time() - started:.1f}s"
            )

    missing = [pid for pid in TARGET_PAGE_IDS if pid not in found]

    # Preserve the exact order from BATCH_001_FINDINGS.md.
    ordered_rows = [found[pid] for pid in TARGET_PAGE_IDS if pid in found]

    jsonl_path = args.output_dir / "batch_001_full_pages.jsonl"
    with jsonl_path.open("w", encoding="utf-8") as fh:
        for row in ordered_rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")

    missing_path = args.output_dir / "missing_page_ids.txt"
    missing_path.write_text(
        "\n".join(missing) + ("\n" if missing else ""),
        encoding="utf-8",
    )

    failures_path = args.output_dir / "extraction_failures.jsonl"
    with failures_path.open("w", encoding="utf-8") as fh:
        for row in extraction_failures:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")

    elapsed = time.time() - started
    full_extracted_nonempty = sum(bool(row["extracted_text_full"]) for row in ordered_rows)

    report = f"""# Batch 001 Full-Page Calibration Extraction

**Script:** `{SCRIPT_VERSION}`

## Purpose

Read-only extraction of full raw wikitext and full extracted text for the
{EXPECTED_COUNT} batch_001 candidates previously marked `NEEDS_FULL_PAGE_REVIEW`.

No cleaning, classification, segmentation, retrieval evaluation, or dump modification
is performed.

## Result

- Target page IDs: **{EXPECTED_COUNT}**
- Found: **{len(found)}**
- Missing: **{len(missing)}**
- Extraction failures: **{len(extraction_failures)}**
- Non-empty full extracted texts: **{full_extracted_nonempty}**
- XML pages scanned before completion/end: **{pages_seen:,}**

## Reproducibility

- Wikipedia dump: `{args.wikipedia}`
- Dump bytes: `{args.wikipedia.stat().st_size}`
- Dump SHA-256: `{dump_hash}`
- Python: `{platform.python_version()}`
- lxml: `{version_or_unknown("lxml")}`
- mwparserfromhell: `{version_or_unknown("mwparserfromhell")}`
- Elapsed seconds: `{elapsed:.2f}`

## Output

- `batch_001_full_pages.jsonl` — full raw + extracted text in calibration order
- `missing_page_ids.txt`
- `extraction_failures.jsonl`

## Validation rule

Proceed to Codex full-page recalibration only if:

- `Found = 35`
- `Missing = 0`
- `Extraction failures = 0`

The full-page review must revise observation completeness and taxonomy boundaries,
not create cleaning rules.
"""
    (args.output_dir / "FULL_PAGE_EXTRACTION_REPORT.md").write_text(
        report, encoding="utf-8"
    )

    print()
    print(report)
    print(f"Outputs: {args.output_dir}")

    if missing or extraction_failures or len(found) != EXPECTED_COUNT:
        return 4
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
