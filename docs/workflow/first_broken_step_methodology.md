# First Broken Step Methodology

## Purpose

First Broken Step Methodology defines a reusable GDS debugging method for
finding where a pipeline first becomes wrong.

This methodology is not OCR-specific. It can be used for Import, API, Parser,
Database, UI, AI Pipeline, recommendation, classification, review, and other
multi-step development workflows.

The goal is not immediate improvement. The goal is root cause.

## Standard Methodology

```text
Confirm the Symptom
  -> Reproduce the Issue
  -> Collect Evidence
  -> Trace the Entire Pipeline
  -> Identify the First Broken Step
  -> Confirm the Root Cause
  -> Apply the Fix
  -> Validate the Result
  -> Perform Regression Check
  -> Document the Lessons Learned
```

## Core Principles

- Improvement is not the first goal; root cause is the first goal.
- Do not optimize parameters before proving the pipeline is correct.
- Evidence precedes optimization.
- Metrics are evidence, not truth.
- When metrics and human-visible evidence conflict, stop adoption and
  investigate why the evidence disagrees.
- A final bad output is a symptom, not automatically the root cause.

## Step 1: Confirm The Symptom

State what is wrong in observable terms.

Record what failed, where it failed, who or what observed it, whether it is
reproducible, and whether it is visible to humans, metrics, logs, or downstream
output.

Do not start tuning during this step.

## Step 2: Reproduce The Issue

Find the smallest repeatable path that shows the issue.

Record the input, environment or mode, command or workflow path, expected
result, and actual result.

If the issue cannot be reproduced, stop and classify it as an investigation
gap, not a fix candidate.

## Step 3: Collect Evidence

Collect enough evidence to compare stages.

Useful evidence includes logs, metrics, source input, intermediate artifacts,
screenshots, overlays, review reports, database snapshots, API responses,
parser output, and before / after comparisons.

## Step 4: Trace The Entire Pipeline

Trace the path from input to final decision.

Examples:

- Import: source file -> parser -> normalized record -> validation -> database.
- API: request -> response -> mapping -> cache -> UI state.
- Database: query -> join -> transformation -> output.
- UI: user action -> state change -> render -> visible result.
- AI Pipeline: input -> candidate generation -> scoring -> selection -> output.

The trace should show where state changes, not just where the final output is
wrong.

Separate detection, candidate generation, recognition, scoring, selection, and
rendering failures. If the correct candidate was never generated, tuning a
later recognition or scoring stage cannot prove root cause.

## Step 5: Identify The First Broken Step

Find the first stage where the output stops matching the expected state.

Check that the previous step is correct, the current step is the first observed
failure, later failures are consequences, and identity drift, selection error,
scoring failure, and rendering failure are not being mixed together.

If the first broken step is unclear, continue investigation before tuning or
algorithm change.

## Step 6: Confirm The Root Cause

Explain why the first broken step happened.

Root cause must be supported by evidence. It should not be a guess based only on
final output.

Record important rejected hypotheses as Negative Knowledge when they are likely
to save future review time.

## Step 7: Apply The Fix

Apply the smallest fix that addresses the confirmed root cause.

Do not use the fix to hide missing evidence. If the fix changes scope, create or
update the Q before implementation.

## Step 8: Validate The Result

Validate the fixed path against the evidence gathered earlier.

Use the original reproduction path, relevant metrics, human review when visual
or semantic quality is involved, and debug artifacts when intermediate behavior
matters.

## Step 9: Perform Regression Check

Check that the fix did not break nearby behavior.

Use a focused check for narrow changes and broader checks for shared workflow,
parser, database, UI, or AI pipeline behavior.

## Step 10: Document Lessons Learned

Preserve reusable knowledge in the right destination:

- `pip/cases/`
- `pip/concepts/`
- `pip/investigations/`
- `pip/rule_stories/`
- `pip/best_practices/`
- `docs/rules/`
- `docs/workflow/`

## Completion Report Requirements

When this methodology is used, the completion report should state:

- symptom;
- reproduction path;
- evidence reviewed;
- pipeline stages traced;
- first broken step;
- rejected hypotheses, when useful;
- root cause;
- fix applied or deferred;
- validation result;
- regression check result;
- reusable lessons and promotion targets.

## Related Concepts

- CONCEPT-2026-001: Trace Before Tune
- CONCEPT-2026-002: First Broken Step
- CONCEPT-2026-003: Pipeline Traceability
- CONCEPT-2026-004: Human Review Over Automation
- CONCEPT-2026-007: Metrics Are Evidence, Not Truth
- CONCEPT-2026-009: Root Cause Before Optimization
- CONCEPT-2026-013: Evidence Driven Development
- CONCEPT-2026-014: Negative Knowledge

## Related CASE

- CASE-0008: Steam OCR Root Cause Investigation

## Related Rules And Workflows

- `docs/rules/debug_escalation_ladder_rules.md`
- `docs/workflow/debug_escalation_ladder.md`
- `docs/workflow/debug_artifact_review_workflow.md`
- `pip/templates/investigation_pattern_template.md`

## Do Not

- Do not tune before tracing.
- Do not call the final bad output the root cause by default.
- Do not skip human review when metrics and human-visible evidence conflict.
- Do not ignore rejected hypotheses when they are likely to recur.
- Do not apply a broad fix when the first broken step is still unknown.
