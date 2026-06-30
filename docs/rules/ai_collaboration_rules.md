# AI Collaboration Rules

**Version:** 2.1

**Last Updated:** 2026-06-30

## Purpose

This document defines how humans and AI collaborate on Ghost Development System
Docs.

## Collaboration Philosophy

### Human Leads

Humans approve goals, architecture, scope, naming, release decisions, and
destructive changes.

### AI Is A Partner

AI helps draft, review, compare, summarize, and propose improvements. AI should
improve quality, not replace human judgment.

### Evidence First

AI should base suggestions on visible documents, known rules, reviewed
decisions, and explicit user requests.

### Knowledge Must Be Written Down

Reusable learning should move into rules, templates, roadmap, workflow, or
architecture documents. It should not remain only in conversation.

## AI Responsibilities

AI may:

- review documentation structure;
- draft and revise Markdown;
- identify missing related updates;
- propose future candidates;
- suggest commit messages;
- summarize changes;
- recommend next Q files.

AI must not:

- perform runtime implementation during documentation-only work;
- migrate repositories unless explicitly requested;
- commit unless explicitly requested;
- bypass Human Approval Gate;
- treat Future Candidates as approved implementation.

## Multi-AI Collaboration

Different AI tools may be used for different strengths, but all AI output must
remain reviewable by humans.

Cross-review is recommended for:

- architecture boundaries;
- roadmap direction;
- public terminology;
- major rule changes;
- reusable templates.

## Communication Rules

AI should report:

- changed files;
- what changed;
- verification performed;
- remaining issues;
- future candidates;
- recommended next Q;
- suggested commit message.

## Goal

The goal is a durable collaboration system where humans and AI share the same
knowledge base, reduce repeated mistakes, and improve the archive over time.
