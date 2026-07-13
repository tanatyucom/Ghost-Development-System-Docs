# Q File Examples

## Purpose

This file gives good and bad examples for Q ID, Q filename, request workspace, addendum handling, and completion report linkage.

Rules come from:

- `docs/rules/q_file_artifact_standard.md`
- `docs/rules/q_file_naming_rules.md`
- `docs/rules/q_file_template_rules.md`

## Good: Full Task Workspace

A reusable, reviewable, AI-handoff, or Git-managed Q uses a workspace.

```text
docs/requests/gds/draft/GDS-QTEMPLATE-001_q_template_and_naming_standard/
  request.md
  notes.md
  completion_report.md
  attachments/
```

Why this is good:

- Q ID is stable.
- Project is visible.
- Status is visible.
- `request.md` is the authoritative Q.
- `completion_report.md` stays beside the source Q.
- Notes and attachments remain traceable.

## Good: Simple File Form

A small Q that does not need a workspace yet may use a single Markdown file.

```text
docs/requests/gds/draft/Q_GDS-QTEMPLATE-001_q_template_and_naming_standard_JP.md
```

Why this is good:

- The filename starts with `Q_`.
- The Q ID is visible.
- The topic is purpose-oriented.
- The language suffix is visible.
- No date is used as the default identity.

## Bad: Date As Default Identity

```text
docs/requests/gds/draft/2026-07-13_gds_update.md
```

Why this is bad:

- The topic is too vague.
- The Q identity depends on date instead of Q ID.
- The filename does not show whether this is template, rule, workflow, or review work.
- Later updates would create rename pressure.

## Good: Date Exception

Date is acceptable when date is the primary identity.

```text
docs/requests/gds/completed/2026-07-13_repository_migration_snapshot.md
```

Why this is acceptable:

- The artifact is a date-specific snapshot.
- The date is part of the meaning, not just creation time.

## Good: Addendum For Small Scope Extension

```text
docs/requests/gds/review/GDS-KNOWLEDGE-SUGGESTION-001_context_aware_assistant/
  request.md
  addendum_v1.1.md
  completion_report.md
```

Use an addendum when the original objective is unchanged and the user adds a narrow requirement.

Example:

```text
Add Daily Knowledge Source Review to the already approved Context-Aware Knowledge Suggestion Assistant proposal.
```

## Bad: New Q For Every Clarification

```text
Q_GDS-KNOWLEDGE-SUGGESTION-001_context_aware_assistant_JP.md
Q_GDS-KNOWLEDGE-SUGGESTION-002_context_aware_assistant_add_one_line_JP.md
Q_GDS-KNOWLEDGE-SUGGESTION-003_context_aware_assistant_fix_wording_JP.md
```

Why this is bad:

- Small clarifications fragment the history.
- Reviewers must reconstruct one decision from many files.
- The original Q and completion report become harder to connect.

## Good: New Q For Different Objective

Create a new Q when the objective changes materially.

```text
Q_GDS-COMMAND-CENTER-001_command_center_architecture_specification_JP.md
Q_GDS-COMMAND-CENTER-002_command_center_minimal_prototype_JP.md
```

Why this is good:

- Architecture specification and prototype implementation have different risk, scope, validation, and deliverables.
- Each Q can carry its own completion report and Safe Commit Set.

## Bad: Missing Repository Context

```text
# Fix the docs

Please update the template and commit.
```

Why this is bad:

- Working Repository is missing.
- Target Project is missing.
- Non-Target Project is missing.
- Commit policy is ambiguous.
- Scope and Out of Scope are missing.
- AI may edit the wrong repository.

## Good: Repository Context

```text
Working Repository: Ghost-Development-System-Docs
Working Directory: C:\GitHub\Ghost-Development-System-Docs
Target Project: Ghost Development System
Non-Target Project: GameGhost
Allowed Edit Scope: GDS documentation only
Forbidden Edit Scope: GameGhost, runtime DB, production data
Commit: Do not execute
Push: Do not execute
```

Why this is good:

- Repository confusion is prevented.
- GameGhost is protected as reference-only.
- Commit and push cannot happen silently.

## Good: Completion Report Linkage

```text
Source Q File:
docs/requests/gds/completed/GDS-QTEMPLATE-001_q_template_and_naming_standard/request.md

Completion Report:
docs/requests/gds/completed/GDS-QTEMPLATE-001_q_template_and_naming_standard/completion_report.md

Safe Commit Set:
- docs/rules/q_file_naming_rules.md
- docs/rules/q_file_template_rules.md
- docs/workflow/q_file_creation_workflow.md
- docs/workflow/q_revision_addendum_workflow.md
- templates/Q_TEMPLATE.md
```

Why this is good:

- Source request and report are paired.
- Changed files are reviewable.
- Safe Commit Set is explicit.
- The completion report can be audited later.
