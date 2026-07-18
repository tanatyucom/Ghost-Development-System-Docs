# Workflow

## Purpose

This folder explains the standard development workflow for Ghost Development
System Docs.

Workflow documents describe how ideas become reviewed work, how completed work
produces reusable knowledge, and how Improvement Review acts as a completion
gate.

## Contains

- `README.md`: workflow folder guide.
- `startup_checklist_workflow.md`: startup confirmation flow for repository,
  Q artifacts, applicable rules, methodologies, scope, dirty workspace, and
  commit policy before implementation or review begins.
- `startup_completion_evidence.md`: evidence standard showing which canonical
  sources were reviewed before Q creation, implementation, review, or
  documentation update. It includes Repository Context Evidence, freshness /
  invalidation checks, and task-specific context refresh.
- `startup_completion_gate.md`: verification gate after Startup Checklist and
  before Q creation, implementation, review, or documentation update.
- `ai_startup_procedure.md`: AI reading order and startup procedure before
  Startup Checklist, Q execution, implementation, review, or documentation
  update.
- `intent_driven_workflow.md`: natural language intent routing workflow from
  user utterance to canonical source review, repository / conversation state
  review, workflow selection, Recommendation, Pending Action, Human Approval,
  Action, or SCW.
- `artifact_creation_startup_enforcement_workflow.md`: pre-generation workflow
  for managed artifacts that requires artifact intent classification, workflow
  resolution, knowledge resolution, canonical template verification, Revision
  First, Constraint Check, and Gate Decision before drafting.
- `runtime_startup_enforcement_workflow.md`: future runtime workflow for
  executing Startup Enforcement as a state machine before Template Engine,
  Artifact Pipeline, or Command Center draft generation.
- `knowledge_preservation_gate.md`: workflow for deciding whether a Q, review,
  completion, or design conversation should produce an Issa draft, ADR
  candidate, Improvement Record candidate, Architecture Principle candidate, or
  child Q without automatically promoting it.
- `knowledge_carry_forward_workflow.md`: low-friction workflow for attaching
  approved knowledge promotion candidates to the most relevant current or
  future Q instead of generating many standalone Q files.
- `generation_handoff_workflow.md`: workflow for preserving North Star,
  design intent, Vision Scenario, Experience continuity, current mission,
  pending decisions, and approval boundaries when work moves between AI
  generations, tools, tasks, or human review contexts.
- `approval_request_intent_queue_workflow.md`: workflow from Review Result to
  Candidate Disclosure, Approval Request, Human Approval, Intent Queue,
  Execution Authority, Delegation, Execution Evidence, and Completion.
- `runtime_intent_queue_resolution_workflow.md`: workflow for resolving
  approval phrases into Intent Queue and Execution Queue, showing deliverables,
  canonical artifact, Codex handoff, delegation, and evidence state.
- `governed_execution_adapter_workflow.md`: workflow connecting Runtime Queue
  items to governed execution or delegation through request contracts, adapter
  routing, result / evidence envelopes, reconciliation, and completion review.
- `authority_validation_gate.md`: workflow for checking Execution Authority
  Registry, Approval Unit, actor authority, scope, Human Approval requirement,
  approval state, and evidence responsibility before Approval Request,
  execution, delegation, or SCW.
  It also checks Capability / Authority bindings when execution or mutation is
  involved.
- `improvement_record_promotion_workflow.md`: workflow for turning observed
  operation gaps into Improvement Records, Promotion Candidates, and future
  standards without automatic approval or repository mutation.
- `capability_verification_first.md`: workflow for verifying current AI,
  repository, tool, permission, connected service, and chat capabilities before
  answering whether a task can be done. Memory capability should be reported as
  separate Read / Write / Unknown status rather than an ambiguous availability
  flag.
- `ai_daily_operation_cycle.md`: daily operating cycle that connects AI
  Startup Procedure, Q review, implementation, verification, human review,
  Completion Checklist, commit / push, Knowledge Update, Repository Update,
  Next Q Planning, and the next startup.
- `gds_health_update_workflow.md`: update workflow for GDS Health Dashboard
  status, notes, improvement candidates, and completion report reflection.
  Validate related structure and links with `scripts/validate_gds_health.py`.
- `repository_quality_audit_workflow.md`: repository-wide quality audit flow
  that combines UTF-8, mojibake, AI index, GDS Health, link, README, history,
  project profile, and Markdown validation checks. Its result can be described
  as Repository Quality Gate Evidence through
  `docs/architecture/repository_quality_gate_evidence_specialization.md`.
