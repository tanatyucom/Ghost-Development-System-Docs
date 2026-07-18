# AI Collaboration Rules

**Version:** 2.6

**Last Updated:** 2026-07-13

## Purpose

This document defines how humans and AI collaborate on Ghost Development System
Docs.

## Collaboration Philosophy

### Human Leads

Humans approve goals, architecture, scope, naming, release decisions, and
destructive changes.

Human approval applies only to the latest valid Approval Request. A review
result such as PASS, Ready, or Commit OK is not execution authority by itself.
Commit approval must not be reused as push approval.

Approval Request must be Candidate First when follow-up work is reasonably
discoverable. Show Requested Operations and Recommended Follow-up Candidates
before asking for approval. `お願いします` approves only the visible Requested
Operations. `これ全てお願いします` applies only to the visible Requested
Operations and visible Recommended Follow-up Candidates. Approved work must not
be reported as executed until verifiable Execution Evidence exists.

After approval, Runtime Intent Queue output should show Pending, Delegated,
Waiting For Evidence, Blocked, Excluded, and Completed states. Completion
Review should also distinguish `Codexへ渡す` from `閲覧用`, and explicitly
declare the Canonical Artifact. When a ZIP exists, the ZIP is canonical; when no
ZIP exists, Markdown is canonical.

Execution adapters must be treated as governed boundaries, not generic command
wrappers. They may execute or delegate only approved scope, with known
authority, satisfied dependencies, and explicit evidence requirements. Unknown,
partial, or evidence-missing results must not be reported as completed.

### Working Agreement And Current Position

When work spans Q creation, review, implementation, completion review, or
commit decisions, AI should keep the workflow context visible.

Before selecting the next action, AI should state:

- Current Phase.
- Current Review.
- Current Position.
- Next Action.

Short approval phrases such as OK, おｋ, お願いします, 採用, 承認, 続けて, and
進めて approve only the currently visible requested action and continue the
workflow.

They do not authorize repository modification, commit, push, tag, or release.

Each approval boundary remains independent.

### AI Is A Partner

AI helps draft, review, compare, summarize, and propose improvements. AI should
improve quality, not replace human judgment.

### AI Role

In GDS, AI acts as a repository-aware platform collaborator.

Default posture:

- read repository truth before repository-governed reasoning;
- transform recurring friction into durable knowledge;
- propose platform improvements when evidence shows cross-project value;
- separate proposal, approval, execution, and evidence;
- classify immature ideas as Future Candidates instead of forcing immediate
  implementation;
- keep Human Approval Required for repository mutation, commit, push, tag,
  release, destructive change, and canonical promotion.

AI must not become the Single Source of Truth. The repository remains the
canonical memory; AI sessions are replaceable actors that reconstruct context
from the repository.

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

### Constraint To Execution

When AI knows a capability, tool, environment, permission, repository, or scope
constraint, it should declare that constraint before proposing a solution.

Use this pattern:

```text
Constraint
  -> Objective
  -> Workaround
  -> Execution
```

Required behavior:

1. Declare capability, tool, environment, or permission constraints as soon as
   they are known.
2. Identify the user's actual objective.
3. Present practical workarounds that still satisfy the objective.
4. Recommend the smallest effective path.
5. Execute only after the path and approval boundary are clear.

This prevents unrelated reasoning, false assumptions, avoidable rework, and
solutions that optimize for the wrong limitation.

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
- skip known constraints and reason as if unavailable tools, permissions,
  repositories, or runtime capabilities were available.

## Multi-AI Collaboration

Different AI tools may be used for different strengths, but all AI output must
remain reviewable by humans.

Cross-review is recommended for:

- architecture boundaries;
- roadmap direction;
- public terminology;
- major rule changes;
- reusable templates.

When work is handed off between ChatGPT, Codex, Claude, Gemini, human review,
or another AI context, the handoff should include:

- Current Status.
- Current Focus.
- Scope.
- Source of Truth.
- Changed Files.
- Verification Results.
- Remaining Issues.
- Recommended Next Q.

Before using chat memory during handoff, confirm sources in this order:

1. Knowledge Access Index.
2. Repository.
3. Completion Report.
4. Chat.

Scope protection must name:

- editable targets;
- forbidden edit targets;
- target repository;
- out-of-scope repositories.

Use `templates/multi_ai_handoff_template.md` for the handoff artifact when the
handoff is reusable, reviewable, long-running, or likely to cross tool
boundaries.

Use `templates/multi_ai_handoff_checklist_template.md` to review whether the
handoff artifact is complete enough for the receiving AI or human reviewer.

Use `templates/HANDOFF_TEMPLATE_V2.md` when the handoff must preserve North
Star, design intent, intended experience, Vision Scenario, Approval Request
lifecycle, or generation-to-generation continuity.

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

When the review conclusion is `Commit OK` and the Q or repository policy says
commit is required, AI should immediately provide copy-paste-ready Git Bash
commands for the reviewed Safe Commit Set. The commands must start with:

```bash
cd /c/GitHub/Ghost-Development-System-Docs
```

AI must not execute the commit unless the user explicitly requests it.

Completion reports and final task summaries should prioritize:

- Summary.
- Verification.
- Remaining Issues.
- Recommended Next Q.

## AI Cognitive Load Reduction

Patterns that repeat should become rules, workflows, templates, examples,
checklists, or validations so humans and AI can spend attention on design,
judgment, review, and improvement rather than remembering mechanical steps.

## AI Actor And Adapter Boundary

GDS is the Core authority for approval, intent resolution, queue state, policy,
and completion judgment.

AI is an exchangeable Actor / Interpreter / Delegate. AI may interpret,
prepare, delegate, and report, but it must not become the canonical owner of
runtime state or treat natural-language claims as execution evidence.

Target systems such as Git are Adapter targets. Commit, Push, and Tag
operations require governed adapter boundaries and verifiable evidence before
they may be reported as completed.

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
- `docs/rules/hotfix_policy_rules.md`
- `templates/completion_report_template.md`
- `templates/multi_ai_handoff_template.md`
- `templates/multi_ai_handoff_checklist_template.md`
- `docs/workflow/ai_daily_operation_cycle.md`
- `docs/architecture/gds_core_ai_actor_adapter_boundary.md`
- `docs/architecture/git_execution_adapter_vertical_slice.md`
- `docs/rules/git_execution_adapter_rules.md`
