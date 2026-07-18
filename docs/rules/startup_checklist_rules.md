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
- Memory Candidate Review.
- Pending Decision Review.
- Pending Insight Review.
- Knowledge Suggestion Assistant.
- Beginner & Future Self Test, when durable documentation or handoff quality is relevant.
- Startup Completion Evidence.
- Startup Completion Gate.
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
- Beginner & Future Self Test.

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
- Beginner & Future Self Test.

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
- Memory Candidates。
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

判断保留が望ましい会話由来の候補は、Pending Insight として扱えます。
Pending Insight は正式Knowledgeではなく、後日のHuman Reviewで扱いを決める候補です。

### Memory Candidate Review

Startupまたは当日最初の適切なProject interactionで、Memory Candidate の有無を確認します。

確認すること:

- 会話由来の知見に Lost Context Risk があるか。
- Memory、Q、Repository Knowledge、Conversation Insightのどれに進めるか未確定か。
- 既存MCまたは既存Knowledgeと重複しないか。
- Human Approvalなしで保存、昇格、実装根拠化していないか。
- Deferred Reviewへ回す必要があるか。

MCは正式Knowledgeではありません。Repository登録、Q化、Memory保存、Reject、
Duplicate、Deferred、Expiredなどの決定を経てからCloseします。

### Pending Insight Review

Startupまたは当日最初の適切なProject interactionで、Pending Insight の有無を確認します。

確認すること:

- `docs/knowledge/conversation_insights/pending/` に未解決候補があるか。
- 昨日または前回会話由来の候補か。
- Current Project と関連するか。
- 今レビューする価値があるか。
- Register / Q / Hold / Reject / Already Reflected のどれを選ぶか。
- Resolved Pending の cleanup 確認が必要か。

Pending Insight は Outstanding Review Notification の一種として扱います。
Daily Knowledge Source Review と重複させず、必要なときだけ短く通知します。

Pending状態ではCodex実行へ進みません。

### Pending Decision Review

Startupまたは当日最初の適切なProject interactionで、Pending Decision の有無を確認します。

Pending Decision は、conversation-approved but not-yet-canonical decision です。
これは正式Knowledgeではなく、Startupで見直すための一時decision recordです。

確認すること:

- Pending Decision が存在するか。
- Current Project / Current Q と関連するか。
- Human Approval To Record があるか。
- Integration Target が Rule / Workflow / Architecture / Roadmap / ADR / Q などへ
  明確か。
- Conflict Check が必要か。
- integrated / rejected / superseded / archived のどれへ進めるべきか。
- 別Qにするべきか。

Pending Decision は Repository First を置き換えません。正式な作業根拠にするには、
対象canonical artifactへ統合し、必要な Human Approval と Completion Report を経由します。

Pending Decision 状態では Codex execution、commit、push、tag、release へ進みません。

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

### Startup Completion Evidence

Startup Checklist の結果は、作業開始前に Startup Completion Evidence として
確認可能な証跡にします。

確認すること:

- Memory Check completed.
- Startup reviewed.
- AI Repository Index reviewed.
- Current Mission / Current Q reviewed.
- Canonical `templates/Q_TEMPLATE.md` reviewed, when Q creation or revision is involved.
- Related Rules reviewed.
- Related Workflows reviewed.
- Related ADRs / Architecture reviewed, when relevant.
- Constraint Check completed.

### Startup Completion Gate

Startup Completion Gate は、Startup Completion Evidence を確認してから
implementation / review / documentation update / Q creation へ進むための gate です。

Gate result:

- PASS: 必須証跡が揃っている。
- PASS WITH LIMITATION: 未確認事項の理由と次Actionが明記されている。
- BLOCKED: repository、Q、scope、commit policy、Human Approval などに重大な未確認または矛盾がある。

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
- Pending Insight Review:
- Pending Insight items:
- Pending Insight decision:
- Memory Candidate Review:
- Memory Candidate items:
- Memory Candidate decision:
- Lost Context Risk:
- Related Knowledge Suggestions:
- Conversation Insight Detection:
- Conversation Insight Candidate:
- Conversation Insight Draft approved:
- Research Task Detection:
- Research Mission required:
- Startup Completion Evidence:
- Startup Completion Gate:
- Missing startup evidence:
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
- `docs/workflow/startup_completion_evidence.md`
- `docs/workflow/startup_completion_gate.md`
- `docs/rules/ai_startup_procedure_rules.md`
- `docs/rules/research_mission_rules.md`
- `docs/rules/conversation_insight_capture_rules.md`
- `docs/rules/memory_candidate_rules.md`
- `docs/workflow/memory_candidate_operation_guide.md`
- `docs/architecture/context_aware_knowledge_suggestion_assistant.md`
- `templates/startup_checklist_template.md`
- `templates/startup_verification_checklist.md`
- `templates/research_mission_template.md`
- `templates/conversation_insight_template.md`
- `templates/memory_candidate_template.md`
- `templates/memory_candidate_review_checklist.md`
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
- `docs/workflow/memory_candidate_workflow.md`
- `docs/README.md`
