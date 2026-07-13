# Notes: Pending Conversation Insight Review Workflow

## Source

- Original Q: `C:/Users/tanat/Downloads/Q_GDS_Pending_Conversation_Insight_Review_Workflow_JP.md`
- Workspace copy: `request.md`

## Storage Decision

Pending Insight の標準保存先は次に決定しました。

```text
docs/knowledge/conversation_insights/pending/
```

理由:

- Conversation Insight の前段として自然に辿れる。
- 正式 Approved Insight と folder boundary で分離できる。
- Git管理できる。
- Startup / Daily Review から参照しやすい。
- 後から Delete / Resolved / Archive / Keep temporarily を判断できる。

## Initial Pending Insight Handling

- PI-00001: Keep Pending。既存 Knowledge Poka-Yoke / Checklist / Validator /
  Gate と重複確認してから正式登録または既存文書更新を判断する。
- PI-00002: Already Reflected。今回のRule / Workflow / Template / Pending Queueへ
  標準化済み。ただし削除・ArchiveはHuman confirmation待ち。

## Safety Notes

- Pending Insight は正式Knowledgeではない。
- Pending状態ではCodex実行しない。
- チャット全文や個人情報は保存しない。
- cleanup は自動削除せずHuman confirmationで決める。
