# AI Response Checklist v2

## Purpose

AI Response Checklist v2 は、AI がユーザーへ最終回答を出す直前に使う品質確認です。

目的は、成果物の実装や文書作成が終わった後に、回答そのものがルール、制約、
ユーザーの希望、実際の検証結果と一致しているかを確認することです。

## Checklist

### Startup / Context

- Startup Completion Evidence passed or limitation recorded:
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
- Repository Recommendation values are Recommended / Hold / Not Applicable:
- Repository Recommendation avoids Approved:
- Safe Commit Set included when commit is recommended:
- Approval state checked before asking approval:
- Workflow Recommendation already served as Approval Request:
- Execution Instruction used after valid approval:
- Execution Instruction audience is Human:
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