- `encoding_regression_prevention_workflow.md`: commit-gate workflow for
  UTF-8, mojibake regression, intentional evidence exclusions, and staged
  Markdown validation.
- `japanese_documentation_localization_workflow.md`: GDS Docs の説明文を
  日本語優先で維持しつつ、command、path、URL、identifier、status value を
  必要に応じて英語維持するための workflow。
- `repository_root_validation_workflow.md`: startup workflow for checking the
  actual Git repository root against the Q Working Repository.
- `collaborative_decision_workflow.md`: workflow for AI and user proposals,
  discussion, evidence review, knowledge classification review, decision, and
  documentation.
- `completion_checklist_workflow.md`: completion confirmation flow for
  verification, review, completion report, Improvement Review, commit, tag,
  release, next Q, and workspace clean confirmation.
- `pre_response_verification_gate.md`: final response quality gate for checking
  repository scope, requested output format, approval boundaries, commit /
  push reality, Repository Context Evidence freshness, and constraint validity
  before the final AI response.
- `repository_drift_prevention.md`: Future Candidate workflow for preventing
  AI Repository Drift during artifact generation by re-anchoring to canonical
  repository sources between reasoning and output, and for preserving Startup
  execution context through completion. It also records AI Context
  Synchronization Countermeasures as a Future Candidate.
- `completion_report_workflow.md`: workflow for creating Completion Report v2
  with Identity, Changed Files, Verification, Safe Commit Set, Commit / Push
  Status, Project Edit Status, Improvement Review, Lessons Learned,
  Reusable Assets Created, Remaining Issues, Recommended Next Q, and
  Suggested Commit Message.
- `beginner_future_self_test_workflow.md`: lightweight review workflow for
  checking whether a managed artifact is understandable to beginners, new AI
  sessions, returning project owners, and future selves without hidden chat
  context.
- `research_mission_workflow.md`: scoped investigation workflow from
  Observation to Research Mission, Evidence Collection, Validation,
  Completion Report, Knowledge Promotion Review, Human Approval, and
  Repository update.
- `ghost_research_workflow.md`: external-knowledge intake workflow from
  External Source to Ghost Research, idea-level Adoption Decision, Future
  Candidate, GG Validation, Evidence, Platform Candidate, ADR, and GDS Standard
  without automatic adoption or implementation.
- `output_policy.md`: chat versus file artifact output decision policy.
- `q_file_creation_workflow.md`: workflow from idea to Q ID, repository
  context, template completion, Task Artifact Workspace save, and approval
  before AI execution.
- `q_revision_addendum_workflow.md`: workflow for deciding whether a
  requirement change is an addendum, revised request, or new Q.
- `audit_before_repair_workflow.md`: audit, classification, evidence, human
  review, scoped repair Q, verification, and commit flow before repair work.
- `commit_safety_checklist.md`: dirty workspace and commit safety workflow.
- `debug_artifact_review_workflow.md`: Debug Mode, intermediate artifact
  review, expected state check, AI review handoff, and Fix Q draft workflow.
- `review_center_workflow.md`: workflow from source artifacts through review
  plugin / adapter, Review Center session, human decision, save / resume,
  result export, domain gate adapter, gate readiness, and completion report.
- `architecture_promotion_lifecycle.md`: workflow from Problem, Q,
  Implementation, Completion Report, Operational Validation, Repository
  Operation, Maturity & Evidence Confirmation, Architecture Decision, ADR, and
  optional GDS Rule / Template / Workflow / SDK promotion.
- Documentation Synchronization:
  `documentation_synchronization_workflow.md` is the gate workflow for keeping
  README / folder index, AI Repository Index, completion checklist, completion
  report, and repository quality audit synchronized after documentation
  changes.
- `documentation_synchronization_workflow.md`: workflow for detecting
  documentation changes, updating README / folder index entry points,
  regenerating AI Repository Index, confirming completion checklist / report
  synchronization, and running Repository Quality Audit before completion.
- `debug_escalation_ladder.md`: standard escalation order from phenomenon
  check to algorithm change.
- `first_broken_step_methodology.md`: reusable debugging methodology for
  tracing a pipeline to the first broken step before root cause and fix.
- `migration_first_workflow.md`: internal architecture change workflow for
  new standard, migration plan, reference update, verification, legacy removal,
  completion report, and commit.
