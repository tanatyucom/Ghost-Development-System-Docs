# AI Startup Procedure Rules

## Purpose

AI Startup Procedure は、AI が GDS 作業を始める前に読む順番と確認順を
標準化するルールです。

目的は AI を縛ることではなく、人間と AI が毎回同じ前提で安全に作業を
始められるようにすることです。

## Core Rule

AI は実装、レビュー、文書更新、Q 実行を始める前に、次の順番で前提を確認します。

```text
Intent-Driven Workflow, when the user starts from natural language intent
  -> Capability Verification, when capability is asked or uncertain
  -> AI Repository Index
  -> Daily Knowledge Source Review, when first major project work of the day
  -> Information Package, when provided
  -> Current Q File
  -> Repository Root Validation
  -> GDS Core Rules / Templates
  -> Target Project Profile
  -> Startup Checklist
  -> Startup Completion Evidence
  -> Startup Completion Gate
  -> Scope / Out of Scope
  -> Pending Decision Review, when pending decisions exist
  -> Conversation Insight Detection
  -> Memory Candidate Review, when memory candidates or lost context risk exist
  -> Pending Insight Review, when pending candidates exist
  -> Research Task Detection
  -> Normal Implementation / Review Start, when not research
  -> Research Mission, when research
```

この順番は、Q の内容を読む前に必要なすべての文書を丸暗記するためのものでは
ありません。対象リポジトリ、対象プロジェクト、適用ルール、作業範囲を
取り違えないための開始手順です。

## Repository-Aware AI Rule

When a canonical repository exists, AI must not use conversation memory alone
for repository-governed decisions.

AI must resolve the current canonical repository state and load the
task-relevant authoritative assets before planning, creating, revising,
reviewing, recommending, or executing repository work.

Decision precedence:

```text
Canonical Repository
  -> Current governed repository state
  -> Explicit current Human instruction within authority boundaries
  -> Session context
  -> Model memory / generic behavior
```

If repository access or a required canonical source is unavailable, AI must
record the limitation, apply SCW when needed, and avoid claiming Startup PASS
or repository-governed verification from memory.

## Required Checks

### Capability Verification

ユーザーが capability を問う場合、または repository、tool、permission、connected
service、current chat limitation が不明な場合、AI は計画前に capability を確認します。

AI は未検証の状態で `できます` と断定してはいけません。

Memory capability must not be summarized as only `Memory Available`. Startup
and Capability Verification should distinguish:

```text
Memory Capability:
- Read: PASS / UNAVAILABLE / UNKNOWN
- Write: PASS / UNAVAILABLE / UNKNOWN
```

Memory Read availability does not imply Memory Write availability. If Write is
unavailable, use repository-backed artifacts for durable knowledge capture.

Details follow `docs/workflow/capability_verification_first.md` and
`docs/rules/capability_disclosure_rule.md`.

### Intent-Driven Workflow

ユーザーが `続きやろう`、`何をやったらいい？`、`終わった`、
`お願いします`、`commitしていい？`、`pushしていい？`、`次は？` のような
自然言語で作業意図を示した場合、AI はその発言を直接実行コマンドとして扱わず、
Intent-Driven Workflow によって workflow selection、Recommendation、
Pending Action、Human Approval、SCW のいずれかへ分類します。

`お願いします`、`はい`、`OK` は、直前に一意な Pending Action が存在し、
repository、operation、scope、diff、state が変化していない場合だけ承認として
扱えます。

Details follow `docs/workflow/intent_driven_workflow.md`.

### AI Repository Index

公開 GDS knowledge を読む場合、最初に `docs/ai_repository_index.md` を確認します。

確認すること:

- 必要な Markdown 文書が Index に存在する。
- Raw URL または local path から対象文書へ辿れる。
- 新しい公開入口を追加した場合、Index を再生成・検証する。

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

これは Context Recovery Principle の実行入口です。新しい AI session が chat
memory ではなく repository source から現在地へ復帰できることを目的にします。

これは自動編集、自動Promotion、自動Q生成、自動実装、自動Commitの権限を
与えません。

### Pending Decision Review

Pending Decision は、conversation-approved but not-yet-canonical decision を
Startupで見失わないための一時review stateです。

これは新しい canonical knowledge layer ではありません。

Startupでは次を確認します。

- Pending Decision が存在するか。
- Current Project / Current Q と関連するか。
- Human Approval To Record があるか。
- Integration Target が明確か。
- conflict / obsolete / superseded 状態がないか。
- Next Action が integration / reject / supersede / archive / follow-up Q のどれか。

Pending Decision は review するだけです。Pending Decision の存在だけで、
implementation、canonical promotion、commit、push、tag、release を開始してはいけません。

Formal action requires the target workflow, Q, ADR, Rule, Workflow, Roadmap,
or other canonical integration path plus Human Approval.

### Information Package

Information Package が提供されている場合、Current Q と一緒に読みます。

確認すること:

- Current Status.
- Current Focus.
- Active Repository.
- Recent Decisions.
- Open Issues.
- Recent Artifacts.
- Recommended Next Q.
- Research Mission が必要な調査タスクか。

