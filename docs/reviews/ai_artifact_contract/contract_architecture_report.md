# Contract Architecture Report

## Executive summary

Adopt GDS-DOCS Canonical + Generated Bindings. This prevents the Runtime and the
independent orchestration platform from inventing incompatible semantics while
avoiding a premature shared repository. GDS Runtime remains Policy Provider; the
platform is Policy Consumer and operational state owner; workers produce scoped
evidence; gateways alone produce external-effect receipts.

## Goals and non-goals

The design standardizes envelopes, identity, correlation, delivery, integrity,
security, retention, and compatibility. It does not create repositories, execute
Git effects, implement queues/gateways/MCP, or mutate GameGhost/Registry.

## Key decisions

- Artifact and Event are separate: durable content versus observation/transition.
- Approval is a reference with immutable scope evidence, not a full credentialed copy.
- Execution/Completion packages are self-contained but reference large canonical inputs.
- At-least-once plus durable inbox/outbox and receipts replaces impossible
  exactly-once claims.
- Commit and push are distinct effects. Expected HEAD, safe-set digest, actual
  diff digest, allowlist, expiry, secret check, and existing receipt are required.
- Tag recommendation is not an effect.
- Dead letter and SCW are distinct operational/governance concepts.
- SHA-256 with JCS canonicalization is the version 1 integrity baseline.
- Minimal four-level classification and explicit retention classes are retained.

## Existing contract review

No blocking conflict was found. Existing approval policy remains authoritative
for approval classification; execution-result evidence remains authoritative for
evidence completeness; repository-action status remains authoritative for action
reporting. This contract supplies transportable identities and envelopes around
those meanings. Registry identity `GDS-DOCS` is reused. ADR-GDS-012 and the host
architecture confirm GDS-DOCS authority, independent runtime hosting, Python-first
future implementation, and optional MCP transport.

## Open decisions deferred

Operational storage engine, lease durations, retry budgets, blob backend,
credential-reference provider, and binding generator language require repository
architecture/implementation evidence. They do not block the canonical contract.

## Recommended next Q

`Q_AI-DEVELOPMENT-ORCHESTRATOR-ARCHITECTURE-DECISION-001`, using this contract's
identity, storage, recovery, deployment, credential-boundary, and threat-model inputs.