- `innovation_pipeline_workflow.md`: workflow for growing ideas from Idea,
  Experiment, Prototype, Validation, Platform Promotion, Standardization, and
  Propagation.
- `conversation_insight_capture_workflow.md`: workflow for preserving
  conversation-origin design philosophy, operation policy, migration strategy,
  Command Center concepts, and long-term vision as Human Approval-gated
  pre-promotion knowledge.
- `pending_conversation_insight_review_workflow.md`: workflow for holding
  conversation-origin ideas as temporary Pending Insights, reviewing them at
  Startup / Daily Knowledge Review, blocking Codex execution while pending,
  and resolving or keeping them after Human Review.
- `memory_candidate_workflow.md`: workflow for capturing conversation-born
  knowledge as temporary Memory Candidates, triaging it to Memory / Q /
  Repository Knowledge, and closing or deferring it without treating it as
  canonical authority.
- `platform_registry_update_artifact_storage.md`: storage location, naming
  rule, and management workflow for Platform Registry Update Artifacts.
- `auto_registry_update_from_promotion_report.md`: workflow design for
  generating Platform Registry Update Artifact drafts from Platform Promotion
  Decision Reports.
- `concept_promotion_workflow.md`: how concepts move from Candidate to
  Under Review, Experiment, Validated, Promoted, or Archived.
- `pip_case_knowledge_base_workflow.md`: how reusable lessons become tagged
  PIP cases, rule stories, best practices, evolutions, and Knowledge Promotion.
- `../knowledge/README.md`: Knowledge Inventory entry point for classifying
  reusable knowledge before formal promotion.
- `roadmap2_knowledge_salvage_loop.md`: final Roadmap2 knowledge migration
  loop from review request to no remaining missing knowledge.
- `template_lifecycle.md`: how useful knowledge becomes a template, rule, or
  Knowledge Base document.

Innovation Pipeline records should use
`templates/innovation_pipeline_template.md`.

## Does NOT Contain

- Runtime implementation.
- Queue execution state.
- Release artifacts.
- Git migration operations.
- Project-specific feature workflow.

## Standard Development Flow

```text
Idea
  -> Intent-Driven Workflow, when the user gives a natural language goal such
     as "続きやろう", "何をやったらいい？", "終わった", "お願いします",
     "commitしていい？", "pushしていい？", or "次は？"
  -> Artifact Creation Startup Enforcement, when a managed artifact will be
     created or revised
  -> Runtime Startup Enforcement, when a future runtime caller executes the
     gate before Template Engine or Artifact Pipeline
  -> AI Daily Operation Cycle
  -> Capability Verification, when capability is asked or uncertain
  -> AI Startup Procedure
  -> Startup Checklist
  -> Startup Completion Evidence
  -> Startup Completion Gate
  -> Repository Root Validation
  -> Information Package Check, when provided
  -> Current Q Check
  -> AI Repository Index Check, when public repository knowledge is needed
  -> Knowledge Check
  -> Knowledge Poka-Yoke Check
  -> Collaborative Decision, when classification or design is uncertain
  -> Output Decision
  -> Review
  -> Q ID Decision
  -> Q Artifact Workspace
  -> Workspace Save Verification
  -> Conversation Insight Detection, when conversation-origin philosophy,
     operation policy, maintenance policy, migration strategy, Command Center
     concept, or long-term vision may need preservation
  -> Research Task Detection
  -> Research Mission, when investigation scope and evidence must be explicit
  -> Audit Before Repair, when repairing or cleaning up
  -> Approval
  -> Codex / AI Implementation
  -> Debug Escalation Ladder, when cause is uncertain
  -> Debug Artifact Review, when applicable
  -> Encoding Regression Validation, before commit approval
  -> Completion Report Artifact
  -> Completion Report v2 Section Check
  -> Beginner & Future Self Test, when artifact readability across time or
     handoff matters
  -> Knowledge Inventory, when reusable knowledge is found but not yet promoted
  -> PIP Update, when project state or decisions changed
  -> PIP Case Candidate, when reusable knowledge was found
  -> Concept Promotion, when knowledge is still an early concept
  -> Conversation Insight, when conversation-origin philosophy or long-term
     operation knowledge should be preserved
  -> Innovation Pipeline, when a reusable experiment may become Platform Standard
  -> Architecture Promotion Lifecycle, when a field result may become an ADR or
     GDS standard
  -> Knowledge Preservation Gate, when problem definition, reasoning,
     architecture decision, or future reconstruction value may be lost
  -> Knowledge Carry-Forward, when approved promotion candidates should be
     preserved in the current or next Q
  -> Platform Registry Update Artifact, when Platform Standard Registry changes
  -> Roadmap2 Knowledge Salvage, when Roadmap2-only knowledge remains
  -> Human Review
  -> Completion Checklist
  -> Repository Re-anchor, when long artifact generation or drift risk exists
  -> Pre-Response Verification Gate
  -> Commit
  -> Knowledge Promotion
  -> Archive
```

