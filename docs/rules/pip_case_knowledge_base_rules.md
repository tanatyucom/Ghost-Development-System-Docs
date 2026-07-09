# PIP Case Knowledge Base Rules

## Purpose

PIP Case Knowledge Base は、PIP を一時的な briefing ではなく、長期的に再利用できる改善知識データベースとして育てるための標準です。

## Core Rule

再利用できる失敗、調査、レビュー、改善、予防知識は、チャットや completion report だけに残さず、必要に応じて PIP Case として保存します。

## Required Locations

PIP Case Knowledge Base は次の構造を使います。

```text
pip/cases/
pip/rule_stories/
pip/evolutions/
pip/best_practices/
pip/investigations/
pip/concepts/
pip/templates/
```

PIP Master Document and Title List are stored here:

```text
pip/MASTER_DOCUMENT_JP.md
pip/MASTER_TITLE_LIST_JP.md
```

Case Index は次に保存します。

```text
pip/case_index.md
```

Tagging Standard は次に保存します。

```text
pip/tagging_standard.md
```

## CASE Metadata Rule

各 CASE は次の metadata を必ず持ちます。

- Case ID
- Date
- Status
- Related Q
- Related Report
- Related Rule
- Related PIP
- Tags
- Keywords

## CASE Body Rule

各 CASE は次の sections を持ちます。

- Problem
- Symptoms
- Investigation
- Evidence
- First Broken Step
- Root Cause
- Fix
- Validation
- Lessons Learned
- Related Rules
- Related Cases

## Tagging Rule

PIP Case の tags は `pip/tagging_standard.md` に従います。

Searchability を保つため、各 CASE は少なくとも Project、Category、Methodology、Priority、Lifecycle のタグを持ちます。

## Promotion Rule

Completion Report や Debug Artifact Review から再利用可能な知識が見つかった場合、Improvement Review で次を判断します。

- PIP Case にするか。
- Rule Story にするか。
- Best Practice にするか。
- Workflow、Template、Rule、Architecture へ昇格するか。
- Future Candidate として残すか。

## Evidence Rule

PIP Case は証跡を要約し、証跡の場所へリンクします。

Raw evidence、巨大な debug artifact、screenshots、generated reports は、元の evidence package や task artifact workspace に残し、PIP Case にはコピーしません。

## Human Approval Rule

PIP Case から rule standardization、workflow standardization、architecture decision へ昇格する場合は Human Approval Gate を通します。

## Master Document Rule

`pip/MASTER_DOCUMENT_JP.md` is the human-readable master document for Roadmap2-derived GDS / PIP methodology.

`pip/MASTER_TITLE_LIST_JP.md` is the classification source for CASE, Best Practice, Evolution, Investigation, and Rule Story candidates.

When these files change, update the relevant candidate list, `pip/case_index.md`, `pip/README.md`, and `docs/README.md`.

Candidate files are not official rules by themselves. Promotion to official rule, workflow, template, or architecture still requires review and Human Approval Gate.

## Concept Lifecycle Rule

Concept entries under `pip/concepts/` preserve reusable ideas before they are
strong enough to become CASE, Rule Story, Best Practice, Evolution,
Investigation, official Rule, Workflow, Principle, template, glossary, or
architecture.

Concept status values are:

- `Candidate`
- `Under Review`
- `Experiment`
- `Validated`
- `Promoted`
- `Archived`

Concepts must not remain permanent unreviewed storage. They should move toward
promotion or archive through `docs/workflow/concept_promotion_workflow.md`.

Promotion requires source evidence, reuse value, consistency with GDS
principles, documentation, review, and the required Human Approval Gate when
the destination is a rule, workflow, architecture boundary, public terminology,
or principle.

Use `pip/templates/concept_template.md` for individual Concept entries,
`pip/templates/concept_status_change_report_template.md` for status changes,
and `pip/templates/concept_review_checklist.md` before promotion or archive
decisions.

## Knowledge Classification Rule

Classify Roadmap2 follow-up knowledge by reusable form:

- Concept: reusable thinking, principle, or design philosophy.
- PIP: experiment result, parameter note, implementation detail, or
  project-specific status information.
- CASE: a real case with problem, investigation, evidence, first broken step,
  root cause, lessons learned, related concepts, rules, and workflow.
- Investigation: reusable investigation pattern or method.
- Negative Knowledge: an important rejected hypothesis or proven non-cause that
  prevents repeated investigation.

Do not promote parameter values, OCR tuning values, band widths, BBox tuning
results, or one-off experiment results into Concept entries unless they reveal a
reusable cross-project idea.

## Decision Background

PIP v1.0 stable は Importance と Tags による読みやすさを持っていました。PIP v1.1 delta は Trace Before Tune、First Broken Step、Review Entry Point、Human Visual Review を reusable methodology として追加しました。このルールは、その流れを CASE、タグ、索引、テンプレートとして固定します。
