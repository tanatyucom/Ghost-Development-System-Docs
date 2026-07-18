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
  -> Daily Knowledge Source Review
  -> Information Package Check, when provided
  -> Current Q Check
  -> Repository Root Validation
  -> Repository Confirmation
  -> Target Project Profile Confirmation
  -> Q / Artifact Confirmation
  -> Q ID / Naming Confirmation
  -> Q Template Required Fields Confirmation
  -> Applicable Rules Confirmation
  -> Applicable Methodologies Confirmation
  -> Beginner & Future Self Test Reminder, when durable documentation or
     handoff quality is relevant
  -> Scope / Out of Scope Confirmation
  -> Conversation Insight Detection
  -> Memory Candidate Review
  -> Pending Insight Review
  -> Knowledge Suggestion Assistant Check
  -> Research Task Detection
  -> Proactive Proposal Check
  -> Dirty Workspace / Commit Policy Confirmation
  -> Checklist Complete
  -> Startup Completion Evidence
  -> Startup Completion Gate
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

### Q ID / Naming Confirmation

Confirm:

- Q ID exists for official reusable Q artifacts.
- Filename follows `Q_<Q_ID>_<short_topic>_JP.md` when a simple file form is used.
- Task workspace follows `docs/requests/<project>/<status>/<Q_ID>_<short_topic>/` when a workspace is used.
- Date in filename is used only for snapshot, incident, release, migration, external event, or temporary handoff artifacts.
- Addendum versus new Q decision follows `docs/workflow/q_revision_addendum_workflow.md`.

### Q Template Required Fields Confirmation

Confirm:

- Repository Context is complete.
- Commit / Push Policy is explicit.
- Purpose, Background, Scope, and Out of Scope are separated.
- Existing Knowledge / Dependencies are reviewed.
- Deliverables and Validation are defined.
- AI Repository Index Update Gate is decided.
- Completion Report Requirements and Safe Commit Set are required.

### Applicable Rules Confirmation

作業内容に応じて確認する rules:

- `docs/rules/rules.md`
- `docs/rules/project_rules.md`
- `docs/rules/language_rules.md`
- `docs/rules/artifact_first_rules.md`
- `docs/rules/q_file_artifact_standard.md`
- `docs/rules/q_file_naming_rules.md`
- `docs/rules/q_file_template_rules.md`
- `docs/rules/audit_before_repair_rules.md`
- `docs/rules/debug_artifact_review_rules.md`
- `docs/rules/debug_escalation_ladder_rules.md`
- `docs/rules/migration_first_rules.md`
- `docs/rules/git_rules.md`

### Applicable Methodologies Confirmation

When the task creates or reviews durable documentation, roadmap, decision, Q,
Completion Report, handoff, README, or index artifacts, confirm whether the
Beginner & Future Self Test should be applied during review or completion.

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

判断保留が望ましい候補は Pending Insight として扱い、後日レビューへ回します。

### Memory Candidate Review

Conversation Insight Detection後、会話由来の重要な知見がMemory、Q、Repository
Knowledgeのどれにもまだ整理されていない場合は、Memory Candidateとして扱うかを
確認します。

確認する項目:

- Lost Context Risk。
- Existing MC duplicate。
- Promotion target候補。
- Human Approval needed。
- Deferred Review needed。

分岐:

```text
Memory Candidate: Not needed
  -> Continue startup checklist

Memory Candidate: Needed
  -> Capture as temporary MC
  -> Decide Memory / Q / Repository Draft / Deferred / Rejected / Duplicate later
```

MCはCanonical Knowledgeではありません。実装、Commit、Promotionの直接根拠には
使いません。

### Pending Insight Review

Startupまたは当日最初の適切なProject interactionで、
`docs/knowledge/conversation_insights/pending/` を確認します。

確認する項目:

- Pending items。
- Current Project relevance。
- Review now。
- Recommended action。
- Human decision。
- Cleanup needed。

分岐:

```text
Pending Insight: None
  -> Continue startup checklist

Pending Insight: Exists
  -> Notify briefly as Outstanding Review
  -> Human Review Decision
  -> Register Conversation Insight / Create Q / Keep Pending / Reject / Already Reflected
```

