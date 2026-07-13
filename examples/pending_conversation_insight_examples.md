# Pending Conversation Insight Examples

## Good Example: Decide Later

Situation:

```text
雑談中に「同じ注意を繰り返すより、Process / Checklist / Validator / Gateを
改善すべき」という考えが出た。
```

Good response:

```text
これは再利用価値がありそうですが、今すぐRule化するより、
Pending Insightとして明日レビューするのが安全です。

Pendingにしてよいですか？
```

Why good:

- 価値を拾っている。
- 即時正式登録していない。
- Human Approval To Pending を求めている。
- 後日の判断に回している。

## Good Example: Startup Review

```text
Pending Insight Review:
- PI-00001: Process Improvement Over Repeated Reminder
- Current Project relevance: High
- Suggested action: Existing Knowledge Poka-Yoke ruleとの重複確認
- Decision options: Register / Q / Keep Pending / Reject / Already Reflected
```

Why good:

- Type、ID、理由、推奨Actionが短い。
- 実装やPromotionを強制していない。
- Outstanding Review Notification として扱っている。

## Good Example: Already Reflected

```text
PI-00002 は今回の Pending Conversation Insight Review Rules と Workflow に
反映済みです。Pending状態を解消するか、履歴として残すかを確認してください。
```

Why good:

- 反映先を明示している。
- 自動削除していない。
- Human confirmation を残している。

## Bad Example: Immediate Codex Execution

```text
飲酒中に良いアイデアが出たので、そのままCodexへ実装依頼します。
```

Why bad:

- Pending状態を飛ばしている。
- 翌日レビューがない。
- Human Approval境界が弱い。

## Bad Example: Full Chat Capture

```text
昨日の雑談ログ全文をRepositoryへ保存します。
```

Why bad:

- チャット全文保存は禁止。
- 個人情報や一時感情が混入する。
- 要約とレビュー対象だけを保存すべき。

## Bad Example: Pending Equals Approved

```text
Pendingに保存したので、これは承認済みRule候補として扱います。
```

Why bad:

- Pending Insight は正式Knowledgeではない。
- Approved Insight、Rule、Workflow、Q実行承認ではない。
- Human Review が必要。
