# Completion Checklist Examples

## Purpose

この文書は、Completion Checklist System の良い例と悪い例を示します。

Examples は参考資料です。正式なルールは
`docs/rules/completion_checklist_rules.md` に従います。

## Good Example: Documentation Task, No Commit

```text
Completion Checklist:
- Verification Completed: Yes, git diff --check passed
- Review Completed: Self-review completed, human review pending
- Completion Report Completed: Final response includes required sections
- Improvement Review Completed: Yes
- Commit Required: No, Q says do not commit
- Commit Executed: No
- Tag Required: No
- Tag Executed: No
- Release Required: No
- Release Published: No
- Recommended Next Q: Request workspace path reconciliation
- Workspace Clean Confirmation: Dirty workspace remains; safe commit set reported
```

良い理由:

- Commit Required と Commit Executed を分けている。
- Q の commit 禁止を守っている。
- workspace が clean ではないことを隠していない。
- Recommended Next Q がある。

## Good Example: Release Task

```text
Completion Checklist:
- Verification Completed: Yes
- Review Completed: Human approval received
- Completion Report Completed: Saved
- Improvement Review Completed: Yes
- Commit Required: Yes
- Commit Executed: Yes, abc1234
- Tag Required: Yes
- Tag Executed: Yes, v1.2.0
- Release Required: Yes
- Release Published: Yes, v1.2.0
- Recommended Next Q: Post-release review
- Workspace Clean Confirmation: Clean
```

良い理由:

- Commit、Tag、Release の必要性と実行結果が追跡できる。
- Human Approval を release 前提として記録している。

## Bad Example: Done Without End Check

```text
実装終わりました。
```

問題:

- Verification が不明。
- Completion Report が不明。
- Commit / Tag / Release の必要性が不明。
- 次の Q が不明。
- workspace clean 状態が不明。

## Bad Example: Commit Ambiguity

```text
多分 commit して大丈夫です。
```

問題:

- Commit Required と Commit Executed が分かれていない。
- safe commit set が不明。
- unrelated dirty files が混ざる可能性がある。

## Review Checklist

- Verification Completed が記録されているか。
- Review Completed が記録されているか。
- Completion Report Completed が記録されているか。
- Improvement Review Completed が記録されているか。
- Commit Required と Commit Executed が分離されているか。
- Tag Required と Tag Executed が分離されているか。
- Release Required と Release Published が分離されているか。
- Recommended Next Q があるか、不要理由があるか。
- Workspace Clean Confirmation または dirty state が記録されているか。
