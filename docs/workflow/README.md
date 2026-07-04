# Workflow

## Purpose

This folder explains the standard development workflow for Ghost Development
System Docs.

Workflow documents describe how ideas become reviewed work, how completed work
produces reusable knowledge, and how Improvement Review acts as a completion
gate.

## Contains

- `README.md`: workflow folder guide.
- `output_policy.md`: chat versus file artifact output decision policy.
- `commit_safety_checklist.md`: dirty workspace and commit safety workflow.
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
  -> Output Decision
  -> Review
  -> Q Artifact Workspace
  -> Workspace Save Verification
  -> Approval
  -> Codex / AI Implementation
  -> Completion Report Artifact
  -> Human Review
  -> Commit
  -> Knowledge Promotion
  -> Archive
```

## Output Policy

Before implementation or review, decide whether the requested output should be
chat or a file artifact.

Use chat for short consultation, clarification, and temporary status.

Use file artifacts for long Q files, design documents, specifications, review
requests, Codex / Gemini / Claude requests, roadmap update proposals, human
approval packets, and Git-managed documentation.

Standard artifact formats are Markdown `.md` and Word `.docx`. Markdown is the
default for Git and AI handoff. `.docx` is required when human review,
redline, approval review, or offline reading is expected.

When an artifact is the authoritative output, chat should contain only a short
summary, artifact paths or links, verification notes, and remaining issues.

## Commit Safety Workflow

Before committing, use the standard dirty workspace review:

```text
git status
  -> Classify changes
  -> Review unrelated files
  -> Restore accidental files
  -> git diff --check
  -> Commit
  -> Push
```

Every completion report should state whether a dirty workspace was detected,
whether unrelated files were present, any suggested restore commands, and the
safe commit set.

## Q Artifact Workflow

Q files are generated and saved before Codex or another AI executes the work.

Standard flow:

```text
Idea
  -> Q Artifact Workspace
  -> Save request.md in docs/requests/
  -> Workspace Save Verification
  -> Approval
  -> Codex / AI Implementation
  -> Completion Report Artifact
  -> Human Review
  -> Commit
  -> Knowledge Promotion
  -> Archive
```

Q artifacts and completion report artifacts are saved under:

```text
docs/requests/
```

Use this workspace pattern when the task has related artifacts:

```text
docs/requests/<target_project>/<status>/<request_id>_<short_title>/
  request.md
  completion_report.md
  notes.md
  attachments/
```

Simple file form is allowed for small tasks:

```text
docs/requests/<target_project>/<status>/YYYY-MM-DD_<target_project>_<short_title>.md
```

Status folders are `draft`, `approved`, `completed`, and `archived`.

Workspace save verification means confirming that the authoritative Q exists
as `request.md` or an approved simple-form `.md` file under
`docs/requests/<target_project>/<status>/`. A Q that exists only in chat, a
download folder, clipboard, or temporary sandbox path should not be treated as
the official task input. Save the Q first, then begin implementation.

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

Q Artifact Workspace:

A structured request that defines Repository Information, Scope Guard, Do / Do
Not, completion criteria, and deliverables, plus the task folder that preserves
the request, completion report, notes, and attachments. It should be saved in
`docs/requests/<target_project>/<status>/` before implementation when it is
reusable, reviewable, AI-handoff, or Git-managed.

The minimum full workspace is:

```text
request.md
completion_report.md
notes.md
attachments/
```

Completion Report Artifact:

A saved report that links the completed work back to the source Q file,
generated files, output artifacts, commit hash when one exists, and follow-up Q.
It should be stored alongside the source Q artifact.

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
- `docs/workflow/output_policy.md`
- `docs/workflow/commit_safety_checklist.md`
- `docs/rules/workflow_rules.md`
- `docs/rules/git_rules.md`
- `docs/rules/artifact_first_rules.md`
- `docs/rules/q_file_artifact_standard.md`
- `docs/requests/README.md`
- `docs/rules/project_rules.md`
- `docs/templates/q_file_template.md`
- `docs/templates/review_checklist.md`
- `docs/history/knowledge_base_history.md`
