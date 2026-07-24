# Repository Role Definitions

**Version:** 1.0
**Status:** Adopted
**Effective Date:** 2026-07-24

| Role | Meaning | Default mutation |
| --- | --- | --- |
| `OUTPUT` | Stores the Q's governed deliverables. | Must be explicit in the Q. |
| `SOURCE` | Supplies vocabulary, specification, or implementation evidence. | `NONE` |
| `TARGET` | Future change target or subject of evaluation. | Must be explicit in the Q. |
| `VALIDATION` | Tests portability, compatibility, or reuse. | `NONE` |
| `REFERENCE` | Supplies supporting evidence only. | `NONE` |

Each repository declaration owns its own root, branch rule, working directory,
mutation policy, allowed operations, prohibited operations, and approval scope.
Repository identity or approval must not be inherited from another declaration.

`NONE` prohibits file creation, update, deletion, formatting, caches, test
artifacts, and Git mutation. If an inspection tool may create side effects, use
a side-effect-free alternative or SCW.
