# Q File Creation Workflow

**Version:** 2.0

**Last Updated:** 2026-07-24

## Purpose

This workflow defines how a Q moves from idea to saved request artifact before
AI execution.

## Flow

```text
Idea
  -> Artifact Creation Startup Enforcement
  -> Decide Q ID
  -> Select Target Project
  -> Fill Canonical Q Template v3.0
  -> Complete Mandatory Execution Context
  -> Decide Commit / Push Policy
  -> Decide AI Repository Index Gate
  -> Save Task Artifact Workspace
  -> Verify request.md exists
  -> Template Validation
  -> Approved Q
  -> Codex / AI Execution
```

## Step 1: Decide Q ID

Before deciding a Q ID, run Artifact Creation Startup Enforcement.

Confirm:

- artifact intent is Q creation or Q revision;
- `docs/workflow/q_file_creation_workflow.md` is the required workflow;
- `templates/Q_TEMPLATE.md` is the canonical template;
- related rules, workflow, architecture, roadmap, and Current Mission were
  checked;
- Revision First does not require updating an existing Q or addendum instead;
- Constraint Check is complete.

Details follow `artifact_creation_startup_enforcement_workflow.md`.

Use `docs/rules/q_file_naming_rules.md`.

New official Qs should use:

```text
<PROJECT>-<DOMAIN>-<NUMBER>
```

Do not use date as the default identity.

## Step 2: Select Target Project

Record:

- Target Project.
- Non-Target Project.
- Allowed Edit Scope.
- Forbidden Edit Scope.

When GameGhost is reference only, write:

```text
GameGhost: Do not edit
```

## Step 3: Complete Mandatory Execution Context

Record before Issue:

```text
Repository Name / Type / Purpose / ID / Role
Workspace Root / Repository Root / Execution Root / Working Directory / Boundary
Expected Base Branch / Expected Remote or Tracking Branch
Execution Mode / Mutation Authority
Priority / Risk
Approval Scope: Repository / Workflow / Operation / Capability
Commit / Push / Tag / Release Policy
Required Capability Matrix
```

Do not infer missing values. Missing context returns `ISSUE_NG`; unsafe or
unresolvable conflict returns `SCW_REQUIRED`.

## Step 4: Fill Q Template

Use:

```text
templates/Q_TEMPLATE.md
```

Required sections follow:

- `docs/rules/q_file_template_rules.md`
- `docs/rules/q_file_artifact_standard.md`

The Q Template includes Artifact Creation Startup Enforcement Evidence.

Before filling the main Q body, record:

- Artifact Intent.
- Required Workflow.
- Required Knowledge.
- Canonical Repository Verification.
- Canonical Template Verification.
- Revision First Decision.
- Constraint Check.
- Gate Decision.
- Gate Reason Codes.
- Missing / Conflicting Evidence.
- SCW Reason, when applicable.

Gate Decision values:

```text
PASS
PASS_WITH_LIMITATION
BLOCK
SCW_REQUIRED
```

`PASS_WITH_LIMITATION` requires limitation evidence. `BLOCK` and
`SCW_REQUIRED` stop drafting or execution until resolved.

## Step 5: Save Task Artifact Workspace

Preferred workspace:

```text
docs/requests/<project>/<status>/<Q_ID>_<short_topic>/
  request.md
  notes.md
  completion_report.md
  attachments/
```

The authoritative Q is:

```text
request.md
```

## Step 6: Template Validation And Issue

Run `templates/q_template_validation_checklist.md` after saving the draft and
before issuing it as executable.

```text
ISSUE_OK       -> Human Approval -> Approved Q
ISSUE_NG       -> return to Draft
SCW_REQUIRED   -> Stop / Call / Wait
```

Validate each repository separately. Capability availability is evidence, not
permission. Material repository-state or scope changes invalidate the related
approval.

## Step 7: Verify Before Execution

Before execution:

- `request.md` exists.
- Template Validation result is `ISSUE_OK`.
- Repository identity, workspace boundary, and Working Directory are explicit.
- Target / Non-Target scope is explicit.
- Commit / Push / Tag / Release policy is explicit.
- Validation commands exist.
- AI Repository Index Update Gate exists.
- Safe Commit Set requirement exists.

## Step 8: Execute

AI may execute only within the approved scope.

```text
Capability Verification
  -> Repository Verification
  -> Execution Context Validation
  -> Startup Report
  -> Execution
```

Chat should contain a short summary and artifact paths, not the whole Q body.

## Completion

When work completes:

```text
Implementation
  -> Verification
  -> Completion Review
  -> Safe Commit Set
  -> STOP
```

Do not commit unless the Q and user approval allow it.
