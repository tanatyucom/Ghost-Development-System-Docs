# Command Center Working Context Model

**Status:** Architecture Candidate

**Last Updated:** 2026-07-18

## Purpose

This document defines Working Context as the generated operational view used by
Command Center.

Working Context helps humans and AI understand what is happening now, what is
blocked, what has been approved, and what should be considered next. It is not a
new source of truth and must not duplicate repository state as an independent
canonical asset.

## Core Decision

Working Context should become a derived operational model.

```text
Repository
  -> Repository Context Evidence
  -> Working Context
  -> Command Center presentation / recommendation
  -> Human Approval
```

Repository remains the Single Source of Truth. Repository Context Evidence
records what was checked. Working Context summarizes that evidence into a
reviewable current operating view.

## Model Definition

Working Context is:

- generated from repository state and evidence;
- scoped to the current session, task, mission, or review window;
- refreshable when relevant source state changes;
- human-readable and AI-readable;
- advisory until Human Approval turns a recommendation into an approved action.

Working Context is not:

- canonical project state;
- a replacement for AI Repository Index;
- a replacement for Startup Completion Evidence;
- a replacement for Repository Context Evidence;
- an approval record;
- an execution instruction;
- a durable project asset by default.

## Recommended Contents

Working Context may include:

| Field | Meaning | Canonical Source |
| --- | --- | --- |
| Current Priority | Current top-level priority being considered. | Roadmap, Current Mission, Human decision. |
| Current Focus | Immediate working focus inside the current priority. | Q file, Completion Report, Current Mission. |
| Current Mission | Active mission or platform direction. | Roadmap, Information Package, Project Profile. |
| Active Q | Current request artifact and scope. | Q artifact. |
| Repository Health | Current repository quality / validation state. | Repository Quality Report and validation evidence. |
| Approval Status | Whether an action is pending, approved, rejected, or deferred. | Approval Request / Pending Action evidence. |
| Completion Review Status | Whether the latest work is complete, needs revision, or requires review. | Completion Report / Completion Review Evidence. |
| Deferred Items | Known deferred work that should not be lost. | Completion reports, roadmap, pending decision artifacts. |
| Blocking Issues | Current blockers, SCW states, missing evidence, or quality gates. | Startup, quality, approval, and completion evidence. |
| Recommended Next Action | Advisory next step with evidence paths. | Decision Engine / Command Center recommendation. |

## Excluded Contents

Working Context must not contain:

- unverifiable memory-only claims as facts;
- hidden approvals;
- broad or implicit permission to execute;
- generated priority changes presented as approved decisions;
- raw secrets, credentials, tokens, or private runtime state;
- unrelated repository state outside the approved scope;
- implementation diffs as if they were accepted architecture;
- stale source summaries without freshness status;
- field-project runtime state unless explicitly in scope.

## Refresh Model

Working Context should be refreshed when:

- Startup completes;
- Repository Context Evidence changes;
- repository files relevant to the task change;
- AI Repository Index is regenerated or validated;
- Repository Quality state changes;
- Completion Review completes;
- Approval state changes;
- Current Mission changes;
- Active Q changes;
- a blocker or SCW state is resolved.

Refresh behavior:

```text
Trigger
  -> identify affected canonical sources
  -> reread evidence / repository sources
  -> rebuild Working Context
  -> mark freshness and limitations
  -> present changes for review
```

If Working Context cannot be refreshed from evidence, Command Center must label
it as stale, partial, or blocked instead of treating it as current.

## Lifecycle Proposal

Recommended lifecycle:

```text
Not Generated
  -> Generated
  -> Presented
  -> Reviewed
  -> Used For Recommendation
  -> Refreshed / Superseded
  -> Discarded or Archived As Evidence
```

Working Context should normally be temporary. It may be stored only when a
specific workflow needs auditability, handoff, review, or later reconstruction.

When stored, the artifact must declare:

- source repository and revision;
- source evidence paths;
- generation time;
- refresh trigger;
- freshness status;
- limitations;
- approval status;
- supersession relationship, when applicable.

Stored Working Context remains evidence or handoff material. It does not become
the canonical source for project state.

## Responsibility Boundaries

| Component | Owns | Does Not Own |
| --- | --- | --- |
| Repository | Canonical documents, code, reports, and durable evidence. | Derived operational summary. |
| Repository Context Evidence | What was checked, when, from which source, with what result. | Project priority or approval. |
| Working Context | Current operational view derived from evidence. | Canonical truth or approval. |
| Command Center | Presentation, recommendation, refresh routing, handoff support. | Source-of-truth ownership or autonomous action. |
| Human Approval | Scope, priority decision, approval, rejection, risk acceptance. | Mechanical context aggregation. |
| Codex / Execution Adapter | Approved execution and evidence production. | Working Context authority or priority ownership. |

## Working Context Versus Repository Context Evidence

Repository Context Evidence answers:

```text
What did the AI/system check, from where, and with what result?
```

Working Context answers:

```text
Given that evidence, what is the current operating picture?
```

Repository Context Evidence should be preserved as evidence. Working Context
should be regenerated from it when needed.

## Storage Policy

Working Context should not always be stored.

Default:

- generate temporarily during Startup, Command Center review, or handoff;
- present summary and evidence links;
- discard or supersede after the session or after source state changes.

Store only when:

- a handoff package needs it;
- a Completion Review needs to preserve the operating state used for a decision;
- a Human Approval packet needs a visible context snapshot;
- a future Command Center runtime requires auditable context reconstruction.

Do not store when:

- it only repeats repository documents;
- no decision, handoff, or review depends on it;
- it would become stale immediately;
- it would encourage treating summary as canonical truth.

## Review Question Answers

Should Working Context always be generated?

- No. It should be generated when Command Center, Startup, handoff, approval, or
  completion review needs a current operational view.

Should it ever be stored?

- Yes, but only as evidence, handoff, or review support. Stored Working Context
  is not canonical project state.

Should it only exist temporarily?

- By default, yes. Persistent storage is an exception for auditability or
  handoff.

What belongs in Working Context versus Repository Context Evidence?

- Working Context contains the interpreted operational summary. Repository
  Context Evidence contains source checks, paths, timestamps, and validation
  facts.

What should never appear in Working Context?

- Hidden approval, secrets, unverifiable memory claims, unauthorized scope,
  stale facts without freshness labels, or execution commands.

## Phase Recommendation

Phase 1:

- Define the model and boundaries.
- Use Working Context manually in architecture reviews and completion reports.
- Allow Command Center to display a generated, evidence-backed summary.
- Do not implement runtime generation, storage, scoring, queue execution, or UI.

Future phases:

- Add a Working Context package template.
- Define a machine-readable context snapshot format.
- Connect Repository Intelligence signals.
- Add freshness validation.
- Add Command Center UI presentation.
- Add priority scoring only as advisory and approval-gated.

## Guardrails

- No implementation is approved by this document.
- No new repository state is required by this document.
- No Startup, Bootstrap, or Approval workflow behavior is modified by this
  document.
- Command Center may consume Working Context, but must not use it to bypass
  Human Approval.
- Conflicts between Working Context and repository sources must be resolved in
  favor of repository sources or routed to SCW.

## Related Documents

- `docs/architecture/command_center_architecture.md`
- `docs/architecture/platform_execution_evidence_contract.md`
- `docs/architecture/runtime_startup_enforcement.md`
- `docs/architecture/repository_quality_gate_evidence_specialization.md`
- `docs/architecture/completion_review_execution_evidence_specialization.md`
- `templates/completion_report_template.md`
- `roadmap/ghost_development_system_roadmap.md`
