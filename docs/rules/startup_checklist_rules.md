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

AI は Startup Checklist の前に AI Startup Procedure を使い、AI Repository
Index、Information Package when provided、Current Q File、Repository Root
Validation、GDS Core Rules / Templates、Target Project Profile を順に確認します。

最低限確認する項目:

- Working Repository.
- AI Repository Index.
- Daily Knowledge Source Review.
- Information Package, when provided.
- Target Project Profile.
- Repository Root Validation.
- Production repository / backup / reference-only repository.
- Current Phase.
- Current Goal.
- Applicable Rules.
- Applicable Methodologies.
- Conversation Insight Detection.
- Knowledge Suggestion Assistant.
- Research Task Detection.
- Repository Information.
- Q Format.
- Artifact / Download File Rule.
- Scope / Out of Scope.
- Commit policy.
- Proactive Proposal check.

## Required Checks

### Repository Check

作業開始前に、編集してよい repository と参照のみの repository を区別します。

確認すること:

- Target Project は何か。
- Working Repository はどこか。
- Single Source Of Truth は何か。
- Related Repository は editable / reference only / forbidden のどれか。
- GameGhost など関連 repository を誤って編集しないか。

### Repository Root Validation

作業開始前に実際の Git repository root を確認します。

標準コマンド:

```bash
pwd
git rev-parse --show-toplevel
git status
```

確認すること:

- Current Working Directory.
- Git repository root.
- Working Repository と Git root が一致しているか。
- Production Repository か。
- Backup / Reference Repository ではないか。
- `git status` が意図した repository の状態を示しているか。

Root が一致しない場合は implementation / review / commit を開始しません。

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
- Research Mission.
- Migration First.
- Dirty Workspace / Commit Safety.
- PIP Case Knowledge Base.
- Concept Promotion.
- Roadmap2 Knowledge Salvage.
- AI Proactive Proposal.
- Repository Root Validation.

### Methodology Check

作業内容に応じて適用する methodology を確認します。

代表例:

- First Broken Step Methodology.
- Research Mission.
- Trace Before Tune.
- Human Review Before Automation.
- Knowledge Before Automation.
- Evidence Feedback Loop.
- Knowledge Promotion.

### Proactive Proposal Check

AI は、作業前または作業中に改善案、時間短縮、repository / scope conflict、
rule conflict、methodology conflict、maintenance risk、knowledge opportunity を検知した場合、
勝手に実装変更せず、根拠つきで提案します。

確認すること:

- Better approach available?
- Significant time saving possible?
- Repository / Scope concern?
- Rule conflict?
- Methodology conflict?
- Knowledge opportunity detected?
- Any constructive concern?

### Daily Knowledge Source Review

少なくとも1日1回、主要なProject作業または重要な提案を行う前に、
Canonical Knowledge Sourceを確認します。

Canonical daily entry point:

```text
docs/ai_repository_index.md
```

Minimum targets:

- AI Repository Index。
- Current Information Package。
- Current Project Profile。
- Current Roadmap。
- Conversation Insights。
- Future Candidates。
- Research Missions。
- Improvement Records。
- Relevant CASE / Rule / Architecture / Workflow。

これは自動編集、自動Promotion、自動Q生成、自動実装、自動Commitの権限を
与えません。

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

### Conversation Insight Detection

Scope / Out of Scope確認後、通常実装やResearch Task Detectionへ進む前に、
Conversation Insight Candidateがあるかを確認します。

検出するもの:

- 重要な設計思想。
- 運用方針。
- 保守方針。
- Migration戦略。
- Command Center構想。
- 長期運用方針。
- 将来構想。

AI は、Repositoryへ残す価値が高い場合のみ Candidate として提案し、
保存価値の理由を短く説明します。

AI は自動保存してはいけません。チャット全文を保存してはいけません。
`書いといて`、`保存して`、`Repositoryへ追加`、`Q化して` などの
明示承認後のみ Draft 生成に進みます。

### Knowledge Suggestion Assistant

Startupまたは当日最初の適切なProject interactionで、関連Knowledgeを短く提案できます。

通知・提案対象:

- Outstanding Review。
- Related Knowledge Suggestions。
- Promotion Candidates。
- Future Candidates。

Outstanding Review Notification は未レビューKnowledgeの通知です。
Reviewed / Approved Knowledge の Context-Aware Re-Suggestion とは区別します。

Reviewed / Approved Knowledge も、現在の会話、作業、Repository状況と高い関連性が
ある場合は再提案できます。

AIは提案のみ行います。Roadmap追加、Q化、Codex実装依頼、Rule化、Architecture化、
Workflow化、Archive、Reject、No Action は人間が判断します。

### Research Task Detection

Scope / Out of Scope確認後、通常実装へ進む前にResearch Taskかどうかを判定します。

Research Task の代表例:

- 原因が未確定の調査。
- Root Cause確認。
- 仮説比較。
- Evidence collection。
- Knowledge gap分類。
- Debug / review結果から次の判断材料を集める作業。
- First Broken Step特定が必要な作業。

Research Taskではない場合、通常のimplementation / reviewへ進みます。

Research Taskの場合、`templates/research_mission_template.md` を読み、
Goal、Scope、Out of Scope、Required Evidence、Validation Methodを確認してから
Research Mission Workflowへ進みます。

## Startup Checklist Output

Startup Checklist の結果は、必要に応じて短く記録します。

推奨形式:

```text
Startup Checklist:
- AI Repository Index read:
- Information Package read:
- Target Project identified:
- Project Profile read:
- Repository confirmed:
- Core rules read:
- Current Q read:
- Scope confirmed:
- Applicable rules:
- Applicable methodologies:
- Daily Knowledge Source Review:
- Outstanding Review Notification:
- Related Knowledge Suggestions:
- Conversation Insight Detection:
- Conversation Insight Candidate:
- Conversation Insight Draft approved:
- Research Task Detection:
- Research Mission required:
- Q artifact status:
- Commit policy:
- Repository root validation:
- Session health:
- Proactive proposal:
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
- `docs/workflow/ai_startup_procedure.md`
- `docs/rules/ai_startup_procedure_rules.md`
- `docs/rules/research_mission_rules.md`
- `docs/rules/conversation_insight_capture_rules.md`
- `docs/architecture/context_aware_knowledge_suggestion_assistant.md`
- `templates/startup_checklist_template.md`
- `templates/research_mission_template.md`
- `templates/conversation_insight_template.md`
- `templates/information_package_template.md`
- `examples/startup_checklist_examples.md`
- `docs/rules/project_rules.md`
- `docs/rules/repository_root_validation_rules.md`
- `docs/rules/ai_proactive_proposal_rules.md`
- `docs/rules/artifact_first_rules.md`
- `docs/rules/q_file_artifact_standard.md`
- `docs/rules/git_rules.md`
- `docs/workflow/commit_safety_checklist.md`
- `docs/workflow/first_broken_step_methodology.md`
- `docs/workflow/research_mission_workflow.md`
- `docs/workflow/conversation_insight_capture_workflow.md`
- `docs/README.md`
