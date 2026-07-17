# Template Integration Matrix

## Purpose

This matrix records how Artifact Creation Startup Enforcement is connected to
templates, rules, workflows, and completion reporting.

## Integration Matrix

| Layer | File | Integration |
| --- | --- | --- |
| Q Template | `templates/Q_TEMPLATE.md` | Adds the required evidence block before managed artifact drafting. |
| Q Rule | `docs/rules/q_file_template_rules.md` | Makes the evidence block mandatory for official Q files. |
| Q Workflow | `docs/workflow/q_file_creation_workflow.md` | Runs enforcement before Q ID selection and Q body drafting. |
| Startup Evidence | `templates/startup_verification_checklist.md` | Adds enforcement fields to startup evidence collection. |
| Startup Gate | `docs/workflow/startup_completion_gate.md` | Treats `BLOCK` and `SCW_REQUIRED` as startup blockers. |
| Completion Report Template | `templates/completion_report_template.md` | Records gate decision, limitation, reason codes, and SCW reason. |
| Completion Report Workflow | `docs/workflow/completion_report_workflow.md` | Requires enforcement result recording when managed artifact creation or revision occurred. |
| Template Index | `templates/README.md` | Explains the new template-level requirement. |

## Gate Values

```text
PASS
PASS_WITH_LIMITATION
BLOCK
SCW_REQUIRED
```

## Required Evidence Fields

```text
Artifact Intent
Required Workflow
Required Knowledge
Canonical Repository Verification
Canonical Template Verification
Revision First Decision
Constraint Check
Gate Decision
Gate Reason Codes
Missing / Conflicting Evidence
SCW Reason
```

## Compatibility

- Historical artifacts are not rewritten.
- Existing Q files can remain as historical records.
- New or revised official Q files should use `templates/Q_TEMPLATE.md` v2.1.
- Completion Reports should record this gate when the task involved managed
  artifact creation or revision.
