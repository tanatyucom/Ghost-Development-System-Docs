# Requests

## Purpose

This folder stores Q file artifacts, task workspaces, and related request artifacts for Ghost Development System Docs.

Use it when a request should be reused, reviewed, handed to AI, connected to a completion report, or managed in Git.

## Contains

- Q file artifacts.
- Task artifact workspaces.
- AI implementation request artifacts.
- Related completion report artifacts.
- Notes files.
- Attachments folders.
- Optional `.docx` review copies when human review is expected.
- Optional `addendum_*.md` files for approved scope deltas.

## Does NOT Contain

- Reusable templates.
- Examples.
- Runtime code.
- Private project data.
- Queue execution state.
- Release artifacts.

## Standard Structure

Use this structure for official Q workspaces:

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

Existing folders may keep the smaller set until a migration Q expands them:

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

## Q ID

New official Q artifacts should use a stable Q ID:

```text
<PROJECT>-<DOMAIN>-<NUMBER>
```

Examples:

```text
GDS-QTEMPLATE-001
GG-STEAM-OCR-003
```

The Q ID should appear in:

- folder name;
- `request.md` metadata;
- Source Q File in `completion_report.md`;
- simple-form filename, when used.

## Task Workspace

Use a task workspace when a request has related artifacts, notes, attachments, `.docx` review copies, generated outputs, addenda, or completion report requirements.

```text
docs/requests/<project>/<status>/<Q_ID>_<short_topic>/
  request.md
  notes.md
  completion_report.md
  attachments/
```

Files:

- `request.md`: authoritative Q file.
- `notes.md`: optional review notes, migration notes, uncertainty, or working notes.
- `completion_report.md`: authoritative completion report.
- `attachments/`: supporting files that belong with the task.
- `addendum_*.md`: optional scope deltas that do not justify a new Q.

The first action after creating an official Q artifact is to save `request.md` in this workspace. Codex / AI implementation should not start from an unsaved Q when the task is reusable, reviewable, AI-handoff, Git-managed, or expected to produce a completion report.

`completion_report.md` should be saved in the same workspace after the work is completed. Keep `request.md`, `completion_report.md`, `notes.md`, and `attachments/` together through status moves.

## Simple File Form

For small Q artifacts that do not need a full task workspace yet, this simpler form is allowed:

Q file:

```text
docs/requests/<project>/<status>/Q_<Q_ID>_<short_topic>_JP.md
```

Human review copy, when needed:

```text
docs/requests/<project>/<status>/Q_<Q_ID>_<short_topic>_JP.docx
```

Completion report:

```text
docs/requests/<project>/<status>/Q_<Q_ID>_<short_topic>_JP_completion_report.md
```

Example:

```text
docs/requests/gameghost/completed/Q_GG-STEAM-OCR-003_human_review_gate_clearance_JP.md
docs/requests/gameghost/completed/Q_GG-STEAM-OCR-003_human_review_gate_clearance_JP_completion_report.md
```

Legacy date form remains readable but is not the default for new Qs:

```text
docs/requests/<project>/<status>/YYYY-MM-DD_<project>_<short_title>.md
```

Use date in a filename only when the date is the primary identity, such as snapshot, incident, release, migration, external event, or temporary handoff.

## Status Folders

`draft`:

The Q is being prepared and is not approved for execution.

`approved`:

The Q is approved and ready for Codex / AI implementation.

`in_progress`:

Execution has started and the repository needs that state recorded.

`review`:

The result is ready for human review.

`completed`:

Implementation and completion report artifacts have been returned and reviewed enough to preserve together.

`archived`:

The task is old, superseded, cancelled after review, or retained only for history.

`rejected`:

The Q was reviewed and intentionally not adopted.

## Revision / Addendum

When requirements change:

```text
Small scope extension
  -> addendum_vX.Y.md

Materially different objective
  -> new Q

Correction before execution
  -> revise request.md / Q file
```

Do not create new Qs for every small clarification.

Do not overwrite completed Q history without a review note or addendum.

## Movement Rules

Move artifacts through status folders only when the status meaning changes.

Recommended path:

```text
draft -> approved -> in_progress -> review -> completed -> archived
```

Rules:

- Create new, unapproved Q artifacts in `draft`.
- Move to `approved` only after the Q is approved for Codex / AI execution.
- Move to `in_progress` when execution has started and status tracking is needed.
- Move to `review` when the result is ready for human review.
- Move to `completed` when implementation and completion report artifacts are returned and reviewed.
- Move to `archived` when the workspace is old, superseded, cancelled after review, or retained only for history.
- Move to `rejected` when the Q is intentionally not adopted.
- Move the whole task workspace folder together. Do not separate `request.md`, `completion_report.md`, `notes.md`, and `attachments/`.

## Attachments

Put task-specific supporting files in:

```text
attachments/
```

Attachments may include review screenshots, exported documents, supporting CSV/XLSX/PDF/PPTX files, or other files required to understand the task.

Do not store private data or runtime artifacts here unless a Q explicitly approves that documentation scope.

## Standard Workflow

```text
Idea
  -> Q ID Decision
  -> Q Artifact Workspace
  -> Save request.md in docs/requests/
  -> Workspace Save Verification
  -> Approval
  -> Codex / AI Implementation
  -> Completion Report Artifact
  -> Human Review
  -> Commit Decision
  -> Knowledge Promotion
  -> Archive
```

## Migration Guidance

Do not blindly move or rename existing request artifacts.

Recommended safe migration:

1. Identify Target Project.
2. Identify current status.
3. Decide whether the request needs task workspace form or simple file form.
4. Assign or preserve Q ID.
5. Move only after review confirms the destination path.
6. Preserve related completion reports and notes with the source Q.
7. Use `notes.md` to record uncertainty or migration context.

Bulk migration should be handled by a separate Q when many files exist.

## Update Policy

Add request artifacts when a Q or completion report should remain findable after the chat session.

Do not store one-off chat clarifications here unless they become reusable, reviewable, or decision-bearing.

## Related Documents

- `docs/rules/q_file_artifact_standard.md`
- `docs/rules/q_file_naming_rules.md`
- `docs/rules/q_file_template_rules.md`
- `docs/workflow/q_file_creation_workflow.md`
- `docs/workflow/q_revision_addendum_workflow.md`
- `docs/rules/artifact_first_rules.md`
- `docs/workflow/output_policy.md`
- `templates/Q_TEMPLATE.md`
- `templates/completion_report_template.md`
- `examples/q_file_artifact_workflow.md`
- `examples/q_file_examples.md`
