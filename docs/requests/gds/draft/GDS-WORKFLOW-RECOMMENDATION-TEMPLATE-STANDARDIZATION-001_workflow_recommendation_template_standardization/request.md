# Q_GDS_WORKFLOW_RECOMMENDATION_TEMPLATE_STANDARDIZATION_001

## Title

Workflow Recommendation Template Standardization

## Request ID

GDS-WORKFLOW-RECOMMENDATION-TEMPLATE-STANDARDIZATION-001

## Type

Revision / Template Standardization

## Objective

Standardize the Workflow Recommendation produced by ChatGPT after Completion
Review.

The template must convert a Codex Repository Recommendation and review evidence
into a concise, responsibility-safe, human-facing recommendation.

## Core Principle

Workflow Recommendation is ChatGPT's human-facing recommendation after
Completion Review.

It is not:

- Codex Repository Recommendation;
- Human Final Approval;
- Execution Instruction after approval;
- repository action execution;
- Execution Evidence.

Workflow Recommendation may function as the single Approval Request when it
visibly contains all Approval Units requiring Human judgment.

Once the human approves that Workflow Recommendation, ChatGPT must not ask for
the same approval again.

## Required Work

- Review existing Workflow Recommendation, Completion Review, Repository
  Recommendation, Approval Request, Execution Instruction, and verification
  assets.
- Define one canonical Workflow Recommendation template.
- Preserve state vocabulary ownership across Repository Recommendation,
  Workflow Recommendation, and Execution Instruction.
- Make `Current Step` explicit.
- Keep Commit, Push, and Tag independent.
- Document mapping from Codex Repository Recommendation to ChatGPT Workflow
  Recommendation.
- Add Audience verification.
- Document abnormal paths with Hold / Stop / SCW.
- Include UTF-8-aware PowerShell reading guidance.

## Required Validation Cases

- Normal Commit Approval Request.
- Human Approves Commit.
- Human Approval Without Pending Request.
- Commit Approved, Push Not Approved.
- Commit Completed, Push Recommendation.
- Repository Recommendation Hold.
- Stale Repository Recommendation.
- Mixed Scope.
- Incorrect Audience Wording.
- Duplicate Approval Prompt.
- Tag Independence.
- Encoding Display False Positive.

## Constraints

- Repository First.
- Revision First.
- Evidence First.
- Human Approval First.
- Single Source of Truth.
- SCW: Stop / Call / Wait.
- No guessing under ambiguity.
- No duplicate Approval Request.
- No direct ChatGPT-to-Codex control assumption.
- No Commit.
- No Push.
- No Tag.
- No GameGhost modification.

## UTF-8 Read Requirement

When reading Japanese Markdown or Q files in PowerShell, use:

```powershell
Get-Content -LiteralPath <path> -Encoding UTF8
```

Do not treat mojibake from default `Get-Content` as evidence of file
corruption.