## Output Policy

Before implementation or review, decide whether the requested output should be
chat or a file artifact.

Use chat for short consultation, clarification, and temporary status.

Use file artifacts for long Q files, design documents, specifications, review
requests, Codex / Gemini / Claude requests, roadmap update proposals, human
approval packets, and Git-managed documentation.

Standard artifact formats are Markdown `.md` and Word `.docx`. Markdown is the
default for Git and AI handoff. `.docx` is required when human review,
redline, approval review, or offline reading is expected.

When an artifact is the authoritative output, chat should contain only a short
summary, artifact paths or links, verification notes, and remaining issues.

## AI Daily Operation Cycle

Use AI Daily Operation Cycle as the standard outer loop for long-running human
and AI work.

```text
AI Startup Procedure
  -> Current Q Review
  -> Implementation
  -> Verification
  -> Human Review
  -> Completion Checklist
  -> Pre-Response Verification Gate
  -> Commit / Push
  -> Knowledge Update
  -> Repository Update
  -> Next Q Planning
  -> Next Startup
```

Details follow `ai_daily_operation_cycle.md`.

Use `templates/daily_operation_checklist_template.md` when the cycle itself
should be recorded as a reusable checklist artifact.

Use `docs/health/gds_health_dashboard.md` when the cycle reveals repository,
knowledge, workflow, template, example, automation, CI, or project profile
health issues that should be visible across tasks.

Details follow `gds_health_update_workflow.md`.

Run `python scripts/validate_gds_health.py` after changing Health Dashboard
structure, Health links, README entry points, or AI Repository Index entries.

Run `python scripts/repository_quality_audit.py` when a task needs a single
repository-wide quality report.

## Startup Checklist Workflow

Before Startup Checklist is completed, AI should follow the AI Startup
Procedure reading order:

```text
AI Repository Index
  -> Repository Root Validation
  -> GDS Core Rules / Workflow
  -> Target Project Profile
  -> Current Q File
  -> Startup Checklist
```

Details follow `ai_startup_procedure.md`.

Before implementation, review, Q execution, or documentation update begins, use
Startup Checklist to confirm repository boundaries, Q artifact status,
applicable rules, applicable methodologies, scope, dirty workspace, and commit
policy.

```text
Start
  -> Repository Confirmation
  -> Q / Artifact Confirmation
  -> Applicable Rules Confirmation
  -> Applicable Methodologies Confirmation
  -> Scope / Out of Scope Confirmation
  -> Dirty Workspace / Commit Policy Confirmation
  -> Checklist Complete
  -> Implementation / Review Start
```

Details follow `startup_checklist_workflow.md`.

## Startup Completion Gate

After Startup Checklist, use Startup Completion Evidence to record the minimum
proof that canonical sources were checked.

```text
Startup Checklist
  -> Startup Completion Evidence
  -> Startup Completion Gate
  -> Q Creation / Implementation / Review
```

Details follow `startup_completion_evidence.md` and `startup_completion_gate.md`.

## Pre-Response Verification Gate

Before delivering a final AI response, confirm that the response matches the
actual changed files, verification results, repository scope, output format,
Human Approval boundary, and commit / push state.

```text
Completion Checklist
  -> Pre-Response Verification Gate
  -> Final Response
```

Details follow `pre_response_verification_gate.md`.

## Repository Root Validation Workflow

Before implementation, review, commit, tag, or release work begins, confirm the
actual Git root and compare it with the expected Working Repository.

```text
Start
  -> Current Working Directory Check
  -> Git Root Check
  -> Working Repository Match Check
  -> Production / Backup / Reference Check
  -> git status Check
  -> Safe To Start Decision
```

Details follow `repository_root_validation_workflow.md`.

## AI Repository Knowledge Access Workflow

