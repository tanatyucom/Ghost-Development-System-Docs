# Workflow Recommendation Validation Cases

## Covered Cases

1. Normal Commit Approval Request
   - Expected: `Current Step: Approval Request`, `Commit: Recommended`,
     `Push: Hold`, `Tag: Hold`.
2. Human Approves Commit
   - Expected: `Current Step: Execution Instruction`, `Commit: Approved`.
   - Duplicate approval question is prohibited.
3. Human Approval Without Pending Request
   - Expected: no unit becomes `Approved`; clarification or SCW is required.
4. Commit Approved, Push Not Approved
   - Expected: `Commit: Approved`, `Push: Hold`, `Tag: Hold`.
5. Commit Completed, Push Recommendation
   - Expected: `Commit: Completed`, `Push: Recommended`, `Tag: Hold`.
   - `Completed` requires valid Execution Evidence.
6. Repository Recommendation Hold
   - Expected: Workflow Recommendation uses `Hold`.
   - ChatGPT does not override without new evidence.
7. Stale Repository Recommendation
   - Expected: no approval request; state becomes `Hold` or `Stop`.
8. Mixed Scope
   - Expected: `Commit: Hold`, SCW, no optimistic approval request.
9. Incorrect Audience Wording
   - Expected: human-facing instruction, not direct ChatGPT-to-Codex wording.
10. Duplicate Approval Prompt
    - Expected: Human approval transitions directly to Execution Instruction.
11. Tag Independence
    - Expected: `Tag: Recommended` remains separately approvable.
12. Encoding Display False Positive
    - Expected: use `Get-Content -LiteralPath <path> -Encoding UTF8` before
      reporting corruption.

## Example Source

Full examples are stored in:

```text
examples/workflow_recommendation_examples.md
```
