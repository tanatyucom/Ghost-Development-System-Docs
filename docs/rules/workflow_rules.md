# Workflow Rules

**Version:** 2.2

**Last Updated:** 2026-07-01

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

### Retrospective Rule

After substantial work, record reusable learning as:

- rule improvement;
- template improvement;
- workflow improvement;
- roadmap future candidate;
- remaining issue.

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
