# Ghost Development System Rules

**Version:** 2.1

**Last Updated:** 2026-06-30

## Purpose

This document is the entry point for the official rules of Ghost Development
System Docs.

Rules are higher priority than roadmap, workflow drafts, templates, and Queue
items. When documents conflict, follow the rules first and update the lower
priority document.

## Rule Priority

1. Rules
2. Workflow
3. Architecture
4. Roadmap
5. Status
6. Queue
7. Research

## Rule Organization

Rules follow these principles:

- One File One Theme.
- One Folder One Responsibility.
- Evidence First.
- Human Approval Gate.
- Future Scope Guard.

`rules.md` is the index and priority document. Detailed rules belong in their
own files.

## Official Rule Documents

- `core_principles.md`
- `documentation_rules.md`
- `workflow_rules.md`
- `git_rules.md`
- `quality_rules.md`
- `ai_collaboration_rules.md`
- `script_architecture_rules.md`

## Human Approval Gate

Humans approve:

- architecture changes;
- destructive changes;
- scope expansion;
- release decisions;
- rule standardization;
- migration work;
- public terminology changes.

AI may propose, draft, compare, and review. AI must not silently promote future
candidates, expand scope, or perform destructive work.

## Future Scope Guard

Ideas that are useful but not yet validated must be recorded as Future
Candidates.

Future Candidates are not implementation approval. Promotion requires roadmap or
architecture review.

## Rule Change Policy

When changing rules, record:

- reason for change;
- expected benefit;
- affected documents;
- whether templates or workflow need updates.

Rules should be standardized from proven practice, not from speculation.

## Goal

Rules keep the knowledge base understandable for future humans and AI. They
make collaboration repeatable, reduce hidden assumptions, and protect long-term
maintainability.
