# Git Execution Adapter Vertical Slice Workflow

**Status:** Draft Workflow

**Last Updated:** 2026-07-17

## Purpose

This workflow describes the documentation-level vertical slice from Human
Approval to Git Commit / Push / Tag evidence through GDS Core and governed Git
adapters.

## Commit Flow

```text
Completion Review PASS
  -> Approval Request
  -> Human Approval
  -> Intent Resolution
  -> Commit Queue Item
  -> Git Commit Adapter Request
  -> Authority / Scope / Dependency Check
  -> Execute or Delegate
  -> Commit Evidence
  -> Evidence Reconciliation
  -> Queue Item Completed or SCW
```

## Commit + Push Flow

```text
Commit Queue Item
  -> Commit Evidence Validated
  -> Push Queue Item Unblocked
  -> Git Push Adapter Request
  -> Remote / Branch / Authority Check
  -> Push Evidence
  -> Evidence Reconciliation
```

## Tag Flow

```text
Tag Policy Check
  -> Tag Create Queue Item
  -> Duplicate Tag Check
  -> Tag Create Evidence
  -> Optional Tag Push Queue Item
  -> Remote Push Evidence
```

Tag create and tag push may be separate operations.

## Actor Replacement

The same canonical request may be delegated to Human, Codex, or a future
adapter without changing GDS Core semantics.

## Failure Handling

| Condition | Result |
| --- | --- |
| Missing approval | Reject before adapter invocation. |
| AI lacks capability | Delegated / Waiting For Evidence. |
| Unexpected dirty scope | SCW Required. |
| Nothing to commit | Policy-based result; do not fabricate success. |
| Push authentication failure | Push Failed; Commit remains Completed. |
| Push unknown | Unknown + SCW; no automatic retry. |
| Duplicate tag different target | SCW Required. |
| Missing commit ID | Waiting For Evidence / Unknown. |
| Wrong repository | SCW before mutation. |

## Completion Report

Record:

- canonical package artifact;
- Core / AI / Adapter boundary;
- commit / push / tag execution status;
- test coverage;
- GameGhost untouched;
- validation results.
