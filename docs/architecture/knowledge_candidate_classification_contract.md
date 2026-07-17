# Knowledge Candidate Classification Contract

**Status:** Draft Contract

**Last Updated:** 2026-07-17

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
duplicate_status: unchecked | no_duplicate_found | revision_preferred | duplicate_possible | duplicate_confirmed
required_approval:
  draft_creation: true
  canonical_promotion: true
  repository_mutation: true
recommended_next_action: carry_forward | revise_existing | create_draft | create_child_q | scw
reason_codes: []
blocking_reasons: []
application_targets: []
status: detected | recommended | pending_approval | carried_forward | draft_created | promoted | rejected | archived | scw
```

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
