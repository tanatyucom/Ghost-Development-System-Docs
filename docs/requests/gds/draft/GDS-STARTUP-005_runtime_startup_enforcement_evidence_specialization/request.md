# Q_GDS-STARTUP-005 Runtime Startup Enforcement Evidence Specialization

**Template Version:** 2.1
**Created Date:** 2026-07-17
**Last Updated Date:** 2026-07-17

## Identity

- Q ID: GDS-STARTUP-005
- Title: Runtime Startup Enforcement Evidence Specialization
- Version: 1.0
- Status: Draft
- Priority: Critical
- Category: Startup Enforcement / Platform Execution Evidence / Architecture Contract
- Created Date: 2026-07-17
- Last Updated Date: 2026-07-17
- Owner / Target AI: Codex

## Artifact Output

- Markdown required: Yes
- `.docx` required when human review is expected: No
- Chat body should contain summary only: Yes
- Required artifacts:
  - `request.md`: Yes
  - `notes.md`: Yes
  - `completion_report.md`: Yes
  - `attachments/`: Yes
  - `addendum_*.md`: Only when required by Revision / Addendum Policy

## Save Location

Preferred Task Artifact Workspace:

```text
docs/requests/gds/draft/GDS-STARTUP-005_runtime_startup_enforcement_evidence_specialization/
├── request.md
├── notes.md
├── completion_report.md
└── attachments/
    ├── parent_field_mapping.md
    ├── startup_evidence_field_catalog.md
    ├── result_and_reason_code_mapping.md
    ├── producer_consumer_and_approval_matrix.md
    ├── compatibility_and_extension_review.md
    ├── evidence_examples.md
    └── beginner_future_self_test.md
```

The canonical Startup Evidence Specialization should be added by Revision First to the most appropriate existing architecture location after repository audit.

Expected candidate:

```text
docs/architecture/runtime_startup_enforcement_evidence_specialization.md
```

Codex must confirm that no equivalent canonical artifact already exists before creating it.

Standalone handoff filename:

```text
Q_GDS-STARTUP-005_runtime_startup_enforcement_evidence_specialization_JP.md
```

## File Naming

- Standard filename: `Q_GDS-STARTUP-005_runtime_startup_enforcement_evidence_specialization_JP.md`
- Slug: `runtime_startup_enforcement_evidence_specialization`
- Date is recorded in metadata, not the filename.

## Status

- Status folder: `draft`
- Current status: Draft

## Repository Context

- Working Repository: Ghost-Development-System-Docs
- Working Directory: `C:\GitHub\Ghost-Development-System-Docs`
- Preferred Shell: PowerShell
- Target Project: Ghost Development System
- Non-Target Project:
  - GameGhost
  - GrayGhostArchive
  - AnimeGhost
  - ComicGhost
  - Other field-project runtime repositories
- Allowed Edit Scope:
  - GDS Startup Enforcement architecture
  - Platform Execution Evidence references
  - Startup workflow / template references when required
  - request workspace
  - README / roadmap references when evidence justifies revision
  - AI Repository Index
  - Repository Quality Report
- Forbidden Edit Scope:
  - GameGhost / GrayGhostArchive runtime
  - field-project databases and production data
  - runtime code
  - JSON Schema implementation
  - YAML serialization implementation
  - GUI / plugin / server implementation
  - automatic artifact generation
  - automatic repository mutation
  - commit / push / tag
- Documentation Root: `C:\GitHub\Ghost-Development-System-Docs`
- Runtime Root: Not Applicable
- Single Source Of Truth: Ghost-Development-System-Docs repository
- Related Repository: Not Applicable
- Cross Project Impact: High
- Scope Guard:

```text
Define Startup Enforcement Evidence as a specialization of the canonical
Platform Execution Evidence Contract.

Do not create a competing parent evidence model.
Do not implement runtime serialization or executable validation.
Do not edit GameGhost.
Do not commit, push, or tag.
```

## Canonical Template Synchronization

- Startup completed: Yes
- AI Repository Index verified: Yes
- Current Mission verified: Yes
- Template revision verified: Yes
- Template revision source: `templates/Q_TEMPLATE.md`
- Canonical Repository confirmed: Yes
- Canonical Repository path: `Ghost-Development-System-Docs/templates/Q_TEMPLATE.md`
- Raw reference freshness confirmed when applicable: Yes
- Raw reference URL:

```text
https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/templates/Q_TEMPLATE.md
```

- Raw reference checked at: 2026-07-17
- Template mismatch found: No
- Template mismatch action: Not Applicable

## Artifact Creation Startup Enforcement Evidence

- Artifact Intent: Create architecture specialization Q
- Required Workflow:
  - `docs/workflow/artifact_creation_startup_enforcement_workflow.md`
  - `docs/workflow/q_file_creation_workflow.md`
  - `docs/workflow/runtime_startup_enforcement_workflow.md`
