# Research Decisions

Format: `ID — date — status — decision — rationale`.

## D-001 — 2026-08-31 — ACTIVE
**GitHub `main` is the PhD source of truth.**

Rationale: new chats must recover research state without relying on conversation memory.

## D-002 — 2026-08-31 — ACTIVE
**Research gap is provisional and may change.**

Rationale: deeper literature review and experiments may invalidate current assumptions.

## D-003 — 2026-08-31 — ACTIVE
**Explain technical terms simply before relying on formal terminology.**

Rationale: user wants to understand papers deeply, not only receive academic summaries.

## D-004 — 2026-08-31 — ACTIVE
**BM25 remains the primary lexical baseline candidate.**

Rationale: robust and widely accepted baseline; supported by BM25 literature and BEIR.

This does not mean BM25 is assumed to be optimal for Uzbek.

## D-005 — 2026-08-31 — ACTIVE
**Do not claim Uzbek hybrid retrieval is absent.**

Rationale: USHRA and O-RAG already exist.

## D-006 — 2026-08-31 — ACTIVE
**Do not claim Uzbek semantic retrieval evaluation is absent.**

Rationale: 2026 work includes corpus-level Uzbek semantic retrieval with standard IR metrics and SIGTURK Uzbek semantic-retrieval benchmark.

## D-007 — 2026-08-31 — ACTIVE
**Do not treat fixed BM25+dense fusion, RRF, or dynamic alpha(q) as novelty by themselves.**

Rationale: established international literature already covers these mechanisms.

## D-008 — 2026-08-31 — ACTIVE
**Morphological normalization is currently treated as a lexical-representation variant, not automatically as a third independent retrieval paradigm.**

Rationale: independence must be demonstrated empirically.

Possible future revision: if raw lexical and morph-normalized lexical provide reliably independent gains, a three-component architecture can be justified.

## D-009 — 2026-08-31 — ACTIVE
**Separate language/semantic infrastructure from retrieval effectiveness.**

Examples:

- UzBERT/BERTbek → language models, not automatically retrievers.
- UZWORDNET → semantic resource, not ranker.
- SimRelUz/STS → similarity evaluation, not corpus-level IR.

## D-010 — 2026-08-31 — ACTIVE
**Separate RAG from IR.**

Rationale: final answer quality depends on retrieval + generator + context/prompt; answer accuracy cannot be interpreted as pure retrieval quality.

## D-011 — 2026-08-31 — ACTIVE
**Chapter I working structure is fixed for now.**

1.1 lexical
1.2 semantic
1.3 hybrid
chapter conclusions.

May change only if deeper evidence justifies restructuring.

## D-012 — 2026-08-31 — ACTIVE
**Do not reduce Chapter I page count yet.**

Rationale: current Word v0.9 is ~35 pages excluding bibliography, larger than previous target. User decided to postpone volume compression until deeper re-analysis of key research works.

## D-013 — 2026-08-31 — ACTIVE
**Current gap is about missing knowledge, not a predetermined algorithm.**

Rationale: adaptive fusion is a potential hypothesis/solution only if query-dependent complementarity is experimentally established.

## D-014 — 2026-08-31 — ACTIVE
**Use reliability levels A/B/C/D.**

Rationale: prevent model cards, preprints, aggregator pages and unverified manuscripts from being treated as equivalent to primary peer-reviewed sources/official PhDs.

## D-015 — 2026-08-31 — ACTIVE
**The unverified Scribd “Context-Aware Hybrid BM25–BERT Retrieval for Uzbek Legal Texts” is not citable evidence.**

Rationale: no reliable publisher record/full verified publication has been confirmed. Keep only as a search lead.

## D-016 — 2026-09-01 — ACTIVE
**Для текста диссертации принят Russian-first terminology policy, определённый в `decisions/TERMINOLOGY_GUIDE.md`.**

Rationale:

- основной научный текст должен оставаться русскоязычным;
- английский оригинал специализированного термина вводится при необходимости для точности и идентификации;
- далее преимущественно используется согласованная русская форма или общепринятая аббревиатура;
- официальные названия моделей, алгоритмов, методов и ресурсов не переводятся, если перевод может исказить или затруднить их идентификацию;
- решение основано на анализе практики реальных русскоязычных диссертаций по информационному поиску, NLP и векторной семантике.

Термины, отмеченные в `decisions/TERMINOLOGY_GUIDE.md` как pending или требующие отдельного согласования, нельзя самостоятельно стандартизировать.

## D-017 — 2026-09-10 — ACTIVE
**Current working gap is the morphology-induced change in lexical–semantic complementarity, not the existence of morphology-aware, dense, hybrid, or query-dependent retrieval components.**

Rationale: targeted analysis of Uzbek evidence plus UPERF, Aboasal et al., Shona SIGIR evidence and GreekBarRetrieval shows that the individual components and many of their pairwise combinations are already represented in the literature. The unresolved question is how changing the Uzbek lexical morphological representation changes the unique relevant evidence contributed by lexical versus semantic retrieval and the resulting incremental hybrid gain.

See `research/CURRENT_GAP.md` and `research/GAP_BOUNDARY_2026-09-10.md`.

## D-018 — 2026-09-10 — ACTIVE
**For the main morphology–complementarity experiment, keep the dense comparator and fusion protocol fixed across lexical morphology variants.**

Rationale: to attribute an observed change to lexical morphological representation, the core comparison should vary `BM25_raw`, `BM25_stem`, and `BM25_lemma` while holding the same modern dense retriever `D` and the same validated fusion procedure constant. Otherwise morphology effects are confounded with changes in the semantic model or fusion mechanism.

## D-019 — 2026-09-10 — ACTIVE
**Aggregate retrieval metrics alone are insufficient for the main explanatory claim about complementarity.**

Rationale: MAP/nDCG/Recall can show whether effectiveness changed, but they do not reveal how morphology changes the division of useful evidence between retrievers. Where qrels permit, the analysis should include per-query unique relevant hits, relevant-set overlap/intersection, oracle union, incremental hybrid gain and query-level statistical testing.

## D-020 — 2026-09-10 — ACTIVE
**Sharifbaev 2026 dissertation manuscript remains D-level evidence until an official final/defense record is verified.**

Rationale: the analyzed manuscript is highly relevant and describes lemmatized BM25, LaBSE, graph retrieval and adaptive control on Uzbek/Russian legal data, but contains unresolved placeholders and internal numerical/data-count inconsistencies. It may constrain gap search as a serious lead, but must not yet be cited as an established defended result.

## D-021 — 2026-09-10 — ACTIVE
**Broad generic research-gap search is provisionally saturated; future literature search should target direct residual-gap killers or new evidence.**

Rationale: recent searches increasingly return already-known component combinations. The current bottleneck is no longer collecting more broadly related papers, but testing whether the residual interaction actually exists: `morphological representation → lexical–dense overlap/unique hits → incremental hybrid gain → Uzbek query characteristics`.

This is not a claim that the literature search is exhaustive. Re-open the gap if a direct analogue, a stronger publication version, or pilot experimental evidence contradicts the current position.
