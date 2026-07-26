# Q Creation Implementation Approval Examples

## Purpose

Show the boundary between approved-at-creation implementation, draft-only Qs,
and ambiguous intent.

| User intent | Result | Implementation |
| --- | --- | --- |
| `次のQファイルお願いします` | `APPROVED FOR IMPLEMENTATION` | Through Completion Review |
| `この結果を改善するQが欲しい` | `APPROVED FOR IMPLEMENTATION` | Through Completion Review |
| `レビュー用の草案だけ作って` | `DRAFT ONLY` | Prohibited |
| `Qにして。ただしまだ実装しない` | `DRAFT ONLY` | Prohibited |
| `これQにできる？` | Clarification or `SCW_REQUIRED` | Prohibited pending resolution |

In every row, Commit, Push, Tag, Release, Registry mutation, external effects,
and scope expansion remain unapproved.
