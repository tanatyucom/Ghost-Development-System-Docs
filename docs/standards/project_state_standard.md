# Project State Standard

**Status:** Adopted
**Version:** 1.0

## Canonical States

| State | Meaning |
| --- | --- |
| `Active` | Approved work is currently progressing. |
| `Blocked` | Progress cannot continue until a named condition is resolved. |
| `Waiting` | Progress awaits a known external or Human event. |
| `Deprecated` | Retained for compatibility or history; no longer preferred. |
| `Cancelled` | Intentionally terminated; no automatic resume. |
| `Future Candidate` | Valuable possible work without current execution authority. |

Each state record contains subject, scope, effective date, owner, reason,
evidence, allowed next transitions, resume/exit conditions, and related Q or
decision. Project State does not encode approval implicitly.

`Blocked` requires a concrete blocker and resume requirement. `Waiting`
requires the awaited event. `Future Candidate` must not be treated as planned or
approved work. State conflicts use SCW.
