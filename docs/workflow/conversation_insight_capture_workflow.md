# Conversation Insight Capture Workflow

## Purpose

Conversation Insight Capture Workflow は、長時間の設計議論、運用理念、
保守方針、将来構想など、通常の Q、Research Mission、CASE になりにくい重要な
会話由来の知見を、GDS Knowledge Source として保存するための標準 workflow です。

目的は、会話の熱量や一時的な感想をそのまま保存することではありません。Repositoryへ
残す価値がある insight を、人間の承認を通して Future Candidate または正式な
Rule / Architecture / Workflow へ昇格できる状態にすることです。

## Standard Flow

```text
Conversation
  -> Conversation Insight Candidate
  -> Pending Insight, when immediate decision should be deferred
  -> Pending Decision, when a conversation-approved decision is not yet canonical
  -> Human Approval To Draft
  -> Conversation Insight Artifact
  -> Review
  -> Future Candidate
  -> Rule / Architecture / Workflow / Roadmap / Concept / CASE
```

## Scope

対象:

- 設計思想。
- Platform思想。
- 開発理念。
- 保守方針。
- Migration戦略。
- Command Center構想。
- 長期運用方針。
- 将来構想。
- 既存RuleやWorkflowへ昇格する前の哲学的・運用的判断材料。

対象外:

- 日常雑談。
- 一時的な感想。
- 単なる雑談。
- 既存Knowledgeと重複する内容。
- 具体的な実装指示。
- Human ApprovalなしのRepository保存。

## AI Behavior

AI は、Repositoryへ残す価値が高いと判断した場合のみ
Conversation Insight Candidate を提案できます。

AI ができること:

- insight候補を短く提案する。
- なぜ保存価値があるか説明する。
- 既存Knowledgeとの重複可能性を指摘する。
- 保存先候補を提案する。
- 判断保留が望ましい場合、Pending Insight 化を提案する。
- 人間が依頼した場合のみ draft artifact を作る。

AI がしてはいけないこと:

- 自動保存。
- 会話の全文保存。
- Human ApprovalなしのRule化。
- 雑談や一時感情をKnowledgeとして扱う。
- Future Candidateをapproved scopeとして扱う。
- Pending状態からCodex実行へ進める。

## Human Approval

次のような明示指示があった場合のみ、AI は Conversation Insight Draft を生成します。

- 書いといて。
- 保存して。
- Repositoryへ追加。
- Q化して。
- Conversation Insightとして残して。

明示指示がない場合、AI は候補提案に留めます。

## Pending Insight Branch

その場で正式登録、Q化、Codex実行を決めるべきではない場合は、
Pending Conversation Insight Review Workflow に分岐します。

```text
Conversation Insight Candidate
  -> Pending Insight Proposal
  -> Human Approval To Pending
  -> Pending Insight Artifact
  -> Next Startup / Daily Review
  -> Human Review Decision
```

Pending Insight は Approved Insight ではありません。

Pending Insight の保存先:

```text
docs/knowledge/conversation_insights/pending/
```

Details follow `docs/workflow/pending_conversation_insight_review_workflow.md`.

## Pending Decision Branch

Pending Decision は、Conversation Insight や Pending Insight とは別に、
会話で人間が承認した設計判断がまだ canonical repository asset に統合されて
いない場合に使う一時review stateです。

Use this branch when:

- a concrete architecture / workflow / governance decision was approved in
  conversation;
- the decision has not yet been integrated into Rule, Workflow, Architecture,
  Roadmap, ADR, Q, or another canonical artifact;
- losing the decision across chat boundaries would cause rediscovery or
  repeated review.

Do not use Pending Decision for:

- vague insight or philosophy without a concrete decision;
- action approval waiting for execution, which is Pending Action;
- implementation request, which should become a Q;
- accepted ADR or already canonical document.

Pending Decision lifecycle:

```text
Conversation Decision
  -> Human Approval To Record
  -> Pending Decision
  -> Startup Review
  -> Classification
  -> Canonical Integration / Rejected / Superseded / Archived
```

Pending Decision must never become a second canonical repository. It exists
only until integrated, rejected, superseded, or archived.

## Candidate Criteria

Conversation Insight Candidate として提案してよい条件:

- GDSの設計思想または運用方針に関わる。
- 複数回の作業や複数Projectで再利用できる可能性がある。
- Q、Research Mission、CASE、Completion Reportだけでは拾いにくい。
- 将来のRule / Architecture / Workflow / Roadmapへ昇格する可能性がある。
- 既存Knowledgeと完全重複していない。

提案しない条件:

- その場限りの感想。
- 行動に結びつかない雑談。
- 既に正式RuleやWorkflowに同じ内容がある。
- 個人情報やprivate contextに依存する。
- 具体的な実装が必要で、Qとして扱うべき内容。

## Artifact Location

Conversation Insight artifacts are stored under:

```text
docs/knowledge/conversation_insights/
```

Recommended naming:

```text
YYYY-MM-DD_<short_title>.md
```

Example:

```text
2026-07-12_ai_should_suggest_but_not_auto_save.md
```

## Template

Use:

```text
templates/conversation_insight_template.md
```

For Pending Insight, use:

```text
templates/pending_conversation_insight_template.md
```

## Review Fields

Every Conversation Insight artifact should record:

- Insight ID.
- Title.
- Source conversation summary.
- Capture reason.
- Insight summary.
- Applicable scope.
- Out of scope.
- Related existing knowledge.
- Duplicate check.
- Promotion candidate type.
- Future candidate status.
- Human approval.
- Review result.
- Recommended next action.

Pending Decision records should include:

- Decision ID.
- Title.
- Source Conversation.
- Human Approval Evidence.
- Decision Summary.
- Scope.
- Integration Target.
- Status.
- Conflict Check.
- Next Action.
- Review / Expiration Condition.

## Promotion Path

Conversation Insight is not automatically authoritative.

Possible promotion destinations:

- `docs/rules/`
- `docs/workflow/`
- `docs/architecture/`
- `roadmap/`
- `pip/concepts/`
- `pip/cases/`
- `docs/knowledge/inventory/`
- `templates/`
- `examples/`

Promotion requires the target workflow:

- Concept Promotion Workflow for early concepts.
- Innovation Pipeline Workflow for Platform candidates.
- Platform Promotion Decision Report for Platform Standard decisions.
- Knowledge Inventory for pre-promotion classification.
- Standard Q and Completion Report for documentation changes.

## Command Center Future Candidate

Future candidates:

- Command Centerによる Conversation Insight Candidate 自動検出。
- Insight Promotion Review。
- Knowledge Mining Dashboard。

These are future candidates only. They do not approve automatic repository
writes, automatic promotion, or Human Approval bypass.

## Completion Rule

Conversation Insight capture is complete when:

- Human Approval to draft is recorded.
- Artifact is saved under `docs/knowledge/conversation_insights/`.
- Duplicate check is recorded.
- Promotion path or archive decision is recorded.
- README / index route is updated when the artifact becomes a durable entry point.
- Completion Report records changed files, verification, remaining issues, and next Q.

Pending Insight review is complete when:

- Pending artifact is reviewed.
- Human decision is recorded.
- Codex execution remains blocked while Pending.
- Cleanup decision is confirmed after formal reflection or rejection.
