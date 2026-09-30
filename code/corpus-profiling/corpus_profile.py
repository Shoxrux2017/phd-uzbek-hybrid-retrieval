#!/usr/bin/env python3
"""Corpus feasibility and retrieval-unit profiling for the Uzbek hybrid IR PhD.

Purpose
-------
Profile Wikipedia / News / Legal source documents before freezing retrieval-unit
segmentation. The tool is intentionally pre-retrieval: it never uses qrels or
retrieval effectiveness.

Key outputs
-----------
- source_profile.csv
- segmentation_profile.csv
- sample_documents.csv (metadata/statistics only; no source text)
- structural_quality_profile.csv
- structural_anomaly_examples.csv
- recommendation.json
- REPORT.md

Typical first pass
------------------
python corpus_profile.py \
  --wikipedia /data/uzwiki-20260901-pages-articles.xml.bz2 \
  --news /data/uzbek_news.csv \
  --legal /data/uzbek_legal \
  --sample-per-source 10000 \
  --word-limits 150 180 200 220 \
  --output-dir profile_run_001

Install optional dependencies for exact tokenizer profiling and large parquet:
  pip install transformers sentencepiece pandas pyarrow mwparserfromhell

The script can also run a dependency-light self-test:
  python corpus_profile.py --demo --skip-tokenizers --output-dir demo_profile
"""

from __future__ import annotations

import argparse
import bz2
import csv
import hashlib
import json
import math
import random
import re
import sys
import unicodedata
import warnings
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, Iterator, List, Optional, Sequence, Tuple


# --------------------------- basic text helpers ---------------------------

WS_RE = re.compile(r"\s+")
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?…])\s+")
LATIN_RE = re.compile(r"[A-Za-zÀ-ž]")
CYRILLIC_RE = re.compile(r"[\u0400-\u04FF]")
APOSTROPHE_VARIANTS = {"'", "’", "‘", "ʻ", "ʼ", "`", "´", "ʹ", "ʽ"}


def normalize_text(text: str) -> str:
    text = unicodedata.normalize("NFC", text or "")
    return WS_RE.sub(" ", text).strip()


def preserve_layout_text(text: str) -> str:
    """Normalize Unicode/spacing while preserving paragraph boundaries."""
    text = unicodedata.normalize("NFC", text or "").replace("\r\n", "\n").replace("\r", "\n")
    lines = [re.sub(r"[ \t]+", " ", line).strip() for line in text.split("\n")]
    out: List[str] = []
    blank = False
    for line in lines:
        if line:
            out.append(line)
            blank = False
        elif out and not blank:
            out.append("")
            blank = True
    return "\n".join(out).strip()


def word_count(text: str) -> int:
    text = normalize_text(text)
    return 0 if not text else len(text.split(" "))


def script_stats(text: str) -> Dict[str, Any]:
    latin = len(LATIN_RE.findall(text))
    cyr = len(CYRILLIC_RE.findall(text))
    letters = latin + cyr
    apos = Counter(ch for ch in text if ch in APOSTROPHE_VARIANTS)
    return {
        "latin_letters": latin,
        "cyrillic_letters": cyr,
        "latin_share": (latin / letters) if letters else 0.0,
        "cyrillic_share": (cyr / letters) if letters else 0.0,
        "mixed_latin_cyrillic": bool(latin and cyr),
        "apostrophe_variants": "".join(sorted(apos.keys())),
    }


def exact_hash(text: str) -> str:
    canonical = normalize_text(text).casefold()
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def percentile(values: Sequence[float], p: float) -> Optional[float]:
    if not values:
        return None
    vals = sorted(values)
    if len(vals) == 1:
        return float(vals[0])
    rank = (len(vals) - 1) * p
    lo = int(math.floor(rank))
    hi = int(math.ceil(rank))
    if lo == hi:
        return float(vals[lo])
    return float(vals[lo] + (vals[hi] - vals[lo]) * (rank - lo))


def summarize(values: Sequence[float], prefix: str = "") -> Dict[str, Any]:
    if not values:
        return {
            f"{prefix}n": 0,
            f"{prefix}mean": None,
            f"{prefix}p50": None,
            f"{prefix}p75": None,
            f"{prefix}p90": None,
            f"{prefix}p95": None,
            f"{prefix}p99": None,
            f"{prefix}max": None,
        }
    return {
        f"{prefix}n": len(values),
        f"{prefix}mean": sum(values) / len(values),
        f"{prefix}p50": percentile(values, 0.50),
        f"{prefix}p75": percentile(values, 0.75),
        f"{prefix}p90": percentile(values, 0.90),
        f"{prefix}p95": percentile(values, 0.95),
        f"{prefix}p99": percentile(values, 0.99),
        f"{prefix}max": max(values),
    }


# ---------------------------- tokenizer layer ----------------------------

class TokenCounter:
    name: str
    max_length: int

    def count(self, text: str, *, is_document: bool = True) -> int:
        raise NotImplementedError

    def count_many(self, texts: Sequence[str], *, is_document: bool = True) -> List[int]:
        return [self.count(text, is_document=is_document) for text in texts]


class TransformersTokenCounter(TokenCounter):
    def __init__(self, model_id: str, name: str, max_length: int, e5_prefix: bool = False):
        try:
            from transformers import AutoTokenizer  # type: ignore
        except ImportError as exc:
            raise RuntimeError(
                "transformers is not installed. Run: pip install transformers sentencepiece"
            ) from exc
        self.tokenizer = AutoTokenizer.from_pretrained(model_id, use_fast=True)
        self.name = name
        self.max_length = max_length
        self.e5_prefix = e5_prefix

    def count(self, text: str, *, is_document: bool = True) -> int:
        if self.e5_prefix:
            text = ("passage: " if is_document else "query: ") + text
        encoded = self.tokenizer(
            text,
            add_special_tokens=True,
            truncation=False,
            return_attention_mask=False,
            return_token_type_ids=False,
            verbose=False,
        )
        return len(encoded["input_ids"])

    def count_many(self, texts: Sequence[str], *, is_document: bool = True) -> List[int]:
        batch = list(texts)
        if self.e5_prefix:
            prefix = "passage: " if is_document else "query: "
            batch = [prefix + text for text in batch]
        if not batch:
            return []
        encoded = self.tokenizer(
            batch,
            add_special_tokens=True,
            truncation=False,
            padding=False,
            return_attention_mask=False,
            return_token_type_ids=False,
            return_length=True,
            verbose=False,
        )
        lengths = encoded.get("length")
        if lengths is not None:
            return [int(x) for x in lengths]
        return [len(ids) for ids in encoded["input_ids"]]


