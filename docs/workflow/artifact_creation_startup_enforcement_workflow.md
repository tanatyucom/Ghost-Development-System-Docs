# Artifact Creation Startup Enforcement Workflow

**Status:** Draft Workflow

**Last Updated:** 2026-07-17

## Purpose

This workflow defines the required pre-generation gate for managed GDS
artifacts.

Managed artifacts include Q, ADR, Rule, Workflow, Template, Roadmap,
Completion Report, Knowledge artifact, registry update, and other durable
repository documents.

## Standard Flow

```text
Artifact Generation Request
  -> Artifact Intent Classification
  -> Required Workflow Resolution
  -> Required Knowledge Resolution
  -> Canonical Repository / Template Verification
  -> Revision First Decision
  -> Constraint Check
  -> Gate Decision
  -> Draft / Recommendation / SCW
```

## Step 1: Artifact Intent Classification

Classify the requested artifact:

- Q.
- ADR.
- Rule.
- Workflow.
- Template.
- Roadmap.
- Completion Report.
- Knowledge artifact.
- Conversation Insight.
- Issa draft.
- Registry / index update.

If intent is ambiguous, apply SCW.

## Step 2: Required Workflow Resolution

Resolve the workflow that governs the artifact.

Examples:

- Q -> Q File Creation Workflow.
- Q revision -> Q Revision Addendum Workflow.
- ADR -> Architecture Promotion Lifecycle and ADR README.
- Completion Report -> Completion Report Workflow.
- Knowledge candidate -> Knowledge Preservation Gate / Knowledge Promotion Engine.
- Template -> Canonical Template Synchronization and template lifecycle.

## Step 3: Required Knowledge Resolution

Resolve required knowledge:

- AI Repository Index.
- Current Mission.
- Target Project Profile.
- Related Rule.
- Related Workflow.
- Related Architecture / ADR.
- Related Template.
- Existing canonical artifact.
- Related Completion Report.

## Step 4: Canonical Repository / Template Verification

Confirm the canonical source.

For Q creation:

```text
templates/Q_TEMPLATE.md
```

Rules:

- Do not use remembered template structure as canonical.
- Do not treat uploaded copies as current without freshness verification.
- Do not claim repository access failure without attempting an available
  repository or Raw URL check and recording the actual failure.

## Step 5: Revision First Decision

Before creating a new artifact, check whether an existing artifact should be
revised.

Record one of:

- `new_artifact_allowed`
- `revision_required`
- `addendum_required`
- `duplicate_found`
- `scw_required`

## Step 6: Constraint Check

Confirm:

- Working Repository.
- Target Project.
- Non-Target Project.
- Allowed edit scope.
- Forbidden edit scope.
- Commit / Push policy.
- Runtime / documentation boundary.
- Human Approval boundary.
- Validation commands.

## Step 7: Gate Decision

Decision values:

- `PASS`
- `PASS_WITH_LIMITATION`
- `BLOCK`
- `SCW_REQUIRED`

Draft generation may begin only when the gate is `PASS` or
`PASS_WITH_LIMITATION` with the limitation explicitly recorded.

## Required Evidence

Record:

- artifact intent;
- resolved workflow;
- resolved knowledge;
- canonical template source;
- revision first decision;
- constraint check result;
- gate decision;
- missing or conflicting evidence;
- SCW reason when applicable.

## Related Documents

- `docs/architecture/intent_aware_startup_enforcement.md`
- `docs/rules/artifact_creation_startup_enforcement_rules.md`
- `docs/workflow/q_file_creation_workflow.md`
- `docs/workflow/startup_completion_gate.md`
- `docs/workflow/intent_driven_workflow.md`
- `docs/architecture/command_center_architecture.md`
