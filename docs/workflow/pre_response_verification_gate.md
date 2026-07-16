# Pre-Response Verification Gate

## Purpose

Pre-Response Verification Gate は、AI が最終回答を出す直前に、出力内容が
canonical repository rules、ユーザーの運用慣習、現在の制約に合っているかを
確認する品質ゲートです。

Startup Completion Evidence が「作業開始前の確認」を担当するのに対し、
Pre-Response Verification Gate は「回答直前の確認」を担当します。

## Standard Flow

```text
Artifact Generation / Documentation Update
  -> Verification
  -> Completion Report / Completion Checklist, when required
  -> Pre-Response Verification Gate
  -> Final Response
```

## Required Checks

- Startup Completion Evidence passed or limitation recorded.
- Correct repository scope.
- Correct output format requested by the user.
- User language preference respected.
- Git Bash / PowerShell command format appropriate for the context.
- Download link or artifact path format correct, when required.
- Revision-first policy respected.
- Human Approval boundary respected.
- Commit / Push boundary respected.
- Scope creep check completed.
- Constraint Check still valid.
- Changed files and verification results are accurately reported.
- Remaining issues and not-run checks are not hidden.

## Gate Decision

### PASS

Final response may be delivered when all required checks pass or are
not applicable with a reason.

### PASS WITH LIMITATION

Final response may be delivered when a limitation exists but is clearly stated
and does not invalidate the answer.

Examples:

- A command was not run because it was out of scope.
- A check is not applicable to documentation-only work.
- Line-ending warnings exist but no diff check failure occurred.

### BLOCKED

Do not deliver a final response if:

- The response would claim unverified work was verified.
- The response would imply commit / push was done when it was not.
- Required Human Approval is missing.
- Repository scope is unclear.
- The requested output format is not satisfied.
- Known remaining issues are omitted.

## Required Output

Completion Report または最終回答前の内部確認として、次を確認します。

```text
Pre-Response Verification Gate:
- Gate result:
- Startup evidence checked:
- Scope check:
- Output format check:
- Human Approval boundary:
- Commit / Push boundary:
- Constraint check:
- Final response ready:
```

## Out Of Scope

- Automatic enforcement.
- Automatic correction.
- Repository mutation.
- Commit / Push.
- Startup redesign.

## Related Documents

- `templates/ai_response_checklist_v2.md`
- `templates/response_verification_checklist.md`
- `docs/workflow/startup_completion_evidence.md`
- `docs/workflow/startup_completion_gate.md`
- `docs/workflow/completion_checklist_workflow.md`
- `templates/completion_report_template.md`
- `templates/completion_checklist_template.md`
