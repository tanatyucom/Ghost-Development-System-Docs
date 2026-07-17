# Evidence Examples

## PASS Example

```yaml
evidence_id: cr-20260717-001
evidence_type: completion_review
producer: Completion Report Workflow
consumer:
  - Human Reviewer
  - Command Center
source_request: GDS-COMPLETION-REVIEW-EVIDENCE-001
target_project: Ghost Development System
working_repository: Ghost-Development-System-Docs
scope:
  - completion review evidence architecture
out_of_scope:
  - GameGhost
  - commit
inputs:
  - source_q
  - changed_files
  - repository_quality_evidence
checks_performed:
  - changed_files_review
  - verification_review
  - safe_commit_set_review
result: PASS
reason_codes:
  - COMPLETION_SCOPE_CONFIRMED
  - VERIFICATION_PASSED
  - SAFE_COMMIT_SET_CONFIRMED
limitations: []
missing_or_conflicting_evidence: []
human_approval_state: required
scw_reason: null
allowed_next_step:
  - request_human_commit_approval
  - proceed_to_platform_ready_review
blocked_next_step:
  - commit_without_approval
  - push_without_approval
created_at: 2026-07-17
related_artifacts:
  - completion_report.md
```

## PASS_WITH_LIMITATION Example

```yaml
evidence_id: cr-20260717-002
evidence_type: completion_review
producer: Completion Checklist Workflow
consumer:
  - Human Reviewer
source_request: completion_review
target_project: Ghost Development System
working_repository: Ghost-Development-System-Docs
scope:
  - documentation update
out_of_scope:
  - push
inputs:
  - completion_report
  - repository_quality_report
checks_performed:
  - verification_review
  - quality_evidence_review
result: PASS_WITH_LIMITATION
reason_codes:
  - VERIFICATION_LIMITED
  - COMMIT_APPROVAL_REQUIRED
limitations:
  - Standard python command failed for one script, bundled Python was used successfully.
missing_or_conflicting_evidence: []
human_approval_state: required
scw_reason: null
allowed_next_step:
  - request_human_review
blocked_next_step:
  - commit_without_approval
created_at: 2026-07-17
related_artifacts:
  - completion_report.md
```

## BLOCK Example

```yaml
evidence_id: cr-20260717-003
evidence_type: completion_review
producer: AI-assisted completion review
consumer:
  - Human Reviewer
source_request: pre_commit_review
target_project: Ghost Development System
working_repository: Ghost-Development-System-Docs
scope:
  - current_q
out_of_scope:
  - push
inputs:
  - verification_output
checks_performed:
  - verification_review
result: BLOCK
reason_codes:
  - VERIFICATION_FAILED
limitations: []
missing_or_conflicting_evidence: []
human_approval_state: blocked
scw_reason: null
allowed_next_step:
  - repair_failure
blocked_next_step:
  - commit_recommendation
created_at: 2026-07-17
related_artifacts:
  - reports/repository_quality_report.md
```

## SCW_REQUIRED Example

```yaml
evidence_id: cr-20260717-004
evidence_type: completion_review
producer: Completion Report Workflow
consumer:
  - Human Reviewer
source_request: completion_claim
target_project: Ghost Development System
working_repository: Ghost-Development-System-Docs
scope:
  - unknown
out_of_scope:
  - repository_mutation
inputs:
  - git_status
checks_performed:
  - changed_files_review
result: SCW_REQUIRED
reason_codes:
  - DIRTY_WORKSPACE_CONFLICT
  - SCW_REQUIRED
limitations: []
missing_or_conflicting_evidence:
  - Changed files do not match Safe Commit Set.
human_approval_state: pending
scw_reason: Dirty workspace contains changes whose origin is unclear.
allowed_next_step:
  - ask_human_for_scope_decision
blocked_next_step:
  - commit_recommendation
created_at: 2026-07-17
related_artifacts:
  - git_status_output
```
