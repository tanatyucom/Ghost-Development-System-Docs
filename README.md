# Ghost Development System Docs

Official knowledge base for the Ghost Development System.

This repository collects the public rules, roadmap, templates, and operating
principles used to develop the Ghost Development System with human and AI
collaboration.

## Purpose

Ghost Development System Docs exists to make development knowledge durable.

It records:

- long-term development direction;
- responsibility boundaries between DevelopmentSystem, Gray Ghost Core,
  Archive Modules, and Launcher;
- rules for human and AI collaboration;
- reusable request, review, planning, and delivery templates;
- future candidates that should be considered without being implemented too
  early.

## Scope

This repository is documentation-only.

It may define or improve:

- roadmap;
- rules;
- templates;
- workflow guidance;
- architecture notes;
- public knowledge base structure.

It does not contain runtime code, private archive data, migration scripts,
GitHub Actions, release artifacts, or module-specific implementation.

## Repository Structure

```text
docs/
  architecture/  Architecture notes and responsibility boundaries.
  examples/      Example documents and usage samples.
  roadmap/       Version roadmap and future candidate direction.
  rules/         Official operating rules for development and documentation.
  templates/     Reusable templates for Q files, reviews, specs, and reports.
  workflow/      Workflow documents and trial process definitions.
```

## Collaboration Model

The Ghost Development System is built for human-led, AI-assisted development.

AI may draft, review, compare, and propose improvements. Humans approve scope,
architecture, destructive changes, releases, and standardization decisions.

The knowledge base should help both humans and AI understand the same project
state without relying on memory, private context, or hidden assumptions.
