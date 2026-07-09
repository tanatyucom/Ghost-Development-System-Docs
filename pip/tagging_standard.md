# PIP Tagging Standard

## Purpose

PIP Case を長期的に検索、再利用、比較できるようにするため、Case、Rule Story、Evolution、Best Practice に付けるタグを標準化します。

## Required Metadata

各 CASE は、少なくとも次の metadata を持ちます。

- Case ID
- Date
- Status
- Related Q
- Related Report
- Related Rule
- Related PIP
- Tags
- Keywords

## Standard Tag Set

### Project

- `Steam`
- `Switch`
- `3DS`
- `PSN`
- `RAWG`
- `AniList`
- `Database`
- `UI`
- `GDS`

### Category

- `OCR`
- `Debug`
- `Import`
- `Review`
- `Investigation`
- `Pipeline`
- `Metadata`
- `Rule`
- `Workflow`
- `Concept`

### Methodology

- `Trace Before Tune`
- `First Broken Step`
- `Human Review`
- `Human Review First`
- `Pipeline Trace`
- `Review Entry Point`
- `Evidence Before Fix`
- `Root Cause Before Algorithm Change`
- `Audit Before Repair`
- `Migration First`
- `Knowledge Salvage`
- `Missing Knowledge Extraction`

### Priority

- `P1`
- `P2`
- `P3`

### Lifecycle

- `Investigation`
- `Under Review`
- `Experiment`
- `Validated`
- `Standardized`
- `Promoted`
- `Archived`
- `Candidate`

## Tagging Rules

- Tags must use the standard values above unless a new tag is explicitly approved.
- Each CASE should include at least one Project tag, one Category tag, one Methodology tag, one Priority tag, and one Lifecycle tag.
- Each Concept should include a lifecycle status from the Concept status set and
  should use `pip/templates/concept_template.md` when written as an individual
  file.
- Each Concept should use an ID from `docs/rules/concept_id_naming_rules.md`
  and should appear in `pip/concepts/concept_index.md`.
- Concept status changes should use
  `pip/templates/concept_status_change_report_template.md` when the decision
  affects promotion, archive, or future review.
- Free-form `Keywords` may be used for search terms that are not stable enough to become tags.
- Use `Related Rule` for official rule documents or rule stories.
- Use `Related PIP` for PIP sections, PIP versions, or package references.
- Do not use tags to hide uncertainty. If the case is still under investigation, set Lifecycle to `Investigation`.

## Tag Search Policy

The Case Index should support search by:

- Project
- Category
- Methodology
- Priority
- Lifecycle
- Rule

Example query targets:

- All `Steam` cases that use `First Broken Step`.
- All `GDS` cases related to `Workflow`.
- All `P1` cases still in `Investigation`.
- All cases related to `Review Entry Point`.

## Decision Background

PIP v1.0 already treated Importance and Tags as readability controls. PIP v1.1 expanded PIP into an improvement knowledge database. This standard keeps that philosophy and makes tags consistent enough for humans, AI, and future Command Center search.
