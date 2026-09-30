# Corpus profiling — first run

This tool profiles the three working Corpus v0.1 sources before a retrieval-unit length is frozen:

1. official Uzbek Wikipedia dump;
2. Uzbek News Dataset;
3. Uzbek Legal Corpus.

It compares candidate maximum unit sizes `150 / 180 / 200 / 220` words and, when the Hugging Face tokenizers are available, measures exact E5/BGE-M3 token lengths and truncation risk.

## 1. Install

```powershell
cd G:\PhD\phd-uzbek-hybrid-retrieval
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-corpus-profile.txt
```

## 2. Structural self-test

```powershell
python corpus_profile.py --demo --skip-tokenizers --output-dir profile_demo
```

This validates parsing/segmentation/report generation, but does **not** choose a retrieval-unit size.

## 3. Real screening run

Example only; replace paths with the real downloaded files/directories:

```powershell
python corpus_profile.py `
  --wikipedia "G:\PhD\data\uzwiki-pages-articles.xml.bz2" `
  --news "G:\PhD\data\uzbek-news" `
  --legal "G:\PhD\data\uzbek-legal-corpus" `
  --sample-per-source 10000 `
  --word-limits 150 180 200 220 `
  --output-dir "G:\PhD\profile_run_001"
```

By default, news category `Qonunchilik` is excluded from this profiling pass to reduce overlap with the dedicated legal source. Add `--include-news-qonunchilik` if you intentionally want it included.

If automatic column detection is wrong, specify fields, for example:

```powershell
--news-text-field body --news-title-field title --news-id-field link --news-category-field category
```

and similarly for `--legal-*`.

## 4. Outputs

- `source_profile.csv` — original document length/script/duplicate diagnostics;
- `segmentation_profile.csv` — 150/180/200/220 segmentation results and tokenizer overflow;
- `sample_documents.csv` — sampled metadata/statistics only, no source text;
- `recommendation.json` — mechanical screening recommendation, **not** a scientific freeze;
- `REPORT.md` — readable summary;
- `run_config.json` — run parameters for reproducibility.

## 5. Decision rule

Do **not** automatically accept the recommended number. We review at least:

- E5 overflow percentage separately for Wikipedia, News and Legal;
- E5 P95/P99 token lengths;
- percentage of documents preserved whole;
- units per source document;
- long-tail behavior in Legal;
- mixed Latin/Cyrillic coverage;
- exact-duplicate diagnostics.

Only then should the retrieval-unit length be frozen in the research protocol.

## 6. Important boundary

The script is pre-retrieval. It must not use nDCG, Recall, qrels, system winners or morphology effects to select the segmentation length. That protects the later causal raw/stem/lemma comparison from outcome-driven preprocessing choices.
