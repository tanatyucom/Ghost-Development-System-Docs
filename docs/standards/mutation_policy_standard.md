# Repository Mutation Policy Standard

**Version:** 1.0
**Status:** Adopted
**Effective Date:** 2026-07-24

| Authority | Meaning |
| --- | --- |
| `NONE` | No repository mutation; reads only and no generated side effects. |
| `DOCUMENTATION_ONLY` | Create or update only the documentation deliverables and paths named by the Q. |
| `SAFE` | Explicitly allowed, reversible, low-risk local mutations. |
| `NORMAL` | Bounded ordinary mutations with validation and recorded evidence. |
| `CONTROLLED` | Repository-state or externally visible mutations requiring governed approval. |
| `FULL` | Broad declared workflow authority, still bounded by repository, operation, capability, risk, and destructive-operation governance. |

The authority must be explicit for every repository, including `OUTPUT`. An
unspecified authority requires SCW. A broader technical permission never
expands the Q's authority. `FULL` never means unrestricted shell or destructive
permission. Force push, history rewrite, branch/tag deletion, bulk deletion,
runtime changes, database changes, and external writes require separate explicit
governance or remain prohibited.
