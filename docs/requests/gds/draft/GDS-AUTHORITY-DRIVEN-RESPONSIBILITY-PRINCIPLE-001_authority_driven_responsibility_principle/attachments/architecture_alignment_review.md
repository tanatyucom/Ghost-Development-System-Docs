# Architecture Alignment Review

## Scope

This review checks whether current GDS responsibility assets align with
Authority-Driven Responsibility Principle.

## Reviewed Areas

| Area | Reviewed Asset | Result | Notes |
| --- | --- | --- | --- |
| Responsibility Layer | `docs/architecture/responsibility_boundary.md` | Updated | Added authority-first assignment guidance and SCW boundary. |
| Approval Request | `docs/rules/approval_request_rules.md` | Already aligned / reinforced | Previous correction already moved Codex-owned Approval Request into rule. |
| Approval / Intent / Evidence | `docs/architecture/approval_request_intent_queue_execution_evidence.md` | Updated | Replaced stale ChatGPT-owned Workflow Recommendation wording with Codex-owned Approval Request path. |
| Workflow Recommendation | `templates/workflow_recommendation_template.md` | Already aligned | Prior output contract enforcement made Codex final output owner explicit. |
| Repository Recommendation | `templates/repository_recommendation_template.md` | Already aligned | Codex recommendation remains evidence-backed and non-approval. |
| Intent Engine | `docs/architecture/intent_driven_workflow.md` | No direct edit | Existing design separates intent, Human Approval, action, and SCW. |
| Repository Intelligence | `docs/architecture/repository_intelligence_dashboard_foundation.md` | No direct edit | Current foundation is read-only and does not own mutation. |
| Automation / Runtime | `docs/architecture/governed_execution_adapter_foundation.md` | Updated | Added explicit link to authority-driven assignment before routing execution. |
| Ghost SDK / Actor / Adapter | `docs/architecture/gds_core_ai_actor_adapter_boundary.md` | Updated | Clarified that AI may create Approval Requests only when it is the execution-capable actor or governed delegate. |
| Capability / Tool Boundary | `templates/review_checklist.md` | Updated | Added authority / responsibility alignment checks. |

## Findings

- The most important stale wording was in
  `docs/architecture/approval_request_intent_queue_execution_evidence.md`.
- The current rules already separate Human Approval, recommendation, execution,
  and evidence.
- The new principle makes the reason reusable beyond Approval Request.

## Remaining Risk

Future architecture documents may still use feature-name ownership language.
Apply `docs/rules/responsibility_assignment_rules.md` during future design
review before promoting such documents.
