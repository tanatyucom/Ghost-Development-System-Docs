# Q File Artifact Standard

**Version:** 1.3

**Last Updated:** 2026-07-13

## Purpose

This document standardizes how Q files are generated, saved, named, reused, moved through workflow status, and connected to completion reports.

It extends Artifact First for Q-specific work and delegates the detailed ID and filename rules to `docs/rules/q_file_naming_rules.md`.

## Core Standard

Q files should be generated and saved as managed artifacts before they are used for Codex, Gemini, Claude, ChatGPT, or human review.

The chat body should not be the authoritative copy of a Q file.

The first action after creating a reusable, reviewable, AI-handoff, human-approval, or Git-managed Q is to save it into the Task Artifact Workspace. Implementation must not start from an unsaved Q when the Q is expected to be reused, reviewed, tracked in Git, or connected to a completion report.

Chat should contain:

- a short summary;
- the saved Q file path or download link;
- related artifact paths, when any;
- verification notes.

## Standard Save Location

Save official Q file artifacts under:

```text
docs/requests/
```

A Q that exists only as a chat message, download, clipboard copy, or sandbox-local file is not an official executable task until it has been saved in the correct workspace path.

Reason:

- `docs/requests/` is broad enough to store Q files, task workspaces, AI requests, notes, attachments, and related completion report artifacts.
- It keeps generated request artifacts separate from reusable templates.
- It keeps real operational artifacts separate from examples.
- It is easier to browse than a deeper path such as `docs/artifacts/q/`.

## Canonical Q Identity

New official Q artifacts should use a stable Q ID.

```text
<PROJECT>-<DOMAIN>-<NUMBER>
```

Examples:

```text
GDS-QTEMPLATE-001
GG-STEAM-OCR-003
```

Q identity is carried by:

- Q ID;
- folder name;
- `request.md` metadata;
- Source Q File in the completion report.

Date is not the default identity for a Q.

## Task Artifact Workspace Structure

Use this structure for scalable Q artifact storage:

```text
docs/requests/
  <project>/
    draft/
    approved/
    in_progress/
    review/
    completed/
    archived/
    rejected/
```

Existing repositories may keep the current smaller folder set until a migration Q explicitly expands it:

```text
draft / approved / completed / archived
```

Recommended project folder names:

- `gds`
- `gameghost`
- `animeghost`
- `comicghost`
- `experiments`

Use `experiments` for exploratory or cross-project requests that do not yet belong to one approved Target Project.

## Status Folders

Allowed Q statuses:

```text
Draft / Approved / In Progress / Review / Completed / Archived / Rejected
```

Recommended folder names:

```text
draft / approved / in_progress / review / completed / archived / rejected
```

Status meaning:

- `draft`: idea or request is being prepared and is not approved for execution.
- `approved`: Q is approved and ready for Codex or another AI to execute.
- `in_progress`: execution has started but is not ready for review.
- `review`: implementation or documentation is ready for human review.
- `completed`: implementation and completion report have been returned and reviewed enough to preserve together.
- `archived`: old, superseded, or retained-for-history work that should not be used as active execution input.
- `rejected`: reviewed and intentionally not adopted.

## Task Workspace

When a Q has multiple related artifacts, use a task workspace folder:

```text
docs/requests/<project>/<status>/<Q_ID>_<short_topic>/
  request.md
  notes.md
  completion_report.md
  attachments/
```

Task workspace files:

- `request.md`: authoritative Q file.
- `notes.md`: optional working notes, review notes, or migration notes.
- `completion_report.md`: authoritative completion report.
- `attachments/`: optional supporting files, screenshots, exported docs, or review materials.
- `addendum_*.md`: optional requirement deltas that do not justify a new Q.

Use a task workspace by default when the task has attachments, a `.docx` review copy, multiple generated files, long review history, known Q ID, or completion report requirements.

For normal Codex / AI implementation work, the preferred artifact is:

```text
docs/requests/<project>/<status>/<Q_ID>_<short_topic>/request.md
```

`request.md` is the authoritative input. Chat may point to it, but should not replace it.

## Simple File Form

For small Q artifacts that do not need a task workspace yet, this simpler form is allowed:

```text
docs/requests/<project>/<status>/Q_<Q_ID>_<short_topic>_JP.md
```

The related completion report should use the same folder and basename:

```text
docs/requests/<project>/<status>/Q_<Q_ID>_<short_topic>_JP_completion_report.md
```

Legacy date form remains readable but is not the default for new Qs:

```text
docs/requests/<project>/<status>/YYYY-MM-DD_<project>_<short_title>.md
```

Do not mass-rename existing Q files just to satisfy this standard.

## Standard Formats

Required:

```text
.md
```

Optional when human review is expected:

```text
.docx
```

Markdown `.md` is the source of truth for Git review and AI handoff.

Word `.docx` is for human review, comments, approval, redline, or offline reading.

## File Naming

Use this naming pattern for new standalone Q files:

```text
Q_<Q_ID>_<short_topic>_JP.md
```

Rules:

- use the Q ID as the stable identity;
- use lowercase ASCII snake_case for `short_topic`;
- keep the topic short but specific;
- avoid spaces;
- avoid implementation-only names when a purpose-oriented name is clearer;
- do not put a date in ordinary Q filenames.

Example:

```text
Q_GDS-QTEMPLATE-001_q_template_and_naming_standard_JP.md
```

When a `.docx` version is generated, use the same basename:

```text
Q_GDS-QTEMPLATE-001_q_template_and_naming_standard_JP.docx
```

Date in filename is allowed only when date is the primary identity:

