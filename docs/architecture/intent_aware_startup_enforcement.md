# Intent-Aware Startup Enforcement Architecture

**Status:** Draft Architecture Foundation

**Last Updated:** 2026-07-17

## Purpose

Intent-Aware Startup Enforcement prevents AI from generating managed artifacts
from memory, stale templates, uploaded copies, or incomplete context.

Before creating Q, ADR, Rule, Workflow, Template, Roadmap, Completion Report,
or similar managed artifacts, AI must resolve the user's intent into required
workflow, required knowledge, canonical template, revision target, constraint
check, and approval boundary.

This document defines the architecture boundary. It does not implement runtime
automation or autonomous execution.

Runtime execution details are defined separately in
`docs/architecture/runtime_startup_enforcement.md`.

## Problem Statement

GDS has Startup, Q File Creation Workflow, Canonical Template Synchronization,
Intent-Driven Workflow, Knowledge Promotion Engine, and Human Approval Gate.

The missing layer is enforcement between:

```text
User Intent -> Artifact Generation
```

Without this layer, AI can incorrectly:

- generate from remembered template structure;
- claim repository access is unavailable without attempting available checks;
- skip canonical source review;
- skip Revision First;
- apply SCW instead of performing available required checks;
- create duplicate artifacts when revision is enough.

## Architecture Overview

```text
User Artifact Intent
  -> Intent-Aware Startup Enforcement
  -> Artifact Intent Classifier
  -> Workflow Resolver
  -> Knowledge Requirement Resolver
  -> Canonical Repository / Template Verification
  -> Revision First Resolver
  -> Constraint Check
  -> Gate Decision
  -> Recommendation / Draft Generation / SCW
  -> Pending Action
  -> Human Approval
  -> Execution
```

## Core Components

### Artifact Intent Classifier

Classifies managed artifact generation requests.

Initial artifact intents:

- Q creation / revision.
- ADR creation / revision.
- Rule creation / revision.
- Workflow creation / revision.
- Template creation / revision.
- Roadmap creation / revision.
- Completion Report creation.
- Knowledge / Conversation Insight / Issa draft.
- Registry or index update.

### Workflow Resolver

Maps artifact intent to required workflow.

Examples:

| Artifact Intent | Required Workflow |
| --- | --- |
| Q creation | `docs/workflow/q_file_creation_workflow.md` |
| Q revision | `docs/workflow/q_revision_addendum_workflow.md` |
| ADR candidate | `docs/workflow/architecture_promotion_lifecycle.md` |
| Rule / Workflow promotion | `docs/workflow/knowledge_preservation_gate.md` and relevant lifecycle |
| Completion Report | `docs/workflow/completion_report_workflow.md` |
| Template update | Canonical Template Synchronization and template lifecycle |
| Roadmap update | Roadmap responsibility and Product Documentation Hierarchy |

Workflow Resolver is advisory and gate-oriented. It does not execute work.

### Knowledge Requirement Resolver

Maps artifact intent to required knowledge.

Examples:

- AI Repository Index.
- Current Mission / Roadmap.
- Target Project Profile.
- Related Rules.
- Related Workflow.
- Related Architecture / ADR.
- Canonical Template.
- Existing artifacts in the target directory.
- Related Completion Reports.
- Constraint / scope / Human Approval boundary.

### Canonical Repository / Template Verification

Verifies that the artifact is generated from the canonical repository source,
not from memory or stale copies.

For Q creation, the canonical template is:

```text
templates/Q_TEMPLATE.md
```

If a Raw URL is used, freshness must be recorded. If repository access is
available, AI must attempt the actual check before claiming it cannot access
the repository.

### Revision First Resolver

Checks whether the requested artifact should revise an existing canonical
artifact instead of creating a competing one.

Outcomes:

- `new_artifact_allowed`
- `revision_required`
- `addendum_required`
- `duplicate_found`
- `scw_required`

### Constraint Check

Confirms:

- repository scope;
- target / non-target project;
- commit / push policy;
- forbidden edits;
- runtime / documentation boundary;
- Human Approval needs;
- validation commands.

### Gate Decision

Possible decisions:

- `PASS`: all required checks complete.
- `PASS_WITH_LIMITATION`: safe limitation recorded.
- `BLOCK`: generation must not start.
- `SCW_REQUIRED`: stop, call, wait for human decision.

## Enforcement Rule

Managed artifact generation must not begin until:

1. artifact intent is classified;
2. required workflow is resolved;
3. required knowledge is resolved;
4. canonical repository / template source is verified;
5. Revision First is decided;
6. Constraint Check is complete;
7. Human Approval boundary is clear.

## Responsibility Boundaries

| Component | Owns | Does Not Own |
| --- | --- | --- |
| Intent Engine | User intent interpretation | Artifact generation gate completion |
| Startup Enforcement | Required pre-generation checks | Runtime automation |
| Workflow Resolver | Required workflow mapping | Workflow execution |
| Knowledge Requirement Resolver | Required knowledge mapping | Knowledge promotion |
| Template Engine | Template application after verification | Canonical source authority |
| Command Center | Future orchestration | Human Approval replacement |

## SCW Conditions

Apply SCW when:

- canonical artifact cannot be found;
- canonical template is unreadable;
- template version or source conflicts;
- multiple workflow owners conflict;
- related knowledge is required but missing;
- duplicate artifact is possible and revision owner is unclear;
- repository access actually fails after an attempted check;
- user intent conflicts with scope or constraints;
- Human Approval boundary is unclear.

Do not use SCW as a substitute for performing an available required check.

## Reason Codes

Positive:

- `INTENT_CLASSIFIED`
- `WORKFLOW_RESOLVED`
- `KNOWLEDGE_REQUIREMENTS_RESOLVED`
- `CANONICAL_REPOSITORY_VERIFIED`
- `CANONICAL_TEMPLATE_VERIFIED`
- `REVISION_FIRST_DECIDED`
- `CONSTRAINT_CHECK_PASSED`
- `GENERATION_GATE_PASSED`

Blocking:

- `INTENT_AMBIGUOUS`
- `WORKFLOW_UNRESOLVED`
- `KNOWLEDGE_REQUIREMENT_UNRESOLVED`
- `CANONICAL_NOT_FOUND`
- `TEMPLATE_MISMATCH`
- `DUPLICATE_FOUND`
- `REVISION_REQUIRED`
- `CONSTRAINT_FAILED`
- `REPOSITORY_ACCESS_UNATTEMPTED`
- `REPOSITORY_ACCESS_FAILED`
- `HUMAN_APPROVAL_REQUIRED`
- `SCW_REQUIRED`

## Relationship To Existing GDS Architecture

- Intent-Driven Workflow decides what the user is asking for.
- Startup Enforcement decides what must be checked before artifact generation.
- Runtime Startup Enforcement defines how a future runtime caller executes that
  gate, records evidence, returns gate decisions, and preserves Human Approval
  and SCW boundaries.
- Q File Creation Workflow defines how Q artifacts are created.
- Q File Template Rules define mandatory Q fields.
- ADR-GDS-005 explains repository-based context reconstruction and
  knowledge-guided recommendations.
- Knowledge Promotion Engine handles reusable knowledge discovered during or
  after work.

## Out Of Scope

- Runtime enforcement implementation.
- LLM classifier implementation.
- Automatic repository clone / pull.
- Automatic artifact generation without approval.
- Automatic commit / push / tag.
- GameGhost / GrayGhostArchive edits.
- GUI / dashboard implementation.
