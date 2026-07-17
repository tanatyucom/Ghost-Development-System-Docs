# Ghost Package Standard Architecture Standard Candidate

**Status:** Architecture Standard Candidate

**Last Updated:** 2026-07-18

## Purpose

Ghost Package Standard (GPS) is the candidate package model for preserving,
reviewing, transporting, and discovering GDS knowledge units across humans,
Codex, ChatGPT, Claude, Gemini, local AI, future Command Center components,
and other Ghost repositories.

GPS is registered as an architecture standard candidate only. This document
does not implement package scanning, registry runtime, ZIP validation
automation, Command Center package browsing, API behavior, or repository
mutation.

## Candidate Scope

GPS candidate scope includes:

- Design Package;
- Milestone Package;
- Release Package;
- `PACKAGE.md` as the human-readable package summary;
- `PACKAGE.yaml` as the machine-readable package manifest;
- package discovery direction;
- package metadata direction;
- package lifecycle direction;
- package validation direction;
- cross-repository identity direction;
- multi-AI package handoff direction;
- future Package Scanner and Package Registry direction;
- future Command Center Package Browser direction.

## Non-Scope

This candidate does not approve:

- runtime package scanner implementation;
- package registry implementation;
- automatic package promotion;
- automatic package ZIP validation;
- Command Center implementation;
- GUI implementation;
- API implementation;
- MCP integration;
- Git commit, push, tag, release, merge, rebase, reset, amend, or stash
  execution;
- GameGhost or other project-specific runtime changes.

## Candidate Package Layout

The candidate package layout is:

```text
Package/
├── PACKAGE.md
├── PACKAGE.yaml
├── Q/
├── ADR/
├── Architecture/
├── Workflow/
├── Rules/
├── Templates/
├── Roadmap/
├── Completion/
├── Evidence/
└── Attachments/
```

Not every package must use every folder. A later GPS schema Q must define
required folders by package type.

## Canonical Artifact Direction

GPS uses this candidate direction:

- expanded repository folder is the canonical artifact;
- ZIP is a transport and distribution artifact;
- `PACKAGE.yaml` is the canonical machine-readable manifest inside the package;
- `PACKAGE.md` is the human-readable package summary;
- repository source-of-truth remains authoritative over chat messages or
  one-off downloads.

This direction is not final schema. It must be validated by the future
`PACKAGE.yaml v0.1` and Package Lifecycle Q.

## PACKAGE.yaml v0.1 Direction

The future `PACKAGE.yaml v0.1` schema should define required and optional
fields for:

- package identity;
- schema version;
- title and summary;
- package type;
- lifecycle state;
- status;
- canonical path;
- canonical artifact;
- transport artifact;
- source repository;
- target repository;
- canonical repository;
- related Q;
- related ADR;
- related rules;
- related workflows;
- related templates;
- related commits;
- evidence requirements;
- dependencies;
- promotion state;
- human review requirement;
- execution allowance;
- risk level;
- version;
- timestamps;
- tags;
- supersession and replacement.

## Lifecycle Direction

The future lifecycle should define authority, approval requirements, allowed
transitions, forbidden transitions, and evidence requirements for:

```text
Draft
  -> Review Candidate
  -> Approved
  -> Promoted
  -> Deprecated / Archived
```

## Type Taxonomy Direction

The future package type taxonomy should include at least:

- `knowledge`;
- `design`;
- `milestone`;
- `release`;
- `adapter`;
- `workflow`;
- `rule`;
- `evidence`.

## Validation Direction

Future package validation should check:

- required files;
- required metadata;
- identifier format;
- canonical path;
- related artifact existence;
- broken references;
- dependency resolution;
- evidence requirements;
- lifecycle consistency;
- supersession and deprecation consistency.

## Command Center Relationship

Future Command Center may use GPS metadata to discover and present packages:

```text
Package Scanner
  -> PACKAGE.yaml
  -> Package Registry
  -> Command Center
  -> PACKAGE.md and related artifacts
```

Command Center must not treat package presence, schema completeness, or ZIP
availability as implementation approval or execution authority.

## Multi-AI Relationship

GPS is intended to become a common metadata layer between:

- ChatGPT;
- Codex;
- Claude;
- Gemini;
- Local AI;
- future AI actors.

AI actors may read and summarize GPS packages. They must not automatically
promote, execute, mutate, or commit package contents without Human Approval and
the relevant governed workflow.

## Promotion Criteria

GPS can move from Architecture Standard Candidate toward Standard only after:

- `PACKAGE.yaml v0.1` is specified;
- package lifecycle state machine is specified;
- package validation rules are specified;
- canonical artifact rule is confirmed;
- cross-repository identity is specified;
- supersession and deprecation model is specified;
- at least one reviewable package example exists;
- Human Architecture Review approves the promotion scope;
- Completion Review records verification and remaining limitations.

## Recommended Next Q

`Q_GDS-GPS-001_GHOST_PACKAGE_STANDARD_FOUNDATION`
