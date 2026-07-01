# Documentation Rules

**Version:** 2.2

**Last Updated:** 2026-07-01

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
