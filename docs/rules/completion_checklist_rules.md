# Completion Checklist Rules

## Purpose

Completion Checklist は、作業完了時に確認漏れを防ぐための終了ルールです。

Startup Checklist が開始時の確認を担当するのに対して、Completion Checklist は
実装、検証、レビュー、完了報告、Improvement Review、commit / tag / release
判断、次の Q、workspace clean confirmation を終了時に確認します。

このルールは既存の Completion Report、Commit Safety、Human Approval Gate、
Release 判断を置き換えません。完了時にそれらを一貫して確認するための入口です。

## Core Rule

作業を完了扱いにする前に、Completion Checklist を確認します。

最低限確認する項目:

- Verification Completed.
- Review Completed.
- Completion Report Completed.
- Improvement Review Completed.
- Commit Required?
- Commit Executed?
- Tag Required?
- Tag Executed?
- Release Required?
- Release Published?
- Recommended Next Q.
- Workspace Clean Confirmation.

## Required Checks

### Verification Check

確認すること:

- 実行した verification は何か。
- 実行できなかった verification は何か。
- 失敗、未測定、未確認の項目が Remaining Issues に残っているか。
- Runtime / docs / artifact / generated output の scope が守られているか。

### Review Check

確認すること:

- 人間レビューが必要な作業か。
- Debug Artifact / Review Artifact がある場合、Review Entry Point があるか。
- Human Approval Gate が必要な判断を AI が勝手に確定していないか。
- Future Candidate と approved scope が混ざっていないか。

### Completion Report Check

確認すること:

- Source Q File が記録されているか。
- Changed Files が記録されているか。
- Verification が記録されているか。
- Improvement Review が記録されているか。
- Remaining Issues が記録されているか。
- Recommended Next Q が記録されているか。
- Suggested Commit Message が記録されているか。

### Commit / Tag / Release Check

確認すること:

- Commit が必要か。
- Q が commit 禁止なら commit していないか。
- Commit 済みなら commit hash と message が記録されているか。
- Tag が必要か。
- Tag 済みなら tag name が記録されているか。
- Release が必要か。
- Release 済みなら release name / version / URL が記録されているか。

### Workspace Clean Check

確認すること:

- `git status` を確認したか。
- Dirty workspace がある場合、safe commit set と unrelated files を分けたか。
- 生成物、debug artifact、temporary file、backup file を誤って commit 対象にしていないか。
- 作業後に残る dirty state を報告したか。

## Completion Checklist Output

Completion Checklist の結果は、Completion Report または最終報告に記録します。

推奨形式:

```text
Completion Checklist:
- Verification Completed:
- Review Completed:
- Completion Report Completed:
- Improvement Review Completed:
- Commit Required:
- Commit Executed:
- Tag Required:
- Tag Executed:
- Release Required:
- Release Published:
- Recommended Next Q:
- Workspace Clean Confirmation:
```

## Decision Background

作業完了時には、実装そのものは終わっていても、commit 判断、tag 判断、release 判断、
Completion Report、Improvement Review、次の Q、workspace clean confirmation が
会話ベースで曖昧になることがあります。

Completion Checklist は、作業を「終わったことにする」前に必要な終了確認を
一貫して行うための仕組みです。

## Related Documents

- `docs/workflow/completion_checklist_workflow.md`
- `templates/completion_checklist_template.md`
- `examples/completion_checklist_examples.md`
- `templates/completion_report_template.md`
- `templates/review_checklist.md`
- `docs/rules/git_rules.md`
- `docs/workflow/commit_safety_checklist.md`
- `docs/rules/startup_checklist_rules.md`
- `docs/workflow/startup_checklist_workflow.md`
