# Repository Action Status and Recommendation Model

**Status:** Draft Standard

**Last Updated:** 2026-07-18

## Purpose

This standard defines how GDS reports governed repository actions so humans and
AI agents do not confuse recommendation, approval, execution, and evidence.

It applies to:

- Commit.
- Push.
- Tag.
- Release.
- Promotion.
- SDK Export.
- Other governed execution actions.

## Core Principle

```text
Recommendation describes what should happen.
Approval authorizes what may happen.
Execution Status records what is happening or has happened.
Execution Evidence proves what happened.
```

Repository mutation must remain governed by explicit Human Approval.

## Required Separation

Reports must keep these concepts separate:

| Concept | Meaning | Must Not Be Confused With |
| --- | --- | --- |
| Execution Status | Current or final state of an action. | Recommendation or approval. |
| Repository Recommendation | Evidence-backed suggestion from Codex / repository-aware review. | Human Approval or execution instruction. |
| Approval Status | Whether a human approval unit is requested, approved, rejected, expired, or invalidated. | Recommendation or execution result. |
| Suggested Action Details | Proposed commit message, command, tag name, release name, or export target. | Evidence that action happened. |
| Execution Evidence | Immutable proof of completed or failed execution. | Suggested details or approval text. |

## Standard Reporting Order

Completion Reports and chat-facing completion summaries should use this order
when repository actions are relevant:

1. Completion Review Result.
2. Execution Status.
3. Repository Recommendation.
4. Approval Status.
5. Suggested Action Details.
6. Approval Request.
7. Execution Evidence.

Execution Status appears before recommendations so the reader first sees what
has actually happened.

## Mandatory Execution Status Fields

Every Completion Report should include explicit status for relevant governed
actions.

Minimum fields:

- Commit Status.
- Push Status.
- Tag Status.
- Release Status, when release is in scope.
- Promotion Status, when canonical promotion is in scope.
- SDK Export Status, when SDK export is in scope.

If an action is not in scope, use `Not Applicable`.

## Allowed Execution Status Values

Use these values for action execution state:

- `Not Evaluated`: action relevance has not been checked.
- `Not Applicable`: action is outside the current scope.
- `Not Executed`: action has not been executed.
- `Executing`: action is currently being executed.
- `Completed`: action completed and has evidence.
- `Failed`: action was attempted and failed; evidence or error must be shown.
- `Blocked`: action cannot proceed because a gate, scope, validation,
  authority, approval, or repository condition blocks it.

`Completed` requires valid Execution Evidence.

## Allowed Recommendation Values

Repository Recommendation approval units use:

- `Recommended`
- `Hold`
- `Not Applicable`

Do not use `Approved` in Repository Recommendation.

## Allowed Approval Status Values

Use these values for approval state:

- `Not Requested`: no approval request was presented.
- `Pending Human Approval`: visible approval request is current.
- `Approved`: human approved the specific visible approval unit.
- `Rejected`: human rejected the specific visible approval unit.
- `Expired`: approval request expired by policy or context.
- `Invalidated`: repository state, scope, validation, or recommendation changed.
- `Superseded`: a newer approval request replaced it.
- `Not Applicable`: action does not require approval in this scope.

Approval state is not execution state.

## Suggested Action Details

Suggested action details are proposals for non-executed or not-yet-approved
actions.

Examples:

- Suggested Commit Message.
- Suggested Command.
- Suggested Tag Name.
- Suggested Release Name.
- Suggested SDK Export Target.

Rules:

- Suggested details must appear after Execution Status.
- Suggested details must be clearly labeled as proposals.
- Suggested Commit Message alone is never execution evidence.
- After an action is completed, prefer execution evidence over suggested
  details.
- If retaining a suggested message after completion is useful for audit, label
  it as historical input, not current recommendation.

## Execution Evidence

Completed or failed actions must include evidence.

Minimum evidence by action:

| Action | Required Evidence |
| --- | --- |
| Commit | Commit ID / SHA, subject, repository, branch, command or adapter, before / after state. |
| Push | Remote, branch, pushed commit range or SHA, command or adapter, result. |
| Tag | Tag name, target commit, tag creation result, tag push result when applicable. |
| Release | Release ID / URL / version, target commit or tag, publication result. |
| Promotion | Source artifact, target canonical path, approval record, resulting registry / document change. |
| SDK Export | Source revision, export artifact path or package ID, checksum or verification result when available. |

Approval text alone is not execution evidence.

## Failed Versus Blocked

Use `Failed` when execution was attempted and did not succeed.

Use `Blocked` when execution was not attempted because a precondition failed.

Examples:

- `Failed`: `git push` was run and rejected by remote.
- `Blocked`: push was not run because Push approval was missing.
- `Blocked`: commit was not run because Safe Commit Set was mixed.
- `Failed`: tag creation command was run and returned an error.

## Partial Execution

Each approval unit must report its own status.

Example:

```text
Commit Status: Completed
Commit ID: abcdef1

Push Status: Not Executed
Tag Status: Not Executed
```

Do not summarize partial execution as simply `Completed` unless every requested
approval unit has evidence-backed completion.

## Compatibility With Command Center

Command Center and Working Context views should reuse this model.

Command Center may display:

- Execution Status.
- Repository Recommendation.
- Approval Status.
- Suggested Action Details.
- Execution Evidence.

It must not convert recommendation into approval, or approval into execution.

## Completion Report Compatibility

Older Completion Reports may include `Commit / Push Status` and `Suggested
Commit Message`. This remains understandable, but new reports should use the
standard order and explicit status values.

Backward-compatible mapping:

| Legacy Field | New Interpretation |
| --- | --- |
| Commit executed: No | Commit Status: Not Executed |
| Push executed: No | Push Status: Not Executed |
| Commit hash empty | No Commit Execution Evidence |
| Suggested Commit Message | Suggested Action Details / proposal |
| Commit executed: Yes + hash | Commit Status: Completed + Commit Evidence |

Existing historical reports do not need bulk rewrite unless they are being
actively revised.

## Review Questions

### Should Execution Status always appear before Repository Recommendation?

Yes. The first thing the reader should see is what actually happened.

### Should Suggested Commit Message be omitted after commit completion?

Usually yes. Completed actions should show execution evidence. If the suggested
message is retained, label it as historical input.

### How should no approval request be displayed?

Use:

```text
Approval Status
Commit: Not Requested
Push: Not Requested
Tag: Not Requested
```

### How should rejected or expired approval be represented?

Use `Rejected`, `Expired`, `Invalidated`, or `Superseded` per approval unit.
Execution Status should remain `Not Executed` or `Blocked` unless execution was
attempted.

### Which actions require immutable execution evidence?

Any completed or failed governed action that mutates repository, release,
registry, package, promotion, export, or external publication state.

## Non-Goals

This standard does not:

- approve repository mutation;
- implement Command Center UI;
- implement an Execution Adapter;
- change repository history;
- bypass Human Approval;
- modify GameGhost.

## Related Documents

- `templates/completion_report_template.md`
- `templates/repository_recommendation_template.md`
- `templates/approval_request_block_template.md`
- `docs/rules/approval_request_rules.md`
- `docs/architecture/approval_runtime_state_machine.md`
- `docs/architecture/platform_execution_evidence_contract.md`
- `docs/architecture/command_center_working_context_model.md`
- `examples/repository_action_status_examples.md`
