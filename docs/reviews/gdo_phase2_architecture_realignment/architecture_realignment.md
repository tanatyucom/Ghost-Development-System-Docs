# GDO Phase 2 Architecture Realignment Decision

## Mission and Scope

Adopt mission `INTENT_DRIVEN_LOCAL_AI_ASSISTED_DEVELOPMENT_ORCHESTRATION` and scope `PHASE2_INTENT_DRIVEN_READ_ONLY_PROPOSAL_AND_CODEX_PACKAGE_ORCHESTRATION`.

The pipeline is Intent Engine -> Capability Registry -> Local AI Gateway -> Repository/SQLite Read-Only -> Summary/Classification/Draft -> Human Decision/Approval -> Q/Codex Package -> Codex Change -> Validation -> Commit/Push Approval -> Git Effect.

## Intent Sources

The closed vocabulary is `DIRECT_USER_INTENT`, `NEWS_PROPOSAL`, `REPOSITORY_FINDING`, `REVIEW_FINDING`, and `EXTERNAL_RESEARCH_FINDING`. Unknown values fail closed. Source identity and provenance are immutable; source text never grants authority.

## NEWS_PROPOSAL and Proposal Candidate

Only a structured Proposal Candidate section from Gray Ghost News Full may be ingested. Required planning fields are proposal/source identity, target domain, bounded summary/benefit/risk/confidence, duplicate hint, classification, next action, and timestamp. Whole reports are never executable intent.

Proposal states are `NEW`, `TRIAGED`, `DUPLICATE`, `INCUBATING`, `ACCEPTED_FOR_DECISION`, `REJECTED`, `PROMOTED_TO_Q`, and `ARCHIVED`. Proposal creation grants no authority; duplicate detection prevents duplicate Qs; rejected candidates remain auditable. Incubation is temporary evidence linked or retired after promotion, never a second permanent architecture source.

## Capability Registry and Local AI Gateway

The Capability Registry resolves stable versioned capability IDs to provider identity, closed input/output contracts, authority/read-write class, availability, health, failure behavior, and provenance. Missing or unhealthy capability fails closed.

The Local AI Gateway is provider-neutral across text, OCR, speech, embedding, and future providers. It enforces bounded input/output and provenance and grants no Repository, SQLite, Git, approval, or mutation authority. No provider is invoked by this Q.

## Architecture Ownership

GDS-DOCS owns architecture/contracts/governance/roadmap; GDS Runtime owns deterministic policy; GDO owns Intent/proposal/package operational state; Local AI Gateway owns provider abstraction; providers perform bounded inference; Codex performs bounded approved changes; Git Adapter performs separately approved post-validation effects. GDS Runtime never depends on GDO.

## Schema and Registry Impact

No schema migration occurs. Candidate intent/proposal/provider entities are deferred to the Intent Engine Foundation and later data-model Q. The prior Git-effect schema-v8 proposal is deferred for resequencing. Registry stays at Phase 1 scope until implementation, E2E, activation assessment, Human Approval, and a separate mutation Q.
