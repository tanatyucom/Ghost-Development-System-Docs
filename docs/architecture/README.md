# Architecture

## Purpose

This folder explains the architecture of the Ghost Development System knowledge
base.

Architecture documents describe responsibility boundaries, design philosophy,
and how the roadmap relates to future implementation. They do not implement
runtime behavior.

## Contains

- `responsibility_boundary.md`: ownership boundaries for DevelopmentSystem,
  Output Layer, Migration First Boundary, Knowledge Asset Layer, Metrics Layer,
  PIP, Gray Ghost Core, Archive Modules, Command Center, and Launcher.
- `design_philosophy.md`: principles that guide architecture and documentation.

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
- Output Layer owns the durable boundary between chat summaries and managed
  artifacts.
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
- Command Center owns the operational entry point and may route to Knowledge
  Dashboard or Editor.
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
Human Approval Gate, Knowledge Before Automation, Artifact First, Debug
Artifact Review, and Migration First.

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

## Update Policy

Update architecture documents when responsibility boundaries, design philosophy,
or accepted architecture terms change.

Do not use this folder to approve Future Candidates by implication.

## Related Documents

- `docs/architecture/responsibility_boundary.md`
- `docs/architecture/design_philosophy.md`
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
