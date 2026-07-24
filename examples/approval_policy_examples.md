# Approval Policy Examples

| Scenario | Result | Reason |
| --- | --- | --- |
| Read repository status during Startup. | `AUTO` | Read-only and required by an approved Q. |
| Create documentation in approved paths. | `AUTO` | Existing DOCUMENTATION_ONLY authority covers it. |
| Commit after a PASS where Commit is separate approval. | `PROMPT` | Reversible local mutation but a distinct approval unit. |
| Push exact approved commits to expected branch. | `PROMPT` | External synchronization requires a focused decision. |
| Generate an enriched follow-up. | `AUTO` | Documentation evidence inside approved completion scope. |
| Generate a Q draft from an enriched candidate. | `AUTO` | Draft creation grants no execution authority. |
| Normalize `C:/GitHub/X` to `C:\GitHub\X`. | `AUTO` | Safe, unique path representation correction. |
| Choose between two repositories with similar names. | `SCW_REQUIRED` | Repository identity affects boundary and authority. |
| Dirty workspace contains unrelated known files. | `AUTO` with warning | Preserve files and use an explicit Safe Commit Set. |
| Dirty workspace overlaps unknown ownership. | `SCW_REQUIRED` | Mutation safety cannot be determined. |
| Migration or repository boundary change. | `REQUIRED` | Material, high-impact scope change. |
| Release, Tag, destructive Git, or DB mutation. | `REQUIRED` | Irreversible or high-impact operation. |
| Optional GitHub access is unavailable. | `AUTO` with warning | It is not required for local documentation validation. |
| Handover supplies fresh branch and root context. | `AUTO` | Reuse with provenance; do not ask again. |
| A prompt requests repository context already present in fresh canonical evidence. | `AUTO` | Reuse and cite the source; repeated questioning fails the DX gate. |

## Low-friction Documentation Q

An Approved Q names a clean repository, documentation-only paths, and prohibited
Git mutations. Startup inspection, document generation, validation, enriched
follow-ups, and Safe Commit Set generation proceed as `AUTO`. Execution stops at
Completion Review because Commit remains prohibited.

## High-risk Required Case

A request proposes moving canonical artifacts to another repository. Even when
both roots are known and tools are available, repository-boundary change and
migration are `REQUIRED`. No context inheritance can convert that decision to
`AUTO`.
