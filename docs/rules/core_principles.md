# Core Principles

**Version:** 2.5

**Last Updated:** 2026-07-13

## Purpose

This document defines the core philosophy used to maintain Ghost Development
System Docs.

## Principles

### Archive First

Design for Gray Ghost Archive first.

External reuse is valuable only when it emerges naturally from good internal
architecture.

### Future Self First

Write documents so a future maintainer can understand purpose, scope, ownership,
and status without relying on memory.

### Context Recovery Principle

Repository and documentation structures should optimize for context recovery,
not memory retention.

Canonical Japanese statement:

```text
Repositoryと文書体系は、
利用者が過去を覚えていることではなく、
忘れた状態から安全かつ迅速に現在地へ復帰できることを前提に設計する。
```

GDS assumes that humans and AI may return with little or no retained context.
The system should help them recover:

1. what the artifact or system is;
2. why it exists;
3. what the current position is;
4. what has already been completed;
5. what remains unfinished;
6. what decision and evidence led to the current state;
7. what action should happen next;
8. where authoritative information is located;
9. what actions require Human Approval;
10. what must not be changed automatically.

This principle applies to human users, future selves, new AI sessions,
Codex / ChatGPT / Claude / Gemini or other AI collaborators, new contributors,
long-term maintenance, incident recovery, server and infrastructure recovery,
project resumption after long inactivity, and handoff between projects or agents.

The review question is:

```text
Can this project or artifact be safely resumed by someone who remembers nothing?
```

If the answer is no, identify the smallest missing recovery aid. Common aids
include Current Position, Decision Record, Completion Report, canonical entry
point, README navigation, recovery procedure, explicit next action, Human
Approval boundary, known blocker, and last verified state.

Relationship to existing standards:

- AI Startup Procedure provides the canonical entry point.
- Development Context Synchronization restores repository knowledge, current
  approved mission, current information package, current task, and human goal.
- Product Documentation Hierarchy distributes recovery responsibilities across
  Blueprint, Roadmap, Decision Record, Q Documents, and Completion Report.
- Beginner & Future Self Test verifies whether the principle works in practice.
- Completion Report preserves actual results, evidence, lessons learned,
  remaining issues, and recommended next work.

### Human And AI Friendly

Documents should be readable by humans and structured enough for AI to use
without guessing.

### Project First

Every Q must declare its Target Project before implementation.

Target Project, Repository, Single Source Of Truth, Related Repository,
Cross Project Impact, and Scope Guard should be clear enough to prevent AI from
editing the wrong project or mixing parent platform responsibilities with
project-specific responsibilities.

### Japanese First

Ghost Development System Docs uses Japanese as the default language for human
judgment, approval, review, Q files, templates, rules, roadmap, and completion
reports.

English may remain for code, APIs, identifiers, filenames, paths, Git commands,
commit messages, and terms that need English form.

### Evidence First

Base decisions on actual files, reviewed designs, implementation results, and
documented history.

When repeated operation produces comparable results, preserve the relevant
metrics as evidence. Metrics should have clear source, meaning, owner, and
review boundary. They support judgment; they do not replace Human Approval Gate.

When metrics and reviewed human-visible evidence disagree, pause adoption and
investigate the conflict. Do not treat either side as automatically correct.
Use pipeline trace, intermediate artifacts, and first broken step analysis to
find why the evidence disagrees.

### Authority-Driven Responsibility

Responsibility should be assigned by authority, not by feature name or
explanation capability.

Canonical Japanese statement:

```text
責務は機能ではなく、権限で決める。
```

An actor that can review or explain an operation does not automatically own the
right to request execution permission, mutate repository state, or claim
execution evidence. Approval Request for a mutation belongs to the
execution-capable actor or governed execution surface.

When authority, approval target, or evidence ownership is unclear, use SCW.

Details follow:

```text
docs/architecture/authority_driven_responsibility_principle.md
docs/rules/responsibility_assignment_rules.md
```

### Knowledge Before Automation

When automation fails, first ask whether the system lacks reusable knowledge
before making the automation more complex.

Prefer mechanisms that capture, review, approve, and reuse knowledge, such as
Review, Human Approval, Knowledge Base, Alias, Metadata, and Rules.

Automation should improve because the knowledge base improves. It should not
become a pile of hidden exceptions, AI guesses, or one-off complexity.

When reusable operational knowledge should be consumed by tools, treat it as a
Knowledge Asset. Knowledge Assets should be reviewed, have clear ownership, and
be promoted through Knowledge Asset Layer before automation depends on them.
Raw CSV edits, unreviewed guesses, or hidden prompt exceptions are not approved
Knowledge Assets.

