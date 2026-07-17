# GDS-QUALITY-002 Repository Drift Prevention and Re-anchor Workflow

## Identity

- Q ID: GDS-QUALITY-002
- Status: Draft
- Priority: High
- Category: Quality / Workflow / AI Collaboration
- Owner: GDS

## Source

- Source Q: `C:/Users/tanat/Downloads/Q-GDS-QUALITY-002_Repository_Drift_Prevention_and_Re-anchor_Workflow.md`
- Read mode: UTF-8

## Purpose

Define Repository Drift as a quality issue observed during long-term human and
AI collaboration, and register Repository Re-anchor as a Future Candidate
workflow that complements Startup rather than replacing it.

## Background

Observed pattern:

- Startup completed.
- Repository synchronized.
- Template understood.
- During artifact creation, the AI does not re-check the current template.
- Output starts from abstracted internal knowledge instead of the current
  repository source.
- The issue is reproducible in new chats and long-running work.

## Definitions

### Repository Drift

Repository Drift is the movement of the active reference center from canonical
repository files to the AI's internal summarized or abstracted understanding.

### Repository Re-anchor

Repository Re-anchor is the practice of returning to canonical repository
sources during artifact generation.

### Reference Loop

```text
Reference -> Reason -> Reference -> Reason -> Reference -> Output
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

## Roadmap Status

- Future Candidate.
- Quality Improvement.
- Complement to Startup, not a replacement.

## Deliverables

- `request.md`
- `completion_report.md`
- `docs/workflow/repository_drift_prevention.md`
- Workflow index update
- Roadmap update
- AI Repository Index update

## Out of Scope

- AI reasoning control.
- Automatic re-reference mechanism.
- SDK implementation.
- GameGhost changes.
- Commit / Push.

## Promotion Conditions

- More reproduction examples.
- Cross-check across Q, ADR, Roadmap, Completion Report, and template work.
- Human Review.

## Success Criteria

- Repository Drift is defined as a quality issue.
- Repository Re-anchor is registered as a Future Candidate.
- Responsibility boundary with Startup is clear.

## Expected Review Decision

REGISTERED_AS_FUTURE_CANDIDATE.
