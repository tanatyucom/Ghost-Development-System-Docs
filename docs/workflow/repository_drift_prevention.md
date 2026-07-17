# Repository Drift Prevention

## Status

Future Candidate.

This workflow candidate is registered for quality improvement. It does not
replace AI Startup Procedure, Startup Checklist, Startup Completion Evidence,
Startup Completion Gate, or Pre-Response Verification Gate.

## Purpose

Repository Drift is the quality risk where an AI starts from canonical
repository sources, but during reasoning and artifact generation gradually
shifts its working reference point toward internal abstracted knowledge.

Repository Re-anchor is the proposed practice of returning to canonical
repository sources during artifact generation so the repository remains the
reasoning baseline.

## Definitions

### Repository Drift

Repository Drift is the movement of the active reference center from canonical
repository files to the AI's internal summarized or abstracted understanding.

Observed pattern:

- Startup completed.
- Repository synchronized.
- Template understood.
- Artifact generation starts.
- Template or rule is not re-read at the point of use.
- Output is based on generalized memory of the template instead of the current
  repository version.
- The pattern is especially likely in a new chat or long-running task.

### Repository Re-anchor

Repository Re-anchor is a deliberate return to canonical repository sources
while work is in progress.

It asks the AI to re-check the relevant template, rule, workflow, roadmap,
index, or artifact before producing or finalizing an output.

### Reference Loop

```text
Reference
  -> Reason
  -> Reference
  -> Reason
  -> Reference
  -> Output
```

## Candidate Workflow

```text
Template reference
  -> Rule reference
  -> Workflow reference
  -> Reasoning
  -> Repository Re-anchor
  -> Artifact creation
  -> Final template check
```

## Relationship To Startup

Startup confirms the repository, task, rules, templates, and scope before work
begins.

Repository Re-anchor is a mid-work and pre-output candidate. It is used when
the AI may drift from the current repository version during artifact
generation.

Repository Re-anchor is not a second Startup and does not reset the task.

## When To Consider Re-anchor

Use or propose Repository Re-anchor when:

- a long Q, ADR, roadmap, completion report, or template-based artifact is
  being generated;
- the task spans many files or many steps;
- the AI is relying on a remembered template rather than a current file;
- a previous completion report showed missing template sections;
- the user reports that the output does not match the repository standard;
- a new chat is continuing work from earlier repository context;
- canonical sources have changed recently.

## Minimum Re-anchor Targets

Choose only sources relevant to the current output.

- Current Q file.
- AI Repository Index.
- Current template.
- Relevant rule.
- Relevant workflow.
- Current roadmap or architecture document.
- Current request artifact or completion report, when revising.

## Output Evidence

When Repository Re-anchor is used, record a short evidence block in the
completion report or final response:

```text
Repository Re-anchor:
- Trigger:
- Sources re-checked:
- Drift risk found:
- Output adjusted:
- Remaining limitation:
```

## Promotion Conditions

This candidate may be promoted after:

- repeated repository drift examples are recorded;
- Q, ADR, roadmap, completion report, and template work show cross-artifact
  value;
- Human Review confirms that the practice reduces missing sections,
  stale-template output, or repository mismatch;
- the additional review cost is acceptable.

## Guardrails

- Do not treat Repository Re-anchor as automatic enforcement.
- Do not create background repository reads without task relevance.
- Do not replace Startup or Pre-Response Verification Gate.
- Do not use Re-anchor as permission to expand scope.
- Do not auto-update files, generate Qs, or commit changes without explicit
  approval.

## Expected Review Decisions

- REGISTERED_AS_FUTURE_CANDIDATE.
- NEEDS_MORE_EVIDENCE.
- REJECTED.

## Related Documents

- `docs/workflow/ai_startup_procedure.md`
- `docs/workflow/startup_checklist_workflow.md`
- `docs/workflow/startup_completion_evidence.md`
- `docs/workflow/startup_completion_gate.md`
- `docs/workflow/pre_response_verification_gate.md`
- `templates/completion_report_template.md`
- `templates/Q_TEMPLATE.md`
