# Research Mission Rules

## Purpose

Research Mission Rules define the minimum requirements for reusable GDS
investigation work.

The rule exists because vague investigation requests are hard to reproduce,
review, validate, or promote into knowledge. Research Missions make the
research goal, allowed scope, evidence, validation, and completion report
explicit before the work begins.

## Core Rule

When a task asks AI or a human to investigate an uncertain cause, compare
hypotheses, trace a failure, classify a knowledge gap, or prepare reusable
research, create or use a Research Mission artifact.

A Research Mission must include:

- Goal.
- Research Questions.
- Expected Hypothesis.
- Scope.
- Out of Scope.
- Required Evidence.
- Validation Method.
- Deliverables.
- Success Criteria.
- Negative Result Policy.
- Completion Report requirement.

## Required Behavior

### Goal

State what the mission should prove, disprove, clarify, or classify.

Do not use a vague goal such as "investigate" without a reviewable outcome.

### Scope

State what files, artifacts, repositories, data, reports, or behaviors may be
examined.

Scope must also state whether runtime code, related repositories, generated
artifacts, or raw data may be edited.

### Out of Scope

State what must not be changed.

If the mission is documentation-only, runtime code and related implementation
repositories must remain out of scope unless the Q explicitly says otherwise.

### Evidence

Research conclusions must be tied to evidence.

Evidence may include:

- source files;
- logs;
- generated reports;
- screenshots or visual artifacts;
- metrics;
- human review notes;
- comparison artifacts;
- prior rules, workflow, CASE, or history entries.

AI guesses, summaries, and metrics are not final proof without review.

### Validation

State how the conclusion will be checked.

Validation may include reproduction, comparison, regression check, human review,
repository quality audit, AI Repository Index validation, or explicit evidence
gap reporting.

### Completion Report

Every completed Research Mission must produce a Completion Report or an
equivalent saved report artifact.

The report must include:

- source Research Mission;
- evidence reviewed;
- hypotheses accepted;
- hypotheses rejected;
- validation result;
- remaining uncertainty;
- Knowledge Promotion recommendation;
- recommended next Q;
- commit status.

### Negative Result

Rejected hypotheses are knowledge when they prevent repeated false paths.

Record negative results when:

- the rejected hypothesis was plausible;
- evidence was checked;
- the rejection affects future work;
- the result should inform CASE, Concept, Workflow, Rule, or Knowledge
  Inventory.

## Relationship To Other Rules

Research Mission does not replace:

- Artifact First.
- Q File Artifact Standard.
- Startup Checklist.
- Debug Artifact Review.
- Debug Escalation Ladder.
- First Broken Step Methodology.
- Completion Checklist.
- PIP Case Knowledge Base.
- Human Approval Gate.

It is the standard front door for research-like work before those workflows are
selected or completed.

## Stop Conditions

Do not begin a Research Mission when:

- the target repository is unclear;
- the authoritative Q or mission artifact is missing when required;
- scope or out-of-scope boundaries are unclear;
- required evidence is inaccessible and no evidence gap is recorded;
- the task would edit a reference-only repository;
- commit policy is unclear.

## Decision Background

Steam OCR Root Cause Investigation showed that research quality improved when
the request named Goal, Scope, Out of Scope, Evidence, Validation, and
Completion Report requirements.

This rule promotes that practice from a project-specific success into a GDS
standard that can be reused outside Steam OCR.

## Related Documents

- `templates/research_mission_template.md`
- `docs/workflow/research_mission_workflow.md`
- `templates/completion_report_template.md`
- `docs/rules/completion_checklist_rules.md`
- `docs/rules/debug_artifact_review_rules.md`
- `docs/rules/debug_escalation_ladder_rules.md`
- `docs/rules/q_file_artifact_standard.md`
- `docs/workflow/first_broken_step_methodology.md`
- `docs/workflow/pip_case_knowledge_base_workflow.md`

