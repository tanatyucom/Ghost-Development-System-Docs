# GDO Phase 2 Pipeline Boundary Report

## Read-Only Analysis

Repository adapters permit bounded file/document/Git-state reads only. SQLite adapters open immutable/read-only connections and permit schema inspection and `SELECT` only. Filesystem write/delete/rename, staging, Commit/Push, SQL mutation/migration, Registry mutation, remote execution, extensions that can write, and prompt-only enforcement are prohibited. Technical read-only mode, root containment, statement allowlists, size/time limits, and post-read verification are required.

## Outputs

`INSPECTION_REPORT`, `SUMMARY_REPORT`, `CLASSIFICATION_RESULT`, `PROPOSAL_CANDIDATE`, `DRAFT_Q`, `DRAFT_DECISION`, `DRAFT_PATCH_PLAN`, `DRAFT_EXECUTION_PACKAGE`, and `DRAFT_VALIDATION_PACKAGE` are non-authoritative proposal artifacts. Each is bounded, explicitly draft, provenance-rich, confidence-bearing, deterministic where applicable, and has `execution_authority=false`.

## Human Decision, Approval, and Q Promotion

Human Decision accepts/rejects/incubates/promotes proposals or selects architecture. Human Approval separately authorizes Q execution, bounded Codex invocation, returned-change acceptance, Commit, Push, Tag, or Release. Neither implies the other.

Q Promotion requires an accepted Decision, new Q ID, target repository, bounded objective/scope/exclusions, authority and validation boundaries, predecessor/successor context, and source provenance. Proposal identity remains linked but never substitutes for Q identity or authority.

## Codex and Validation

Codex receives only an approved Q and bounded Execution Package. It may change the designated worktree but cannot infer Commit/Push/Tag/Release, expand scope, mutate another repository, accept approval, or bypass SCW. Automatic invocation is deferred.

Returned changes enter a Validation Package covering scope, contract, diff, tests, security, Safe Commit Set, Completion Review, and effect recommendation. Validation PASS is not Git approval.

## Git Effect Repositioning

Git Effect becomes a downstream post-validation capability family. The preserved plan supplies later Approval Binding, Safe Commit Set/fingerprint, bounded adapter, retry/rollback, and hook/signing/credential work. It cannot enter active implementation order before Intent, capability, provider, read-only, proposal, promotion, Codex package, and validation foundations.

## Security and SCW

Ambiguous intent/source/authority, unknown capability, unhealthy provider, read-only enforcement failure, Decision/Approval conflation, package scope uncertainty, provider/Codex/Git implicit authority, migration need, or Registry need triggers SCW. No operational code, provider/OCR/speech/Codex invocation, Git effect, migration, Registry/Runtime/GameGhost mutation, credential, automatic approval/retry/failover, or external execution occurs here.
