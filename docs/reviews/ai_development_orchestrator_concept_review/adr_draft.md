# ADR Draft: Independent AI Development Orchestration Platform

**Status:** Proposed — Human Review Required

## Context

GDS Runtime provides governance policy, while reliable ChatGPT/Codex artifact
exchange, worker lifecycle, retries, recovery, and governed Git effects require
operational state and privileged boundaries that do not belong in GDS Runtime
or product repositories.

## Decision

Create an independent AI Development Orchestration Platform as a versioned GDS
Policy Consumer. Initially deploy it as one local application with modular
boundaries. Keep GDS Runtime, GameGhost, and future products independent. Treat
MCP as an optional adapter. Add Execution Gateway only after artifact/queue
reliability and security contracts are validated.

Shared semantic contracts are canonical in GDS-DOCS. Runtime repositories may
package generated bindings tied to explicit contract versions.

## Alternatives

- GDS Runtime package: rejected due responsibility, privilege, fault, and release coupling.
- Fully independent platform: selected target.
- Monorepo application: acceptable only as a temporary bootstrap convenience if
  physical independence is preserved and extraction criteria are explicit; not preferred.

## Consequences

Benefits: clear trust/failure boundary, reusable platform, independent upgrades,
durable recovery, least-privilege execution. Costs: contracts, two repository
lifecycles, compatibility testing, deployment and operational ownership.

## Risks

Confused deputy, stale approval, duplicate delivery, credential leakage,
contract drift, queue loss, oversized platform scope, and premature Git automation.

## Follow-up

Artifact Contract Q, formal ADR Q, GDS Runtime bootstrap, platform repository
bootstrap, then phased implementation.

## Related Decisions

- ADR-GDS-012: GDS Implementation Host and Runtime Selection.
- Governed Execution Adapter Foundation.
- Git Execution Adapter Vertical Slice.

## Superseded Decisions

None. This draft clarifies that the future MCP adapter mentioned by ADR-GDS-012
does not imply Orchestrator ownership inside GDS Runtime.
