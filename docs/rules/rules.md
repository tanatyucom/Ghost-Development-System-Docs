# Ghost Development System Rules

**Version:** 2.4

**Last Updated:** 2026-07-05

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
- Artifact First.
- Audit Before Repair.
- Debug Artifact Review.
- Migration First.
- PIP Case Knowledge Base.
- Human Approval Gate.
- Future Scope Guard.

`rules.md` is the index and priority document. Detailed rules belong in their
own files.

## Official Rule Documents

- `core_principles.md`
- `project_rules.md`
- `language_rules.md`
- `documentation_rules.md`
- `artifact_first_rules.md`
- `q_file_artifact_standard.md`
- `audit_before_repair_rules.md`
- `debug_artifact_review_rules.md`
- `migration_first_rules.md`
- `pip_case_knowledge_base_rules.md`
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

## Debug Artifact Review

AI, OCR, recommendation, auto-detection, candidate extraction, fuzzy matching,
and visual processing work should use Debug Mode during development when
intermediate behavior needs review.

Normal execution must not generate debug artifacts unless Debug Mode is
explicitly requested.

Completion reports should name the debug artifact save location, verification
target, expected normal state, review viewpoints, AI review target artifacts
when applicable, and whether the artifacts are excluded from Git.

When many debug or review artifacts are generated, completion reports should
also include a Review Entry Point: the first artifact path or ordered artifact
list for human and AI review.

Details follow `debug_artifact_review_rules.md`.

## Audit Before Repair

Repair work should start with audit, classification, evidence, and human review
before scoped repair begins.

Standard flow:

```text
Idea / Bug
  -> Audit
  -> Classification
  -> Evidence
  -> Human Review
  -> Repair Q
  -> Verification
  -> Commit
```

Audit results should classify findings as `fix_candidate`,
`needs_human_review`, `generated_artifact`, `raw_data`, or `false_positive`.

AI must not perform broad one-shot repair when the target includes raw data,
generated artifacts, OCR evidence, DB files, or unrelated dirty workspace
changes.

Details follow `audit_before_repair_rules.md`.

## Migration First

Internal architecture changes should prefer migration to a new standard over
permanent compatibility fallback.

Standard flow:

```text
New Standard
  -> Migration Plan
  -> Reference Update
  -> Verification
  -> Legacy Removal
```

Public compatibility is protected for public release, public API / CLI,
documented external workflow, exported artifact schema, DB schema, and
user-facing data formats. Internal folder structure, script layout, adapter
interfaces, prototype scripts, shared utility locations, artifact workspace
layout, queue / request structure, and future GhostCore / GDS internal modules
should not accumulate permanent legacy fallback.

Details follow `migration_first_rules.md`.

## PIP Case Knowledge Base

Reusable failures, investigations, review methods, first broken steps, root causes, fixes, validation results, and lessons learned should be promoted to PIP Case entries when they are useful beyond a single task.

Standard locations:

```text
pip/cases/
pip/rule_stories/
pip/evolutions/
pip/best_practices/
pip/investigations/
pip/templates/
```

Each CASE must include required metadata, standard tags, evidence links, related rules, and related cases.

Details follow `pip_case_knowledge_base_rules.md`.

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