Information Package は Q File、Project Profile、rules を置き換えません。

### Current Q File

Current Q File で確認すること:

- Target Project
- Working Repository
- Single Source Of Truth
- Related Repository
- Scope Guard
- Do / Do Not
- Completion Criteria
- Commit policy
- Research Task Detection

Windows PowerShell 5.1 で Q File を読む場合は、必ず UTF-8 を明示します。

```powershell
Get-Content -LiteralPath <Q file> -Encoding UTF8
```

Plain `Get-Content` で表示された mojibake を、UTF-8検証なしにファイル破損として
扱ってはいけません。

Q が Artifact First 対象の場合、`docs/requests/` 配下の authoritative artifact を
確認します。Chat 本文だけを正式な作業入力として扱ってはいけません。

### Repository Root Validation

作業開始前に、宣言された Working Repository と実際の Git root が一致することを
確認します。

標準確認:

```bash
pwd
git rev-parse --show-toplevel
git status
```

Git root が Q の Working Repository と一致しない場合、編集、レビュー、commit を
開始してはいけません。

### GDS Core Rules / Templates

AI は対象作業に応じて GDS 共通ルール、workflow、template を確認します。

最低限の入口:

- `docs/rules/rules.md`
- `docs/rules/project_rules.md`
- `docs/rules/startup_checklist_rules.md`
- `docs/workflow/README.md`
- `templates/README.md`

作業内容に応じて Artifact First、Audit Before Repair、Debug Artifact Review、
Research Mission、Migration First、Completion Checklist などを追加で確認します。

### Target Project Profile

Target Project に Project Profile がある場合、Q 実行前に必ず読みます。

例:

```text
project_profiles/gameghost/README.md
```

Project Profile は Q File を置き換えません。Project Profile は安定した
プロジェクト前提を示し、Q File は今回の作業範囲を示します。

Project Profile と Q File が矛盾する場合は、作業を止めてユーザーに確認します。

### Startup Checklist

Startup Checklist は AI Startup Procedure の確認結果を、作業開始直前に
チェック可能な形へ落とし込む gate です。

確認すること:

- AI Repository Index read?
- Information Package read, when provided?
- Target Project identified?
- Project Profile read?
- Repository Root validated?
- Core Rules read?
- Current Q read?
- Scope / Out of Scope confirmed?
- Daily Knowledge Source Review done?
- Outstanding Review Notification needed?
- Pending Insight Review needed?
- Memory Candidate Review needed?
- Pending Decision Review needed?
- Related Knowledge Suggestions needed?
- Research Task detected?
- Session Health checked?

### Startup Completion Evidence

Startup Checklist の後、AI は確認した source と結果を短く証跡化します。

必須証跡:

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

AI memory、過去チャット、前回作業の印象は authoritative source ではありません。

Repository Context Evidence should include repository identity, git root or
repository root evidence, branch or revision when available, AI Repository
Index state, Current Q / Mission, canonical template source, related canonical
assets read, unresolved assets, conflict status, and freshness limitation.

Startup evidence must be refreshed or limited when repository state, task
type, workflow state, approval state, or Pending Action state changes.

### Startup Completion Gate

Startup Completion Evidence を確認し、Gate result を PASS / PASS WITH LIMITATION /
BLOCKED のいずれかで記録します。

BLOCKED の場合、Q creation、implementation、review、documentation update を
開始してはいけません。

Details follow `docs/workflow/startup_completion_evidence.md` and
`docs/workflow/startup_completion_gate.md`.

### Conversation Insight Detection

Scope / Out of Scope 確認後に、Conversation Insight Candidate があるかを判定します。

検出対象:

- 重要な設計思想。
- Platform思想。
- 開発理念。
- 運用方針。
- 保守方針。
- Migration戦略。
- Command Center構想。
- 長期運用方針。
- 将来構想。

AI が行うこと:

- Candidateとして提案する。
- Repositoryへ残す価値の理由を短く説明する。
- 既存Knowledgeとの重複可能性を確認する。
- 自動保存しない。
- チャット全文を保存しない。
- `書いといて`、`保存して`、`Repositoryへ追加`、`Q化して` などの
  明示承認後のみ Draft 生成へ進む。

Conversation Insight Draft は approved knowledge ではありません。保存後も、
正式Rule、Architecture、Workflow、Roadmap、Concept、CASEなどへ昇格するには
別途reviewとpromotion workflowが必要です。

Details follow `conversation_insight_capture_rules.md`.

### Memory Candidate Review

Conversation Insight Detection後、Memory、Q、Repository Knowledge、
Conversation Insightのどれへ進めるか未確定だが、失うと困る会話由来Knowledgeが
あるかを確認します。

確認すること:

- Lost Context Risk があるか。
- 既存MCまたは既存Knowledgeと重複しないか。
- Memory / Q / Repository Draft / Conversation Insight / Deferred / Reject の候補があるか。
- Human Approvalなしで保存、昇格、実装根拠化しようとしていないか。