### Platform First

When a new function, rule, workflow, template, checklist, prompt, or validation
could be useful across multiple Ghost projects, evaluate Platform suitability
before treating it as project-specific.

Common capability belongs in GDS. Domain-specific behavior belongs in the
target Ghost project until evidence supports migration.

### Repository First

Adopted repository knowledge has priority over chat memory.

Decision order:

```text
Knowledge Access Index
  -> Repository
  -> Chat
```

If chat guidance conflicts with adopted repository rules, follow the repository
and propose a repository update when needed.

### Knowledge Poka-Yoke / Design For Forgetfulness

People forget.

AI forgets.

Processes drift.

Therefore, design systems that make forgetting safe.

GDS should not rely on memory, personal discipline, or perfect AI context as
the main safety mechanism. Repeated mistakes should become visible checks,
templates, workflow steps, review prompts, or automation support before they
become incidents.

Knowledge Poka-Yoke means:

- do not blame people for forgetting predictable steps;
- do not rely on memory when a checklist, template, or validation can carry the
  step;
- make important checks reviewable;
- automate checks that can be automated safely;
- detect mistakes before they become commits, releases, data changes, or scope
  drift;
- turn small concerns into improvement opportunities;
- create an environment where humans and AI can safely resume long-running
  development.

Examples include Startup Checklist, Completion Checklist, Repository Root
Validation, Repository Information, Scope / Out of Scope, Q Artifact format,
Download File Rule, AI Repository Knowledge Access Index, Completion Report,
Human Review, AI Proactive Proposal, and Collaborative Decision Workflow.

Context Recovery Principle explains the design objective behind these supports:
forgetting should not block safe resumption.

### One File One Theme

One document should have one primary purpose. Split documents when unrelated
responsibilities start to mix.

### One Folder One Responsibility

One folder should represent one clear responsibility. Avoid mixing roadmap,
rules, templates, workflow, and implementation details.

### Purpose-Oriented Naming

Name roadmap items, Q files, and public knowledge base topics by their intended
purpose before naming a specific implementation method.

Implementation terms such as parser, OCR, API, CSV import, migration, or script
may appear in descriptions, target lists, or specifications when they are useful.
They should not be the public title when the real goal is broader than one
technique.

Use purpose-oriented names to keep future implementation options open and to
make roadmap items understandable outside a single technical approach.

### Documentation First

When design, workflow, or ownership changes, documentation should be updated as
part of the work, not left as a later cleanup.

### Incremental Development

Prefer small reviewed changes over large unreviewed rewrites.

### Review Before Standardization

Do not turn an idea into a rule or platform feature until practice proves it is
useful.

Platform standard status must move through a reviewed lifecycle. Idea,
Candidate, Prototype, Validation, Standard, Deprecated, Replaced, and Archived
are not labels to change casually; each transition needs the required artifact,
review, and report defined in Platform Standard Registry.

### Human Approval Gate

Humans retain final authority over architecture, destructive changes,
standardization, releases, and scope expansion.

Platform Standard Registry status changes to Standard, Deprecated, Replaced, or
Archived require Human Approval or an explicit human-reviewed completion
report.

### Continuous Improvement

Retrospectives should produce concrete improvements to rules, templates,
workflow, or roadmap when the learning is reusable.

Useful negative results are also improvement input. When a rejected approach,
failed hypothesis, or contradicted metric is likely to prevent future repeated
work, preserve it in the appropriate completion report, CASE, PIP, Knowledge
Inventory, or rule story.

### AI Cognitive Load Reduction

GDS should standardize repeated mechanical decisions so humans and AI can
focus on high-value judgment, design, review, and improvement.

## Platform Era Classification

Platform Era の新しい思想は、Core Rule、Design Principle、Platform
Architecture、Long-Term Vision に分類して扱います。

Classification:

- Core Rule:
  - Knowledge Before Automation.
  - Human Approval Required.
- Design Principle:
  - Silent Operation Principle.
  - Context Recovery Principle.
  - Platform First.
  - Reuse Before Rebuild.
- Platform Architecture:
  - Innovation Pipeline.
  - Shared Components.
  - Ghost SDK.
- Long-Term Vision:
  - Ghost Ecosystem.
  - Automation Server.
  - AI Continuous Improvement.

詳細は `docs/architecture/platform_era_core_principles.md` を参照します。

Platform Standard Registry status lifecycle is defined in
`docs/architecture/platform_standard_registry.md`.

## Development Philosophy

The goal is not merely to write code or documents. The goal is to build a
durable development system that keeps knowledge, decisions, and responsibilities
clear across time.
