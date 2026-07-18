# Artifact Creation Startup Enforcement Rules

**Status:** Draft Rule

**Last Updated:** 2026-07-17

## Purpose

This rule prevents managed artifact generation from starting before required
Startup, workflow, knowledge, template, revision, and constraint checks are
complete.

## Core Rule

AI must not generate a managed artifact from memory or stale local assumptions.

Before generating Q, ADR, Rule, Workflow, Template, Roadmap, Completion Report,
Knowledge artifact, registry update, or similar durable artifact, AI must
complete the Artifact Creation Startup Enforcement Workflow.

## Output Contract Rule

When the primary deliverable is a reusable project artifact, the default output
is a repository-saved or downloadable Markdown artifact.

Reusable project artifacts include:

- Q;
- ADR;
- Roadmap;
- handoff;
- report;
- specification;
- review request;
- design document;
- template;
- completion report;
- approval packet.

For these deliverables, chat should contain only a short summary, the artifact
path or download link, and verification notes unless the user explicitly
requests inline text.

## Required Checks

- Artifact Intent classified.
- Required Workflow resolved.
- Required Knowledge resolved.
- Canonical Repository verified.
- Required Template verified.
- Related Rule / Workflow / ADR / Roadmap / Current Mission checked.
- Revision First decision recorded.
- Constraint Check completed.
- Output Contract checked.
- Human Approval boundary identified.

## Forbidden Behavior

AI must not:

- generate from remembered template structure;
- treat uploaded copies as current without freshness verification;
- create a competing artifact before duplicate / revision audit;
- claim repository access failure without attempting available checks;
- use SCW instead of performing an available required check;
- bypass Human Approval with generic agreement phrases;
- treat Future Candidates as approved scope;
- commit, push, tag, release, or cross repositories without approval.
- return only inline text for a reusable project artifact when the project
  Output Contract requires a managed file artifact.

## SCW Conditions

Apply SCW when:

- intent remains ambiguous;
- required workflow cannot be identified;
- required knowledge cannot be read;
- canonical source conflicts;
- template mismatch is detected;
- duplicate artifact is possible;
- Revision First cannot be decided;
- constraint check fails;
- Output Contract cannot be satisfied;
- Human Approval boundary is unclear.

## Reason Codes

PASS:

- `INTENT_CLASSIFIED`
- `WORKFLOW_RESOLVED`
- `KNOWLEDGE_REQUIREMENTS_RESOLVED`
- `CANONICAL_REPOSITORY_VERIFIED`
- `CANONICAL_TEMPLATE_VERIFIED`
- `REVISION_FIRST_DECIDED`
- `CONSTRAINT_CHECK_PASSED`
- `OUTPUT_CONTRACT_CHECKED`

BLOCK / SCW:

- `INTENT_AMBIGUOUS`
- `WORKFLOW_UNRESOLVED`
- `KNOWLEDGE_REQUIREMENT_UNRESOLVED`
- `CANONICAL_NOT_FOUND`
- `TEMPLATE_MISMATCH`
- `DUPLICATE_FOUND`
- `REVISION_REQUIRED`
- `CONSTRAINT_FAILED`
- `OUTPUT_CONTRACT_UNRESOLVED`
- `INLINE_ONLY_NOT_ALLOWED`
- `REPOSITORY_ACCESS_UNATTEMPTED`
- `REPOSITORY_ACCESS_FAILED`
- `HUMAN_APPROVAL_REQUIRED`
- `SCW_REQUIRED`

## Related Documents

- `docs/workflow/artifact_creation_startup_enforcement_workflow.md`
- `docs/architecture/intent_aware_startup_enforcement.md`
- `docs/workflow/q_file_creation_workflow.md`
- `docs/rules/q_file_template_rules.md`
- `docs/rules/q_file_artifact_standard.md`
- `docs/workflow/startup_completion_gate.md`
