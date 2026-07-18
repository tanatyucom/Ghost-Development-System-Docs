# Q_GDS_APPROVAL_EXECUTION_INSTRUCTION_FIX_001

Status: Draft
Priority: High
Category: Fix / Governance / Approval / Execution Instruction

## Purpose

Fix the Approval workflow so that ChatGPT does not request Human Approval again
after the Human has already approved the current Approval Request.

After valid Human Final Approval, ChatGPT must issue an explicit Execution
Instruction to the governed execution actor.

This is a revision of the existing Approval Request architecture and rules.
Do not create a parallel approval system.

---

## Background

The existing governed flow is:

```text
Codex
-> Repository Recommendation
-> ChatGPT
-> Workflow Recommendation / Completion Review
-> Human
-> Final Approval
-> ChatGPT
-> Execution Instruction
-> Codex / Adapter
-> Governed Execution
-> Execution Evidence
```

A wording and responsibility-boundary defect remains in current operation.

Observed behavior after Human Final Approval:

```text
コミットしても良いですか？
```

This incorrectly starts a second approval request even though Human Final
Approval has already been granted.

Required behavior after approval:

```text
Commit OKです。
Codex側でCommitを実行してください。
```

The same principle must apply independently to Push and Tag.

---

## Acceptance Criteria

- Approval Request and Execution Instruction are explicitly separated.
- Human Final Approval transitions the workflow to Execution Instruction.
- ChatGPT does not request the same approval again after approval.
- Commit / Push / Tag remain independent Approval Units.
- Unapproved units remain Hold.
- Execution actor and Execution Evidence requirement are explicit.
- Existing Approval assets are revised without creating parallel architecture.
