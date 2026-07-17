# Result And Reason Code Mapping

## Result Mapping

| Startup Result | Common Meaning | Draft Generation | Repository Mutation | Required Evidence |
| --- | --- | --- | --- | --- |
| `PASS` | Proceed. | Allowed. | Not authorized. | All required checks resolved. |
| `PASS_WITH_LIMITATION` | Proceed with explicit limitation. | Allowed with visible limitation. | Not authorized. | Limitation, risk, and next action. |
| `BLOCK` | Stop. | Not allowed. | Not authorized. | Failed check, blocking reason, recovery action. |
| `SCW_REQUIRED` | Stop / Call / Wait. | Not allowed until resolved. | Not authorized. | Unknown issue, human question, blocked action, required answer. |

No Startup result authorizes commit, push, tag, release, deletion, canonical promotion, external publication, or repository mutation by itself.

## Reason Code Policy

- Use uppercase snake case.
- Keep codes stable and machine-readable.
- Put the primary decision reason first.
- Add blocking or limitation reason next.
- Add supporting check reasons after the primary reason.
- Unknown codes must never be treated as `PASS`.
- Deprecated codes should remain readable in historical reports.

## Positive / Success Codes

- `INTENT_CLASSIFIED`
- `WORKFLOW_RESOLVED`
- `KNOWLEDGE_REQUIREMENTS_RESOLVED`
- `CANONICAL_REPOSITORY_VERIFIED`
- `CANONICAL_TEMPLATE_VERIFIED`
- `REVISION_FIRST_DECIDED`
- `CONSTRAINT_CHECK_PASSED`
- `GENERATION_GATE_PASSED`

## Limitation Codes

- `NON_BLOCKING_SOURCE_MISSING`
- `RAW_FRESHNESS_LIMITED`
- `HUMAN_REVIEW_RECOMMENDED`
- `RELATED_ARTIFACT_LIMITED`
- `REPORT_INDEX_PENDING`

## Blocking Codes

- `INTENT_AMBIGUOUS`
- `WORKFLOW_UNRESOLVED`
- `KNOWLEDGE_REQUIRED_BUT_MISSING`
- `REPOSITORY_NOT_VERIFIED`
- `TEMPLATE_NOT_VERIFIED`
- `TEMPLATE_MISMATCH`
- `DUPLICATE_OR_REVISION_CONFLICT`
- `CONSTRAINT_FAILED`
- `HUMAN_APPROVAL_REQUIRED`
- `SCW_REQUIRED`

## SCW Codes

- `SCOPE_UNCLEAR`
- `TARGET_PROJECT_UNCLEAR`
- `CONFLICTING_INSTRUCTIONS`
- `CANONICAL_SOURCE_CONFLICT`
- `REVISION_OR_NEW_ARTIFACT_UNCLEAR`
- `APPROVAL_BOUNDARY_UNCLEAR`

## Result Examples

| Situation | Result | Reason Codes |
| --- | --- | --- |
| Canonical template, workflow, repository, and constraints are all resolved. | `PASS` | `INTENT_CLASSIFIED`, `WORKFLOW_RESOLVED`, `CANONICAL_TEMPLATE_VERIFIED`, `GENERATION_GATE_PASSED` |
| Local repository is verified but public Raw freshness was not needed or could not be confirmed. | `PASS_WITH_LIMITATION` | `CANONICAL_REPOSITORY_VERIFIED`, `RAW_FRESHNESS_LIMITED`, `GENERATION_GATE_PASSED` |
| Template path is unknown. | `BLOCK` | `TEMPLATE_NOT_VERIFIED` |
| User request conflicts with existing artifact revision policy. | `SCW_REQUIRED` | `DUPLICATE_OR_REVISION_CONFLICT`, `REVISION_OR_NEW_ARTIFACT_UNCLEAR`, `SCW_REQUIRED` |
