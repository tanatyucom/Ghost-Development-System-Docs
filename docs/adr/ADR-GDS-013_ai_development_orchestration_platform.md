# ADR-GDS-013: Independent AI Development Orchestration Platform

**Status:** Accepted
**Date:** 2026-07-25
**Accepted Date:** 2026-07-25
**Decision Owner:** Project Owner
**Adoption Authority:** Q_GDS-ADR-GDS-013-HUMAN-ADOPTION-001

## Context

GDS requires durable exchange of approved execution packages, worker evidence,
events, retries, and external-effect receipts. Placing those operational concerns
inside GDS Runtime would merge deterministic policy with stateful orchestration,
privileges, and failure recovery. Placing them in GameGhost would make a product
repository a reusable development-system dependency. MCP alone is a transport,
not an operational system.

## Decision

Create, through a later separately approved bootstrap, an independent platform:

- Product name: **Ghost Development Orchestrator**
- Short name: **GDO**
- Repository candidate: `ghost-development-orchestrator`
- Registry ID candidate: `GHOST-DEVELOPMENT-ORCHESTRATOR-PROVISIONAL`
- Classification: independent local-first platform and GDS Policy Consumer

GDS-DOCS owns governance and canonical semantic contracts. GDS Runtime is the
deterministic Policy Provider. GDO owns durable operational state, artifact/event
routing, admission, worker attempts, retry/recovery, effect coordination, and
receipts. GameGhost remains an independent product and has no GDO runtime
dependency. ChatGPT reviews, recommends, and coordinates approval; Codex consumes
scoped execution packages and returns evidence. Neither actor invents authority.

## Decision Drivers

- Clear policy/operation and product/platform responsibility
- Independent fault, privilege, release, and recovery boundaries
- Reuse across repositories without GameGhost coupling
- At-least-once delivery and receipt-first recovery
- Least privilege for future Git effects
- Contract compatibility without premature repository proliferation

## Architecture

```text
GDS-DOCS --canonical contracts--> GDS Runtime --policy decisions-->
Ghost Development Orchestrator --scoped packages--> Codex Worker
Ghost Development Orchestrator --approved effects--> Execution Gateway
Execution Gateway --immutable receipts--> Ghost Development Orchestrator
```

## Responsibility Boundary

GDS-DOCS defines meaning. GDS Runtime evaluates deterministic governance policy
without queue, credential, worker, or Git ownership. GDO consumes decisions and
owns operational truth without changing policy. Workers perform bounded work.
The future Gateway performs typed approved effects. Product repositories are
targets only under an explicit Q assignment.

## Repository Strategy

Use a separate private GitHub repository owned by Project Owner, default branch
`main`, local root candidate `C:/GitHub/ghost-development-orchestrator`, remote
candidate `https://github.com/tanatyucom/ghost-development-orchestrator.git`.
These are proposals, not verified identities. Bootstrap and Registry mutation
are separate approval units. Generated bindings are version-pinned derivatives
of GDS-DOCS schemas; dependencies flow from GDO to published/pinned GDS contracts
and policy interfaces, never from GDS Runtime to GDO.

## Deployment Model

Phase 1 is one manually launched local application with internal modules and
durable local storage. Storage technology is deferred. Phase 3 introduces a
separate least-privilege Execution Gateway process. Windows Service, Docker,
cloud, remote workers, and multi-user tenancy are excluded until evidence and
separate decisions justify them.

## Security Boundary

Credentials never enter artifacts, events, prompts, or audit payloads. Only the
future Gateway obtains scoped credentials from an approved OS/user credential
facility. Effects are typed and allowlisted; unrestricted shell and force push
are prohibited. Expected repository/branch/remote/HEAD, safe-set and diff
digests, secret scan, approval expiry/invalidation, and receipt lookup are gates.

## Contract Ownership

GDS-DOCS is the semantic and schema source of truth at Artifact Contract 1.0.0.
Consumers may generate pinned bindings. No shared schema repository is created
initially. Contract downgrade or unsupported major versions are rejected.

## MCP Positioning

MCP is an optional adapter inside GDO. It is not the platform identity, durable
queue, policy authority, approval authority, recovery owner, GDS Runtime, or
GameGhost dependency. Phase 1 must work without MCP.

## Consequences

The design adds a repository and deployment boundary later, plus contract and
release coordination. In return it isolates privileges and failures, preserves
GDS and GameGhost responsibilities, and supports reusable durable orchestration.

## Risks

Contract drift, confused deputy behavior, stale approvals, duplicate delivery,
artifact injection, credential leakage, audit tampering, and local compromise
remain risks. Version pinning, validation, least privilege, immutable evidence,
and the threat-model gates mitigate them.

## Alternatives

- Option A, GDS Runtime package: rejected because policy and operational state,
  privilege, failure, and release boundaries would merge.
- Option C, monorepo independent apps: rejected as target because physical and
  release coupling remains; acceptable only as an explicitly temporary prototype.

## Follow-up

Human adoption is complete. Next, execute GDS Runtime bootstrap under separate
repository-creation authority, verify its Registry activation, execute GDO
bootstrap, add its Planned Registry entry through separate authority, and
progress through Artifact Exchange, Queue/Worker, Gateway, and advanced recovery
phases.

## Related Decisions

- ADR-GDS-012: GDS Implementation Host and Runtime Selection
- AI Development Artifact Contract 1.0.0
- AI Development Orchestrator Concept Review

## Superseded Decisions

None. The provisional MCP-repository concept is not promoted by this ADR and
requires separate Registry reconciliation if retained.
