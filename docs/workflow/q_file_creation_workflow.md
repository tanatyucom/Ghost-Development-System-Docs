# Q File Creation Workflow

**Version:** 1.0

**Last Updated:** 2026-07-13

## Purpose

This workflow defines how a Q moves from idea to saved request artifact before
AI execution.

## Flow

```text
Idea
  -> Decide Q ID
  -> Select Target Project
  -> Confirm Repository Context
  -> Fill Q Template
  -> Decide Commit / Push Policy
  -> Decide AI Repository Index Gate
  -> Save Task Artifact Workspace
  -> Verify request.md exists
  -> Human Approval
  -> Codex / AI Execution
```

## Step 1: Decide Q ID

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

## Step 3: Confirm Repository Context

Record:

```text
Working Repository:
Working Directory:
Preferred Shell:
```

AI should validate the actual repository root before implementation.

## Step 4: Fill Q Template

Use:

```text
templates/Q_TEMPLATE.md
```

Required sections follow:

- `docs/rules/q_file_template_rules.md`
- `docs/rules/q_file_artifact_standard.md`

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

## Step 6: Verify Before Execution

Before execution:

- `request.md` exists.
- Working Repository / Working Directory are explicit.
- Target / Non-Target scope is explicit.
- Commit / Push policy is explicit.
- Validation commands exist.
- AI Repository Index Update Gate exists.
- Safe Commit Set requirement exists.

## Step 7: Execute

AI may execute only within the approved scope.

Chat should contain a short summary and artifact paths, not the whole Q body.

## Completion

When work completes:

```text
Implementation
  -> Verification
  -> completion_report.md
  -> Safe Commit Set
  -> Human Review Decision
```

Do not commit unless the Q and user approval allow it.
