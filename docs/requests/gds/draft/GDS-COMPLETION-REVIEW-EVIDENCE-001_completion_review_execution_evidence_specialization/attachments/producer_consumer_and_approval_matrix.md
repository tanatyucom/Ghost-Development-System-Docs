# Producer / Consumer And Approval Matrix

## Producers

| Producer | Produces | Ownership Boundary |
| --- | --- | --- |
| Completion Report Workflow | Completion artifact and evidence summary. | Owns completion recording process. |
| Completion Checklist Workflow | Checklist state and completion readiness. | Owns final checklist flow. |
| Human reviewer | Approval or rejection. | Owns human approval decision. |
| AI-assisted completion review | Draft evidence and recommendation. | Does not execute Git actions. |
| Future Command Center adapter | Aggregated completion view. | Does not override review truth. |

## Consumers

| Consumer | Consumes | Required Behavior |
| --- | --- | --- |
| Human reviewer | Result, limitations, safe commit set, recommendations. | Decides approval. |
| Commit decision | Safe Commit Set and commit recommendation. | Must require explicit permission. |
| Command Center | Completion state and next action. | Must not auto-commit or auto-push. |
| Knowledge Promotion Engine | Lessons and promotion candidates. | Must require Human Approval before promotion. |
| Platform Ready Review | Compatibility across evidence layers. | Uses evidence for readiness. |

## Approval Matrix

| State | Meaning | Commit | Push |
| --- | --- | --- | --- |
| `not_required` | No approval needed for non-mutating next step. | Not enough by itself. | Not enough by itself. |
| `required` | Approval needed. | Wait. | Wait. |
| `pending` | Approval requested but unresolved. | Do not execute. | Do not execute. |
| `granted` | Scoped approval granted. | Execute only if scope matches. | Execute only if push scope matches. |
| `blocked` | Approval blocked. | Do not execute. | Do not execute. |
| `rejected` | Approval denied. | Do not execute. | Do not execute. |

## Approval Expiration

Approval expires when:

- changed files change;
- Safe Commit Set changes;
- Repository Quality result changes;
- verification result changes;
- target branch changes;
- Q policy changes;
- scope changes.
