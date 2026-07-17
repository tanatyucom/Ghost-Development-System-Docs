# Dogfooding Case Matrix

| Case | Human Input | Expected Runtime Resolution | Evidence Need |
| --- | --- | --- | --- |
| A | `お願いします` | Requested Operations only. | Depends on selected operation. |
| B | `お願いします 次のQお願いします` | Requested Operations plus Next Q chained intent. | Operation evidence plus artifact path. |
| C | `これ全てお願いします` | All visible selectable Requested Operations and Follow-up Candidates. | Evidence per queue item. |
| D | `これ全てお願いします Tagだけ除外` | All visible selectable items except Tag. | Evidence per remaining item. |

## Improvement Found

After approval, a plain list is not enough.

Required display includes:

- state;
- actor;
- dependency;
- evidence required;
- next action.