- Required Knowledge:
  - `templates/Q_TEMPLATE.md`
  - `docs/ai_repository_index.md`
  - `docs/architecture/platform_execution_evidence_contract.md`
  - `docs/architecture/runtime_startup_enforcement.md`
  - `docs/architecture/intent_aware_startup_enforcement.md`
  - `docs/workflow/artifact_creation_startup_enforcement_workflow.md`
  - `docs/workflow/runtime_startup_enforcement_workflow.md`
  - `roadmap/ghost_development_system_roadmap.md`
  - GDS-STARTUP-002 Completion Report
  - GDS-STARTUP-003 Completion Report
  - GDS-STARTUP-004 Completion Report
  - GDS-ROADMAP-001 Completion Report
  - GDS-PLATFORM-EXECUTION-EVIDENCE-001 Completion Report
- Canonical Repository Verification: PASS
- Canonical Template Verification: PASS
- Revision First Decision: new_artifact_allowed
- Constraint Check: PASS
- Gate Decision: PASS
- Gate Reason Codes:
  - `INTENT_CLASSIFIED`
  - `WORKFLOW_RESOLVED`
  - `KNOWLEDGE_REQUIREMENTS_RESOLVED`
  - `CANONICAL_REPOSITORY_VERIFIED`
  - `CANONICAL_TEMPLATE_VERIFIED`
  - `REVISION_FIRST_DECIDED`
  - `CONSTRAINT_CHECK_PASSED`
  - `GENERATION_GATE_PASSED`
- Missing / Conflicting Evidence:
  - Codex must verify the latest local main branch and actual canonical paths before editing.
- SCW Reason: Not Applicable at Q creation

## Commit / Push Policy

- Commit: Do not execute
- Push: Do not execute
- Suggested Commit Message:

```text
docs(startup): define startup execution evidence specialization
```

## Purpose

`Platform Execution Evidence Contract`を親Contractとして、Runtime Startup Enforcementが生成するEvidenceのStartup固有構造、意味、状態、reason code、producer / consumer、Human Approval、SCW、互換性を定義する。

このQにより、STARTUP-004で定義したruntime evidence modelをPlatform共通Contractへ正式に接続する。

目標は次のとおり。

```text
Platform Execution Evidence Contract
        ↓ extends
Runtime Startup Enforcement Evidence Specialization
        ↓ future implementation
Startup Evidence JSON / YAML Schema
        ↓ future runtime
Runtime Startup Enforcement
```

本QはSpecialization architectureを定義する。実行可能Schemaやruntime codeは実装しない。

## Background

GDS-STARTUP-004では、Runtime Startup Enforcementの以下を設計した。

- state machine
- gate decision contract
- startup evidence model
- startup execution log
- repository interaction contract
- Human Approval boundary
- Command Center integration
- failure recovery
- reason codes

その時点では、Startup固有のEvidence Modelが先行していた。

GDS-ROADMAP-001では、STARTUP-005へ直行すると次の領域と重複する可能性があると判断した。

- Repository Quality Evidence
- Command Center Execution Evidence
- Completion Review Evidence
- Knowledge Promotion Evidence

そこでGDS-PLATFORM-EXECUTION-EVIDENCE-001を先に実施し、共通親Contractを定義した。

親Contractは以下を要求する。

- common lifecycle
- required parent fields
- common result meaning
- producer / consumer ownership
- Human Approval state
- SCW evidence
- allowed / blocked next step
- extension rules
- versioning and compatibility rules

本Qは、STARTUP-004の既存Evidence Modelを破棄するのではなく、Revision Firstで親Contractに適合させる。

## Primary Design Question

```text
How should Runtime Startup Enforcement express its domain-specific execution
evidence while remaining fully compatible with the common Platform Execution
Evidence Contract?
```

## Scope

### 1. Parent Contract Mapping

Startup evidenceを、`Platform Execution Evidence Contract`の全必須fieldへmappingする。

親Contract必須field:

- `evidence_id`
- `evidence_type`
- `producer`
- `consumer`
- `source_request`
- `target_project`
- `working_repository`
- `scope`
- `out_of_scope`
- `inputs`
- `checks_performed`
- `result`
- `reason_codes`
- `limitations`
- `missing_or_conflicting_evidence`
- `human_approval_state`
- `scw_reason`
- `allowed_next_step`
- `blocked_next_step`
- `created_at`
- `related_artifacts`

各fieldについて次を明記する。

- Startupでの意味
- Required / Conditional / Optional
- Data shape concept
- Producer
- Consumer
- Source
- Validation expectation
- Empty / missing behavior
- Compatibility note

### 2. Startup-Specific Field Catalog

少なくとも以下をStartup固有field候補として監査する。

- `startup_execution_id`
- `request_id`
- `artifact_intent`
- `artifact_type`
- `intent_confidence`
- `required_workflow`
- `required_knowledge`
- `repository_verification`
- `template_verification`
- `revision_first_decision`
- `constraint_check`
- `gate_decision`
- `gate_reason_codes`
- `startup_state`
- `startup_state_history`
- `missing_or_conflicting_evidence`
- `limitations`
- `scw_reason`
- `human_approval_required`
- `human_approval_state`
- `pending_action`
- `allowed_next_step`
- `blocked_next_step`
- `output_artifact_path`
- `startup_log_reference`
- `source_q`
- `known_constraints`
- `raw_freshness_state`
- `canonical_source_state`

Codex must decide whether each field is:

- inherited parent field
- Startup specialization field
- alias requiring removal
- derived field
- future serialization field
- runtime-only field
- log-only field
- not adopted

### 3. Evidence Type Definition

