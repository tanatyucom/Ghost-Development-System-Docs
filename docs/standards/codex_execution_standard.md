# Codex Execution Standard

**Version:** 1.1

**Status:** Adopted

**Effective Date:** 2026-07-23

## Purpose

This standard defines the repository-governed execution contract for Codex and
other AI executors working from a Q file. It consolidates the common execution,
safety, evidence, completion, and approval rules that every executable Q must
preserve.

## Scope

This standard applies to Q creation, Startup, repository investigation,
documentation or implementation work, validation, Completion Review, and
recommendations for later repository actions.

It does not grant authority to commit, push, tag, merge, release, perform a
destructive action, or make a major canonical Notion update.

## Roles And Sources Of Truth

- The Q file is the current Execution Contract and owns task-specific purpose,
  scope, constraints, validation, and approval state.
- Repository documents are the Formal Source of Truth for durable GDS rules,
  standards, architecture, ADRs, workflows, and templates.
- Notion is a Knowledge Hub for navigation, design incubation, discussion, and
  Knowledge Promotion candidates. It is not the formal implementation source.
- Human reviewers own final approval for governed actions.
- Codex may investigate, edit within approved scope, validate, review, and
  recommend. Capability does not imply authority.

## Canonical Knowledge Priority

When sources conflict, use this order:

1. The current Q file.
2. Formal repository documents.
3. Accepted ADRs, rules, standards, and architecture.
4. Supplemental Notion knowledge.
5. Unpromoted conversation or research notes.

If a Q materially conflicts with an accepted ADR or Architecture Freeze, do
not silently override either source. Use SCW.

## Required Execution Rules

### Architecture First

Read applicable architecture, ADRs, responsibility boundaries, and Architecture
Freeze decisions before editing. If the task requires an unapproved design
change, stop and request Human Review instead of creating a de facto decision.

### One Q = One Responsibility

Each Q has one primary responsibility. A separate responsibility discovered
during execution becomes a Follow-up Q Candidate unless the current Q explicitly
includes it.

### No Hidden Refactoring

Do not add unrelated refactoring, renaming, movement, formatting, or structural
change. If such work becomes necessary, report the reason and affected scope
and obtain approval before proceeding.

### No Unauthorized Platform Promotion

Do not promote a Platform Candidate, Future Candidate, or Reusable Candidate
into GDS Core or Platform without explicit governed approval. Similarity or
possible reuse is evidence, not promotion authority.

### Optional Package Preservation

Optional candidates such as Archive Foundation, OCR Foundation, Local
Intelligence Gateway, and Repository Intelligence must remain selectable and
bounded. Do not embed them into Core or distribute them to every generated
project through a large template.

Templates own selection and initialization. Packages own implementation,
schema, migration, adapters, and bounded capability behavior.

### Thin Template Principle

Keep templates thin. A template may declare, select, connect, configure, and
initialize capabilities. It must not copy capability implementations or impose
unused dependencies and maintenance obligations on every generated project.

### Cleanup Is Not Extraction

A Cleanup Q may delete, organize, classify, and make safe placement
improvements. Movement into GDS, package creation, Platform Extraction, or
responsibility redesign requires a separate Q.

### Migration Manifest

When moving or renaming files or transferring responsibility, record:

- Before.
- After.
- Reason.
- Whether responsibility changes.
- Compatibility impact.

### Capability Verification First

Before execution begins, the AI executor must verify and report:

- Repository.
- Branch.
- Workspace Status.
- Available Tools.
- Repository Search Capability.
- GitHub Access.
- Notion Access.
- External Knowledge Access.
- Write Permission.
- Approval Required Operations.
- Protected Scope.

Verification must distinguish technical capability from execution authority.
For example, an available GitHub or Notion write tool does not authorize its
use when the Q prohibits writes or requires Human Approval.

The result must be emitted as a Startup Capability Report before implementation
or documentation editing begins. The report includes:

- Capability Verification Result: `PASS`, `PASS_WITH_LIMITATION`, or
  `SCW_REQUIRED`.