- daily snapshot;
- date-specific incident;
- release-specific record;
- migration executed on a specific date;
- external event tied to a concrete date;
- temporary handoff package.

## Completion Report Naming

Completion reports generated from a Q should be saved in the same folder.

Inside a task workspace, use stable artifact names:

```text
request.md
notes.md
completion_report.md
attachments/
```

If a simple file form is used, save the completion report beside the source Q:

```text
Q_<Q_ID>_<short_topic>_JP_completion_report.md
```

If human review is expected:

```text
Q_<Q_ID>_<short_topic>_JP_completion_report.docx
```

## Required Q Metadata

Each saved Q artifact should include:

- Q ID;
- Title;
- Version;
- Status;
- Priority;
- Category;
- Created Date;
- Last Updated Date;
- Artifact Output;
- Save Location;
- File Naming;
- Artifact Workspace path;
- Status Folder;
- Repository Context;
- Commit / Push Policy;
- Scope Guard;
- Purpose / Background / Scope / Out of Scope;
- Existing Knowledge / Dependencies;
- Do / Do Not;
- Completion Criteria;
- Deliverables;
- Validation;
- AI Repository Index Update Gate;
- Related Completion Report;
- Safe Commit Set requirement;
- Suggested Commit Message.

## Related Completion Report

Each Q should identify the expected completion report artifact path.

Example:

```text
Related Completion Report:
docs/requests/gds/completed/GDS-QTEMPLATE-001_q_template_and_naming_standard/completion_report.md
```

If the work is not completed yet, use `Planned`.

The completion report should be saved in the same Task Artifact Workspace as the source Q:

```text
docs/requests/<project>/<status>/<Q_ID>_<short_topic>/completion_report.md
```

If the task uses simple file form, save the completion report beside the source Q with the same basename and `_completion_report.md` suffix.

## Related Commit

Q files should identify commit policy before implementation.

Allowed values:

- Do not execute.
- Execute only after explicit approval.
- Required after Commit OK.

After a commit exists, the completion report should record the commit hash. Before a commit exists, use:

```text
Related Commit: Not created.
```

## Revision / Addendum Rules

When requirements change:

```text
Small scope extension
  -> addendum_vX.Y.md

Materially different objective
  -> new Q

Correction before execution
  -> revise request.md / Q file
```

Do not create a new Q for every small clarification.

Do not overwrite completed Q history without a review note or addendum.

## Movement Rules

Move Q artifacts through statuses only when the status meaning changes.

```text
draft -> approved -> in_progress -> review -> completed -> archived
```

Rules:

- Move to `draft` when the Q is being prepared but is not approved.
- Move to `approved` when the Q is approved for Codex / AI implementation.
- Move to `in_progress` when execution has started and the repository needs that state recorded.
- Move to `review` when the result is ready for human review.
- Move to `completed` when implementation and completion report artifacts are returned and review has accepted them as the durable record.
- Move to `archived` when the task is old, superseded, cancelled after review, or retained only for history.
- Move to `rejected` when a reviewed Q is intentionally not adopted.

Do not move files only to make the folder look tidy. Movement should reflect workflow status.

When moving a task workspace, move the whole workspace folder so `request.md`, `completion_report.md`, `notes.md`, and `attachments/` remain together.

## Review Quality Rule

Artifact location is part of review quality.

Reviewers should treat these as issues:

- missing Q artifact path;
- missing Q ID;
- approved Q left only in chat;
- Q generated outside `docs/requests/` but never saved into the workspace;
- Codex / AI implementation started before workspace save is complete;
- approved Q stored outside the correct project/status workspace;
- completion report not stored beside the source Q;
- missing or ambiguous Target Project in the path;
- missing status folder;
- filename using date by default without date-specific reason;
- missing link between Q, completion report, and commit policy;
- missing Safe Commit Set requirement.

## Migration Guidance

Do not blindly move or rename existing request artifacts.

Safe migration steps:

1. Identify the Target Project for each existing Q.
2. Identify current workflow status.
3. Decide whether the artifact needs a full task workspace or simple file form.
4. Assign or preserve a Q ID.
5. Move only after review confirms the destination path.
6. Preserve filenames and history when practical.
7. Add `notes.md` if migration context or uncertainty should be preserved.

Recommended destination:

```text
docs/requests/<project>/<status>/<Q_ID>_<short_topic>/
```

Use a later migration Q for bulk moves when many files exist.

## Workflow

Standard Q artifact workflow:

```text
Idea
  -> Q ID Decision
  -> Q Artifact Workspace
  -> request.md Save Verification
  -> Approval
  -> Codex / AI Implementation
  -> Completion Report Artifact
  -> Human Review
  -> Commit Decision
  -> Knowledge Promotion
  -> Archive
```

## Failure Modes Prevented

This standard prevents:

- Q text being lost in chat;
- incomplete copy-paste into AI tools;
- implementation from a truncated request;
- missing completion criteria;
- inability to find the original Q after implementation;
- ambiguous project or workflow status;
- date-only names becoming untraceable;
- completion reports separated from source Q files;
- lost notes or attachments;
- weak link between Q, completion report, and commit policy.

## Related Documents

- `docs/rules/artifact_first_rules.md`
- `docs/rules/q_file_naming_rules.md`
- `docs/rules/q_file_template_rules.md`
- `docs/workflow/q_file_creation_workflow.md`
- `docs/workflow/q_revision_addendum_workflow.md`
- `docs/workflow/output_policy.md`
- `docs/requests/README.md`
- `templates/Q_TEMPLATE.md`
- `templates/completion_report_template.md`
- `examples/q_file_artifact_workflow.md`
- `examples/q_file_examples.md`