Canonical Startup evidence type must be defined.

Candidate:

```text
startup_enforcement
```

or:

```text
startup_gate
```

Select one canonical value and explain aliases / compatibility.

Evidence subtype candidates:

- `artifact_creation_startup`
- `artifact_revision_startup`
- `completion_report_startup`
- `roadmap_review_startup`
- `repository_mutation_preflight`
- future capability-specific startup

Do not overdesign subtype taxonomy. Adopt only evidence-supported values.

### 4. Lifecycle Specialization

Map the common lifecycle:

```text
Observed
-> Collected
-> Classified
-> Checked
-> Decided
-> Reviewed
-> Consumed
-> Archived
```

to Runtime Startup Enforcement states.

Current runtime state machine:

```text
IDLE
-> REQUEST_RECEIVED
-> INTENT_CLASSIFIED
-> WORKFLOW_RESOLVED
-> KNOWLEDGE_RESOLVED
-> REPOSITORY_VERIFIED
-> TEMPLATE_VERIFIED
-> REVISION_DECIDED
-> CONSTRAINT_CHECKED
-> GATE_DECIDED
-> COMPLETED
```

Failure states:

- `INTENT_AMBIGUOUS`
- `WORKFLOW_UNRESOLVED`
- `KNOWLEDGE_MISSING`
- `REPOSITORY_UNVERIFIED`
- `TEMPLATE_UNVERIFIED`
- `REVISION_CONFLICT`
- `CONSTRAINT_FAILED`
- `HUMAN_APPROVAL_REQUIRED`
- `SCW_WAITING`
- `BLOCKED`

Recovery states:

- `AWAITING_HUMAN_DECISION`
- `AWAITING_REPOSITORY_ACCESS`
- `AWAITING_TEMPLATE_SOURCE`
- `AWAITING_SCOPE_CLARIFICATION`
- `RESUME_REQUESTED`
- `RESUMED`

Required output:

- common lifecycle to startup state mapping
- legal transitions
- terminal states
- resumable states
- archived state behavior
- evidence update vs new evidence record decision
- repeated execution behavior
- retry relationship
- immutable history requirement

### 5. Result Mapping

Startup result values:

- `PASS`
- `PASS_WITH_LIMITATION`
- `BLOCK`
- `SCW_REQUIRED`

Map these to common action meanings:

- Proceed
- Proceed with explicit limitation
- Stop
- Ask human / wait

For every result define:

- required fields
- allowed next step
- blocked next step
- Human Approval state
- whether artifact draft generation is allowed
- whether repository mutation is allowed
- whether Completion Review may consume it
- whether Command Center may aggregate it
- required reason code classes

Explicitly preserve:

```text
No result value authorizes commit, push, tag, release, deletion,
canonical promotion, external publication, or repository mutation by itself.
```

### 6. Reason Code Specialization

Audit the STARTUP-004 reason codes.

Success:

- `INTENT_CLASSIFIED`
- `WORKFLOW_RESOLVED`
- `KNOWLEDGE_RESOLVED`
- `REPOSITORY_VERIFIED`
- `CANONICAL_TEMPLATE_VERIFIED`
- `REVISION_FIRST_DECIDED`
- `CONSTRAINT_CHECK_PASSED`
- `GATE_PASS`

Limitation:

- `KNOWLEDGE_PARTIAL`
- `NON_BLOCKING_SOURCE_MISSING`
- `RAW_FRESHNESS_LIMITED`
- `HUMAN_REVIEW_RECOMMENDED`

Blocking:

- `INTENT_AMBIGUOUS`
- `WORKFLOW_UNRESOLVED`
- `KNOWLEDGE_REQUIRED_BUT_MISSING`
- `REPOSITORY_NOT_VERIFIED`
- `TEMPLATE_NOT_VERIFIED`
- `TEMPLATE_MISMATCH`
- `DUPLICATE_OR_REVISION_CONFLICT`
- `CONSTRAINT_FAILED`
- `HUMAN_APPROVAL_REQUIRED`
- `SCW_REQUIRED`

Required design:

- canonical reason code naming rule
- success / limitation / block / SCW categories
- stable machine-readable values
- human-readable explanation requirement
- code deprecation policy
- code addition policy
- parent contract compatibility
- unknown reason code handling
- multiple reason code ordering
- primary reason vs supporting reason
- field-specific reason association

### 7. Producer / Consumer Contract

Producer:

- Runtime Startup Enforcement
- human-executed Startup workflow until runtime exists
- future Command Center adapter calling Startup Enforcement

Consumers:

- Template Engine
- Command Center
- Artifact Pipeline
- Completion Review
- Repository Quality
- Human reviewer
- future Information Package Builder

For each consumer define:

- fields required
- stop-state handling
- limitation display requirements
- prohibited reinterpretation
- whether aggregation is allowed
- whether original evidence must remain linked
- whether consumer may modify evidence
- Human Approval behavior

Core ownership rule:

```text
Runtime Startup Enforcement owns Startup gate truth.
Command Center may aggregate it but must not override it.
Template Engine may consume it but must not treat it as approval.
Human Approval Gate owns approval state.
```

### 8. Human Approval Specialization

Define Startup-specific use of:

```text
human_approval_state
```

Allowed parent values:

- `not_required`
- `required`
- `pending`
- `granted`
- `blocked`
- `rejected`

Clarify:

- when Startup can return PASS while later mutation approval is pending
- when ambiguous artifact intent requires Human Approval before generation
- when repository boundary conflict forces SCW
- when template mismatch blocks generation
- when `granted` applies only to a specific decision
- approval scope and expiry
- why quality Green is not approval
- why evidence completeness is not approval
- why previous chat approval cannot be silently reused for a different mutation

### 9. SCW Specialization

Startup SCW evidence must include:

- unknown condition
- safety reason
- blocked action
- required human decision
- available options
- evidence needed to resume
- resume target state
- prior state
- retry count or attempt reference
- pending action reference

Define relationship between:

- `SCW_REQUIRED`
- `BLOCK`
- `HUMAN_APPROVAL_REQUIRED`
- recoverable missing evidence
- nonrecoverable constraint violation

SCW is not a substitute for performing available checks.

### 10. Revision First Evidence

Define canonical evidence for:

- `new_artifact_allowed`
- `revision_required`
- `addendum_required`
- `duplicate_found`
- `scw_required`

Required fields:

- candidate artifact path
- existing artifact path
- duplicate evidence
- revision rationale
- addendum rationale
- canonical owner
- decision
- Human Approval need
- blocked next step

Avoid duplicating general Artifact Schema semantics.

### 11. Repository Verification Evidence

Define evidence expectations for:

- repository root
- working repository
- working directory
- target project
- non-target project
- canonical source
- local branch state
- dirty workspace
- source existence
- public Raw freshness when applicable
- repository boundary
- permission / access limitation

Do not require GitHub Raw for purely local work unless applicable.

Public Raw availability boundary:

```text
local generation
-> commit
-> push
-> public Raw availability
```

Do not treat a local file as publicly available before Push.

### 12. Template Verification Evidence

Define:

- canonical template path
- template version
- source read
- freshness state
- mismatch state
- copied / downloaded artifact relationship
- local canonical preference
- raw reference relationship
- resolution action
- block conditions

Template mismatch must not silently become PASS.

### 13. Knowledge and Workflow Resolution Evidence

Required Workflow evidence:

- resolved workflow IDs / paths
- source of resolution
- unresolved workflow
- optional workflow
- ordering
- version / freshness
- conflict state

Required Knowledge evidence:

- required assets
- assets read
- missing assets
- conflicting assets
- superseded assets
- index source
- current mission
- related completion reports
- limitation status

A list of intended reads is not proof of completed checks.

### 14. Constraint Check Evidence

Define Startup constraint categories:

- scope
- out of scope
- forbidden edits
- repository boundary
- tool availability
- permission
- Human Approval
- commit policy
- push policy
- tag / release policy
- artifact output capability
- encoding
- Revision First
- unsafe or mixed-scope conditions

Each constraint result should identify:

- constraint ID
- expected state
- observed state
- result
- reason
- remediation
- blocking status

### 15. Startup Execution Log Relationship

Define whether the evidence record and log are:

- same artifact
- linked artifacts
- append-only event plus current snapshot
- future runtime choice

Architecture requirement:

- current decision must be readable
- state transition history must be traceable
- original failed / SCW states must not disappear
- retry and resume must be linked
- Completion Report must be able to cite the evidence
- Command Center must be able to display the current state
- Repository Quality may detect missing evidence

Do not implement the storage format.

### 16. Compatibility Review

Review compatibility with:

- `templates/Q_TEMPLATE.md`
- `templates/completion_report_template.md`
- `templates/startup_verification_checklist.md`
- `docs/architecture/runtime_startup_enforcement.md`
- `docs/workflow/runtime_startup_enforcement_workflow.md`
- `docs/workflow/artifact_creation_startup_enforcement_workflow.md`
- `docs/architecture/command_center_architecture.md`
- `docs/architecture/platform_execution_evidence_contract.md`
- relevant rules
- existing GDS-STARTUP-002 / 003 / 004 artifacts

Decide for each:

- no change
- reference update
- field alignment update
- future implementation dependency
- superseded wording
- addendum required
- new Q required

Do not automatically expand edits beyond evidence.

### 17. Example Evidence Records

Produce human-readable examples for:

1. PASS
2. PASS_WITH_LIMITATION
3. BLOCK
4. SCW_REQUIRED
5. Revision required
6. Template mismatch
7. Repository boundary conflict
8. Retry after Human Approval

Examples must:

- include parent required fields
- include Startup-specific fields
- show allowed and blocked next steps
- show approval state
- show reason codes
- avoid pretending JSON Schema already exists
- avoid authorizing commit / push

### 18. Future Implementation Boundary

Identify, but do not implement:

- Startup Evidence JSON Schema
- YAML representation
- evidence validator
- reason code registry
- execution log storage
- Command Center adapter
- Template Engine preflight adapter
- Repository Quality missing-evidence check
- test fixture set
- migration tool for older artifacts

Recommend whether each requires:

- separate Q
- grouped implementation Q
- Future Candidate
- no action

## Out of Scope

