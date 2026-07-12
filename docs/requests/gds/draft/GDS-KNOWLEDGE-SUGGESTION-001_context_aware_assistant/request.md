# Q_GDS_Context_Aware_Knowledge_Suggestion_Assistant_JP

Version: 1.0
Status: Draft
Priority: High
Category: Command Center / Knowledge

## Purpose

Startupおよび日常利用時に、未レビュー項目だけでなく、
**現在の作業内容と関連するKnowledgeをAIが提案する**
Knowledge Suggestion Assistant を設計する。

## Background

Conversation Insightの導入によりKnowledgeは保存できるようになった。

しかし、

- Review済みKnowledge
- Future Candidate
- Research Mission
- Improvement Record

も、必要なタイミングで再提示されなければ価値を十分発揮できない。

## Concept

AIは現在の会話・作業・Repository状況をもとに、

「今、このKnowledgeが役立つ可能性があります」

という提案のみを行う。

決定権は常に人間が持つ。

## Target Knowledge

- Conversation Insight
- Future Candidate
- Research Mission
- Improvement Record
- CASE
- Architecture
- Rule
- Workflow

## Suggestion Rules

AIは以下を優先して提案する。

- 現在の話題との関連性
- 最近参照されていない重要Knowledge
- 未レビューKnowledge
- Promotion候補
- 実装候補

既レビューKnowledgeも、
現在のテーマと高い関連性がある場合は提案対象とする。

## Startup Behavior

Startup時に以下を表示する。

- Outstanding Review
- Related Knowledge Suggestions
- Promotion Candidates
- Future Candidates

必要な場合のみ詳細レビューへ進む。

## Human Approval

AIは提案のみ。

以下は人間が判断する。

- Roadmapへ追加
- Q化
- Codex実装依頼
- Rule化
- Architecture化
- Archive
- Reject

## Out of Scope

- 自動Promotion
- 自動Commit
- 自動Q生成
- 自動実装

## Future Candidates

- 類似Knowledge検索
- 関連度スコア
- Command Center Dashboard
- Knowledge Recommendation Engine

## Suggested Commit Message

docs: add context-aware knowledge suggestion assistant proposal
