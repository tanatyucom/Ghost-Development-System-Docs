# Template Inventory Audit

## Scope

This audit checks the public template inventory for GDS-STARTUP-003 and decides
where Artifact Creation Startup Enforcement evidence should be integrated.

## Folder Findings

| Location | Result | Decision |
| --- | --- | --- |
| `templates/` | Exists and contains canonical templates. | Use as canonical template source. |
| `docs/templates/` | Not found. | Do not create a duplicate template folder. |

## Directly Updated Templates

| Template | Reason | Change Type |
| --- | --- | --- |
| `templates/Q_TEMPLATE.md` | Q artifacts are the first managed artifact type affected by Artifact Creation Startup Enforcement. | Added required evidence block and gate values. |
| `templates/completion_report_template.md` | Completion Reports must record whether the startup enforcement gate was used and what decision was made. | Added evidence block for gate result and limitations. |
| `templates/startup_verification_checklist.md` | Startup evidence must include artifact generation gate results before Q creation, implementation, review, or documentation update proceeds. | Added checklist fields and source evidence row. |
| `templates/README.md` | Template users need an index-level explanation of the new evidence requirement. | Added template policy guidance. |

## Related Rule / Workflow Updates

| File | Reason |
| --- | --- |
| `docs/rules/q_file_template_rules.md` | Makes the evidence block mandatory for official Q files. |
| `docs/workflow/q_file_creation_workflow.md` | Places the enforcement gate before Q ID and main Q body drafting. |
| `docs/workflow/startup_completion_gate.md` | Connects the enforcement gate to Startup Completion Gate PASS / BLOCK decisions. |
| `docs/workflow/completion_report_workflow.md` | Requires Completion Reports to record enforcement results when managed artifact creation or revision was involved. |

## Templates Reviewed But Not Changed

| Template Group | Examples | Reason Not Changed |
| --- | --- | --- |
| Planning templates | `roadmap_template.md`, `decision_template.md`, `adr_template.md` | These are downstream managed artifacts, but this Q only standardizes Q, startup evidence, and completion reporting. |
| Development templates | `specification_template.md`, `architecture_template.md`, `feature_template.md`, `bugfix_template.md`, `refactoring_template.md` | Future shared managed-artifact header may be useful, but broad migration is outside this Q. |
| Collaboration templates | `ai_implementation_request.md`, `codex_review_template.md`, `multi_ai_handoff_template.md`, `information_package_template.md` | No direct Q requirement to update these files. |
| Release templates | `release_checklist.md`, `release_notes_template.md` | Release artifacts are not part of this startup enforcement integration Q. |

## Recommendation

Create a future Q for a shared "Managed Artifact Startup Evidence" block if
the same fields need to be propagated across ADR, roadmap, architecture,
specification, review, handoff, and release templates.