- JSON Schema files
- YAML schema files
- Python / TypeScript implementation
- runtime package
- database tables
- execution log storage implementation
- event sourcing implementation
- Command Center implementation
- Template Engine implementation
- Artifact Pipeline implementation
- Repository Quality runtime implementation
- automatic evidence generation
- automatic approval
- automatic artifact generation
- automatic Git operations
- migration of all historical Q files
- rewrite of all Completion Reports
- GameGhost edits
- field-project integration
- release / tag
- commit / push

## Existing Knowledge / Dependencies

### Related Rules

- `docs/rules/core_principles.md`
- `docs/rules/artifact_creation_startup_enforcement_rules.md`
- `docs/rules/human_approval_rules.md`
- canonical SCW rules discovered by repository audit
- `docs/rules/q_file_template_rules.md`
- `docs/rules/completion_checklist_rules.md`
- `docs/rules/beginner_future_self_test_rules.md`
- Repository Quality-related rules

### Related Architecture

- `docs/architecture/platform_execution_evidence_contract.md`
- `docs/architecture/runtime_startup_enforcement.md`
- `docs/architecture/intent_aware_startup_enforcement.md`
- `docs/architecture/command_center_architecture.md`
- `docs/architecture/artifact_schema_standard.md`
- `docs/architecture/responsibility_boundary.md`

### Related Workflow

- `docs/workflow/runtime_startup_enforcement_workflow.md`
- `docs/workflow/artifact_creation_startup_enforcement_workflow.md`
- `docs/workflow/q_file_creation_workflow.md`
- `docs/workflow/startup_completion_gate.md`
- `docs/workflow/completion_report_workflow.md`
- Repository Quality workflows

### Related Templates

- `templates/Q_TEMPLATE.md`
- `templates/completion_report_template.md`
- `templates/startup_verification_checklist.md`
- `templates/beginner_future_self_test_template.md`

### Related Conversation Insight

```text
STARTUP-005 should not create the parent evidence model.
The common Platform Execution Evidence Contract must be defined first.
STARTUP-005 should become a Startup Evidence Specialization.
```

### Related Pending Insight

- Not Applicable after GDS-ROADMAP-001 and GDS-PLATFORM-EXECUTION-EVIDENCE-001 completion.

### Related Future Candidate

- Runtime Startup Enforcement JSON Schema
- evidence compatibility validator
- reason code registry
- startup execution log implementation

### Related Q

- GDS-STARTUP-002
- GDS-STARTUP-003
- GDS-STARTUP-004
- GDS-ROADMAP-001
- GDS-PLATFORM-EXECUTION-EVIDENCE-001

### Related Completion Report

- GDS-STARTUP-002 Completion Report
- GDS-STARTUP-003 Completion Report
- GDS-STARTUP-004 Completion Report
- GDS-ROADMAP-001 Completion Report
- GDS-PLATFORM-EXECUTION-EVIDENCE-001 Completion Report

### Related Reports

- `reports/repository_quality_report.md`

## Do

- Verify the latest local main branch before editing.
- Start with the AI Repository Index.
- Read the parent Platform Execution Evidence Contract completely.
- Use Revision First.
- Preserve all parent required field meanings.
- Explicitly separate inherited and Startup-specific fields.
- Reconcile STARTUP-004 aliases and parent field names.
- Preserve Startup gate truth ownership.
- Preserve Human Approval.
- Preserve SCW.
- Preserve Repository Quality as gate evidence.
- Preserve Command Center as orchestrator, not domain truth owner.
- Include concrete evidence examples.
- Include compatibility review.
- Include Safe Commit Set.
- Keep Repository Quality Green.
- Record uncertainty and unresolved decisions honestly.
- Recommend a single next Q.

## Do Not

- Do not create a competing parent model.
- Do not redefine parent field meaning.
- Do not treat evidence as approval.
- Do not treat PASS as mutation authorization.
- Do not treat Green as approval.
- Do not let Command Center override Startup gate evidence.
- Do not hide BLOCK or SCW.
- Do not create executable schemas.
- Do not implement runtime code.
- Do not mass-migrate historical artifacts.
- Do not edit GameGhost.
- Do not commit.
- Do not push.
- Do not tag.
- Do not claim public Raw availability before Push.
- Do not add fields merely because they may be useful someday.
- Do not create duplicate reason code registries without repository audit.

## Encoding Regression Prevention

- Markdown changes expected: Yes
- Explicit UTF-8 read / write required: Yes
- Full-file rewrite expected: Review Required
- Full-file rewrite justification:
  - Prefer patch-based edits.
  - Controlled full-file rewrite is allowed only when preserving UTF-8 and when diff review shows no unrelated change.
- Intentional encoding evidence expected: Yes
- Exclusion config update required: No unless audit proves necessary
- Validator command:

```powershell
python scripts/validate_encoding_regression.py --all
python scripts/validate_encoding_regression.py --staged
```

## Target Files

Expected review targets:

- `docs/architecture/platform_execution_evidence_contract.md`
- `docs/architecture/runtime_startup_enforcement.md`
- expected specialization architecture path
- `docs/architecture/README.md`
- `docs/workflow/runtime_startup_enforcement_workflow.md`
- `docs/workflow/artifact_creation_startup_enforcement_workflow.md`
- `templates/Q_TEMPLATE.md`
- `templates/completion_report_template.md`
- `templates/startup_verification_checklist.md`
- `roadmap/ghost_development_system_roadmap.md`
- `README.md`
- `docs/README.md`
- `docs/ai_repository_index.md`
- `reports/repository_quality_report.md`
- request workspace

