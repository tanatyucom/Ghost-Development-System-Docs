# Repository Intelligence Dashboard Foundation

**Version:** Draft 1.0

**Status:** Draft Architecture Specification

**Last Updated:** 2026-07-16

## Purpose

Repository Intelligence Dashboard Foundation defines the read-only dashboard
boundary for showing repository health, registries, governance, architecture,
and current work state in one place.

The dashboard is a foundation for future Command Center work. It does not
implement a UI, server, scanner, database, automation, promotion, commit, or
repository mutation.

## Background

GDS4 established Startup, Platform Governance, ADRs, and Canonical Knowledge
Ownership. The next step is not to add more governance first, but to make the
existing repository state visible.

Repository Intelligence Dashboard is the visibility layer between repository
knowledge and future Command Center operation.

```text
Canonical Repository Knowledge
        |
        v
Repository Intelligence Dashboard
        |
        v
Human Review / Current Mission / Future Command Center
```

## Design Principles

- Read-only by default.
- Canonical-first.
- Repository is the source of truth.
- No automatic promotion.
- No automatic commit or push.
- No automatic repository mutation.
- Human Approval First.
- SCW compliant.

SCW means the dashboard must keep source, context, and workflow visible enough
that humans and AI can recover the reasoning path without hidden chat context.

## Initial Dashboard Sections

### Repository Health

Purpose:

- Show the current health of the GDS Docs repository.
- Surface quality gate status, encoding status, stale index warnings, broken
  links, missing completion reports, and known documentation gaps.

Canonical sources:

- `reports/repository_quality_report.md`
- `docs/health/gds_health_dashboard.md`
- `docs/workflow/repository_quality_audit_workflow.md`
- `docs/rules/quality_rules.md`
- `docs/rules/utf8_read_rules.md`

Required display fields:

- Health status.
- Last checked source.
- Current warnings.
- Required human action, if any.
- Related verification command or report path.

### Capability Registry

Purpose:

- Show reusable capabilities, platform candidates, and standard components that
  may be relevant to the current mission.

Canonical sources:

- `docs/research/research_registry.md`
- `docs/architecture/ghost_research_knowledge_asset.md`
- `docs/architecture/platform_standard_registry.md`
- `docs/architecture/platform_discoverability_and_component_standard.md`
- `docs/architecture/plugin_architecture_standard.md`
- `docs/workflow/innovation_pipeline_workflow.md`

Required display fields:

- Capability or standard name.
- Type.
- Status.
- Owner boundary.
- Related rule / workflow / architecture.
- Recommended next review.

### Architecture Registry

Purpose:

- Show accepted architecture documents, draft architecture proposals, and their
  relationship to current repository direction.

Canonical sources:

- `docs/architecture/README.md`
- `docs/architecture/platform_standard_registry.md`
- `docs/adr/README.md`
- `roadmap/ghost_development_system_roadmap.md`

Required display fields:

- Architecture name.
- Status.
- Canonical path.
- Related ADR, if any.
- Related roadmap direction.
- Implementation approval state.

### ADR Summary

Purpose:

- Show accepted Architecture Decision Records and future review needs without
  requiring humans to open every ADR first.

Canonical sources:

- `docs/adr/README.md`
- `docs/adr/ADR-GDS-001_ghost_platform_three_pillars.md`
- `docs/adr/ADR-GDS-002_repository_component_templates.md`
- `docs/adr/ADR-GDS-003_canonical_knowledge_ownership_and_local_artifact_governance.md`

Required display fields:

- ADR ID.
- Title.
- Status.
- Decision summary.
- Consequence summary.
- Related platform pillar or component type.

### Current Mission

Purpose:

- Show what the repository is currently trying to do, which Q or request
  artifact drives the work, and which boundaries apply.

Canonical sources:

- Current Q artifact.
- Current completion report, if present.
- `docs/ai_repository_index.md`
- `docs/workflow/ai_startup_procedure.md`
- `docs/workflow/startup_checklist_workflow.md`
- `templates/Q_TEMPLATE.md`
- `templates/completion_report_template.md`

Required display fields:

- Current mission title.
- Source Q path.
- Scope.
- Out of scope.
- Current status.
- Next action.
- Commit policy.

### Future Candidates

Purpose:

