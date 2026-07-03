# Q File Artifact Standard

**Version:** 1.1

**Last Updated:** 2026-07-04

## Purpose

This document standardizes how Q files are generated, saved, named, reused,
moved through workflow status, and connected to completion reports.

It extends Artifact First for Q-specific work.

## Core Standard

Q files should be generated and saved as managed artifacts before they are used
for Codex, Gemini, Claude, or human review.

The chat body should not be the authoritative copy of a Q file.

Chat should contain:

- a short summary;
- the saved Q file path or download link;
- related artifact paths, when any;
- verification notes.

## Standard Save Location

Save Q file artifacts under:

```text
docs/requests/
```

Reason:

- `docs/requests/` is broad enough to store Q files, task workspaces, AI
  requests, notes, attachments, and related completion report artifacts.
- It keeps generated request artifacts separate from reusable templates in
  `docs/templates/`.
- It keeps real operational artifacts separate from examples in
  `docs/examples/`.
- It is easier to browse than a deeper path such as `docs/artifacts/q/`.

## Task Artifact Workspace Structure

Use this structure for scalable Q artifact storage:

```text
docs/requests/
  <target_project>/
    draft/
    approved/
    completed/
    archived/
```

Standard project folder names:

- `ghost-development-system`
- `gameghost`
- `animeghost`
- `comicghost`
- `experiments`

Use `experiments` for exploratory or cross-project requests that do not yet
belong to one approved Target Project.

## Status Folders

Use these status folders:

- `draft`
- `approved`
- `completed`
- `archived`

Status meaning:

- `draft`: idea or request is being prepared and is not approved for execution.
- `approved`: Q is approved and ready for Codex or another AI to execute.
- `completed`: implementation and completion report have been returned and
  reviewed enough to preserve together.
- `archived`: old, superseded, or retained-for-history work that should not be
  used as active execution input.

## Task Workspace

When a Q has multiple related artifacts, use a task workspace folder:

```text
docs/requests/<target_project>/<status>/<request_id>_<short_title>/
  request.md
  completion_report.md
  notes.md
  attachments/
```

Task workspace files:

- `request.md`: authoritative Q file.
- `completion_report.md`: authoritative completion report.
- `notes.md`: optional working notes, review notes, or migration notes.
- `attachments/`: optional supporting files, screenshots, exported docs, or
  review materials.

Use a task workspace by default when the task has attachments, a `.docx`
review copy, multiple generated files, long review history, or a known request
ID / task ID.

## Simple File Form

For small Q artifacts that do not need a task workspace yet, this simpler form
is allowed:

```text
docs/requests/<target_project>/<status>/YYYY-MM-DD_<target_project>_<short_title>.md
```

The related completion report should use the same folder and basename:

```text
docs/requests/<target_project>/<status>/YYYY-MM-DD_<target_project>_<short_title>_completion_report.md
```

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

Word `.docx` is for human review, comments, approval, redline, or offline
reading.

## File Naming

Use this naming pattern:

```text
YYYY-MM-DD_<target_project>_<short_title>.md
```

Rules:

- use the local date when the Q artifact is created;
- use lowercase ASCII for `target_project`;
- use lowercase ASCII snake_case for `short_title`;
- keep the title short but specific;
- avoid spaces;
- avoid implementation-only names when a purpose-oriented name is clearer.

Example:

```text
2026-07-03_gameghost_steam_ownership_gap_audit.md
```

When a `.docx` version is generated, use the same basename:

```text
2026-07-03_gameghost_steam_ownership_gap_audit.docx
```

## Completion Report Naming

Completion reports generated from a Q should be saved in the same folder:

```text
YYYY-MM-DD_<target_project>_<short_title>_completion_report.md
```

If human review is expected:

```text
YYYY-MM-DD_<target_project>_<short_title>_completion_report.docx
```

Inside a task workspace, use stable artifact names instead:

```text
request.md
completion_report.md
notes.md
attachments/
```

## Required Q Metadata

Each saved Q artifact should include:

- Artifact Output;
- Save Location;
- File Naming;
- Request ID or Task ID, when available;
- Artifact Workspace path;
- Status Folder;
- Related Completion Report;
- Output Artifacts;
- Related Commit;
- Movement Instructions;
- Repository Information;
- Scope Guard;
- Do / Do Not;
- Completion Criteria;
- Deliverables;
- Suggested Commit Message.

## Related Completion Report

Each Q should identify the expected completion report artifact path.

Example:

```text
Related Completion Report:
docs/requests/gameghost/completed/GG-0001_steam_ownership_gap/completion_report.md
```

If the work is not completed yet, use `Planned`.

## Related Commit

Q files should identify commit policy before implementation.

Allowed values:

- Do not commit.
- Commit only when explicitly requested.
- Commit expected after review.

After a commit exists, the completion report should record the commit hash.
Before a commit exists, use:

```text
Related Commit: Not created.
```

## Movement Rules

Move Q artifacts through statuses only when the status meaning changes.

```text
draft -> approved -> completed -> archived
```

Rules:

- Move to `draft` when the Q is being prepared but is not approved.
- Move to `approved` when the Q is approved for Codex / AI implementation.
- Move to `completed` when implementation and completion report artifacts are
  returned and review has accepted them as the durable record.
- Move to `archived` when the task is old, superseded, cancelled after review,
  or retained only for history.

Do not move files only to make the folder look tidy. Movement should reflect
workflow status.

When moving a task workspace, move the whole workspace folder so `request.md`,
`completion_report.md`, `notes.md`, and `attachments/` remain together.

## Review Quality Rule

Artifact location is part of review quality.

Reviewers should treat these as issues:

- missing Q artifact path;
- approved Q left only in chat;
- approved Q stored outside the correct project/status workspace;
- completion report not stored beside the source Q;
- missing or ambiguous Target Project in the path;
- missing status folder;
- missing link between Q, completion report, and commit policy.

## Migration Guidance

Do not blindly move existing request artifacts.

Safe migration steps:

1. Identify the Target Project for each existing Q.
2. Identify current workflow status.
3. Decide whether the artifact needs a full task workspace or simple file
   form.
4. Move only after review confirms the destination path.
5. Preserve filenames and history when practical.
6. Add `notes.md` if migration context or uncertainty should be preserved.

Recommended destination:

```text
docs/requests/<target_project>/<status>/<request_id>_<short_title>/
```

Use a later migration Q for bulk moves when many files exist.

## Workflow

Standard Q artifact workflow:

```text
Idea
  -> Q Artifact Workspace
  -> Approval
  -> Codex / AI Implementation
  -> Completion Report Artifact
  -> Human Review
  -> Commit
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
- completion reports separated from source Q files;
- lost notes or attachments;
- weak link between Q, completion report, and commit.

## Related Documents

- `docs/rules/artifact_first_rules.md`
- `docs/workflow/output_policy.md`
- `docs/requests/README.md`
- `docs/templates/q_file_template.md`
- `docs/templates/completion_report_template.md`
- `docs/examples/q_file_artifact_workflow.md`
