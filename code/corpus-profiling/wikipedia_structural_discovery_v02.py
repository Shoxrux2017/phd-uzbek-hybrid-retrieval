#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Uzbek Wikipedia Structural Discovery — full-corpus pre-cleaning audit.

Purpose
-------
Scan the official Uzbek Wikipedia pages-articles dump in streaming mode and build
an evidence package for later human/Codex inspection BEFORE any cleaning policy
is designed.

The script:
1) censuses every XML <page>;
2) measures raw wikitext and extracted text separately;
3) writes one feature row per main-namespace, non-redirect, text-bearing page;
4) builds deterministic, interpretable structural signatures;
5) keeps representative examples for frequent and rare signatures;
6) keeps extreme/outlier examples on multiple model-independent feature axes;
7) inventories unusual Unicode code points;
8) produces deterministic Codex review candidates and small JSONL batches.

It deliberately DOES NOT:
- label pages as good/bad/severe;
- delete or rewrite the dump;
- use BM25, dense retrieval, qrels, retrieval metrics, or tokenizer overflow;
- apply retrieval-unit segmentation;
- infer corruption from a single feature such as a high digit ratio.

Python 3.12+
Dependencies:
    pip install lxml mwparserfromhell
"""

from __future__ import annotations

import argparse
import bz2
import csv
import hashlib
import heapq
import importlib.metadata
import json
import os
import platform
import random
import re
import sys
import time
import unicodedata
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, Iterator, List, Optional, TextIO, Tuple

SCRIPT_VERSION = "W-DISCOVERY-v0.2"
DEFAULT_SEED = 20260920

# ------------------------------ regex layer ------------------------------

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
RAW_INFOBOX_HINT_RE = re.compile(r"(?i)\{\{\s*(?:infobox|taxobox|geobox|chembox|sidebar)\b")
RAW_NAV_HINT_RE = re.compile(r"(?i)\{\{\s*(?:navbox|navigation|navbar)\b")
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


# ------------------------------- data types ------------------------------

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


@dataclass
class SignatureState:
    count: int = 0
    # max-heap by deterministic hash score using negative score; stores smallest scores
    examples: List[Tuple[int, str, Dict[str, Any]]] = None  # type: ignore[assignment]

    def __post_init__(self) -> None:
        if self.examples is None:
            self.examples = []


class TopKTracker:
    """Keep deterministic top-k maxima or minima by one numeric feature."""

    def __init__(self, name: str, k: int, mode: str = "max"):
        self.name = name
        self.k = k
        if mode not in {"max", "min"}:
            raise ValueError("mode must be max or min")
        self.mode = mode
        self.heap: List[Tuple[float, str, Dict[str, Any]]] = []

    def offer(self, value: float, tie: str, example: Dict[str, Any]) -> None:
        # Convert minima into maxima of -value. Heap retains k largest scores.
        score = value if self.mode == "max" else -value
        item = (score, tie, example)
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, item)
        elif item[:2] > self.heap[0][:2]:
            heapq.heapreplace(self.heap, item)

    def results(self) -> List[Dict[str, Any]]:
        ordered = sorted(self.heap, key=lambda x: (x[0], x[1]), reverse=True)
        out = []
        for score, _tie, ex in ordered:
            row = dict(ex)
            row["outlier_axis"] = self.name
            row["outlier_direction"] = self.mode
            row["outlier_value"] = score if self.mode == "max" else -score
            out.append(row)
        return out


# ------------------------------- utilities -------------------------------

def safe_ratio(num: int | float, den: int | float) -> float:
    return float(num) / float(den) if den else 0.0


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


def stable_score(seed: int, scope: str, page_id: str) -> int:
    payload = f"{seed}|{scope}|{page_id}".encode("utf-8", errors="replace")
    return int.from_bytes(hashlib.blake2b(payload, digest_size=8).digest(), "big")


def version_or_unknown(dist: str) -> str:
    try:
        return importlib.metadata.version(dist)
    except Exception:
        return "unknown"


def smart_excerpt(text: str, max_chars: int) -> str:
    """Head + longest-token context + tail; preserves evidence without full text dump."""
    s = (text or "").replace("\r\n", "\n").replace("\r", "\n")
    if len(s) <= max_chars:
        return s
    head_n = max_chars // 3
    tail_n = max_chars // 4
    focus_n = max_chars - head_n - tail_n - 80

    longest_match = None
    for m in re.finditer(r"\S+", s):
        if longest_match is None or (m.end() - m.start()) > (longest_match.end() - longest_match.start()):
            longest_match = m

    if longest_match is not None:
        center = (longest_match.start() + longest_match.end()) // 2
    else:
        center = len(s) // 2
    a = max(0, center - focus_n // 2)
    b = min(len(s), a + focus_n)
    focus = s[a:b]
    return (
        s[:head_n]
        + "\n\n[...FOCUS AROUND LONGEST TOKEN / MIDDLE...]\n\n"
        + focus
        + "\n\n[...TAIL...]\n\n"
        + s[-tail_n:]
    )


def token_transition_count(token: str) -> int:
    return len(ALPHA_DIGIT_TRANSITION_RE.findall(token or ""))


def repeated_line_stats(lines: List[str]) -> Tuple[int, float]:
    nonempty = [line.strip() for line in lines if line.strip()]
    if not nonempty:
        return 0, 0.0
    counts = Counter(nonempty)
    repeated_instances = sum(v - 1 for v in counts.values() if v > 1)
    return repeated_instances, safe_ratio(repeated_instances, len(nonempty))


def script_class(text: str) -> str:
    latin = len(LATIN_RE.findall(text or ""))
    cyr = len(CYRILLIC_RE.findall(text or ""))
    if latin and cyr:
        total = latin + cyr
        minor = min(latin, cyr) / total
        return "MIXED_BALANCED" if minor >= 0.10 else "MIXED_MINOR"
    if latin:
        return "LATIN"
    if cyr:
        return "CYRILLIC"
    return "NO_LATIN_CYR"


# ---------------------------- feature extraction -------------------------

def text_features(text: str, prefix: str) -> Dict[str, Any]:
    s = text or ""
    chars = len(s)
    utf8_bytes = len(s.encode("utf-8"))
    lines = s.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    nonempty_lines = [line for line in lines if line.strip()]
    tokens = s.split()

    alpha = digit = whitespace = punct = 0
    controls = formats = private_use = replacement = symbols = combining = 0
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
        if cat.startswith("M"):
            combining += 1
        if cat.startswith("S"):
            symbols += 1
        if ch == "\ufffd":
            replacement += 1

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
    apostrophe_present = "".join(v for v in APOSTROPHE_VARIANTS if v in s)

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
        f"{prefix}_symbol_ratio": round(safe_ratio(symbols, chars), 8),
        f"{prefix}_latin_letters": latin,
        f"{prefix}_cyrillic_letters": cyrillic,
        f"{prefix}_latin_share_of_latin_cyr": round(safe_ratio(latin, latin + cyrillic), 8),
        f"{prefix}_cyrillic_share_of_latin_cyr": round(safe_ratio(cyrillic, latin + cyrillic), 8),
        f"{prefix}_mixed_latin_cyrillic": int(bool(latin and cyrillic)),
        f"{prefix}_control_chars": controls,
        f"{prefix}_format_chars": formats,
        f"{prefix}_private_use_chars": private_use,
        f"{prefix}_replacement_chars": replacement,
        f"{prefix}_combining_marks": combining,
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
        "raw_infobox_hint_count": len(RAW_INFOBOX_HINT_RE.findall(raw)),
        "raw_nav_hint_count": len(RAW_NAV_HINT_RE.findall(raw)),
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
    extracted = unicodedata.normalize("NFC", extracted or "")
    extracted = extracted.replace("\r\n", "\n").replace("\r", "\n")
    return extracted, code


# ------------------------------ XML layer --------------------------------

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
        "page_id": page_id,
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


# ---------------------------- signature layer ----------------------------

def count_bucket(v: int, cuts: Tuple[int, ...]) -> str:
    if v <= 0:
        return "0"
    prev = 1
    for cut in cuts:
        if v <= cut:
            return f"{prev}-{cut}" if prev != cut else str(cut)
        prev = cut + 1
    return f"{prev}+"


def ratio_bucket(v: float, cuts: Tuple[float, ...]) -> str:
    lo = 0.0
    for cut in cuts:
        if v < cut:
            return f"<{cut:g}"
        lo = cut
    return f">={lo:g}"


def length_bucket(words: int) -> str:
    if words == 0:
        return "0"
    if words <= 20:
        return "1-20"
    if words <= 100:
        return "21-100"
    if words <= 500:
        return "101-500"
    if words <= 1500:
        return "501-1500"
    return "1501+"


def max_token_bucket(v: int) -> str:
    if v < 25:
        return "<25"
    if v < 40:
        return "25-39"
    if v < 80:
        return "40-79"
    if v < 160:
        return "80-159"
    return "160+"


def compression_bucket(v: float) -> str:
    if v < 0.05:
        return "<0.05"
    if v < 0.15:
        return "0.05-0.15"
    if v < 0.35:
        return "0.15-0.35"
    if v < 0.65:
        return "0.35-0.65"
    if v < 0.90:
        return "0.65-0.90"
    if v <= 1.10:
        return "0.90-1.10"
    return ">1.10"


def build_signatures(row: Dict[str, Any], extracted: str) -> Tuple[str, str, str]:
    """Build COARSE structural archetypes for discovery grouping.

    Important:
    - these are NOT validity/corruption labels;
    - normal/neutral feature bins are deliberately omitted;
    - detailed numeric features remain in page_features.csv for later rare-tail analysis.

    The v0.1 Cartesian signature was too granular on the 5k smoke run
    (1,089 joint signatures for 3,043 pages). v0.2 therefore uses sparse,
    interpretable tags that group structurally similar pages more broadly.
    """
    raw_tags: List[str] = []

    templates = int(row["raw_template_ast_count"])
    tables = int(row["raw_table_start_count"])
    list_lines = int(row["raw_list_line_count"])
    refs = int(row["raw_ref_tag_count"])
    files = int(row["raw_file_link_count"])
    galleries = int(row["raw_gallery_tag_count"])
    urls = int(row["raw_url_count"])
    kv = int(row["raw_key_value_line_count"])
    headings = int(row["raw_heading_line_count"])

    if templates > 0:
        raw_tags.append("TEMPLATE_PRESENT")
    if templates >= 10:
        raw_tags.append("TEMPLATE_HEAVY")
    if tables > 0:
        raw_tags.append("TABLE_PRESENT")
    if tables >= 4:
        raw_tags.append("TABLE_HEAVY")
    if list_lines >= 5:
        raw_tags.append("LIST_PRESENT")
    if list_lines >= 20:
        raw_tags.append("LIST_HEAVY")
    if refs > 0:
        raw_tags.append("REF_PRESENT")
    if refs >= 10:
        raw_tags.append("REF_HEAVY")
    if files > 0:
        raw_tags.append("MEDIA_PRESENT")
    if galleries > 0:
        raw_tags.append("GALLERY_PRESENT")
    if urls > 0:
        raw_tags.append("URL_PRESENT")
    if kv >= 5:
        raw_tags.append("KEYVALUE_PRESENT")
    if kv >= 20:
        raw_tags.append("KEYVALUE_HEAVY")
    if int(row["raw_infobox_hint_count"]) > 0:
        raw_tags.append("INFOBOX_HINT")
    if int(row["raw_nav_hint_count"]) > 0:
        raw_tags.append("NAV_HINT")
    if headings >= 5:
        raw_tags.append("HEADING_RICH")

    raw_sig = "+".join(raw_tags) if raw_tags else "RAW_BASELINE"

    surface_tags: List[str] = []
    script = script_class(extracted)
    words = int(row["extracted_words_ws"])
    max_tok = int(row["extracted_max_token_len"])
    digit_ratio = float(row["extracted_digit_ratio"])
    punct_ratio = float(row["extracted_punct_ratio"])
    whitespace_ratio = float(row["extracted_whitespace_ratio"])
    alpha_ratio = float(row["extracted_alpha_ratio"])
    transitions = int(row["extracted_alpha_digit_transitions"])
    glued_tokens = int(row["extracted_glued_transition_tokens"])
    long_digit_runs = int(row["extracted_long_digit_runs"])
    repeated_line_ratio = float(row["extracted_repeated_line_ratio"])
    residue = int(row["extracted_wiki_residue_count"])
    extraction_ratio = float(row["extracted_to_raw_char_ratio"])
    unicode_special = (
        int(row["extracted_control_chars"])
        + int(row["extracted_format_chars"])
        + int(row["extracted_private_use_chars"])
        + int(row["extracted_replacement_chars"])
    )

    # Latin prose is the neutral script condition and is therefore omitted.
    if script == "CYRILLIC":
        surface_tags.append("SCRIPT_CYRILLIC")
    elif script == "MIXED_BALANCED":
        surface_tags.append("SCRIPT_MIXED_BALANCED")
    elif script == "MIXED_MINOR":
        surface_tags.append("SCRIPT_MIXED_MINOR")
    elif script == "NO_LATIN_CYR":
        surface_tags.append("SCRIPT_OTHER_OR_NONE")

    if words <= 20:
        surface_tags.append("VERY_SHORT")
    elif words > 1500:
        surface_tags.append("VERY_LONG")

    if max_tok >= 40:
        surface_tags.append("LONG_TOKEN")
    if max_tok >= 80:
        surface_tags.append("EXTREME_TOKEN")

    if digit_ratio >= 0.15:
        surface_tags.append("DIGIT_HIGH")
    if digit_ratio >= 0.30:
        surface_tags.append("DIGIT_VERY_HIGH")
    if punct_ratio >= 0.20:
        surface_tags.append("PUNCT_HIGH")
    if whitespace_ratio < 0.05:
        surface_tags.append("WHITESPACE_LOW")
    if alpha_ratio < 0.50:
        surface_tags.append("ALPHA_LOW")
    if transitions >= 10:
        surface_tags.append("ALNUM_TRANSITIONS_HIGH")
    if glued_tokens > 0:
        surface_tags.append("GLUED_TRANSITION_TOKEN")
    if long_digit_runs >= 2:
        surface_tags.append("LONG_DIGIT_RUNS")
    if repeated_line_ratio >= 0.20:
        surface_tags.append("REPEATED_LINES")
    if residue > 0:
        surface_tags.append("WIKI_RESIDUE")
    if unicode_special > 0:
        surface_tags.append("UNICODE_SPECIAL")

    if extraction_ratio < 0.15:
        surface_tags.append("EXTRACTION_EXTREME_LOSS")
    elif extraction_ratio < 0.35:
        surface_tags.append("EXTRACTION_LARGE_LOSS")
    elif extraction_ratio > 1.10:
        surface_tags.append("EXTRACTION_EXPANSION")

    if int(row["extracted_list_line_count"]) >= 20:
        surface_tags.append("EXTRACTED_LIST_HEAVY")
    if int(row["extracted_key_value_line_count"]) >= 20:
        surface_tags.append("EXTRACTED_KEYVALUE_HEAVY")
    if int(row["title_occurrences_in_extracted"]) > 1:
        surface_tags.append("TITLE_REPEATED")

    ext_sig = "+".join(surface_tags) if surface_tags else "SURFACE_BASELINE"
    return raw_sig, ext_sig, raw_sig + "||" + ext_sig


# ----------------------- deterministic example sampling ------------------

def example_record(
    page: Dict[str, Any],
    row: Dict[str, Any],
    raw: str,
    extracted: str,
    joint_signature: str,
    max_chars: int,
) -> Dict[str, Any]:
    return {
        "page_id": page["page_id"],
        "title": page["title"],
        "joint_signature": joint_signature,
        "raw_chars": row["raw_chars"],
        "extracted_chars": row["extracted_chars"],
        "extracted_words_ws": row["extracted_words_ws"],
        "extracted_digit_ratio": row["extracted_digit_ratio"],
        "extracted_punct_ratio": row["extracted_punct_ratio"],
        "extracted_whitespace_ratio": row["extracted_whitespace_ratio"],
        "extracted_max_token_len": row["extracted_max_token_len"],
        "extracted_alpha_digit_transitions": row["extracted_alpha_digit_transitions"],
        "extracted_repeated_line_ratio": row["extracted_repeated_line_ratio"],
        "extracted_wiki_residue_count": row["extracted_wiki_residue_count"],
        "raw_template_ast_count": row["raw_template_ast_count"],
        "raw_table_start_count": row["raw_table_start_count"],
        "raw_list_line_count": row["raw_list_line_count"],
        "raw_ref_tag_count": row["raw_ref_tag_count"],
        "raw_file_link_count": row["raw_file_link_count"],
        "extracted_to_raw_char_ratio": row["extracted_to_raw_char_ratio"],
        "raw_excerpt": smart_excerpt(raw, max_chars),
        "extracted_excerpt": smart_excerpt(extracted, max_chars),
    }


def offer_signature_example(
    state: SignatureState,
    example: Dict[str, Any],
    signature: str,
    page_id: str,
    seed: int,
    k: int,
) -> None:
    score = stable_score(seed, "signature:" + signature, page_id)
    item = (-score, page_id, example)  # root = largest score => easiest to replace
    if len(state.examples) < k:
        heapq.heappush(state.examples, item)
    else:
        current_largest = -state.examples[0][0]
        if score < current_largest:
            heapq.heapreplace(state.examples, item)


def signature_examples(state: SignatureState) -> List[Dict[str, Any]]:
    return [x[2] for x in sorted(state.examples, key=lambda x: (-x[0], x[1]))]


# -------------------------- Unicode inventory ----------------------------

def update_unicode_inventory(
    text: str,
    counter: Counter[str],
    examples: Dict[str, Tuple[int, Dict[str, Any]]],
    example: Dict[str, Any],
    page_id: str,
    seed: int,
    scope: str,
) -> None:
    # Count non-ASCII non-whitespace plus invisible/control/private-use codepoints.
    local = Counter()
    for ch in text or "":
        cat = unicodedata.category(ch)
        if (ord(ch) > 127 and not ch.isspace()) or cat in {"Cc", "Cf", "Co"}:
            local[ch] += 1
    if not local:
        return
    counter.update(local)
    for ch in local:
        score = stable_score(seed, f"unicode:{scope}:{ord(ch)}", page_id)
        cur = examples.get(ch)
        if cur is None or score < cur[0]:
            examples[ch] = (score, example)


# --------------------------- output helpers ------------------------------

def write_rows(path: Path, rows: Iterable[Dict[str, Any]], fieldnames: Optional[List[str]] = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    rows = list(rows)
    if not rows:
        path.write_text("", encoding="utf-8-sig")
        return
    if fieldnames is None:
        fieldnames = list(rows[0].keys())
    with path.open("w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def write_jsonl(path: Path, rows: Iterable[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")


def write_signature_counts(path: Path, states: Dict[str, SignatureState]) -> None:
    rows = [
        {"signature": sig, "pages": st.count}
        for sig, st in sorted(states.items(), key=lambda kv: (-kv[1].count, kv[0]))
    ]
    write_rows(path, rows)


def unicode_rows(
    counter: Counter[str], examples: Dict[str, Tuple[int, Dict[str, Any]]]
) -> List[Dict[str, Any]]:
    rows = []
    for ch, count in sorted(counter.items(), key=lambda kv: (kv[1], ord(kv[0]))):
        score, example = examples.get(ch, (0, {}))
        page_id = str(example.get("page_id", ""))
        title = str(example.get("title", ""))
        rows.append({
            "codepoint": f"U+{ord(ch):04X}",
            "char": ch,
            "unicode_name": unicodedata.name(ch, "<UNNAMED>"),
            "category": unicodedata.category(ch),
            "count": count,
            "sample_page_id": page_id,
            "sample_title": title,
        })
    return rows


# ------------------------ Codex candidate builder ------------------------

def add_candidate(
    selected: Dict[str, Dict[str, Any]],
    ex: Dict[str, Any],
    reason: str,
    signature_population: Optional[int] = None,
) -> None:
    pid = str(ex["page_id"])
    if pid not in selected:
        selected[pid] = dict(ex)
        selected[pid]["selection_reasons"] = []
        selected[pid]["signature_population"] = signature_population
    selected[pid]["selection_reasons"].append(reason)
    if signature_population is not None:
        selected[pid]["signature_population"] = signature_population


def build_codex_candidates(
    joint_states: Dict[str, SignatureState],
    baseline_examples: List[Dict[str, Any]],
    outlier_trackers: Dict[str, TopKTracker],
    unicode_counter: Counter[str],
    unicode_examples: Dict[str, Tuple[int, Dict[str, Any]]],
    example_by_page: Dict[str, Dict[str, Any]],
    args: argparse.Namespace,
) -> List[Dict[str, Any]]:
    selected: Dict[str, Dict[str, Any]] = {}

    for ex in baseline_examples:
        add_candidate(selected, ex, "RANDOM_BASELINE")

    top_sigs = sorted(joint_states.items(), key=lambda kv: (-kv[1].count, kv[0]))[: args.frequent_signature_count]
    for sig, st in top_sigs:
        for ex in signature_examples(st)[: args.frequent_examples_per_signature]:
            add_candidate(selected, ex, "FREQUENT_SIGNATURE", st.count)

    rare_sigs = [(sig, st) for sig, st in joint_states.items() if st.count <= args.rare_signature_max_count]
    rare_sigs.sort(key=lambda kv: stable_score(args.seed, "rare-signature", kv[0]))
    for sig, st in rare_sigs[: args.rare_signature_count]:
        exs = signature_examples(st)
        if exs:
            add_candidate(selected, exs[0], "RARE_SIGNATURE", st.count)

    for axis, tracker in sorted(outlier_trackers.items()):
        for ex in tracker.results():
            add_candidate(selected, ex, f"OUTLIER:{axis}")

    rare_chars = [(ch, n) for ch, n in unicode_counter.items() if n <= args.rare_unicode_max_count]
    rare_chars.sort(key=lambda kv: (kv[1], stable_score(args.seed, "rare-unicode", str(ord(kv[0])))))
    for ch, n in rare_chars[: args.rare_unicode_count]:
        rec = unicode_examples.get(ch)
        if not rec:
            continue
        _score, ex = rec
        if ex:
            add_candidate(selected, ex, f"RARE_UNICODE:U+{ord(ch):04X}:count={n}")

    # Deterministic stable order, while prioritizing breadth-rich cases.
    rows = list(selected.values())
    for row in rows:
        row["selection_reasons"] = sorted(set(row["selection_reasons"]))
        row["candidate_id"] = f"UZWP-{row['page_id']}"
        row["review_fields"] = {
            "human_or_codex_category": "",
            "issue_tags": [],
            "action_candidate": "",
            "notes": "",
        }
    rows.sort(
        key=lambda r: (
            -len(r["selection_reasons"]),
            stable_score(args.seed, "codex-order", str(r["page_id"])),
        )
    )
    return rows[: args.codex_candidate_cap]


def write_batches(out_dir: Path, candidates: List[Dict[str, Any]], batch_size: int) -> int:
    batch_dir = out_dir / "codex_batches"
    batch_dir.mkdir(parents=True, exist_ok=True)
    batch_count = 0
    for i in range(0, len(candidates), batch_size):
        batch_count += 1
        batch = candidates[i:i + batch_size]
        write_jsonl(batch_dir / f"batch_{batch_count:03d}.jsonl", batch)
    return batch_count


# ------------------------------ report -----------------------------------

def build_report(
    census: Census,
    namespace_counts: Counter[str],
    raw_states: Dict[str, SignatureState],
    ext_states: Dict[str, SignatureState],
    joint_states: Dict[str, SignatureState],
    candidates: List[Dict[str, Any]],
    batch_count: int,
    elapsed: float,
    dump_sha256: str,
    args: argparse.Namespace,
) -> str:
    den = max(1, census.feature_rows_written)
    lines = [
        "# Uzbek Wikipedia Structural Discovery",
        "",
        f"**Script:** `{SCRIPT_VERSION}`",
        "",
        "## Scientific boundary",
        "",
        "This run performs structural discovery only. It does not declare pages valid/invalid,",
        "does not remove content, and does not use retrieval effectiveness, qrels, BM25, dense",
        "retrieval, tokenizer overflow, or retrieval-unit segmentation.",
        "",
        "## Census",
        "",
        f"- XML pages seen: **{census.pages_total:,}**",
        f"- Main namespace pages: **{census.main_namespace_pages:,}**",
        f"- Non-main namespace pages: **{census.non_main_namespace_pages:,}**",
        f"- Redirects total: **{census.redirects_total:,}**",
        f"- Main namespace redirects: **{census.main_namespace_redirects:,}**",
        f"- Main non-redirect text-bearing pages: **{census.main_nonredirect_text_pages:,}**",
        f"- Feature rows written: **{census.feature_rows_written:,}**",
        f"- Extraction success: **{census.extraction_success:,}**",
        f"- Extraction empty: **{census.extraction_empty:,}** ({100*census.extraction_empty/den:.4f}%)",
        f"- Extraction failures: **{census.extraction_failures:,}** ({100*census.extraction_failures/den:.4f}%)",
        "",
        "## Discovery grouping",
        "",
        f"- Distinct raw structural signatures: **{len(raw_states):,}**",
        f"- Distinct extracted-surface signatures: **{len(ext_states):,}**",
        f"- Distinct joint signatures: **{len(joint_states):,}**",
        f"- Joint signatures with population <= {args.rare_signature_max_count}: **{sum(st.count <= args.rare_signature_max_count for st in joint_states.values()):,}**",
        "",
        "A signature is a coarse deterministic structural archetype for discovery. It is not a corruption label. Detailed numeric features remain in page_features.csv for later rare-tail/outlier analysis.",
        "",
        "## Codex review package",
        "",
        f"- Review candidates: **{len(candidates):,}**",
        f"- Batch size: **{args.batch_size}**",
        f"- Batch files: **{batch_count}**",
        "",
        "Candidate selection mixes random baseline pages, frequent signatures, rare signatures,",
        "multiple extreme feature axes, and rare Unicode cases. Real raw/extracted excerpts are",
        "included so later interpretation is based on text rather than numbers alone.",
        "",
        "## Namespace counts",
        "",
        "| Namespace | Pages |",
        "|---:|---:|",
    ]
    for ns, count in sorted(namespace_counts.items(), key=lambda kv: (-kv[1], kv[0])):
        lines.append(f"| {ns or '(blank)'} | {count:,} |")

    lines += [
        "",
        "## Reproducibility",
        "",
        f"- Input: `{args.wikipedia}`",
        f"- Input bytes: `{args.wikipedia.stat().st_size}`",
        f"- Input SHA-256: `{dump_sha256}`",
        f"- Seed: `{args.seed}`",
        f"- Max XML pages: `{args.max_pages if args.max_pages else 'FULL'}`",
        f"- Example chars per representation: `{args.example_chars}`",
        f"- Elapsed seconds: `{elapsed:.2f}`",
        f"- Python: `{platform.python_version()}`",
        f"- lxml: `{version_or_unknown('lxml')}`",
        f"- mwparserfromhell: `{version_or_unknown('mwparserfromhell')}`",
        "",
        "## Next step",
        "",
        "Do not write cleaning rules from this report alone. First review the generated Codex batches,",
        "interpret frequent and rare groups from their real examples, add new issue classes when needed,",
        "and only then construct an evidence-backed taxonomy and deterministic cleaning policy.",
        "",
    ]
    return "\n".join(lines)


# ----------------------------- main scan ---------------------------------

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Full-corpus structural discovery for Uzbek Wikipedia before cleaning",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument("--wikipedia", type=Path, required=True)
    p.add_argument("--output-dir", type=Path, required=True)
    p.add_argument("--max-pages", type=int, default=0, help="Smoke-test XML page cap; 0 = full dump")
    p.add_argument("--progress-every", type=int, default=10000)
    p.add_argument("--seed", type=int, default=DEFAULT_SEED)
    p.add_argument("--signature-examples", type=int, default=3)
    p.add_argument("--example-chars", type=int, default=4000)
    p.add_argument("--baseline-count", type=int, default=80)
    p.add_argument("--outlier-per-axis", type=int, default=20)
    p.add_argument("--frequent-signature-count", type=int, default=40)
    p.add_argument("--frequent-examples-per-signature", type=int, default=2)
    p.add_argument("--rare-signature-max-count", type=int, default=3)
    p.add_argument("--rare-signature-count", type=int, default=120)
    p.add_argument("--rare-unicode-max-count", type=int, default=5)
    p.add_argument("--rare-unicode-count", type=int, default=80)
    p.add_argument("--codex-candidate-cap", type=int, default=800)
    p.add_argument("--batch-size", type=int, default=50)
    return p.parse_args()


def main() -> int:
    args = parse_args()
    if not args.wikipedia.exists() or not args.wikipedia.is_file():
        print(f"ERROR: Wikipedia dump not found: {args.wikipedia}", file=sys.stderr)
        return 2
    if args.max_pages < 0 or args.progress_every <= 0 or args.signature_examples <= 0:
        print("ERROR: invalid numeric arguments", file=sys.stderr)
        return 2

    try:
        import lxml  # noqa: F401
        import mwparserfromhell  # noqa: F401
    except ImportError as exc:
        print("ERROR: install dependencies: pip install lxml mwparserfromhell", file=sys.stderr)
        print(exc, file=sys.stderr)
        return 3

    args.output_dir.mkdir(parents=True, exist_ok=True)
    started = time.time()
    print(f"[{SCRIPT_VERSION}] hashing input dump...", flush=True)
    dump_sha256 = file_sha256(args.wikipedia)
    print(f"[{SCRIPT_VERSION}] input SHA-256: {dump_sha256}", flush=True)

    census = Census()
    namespace_counts: Counter[str] = Counter()
    feature_writer = CsvStreamWriter(args.output_dir / "page_features.csv")
    failure_writer = CsvStreamWriter(args.output_dir / "extraction_failures.csv")

    raw_states: Dict[str, SignatureState] = {}
    ext_states: Dict[str, SignatureState] = {}
    joint_states: Dict[str, SignatureState] = {}

    # Deterministic global random-baseline sample: keep lowest hash scores.
    baseline_heap: List[Tuple[int, str, Dict[str, Any]]] = []

    outlier_trackers: Dict[str, TopKTracker] = {
        "MAX_EXTRACTED_WORDS": TopKTracker("MAX_EXTRACTED_WORDS", args.outlier_per_axis, "max"),
        "MIN_EXTRACTED_WORDS_NONEMPTY": TopKTracker("MIN_EXTRACTED_WORDS_NONEMPTY", args.outlier_per_axis, "min"),
        "MAX_EXTRACTED_TOKEN_LEN": TopKTracker("MAX_EXTRACTED_TOKEN_LEN", args.outlier_per_axis, "max"),
        "MAX_DIGIT_RATIO": TopKTracker("MAX_DIGIT_RATIO", args.outlier_per_axis, "max"),
        "MAX_PUNCT_RATIO": TopKTracker("MAX_PUNCT_RATIO", args.outlier_per_axis, "max"),
        "MAX_SYMBOL_RATIO": TopKTracker("MAX_SYMBOL_RATIO", args.outlier_per_axis, "max"),
        "MIN_WHITESPACE_RATIO": TopKTracker("MIN_WHITESPACE_RATIO", args.outlier_per_axis, "min"),
        "MIN_ALPHA_RATIO": TopKTracker("MIN_ALPHA_RATIO", args.outlier_per_axis, "min"),
        "MAX_ALPHA_DIGIT_TRANSITIONS": TopKTracker("MAX_ALPHA_DIGIT_TRANSITIONS", args.outlier_per_axis, "max"),
        "MAX_LONG_DIGIT_RUNS": TopKTracker("MAX_LONG_DIGIT_RUNS", args.outlier_per_axis, "max"),
        "MAX_REPEATED_LINE_RATIO": TopKTracker("MAX_REPEATED_LINE_RATIO", args.outlier_per_axis, "max"),
        "MAX_RAW_TABLES": TopKTracker("MAX_RAW_TABLES", args.outlier_per_axis, "max"),
        "MAX_RAW_TEMPLATES": TopKTracker("MAX_RAW_TEMPLATES", args.outlier_per_axis, "max"),
        "MAX_RAW_LIST_LINES": TopKTracker("MAX_RAW_LIST_LINES", args.outlier_per_axis, "max"),
        "MAX_EXTRACTED_WIKI_RESIDUE": TopKTracker("MAX_EXTRACTED_WIKI_RESIDUE", args.outlier_per_axis, "max"),
        "MAX_CONTROL_FORMAT_PRIVATE_REPLACEMENT": TopKTracker("MAX_CONTROL_FORMAT_PRIVATE_REPLACEMENT", args.outlier_per_axis, "max"),
        "MIN_EXTRACTION_CHAR_RATIO": TopKTracker("MIN_EXTRACTION_CHAR_RATIO", args.outlier_per_axis, "min"),
        "MAX_EXTRACTION_CHAR_RATIO": TopKTracker("MAX_EXTRACTION_CHAR_RATIO", args.outlier_per_axis, "max"),
        "MAX_TITLE_REPETITION": TopKTracker("MAX_TITLE_REPETITION", args.outlier_per_axis, "max"),
    }

    raw_unicode: Counter[str] = Counter()
    ext_unicode: Counter[str] = Counter()
    raw_unicode_examples: Dict[str, Tuple[int, Dict[str, Any]]] = {}
    ext_unicode_examples: Dict[str, Tuple[int, Dict[str, Any]]] = {}

    # Only examples that survive one of our deterministic samplers live in memory.
    # This lookup is populated for every retained sampler example, enabling rare-Unicode selection.
    example_by_page: Dict[str, Dict[str, Any]] = {}

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
            if page["has_text_node"] and not page["raw"]:
                census.pages_with_empty_text += 1

            if ns == "0" and not page["is_redirect"]:
                if not page["raw"].strip():
                    census.main_nonredirect_empty_text_pages += 1
                else:
                    census.main_nonredirect_text_pages += 1
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
                        "namespace": ns,
                        "raw_nonempty": 1,
                        "extraction_ok": int(extraction_error is None),
                        "extraction_empty": int(extraction_error is None and not extracted.strip()),
                    }
                    row.update(text_features(raw, "raw"))

                    if code is not None:
                        row.update(raw_wiki_features(raw, code))
                    else:
                        row.update({
                            "raw_template_open_count": raw.count("{{"),
                            "raw_template_close_count": raw.count("}}"),
                            "raw_template_ast_count": 0,
                            "raw_table_start_count": raw.count("{|"),
                            "raw_table_end_count": raw.count("|}"),
                            "raw_table_row_marker_count": 0,
                            "raw_table_cell_like_line_count": 0,
                            "raw_wikilink_open_count": raw.count("[["),
                            "raw_wikilink_ast_count": 0,
                            "raw_external_link_count": len(RAW_EXTERNAL_LINK_RE.findall(raw)),
                            "raw_url_count": len(URL_RE.findall(raw)),
                            "raw_ref_tag_count": len(RAW_REF_RE.findall(raw)),
                            "raw_references_tag_count": len(RAW_REFERENCES_RE.findall(raw)),
                            "raw_gallery_tag_count": len(RAW_GALLERY_RE.findall(raw)),
                            "raw_html_tag_count": len(RAW_HTML_TAG_RE.findall(raw)),
                            "raw_tag_ast_count": 0,
                            "raw_file_link_count": len(RAW_FILE_RE.findall(raw)),
                            "raw_category_link_count": len(RAW_CATEGORY_RE.findall(raw)),
                            "raw_infobox_hint_count": len(RAW_INFOBOX_HINT_RE.findall(raw)),
                            "raw_nav_hint_count": len(RAW_NAV_HINT_RE.findall(raw)),
                            "raw_heading_line_count": 0,
                            "raw_list_line_count": 0,
                            "raw_key_value_line_count": 0,
                            "raw_pipe_chars": raw.count("|"),
                            "raw_equals_chars": raw.count("="),
                        })

                    if extraction_error is None:
                        census.extraction_success += 1
                        if not extracted.strip():
                            census.extraction_empty += 1
                        row.update(text_features(extracted, "extracted"))
                        row.update(extracted_residue_features(extracted))
                        row["extracted_to_raw_char_ratio"] = round(safe_ratio(len(extracted), len(raw)), 8)
                        row["extracted_to_raw_word_ratio"] = round(safe_ratio(len(extracted.split()), len(raw.split())), 8)
                        title_norm = unicodedata.normalize("NFC", page["title"] or "").strip().casefold()
                        row["title_occurrences_in_extracted"] = extracted.casefold().count(title_norm) if title_norm else 0

                        raw_sig, ext_sig, joint_sig = build_signatures(row, extracted)
                        row["raw_signature"] = raw_sig
                        row["extracted_signature"] = ext_sig
                        row["joint_signature"] = joint_sig

                        ex = example_record(page, row, raw, extracted, joint_sig, args.example_chars)

                        for sig, states in ((raw_sig, raw_states), (ext_sig, ext_states), (joint_sig, joint_states)):
                            st = states.get(sig)
                            if st is None:
                                st = SignatureState()
                                states[sig] = st
                            st.count += 1
                            # Store examples only for joint groups; raw/extracted group examples are not needed.
                            if states is joint_states:
                                offer_signature_example(st, ex, sig, str(page["page_id"]), args.seed, args.signature_examples)

                        # Global deterministic baseline.
                        bscore = stable_score(args.seed, "baseline", str(page["page_id"]))
                        bitem = (-bscore, str(page["page_id"]), ex)
                        if len(baseline_heap) < args.baseline_count:
                            heapq.heappush(baseline_heap, bitem)
                        elif bscore < -baseline_heap[0][0]:
                            heapq.heapreplace(baseline_heap, bitem)

                        # Extreme axes.
                        tie = f"{stable_score(args.seed, 'outlier-tie', str(page['page_id'])):020d}:{page['page_id']}"
                        unicode_problem_count = (
                            int(row["extracted_control_chars"]) + int(row["extracted_format_chars"])
                            + int(row["extracted_private_use_chars"]) + int(row["extracted_replacement_chars"])
                        )
                        values = {
                            "MAX_EXTRACTED_WORDS": float(row["extracted_words_ws"]),
                            "MIN_EXTRACTED_WORDS_NONEMPTY": float(row["extracted_words_ws"]),
                            "MAX_EXTRACTED_TOKEN_LEN": float(row["extracted_max_token_len"]),
                            "MAX_DIGIT_RATIO": float(row["extracted_digit_ratio"]),
                            "MAX_PUNCT_RATIO": float(row["extracted_punct_ratio"]),
                            "MAX_SYMBOL_RATIO": float(row["extracted_symbol_ratio"]),
                            "MIN_WHITESPACE_RATIO": float(row["extracted_whitespace_ratio"]),
                            "MIN_ALPHA_RATIO": float(row["extracted_alpha_ratio"]),
                            "MAX_ALPHA_DIGIT_TRANSITIONS": float(row["extracted_alpha_digit_transitions"]),
                            "MAX_LONG_DIGIT_RUNS": float(row["extracted_long_digit_runs"]),
                            "MAX_REPEATED_LINE_RATIO": float(row["extracted_repeated_line_ratio"]),
                            "MAX_RAW_TABLES": float(row["raw_table_start_count"]),
                            "MAX_RAW_TEMPLATES": float(row["raw_template_ast_count"]),
                            "MAX_RAW_LIST_LINES": float(row["raw_list_line_count"]),
                            "MAX_EXTRACTED_WIKI_RESIDUE": float(row["extracted_wiki_residue_count"]),
                            "MAX_CONTROL_FORMAT_PRIVATE_REPLACEMENT": float(unicode_problem_count),
                            "MIN_EXTRACTION_CHAR_RATIO": float(row["extracted_to_raw_char_ratio"]),
                            "MAX_EXTRACTION_CHAR_RATIO": float(row["extracted_to_raw_char_ratio"]),
                            "MAX_TITLE_REPETITION": float(row["title_occurrences_in_extracted"]),
                        }
                        for axis, value in values.items():
                            if axis == "MIN_EXTRACTED_WORDS_NONEMPTY" and value <= 0:
                                continue
                            outlier_trackers[axis].offer(value, tie, ex)

                        update_unicode_inventory(raw, raw_unicode, raw_unicode_examples, ex, str(page["page_id"]), args.seed, "raw")
                        update_unicode_inventory(extracted, ext_unicode, ext_unicode_examples, ex, str(page["page_id"]), args.seed, "extracted")

                    else:
                        census.extraction_failures += 1
                        row.update({
                            "extracted_chars": "", "extracted_utf8_bytes": "", "extracted_words_ws": "",
                            "extracted_lines": "", "extracted_nonempty_lines": "", "extracted_max_line_len": "",
                            "extracted_alpha_ratio": "", "extracted_digit_ratio": "", "extracted_whitespace_ratio": "",
                            "extracted_punct_ratio": "", "extracted_symbol_ratio": "", "extracted_latin_letters": "",
                            "extracted_cyrillic_letters": "", "extracted_latin_share_of_latin_cyr": "",
                            "extracted_cyrillic_share_of_latin_cyr": "", "extracted_mixed_latin_cyrillic": "",
                            "extracted_control_chars": "", "extracted_format_chars": "", "extracted_private_use_chars": "",
                            "extracted_replacement_chars": "", "extracted_combining_marks": "", "extracted_apostrophe_variants": "",
                            "extracted_max_token_len": "", "extracted_long_tokens_40": "", "extracted_long_tokens_80": "",
                            "extracted_long_tokens_120": "", "extracted_long_tokens_200": "", "extracted_alpha_digit_transitions": "",
                            "extracted_glued_transition_tokens": "", "extracted_long_digit_runs": "", "extracted_unique_token_ratio": "",
                            "extracted_top_token_share": "", "extracted_repeated_line_instances": "", "extracted_repeated_line_ratio": "",
                            "extracted_repeated_delimiter_runs": "", "extracted_sha256": "", "extracted_url_count": "",
                            "extracted_wiki_residue_count": "", "extracted_double_brace_count": "", "extracted_table_marker_count": "",
                            "extracted_pipe_chars": "", "extracted_equals_chars": "", "extracted_heading_line_count": "",
                            "extracted_list_line_count": "", "extracted_key_value_line_count": "", "extracted_to_raw_char_ratio": "",
                            "extracted_to_raw_word_ratio": "", "title_occurrences_in_extracted": "",
                            "raw_signature": "EXTRACTION_FAILED", "extracted_signature": "EXTRACTION_FAILED", "joint_signature": "EXTRACTION_FAILED",
                        })
                        failure_writer.write({
                            "page_id": page["page_id"],
                            "title": page["title"],
                            "error": extraction_error,
                            "raw_chars": len(raw),
                            "raw_excerpt": smart_excerpt(raw, min(args.example_chars, 2000)),
                        })

                    feature_writer.write(row)
                    census.feature_rows_written += 1

            if census.pages_total % args.progress_every == 0:
                elapsed = time.time() - started
                print(
                    f"pages={census.pages_total:,} main_text={census.main_nonredirect_text_pages:,} "
                    f"features={census.feature_rows_written:,} joint_signatures={len(joint_states):,} "
                    f"elapsed={elapsed:.1f}s",
                    flush=True,
                )

            if args.max_pages and census.pages_total >= args.max_pages:
                break

    finally:
        feature_writer.close()
        failure_writer.close()

    # Gather every retained example into a lookup for Unicode candidate resolution.
    for st in joint_states.values():
        for ex in signature_examples(st):
            example_by_page[str(ex["page_id"])] = ex
    baseline_examples = [x[2] for x in sorted(baseline_heap, key=lambda x: (-x[0], x[1]))]
    for ex in baseline_examples:
        example_by_page[str(ex["page_id"])] = ex
    for tracker in outlier_trackers.values():
        for ex in tracker.results():
            example_by_page[str(ex["page_id"])] = ex

    write_signature_counts(args.output_dir / "raw_signature_counts.csv", raw_states)
    write_signature_counts(args.output_dir / "extracted_signature_counts.csv", ext_states)
    write_signature_counts(args.output_dir / "joint_signature_counts.csv", joint_states)

    signature_example_rows = []
    for sig, st in sorted(joint_states.items(), key=lambda kv: (-kv[1].count, kv[0])):
        for idx, ex in enumerate(signature_examples(st), start=1):
            rec = dict(ex)
            rec["signature_population"] = st.count
            rec["example_rank"] = idx
            signature_example_rows.append(rec)
    write_jsonl(args.output_dir / "joint_signature_examples.jsonl", signature_example_rows)

    outlier_rows = []
    for axis, tracker in sorted(outlier_trackers.items()):
        outlier_rows.extend(tracker.results())
    write_jsonl(args.output_dir / "outlier_examples.jsonl", outlier_rows)

    write_rows(args.output_dir / "unicode_inventory_raw.csv", unicode_rows(raw_unicode, raw_unicode_examples))
    write_rows(args.output_dir / "unicode_inventory_extracted.csv", unicode_rows(ext_unicode, ext_unicode_examples))

    candidates = build_codex_candidates(
        joint_states, baseline_examples, outlier_trackers,
        ext_unicode, ext_unicode_examples, example_by_page, args,
    )
    write_jsonl(args.output_dir / "codex_review_candidates.jsonl", candidates)
    batch_count = write_batches(args.output_dir, candidates, args.batch_size)

    elapsed = time.time() - started
    manifest = {
        "script_version": SCRIPT_VERSION,
        "scientific_scope": "structural discovery before cleaning; no validity/corruption labels",
        "input": {
            "path": str(args.wikipedia),
            "bytes": args.wikipedia.stat().st_size,
            "sha256": dump_sha256,
        },
        "runtime": {
            "python": platform.python_version(),
            "platform": platform.platform(),
            "lxml": version_or_unknown("lxml"),
            "mwparserfromhell": version_or_unknown("mwparserfromhell"),
        },
        "parameters": vars(args) | {"wikipedia": str(args.wikipedia), "output_dir": str(args.output_dir)},
        "census": asdict(census),
        "signature_counts": {
            "raw_distinct": len(raw_states),
            "extracted_distinct": len(ext_states),
            "joint_distinct": len(joint_states),
        },
        "review_candidates": len(candidates),
        "codex_batches": batch_count,
        "elapsed_seconds": elapsed,
    }
    (args.output_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    report = build_report(
        census, namespace_counts, raw_states, ext_states, joint_states,
        candidates, batch_count, elapsed, dump_sha256, args,
    )
    (args.output_dir / "DISCOVERY_REPORT.md").write_text(report, encoding="utf-8")

    print("\n" + report)
    print(f"Outputs: {args.output_dir.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
