# GDO Phase 2 Architecture Plan

## Mission and Scope Decisions

Mission: `HUMAN_APPROVED_BOUNDED_GIT_EFFECT_ORCHESTRATION`.

Initial scope: `PHASE2_BOUNDED_HUMAN_APPROVED_SINGLE_REPOSITORY_GIT_EFFECTS`.

First vertical slice: `HUMAN_APPROVED_SINGLE_REPOSITORY_COMMIT`. It inspects one registered repository, locks an exact state and Safe Commit Set, creates one Commit proposal, binds one explicit Human Approval, executes one bounded Commit, verifies it, records Completion/Attempt/Audit, and stops. Push is not included.

## Candidate Capability Assessment

| Capability | Classification | Reason |
|---|---|---|
| Intent Intake | PHASE2_INITIAL | Produces one bounded pending Commit action; no autonomous interpretation. |
| Approval Request Binding | PHASE2_INITIAL | Mandatory one-action authority boundary. |
| Repository State Fingerprint | PHASE2_INITIAL | Invalidates approval on drift. |
| Safe Commit Set Contract | PHASE2_INITIAL | Prevents staging expansion. |
| Git Effect Request | PHASE2_INITIAL | Closed Commit request specialization. |
| Git Effect Result | PHASE2_INITIAL | Bounded execution evidence. |
| Commit Effect Adapter | PHASE2_INITIAL | Smallest local recoverable effect. |
| Push Effect Adapter | PHASE2_LATER | Remote, credentials, protection, partial effects. |
| Tag Effect Adapter | DEFERRED | Independent approval/evidence contract. |
| Release Effect Adapter | DEFERRED | Remote service and release artifact boundary. |
| Codex Worker Invocation | PHASE2_LATER | Only after Commit slice validation. |
| Cross-Repository Mutation | DEFERRED | Multi-owner atomicity and recovery unresolved. |
| Scheduler | OUT_OF_SCOPE | Conflicts with manual approval-first slice. |
| Operational Observability | PHASE2_LATER | Add after effect semantics stabilize. |
| Partial Effect Recovery | PHASE2_LATER | Required before Push activation. |
| Phase 2 Activation / Post-Activation | PHASE2_LATER | Follows implementation and E2E evidence. |

## Human Approval Model

The Canonical flow remains Completion Review -> Approval Request -> Pending Human Approval -> Explicit Approval -> Action Execution. Approval is durable because single-use consumption, revocation, stale-state evidence, conflict classification, and crash recovery cannot be reconstructed safely from conversation alone.

An immutable Approval Request binds repository, effect type `COMMIT`, branch, HEAD, repository fingerprint, Safe Commit Set digest, commit-message digest, validation digest, expiry, and one approval unit. A separate immutable Human Approval Record binds the exact request digest and human decision. `お願いします` resolves only when exactly one current visible pending request exists; otherwise SCW. State drift marks the request stale, never rewrites the human record, and requires a new request and approval. Approval cannot imply Push, Tag, Release, extra paths, or reuse.

## Git Adapter Strategy

Decision: `BOUNDED_SUBPROCESS_GIT_ADAPTER`.

Git is the authoritative implementation of index, hooks, signing, and commit-object semantics. A library abstraction risks semantic drift and still must model native repository state. The adapter accepts typed operations, never an arbitrary command string. It uses fixed executables and argv allowlists, exact repository root, explicit pathspecs, bounded time/output, scrubbed environment, no shell expansion, and no network for Commit.

Allowed Commit operations are status/fingerprint inspection, `git add -- <exact files>`, and `git commit -m <exact message>`. Forbidden forms include `.`, `-A`, `-a`, force, clean, reset, wildcard push, and dynamic remote. The adapter returns closed evidence, not unrestricted stdout/stderr.

## Commit, Push, Tag, Release, Codex, and Cross-Repository Boundaries

- Decision: `COMMIT_FIRST_VERTICAL_SLICE`; `PUSH_SEPARATE_LATER_VERTICAL_SLICE`.
- Push requires its own approval, credentials/branch-protection contract, partial-state model, E2E, and activation.
- Tag and Release are deferred independent effects. Commit/Push approval never implies either.
- Codex invocation is deferred until the Commit effect slice is validated. Later workers consume bounded Execution Packages and receive no Git authority implicitly.
- Cross-repository mutation is deferred until single-repository Commit and later Push recovery are validated.

## Retry, Rollback, and Partial Effects

Decision: `NO_AUTOMATIC_RETRY`. A failed Attempt is durable; drift invalidates approval; retry requires a new request/approval and a linear chain. Exact successful replay returns prior evidence without another Git call.

Before a Commit object exists, no destructive rollback is allowed. The adapter may restore the index only from an exact pre-index snapshot when byte-for-byte verification is possible; otherwise SCW. If a Commit exists but verification fails, preserve it and evidence, do not reset, and SCW. Later Push failure preserves the local Commit; a verification uncertainty after remote success never rewrites the remote.

## Hook, Signing, and Credential Policy

Repository profile must explicitly state hook and signing policy before execution. Hooks must be absent or individually allowlisted by path/content digest, executable behavior, expected file mutations, and timeout. Hook mutation outside the Safe Commit Set or any hook failure is SCW. `--no-verify` is prohibited without a future Canonical decision.

Signing must be explicitly `REQUIRED` or `NOT_REQUIRED`. Required signing must use a prevalidated noninteractive signer identity; any prompt, missing key, or configuration drift is SCW. GDO captures no secret. Commit uses no remote credentials. Any credential request blocks. Push credential and protection behavior belong to its later Q.

## Operability States

Durable states are `PROPOSED`, `PENDING_APPROVAL`, `APPROVED`, `STALE`, `EXECUTING`, `SUCCEEDED`, `FAILED`, `BLOCKED`, and `CANCELLED`. Every transition is versioned and audited. `APPROVED` requires an immutable approval record; `STALE` is persisted when fingerprint mismatch is observed. Eligibility such as “ready to execute” is derived from state plus current verification and never stored as authority by itself.
