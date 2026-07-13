# Artifact Metadata Reference Examples

## Purpose

This document provides reference examples for
`templates/structured_artifact_metadata_template.md`.

Use these examples to review whether structured artifact metadata is readable,
diff-friendly, and safe before creating validators, parsers, Component
Interfaces, Command Center automation, or Ghost SDK contracts.

Examples are references. `docs/architecture/artifact_schema_standard.md` and
`templates/structured_artifact_metadata_template.md` remain authoritative.

## Good Examples

### Q Artifact: Draft / Pending Approval

```yaml
---
artifact_type: q
artifact_id: GDS-Q-20260711-001
title: Command Center Component Interface Specification
schema_version: "1.0"
artifact_version: "0.1"
status: draft
lifecycle_state: draft
created_date: "2026-07-11"
updated_date: "2026-07-11"
owner: Ghost Development System Docs
target_project: Ghost Development System
working_repository: Ghost-Development-System-Docs
source_of_truth: q_artifact
human_approval: pending
related_q: null
related_completion_report: null
related_handoff: null
related_registry_update: null
related_rules:
  - docs/rules/ai_collaboration_rules.md
related_templates:
  - templates/Q_TEMPLATE.md
related_artifacts:
  - docs/architecture/command_center_architecture.md
inputs:
  - docs/architecture/artifact_schema_standard.md
outputs:
  - docs/requests/draft/gds/example/request.md
verification_status: not_started
recommended_next_action: Human review before approval
---
```

Body:

```markdown
# Command Center Component Interface Specification Q

This Q drafts component interface boundaries. It is not approved for execution.
```

Why this metadata is valid:

- Required fields are present.
- `status: draft`, `lifecycle_state: draft`, and `human_approval: pending` are consistent.
- Missing single references use `null`.
- Related lists use arrays.

### Completion Report: Completed / Verification Passed

```yaml
---
artifact_type: completion_report
artifact_id: GDS-REPORT-20260711-001
title: Artifact Schema Standard Completion Report
schema_version: "1.0"
artifact_version: "1.0"
status: complete
lifecycle_state: completed
created_date: "2026-07-11"
updated_date: "2026-07-11"
owner: Ghost Development System Docs
target_project: Ghost Development System
working_repository: Ghost-Development-System-Docs
source_of_truth: completion_report
human_approval: not_required
related_q: C:/Users/tanat/Downloads/Q_GDS_Artifact_Schema_Standard_JP.md
related_completion_report: reports/artifact_schema_standard_completion_report.md
related_handoff: null
related_registry_update: null
related_rules:
  - docs/rules/ai_collaboration_rules.md
related_templates:
  - templates/completion_report_template.md
related_artifacts:
  - docs/architecture/artifact_schema_standard.md
inputs:
  - C:/Users/tanat/Downloads/Q_GDS_Artifact_Schema_Standard_JP.md
outputs:
  - docs/architecture/artifact_schema_standard.md
verification_status: passed
recommended_next_action: Create structured artifact metadata template
---
```

Body:

```markdown
# Artifact Schema Standard Completion Report

Summary, verification, remaining issues, and recommended next Q are recorded below.
```

Why this metadata is valid:

- Completed artifact uses `status: complete`, `lifecycle_state: completed`, and `verification_status: passed`.
- Metadata points to artifacts instead of duplicating the report body.

### Information Package: Active / Unknown Owner

```yaml
---
artifact_type: information_package
artifact_id: GDS-IP-20260711-001
title: Command Center Current State Package
schema_version: "1.0"
artifact_version: "0.1"
status: active
lifecycle_state: reviewed
created_date: "2026-07-11"
updated_date: "2026-07-11"
owner: unknown
target_project: Ghost Development System
working_repository: Ghost-Development-System-Docs
source_of_truth: information_package
human_approval: required
related_q: null
related_completion_report: null
related_handoff: null
related_registry_update: null
related_rules: []
related_templates:
  - templates/information_package_template.md
related_artifacts:
  - roadmap/ghost_development_system_roadmap.md
inputs:
  - docs/ai_repository_index.md
outputs: []
verification_status: partial
recommended_next_action: Assign owner before approval
---
```

