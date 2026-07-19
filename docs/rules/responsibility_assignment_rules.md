# Responsibility Assignment Rules

**Status:** Draft Rule

**Last Updated:** 2026-07-18

## Purpose

These rules define how GDS assigns responsibility when a new workflow,
architecture component, actor, adapter, template, or execution surface is
introduced.

The governing principle is:

```text
責務は機能ではなく、権限で決める。
```

Equivalent architecture wording:

```text
Responsibility follows execution authority.
```

## Core Rule

Assign responsibility to the actor that has authority to execute, delegate, or
govern the operation.

Do not assign a responsibility only because an actor can describe, review,
summarize, or recommend the operation.

## Approval Request Rule

Approval Request for a mutation or external side effect must be displayed by
the Execution Actor or the governed execution surface that owns authority for
that operation.

Review Actor may recommend, review, or guide. Review Actor must not request
execution permission for an operation it cannot execute or delegate through a
governed path.

## Multi-Stage Promotion Responsibility Rule

In AI Multi-Stage Promotion Workflow, responsibility remains stage-specific:

- Human owns vision and final approval.
- GDS owns canonical governance and architecture boundary.
- Codex owns scoped review, validation, implementation, and evidence only when
  the current Q authorizes that work.
- Command Center owns orchestration display and next-action recommendation.
- Repository owns canonical truth.

Command Center stage visibility must not be treated as execution authority.
Codex review or validation must not be treated as Human Approval.
Human approval applies only to the visible Pending Action or Approval Unit.

## Required Assignment Checks

Before adding or changing a responsibility, confirm:

1. Does this operation change state?
2. Does this operation produce an external side effect?
3. Which actor has execution authority?
4. Is Human Approval required?
5. Which actor displays the Approval Request?
6. Which actor generates Execution Evidence?
7. Are Review Actor and Execution Actor mixed?

If any answer is unclear, use SCW and do not proceed to execution.

## Registry Requirement

For Approval Request, execution, mutation, delegation, external side effect, or
Execution Evidence responsibilities, check the Execution Authority Registry:

```text
docs/registries/execution_authority_registry.yaml
```

The registry must identify:

- actor ID;
- Approval Unit;
- execution actor;
- Approval Request actor;
- repository / resource scope;
- Human Approval requirement;
- Evidence Responsibility;
- SCW conditions.

If the registry cannot resolve the actor, authority, scope, or evidence owner,
use SCW.

## Review Actor Boundary

Review Actor may own:

- Completion Review
- Independent Review
- Architecture / Design Review
- risk identification
- execution guidance

Review Actor must not own:

- Approval Request for a repository mutation;
- direct Git operation execution;
- runtime mutation;
- external side effect execution;
- execution evidence for an operation it did not execute.

## Execution Actor Boundary

Execution Actor may own:

- Repository Recommendation
- Workflow Recommendation
- Approval Request
- readiness check
- execution or governed delegation
- Execution Evidence
- failure / abort reporting

Execution Actor must not:

- bypass Human Approval;
- expand hidden scope;
- treat recommendation as approval;
- mark execution complete without evidence;
- continue when authority is unknown.

## Human Authority Boundary

Human owns:

- Final Approval;
- rejection;
- hold;
- scope change approval;
- high-risk override.

Human approval applies only to the latest visible Approval Request, current
repository state, and visible Approval Units.

## SCW Conditions

Use SCW when:

- authority cannot be proven;
- Review Actor and Execution Actor are mixed;
- Approval Request issuer is not the execution-capable actor;
- Approval Unit and Execution Unit do not match;
- evidence producer is unclear;
- repository or runtime mutation would happen without a valid approval path.

## Prohibited Patterns

- A Review Actor asks `Commitしますか？` when it cannot commit or delegate
  through a governed execution path.
- A recommendation is treated as Human Final Approval.
- An Approval Request omits the actor that will execute or delegate.
- Execution Evidence is claimed by an actor that only reviewed the work.
- Unknown authority is treated as permission.

## Related Documents

- `docs/architecture/authority_driven_responsibility_principle.md`
- `docs/architecture/execution_authority_registry.md`
- `docs/registries/execution_authority_registry.yaml`
- `docs/workflow/authority_validation_gate.md`
- `docs/rules/approval_request_rules.md`
- `docs/architecture/responsibility_boundary.md`
- `docs/architecture/approval_request_intent_queue_execution_evidence.md`
- `docs/architecture/governed_execution_adapter_foundation.md`
- `docs/architecture/ai_multi_stage_promotion_workflow.md`
- `templates/review_checklist.md`
- `templates/approval_request_block_template.md`
