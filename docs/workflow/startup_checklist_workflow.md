# Startup Checklist Workflow

## Purpose

Startup Checklist Workflow は、新しい AI セッション、Codex 実行、
レビュー、文書更新、Q 実装を開始する前に、GDS の前提を確認する標準フローです。

目的は、新しいルールを増やすことではなく、既存の Rules、Workflow、
Methodology、Repository Information を開始時に確実に思い出すことです。

## Standard Flow

```text
Start
  -> Repository Confirmation
  -> Q / Artifact Confirmation
  -> Applicable Rules Confirmation
  -> Applicable Methodologies Confirmation
  -> Scope / Out of Scope Confirmation
  -> Dirty Workspace / Commit Policy Confirmation
  -> Checklist Complete
  -> Implementation / Review Start
```

## Step Details

### Repository Confirmation

確認する項目:

- Target Project.
- Working Repository.
- Documentation Root.
- Runtime Root, when needed.
- Single Source Of Truth.
- Related Repository.
- Cross Project Impact.
- Scope Guard.

### Q / Artifact Confirmation

確認する項目:

- Q が Artifact First 対象か。
- Q が `docs/requests/` 配下に保存済みか。
- `request.md` が存在するか。
- completion report の保存先が決まっているか。
- 添付ファイル、download file、外部 artifact が参照のみか編集対象か。

### Applicable Rules Confirmation

作業内容に応じて確認する rules:

- `docs/rules/rules.md`
- `docs/rules/project_rules.md`
- `docs/rules/language_rules.md`
- `docs/rules/artifact_first_rules.md`
- `docs/rules/q_file_artifact_standard.md`
- `docs/rules/audit_before_repair_rules.md`
- `docs/rules/debug_artifact_review_rules.md`
- `docs/rules/debug_escalation_ladder_rules.md`
- `docs/rules/migration_first_rules.md`
- `docs/rules/git_rules.md`

### Applicable Methodologies Confirmation

作業内容に応じて確認する methodology:

- First Broken Step Methodology.
- Trace Before Tune.
- Human Review before broad repair or adoption.
- Knowledge Before Automation.
- Evidence Feedback Loop.
- Concept Promotion.
- PIP Case Knowledge Base.
- Roadmap2 Knowledge Salvage.

### Scope / Out of Scope Confirmation

確認する項目:

- 編集対象。
- 参照のみの repository。
- runtime code の扱い。
- generated artifact の扱い。
- Debug Artifact の Git policy。
- Commit policy。

## Minimal Startup Checklist

短い作業では、以下の最小形式でよいです。

```text
Startup Checklist:
- Repository:
- Scope:
- Rules:
- Methodology:
- Q artifact:
- Commit:
- Ready:
```

## Full Startup Checklist

長い Q、複数 repository、review artifact、debug artifact、repair、migration、
commit review を含む作業では `templates/startup_checklist_template.md` を使います。

## Chat Policy

チャットには checklist の要約だけを書きます。

Checklist 自体が再利用、レビュー、Git 管理対象になる場合は、file artifact として
保存します。

## Completion Criteria

- Working Repository が確認されている。
- Related Repository の編集可否が確認されている。
- Applicable Rules が確認されている。
- Applicable Methodologies が確認されている。
- Q Artifact / Download File の扱いが確認されている。
- Scope / Out of Scope が確認されている。
- Commit policy が確認されている。
- Checklist 完了後に implementation / review を開始できる。

## Related Documents

- `docs/rules/startup_checklist_rules.md`
- `templates/startup_checklist_template.md`
- `examples/startup_checklist_examples.md`
- `docs/workflow/README.md`
- `docs/rules/rules.md`
- `docs/rules/project_rules.md`
- `docs/rules/q_file_artifact_standard.md`
- `docs/workflow/commit_safety_checklist.md`
