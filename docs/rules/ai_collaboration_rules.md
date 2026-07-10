# AI Collaboration Rules

**Version:** 2.5

**Last Updated:** 2026-07-11

## Purpose

This document defines how humans and AI collaborate on Ghost Development System
Docs.

## Collaboration Philosophy

### Human Leads

Humans approve goals, architecture, scope, naming, release decisions, and
destructive changes.

### AI Is A Partner

AI helps draft, review, compare, summarize, and propose improvements. AI should
improve quality, not replace human judgment.

### Evidence First

AI should base suggestions on visible documents, known rules, reviewed
decisions, and explicit user requests.

### Knowledge Must Be Written Down

Reusable learning should move into rules, templates, roadmap, workflow, or
architecture documents. It should not remain only in conversation.

### Persistent Collaboration

Collaboration rules adopted into this repository continue to apply in future
Chats, Codex runs, Claude prompts, Gemini prompts, reviews, and Q executions.

Repository knowledge is persistent. Chat context is temporary. When the two
conflict, follow the repository and update the repository if the rule needs to
change.

### Platform First

For new shared behavior, first ask whether it belongs in the GDS Platform.

- Common capability -> GDS.
- Domain-specific behavior -> target Ghost project.

After field practice matures, run a migration audit to decide whether common
behavior should be promoted into GDS.

### Repository First

Decision order:

1. Knowledge Access Index.
2. Repository documents.
3. Chat.

The repository is the Single Source of Truth for adopted rules, workflows,
templates, examples, reports, and platform standards.

### Proactive Proposal

AI should share evidence-based proposals when it notices a better approach,
time saving opportunity, repository / scope conflict, rule conflict,
methodology conflict, future maintenance risk, or knowledge opportunity.

AI must separate proposal from implementation. AI should not silently expand
scope, alter the implementation plan, or bypass user judgment.

### Collaborative Decision

When AI and user proposals require discussion, evidence review, or knowledge
classification, use Collaborative Decision Workflow.

The goal is not to prove that AI or the user is right. The goal is to find the
most maintainable, reusable, and understandable decision together.

### Artifact First

Reusable AI requests, long review prompts, Q files, design documents,
specifications, and roadmap update proposals should be generated as managed
file artifacts before execution or review.

AI should summarize the artifact in chat and provide the file path or link
instead of making the chat body the authoritative copy.

### Download First

When an output is reusable, reviewable, or intended for another human / AI,
provide it as a downloadable or repository-saved artifact by default.

Default file-first outputs include:

- Q.
- Template.
- Checklist.
- Prompt.
- Markdown.
- Report.

Short consultation, small status updates, and minor corrections may remain in
chat.

### Rule Priority

When guidance conflicts, follow this priority for collaboration behavior:

```text
Rule
  -> Workflow
  -> Template
  -> Example
  -> Implementation
```

If a lower-priority document conflicts with a rule, follow the rule and treat
the conflict as a documentation update candidate.

### Debug Artifact Review

For AI, OCR, recommendation, auto-detection, candidate extraction, fuzzy
matching, and visual processing work, AI should make intermediate behavior
inspectable during development.

AI should name debug artifact paths, expected normal state, review viewpoints,
and future AI review targets when Debug Mode applies.

AI should not generate debug artifacts during normal execution unless Debug
Mode is explicitly requested.

### Audit Before Repair

Before repair, cleanup, OCR result correction, DB correction, mojibake
correction, duplicate resolution, metadata correction, or other repair work, AI
should request or perform an audit step first.

AI should classify findings as `fix_candidate`, `needs_human_review`,
`generated_artifact`, `raw_data`, or `false_positive`, then create a scoped
repair Q that names the source audit artifact, exclusions, verification method,
safe commit set, and restore guidance.

AI should not broad-fix raw data, generated artifacts, OCR evidence, DB files,
or unrelated dirty workspace files without explicit human approval.

## AI Responsibilities

AI may:

- review documentation structure;
- draft and revise Markdown;
- generate Markdown and `.docx` artifacts for reusable requests or human
  review packets;
- identify missing related updates;
- propose future candidates;
- proactively propose evidence-based improvements, risks, conflicts, or
  knowledge opportunities;
- suggest commit messages;
- summarize changes;
- recommend next Q files.
- prepare future AI review handoff by listing the debug artifacts and review
  questions when intermediate evidence is needed.
- prepare audit-first repair handoff by listing source audit artifacts,
  classifications, excluded items, and remaining candidates.

AI must not:

- perform runtime implementation during documentation-only work;
- migrate repositories unless explicitly requested;
- commit unless explicitly requested;
- bypass Human Approval Gate;
- treat Future Candidates as approved implementation.
- silently apply proactive proposals without user approval when they change
  scope, architecture, commit behavior, release behavior, or repository target.
- hide uncertain intermediate behavior behind a final summary when debug
  artifacts are needed for review.
- repair broad or uncertain targets before audit, classification, evidence
  review, and required human approval.

## Multi-AI Collaboration

Different AI tools may be used for different strengths, but all AI output must
remain reviewable by humans.

Cross-review is recommended for:

- architecture boundaries;
- roadmap direction;
- public terminology;
- major rule changes;
- reusable templates.

## Communication Rules

AI should report:

- changed files;
- what changed;
- verification performed;
- debug artifact review performed, when applicable;
- audit before repair performed, when applicable;
- remaining issues;
- future candidates;
- recommended next Q;
- suggested commit message.
- proactive proposals made, when applicable.
- collaborative decisions made, when applicable.

When AI presents CLI commands to a user, the command block should start with a
`cd` command and be copy-pasteable as one block whenever possible.

Example:

```powershell
cd C:\GitHub\Ghost-Development-System-Docs
python scripts\repository_quality_audit.py
```

For review tasks, AI should give one of these conclusions when evidence allows:

- `Commit OK`
- `Revision Recommended`

When neither conclusion is possible, AI should state the blocker and the
minimum next evidence needed.

Platform Era reviews should include a `Recommended Next Q` when the next useful
step is visible.

Completion reports and final task summaries should prioritize:

- Summary.
- Verification.
- Remaining Issues.
- Recommended Next Q.

## AI Cognitive Load Reduction

Patterns that repeat should become rules, workflows, templates, examples,
checklists, or validations so humans and AI can spend attention on design,
judgment, review, and improvement rather than remembering mechanical steps.

## Goal

The goal is a durable collaboration system where humans and AI share the same
knowledge base, reduce repeated mistakes, and improve the archive over time.

Platform Philosophy:

GDS is a platform that standardizes what humans and AI should not need to
rethink, so they can focus on what truly requires judgment.

## Related Documents

- `examples/persistent_collaboration_examples.md`
- `docs/rules/core_principles.md`
- `docs/rules/artifact_first_rules.md`
- `docs/rules/quality_rules.md`
- `templates/completion_report_template.md`
- `docs/workflow/ai_daily_operation_cycle.md`
