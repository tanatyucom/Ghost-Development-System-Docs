# Ghost Development System Rules

**Version:** 3.1

**Last Updated:** 2026-07-10

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
- Knowledge Poka-Yoke / Design For Forgetfulness.
- External Source Access / AI Repository Knowledge Access.
- AI Startup Procedure.
- AI Daily Operation Cycle.
- Startup Checklist.
- Repository Root Validation.
- AI Proactive Proposal.
- Completion Checklist.
- Artifact First.
- Audit Before Repair.
- Debug Artifact Review.
- Debug Escalation Ladder.
- Migration First.
- PIP Case Knowledge Base.
- Concept Promotion.
- Concept ID Naming.
- Roadmap2 Knowledge Salvage.
- Human Approval Gate.
- Future Scope Guard.

`rules.md` is the index and priority document. Detailed rules belong in their
own files.

## Official Rule Documents

- `core_principles.md`
- `external_source_access_rules.md`
- `ai_startup_procedure_rules.md`
- `project_rules.md`
- `language_rules.md`
- `documentation_rules.md`
- `startup_checklist_rules.md`
- `repository_root_validation_rules.md`
- `ai_proactive_proposal_rules.md`
- `completion_checklist_rules.md`
- `artifact_first_rules.md`
- `q_file_artifact_standard.md`
- `audit_before_repair_rules.md`
- `debug_artifact_review_rules.md`
- `debug_escalation_ladder_rules.md`
- `migration_first_rules.md`
- `pip_case_knowledge_base_rules.md`
- `concept_id_naming_rules.md`
- `roadmap2_knowledge_salvage_rules.md`
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

## Startup Checklist

Before implementation, review, Q execution, or documentation update begins,
confirm the working repository, production / backup / reference-only boundaries,
current phase, current goal, applicable rules, applicable methodologies, Q
artifact status, scope, out-of-scope items, and commit policy.

Standard startup flow:

```text
Start
  -> Repository Confirmation
  -> Q / Artifact Confirmation
  -> Applicable Rules Confirmation
  -> Applicable Methodologies Confirmation
  -> Scope / Out of Scope Confirmation
  -> Dirty Workspace / Commit Policy Confirmation
  -> Checklist Complete
  -> Implementation / Review Start
```

Startup Checklist is an entry point for existing rules. It does not replace
Project First, Japanese First, Artifact First, Audit Before Repair, Debug
Artifact Review, Debug Escalation Ladder, Migration First, PIP Case Knowledge
Base, Concept Promotion, Roadmap2 Knowledge Salvage, or Commit Safety.

Details follow `startup_checklist_rules.md`.

## Repository Root Validation

Before implementation, review, commit, tag, or release work begins, confirm the
actual Git repository root and compare it with the Q Working Repository.

Standard commands:

```bash
pwd
git rev-parse --show-toplevel
git status
```

If the actual Git root does not match the expected Working Repository, stop and
resolve the repository mismatch before editing or committing.

Details follow `repository_root_validation_rules.md`.

## AI Proactive Proposal

AI may proactively propose evidence-based improvements, time savings,
repository / scope conflict warnings, rule conflict warnings, methodology
conflict warnings, maintenance risks, and knowledge opportunities.

AI must not silently change implementation based on the proposal. The proposal
should include evidence and leave the final decision to the user.

Details follow `ai_proactive_proposal_rules.md`.

## Knowledge Poka-Yoke / Design For Forgetfulness

People forget. AI forgets. Processes drift.

GDS treats forgetting as a design condition. Important work should be supported
by checklists, templates, validation, artifact rules, completion reports, human
review, proactive proposals, and collaborative decisions so forgetting is caught
before it becomes a repository, scope, commit, release, or knowledge loss
incident.

Details follow `core_principles.md`.

## External Source Access / AI Repository Knowledge Access

When ChatGPT, Codex, or another AI needs to read the public GDS Docs repository
as an external Knowledge Source, it should start from
`docs/ai_repository_index.md` and use Raw URLs for the required files.