- Show known future candidates without treating them as approved work.

Canonical sources:

- `docs/architecture/platform_standard_registry.md`
- `docs/knowledge/conversation_insights/pending/README.md`
- `pip/concepts/concept_index.md`
- `roadmap/ghost_development_system_roadmap.md`
- `reports/*completion_report.md`

Required display fields:

- Candidate title.
- Type.
- Source.
- Why it may matter now.
- Required approval before action.
- Recommended next Q, if known.

### Repository Scanner Summary

Purpose:

- Show what the repository scanner or manual repository review found, without
  treating scan output as authority over canonical documents.

Canonical sources:

- `docs/architecture/command_center_architecture.md`
- `docs/ai_repository_index.md`
- Repository quality reports.
- Future Repository Scanner outputs.

Required display fields:

- Scan source.
- Scan time or report date.
- Coverage.
- Missing or stale sources.
- Human review needed.
- Follow-up recommendation.

## Metadata Definitions

Dashboard sections should use stable metadata so future UI, generated reports,
or Command Center components can read the same structure.

Minimum section metadata:

- `section_id`: stable lowercase identifier.
- `title`: human-readable section title.
- `status`: Green / Yellow / Red / Unknown / Draft.
- `source_paths`: canonical repository paths used by the section.
- `last_source_update`: known source date or report date.
- `summary`: short current state.
- `alerts`: warnings or blockers.
- `recommended_action`: next human-readable action.
- `approval_required`: yes / no.
- `automation_allowed`: yes / no; default is no.

Minimum item metadata:

- `item_id`: stable local identifier when available.
- `item_title`: human-readable title.
- `item_type`: Health / Capability / Architecture / ADR / Mission /
  Candidate / ScannerFinding.
- `canonical_path`: repository path of the source-of-truth document.
- `related_paths`: optional supporting documents.
- `status`: item status.
- `evidence`: path or short evidence note.
- `human_review`: Required / Optional / Not Required / Completed.
- `notes`: short context for humans and AI.

## Registry Integration Plan

The dashboard reads registry and architecture documents. It does not become the
registry.

Integration rules:

- Platform Standard Registry remains the source of truth for standards and
  candidates.
- ADR folder remains the source of truth for Architecture Decision Records.
- AI Repository Index remains the source of truth for public AI-readable entry
  paths.
- Repository Quality Report remains the source of truth for quality findings.
- The dashboard may show stale or missing registry coverage, but it must not
  update registry files automatically.
- Registry updates require the existing registry update workflow and Human
  Approval Gate.

Future registry-aware dashboard behavior may include:

- listing standards by status;
- detecting missing AI Repository Index entries;
- showing ADR-to-architecture relationships;
- showing candidate items that need review;
- linking future Repository Scanner results to canonical registry entries.

## Future Command Center Integration

Repository Intelligence Dashboard is the visual inspection layer for future
Command Center.

```text
Repository Scanner
        |
        v
Repository Intelligence Database
        |
        v
Repository Intelligence Dashboard
        |
        v
Knowledge Promotion Candidate
        |
        v
Command Center
```

Command Center may later use this dashboard foundation to:

- present repository state before recommending an action;
- show which canonical sources were read;
- route humans to Q drafts, completion reports, registry updates, or reviews;
- separate current mission state from future candidates;
- keep Human Approval visible before any execution.

This document does not approve Command Center implementation, dashboard UI,
database schema, backend service, automatic suggestion engine, or scanner
runtime.

## Non-Responsibilities

Repository Intelligence Dashboard must not:

- approve promotions;
- create commits;
- push to GitHub;
- mutate repository files;
- rewrite canonical sources;
- replace README, AI Repository Index, Platform Standard Registry, ADRs, or
  Repository Quality Report;
- treat generated summaries as more authoritative than source documents;
- implement Command Center.

## Initial Acceptance Criteria

The foundation is ready when:

- dashboard purpose and boundaries are documented;
- initial sections are defined;
- each section has canonical sources;
- minimum metadata is defined;
- registry integration is read-only and canonical-first;
- future Command Center relationship is documented;
- README / Architecture Index / AI Repository Index can route humans and AI to
  this document;
- implementation, automation, promotion, commit, and push remain explicitly out
  of scope.
