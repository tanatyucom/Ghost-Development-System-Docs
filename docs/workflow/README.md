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
  -> Template / Rule / Knowledge Base
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
