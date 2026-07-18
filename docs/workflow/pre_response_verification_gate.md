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
- Capability disclosure still matches actual work, when capability was discussed.
- Correct repository scope.
- Correct output format requested by the user.
- Reusable project artifact check completed.
- Project Output Contract respected.
- Markdown artifact path or download link provided when the Output Contract
  requires file delivery.
- Inline-only response is explicitly requested or justified as not reusable.
- User language preference respected.
- Git Bash / PowerShell command format appropriate for the context.
- Download link or artifact path format correct, when required.
- Revision-first policy respected.
- Human Approval boundary respected.
- Commit / Push boundary respected.
- Approval state checked before generating approval or execution wording.
- Whether Workflow Recommendation already served as the Approval Request.
- If Human Final Approval already exists for the current Approval Request, the
  response uses Execution Instruction instead of repeating the same Approval
  Request.
- Execution Instruction is addressed to the human and does not read as a direct
  ChatGPT-to-Codex command.
- Execution Instruction names the intended execution actor and required
  Execution Evidence.
- Unapproved Approval Units remain Hold.
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
- The response asks for the same approval again after valid Human Final
  Approval and no invalidation occurred.
- The response asks for approval again after the human approved a Workflow
  Recommendation that already served as the Approval Request.
- Execution Instruction is missing after valid Human Final Approval.
- Execution Instruction omits human-facing audience, intended actor, or evidence
  requirements.
- Unapproved Approval Units are promoted to Approved.
- Repository scope is unclear.
- The requested output format is not satisfied.
- A reusable project artifact is returned only as inline text without explicit
  user request.
- Known remaining issues are omitted.

## Required Output

Completion Report または最終回答前の内部確認として、次を確認します。

```text
Pre-Response Verification Gate:
- Gate result:
- Startup evidence checked:
- Scope check:
- Output format check:
- Output Contract check:
- Reusable artifact delivery:
- Human Approval boundary:
- Commit / Push boundary:
- Approval state:
- Workflow Recommendation served as Approval Request:
- Next output type:
- Duplicate approval request:
- Execution instruction audience:
- Execution instruction evidence:
- Constraint check:
- Final response ready:
```

If capability was discussed, the final response must not claim more capability
than was verified.

## Out Of Scope

- Automatic enforcement.
- Automatic correction.
- Repository mutation.
- Commit / Push.
- Startup redesign.

## Related Documents

- `templates/ai_response_checklist_v2.md`
- `docs/workflow/capability_verification_first.md`
- `docs/rules/capability_disclosure_rule.md`
- `templates/response_verification_checklist.md`
- `docs/workflow/startup_completion_evidence.md`
- `docs/workflow/startup_completion_gate.md`
- `docs/workflow/completion_checklist_workflow.md`
- `templates/completion_report_template.md`
- `templates/completion_checklist_template.md`
