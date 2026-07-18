# Knowledge Candidate Classification Contract

**Status:** Draft Contract

**Last Updated:** 2026-07-18

## Purpose

This contract defines the minimum fields, candidate types, evidence
requirements, duplicate checks, approval boundaries, and reason codes used by
the Knowledge Promotion Engine.

It is documentation-only and does not implement a detector or classifier.

## Candidate Record

```yaml
candidate_id: KPC-YYYYMMDD-NNN
candidate_type: workflow_candidate
statement: concise reusable knowledge statement
origin:
  source_q:
  source_completion_report:
  source_repository:
  source_files: []
evidence:
  - type:
    path:
    summary:
related_artifacts: []
proposed_canonical_target:
confidence: low | medium | high
classification_result: revision_preferred | future_candidate | evidence_only | new_candidate_review_required | reject
blocking_state: none | scw_required
duplicate_status: unchecked | no_duplicate_found | duplicate_possible | duplicate_confirmed
required_approval:
  draft_creation: true
  canonical_promotion: true
  repository_mutation: true
recommended_next_action: revise_existing | carry_forward | attach_evidence | create_draft | create_child_q | reject | scw
reason_codes: []
blocking_reasons: []
application_targets: []
status: detected | classified | recommended | pending_approval | carried_forward | draft_created | promoted | rejected | archived | blocked
```

## Classification Result Taxonomy

`classification_result` records the classification decision. It does not record
the next action, approval state, duplicate state, or execution state.

| Result | Meaning | Typical Next Action |
| --- | --- | --- |
| `revision_preferred` | Existing canonical artifact should be revised instead of creating a new artifact. | `revise_existing` |
| `future_candidate` | The idea is valid but not mature enough for canonical promotion now. | `carry_forward` or `create_draft` |
| `evidence_only` | The material should remain as supporting evidence, not a promoted knowledge item. | `attach_evidence` |
| `new_candidate_review_required` | No suitable existing artifact is known, but human review is required before creating a new draft. | `create_draft` or `create_child_q` after approval |
| `reject` | The candidate should not be promoted or carried forward. | `reject` |

`revision_preferred` is the default preferred result when an existing canonical
artifact can absorb the knowledge without creating a parallel artifact.

## Blocking State

`blocking_state` records whether classification can continue.

| State | Meaning | Required Behavior |
| --- | --- | --- |
| `none` | No blocking condition is active. | Continue with the recommended next action after required approval. |
| `scw_required` | Source, canonical target, approval, or repository state is ambiguous enough to require Stop / Clarify / Wait. | Stop and emit SCW output before repository mutation. |

`blocking_state` is separate from `classification_result`. A candidate can have
a likely classification result and still require SCW before any repository
change.

## Responsibility Separation

The classification fields have separate responsibilities:

- `classification_result` says what the candidate is.
- `blocking_state` says whether action must stop.
- `duplicate_status` says whether an existing artifact or candidate may already cover it.
- `recommended_next_action` says what should happen next.
- `status` says where the candidate is in the lifecycle.

Do not use `recommended_next_action` as a substitute for classification.
Do not use `classification_result` as execution approval.

## Candidate Types

| Type | Meaning | Typical Target |
| --- | --- | --- |
| `adr_candidate` | Durable architecture decision may be needed. | `docs/adr/` |
| `issa_candidate` | Reasoning / discovery path needs preservation. | Draft attachment until canonical Issa standard exists. |
| `improvement_record_candidate` | Operational improvement lifecycle should be preserved. | PIP / future Improvement Record standard. |
| `rule_candidate` | Mandatory behavior or prohibition may be needed. | `docs/rules/` |
| `architecture_principle_candidate` | Broad design philosophy or boundary may guide future work. | `docs/architecture/` or `docs/rules/core_principles.md` |
| `workflow_candidate` | Repeated sequence should become visible and reviewable. | `docs/workflow/` |
| `template_candidate` | Repeated artifact structure should become reusable. | `templates/` |
| `example_candidate` | Good / bad examples would prevent future ambiguity. | `examples/` |
| `ghost_research_candidate` | External OSS, framework, architecture, or engineering-practice learning should be preserved and evaluated before candidate extraction. | `docs/research/` |
| `checklist_candidate` | Repeated review items should become checkable. | `templates/` or `docs/workflow/` |
| `intent_registry_candidate` | Intent routing may need registry update. | Intent Registry / related architecture. |
| `quality_gate_candidate` | Validation or completion gate may need update. | workflow / rules / templates. |
| `capability_registry_candidate` | Capability knowledge should feed future repository intelligence. | Capability Registry candidate. |
| `data_contract_candidate` | Artifact or data shape needs a contract. | architecture / schema / template. |
| `child_q_candidate` | Implementation or revision work requires a future Q. | `queue/` or request attachment. |

## Evidence Requirements

A candidate must include at least one concrete source:

- Q acceptance criteria.
- Completion Report.
- Changed file.
- Validation result.
- Review finding.
- Explicit user decision.
- SCW event.
- Repeated friction.
- Repository architecture change.

Candidates without evidence are suggestions, not promotion candidates.

## Duplicate And Canonical Source Check

Before creating a new artifact, check:

- `docs/ai_repository_index.md`;
- related canonical directory;
- existing ADRs;
- existing Rules;
- existing Workflows;
- existing Templates;
- existing Knowledge Inventory;
- existing Conversation Insights;
- active and planned Q files.

Preferred outcomes:

1. revise existing canonical artifact;
2. link to existing artifact;
3. attach to active or related Q;
4. create Draft;
5. create child Q.

These outcomes should be represented through `classification_result` and
`recommended_next_action`, not by overloading `duplicate_status`.

Example:

```yaml
classification_result: revision_preferred
duplicate_status: no_duplicate_found
recommended_next_action: revise_existing
```

If a near-duplicate exists but the canonical owner is unclear, use:

```yaml
classification_result: revision_preferred
blocking_state: scw_required
duplicate_status: duplicate_possible
recommended_next_action: scw
```

## Approval Boundary

The following require Human Approval:

- canonical promotion;
- ADR status change to Accepted / Superseded / Deprecated;
- canonical Rule / Workflow / Template update;
- creation of a new canonical artifact class;
- repository mutation;
- commit / push / tag / release;
- cross-repository change.

## Positive Reason Codes

- `KNOWLEDGE_CANDIDATE_DETECTED`
- `CLASSIFICATION_RESULT_ASSIGNED`
- `BLOCKING_STATE_CONFIRMED`
- `PROMOTION_TARGET_IDENTIFIED`
- `CANONICAL_SOURCE_CONFIRMED`
- `EXISTING_ARTIFACT_REVISION_PREFERRED`
- `NEW_DRAFT_REQUIRED`
- `KNOWLEDGE_CARRY_FORWARD_SELECTED`
- `HUMAN_APPROVAL_RECEIVED`
- `PROMOTION_VALIDATION_PASSED`
- `LINEAGE_UPDATED`
- `APPLICATION_TARGET_DEFINED`

## Blocking Reason Codes

- `CANDIDATE_TYPE_AMBIGUOUS`
- `CANONICAL_SOURCE_UNREADABLE`
- `CANONICAL_OWNER_UNKNOWN`
- `DUPLICATE_ARTIFACT_POSSIBLE`
- `PROMOTION_TARGET_AMBIGUOUS`
- `NO_PENDING_ACTION`
- `MULTIPLE_PENDING_ACTIONS`
- `REPOSITORY_STATE_CHANGED`
- `HUMAN_APPROVAL_REQUIRED`
- `TEMPLATE_NOT_FOUND`
- `LIFECYCLE_UNDEFINED`
- `LINEAGE_TARGET_UNKNOWN`
- `VALIDATION_NOT_RUN`
- `VALIDATION_FAILED`
- `CROSS_REPOSITORY_SCOPE_UNAPPROVED`
- `SCW_REQUIRED`

## SCW Output

```text
SCW:
- Candidate:
- Stop reason:
- Missing or conflicting canonical source:
- Last safe state:
- Required human decision:
- Actions not performed:
```
