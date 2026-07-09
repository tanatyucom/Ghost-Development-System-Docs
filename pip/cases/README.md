# PIP Cases

## Purpose

This folder stores reusable improvement cases.

A PIP Case records a problem, symptoms, investigation, evidence, first broken step, root cause, fix, validation, and lessons learned so that future work can reuse the learning instead of rediscovering it.

## Required Template

Use:

```text
pip/templates/case_template.md
```

## Required Metadata

- Case ID
- Date
- Status
- Related Q
- Related Report
- Related Rule
- Related PIP
- Tags
- Keywords

## Index

After adding or changing a case, update:

```text
pip/case_index.md
```

## Candidate Lists

- `case_candidates_from_master_title_list.md`
- `case_candidates_from_roadmap2_salvage.md`

## Scope

This folder contains reviewed knowledge entries. Raw evidence, large debug artifacts, screenshots, and generated reports should remain in their source evidence package or task artifact workspace and be linked from the case.
