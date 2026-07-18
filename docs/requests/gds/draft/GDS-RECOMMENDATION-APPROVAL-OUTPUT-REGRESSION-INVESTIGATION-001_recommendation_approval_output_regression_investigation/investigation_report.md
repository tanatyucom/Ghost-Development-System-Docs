# Recommendation / Approval Output Regression Investigation

## Executive Summary

Result: confirmed regression / output-contract bypass.

The latest Ghost Research completion produced:

- a Completion Report artifact;
- a visible Codex chat summary;
- a suggested commit message;
- a successful commit after later human approval.

However, neither the Completion Report nor the visible Codex final response
contained the current canonical Repository Recommendation block required by
`templates/repository_recommendation_template.md` and referenced by
`templates/completion_report_template.md`.

Correction:

The previous investigation incorrectly assigned Workflow Recommendation and
Approval Request ownership to ChatGPT. Under the corrected GDS responsibility
model, Codex is the Git execution actor and must display Repository
Recommendation, Workflow Recommendation, Approval Request, repository
validation, execution, and Execution Evidence.

ChatGPT remains responsible for Completion Review, Independent Review,
Architecture / Design Review, and Execution Guidance.

Primary root cause:

- Completion Report Template Invocation / Routing Defect.
- Manual Summary Bypass.
- Verification Coverage / Execution Gap.

Severity: High.

Reason: Commit approval safety was not broken at runtime in the observed case
because the human explicitly asked to commit later, but the standardized
Codex-facing approval surface was incomplete. This weakens Commit / Push / Tag
independence and makes Human Approval less visible before execution.

## Triggering Evidence

### Observed Chat Output

The visible Codex final response after Ghost Research work contained:

- Changed Files.
- Summary.
- Verification.
- Remaining Issues / Future Candidates.
- Recommended Next Q.
- Suggested Commit Message.

It did not visibly include:

```text
Repository Recommendation

Approval Units:
- Commit: Recommended
- Push: Hold
- Tag: Hold
```

It also did not include a Workflow Recommendation / Approval Request block.

### Ghost Research Completion Report

File:

```text
docs/requests/gds/draft/GDS-GHOST-RESEARCH-KNOWLEDGE-ASSET-STANDARDIZATION-001_ghost_research_knowledge_asset_standardization/completion_report.md
```

Observed section:

```text
## Repository Recommendation

Recommended for commit after human review.

Commit / Push / Tag were not executed.
```

This is not the canonical Repository Recommendation block. It omits repository,
branch, request, completion status, repository quality, scope review,
repository state, remote state, safe commit set, validation summary, approval
units, reasons, warnings, remaining issues, and review boundary.

## Canonical Responsibility Map

| Layer | Owner | Evidence |
| --- | --- | --- |
| Repository Recommendation | Codex | Corrected responsibility model from `GDS-CANONICAL-RESPONSIBILITY-APPROVAL-REQUEST-CORRECTION-001`. |
| Workflow Recommendation | Codex | Codex is the Git execution actor and displays the next repository operation recommendation. |
| Approval Request | Codex | Approval Request is displayed by the execution actor before Commit / Push / Tag. |
| Repository Validation | Codex | Codex verifies repository state, safe commit set, and validation evidence. |
| Completion Review | ChatGPT | ChatGPT performs independent review, not Git execution approval request display. |
| Independent / Architecture Review | ChatGPT | ChatGPT may review design, architecture, and completion evidence. |
| Execution Guidance | ChatGPT | ChatGPT may guide the human after review, but does not execute Git operations. |
| Human Final Approval | Human | Human approves visible Codex Approval Request units. |
| Governed Execution | Codex / Adapter after approval | Codex executes only approved repository operations. |
| Execution Evidence | Codex / Adapter | Codex records evidence for executed operations. |

## Expected-vs-Actual Matrix

| Output Element | Expected Owner | Expected Location | Required? | Actual Location | Result |
| --- | --- | --- | --- | --- | --- |
| Completion Review | ChatGPT | ChatGPT independent review layer | Not required from Codex | Not present | Correctly absent from Codex output. |
| Repository Recommendation | Codex | Completion Report and/or chat-facing handoff | Required when recommending commit / push / tag | Informal one-line note in Completion Report; absent in chat | Defect. |
| Workflow Recommendation | Codex | Codex completion output before Human Approval | Required when Codex proposes repository operation next step | Not present | Defect. |
| Current Step | Codex Workflow Recommendation | Workflow Recommendation / Approval Request block | Required when asking or preparing for approval | Not present | Defect. |
| Approval Units | Codex | Repository Recommendation, Workflow Recommendation, and Approval Request blocks | Required before Human Approval | Missing in Ghost Research Completion Report and chat response | Defect. |
| Human Approval Request | Codex | Codex-displayed Approval Request | Required before Commit / Push / Tag approval | Not present | Defect. |
| Suggested Commit Message | Codex | Completion Report and chat summary | Required by Q / Completion Report pattern | Present | PASS. |
| Execution Instruction | Codex after Human Final Approval | Post-approval execution handoff / action confirmation | Not applicable before approval | Not present | Correctly absent before approval. |
| Execution Evidence Requirement | Codex | Approval Request / Execution Evidence output | Required once execution is requested or performed | Not present in final summary | Coverage gap before execution; required after execution. |

