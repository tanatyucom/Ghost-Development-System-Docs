# Intent Phrase Resolution Matrix

| Phrase | Active Approval Required | Selected Scope | Follow-up Candidates | SCW Condition |
| --- | --- | --- | --- | --- |
| `お願いします` | Yes | Requested Operations only | Not selected | No active request or ambiguous request |
| `お願いします 次のQお願いします` | Yes for approval part | Requested Operations plus Next Q | Explicit Next Q selected | Requested Operation unclear |
| `これ全てお願いします` | Yes | All visible selectable items | Selected if visible | Visible scope not recoverable |
| `これ全てお願いします Tagだけ除外` | Yes | All visible selectable items except Tag | Selected except exclusion | Exclusion ambiguous or conflicts |

## Rule

Hidden candidates are never selected by `これ全て`.