If a required public source cannot be fetched or read, AI should report the
access gap instead of pretending repository knowledge is complete.

When important public knowledge entry points are added, moved, renamed, or
materially changed, update `docs/ai_repository_index.md`.

Details follow `external_source_access_rules.md`.

## AI Startup Procedure

Before implementation, review, documentation update, or Q execution begins,
AI should read and confirm the required startup sources in a stable order.

Standard AI startup order:

```text
AI Repository Index
  -> Repository Root Validation
  -> GDS Core Rules / Workflow
  -> Target Project Profile
  -> Current Q File
  -> Startup Checklist
  -> Scope / Out of Scope
  -> Implementation / Review Start
```

If the repository, Target Project, Project Profile, Q File, scope, or commit
policy is unclear, AI should stop and ask before editing.

Details follow `ai_startup_procedure_rules.md`.

## AI Daily Operation Cycle

AI Daily Operation Cycle is the standard outer loop for recurring human / AI
GDS work.

```text
AI Startup Procedure
  -> Current Q Review
  -> Implementation
  -> Verification
  -> Human Review
  -> Completion Checklist
  -> Commit / Push
  -> Knowledge Update
  -> Repository Update
  -> Next Q Planning
  -> Next Startup
```

This cycle connects existing rules and workflows. It does not replace Startup
Checklist, Completion Checklist, Project Profile, Q File, Human Approval Gate,
commit approval, or release approval.

Details follow `docs/workflow/ai_daily_operation_cycle.md` and
`workflow_rules.md`.

## Completion Checklist

Before a task is treated as complete, confirm verification, review, completion
report, Improvement Review, commit requirement, commit execution, tag
requirement, tag execution, release requirement, release publication,
Recommended Next Q, and workspace clean confirmation.

Standard completion flow:

```text
Implementation
  -> Verification
  -> Review
  -> Completion Report
  -> Completion Checklist
  -> Commit / Tag / Release Decision
  -> Recommended Next Q
  -> End
```

Completion Checklist records decisions. It does not automatically approve
commit, tag, release, or Human Approval Gate items.

Details follow `completion_checklist_rules.md`.

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

## Debug Escalation Ladder

Uncertain defects and quality issues should move through evidence and review
before algorithm change.

Standard ladder:

```text
Phenomenon Check
  -> Metrics Check
  -> Human Review
  -> Debug Artifact Generation
  -> Pipeline Trace
  -> First Broken Step Identification
  -> Root Cause Confirmation
  -> Algorithm Change
```

Algorithm change must not be the first reaction to a symptom or metric.

Details follow `debug_escalation_ladder_rules.md`.

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
pip/concepts/
pip/templates/
```

Each CASE must include required metadata, standard tags, evidence links, related rules, and related cases.

Concepts under `pip/concepts/` move through Candidate, Under Review,
Experiment, Validated, Promoted, or Archived status before they become a
stronger knowledge unit or are preserved as history.

Use `pip/templates/concept_template.md`,
`pip/templates/concept_status_change_report_template.md`, and
`pip/templates/concept_review_checklist.md` for Concept operation.

Concept IDs use `CONCEPT-YYYY-NNN`, with optional short form `C-YYYY-NNN`.
Every tracked Concept should appear in `pip/concepts/concept_index.md`.
Promoted Concepts must record destination. Archived Concepts must record
archive reason.

Details follow `pip_case_knowledge_base_rules.md`.

Details for ID assignment follow `concept_id_naming_rules.md`.

## Roadmap2 Knowledge Salvage

Roadmap2 knowledge should be reviewed, extracted, and migrated until no
reusable knowledge remains only in Roadmap2.

Standard loop:

```text
Roadmap2 Review Request
  -> Review Result
  -> Missing Knowledge Extraction
  -> Q Artifact
  -> Codex Documentation Update
  -> GitHub Push / Review
  -> Roadmap2 Re-review
  -> Repeat Until No Missing Knowledge
```

After completion, Roadmap2 becomes history and GDS Knowledge Base is the active
source.

Details follow `roadmap2_knowledge_salvage_rules.md`.

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
