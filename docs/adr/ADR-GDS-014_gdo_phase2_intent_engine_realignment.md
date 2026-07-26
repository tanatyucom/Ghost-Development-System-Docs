# ADR-GDS-014 GDO Phase 2 Intent Engine Realignment

## Status

Accepted for Phase 2 planning. Operational implementation is not authorized.

## Context

The original Phase 2 Planning Q completed successfully but was not committed. Before commit, the Human Architecture Decision changed the Phase 2 entry point from Git effects to intent-driven, local-AI-assisted, read-only proposal orchestration. Rewriting the historical plan would destroy decision history; committing it as current truth would misstate the adopted architecture.

## Decision

Adopt `INTENT_DRIVEN_LOCAL_AI_ASSISTED_DEVELOPMENT_ORCHESTRATION` with initial scope `PHASE2_INTENT_DRIVEN_READ_ONLY_PROPOSAL_AND_CODEX_PACKAGE_ORCHESTRATION`.

The canonical flow is Intent Engine -> Capability Registry -> Local AI Gateway -> Repository/SQLite read-only analysis -> Summary/Classification/Draft -> Human Decision/Approval -> Q/Codex Package -> Codex Change -> Validation -> separate Git Effect Approval -> Git Effect.

Intent Sources are closed to `DIRECT_USER_INTENT`, `NEWS_PROPOSAL`, `REPOSITORY_FINDING`, `REVIEW_FINDING`, and `EXTERNAL_RESEARCH_FINDING`. Unknown sources fail closed. A `NEWS_PROPOSAL` is a candidate only and enters Proposal Inbox/triage/incubation before Human Decision and Q Promotion.

The prior `HUMAN_APPROVED_BOUNDED_GIT_EFFECT_ORCHESTRATION` plan is classified `HISTORICAL_VALID_PLANNING_SUPERSEDED_BEFORE_COMMIT`. Its Approval Binding, Safe Commit Set, fingerprint, bounded Git adapter, retry/rollback, and hook/signing/credential concepts are retained as a downstream capability family after validation.

## Consequences

- Intent Engine becomes the orchestration front door but never mutates directly.
- Capability absence, provider failure, read-only enforcement failure, ambiguity, or authority uncertainty fails closed through SCW.
- Local AI providers are replaceable behind a provider-neutral gateway and receive no repository, SQLite, Git, or approval authority.
- Human Decision governs proposal disposition and Q Promotion; Human Approval separately governs execution and effects.
- Codex is a bounded change worker and receives no implicit Git authority.
- Validation precedes Git Effect recommendation and approval.
- No schema migration or Registry mutation follows from this ADR alone.

## First Successor

`Q_AI-DEVELOPMENT-ORCHESTRATOR-PHASE2-INTENT-ENGINE-FOUNDATION-001` defines a closed deterministic Intent Record for `DIRECT_USER_INTENT`, classifies it, lists required capabilities, invokes no provider, mutates nothing, and stops.

## Rejected Ordering

Git-effect-first remains useful but is rejected as the Phase 2 entry point because it begins at the final effect boundary before intent, capability discovery, proposal governance, Codex packaging, and validation are established.
