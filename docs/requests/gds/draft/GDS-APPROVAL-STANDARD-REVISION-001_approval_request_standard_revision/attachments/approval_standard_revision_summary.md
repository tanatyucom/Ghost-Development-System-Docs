# Approval Standard Revision Summary

## Purpose

Close the governance gap where Codex or ChatGPT may reach a completion state
without displaying a clear Approval Request Block.

## Core Boundary

```text
Codex -> Repository Recommendation
ChatGPT -> Workflow Recommendation / Completion Review
Human -> Final Approval
Codex / Adapter -> Governed Execution
Execution Evidence -> Execution Proof
```

## Key Revision

- Recommendation is not approval.
- Approval is not execution.
- Execution is not complete without evidence.
- Commit, push, tag, release, delete, and canonical promotion are independent
  Approval Units.

## Template Decision

Use one common Approval Request Block. Do not create separate Codex and ChatGPT
templates unless a later runtime Q proves the need.
