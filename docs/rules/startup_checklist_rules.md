# Startup Checklist Rules

## Purpose

Startup Checklist は、新しい ChatGPT / Codex / AI セッション開始時に、
GDS の運用ルール、Methodology、Repository Information、Scope Guard を
短時間で再確認するための起動ルールです。

このルールは既存ルールを置き換えません。既存ルールを必要なタイミングで
思い出し、適切に適用するための入口です。

## Core Rule

実装、レビュー、文書更新、Q 実行を開始する前に、AI と人間は
Startup Checklist を確認します。

最低限確認する項目:

- Working Repository.
- Production repository / backup / reference-only repository.
- Current Phase.
- Current Goal.
- Applicable Rules.
- Applicable Methodologies.
- Repository Information.
- Q Format.
- Artifact / Download File Rule.
- Scope / Out of Scope.
- Commit policy.

## Required Checks

### Repository Check

作業開始前に、編集してよい repository と参照のみの repository を区別します。

確認すること:

- Target Project は何か。
- Working Repository はどこか。
- Single Source Of Truth は何か。
- Related Repository は editable / reference only / forbidden のどれか。
- GameGhost など関連 repository を誤って編集しないか。

### Rule Check

作業内容に応じて適用する rules を確認します。

代表例:

- Project First Principle.
- Japanese First.
- Artifact First.
- Q File Artifact Standard.
- Audit Before Repair.
- Debug Artifact Review.
- Debug Escalation Ladder.
- Migration First.
- Dirty Workspace / Commit Safety.
- PIP Case Knowledge Base.
- Concept Promotion.
- Roadmap2 Knowledge Salvage.

### Methodology Check

作業内容に応じて適用する methodology を確認します。

代表例:

- First Broken Step Methodology.
- Trace Before Tune.
- Human Review Before Automation.
- Knowledge Before Automation.
- Evidence Feedback Loop.
- Knowledge Promotion.

### Q Artifact Check

Q が長文、再利用対象、レビュー対象、Git 管理対象、AI handoff 対象の場合は、
Artifact First と Q File Artifact Standard に従います。

確認すること:

- Q は `docs/requests/` 配下の Task Artifact Workspace に保存されているか。
- `request.md` が実装前に存在するか。
- completion report の保存先が決まっているか。
- Chat 本文だけが authoritative source になっていないか。

### Scope Check

実装前に Scope / Out of Scope を確認します。

確認すること:

- 編集対象ファイルは明確か。
- runtime code が out of scope の場合、変更されないか。
- backup / generated / debug artifact を誤って正規成果物にしないか。
- commit 禁止の Q で commit しないか。

## Startup Checklist Output

Startup Checklist の結果は、必要に応じて短く記録します。

推奨形式:

```text
Startup Checklist:
- Repository confirmed:
- Scope confirmed:
- Applicable rules:
- Applicable methodologies:
- Q artifact status:
- Commit policy:
- Ready to start:
```

長い checklist が必要な場合は、チャット本文ではなく file artifact として
保存します。

## Decision Background

長期開発では、AI セッションや人間の作業開始時に重要なルールを忘れることが
あります。Knowledge Base にルールが存在していても、必要な瞬間に参照されない
場合、scope drift、repository 混同、Q 欠落、commit 事故、未確認の修復作業が
発生します。

Startup Checklist は、既存 Knowledge を増やすためではなく、既存 Knowledge を
起動時に確実に呼び出すための仕組みです。

## Related Documents

- `docs/workflow/startup_checklist_workflow.md`
- `templates/startup_checklist_template.md`
- `examples/startup_checklist_examples.md`
- `docs/rules/project_rules.md`
- `docs/rules/artifact_first_rules.md`
- `docs/rules/q_file_artifact_standard.md`
- `docs/rules/git_rules.md`
- `docs/workflow/commit_safety_checklist.md`
- `docs/workflow/first_broken_step_methodology.md`
- `docs/README.md`
