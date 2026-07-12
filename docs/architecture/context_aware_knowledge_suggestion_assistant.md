# Context-Aware Knowledge Suggestion Assistant

**Version:** Draft 1.1

**Status:** Draft Architecture Proposal

**Last Updated:** 2026-07-12

## Purpose

Context-Aware Knowledge Suggestion Assistant は、Startup および日常利用時に、
現在の会話、作業内容、Repository 状況に関連する GDS Knowledge を AI が提案する
ための Command Center / Knowledge architecture proposal です。

目的は、AI が判断や実行を自動化することではありません。

目的は、必要なタイミングで次のように提案することです。

```text
今、このKnowledgeが役立つ可能性があります。
```

決定権は常に人間が持ちます。

## Background

Conversation Insight により、会話由来の重要な知識を保存できるようになりました。

しかし、保存された Knowledge は、必要な場面で再提示されなければ十分に活用されません。

対象には、未レビュー項目だけでなく、すでにレビュー済みだが現在の作業に強く関係する
Knowledge も含まれます。

## Positioning

This assistant is a proposal layer.

It may suggest:

- Related Knowledge.
- Outstanding Review.
- Promotion Candidates.
- Future Candidates.
- Possible next review target.
- Possible next Q candidate.

It must not decide, promote, generate, implement, or commit automatically.

## Target Knowledge

Suggestion対象:

- Conversation Insight。
- Future Candidate。
- Research Mission。
- Improvement Record。
- CASE。
- Architecture。
- Rule。
- Workflow。
- Template。
- Example。
- Completion Report。

## Suggestion Inputs

Context sources:

- Daily Canonical Knowledge Source Review.
- Current Q file。
- Current conversation summary。
- Startup Checklist。
- Information Package, when provided。
- AI Repository Index。
- Recently changed files。
- Repository Quality Report。
- Completion Reports。
- Platform Standard Registry。
- Conversation Insights。
- Rules / Workflow / Architecture / Roadmap。

The assistant should cite file paths when suggesting knowledge.

## Daily Canonical Knowledge Source Review

At least once per day, before major project work or significant proposals, AI
should review the canonical knowledge sources needed to recover current context.

Canonical daily entry point:

- `docs/ai_repository_index.md`

Minimum targets:

- AI Repository Index。
- Current Information Package。
- Current Project Profile。
- Current Roadmap。
- Conversation Insights。
- Future Candidates。
- Research Missions。
- Improvement Records。
- Relevant CASE / Rule / Architecture / Workflow。

Purpose:

- AI forgetting prevention。
- Detect stale assumptions。
- Notice repository updates。
- Restore context after chat movement。
- Rediscover Knowledge related to current work。

This review does not grant edit, promotion, Q generation, implementation,
commit, or background execution authority.

## Suggestion Rules

AI prioritizes suggestions by:

1. Current Context Relevance.
2. Immediate Risk / Blocker.
3. Promotion Opportunity.
4. Outstanding Review.
5. Important Knowledge not recently referenced.
6. Future Candidate readiness.

Reviewed Knowledge may still be suggested when it is highly relevant to the
current theme.

Outstanding review notification and reviewed Knowledge re-suggestion must be
labeled separately.

## Startup Behavior

At Startup, the assistant may surface a short suggestion block:

```text
Knowledge Suggestions:
- Daily Knowledge Source Review:
- Outstanding Review:
- Related Knowledge Suggestions:
- Promotion Candidates:
- Future Candidates:
```

The startup output should stay short. It should link to artifacts rather than
copying long content into chat.

Detailed review begins only when the user chooses to inspect, Q化, promote,
archive, reject, or otherwise act on a suggestion.

## Outstanding Review Notification

If unreviewed Knowledge exists, AI may notify at Startup or the first suitable
project interaction of the day.

Notification candidates:

- Conversation Insight。
- Future Candidate。
- Research Mission。
- Improvement Record。
- CASE。
- Promotion Candidate。

Notification content:

- Type。
- ID / Title。
- Why reviewing now may be valuable。
- Recommended action。

The assistant should avoid repeatedly notifying the same item without a useful
context change.

## Context-Aware Re-Suggestion

Reviewed or Approved Knowledge may be suggested again when it has high
relevance to the current conversation, task, or repository state.

Rules:

- Prioritize Current Context Relevance over review status.
- Distinguish reviewed re-suggestion from outstanding review notification.
- Explain the reason briefly.
- Do not force review or implementation.
- Leave the final decision to Human Approval.

Example:

