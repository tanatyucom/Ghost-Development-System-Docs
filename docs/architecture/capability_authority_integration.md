# Capability / Authority Integration

**Status:** Draft Architecture Contract

**Last Updated:** 2026-07-18

## Purpose

This document defines how Capability Registry concepts connect to Execution
Authority Registry.

Core distinction:

```text
Capability = what can be done.
Authority = what may be executed.
Execution requires both.
```

Japanese:

```text
能力があることは、実行権限があることを意味しない。
実行権限があることは、能力が実装されていることを意味しない。
実行にはCapabilityとAuthorityの両方が必要である。
```

## Source Of Truth

Machine-readable binding source:

```text
docs/registries/capability_authority_bindings.yaml
```

Related authority source:

```text
docs/registries/execution_authority_registry.yaml
```

Human-readable schema:

```text
docs/standards/capability_authority_binding_schema.md
```

Delegation contract:

```text
docs/standards/capability_delegation_contract.md
```

## Resolution Model

```text
Requested Action
  -> Required Capability
  -> Capability Provider
  -> Capability Status
  -> Execution Actor
  -> Authority
  -> Scope
  -> Approval Unit
  -> Human Approval Requirement
  -> Evidence Responsibility
  -> Execute / Delegate / Pending Approval / Block / SCW
```

## Capability Classes

| Class | Meaning |
| --- | --- |
| Observe | Read files, repositories, diffs, registries, or runtime state. |
| Analyze | Evaluate observed state, quality, risk, architecture, or completion. |
| Recommend | Propose next action without granting execution. |
| ApprovalRequest | Ask Human for approval for a visible Approval Unit. |
| Execute | Perform a governed action after checks. |
| Mutate | Change repository, runtime, resource, data, external API, release, or deployment state. |
| Evidence | Produce review, execution, abort, SCW, approval linkage, or validation evidence. |

## Binding Fields

Minimum fields:

- Binding ID
- Capability ID
- Capability Provider
- Execution Actor
- Authority Type
- Repository / Resource Scope
- Approval Unit
- Human Approval Requirement
- Evidence Type
- Risk Level
- SCW Conditions
- Status
- Source of Truth

## Integration Contracts

### Capability Registry Contract

Capability records should expose:

- Capability ID
- Capability Name
- Provider
- Provider Type
- Capability Class
- Read / Analyze / Recommend / Execute / Mutate class
- Input Contract
- Output Contract
- Repository / Resource Scope
- Risk Level
- Lifecycle Status
- Version
- Dependencies
- Evidence Capability

### Authority Registry Contract

Authority entries should expose:

- Actor ID
- Authority Type
- allowed Capability IDs or Classes
- Scope
- Approval Unit
- Approval Requirement
- Evidence Responsibility
- Risk Constraints
- Status

## Approval Unit Integration

Approval Units are connected to capabilities through the binding registry.

Minimum units:

- Commit
- Push
- Tag
- File Mutation
- Registry Update
- Repository Migration
- External API Write
- Data Deletion
- Automation Activation
- Release

Each unit must identify:

- Required Capability
- Execution Actor
- Authority Type
- Human Approval Requirement
- Evidence Capability
- Default Recommendation Policy

## Pre-Response Integration

Before Codex outputs Workflow Recommendation or Approval Request, check:

- corresponding Capability is Active;
- Codex is the Capability Provider or registered Execution Actor;
- matching Authority exists;
- scope matches;
- Approval Unit is defined;
- Human Approval requirement is known;
- Evidence Capability exists.

If any check fails, use SCW and do not display an Approval Request.

## Pre-Execution Integration

```text
Capability Validation
  -> Authority Validation
  -> Scope Validation
  -> Approval Validation
  -> Evidence Readiness Validation
  -> Execute
```

Any failure blocks execution or produces SCW.

## Delegation Model

Tool capability does not grant actor authority.

Example:

```text
Codex
  -> delegates
Git CLI
```

Git CLI may provide the technical capability, but Authority remains attached to
the Execution Actor and approved scope.

Minimum delegation fields:

- Delegating Actor
- Tool / Provider
- Capability
- Delegation Scope
- Authority Source
- Evidence Responsibility

## Non-Goals

This integration does not implement:

- runtime parser;
- automatic schema validator;
- Intent Engine runtime;
- Workflow Engine runtime;
- Automation runtime;
- Ghost SDK runtime;
- Git Runtime changes;
- GameGhost changes.