When ChatGPT, Codex, or another AI reads the public GDS Docs GitHub repository
as a Knowledge Source, use the Raw URL Index first.

```text
Need public GDS knowledge
  -> Read docs/ai_repository_index.md
  -> Select required Raw URL
  -> Read target file
  -> Follow related files only when needed
  -> Report missing access honestly
```

When a task changes public entry points, the completion flow should check
whether `docs/ai_repository_index.md` needs an update.

Details follow `docs/rules/external_source_access_rules.md`.

## Collaborative Decision Workflow

Use this workflow when AI and user proposals need discussion before deciding
whether knowledge belongs in a Rule, Workflow, Methodology, CASE, Concept,
Template, Example, Glossary, Architecture, PIP Decision History, Future
Candidate, or no durable document.

```text
Idea
  -> AI Proposal
  -> User Proposal
  -> Discussion
  -> Evidence Review
  -> Knowledge Classification Review
  -> Decision
  -> Documentation
```

Details follow `collaborative_decision_workflow.md`.

## Completion Checklist Workflow

Before work is treated as complete, use Completion Checklist to confirm
verification, review, completion report, Improvement Review, commit / tag /
release decisions, Recommended Next Q, and workspace clean confirmation.

```text
Implementation
  -> Verification
  -> Review
  -> Completion Report
  -> Completion Checklist
  -> Commit / Tag / Release Decision
  -> Recommended Next Q
  -> End
```

Details follow `completion_checklist_workflow.md`.

## Research Mission Workflow

Use Research Mission Workflow when the task is not yet a fix or specification,
but an evidence-based investigation.

```text
Observation
  -> Research Mission
  -> Evidence Collection
  -> Validation
  -> Completion Report
  -> Knowledge Promotion Review
  -> Human Approval
  -> Rule / Workflow / Template / CASE / Inventory
  -> Repository
```

The mission artifact should define Goal, Research Questions, Expected
Hypothesis, Scope, Out of Scope, Required Evidence, Validation Method,
Deliverables, Success Criteria, Negative Result Policy, and Completion Report
requirements.

Details follow `research_mission_workflow.md`.

## Audit Before Repair Workflow

Before repair, cleanup, OCR result correction, DB correction, text encoding
fixes, metadata correction, duplicate resolution, or other destructive-looking
maintenance, use this flow:

```text
Idea / Bug
  -> Audit
  -> Classification
  -> Evidence
  -> Human Review
  -> Repair Q
  -> Verification
  -> Commit
```

Audit results should classify findings as `fix_candidate`,
`needs_human_review`, `generated_artifact`, `raw_data`, or `false_positive`.
Repair Q files should name the source audit artifact, target scope, exclusions,
verification method, safe commit set, and restore guidance.

Details follow `audit_before_repair_workflow.md`.

## Commit Safety Workflow

Before committing, use the standard dirty workspace review:

```text
git status
  -> Classify changes
  -> Review unrelated files
  -> Restore accidental files
  -> git diff --check
  -> Commit
  -> Push
```

Every completion report should state whether a dirty workspace was detected,
whether unrelated files were present, any suggested restore commands, and the
safe commit set.

## Debug Artifact Review Workflow

AI output、OCR output、recommendation、auto-detection、candidate extraction、
fuzzy matching、image overlay、その他の中間処理を扱う場合は Debug Artifact
Review を使います。

Standard flow:

```text
Issue / Idea
  -> Debug Mode Decision
  -> Intermediate Artifact Generation
  -> Visual / Intermediate Review
  -> Expected State Check
  -> Design Review, when needed
  -> Fix Q Draft or Implementation
  -> Verification
  -> Completion Report
```

通常実行では、Debug Mode が明示されていない限り Debug Artifact を生成しません。

Debug Mode が適用される場合、Completion Report には Debug Artifact の保存場所、
verification target、expected normal state、review viewpoints、必要に応じた
AI review target artifacts、Git policy を記載します。

## Debug Escalation Ladder Workflow

When cause is uncertain, use the standard ladder before changing algorithms:

```text
Phenomenon Check
  -> Metrics Check
  -> Human Review
  -> Debug Artifact Generation
  -> Pipeline Trace
  -> First Broken Step Identification
  -> Root Cause Confirmation
  -> Algorithm Change
```

Details follow `debug_escalation_ladder.md`.

## First Broken Step Methodology

