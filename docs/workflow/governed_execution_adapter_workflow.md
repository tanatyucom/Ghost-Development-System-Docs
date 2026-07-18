# Governed Execution Adapter Workflow

**Status:** Draft Workflow

**Last Updated:** 2026-07-17

## Purpose

This workflow connects Runtime Intent Queue items to execution actors and
evidence without turning approval into automatic execution.

## Flow

```text
1. Runtime Queue item selected
2. Execution Request Envelope created
3. Authority Validation Gate checks actor, Approval Unit, scope, approval, and evidence
4. Adapter Router checks approval, authority, scope, dependency, idempotency
5. Adapter executes or delegates
6. Execution Result / Evidence Envelope returned
7. Evidence Reconciler validates result
8. Runtime Queue state updates
9. Completion Report records outcome
```

## Preconditions

Before execution or delegation:

- approval reference exists;
- Execution Authority Registry resolves the actor and Approval Unit;
- approved scope is explicit;
- actor authority is known;
- tool availability is known;
- dependency requirements are satisfied;
- evidence requirements are known;
- repository boundary is verified.

Missing preconditions produce `BLOCKED` or `SCW_REQUIRED`.

Authority source of truth:

```text
docs/registries/execution_authority_registry.yaml
```

Gate:

```text
docs/workflow/authority_validation_gate.md
```

## Delegation

When current actor cannot execute:

```text
Execution Queue Item
  -> Human Delegation Adapter or Codex Delegation
  -> DELEGATED
  -> WAITING_FOR_EVIDENCE
```

Delegation must include expected evidence.

## Evidence Reconciliation

Evidence is compared against:

- request ID;
- queue item ID;
- operation;
- repository;
- branch;
- actor;
- approved scope;
- dependency state;
- required evidence fields.

If evidence is missing, conflicting, partial, or unknown, do not mark complete.

## Failure Handling

| Condition | Workflow Result |
| --- | --- |
| Tool unavailable | `BLOCKED` or `DELEGATION_REQUIRED` |
| Credential unavailable | `SCW_REQUIRED` |
| Scope violation | `SCW_REQUIRED` |
| Partial success | `PARTIAL` and review |
| Unknown result | `SCW_REQUIRED` |
| Failure with evidence | `FAILED` |

## Completion Report Requirements

Record:

- adapter decision;
- request / result contract used;
- authority outcome;
- delegation result;
- evidence status;
- queue state mapping;
- SCW or failure behavior;
- commit / push / tag status.
