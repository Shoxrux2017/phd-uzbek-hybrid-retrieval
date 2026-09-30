#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase W1 — full Uzbek Wikipedia census + paired structural feature scan.

Purpose
-------
Read the official Uzbek Wikipedia pages-articles XML/XML.bz2 in streaming mode and:
1) census every <page> in the dump;
2) count namespaces, redirects, missing/empty revisions/text;
3) for main-namespace, non-redirect, text-bearing pages, compute model-independent
   structural features for BOTH raw wikitext and extracted plain text;
4) write reproducible audit outputs without modifying the source dump.

This phase is intentionally pre-retrieval:
- no BM25;
- no dense retrieval;
- no qrels;
- no effectiveness metrics;
- no retrieval-unit segmentation;
- no automatic document exclusion;
- no final CLEANABLE/SEVERE classification.

The purpose is discovery and measurement, not cleaning.

Python: 3.12+
Required:
    pip install lxml mwparserfromhell
"""

from __future__ import annotations

import argparse
import bz2
import csv
import hashlib
import json
import os
import re
import sys
import time
import unicodedata
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Dict, Iterator, Optional, TextIO, Tuple

SCRIPT_VERSION = "W1-v0.1"

# Unicode/script helpers.
LATIN_RE = re.compile(r"[A-Za-zÀ-ž]")
CYRILLIC_RE = re.compile(r"[\u0400-\u04FF]")
URL_RE = re.compile(r"(?i)\b(?:https?://|www\.)\S*")
RAW_EXTERNAL_LINK_RE = re.compile(r"(?i)\[(?:https?://|//)")
RAW_FILE_RE = re.compile(r"(?i)\[\[(?:File|Image|Fayl):")
RAW_CATEGORY_RE = re.compile(r"(?i)\[\[(?:Category|Turkum):")
RAW_REF_RE = re.compile(r"(?i)<\s*ref\b")
RAW_REFERENCES_RE = re.compile(r"(?i)<\s*references\b")
RAW_GALLERY_RE = re.compile(r"(?i)<\s*gallery\b")
RAW_HTML_TAG_RE = re.compile(r"(?i)</?[A-Za-z][^>]{0,300}>")
EXTRACTED_WIKI_RESIDUE_RE = re.compile(
    r"(?i)(?:\blink=|\bFayl:|\bFile:|\bImage:|upload\.wikimedia|wikimedia\.org|"
    r"\bframeless\b|\bthumb\b|\balt=|[0-9]{2,4}x[0-9]{2,4}px)"
)
LONG_DIGIT_RUN_RE = re.compile(r"\d{8,}")
ALPHA_DIGIT_TRANSITION_RE = re.compile(
    r"(?i)(?:[A-Za-zÀ-ž\u0400-\u04FFʻʼ‘’'`][0-9]|"
    r"[0-9][A-Za-zÀ-ž\u0400-\u04FFʻʼ‘’'`])"
)
HEADING_LINE_RE = re.compile(r"^\s*=+[^=\n].*?=+\s*$")
LIST_LINE_RE = re.compile(r"^\s*[*#;:]+")
TABLE_ROW_LINE_RE = re.compile(r"^\s*\|-")
TABLE_CELL_LINE_RE = re.compile(r"^\s*[!|]")
KEY_VALUE_LINE_RE = re.compile(r"^\s*[^=\n]{1,80}\s*=\s*\S")
REPEATED_DELIMITER_RE = re.compile(r"(?:\|{3,}|={4,}|-{6,}|_{8,}|\.{6,})")
APOSTROPHE_VARIANTS = ("'", "’", "‘", "ʻ", "ʼ", "`", "´", "ʹ", "ʽ")


@dataclass
class Census:
    pages_total: int = 0
    main_namespace_pages: int = 0
    non_main_namespace_pages: int = 0
    redirects_total: int = 0
    main_namespace_redirects: int = 0
    pages_without_revision: int = 0
    pages_without_text_node: int = 0
    pages_with_empty_text: int = 0
    main_nonredirect_text_pages: int = 0
    main_nonredirect_empty_text_pages: int = 0
    feature_rows_written: int = 0
    extraction_success: int = 0
    extraction_empty: int = 0
    extraction_failures: int = 0


class CsvStreamWriter:
    """Create a CSV lazily from the first row and stream subsequent rows."""

    def __init__(self, path: Path):
        self.path = path
        self.fh: Optional[TextIO] = None
        self.writer: Optional[csv.DictWriter] = None

    def write(self, row: Dict[str, Any]) -> None:
        if self.writer is None:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            self.fh = self.path.open("w", encoding="utf-8-sig", newline="")
            self.writer = csv.DictWriter(self.fh, fieldnames=list(row.keys()))
            self.writer.writeheader()
        self.writer.writerow(row)

    def close(self) -> None:
        if self.fh is not None:
            self.fh.close()
            self.fh = None
            self.writer = None


def sha256_text(text: str) -> str:
    return hashlib.sha256((text or "").encode("utf-8")).hexdigest()


def safe_ratio(num: int | float, den: int | float) -> float:
    return float(num) / float(den) if den else 0.0


def token_transition_count(token: str) -> int:
    return len(ALPHA_DIGIT_TRANSITION_RE.findall(token or ""))


def repeated_line_stats(lines: list[str]) -> Tuple[int, float]:
    nonempty = [line.strip() for line in lines if line.strip()]
    if not nonempty:
        return 0, 0.0
    counts = Counter(nonempty)
    repeated_instances = sum(v - 1 for v in counts.values() if v > 1)
    return repeated_instances, safe_ratio(repeated_instances, len(nonempty))


def text_features(text: str, prefix: str) -> Dict[str, Any]:
    """Model-independent surface features for raw or extracted text."""
    s = text or ""
    chars = len(s)
    utf8_bytes = len(s.encode("utf-8"))
    lines = s.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    nonempty_lines = [line for line in lines if line.strip()]
    tokens = s.split()

    alpha = digit = whitespace = punct = 0
    controls = formats = private_use = replacement = other_symbols = 0
    latin = len(LATIN_RE.findall(s))
    cyrillic = len(CYRILLIC_RE.findall(s))

    for ch in s:
        cat = unicodedata.category(ch)
        if ch.isalpha():
            alpha += 1
        elif ch.isdigit():
            digit += 1
        elif ch.isspace():
            whitespace += 1
        elif cat.startswith("P"):
            punct += 1

        if cat == "Cc":
            controls += 1
        elif cat == "Cf":
            formats += 1
        elif cat == "Co":
            private_use += 1

        if ch == "\ufffd":
            replacement += 1
        if cat.startswith("S"):
            other_symbols += 1

    token_lengths = [len(tok) for tok in tokens]
    max_token_len = max(token_lengths, default=0)
    long40 = sum(n >= 40 for n in token_lengths)
    long80 = sum(n >= 80 for n in token_lengths)
    long120 = sum(n >= 120 for n in token_lengths)
    long200 = sum(n >= 200 for n in token_lengths)
    transitions = sum(token_transition_count(tok) for tok in tokens)
    glued_transition_tokens = sum(
        1 for tok in tokens if len(tok) >= 30 and token_transition_count(tok) >= 2
    )

    token_counts = Counter(tokens)
    unique_tokens = len(token_counts)
    top_token_freq = max(token_counts.values(), default=0)

    repeated_lines, repeated_line_ratio = repeated_line_stats(lines)
    max_line_len = max((len(line) for line in lines), default=0)

    apostrophe_counts = {variant: s.count(variant) for variant in APOSTROPHE_VARIANTS}
    apostrophe_present = "".join(k for k, v in apostrophe_counts.items() if v)

    return {
        f"{prefix}_chars": chars,
        f"{prefix}_utf8_bytes": utf8_bytes,
        f"{prefix}_words_ws": len(tokens),
        f"{prefix}_lines": len(lines),
        f"{prefix}_nonempty_lines": len(nonempty_lines),
        f"{prefix}_max_line_len": max_line_len,
        f"{prefix}_alpha_ratio": round(safe_ratio(alpha, chars), 8),
        f"{prefix}_digit_ratio": round(safe_ratio(digit, chars), 8),
        f"{prefix}_whitespace_ratio": round(safe_ratio(whitespace, chars), 8),
        f"{prefix}_punct_ratio": round(safe_ratio(punct, chars), 8),
        f"{prefix}_symbol_ratio": round(safe_ratio(other_symbols, chars), 8),
        f"{prefix}_latin_letters": latin,
        f"{prefix}_cyrillic_letters": cyrillic,
        f"{prefix}_latin_share_of_latin_cyr": round(safe_ratio(latin, latin + cyrillic), 8),
        f"{prefix}_cyrillic_share_of_latin_cyr": round(safe_ratio(cyrillic, latin + cyrillic), 8),
        f"{prefix}_mixed_latin_cyrillic": int(bool(latin and cyrillic)),
        f"{prefix}_control_chars": controls,
        f"{prefix}_format_chars": formats,
        f"{prefix}_private_use_chars": private_use,
        f"{prefix}_replacement_chars": replacement,
        f"{prefix}_apostrophe_variants": apostrophe_present,
        f"{prefix}_max_token_len": max_token_len,
        f"{prefix}_long_tokens_40": long40,
        f"{prefix}_long_tokens_80": long80,
        f"{prefix}_long_tokens_120": long120,
        f"{prefix}_long_tokens_200": long200,
        f"{prefix}_alpha_digit_transitions": transitions,
        f"{prefix}_glued_transition_tokens": glued_transition_tokens,
        f"{prefix}_long_digit_runs": len(LONG_DIGIT_RUN_RE.findall(s)),
        f"{prefix}_unique_token_ratio": round(safe_ratio(unique_tokens, len(tokens)), 8),
        f"{prefix}_top_token_share": round(safe_ratio(top_token_freq, len(tokens)), 8),
        f"{prefix}_repeated_line_instances": repeated_lines,
        f"{prefix}_repeated_line_ratio": round(repeated_line_ratio, 8),
        f"{prefix}_repeated_delimiter_runs": len(REPEATED_DELIMITER_RE.findall(s)),
        f"{prefix}_sha256": sha256_text(s),
    }


def raw_wiki_features(raw: str, code: Any) -> Dict[str, Any]:
    lines = (raw or "").replace("\r\n", "\n").replace("\r", "\n").split("\n")
    template_count = wikilink_count = tag_count = 0
    try:
        template_count = len(code.filter_templates(recursive=True))
        wikilink_count = len(code.filter_wikilinks(recursive=True))
        tag_count = len(code.filter_tags(recursive=True))
    except Exception:
        # Parsing succeeded enough for extraction; AST introspection failure is not
        # grounds to abort the census.
        pass

    return {
        "raw_template_open_count": raw.count("{{"),
        "raw_template_close_count": raw.count("}}"),
        "raw_template_ast_count": template_count,
        "raw_table_start_count": raw.count("{|"),
        "raw_table_end_count": raw.count("|}"),
        "raw_table_row_marker_count": sum(bool(TABLE_ROW_LINE_RE.match(line)) for line in lines),
        "raw_table_cell_like_line_count": sum(bool(TABLE_CELL_LINE_RE.match(line)) for line in lines),
        "raw_wikilink_open_count": raw.count("[["),
        "raw_wikilink_ast_count": wikilink_count,
        "raw_external_link_count": len(RAW_EXTERNAL_LINK_RE.findall(raw)),
        "raw_url_count": len(URL_RE.findall(raw)),
        "raw_ref_tag_count": len(RAW_REF_RE.findall(raw)),
        "raw_references_tag_count": len(RAW_REFERENCES_RE.findall(raw)),
        "raw_gallery_tag_count": len(RAW_GALLERY_RE.findall(raw)),
        "raw_html_tag_count": len(RAW_HTML_TAG_RE.findall(raw)),
        "raw_tag_ast_count": tag_count,
        "raw_file_link_count": len(RAW_FILE_RE.findall(raw)),
        "raw_category_link_count": len(RAW_CATEGORY_RE.findall(raw)),
        "raw_heading_line_count": sum(bool(HEADING_LINE_RE.match(line)) for line in lines),
        "raw_list_line_count": sum(bool(LIST_LINE_RE.match(line)) for line in lines),
        "raw_key_value_line_count": sum(bool(KEY_VALUE_LINE_RE.match(line)) for line in lines),
        "raw_pipe_chars": raw.count("|"),
        "raw_equals_chars": raw.count("="),
    }


def extracted_residue_features(text: str) -> Dict[str, Any]:
    s = text or ""
    lines = s.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    return {
        "extracted_url_count": len(URL_RE.findall(s)),
        "extracted_wiki_residue_count": len(EXTRACTED_WIKI_RESIDUE_RE.findall(s)),
        "extracted_double_brace_count": s.count("{{") + s.count("}}"),
        "extracted_table_marker_count": s.count("{|") + s.count("|}"),
        "extracted_pipe_chars": s.count("|"),
        "extracted_equals_chars": s.count("="),
        "extracted_heading_line_count": sum(bool(HEADING_LINE_RE.match(line)) for line in lines),
        "extracted_list_line_count": sum(bool(LIST_LINE_RE.match(line)) for line in lines),
        "extracted_key_value_line_count": sum(bool(KEY_VALUE_LINE_RE.match(line)) for line in lines),
    }


def extract_plain_text(raw: str) -> Tuple[str, Any]:
    import mwparserfromhell  # type: ignore

    code = mwparserfromhell.parse(raw or "")
    extracted = code.strip_code(normalize=True, collapse=True)
    # Unicode normalization only; preserve line structure. This is an observation
    # representation, not the final cleaning policy.
    extracted = unicodedata.normalize("NFC", extracted or "")
    extracted = extracted.replace("\r\n", "\n").replace("\r", "\n")
    return extracted, code


def find_child_text(elem: Any, local: str) -> str:
    node = elem.find(f"{{*}}{local}")
    return "" if node is None or node.text is None else node.text


def page_record(elem: Any) -> Dict[str, Any]:
    title = find_child_text(elem, "title")
    ns = find_child_text(elem, "ns")
    page_id = find_child_text(elem, "id") or title
    redirect_node = elem.find("{*}redirect")
    is_redirect = redirect_node is not None
    redirect_title = ""
    if redirect_node is not None:
        redirect_title = redirect_node.get("title") or ""

    rev = elem.find("{*}revision")
    has_revision = rev is not None
    text_node = rev.find("{*}text") if rev is not None else None
    has_text_node = text_node is not None
    raw = ""
    if text_node is not None and text_node.text is not None:
        raw = text_node.text

    return {
        "page_id": page_id,
        "title": title,
        "namespace": ns,
        "is_redirect": is_redirect,
        "redirect_title": redirect_title,
        "has_revision": has_revision,
        "has_text_node": has_text_node,
        "raw": raw,
    }


def feature_row(page: Dict[str, Any]) -> Tuple[Dict[str, Any], Optional[str]]:
    raw = page["raw"]
    extraction_error: Optional[str] = None
    extracted = ""
    code = None

    try:
        extracted, code = extract_plain_text(raw)
    except Exception as exc:
        extraction_error = f"{type(exc).__name__}: {exc}"

    row: Dict[str, Any] = {
        "page_id": page["page_id"],
        "title": page["title"],
        "namespace": page["namespace"],
        "is_redirect": int(page["is_redirect"]),
        "raw_nonempty": int(bool(raw.strip())),
        "extraction_ok": int(extraction_error is None),
        "extraction_empty": int(extraction_error is None and not extracted.strip()),
    }
    row.update(text_features(raw, "raw"))

    if code is not None:
        row.update(raw_wiki_features(raw, code))
    else:
        # Stable schema even when extraction failed.
        row.update({
            "raw_template_open_count": raw.count("{{"),
            "raw_template_close_count": raw.count("}}"),
            "raw_template_ast_count": "",
            "raw_table_start_count": raw.count("{|"),
            "raw_table_end_count": raw.count("|}"),
            "raw_table_row_marker_count": "",
            "raw_table_cell_like_line_count": "",
            "raw_wikilink_open_count": raw.count("[["),
            "raw_wikilink_ast_count": "",
            "raw_external_link_count": len(RAW_EXTERNAL_LINK_RE.findall(raw)),
            "raw_url_count": len(URL_RE.findall(raw)),
            "raw_ref_tag_count": len(RAW_REF_RE.findall(raw)),
            "raw_references_tag_count": len(RAW_REFERENCES_RE.findall(raw)),
            "raw_gallery_tag_count": len(RAW_GALLERY_RE.findall(raw)),
            "raw_html_tag_count": len(RAW_HTML_TAG_RE.findall(raw)),
            "raw_tag_ast_count": "",
            "raw_file_link_count": len(RAW_FILE_RE.findall(raw)),
            "raw_category_link_count": len(RAW_CATEGORY_RE.findall(raw)),
            "raw_heading_line_count": "",
            "raw_list_line_count": "",
            "raw_key_value_line_count": "",
            "raw_pipe_chars": raw.count("|"),
            "raw_equals_chars": raw.count("="),
        })

    if extraction_error is None:
        row.update(text_features(extracted, "extracted"))
        row.update(extracted_residue_features(extracted))
        row["extracted_to_raw_char_ratio"] = round(
            safe_ratio(len(extracted), len(raw)), 8
        )
        row["extracted_to_raw_word_ratio"] = round(
            safe_ratio(len(extracted.split()), len(raw.split())), 8
        )
        title_norm = unicodedata.normalize("NFC", page["title"] or "").strip().casefold()
        extracted_norm = extracted.casefold()
        row["title_occurrences_in_extracted"] = (
            extracted_norm.count(title_norm) if title_norm else 0
        )
    else:
        # Fill the extracted-side schema deterministically with blanks.
        for key in text_features("", "extracted"):
            row[key] = ""
        for key in extracted_residue_features(""):
            row[key] = ""
        row["extracted_to_raw_char_ratio"] = ""
        row["extracted_to_raw_word_ratio"] = ""
        row["title_occurrences_in_extracted"] = ""

    return row, extraction_error


def iter_pages(path: Path) -> Iterator[Any]:
    try:
        from lxml import etree  # type: ignore
    except ImportError as exc:
        raise RuntimeError("Missing dependency: pip install lxml") from exc

    opener = bz2.open if path.suffix.lower() == ".bz2" else open
    mode = "rb"

    with opener(path, mode) as fh:  # type: ignore[arg-type]
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


def write_namespace_counts(path: Path, counter: Counter[str]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["namespace", "pages"])
        writer.writeheader()
        def sort_key(item: Tuple[str, int]) -> Tuple[int, str]:
            ns = item[0]
            try:
                return (0, f"{int(ns):012d}")
            except ValueError:
                return (1, ns)
        for ns, count in sorted(counter.items(), key=sort_key):
            writer.writerow({"namespace": ns, "pages": count})


def feature_schema() -> Dict[str, Any]:
    return {
        "script_version": SCRIPT_VERSION,
        "population": (
            "All XML <page> elements are censused. Per-page structural feature rows "
            "are written only for namespace=0, non-redirect, non-empty-text pages."
        ),
        "representation_levels": {
            "raw": "Original revision text from the dump; never rewritten.",
            "extracted": (
                "mwparserfromhell.strip_code(normalize=True, collapse=True), followed only "
                "by NFC and CRLF/CR newline normalization for measurement."
            ),
        },
        "important_interpretation_rule": (
            "A feature is a measurement signal, not a corruption label. High digit, URL, "
            "table, list, markup or long-token counts do not by themselves imply exclusion."
        ),
        "selected_feature_groups": {
            "surface": [
                "lengths", "line structure", "alpha/digit/whitespace/punctuation ratios",
                "Latin/Cyrillic shares", "Unicode control/format/private-use/replacement chars",
            ],
            "token_shape": [
                "max token length", "long-token counts", "alpha-digit transitions",
                "long digit runs", "unique-token ratio", "top-token share",
            ],
            "repetition": ["repeated lines", "repeated delimiter runs"],
            "raw_wiki_structure": [
                "templates", "tables", "wikilinks", "external links", "references",
                "galleries", "HTML-like tags", "file/category links", "headings", "lists",
                "key=value-like lines", "pipe/equal characters",
            ],
            "extraction_residue": [
                "URLs", "wiki/image/layout residue", "brace/table markers",
                "headings/lists/key=value-like lines", "pipe/equal characters",
            ],
            "paired_change": [
                "extracted/raw char ratio", "extracted/raw whitespace-word ratio",
                "title occurrences after extraction",
            ],
        },
    }


def build_report(
    census: Census,
    namespace_counts: Counter[str],
    elapsed_seconds: float,
    args: argparse.Namespace,
) -> str:
    main_feature_den = max(1, census.feature_rows_written)
    lines = [
        "# Uzbek Wikipedia Structural Audit — Phase W1",
        "",
        f"**Script:** `{SCRIPT_VERSION}`",
        "",
        "## Scope",
        "",
        "- 100% XML page census unless `--max-pages` was used.",
        "- Per-page features: namespace 0, non-redirect, non-empty revision text.",
        "- Raw wikitext and extracted text are measured separately.",
        "- No cleaning/exclusion decision is made in W1.",
        "- No segmentation, tokenizer overflow or retrieval effectiveness is used.",
        "",
        "## Census",
        "",
        f"- XML pages seen: **{census.pages_total:,}**",
        f"- Main namespace pages: **{census.main_namespace_pages:,}**",
        f"- Non-main namespace pages: **{census.non_main_namespace_pages:,}**",
        f"- Redirects total: **{census.redirects_total:,}**",
        f"- Main-namespace redirects: **{census.main_namespace_redirects:,}**",
        f"- Pages without revision: **{census.pages_without_revision:,}**",
        f"- Pages without text node: **{census.pages_without_text_node:,}**",
        f"- Pages with empty text: **{census.pages_with_empty_text:,}**",
        f"- Main non-redirect text-bearing pages: **{census.main_nonredirect_text_pages:,}**",
        f"- Feature rows written: **{census.feature_rows_written:,}**",
        "",
        "## Extraction observation",
        "",
        f"- Extraction success: **{census.extraction_success:,}**",
        f"- Extraction produced empty text: **{census.extraction_empty:,}** "
        f"({100.0 * census.extraction_empty / main_feature_den:.4f}%)",
        f"- Extraction failures: **{census.extraction_failures:,}** "
        f"({100.0 * census.extraction_failures / main_feature_den:.4f}%)",
        "",
        "## Namespace counts",
        "",
        "| Namespace | Pages |",
        "|---:|---:|",
    ]
    for ns, count in sorted(namespace_counts.items(), key=lambda x: (-x[1], x[0])):
        lines.append(f"| {ns or '(blank)'} | {count:,} |")

    lines += [
        "",
        "## Run",
        "",
        f"- Input: `{args.wikipedia}`",
        f"- Input bytes: `{args.wikipedia.stat().st_size if args.wikipedia.exists() else 'NA'}`",
        f"- `--max-pages`: `{args.max_pages if args.max_pages else 'none'}`",
        f"- Progress interval: `{args.progress_every}`",
        f"- Elapsed seconds: `{elapsed_seconds:.2f}`",
        "",
        "## Interpretation boundary",
        "",
        "W1 does **not** declare any page PROSE_LIKE, CLEANABLE, STRUCTURED, SEVERE or EXCLUDE.",
        "Those categories must be induced and validated in later phases from the full feature population "
        "and real examples, including rare-tail/outlier analysis.",
        "",
    ]
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Phase W1: full Uzbek Wikipedia census + paired structural feature scan",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument("--wikipedia", type=Path, required=True, help="Official pages-articles XML/XML.bz2")
    p.add_argument("--output-dir", type=Path, required=True)
    p.add_argument(
        "--max-pages",
        type=int,
        default=0,
        help="Smoke-test cap over XML pages; 0 means no cap/full dump",
    )
    p.add_argument("--progress-every", type=int, default=10000)
    return p.parse_args()


def main() -> int:
    args = parse_args()

    if not args.wikipedia.exists() or not args.wikipedia.is_file():
        print(f"ERROR: Wikipedia dump not found: {args.wikipedia}", file=sys.stderr)
        return 2
    if args.max_pages < 0:
        print("ERROR: --max-pages must be >= 0", file=sys.stderr)
        return 2
    if args.progress_every <= 0:
        print("ERROR: --progress-every must be > 0", file=sys.stderr)
        return 2

    try:
        import lxml  # noqa: F401
        import mwparserfromhell  # noqa: F401
    except ImportError as exc:
        print(
            "ERROR: missing dependency. Install with: pip install lxml mwparserfromhell",
            file=sys.stderr,
        )
        print(f"DETAIL: {exc}", file=sys.stderr)
        return 3

    args.output_dir.mkdir(parents=True, exist_ok=True)

    feature_writer = CsvStreamWriter(args.output_dir / "w1_page_features.csv")
    failure_writer = CsvStreamWriter(args.output_dir / "w1_extraction_failures.csv")
    namespace_counts: Counter[str] = Counter()
    census = Census()
    started = time.time()

    try:
        for elem in iter_pages(args.wikipedia):
            census.pages_total += 1
            page = page_record(elem)
            ns = page["namespace"]
            namespace_counts[ns] += 1

            if ns == "0":
                census.main_namespace_pages += 1
            else:
                census.non_main_namespace_pages += 1

            if page["is_redirect"]:
                census.redirects_total += 1
                if ns == "0":
                    census.main_namespace_redirects += 1

            if not page["has_revision"]:
                census.pages_without_revision += 1
            if not page["has_text_node"]:
                census.pages_without_text_node += 1
            if not page["raw"].strip():
                census.pages_with_empty_text += 1

            # Feature population: main namespace, non-redirect, text-bearing pages.
            if ns == "0" and not page["is_redirect"]:
                if page["raw"].strip():
                    census.main_nonredirect_text_pages += 1
                    row, extraction_error = feature_row(page)
                    feature_writer.write(row)
                    census.feature_rows_written += 1

                    if extraction_error is None:
                        census.extraction_success += 1
                        if row["extraction_empty"]:
                            census.extraction_empty += 1
                    else:
                        census.extraction_failures += 1
                        failure_writer.write({
                            "page_id": page["page_id"],
                            "title": page["title"],
                            "namespace": ns,
                            "error": extraction_error,
                        })
                else:
                    census.main_nonredirect_empty_text_pages += 1

            if census.pages_total % args.progress_every == 0:
                elapsed = max(0.001, time.time() - started)
                rate = census.pages_total / elapsed
                print(
                    f"[W1] pages={census.pages_total:,} "
                    f"feature_rows={census.feature_rows_written:,} "
                    f"extract_fail={census.extraction_failures:,} "
                    f"rate={rate:,.1f} pages/s",
                    flush=True,
                )

            if args.max_pages and census.pages_total >= args.max_pages:
                break

    finally:
        feature_writer.close()
        failure_writer.close()

    elapsed = time.time() - started

    write_namespace_counts(args.output_dir / "w1_namespace_counts.csv", namespace_counts)

    run_config = {
        "script_version": SCRIPT_VERSION,
        "python": sys.version,
        "platform": sys.platform,
        "wikipedia_path": str(args.wikipedia.resolve()),
        "wikipedia_size_bytes": args.wikipedia.stat().st_size,
        "wikipedia_mtime_ns": args.wikipedia.stat().st_mtime_ns,
        "max_pages": args.max_pages,
        "progress_every": args.progress_every,
        "full_dump_requested": args.max_pages == 0,
        "cwd": os.getcwd(),
    }
    (args.output_dir / "W1_RUN_CONFIG.json").write_text(
        json.dumps(run_config, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (args.output_dir / "w1_census.json").write_text(
        json.dumps(asdict(census), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (args.output_dir / "W1_FEATURE_SCHEMA.json").write_text(
        json.dumps(feature_schema(), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    report = build_report(census, namespace_counts, elapsed, args)
    (args.output_dir / "W1_REPORT.md").write_text(report, encoding="utf-8")

    print()
    print(report)
    print(f"Outputs: {args.output_dir.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