Use this methodology when a pipeline, import, API, parser, database, UI, or AI
workflow fails and the root cause is not yet proven.

```text
Confirm the Symptom
  -> Reproduce the Issue
  -> Collect Evidence
  -> Trace the Entire Pipeline
  -> Identify the First Broken Step
  -> Confirm the Root Cause
  -> Apply the Fix
  -> Validate the Result
  -> Perform Regression Check
  -> Document the Lessons Learned
```

Details follow `first_broken_step_methodology.md`.

## Q Artifact Workflow

Q files are generated and saved before Codex or another AI executes the work.

Standard flow:

```text
Idea
  -> Q Artifact Workspace
  -> Save request.md in docs/requests/
  -> Workspace Save Verification
  -> Approval
  -> Codex / AI Implementation
  -> Completion Report Artifact
  -> Human Review
  -> Commit
  -> Knowledge Promotion
  -> Archive
```

Q artifacts and completion report artifacts are saved under:

```text
docs/requests/
```

Use this workspace pattern when the task has related artifacts:

```text
docs/requests/<project>/<status>/<Q_ID>_<short_topic>/
  request.md
  completion_report.md
  notes.md
  attachments/
```

Simple file form is allowed for small tasks:

```text
docs/requests/<project>/<status>/Q_<Q_ID>_<short_topic>_JP.md
```

Status folders include `draft`, `approved`, `in_progress`, `review`, `completed`, `archived`, and `rejected`. Existing repositories may keep the smaller current set until a migration Q expands it.

Workspace save verification means confirming that the authoritative Q exists
as `request.md` or an approved simple-form `.md` file under
`docs/requests/<project>/<status>/`. A Q that exists only in chat, a
download folder, clipboard, or temporary sandbox path should not be treated as
the official task input. Save the Q first, then begin implementation.

## Migration First Workflow

When a task changes internal architecture, internal folder structure, script
layout, adapter internal interface, prototype scripts, shared utility location,
artifact workspace layout, queue / request internal structure, or future
GhostCore / GDS internal modules, use Migration First.

Standard flow:

```text
Internal Architecture Change
  -> New Standard
  -> Migration Plan
  -> Reference Update
  -> Verification
  -> Legacy Removal
  -> Completion Report
  -> Commit
```

Public compatibility should be reviewed only for public release, public API /
CLI, documented external workflow, exported artifact schema, DB schema, and
user-facing data format.

If temporary legacy fallback is kept, the Q and completion report should state
the reason, removal plan, verification result, Remaining Legacy, and Restore /
Rollback Guidance.

## Knowledge Before Automation Flow

When the idea is an automation failure, do not jump directly from problem to
more automation.

Use this smaller decision loop first:

```text
Idea
  -> Knowledge
  -> Automation
```

Knowledge means reviewed information that the system can reuse: human approval,
alias decisions, metadata, rules, examples, review reports, and Knowledge Base
updates.

Automation should consume explicit knowledge. It should not hide repeated human
judgment inside increasingly complex code or AI prompts.

## Knowledge Poka-Yoke Flow

When a repeated omission, memory-dependent step, repository confusion,
copy-paste risk, missing artifact, scope drift, or review handoff gap appears,
convert it into a checkable control instead of relying on memory.

```text
Forgotten / Drift-Prone Step
  -> Make It Visible
  -> Checklist / Template / Validation / Artifact
  -> Human Review
  -> Automation, only when safe
```

This flow connects Startup Checklist, Completion Checklist, Repository Root
Validation, Repository Information, Scope Guard, Q Artifact, Completion Report,
AI Proactive Proposal, and Collaborative Decision. Its purpose is not to blame
forgetting, but to make forgetting safe.

## Evidence Feedback Loop

When a completed task produces measurable results, feed those results back into
the knowledge base.

```text
Implementation
  -> Review
  -> Metrics
  -> Knowledge
  -> Rule
  -> Next Improvement
```

Metrics are reviewed evidence, not automatic decisions. They should explain
what changed, where the data came from, what period or sample was measured, and
what interpretation still needs human review.

Use this loop when a change affects OCR quality, review workload, documentation
reuse, automation behavior, or workflow efficiency.

## Knowledge Asset Promotion Flow

When a task discovers reusable project knowledge, use this flow:

```text
Observed result
  -> Review
  -> Candidate Knowledge Asset
  -> Human Approval when required
  -> Knowledge Asset Layer
  -> Automation / Candidate Engine / Review GUI consumes asset
  -> Improvement Review checks whether workflow, rules, or roadmap need updates
```

