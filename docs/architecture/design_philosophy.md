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
