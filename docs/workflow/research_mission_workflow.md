# Research Mission Workflow

## Purpose

Research Mission Workflow defines how GDS turns an uncertain problem,
investigation request, or knowledge gap into a scoped, evidence-based research
mission.

It exists so humans and AI do not start from vague instructions such as
"investigate this." A Research Mission must state Goal, Scope, Out of Scope,
Evidence, Validation, and Completion Report requirements before the
investigation begins.

## Standard Flow

```text
Observation
  -> Research Mission
  -> Evidence Collection
  -> Validation
  -> Completion Report
  -> Knowledge Promotion Review
  -> Human Approval
  -> Rule / Workflow / Template / CASE / Inventory
  -> Repository
```

## Step Details

### 1. Observation

Start from an observed issue, uncertainty, failed assumption, review concern,
or repeated question.

Do not jump directly to implementation when the first broken step or root cause
is unknown.

### 2. Research Mission

Create or fill a Research Mission artifact using
`templates/research_mission_template.md`.

The mission must define:

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

### 3. Evidence Collection

Collect evidence that is directly tied to the mission questions.

Evidence may include source files, logs, debug artifacts, visual review,
metrics, comparison reports, human review notes, or existing repository
documents.

Do not treat metrics, OCR text, AI guesses, or generated summaries as final
truth without review.

### 4. Validation

Validate whether the evidence supports or rejects each hypothesis.

If the expected hypothesis is rejected, preserve the rejected path when it is
likely to prevent repeated work.

### 5. Completion Report

Write a Completion Report artifact that links the mission, evidence,
validation result, rejected hypotheses, remaining uncertainty, and recommended
next action.

The report should be stored beside the source Q or mission artifact when the
work uses a Task Artifact Workspace.

### 6. Knowledge Promotion Review

Review whether the result should become:

- CASE.
- Rule Story.
- Best Practice.
- Workflow.
- Rule.
- Template.
- Concept.
- Knowledge Inventory entry.
- Archive only.

Promotion requires human review when it changes official rules, workflow,
templates, architecture, or public terminology.

### 7. Repository

Promoted knowledge should be saved in the correct repository location and
linked from README, folder indexes, AI Repository Index, or history when it is
a public entry point.

## Relationship To Existing Workflows

Research Mission is the investigation request layer.

It can feed:

- Debug Escalation Ladder, when the problem is a defect or quality issue.
- First Broken Step Methodology, when a pipeline must be traced.
- Knowledge Inventory, when the result is reusable but not yet promoted.
- PIP Case Knowledge Base, when the result becomes a CASE or Investigation.
- Concept Promotion, when the lesson is still early.
- Completion Checklist, before the task is treated as complete.

## Negative Results

A negative result is useful when it records:

- A plausible hypothesis.
- The evidence checked.
- Why the hypothesis was rejected.
- What future work should avoid repeating.

Negative results may become CASE sections, Investigation entries, Concept
notes, or Knowledge Inventory entries.

## Completion Criteria

A Research Mission is complete when:

- The mission artifact exists.
- Goal, Scope, Out of Scope, Evidence, and Validation are explicit.
- Evidence was collected or the evidence gap was reported.
- Accepted and rejected hypotheses are recorded.
- Completion Report is created.
- Knowledge Promotion recommendation is recorded.
- AI Repository Index update decision is recorded when public Markdown changed.

## Related Documents

- `templates/research_mission_template.md`
- `docs/rules/research_mission_rules.md`
- `templates/completion_report_template.md`
- `docs/workflow/completion_checklist_workflow.md`
- `docs/workflow/debug_escalation_ladder.md`
- `docs/workflow/first_broken_step_methodology.md`
- `docs/knowledge/README.md`
- `docs/workflow/pip_case_knowledge_base_workflow.md`

