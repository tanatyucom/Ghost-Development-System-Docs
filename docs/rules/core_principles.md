# Core Principles

**Version:** 2.3

**Last Updated:** 2026-07-10

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
Download File Rule, Completion Report, Human Review, AI Proactive Proposal, and
Collaborative Decision Workflow.

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

### Human Approval Gate

Humans retain final authority over architecture, destructive changes,
standardization, releases, and scope expansion.

### Continuous Improvement

Retrospectives should produce concrete improvements to rules, templates,
workflow, or roadmap when the learning is reusable.

## Development Philosophy

The goal is not merely to write code or documents. The goal is to build a
durable development system that keeps knowledge, decisions, and responsibilities
clear across time.
