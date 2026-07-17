# ADR-GDS-006 Approval State and Execution State Separation

## Status

Proposed

## Date

2026-07-17

## Context

GDS has Completion Review, Repository Quality, Intent-Driven Workflow, Human
Approval First, and Platform Execution Evidence. However, live approval
conversations showed that these states can still be confused:

```text
Approval Accepted
!= Execution Completed
!= Evidence Collected
```

Natural-language inputs such as `お願いします`, `これ全てお願いします`, and
`お願いします。次のQファイルお願いします` require stateful interpretation.

## Decision

Treat Approval State and Execution State as separate platform concepts.

Approval State records what the human approved in visible scope.

Execution State records whether an authorized actor executed the operation and
whether evidence exists.

Bulk approval applies only to displayed Requested Operations and displayed
Recommended Follow-up Candidates.

## Consequences

- Commit, Push, Tag, and artifact creation need operation-specific prompts.
- Chained requests become an Intent Queue.
- Current actor execution authority must be checked before action.
- ChatGPT or any AI without local Git authority may prepare instructions but
  must not claim commit / push / tag completion without evidence.
- Platform Ready Review can test whether approval and execution are separated.

## Non-Goals

- No runtime implementation.
- No MCP server.
- No GUI.
- No automatic Git operation.
- No automatic commit / push / tag approval.

## Related Documents

- `docs/architecture/approval_request_intent_queue_execution_evidence.md`
- `docs/workflow/approval_request_intent_queue_workflow.md`
- `docs/rules/approval_request_rules.md`
- `templates/approval_request_block_template.md`
