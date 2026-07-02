# Workflow

## Purpose

This folder explains the standard development workflow for Ghost Development
System Docs.

Workflow documents describe how ideas become reviewed work, how completed work
produces reusable knowledge, and how Improvement Review acts as a completion
gate.

## Contains

- `README.md`: workflow folder guide.
- `template_lifecycle.md`: how useful knowledge becomes a template, rule, or
  Knowledge Base document.

## Does NOT Contain

- Runtime implementation.
- Queue execution state.
- Release artifacts.
- Git migration operations.
- Project-specific feature workflow.

## Standard Development Flow

```text
Idea
  -> Knowledge Check
  -> Review
  -> Q File
  -> Implementation
  -> Verification
  -> Improvement Review
  -> Recommended / Future Candidates
  -> Template / Rule / Knowledge Base / Knowledge Asset
```

## Knowledge Before Automation Flow

When the idea is an automation failure, do not jump directly from problem to
more automation.

Use this smaller decision loop first:

```text
Idea
  -> Knowledge
  -> Automation
```

Knowledge means reviewed information that the system can reuse: human approval,
alias decisions, metadata, rules, examples, review reports, and Knowledge Base
updates.

Automation should consume explicit knowledge. It should not hide repeated human
judgment inside increasingly complex code or AI prompts.

## Evidence Feedback Loop

When a completed task produces measurable results, feed those results back into
the knowledge base.

```text
Implementation
  -> Review
  -> Metrics
  -> Knowledge
  -> Rule
  -> Next Improvement
```

Metrics are reviewed evidence, not automatic decisions. They should explain
what changed, where the data came from, what period or sample was measured, and
what interpretation still needs human review.

Use this loop when a change affects OCR quality, review workload, documentation
reuse, automation behavior, or workflow efficiency.

## Knowledge Asset Promotion Flow

When a task discovers reusable project knowledge, use this flow:

```text
Observed result
  -> Review
  -> Candidate Knowledge Asset
  -> Human Approval when required
  -> Knowledge Asset Layer
  -> Automation / Candidate Engine / Review GUI consumes asset
  -> Improvement Review checks whether workflow, rules, or roadmap need updates
```

Knowledge Assets may include Approved Alias, Metadata Override, Unicode Rules,
Golden Samples, OCR Confusion Rules, Review Decisions, Series Rules, Platform
Rules, and User Overrides.

Knowledge Asset Layer is used after review has identified reusable knowledge
and before automation relies on that knowledge. Raw observations, unreviewed
CSV edits, and one-off AI guesses should not be treated as approved assets.

## Step Meanings

Idea:

An observation, problem, feature request, or improvement proposal.

Knowledge Check:

Check whether the idea should first produce reusable knowledge before changing
automation. For example, an OCR failure may need Alias Review and approved
metadata before it needs another OCR profile.

Review:

Clarify scope, risk, repository boundaries, and whether the idea should be
handled now or preserved as a Future Candidate.

Q File:

A structured request that defines Repository Information, Scope Guard, Do / Do
Not, completion criteria, and deliverables.

Implementation:

The accepted scope is applied. Documentation-only requests stay documentation
only.

Verification:

Confirm changed files, scope boundaries, non-scope items, and requested
acceptance criteria.

Improvement Review:

Review whether the completed work revealed reusable improvements for
Documentation, Templates, Workflow, Roadmap, Rules, Architecture, or Knowledge
Base.

Recommended / Future Candidates:

Separate near-term improvements from ideas that should remain future work.

Template / Rule / Knowledge Base:

Promote reusable knowledge into the right durable location.

Knowledge Asset:

Promote reviewed operational knowledge into Knowledge Asset Layer when it
should be consumed by tools, candidate engines, review GUI, Knowledge Editor, or
future project automation.

## Improvement Review As Completion Gate

Improvement Review is part of completion.

A task is not fully reported until it has considered whether reusable knowledge
should be promoted or preserved.

## Update Policy

Update workflow documents when repeated practice proves a better standard flow.

Do not treat an unreviewed Future Candidate as approved workflow.

## Related Documents

- `docs/workflow/template_lifecycle.md`
- `docs/rules/workflow_rules.md`
- `docs/rules/project_rules.md`
- `docs/templates/q_file_template.md`
- `docs/templates/review_checklist.md`
- `docs/history/knowledge_base_history.md`