## Asset Inspection Results

### Repository Recommendation Template

File:

```text
templates/repository_recommendation_template.md
```

Findings:

- Defines Repository Recommendation as Codex-produced.
- Defines it as evidence-backed handoff to ChatGPT.
- Requires `Approval Units`.
- Prohibits `Approved`.
- Requires `Review Boundary: ChatGPT Completion Review / Workflow Recommendation required.`

### Completion Report Template

File:

```text
templates/completion_report_template.md
```

Findings:

- Contains a dedicated `## Repository Recommendation` section.
- Explicitly says to use `templates/repository_recommendation_template.md`.
- Lists required fields including Approval Units.

### Workflow Recommendation Template

File:

```text
templates/workflow_recommendation_template.md
```

Findings:

- Previously interpreted as ChatGPT-produced after Completion Review.
- Corrected responsibility model assigns repository-operation Workflow
  Recommendation to Codex because Codex is the Git execution actor.
- The template remains useful structurally, but ownership language requires a
  future canonical documentation correction.

### Approval Request Rules

File:

```text
docs/rules/approval_request_rules.md
```

Findings:

- Codex provides Repository Recommendation, Workflow Recommendation, Approval
  Request, repository validation, execution, and Execution Evidence.
- ChatGPT provides Completion Review, Independent Review, Architecture /
  Design Review, and Execution Guidance.
- Human remains final approval authority.
- Repository Recommendation must not ask the human for approval.
- Missing required recommendation should trigger SCW or re-display of the
  Approval Request.

### Approval Runtime State Machine

File:

```text
docs/architecture/approval_runtime_state_machine.md
```

Findings:

- Was previously read as assigning Workflow Recommendation / Approval Request
  to ChatGPT.
- Corrected responsibility model supersedes that reading for Git execution
  operations: Approval Request is displayed by Codex, the execution actor.
- Separates recommendation, approval, execution, and evidence.

### Pre-Response Verification Gate

File:

```text
docs/workflow/pre_response_verification_gate.md
```

Findings:

- Checks Human Approval boundary and Commit / Push boundary.
- Checks Workflow Recommendation state when Workflow Recommendation is shown.
- Does not explicitly require that every Codex final response include a
  canonical Repository Recommendation block when commit is recommended.

### AI Response Checklist

File:

```text
templates/ai_response_checklist_v2.md
```

Findings:

- Contains checks for Repository Recommendation values and Safe Commit Set.
- The checklist is not embedded into the observed Completion Report.
- No evidence shows it was executed before the final chat response.

### Response Verification Checklist

File:

```text
templates/response_verification_checklist.md
```

Findings:

- Contains Repository Recommendation boundary, values, and Safe Commit Set
  evidence fields.
- It is a template, not an enforced gate.

### Recent Revision Comparison

Files / commits inspected:

- `c3e76d4 docs: standardize repository recommendation template`
- `98cea8e docs: standardize workflow recommendation template`
- `a812a1a docs: define approval runtime state machine`
- `3344ff2 docs: standardize ghost research knowledge asset`

Findings:

- Repository Recommendation and Workflow Recommendation standards exist.
- The later Approval Runtime and Ghost Research completion reports contain a
  simplified `Repository Recommendation` section rather than the canonical
  block.
- The regression includes both output invocation / manual summary failure and a
  responsibility-map error in this investigation artifact.

## Root Cause

### Confirmed Cause

`Completion Report Template Invocation / Routing Defect`

The Ghost Research Completion Report did not instantiate the canonical
Repository Recommendation block even though the template requires it.

`Manual Summary Bypass`

The final chat response summarized key sections and included Suggested Commit
Message, but did not carry forward the canonical Repository Recommendation
handoff block.

### Contributing Factor

`Verification Coverage / Execution Gap`

Verification assets contain Repository Recommendation checks, but the observed
Completion Report and final chat response do not show evidence that those
checks were executed or that missing Approval Units blocked output.

### Not Confirmed

`Canonical Documentation Conflict`

The previous report said no conflict was found. This is corrected: the report's
responsibility assignment was wrong for the current GDS operating model.
Codex owns Repository Recommendation, Workflow Recommendation, Approval
Request, repository validation, execution, and Execution Evidence for Git
operations.

`Approval Runtime Failure`

No evidence shows a runtime state transition failure. The issue is output and
artifact contract compliance.

## Impact And Severity

Severity: High.

Impact:

- Affects at least the Ghost Research completion and the immediately preceding
  Approval Runtime completion report pattern.
- Primarily affects completion artifacts and chat-facing output.
- Does not prove Approval Runtime state transition failure.
- Does not prove execution evidence binding failure.
- Does increase risk that Commit, Push, and Tag independence is not visible to
  the human before approval.
