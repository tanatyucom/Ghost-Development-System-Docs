# Conversation Insights

Conversation Insights は、長時間の設計議論、運用理念、保守方針、将来構想など、
通常の Q、Research Mission、CASE になりにくい重要な会話由来の知見を保存する
pre-promotion knowledge area です。

ここに保存された内容は、正式Ruleではありません。
Rule / Architecture / Workflow / Roadmap / Concept / CASE へ昇格するには、
別Q、review、Human Approval、Completion Report が必要です。

## Standard Flow

```text
Conversation
  -> Conversation Insight Candidate
  -> Human Approval To Draft
  -> Conversation Insight Artifact
  -> Review
  -> Future Candidate
  -> Rule / Architecture / Workflow / Roadmap / Concept / CASE
```

## Entry Points

- Rule: `docs/rules/conversation_insight_capture_rules.md`
- Workflow: `docs/workflow/conversation_insight_capture_workflow.md`
- Template: `templates/conversation_insight_template.md`
- Examples: `examples/conversation_insight_examples.md`

## Approved Insights

| ID | Title | Status | Role |
| --- | --- | --- | --- |
| CI-00001 | Knowledge Mining from Casual Conversation | Approved Insight | Good Template reference for conversation as Knowledge Source |
| CI-00002 | Design Conversation Mode | Approved Insight | Good Template reference for preserving design philosophy from conversation |

Initial approved artifacts:

- [`CI-00001_knowledge_mining_from_casual_conversation.md`](CI-00001_knowledge_mining_from_casual_conversation.md)
- [`CI-00002_design_conversation_mode.md`](CI-00002_design_conversation_mode.md)

These artifacts are Approved Insights. They are not automatically promoted
Rules, Architecture, Workflow, Roadmap, Concepts, or CASE entries. Promotion
requires a separate review.

## Storage Rule

Save artifacts here:

```text
docs/knowledge/conversation_insights/
```

Recommended naming:

```text
CI-00000_<short_title>.md
```

ID format:

```text
CI-00001
CI-00002
CI-00003
```

Conversation Insight IDs use `CI-` plus a five-digit zero-padded sequence.

## Good Template Reference

Use the initial Approved Insights as practical references when creating a new
Conversation Insight artifact:

- CI-00001 shows how to preserve conversation as a Knowledge Source without
  saving casual chat.
- CI-00002 shows how to capture design philosophy that appears naturally in
  conversation, while deferring adoption to review.

## Guard

- AI may propose candidates.
- AI must not auto-save.
- Human Approval is required before draft generation.
- Conversation Insight does not replace Q, Research Mission, CASE, or Completion Report.
- Future Candidate is not approved scope.
- Approved Insight does not equal promoted Rule, Architecture, Workflow, or CASE.
