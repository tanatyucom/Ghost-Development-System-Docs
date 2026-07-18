# Governed Execution Adapter Foundation

**Status:** Draft Architecture Foundation

**Last Updated:** 2026-07-17

## Purpose

This document defines the Governed Execution Adapter Interface foundation.

Execution Adapter is not a simple command wrapper. It is both:

1. a governed execution boundary that checks approval, authority, scope, and
   dependencies before execution or delegation;
2. an evidence provider boundary that returns verifiable execution results to
   Runtime Queue reconciliation.

This document follows `GDS-EXECUTION-ADAPTER-FOUNDATION-001 v1.0`.

## Non-Goals

This foundation does not implement:

- production runtime engine;
- Git adapter code;
- MCP server or MCP tool;
- GUI;
- credential storage;
- secret management;
- automatic commit / push / tag;
- GameGhost changes.

## Parent Architecture

- `docs/architecture/runtime_intent_queue_resolver.md`
- `docs/architecture/approval_request_intent_queue_execution_evidence.md`
- `docs/architecture/platform_execution_evidence_contract.md`
- `docs/standards/execution_queue_display_contract.md`
- `docs/rules/runtime_intent_resolution_rules.md`

## Architecture

```text
Human Approval
  -> Runtime Intent Resolver
  -> Execution Queue Item
  -> Execution Adapter Router
     -> Capability Check
     -> Authority Check
     -> Scope Check
     -> Dependency Check
     -> Idempotency Check
  -> Selected Execution Adapter
     -> Codex Adapter
     -> Human Delegation Adapter
     -> Git Adapter (future)
     -> Filesystem Adapter (future)
     -> MCP Adapter (future)
     -> GUI Adapter (future)
  -> Execution Result Envelope
  -> Evidence Validator / Reconciler
  -> Runtime Queue State Transition
```

## Responsibilities

Execution Adapter must:

- validate the execution request;
- confirm approval reference;
- confirm operation scope;
- confirm actor / tool capability;
- confirm explicit authority;
- confirm dependencies;
- record pre-execution state;
- execute or delegate to a human / external actor;
- return structured result;
- attach evidence;
- report retry and idempotency risk;
- preserve unknown, partial, failed, and blocked states honestly.

Execution Adapter must not:

- add unapproved operations;
- expand hidden scope;
- ignore missing authority;
- return completed without evidence;
- skip dependencies;
- infer human approval;
- turn failed or unknown results into success.

## Execution Adapter Router

The router chooses a target adapter only after:

```text
Human Approval
  -> Authority-Driven Responsibility Check
  -> Actor Capability
  -> Tool Availability
  -> Repository Boundary
  -> Operation Permission
  -> Credential Availability
  -> Execution Allowed
```

## Authority Outcomes

| Outcome | Meaning |
| --- | --- |
| `AUTHORIZED` | Actor and tool may execute the operation within approved scope. |
| `DELEGATION_REQUIRED` | Current actor cannot execute but can delegate. |
| `TOOL_UNAVAILABLE` | Required tool is not available. |
| `CREDENTIAL_UNAVAILABLE` | Required credential is missing. |
| `SCOPE_DENIED` | Requested operation is outside approved scope. |
| `APPROVAL_MISSING` | Approval reference is absent or invalid. |
| `AUTHORITY_UNKNOWN` | Authority cannot be proven; execution must stop. |

`AUTHORITY_UNKNOWN` is not safe to execute.

Authority-driven responsibility check:

```text
責務は機能ではなく、権限で決める。
```

If the selected actor can explain or review an operation but cannot execute or
delegate it through a governed adapter, it must not own the Approval Request or
Execution Evidence for that operation.

## Runtime Queue State Mapping

| Adapter Result | Evidence | Runtime Queue State |
| --- | --- | --- |
| `DELEGATED` | Not yet | `DELEGATED` |
| `WAITING_FOR_EVIDENCE` | Not yet | `WAITING_FOR_EVIDENCE` |
| `SUCCEEDED` | Complete and valid | `COMPLETED` |
| `SUCCEEDED` | Missing or invalid | `WAITING_FOR_EVIDENCE` or `SCW_REQUIRED` |
| `FAILED` | Failure evidence present | `FAILED` |
| `PARTIAL` | Partial evidence | `PARTIAL` or `SCW_REQUIRED` |
| `UNKNOWN` | Unknown | `SCW_REQUIRED` |
| `BLOCKED` | Block reason present | `BLOCKED` |

Runtime State Reconciler makes the final state decision. Adapter output alone
does not force `COMPLETED`.

## Reference Adapter Contracts

### Human Delegation Adapter

Used when AI lacks execution authority.

It returns:

- command or instruction;
- working directory;
- preconditions;
- expected evidence;
- failure reporting instructions.

Showing a command is not completion.

### Codex Execution Adapter

Used when Codex has repository access and explicit approval.

Required:

- target repository;
- scope;
- prohibited operations;
- approval reference;
- completion report;
- evidence.

### Git Commit Adapter Contract

Evidence:

- commit ID;
- commit message;
- changed file summary;
- exit status.

### Git Push Adapter Contract

Precondition:

- Commit queue item is `COMPLETED`.

Evidence:

- remote name;
- branch or ref;
- push result;
- remote commit confirmation when available.

### Git Tag Adapter Contract

Preconditions:

- tag policy satisfied;
- target commit identified;
- push requirement resolved.

Tag creation and tag push may be separate operations.

## Idempotency And Retry

Adapter result should report:

- retryable: yes / no / unknown;
- idempotency key;
- duplicate execution risk;
- safe retry condition;
- human review requirement.

Retry is a new execution attempt and should preserve evidence.

## SCW

Use Stop / Call / Wait when:

- approval reference is missing;
- scope is outside approval;
- actor authority is unknown;
- tool availability is unknown;
- credential is missing;
- dependency is incomplete;
- evidence requirement is unclear;
- output contract mismatches;
- result is partial or unknown;
- idempotency risk is unclear;
- repository boundary conflicts;
- GameGhost is unexpectedly touched;
- canonical artifact conflict exists.
