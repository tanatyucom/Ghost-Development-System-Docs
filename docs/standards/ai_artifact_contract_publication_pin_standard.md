# AI Artifact Contract Publication Pin Standard

## Decision

Contract content identity and Git publication evidence are separate. A content manifest identifies versioned bytes through schema, fixture, and contract bundle digests. A machine-readable Publication Receipt in a later commit identifies the Git commit that first published those bytes.

The manifest must contain `publication_state: CONTENT_FINALIZED` and `publication_commit_source: EXTERNAL_PUBLICATION_RECEIPT`. A published manifest must not contain `PENDING_PUBLICATION`, a same-commit self-pin, or a mutable commit placeholder.

## Publication Receipt

A Receipt contains the exact Contract version, canonical Repository ID, 40-lowercase-hex content publication commit, bundle digests, `publication_status: PUBLISHED`, supported `receipt_version`, and a SHA-256 digest over RFC 8785 bytes after removing only `receipt_digest`. The manifest digest follows the same explicit self-field exclusion rule already defined by its `manifest_digest` field; no publication field is excluded.

The Receipt is evidence about an earlier immutable content commit. Its containing commit is the Receipt publication commit and is intentionally not embedded in the Receipt.

## Consumer Verification

Consumers fail closed unless all steps pass:

1. Pin the Receipt publication commit externally in the binding configuration.
2. Load the Receipt from that commit and reject unknown critical fields or unsupported Receipt versions.
3. Require `PUBLISHED`, exact Contract version, canonical Repository ID, and a valid content commit format.
4. Verify that the content commit exists and load schemas, fixtures, and manifest from exactly that commit.
5. Recalculate schema, fixture, contract bundle, manifest, and Receipt digests offline.
6. Require every Receipt digest to match the content commit manifest and actual files.
7. Reject `PENDING_PUBLICATION`, missing Receipt evidence, remote schema resolution, inference, or fallback.

Runtime verification requires no network when both commits are present in the pinned source bundle. Updating either pin requires a separate approved Q.

## Rejected Alternatives

- Same-commit self-pin: cryptographically unstable.
- Permanent placeholder: not machine-verifiable.
- Consumer inference: non-deterministic and fail-open.
- Hidden mutable digest exclusions: weakens content identity.

This clarification changes publication metadata semantics only. Contract 1.0.1 schemas, fixtures, accepted instances, and policy semantics are unchanged.
