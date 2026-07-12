# CI-00002 Design Conversation Mode

## Metadata

- Insight ID: CI-00002
- Title: Design Conversation Mode
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

- 設計思想や長期運用方針は、リラックスした会話で自然に言語化されることがある。
  Conversation Insight は、その思想を採掘し、後から冷静にレビューできるよう保存する。

Important context:

- 重要な設計判断は、正式な仕様書やQだけでなく、会話中に初めて言葉になることがある。
- その場で採用するのではなく、Candidate化し、Human Review後にPromotionする。

What is intentionally not preserved:

- 会話全文。
- 雑談そのもの。
- 一時的な感情や状況。
- 飲酒などの状況描写を本質として扱うこと。

## Capture Reason

Why this conversation should be preserved as Knowledge:

- GDS が「いつ設計思想が生まれるか」を狭く決めすぎないため。
- リラックスした会話から生まれた思想を、後で冷静にレビューできる形へ変換する
  運用を示すため。

Why chat history alone is insufficient:

- 会話の中に埋もれた設計思想は、artifact化しないと後から見つけにくく、
  reviewやpromotionにつながりにくいため。

## Insight Summary

Core insight:

- 設計思想や長期運用方針は、自然な会話の中で表出することがある。
- 重要なのは会話の状況ではなく、設計思想の表出である。
- 判断をその場で採用せず、Insight Candidate化し、Human Review後にPromotionする。

Operational meaning:

- AI は設計思想らしき発言を検出した場合、すぐRule化せず、
  Conversation Insight Candidateとして提案する。
- Human Approval後にartifact化し、冷静なreviewを待つ。

Long-term value:

- GDS は、堅い仕様書だけでなく、人間とAIの協働から自然に生まれる思想も
  Knowledge Promotion Pipelineへ取り込める。

## Applicable Scope

Applies to:

- GDS design discussion。
- Long-term operation planning。
- Command Center concept discussion。
- Platform philosophy discussion。
- AI / human collaboration。

Does not apply to:

- 会話の雰囲気や雑談そのものの保存。
- その場の発言を即時にapproved ruleへ変換すること。
- Human ReviewなしのPromotion。

## Related Existing Knowledge

Related rules:

- `docs/rules/conversation_insight_capture_rules.md`
- `docs/rules/ai_proactive_proposal_rules.md`
- `docs/rules/core_principles.md`

Related workflow:

- `docs/workflow/conversation_insight_capture_workflow.md`
- `docs/workflow/collaborative_decision_workflow.md`

Related architecture:

- `docs/architecture/command_center_architecture.md`
- `docs/architecture/platform_era_core_principles.md`

Related concepts / CASE / inventory:

- `docs/knowledge/conversation_insights/README.md`

## Duplicate Check

Existing similar knowledge:

- Conversation Insight Capture Standard already defines the formal capture rule.

Duplicate risk:

```text
Low
```

Decision:

```text
New
```

Reason:

- This artifact captures the operating insight that design philosophy can surface
  naturally in conversation and should be reviewed later, rather than adopted
  immediately.

## Promotion Candidate

Candidate type:

- Workflow
- Architecture
- Concept
- Future Candidate only

Target location:

- Future review may decide whether Design Conversation Mode belongs in
  collaboration workflow, Command Center guidance, or Platform philosophy docs.

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
- The essence is design philosophy expression, not the casual context itself.

Human Approval:

```text
Approved
```

## Recommended Next Action

- Use this artifact as a Good Template reference for future Conversation Insight
  artifacts.
- Review later whether Design Conversation Mode should become a collaboration
  methodology or Command Center support mode.

## Completion Notes

Generated artifacts:

- `docs/knowledge/conversation_insights/CI-00002_design_conversation_mode.md`

Updated docs:

- `docs/knowledge/conversation_insights/README.md`

Remaining issues:

- Promotion Review Template is not yet defined.
