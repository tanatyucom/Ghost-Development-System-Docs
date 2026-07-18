# Execution Authority Registry

**Status:** Draft Architecture Contract

**Last Updated:** 2026-07-18

## Purpose

Execution Authority Registry is the canonical lookup layer for actor, tool, and
capability authority in GDS.

It operationalizes Authority-Driven Responsibility Principle:

```text
責務は機能ではなく、権限で決める。
```

The registry answers:

- what an actor can observe;
- what an actor can analyze;
- what an actor can recommend;
- whether an actor may request Human Approval;
- whether an actor may execute;
- whether an actor may mutate repository or external state;
- which operations require Human Approval;
- which evidence the actor must produce after execution.

## Source Of Truth

Machine-readable source:

```text
docs/registries/execution_authority_registry.yaml
```

Human-readable schema:

```text
docs/standards/execution_authority_registry_schema.md
```

Validation workflow:

```text
docs/workflow/authority_validation_gate.md
```

The YAML registry is the single source of truth for initial authority entries.
Markdown documents explain the meaning, lifecycle, and review behavior.

## Authority Categories

| Category | Meaning |
| --- | --- |
| Observe | Read state, files, diffs, registry entries, runtime status, or evidence. |
| Analyze | Evaluate observed data, risk, quality, completion, or architecture. |
| Recommend | Propose next actions without implying execution authority. |
| Request Approval | Ask Human for Final Approval for a visible Approval Unit. |
| Execute | Perform or delegate an action after authority and approval checks. |
| Mutate | Change repository, runtime, data, external system, release, or deployment state. |
| Produce Evidence | Record execution result, failure, abort, or review evidence. |

## Initial Actor Model

| Actor | Observe | Analyze | Recommend | Request Approval | Execute / Mutate | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| ChatGPT | Limited / context-dependent | Yes | Yes | No | No | Review Evidence only |
| Codex | Yes, current repository | Yes | Yes | Yes, for executable actions | Yes, within approved scope | Execution Evidence |
| Human | Yes | Yes | Yes | Not applicable | Manual or delegated | Human decision / manual evidence |
| Automation Actor | Conditional | Conditional | Conditional | No by default | No by default | Required if granted |
| Read-only Adapter | Yes | Limited | No | No | No | Observation Evidence |
| Repository Mutation Adapter | Yes | Limited | No | No | Conditional | Execution Evidence |

## Approval Unit Mapping

Authority is action-specific. Minimum Approval Units are:

- Commit
- Push
- Tag
- File Mutation
- Repository Migration
- External API Write
- Data Deletion
- Automation Activation
- Release
- Deployment

Each Approval Unit maps:

- Execution Actor
- Approval Request Actor
- Required Human Authority
- Evidence Type
- Risk Level
- Default Recommendation Policy

## Validation Rules

The registry is consumed by Authority Validation Gate.

Minimum rules:

1. Approval Request Authority requires matching Execution Authority.
2. Mutation Authority requires defined repository / resource scope.
3. High-risk Execution Authority requires Human Approval Requirement.
4. Execution Authority requires Evidence Responsibility.
5. Unknown Authority, Conflicting Authority, or Missing Scope requires SCW.
6. Recommendation Authority does not imply Execution Authority.
7. Review Actor must not issue Approval Request unless it is also the
   registered Execution Actor for that Approval Unit.

## Lifecycle

Registry entries use:

- Draft
- Reviewed
- Approved
- Active
- Deprecated
- Revoked
- Archived

Authority changes must preserve history through request artifacts, completion
reports, and registry update records.

## Non-Goals

This registry does not implement:

- runtime database;
- Git automation;
- Intent Engine runtime;
- Workflow Engine runtime;
- Automation runtime;
- Ghost SDK runtime;
- credential management;
- GameGhost changes.
