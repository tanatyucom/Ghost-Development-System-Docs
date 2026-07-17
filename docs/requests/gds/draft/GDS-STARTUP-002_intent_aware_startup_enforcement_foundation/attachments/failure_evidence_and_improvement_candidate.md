# Failure Evidence and Improvement Candidate

## Purpose

Record why Intent-Aware Startup Enforcement exists.

## Evidence Summary

The triggering failure pattern was not lack of knowledge. The repository
contained Q Template, Startup, Canonical Template Synchronization, and related
rules. The failure was that AI moved from user intent to artifact generation
without resolving the required workflow and knowledge first.

Observed pattern:

1. Q file creation was requested.
2. AI generated from remembered structure instead of the canonical repository
   `templates/Q_TEMPLATE.md`.
3. After correction, AI described the need for repository reference but did not
   perform the reference.
4. AI treated an unattempted check as unavailable access.
5. SCW risk appeared even though the required check was available.

## Improvement Candidate

Candidate type:

- Workflow / Rule / Architecture improvement.

Statement:

- Managed artifact generation needs a pre-generation enforcement gate between
  Intent and Draft Generation.

Proposed targets:

- `docs/architecture/intent_aware_startup_enforcement.md`
- `docs/workflow/artifact_creation_startup_enforcement_workflow.md`
- `docs/rules/artifact_creation_startup_enforcement_rules.md`

Application target:

- Q File Creation.
- ADR / Rule / Workflow / Template / Roadmap artifact generation.
- Future Command Center Template Engine.

Status:

- Captured in GDS-STARTUP-002 as architecture foundation.
- Runtime enforcement remains future scope.
