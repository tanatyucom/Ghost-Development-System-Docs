# Roadmap Template

## Template Metadata

- Template Version:
- Last Updated:
- Author / Maintainer:
- Review Status:
- Related Q:
- Related Completion Report:

## Canonical Template Synchronization

- Startup completed: Yes / No
- AI Repository Index verified: Yes / No
- Current Mission verified: Yes / No
- Template revision verified: Yes / No
- Canonical Repository confirmed: Yes / No
- Canonical Repository path:
- Raw reference freshness confirmed when applicable: Yes / No / Not Applicable
- Raw reference URL:
- Template mismatch found:
- Template mismatch action:

## Identity

- Roadmap ID:
- Title:
- Owner:
- Canonical Repository:
- Target Project:
- Roadmap Type:
- Status:
- Priority:
- Category:

## Hierarchy Layer

Choose the Product Documentation Hierarchy layer.

- Product Blueprint
- Master Roadmap
- Domain Roadmap
- Execution Roadmap

## Roadmap Type

Choose the roadmap type that best matches the responsibility.

- GDS Platform Roadmap
- Field Project Roadmap
- Domain Roadmap
- Execution Roadmap
- Architecture Roadmap
- Governance Roadmap
- Template / Documentation Roadmap
- Future Candidate Track

## Canonical Repository

Record where the canonical roadmap is maintained.

- Canonical Repository:
- Canonical Path:
- Reference Repository:
- Related Implementation Repository:
- Cross Repository Impact:

Guidance:

- GDS-owned platform direction belongs in `Ghost-Development-System-Docs`.
- GameGhost runtime, metadata, DB, OCR, and GUI direction belongs in GameGhost
  unless explicitly promoted through a later Q.
- A roadmap can reference another repository without taking ownership of its
  implementation.

## Target Project

Record the project responsibility.

Examples:

- Ghost Development System
- GameGhost
- AnimeGhost
- ComicGhost
- Other

## Owner

- Roadmap Owner:
- Review Owner:
- Implementation Owner:
- Human Approval Owner:

## Purpose

Explain why this roadmap exists.

## Background

Describe the evidence or completed work that created the need for this roadmap.

## Scope

### In Scope

-

### Out of Scope

- Runtime implementation:
- SDK implementation:
- Provider API implementation:
- Metadata / DB write:
- Automatic promotion:
- Commit / Push:

## Product Blueprint Fields

Use when hierarchy layer is Product Blueprint.

- Vision:
- Mission:
- Product Identity:
- Principles:
- Scope In:
- Scope Out:
- Success Definition:

## Current Position

Use this section in Master Roadmap. Do not place Current Position in Product
Blueprint.

- Current Mission:
- Current Phase:
- Overall Progress:
- Current Focus:
- Next Milestone:
- Known Blockers:
- Current Owner:
- Last Updated:

## Roadmap Flow

```text
Current State
  -> Next Milestone
  -> Future Candidate
  -> Promotion Review
```

## Roadmap Items

| ID | Phase | Priority | Title | Status | Owner | Success Criteria |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

## Promotion Stage

Choose the current promotion stage.

- Idea
- Candidate
- Draft Roadmap
- Active Roadmap Track
- Validated Evidence
- Platform Candidate
- Platform Standard Candidate
- Approved Platform Standard
- Archived

## Promotion Evidence

Record the evidence required for promotion.

- Source Q:
- Completion Report:
- Validation Artifact:
- ADR:
- Architecture Review:
- Human Review:
- Cross Project Evidence:
- Field Project Evidence:
- Metrics / Quality Gate:
- Repository Index Entry:

## Promotion Criteria

Define the conditions for moving to the next stage.

- Evidence is reproducible:
- Ownership boundary is clear:
- Human Approval is recorded:
- Runtime responsibility is separated:
- Cross repository impact is reviewed:
- Validation strategy is documented:
- Remaining issues are tracked:

## Success Criteria

Define how humans and AI can tell the roadmap update succeeded.

- Discoverable from README / index:
- Canonical repository is explicit:
- Roadmap type is explicit:
- Promotion stage is explicit:
- Future candidates are marked as future:
- Out of scope is explicit:
- Next Q is recommended:

## Architecture Impact

Record whether this roadmap changes architecture direction.

- Architecture Impact: None / Reference / Direction / Candidate / Standard
- Related Architecture:
- Related ADR:
- Affected Pattern:
- Responsibility Boundary:
- Center / Engine / Registry / Adapter / Contract Impact:

## Dependencies

- Required prior Q:
- Required completion report:
- Required ADR:
- Required architecture review:
- Required validation artifact:
- Related roadmap:
- Related rule / workflow:
- External dependency:

## Validation Strategy

Describe how the roadmap update will be verified.

- AI Repository Index update:
- README / docs README route:
- Roadmap index route:
- Template consistency:
- Mojibake marker search:
- `git diff --check`:
- Repository quality check:
- Human review required:

## Responsibility Separation

Separate GDS responsibility from field project responsibility.

Ownership rule:

- Common reusable assets: GDS
- Platform direction: GDS
- Architecture decision: GDS when cross-project
- Domain adapters and domain rules: project owner such as GameGhost
- Runtime implementation: field project unless separately promoted

## Cross Project Impact

Recommended values:

- None
- Reference Only
- Documentation Impact
- Runtime Impact
- Requires Separate Q

## Standard Management Axes

- Phase:
- Priority:
- Dependency:
- Status:
- Ownership:
- Promotion:
- Trigger:
- Exit Criteria:
- Risk:
- Success Metric:
- Why:
- Evidence:

## Status Lifecycle

Allowed values:

- Research
- Planned
- In Progress
- Operational Complete
- Improvement Required

Operational Complete means current operational needs are met.
Improvement Required should be used only when new evidence or changed
requirements require follow-up.

## Guardrails

- This roadmap does not approve runtime implementation by itself.
- This roadmap does not approve SDK extraction by itself.
- This roadmap does not approve provider API integration by itself.
- This roadmap does not approve automatic promotion by itself.
- This roadmap does not replace Human Approval.

## Current Focus Handoff

- Current Focus:
- Next Milestone:
- Recommended Next Q:
- Stop Conditions:
- Resume Notes:

## Future Expansion

- Future Candidate:
- Trigger:
- Required Evidence:
- Promotion Boundary:

## Related Documents

- Related Specification:
- Related Decision Record:
- Related Architecture:
- Related Rule:
- Related Workflow:
- Related Completion Report:
- Related Roadmap:

## Completion Report Linkage

After execution, the completion report should record:

- Implementation Results:
- Verification:
- Evidence:
- Lessons Learned:
- Promotion Candidates:
- Remaining Issues:
- Recommended Next Work:
