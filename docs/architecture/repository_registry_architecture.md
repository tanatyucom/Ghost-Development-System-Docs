# Repository Registry Architecture

**Status:** Adopted Architecture
**Version:** 1.0
**Effective Date:** 2026-07-24

## Purpose

Repository Registry is the canonical identity layer for repositories known to
GDS. It prevents a directory, workspace, planned repository, or remembered path
from being treated as an executable repository identity.

```text
Repository ID
  -> Identity and Lifecycle Status
  -> Root Policy and Machine Mapping
  -> Branch and Remote Evidence
  -> Supported Role Capabilities
  -> Mutation Class and Owner
  -> Freshness
  -> Q-specific Assignment and Authority
```

## Canonical Assets

- Machine-readable source: `docs/registries/repository_registry.yaml`
- Human-readable view: `docs/repository_registry.md`
- Schema and constraints: `docs/standards/repository_registry_standard.md`
- Identity rules: `docs/standards/repository_identity_standard.md`
- Lifecycle workflow: `docs/workflow/repository_registry_lifecycle_workflow.md`

The YAML source owns lookup values. The Markdown view explains them and must not
silently diverge.

## Identity Model

`repository_id` is stable and independent of a local absolute path. `name` is a
human label. `canonical_root` is verified local evidence when root policy is
fixed for the current environment. Machine-specific roots are mappings keyed by
`machine_id`; they do not redefine identity.

```text
Directory != Repository
Workspace != Repository
Planned Repository != Active Repository
Path != Repository ID
```

## Lifecycle

```text
Planned -> Active -> Suspended -> Active
    \          \-> Archived
     \-> Rejected / Removed
```

Only `Active` plus valid freshness may supply a mutation target. `Planned` is
discoverable design context with Mutation Class `NONE`; unresolved root and
remote values are expected rather than inferred.

## Role and Authority Boundary

The Registry records roles a repository can support. A Q assigns actual roles.
The Registry mutation class is an input ceiling, not Q authority. Effective
execution remains bounded by the stricter combination of Registry class,
Q-specific Mutation Authority, operation risk, and human approval.

## Consumers

- Canonical Draft Q Generator resolves repository assignment candidates.
- Context Inheritance verifies identity, root, lifecycle, freshness, and branch.
- Approval Engine v2 consumes status, mutation class, role, and freshness but
  cannot lower approval from Registry data alone.
- Safe Auto-Correction may resolve a unique verified name, root, branch basis,
  or machine mapping; conflict or ambiguity requires SCW.

## Non-goals

No discovery service, database, Git mutation, repository bootstrap, migration,
remote update, or runtime approval engine is implemented here.
