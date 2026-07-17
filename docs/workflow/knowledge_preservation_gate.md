# Knowledge Preservation Gate

**Status:** Draft Workflow

**Last Updated:** 2026-07-17

## Purpose

Knowledge Preservation Gate helps AI and humans decide when a Q, review,
completion report, or design conversation should produce additional durable
knowledge such as an Issa draft, ADR candidate, Improvement Record candidate,
Architecture Principle candidate, or child Q.

It does not automatically promote artifacts, approve ADRs, create canonical
Issa storage, commit, push, or tag.

## Standard Flow

```text
Q / Review / Completion / Design Conversation
  -> Knowledge Preservation Check
  -> Artifact Responsibility Classification
  -> Issa Recommendation, when reasoning value is high
  -> ADR Candidate Check, when architecture decision exists
  -> Improvement Record Candidate, when operational evidence exists
  -> Human Review
  -> Draft / Candidate Artifact
  -> AI Repository Index Update Gate, when public knowledge changed
```

## Knowledge Preservation Check

Use this check during Q creation, Q revision, architecture review, completion
review, and major design conversation capture.

```yaml
knowledge_preservation_check:
  problem_definition_changed: false
  multiple_hypotheses_evaluated: false
  reusable_reasoning_found: false
  architecture_decision_found: false
  future_reconstruction_value: low
  q_alone_loses_why: false
  cross_workflow_or_cross_repository_impact: false
```

## Issa Recommendation

Recommend an Issa draft when one or more of these are true:

- problem definition changed materially;
- multiple hypotheses, experiments, or rejected paths led to the result;
- reusable reasoning or decomposition was discovered;
- an architecture or design principle emerged;
- a general failure pattern and improvement method was found;
- Q alone would preserve what changed but lose why;
- the discussion became a turning point for multiple child Qs.

Classification:

| Result | Meaning |
| --- | --- |
| `not_needed` | Routine task; no special reasoning preservation needed. |
| `recommended` | Reasoning has reuse value; draft can be useful. |
| `required_candidate` | Future reconstruction risk is high; Human Review should decide preservation. |
| `scw_required` | Canonical storage, template, authority, or overlap is unclear. |

Reason codes:

- `PROBLEM_DEFINITION_CHANGED`
- `MULTIPLE_HYPOTHESES_EVALUATED`
- `REUSABLE_REASONING_FOUND`
- `ARCHITECTURE_PRINCIPLE_FOUND`
- `Q_ALONE_LOSES_WHY`
- `FUTURE_RECONSTRUCTION_VALUE_HIGH`
- `MULTI_Q_TURNING_POINT`
- `CANONICAL_ISSA_STORAGE_UNCLEAR`

## ADR Candidate Check

Use this check when a design choice may affect architecture, ownership,
compatibility, safety, Human Approval boundaries, or cross-project workflow.

```yaml
adr_candidate_check:
  multiple_viable_options: false
  long_term_architecture_impact: false
  cross_repository_impact: false
  future_explanation_required: false
  compatibility_or_safety_boundary: false
  human_approval_boundary_decided: false
```

ADR candidate is true when the decision needs durable explanation beyond a Q
or Completion Report.

ADR Status rules:

- Proposed ADR can be drafted for review.
- Accepted / Superseded / Deprecated requires Human Approval.
- ADR does not approve runtime implementation, migration, SDK completion,
  commit, push, tag, or release.

## Over-generation Guard

Do not create extra artifacts for:

- small wording fixes;
- simple file moves;
- routine template fill;
- repeated known procedure with no new reasoning;
- implementation details already captured in a Completion Report;
- ideas already captured in an existing canonical artifact.

Prefer revising an existing authoritative document over creating a competing
one.

## Human Approval Boundary

The gate may recommend:

- Issa draft;
- ADR candidate;
- Improvement Record candidate;
- Architecture Principle candidate;
- child Q;
- SCW.

The gate must not automatically:

- promote a draft to canonical status;
- mark ADR Accepted;
- create new canonical Issa storage;
- change roadmap priority;
- commit, push, tag, release, or publish.

## Related Documents

- `docs/architecture/knowledge_artifact_responsibility_map.md`
- `docs/adr/README.md`
- `docs/workflow/architecture_promotion_lifecycle.md`
- `docs/workflow/completion_report_workflow.md`
- `docs/workflow/conversation_insight_capture_workflow.md`
- `docs/architecture/intent_driven_workflow.md`