class SentencePieceTokenCounter(TokenCounter):
    """Offline fallback using a local XLM-R SentencePiece model.

    Counts SentencePiece pieces + two boundary special tokens. This is suitable
    for length screening but the final freeze should use the exact production
    tokenizer implementation/checkpoint.
    """

    def __init__(self, model_path: Path, name: str, max_length: int, e5_prefix: bool = False):
        try:
            import sentencepiece as spm  # type: ignore
        except ImportError as exc:
            raise RuntimeError("sentencepiece is not installed") from exc
        self.sp = spm.SentencePieceProcessor(model_file=str(model_path))
        self.name = name
        self.max_length = max_length
        self.e5_prefix = e5_prefix

    def count(self, text: str, *, is_document: bool = True) -> int:
        if self.e5_prefix:
            text = ("passage: " if is_document else "query: ") + text
        return len(self.sp.encode(text, out_type=int)) + 2


def build_tokenizers(args: argparse.Namespace) -> List[TokenCounter]:
    if args.skip_tokenizers:
        return []

    counters: List[TokenCounter] = []
    if args.e5_sp_model:
        counters.append(
            SentencePieceTokenCounter(Path(args.e5_sp_model), "e5", args.e5_max_tokens, e5_prefix=True)
        )
    else:
        counters.append(
            TransformersTokenCounter(args.e5_model, "e5", args.e5_max_tokens, e5_prefix=True)
        )

    if args.bge_sp_model:
        counters.append(
            SentencePieceTokenCounter(Path(args.bge_sp_model), "bge_m3", args.bge_max_tokens)
        )
    else:
        counters.append(
            TransformersTokenCounter(args.bge_model, "bge_m3", args.bge_max_tokens)
        )
    return counters


# ------------------------------ source I/O -------------------------------

TEXT_FIELD_CANDIDATES = [
    "text", "body", "content", "article_text", "full_text", "document_text",
    "article", "description", "raw_text"
]
TITLE_FIELD_CANDIDATES = [
    "title", "document_title", "headline", "name", "doc_title"
]
ID_FIELD_CANDIDATES = [
    "id", "doc_id", "document_id", "article_id", "page_id", "url", "link", "source_url"
]
CATEGORY_FIELD_CANDIDATES = ["category", "label", "topic", "section"]


@dataclass
class Document:
    source: str
    doc_id: str
    title: str
    text: str
    category: str = ""
    provenance: str = ""


def first_present(record: Dict[str, Any], candidates: Sequence[str], explicit: Optional[str] = None) -> str:
    if explicit:
        value = record.get(explicit, "")
        return "" if value is None else str(value)
    for key in candidates:
        if key in record and record[key] not in (None, ""):
            return str(record[key])
    return ""


def iter_jsonl(path: Path) -> Iterator[Dict[str, Any]]:
    opener = bz2.open if path.suffix == ".bz2" else open
    mode = "rt"
    with opener(path, mode, encoding="utf-8", errors="replace") as fh:  # type: ignore[arg-type]
        for line in fh:
            line = line.strip()
            if not line:
                continue
            obj = json.loads(line)
            if isinstance(obj, dict):
                yield obj


def iter_csv(path: Path) -> Iterator[Dict[str, Any]]:
    opener = bz2.open if path.suffix == ".bz2" else open
    with opener(path, "rt", encoding="utf-8-sig", errors="replace", newline="") as fh:  # type: ignore[arg-type]
        sample = fh.read(8192)
        fh.seek(0)
        try:
            dialect = csv.Sniffer().sniff(sample, delimiters=",;\t|")
        except csv.Error:
            dialect = csv.excel
        reader = csv.DictReader(fh, dialect=dialect)
        for row in reader:
            yield dict(row)


def iter_parquet(path: Path) -> Iterator[Dict[str, Any]]:
    try:
        import pyarrow.dataset as ds  # type: ignore
    except ImportError as exc:
        raise RuntimeError("Parquet input requires pyarrow: pip install pyarrow") from exc
    dataset = ds.dataset(str(path), format="parquet")
    for batch in dataset.to_batches(batch_size=2048):
        for row in batch.to_pylist():
            yield row


def txt_record(path: Path, root: Optional[Path] = None) -> Optional[Dict[str, Any]]:
    """Parse the Uzbek News Dataset .txt convention.

    Expected shape:
      first non-empty line = title
      remaining text       = article body

    Category is taken from the immediate parent directory (e.g. Texnologiya).
    The ID is the relative POSIX path when a root directory is supplied.
    """
    raw = path.read_text(encoding="utf-8-sig", errors="replace")
    raw = raw.replace("\r\n", "\n").replace("\r", "\n")
    lines = raw.split("\n")

    first_idx = None
    for i, line in enumerate(lines):
        if line.strip():
            first_idx = i
            break
    if first_idx is None:
        return None

    title = lines[first_idx].strip()
    body = preserve_layout_text("\n".join(lines[first_idx + 1:]))
    if not body:
        # Keep one-line files usable rather than dropping them.
        body = title
        title = ""

    if root is not None:
        try:
            doc_id = path.relative_to(root).as_posix()
        except ValueError:
            doc_id = path.name
    else:
        doc_id = path.name

    return {
        "id": doc_id,
        "title": title,
        "text": body,
        "category": path.parent.name,
        "source_path": str(path),
    }


