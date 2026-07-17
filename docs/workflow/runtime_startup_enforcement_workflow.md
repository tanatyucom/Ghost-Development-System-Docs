# Runtime Startup Enforcement Workflow

**Status:** Draft Workflow

**Last Updated:** 2026-07-17

## Purpose

This workflow defines how Runtime Startup Enforcement executes before managed
artifact generation.

The workflow is intended for future Command Center, Template Engine, Artifact
Pipeline, or automation boundary components. It is not an implementation plan
for autonomous repository modification.

Evidence produced by this workflow should follow
`docs/architecture/runtime_startup_enforcement_evidence_specialization.md`.

## Standard Flow

```text
Artifact Request
  -> Runtime Startup Enforcement
  -> State Machine Execution
  -> Evidence Record
  -> Gate Decision
  -> Allowed Next Step / Pending Action / Stop
```

## Step 1: Receive Request

Input may come from:

- user message;
- Q file;
- Pending Action;
- Command Center request;
- Template Engine request;
- Artifact Pipeline request.

Required input:

- target project;
- working repository;
- artifact intent or user intent;
- known constraints;
- Human Approval state.

If the input is missing the target repository or artifact intent, continue only
far enough to request clarification.

## Step 2: Create Startup Execution ID

Create an execution identifier for traceability.

Recommended format:

```text
RSE-YYYYMMDD-HHMMSS-<short-id>
```

The ID should be stored with evidence, logs, and Completion Report references.

## Step 3: Classify Artifact Intent

Classify the request into one of the supported managed artifact intents:

- Q creation;
- Q revision;
- ADR;
- Rule;
- Workflow;
- Template;
- Roadmap;
- Completion Report;
- Knowledge artifact;
- Registry / index update;
- other managed repository artifact.

If classification is ambiguous, return `SCW_REQUIRED`.

## Step 4: Resolve Required Workflow

Resolve the governing workflow.

Examples:

| Intent | Workflow |
| --- | --- |
| Q creation | `docs/workflow/q_file_creation_workflow.md` |
| Q revision | `docs/workflow/q_revision_addendum_workflow.md` |
| Completion Report | `docs/workflow/completion_report_workflow.md` |
| Template revision | `docs/workflow/template_lifecycle.md` |
| ADR | `docs/workflow/architecture_promotion_lifecycle.md` |

If no workflow can be resolved, return `BLOCK` or `SCW_REQUIRED`.

## Step 5: Resolve Required Knowledge

Resolve required knowledge sources:

- AI Repository Index;
- Current Mission or Current Q;
- Target Project Profile;
- related Rules;
- related Workflows;
- related Architecture / ADR;
- canonical Template;
- existing artifact directory;
- related Completion Reports.

Missing non-critical knowledge may produce `PASS_WITH_LIMITATION`.
Missing critical knowledge produces `BLOCK` or `SCW_REQUIRED`.

## Step 6: Verify Repository

Verify:

- actual repository root;
- declared Working Repository;
- declared Working Directory;
- target / non-target repository boundary;
- canonical source availability;
- dirty workspace risk when relevant.

Repository verification may read state. It must not mutate state.

## Step 7: Verify Template

Verify:

- canonical template path;
- template exists;
- template version or last updated marker when available;
- uploaded copy freshness when applicable;
- template mismatch or duplicate template risk.

For Q creation, the canonical template is:

```text
templates/Q_TEMPLATE.md
```

## Step 8: Decide Revision First

Return one of:

- `new_artifact_allowed`
- `revision_required`
- `addendum_required`
- `duplicate_found`
- `scw_required`

Runtime must prefer revision or addendum when a canonical artifact already
exists and the user intent is a change to that artifact.

## Step 9: Run Constraint Check

Confirm:

- scope;
- out of scope;
- forbidden edits;
- commit / push policy;
- Human Approval boundary;
- validation commands;
- runtime versus documentation boundary.

Any conflict that would make execution unsafe returns `BLOCK`.

## Step 10: Build Evidence Record

Build the runtime evidence model defined in
`docs/architecture/runtime_startup_enforcement.md`.

The evidence record must include:

- artifact intent;
- required workflow;
- required knowledge;
- repository verification;
- template verification;
- revision first decision;
- constraint check;
- gate decision;
- reason codes;
- missing or conflicting evidence;
- SCW reason when applicable.

## Step 11: Decide Gate

Gate values:

```text
PASS
PASS_WITH_LIMITATION
BLOCK
SCW_REQUIRED
```

Generation behavior:

- `PASS`: artifact generation may proceed.
- `PASS_WITH_LIMITATION`: artifact generation may proceed only with visible
  limitation and next action.
- `BLOCK`: artifact generation must not proceed.
- `SCW_REQUIRED`: stop and wait for human decision.

## Step 12: Return Runtime Decision

Return:

- gate decision;
- allowed next step;
- pending action;
- evidence record;
- display summary;
- Completion Report linkage.

## Runtime Output Examples

### PASS

```yaml
gate_decision: PASS
allowed_next_step: generate_artifact_draft
reason_codes:
  - INTENT_CLASSIFIED
  - WORKFLOW_RESOLVED
  - KNOWLEDGE_RESOLVED
  - REPOSITORY_VERIFIED
  - CANONICAL_TEMPLATE_VERIFIED
  - REVISION_FIRST_DECIDED
  - CONSTRAINT_CHECK_PASSED
```

### PASS_WITH_LIMITATION

```yaml
gate_decision: PASS_WITH_LIMITATION
allowed_next_step: generate_artifact_draft_with_limitation
limitation: "Related ADR not found; workflow and template are sufficient."
next_action: "Record limitation in Completion Report."
```

### BLOCK

```yaml
gate_decision: BLOCK
allowed_next_step: none
reason_codes:
  - TEMPLATE_NOT_VERIFIED
recovery: "Confirm canonical template before generation."
```

### SCW_REQUIRED

```yaml
gate_decision: SCW_REQUIRED
allowed_next_step: ask_human
scw_reason: "User intent conflicts with repository boundary."
question: "Should this revise the existing artifact or create a new Q?"
```

## Completion Report Requirements

When Runtime Startup Enforcement is used, the Completion Report should record:

- startup execution ID;
- gate decision;
- reason codes;
- limitation / block / SCW reason;
- evidence artifact or log path;
- whether Human Approval was required;
- final allowed next step.

## Related Documents

- `docs/architecture/runtime_startup_enforcement.md`
- `docs/architecture/runtime_startup_enforcement_evidence_specialization.md`
- `docs/architecture/intent_aware_startup_enforcement.md`
- `docs/workflow/artifact_creation_startup_enforcement_workflow.md`
- `docs/architecture/command_center_architecture.md`
- `templates/Q_TEMPLATE.md`
- `templates/completion_report_template.md`
