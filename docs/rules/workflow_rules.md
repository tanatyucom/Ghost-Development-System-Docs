# Workflow Rules

**Version:** 2.4

**Last Updated:** 2026-07-04

## Purpose

This document defines workflow rules for human-led, AI-assisted development.

## Development Workflow Version 2.0 Trial

Development Workflow Version 2.0 is in trial for Ver1.4.

Reference:

```text
docs/workflow/development_workflow_v2_trial.md
```

The trial may be used for Ver1.4 operations, but it is not yet permanent.
Promote it only after retrospective evidence shows that it reduces operational
mistakes and improves resume quality.

During the trial:

- update Current Focus when creating a Queue item;
- update Current Focus after completing a Queue item;
- move completed Queue items before moving Current Focus to the next task;
- run a short retrospective after completion;
- record proposed rule, template, workflow, or roadmap improvements.

## Core Workflow Rules

### Scope Freeze Rule

Do the accepted scope first.

New ideas discovered during work should be recorded as improvements or Future
Candidates unless they are required to complete the accepted scope.

### Project First Gate

Before implementation, confirm:

- Target Project.
- Repository.
- Working Directory.
- Documentation Root.
- Runtime Root.
- Single Source Of Truth.
- Related Repository.
- Cross Project Impact.
- Scope Guard.

If these are missing or conflicting, stop and clarify before editing.

### Artifact First Gate

Before implementation or review, decide whether the requested output belongs
in chat or in a file artifact.

Use a file artifact by default for long Q files, design documents,
specifications, review requests, Codex / Gemini / Claude requests, roadmap
update proposals, and any output expected to be stored in Git.

Use chat only for short consultation, clarification, or status that is not the
authoritative copy of reusable work.

Q artifacts should be saved in the correct Task Artifact Workspace under:

```text
docs/requests/<target_project>/<status>/
```

Use full workspace form when the task has related artifacts:

```text
docs/requests/<target_project>/<status>/<request_id>_<short_title>/
  request.md
  completion_report.md
  notes.md
  attachments/
```

Completion report artifacts should be stored alongside the source Q artifact.

Approved Q files should not remain only in chat and should not remain outside
the correct project/status workspace.

Missing Q artifact path is a review issue.

### Task Artifact Movement Rule

Move Q artifacts through this status path:

```text
draft -> approved -> completed -> archived
```

Movement rules:

- `draft`: Q is being prepared and is not approved for execution.
- `approved`: Q is approved and ready for Codex / AI implementation.
- `completed`: implementation and completion report artifacts are returned and
  reviewed.
- `archived`: old, superseded, cancelled after review, or retained only for
  history.

When using a task workspace, move the whole workspace folder. Do not separate
`request.md`, `completion_report.md`, `notes.md`, and `attachments/`.

### Stop Gate

Stop and return to planning when:

- scope becomes unclear;
- implementation would require destructive change;
- a future candidate is being treated as approved work;
- documents conflict in a way that affects the result;
- the task would require runtime, migration, release, or CI work outside the
  accepted request.

### Review Gate

Review before marking work complete.

For documentation work, review for:

- purpose clarity;
- scope control;
- terminology consistency;
- responsibility boundaries;
- future candidate handling;
- template impact.
- artifact location;
- source Q path;
- completion report pairing;
- correct project/status workspace.

### Retrospective Rule

After substantial work, record reusable learning as:

- rule improvement;
- template improvement;
- workflow improvement;
- roadmap future candidate;
- Knowledge Asset candidate;
- metric or evidence improvement;
- remaining issue.

Knowledge Asset candidates require review before use. If automation will depend
on the asset, confirm ownership, approval state, and whether the asset belongs
to a project-specific repository or the shared Knowledge Asset Layer.

When metrics are available, record whether they support the improvement. Useful
signals may include completion time, review iterations, reuse count,
automation rate, human review time, duplicate prevention, or OCR quality
changes. Do not treat raw metrics as automatic approval.

## AI Workflow Rules

AI should:

- read existing context before editing;
- confirm Target Project before editing;
- confirm Cross Project Impact before editing;
- state assumptions when needed;
- prefer narrow, complete changes;
- avoid runtime work when the request is documentation-only;
- report verification and remaining issues.

AI should not:

- commit unless explicitly requested;
- migrate repositories unless explicitly requested;
- silently change scope;
- promote future candidates without review.

## Goal

Workflow rules keep development resumable, reviewable, and safe across humans,
AI, and long-running archive work.
