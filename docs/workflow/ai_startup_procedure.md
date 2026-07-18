# AI Startup Procedure

## Purpose

AI Startup Procedure は、AI が GDS 作業を開始する前に読む順番と確認順を
定義する workflow です。

Startup Checklist が「開始直前のチェックリスト」なら、AI Startup Procedure は
「チェックリストへ進む前の読み込み手順」です。

## Standard Flow

```text
Start
  -> Intent-Driven Workflow, when the user starts from natural language intent
  -> Capability Verification, when capability is asked or uncertain
  -> AI Repository Index Check
  -> Daily Knowledge Source Review, when first major project work of the day
  -> Information Package Check, when provided
  -> Current Q File Check
  -> Repository Root Validation
  -> GDS Core Rules / Templates Check
  -> Target Project Profile Check
  -> Startup Checklist
  -> Startup Completion Evidence
  -> Startup Completion Gate
  -> Scope / Out of Scope Confirmation
  -> Pending Decision Review, when pending decisions exist
  -> Conversation Insight Detection
  -> Pending Insight Review, when pending candidates exist
  -> Research Task Detection
  -> Normal Implementation / Review Start, when not research
  -> Research Mission, when research
```

## Step Details

## Repository-Aware AI Principle

When a canonical repository exists, AI must not rely on conversation memory
alone for repository-governed decisions.

Before planning, creating, revising, reviewing, recommending, or executing
repository work, AI resolves the current canonical repository state, loads the
task-relevant authoritative assets, and bases the response on that evidence.

Precedence:

```text
Canonical Repository
  -> Current governed repository state
  -> Explicit current Human instruction within authority boundaries
  -> Session context
  -> Model memory / generic behavior
```

If a remembered rule, uploaded copy, or conversation summary conflicts with the
current canonical repository, the canonical repository wins. If the canonical
source cannot be resolved, apply SCW or record a visible limitation instead of
fabricating repository-governed output.

### 0. Capability Verification

ユーザーが「このAIでできるか」「このチャットで完了できるか」「このtoolを使えるか」
など capability を問う場合、または能力・権限・接続状態が不明な場合は、計画前に
Capability Verification First を実行します。

確認すること:

- Memory capability status:
  - Read: PASS / UNAVAILABLE / UNKNOWN.
  - Write: PASS / UNAVAILABLE / UNKNOWN.
- Repository accessibility.
- Tool availability.
- Commit / Push authority.
- Connected service availability.
- Current chat limitations.
- Alternative workflows when unavailable.

Details follow `capability_verification_first.md`.

### 0A. Intent-Driven Workflow

ユーザーが `続きやろう`、`何をやったらいい？`、`終わった`、
`commitしていい？`、`お願いします`、`次は？` のような自然言語で開始した場合、
AI はその発言を直接実行コマンドとして扱わず、Intent-Driven Workflow として
分類します。

確認すること:

- intent candidate。
- 対象 repository。
- conversation state。
- current Pending Action。
- Human Approval が必要な操作か。
- SCW 条件に該当しないか。

Details follow `intent_driven_workflow.md` and
`../architecture/intent_registry_and_pending_action_contract.md`.

### 1. AI Repository Index Check

公開 GDS knowledge を参照する場合、`docs/ai_repository_index.md` から開始します。

確認すること:

- 必要な文書が Index に登録されている。
- Raw URL または local path が使える。
- 新規 Markdown を追加する作業では、最後に Index 再生成が必要か確認する。

### 2. Daily Knowledge Source Review

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
- Pending Conversation Insights。
- Pending Decisions。
- Future Candidates。
- Research Missions。
- Improvement Records。
- Relevant CASE / Rule / Architecture / Workflow。

目的:

- AIの忘却対策。
- 古い前提の検出。
- Repository更新の把握。
- Chat移動後のContext復元。
- 現在作業と関連するKnowledgeの再発見。

これは Context Recovery Principle の実行入口です。AI が過去の会話を覚えている
ことではなく、repository source から現在地へ復帰できることを前提にします。

これは自動編集、自動Promotion、自動Q生成、自動実装、自動Commitの権限を
与えません。

### 2A. Pending Decision Review

Pending Decision は、会話で人間が承認したが、まだ canonical repository asset に
統合されていない一時的な decision record です。

Startup では、repository sync の後、Current Mission や開発開始の前に、
現在の作業と関連する Pending Decision がないかを確認します。

```text
Repository Sync
  -> Pending Decision Review
  -> Current Mission
  -> Development
```

確認すること:

- conversation-approved decision が未統合のまま残っていないか。
- Human Approval To Record があるか。
- integration target が Rule / Workflow / Architecture / Roadmap / ADR / Q のどれか。
- conflicting or obsolete decision がないか。
- status が pending / integrated / rejected / superseded / archived のどれか。
- Current Q で扱うべきか、別 Q にするべきか。

Pending Decision は canonical knowledge ではありません。実装、commit、push、
canonical promotion の根拠にするには、対象文書へ統合し、必要な Human Approval と
Completion Report を経由します。