def iter_generic_records(path: Path) -> Iterator[Dict[str, Any]]:
    if path.is_dir():
        parquet_files = list(path.rglob("*.parquet"))
        if parquet_files:
            yield from iter_parquet(path)
            return

        # Uzbek News Dataset is distributed as nested category directories
        # containing one UTF-8 .txt file per article.
        txt_files = sorted(path.rglob("*.txt"))
        if txt_files:
            for child in txt_files:
                record = txt_record(child, root=path)
                if record is not None:
                    yield record
            return

        for child in sorted(path.rglob("*")):
            if child.is_file() and child.suffix.lower() in {".jsonl", ".ndjson", ".csv", ".tsv", ".json"}:
                yield from iter_generic_records(child)
        return

    suffixes = [s.lower() for s in path.suffixes]
    if ".parquet" in suffixes:
        yield from iter_parquet(path)
    elif ".jsonl" in suffixes or ".ndjson" in suffixes:
        yield from iter_jsonl(path)
    elif ".csv" in suffixes or ".tsv" in suffixes:
        yield from iter_csv(path)
    elif ".txt" in suffixes:
        record = txt_record(path)
        if record is not None:
            yield record
    elif ".json" in suffixes:
        with open(path, "r", encoding="utf-8") as fh:
            obj = json.load(fh)
        if isinstance(obj, list):
            for item in obj:
                if isinstance(item, dict):
                    yield item
        elif isinstance(obj, dict):
            records = obj.get("data") or obj.get("records") or obj.get("items")
            if isinstance(records, list):
                for item in records:
                    if isinstance(item, dict):
                        yield item
            else:
                yield obj
    else:
        raise ValueError(f"Unsupported input format: {path}")


def clean_wikitext(text: str) -> str:
    try:
        import mwparserfromhell  # type: ignore
    except ImportError as exc:
        raise RuntimeError(
            "Wikipedia XML profiling requires mwparserfromhell: pip install mwparserfromhell"
        ) from exc
    code = mwparserfromhell.parse(text or "")
    return preserve_layout_text(code.strip_code(normalize=True, collapse=True))


def iter_wikipedia_xml(path: Path) -> Iterator[Document]:
    try:
        from lxml import etree  # type: ignore
    except ImportError as exc:
        raise RuntimeError("Wikipedia XML profiling requires lxml: pip install lxml") from exc

    if path.suffix == ".bz2":
        fh = bz2.open(path, "rb")
    else:
        fh = open(path, "rb")

    with fh:
        context = etree.iterparse(fh, events=("end",), tag="{*}page", recover=True, huge_tree=True)
        for _, elem in context:
            def find_text(local: str) -> str:
                node = elem.find(f"{{*}}{local}")
                return "" if node is None or node.text is None else node.text

            ns = find_text("ns")
            if ns and ns != "0":
                elem.clear()
                continue
            if elem.find("{*}redirect") is not None:
                elem.clear()
                continue
            title = find_text("title")
            page_id = find_text("id") or title
            rev = elem.find("{*}revision")
            raw = ""
            if rev is not None:
                text_node = rev.find("{*}text")
                if text_node is not None and text_node.text:
                    raw = text_node.text
            if raw:
                cleaned = clean_wikitext(raw)
                if cleaned:
                    yield Document("wikipedia", page_id, title, cleaned, provenance=str(path))
            elem.clear()
            while elem.getprevious() is not None:
                del elem.getparent()[0]


def iter_table_documents(
    source: str,
    path: Path,
    *,
    text_field: Optional[str],
    title_field: Optional[str],
    id_field: Optional[str],
    category_field: Optional[str],
    exclude_categories: Sequence[str] = (),
) -> Iterator[Document]:
    excluded = {x.casefold().strip() for x in exclude_categories if x.strip()}
    for idx, row in enumerate(iter_generic_records(path), start=1):
        text = first_present(row, TEXT_FIELD_CANDIDATES, text_field)
        if not text.strip():
            continue
        title = first_present(row, TITLE_FIELD_CANDIDATES, title_field)
        doc_id = first_present(row, ID_FIELD_CANDIDATES, id_field) or f"{source}-{idx}"
        category = first_present(row, CATEGORY_FIELD_CANDIDATES, category_field)
        if category.casefold().strip() in excluded:
            continue
        yield Document(source, doc_id, title, preserve_layout_text(text), category, str(path))



def sample_news_txt_directory(
    root: Path,
    k: int,
    seed: int,
    *,
    include_qonunchilik: bool = False,
) -> Tuple[List[Document], int]:
    """Deterministically sample original Uzbek News Dataset paths before reading text."""
    files = [
        p for p in root.rglob("*.txt")
        if p.is_file() and (
            include_qonunchilik or p.parent.name.casefold().strip() != "qonunchilik"
        )
    ]
    files.sort(key=lambda p: p.as_posix())
    total = len(files)
    if total == 0:
        return [], 0
    rng = random.Random(seed)
    chosen = files if total <= k else [files[i] for i in sorted(rng.sample(range(total), k))]
    docs: List[Document] = []
    for p in chosen:
        row = txt_record(p, root=root)
        if row is None:
            continue
        docs.append(Document(
            source="news",
            doc_id=str(row.get("id", p.name)),
            title=str(row.get("title", "")),
            text=preserve_layout_text(str(row.get("text", ""))),
            category=str(row.get("category", p.parent.name)),
            provenance=str(p),
        ))
    return docs, total


