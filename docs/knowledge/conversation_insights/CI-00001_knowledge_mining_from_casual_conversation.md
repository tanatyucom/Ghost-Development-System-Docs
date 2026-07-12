# CI-00001 Knowledge Mining from Casual Conversation

## Metadata

- Insight ID: CI-00001
- Title: Knowledge Mining from Casual Conversation
- Date: 2026-07-12
- Status: Approved Insight
- Source:
  - Conversation
  - Design discussion
  - Platform discussion
- Human Approval to draft: Yes
- Approval source: `Q_GDS_Conversation_Insight_Initial_Artifacts_JP_v1.1`
- Created by: Codex
- Reviewer: Human approved by Q

## Source Conversation Summary

Short summary:

- Conversation Insight は雑談保存ではなく、価値ある知識を会話から採掘し、
  Human Review を経て Repository へ昇格する仕組みである。

Important context:

- GDS は、Q、Research Mission、CASE、Completion Report だけでは拾いにくい
  設計思想や運用原則を扱う必要がある。
- 会話は正式な Knowledge Source になり得るが、Repositoryへ保存するには
  Human Approval と review が必要である。

What is intentionally not preserved:

- チャット全文。
- 日常雑談。
- 一時的な感情。
- private context。

## Capture Reason

Why this conversation should be preserved as Knowledge:

- Conversation Insight Capture Standard の運用開始点として、
  会話由来の知識をどう扱うかを示す基準になるため。

Why chat history alone is insufficient:

- チャット履歴は長期的な repository memory として検索、review、promotion、
  Git管理に向かないため。

## Insight Summary

Core insight:

- Conversation は正式な Knowledge Source になり得る。
- AI は Candidate 提案まで行い、Human Approval を待つ。
- Repository は長期記憶として使う。
- Promotion は review 後に行う。

Operational meaning:

- AI は会話中に価値ある知識を見つけた場合、保存価値を短く説明し、
  Candidate として提案できる。
- AI は自動保存せず、Human Approval 後にのみ Draft または Approved Insight
  artifact を作成する。

Long-term value:

- GDS が会話由来の思想や運用原則を失わず、後からRule、Architecture、
  Workflow、Roadmap、Concept、CASEへ昇格できるようにする。

## Applicable Scope

Applies to:

- GDS Knowledge Base。
- Conversation Insight Capture。
- Knowledge Promotion Pipeline。
- AI / human collaboration。
- Command Center 将来構想。

Does not apply to:

- 雑談全文の保存。
- Human ApprovalなしのRepository保存。
- Conversation Insightを即座にRuleとして扱う運用。

## Related Existing Knowledge

Related rules:

- `docs/rules/conversation_insight_capture_rules.md`
- `docs/rules/ai_startup_procedure_rules.md`
- `docs/rules/startup_checklist_rules.md`

Related workflow:

- `docs/workflow/conversation_insight_capture_workflow.md`
- `docs/workflow/ai_startup_procedure.md`
- `docs/workflow/startup_checklist_workflow.md`

Related architecture:

- `docs/architecture/command_center_architecture.md`

Related concepts / CASE / inventory:

- `docs/knowledge/README.md`
- `docs/knowledge/conversation_insights/README.md`

## Duplicate Check

Existing similar knowledge:

- Conversation Insight Capture Rule and Workflow define the operating standard.

Duplicate risk:

```text
Low
```

Decision:

```text
New
```

Reason:

- This artifact is not another rule definition. It is the first approved
  example insight showing why conversation can be treated as a Knowledge Source.

## Promotion Candidate

Candidate type:

- Rule
- Workflow
- Architecture
- Knowledge Inventory

Target location:

- Future review may decide whether this insight should update core principles,
  Knowledge Promotion documentation, or Command Center architecture.

Promotion readiness:

```text
Needs Review
```

## Review

Review result:

```text
Accepted
```

Review notes:

- Registered as an initial Approved Insight by Q.
- Rule / Architecture promotion is intentionally deferred to a separate review.

Human Approval:

```text
Approved
```

## Recommended Next Action

- Use this artifact as a Good Template reference for future Conversation Insight
  artifacts.
- Review later whether Knowledge Mining should become a Command Center
  capability or Knowledge Promotion sub-workflow.

## Completion Notes

Generated artifacts:

- `docs/knowledge/conversation_insights/CI-00001_knowledge_mining_from_casual_conversation.md`

Updated docs:

- `docs/knowledge/conversation_insights/README.md`

Remaining issues:

- Promotion Review Template is not yet defined.
