# Architecture

## Purpose

This folder explains the architecture of the Ghost Development System knowledge
base.

Architecture documents describe responsibility boundaries, design philosophy,
and how the roadmap relates to future implementation. They do not implement
runtime behavior.

## Contains

- `artifact_schema_standard.md`: common schema standard for managed artifacts
  such as Q, Completion Report, Information Package, Multi-AI Handoff, Review
  Report, Decision Record, Registry Update, and Health Report.
- `adapter_only_execution_policy_review.md`: candidate-only review of
  Adapter-Only Execution for future Engine / Center production boundaries. It
  does not adopt enforcement or implementation.
- `canonical_rule_gap_resolution.md`: decision boundary for resolving
  implementation-repository style findings as repository remediation, Local
  Rule candidates, Canonical Rule gaps, Temporary Assembly candidates, or Human
  Architecture Decisions.
- `command_center_architecture.md`: Command Center architecture specification
  for Repository Scanner, Information Package Builder, Decision Engine,
  Template Engine, Artifact Pipeline, Human Approval Gate, Repository Health
  Adapter, Registry Adapter, and Handoff / Completion Adapter.
- `design_intent_preservation.md`: architecture for preserving why a design
  exists, what experience it should produce, and what must not be lost during
  generation-to-generation or tool-to-tool handoff.
- `experience_layer.md`: user-visible collaboration state layer for Vision
  Scenario, End-to-End User Journey, Approval Request, Pending Human Approval,
  BLOCK / SCW recovery, and execution boundaries.
- `approval_request_intent_queue_execution_evidence.md`: Approval Request
  specialization that defines Candidate Disclosure, Requested Operations,
  natural-language approval resolution, Intent Queue, Execution Authority,
  Delegation, and Execution Evidence without runtime Git automation.
- `approval_runtime_state_machine.md`: canonical runtime specification for
  Approval Request, Approval Unit, Human Approval, Execution Instruction,
  Action Execution, Execution Evidence, valid / invalid transitions,
  invalidation, persistence, audit events, schema direction, and conceptual API
  boundaries without implementing runtime code.
- `runtime_intent_queue_resolver.md`: documentation-level Runtime Intent Queue
  Resolver foundation for resolving approval phrases into visible execution
  queue state, execution authority, delegation, evidence reconciliation,
  deliverables, canonical artifact, and Codex handoff.
- `governed_execution_adapter_foundation.md`: governed boundary between Runtime
  Queue and execution actors/tools, defining approval, authority, scope,
  dependency, idempotency, result envelope, evidence provider, and state
  reconciliation responsibilities.
- `intent_driven_workflow.md`: canonical architecture foundation for routing
  natural language user intent through repository / conversation state review,
  workflow selection, quality gate / SCW, Human Approval, and approved action
  boundaries without implementing runtime automation.
- `intent_aware_startup_enforcement.md`: architecture foundation for blocking
  managed artifact generation until artifact intent, required workflow,
  required knowledge, canonical repository / template verification,
  Revision First, Constraint Check, and Human Approval boundary are resolved.
- `runtime_startup_enforcement.md`: runtime architecture contract for executing
  Startup Enforcement before managed artifact generation, including state
  machine, gate decision behavior, evidence model, execution log, failure
  recovery, repository interaction contract, and Command Center integration
  boundary.
- `runtime_startup_enforcement_evidence_specialization.md`: Startup-specific
  evidence specialization that extends Platform Execution Evidence Contract.
  It maps parent fields, Startup fields, lifecycle states, result meanings,
  reason codes, producer / consumer behavior, Human Approval, SCW, Revision
  First, repository verification, template verification, workflow / knowledge
  resolution, constraint evidence, and startup log relationship without
  implementing JSON schema or runtime code.
- `intent_registry_and_pending_action_contract.md`: initial Intent Registry,
  Pending Action Contract, Approval Resolution Rule for `お願いします` / `はい` /
  `OK`, Commit / Push / Tag recommendation rules, and reason code set.
