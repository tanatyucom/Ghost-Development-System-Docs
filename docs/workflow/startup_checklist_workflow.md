# Startup Checklist Workflow

## Purpose

Startup Checklist Workflow は、新しい AI セッション、Codex 実行、
レビュー、文書更新、Q 実装を開始する前に、GDS の前提を確認する標準フローです。

目的は、新しいルールを増やすことではなく、既存の Rules、Workflow、
Methodology、Repository Information を開始時に確実に思い出すことです。

## Standard Flow

```text
Start
  -> AI Startup Procedure
  -> AI Repository Index Check
  -> Information Package Check, when provided
  -> Current Q Check
  -> Repository Root Validation
  -> Repository Confirmation
  -> Target Project Profile Confirmation
  -> Q / Artifact Confirmation
  -> Applicable Rules Confirmation
  -> Applicable Methodologies Confirmation
  -> Scope / Out of Scope Confirmation
  -> Conversation Insight Detection
  -> Research Task Detection
  -> Proactive Proposal Check
  -> Dirty Workspace / Commit Policy Confirmation
  -> Checklist Complete
  -> Normal Implementation / Review Start, when not research
  -> Research Mission, when research
```

## Step Details

### AI Startup Procedure

Startup Checklist の前に、AI は AI Startup Procedure に従い、
AI Repository Index、Information Package when provided、Current Q File、
Repository Root Validation、GDS Core Rules / Templates、Target Project
Profile を順に確認します。

Details follow `ai_startup_procedure.md`.

### Information Package Check

Information Package が提供されている場合は、Qと合わせて現在状態を確認します。

確認すること:

- Current Status.
- Current Focus.
- Active Repository.
- Recent Decisions.
- Open Issues.
- Recent Artifacts.
- Recommended Next Q.
- Research Taskかどうか。

### AI Repository Index Check

公開 GDS knowledge を使う場合は `docs/ai_repository_index.md` を開始点にします。

確認すること:

- Index read.
- Required document found.
- Raw URL or local path usable.
- Index regeneration needed after this Q.

### Repository Root Validation

作業開始前に、現在の shell が正しい Git repository root にいるか確認します。

```bash
pwd
git rev-parse --show-toplevel
git status
```

確認する項目:

- Current Working Directory.
- Git repository root.
- Expected Working Repository.
- Root matches Working Repository.
- Production Repository.
- Backup / Reference Repository.
- Safe to start.

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

### Target Project Profile Confirmation

Target Project に Project Profile がある場合は、Q 実行前に読みます。

確認すること:

- Project Profile path.
- Repository and edit boundary.
- Project-specific rules.
- Project-specific workflow.
- AI context.
- Completion policy.
- Conflict with Q.

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
- Research Mission.
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

### Conversation Insight Detection

Scope / Out of Scope確認後、Conversation Insight Candidateがあるかを判定します。

検出対象:

- 重要な設計思想。
- 運用方針。
- 保守方針。
- Migration戦略。
- Command Center構想。
- 長期運用方針。
- 将来構想。

分岐:

```text
Conversation Insight Candidate: No
  -> Continue startup checklist

Conversation Insight Candidate: Yes
  -> Propose candidate
  -> Explain repository value briefly
  -> Do not auto-save
  -> Wait for explicit Human Approval To Draft
```

明示承認の例:

- `書いといて`
- `保存して`
- `Repositoryへ追加`
- `Q化して`
- `Conversation Insightとして残して`

AI はチャット全文を保存しません。Draftはapproved knowledgeではなく、
Promotionには別途reviewと該当workflowが必要です。

### Research Task Detection

Scope / Out of Scope確認後、通常実装へ進む前にResearch Taskかどうかを判定します。

Research Task の代表例:

- 原因が未確定。
- Root Cause確認。
- 仮説比較。
- Evidence collection。
- Knowledge gap分類。
- Debug / review結果から次の判断材料を集める作業。
- First Broken Step特定が必要。

分岐:

```text
Research Task: No
  -> Normal Implementation / Review Start

Research Task: Yes
  -> Read/Create Research Mission
  -> Goal / Scope / Out of Scope
  -> Evidence / Validation
  -> Research Mission Workflow
```

Research Task が Yes の場合は、`templates/research_mission_template.md` を使い、
Goal、Scope、Out of Scope、Required Evidence、Validation Methodを明示してから
調査を開始します。

### Proactive Proposal Check

AI は、より安全または短い進め方、repository / scope conflict、rule conflict、
methodology conflict、maintenance risk、knowledge opportunity を検知した場合、
勝手に実装変更せず、根拠と影響を添えて提案します。

## Minimal Startup Checklist

短い作業では、以下の最小形式でよいです。

```text
Startup Checklist:
- AI index:
- Project profile:
- Repository:
- Root:
- Scope:
- Rules:
- Methodology:
- Q artifact:
- Proposal:
- Conversation Insight:
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
- Research Task Detection が確認されている。
- Conversation Insight Detection が確認されている。
- Research Task の場合、Research Mission の入口が確認されている。
- Commit policy が確認されている。
- Checklist 完了後に implementation / review を開始できる。

## Related Documents

- `docs/rules/startup_checklist_rules.md`
- `docs/rules/ai_startup_procedure_rules.md`
- `docs/workflow/ai_startup_procedure.md`
- `docs/rules/research_mission_rules.md`
- `docs/rules/conversation_insight_capture_rules.md`
- `docs/workflow/research_mission_workflow.md`
- `docs/workflow/conversation_insight_capture_workflow.md`
- `templates/research_mission_template.md`
- `templates/conversation_insight_template.md`
- `templates/information_package_template.md`
- `templates/startup_checklist_template.md`
- `examples/startup_checklist_examples.md`
- `docs/workflow/README.md`
- `docs/rules/rules.md`
- `docs/rules/project_rules.md`
- `docs/rules/repository_root_validation_rules.md`
- `docs/rules/ai_proactive_proposal_rules.md`
- `docs/rules/q_file_artifact_standard.md`
- `docs/workflow/commit_safety_checklist.md`