- Verified repository, branch, and workspace state.
- Available and unavailable required capabilities.
- Access and permission limitations.
- Approval-required operations.
- Protected scope.
- Safe Next Action.

Never claim or assume an unavailable capability.

#### Verification Failure Rule

If a required capability, access path, permission, repository identity, or
workspace state cannot be verified, use SCW:

```text
Stop
  -> Call
  -> Wait
```

Do not begin implementation by guessing. Report the missing or conflicting
evidence, affected scope, recommended decision, and safe next action, then wait
for the required Human Decision or capability restoration.

### Evidence Before Completion

Completion requires evidence from validation, changed-file review, repository
state, and required generated artifacts. Editing alone is not proof of
completion.

## External Knowledge Independence

An executable Q must remain safe and reproducible when Notion, Google Drive,
Slack, or another external service is unavailable. External knowledge may
support research and identify promotion candidates, but must not be the only
source required to execute the Q.

At minimum, an executable Q records:

- background and purpose;
- scope and out of scope;
- formal repository references;
- constraints and forbidden actions;
- execution order and validation method;
- completion criteria and Completion Review format;
- Commit, Push, and Tag approval state.

Knowledge required for durable execution must be promoted into repository
documentation before the Q depends on it.

## Knowledge Promotion

Use the following lifecycle:

```text
Conversation / Research
  -> Notion Draft / Knowledge Candidate
  -> Review
  -> Repository Docs / ADR / Standard
  -> Q Template / Execution Rule
```

Do not treat unpromoted knowledge as an adopted specification.

## SCW — Stop / Call / Wait

Use SCW instead of guessing when any of these conditions exists:

- architecture or formal documents conflict;
- scope contains mixed responsibilities;
- a destructive change is required;
- the canonical source cannot be identified;
- responsibility would change without approval;
- safe validation is unavailable;
- a major gap prevents the Completion Criteria from being satisfied.

An SCW report includes:

- Stop Reason.
- Evidence.
- Affected Scope.
- Recommended Decision.
- Safe Next Action.

Do not perform the blocked change until the required Human Decision is received.

## Completion Review Contract

Every Q ends with a Completion Review that includes:

- Summary.
- Changed Files.
- Unchanged / Protected Scope.
- Validation / Tests.
- Repository Status.
- Risks.
- Follow-up Candidates.
- Completion Judgment.
- Commit Recommendation.
- Approval Request or explicit Approval State.

The judgment is `PASS`, `PASS WITH FOLLOW-UP`, or `SCW-BLOCKED`. A PASS is
completion evidence, not execution authority.

## Human Approval Contract

The following actions require explicit Human Approval bound to the latest
unexecuted Approval Request:

- Commit.
- Push.
- Tag.
- Merge.
- Release.
- Destructive change.
- Major update to a canonical Notion page.

A generic acknowledgement applies only to the concrete, immediately preceding
Approval Request. Approval expires when the scope, changed files, validation,
safe commit set, repository state, or Q policy changes.

## Q Execution Lifecycle

```text
Q Intake
  -> Capability Verification And Startup Capability Report
  -> Startup And Canonical Discovery
  -> Scope And Architecture Check
  -> Execute The Single Responsibility
  -> Validate And Review Evidence
  -> Completion Review
  -> Human Approval, when requested
  -> Separately Authorized Action Execution
```

## Q Contract Requirements

The canonical Q template is `templates/Q_TEMPLATE.md`. A Q may add stricter
task-specific constraints but must not silently weaken this standard. Every Q
must explicitly state its external knowledge independence, canonical knowledge
priority, scope boundaries, forbidden actions, completion criteria, Completion
Review contract, and Human Approval state.

## Related Documents

- `templates/Q_TEMPLATE.md`
- `docs/rules/q_file_artifact_standard.md`
- `docs/rules/q_file_template_rules.md`
- `docs/workflow/q_file_creation_workflow.md`
- `docs/workflow/ai_startup_procedure.md`
- `docs/rules/approval_request_rules.md`
- `docs/architecture/completion_review_execution_evidence_specialization.md`
- `docs/adr/ADR-GDS-003_canonical_knowledge_ownership_and_local_artifact_governance.md`