Why this metadata is valid:

- `unknown` is used only where the value should exist but is not known yet.
- `[]` is used for empty lists.
- `verification_status: partial` honestly reflects incomplete review.

### Multi-AI Handoff: Approved

```yaml
---
artifact_type: multi_ai_handoff
artifact_id: GDS-HANDOFF-20260711-001
title: Artifact Metadata Work Handoff
schema_version: "1.0"
artifact_version: "1.0"
status: active
lifecycle_state: approved
created_date: "2026-07-11"
updated_date: "2026-07-11"
owner: Ghost Development System Docs
target_project: Ghost Development System
working_repository: Ghost-Development-System-Docs
source_of_truth: repository
human_approval: approved
related_q: docs/requests/draft/gds/example/request.md
related_completion_report: docs/requests/draft/gds/example/completion_report.md
related_handoff: null
related_registry_update: null
related_rules:
  - docs/rules/ai_collaboration_rules.md
related_templates:
  - templates/multi_ai_handoff_template.md
related_artifacts:
  - templates/structured_artifact_metadata_template.md
inputs:
  - docs/requests/draft/gds/example/completion_report.md
outputs:
  - next_ai_entry_point
verification_status: passed
recommended_next_action: Continue from completion report
---
```

Why this metadata is valid:

- `human_approval: approved` is paired with `lifecycle_state: approved`.
- It does not treat the handoff as execution.

### Registry Update: Archived

```yaml
---
artifact_type: registry_update
artifact_id: GDS-REGISTRY-20260711-001
title: Legacy Standard Archive Update
schema_version: "1.0"
artifact_version: "1.0"
status: archived
lifecycle_state: archived
created_date: "2026-07-11"
updated_date: "2026-07-11"
owner: Ghost Development System Docs
target_project: Ghost Development System
working_repository: Ghost-Development-System-Docs
source_of_truth: repository
human_approval: approved
related_q: null
related_completion_report: reports/example_completion_report.md
related_handoff: null
related_registry_update: registry_updates/20260711_legacy_standard_archive.md
related_rules:
  - docs/rules/core_principles.md
related_templates:
  - templates/platform_registry_update_template.md
related_artifacts:
  - docs/architecture/platform_standard_registry.md
inputs:
  - reports/example_completion_report.md
outputs:
  - docs/architecture/platform_standard_registry.md
verification_status: passed
recommended_next_action: null
---
```

Why this metadata is valid:

- Archived state is explicit.
- No next action is needed, so `recommended_next_action: null` is correct.

### Health Report: Completed / Not Applicable Project

```yaml
---
artifact_type: health_report
artifact_id: GDS-HEALTH-20260711-001
title: Repository Quality Report
schema_version: "1.0"
artifact_version: "1.0"
status: complete
lifecycle_state: completed
created_date: "2026-07-11"
updated_date: "2026-07-11"
owner: Ghost Development System Docs
target_project: not_applicable
working_repository: Ghost-Development-System-Docs
source_of_truth: repository
human_approval: not_required
related_q: null
related_completion_report: null
related_handoff: null
related_registry_update: null
related_rules: []
related_templates: []
related_artifacts:
  - reports/repository_quality_report.md
inputs:
  - scripts/repository_quality_audit.py
outputs:
  - reports/repository_quality_report.md
verification_status: passed
recommended_next_action: null
---
```

Why this metadata is valid:

- `not_applicable` is used because health report is repository-wide, not project-specific.
- Empty optional lists use `[]`.

## Bad Examples / Anti-Patterns

### Required Field Missing

Problem:

`artifact_type` is missing.

Risk:

Command Center cannot classify the artifact.

Corrected example:

```yaml
artifact_type: q
artifact_id: GDS-Q-20260711-002
title: Example Q
```

