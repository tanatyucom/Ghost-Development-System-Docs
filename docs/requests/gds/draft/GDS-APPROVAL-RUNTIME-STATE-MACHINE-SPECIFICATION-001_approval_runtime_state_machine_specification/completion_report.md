# Completion Report: GDS-APPROVAL-RUNTIME-STATE-MACHINE-SPECIFICATION-001

## Summary

Added the canonical Approval Runtime State Machine specification for GDS.

The new specification defines approval as a governed runtime state transition
instead of conversational wording alone. It separates recommendation, human
approval, execution instruction, action execution, and execution evidence so
Commit, Push, and Tag approval units cannot accidentally authorize each other.

## Changed Files

- `docs/architecture/approval_runtime_state_machine.md`
- `docs/architecture/README.md`
- `docs/README.md`
- `docs/architecture/approval_request_intent_queue_execution_evidence.md`
- `docs/architecture/runtime_intent_queue_resolver.md`
- `docs/architecture/platform_execution_evidence_contract.md`
- `docs/rules/approval_request_rules.md`
- `docs/rules/runtime_intent_resolution_rules.md`
- `docs/standards/execution_result_evidence_contract.md`
- `docs/workflow/runtime_intent_queue_resolution_workflow.md`
- `examples/approval_runtime_state_machine_examples.md`
- `examples/README.md`
- `docs/requests/gds/draft/GDS-APPROVAL-RUNTIME-STATE-MACHINE-SPECIFICATION-001_approval_runtime_state_machine_specification/request.md`
- `docs/requests/gds/draft/GDS-APPROVAL-RUNTIME-STATE-MACHINE-SPECIFICATION-001_approval_runtime_state_machine_specification/attachments/approval_runtime_state_machine_validation_cases.md`
- `docs/requests/gds/draft/GDS-APPROVAL-RUNTIME-STATE-MACHINE-SPECIFICATION-001_approval_runtime_state_machine_specification/completion_report.md`
- `docs/ai_repository_index.md`
- `reports/repository_quality_report.md`

## Canonical Runtime Entity Model

Defined:

- Approval Request.
- Approval Unit.
- Repository State Snapshot.
- Human Approval Record.
- Execution Request / Instruction.
- Execution Evidence.

## Canonical State Model

Defined separate state families:

- Approval Request State.
- Approval Unit Recommendation State.
- Approval Unit Approval State.
- Approval Unit Execution State.
- Workflow Current Step.

Recommendation, approval, execution, and evidence are not collapsed into one
field.

## Valid Transition Table

The specification includes canonical valid transitions for:

- recommendation creation;
- completion review;
- approval request creation;
- human approval;
- partial approval;
- rejection;
- invalidation;
- supersession;
- execution instruction;
- execution start;
- execution success;
- execution failure;
- execution unknown;
- cancellation;
- completion.

## Invalid Transition Table

The specification explicitly prohibits transitions such as:

- `Recommended -> Completed` without Human Approval and Execution Evidence.
- `Pending Human Approval -> Executing` without a Human Approval Record.
- `Commit Approved -> Push Approved` by inference.
- `Expired -> Approved` without a new request.
- `Invalidated -> Executing`.
- `Failed -> Succeeded` without new execution evidence.
- `Not Applicable -> Approved`.
- `Rejected -> Execution Pending`.

## Human Approval Binding Rules

Human wording such as `お願いします`, `OK`, `承認します`, `コミットお願いします`,
`Pushもお願いします`, and `全部お願いします` may bind only when the current
Approval Request, repository, branch, request ID, visible Approval Units,
freshness state, and scope are unambiguous.

Generic approval cannot approve absent, hidden, held, stale, expired,
invalidated, superseded, or ambiguous units.

## Repository State Fingerprint And Invalidation Rules

The specification defines a semantic repository fingerprint including
repository identity, branch, HEAD, index state, working-tree diff, untracked
scope, Safe Commit Set, upstream state, relevant remote state, tag target, and
required validation evidence.

Repository-state invalidation takes precedence over elapsed time.

## Approval Unit Parent-State Derivation

Parent Approval Request state is derived from child Approval Units. Examples
include all pending, some approved, all approved, rejected, invalidated, failed,
all completed, all not applicable, and cancelled states.

## Execution Evidence Binding

Execution Evidence must bind to one Approval Unit. Commit SHA evidence completes
Commit only; it does not complete Push or Tag.

## Duplicate / Unknown Execution Handling

Duplicate approvals must not expand scope. Duplicate execution requests must
first check existing evidence and current repository state. Unknown execution
results require evidence inspection and SCW rather than blind retry.

## Persistence And Audit Direction

The runtime direction is repository-first, recoverable, and auditable. The
specification defines canonical state, derived views, recovery, corruption
handling, retention direction, and an append-only event model.

## Machine-Readable Schema Direction

The specification includes YAML-style schema direction for Approval Request,
Approval Unit, Repository State Snapshot, Human Approval Record, Execution
Instruction, Execution Evidence, and transition definitions.

## Conceptual Runtime API Contract

Conceptual operations are documented, including:

- `create_approval_request`
- `get_pending_approval_requests`
- `review_approval_request`
- `record_human_approval`
- `invalidate_approval_request`
- `issue_execution_instruction`
- `start_execution`
- `record_execution_evidence`
- `complete_approval_unit`
- `supersede_approval_request`
- `reconcile_runtime_state`

No API implementation was added.

## SCW Integration

The specification defines SCW triggers for ambiguous approval, missing pending
request, multiple matches, stale state, unknown execution result, conflicting
evidence, mixed scope, failed validation, held-unit approval, invalidated-unit
execution, inconsistent parent / child states, duplicate tag, and conflicting
remote state.

## Validation Results

- `git diff --check`: PASS.
  - Note: Git reported CRLF-to-LF normalization warnings for
    `docs/ai_repository_index.md`, `examples/README.md`, and
    `reports/repository_quality_report.md`; no whitespace errors were reported.
- Targeted mojibake marker search for changed / new public documentation:
  PASS, no matches.
- Broad mojibake marker search: existing intentional examples were found in
  `docs/rules/utf8_read_rules.md`; not a new corruption finding.
- `python scripts/generate_ai_repository_index.py --validate`: PASS,
  718 Markdown files indexed.
- `python scripts/validate_encoding_regression.py --all`: PASS.
- `python scripts/repository_quality_audit.py`: PASS, Repository Quality Audit
  Green, 12 passed, 0 warnings, 0 errors.

## Required Validation Cases Added Or Revised

- Added `examples/approval_runtime_state_machine_examples.md`.
- Added `attachments/approval_runtime_state_machine_validation_cases.md`.

The examples cover all 17 required validation cases.

## Remaining Issues

- Runtime storage format is intentionally not implemented.
- Natural-language parsing is intentionally not implemented.
- Fixed expiry duration is intentionally left as a policy hook.
- Production API / DB / GUI / MCP integration remain future work.

## Repository Recommendation

Recommended for commit after human review.

Commit / Push / Tag were not executed.

## Suggested Commit Message

```text
docs: define approval runtime state machine
```
