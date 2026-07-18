# Q_GDS_APPROVAL_REQUEST_UX_REVISION_001

## Title

Approval Request UX Revision

## Type

Revision

## Objective

Improve Approval Request and Execution Instruction wording so it matches the
actual operational workflow.

## Background

The previous wording could be misunderstood as ChatGPT directly instructing
Codex.

Actual flow:

```text
ChatGPT -> Human -> Codex
```

Execution Instructions are presented to the human. The human then requests
execution from Codex or the approved execution actor.

## Required Revision

Replace wording that implies direct ChatGPT-to-Codex command behavior, such as:

```text
ChatGPT will issue an Execution Instruction and Codex will execute the Commit.
```

Use human-facing wording such as:

```text
Commit OKです。
次に、人間側からCodexへCommit実行を依頼してください。
```

For Commit and Push:

```text
CommitとPushはOKです。
次に、人間側からCodexへCommitとPushの実行を依頼してください。
```

## Requirements

- Clarify the audience is Human.
- Preserve responsibility boundaries.
- Do not create a parallel approval architecture.
- Do not implement runtime changes.
- Update related templates and verification checklists if necessary.

## Acceptance Criteria

- Approval Request wording is revised.
- Execution Instruction wording is revised.
- Existing Approval workflow remains valid.
- Repository consistency is maintained.

## Out of Scope

- Runtime
- MCP
- GUI
- Adapter implementation
- Commit / Push / Tag without separate Human Approval
