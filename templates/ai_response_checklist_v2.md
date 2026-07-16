# AI Response Checklist v2

## Purpose

AI Response Checklist v2 は、AI がユーザーへ最終回答を出す直前に使う品質確認です。

目的は、成果物の実装や文書作成が終わった後に、回答そのものがルール、制約、
ユーザーの希望、実際の検証結果と一致しているかを確認することです。

## Checklist

### Startup / Context

- Startup Completion Evidence passed or limitation recorded:
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

### Output Format

- User-requested language respected:
- User-requested format respected:
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

### Final Response

- No claim of commit / push unless actually done:
- No claim of tests passing unless actually run and passed:
- No hidden scope creep:
- No unnecessary long quotation or copied artifact body:
- Final response ready:

## Gate Result

- PASS:
- PASS WITH LIMITATION:
- BLOCKED:
- Limitation / blocker:
