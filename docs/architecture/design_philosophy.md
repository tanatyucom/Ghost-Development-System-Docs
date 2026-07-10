# Design Philosophy

## Purpose

This document collects the design philosophy behind the Ghost Development
System knowledge base.

## Archive First

Design for Gray Ghost Archive first.

External reuse is welcome when it emerges from clean architecture, but external
reuse is not the primary design driver.

## Project First

Every Q declares Target Project before implementation.

Ghost Development System is the parent development foundation for current and
future projects such as GameGhost, AnimeGhost, ComicGhost, and Other. It should
support project development without absorbing project-specific runtime
ownership.

Target Project, Repository, Single Source Of Truth, Related Repository,
Cross Project Impact, and Scope Guard must be clear enough to prevent
responsibility confusion.

## Japanese First

Human approval requires human-readable requests.

Ghost Development System Docs uses Japanese-first documentation for Q files,
rules, templates, roadmap, reviews, completion reports, and human-facing AI
requests. English remains appropriate for code, APIs, identifiers, filenames,
paths, Git commands, commit messages, and required proper nouns.

## Evidence First

Decisions should be based on visible documents, reviewed work, implementation
results, and explicit user intent.

Avoid hidden assumptions.

## Evidence First With Metrics

Evidence First should grow from "there is evidence" to "the evidence can be
reviewed and measured."

Metrics do not replace human judgment. They make repeated improvement visible
by recording comparable signals such as success rate, review rate, review
iterations, reuse count, automation rate, and human review time.

Use metrics to answer:

- Did the change improve real operation?
- Did the change reduce repeated review work?
- Did the change create reusable knowledge?
- Did the change prevent duplication or hidden assumptions?

Metrics should be connected to reviewed artifacts. Raw numbers without context
are not evidence. A metric becomes useful when its source, owner, meaning, and
review boundary are clear.

## Purpose-Oriented Naming

Public names should describe the intended outcome before a specific
implementation method.

Implementation terms may appear in explanations, targets, or specifications
when they clarify the current approach.

## Human Approval Gate

Humans approve:

- architecture changes;
- destructive changes;
- scope expansion;
- release decisions;
- standardization;
- migration work.

AI may propose, draft, review, and prepare work, but it must not bypass human
approval.

## Artifact First

Reusable, reviewable, or Git-managed outputs should be generated as file
artifacts before they become implementation or approval inputs.

Markdown `.md` is the standard format for Git-managed documentation, AI
handoff, and diff review. Word `.docx` is required when human review,
comments, approval, redline, or offline reading is expected.

Chat is useful for short consultation and status, but it should not be the
authoritative copy for long Q files, design documents, specifications, review
requests, AI implementation requests, or roadmap proposals.

Artifact First supports Human Approval Gate, prevents copy loss, and makes
Knowledge Promotion easier.

## Migration First

Internal architecture should stay simple enough for humans and AI to review.

When an internal folder structure, script layout, adapter internal interface,
prototype script, shared utility location, artifact workspace layout, queue /
request internal structure, or future GhostCore / GDS internal module changes,
prefer migration to the new standard over accumulating permanent compatibility
fallback.

Use:

```text
New Standard
  -> Migration Plan
  -> Reference Update
  -> Verification
  -> Legacy Removal
```

Public Compatibility is protected for public release, public API / CLI,
documented external workflow, exported artifact schema, DB schema, and
user-facing data format. Internal legacy fallback should be temporary,
documented, verified, and removed.

Migration First supports Human Approval Gate by making migration intent,
public impact, remaining legacy, and restore / rollback guidance explicit.

## Knowledge Before Automation

When automation fails, the first architectural question is whether the system
lacks reusable knowledge.

Prefer a loop that captures reviewed knowledge before adding more automation
logic:

```text
Idea
  -> Knowledge
  -> Automation
```

Knowledge may appear as Review, Human Approval, Knowledge Base entries,
Aliases, Metadata, Rules, or Examples. Automation should then consume that
knowledge explicitly.

GameGhost OCR is the reference example: OCR profile expansion was considered,
but the stronger improvement came from Alias Review, Safe Alias, Human Approval,
Unicode Normalizer, Alias Candidate Report, and Review GUI. Those mechanisms
made future OCR results better by accumulating reusable knowledge rather than
only making the OCR engine more complex.

## Knowledge Poka-Yoke / Design For Forgetfulness

People forget. AI forgets. Processes drift.

Therefore, GDS designs systems that make forgetting safe.

Knowledge Poka-Yoke treats forgetting as a predictable design condition, not a
personal failure. If a step is important enough to cause repository confusion,
scope drift, missing Q artifacts, incomplete completion reports, unsafe commits,
or missed human review, the system should make that step visible, checkable, and
repeatable.

Examples:

- Startup Checklist recalls the right rules before work begins.
- Completion Checklist recalls verification, report, commit, tag, release, and
  next-Q decisions before work is treated as complete.
- Repository Root Validation verifies the actual Git root instead of trusting
  memory or shell context.
- Repository Information and Scope / Out of Scope prevent project and
  responsibility confusion.
- Q Artifact format and Download File Rule prevent chat-only or clipboard-only
  loss.
- Completion Report preserves what changed, what was verified, and what remains.
- Human Review keeps high-impact judgment with humans.
- AI Proactive Proposal lets AI surface concerns before they become mistakes.
- Collaborative Decision turns disagreement and classification uncertainty into
  reviewed knowledge.

The cultural rule is simple: do not blame forgetting; design the workflow so
forgetting is caught early.

## Knowledge As Assets

Reusable knowledge should be treated as an asset when it can improve future
automation, review, or project quality.

Knowledge Assets may include Approved Alias, Metadata, Unicode Rules, Golden
Samples, OCR Confusion Rules, Review Decisions, Series Rules, Platform Rules,
User Overrides, and future AI knowledge.

The user-facing direction is to edit Knowledge, not implementation storage.
CSV, JSON, or database tables may remain internal forms, but the public design
should expose reviewed meaning, approval state, and reuse boundaries.

## Knowledge Evolves Through Implementation

Knowledge improves when real work exposes repeated problems, useful patterns,
and better standards.

Reusable knowledge should be promoted to templates, rules, examples, or
documentation whenever practical.

## Architecture Evolves Through Implementation

Architecture should be validated by actual development work.

Speculative architecture remains a Future Candidate until review promotes it.

## Future Scope Guard

Future Candidates are preserved for later review.

They are not approved implementation scope.

## External Reuse

Reusable platform behavior may become valuable beyond Gray Ghost Archive.

That reuse should be a consequence of good architecture and repeated validation,
not a reason to overbuild too early.
