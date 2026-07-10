# AI Proactive Proposal Examples

## Purpose

この文書は、AI Proactive Proposal Rule の良い例と悪い例を示します。

## Good Example: Scope Concern

```text
Proactive Proposal:
- Observation: Q は GDS Docs のみ編集可ですが、GameGhost 側にも変更候補があります。
- Evidence: Related Repository is reference only.
- Proposal: 今回は GDS Docs のルール更新だけにし、GameGhost 変更は別 Q に分ける。
- Impact: scope drift と誤編集を防げます。
- User decision needed: No, current Q scopeに従います。
```

## Good Example: Time Saving

```text
Proactive Proposal:
- Observation: 新規文書を作るより既存 Startup Checklist を拡張した方が短いです。
- Evidence: 既存文書に該当セクションがあります。
- Proposal: 新規追加ではなく既存テンプレートへ項目追加します。
- Impact: 重複を避け、レビュー量を減らせます。
- User decision needed: No,既存ルールに沿います。
```

## Bad Example: Silent Scope Expansion

```text
良さそうなので関連 repository も修正しました。
```

問題:

- 提案ではなく勝手に実装している。
- Scope Guard を破っている可能性がある。
- ユーザー判断がない。

## Bad Example: Unsupported Suggestion

```text
なんとなく別方式の方が良いです。
```

問題:

- Evidence がない。
- Impact が不明。
- 実装変更の判断材料にならない。

## Review Checklist

- 提案に Observation / Evidence / Proposal / Impact があるか。
- 勝手に実装変更していないか。
- ユーザー判断が必要な場合、明示されているか。
- Recommended Improvements / Future Candidates に残すべき内容か。
