# Q_GDS_WORKFLOW_RECOMMENDATION_APPROVAL_SIMPLIFICATION_001

## Title

Workflow Recommendation Approval Simplification

## Type

Revision

## Objective

Remove redundant approval questions that appear after Human Final Approval.

## Background

Current problematic flow:

```text
Completion Review
-> Workflow Recommendation
-> ChatGPT: "コミットしても良いですか？"
-> Human Approval
-> Execution Instruction
```

This causes unnecessary friction when the approval target is already visible in
the Workflow Recommendation and ChatGPT cannot execute the commit directly.

## Required Revision

After Human Final Approval:

- Do not ask `コミットしても良いですか？` again.
- Transition directly to Execution Instruction.

## Rule Addition

Workflow Recommendation acts as the Approval Request when it includes the
required visible approval fields.

After Human Final Approval, ChatGPT shall not request approval again and shall
only present Execution Instruction.

## Acceptance Criteria

- Duplicate approval prompt is removed.
- Workflow Recommendation can become the single approval point.
- Execution Instruction is displayed immediately after valid approval.
- Responsibility boundaries remain unchanged.
- Runtime remains unchanged.

## Out of Scope

- Runtime implementation
- MCP
- GUI
- Adapter changes
- Commit / Push / Tag without separate Human Approval
