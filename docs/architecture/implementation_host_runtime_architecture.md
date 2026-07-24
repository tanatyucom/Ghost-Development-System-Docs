# GDS Implementation Host and Runtime Architecture

**Status:** Adopted Decision
**Version:** 1.0
**Effective Date:** 2026-07-24

## Decision

GDS governance tooling runtime is hosted in a dedicated repository with the
provisional Registry ID `GDS-RUNTIME-PROVISIONAL`. The repository remains
`Planned`; this decision does not create or initialize it. Python is the primary
core runtime. MCP and other transports are adapters outside the core.

## Why

- GDS-DOCS remains the canonical documentation/governance repository and should
  not acquire runtime packaging, dependency, test, or release responsibility.
- GameGhost is an application repository; hosting cross-repository governance
  tooling there creates coupling and authority contamination.
- No existing verified Execution Platform repository is available.
- Python fits existing GDS validation evidence, YAML/Markdown processing,
  Windows paths, CLI/library use, golden tests, and existing team familiarity.
- A dedicated repository isolates dependencies, releases, source mutation, and
  audit evidence while preserving GDS-DOCS as specification authority.

## Host Contract

- Provisional name: `GDS Runtime`.
- Registry ID: `GDS-RUNTIME-PROVISIONAL`.
- Status: Planned / Pending.
- Root, remote, default branch: UNKNOWN until bootstrap approval.
- Mutation Class: NONE until activation.
- Bootstrap is a separate REQUIRED Q.

## Runtime Decision

Primary runtime: Python 3.12-compatible or later version selected by the
bootstrap Q and locked by project metadata. The architecture does not authorize
installation. Standard library is preferred; external packages require an
approved dependency manifest, lock, license/provenance review, and vulnerability
review.

TypeScript/Node.js is reserved for a future MCP/transport adapter when evidence
requires it. PowerShell may be an invocation adapter on Windows, not core policy.
Mixed-runtime core is rejected because it duplicates models and increases DX
and audit cost.

## Repository Layout Contract

```text
src/gds_runtime/
  approval/
  draft_q/
  repository_registry/
  context/
  validation/
  audit/
  cli/
  adapters/
  schemas/
tests/
  unit/
  golden/
  scenarios/
  integration/
docs/
```

Core policy must not import repository-specific or transport adapters. Adapters
depend inward on stable core interfaces.

## Integration Surfaces

- Approval: operation/risk/Registry/Q authority/scope/evidence -> classification,
  reasons, audit record.
- Draft Q: candidate/completion/handover/Registry/template -> non-executable
  draft, missing-input report, provenance.
- Registry: canonical YAML + observed facts -> PASS/WARNING/CONFLICT, lookup,
  freshness, diagnostics.
- MCP: future exchange adapter only; no core policy and no Steam relationship.

## Authority and Security

Implementation Qs must name the activated repository entry, exact roots, source,
test, schema, config, generated, and prohibited paths. Default interfaces are
read-only. No secret logging, credential inference, auto-approval, or automatic
mutation occurs without an explicit governed policy and approval unit.

## Test and Version Strategy

Use unit, schema, golden, 16/18-scenario, fixture, Windows path, encoding,
mojibake, escalation, Planned-rejection, correction, and SCW boundary tests.
Package, policy, and schema versions are separate. Semantic Versioning is used
after first release; pre-release compatibility is explicit. Runtime/schema
compatibility is published as a matrix. Release and tags remain separately approved.
