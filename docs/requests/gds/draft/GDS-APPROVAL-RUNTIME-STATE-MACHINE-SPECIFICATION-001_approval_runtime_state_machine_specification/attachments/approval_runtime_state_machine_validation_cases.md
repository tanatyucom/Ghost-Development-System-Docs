# Approval Runtime State Machine Validation Cases

## Purpose

This attachment records the validation cases required by
`GDS-APPROVAL-RUNTIME-STATE-MACHINE-SPECIFICATION-001`.

The canonical reusable example set is:

- `examples/approval_runtime_state_machine_examples.md`

## Cases

| Case | Scenario | Expected Result | Covered By |
| --- | --- | --- | --- |
| 1 | Normal Commit lifecycle | Recommendation, approval, execution, evidence, and completion occur in order. | `Case 1` |
| 2 | Generic human approval with one valid Commit request | Approval binds to Commit only. Push and Tag remain unchanged. | `Case 2` |
| 3 | Generic human approval with no pending request | No transition. SCW or clarification. | `Case 3` |
| 4 | Generic human approval with multiple pending requests | Ambiguous. No transition. SCW. | `Case 4` |
| 5 | Repository changed before approval | Request invalidated. Re-review required. | `Case 5` |
| 6 | Repository changed after approval before execution | Approved unit invalidated. Execution instruction stale. | `Case 6` |
| 7 | Commit approved while Push is held | Commit may proceed. Push remains unapproved. | `Case 7` |
| 8 | Partial approval | Parent request becomes `Partially Approved`. | `Case 8` |
| 9 | Commit execution succeeds | Commit evidence completes Commit unit only. | `Case 9` |
| 10 | Execution failure | Execution state becomes `Failed`; Hold or re-review follows. | `Case 10` |
| 11 | Duplicate human approval | No scope expansion or duplicate approval mutation. | `Case 11` |
| 12 | Duplicate execution request | Existing successful evidence is reused; no duplicate mutation. | `Case 12` |
| 13 | Unknown execution result | State becomes `Unknown`; inspect evidence and apply SCW if needed. | `Case 13` |
| 14 | Push evidence | Push completes only; Tag remains independent. | `Case 14` |
| 15 | Existing conflicting tag | Tag enters Hold; no overwrite. | `Case 15` |
| 16 | Superseded request | Old request cannot be approved by later generic wording. | `Case 16` |
| 17 | UTF-8 display verification | Use UTF-8-aware read before declaring mojibake. | `Case 17` |

## Review Result

All required cases are represented in the example file. These are
documentation-level validation cases only and do not execute runtime code.