def write_sample_cache(
    path: Path,
    sampled_by_source: Dict[str, Tuple[List[Document], int]],
) -> None:
    """Write a local-only JSONL cache of sampled source text for repeat profiling."""
    path.parent.mkdir(parents=True, exist_ok=True)
    meta: Dict[str, Dict[str, int]] = {}
    with path.open("w", encoding="utf-8") as fh:
        for source, (docs, total_seen) in sampled_by_source.items():
            meta[source] = {"total_seen": int(total_seen), "sampled": len(docs)}
            for d in docs:
                fh.write(json.dumps({
                    "source": d.source,
                    "doc_id": d.doc_id,
                    "title": d.title,
                    "text": d.text,
                    "category": d.category,
                    "provenance": d.provenance,
                }, ensure_ascii=False) + "\n")
    path.with_suffix(path.suffix + ".meta.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def read_sample_cache(path: Path) -> Dict[str, Tuple[List[Document], int]]:
    grouped: Dict[str, List[Document]] = defaultdict(list)
    with path.open("r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            source = str(row["source"])
            grouped[source].append(Document(
                source=source,
                doc_id=str(row.get("doc_id", "")),
                title=str(row.get("title", "")),
                text=str(row.get("text", "")),
                category=str(row.get("category", "")),
                provenance=str(row.get("provenance", "")),
            ))
    meta_path = path.with_suffix(path.suffix + ".meta.json")
    meta = json.loads(meta_path.read_text(encoding="utf-8")) if meta_path.exists() else {}
    return {
        source: (docs, int(meta.get(source, {}).get("total_seen", len(docs))))
        for source, docs in grouped.items()
    }


# -------------------------- sampling / segmentation -----------------------

def reservoir_sample(iterable: Iterable[Document], k: int, seed: int) -> Tuple[List[Document], int]:
    rng = random.Random(seed)
    sample: List[Document] = []
    total = 0
    for total, item in enumerate(iterable, start=1):
        if len(sample) < k:
            sample.append(item)
        else:
            j = rng.randint(1, total)
            if j <= k:
                sample[j - 1] = item
    return sample, total


def sentence_units(text: str) -> List[str]:
    # Paragraph first, sentence second. Empty lines are preserved upstream only
    # conceptually; normalize_text later removes repeated whitespace.
    raw_paragraphs = [p.strip() for p in re.split(r"\n\s*\n|\r\n\s*\r\n", text) if p.strip()]
    if not raw_paragraphs:
        raw_paragraphs = [text]
    units: List[str] = []
    for p in raw_paragraphs:
        sents = [s.strip() for s in SENTENCE_SPLIT_RE.split(p) if s.strip()]
        units.extend(sents or [p])
    return units


def hard_split_words(text: str, max_words: int) -> List[str]:
    words = normalize_text(text).split()
    return [" ".join(words[i:i + max_words]) for i in range(0, len(words), max_words)]


def segment_document(title: str, body: str, max_words: int) -> List[str]:
    title = normalize_text(title)
    body = preserve_layout_text(body)
    if not body:
        return []

    prefix_words = word_count(title)
    if prefix_words >= max_words:
        # Extremely long title: keep a bounded prefix for profiling; flagging is
        # visible in the resulting token/word counts.
        title = " ".join(title.split()[: max(1, max_words // 4)])
        prefix_words = word_count(title)

    capacity = max(1, max_words - prefix_words)
    units = sentence_units(body)
    chunks_body: List[str] = []
    current: List[str] = []
    current_words = 0

    for unit in units:
        uw = word_count(unit)
        if uw > capacity:
            if current:
                chunks_body.append(" ".join(current))
                current, current_words = [], 0
            chunks_body.extend(hard_split_words(unit, capacity))
            continue
        if current and current_words + uw > capacity:
            chunks_body.append(" ".join(current))
            current, current_words = [], 0
        current.append(unit)
        current_words += uw
    if current:
        chunks_body.append(" ".join(current))

    if not chunks_body:
        return []
    return [normalize_text(f"{title}\n{chunk}" if title else chunk) for chunk in chunks_body]


# ------------------------------ demo data --------------------------------
def demo_documents() -> Dict[str, List[Document]]:
    wiki_short = (
        "O‘zbekiston Markaziy Osiyoda joylashgan davlat. Poytaxti Toshkent shahri. "
        "Mamlakat tarix, madaniyat, ta’lim va ilm-fan sohalarida boy merosga ega."
    )
    wiki_long = " ".join([wiki_short] * 40)
    news = (
        "Bugun Samarqand shahrida ta’lim va raqamli texnologiyalar bo‘yicha yangi loyiha taqdim etildi. "
        "Loyiha doirasida talabalar uchun amaliy mashg‘ulotlar va ochiq ma’ruzalar tashkil etiladi."
    )
    legal = (
        "Ushbu modda axborot tizimlaridan foydalanish tartibini belgilaydi. "
        "Foydalanuvchilar qonunchilik talablariga rioya etishi, shaxsga doir ma’lumotlarni himoya qilishi va "
        "belgilangan tartibda murojaat yuborishi lozim."
    )
    return {
        "wikipedia": [
            Document("wikipedia", "w1", "O‘zbekiston", wiki_short),
            Document("wikipedia", "w2", "Uzun ensiklopedik maqola", wiki_long),
        ],
        "news": [
            Document("news", "n1", "Raqamli ta’lim loyihasi", " ".join([news] * 12), "Ta'lim"),
            Document("news", "n2", "Texnologiya yangiliklari", news, "Texnologiya"),
        ],
        "legal": [
            Document("legal", "l1", "Axborot tizimlari to‘g‘risida", " ".join([legal] * 35), "legal"),
            Document("legal", "l2", "Qisqa norma", legal, "legal"),
        ],
    }


# ------------------------------- profiling -------------------------------
def profile_source(
    source: str,
    docs: Sequence[Document],
    total_seen: int,
    word_limits: Sequence[int],
    tokenizers: Sequence[TokenCounter],
) -> Tuple[Dict[str, Any], List[Dict[str, Any]], List[Dict[str, Any]]]:
    orig_words: List[int] = []
    orig_chars: List[int] = []
    latin_shares: List[float] = []
    cyr_shares: List[float] = []
    mixed_count = 0
    exact_counts: Counter[str] = Counter()
    sample_rows: List[Dict[str, Any]] = []

    for d in docs:
        full = normalize_text(f"{d.title}\n{d.text}" if d.title else d.text)
        wc = word_count(full)
        sc = script_stats(full)
        orig_words.append(wc)
        orig_chars.append(len(full))
        latin_shares.append(sc["latin_share"])
        cyr_shares.append(sc["cyrillic_share"])
        mixed_count += int(sc["mixed_latin_cyrillic"])
        exact_counts[exact_hash(full)] += 1
        sample_rows.append({
            "source": source,
            "doc_id": d.doc_id,
            "category": d.category,
            "title_words": word_count(d.title),
            "body_words": word_count(d.text),
            "total_words": wc,
            "chars": len(full),
            "latin_share": round(sc["latin_share"], 6),
            "cyrillic_share": round(sc["cyrillic_share"], 6),
            "mixed_latin_cyrillic": sc["mixed_latin_cyrillic"],
            "apostrophe_variants": sc["apostrophe_variants"],
            "exact_hash": exact_hash(full),
        })

    duplicate_docs = sum(v - 1 for v in exact_counts.values() if v > 1)
    src_row: Dict[str, Any] = {
        "source": source,
        "source_records_seen": total_seen,
        "sampled_documents": len(docs),
        "sample_exact_duplicate_docs": duplicate_docs,
        "sample_exact_duplicate_pct": 100 * duplicate_docs / max(1, len(docs)),
        "mixed_script_documents": mixed_count,
        "mixed_script_pct": 100 * mixed_count / max(1, len(docs)),
        "mean_latin_share": sum(latin_shares) / max(1, len(latin_shares)),
        "mean_cyrillic_share": sum(cyr_shares) / max(1, len(cyr_shares)),
    }
    src_row.update(summarize(orig_words, "words_"))
    src_row.update(summarize(orig_chars, "chars_"))

    seg_rows: List[Dict[str, Any]] = []
    for limit in word_limits:
        chunks: List[str] = []
        chunks_per_doc: List[int] = []
        whole_docs = 0
        for d in docs:
            segs = segment_document(d.title, d.text, limit)
            chunks.extend(segs)
            chunks_per_doc.append(len(segs))
            if len(segs) == 1:
                whole_docs += 1

        row: Dict[str, Any] = {
            "source": source,
            "word_limit": limit,
            "sampled_documents": len(docs),
            "retrieval_units": len(chunks),
            "mean_units_per_doc": sum(chunks_per_doc) / max(1, len(chunks_per_doc)),
            "p95_units_per_doc": percentile(chunks_per_doc, 0.95),
            "max_units_per_doc": max(chunks_per_doc) if chunks_per_doc else 0,
            "whole_document_preserved_pct": 100 * whole_docs / max(1, len(docs)),
        }
        chunk_words = [word_count(c) for c in chunks]
        row.update(summarize(chunk_words, "unit_words_"))

        for tok in tokenizers:
            counts = tok.count_many(chunks, is_document=True)
            row.update(summarize(counts, f"{tok.name}_tokens_"))
            overflow = sum(1 for n in counts if n > tok.max_length)
            row[f"{tok.name}_max_tokens"] = tok.max_length
            row[f"{tok.name}_overflow_units"] = overflow
            row[f"{tok.name}_overflow_pct"] = 100 * overflow / max(1, len(counts))
            row[f"{tok.name}_p99_headroom"] = (
                tok.max_length - (percentile(counts, 0.99) or 0)
            )
        seg_rows.append(row)

    return src_row, seg_rows, sample_rows


def recommend_limit(
    seg_rows: Sequence[Dict[str, Any]],
    word_limits: Sequence[int],
    max_e5_overflow_pct: float,
    e5_p99_target: int,
) -> Dict[str, Any]:
    if not seg_rows or "e5_overflow_pct" not in seg_rows[0]:
        return {
            "status": "tokenizers_not_run",
            "recommended_word_limit": None,
            "reason": "Run with the exact E5 tokenizer (or local SentencePiece model) before freezing a limit.",
        }

    per_limit: Dict[int, List[Dict[str, Any]]] = defaultdict(list)
    for row in seg_rows:
        per_limit[int(row["word_limit"])].append(row)

    checks = []
    eligible = []
    for limit in sorted(word_limits):
        rows = per_limit[limit]
        worst_overflow = max(float(r.get("e5_overflow_pct", 100.0)) for r in rows)
        worst_p99 = max(float(r.get("e5_tokens_p99") or 10**9) for r in rows)
        ok = worst_overflow <= max_e5_overflow_pct and worst_p99 <= e5_p99_target
        checks.append({
            "word_limit": limit,
            "worst_source_e5_overflow_pct": worst_overflow,
            "worst_source_e5_p99_tokens": worst_p99,
            "passes_screen": ok,
        })
        if ok:
            eligible.append(limit)

    return {
        "status": "screening_only_not_a_scientific_freeze",
        "recommended_word_limit": max(eligible) if eligible else None,
        "screening_rule": {
            "max_e5_overflow_pct_per_source": max_e5_overflow_pct,
            "max_e5_p99_tokens_per_source": e5_p99_target,
        },
        "checks": checks,
        "warning": (
            "This is a mechanical screening recommendation. Final retrieval-unit length must be reviewed "
            "with actual source distributions and frozen before comparative retrieval analysis."
        ),
    }



# ------------------------ structural-quality audit ------------------------

STRUCTURAL_RULES_VERSION = "surface-v0.1"


def structural_quality_flags(text: str) -> Dict[str, Any]:
    """Model-independent surface/format audit for one candidate retrieval unit.

    These rules do NOT use qrels, retrieval scores, E5/BGE token counts, or
    downstream effectiveness. They only flag obvious extraction/table/markup
    patterns for audit; they do not delete or rewrite data.
    """
    s = text or ""
    words = s.split()
    n_chars = len(s)
    longest = max(words, key=len) if words else ""

    digit_chars = sum(ch.isdigit() for ch in s)
    alpha_chars = sum(ch.isalpha() for ch in s)
    punct_chars = sum((not ch.isalnum()) and (not ch.isspace()) for ch in s)

    digit_ratio = digit_chars / max(1, n_chars)
    alpha_ratio = alpha_chars / max(1, n_chars)
    punct_ratio = punct_chars / max(1, n_chars)

    long40 = sum(len(w) >= 40 for w in words)
    long80 = sum(len(w) >= 80 for w in words)

    transitions = len(
        re.findall(r"(?i)(?:[A-Za-zÀ-žʻʼ‘’'`][0-9]|[0-9][A-Za-zÀ-žʻʼ‘’'`])", s)
    )
    long_digit_runs = len(re.findall(r"\d{8,}", s))

    wiki_markup = bool(
        re.search(
            r"(?i)(?:\blink=|\bFayl:|upload\.wikimedia|wikimedia\.org|"
            r"\bframeless\b|\bthumb\b|\balt=|[0-9]{2,4}x[0-9]{2,4}px)",
            s,
        )
    )
    url_markup = bool(re.search(r"(?i)(?:https?://|www\.|%[0-9A-F]{2})", s))

    collapsed_table = (
        transitions >= 10
        or long_digit_runs >= 2
        or (digit_ratio >= 0.25 and transitions >= 4)
        or long80 >= 1
        or long40 >= 3
    )
    markup_artifact = wiki_markup or url_markup
    digit_heavy = digit_ratio >= 0.25
    symbol_heavy = punct_ratio >= 0.25 and alpha_ratio < 0.60

    reasons: List[str] = []
    if markup_artifact:
        reasons.append("MARKUP_ARTIFACT")
    if collapsed_table:
        reasons.append("COLLAPSED_TABLE_OR_GLUE")
    if digit_heavy:
        reasons.append("DIGIT_HEAVY")
    if symbol_heavy:
        reasons.append("SYMBOL_HEAVY")
    if len(longest) >= 80:
        reasons.append("VERY_LONG_SURFACE_TOKEN")

    core_flag = bool(markup_artifact or collapsed_table)

    if markup_artifact and collapsed_table:
        label = "MARKUP_AND_STRUCTURED"
    elif markup_artifact:
        label = "MARKUP_ARTIFACT"
    elif collapsed_table:
        label = "STRUCTURED_OR_COLLAPSED"
    elif digit_heavy or symbol_heavy:
        label = "REVIEW_SURFACE"
    else:
        label = "PROSE_LIKE"

    return {
        "rules_version": STRUCTURAL_RULES_VERSION,
        "label": label,
        "core_flag": core_flag,
        "reasons": reasons,
        "words": len(words),
        "chars": n_chars,
        "max_word_len": len(longest),
        "long_token_count_40": long40,
        "long_token_count_80": long80,
        "digit_ratio": digit_ratio,
        "alpha_ratio": alpha_ratio,
        "punct_ratio": punct_ratio,
        "alpha_digit_transitions": transitions,
        "long_digit_runs": long_digit_runs,
        "wiki_markup": wiki_markup,
        "url_markup": url_markup,
    }


def build_structural_audit(
    sampled_by_source: Dict[str, Tuple[List[Document], int]],
    word_limits: Sequence[int],
    tokenizers: Sequence[TokenCounter],
    e5_max_tokens: int,
    example_limit_words: int,
    example_cap_per_source: int,
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """Build aggregate audit rows and example rows without modifying data."""
    rows: List[Dict[str, Any]] = []
    examples: List[Dict[str, Any]] = []

    e5_counter: Optional[TokenCounter] = None
    for tok in tokenizers:
        if "e5" in getattr(tok, "name", "").lower():
            e5_counter = tok
            break

    for source in ("wikipedia", "news", "legal"):
        if source not in sampled_by_source:
            continue
        docs, _ = sampled_by_source[source]

        for limit in word_limits:
            chunks: List[str] = []
            audits: List[Dict[str, Any]] = []

            for doc in docs:
                for chunk in segment_document(doc.title, doc.text, int(limit)):
                    chunks.append(chunk)
                    audits.append(structural_quality_flags(chunk))

            e5_counts: Optional[List[int]] = None
            if e5_counter is not None and chunks:
                e5_counts = e5_counter.count_many(chunks, is_document=True)

            core_idx = [i for i, a in enumerate(audits) if a["core_flag"]]
            clean_idx = [i for i, a in enumerate(audits) if not a["core_flag"]]

            markup_units = sum("MARKUP_ARTIFACT" in a["reasons"] for a in audits)
            table_units = sum("COLLAPSED_TABLE_OR_GLUE" in a["reasons"] for a in audits)
            digit_heavy_units = sum("DIGIT_HEAVY" in a["reasons"] for a in audits)
            very_long_units = sum("VERY_LONG_SURFACE_TOKEN" in a["reasons"] for a in audits)

            all_over = clean_over = flagged_over = None
            if e5_counts is not None:
                all_over_n = sum(int(n) > e5_max_tokens for n in e5_counts)
                clean_over_n = sum(int(e5_counts[i]) > e5_max_tokens for i in clean_idx)
                flagged_over_n = sum(int(e5_counts[i]) > e5_max_tokens for i in core_idx)
                all_over = 100.0 * all_over_n / max(1, len(e5_counts))
                clean_over = 100.0 * clean_over_n / max(1, len(clean_idx))
                flagged_over = 100.0 * flagged_over_n / max(1, len(core_idx))

            rows.append({
                "source": source,
                "word_limit": int(limit),
                "retrieval_units": len(chunks),
                "core_flagged_units": len(core_idx),
                "core_flagged_pct": 100.0 * len(core_idx) / max(1, len(chunks)),
                "markup_units": markup_units,
                "collapsed_table_units": table_units,
                "digit_heavy_units": digit_heavy_units,
                "very_long_surface_token_units": very_long_units,
                "e5_overflow_pct_all": all_over,
                "e5_overflow_pct_unflagged": clean_over,
                "e5_overflow_pct_flagged": flagged_over,
            })

        count_examples = 0
        for doc in docs:
            for idx, chunk in enumerate(
                segment_document(doc.title, doc.text, int(example_limit_words)),
                start=1,
            ):
                a = structural_quality_flags(chunk)
                if not a["core_flag"]:
                    continue
                examples.append({
                    "source": source,
                    "doc_id": doc.doc_id,
                    "category": doc.category,
                    "word_limit": int(example_limit_words),
                    "chunk_index": idx,
                    "label": a["label"],
                    "reasons": "|".join(a["reasons"]),
                    "words": a["words"],
                    "max_word_len": a["max_word_len"],
                    "digit_ratio": round(a["digit_ratio"], 4),
                    "alpha_digit_transitions": a["alpha_digit_transitions"],
                    "long_digit_runs": a["long_digit_runs"],
                    "title": doc.title,
                    "snippet": chunk[:500].replace("\n", " "),
                })
                count_examples += 1
                if count_examples >= int(example_cap_per_source):
                    break
            if count_examples >= int(example_cap_per_source):
                break

    return rows, examples



def write_csv(path: Path, rows: Sequence[Dict[str, Any]]) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fields: List[str] = []
    seen = set()
    for row in rows:
        for key in row.keys():
            if key not in seen:
                seen.add(key)
                fields.append(key)
    with path.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def fmt(v: Any, digits: int = 2) -> str:
    if v is None:
        return "NA"
    if isinstance(v, float):
        return f"{v:.{digits}f}"
    return str(v)


def build_report(
    source_rows: Sequence[Dict[str, Any]],
    seg_rows: Sequence[Dict[str, Any]],
    structural_rows: Sequence[Dict[str, Any]],
    recommendation: Dict[str, Any],
    args: argparse.Namespace,
) -> str:
    lines = [
        "# Corpus Profiling Report",
        "",
        "**Status:** screening / pre-freeze evidence only",
        "",
        "This report profiles source-document lengths and candidate canonical retrieval-unit limits. "
        "It does not use qrels or retrieval effectiveness and must not be treated as an experiment result.",
        "",
        "## Run configuration",
        "",
        f"- Sample per source: `{args.sample_per_source}`",
        f"- Seed: `{args.seed}`",
        f"- Candidate word limits: `{', '.join(map(str, args.word_limits))}`",
        f"- E5 model: `{args.e5_model}` (max `{args.e5_max_tokens}` tokens)",
        f"- BGE-M3 model: `{args.bge_model}` (max `{args.bge_max_tokens}` tokens)",
        f"- Tokenizer profiling skipped: `{args.skip_tokenizers}`",
        "",
        "## Source-document profile",
        "",
        "| Source | Seen | Sample | Words P50 | P90 | P95 | P99 | Max | Exact dup % | Mixed script % |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for r in source_rows:
        lines.append(
            f"| {r['source']} | {r['source_records_seen']} | {r['sampled_documents']} | "
            f"{fmt(r.get('words_p50'))} | {fmt(r.get('words_p90'))} | {fmt(r.get('words_p95'))} | "
            f"{fmt(r.get('words_p99'))} | {fmt(r.get('words_max'))} | "
            f"{fmt(r.get('sample_exact_duplicate_pct'))} | {fmt(r.get('mixed_script_pct'))} |"
        )

    lines += [
        "",
        "## Candidate segmentation profile",
        "",
        "| Source | Limit words | Units | Mean units/doc | Whole doc % | Unit words P99 | E5 P99 | E5 overflow % | BGE-M3 P99 | BGE overflow % |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for r in seg_rows:
        lines.append(
            f"| {r['source']} | {r['word_limit']} | {r['retrieval_units']} | "
            f"{fmt(r.get('mean_units_per_doc'))} | {fmt(r.get('whole_document_preserved_pct'))} | "
            f"{fmt(r.get('unit_words_p99'))} | {fmt(r.get('e5_tokens_p99'))} | "
            f"{fmt(r.get('e5_overflow_pct'))} | {fmt(r.get('bge_m3_tokens_p99'))} | "
            f"{fmt(r.get('bge_m3_overflow_pct'))} |"
        )


    lines += [
        "",
        "## Structural-quality audit",
        "",
        "These flags use deterministic surface/format rules only. They do not use qrels, "
        "retrieval effectiveness, E5/BGE token thresholds, or downstream results, and they do not remove data.",
        "",
        "| Source | Limit words | Units | Core flagged % | Markup | Collapsed/table | "
        "E5 overflow all % | E5 overflow unflagged % |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for r in structural_rows:
        lines.append(
            f"| {r['source']} | {r['word_limit']} | {r['retrieval_units']} | "
            f"{fmt(r.get('core_flagged_pct'))} | {r['markup_units']} | "
            f"{r['collapsed_table_units']} | {fmt(r.get('e5_overflow_pct_all'))} | "
            f"{fmt(r.get('e5_overflow_pct_unflagged'))} |"
        )

    lines += [
        "",
        f"Flagged examples are exported at `{args.structural_audit_limit}` words. "
        "A structural flag is a review signal, not an automatic exclusion rule.",
        "",
    ]

    lines += ["", "## Mechanical screening recommendation", ""]
    if recommendation.get("recommended_word_limit") is None:
        lines.append(f"**No retrieval-unit limit is frozen.** {recommendation.get('reason', '')}")
    else:
        lines.append(
            f"Largest candidate passing the configured screening rule: **{recommendation['recommended_word_limit']} words**."
        )
        lines.append("")
        lines.append(
            "This is not a scientific decision by itself. Review source-specific distributions, token overflow, "
            "title overhead, segmentation behavior and the exact production tokenizer before freezing the protocol."
        )

    lines += [
        "",
        "## Required interpretation checks before freeze",
        "",
        "1. Prefer a limit with effectively zero E5 truncation risk on every source, not only on the pooled average.",
        "2. Inspect P95/P99 and worst cases separately for Wikipedia, News and Legal.",
        "3. Keep the same canonical retrieval-unit text/IDs for BM25_raw, BM25_stem, BM25_lemma and dense retrieval.",
        "4. Do not introduce overlap in the primary segmentation without a separate methodological justification.",
        "5. Exact duplicates in this report are sample diagnostics; full cross-source/near-duplicate resolution is a separate corpus-freeze task.",
        "6. Re-run the final candidate segmentation over the full corpus before Corpus v0.1 is frozen.",
        "",
    ]
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    p.add_argument("--wikipedia", type=Path, help="Official Wikimedia pages-articles XML/XML.bz2")
    p.add_argument("--news", type=Path, help="News input: nested UTF-8 .txt directory or CSV/TSV/JSONL/JSON/Parquet")
    p.add_argument("--legal", type=Path, help="Legal input: CSV/TSV/JSONL/JSON/Parquet/directory")
    p.add_argument("--demo", action="store_true", help="Run on built-in synthetic Uzbek documents")

    for src in ("news", "legal"):
        p.add_argument(f"--{src}-text-field")
        p.add_argument(f"--{src}-title-field")
        p.add_argument(f"--{src}-id-field")
        p.add_argument(f"--{src}-category-field")

    p.add_argument(
        "--include-news-qonunchilik",
        action="store_true",
        help="Include news category Qonunchilik; default excludes it to reduce legal cross-source duplication risk",
    )
    p.add_argument("--sample-per-source", type=int, default=10000)
    p.add_argument("--seed", type=int, default=20260916)
    p.add_argument("--sample-cache-out", type=Path,
                   help="Write sampled source texts to a local JSONL cache for faster repeat profiling")
    p.add_argument("--sample-cache-in", type=Path,
                   help="Reuse a local JSONL sample cache and skip source scanning")
    p.add_argument("--word-limits", type=int, nargs="+", default=[150, 180, 200, 220])
    p.add_argument("--output-dir", type=Path, default=Path("corpus_profile_output"))
    p.add_argument(
        "--structural-audit-limit",
        type=int,
        default=120,
        help="Word limit used when exporting flagged structural examples",
    )
    p.add_argument(
        "--structural-example-cap",
        type=int,
        default=100,
        help="Maximum flagged examples exported per source",
    )

    p.add_argument("--skip-tokenizers", action="store_true")
    p.add_argument("--e5-model", default="intfloat/multilingual-e5-large")
    p.add_argument("--bge-model", default="BAAI/bge-m3")
    p.add_argument("--e5-max-tokens", type=int, default=512)
    p.add_argument("--bge-max-tokens", type=int, default=8192)
    p.add_argument("--e5-sp-model", type=Path, help="Optional local SentencePiece model for offline E5 length screening")
    p.add_argument("--bge-sp-model", type=Path, help="Optional local SentencePiece model for offline BGE-M3 length screening")
    p.add_argument("--max-e5-overflow-pct", type=float, default=0.1)
    p.add_argument("--e5-p99-target", type=int, default=480)
    return p.parse_args()


def main() -> int:
    args = parse_args()
    if not args.demo and not args.sample_cache_in and not any([args.wikipedia, args.news, args.legal]):
        print("ERROR: provide --wikipedia/--news/--legal or use --demo", file=sys.stderr)
        return 2
    if any(x <= 0 for x in args.word_limits):
        print("ERROR: word limits must be positive", file=sys.stderr)
        return 2

    args.output_dir.mkdir(parents=True, exist_ok=True)

    try:
        tokenizers = build_tokenizers(args)
    except Exception as exc:
        print(f"ERROR loading tokenizers: {exc}", file=sys.stderr)
        print("Tip: install dependencies or use --skip-tokenizers for a structural self-test.", file=sys.stderr)
        return 3

    sampled_by_source: Dict[str, Tuple[List[Document], int]] = {}
    if args.sample_cache_in:
        sampled_by_source = read_sample_cache(args.sample_cache_in)
    elif args.demo:
        for source, docs in demo_documents().items():
            sampled_by_source[source] = (docs, len(docs))
    else:
        if args.wikipedia:
            sample, total = reservoir_sample(iter_wikipedia_xml(args.wikipedia), args.sample_per_source, args.seed)
            sampled_by_source["wikipedia"] = (sample, total)

        if args.news:
            if args.news.is_dir() and next(args.news.rglob("*.txt"), None) is not None:
                sample, total = sample_news_txt_directory(
                    args.news,
                    args.sample_per_source,
                    args.seed + 1,
                    include_qonunchilik=args.include_news_qonunchilik,
                )
            else:
                excluded = [] if args.include_news_qonunchilik else ["Qonunchilik"]
                docs = iter_table_documents(
                    "news", args.news,
                    text_field=args.news_text_field,
                    title_field=args.news_title_field,
                    id_field=args.news_id_field,
                    category_field=args.news_category_field,
                    exclude_categories=excluded,
                )
                sample, total = reservoir_sample(docs, args.sample_per_source, args.seed + 1)
            sampled_by_source["news"] = (sample, total)

        if args.legal:
            docs = iter_table_documents(
                "legal", args.legal,
                text_field=args.legal_text_field,
                title_field=args.legal_title_field,
                id_field=args.legal_id_field,
                category_field=args.legal_category_field,
            )
            sample, total = reservoir_sample(docs, args.sample_per_source, args.seed + 2)
            sampled_by_source["legal"] = (sample, total)

        if args.sample_cache_out:
            write_sample_cache(args.sample_cache_out, sampled_by_source)

    source_rows: List[Dict[str, Any]] = []
    seg_rows: List[Dict[str, Any]] = []
    sample_rows: List[Dict[str, Any]] = []
    for source in ("wikipedia", "news", "legal"):
        if source not in sampled_by_source:
            continue
        docs, total = sampled_by_source[source]
        src, seg, samp = profile_source(source, docs, total, args.word_limits, tokenizers)
        source_rows.append(src)
        seg_rows.extend(seg)
        sample_rows.extend(samp)

    recommendation = recommend_limit(
        seg_rows,
        args.word_limits,
        args.max_e5_overflow_pct,
        args.e5_p99_target,
    )

    structural_rows, structural_examples = build_structural_audit(
        sampled_by_source=sampled_by_source,
        word_limits=args.word_limits,
        tokenizers=tokenizers,
        e5_max_tokens=args.e5_max_tokens,
        example_limit_words=args.structural_audit_limit,
        example_cap_per_source=args.structural_example_cap,
    )

    write_csv(args.output_dir / "source_profile.csv", source_rows)
    write_csv(args.output_dir / "segmentation_profile.csv", seg_rows)
    write_csv(args.output_dir / "sample_documents.csv", sample_rows)
    write_csv(args.output_dir / "structural_quality_profile.csv", structural_rows)
    write_csv(args.output_dir / "structural_anomaly_examples.csv", structural_examples)

    (args.output_dir / "recommendation.json").write_text(
        json.dumps(recommendation, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (args.output_dir / "run_config.json").write_text(
        json.dumps({
            "sample_per_source": args.sample_per_source,
            "seed": args.seed,
            "word_limits": args.word_limits,
            "skip_tokenizers": args.skip_tokenizers,
            "e5_model": args.e5_model,
            "bge_model": args.bge_model,
            "e5_max_tokens": args.e5_max_tokens,
            "bge_max_tokens": args.bge_max_tokens,
            "news_qonunchilik_included": args.include_news_qonunchilik,
            "structural_rules_version": STRUCTURAL_RULES_VERSION,
            "structural_audit_limit": args.structural_audit_limit,
            "structural_example_cap": args.structural_example_cap,

        }, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    report = build_report(source_rows, seg_rows, structural_rows, recommendation, args)
    (args.output_dir / "REPORT.md").write_text(report, encoding="utf-8")

    print(report)
    print(f"\nOutputs: {args.output_dir.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
