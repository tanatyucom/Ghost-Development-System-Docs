# Upstream Evidence Consumption

## Purpose

Completion Review consumes Startup Evidence and Repository Quality Evidence to decide whether the work can be treated as complete.

## Startup Evidence Consumption

Completion Review should inspect:

- evidence type;
- source request;
- target project;
- working repository;
- scope;
- result;
- reason codes;
- limitations;
- missing or conflicting evidence;
- allowed next step;
- blocked next step;
- SCW state.

## Startup Decision Matrix

| Startup Result | Completion Review Behavior |
| --- | --- |
| `PASS` | May proceed if scope matches. |
| `PASS_WITH_LIMITATION` | Carry limitation into Completion Review. |
| `BLOCK` | Completion Review usually becomes `BLOCK`. |
| `SCW_REQUIRED` | Completion Review becomes `SCW_REQUIRED` until resolved. |
| Missing when required | `PASS_WITH_LIMITATION`, `BLOCK`, or `SCW_REQUIRED` by task criticality. |

## Repository Quality Evidence Consumption

Completion Review should inspect:

- evidence type;
- assessed repository;
- assessed scope;
- freshness;
- quality state;
- gate result;
- warning count;
- error count;
- limitations;
- allowed next step;
- blocked next step.

## Repository Quality Decision Matrix

| Quality State | Completion Review Behavior |
| --- | --- |
| `Green` | Supports completion but does not approve commit/push. |
| `Yellow` | Completion may be `PASS_WITH_LIMITATION`; limitation must be visible. |
| `Red` | Completion should be `BLOCK` unless reviewing a scoped repair. |
| `Unknown` | Completion should be `SCW_REQUIRED` or `BLOCK`. |
| Stale | Re-audit, limitation, or SCW required. |

## Conflict Handling

If Startup Evidence, Repository Quality Evidence, Completion Report, or verification output disagree, Completion Review must not choose the convenient result silently.

Default behavior:

```text
evidence conflict -> SCW_REQUIRED
known failure -> BLOCK
known limitation -> PASS_WITH_LIMITATION
```
