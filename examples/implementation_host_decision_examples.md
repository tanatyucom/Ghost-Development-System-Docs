# Implementation Host Decision Matrix and Scenarios

## Host Matrix

| Host | Responsibility | Isolation | Portability | Cost | Decision |
| --- | --- | --- | --- | --- | --- |
| GDS-DOCS | Poor: runtime contaminates canonical docs | Poor | Medium | Low initially | Rejected |
| GameGhost | Poor: application owns platform governance | Poor | Low | Low initially | Rejected |
| Dedicated GDS Runtime | Clear | High | High | Medium bootstrap | Selected as Planned |
| Existing Execution Platform | Potentially clear | Unknown | Unknown | Unknown | Unavailable; no verified repository |

## Runtime Matrix

| Runtime | YAML/Markdown/CLI/tests | Cross-platform | MCP affinity | Core complexity | Decision |
| --- | --- | --- | --- | --- | --- |
| Python | Strong | Strong | Adapter possible | Low | Selected core |
| TypeScript/Node.js | Strong | Strong | Strong | Medium | Future transport candidate |
| PowerShell | Medium | Windows-first | Low | Medium | Invocation adapter only |
| Mixed core | Strong | Variable | Strong | High | Rejected |

## Sixteen Scenarios

| # | Scenario | Result |
| --- | --- | --- |
| 1 | Implement in GDS-DOCS. | Reject responsibility contamination. |
| 2 | Implement in GameGhost. | Reject coupling and authority leakage. |
| 3 | Dedicated repository. | Select Planned host. |
| 4 | Repository not created. | Bootstrap REQUIRED; implementation blocked. |
| 5 | Runtime missing. | Python decision supplies architecture; exact version fixed at bootstrap. |
| 6 | Dependency install requested now. | Prohibited; separate approved Q required. |
| 7 | Shared core policy. | Place in inward-only core modules. |
| 8 | GameGhost adapter. | Separate adapter and separate Q. |
| 9 | MCP adapter. | Future transport only; core-independent. |
| 10 | Planned host used for execution. | BLOCK. |
| 11 | Mutation paths absent. | Implementation Q Incomplete. |
| 12 | Cross-repository consumer. | Versioned read-only contract/adapters. |
| 13 | Windows paths. | Fixture and normalization tests required. |
| 14 | Encoding regression. | UTF-8/LF and mojibake tests required. |
| 15 | Approval escalation. | Risk raises level; never auto-elevate authority. |
| 16 | Runtime/schema mismatch. | Compatibility check blocks execution. |
