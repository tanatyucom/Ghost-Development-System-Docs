# Template Lifecycle

## Purpose

This document explains how useful knowledge becomes a reusable template, rule,
or knowledge base document.

## Lifecycle

```text
Idea
  -> Review
  -> Q
  -> Implementation
  -> Improvement Review
  -> Reusable?
  -> Template
  -> Rule
  -> Knowledge Base
```

## Step Meanings

Idea:

A pattern, issue, or improvement noticed during work.

Review:

Check whether the idea is useful, repeated, safe, and aligned with the Ghost
Development System.

Q:

Create a structured request when the improvement should be applied now.

Implementation:

Apply the accepted scope only.

Improvement Review:

Ask what the completed work teaches the system.

Reusable?:

Decide whether the learning is a one-time note, template candidate, rule
candidate, example, or broader documentation update.

Template:

Use a template when the learning improves how future requests or reports are
structured.

Rule:

Use a rule when the learning should become a required standard.

Knowledge Base:

Use knowledge base documentation when the learning explains architecture,
workflow, glossary, examples, roadmap direction, or public operating guidance.

## Knowledge Promotion Policy

Recommended improvements may be promoted when they are:

- repeated or likely to repeat;
- clear enough to teach;
- safe to standardize;
- useful to both humans and AI;
- able to make forgetting, drift, or copy loss safer through a checkable
  control;
- aligned with existing rules and roadmap direction.

If the learning is operational knowledge that tools should consume, promote it
as a Knowledge Asset rather than only as prose documentation.

Promotion path:

```text
Recommended
  -> Template candidate
  -> Rule candidate
  -> Knowledge Base / Knowledge Asset
```

Future Candidates should be preserved but not promoted until reviewed.

## Knowledge Before Automation

If an improvement is requested because automation failed, promote reusable
knowledge before expanding the automation.

Preferred path:

```text
Observed failure
  -> Review
  -> Human Approval
  -> Knowledge Asset
  -> Knowledge Asset Layer
  -> Automation consumes the asset
```

This keeps future automation understandable and portable across GameGhost,
AnimeGhost, ComicGhost, and new archive projects.

## Knowledge Poka-Yoke

If a lesson exists because someone may forget a step, miss a file, work in the
wrong repository, lose a chat-only request, skip verification, or let a process
drift, treat that as a design signal.

Preferred path:

```text
Memory-Dependent Step
  -> Visible Check
  -> Template / Checklist / Validation / Artifact
  -> Review
  -> Automation, when safe
```

The goal is to design systems that make forgetting safe, not to depend on
perfect memory from humans or AI.

## Promotion Checklist

- Is this reusable beyond the current Q?
- Does it reduce future ambiguity?
- Does it prevent a repeated mistake?
- Does it make forgetting, process drift, repository confusion, or copy loss
  safer?
- Does it belong in a template, rule, example, architecture note, workflow
  guide, glossary, or roadmap?
- Does it belong in Knowledge Asset Layer so tools can consume it?
- Is there metric evidence that supports the promotion?
- Does it need Human Approval Gate?
- Should it remain a Future Candidate?
