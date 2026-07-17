# Test Case Coverage

| Case | Result | Evidence |
| --- | --- | --- |
| Case 1: Commit Success | PASS | Commit requires valid approval, authority, execution, and commit ID evidence. |
| Case 2: Commit Claimed Without Evidence | PASS | Natural language without commit ID remains waiting for evidence. |
| Case 3: Push Before Commit | PASS | Push depends on completed commit evidence. |
| Case 4: Human Delegation | PASS | Human Delegation Adapter returns command, preconditions, and expected evidence. |
| Case 5: Scope Violation | PASS | Scope violation maps to SCW. |
| Case 6: Tool Unavailable | PASS | Tool unavailable maps to blocked or delegation required. |
| Case 7: Partial Tag Operation | PASS | Partial is not completed. |
| Case 8: Unknown Timeout | PASS | Unknown result maps to SCW. |
| Case 9: Bulk Approval Dependency Preservation | PASS | Dependencies remain even when operations are approved together. |
| Case 10: Duplicate Retry Risk | PASS | Idempotency risk requires review. |
| Case 11: Missing Approval Reference | PASS | Missing approval blocks execution. |
| Case 12: Evidence Contract Mismatch | PASS | Free text without required evidence cannot complete queue item. |
| Case 13: Candidate Follow-up Non-Execution | PASS | Undisclosed or unapproved candidates cannot execute. |
| Case 14: Canonical Artifact Conflict | PASS | Conflict maps to SCW. |
| Case 15: Failure Evidence | PASS | Failure evidence maps to failed, not completed. |

## Scope

These are documentation-level tests. Runtime code, Git Adapter, MCP, GUI, and
production execution tests are out of scope.