Knowledge Assets may include Approved Alias, Metadata Override, Unicode Rules,
Golden Samples, OCR Confusion Rules, Review Decisions, Series Rules, Platform
Rules, and User Overrides.

Knowledge Asset Layer is used after review has identified reusable knowledge
and before automation relies on that knowledge. Raw observations, unreviewed
CSV edits, and one-off AI guesses should not be treated as approved assets.

## PIP Update Flow

Current project state、priorities、architecture summary、known issues、next
task、reusable improvement history、accepted decisions が変わった場合は PIP を
更新します。

Standard flow:

```text
Completed Q / Reviewed Work
  -> Completion Report
  -> Improvement Review
  -> PIP Improvement History
  -> PIP Decision History, when accepted decisions changed
  -> PIP Current Status / Next Task
  -> Human Review
```

PIP は briefing artifact です。Official documents を要約し、リンクしますが、
rules、workflow、architecture、roadmap、templates、examples、evidence artifacts
を置き換えません。

Command Center は PIP を current briefing source として読めます。GIP は reviewed
specification が作られるまで future candidate として扱います。

## PIP Case Knowledge Base Flow

When a completed Q or review produces reusable knowledge, use this flow:

```text
Field Issue / Completed Q
  -> Completion Report
  -> Improvement Review
  -> Case Candidate
  -> Tagging
  -> PIP Case
  -> Case Index Update
  -> Rule Story / Best Practice / Evolution, when needed
  -> Concept Promotion, when the lesson is still an early concept
  -> Knowledge Promotion
  -> Human Review
```

Use `pip/templates/case_template.md`, tag cases with
`pip/tagging_standard.md`, and update `pip/case_index.md`.

Concept status and promotion follow `concept_promotion_workflow.md`.

## Concept Promotion Workflow

Concepts under `pip/concepts/` should move through a reviewed lifecycle instead
of staying as loose notes.

```text
Idea
  -> Concept Candidate
  -> Under Review
  -> Experiment
  -> Validated Concept
  -> Rule / Best Practice / Workflow / Principle
  -> Promoted
```

Archive path:

```text
Concept Candidate
  -> Under Review
  -> Archived
```

Details follow `concept_promotion_workflow.md`.

Concept operation templates:

- `pip/templates/concept_template.md`
- `pip/templates/concept_status_change_report_template.md`
- `pip/templates/concept_review_checklist.md`

For PIP Master Document / Title List integration, use:

- `pip/MASTER_DOCUMENT_JP.md`
- `pip/MASTER_TITLE_LIST_JP.md`
- `docs/workflow/pip_case_knowledge_base_workflow.md`

## Roadmap2 Knowledge Salvage Loop

Use this loop until Roadmap2 no longer contains reusable knowledge that is
missing from GDS.

```text
Roadmap2 Review Request
  -> Review Result
  -> Missing Knowledge Extraction
  -> Q Artifact
  -> Codex Documentation Update
  -> GitHub Push / Review
  -> Roadmap2 Re-review
  -> Repeat Until No Missing Knowledge
```

Details follow `roadmap2_knowledge_salvage_loop.md`.

## Step Meanings

Idea:

An observation, problem, feature request, or improvement proposal.

Knowledge Check:

Check whether the idea should first produce reusable knowledge before changing
automation. For example, an OCR failure may need Alias Review and approved
metadata before it needs another OCR profile.

Review:

Clarify scope, risk, repository boundaries, and whether the idea should be
handled now or preserved as a Future Candidate.

Q Artifact Workspace:

A structured request that defines Repository Information, Scope Guard, Do / Do
Not, completion criteria, and deliverables, plus the task folder that preserves
the request, completion report, notes, and attachments. It should be saved in
`docs/requests/<project>/<status>/` before implementation when it is
reusable, reviewable, AI-handoff, or Git-managed.

The minimum full workspace is:

```text
request.md
completion_report.md
notes.md
attachments/
```

Completion Report Artifact:

A saved report that links the completed work back to the source Q file,
generated files, output artifacts, commit hash when one exists, and follow-up Q.
It should be stored alongside the source Q artifact.

Implementation:

The accepted scope is applied. Documentation-only requests stay documentation
only.

Verification:

Confirm changed files, scope boundaries, non-scope items, and requested
acceptance criteria.

Improvement Review:

