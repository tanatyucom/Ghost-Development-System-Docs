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
- `command_center_architecture.md`: Command Center architecture specification
  for Repository Scanner, Information Package Builder, Decision Engine,
  Template Engine, Artifact Pipeline, Human Approval Gate, Repository Health
  Adapter, Registry Adapter, and Handoff / Completion Adapter.
- `context_aware_knowledge_suggestion_assistant.md`: draft architecture
  proposal for suggesting related Conversation Insight, Future Candidate,
  Research Mission, Improvement Record, CASE, Architecture, Rule, and Workflow
  knowledge during Startup and daily use without automatic promotion,
  implementation, Q generation, or commit.
- `plugin_architecture_standard.md`: Plugin Architecture Standard for explicit
  registry, `PLUGIN_INFO`, `PluginContext`, `PluginResult`, ownership boundary,
  lifecycle, and promotion from Internal Module to Platform Plugin.
- `platform_discoverability_and_component_standard.md`: Platform folder,
  component classification, naming suffix, 3 second discoverability, migration
  criteria, legacy placement, future Ghost compatibility, and Review Center
  placement standard.
- `platform_first_migration_strategy.md`: staged migration strategy from
  GameGhost to Ghost Platform, including priority matrix, platform / adapter
  boundary, legacy policy, bootstrap order, AnimeGhost check, and future Ghost
  compatibility.
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
