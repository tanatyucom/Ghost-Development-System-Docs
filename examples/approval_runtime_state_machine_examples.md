# Approval Runtime State Machine Examples

## Purpose

These examples show expected Approval Runtime behavior for approval binding,
state transitions, execution evidence, duplicate prevention, and SCW.

## Case 1: Normal Commit Lifecycle

```text
Recommended
-> Pending Human Approval
-> Approved
-> Execution Pending
-> Executing
-> Succeeded
-> Completed
```

`Completed` requires valid Commit Execution Evidence.

## Case 2: Generic Human Approval

One valid pending Commit Approval Request exists.

Human:

```text
お願いします
```

Expected:

- Commit becomes `Approved`;
- Push and Tag remain unchanged;
- no hidden unit is approved.

## Case 3: No Pending Request

Human:

```text
お願いします
```

Expected:

- no state transition;
- no Execution Instruction;
- SCW or clarification.

## Case 4: Multiple Pending Requests

Two valid Approval Requests exist.

Human:

```text
お願いします
```

Expected:

- ambiguous;
- no state transition;
- SCW.

## Case 5: Repository Changed Before Approval

Diff changes after Workflow Recommendation.

Expected:

- Approval Request becomes `Invalidated`;
- Human response cannot approve it;
- re-review required.

## Case 6: Repository Changed After Approval Before Execution

HEAD or Safe Commit Set changes after approval.

Expected:

- approved unit becomes `Invalidated`;
- Execution Instruction becomes stale;
- no execution.

## Case 7: Commit Approved, Push Held

Expected:

- Commit may proceed;
- Push remains `Not Requested` or `Hold`;
- no inferred Push approval.

## Case 8: Partial Approval

Commit and Push are visible as `Recommended`; human approves Commit only.

Expected:

- parent request becomes `Partially Approved`;
- Commit `Approved`;
- Push remains `Pending`;
- Tag unchanged.

## Case 9: Commit Execution Success

Valid Commit evidence includes SHA.

Expected:

- Commit execution state becomes `Succeeded`;
- Commit unit becomes `Completed`;
- parent request derives state from all child units.

## Case 10: Execution Failure

Commit command fails.

Expected:

- execution state becomes `Failed`;
- no `Completed` state;
- failure evidence recorded;
- Hold / re-review path.

## Case 11: Duplicate Human Approval

Commit is already `Approved`.

Human repeats:

```text
お願いします
```

Expected:

- no duplicate approval record with expanded scope;
- state remains `Approved`;
- existing Execution Instruction may be restated safely.

## Case 12: Duplicate Execution

Commit already succeeded, but execution is requested again.

Expected:

- detect existing successful evidence;
- do not create another Commit;
- return or reference existing evidence.

## Case 13: Unknown Execution Result

Command output is lost.

Expected:

- execution state becomes `Unknown`;
- inspect repository state;
- use SCW if completion cannot be proven;
- no blind retry.

## Case 14: Push Evidence

Push succeeds.

Expected:

- Push completed only;
- Tag remains independent.

## Case 15: Existing Conflicting Tag

Requested tag already exists on another Commit.

Expected:

- Tag `Hold`;
- SCW;
- no overwrite.

## Case 16: Superseded Request

A new Workflow Recommendation replaces an older pending one.

Expected:

- old request becomes `Superseded`;
- old approval wording cannot activate it;
- only new request remains pending.

## Case 17: UTF-8 Display Verification

Japanese Markdown appears corrupted under default PowerShell decoding.

Expected:

```powershell
Get-Content -LiteralPath <path> -Encoding UTF8
```

Do not declare corruption unless UTF-8-aware evidence confirms it.