Review whether the completed work revealed reusable improvements for
Documentation, Templates, Workflow, Roadmap, Rules, Architecture, or Knowledge
Base.

Recommended / Future Candidates:

Separate near-term improvements from ideas that should remain future work.

Template / Rule / Knowledge Base:

Promote reusable knowledge into the right durable location.

Knowledge Asset:

Promote reviewed operational knowledge into Knowledge Asset Layer when it
should be consumed by tools, candidate engines, review GUI, Knowledge Editor, or
future project automation.

## Improvement Review As Completion Gate

Improvement Review is part of completion.

A task is not fully reported until it has considered whether reusable knowledge
should be promoted or preserved.

## Update Policy

Update workflow documents when repeated practice proves a better standard flow.

Do not treat an unreviewed Future Candidate as approved workflow.

## Related Documents

- `docs/workflow/template_lifecycle.md`
- `docs/workflow/ai_daily_operation_cycle.md`
- `docs/workflow/gds_health_update_workflow.md`
- `docs/workflow/repository_quality_audit_workflow.md`
- `docs/workflow/encoding_regression_prevention_workflow.md`
- `docs/workflow/japanese_documentation_localization_workflow.md`
- `templates/daily_operation_checklist_template.md`
- `docs/workflow/ai_startup_procedure.md`
- `docs/workflow/intent_driven_workflow.md`
- `docs/workflow/artifact_creation_startup_enforcement_workflow.md`
- `docs/workflow/knowledge_preservation_gate.md`
- `docs/workflow/knowledge_carry_forward_workflow.md`
- `docs/workflow/startup_checklist_workflow.md`
- `docs/rules/conversation_insight_capture_rules.md`
- `docs/workflow/repository_root_validation_workflow.md`
- `docs/ai_repository_index.md`
- `docs/workflow/collaborative_decision_workflow.md`
- `docs/workflow/completion_checklist_workflow.md`
- `docs/workflow/completion_report_workflow.md`
- `docs/workflow/research_mission_workflow.md`
- `docs/workflow/output_policy.md`
- `docs/workflow/q_file_creation_workflow.md`
- `docs/workflow/q_revision_addendum_workflow.md`
- `docs/workflow/commit_safety_checklist.md`
- `docs/workflow/debug_artifact_review_workflow.md`
- `docs/workflow/debug_escalation_ladder.md`
- `docs/workflow/first_broken_step_methodology.md`
- `docs/workflow/migration_first_workflow.md`
- `docs/workflow/innovation_pipeline_workflow.md`
- `docs/workflow/conversation_insight_capture_workflow.md`
- `docs/workflow/concept_promotion_workflow.md`
- `docs/workflow/pip_case_knowledge_base_workflow.md`
- `docs/workflow/roadmap2_knowledge_salvage_loop.md`
- `docs/workflow/git_execution_adapter_vertical_slice_workflow.md`
- `docs/rules/workflow_rules.md`
- `docs/rules/migration_first_rules.md`
- `docs/rules/debug_artifact_review_rules.md`
- `docs/rules/debug_escalation_ladder_rules.md`
- `docs/rules/roadmap2_knowledge_salvage_rules.md`
- `docs/rules/git_rules.md`
- `docs/rules/artifact_first_rules.md`
- `docs/rules/q_file_artifact_standard.md`
- `pip/PIP_README_v1.1.md`
- `docs/requests/README.md`
- `docs/rules/project_rules.md`
- `docs/rules/core_principles.md`
- `docs/rules/external_source_access_rules.md`
- `docs/rules/startup_checklist_rules.md`
- `docs/rules/repository_root_validation_rules.md`
- `docs/rules/ai_proactive_proposal_rules.md`
- `docs/rules/completion_checklist_rules.md`
- `docs/rules/research_mission_rules.md`
- `templates/Q_TEMPLATE.md`
- `templates/innovation_pipeline_template.md`
- `docs/templates/review_checklist.md`
- `docs/history/knowledge_base_history.md`

## AI Repository Index Update Gate

Use `completion_report_workflow.md` and `documentation_synchronization_workflow.md` for the AI Repository Index Update Gate introduced by GDS-QUALITY-005.

The gate requires index regeneration, validation, `git diff --check`, workspace status evidence, generated entry count, and Safe Commit Set classification whenever index-target Knowledge Assets change.

It also requires distinguishing local index generation from public Raw availability after Commit and Push.