### Invalid Lifecycle / Status Combination

Problem:

```yaml
status: archived
lifecycle_state: draft
```

Risk:

The artifact is both active draft and archived.

Corrected example:

```yaml
status: archived
lifecycle_state: archived
```

### Approved But Draft

Problem:

```yaml
human_approval: approved
lifecycle_state: draft
```

Risk:

Human Approval boundary is unclear.

Corrected example:

```yaml
human_approval: pending
lifecycle_state: draft
```

### Metadata Completeness Treated As Approval

Problem:

All metadata fields are filled, so the artifact is treated as approved.

Risk:

Automation or AI may bypass Human Approval.

Corrected example:

```yaml
human_approval: pending
recommended_next_action: Human review required
```

### Unknown Overuse

Problem:

```yaml
artifact_type: unknown
title: unknown
working_repository: unknown
```

Risk:

The metadata provides no useful routing information.

Corrected example:

```yaml
artifact_type: completion_report
title: Artifact Metadata Reference Examples Completion Report
working_repository: Ghost-Development-System-Docs
```

### Empty String For Optional Single Reference

Problem:

```yaml
related_q: ""
```

Risk:

Empty strings are ambiguous.

Corrected example:

```yaml
related_q: null
```

### Null For Optional List

Problem:

```yaml
related_rules: null
```

Risk:

List fields become inconsistent.

Corrected example:

```yaml
related_rules: []
```

### Long Body Duplicated In Metadata

Problem:

`recommended_next_action` contains a long multi-paragraph explanation.

Risk:

Metadata becomes hard to diff and parse.

Corrected example:

```yaml
recommended_next_action: Create metadata validation Q
```

Put the detailed reasoning in the Markdown body.

### Absolute Local Path Dependency

Problem:

```yaml
related_artifacts:
  - C:/Users/example/private/path/secret_notes.md
```

Risk:

The path is private, non-portable, and may expose local information.

Corrected example:

```yaml
related_artifacts:
  - docs/architecture/artifact_schema_standard.md
```

### Draft Artifact As Execution Command

Problem:

```yaml
status: draft
lifecycle_state: draft
recommended_next_action: Run this immediately
```

Risk:

Draft artifact bypasses approval.

Corrected example:

```yaml
status: draft
lifecycle_state: draft
recommended_next_action: Human review before execution
```

## Field Pressure Review

Artifact type fit:

| Artifact Type | Field Pressure Review |
| --- | --- |
| Q | Required fields are useful; `related_completion_report` is usually `null` at draft time. |
| Completion Report | Required fields fit well; `related_completion_report` may point to itself or be omitted in future revision. |
| Information Package | `owner` may often be `unknown`; keep required for now but review after examples accumulate. |
| Multi-AI Handoff | Related fields are useful; `related_handoff` is usually `null` unless chaining handoffs. |
| Registry Update | Related registry update is essential; current schema supports it. |
| Health Report | `target_project: not_applicable` is practical for repository-wide health. |

Design observations:

- `owner` is useful but may need clearer guidance for AI-generated artifacts.
- `status` and `lifecycle_state` overlap, but they serve different needs:
  current condition vs process state.
- `source_of_truth` allowed values are adequate for current examples.
- Related fields are somewhat many, but separating them improves scanning.
- Dates are practical if `unknown` is allowed during draft creation.

Template improvement candidates:

- Add a short owner guidance note.
- Clarify whether `related_completion_report` can point to the current file.
- Add example-specific guidance for self-reference avoidance.

Validator candidates:

- Required field presence.
- Allowed value checks.
- `human_approval: approved` cannot pair with `lifecycle_state: draft`.
- List fields must use arrays.
- Optional single references should use `null` when empty.

## Related Documents

- `templates/structured_artifact_metadata_template.md`
- `docs/architecture/artifact_schema_standard.md`
- `docs/architecture/command_center_architecture.md`
- `templates/completion_report_template.md`
