# Documentation Rules

**Version:** 2.5

**Last Updated:** 2026-07-10

## Purpose

This document defines how documentation is organized, updated, and reviewed in
Ghost Development System Docs.

## Documentation Principles

### Documentation Is A First-Class Asset

Documentation is part of the development system. Treat it with the same care as
runtime code in implementation repositories.

### One Document One Purpose

Each Markdown file should have one clear purpose. If a document starts carrying
multiple responsibilities, split it.

### Public Knowledge Base Quality

Public documents should be readable without private context. Avoid unexplained
abbreviations, hidden assumptions, and outdated references.

### Artifact First

Reusable, reviewable, or Git-managed documentation should be generated as a
file artifact instead of being delivered only in chat.

Use Markdown `.md` as the standard Git and AI handoff format. Use Word `.docx`
when human review, redline, approval, or offline reading is expected.

Chat should contain a summary and artifact links or paths, not the full
authoritative long-form document, unless explicitly requested.

### Task Artifact Workspace Documentation

Q artifacts, completion reports, notes, and attachments should be stored in a
human-readable and AI-readable workspace:

```text
docs/requests/<target_project>/<status>/<request_id>_<short_title>/
```

The path should show Target Project, workflow status, and task purpose.

Artifact location is part of documentation quality. A missing Q artifact path,
wrong project folder, wrong status folder, or missing completion report pairing
should be treated as a documentation review issue.

### AI Repository Knowledge Access

When public AI knowledge entry points change, update or review:

```text
docs/ai_repository_index.md
```

This applies when README, roadmap, rules, workflow, templates, examples,
glossary, history, PIP, CASE, Concept, methodology, or other important public
Markdown entry points are added, moved, renamed, or materially changed.

The index should provide Raw URLs that AI systems can fetch reliably.

### Current Scope Must Be Explicit

Every substantial documentation request should say what is in scope and what is
out of scope.

### Project First Documentation

Every substantial documentation request should declare Target Project before
implementation.

Repository, Documentation Root, Single Source Of Truth, Related Repository,
Cross Project Impact, and Scope Guard should be written before the task details
when practical.

### Japanese First Documentation

Human-facing documentation should be written in Japanese by default.

Keep English where required for source code, APIs, identifiers, filenames,
paths, Git commands, commit messages, and established proper nouns.

## README Rules

Each major folder should have a README that includes:

- Purpose.
- Contains.
- Does NOT Contain.
- Update Policy.
- Related Documents.

The README is an operating guide for the folder, not a decorative summary.

## Folder Responsibilities

- `architecture/`: architecture notes and responsibility boundaries.
- `examples/`: reusable examples.
- `roadmap/`: long-term direction and future candidates.
- `requests/`: Q artifacts, task workspaces, completion reports, notes, and
  attachments.
- `rules/`: official operating rules.
- `templates/`: reusable request, review, planning, and report templates.
- `workflow/`: development process and trial workflows.

## Documentation Update Timing

Update documentation when:

- architecture changes;
- responsibility boundaries change;
- workflow changes;
- rules change;
- templates are improved;
- public AI knowledge entry points change;
- a review discovers missing or misleading knowledge;
- a future candidate is promoted or clarified.

## Impact Awareness

When changing rules, workflow, architecture, or templates, check whether related
documents also need updates.

This is the human version of the future Documentation Impact Analyzer.

## Delivery Rule

Deliver updated documents as complete files, not partial fragments, unless the
review request explicitly asks for a patch-level proposal.

## Goal

Documentation should make the project easier to resume, review, and improve for
both humans and AI.
