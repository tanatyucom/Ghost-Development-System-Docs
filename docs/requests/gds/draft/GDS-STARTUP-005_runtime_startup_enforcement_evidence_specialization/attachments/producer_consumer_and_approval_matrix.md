# Producer / Consumer And Approval Matrix

## Producer Matrix

| Producer | Produces | Ownership Boundary |
| --- | --- | --- |
| Runtime Startup Enforcement | Startup gate evidence, result, reason codes, missing evidence, allowed/blocked next step. | Owns Startup gate truth only. |
| Human-executed Startup workflow | Manual evidence when runtime implementation does not exist. | Must preserve parent field meaning. |
| Future Command Center adapter | Aggregated view or invocation wrapper. | Does not override domain evidence. |
| Future Template Engine preflight | Consumed Startup evidence reference. | Does not own Startup decision. |

## Consumer Matrix

| Consumer | Consumes | Required Behavior |
| --- | --- | --- |
| Template Engine | Result, allowed next step, template verification. | Must not generate when `BLOCK` or `SCW_REQUIRED`. |
| Artifact Pipeline | Startup evidence and pending action. | Must preserve limitation/block evidence in generated report. |
| Command Center | Evidence summary and status. | May orchestrate and display, but not replace approval. |
| Completion Review | Startup evidence, limitations, missing evidence, safe commit context. | Must surface non-PASS risk. |
| Repository Quality | Evidence completeness and references. | May warn on missing or incompatible evidence. |
| Human Reviewer | Approval state, SCW question, limitations. | Owns scoped approval decision. |

## Approval State Matrix

| `human_approval_state` | Meaning | Draft Allowed | Mutation Allowed |
| --- | --- | --- | --- |
| `not_required` | No human approval required for the next draft step. | Yes if result allows. | No. |
| `required` | Approval is required before the next action. | Depends on action. | No. |
| `pending` | Waiting for explicit decision. | No for blocked action. | No. |
| `granted` | Scoped approval was granted. | Yes within scope. | Only if explicitly granted for that mutation. |
| `blocked` | Approval path is blocked. | No. | No. |
| `rejected` | Approval was denied. | No. | No. |

## Human Approval Rules

- Evidence completeness is not approval.
- Quality Green is not approval.
- Previous chat approval must not be reused across changed scope, repository, target project, or operation.
- Approval must be scoped to the specific action.
- Commit / push / tag / release / delete / canonical promotion require explicit separate approval.

## SCW Rules

`SCW_REQUIRED` must include:

- what is unknown;
- why safe decision is impossible;
- what action is blocked;
- what human decision or evidence is required;
- how execution can resume.
