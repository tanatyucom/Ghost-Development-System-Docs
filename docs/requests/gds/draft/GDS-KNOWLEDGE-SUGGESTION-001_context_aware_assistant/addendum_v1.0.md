# Q_GDS_Knowledge_Suggestion_Assistant_Addendum_JP

Version: 1.0
Status: Approved Addendum
Priority: High
Category: Startup / Knowledge Retrieval / Command Center

## Purpose

実行中または完了済みの
`Q_GDS_Context_Aware_Knowledge_Suggestion_Assistant_JP`
へ、以下の追加仕様を正式に反映する。

1. 1日1回のCanonical Knowledge Source Review
2. 未レビューKnowledgeの通知
3. レビュー済みKnowledgeのContext-Aware再提案

## Background

Knowledgeを保存するだけでは、
長期チャット・チャット移動・時間経過によりAIが重要情報を見落とす可能性がある。

そのためGDSは、

```text
保存
→ 日次確認
→ 未レビュー通知
→ Contextに応じた再提示
→ Human Decision
```

までを標準運用とする。

## Scope

- Startup ProcedureへDaily Knowledge Source Reviewを追加
- AI Repository Indexを日次Canonical Reviewの入口に指定
- 未レビューKnowledge通知を追加
- レビュー済みKnowledgeも関連時に再提案可能とする
- Startup Checklist / Rule / Workflow / Template更新
- Completion Report更新
- AI Repository Index Update Gate実施

## Out of Scope

- 常駐監視
- バックグラウンド自動実行
- 自動Promotion
- 自動Q生成
- 自動実装
- 自動Commit
- Command Center GUI
- Knowledge Recommendation Engine実装

## Requirement 1: Daily Knowledge Source Review

少なくとも1日1回、
主要なProject作業または提案を行う前にCanonical Knowledge Sourceを確認する。

Minimum targets:

- AI Repository Index
- Current Information Package
- Current Project Profile
- Current Roadmap
- Conversation Insights
- Future Candidates
- Research Missions
- Improvement Records
- Relevant CASE / Rule / Architecture / Workflow

目的:

- AIの忘却対策
- 古い前提の検出
- Repository更新の把握
- Chat移動後のContext復元
- 現在作業と関連するKnowledgeの再発見

これは自動編集権限を与えない。

## Requirement 2: Outstanding Review Notification

未レビューKnowledgeが存在する場合、
Startupまたは当日最初の適切なProject interactionで通知する。

対象候補:

- Conversation Insight
- Future Candidate
- Research Mission
- Improvement Record
- CASE
- Promotion Candidate

通知内容:

- Type
- ID / Title
- 現在レビューする価値
- 推奨Action

同じ項目を過剰に繰り返し通知しない。

## Requirement 3: Context-Aware Re-Suggestion

レビュー済み・Approved済みKnowledgeも、
現在の会話・作業・Repository状況と高い関連性がある場合は再提案する。

Rules:

- Review statusよりCurrent Context Relevanceを優先
- 未レビュー通知とレビュー済み再提案を区別
- 提案理由を簡潔に説明
- Reviewや実装を強制しない
- 最終判断はHuman Approval

Example:

```text
以前承認済みのCI-00002ですが、
現在のCommand Center設計と強く関連するため再提案します。
```

## Suggestion Priority

1. Current Context Relevance
2. Immediate Risk / Blocker
3. Promotion Opportunity
4. Outstanding Review
5. Important Knowledge not recently referenced
6. Future Candidate readiness

## Human-Controlled Actions

- Roadmap追加
- Q化
- Codex実装依頼
- Rule化
- Architecture化
- Workflow化
- Archive
- Reject
- No Action

## Suggested Commit Message

```text
docs: add daily knowledge review and context-aware suggestions
```
