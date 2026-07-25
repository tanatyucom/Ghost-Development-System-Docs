# Contract Correction Report

Contract 1.0.1 is adopted as a Patch evidence correction. The canonical semantics already define size as the UTF-8 byte length of RFC 8785-canonical payload bytes and digest as SHA-256 over the same bytes.

Two fixtures were corrected: Tag Recommendation size `42 -> 28` and digest; Execution Started Event digest. No fixture payload, schema, `$id`, `$ref`, accepted instance set, or policy meaning changed. All other fixture bytes remain unchanged.

A new machine-readable manifest records all 9 schema digests, all 10 fixture digests, and JCS-derived schema, fixture, and contract bundle digests. The publication commit remains `PENDING_PUBLICATION` until the reviewed Safe Commit Set is committed.
