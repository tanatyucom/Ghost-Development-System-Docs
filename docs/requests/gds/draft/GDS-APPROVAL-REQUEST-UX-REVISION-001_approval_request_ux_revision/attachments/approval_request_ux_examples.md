# Approval Request UX Examples

## Purpose

These examples clarify the wording boundary between Approval Request and
Execution Instruction.

## Approval Request

Approval Request asks the human for permission.

```text
コミットしても良いですか？
```

```text
コミットとPushをしても良いですか？
```

## Execution Instruction

Execution Instruction is shown after valid Human Final Approval. Its audience is
the human.

Commit only:

```text
Commit: Approved
Push: Hold
Tag: Hold

Commit OKです。
次に、人間側からCodexへCommit実行を依頼してください。

Execution Evidence Required
```

Commit and Push:

```text
Commit: Approved
Push: Approved
Tag: Hold

CommitとPushはOKです。
次に、人間側からCodexへCommitとPushの実行を依頼してください。

Execution Evidence Required
```

## Bad Example

```text
ChatGPT will issue an Execution Instruction and Codex will execute the Commit.
```

This can be misread as ChatGPT directly commanding Codex.

## Good Example

```text
Commit OKです。
次に、人間側からCodexへCommit実行を依頼してください。
```

This preserves the actual flow:

```text
ChatGPT -> Human -> Codex
```
