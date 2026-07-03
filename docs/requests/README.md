# Requests

## Purpose

This folder stores Q file artifacts, task workspaces, and related request
artifacts for Ghost Development System Docs.

Use it when a request should be reused, reviewed, handed to AI, connected to a
completion report, or managed in Git.

## Contains

- Q file artifacts.
- Task artifact workspaces.
- AI implementation request artifacts.
- Related completion report artifacts.
- Notes files.
- Attachments folders.
- Optional `.docx` review copies when human review is expected.

## Does NOT Contain

- Reusable templates.
- Examples.
- Runtime code.
- Private project data.
- Queue execution state.
- Release artifacts.

## Standard Structure

Use this structure:

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

`draft`:

The Q is being prepared and is not approved for execution.

`approved`:

The Q is approved and ready for Codex / AI implementation.

`completed`:

Implementation and completion report artifacts have been returned and reviewed
enough to preserve together.

`archived`:

The task is old, superseded, cancelled after review, or retained only for
history.

## Task Workspace

Use a task workspace when a request has related artifacts, notes, attachments,
`.docx` review copies, generated outputs, or a request ID / task ID.

```text
docs/requests/<target_project>/<status>/<request_id>_<short_title>/
  request.md
  completion_report.md
  notes.md
  attachments/
```

Files:

- `request.md`: authoritative Q file.
- `completion_report.md`: authoritative completion report.
- `notes.md`: optional review notes, migration notes, or working notes.
- `attachments/`: supporting files that belong with the task.

## Simple File Form

For small Q artifacts that do not need a full task workspace yet, this simpler
form is allowed:

Q file:

```text
docs/requests/<target_project>/<status>/YYYY-MM-DD_<target_project>_<short_title>.md
```

Human review copy, when needed:

```text
docs/requests/<target_project>/<status>/YYYY-MM-DD_<target_project>_<short_title>.docx
```

Completion report:

```text
docs/requests/<target_project>/<status>/YYYY-MM-DD_<target_project>_<short_title>_completion_report.md
```

Example:

```text
docs/requests/gameghost/completed/2026-07-04_gameghost_steam_ocr.md
docs/requests/gameghost/completed/2026-07-04_gameghost_steam_ocr_completion_report.md
```

## Movement Rules

Move artifacts through this status path:

```text
draft -> approved -> completed -> archived
```

Rules:

- Create new, unapproved Q artifacts in `draft`.
- Move to `approved` only after the Q is approved for Codex / AI execution.
- Move to `completed` when implementation and completion report artifacts are
  returned and reviewed.
- Move to `archived` when the workspace is old, superseded, cancelled after
  review, or retained only for history.
- Move the whole task workspace folder together. Do not separate `request.md`,
  `completion_report.md`, `notes.md`, and `attachments/`.

## Attachments

Put task-specific supporting files in:

```text
attachments/
```

Attachments may include review screenshots, exported documents, supporting
CSV/XLSX/PDF/PPTX files, or other files required to understand the task.

Do not store private data or runtime artifacts here unless a Q explicitly
approves that documentation scope.

## Standard Workflow

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

## Migration Guidance

Do not blindly move existing request artifacts.

Recommended safe migration:

1. Identify Target Project.
2. Identify current status.
3. Decide whether the request needs task workspace form or simple file form.
4. Move only after review confirms the destination path.
5. Preserve related completion reports and notes with the source Q.
6. Use `notes.md` to record uncertainty or migration context.

Bulk migration should be handled by a separate Q when many files exist.

## Update Policy

Add request artifacts when a Q or completion report should remain findable
after the chat session.

Do not store one-off chat clarifications here unless they become reusable,
reviewable, or decision-bearing.

## Related Documents

- `docs/rules/q_file_artifact_standard.md`
- `docs/rules/artifact_first_rules.md`
- `docs/workflow/output_policy.md`
- `docs/templates/q_file_template.md`
- `docs/templates/completion_report_template.md`
