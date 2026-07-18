# Canonical Asset Inventory

## Assessment

Existing definition assessment:

```text
C. Definition exists and is complete but weakly enforced
```

The repository already defines Startup as an AI-facing repository
synchronization protocol. The observed failure risk is not absence of the
definition. The gap is operational evidence and freshness enforcement: AI can
claim Startup from memory unless final response and completion artifacts record
which canonical assets were actually resolved.

## Canonical Assets Reviewed

| Path | Authority | Relevant Heading | Type | Finding |
| --- | --- | --- | --- | --- |
| `README.md` | Entry point | AI Startup Procedure | Normative index | AI Startup is visible from the root README, but the repository-context evidence meaning needed clarification. |
| `docs/README.md` | Knowledge Base index | AI Startup Procedure Index | Normative index | Lists the Startup reading order and Pre-Response gate. Updated to mention Repository Context Evidence. |
| `docs/ai_repository_index.md` | Generated AI entry point | AI Usage Rule | Normative index | Requires AI to read the index first and report missing access honestly. |
| `docs/rules/ai_startup_procedure_rules.md` | Rule | Core Rule / Startup Completion Evidence | Normative | Defines AI startup order and evidence. Updated with Repository-Aware AI Rule and refresh requirements. |
| `docs/workflow/ai_startup_procedure.md` | Workflow | Standard Flow | Normative workflow | Defines AI-facing reading order before implementation, review, documentation update, or Q execution. Updated with repository precedence and task-specific refresh. |
| `docs/workflow/startup_completion_evidence.md` | Evidence workflow | Required Evidence | Normative workflow | Defines proof that canonical sources were reviewed. Updated with Repository Context Evidence and Freshness / Invalidation. |
| `docs/workflow/startup_completion_gate.md` | Gate workflow | Gate Decision | Normative workflow | Defines PASS / limitation / blocked behavior. Updated to require repository context evidence. |
| `docs/workflow/pre_response_verification_gate.md` | Final response gate | Required Checks | Normative workflow | Defines final response checks. Updated to check repository context freshness and task-specific refresh. |
| `templates/startup_verification_checklist.md` | Template | Startup Completion Evidence | Normative template | Updated with Repository Context Evidence and Freshness / Invalidation sections. |
| `templates/ai_response_checklist_v2.md` | Template | Startup / Context | Normative checklist | Updated with repository context evidence checks. |
| `templates/response_verification_checklist.md` | Template | Pre-Response Verification Gate | Normative checklist | Updated with canonical asset and repository context checks. |
| `templates/completion_report_template.md` | Template | Startup Completion Evidence / Pre-Response Verification Gate | Normative template | Updated to preserve repository context evidence in completion artifacts. |
| `templates/Q_TEMPLATE.md` | Template | Canonical Template Synchronization | Normative template | Already requires canonical template source, repository confirmation, and raw freshness. No change needed. |
| `docs/workflow/artifact_creation_startup_enforcement_workflow.md` | Workflow | Canonical Repository / Template Verification | Normative workflow | Already blocks remembered template generation. No change needed. |
| `docs/rules/artifact_creation_startup_enforcement_rules.md` | Rule | Forbidden Behavior | Normative rule | Already forbids remembered templates and unattempted repository access claims. No change needed. |
| `docs/workflow/repository_drift_prevention.md` | Future Candidate | Repository Re-anchor | Future candidate | Already captures mid-work drift risk; kept as future candidate rather than promoted here. |
| `docs/philosophy/human_ai_collaboration_model.md` | Philosophy | Roles | Philosophy standard | Updated with AI role definition from supplied source material. |
| `docs/rules/ai_collaboration_rules.md` | Rule | AI Is A Partner / Repository First | Normative rule | Updated with repository-aware AI role boundary. |
| `examples/persistent_collaboration_examples.md` | Examples | AI Collaboration | Example | Updated with classify-before-implement and human approval examples from supplied source material. |

## Supporting Source Inputs

The following supplied project information sources were preserved as input
evidence for this review:

- `attachments/source_inputs/startup_revision.md`
- `attachments/source_inputs/Constraint_Check.md`
- `attachments/source_inputs/Q_GDS_AI_Response_Checklist_JP.md`
- `attachments/source_inputs/GDS_AI_Collaboration_Examples.md`
- `attachments/source_inputs/GDS_AI_Role_Definition_v1.2.md`

They were not treated as higher priority than repository canonical files.
Reusable parts were integrated by revising existing canonical assets.
