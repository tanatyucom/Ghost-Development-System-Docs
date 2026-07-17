# Repository Audit

## Purpose

Record the duplicate / revision audit for GDS-STARTUP-002.

## Search Terms

- Startup Enforcement
- Intent-Aware
- Workflow Resolver
- Knowledge Requirement Resolver
- Artifact Creation
- pre-generation
- Constraint Check
- Canonical Template
- Revision First

## Findings

Existing artifacts:

- `docs/workflow/q_file_creation_workflow.md`
- `docs/rules/q_file_template_rules.md`
- `docs/workflow/startup_completion_gate.md`
- `docs/workflow/ai_startup_procedure.md`
- `docs/workflow/intent_driven_workflow.md`
- `docs/architecture/intent_driven_workflow.md`
- `docs/architecture/command_center_architecture.md`
- `docs/adr/ADR-GDS-005_context_reconstruction_and_knowledge_guided_recommendations.md`
- `docs/requests/gds/draft/GDS-TEMPLATE-001_canonical_template_synchronization_improvement/attachments/canonical_template_synchronization.md`

Gap:

The repository has Startup, Q Creation, Canonical Template Synchronization, and
Intent-Driven Workflow, but no dedicated pre-generation enforcement layer that
maps managed artifact intent to required workflow, required knowledge,
canonical template verification, Revision First, and Constraint Check before
draft generation.

## Revision First Decision

Create a small new architecture / workflow / rule set and revise related entry
points. Do not replace existing Startup or Q File Creation Workflow.

## SCW Review

No duplicate canonical artifact was found. Runtime enforcement remains out of
scope.
