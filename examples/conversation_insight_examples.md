# Conversation Insight Examples

## Good Example

Situation:

- ChatGPTと人間が、Command Centerは自動実行装置ではなくRepository Orchestratorである、
  という設計思想を長時間議論した。
- その内容は将来のArchitecture、Workflow、Ruleに影響する。
- ただし、すぐに実装Qにする段階ではない。

Good handling:

```text
AI:
この話はGDSの設計思想として残す価値があります。
Conversation Insight Candidateとして保存しますか？

Human:
保存して。

AI:
Conversation Insight Draftを作成し、重複確認とFuture Candidate分類を記録する。
```

Result:

- `docs/knowledge/conversation_insights/YYYY-MM-DD_command_center_as_repository_orchestrator.md`
  に保存。
- Human Approval to draft を記録。
- Future Candidate として保持。
- 必要になったら Architecture または Workflow へ昇格。

## Bad Example: Auto Save

Problem:

- AIが人間の明示指示なしに会話をRepositoryへ保存した。

Why bad:

- Human Approvalを bypass している。
- 雑談や一時的な感情までKnowledge化する危険がある。
- Repositoryがnoiseで増える。

Correct behavior:

- AIは候補提案だけ行う。
- 人間が「保存して」「書いといて」などと指示した場合のみDraftを作る。

## Bad Example: Treating Candidate As Rule

Problem:

- Conversation Insight Candidateを、そのまま正式Ruleとして扱った。

Why bad:

- Review、Duplicate Check、Promotion path、Human Approvalが不足している。
- Future Candidateとapproved scopeが混ざる。

Correct behavior:

- Conversation Insightはpre-promotion knowledgeとして保存する。
- Rule化する場合は別Q、Rule更新、Completion Report、Repository Quality確認を行う。

## Borderline Example

Situation:

- 人間が「これは大事そうだね」と言った。
- しかし「保存して」とは言っていない。

Correct behavior:

```text
AI:
これはConversation Insight Candidateとして残す価値がありそうです。
保存しますか？
```

AIは自動保存しない。