Pending状態ではCodex実行へ進みません。

### Knowledge Suggestion Assistant Check

Startupまたは当日最初の適切なProject interactionで、関連Knowledgeを短く提案できます。

確認する項目:

- Outstanding Review。
- Related Knowledge Suggestions。
- Promotion Candidates。
- Future Candidates。

Outstanding Review Notification と Reviewed / Approved Knowledge の
Context-Aware Re-Suggestion は区別します。

Reviewed / Approved Knowledge も、現在の会話、作業、Repository状況と高い関連性が
ある場合は再提案できます。

AI は提案のみ行い、Roadmap追加、Q化、Codex実装依頼、Rule化、Architecture化、
Workflow化、Archive、Reject、No Action は人間が判断します。

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

### Startup Completion Evidence

Checklist Complete の後、実装やレビューへ進む前に Startup Completion Evidence を
確認します。

確認すること:

- Memory Check が完了している。
- AI Repository Index、Current Q / Mission、関連 Rules / Workflows / ADRs が
  確認されている。
- Q 作成や revision の場合、canonical `templates/Q_TEMPLATE.md` が確認されている。
- Constraint Check が完了している。

Details follow `startup_completion_evidence.md`.

### Startup Completion Gate

Startup Completion Evidence を確認し、Gate result を PASS / PASS WITH LIMITATION /
BLOCKED のいずれかで記録します。

BLOCKED の場合、作業を開始せず、不足証跡または指示矛盾を解消します。

Details follow `startup_completion_gate.md`.

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
- Memory Candidate:
- Pending Insight Review:
- Knowledge Suggestions:
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
- Memory Candidate Review が確認されている。
- Pending Insight Review が確認されている。
- Daily Knowledge Source Review が確認されている。
- Outstanding Review Notification と Related Knowledge Suggestions の要否が確認されている。
- Research Task の場合、Research Mission の入口が確認されている。
- Startup Completion Evidence が確認されている。
- Startup Completion Gate が PASS または PASS WITH LIMITATION になっている。
- Commit policy が確認されている。
- Checklist 完了後に implementation / review を開始できる。

## Related Documents

- `docs/rules/startup_checklist_rules.md`
- `docs/rules/ai_startup_procedure_rules.md`
- `docs/workflow/startup_completion_evidence.md`
- `docs/workflow/startup_completion_gate.md`
- `docs/workflow/ai_startup_procedure.md`
- `docs/rules/research_mission_rules.md`
- `docs/rules/conversation_insight_capture_rules.md`
- `docs/rules/pending_conversation_insight_review_rules.md`
- `docs/rules/memory_candidate_rules.md`
- `docs/workflow/memory_candidate_operation_guide.md`
- `docs/workflow/research_mission_workflow.md`
- `docs/workflow/conversation_insight_capture_workflow.md`
- `docs/workflow/pending_conversation_insight_review_workflow.md`
- `docs/workflow/memory_candidate_workflow.md`
- `docs/architecture/context_aware_knowledge_suggestion_assistant.md`
- `templates/research_mission_template.md`
- `templates/conversation_insight_template.md`
- `templates/pending_conversation_insight_template.md`
- `templates/memory_candidate_template.md`
- `templates/memory_candidate_review_checklist.md`
- `templates/information_package_template.md`
- `templates/startup_checklist_template.md`
- `templates/startup_verification_checklist.md`
- `examples/startup_checklist_examples.md`
- `docs/workflow/README.md`
- `docs/rules/rules.md`
- `docs/rules/project_rules.md`
- `docs/rules/repository_root_validation_rules.md`
- `docs/rules/ai_proactive_proposal_rules.md`
- `docs/rules/q_file_artifact_standard.md`
- `docs/rules/q_file_naming_rules.md`
- `docs/rules/q_file_template_rules.md`
- `docs/workflow/q_file_creation_workflow.md`
- `docs/workflow/q_revision_addendum_workflow.md`
- `docs/workflow/completion_report_workflow.md`
- `docs/workflow/commit_safety_checklist.md`
