# Authority Validation Gate

**Status:** Draft Workflow

**Last Updated:** 2026-07-18

## Purpose

Authority Validation Gate checks whether a requested action can proceed to
Approval Request, execution, delegation, or SCW.

It consumes:

```text
docs/registries/execution_authority_registry.yaml
```

## Standard Flow

```text
Intent / Requested Action
  -> Resolve Approval Unit
  -> Resolve Execution Actor
  -> Check Execution Authority
  -> Check Approval Request Authority
  -> Check Scope
  -> Check Human Approval Requirement
  -> Check Approval State
  -> Check Evidence Responsibility
  -> Execute / Delegate / Approval Request / SCW
```

## Pre-Response Integration

Before Codex displays an Approval Request, confirm:

- Codex or the selected actor is registered as the Execution Actor.
- The Approval Unit is known.
- The actor has matching Execution Authority.
- The actor has Approval Request Authority for that unit.
- Human Approval requirement is known.
- Repository or resource scope matches the current Q.
- Evidence responsibility is defined.

If any check fails, do not show the Approval Request. Use SCW with the missing
or conflicting authority reason.

## Pre-Execution Integration

Before execution or delegation, confirm:

- Human Approval exists when required.
- Approval scope matches the requested action.
- Execution Actor matches the registry.
- Mutation scope is defined.
- Adapter or tool authority is known.
- Evidence contract is available.

Unknown, conflicting, or stale authority blocks execution.

## Gate Outcomes

| Outcome | Meaning | Next Step |
| --- | --- | --- |
| `AUTHORIZED_FOR_APPROVAL_REQUEST` | Actor may ask Human for Approval. | Display Approval Request. |
| `AUTHORIZED_FOR_EXECUTION` | Actor may execute approved unit. | Execute or delegate through governed path. |
| `DELEGATION_REQUIRED` | Current actor cannot execute but registered delegate can. | Create delegation request with expected evidence. |
| `BLOCKED` | Known violation. | Stop and report. |
| `SCW_REQUIRED` | Authority, scope, approval, or evidence is unclear. | Stop / Call / Wait. |

## SCW Conditions

Use SCW when:

- Approval Unit cannot be resolved.
- Execution Actor is missing from the registry.
- Approval Request Actor is not the registered Execution Actor or governed
  execution surface.
- Recommendation Authority is mistaken for Execution Authority.
- Mutation Authority exists without scope.
- Human Approval requirement is unknown for a high-risk action.
- Evidence Responsibility is missing.
- Registry entry is Draft / Deprecated / Revoked for the requested operation.

## Non-Goals

This workflow does not implement runtime enforcement, Git automation, external
API execution, credential management, or GameGhost behavior.
