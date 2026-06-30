# Core Principles

**Version:** 2.1

**Last Updated:** 2026-06-30

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

### Evidence First

Base decisions on actual files, reviewed designs, implementation results, and
documented history.

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