### 3. Information Package Check

Information Package が提供されている場合、Current Q と一緒に確認します。

確認すること:

- Current Status.
- Current Focus.
- Active Repository.
- Recent Decisions.
- Open Issues.
- Recent Artifacts.
- Recommended Next Q.
- Research Mission が必要な調査タスクか。

Information Package は repository source of truth を置き換えません。現在状態の
briefing として扱い、Q、Project Profile、rules と矛盾する場合は確認します。

### 4. Current Q File Check

Q File から今回の作業範囲を確認します。

確認すること:

- Target Project
- Repository Information
- Scope Guard
- Do / Do Not
- Completion Criteria
- Commit policy
- Required artifacts
- Research Mission requirements, when the Q is investigation or hypothesis
  validation work

Windows PowerShell 5.1 で Q File を読む場合は、次の形式を使います。

```powershell
Get-Content -LiteralPath <Q file> -Encoding UTF8
```

Plain `Get-Content` の表示だけで文字化けやファイル破損を判断しません。

Q が Artifact First 対象の場合、保存済み Q artifact を authoritative source として
扱います。

### 5. Repository Root Validation

作業対象 repository を実測します。

```bash
pwd
git rev-parse --show-toplevel
git status
```

確認すること:

- Current Working Directory
- Actual Git root
- Expected Working Repository
- Production / backup / reference-only boundary
- Dirty workspace state

### 6. GDS Core Rules / Templates Check

最低限、次の入口を確認します。

- `docs/rules/rules.md`
- `docs/rules/project_rules.md`
- `docs/rules/startup_checklist_rules.md`
- `docs/workflow/README.md`
- `templates/README.md`

作業内容に応じて、次の文書を追加確認します。

- Artifact First / Q File Artifact Standard
- Audit Before Repair
- Debug Artifact Review
- Debug Escalation Ladder
- Research Mission
- Migration First
- Completion Checklist
- Commit Safety

### 7. Target Project Profile Check

Target Project に profile がある場合、対象 profile を読みます。

例:

```text
project_profiles/gameghost/README.md
```

確認すること:

- repository location
- edit boundary
- project-specific rules
- project-specific workflow
- AI context
- completion policy

### 8. Startup Checklist

読み込み結果を Startup Checklist に反映します。

最低限の確認:

```text
Startup Checklist:
- AI Repository Index read:
- Target Project identified:
- Project Profile read:
- Repository Root validated:
- Core Rules read:
- Current Q read:
- Daily Knowledge Source Review:
- Outstanding Review Notification:
- Pending Decision Review:
- Pending Insight Review:
- Related Knowledge Suggestions:
- Scope / Out of Scope confirmed:
- Session Health checked:
- Ready:
```

### 9. Startup Completion Evidence

Startup Checklist の後、作業開始前に Startup Completion Evidence を確認します。

確認すること:

- Memory Check completed.
- Memory Capability recorded:
  - Read: PASS / UNAVAILABLE / UNKNOWN.
  - Write: PASS / UNAVAILABLE / UNKNOWN.
- AI Startup Procedure reviewed.
- AI Repository Index reviewed.
- Current Mission / Current Q reviewed.
- Canonical `templates/Q_TEMPLATE.md` reviewed, when Q creation or revision is involved.
- Related Rules reviewed.
- Related Workflows reviewed.
- Related ADRs / Architecture reviewed, when relevant.
- Repository Root Validation completed.
- Constraint Check completed.

Details follow `startup_completion_evidence.md`.

### 10. Startup Completion Gate

Required evidence が揃っているかを確認し、Gate result を
PASS / PASS WITH LIMITATION / BLOCKED のいずれかで判断します。

Q 作成、implementation、review、documentation update は、この Gate の後に
開始します。

Details follow `startup_completion_gate.md`.

### 10A. Task-Specific Context Refresh

Startup is not only a session-opening ritual. It is refreshed when the
repository-governed context changes.

Use full Startup, incremental context refresh, or task-specific context
resolution when:

- task type changes, such as Architecture Review -> Q Creation ->
  Completion Review -> Approval Request -> Execution;
- repository files, generated indexes, or governed artifacts changed after the
  last Startup evidence;
- workflow state, approval state, or Pending Action state changed;
- a user reports that a response contradicts repository policy;
- the AI is about to use a template, rule, workflow, registry, or approval
  contract from memory;
- a required canonical source is missing, stale, or conflicting.

For refresh, record:

- trigger;
- sources re-checked;
- stale or conflicting context found;
- action taken;
- remaining limitation.

### 11. Scope / Out of Scope Confirmation

実装・レビュー・文書更新を始める直前に、今回触ってよい対象と触ってはいけない対象を
確認します。

特に確認すること:

- related repository は reference only か editable か。
- runtime code は scope に入っているか。
- generated artifacts を Git 管理対象にするか。
- commit してよい Q か。

### 12. Conversation Insight Detection

Scope確認後、今回の会話やQに Conversation Insight Candidate が含まれるか判定します。

検出対象:

