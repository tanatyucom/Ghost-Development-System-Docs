# Startup Synchronization Review

## Current-State Architecture Map

```text
AI receives task
  -> Intent-Driven Workflow, when natural language intent needs routing
  -> Capability Verification, when capability or authority is uncertain
  -> AI Repository Index
  -> Current Q / Mission / Information Package
  -> Repository Root Validation
  -> Related Rules / Workflows / ADRs / Architecture / Templates
  -> Startup Checklist
  -> Startup Completion Evidence
  -> Startup Completion Gate
  -> Constraint Check / Scope confirmation
  -> Governed reasoning / artifact work
  -> Verification
  -> Completion Report, when required
  -> Pre-Response Verification Gate
  -> Final response
```

## Root Cause Summary

The repeated AI misunderstanding is best explained as:

```text
Definition exists, but the evidence contract was too easy to satisfy verbally.
```

Startup was already AI-facing and repository-first. However, the system did not
make Repository Context Evidence visible enough at each governed response
boundary. This allowed an AI session to infer the meaning of Startup from
conversation or memory instead of re-reading the current canonical assets.

## Commit Output Inconsistency

The Commit-output variation is caused by stale or incomplete response-state
resolution, not by missing commit rules.

The determining canonical assets are:

- `templates/repository_recommendation_template.md`
- `templates/workflow_recommendation_template.md`
- `templates/approval_request_block_template.md`
- `docs/workflow/pre_response_verification_gate.md`
- `docs/rules/approval_request_rules.md`
- `docs/architecture/approval_runtime_state_machine.md`
- `docs/registries/execution_authority_registry.yaml`
- `docs/registries/capability_authority_bindings.yaml`

Expected behavior:

```text
Repository Recommendation
  -> Workflow Recommendation
  -> Approval Request
  -> Human Approval
  -> Execution Instruction
  -> Execution Evidence
```

If the AI does not refresh workflow state and approval state, adjacent
Completion Reviews can incorrectly alternate between Recommendation, Approval
Request, and command output.

## Expected vs Actual Enforcement Matrix

| Expected behavior | Current canonical support | Enforcement strength before | Observed failure risk | Root cause | Implemented recommendation |
| --- | --- | --- | --- | --- | --- |
| Startup is AI-facing | `ai_startup_procedure.md`, `ai_startup_procedure_rules.md` | Medium | AI calls it a human checklist | Wording existed but was not emphasized at entry points | Added Repository-Aware AI Rule and root README clarification |
| Repository is Single Source of Truth | `ai_repository_index.md`, `ai_collaboration_rules.md`, `Q_TEMPLATE.md` | Medium | Chat memory overrides repository | Precedence was distributed | Added explicit precedence order |
| Startup proves repository access | `startup_completion_evidence.md` | Medium-low | AI says Startup PASS without source evidence | Evidence fields did not require context manifest-like details | Added Repository Context Evidence |
| Q creation opens canonical template | `Q_TEMPLATE.md`, artifact startup enforcement docs | High | AI uses remembered template | Already defined | No duplicate change; reinforced through evidence and response checklist |
| Task transitions refresh context | `repository_drift_prevention.md` as future candidate | Low | Architecture review context reused for commit approval | Refresh triggers were future / advisory | Added Freshness / Invalidation triggers |
| Completion response is consistent | Recommendation / approval templates and Pre-Response gate | Medium | Adjacent responses vary | Final response gate did not explicitly check stale repository / approval context | Added Pre-Response repository context freshness checks |
| Repository unavailable blocks confident output | `ai_repository_index.md`, startup gate | Medium | AI reports confident result without access | Limitation path existed but was not tied to response | Added BLOCK / SCW conditions |

## Machine-Readable Candidate Evaluation

| Candidate | Classification | Reason |
| --- | --- | --- |
| Startup Context Manifest | Future candidate | Useful, but current Q only needs documentation-level evidence fields. |
| Repository Context Requirement Registry | Future candidate | Valuable for automation, but would be premature without runtime validator design. |
| Pre-Response Repository Context Gate | Extend existing asset | Implemented by strengthening `pre_response_verification_gate.md`. |
| Startup Evidence Block | Extend existing asset | Implemented through Startup Completion Evidence and templates. |
| Freshness / Invalidation Rules | Extend existing asset | Implemented in Startup Evidence, Gate, and Procedure. |
| Validator | Future candidate | Requires separate schema/runtime review. |

## Test Case Results

| Case | Result | Evidence |
| --- | --- | --- |
| New Session Q Creation | PASS WITH STRENGTHENING | `Q_TEMPLATE.md` already requires canonical template synchronization; Startup evidence now records repository context and freshness. |
| Existing Definition Misclassified | PASS WITH STRENGTHENING | Startup is already AI-facing; root README and rules now make repository synchronization protocol explicit. |
| Adjacent Completion Reviews | PASS WITH STRENGTHENING | Recommendation / approval templates already exist; Pre-Response now checks stale repository, workflow, and approval context. |
| Repository Updated After Startup | PASS WITH STRENGTHENING | Freshness / Invalidation triggers added. |
| Repository Unavailable | PASS WITH STRENGTHENING | BLOCK / SCW behavior tied to missing repository context evidence. |
| Conflicting Template Copies | PASS | `Q_TEMPLATE.md` and artifact startup enforcement already make canonical template verification required. |

## Minimum Reliable Design

The smallest coherent improvement is:

- revise existing Startup wording;
- revise Startup Completion Evidence;
- revise Startup Completion Gate;
- revise AI Response Checklist / Response Verification;
- extend Pre-Response Verification;
- preserve supplied source inputs as request evidence;
- avoid creating a competing Startup architecture or runtime validator.

No runtime implementation was performed.
