# Registries

## Purpose

This folder stores machine-readable or registry-like source files used by GDS
documentation contracts.

Registries define canonical lookup data. Human-readable explanations, schema
notes, examples, and workflows live in `docs/architecture/`, `docs/standards/`,
`docs/workflow/`, `docs/rules/`, and `examples/`.

## Contains

- `execution_authority_registry.yaml`: machine-readable source of truth for
  Execution Authority Registry v0.1.

## Does NOT Contain

- Runtime database implementation.
- Git automation.
- Credential storage.
- External API integration.
- GameGhost runtime data.

## Update Policy

Registry updates require:

- source Q or approved revision;
- Human Approval when authority, mutation, or high-risk behavior changes;
- updated human-readable documentation when the registry meaning changes;
- AI Repository Index refresh when Markdown entry points are added or changed;
- Repository Quality Audit before completion.

Unknown, conflicting, or missing authority must produce SCW instead of
execution.