- 重要な設計思想。
- 運用方針。
- 保守方針。
- Migration戦略。
- Command Center構想。
- 長期運用方針。
- 将来構想。

判定:

```text
Conversation Insight Candidate: No
  -> Continue startup flow

Conversation Insight Candidate: Yes
  -> Propose candidate
  -> Explain repository value briefly
  -> Check duplicate knowledge
  -> Wait for Human Approval To Draft
```

AI は自動保存せず、チャット全文も保存しません。`書いといて`、`保存して`、
`Repositoryへ追加`、`Q化して` などの明示承認がある場合のみ、
`templates/conversation_insight_template.md` を使って Draft artifact を作成します。

Details follow `docs/rules/conversation_insight_capture_rules.md` and
`docs/workflow/conversation_insight_capture_workflow.md`.

### 11. Pending Insight Review

Pending Insight が存在する場合、Research Task Detection や通常実装へ進む前に
レビュー要否を確認します。

```text
Pending Insight: None
  -> Continue startup flow

Pending Insight: Exists
  -> Notify briefly
  -> Human Review decision
  -> Register / Q / Hold / Reject / Already Reflected
```

Pending状態ではCodex実行へ進みません。

Details follow `docs/rules/pending_conversation_insight_review_rules.md` and
`docs/workflow/pending_conversation_insight_review_workflow.md`.

### 12. Knowledge Suggestion Assistant Check

Startup may surface a short suggestion block when relevant.

```text
Knowledge Suggestions:
- Outstanding Review:
- Pending Insight Review:
- Related Knowledge Suggestions:
- Promotion Candidates:
- Future Candidates:
```

Outstanding Review Notification and reviewed Knowledge re-suggestion must be
distinguished.

Reviewed or Approved Knowledge may be suggested again when current context
relevance is high. The assistant explains the reason briefly and does not force
review, implementation, promotion, Q generation, or commit.

Details follow `docs/architecture/context_aware_knowledge_suggestion_assistant.md`.

### 13. Research Task Detection

Scope確認後、今回のタスクがResearch Missionへ分岐すべきか判定します。

Research Task として扱う代表例:

- 原因が未確定の調査。
- Root Cause確認。
- 仮説比較。
- Evidence collection。
- Knowledge gap分類。
- Debug / review結果から次の判断材料を集める作業。
- 実装前にFirst Broken Stepを特定する必要がある作業。

判定:

```text
Research Task: No
  -> Normal Implementation / Review Start

Research Task: Yes
  -> Read or create Research Mission
  -> Confirm Goal / Scope / Out of Scope
  -> Confirm Required Evidence / Validation
  -> Research Mission Workflow
```

Research Task が Yes の場合、曖昧なまま実装へ進まず、
`templates/research_mission_template.md` と
`docs/workflow/research_mission_workflow.md` に従います。

## Stop Conditions

次の状態では Implementation / Review Start に進みません。

- Git root が Working Repository と一致しない。
- Project Profile が必要なのに読めていない。
- Q と Project Profile が矛盾している。
- Scope Guard が曖昧。
- Conversation Insight Candidate を自動保存しようとしている。
- Conversation Insight Draft を Human Approvalなしで作ろうとしている。
- Knowledge Suggestion Assistant が自動Promotion、自動Q生成、自動実装、
  自動Commitを行おうとしている。
- Research Task なのに Goal、Scope、Out of Scope、Evidence、Validation が不明。
- Commit policy が曖昧。
- authoritative Q artifact が必要なのに保存されていない。
- repository-governed decision が必要なのに、AI Repository Index、Current Q /
  Mission、canonical template、関連rule / workflow / ADRのいずれかを会話記憶だけで
  代替しようとしている。
- task type、repository state、workflow state、approval state の変化後に必要な
  context refresh を行っていない。

## Relationship To Startup Checklist

AI Startup Procedure:

- 読む順番を決める。
- 参照漏れを防ぐ。
- Project Profile と Q File の前後関係を決める。

Startup Checklist:

- 読んだ結果をチェック項目として記録する。
- 実装開始前の gate として使う。
- 必要に応じて artifact として保存する。

## Related Documents

- `docs/ai_bootstrap_source_card.md`
- `docs/rules/ai_startup_procedure_rules.md`
- `docs/rules/startup_checklist_rules.md`
- `docs/workflow/startup_checklist_workflow.md`
- `docs/rules/repository_root_validation_rules.md`
- `docs/workflow/repository_root_validation_workflow.md`
- `docs/rules/external_source_access_rules.md`
- `docs/rules/utf8_read_rules.md`
- `docs/rules/research_mission_rules.md`
- `docs/rules/conversation_insight_capture_rules.md`
- `docs/workflow/research_mission_workflow.md`
- `docs/workflow/conversation_insight_capture_workflow.md`
- `docs/architecture/context_aware_knowledge_suggestion_assistant.md`
- `templates/research_mission_template.md`
- `templates/conversation_insight_template.md`
- `docs/ai_repository_index.md`
- `project_profiles/README.md`
- `templates/startup_checklist_template.md`