- `knowledge_artifact_responsibility_map.md`: responsibility map for Q, Issa,
  ADR, Improvement Record, Rule, Architecture Principle, and Workflow,
  including triggers, lifecycle, approval boundary, canonical location, and
  cross-reference / promotion rules.
- `knowledge_promotion_engine.md`: architecture foundation for detecting,
  classifying, deduplicating, recommending, approving, carrying forward,
  validating, promoting, and applying knowledge candidates without automatic
  canonical promotion or Git operations.
- `knowledge_candidate_classification_contract.md`: candidate record contract,
  candidate types, evidence requirements, duplicate checks, approval boundary,
  and reason codes for Knowledge Promotion Engine.
- `context_aware_knowledge_suggestion_assistant.md`: draft architecture
  proposal for suggesting related Conversation Insight, Future Candidate,
  Research Mission, Improvement Record, CASE, Architecture, Rule, and Workflow
  knowledge during Startup and daily use without automatic promotion,
  implementation, Q generation, or commit.
- `plugin_architecture_standard.md`: Plugin Architecture Standard for explicit
  registry, `PLUGIN_INFO`, `PluginContext`, `PluginResult`, ownership boundary,
  lifecycle, and promotion from Internal Module to Platform Plugin.
- `local_rule_ownership.md`: ownership boundary for GDS-managed Local Rules
  discovered in implementation repositories such as GameGhost.
- `platform_candidate_workspace.md`: recommended future workspace naming and
  guardrails for `platform_candidates/` without creating the folder or
  approving runtime use.
- `platform_execution_evidence_contract.md`: common execution evidence parent
  contract for Startup Enforcement Evidence, Repository Quality Evidence,
  Command Center Execution Evidence, Completion Review Evidence, and Knowledge
  Promotion Evidence. It defines lifecycle, required fields, ownership,
  producer / consumer responsibilities, extension policy, versioning,
  compatibility, Human Approval, SCW, and integration boundaries without
  implementing runtime schema or automation.
- `repository_quality_gate_evidence_specialization.md`: Repository
  Quality-specific evidence specialization that extends Platform Execution
  Evidence Contract. It separates quality state from gate result, maps
  Green / Yellow / Red / Unknown to PASS / PASS_WITH_LIMITATION / BLOCK /
  SCW_REQUIRED, and defines check severity, reason codes, report relationship,
  freshness, Human Approval, SCW, and consumer boundaries without implementing
  schema or runtime code.
- `completion_review_execution_evidence_specialization.md`: Completion
  Review-specific evidence specialization that extends Platform Execution
  Evidence Contract. It defines completion decision, upstream Startup /
  Repository Quality evidence consumption, Safe Commit Set, commit / push
  recommendation boundaries, Human Approval, SCW, and Completion Report
  relationship without implementing schema or runtime code.
- `repository_intelligence_dashboard_foundation.md`: read-only Repository
  Intelligence Dashboard foundation for Repository Health, Capability Registry,
  Architecture Registry, ADR Summary, Current Mission, Future Candidates, and
  Repository Scanner Summary. It defines metadata and integration boundaries
  without implementing UI, database, scanner runtime, automation, promotion, or
  repository mutation.
- `../standards/ghost_package_standard_candidate.md`: Ghost Package Standard
  architecture standard candidate for PACKAGE.md, PACKAGE.yaml, Design Package,
  Milestone Package, package discovery, package registry, multi-AI package
  handoff, and future Command Center package integration without implementing
  scanner, registry, ZIP validation, or runtime automation.
- `platform_discoverability_and_component_standard.md`: Platform folder,
  component classification, naming suffix, 3 second discoverability, migration
  criteria, legacy placement, future Ghost compatibility, and Review Center
  placement standard.
- `platform_first_migration_strategy.md`: staged migration strategy from
  GameGhost to Ghost Platform, including priority matrix, platform / adapter
  boundary, legacy policy, bootstrap order, AnimeGhost check, future Ghost
  compatibility, and the Platform Evolution statement.
- `platform_governance_and_experimental_development.md`: platform governance,
  Temporary Assembly Principle, Core + Adapter Experimental Pattern,
  Architecture Promotion Lifecycle, Canonical Knowledge Ownership, Local Rule
  lifecycle, and Vision-Driven Bottom-Up Development.
- `review_center_architecture.md`: Review Center architecture for shared human
  review session management, artifact presentation, decision capture,
  persistence, result export, gate readiness, and plugin / adapter boundary.
- `responsibility_boundary.md`: ownership boundaries for DevelopmentSystem,
  Startup Checklist, Repository Root Validation, AI Proactive Proposal,
  Collaborative Decision, Completion Checklist, Output Layer, Migration First
  Boundary, Knowledge Asset Layer, Metrics Layer, PIP, Gray Ghost Core, Archive
  Modules, Command Center, and Launcher.
- `design_philosophy.md`: principles that guide architecture and documentation.
- `platform_era_core_principles.md`: classification of Platform Era ideas into
  Core Rule, Design Principle, Platform Architecture, and Long-Term Vision.
- `platform_standard_registry.md`: registry of GDS Platform standards and
  standard candidates for shared Rule, Workflow, Template, Component, Report,
  Validation, and Architecture items.
- `product_document_hierarchy_v2.md`: Product Documentation Hierarchy for
  separating Product Blueprint, Master Roadmap, Domain Roadmap, Execution
  Roadmap, Decision Record, Q Documents, and Completion Report to reduce
  context drift. It also aligns those layers with the Beginner & Future Self
  Test.
- `gameghost_platform_migration_architecture.md`: GameGhostをGDS Platformの
  最初の実利用Projectとして扱うためのPlatform migration architecture review。
- `gameghost_workspace_repository_layout.md`: `C:\GrayGhostArchive` workspace
  root、GameGhost Git root、sibling repository model、shortcut strategyの
  layout review。

## Does NOT Contain

- Runtime code.
- Module-specific implementation details.
- Migration scripts.
- GitHub Actions.
- Release artifacts.

## Relationship To Roadmap

Roadmap records long-term direction and future candidates.

Architecture explains the stable concepts behind that direction. A roadmap item
may propose a future architecture change, but the architecture document should
only describe boundaries and principles that are accepted enough to guide work.

Product Documentation Hierarchy v2 defines how Blueprint、Master Roadmap、
Current Position、Domain Roadmap、Execution Roadmap、Decision Record、
Q Documents、Completion Report are separated.
Use it before adding large roadmap or decision documents.

Beginner & Future Self Test confirms whether those documents remain
understandable to beginners, new AI sessions, returning project owners, and
future selves without hidden chat context.

Context Recovery Principle explains the underlying design objective: repository
and documentation structures should optimize for safe recovery from forgotten
or missing context, not for perfect memory retention.

## Responsibility Boundary Summary

- DevelopmentSystem owns development infrastructure.
- AI Startup Procedure owns the pre-checklist reading order for AI Repository
  Index, Repository Root Validation, GDS Core Rules / Workflow, Target Project
  Profile, Current Q File, and Startup Checklist.
- Startup Checklist owns the session-start confirmation boundary for
  repository, Q artifact, applicable rules, methodologies, scope, and commit
  policy.
- Repository Root Validation owns the boundary between declared Working
  Repository and actual Git root.
- AI Proactive Proposal owns the proposal boundary where AI can raise
  evidence-based improvements or concerns without silently changing scope.
- Collaborative Decision owns the discussion and classification boundary where
  AI and user proposals become reviewed decisions and documentation targets.
- Completion Checklist owns the task-end confirmation boundary for
  verification, review, completion report, commit / tag / release decisions,
  next Q, and workspace clean confirmation.
- Output Layer owns the durable boundary between chat summaries and managed
  artifacts.
- AI Repository Knowledge Access Index owns the public Raw URL entry boundary
  for AI-readable GDS repository knowledge.
- Debug Artifact Review owns the development-time evidence boundary for
  Debug Mode, intermediate artifacts, expected normal state, and review
  handoff.
- Debug Escalation Ladder owns the escalation order from phenomenon check to
  algorithm change.
- Migration First Boundary owns the distinction between internal structures
  that should migrate to a new standard and public compatibility contracts that
  must remain stable.
- Knowledge Asset Layer owns the shared boundary for reviewed Knowledge Assets.
- Metrics Layer owns the shared boundary for reviewed measurement and evidence.
- PIP owns the project briefing boundary for current state, Improvement
  History, Decision History, Case Knowledge Base, and AI handoff.
- Gray Ghost Core owns analysis, recommendation, and cross-module intelligence.
- Archive Modules own business logic, schema, metadata, and import rules.
- Command Center owns the operational entry point and repository orchestration
  boundary. It may scan repository documents, assemble Information Packages,
  route to Knowledge Dashboard or Editor, surface Repository Health, and draft
  Q / review / completion / registry update artifacts through templates.
- Artifact Schema Standard owns the common documentation schema for artifacts
  generated or managed by Command Center, Template Engine, Decision Engine, and
  future Ghost SDK candidates.
  Structured Artifact Metadata Template maps that schema into optional YAML
  front matter for new managed artifacts.
- Platform Execution Evidence Contract owns the common evidence model for
  platform execution decisions and gate results. It is the parent contract for
  Startup Enforcement, Repository Quality, Command Center, Completion Review,
  and Knowledge Promotion evidence. It does not implement JSON schema,
  runtime automation, GUI, plugin behavior, repository mutation, or approval
  replacement.
- Plugin Architecture Standard owns the explicit plugin boundary for future GDS
  Platform extensions. It defines Plugin versus Internal Module, registry,
  metadata, interface, ownership, lifecycle, and promotion rules. It does not
  approve automatic discovery, launcher modification, `tool.py` split, or
  runtime implementation by itself.
- Platform Discoverability and Component Standard owns the folder, naming,
  component classification, and 3 second discoverability boundary for shared
  Ghost Platform components. It separates generic Platform responsibilities
  from project-specific adapters and does not move runtime code by itself.
- Platform First Migration Strategy owns the sequence for moving reusable
  GameGhost-derived capabilities toward Platform. It defines migration priority,
  platform / adapter split, legacy cleanup timing, bootstrap order, and
  cross-Ghost validation before runtime movement.
- Platform Governance and Experimental Development owns the governance boundary
  for ADR-backed platform decisions, Temporary Assembly, Core + Adapter
  experiments, canonical knowledge ownership, Local Rule lifecycle, and
  Architecture Promotion. It does not approve SDK completion, runtime
  implementation, automatic promotion, or bulk migration.
- Review Center Architecture owns the shared Human Review Session Manager
  boundary. It displays artifacts, captures human decisions, manages progress,
  persists review state, exports results, and leaves domain correctness to
  plugins, adapters, and human reviewers.
- Repository Intelligence Dashboard Foundation owns the read-only visibility
  layer for repository health, registries, governance, architecture, current
  mission, future candidates, and scanner summaries. It does not own canonical
  sources, automatic promotion, UI implementation, database implementation,
  scanner runtime, commit, push, or repository mutation.
- Intent-Driven Workflow owns the interpretation boundary between natural
  language user intent and GDS workflow recommendation. It may produce
  Recommendation and Pending Action artifacts, but it does not execute commit,
  push, tag, release, file deletion, data mutation, or external publication
  without explicit Human Approval.
- Intent-Aware Startup Enforcement owns the pre-generation gate for managed
  artifacts. It prevents direct generation from remembered templates or
  incomplete context by resolving required workflow, required knowledge,
  canonical source, Revision First, Constraint Check, and approval boundary.
- Runtime Startup Enforcement owns the future execution contract for running
  that gate before Template Engine or Artifact Pipeline starts managed artifact
  generation. It may read repository state and emit evidence, but it does not
  own artifact content generation, autonomous repository mutation, Human
  Approval replacement, commit, push, tag, release, GUI, or plugin
  implementation.
- Runtime Startup Enforcement Evidence Specialization owns the Startup-specific
  interpretation of Platform Execution Evidence Contract. It keeps Startup
  gate truth compatible with the parent contract while preserving Command
  Center as consumer / orchestrator and Human Approval as the approval owner.
- Repository Quality Gate Evidence Specialization owns the Repository
  Quality-specific interpretation of Platform Execution Evidence Contract. It
  keeps Repository Quality Report as human-readable presentation while making
  quality state, gate result, warnings, errors, freshness, approval state, and
  SCW state available as platform decision evidence.
- Completion Review Execution Evidence Specialization owns the completion
  decision interpretation of Platform Execution Evidence Contract. It connects
  Startup Evidence and Repository Quality Evidence to Completion Report,
  Safe Commit Set, commit / push recommendation, Human Approval, SCW,
  remaining issues, and Recommended Next Q.
- Knowledge Artifact Responsibility Map owns the separation between Q, Issa,
  ADR, Improvement Record, Rule, Architecture Principle, and Workflow so that
  GDS preserves what changed, why it mattered, what was decided, and what should
  be promoted without collapsing all knowledge into a single artifact.
- Knowledge Promotion Engine owns the governed learning loop from development
  experience to candidate detection, classification, canonical source check,
  promotion recommendation, Human Approval, Knowledge Carry-Forward, validation,
  canonical promotion, lineage, and future application targets.
- Launcher owns the user entry point.

## Database Philosophy Summary

DevelopmentSystem owns Database Utility.

Archive Modules own Schema Ownership.

DevelopmentSystem may provide reusable database helpers, validation,
migration-assistance, backup coordination, and health checks. Archive Modules
remain responsible for their own schemas and module-specific data meaning.

Knowledge Asset Layer may provide the shared structure for Approved Alias,
Metadata, Unicode Rules, Golden Samples, OCR Confusion Rules, Review Decisions,
Series Rules, Platform Rules, User Overrides, and future AI knowledge. It does
not replace project-owned schema or runtime behavior.

## Design Philosophy Summary

Accepted design principles include Evidence First, Purpose-Oriented Naming,
Human Approval Gate, Knowledge Before Automation, Knowledge Poka-Yoke / Design
For Forgetfulness, Startup Checklist, Repository Root Validation, AI Proactive
Proposal, Collaborative Decision, Completion Checklist, Artifact First, Debug
Artifact Review, and Migration First.

Startup Checklist supports these principles by confirming the active repository,
scope, applicable rules, methodologies, Q artifact status, and commit policy
before implementation or review begins.

Repository Root Validation supports Startup Checklist by checking the actual
Git root before work begins.

## Command Center Direction

Command Center is a Repository Orchestrator, not only an Auto Q Generator.

```text
Repository Scan
        |
        v
Information Package
        |
        v
Decision Engine
        |-- Q Draft
        |-- Review Draft
        |-- Completion Draft
        |-- Registry Update
        |-- Repository Health
        `-- Recommended Next Q
