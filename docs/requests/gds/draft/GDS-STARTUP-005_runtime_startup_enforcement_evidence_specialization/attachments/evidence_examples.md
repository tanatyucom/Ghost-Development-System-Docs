# Evidence Examples

## PASS Example

```yaml
evidence_id: startup-20260717-001
evidence_type: startup_enforcement
producer: Runtime Startup Enforcement
consumer:
  - Template Engine
  - Completion Review
source_request: Q_GDS-STARTUP-005_runtime_startup_enforcement_evidence_specialization_JP.md
target_project: Ghost Development System
working_repository: Ghost-Development-System-Docs
scope:
  - architecture documentation
  - request workspace
out_of_scope:
  - runtime code
  - GameGhost
  - commit
inputs:
  - docs/architecture/platform_execution_evidence_contract.md
  - docs/architecture/runtime_startup_enforcement.md
checks_performed:
  - repository_verification
  - template_verification
  - revision_first_decision
  - constraint_check
result: PASS
reason_codes:
  - INTENT_CLASSIFIED
  - WORKFLOW_RESOLVED
  - CANONICAL_REPOSITORY_VERIFIED
  - CANONICAL_TEMPLATE_VERIFIED
  - GENERATION_GATE_PASSED
limitations: []
missing_or_conflicting_evidence: []
human_approval_state: not_required
scw_reason: null
allowed_next_step: generate_requested_documentation
blocked_next_step:
  - commit
  - push
created_at: 2026-07-17
related_artifacts:
  - docs/architecture/runtime_startup_enforcement_evidence_specialization.md
```

## PASS_WITH_LIMITATION Example

```yaml
evidence_id: startup-20260717-002
evidence_type: startup_enforcement
producer: Human-executed Startup workflow
consumer:
  - Completion Review
source_request: user_request
target_project: Ghost Development System
working_repository: Ghost-Development-System-Docs
scope:
  - draft artifact
out_of_scope:
  - commit
inputs:
  - local canonical template
checks_performed:
  - template_verification
  - constraint_check
result: PASS_WITH_LIMITATION
reason_codes:
  - CANONICAL_TEMPLATE_VERIFIED
  - RAW_FRESHNESS_LIMITED
  - GENERATION_GATE_PASSED
limitations:
  - Public Raw freshness was not required for this local-only documentation update.
missing_or_conflicting_evidence: []
human_approval_state: not_required
scw_reason: null
allowed_next_step: generate_draft_with_limitation_note
blocked_next_step:
  - commit
  - push
created_at: 2026-07-17
related_artifacts:
  - completion_report.md
```

## BLOCK Example

```yaml
evidence_id: startup-20260717-003
evidence_type: startup_enforcement
producer: Runtime Startup Enforcement
consumer:
  - Template Engine
source_request: user_request
target_project: Ghost Development System
working_repository: unknown
scope: []
out_of_scope:
  - repository mutation
inputs:
  - user_request
checks_performed:
  - repository_verification
result: BLOCK
reason_codes:
  - REPOSITORY_NOT_VERIFIED
limitations: []
missing_or_conflicting_evidence:
  - working_repository could not be confirmed
human_approval_state: blocked
scw_reason: null
allowed_next_step: verify_repository_root
blocked_next_step:
  - generate_managed_artifact
  - edit_files
created_at: 2026-07-17
related_artifacts: []
```

## SCW_REQUIRED Example

```yaml
evidence_id: startup-20260717-004
evidence_type: startup_enforcement
producer: Runtime Startup Enforcement
consumer:
  - Human Reviewer
  - Command Center
source_request: user_request
target_project: Ghost Development System
working_repository: Ghost-Development-System-Docs
scope:
  - startup evidence
out_of_scope:
  - runtime implementation
inputs:
  - user_request
  - existing architecture index
checks_performed:
  - revision_first_decision
  - constraint_check
result: SCW_REQUIRED
reason_codes:
  - DUPLICATE_OR_REVISION_CONFLICT
  - REVISION_OR_NEW_ARTIFACT_UNCLEAR
  - SCW_REQUIRED
limitations: []
missing_or_conflicting_evidence:
  - whether to revise existing architecture or create a new specialization
human_approval_state: pending
scw_reason: Existing artifact candidate and new artifact request conflict.
allowed_next_step: ask_human_to_choose_revision_or_new_artifact
blocked_next_step:
  - generate_final_artifact
created_at: 2026-07-17
related_artifacts:
  - docs/architecture/runtime_startup_enforcement.md
```
