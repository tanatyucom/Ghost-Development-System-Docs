# Local Rule Ownership

## Purpose

This document defines how GDS treats project-specific rules discovered in
implementation repositories.

The goal is to let GameGhost, AnimeGhost, ComicGhost, and future Ghost projects
keep project-specific operating knowledge without creating competing canonical
rule systems.

## Core Decision

Canonical development knowledge belongs to GDS.

Generated execution artifacts belong to the repository where work was
performed.

Durable project-specific rules belong to GDS as GDS-managed Local Rules.

## Local Rule Lifecycle

```text
Candidate
  -> Local
  -> Shared
  -> Core
```

### Candidate

A project-specific rule candidate has been observed but is not yet accepted as
a Local Rule.

Required evidence:

- source project;
- observed repeated need;
- source Q or completion report;
- reason existing GDS rules are not enough;
- human review need.

### Local

The rule is accepted for one named Ghost project.

It should be managed by GDS and referenced by the project profile or project
documentation.

### Shared

The rule is useful across multiple Ghost projects, but not yet Core.

### Core

The rule becomes part of the common GDS operating model.

## Implementation Repository Mirrors

Implementation repositories may keep local operating documents when they help
daily work, but those documents must not claim to be the canonical GDS source.

If a local document mirrors or adapts a GDS-managed Local Rule, it should state:

```text
Canonical owner: GDS
Local mirror: <repository path>
Scope: <project-specific scope>
```

## GameGhost Initial Local Rule Candidates

Initial candidates from `GG-STYLE-COMPLIANCE-001`:

| Candidate | Direction |
|---|---|
| Mission-phase request workspaces | Accept as Local Rule candidate. |
| Existing GameGhost local rules | Review which become GDS-managed Local Rules and which remain operational mirrors. |
| `output/` as legacy/generated area | Treat as GameGhost-local candidate until a broader generated-output rule exists. |
| Raw imported source captures | Treat as GameGhost-local candidate until a broader import/source capture rule exists. |
| GameGhost data/rules ownership matrix | Treat as Local Rule candidate and possible future Knowledge Asset rule input. |
| GameGhost naming alias statement | Treat as Local Rule candidate. |
| `games_importers/` compatibility package | Treat as Local Rule or legacy cleanup candidate. |
| vendored GDS snapshots | Treat as reference/adoption artifacts, not canonical rules. |

## Stop Conditions

Stop and request Human Review when:

- a project rule appears useful across multiple Ghost projects;
- a local rule would conflict with accepted GDS rules;
- a local mirror may be mistaken for canonical GDS knowledge;
- migration would require moving or deleting project files;
- promotion would imply SDK, Platform Standard, or runtime approval.

## Related Documents

- `docs/rules/platform_governance_rules.md`
- `project_profiles/README.md`
- `project_profiles/gameghost/README.md`
- `docs/architecture/canonical_rule_gap_resolution.md`
