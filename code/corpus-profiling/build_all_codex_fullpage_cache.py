#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build full raw/extracted cache for all Codex discovery candidates.

Read-only evidence extraction only. No cleaning, classification, segmentation,
or retrieval evaluation. Extraction matches W-DISCOVERY-v0.3:
    mwparserfromhell.parse(raw).strip_code(normalize=True, collapse=True)
followed by NFC and newline normalization.
"""
from __future__ import annotations

import argparse
import bz2
import hashlib
import importlib.metadata
import json
import platform
import re
import time
import unicodedata
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, Iterator, List, Tuple

SCRIPT_VERSION = "W-FULLPAGE-CACHE-v0.1"
BATCH_RE = re.compile(r"^batch_(\d+)\.jsonl$", re.I)


def file_sha256(path: Path, block_size: int = 8 * 1024 * 1024) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            b = f.read(block_size)
            if not b:
                return h.hexdigest()
            h.update(b)


def text_sha256(text: str) -> str:
    return hashlib.sha256((text or "").encode("utf-8")).hexdigest()


def version(name: str) -> str:
    try:
        return importlib.metadata.version(name)
    except Exception:
        return "unknown"


def child_text(elem: Any, name: str) -> str:
    node = elem.find(f"{{*}}{name}")
    return "" if node is None or node.text is None else node.text


def page_record(elem: Any) -> Dict[str, Any]:
    title = child_text(elem, "title")
    ns = child_text(elem, "ns")
    page_id = child_text(elem, "id") or title
    redirect = elem.find("{*}redirect")
    rev = elem.find("{*}revision")
    text_node = rev.find("{*}text") if rev is not None else None
    raw = "" if text_node is None or text_node.text is None else text_node.text
    return {
        "page_id": str(page_id), "title": title, "namespace": ns,
        "is_redirect": redirect is not None,
        "redirect_title": redirect.get("title", "") if redirect is not None else "",
        "has_revision": rev is not None, "has_text_node": text_node is not None,
        "raw": raw,
    }


def iter_pages(path: Path) -> Iterator[Any]:
    from lxml import etree  # type: ignore
    opener = bz2.open if path.suffix.lower() == ".bz2" else open
    with opener(path, "rb") as f:  # type: ignore[arg-type]
        context = etree.iterparse(f, events=("end",), tag="{*}page", recover=True, huge_tree=True)
        for _, elem in context:
            yield elem
            elem.clear()
            parent = elem.getparent()
            if parent is not None:
                while elem.getprevious() is not None:
                    del parent[0]


def extract_plain(raw: str) -> str:
    import mwparserfromhell  # type: ignore
    out = mwparserfromhell.parse(raw or "").strip_code(normalize=True, collapse=True)
    out = unicodedata.normalize("NFC", out or "")
    return out.replace("\r\n", "\n").replace("\r", "\n")


def batch_key(path: Path) -> Tuple[int, str]:
    m = BATCH_RE.match(path.name)
    return (int(m.group(1)), path.name) if m else (10**9, path.name)


def read_batches(batches_dir: Path):
    files = sorted([p for p in batches_dir.glob("batch_*.jsonl") if BATCH_RE.match(p.name)], key=batch_key)
    if not files:
        raise RuntimeError(f"No batch_*.jsonl files found in {batches_dir}")

    by_page: Dict[str, Dict[str, Any]] = {}
    by_batch: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    duplicates: List[Dict[str, Any]] = []
    global_pos = 0

    for path in files:
        batch = path.stem
        with path.open("r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                row = json.loads(line)
                page_id = str(row.get("page_id", "")).strip()
                if not page_id:
                    cid = str(row.get("candidate_id", "")).strip()
                    if cid.startswith("UZWP-"):
                        page_id = cid[5:]
                if not page_id:
                    raise RuntimeError(f"Missing page_id in {path} line {line_no}")

                global_pos += 1
                meta = {
                    "page_id": page_id,
                    "candidate_id": row.get("candidate_id") or f"UZWP-{page_id}",
                    "batch": batch,
                    "batch_file": path.name,
                    "batch_line": line_no,
                    "global_position": global_pos,
                    "title_from_batch": row.get("title", ""),
                    "selection_reasons": row.get("selection_reasons", []),
                    "raw_signature": row.get("raw_signature", ""),
                    "extracted_signature": row.get("extracted_signature", ""),
                    "joint_signature": row.get("joint_signature", ""),
                    "signature_population": row.get("signature_population"),
                }
                by_batch[batch].append(meta)
                if page_id in by_page:
                    duplicates.append({"page_id": page_id, "first_batch": by_page[page_id]["batch"], "duplicate_batch": batch})
                    if batch not in by_page[page_id]["all_batches"]:
                        by_page[page_id]["all_batches"].append(batch)
                else:
                    meta["all_batches"] = [batch]
                    by_page[page_id] = meta
    return files, by_page, by_batch, duplicates


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--batches-dir", type=Path, required=True)
    ap.add_argument("--wikipedia", type=Path, required=True)
    ap.add_argument("--output-dir", type=Path, required=True)
    ap.add_argument("--progress-every", type=int, default=50000)
    args = ap.parse_args()

    if not args.batches_dir.exists() or not args.wikipedia.exists():
        print("ERROR: input path does not exist")
        return 2
    try:
        import lxml  # noqa: F401
        import mwparserfromhell  # noqa: F401
    except Exception:
        print("ERROR: pip install lxml mwparserfromhell")
        return 3

    t0 = time.time()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    per_dir = args.output_dir / "per_batch_full_pages"
    per_dir.mkdir(parents=True, exist_ok=True)

    print(f"[{SCRIPT_VERSION}] reading discovery batches...")
    batch_files, by_page, by_batch, duplicates = read_batches(args.batches_dir)
    row_count = sum(len(v) for v in by_batch.values())
    targets = set(by_page)
    print(f"[{SCRIPT_VERSION}] batches={len(batch_files)} candidate_rows={row_count} unique_page_ids={len(targets)} duplicate_memberships={len(duplicates)}")

    print(f"[{SCRIPT_VERSION}] hashing input dump...")
    dump_hash = file_sha256(args.wikipedia)
    print(f"[{SCRIPT_VERSION}] input SHA-256: {dump_hash}")

    found: Dict[str, Dict[str, Any]] = {}
    failures: List[Dict[str, str]] = []
    pages_seen = 0

    for elem in iter_pages(args.wikipedia):
        pages_seen += 1
        rec = page_record(elem)
        pid = rec["page_id"]
        if pid in targets and pid not in found:
            raw = rec["raw"]
            err = ""
            try:
                extracted = extract_plain(raw)
            except Exception as exc:
                extracted = ""
                err = f"{type(exc).__name__}: {exc}"
                failures.append({"page_id": pid, "title": rec["title"], "error": err})
            meta = by_page[pid]
            found[pid] = {
                "page_id": pid,
                "candidate_id": meta["candidate_id"],
                "discovery_batches": meta["all_batches"],
                "first_batch": meta["batch"],
                "title": rec["title"],
                "title_from_batch": meta["title_from_batch"],
                "namespace": rec["namespace"],
                "is_redirect": rec["is_redirect"],
                "redirect_title": rec["redirect_title"],
                "has_revision": rec["has_revision"],
                "has_text_node": rec["has_text_node"],
                "raw_chars": len(raw),
                "extracted_chars": len(extracted),
                "raw_sha256": text_sha256(raw),
                "extracted_sha256": text_sha256(extracted),
                "extraction_error": err,
                "selection_reasons": meta["selection_reasons"],
                "raw_signature": meta["raw_signature"],
                "extracted_signature": meta["extracted_signature"],
                "joint_signature": meta["joint_signature"],
                "signature_population": meta["signature_population"],
                "raw_wikitext_full": raw,
                "extracted_text_full": extracted,
            }
            n = len(found)
            if n <= 10 or n % 50 == 0 or n == len(targets):
                print(f"[{SCRIPT_VERSION}] found {n}/{len(targets)} | page_id={pid} | {rec['title']!r}")
            if len(found) == len(targets):
                break
        if args.progress_every and pages_seen % args.progress_every == 0:
            print(f"[{SCRIPT_VERSION}] pages={pages_seen:,} found={len(found)}/{len(targets)} elapsed={time.time()-t0:.1f}s")

    missing = sorted(targets - set(found))

    ordered = sorted(by_page.values(), key=lambda x: x["global_position"])
    with (args.output_dir / "all_candidates_full_pages.jsonl").open("w", encoding="utf-8") as f:
        for meta in ordered:
            if meta["page_id"] in found:
                f.write(json.dumps(found[meta["page_id"]], ensure_ascii=False) + "\n")

    with (args.output_dir / "candidate_index.jsonl").open("w", encoding="utf-8") as f:
        for meta in ordered:
            pid = meta["page_id"]
            r = found.get(pid, {})
            f.write(json.dumps({
                "page_id": pid, "candidate_id": meta["candidate_id"],
                "first_batch": meta["batch"], "all_batches": meta["all_batches"],
                "found": pid in found, "title": r.get("title", ""),
                "raw_chars": r.get("raw_chars"), "extracted_chars": r.get("extracted_chars"),
                "raw_sha256": r.get("raw_sha256"), "extracted_sha256": r.get("extracted_sha256"),
                "extraction_error": r.get("extraction_error", ""),
            }, ensure_ascii=False) + "\n")

    manifest = []
    for batch in sorted(by_batch):
        out = per_dir / f"{batch}_full_pages.jsonl"
        count = 0
        with out.open("w", encoding="utf-8") as f:
            for meta in by_batch[batch]:
                pid = meta["page_id"]
                if pid not in found:
                    continue
                row = dict(found[pid])
                row["review_batch"] = batch
                row["batch_candidate_position"] = meta["batch_line"]
                row["selection_reasons"] = meta["selection_reasons"]
                row["raw_signature"] = meta["raw_signature"]
                row["extracted_signature"] = meta["extracted_signature"]
                row["joint_signature"] = meta["joint_signature"]
                row["signature_population"] = meta["signature_population"]
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
                count += 1
        inp = next(p for p in batch_files if p.stem == batch)
        manifest.append({
            "batch": batch, "input_file": str(inp), "input_sha256": file_sha256(inp),
            "input_rows": len(by_batch[batch]), "output_rows": count, "output_file": str(out),
        })

    (args.output_dir / "batch_manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    (args.output_dir / "missing_page_ids.txt").write_text("\n".join(missing) + ("\n" if missing else ""), encoding="utf-8")
    with (args.output_dir / "extraction_failures.jsonl").open("w", encoding="utf-8") as f:
        for r in failures:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    with (args.output_dir / "duplicate_candidate_memberships.jsonl").open("w", encoding="utf-8") as f:
        for r in duplicates:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    nonempty = sum(bool(r["extracted_text_full"]) for r in found.values())
    batch_lines = "\n".join(f"| {m['batch']} | {m['input_rows']} | {m['output_rows']} |" for m in manifest)
    report = f"""# Discovery Candidates Full-Page Cache\n\n**Script:** `{SCRIPT_VERSION}`\n\n## Scientific boundary\n\nRead-only full-page evidence cache. No cleaning, classification, segmentation or retrieval evaluation.\n\n## Input batches\n\n- Batch files: **{len(batch_files)}**\n- Candidate rows: **{row_count}**\n- Unique page IDs: **{len(targets)}**\n- Duplicate cross-batch memberships: **{len(duplicates)}**\n\n## Extraction result\n\n- Unique targets: **{len(targets)}**\n- Found: **{len(found)}**\n- Missing: **{len(missing)}**\n- Extraction failures: **{len(failures)}**\n- Non-empty extracted texts: **{nonempty}**\n- Empty extracted texts: **{len(found)-nonempty}**\n- XML pages scanned: **{pages_seen:,}**\n\n## Per-batch cache\n\n| Batch | Input rows | Full-page rows |\n|---|---:|---:|\n{batch_lines}\n\n## Reproducibility\n\n- Batches directory: `{args.batches_dir}`\n- Wikipedia dump: `{args.wikipedia}`\n- Dump bytes: `{args.wikipedia.stat().st_size}`\n- Dump SHA-256: `{dump_hash}`\n- Python: `{platform.python_version()}`\n- lxml: `{version('lxml')}`\n- mwparserfromhell: `{version('mwparserfromhell')}`\n- Elapsed seconds: `{time.time()-t0:.2f}`\n\n## Validation gate\n\nProceed to Codex batch_002+ only if `Missing = 0`, `Extraction failures = 0`, and every batch has identical input/output row counts.\n"""
    (args.output_dir / "FULLPAGE_CACHE_REPORT.md").write_text(report, encoding="utf-8")
    print("\n" + report)
    print(f"Outputs: {args.output_dir}")

    bad_counts = [m for m in manifest if m["input_rows"] != m["output_rows"]]
    return 4 if missing or failures or bad_counts else 0


if __name__ == "__main__":
    raise SystemExit(main())
