# AI Repository Index Freshness Semantics Report

## Decision

- Structural validity verifies inventory structure and targets.
- Determinism verifies byte-identical output for identical repository state.
- Freshness verifies that Canonical regeneration produces no tracked Index diff.

These are independent states. The generated file is generator-owned and manual
editing is prohibited. The Canonical commands and remediation are defined in
`docs/standards/ai_repository_index_freshness_gate.md`.
