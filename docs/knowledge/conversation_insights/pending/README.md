# Pending Conversation Insights

Pending Conversation Insights は、会話中に価値がある可能性を検出したが、その場で
正式登録、Q化、Codex実行を決めない一時候補です。

ここは正式Knowledgeの保存場所ではありません。翌日以降のHuman Reviewで扱いを決める
ための一時Queueです。

## Status Boundary

Pending Insight は次を意味しません。

- Approved Conversation Insight。
- Rule。
- Workflow。
- Architecture。
- Q実行承認。
- Codex実行承認。

## Standard Flow

```text
Conversation
  -> Pending Insight
  -> Next Startup / Daily Review
  -> Human Review
  -> Register Conversation Insight / Create Q / Keep Pending / Reject / Already Reflected
  -> Cleanup Confirmation
```

## Naming

```text
PI-00000_<short_title>.md
```

## Review Decisions

- `Register as Conversation Insight`
- `Create Q`
- `Keep Pending`
- `Reject`
- `Already Reflected`

## Guard

- Do not save full chat logs.
- Do not save personal information.
- Do not execute Codex from Pending state.
- Do not auto-promote.
- Do not auto-delete after reflection.

## Current Pending / Resolved Items

| ID | Title | Status | Review Decision | Related Artifact |
| --- | --- | --- | --- | --- |
| PI-00001 | Process Improvement Over Repeated Reminder | Pending formal review | Keep Pending | `PI-00001_process_improvement_over_repeated_reminder.md` |
| PI-00002 | Pending Insight Review Before Codex Execution | Resolved by standardization | Already Reflected | `PI-00002_pending_insight_review_before_codex_execution.md` |

## Related Documents

- `docs/rules/pending_conversation_insight_review_rules.md`
- `docs/workflow/pending_conversation_insight_review_workflow.md`
- `templates/pending_conversation_insight_template.md`
- `examples/pending_conversation_insight_examples.md`
- `docs/rules/conversation_insight_capture_rules.md`
- `docs/workflow/conversation_insight_capture_workflow.md`