Codex must confirm real files and only edit those needed.

## Deliverables

Required:

1. `request.md`
2. `notes.md`
3. `completion_report.md`
4. canonical Startup Evidence Specialization architecture document
5. `attachments/parent_field_mapping.md`
6. `attachments/startup_evidence_field_catalog.md`
7. `attachments/result_and_reason_code_mapping.md`
8. `attachments/producer_consumer_and_approval_matrix.md`
9. `attachments/compatibility_and_extension_review.md`
10. `attachments/evidence_examples.md`
11. `attachments/beginner_future_self_test.md`
12. Changed Files
13. Generated Files
14. Summary
15. Startup Gate Evidence
16. Parent Contract Mapping
17. Startup Field Catalog
18. Lifecycle Mapping
19. Result Mapping
20. Reason Code Policy
21. Producer / Consumer Matrix
22. Human Approval Behavior
23. SCW Behavior
24. Revision First Evidence
25. Repository Verification Evidence
26. Template Verification Evidence
27. Knowledge / Workflow Resolution Evidence
28. Constraint Evidence
29. Startup Log Relationship
30. Compatibility Review
31. Future Implementation Boundary
32. Verification
33. Improvement Review
34. Recommended Improvements
35. Future Candidates
36. Remaining Issues
37. Recommended Next Q
38. Safe Commit Set
39. Suggested Commit Message
40. Review Decision

## Required Parent Field Mapping Table

Required columns:

- Parent Field
- Parent Requirement
- Startup Meaning
- Startup Source
- Startup Producer
- Startup Consumer
- Required / Conditional / Optional
- Existing STARTUP-004 Alias
- Canonical Name
- Validation Expectation
- Missing Behavior
- Compatibility Decision

## Required Startup Field Catalog Table

Required columns:

- Field
- Classification
- Meaning
- Source
- Data Shape Concept
- Required State
- Producer
- Consumer
- Parent Relationship
- Result Dependency
- Human Approval Relevance
- SCW Relevance
- Adopt / Revise / Defer / Reject
- Decision Reason

## Required Result Matrix

Required rows:

- PASS
- PASS_WITH_LIMITATION
- BLOCK
- SCW_REQUIRED

Required columns:

- Startup Result
- Common Meaning
- Artifact Draft Allowed
- Repository Mutation Allowed
- Required Parent Fields
- Required Startup Fields
- Human Approval State
- Allowed Next Step
- Blocked Next Step
- Reason Code Category
- Consumer Requirement

## Required Evidence Examples

Each example must contain at least:

- evidence identity
- evidence type
- producer
- consumer
- request and repository context
- scope / out of scope
- inputs
- checks performed
- Startup-specific checks
- result
- reason codes
- Human Approval state
- limitation or SCW details when applicable
- allowed next step
- blocked next step
- related artifacts
- state / history reference

## Validation

Run from repository root:

```powershell
cd C:\GitHub\Ghost-Development-System-Docs

git status --short --untracked-files=all

python scripts/validate_encoding_regression.py --all
python scripts/generate_ai_repository_index.py --write
python scripts/generate_ai_repository_index.py --validate
python scripts/repository_quality_audit.py

git diff --check
git status --short --untracked-files=all
```

After Human Approval to stage:

```powershell
python scripts/validate_encoding_regression.py --staged
git diff --cached --check
git diff --cached --stat
```

Additional validation:

- Confirm parent required fields remain unchanged in meaning.
- Confirm the specialization declares the parent Contract.
- Confirm no competing evidence parent architecture is created.
- Confirm STARTUP-004 evidence aliases are reconciled.
- Confirm all four result states have examples.
- Confirm Human Approval remains separate from evidence completeness.
- Confirm PASS does not authorize repository mutation.
- Confirm BLOCK and SCW are visible stop states.
- Confirm Command Center cannot override Startup evidence.
- Confirm Template Engine cannot treat evidence as approval.
- Confirm no runtime code or schema implementation was added.
- Confirm no GameGhost files changed.
- Confirm AI Repository Index contains new canonical artifacts.
- Confirm Repository Quality is Green or apply SCW.
- Confirm no mojibake markers in changed files except intentional examples.
- Confirm no trailing whitespace.
- Confirm no unrelated dirty files enter Safe Commit Set.
- Confirm public Raw availability is not claimed before Commit and Push.

## AI Repository Index Update Gate

- AI Repository Index Update Gate: Yes
- Reason:
  - durable architecture, request artifacts, attachments, and possibly reference documents are added or changed
- Expected indexed files:
  - canonical Startup Evidence Specialization
  - request workspace
  - attachments
  - revised architecture / workflow / template references
  - `docs/ai_repository_index.md`
- Regeneration command:

```powershell
python scripts/generate_ai_repository_index.py --write
```

- Validation command:

```powershell
python scripts/generate_ai_repository_index.py --validate
```

- Representative Raw URL verification:
  - verify only after Commit and Push if public retrieval is reported

Failure action:

```text
Apply SCW when generation fails, validation fails, expected assets are absent,
canonical paths conflict, duplicate parent models are found, or unrelated dirty
files may enter the Safe Commit Set.
```

## Startup Checklist

- Canonical Template Synchronization completed: Yes
- Current Q File confirmed as authoritative: No — authoritative after repository placement as `request.md`
- Q File read with explicit UTF-8 when using Windows PowerShell 5.1: Required
- Q File mojibake check result: To be verified
- Repository Root Validation completed: Required
- Working Repository confirmed: Ghost-Development-System-Docs
- Scope / Out of Scope confirmed: Yes
- Commit / Push Policy confirmed: Yes
- Dirty workspace checked: Required
- Applicable Rules confirmed: Yes
- Applicable Workflow confirmed: Yes
- AI Repository Index verified: Yes
- Current Mission verified: Yes
- Template revision verified: Yes
- Canonical Repository confirmed: Yes
- Raw reference freshness confirmed when applicable: Yes at Q creation; recheck latest local main
- Project Profile reviewed when applicable: Not Applicable
- AI Repository Index read when public knowledge is needed: Yes
- Conversation Insight Detection performed when applicable: Yes
- Pending Insight origin:
  - GDS-ROADMAP-001 and GDS-PLATFORM-EXECUTION-EVIDENCE-001
- Pending Insight reviewed before Q creation: Yes
- Pending Insight decision:
  - STARTUP-005 proceeds as a specialization, not a parent schema
- Pending Insight Codex execution restriction cleared by Human Approval: Yes, for this Q

## Audit Before Repair

- Audit Before Repair applies: Yes
- Source audit artifact:
  - `attachments/compatibility_and_extension_review.md`
- Audit command or method:
  - inventory existing Startup evidence fields and parent Contract fields
  - compare architecture, workflow, template, and completion artifacts
  - search for duplicate evidence terminology and reason code definitions
- Classification used:
  - parent field
  - specialization field
  - alias
  - duplicate
  - incompatible meaning
  - future implementation field
  - obsolete wording
- Repair target scope:
  - documentation alignment only
- Explicit exclusions:
  - executable schema
  - runtime implementation
  - historical mass migration
- Evidence to review:
  - STARTUP-004 architecture
  - parent Contract
  - current templates
  - completion reports
- Human Review required before repair: Yes
- Verification method:
  - field mapping
  - diff review
  - example review
  - validation suite
- Safe commit set:
  - report explicitly at completion
- Restore / rollback guidance:
  - revert only Safe Commit Set

## Research Mission

- Research Mission applies: Yes
- Mission Name: Startup Evidence Specialization Design
- Goal:
  - define a compatible, minimal, reviewable Startup specialization
- Research Questions:
  1. Which STARTUP-004 fields are inherited from the parent?
  2. Which fields are truly Startup-specific?
  3. Which aliases should be removed or preserved for compatibility?
  4. How should runtime states map to the common evidence lifecycle?
  5. What evidence must each result state contain?
  6. How should retries and resumed SCW states remain traceable?
  7. Which consumers need which Startup evidence?
  8. What is the next implementation boundary?
- Expected Hypothesis:

```text
The Startup specialization can remain small by inheriting repository context,
scope, result, approval, SCW, and next-step fields from the parent, while adding
artifact intent, workflow / knowledge resolution, repository / template checks,
Revision First, constraint results, gate state, and startup history.
```

- Scope:
  - architecture and documentation
- Out of Scope:
  - serialization and runtime implementation
- Required Evidence:
  - canonical parent Contract
  - STARTUP-004 architecture
  - templates and workflows
  - result examples
- Validation Method:
  - mapping completeness
  - contradiction audit
  - example review
  - Repository Quality
- Deliverables:
  - specialization architecture and attachments
- Success Criteria:
  - no parent conflict
  - all required mappings complete
  - all result states reviewable
- Negative Result Policy:
  - return SCW_REQUIRED if parent meaning conflicts cannot be resolved safely
- Knowledge Promotion Candidate:
  - Startup Evidence Specialization
  - Startup Reason Code Catalog
- Completion Report required: Yes

## Debug Artifact Review

- Debug Artifact Review applies: No
- Debug Mode required during development: No
- Normal execution debug artifact policy: Not Applicable
- Expected debug artifact save location: Not Applicable
- Expected Review Entry Point:
  - parent mapping and evidence examples
- Intermediate artifacts to review:
  - field catalog
  - compatibility review
- Verification target:
  - semantic compatibility
- Expected normal state:
  - no parent conflict
- Review viewpoints:
  - beginner readability
  - future runtime implementability
  - Human Approval safety
- AI review target artifacts:
  - all attachments
- Debug artifact Git policy: Not Applicable

## Migration First / Internal Architecture

- Migration First applies: Yes
- New Standard:

```text
Platform Execution Evidence Contract
        ↓
Runtime Startup Enforcement Evidence Specialization
        ↓
future serialization / validator / runtime adapter
```

- Migration Plan:
  1. Audit STARTUP-004 fields.
  2. Map parent fields.
  3. Classify Startup-specific fields.
  4. Reconcile aliases.
  5. Define lifecycle and result mapping.
  6. Define producer / consumer behavior.
  7. Add examples.
  8. Update references.
  9. Validate.
- Reference Update:
  - update only necessary canonical references
