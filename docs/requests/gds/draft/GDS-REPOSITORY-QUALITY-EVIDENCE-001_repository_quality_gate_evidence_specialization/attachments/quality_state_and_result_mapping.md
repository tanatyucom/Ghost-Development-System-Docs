# Quality State And Result Mapping

## Principle

Quality State and Gate Result are related but not identical.

```text
Quality State = repository condition
Gate Result = next action decision
```

## Mapping Table

| Quality State | Condition | Default Gate Result | Human Approval | SCW |
| --- | --- | --- | --- | --- |
| `Green` | Required checks pass with no warnings or errors in scope. | `PASS` | Normal boundary remains. | No by default. |
| `Yellow` | No blocking error, but warning or limitation exists. | `PASS_WITH_LIMITATION` | May be required to accept known warning. | Maybe, if warning ownership or safety is unclear. |
| `Red` | Error or blocking check failure exists. | `BLOCK` | Cannot silently override critical failure. | Maybe, if repair ownership or evidence conflict is unclear. |
| `Unknown` | Evidence missing, stale, partial, conflicting, or audit failed. | `SCW_REQUIRED` or `BLOCK` | Required for decision. | Yes when uncertainty is decision-dependent. |

## Precedence

1. Critical failure overrides aggregate state and produces `BLOCK`.
2. Evidence conflict produces `SCW_REQUIRED`.
3. Stale evidence cannot be used as current evidence.
4. Partial scope cannot authorize broader claims.
5. Missing evidence is never treated as PASS.
6. Green does not authorize commit, push, tag, release, deletion, or promotion by itself.

## Exception Mapping

| Case | Quality State | Gate Result | Reason |
| --- | --- | --- | --- |
| Whole repository Green, commit not approved. | `Green` | `PASS` for quality; commit still blocked by approval boundary. | Quality and approval are separate. |
| Documentation-only scope has one accepted warning. | `Yellow` | `PASS_WITH_LIMITATION` | Work may continue with visible limitation. |
| Required generated index is stale. | `Red` or `Unknown` | `BLOCK` or `SCW_REQUIRED` | Depends whether stale condition is known or conflicting. |
| Report says Green but raw output shows failure. | `Unknown` | `SCW_REQUIRED` | Conflict must be resolved. |
| Audit tool crashes. | `Unknown` | `BLOCK` for required gate; `SCW_REQUIRED` if environment decision is needed. | No reliable assessment exists. |

## Freshness Behavior

Freshness values:

- `fresh`
- `stale`
- `invalid`
- `unknown`

Evidence is stale when repository revision, working tree, staged diff, quality rules, check catalog, audit tool, generated artifacts, canonical templates, or scan scope changed after the assessment.

## Human Override Behavior

Human Approval may accept known non-critical warnings for a scoped action.

Human Approval must not silently override:

- failed critical check;
- missing required evidence;
- stale evidence for commit recommendation;
- target revision mismatch;
- report/raw output conflict.
