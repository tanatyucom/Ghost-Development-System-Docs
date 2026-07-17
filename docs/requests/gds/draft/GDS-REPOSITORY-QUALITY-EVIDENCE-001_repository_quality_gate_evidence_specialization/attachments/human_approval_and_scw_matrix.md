# Human Approval And SCW Matrix

## Human Approval Principle

Human Approval is independent from quality status.

```text
Quality Green is not approval.
Evidence completeness is not approval.
Report existence is not approval.
```

## Approval Matrix

| Quality State | Human Approval State | Meaning | Example |
| --- | --- | --- | --- |
| `Green` | `not_required` | Quality gate itself does not need approval for draft continuation. | Continue documentation draft. |
| `Green` | `required` | Next action needs approval even though quality is Green. | Commit recommendation. |
| `Yellow` | `pending` | Warning acceptance is awaiting human review. | Known warning before commit recommendation. |
| `Yellow` | `granted` | Human accepted a specific non-critical limitation. | Continue scoped docs work with limitation. |
| `Red` | `blocked` | Critical or blocking failure prevents action. | Encoding regression failure. |
| `Unknown` | `pending` | Human decision or missing evidence is needed. | Conflicting quality outputs. |

## Approval Must Record

- approver role;
- approved action;
- approval scope;
- repository state or revision;
- approval timestamp;
- evidence reference;
- conditions;
- expiration;
- revocation if applicable.

## Non-Overridable Without Dedicated Exception Policy

- failed critical check;
- missing required evidence for a required gate;
- stale evidence for commit recommendation;
- target revision mismatch;
- report/raw output conflict;
- unknown scan scope.

## SCW Matrix

| Situation | Result | SCW Reason |
| --- | --- | --- |
| Report says Green but raw validation shows failure. | `SCW_REQUIRED` | Evidence conflict. |
| Evidence targets a different revision. | `SCW_REQUIRED` | Target revision mismatch. |
| Scan scope is unclear for requested action. | `SCW_REQUIRED` | Scope unclear. |
| Audit tool failed because dependency is missing. | `SCW_REQUIRED` or `BLOCK` | Environment decision or repair needed. |
| Required file is known missing. | `BLOCK` | Known failure, not ambiguity. |

## SCW Evidence Must Include

- unknown condition;
- why safe decision is impossible;
- blocked action;
- required human answer or missing evidence;
- allowed diagnostic action;
- resume condition.