Memory Candidate は canonical knowledge ではありません。実装、commit、
promotion の直接根拠として使ってはいけません。

Details follow `memory_candidate_rules.md`.

### Pending Insight Review

Pending Insight が存在する場合、Research Task Detection や通常実装へ進む前に
Human Review が必要か確認します。

確認すること:

- `docs/knowledge/conversation_insights/pending/` に候補があるか。
- 現在の作業と関連するか。
- Register / Q / Hold / Reject / Already Reflected の判断が必要か。
- Pending状態からCodex実行へ進もうとしていないか。
- 反映済みPendingのcleanup確認が必要か。

Details follow `pending_conversation_insight_review_rules.md`.

### Knowledge Suggestion Assistant

Startupまたは当日最初の適切なProject interactionで、関連Knowledgeを短く提案できます。

提案ブロック:

```text
Knowledge Suggestions:
- Outstanding Review:
- Pending Insight Review:
- Related Knowledge Suggestions:
- Promotion Candidates:
- Future Candidates:
```

Outstanding Review Notification は、未レビューKnowledgeの通知です。
Reviewed / Approved Knowledge の再提案とは区別します。

Reviewed / Approved Knowledge も、現在の会話、作業、Repository状況と高い関連性が
ある場合は再提案できます。

提案の優先順:

1. Current Context Relevance.
2. Immediate Risk / Blocker.
3. Promotion Opportunity.
4. Outstanding Review.
5. Important Knowledge not recently referenced.
6. Future Candidate readiness.

AIは提案のみ行います。Roadmap追加、Q化、Codex実装依頼、Rule化、
Architecture化、Workflow化、Archive、Reject、No Actionは人間が判断します。

Details follow `docs/architecture/context_aware_knowledge_suggestion_assistant.md`.

### Research Task Detection

Scope / Out of Scope 確認後に、Research Taskかどうかを判定します。

Research Task の代表例:

- 原因が未確定の調査。
- Root Cause確認。
- 仮説比較。
- Evidence collection。
- Knowledge gap分類。
- Debug / review結果から次の判断材料を集める作業。
- 実装前にFirst Broken Stepを特定する必要がある作業。

Research Taskではない場合、通常のimplementation / reviewへ進みます。

Research Taskの場合、`templates/research_mission_template.md` を読み、
Goal、Scope、Out of Scope、Required Evidence、Validation Method を確認してから
Research Mission Workflowへ進みます。

## Stop Conditions

次の場合は実装や文書更新を始めず、確認を求めます。

- Working Repository と actual Git root が一致しない。
- Target Project が不明。
- Project Profile が必要だが未確認。
- Q File と Project Profile が矛盾している。
- Related Repository が editable か reference only か不明。
- Scope / Out of Scope が曖昧。
- Conversation Insight Candidate を自動保存しようとしている。
- Conversation Insight Draft を Human Approvalなしで作ろうとしている。
- Memory Candidate を canonical knowledge、implementation authority、commit
  authority として扱おうとしている。
- Knowledge Suggestion Assistant が自動Promotion、自動Q生成、自動実装、
  自動Commitを行おうとしている。
- Research Task なのに Research Mission の Goal、Scope、Out of Scope、
  Evidence、Validation が不明。
- Commit policy が不明。
- Chat-only Q で、Artifact First 対象なのに保存先がない。
- repository-governed decision が必要なのに、現在のcanonical repository sourceを
  読まず、会話記憶や古い添付だけで判断しようとしている。
- repository state、task type、workflow state、approval state、Pending Action state
  の変化後にStartup evidenceを再確認していない。

## Decision Background

GDS は Startup Checklist、Repository Root Validation、AI Repository Index、
Project Profile、Q Artifact を持つようになりました。

しかし、これらを「どの順番で読むか」が曖昧だと、AI は正しい文書を持っていても
作業開始時に参照漏れを起こします。

AI Startup Procedure は、開始前の参照順を固定し、Repository 誤認、Scope drift、
Project Profile 読み漏れ、Q 欠落を防ぐための Knowledge Poka-Yoke です。

## Related Documents

- `docs/ai_repository_index.md`
- `docs/rules/utf8_read_rules.md`
- `docs/rules/external_source_access_rules.md`
- `docs/rules/startup_checklist_rules.md`
- `docs/rules/research_mission_rules.md`
- `docs/rules/conversation_insight_capture_rules.md`
- `docs/rules/memory_candidate_rules.md`
- `docs/rules/repository_root_validation_rules.md`
- `docs/rules/project_rules.md`
- `docs/workflow/ai_startup_procedure.md`
- `docs/workflow/research_mission_workflow.md`
- `docs/workflow/conversation_insight_capture_workflow.md`
- `docs/workflow/memory_candidate_workflow.md`
- `docs/architecture/context_aware_knowledge_suggestion_assistant.md`
- `docs/workflow/startup_checklist_workflow.md`
- `templates/research_mission_template.md`
- `templates/memory_candidate_template.md`
- `templates/information_package_template.md`
- `templates/startup_checklist_template.md`
- `project_profiles/README.md`
