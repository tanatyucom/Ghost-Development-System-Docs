# Ghost Development System Rules

**Version:** 2.2

**Last Updated:** 2026-07-01

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
- Project First Principle.
- Japanese First.
- Evidence First.
- Knowledge Before Automation.
- Human Approval Gate.
- Future Scope Guard.

`rules.md` is the index and priority document. Detailed rules belong in their
own files.

## Official Rule Documents

- `core_principles.md`
- `project_rules.md`
- `language_rules.md`
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

## Project First Principle

すべての Q は、実装前に Target Project を宣言しなければなりません。

AI は Target Project、Repository、Single Source Of Truth、Related Repository、
Cross Project Impact、Scope Guard を確認してから編集します。

詳細は `project_rules.md` に従います。

## Japanese First

Ghost Development System Docs は日本語運用を基本とします。

人間が判断、承認、レビューする文章は日本語で書くことを基本とします。
ソースコード、API、クラス名、関数名、ファイル名、パス、Commit Message、
Git コマンドなど、英語である必要があるものは英語のまま扱ってよいです。

詳細は `language_rules.md` に従います。

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
