# Multi-AI Handoff Checklist Template

## Purpose

Use this checklist to review a handoff artifact when work moves between
ChatGPT, Codex, Claude, Gemini, human review, or another AI-assisted execution
context.

The goal is to preserve context, protect scope, and let the next AI continue
from repository evidence instead of temporary chat memory.

For generation-to-generation or platform-readiness handoffs, also check design
intent, North Star, Vision Scenario, Approval Request lifecycle, and Experience
continuity. Use `templates/HANDOFF_TEMPLATE_V2.md` when those sections are
required.

Use `templates/multi_ai_handoff_template.md` for the handoff artifact itself.
Use this checklist to confirm the artifact is complete enough for the receiver.

## Handoff Summary

- Handoff date:
- Source AI / reviewer:
- Target AI / reviewer:
- Target project:
- Working repository:
- Related Q file:
- Related completion report:
- Current phase:
- Commit policy:

## Repository First Check

Confirm the next AI should read sources in this order:

1. Knowledge Access Index:
2. Repository documents:
3. Completion Report:
4. Chat:

Notes:

-

## Current Status

- Done:
- In progress:
- Not started:
- Blocked:
- Latest decision:

## Current Focus

- Primary focus:
- Secondary focus:
- Out of focus:
- Next expected action:

## Design Intent / Experience Continuity

- North Star preserved:
- What must not be lost:
- Intended experience preserved:
- Vision Scenario included:
- End-to-End User Journey clear:
- Approval Request lifecycle clear:
- Pending Human Approval state clear:
- BLOCK / SCW behavior clear:
- Commit approval separated from Push approval:

## Scope Protection

### Editable

- Working repository:
- Editable directories:
- Editable files:

### Reference Only

- Reference repositories:
- Reference directories:
- Reference files:

### Forbidden

- Do not edit:
- Do not commit:
- Do not run:
- Do not assume:

## Source Of Truth

- AI Repository Index:
- Rules:
- Workflow:
- Templates:
- Examples:
- Architecture:
- Project Profile:
- Q artifact:
- Completion report:

## Changed Files

- Created:
- Updated:
- Deleted:
- Intentionally not changed:

## Verification Results

- Repository Quality Audit:
- AI Repository Index generation:
- AI Repository Index validation:
- UTF-8 / mojibake check:
- `git diff --check`:
- Other verification:

## Remaining Issues

- Issue:
- Impact:
- Owner:
- Recommended next action:

## Recommended Next Q

- Suggested Q title:
- Purpose:
- Scope:
- Out of scope:
- Priority:

## Handoff Message

Use this short message when passing work to another AI or reviewer.

```text
Current Status:

Current Focus:

Scope:

Source of Truth:

Changed Files:

Verification Results:

Remaining Issues:

Recommended Next Q:
```

## Completion Report Linkage

- Completion report updated with handoff summary:
- Handoff checklist stored as artifact:
- Handoff checklist path:
- Next AI entry point:

## Review

- Summary is clear:
- Verification is visible:
- North Star is visible:
- Intended experience is recoverable:
- Human Approval boundary is recoverable:
- Remaining issues are explicit:
- Next action is explicit:
- Scope boundaries are explicit:
- Repository First order is explicit:
- Another AI can continue without chat memory:

## Related Documents

- `docs/rules/ai_collaboration_rules.md`
- `templates/multi_ai_handoff_template.md`
- `templates/HANDOFF_TEMPLATE_V2.md`
- `templates/VISION_SCENARIO_TEMPLATE.md`
- `docs/philosophy/north_star.md`
- `docs/architecture/experience_layer.md`
- `docs/rules/core_principles.md`
- `docs/ai_repository_index.md`
- `templates/completion_report_template.md`
- `templates/daily_operation_checklist_template.md`
- `examples/persistent_collaboration_examples.md`
