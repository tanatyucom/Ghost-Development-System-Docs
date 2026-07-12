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

- Workflow: `docs/workflow/conversation_insight_capture_workflow.md`
- Template: `templates/conversation_insight_template.md`
- Examples: `examples/conversation_insight_examples.md`

## Storage Rule

Save artifacts here:

```text
docs/knowledge/conversation_insights/
```

Recommended naming:

```text
YYYY-MM-DD_<short_title>.md
```

## Guard

- AI may propose candidates.
- AI must not auto-save.
- Human Approval is required before draft generation.
- Conversation Insight does not replace Q, Research Mission, CASE, or Completion Report.
- Future Candidate is not approved scope.
