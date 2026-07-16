# Capability Disclosure Rule

## Purpose

Capability Disclosure Rule は、AI が実行能力を推測で答えず、検証結果を人間へ
明示してから計画・実行へ進むためのルールです。

## Core Rule

AI は、現在の能力を検証する前に「できます」と断定してはいけません。

正しい順序:

```text
Verify capability
  -> disclose capability
  -> plan
  -> execute
```

## Required Disclosure

AI は必要に応じて次を開示します。

- できること。
- できないこと。
- まだ未検証のこと。
- approval が必要なこと。
- user input が必要なこと。
- 代替workflow。

## Capability Areas

### Memory

AI memory や過去チャットを authoritative source として扱いません。
必要な情報は repository、添付ファイル、明示された会話文脈から確認します。

### Repository

Repository access は実測します。

確認例:

```bash
pwd
git rev-parse --show-toplevel
git status --short --untracked-files=all
```

### Tools

使えるtool、使えないtool、承認が必要なtoolを区別します。

### Commit / Push

Commit / Push は capability と authority を分けて扱います。

たとえ技術的に可能でも、QまたはHuman Approvalで許可されていなければ実行しません。

### Connected Services

GitHub、Gmail、Calendar、Drive、browser、Chromeなどの接続サービスは、
利用可能性と接続状態を確認してから使います。

### Current Chat Limitations

添付ファイル不足、画像未確認、長文欠落、コンテキスト不足がある場合は、
計画前に制約として開示します。

## Bad Pattern

```text
User: このAIでできますか？
AI: できます。では計画します。
```

問題:

- repository access を確認していない。
- tool availability を確認していない。
- permission / approval を確認していない。

## Good Pattern

```text
Capability:
- Can do: repository内のMarkdown調査と文書更新。
- Cannot do: commit / pushはQで禁止されているため実行しない。
- Need verification: 対象repositoryのwrite permission。
- Alternative workflow: 書き込み不可なら差分案として提示する。
```

## Related Documents

- `docs/workflow/capability_verification_first.md`
- `templates/capability_decision_matrix.md`
- `examples/capability_examples.md`
- `docs/workflow/pre_response_verification_gate.md`
