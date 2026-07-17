# ADR-GDS-005 Context Reconstruction and Knowledge-Guided Recommendations

**Status:** Accepted

**Date:** 2026-07-17

## Context

Intent-Driven Workflow introduced a front-door architecture where user intent
is routed through repository and conversation state review before workflow
selection, recommendation, pending action, approval, or SCW.

During that design work, a broader decision emerged:

GDS should not rely on humans or AI remembering prior commands, rationale,
workflow names, or safety boundaries. It should preserve enough knowledge in
the repository for future users, beginners, future selves, and new AI sessions
to reconstruct context safely.

Existing principles already support this direction:

- Context Recovery Principle.
- Knowledge Poka-Yoke / Design For Forgetfulness.
- Beginner & Future Self Test.
- Repository First.
- Knowledge Before Automation.
- Human Approval Gate.

This ADR candidate records the combined decision boundary so it can be reviewed
as one architecture decision rather than scattered across chat history.

## Decision

Proposed:

GDS should prioritize repository-based context reconstruction and
knowledge-guided recommendations over command memorization and direct action.

When a user expresses intent, GDS should:

1. read canonical knowledge;
2. review repository and conversation state;
3. explain the recommendation with evidence and reason codes;
4. create a Pending Action only when the operation is specific and reviewable;
5. require Human Approval before mutating actions;
6. preserve significant reasoning as Issa draft, ADR candidate, Improvement
   Record candidate, Architecture Principle, or child Q when needed.

This decision treats beginners and future selves as first-class users.

## Alternatives Considered

### Command-Driven Operation

Users memorize formal commands such as Startup, Q Creation Gate, Completion
Checklist, Commit Gate, Push Gate, and Tag Gate.

Rejected as the primary model because it increases cognitive load and fails
when users return after long gaps.

### Direct Natural Language Execution

Natural language such as `お願いします` or `OK` directly triggers execution.

Rejected because it bypasses scope, repository state, Pending Action, and Human
Approval boundaries.

### Intent-Driven Recommendation Without Knowledge Preservation

Intent Engine routes workflows but does not preserve why decisions were made.

Rejected as incomplete because it would recreate the same context-loss problem
at a higher level.

## Consequences

Positive:

- Users can resume safely without remembering every GDS term.
- AI recommendations become explainable and evidence-backed.
- Important reasoning is less likely to be lost in chat.
- Beginner guidance becomes a core design goal, not an accidental benefit.
- Intent-Driven Workflow remains safer because recommendation and action are
  separated.

Costs:

- More artifact classification work during Q creation and completion.
- Risk of over-generating drafts if the Knowledge Preservation Gate is not
  scoped.
- Issa storage still needs a canonical standard.

## Approval Boundary

This ADR is Proposed only.

Acceptance requires Human Approval. Acceptance would not approve runtime Intent
Engine implementation, LLM classifier implementation, Git automation, canonical
Issa storage, commit, push, tag, release, or cross-repository changes.

## Related Documents

- `docs/architecture/intent_driven_workflow.md`
- `docs/architecture/intent_registry_and_pending_action_contract.md`
- `docs/architecture/knowledge_artifact_responsibility_map.md`
- `docs/workflow/knowledge_preservation_gate.md`
- `docs/rules/core_principles.md`
- `docs/architecture/design_philosophy.md`
- `docs/workflow/architecture_promotion_lifecycle.md`
- `docs/requests/gds/draft/GDS-KNOWLEDGE-001_revolution_aftermath_knowledge_preservation/request.md`
