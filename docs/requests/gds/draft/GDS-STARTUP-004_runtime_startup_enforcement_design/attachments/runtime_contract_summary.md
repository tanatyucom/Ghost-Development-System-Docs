# Runtime Startup Enforcement Contract Summary

## Runtime Flow

```text
User / Command Center / Template Engine
  -> Artifact Request
  -> Runtime Startup Enforcement
  -> Evidence Record
  -> Gate Decision
  -> Artifact Generation / Pending Action / Stop
```

## State Machine

```text
IDLE
  -> REQUEST_RECEIVED
  -> INTENT_CLASSIFIED
  -> WORKFLOW_RESOLVED
  -> KNOWLEDGE_RESOLVED
  -> REPOSITORY_VERIFIED
  -> TEMPLATE_VERIFIED
  -> REVISION_DECIDED
  -> CONSTRAINT_CHECKED
  -> GATE_DECIDED
  -> COMPLETED
```

Stop states:

```text
BLOCKED
SCW_WAITING
AWAITING_HUMAN_DECISION
```

## Gate Values

| Gate | Meaning | Artifact Generation |
| --- | --- | --- |
| `PASS` | Required checks completed. | Allowed. |
| `PASS_WITH_LIMITATION` | Limitation and next action recorded. | Allowed with visible limitation. |
| `BLOCK` | Required check failed or constraint violated. | Not allowed. |
| `SCW_REQUIRED` | Stop, Call, Wait for human decision. | Not allowed. |

## Evidence Record

```yaml
startup_execution_id:
source_request:
artifact_intent:
required_workflow:
required_knowledge:
repository_verification:
template_verification:
revision_first_decision:
constraint_check:
gate_decision:
gate_reason_codes:
missing_or_conflicting_evidence:
scw_reason:
human_approval_required:
pending_action:
allowed_next_step:
created_at:
```

## Command Center Contract

Command Center may call Runtime Startup Enforcement before Template Engine or
Artifact Pipeline prepares a draft. It must display `BLOCK` and `SCW_REQUIRED`
as stop states and show limitations before proceeding on `PASS_WITH_LIMITATION`.
