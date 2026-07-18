# AI Response Checklist v2

## Purpose

AI Response Checklist v2 は、AI がユーザーへ最終回答を出す直前に使う品質確認です。

目的は、成果物の実装や文書作成が終わった後に、回答そのものがルール、制約、
ユーザーの希望、実際の検証結果と一致しているかを確認することです。

## Checklist

### Startup / Context

- Startup Completion Evidence passed or limitation recorded:
- Repository Context Evidence supports this response:
- Startup evidence freshness still valid:
- Task-specific context refresh completed when needed:
- Required canonical assets opened:
- Unresolved canonical assets disclosed:
- Conversation context does not override repository truth:
- Capability disclosure checked, when capability was discussed:
- Current Q / user request answered:
- Target repository correct:
- Related repository boundary respected:

### Scope / Constraints

- Scope respected:
- Out of Scope avoided:
- Constraint Check still valid:
- Revision-first policy respected:
- Human Approval boundary respected:
- Commit / Push boundary respected:
- Execution Status shown before Repository Recommendation when repository action is relevant:
- Commit / Push / Tag status explicit:
- Suggested Commit Message clearly labeled as proposal when commit is not executed:
- Completed repository actions include Execution Evidence:
- Repository Recommendation values are Recommended / Hold / Not Applicable:
- Repository Recommendation avoids Approved:
- Safe Commit Set included when commit is recommended:
- Chat-facing final response includes Repository Recommendation when repository action is recommended:
- Chat-facing final response includes Workflow Recommendation when repository action is recommended:
- Chat-facing final response includes Approval Request when repository action is recommended:
- Required output sequence is Repository Recommendation -> Workflow Recommendation -> Approval Request:
- Current actor can execute the action before creating Approval Request:
- ChatGPT Completion Review does not create Commit Approval Request when Codex execution is required:
- ChatGPT Commit OK uses human-to-Codex Execution Instruction wording:
- Workflow Recommendation Current Step explicit:
- Workflow Recommendation values match approval state:
- Approval Request Current Step explicit:
- Approval Request Approval Units visible:
- Approval state checked before asking approval:
- Workflow Recommendation already served as Approval Request:
- Execution Instruction used after valid approval:
- Execution Instruction audience is Human:
- Next human action explicit:
- Duplicate Approval Request avoided:

### Output Format

- User-requested language respected:
- User-requested format respected:
- Reusable project artifact identified:
- Project Output Contract checked:
- Existing artifact revision checked:
- Inline text explicitly requested instead:
- Markdown artifact created or linked, when required:
- Chat contains summary only when artifact-first applies:
- Artifact paths / download links correct, when required:
- Commands shown in the correct shell style:
- File links / paths accurate:

### Evidence / Verification

- Changed Files accurate:
- Verification commands accurate:
- Not-run checks stated:
- Warnings distinguished from failures:
- Remaining Issues stated:
- Recommended Next Q stated when useful:
- Intended execution actor named when execution is instructed:
- Execution Evidence requirement stated when execution is instructed:
- Unapproved Approval Units remain Hold:

### Final Response

- No claim of commit / push unless actually done:
- No claim of tests passing unless actually run and passed:
- No hidden scope creep:
- No unverified capability claim:
- No unnecessary long quotation or copied artifact body:
- Final response ready:

## Gate Result

- PASS:
- PASS WITH LIMITATION:
- BLOCKED:
- Limitation / blocker:
