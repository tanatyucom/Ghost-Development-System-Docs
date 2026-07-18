# Workflow Recommendation Examples

## Purpose

These examples show how ChatGPT should produce Workflow Recommendation after
Completion Review.

## Case 1: Normal Commit Approval Request

```text
Completion Review

Result:
PASS

Workflow Recommendation

Current Step:
Approval Request

Approval Units:
- Commit: Recommended
- Push: Hold
- Tag: Hold

Recommendation:
この変更はCommit可能です。

Next Human Action:
Commitを承認するか判断してください。
```

## Case 2: Human Approves Commit

```text
Workflow Recommendation

Current Step:
Execution Instruction

Approval Units:
- Commit: Approved
- Push: Hold
- Tag: Hold

Execution Instruction:
ChatGPTとしてはCommit OKです。

Commitする場合は、
人間側からCodexへCommit実行を依頼してください。
```

Do not ask `コミットしても良いですか？` again.

## Case 3: Human Approval Without Pending Request

```text
Workflow Recommendation

Current Step:
Stop

Approval Units:
- Commit: Hold
- Push: Hold
- Tag: Hold

Reason:
- No valid pending Approval Request exists.

Next Human Action:
承認対象を再表示してください。
```

## Case 4: Commit Approved, Push Not Approved

```text
Approval Units:
- Commit: Approved
- Push: Hold
- Tag: Hold
```

Commit approval must not approve Push.

## Case 5: Commit Completed, Push Recommendation

```text
Current Step:
Approval Request

Approval Units:
- Commit: Completed
- Push: Recommended
- Tag: Hold
```

`Completed` requires valid Commit Execution Evidence.

## Case 6: Repository Recommendation Hold

```text
Current Step:
Hold

Approval Units:
- Commit: Hold
- Push: Hold
- Tag: Hold

Reason:
- Codex Repository Recommendation is Hold.
- No new evidence overrides the hold.
```

## Case 7: Stale Repository Recommendation

```text
Current Step:
Stop

Approval Units:
- Commit: Hold
- Push: Hold
- Tag: Hold

Reason:
- Repository state changed after Codex recommendation.
- Re-review required.
```

## Case 8: Mixed Scope

```text
Current Step:
Hold

Approval Units:
- Commit: Hold
- Push: Hold
- Tag: Hold

Reason:
- Safe Commit Set is unclear.
- SCW required.
```

## Case 9: Incorrect Audience Wording

Invalid:

```text
Codex側でCommitを実行してください。
```

Correct:

```text
Commitする場合は、
人間側からCodexへCommit実行を依頼してください。
```

## Case 10: Duplicate Approval Prompt

Invalid:

```text
Workflow Recommendation
-> Human approval
-> Commitしても良いですか？
```

Correct:

```text
Workflow Recommendation
-> Human approval
-> Execution Instruction
```

## Case 11: Tag Independence

```text
Current Step:
Approval Request

Approval Units:
- Commit: Completed
- Push: Completed
- Tag: Recommended
```

Tag still requires separate Human approval.

## Case 12: Encoding Display False Positive

When Japanese Markdown appears corrupted in PowerShell, re-read with:

```powershell
Get-Content -LiteralPath <path> -Encoding UTF8
```

Do not report file corruption unless UTF-8-aware evidence confirms it.
