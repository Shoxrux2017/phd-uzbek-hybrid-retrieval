# Export manifest

This export contains all `ARTICLE_RESEARCH_PROTOCOL` versions visible in the conversation file list: v0.1, v0.2, v0.3, v0.4, v0.5, v0.6, v0.7, v0.8, v0.9, v0.11, and v1.0_FROZEN. Two duplicate filename occurrences were visible for v0.1 and v0.4.

## Duplicate handling

A Windows directory cannot contain two files with exactly the same filename. Therefore one copy of each version is placed directly in this `protocol` folder, while duplicate occurrences are kept under `_duplicates/.../` with the **original filename unchanged**.

The earliest v0.1 and earliest v0.4 conversation attachments no longer expose downloadable backing bytes. The later same-version copies are downloadable. To ensure the requested duplicate file is present, the duplicate subfolder contains a byte-for-byte copy of the downloadable twin and is timestamped to the earlier chat occurrence. These two reconstructed duplicate entries are therefore **not independently verified as byte-identical to the inaccessible earlier backing artifact**.

All other exported protocol files are materialized from their downloadable conversation backing files.
