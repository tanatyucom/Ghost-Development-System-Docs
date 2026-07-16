# Capability Examples

## Good Example: Verify Before Saying Yes

User:

```text
このAIでこのQを最後までできますか？
```

AI:

```text
まず capability を確認します。

Capability:
- Can do: 添付Qを読み、repository内のMarkdownを更新し、検証結果を報告できます。
- Cannot do: QでCommit / Pushが禁止されている場合は実行しません。
- Need verification: 対象repositoryの読み書き権限と必要tool。
- Alternative workflow: 書き込みできない場合は、編集案とpatch案を提示します。
```

## Bad Example: Assumption-Driven Yes

```text
できます。すぐ実装します。
```

問題:

- repository access を確認していない。
- tool availability を確認していない。
- Commit / Push authority を確認していない。
- 添付Qが読めるか確認していない。

## Good Example: Capability With Limitation

```text
Capability:
- Can do: ローカルrepositoryの文書調査とMarkdown更新。
- Cannot do: 外部Web確認はnetwork制限があるため未確認。
- Need approval: sandbox外のpathへ書く場合は承認が必要。
- Alternative workflow: 公式repository内の既存文書を根拠に作業します。
```

## Good Example: Connected Service

```text
Capability:
- Can do: ローカルファイルとGit状態の確認。
- Cannot do currently: Google Drive内の資料確認。Drive connectorが未接続。
- Alternative workflow: 必要ファイルを添付してもらえれば、そのartifactを正本として扱います。
```

## Bad Example: Authority Confusion

```text
pushできます。
```

問題:

- 技術的に可能かと、Q / Human Approvalで許可されているかを混同している。

改善:

```text
技術的にpush可能かは未確認です。さらに、このQではPushが許可されていないため実行しません。
```
