# Execution Evidence Mapping

| Operation | Required Evidence |
| --- | --- |
| Commit | Commit ID, message, repository, branch, changed scope, actor. |
| Push | Remote, branch/ref, pushed commit ID, push result, actor. |
| Tag | Tag name, target commit, local creation result, remote push result when requested. |
| Next Q | Artifact path, canonical artifact declaration, validation result. |
| Roadmap Update | Changed roadmap path, summary, validation result. |
| ADR | ADR path, status, related decision, validation result. |
| Knowledge Promotion | Promotion artifact path or deferred rationale, validation result. |

## Reconciliation

Evidence must match expected action, repository, actor, and scope.

Mismatch means `SCW_REQUIRED`.