```text
以前承認済みのCI-00002ですが、
現在のCommand Center設計と強く関連するため再提案します。
```

## Daily Use Behavior

During ordinary work, the assistant may make a short proposal when context
changes reveal useful knowledge.

Example:

```text
この作業には CI-00001 と Command Center Architecture が関連しそうです。
必要なら関連箇所を確認します。
```

The assistant should avoid noisy repeated suggestions. It should not interrupt
simple tasks unless the knowledge is clearly relevant or risk-reducing.

## Human Approval Boundary

AI only proposes.

Humans decide:

- Roadmapへ追加。
- Q化。
- Codex実装依頼。
- Rule化。
- Architecture化。
- Workflow化。
- CASE化。
- Archive。
- Reject。
- No Action。

## Out Of Scope

Out of scope:

- 自動Promotion。
- 自動Commit。
- 自動Q生成。
- 自動実装。
- 自動Rule化。
- 自動Architecture化。
- 自動Archive。
- Repository write without Human Approval。
- 常駐監視。
- バックグラウンド自動実行。
- Command Center GUI。
- Knowledge Recommendation Engine implementation。
- Replacing AI Proactive Proposal, Conversation Insight Detection, or Startup Checklist.

## Data Flow

```text
Current Context
  -> Daily Canonical Knowledge Source Review
  -> Repository / Knowledge Scan
  -> Related Knowledge Candidate Set
  -> Relevance / Review / Promotion Classification
  -> Suggestion Summary
  -> Human Decision
  -> Q / Review / Promotion / Archive / Reject, when approved
```

## Relationship To Existing Components

### Command Center

The assistant is a Command Center candidate capability. Command Center may use
it to surface Knowledge during Startup, daily operation, review, or planning.

### AI Proactive Proposal

AI Proactive Proposal raises risks, better approaches, and knowledge
opportunities. Knowledge Suggestion Assistant is a more structured future
capability for surfacing related repository Knowledge.

### Conversation Insight

Conversation Insight stores valuable knowledge from conversation. Knowledge
Suggestion Assistant may later recommend relevant Conversation Insights, but it
does not create or promote them automatically.

### Startup Checklist

Startup Checklist may show a short Knowledge Suggestions block in the future.
This proposal does not make detailed review mandatory at startup.

Startup may also record whether Daily Canonical Knowledge Source Review was
performed and whether outstanding reviews or related suggestions were surfaced.

### Information Package

Information Package may provide Current Status, Current Focus, and Recent
Artifacts used for context-aware suggestions.

## Failure Behavior

| Condition | Behavior |
| --- | --- |
| Relevance is weak | Do not suggest. |
| Too many matches | Show top few and say more can be reviewed on request. |
| Source is missing | Report missing source instead of guessing. |
| Knowledge conflicts | Route to Collaborative Decision. |
| Suggestion requires action | Ask for Human Approval before drafting or editing. |
| Repository health is Red | Suggest audit or review before implementation. |
| Same item repeatedly suggested | Suppress unless context changed or user asks. |

## Output Format

Short chat form:

```text
Related Knowledge Suggestions:
- <path>: <reason>
```

Artifact form, when reviewable or Git-managed:

```text
Knowledge Suggestion Report
- Context:
- Daily Knowledge Source Review:
- Suggested Knowledge:
- Outstanding Review:
- Reviewed Knowledge Re-Suggestion:
- Reason:
- Status:
- Human Decision:
- Next Action:
```

## Future Candidates

- 類似Knowledge検索。
- 関連度スコア。
- Command Center Dashboard。
- Knowledge Recommendation Engine。
- Suggestion suppression / cooldown。
- Suggestion history。
- Knowledge Suggestion Report template。
- Daily Knowledge Source Review checklist。

## Review Points

Review this proposal for:

- Human Approval boundary.
- Noise control.
- Relationship with AI Proactive Proposal.
- Relationship with Conversation Insight Detection.
- Startup burden.
- Outstanding review notification noise.
- Reviewed Knowledge re-suggestion criteria.
- Command Center responsibility boundary.
- Whether a template or workflow is needed before implementation.

## Related Documents

- `docs/architecture/command_center_architecture.md`
- `docs/architecture/responsibility_boundary.md`
- `docs/rules/ai_proactive_proposal_rules.md`
- `docs/rules/conversation_insight_capture_rules.md`
- `docs/workflow/ai_startup_procedure.md`
- `docs/workflow/startup_checklist_workflow.md`
- `templates/startup_checklist_template.md`
- `docs/knowledge/conversation_insights/README.md`
- `templates/information_package_template.md`
