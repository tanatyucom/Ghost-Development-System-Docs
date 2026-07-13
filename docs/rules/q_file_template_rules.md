# Q File Template Rules

**Version:** 1.0

**Last Updated:** 2026-07-13

## Purpose

This rule defines the mandatory fields for GDS Q files so repository context,
edit scope, commit policy, validation, deliverables, AI Repository Index gate,
and Safe Commit Set are explicit before AI work begins.

## Required Sections

Every official Q should include these sections or mark them `Not Applicable`.

## Identity

Required fields:

```text
Q ID:
Title:
Version:
Status:
Priority:
Category:
Created Date:
Last Updated Date:
Owner / Target AI:
```

## Repository Context

Required fields:

```text
Working Repository:
Working Directory:
Preferred Shell:
Target Project:
Non-Target Project:
Allowed Edit Scope:
Forbidden Edit Scope:
```

Example:

```text
Working Repository: Ghost-Development-System-Docs
Working Directory: C:\GitHub\Ghost-Development-System-Docs
Preferred Shell: Git Bash
Target Project: GDS only
Non-Target Project: GameGhost
Allowed Edit Scope: GDS documentation only
Forbidden Edit Scope: GameGhost, runtime DB, production data
```

## Commit / Push Policy

Commit and Push policy must be explicit.

Allowed values:

```text
Commit: Do not execute
Commit: Execute only after explicit approval
Commit: Required after Commit OK

Push: Do not execute
Push: Execute only after explicit approval
Push: Required after Commit
```

Default:

```text
Commit: Do not execute
Push: Do not execute
```

## Purpose / Background / Scope / Out of Scope

Every Q must clearly separate:

- Purpose.
- Background.
- Scope.
- Out of Scope.

Out of Scope is a safety boundary, not optional narration.

## Existing Knowledge / Dependencies

Record related knowledge when applicable:

- Related Rules.
- Related Architecture.
- Related Workflow.
- Related Template.
- Related Conversation Insight.
- Related Pending Insight.
- Related Future Candidate.
- Related Q.
- Related Completion Report.

Use `Not Applicable` when no related artifact exists.

If a Q is created from a Pending Insight, record:

- Pending Insight ID.
- Human Review decision.
- Why Q creation was selected.
- Codex execution restriction cleared by Human Approval.
- Pending cleanup expectation.

## Deliverables

Separate required and optional deliverables.

Standard required candidates:

- `request.md`.
- `notes.md`.
- `completion_report.md`.
- affected Rule / Workflow / Architecture / Template.
- README / index updates.
- AI Repository Index.
- Repository Quality Report.

If a candidate does not apply, write `Not Applicable`.

## Validation

Validation should be repository-specific and executable.

GDS Docs default candidates:

```powershell
cd C:\GitHub\Ghost-Development-System-Docs
python scripts/generate_ai_repository_index.py --write
python scripts/generate_ai_repository_index.py --validate
python scripts/repository_quality_audit.py
git diff --check
git status --short
```

Adjust paths and commands for the target repository.

## AI Repository Index Update Gate

Every Q must include:

```text
AI Repository Index Update Gate: Yes / No / Review Required
```

If `Yes`, specify:

- Expected indexed files.
- Index regeneration command.
- Index validation command.
- Representative Raw URL verification, when public access changed.

If `No`, explain why the changed files are not public knowledge entry points.

If `Review Required`, explain what must be checked before deciding.

## Completion Report Requirements

Minimum completion report sections:

- Changed Files.
- Summary.
- Verification.
- Improvement Review.
- Beginner & Future Self Test result, when durable documentation, roadmap,
  decision, handoff, review, or index artifacts are created or updated.
- Recommended Improvements.
- Future Candidates.
- Remaining Issues.
- Recommended Next Q.
- Safe Commit Set.
- Suggested Commit Message.
- Commit Status.
- GameGhost Edit Status, when applicable.

## Safe Commit Set

Completion reports must list an explicit Safe Commit Set.

Check candidates:

- `request.md`.
- `notes.md`.
- `completion_report.md`.
- `addendum_*.md`.
- reports.
- README / index files.
- new files.
- modified files.

The Safe Commit Set must match Changed Files or explain exclusions.

## Review Decision

After completion, return one of:

```text
Commit OK
Revision Recommended
Minor Recommendation
```

This does not permit committing unless the Q Commit Policy or user explicitly
allows it.

## Poka-Yoke Rules

- Do not start implementation until Working Repository and Working Directory
  are explicit.
- Do not edit a Non-Target Project unless the Q explicitly allows it.
- Do not commit or push when the Q omits Commit / Push Policy.
- Do not treat chat text as the authoritative Q when an artifact is required.
- Do not update AI Repository Index silently; follow the gate.
- Do not omit Safe Commit Set from the completion report.
- Do not leave hidden chat context as the only explanation for purpose,
  current position, evidence, or next action.