- Legacy Removal:
  - do not remove historical Q artifacts
  - revise conflicting current canonical wording only with evidence
- Public Compatibility Impact:
  - documentation contract only
- Remaining Legacy:
  - runtime serialization absent
  - older human-readable artifacts remain valid
- Restore / Rollback Guidance:
  - revert Safe Commit Set

## Related Completion Report

- Expected completion report artifact:

```text
docs/requests/gds/draft/GDS-STARTUP-005_runtime_startup_enforcement_evidence_specialization/completion_report.md
```

- Completion report status: Required

## Revision / Addendum Policy

- Small scope extension: `addendum_vX.Y.md`
- Materially different objective: new Q
- Correction before execution: revise `request.md`
- Completed Q correction: add review note or addendum

The following require a new Q:

- executable JSON Schema
- evidence validator
- runtime implementation
- reason code registry implementation
- execution log storage
- Command Center adapter
- Repository Quality integration code
- historical artifact migration
- GameGhost adoption

## Completion Criteria

- Q ID is specified.
- Repository Context is complete.
- Commit / Push Policy is explicit.
- Parent Contract is verified.
- STARTUP-004 evidence model is audited.
- Every parent required field has a Startup mapping.
- Startup-specific fields are classified.
- Aliases are reconciled.
- Canonical evidence type is selected.
- Common lifecycle is mapped to Startup states.
- PASS / PASS_WITH_LIMITATION / BLOCK / SCW_REQUIRED are fully defined.
- Reason code policy is defined.
- Producer / consumer responsibilities are defined.
- Human Approval behavior is explicit.
- SCW behavior is explicit.
- Revision First evidence is defined.
- Repository and Template verification evidence are defined.
- Workflow and Knowledge resolution evidence are defined.
- Constraint evidence is defined.
- Execution log relationship is defined.
- Compatibility review is complete.
- All required examples are produced.
- Future implementation boundary is explicit.
- No executable schema is created.
- No runtime code is created.
- No GameGhost file is edited.
- AI Repository Index is regenerated and validated.
- Repository Quality remains Green.
- Encoding validator passes.
- `git diff --check` passes.
- Beginner & Future Self Test passes.
- Safe Commit Set is reported.
- Recommended Next Q is exactly one Q.
- Review Decision is returned.
- No commit / push / tag is executed.

## Completion Report Requirements

Completion Report must include:

- Source Q File
- Q ID
- Output Artifacts
- Generated Files
- Changed Files
- Summary
- Startup Enforcement Gate Evidence
- Parent Contract verification
- Parent Field Mapping summary
- Startup Field Catalog summary
- Evidence Type decision
- Lifecycle mapping
- Result mapping
- Reason Code policy
- Producer / Consumer behavior
- Human Approval behavior
- SCW behavior
- Revision First evidence
- Repository Verification evidence
- Template Verification evidence
- Workflow / Knowledge evidence
- Constraint evidence
- Startup Log relationship
- Compatibility Review
- Evidence Example review
- Future Implementation Boundary
- Verification
- AI Repository Index result and entry count
- Repository Quality result
- Encoding validation result
- `git diff --check` result
- Improvement Review
- Beginner & Future Self Test result
- Recommended Improvements
- Future Candidates
- Remaining Issues
- Recommended Next Q
- Safe Commit Set
- Commit Status
- Push Status
- Tag Status
- GameGhost Edit Status
- Suggested Commit Message
- Review Decision

## Review Decision

Return one:

```text
Commit OK
Revision Recommended
Minor Recommendation
SCW_REQUIRED
```

This decision does not authorize commit, push, or tag.

## Suggested Commit Message

```text
docs(startup): define startup execution evidence specialization
```

## Related Documents

- `templates/Q_TEMPLATE.md`
- `templates/completion_report_template.md`
- `templates/startup_verification_checklist.md`
- `docs/ai_repository_index.md`
- `docs/architecture/platform_execution_evidence_contract.md`
- `docs/architecture/runtime_startup_enforcement.md`
- `docs/architecture/intent_aware_startup_enforcement.md`
- `docs/architecture/command_center_architecture.md`
- `docs/architecture/artifact_schema_standard.md`
- `docs/workflow/runtime_startup_enforcement_workflow.md`
- `docs/workflow/artifact_creation_startup_enforcement_workflow.md`
- `docs/workflow/q_file_creation_workflow.md`
- `docs/workflow/startup_completion_gate.md`
- `docs/rules/artifact_creation_startup_enforcement_rules.md`
- `docs/rules/human_approval_rules.md`
- `roadmap/ghost_development_system_roadmap.md`
- `reports/repository_quality_report.md`
- GDS-STARTUP-002 Completion Report
- GDS-STARTUP-003 Completion Report
- GDS-STARTUP-004 Completion Report
- GDS-ROADMAP-001 Completion Report
- GDS-PLATFORM-EXECUTION-EVIDENCE-001 Completion Report

## Final Instruction to Codex

Begin with repository verification and parent Contract mapping.

Do not begin by inventing new fields.

Prefer inheritance over duplication.

The final result must make the following statement demonstrably true:

```text
Startup Enforcement Evidence is a compatible specialization of the Platform
Execution Evidence Contract, not a separate evidence system.
```
