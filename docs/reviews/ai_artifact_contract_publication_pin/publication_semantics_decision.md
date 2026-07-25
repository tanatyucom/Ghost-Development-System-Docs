# Publication Semantics Decision

## Problem

A Git commit cannot contain its own stable hash. The published manifest therefore cannot act as both content identity and same-commit publication evidence.

## Decision

The manifest owns content identity and finalization state. A subsequent Publication Receipt owns the exact content publication commit. Consumer binding externally pins the Receipt publication commit and verifies the Receipt-to-content relationship.

Selected Receipt path: `docs/contracts/ai_artifact_contract_publication_receipt_1.0.1.json`.

## Consequences

- No self-reference or placeholder remains in published final-state metadata.
- GDO must pin two commits and three bundle digests.
- Receipt publication commit remains pending until this Safe Commit Set is committed.
- Contract version remains 1.0.1 because schemas, fixtures, and accepted instances do not change.
