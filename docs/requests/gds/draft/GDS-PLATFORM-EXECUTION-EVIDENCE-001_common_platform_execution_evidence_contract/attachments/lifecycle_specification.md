# Platform Execution Evidence Lifecycle Specification

## Lifecycle

```text
Observed
  -> Collected
  -> Classified
  -> Checked
  -> Decided
  -> Reviewed
  -> Consumed
  -> Archived
```

## State Meanings

| State | Meaning | Example |
| --- | --- | --- |
| `Observed` | A request, condition, check result, or review signal exists. | User asks to create a managed artifact. |
| `Collected` | Required source or check output was read or generated. | AI Repository Index or Quality Report read. |
| `Classified` | Evidence type and owner were identified. | `startup_gate` or `repository_quality`. |
| `Checked` | Required validation was performed. | `git diff --check` or template verification. |
| `Decided` | Gate or recommendation result was produced. | `PASS`, `BLOCK`, `Green`, `Yellow`. |
| `Reviewed` | Human or AI review evaluated the evidence. | Completion Report review. |
| `Consumed` | Downstream component used the evidence. | Command Center displays a pending action. |
| `Archived` | Evidence remains as history. | Completed request workspace. |

## Stop Conditions

- Missing producer.
- Missing consumer.
- Missing required check.
- Unknown Human Approval state.
- `SCW_REQUIRED`.
- Blocking result without recovery action.

## Completion Condition

Execution evidence is complete enough to consume only when the allowed next step
and blocked next step are both explicit.