```

Command Center follows Repository First, Platform First, Template First, and
Artifact First. Implementation, automation, UI, and server behavior remain
future work that requires a separate Q and Human Approval Gate.

Detailed specification:

- `docs/architecture/command_center_architecture.md`
- `docs/architecture/context_aware_knowledge_suggestion_assistant.md`
- `docs/architecture/artifact_schema_standard.md`
- `docs/architecture/plugin_architecture_standard.md`
- `docs/architecture/platform_discoverability_and_component_standard.md`
- `docs/architecture/platform_first_migration_strategy.md`
- `docs/architecture/review_center_architecture.md`
- `templates/structured_artifact_metadata_template.md`

AI Proactive Proposal supports human-led collaboration by making concerns and
better options visible without taking control away from the user.

Collaborative Decision turns proposals and disagreements into evidence-reviewed
knowledge classification and documented decisions.

Completion Checklist supports these principles by confirming verification,
review, completion report, Improvement Review, commit / tag / release decisions,
next Q, and workspace clean state before work is treated as complete.

Output Layer supports Artifact First by making reusable Q files, design
documents, specifications, review requests, AI requests, roadmap proposals, and
human approval packets durable, reviewable, and Git-manageable.

Debug Artifact Review supports AI, OCR, recommendation, auto-detection,
candidate extraction, fuzzy matching, and visual processing work by making
intermediate evidence inspectable during development while keeping normal
execution free from debug outputs.

Debug Escalation Ladder keeps uncertain defects from jumping directly to
algorithm change. It orders investigation as phenomenon check, metrics check,
human review, debug artifacts, pipeline trace, first broken step, root cause,
and only then algorithm change.

Migration First supports internal architecture by preferring New Standard,
Migration Plan, Reference Update, Verification, and Legacy Removal over
permanent compatibility fallback. It protects Public Compatibility for public
release, API / CLI, documented external workflow, exported artifact schema, DB
schema, and user-facing data formats.

Q file artifacts and related completion report artifacts are stored in Task
Artifact Workspaces under `docs/requests/` so the request, execution report,
notes, attachments, review, and commit evidence can be followed as one chain.

Knowledge Before Automation means that when automation fails, the system should
first capture reusable reviewed knowledge before adding more automation
complexity.

Knowledge Poka-Yoke / Design For Forgetfulness means that GDS assumes humans
forget, AI forgets, and processes drift. Startup Checklist, Completion
Checklist, Repository Root Validation, Repository Information, Scope Guard, Q
Artifact, AI Repository Knowledge Access Index, Completion Report, Human
Review, AI Proactive Proposal, and Collaborative Decision are treated as
checkable controls that make forgetting safe before it becomes an incident.

AI Repository Knowledge Access Index supports external AI review by making the
public repository readable through stable Raw URLs. It is a documentation
access boundary, not a replacement for official rule authority.

Knowledge Platform direction extends this principle by treating reusable
knowledge as assets that can be edited through Knowledge Editor, observed
through Knowledge Assets Dashboard, and consumed through Knowledge Asset Layer.

Metrics Layer extends Evidence First by turning field results into comparable
signals such as success rate, review rate, reuse count, review iterations, and
automation rate.

PIP は current state とその理由を要約し、AI handoff と Command Center briefing
を支えます。PIP は official GDS Docs、Information Package evidence、roadmap
archives、completion reports を置き換えません。

PIP Case Knowledge Base stores reusable cases, rule stories, evolutions, best
practices, investigations, concepts, and case templates under `pip/`. It summarizes
reviewed knowledge and links evidence, but it does not own official rule
authority or raw evidence.

Roadmap2 Knowledge Salvage is the review loop that moves remaining Roadmap2
knowledge into GDS / PIP before Roadmap2 becomes history. It is a documentation
and knowledge-promotion boundary, not approval for new runtime features.

Concept Promotion is the lifecycle boundary for `pip/concepts/`. It decides
whether an early idea becomes a stronger knowledge unit or is archived, but it
does not itself approve runtime implementation.

Platform Era Core Principle Classification separates roadmap ideas into Core
Rule, Design Principle, Platform Architecture, and Long-Term Vision. This keeps
Silent Operation Principle, Platform First, Reuse Before Rebuild, Innovation
Pipeline, Ghost Ecosystem, Automation Server, and AI Continuous Improvement
usable for design without turning them into implementation approval.

Platform Standard Registry lists accepted GDS Platform standards and standard
candidates after Innovation Pipeline and Platform Promotion review. It is the
lookup point for AI Repository Index, Project Profile System, AI Startup
Procedure, Daily Operation Cycle, GDS Health, Repository Quality Audit, UTF-8
Read Rule, Japanese Documentation Localization, Innovation Pipeline, Platform
Promotion Decision Report, Knowledge Poka-Yoke, and Repository Root Validation.
Platform Discoverability and Component Standard extends this registry direction
by making future component folders and names reviewable before runtime
migration begins.
Platform First Migration Strategy applies that component model to the first
migration sequence and makes Review Center the P0 candidate.
Review Center Architecture defines the P0 candidate boundary before any
GameGhost runtime implementation or Steam OCR adapter extraction begins.
Repository Intelligence Dashboard Foundation defines the visibility layer that
can later sit between Repository Scanner output and Command Center, while
keeping canonical documents and Human Approval as the authority.
GDS Core / AI Actor / Adapter Boundary defines GDS as Core, AI as an
exchangeable Actor / Interpreter / Delegate, and target systems as governed
Adapter targets. Git Execution Adapter Vertical Slice applies that boundary to
Git Commit / Push / Tag without approving production automation.

Project Adoption and Hotfix parking lot candidates are preserved in
`roadmap/ghost_development_system_roadmap.md`,
`roadmap/platform_first_migration_roadmap.md`, and
`docs/rules/hotfix_policy_rules.md`. They do not create a new architecture
layer and do not change the current OCR Vertical Slice priority.

## Update Policy

Update architecture documents when responsibility boundaries, design philosophy,
or accepted architecture terms change.

Do not use this folder to approve Future Candidates by implication.

## Related Documents

- `docs/architecture/responsibility_boundary.md`
- `docs/architecture/design_philosophy.md`
- `docs/architecture/platform_era_core_principles.md`
- `docs/architecture/platform_standard_registry.md`
- `docs/architecture/platform_discoverability_and_component_standard.md`
- `docs/architecture/platform_first_migration_strategy.md`
- `docs/architecture/repository_intelligence_dashboard_foundation.md`
- `docs/architecture/review_center_architecture.md`
- `docs/architecture/gds_core_ai_actor_adapter_boundary.md`
- `docs/architecture/git_execution_adapter_vertical_slice.md`
- `docs/architecture/gameghost_platform_migration_architecture.md`
- `docs/architecture/gameghost_workspace_repository_layout.md`
- `docs/ai_repository_index.md`
- `docs/rules/core_principles.md`
- `docs/rules/external_source_access_rules.md`
- `docs/rules/startup_checklist_rules.md`
- `docs/rules/repository_root_validation_rules.md`
- `docs/rules/ai_proactive_proposal_rules.md`
- `docs/workflow/collaborative_decision_workflow.md`
- `docs/rules/completion_checklist_rules.md`
- `docs/rules/hotfix_policy_rules.md`
- `docs/workflow/startup_checklist_workflow.md`
- `docs/workflow/repository_root_validation_workflow.md`
- `docs/workflow/completion_checklist_workflow.md`
- `docs/rules/artifact_first_rules.md`
- `docs/rules/q_file_artifact_standard.md`
- `docs/rules/debug_artifact_review_rules.md`
- `docs/rules/debug_escalation_ladder_rules.md`
- `docs/rules/migration_first_rules.md`
- `docs/rules/roadmap2_knowledge_salvage_rules.md`
- `docs/requests/README.md`
- `docs/workflow/output_policy.md`
- `docs/workflow/debug_artifact_review_workflow.md`
- `docs/workflow/debug_escalation_ladder.md`
- `docs/workflow/migration_first_workflow.md`
- `docs/workflow/concept_promotion_workflow.md`
- `docs/workflow/roadmap2_knowledge_salvage_loop.md`
- `docs/rules/project_rules.md`
- `docs/roadmap/ghost_development_system_roadmap.md`
- `docs/roadmap/roadmap.md`
