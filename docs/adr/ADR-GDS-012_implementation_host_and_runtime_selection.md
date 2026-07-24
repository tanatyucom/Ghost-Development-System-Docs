# ADR-GDS-012: GDS Implementation Host and Runtime Selection

**Status:** Accepted
**Date:** 2026-07-24

## Context

Approval Engine, Draft Q Generator, Registry Validator, and DX tooling share
unknown implementation host, runtime, dependency, path, and authority fields.
Starting feature Qs before resolving them would create predictable SCW.

## Decision

Use a dedicated Planned GDS Runtime repository and Python as the primary core
runtime. Bootstrap/activation is a separate REQUIRED Q. GDS-DOCS remains the
specification source; adapters connect consumers. MCP is future transport only.

## Rejected Options

- GDS-DOCS: rejected because runtime dependencies, packaging, tests, and release
  would contaminate documentation/governance responsibility.
- GameGhost: rejected because a product repository must not own reusable GDS
  governance tooling or become a core dependency.
- Existing Execution Platform: rejected for now because no Active/Verified
  repository identity exists.
- TypeScript core: not selected because current policy workload and evidence
  favor Python; retained for a future transport adapter.
- PowerShell core: rejected for portability/library/test maintenance.
- Mixed core: rejected for duplicated models, compatibility, and DX cost.

## Consequences

Feature implementation waits for repository bootstrap and Registry activation.
There is multi-repository synchronization cost, offset by clear ownership,
dependency isolation, release independence, and reusable consumers.

## Follow-up

First execute `Q_GDS-RUNTIME-REPOSITORY-BOOTSTRAP-001`. After activation, resume
Approval Engine, Draft Q Generator, Registry Validator, and DX Metrics Qs with
the exact Active Registry context.
