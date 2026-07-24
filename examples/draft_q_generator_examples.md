# Draft Q Generator Scenario Matrix

| # | Scenario | Result |
| --- | --- | --- |
| 1 | Complete enriched candidate + Active Verified GDS. | Draft Ready; provenance attached. |
| 2 | Implementation repository missing. | Incomplete; blocking input, no inference. |
| 3 | Runtime/language missing. | Review Required when human choice is needed. |
| 4 | Multiple repositories support the role. | PROMPT with minimal safe options. |
| 5 | Planned repository selected. | Incomplete; authority NONE and activation required. |
| 6 | Active repository freshness Stale. | Mutation target blocked until Verified. |
| 7 | Inherited root conflicts with Registry. | Invalidate root and SCW. |
| 8 | Fresh Handover supplies state/goal. | Inherit with provenance. |
| 9 | Completion Report supplies Safe Commit Set reference. | Inherit reference, not current approval. |
| 10 | Path separators differ uniquely. | AUTO-correct and record. |
| 11 | Explicit current Human Decision conflicts with candidate. | Human Decision wins; record supersession. |
| 12 | Approval Scope missing. | Incomplete; cannot be Approved. |
| 13 | Mutation Authority missing. | Incomplete; execution NONE. |
| 14 | Optional notes missing. | Draft Ready with warning. |
| 15 | Draft reviewed and approved. | Status may become Approved; Startup still required. |
| 16 | Source artifact superseded. | Invalidate dependent fields and re-resolve. |
| 17 | Duplicate Repository ID. | SCW; no selection. |
| 18 | Proposed question already answered by Registry/Completion. | Suppress question; reuse and cite evidence. |

## Planned Repository Output

```text
Repository Assignment: UNKNOWN / Planned
Execution Authority: NONE
Missing Input: Activation and explicit repository approval
```

## Blocking Draft Envelope

```text
Status: Draft
Draft Status: Incomplete
Approval Status: NOT APPROVED
Startup: NOT PERMITTED
Mutation: NOT PERMITTED
```