- Suggested Commit Message alone is insufficient as Repository Recommendation.

Commit approval safety in the observed case was partially preserved by later
explicit human approval and actual commit evidence, but the governed handoff
was incomplete.

## Reproduction Results

### Case 1: Work Complete, Commit Recommended, Push / Tag Hold

Static reproduction from `examples/repository_recommendation_examples.md`
shows the expected block includes:

```text
Approval Units:
- Commit: Recommended
- Push: Hold
- Tag: Hold
```

Observed Ghost Research Completion Report omitted the Approval Units.

Result: reproduced as artifact-output regression.

### Case 2: Work Complete But Repository Recommendation Hold

Canonical examples define Commit / Push / Tag all as `Hold` when validation or
scope is insufficient.

Observed output did not provide any Approval Unit states, so ChatGPT cannot
distinguish Recommended from Hold using the formal contract.

Result: coverage gap confirmed.

### Case 3: Human Approval Already Granted; Execution Instruction Expected

Corrected responsibility model assigns Git execution-facing Approval Request
and execution handling to Codex.

The Ghost Research final response occurred before explicit commit approval.
Therefore Execution Instruction was not expected before Human Approval, but a
Codex-owned Approval Request was expected.

Result: no defect for missing Execution Instruction before approval; defect
confirmed for missing Approval Request surface.

### Case 4: Chat-Facing Summary Generated From Completion Report

The Completion Report itself lacked the canonical Repository Recommendation
block. Therefore a chat summary derived from that report could not faithfully
carry the full block unless the final response regenerated it independently.

Result: source artifact omission plus chat-output omission.

## SCW Decision

SCW is not required for this correction because the current Q explicitly
supplies the corrected responsibility model:

```text
Codex -> Repository Recommendation / Workflow Recommendation / Approval Request / Repository Validation / Execution / Execution Evidence
ChatGPT -> Completion Review / Independent Review / Execution Guidance
Human -> Final Approval
```

SCW is recommended before any remediation implementation because this Q is
investigation-only and the next change should decide where enforcement belongs.

## Recommended Remediation Q

Recommended next Q:

```text
GDS-RECOMMENDATION-OUTPUT-CONTRACT-ENFORCEMENT-001
```

Purpose:

Revise Completion Report / Pre-Response Verification / AI Response Checklist
invocation so Codex completion artifacts and final chat responses must include
the canonical Repository Recommendation, Codex-owned Workflow Recommendation,
and Approval Request surface whenever Commit / Push / Tag is being recommended,
and must fail or SCW when Approval Units are absent.

This next Q should also align canonical templates and architecture text with
the corrected responsibility model while preserving ChatGPT's independent
review and guidance role.

## Remaining Unknowns

- Whether every future Codex final response should include the full canonical
  Repository Recommendation / Workflow Recommendation / Approval Request block
  inline, or may link to a Completion Report containing it.
- Whether a compact chat-facing Repository Recommendation block is acceptable
  if the Completion Report contains the full block.
- Whether automated validation should parse Completion Reports for Approval
  Units.
- Whether Pre-Response Verification should require a visible gate result in
  every Completion Report.

## Repository Recommendation

Repository:
Ghost-Development-System-Docs

Branch:
main

Request / Q:
GDS-RECOMMENDATION-APPROVAL-OUTPUT-REGRESSION-INVESTIGATION-001

Completion Status:
PASS

Repository Quality:
Green

Scope Review:
Clean

Repository State:
Dirty

Remote State:
unknown

Safe Commit Set:
- `docs/requests/gds/draft/GDS-RECOMMENDATION-APPROVAL-OUTPUT-REGRESSION-INVESTIGATION-001_recommendation_approval_output_regression_investigation/request.md`
- `docs/requests/gds/draft/GDS-RECOMMENDATION-APPROVAL-OUTPUT-REGRESSION-INVESTIGATION-001_recommendation_approval_output_regression_investigation/investigation_report.md`
- `docs/requests/gds/draft/GDS-RECOMMENDATION-APPROVAL-OUTPUT-REGRESSION-INVESTIGATION-001_recommendation_approval_output_regression_investigation/completion_report.md`
- `docs/ai_repository_index.md`
- `reports/repository_quality_report.md`

Validation Summary:
- git diff --check: PASS
- AI Repository Index: PASS
- Encoding Regression: PASS
- Repository Quality Audit: PASS

Approval Units:
- Commit: Recommended
- Push: Hold
- Tag: Hold

Reasons:
- Investigation-only documentation scope is complete.
- Safe Commit Set is limited to this request workspace, AI Repository Index,
  and Repository Quality Report.
- Required validation passed.
- This Q is investigation-only and does not authorize remediation.

Known Warnings:
- Git reported CRLF-to-LF normalization warnings for
  `docs/ai_repository_index.md` and `reports/repository_quality_report.md`.

Remaining Issues:
- Remediation remains out of scope and should be handled by the recommended
  follow-up Q.

Review Boundary:
ChatGPT Completion Review / Independent Review may follow. Human Approval is
required before Codex execution.
