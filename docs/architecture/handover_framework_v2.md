# Handover Framework v2

**Status:** Adopted Architecture
**Version:** 2.0
**Effective Date:** 2026-07-24

## Purpose

Handover Framework v2 changes handover from Result Transfer into Design Context
Transfer. A receiver must be able to reconstruct not only what was decided, but
why it was chosen, what was rejected, which assumptions remain, and where the
next session must enter without inventing a new interpretation.

## Continuity Quality

Continuity Quality is the degree to which a later session can recover the same
design intent, vocabulary, boundaries, decisions, and uncertainty from durable
repository evidence.

```text
Execution Quality -> correct work inside one execution
Continuity Quality -> consistent understanding across sessions
```

Neither quality substitutes for the other.

## Mandatory Handover Sections

Every authoritative cross-session handover contains:

1. Current State.
2. Session Goal.
3. Decision Summary.
4. Decision History.
5. Rejected Options and Reason for Rejection.
6. Architecture Intent.
7. Current Risks.
8. Open Questions.
9. Blocked Items.
10. Assumptions.
11. Terminology.
12. Context Contract.
13. Next Session Entry Point.

Use `Not Applicable` rather than silently omitting a section.

## Architecture

```text
Canonical Repository Evidence
  -> Context Contract
  -> Decision History
  -> Project State
  -> Session Summary
  -> Handover Artifact
  -> Receiver Reconstruction Check
  -> Continue / SCW
```

The handover is a derived navigation and continuity artifact. It does not
replace Q files, ADRs, repository state, approval evidence, or canonical
standards. Conflicts resolve in favor of those canonical sources or use SCW.

## Receiver Reconstruction Gate

Before continuing, the receiver must be able to state:

- the current goal and state;
- the active design intent;
- why the latest material decisions were made;
- rejected options and their rejection conditions;
- fixed terminology and repository roles;
- assumptions and freshness;
- risks, blockers, open questions, and exact entry point.

If any item materially affects execution and cannot be reconstructed, the
handover result is `SCW_REQUIRED`.

## Lifecycle

```text
Session Work
  -> Material Decision / State Change
  -> Update Decision History And Project State
  -> Generate Session Summary
  -> Assemble Handover
  -> Validate Mandatory Sections And Sources
  -> Receiver Reconstruction
  -> Accepted / Partial / SCW_REQUIRED
```

## Boundaries

- Do not preserve private chain-of-thought. Preserve concise decision rationale,
  evidence, constraints, alternatives, and consequences.
- Do not turn assumptions into facts.
- Do not carry expired approvals into a new repository state.
- Do not copy secrets, credentials, or unrelated private state.
- Do not make a summary a new canonical source when an owned source exists.

## Related Documents

- `templates/HANDOFF_TEMPLATE_V2.md`
- `docs/standards/decision_history_standard.md`
- `docs/standards/handover_context_contract.md`
- `docs/standards/project_state_standard.md`
- `docs/standards/session_summary_standard.md`
- `docs/workflow/generation_handoff_workflow.md`
- `docs/adr/ADR-GDS-011_continuity_quality_and_design_context_handover.md`
