# Developer Experience Quality Standard

**Version:** 1.0
**Status:** Adopted

## Quality Objective

GDS quality includes both safety and the ability to continue ordinary approved
work without redundant prompts. Friction reduction is accepted only when
authority, evidence, auditability, and repository boundaries remain intact.

## Metrics

| Metric | Definition |
| --- | --- |
| Prompt Count | Human prompts issued during one Q. |
| Manual Approval Count | Distinct approval decisions requested. |
| Repeated Question Count | Questions whose answer existed in fresh canonical evidence. |
| SCW Frequency | SCW results per executable Q. |
| SCW False Positive Rate | SCWs later resolved only by already-available evidence. |
| Context Reuse Rate | Reusable eligible fields inherited with provenance / eligible fields. |
| Follow-up Resume Success Rate | Follow-ups reaching Startup without context reconstruction / attempted follow-ups. |
| Time to GO | Approved-Q receipt to Startup GO. |
| Completion-to-Next-Q Time | Completion Review to next executable Q. |

## Friction Score

```text
+1 non-blocking prompt
+2 manual approval
+3 repeated known-context question
+4 SCW
+5 SCW caused by incomplete handover/follow-up
+5 re-entry of known repository context
```

Report raw event counts with the score so weighting does not hide causes.

## DX Quality Gate

- Repeated known-context questions: `0`.
- Enriched follow-up mandatory completeness: `100%`.
- No approval unit is silently merged or skipped.
- Every AUTO decision has evidence and remains inside authority.
- False-positive SCW and context reuse are measured, not assumed.
- Any friction reduction that weakens a safety invariant fails the gate.

Initial measurements form a baseline; they do not justify relaxing governance.
