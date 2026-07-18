# Approval Execution Instruction Cases

## Case 1: Commit Approved

Input:

```text
Commit: Recommended
Push: Hold
Tag: Hold
```

Human response:

```text
お願いします
```

Expected:

```text
Commit: Approved
Push: Hold
Tag: Hold

Commit OKです。
Codex側でCommitを実行してください。
```

Prohibited:

```text
コミットしても良いですか？
```

## Case 2: Commit And Push Approved

Expected:

```text
Commit: Approved
Push: Approved
Tag: Hold

CommitとPushはOKです。
Codex側でCommitとPushを実行してください。
```

## Case 3: Repository State Changed

Expected:

```text
SCW
Previous Approval: Invalidated
New Approval Request Required
```

## Case 4: Execution Evidence

Expected transition:

```text
Execution Instruction
-> Governed Execution
-> Execution Evidence
-> Completion Confirmation
```
