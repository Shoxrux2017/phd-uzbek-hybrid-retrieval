# DATABASE SEARCH EXECUTION PLAN v0.1

**Date:** 2026-09-16  
**Purpose:** live systematic-review pilot after verification of National Library access

## 1. Confirmed access

### ProQuest
- ProQuest Dissertations & Theses Global
- Education Research Index
- Coronavirus Research Database
- Publicly Available Content Database

### EBSCOhost
19 databases/collections are available.

## 2. Databases selected for the review

### Core article search
Search simultaneously in EBSCOhost:
1. Academic Search Premier
2. Science & Technology Collection
3. Library, Information Science & Technology Abstracts (LISTA)

### Doctoral evidence
Search separately:
- ProQuest Dissertations & Theses Global

### Discipline-native sources
Search separately:
- ACM Digital Library
- IEEE Xplore
- ACL Anthology

### Optional if access becomes available
- Web of Science Core Collection
- Scopus

## 3. Sources intentionally not used as core databases

Do not include eBook Academic Collection in the primary-study search.

Use eBooks only for:
- background definitions;
- historical context;
- citation chaining.

Do not include ERIC/Education/Business/Art/GreenFILE/etc. unless a later targeted question specifically requires them.

## 4. EBSCOhost live pilot

Select exactly:
- Academic Search Premier
- Science & Technology Collection
- LISTA

Run one combined search.

### Concept block A — retrieval

("information retrieval" OR "document retrieval" OR "text retrieval" OR
"passage retrieval" OR "ad hoc retrieval" OR "lexical retrieval" OR
"sparse retrieval" OR "dense retrieval" OR "semantic retrieval" OR
"semantic search" OR "vector search" OR "neural retrieval" OR
"hybrid retrieval" OR "hybrid search" OR BM25 OR
"retrieval augmented generation")

### Concept block B — morphology

(morpholog* OR stemm* OR lemmat* OR "morphological normalization" OR
"morphological analysis" OR "morphological processing" OR
"morphological preprocessing" OR "morphological segmentation" OR
"morpheme segmentation" OR "morpheme-based" OR inflection* OR
agglutinat* OR "surface form" OR "surface forms" OR "word form" OR
"word forms" OR "root extraction" OR "light stemming" OR
"aggressive stemming" OR "term conflation")

### Combined query

A AND B

### Limits

- publication years: 2000–2026
- do NOT initially require full text
- do NOT initially require peer-reviewed if the platform would thereby hide proceedings/other relevant scholarly records; instead inspect document-type distribution first
- language: no restriction during the first pilot

### Record

- exact query copied from Search History;
- search date;
- selected databases;
- total result count;
- filters;
- first 50–100 result relevance sample;
- known seed hits/misses.

## 5. PQDT Global live pilot

ProQuest supports `ALL(...)` as an all-fields search excluding full text on databases that expose this syntax.

Candidate search:

ALL(
  ("information retrieval" OR "document retrieval" OR "text retrieval" OR
   "passage retrieval" OR "lexical retrieval" OR "dense retrieval" OR
   "semantic retrieval" OR "hybrid retrieval" OR BM25)
  AND
  (morpholog* OR stemm* OR lemmat* OR "morphological normalization" OR
   "morphological analysis" OR "morphological segmentation" OR
   agglutinat* OR "root extraction" OR "morpheme segmentation")
)

Then use the interface to restrict:
- date: 2000–2026;
- document type: dissertations/theses as appropriate.

Do not search PQDT together with the other three ProQuest databases.

## 6. Export plan

For every source export, where available:

- title;
- authors;
- abstract;
- year;
- source;
- DOI;
- keywords/subjects;
- document type;
- database/platform identifier.

Preferred formats:
- RIS for reference-manager/dedup workflows;
- CSV for screening/extraction.

Keep raw exports unchanged and versioned.

## 7. Deduplication

EBSCOhost may suppress many duplicates across databases searched together, but perform project-level deduplication again after merging:

EBSCO + ProQuest + ACM + IEEE + ACL + optional WoS/Scopus + supplementary discovery.

Use:
1. DOI exact match;
2. normalized title exact/fuzzy match;
3. author + year + title confirmation.

## 8. Freeze rule

Scopus is no longer a mandatory blocker.

Freeze protocol v1.0 when:
- accessible core-source pilots have been run;
- search strings are reproducible;
- seed recall is acceptable;
- noise is manageable;
- inclusion/exclusion rules remain stable.

If Scopus/WoS later become available, add them transparently as:
- pre-freeze primary databases, or
- post-freeze protocol amendment / update-search source.
