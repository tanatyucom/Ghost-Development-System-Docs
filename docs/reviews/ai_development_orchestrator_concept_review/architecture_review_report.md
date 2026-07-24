# AI Development Orchestrator Concept Review

## Executive Summary

The proposed AI Development Orchestration Platform is a valid independent
system concept. Its purpose is transport, durable work coordination, governed
execution, and evidence delivery across Human, ChatGPT contexts, Codex workers,
repositories, and GDS policy. It must not become GDS policy, a GameGhost
dependency, or an MCP-branded monolith.

## Review Verdict

`PASS WITH FOLLOW-UP`

Option B, an independent platform consuming versioned GDS contracts, is the
recommended target. Start with contract definition and durable artifact exchange
plus manual worker launch. Automated worker launch and Git execution follow only
after idempotency, optimistic locking, security, and audit gates are proven.

## Strengths

- Correct separation of GDS policy, product repositories, and orchestration.
- MCP is treated as an adapter/transport rather than the whole platform.
- Durable artifact/event handling addresses offline receivers and session gaps.
- Tag remains a separate recommendation and approval flow.
- The concept explicitly protects GameGhost product independence.

## Critical Risks

1. Review actor and execution actor are conflated in the provisional Commit
   responsibility. ChatGPT may review, recommend, and coordinate approval, but
   the Execution Gateway or an authorized worker must execute and return evidence.
2. Q-start Commit/Push authorization is unsafe if treated as one blanket grant.
   Commit and Push remain separate Approval Units with exact repository, branch,
   Expected HEAD, allowed diff, expiry, and invalidation conditions.
3. At-least-once event delivery can duplicate worker or Git execution unless
   idempotency keys, leases, attempt records, and effect receipts are durable.
4. Artifact payloads can leak secrets or over-retain source content.
5. A single service owning queue, policy interpretation, credentials, and Git
   creates a high-value confused-deputy boundary.

## Boundary Conflicts and Corrections

- `ChatGPT executes Commit/Push` becomes: ChatGPT reviews and coordinates; the
  authorized Execution Gateway executes.
- `Codex is stateless` becomes: Codex workers may be replaceable/stateless, while
  execution state is durable in the platform. A worker still has a scoped
  execution identity and attempt ID.
- `Non-stop until Completion` is valid only inside current authority; it does not
  suppress invalidation, evidence conflict, secret detection, or separate Tag/Release approval.
- `Push completes Q` is policy-dependent. A Q requiring publication remains open
  until Push evidence; documentation-only or no-push Qs may close earlier.

## Missing Concepts

- Versioned Artifact/Event Contract and compatibility negotiation.
- Durable inbox/outbox, acknowledgements, leases, retry budgets, dead-letter state.
- Execution/Approval/Q/Repository/Attempt correlation model.
- Optimistic locks: expected repository ID, branch, HEAD, remote, and Safe Commit Set digest.
- Artifact classification, redaction, retention, deletion, and access policy.
- Credential broker boundary; credentials never enter artifacts.
- Append-only/tamper-evident audit chain and clock/actor identity policy.
- Recovery ownership and operational runbook.

## Option Comparison

| Option | Boundary | Fault/Security isolation | Initial cost | Coupling | Verdict |
| --- | --- | --- | --- | --- | --- |
| A: GDS Runtime package | Poor; policy and orchestration merge | Low | Low | High | Rejected |
| B: Independent platform | Clear Policy Provider/Consumer | High | Medium | Low via contracts | Recommended |
| C: Monorepo independent app | Logical separation, physical coupling | Medium | Medium | Release/repository coupling | Transitional only, not target |

## Required Decisions Before Bootstrap

- Product/system identity and provisional Registry ID.
- Repository root/remote/branch/owner and hosting.
- Contract ownership and versioning.
- Local process/deployment model and credential boundary.
- Artifact store, event store, retention, and recovery model.
- MVP exclusion list and security threat model.

## Recommended Next Q Sequence

1. `Q_AI-ARTIFACT-CONTRACT-001` — define envelopes, IDs, versions, receipts,
   idempotency, redaction, retention, and compatibility.
2. `Q_AI-DEVELOPMENT-ORCHESTRATOR-ARCHITECTURE-DECISION-001` — adopt the
   independent-system boundary, identity, repository strategy, deployment and security model.
3. `Q_GDS-RUNTIME-REPOSITORY-BOOTSTRAP-001` — bootstrap Policy Runtime without orchestration components.
4. `Q_AI-DEVELOPMENT-ORCHESTRATOR-REPOSITORY-BOOTSTRAP-001` — only after the ADR
   and contracts are approved.
5. Phase 1 implementation Q — artifact exchange and manual worker launch.
6. Phase 2 Q — durable queue and event-driven worker launch.
7. Phase 3 Q — reviewed Commit/Push Execution Gateway.

Artifact Contract precedes both bootstraps because it fixes the dependency
direction and prevents each repository from inventing incompatible envelopes.

## Sources Reviewed

- `docs/adr/ADR-GDS-012_implementation_host_and_runtime_selection.md`
- `docs/architecture/implementation_host_runtime_architecture.md`
- `docs/architecture/governed_execution_adapter_foundation.md`
- `docs/architecture/git_execution_adapter_vertical_slice.md`
- `docs/architecture/approval_engine_v2.md`
- `docs/standards/approval_policy_standard.md`
- `docs/standards/execution_result_evidence_contract.md`
- `docs/standards/repository_action_status_and_recommendation_model.md`
- `docs/registries/repository_registry.yaml`
