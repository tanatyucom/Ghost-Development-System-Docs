# Evidence Examples

## Green / PASS Example

```yaml
evidence_id: rq-20260717-001
evidence_type: repository_quality
producer: Repository Quality Audit
consumer:
  - Completion Review
  - Command Center
source_request: GDS-REPOSITORY-QUALITY-EVIDENCE-001
target_project: Ghost Development System
working_repository: Ghost-Development-System-Docs
scope:
  - whole_repository
out_of_scope:
  - GameGhost
  - commit
inputs:
  - scripts/repository_quality_audit.py
  - docs/ai_repository_index.md
  - reports/repository_quality_report.md
checks_performed:
  - UTF-8 Audit
  - Mojibake Audit
  - AI Repository Index Validation
  - GDS Health Validation
  - Broken Link Check
  - Markdown Validation
quality_state: Green
result: PASS
reason_codes:
  - QUALITY_GREEN
  - REQUIRED_CHECKS_PASSED
limitations: []
missing_or_conflicting_evidence: []
human_approval_state: not_required
scw_reason: null
allowed_next_step:
  - continue_documentation_work
  - prepare_completion_report
blocked_next_step:
  - commit_without_explicit_approval
  - push_without_explicit_approval
created_at: 2026-07-17
related_artifacts:
  - reports/repository_quality_report.md
```

## Yellow / PASS_WITH_LIMITATION Example

```yaml
evidence_id: rq-20260717-002
evidence_type: repository_quality
producer: Repository Quality Audit
consumer:
  - Completion Review
source_request: completion_review
target_project: Ghost Development System
working_repository: Ghost-Development-System-Docs
scope:
  - whole_repository
out_of_scope:
  - commit
inputs:
  - scripts/repository_quality_audit.py
checks_performed:
  - Documentation Synchronization Gate
quality_state: Yellow
result: PASS_WITH_LIMITATION
reason_codes:
  - QUALITY_YELLOW
  - WARNING_PRESENT
limitations:
  - One non-blocking documentation synchronization warning remains.
missing_or_conflicting_evidence: []
human_approval_state: pending
scw_reason: null
allowed_next_step:
  - repair_warning
  - create_followup_q
blocked_next_step:
  - claim_green
  - commit_without_warning_acceptance
created_at: 2026-07-17
related_artifacts:
  - reports/repository_quality_report.md
```

## Red / BLOCK Example

```yaml
evidence_id: rq-20260717-003
evidence_type: repository_quality
producer: Repository Quality Audit
consumer:
  - Completion Review
source_request: pre_commit_review
target_project: Ghost Development System
working_repository: Ghost-Development-System-Docs
scope:
  - whole_repository
out_of_scope:
  - push
inputs:
  - scripts/validate_encoding_regression.py
checks_performed:
  - Encoding Regression Validation
quality_state: Red
result: BLOCK
reason_codes:
  - QUALITY_RED
  - CRITICAL_CHECK_FAILED
limitations: []
missing_or_conflicting_evidence: []
human_approval_state: blocked
scw_reason: null
allowed_next_step:
  - repair_blocking_failure
  - rerun_quality_audit
blocked_next_step:
  - commit_recommendation
  - push_recommendation
created_at: 2026-07-17
related_artifacts:
  - reports/repository_quality_report.md
```

## Unknown / SCW_REQUIRED Example

```yaml
evidence_id: rq-20260717-004
evidence_type: repository_quality
producer: Human-executed Quality Workflow
consumer:
  - Command Center
  - Human Reviewer
source_request: startup_gate
target_project: Ghost Development System
working_repository: Ghost-Development-System-Docs
scope:
  - whole_repository
out_of_scope:
  - repository_mutation
inputs:
  - reports/repository_quality_report.md
checks_performed:
  - report_review
quality_state: Unknown
result: SCW_REQUIRED
reason_codes:
  - QUALITY_UNKNOWN
  - EVIDENCE_CONFLICT
  - SCW_REQUIRED
limitations: []
missing_or_conflicting_evidence:
  - Report summary and raw validation output disagree.
human_approval_state: pending
scw_reason: Quality report and raw output conflict.
allowed_next_step:
  - collect_missing_evidence
  - rerun_quality_audit
blocked_next_step:
  - treat_as_green
  - commit_recommendation
created_at: 2026-07-17
related_artifacts:
  - reports/repository_quality_report.md
```
