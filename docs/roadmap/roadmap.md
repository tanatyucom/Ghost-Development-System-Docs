# Roadmap

## Purpose

This roadmap is the long-term project map for Gray Ghost Archive.

It records version themes, architectural direction, major work items, and review
gates. Short-term execution details belong in `docs/status/current_focus.md`.
Implementation details belong in Queue specifications.

## Current Direction

Gray Ghost Archive is moving from a GameGhost-centered project into an
Archive-centered platform.

The current architecture direction is:

- Ver1.4 proves the first archive-level foundations and Ghost Development
  Toolkit Trial in normal operation.
- Ver1.5 becomes Archive Foundation.
- Ver2.0 introduces Ghost Development System as the broader archive-wide
  development platform direction.

Architecture evolves through implementation.

Implementation validates architecture.

Roadmap records validated direction.

Gray Ghost Archive should evolve through practical project development.
Speculative architecture should remain a future candidate until it is
validated by real archive work.

## Ver1.4 Roadmap

Status: active.

Theme:

```text
First release that actively uses the Ver1.3 Foundation.
```

Ver1.4 moves the Ver1.3 Foundation from structure-building into real operation.
Development Workflow Version 2.0 is part of the trial operation for the whole
Ver1.4 cycle.

Trial reference:

```text
docs/workflow/development_workflow_v2_trial.md
```

### Operating Principles

- Roadmap is the project map, not a task dump.
- Current Focus is the short resume dashboard.
- Queue items are created only after Roadmap Planning and Stop Gate.
- Codex implements only the accepted Queue scope.
- Retrospective findings are recorded as improvements, not silently folded into
  unrelated work.

### Ver1.4 Work Items

| ID | Category | Priority | Title | Roadmap Role | Success Criteria | Exit Definition |
|---|---|---:|---|---|---|---|
| Ver1.4-A | Architecture / Feature | Critical | Archive Launcher and Archive Target Registry | First archive-level entry point and shared target catalog | Launcher starts, registry loads targets, and archive-level files are accounted for | Launcher and registry are reviewed, documented, and ready for the next iteration |
| Ver1.4-B | Research | High | OCR Import Health Check | Confirm whether OCR import survived structure/output changes | OCR import, review output, debug images, logs, `run_all.py`, and `tool.py health` are checked | PASS moves to normal operation; FAIL creates Ver1.4-C |
| Ver1.4-C | Maintenance | High, conditional | OCR Import Recovery | Fix only if Ver1.4-B finds breakage | Caller/path/output/import issues are repaired without expanding scope | Recovery verification passes, or blocker is documented |
| Ver1.4-D | Trial | High | Development Workflow Version 2.0 Trial | Operate the whole Ver1.4 cycle through the trial workflow | Multiple Queue items complete using Rev.2 flow; trial review is recorded | Promote / revise / reject recommendation is ready |
| Ver1.4-E | Architecture | Normal | `unified_title` Migration Design | Design only; no deletion | Caller audit, migration plan, and cleanup plan are written | Ver1.5+ cleanup scope is clear |
| Ver1.4-F | Feature | Normal | Nintendo 3DS Activity Log Parser | Convert completed research into parser implementation | Parser starts or implementation specification is confirmed | Parser work is started or ready for next Queue item |

### Ghost Development Toolkit Trial

Ver1.4 treats Ghost Development Toolkit as a practical trial of archive-wide
development utilities.

The purpose is to prove usefulness through actual Gray Ghost Archive
development before formalizing a larger system.

Trial candidates include:

- Command Center direction.
- Development workflow.
- Queue operation.
- Review workflow.
- Health and validation coordination.
- Archive Target Registry.
- Documentation practices.

Toolkit items may remain small, experimental, or loosely connected during
Ver1.4. Formal system boundaries belong to Ver2.0 or later.

### Ver1.4 Exit Definition

Ver1.4 can close when:

- Ver1.4-A Launcher and Archive Target Registry work is complete.
- Ver1.4-B OCR Health Check is complete.
- Ver1.4-C OCR Recovery is complete if needed, or explicitly skipped because
  Ver1.4-B passed.
- Ver1.4-D Workflow Trial review is complete.
- Ver1.4-E `unified_title` Migration Design is complete.
- Ver1.4-F 3DS Parser is started or its implementation specification is ready.
- Roadmap, Current Focus, Queue, and Development History are aligned after the
  final retrospective.

### Ver1.4 Trial Metrics

Track these during Ver1.4:

- Current Focus update misses.
- Completed move misses.
- Development History update misses.
- Rule improvement proposals.
- Workflow improvement proposals.
- Template improvement proposals.
- Roadmap update proposals.
- Resume quality after reopening a task.
- Copy/paste or command-example mistakes.

## Ver1.5 Roadmap

Status: planned.

Theme:

```text
Archive Foundation
```

Purpose:

```text
Transform Gray Ghost Archive from a GameGhost-centered repository into an
Archive-centered platform.
```

### Ver1.5-A Archive Root Git Migration

Category: Architecture / Repository Design

Priority: High

Purpose:

- Make `C:\GrayGhostArchive` the long-term Git repository root.
- Preserve existing GameGhost history.
- Avoid nested repositories.
- Use Staged Migration through clean clone + `git mv`.

Success Criteria:

- Archive root is the repository root.
- GameGhost history remains available.
- `launcher.py`, `archive_target_registry.py`, and `archive_targets.json` are
  tracked at archive root.
- Runtime, private, generated, and imported data remain excluded.
- Repository verification passes.

Exit Definition:

- Migration Freeze exit criteria pass.
- Repository layout is documented.
- Rollback path is documented.

### Ver1.5-B Archive Docs Hierarchy

Category: Documentation / Architecture

Priority: High

Purpose:

- Separate Archive Documentation from Module Documentation.
- Clarify document ownership.
- Prepare docs for future modules.

Ownership model:

```text
Archive docs:
  Archive-wide rules, workflow, roadmap, current focus, architecture,
  Command Center, DMS, registry, and cross-module decisions.

Module docs:
  Module-specific schema, scripts, imports, reports, GUI, validation,
  and implementation details.
```

Success Criteria:

- Archive-wide docs have a clear home.
- GameGhost docs are scoped to GameGhost-specific content.
- Future AnimeGhost, ComicGhost, and MemoryGhost docs can follow the same model.

### Ver1.5-C Registry Stabilization

Category: Architecture / Data Contract

Priority: High

Purpose:

- Stabilize Archive Target Registry schema.
- Stabilize target naming rules.
- Add validation expectations.
- Prepare for future Registry Health without implementing full DMS behavior.

Success Criteria:

- Registry fields are documented.
- Required and optional fields are separated.
- Future placeholders are represented consistently.
- Launcher, future Command Center, and future DMS can read the same catalog.

### Ver1.5-D Launcher V2

Category: UX / Operations

Priority: Normal

Possible improvements:

- Search.
- Favorites.
- Resume support.
- Registry-driven UI expansion.
- Better navigation.

Scope note:

Launcher V2 should remain a human entry point. Command Center and DMS behavior
belongs to Ver2.0 or later.

## Migration Freeze Rule

During Archive Root Git Migration:

- Avoid unrelated feature work.
- Avoid launcher redesign.
- Avoid registry redesign.
- Avoid output structure changes.
- Avoid module feature expansion.

Migration should focus only on repository migration, documentation alignment,
and verification.

### Migration Freeze Exit Criteria

Migration Freeze ends only after:

- Launcher Verification passes.
- Registry Verification passes.
- Documentation Verification passes.
- Repository Verification passes.

## Archive Platform Foundation

The Archive Platform Foundation consists of:

- Archive Launcher.
- Archive Target Registry.
- Archive Root repository ownership.
- Archive Documentation hierarchy.
- Module boundaries.

The Archive Target Registry is an Archive-wide shared catalog. It is not a
Launcher-only configuration file.

Expected readers:

- Launcher.
- Command Center.
- Development Management System.
- Future module dashboards.

## Ver2.0 Direction

Ver2.0 direction:

```text
Ghost Development System
```

Ghost Development System is the formal successor and expansion of Ghost
Development Toolkit Trial.

It is an archive-wide development system that supports all archive modules.

It provides development infrastructure, not module business logic.

Roadmap / prose name:

```text
Ghost Development System
```

Possible future implementation or folder name:

```text
DevelopmentSystem
```

Architecture boundary:

```text
DevelopmentSystem owns development infrastructure.
Archive modules own content and business logic.
Gray Ghost Core owns analysis and cross-archive intelligence.
Launcher owns user-facing entry points.
```

DevelopmentSystem supports archive modules.
It should never own module-specific business logic.
Archive modules remain independently evolvable.

Candidate responsibilities:

- Command Center.
- DMS.
- Shared Archive Target Registry.
- Workflow.
- Queue.
- Review.
- Documentation Management.
- Database Utility Framework.
- Templates.
- Release Coordination.
- Backup Coordination.
- Cross-module health checks.
- Human approval gates.

Database philosophy:

DevelopmentSystem may provide import, export, validation, backup, migration,
schema helper, cross-module health, and database quality reporting frameworks.

Each archive module owns its own schema definition.

DevelopmentSystem provides tools, not content ownership.

Design principles:

Ghost Development System shall remain modular, archive-first, incrementally
expandable, AI-assisted, human-reviewed, and module-independent.

Success criteria:

Ghost Development System is considered established when:

- Shared workflow is used across archive modules.
- Health operates archive-wide.
- Archive Target Registry supports all modules.
- Command Center becomes the common entry point.
- Documentation workflow is unified.

Future scope guard:

Before introducing a new feature, determine whether it belongs to:

- DevelopmentSystem.
- Gray Ghost Core.
- Archive Module.
- Launcher.

before implementation.

Human approval remains mandatory. DMS may recommend and prepare work, but it
does not silently apply architectural or destructive changes.

Long-term reuse:

Ghost Development System should remain archive-first.

If the architecture naturally matures over time, it may eventually become
reusable outside Gray Ghost Archive.

External reuse should be a consequence of good architecture, not the primary
design goal.

## Future Candidates

Keep these as Future unless a later roadmap review promotes them:

- Architecture Decision Records.
- Reusable Development Platform.
- Registry Health.
- Documentation Impact Analyzer.
- Dead Documentation Detector.
- Duplicate Idea Checker.
- Improvement Collector.
- Technical Debt Tracker.
- Knowledge Synchronization Design.
- Tool Modularization.

## Repository Growth Policy

Keep Archive Root small.

Archive root should contain only archive-level entry points, shared
infrastructure, archive-wide docs, and module directories.

Module-specific functionality belongs inside modules.

## Architecture Evolution Timeline

```text
Ver1.4:
  Launcher Foundation
  Archive Target Registry
  Workflow Version 2.0 Trial

Ver1.5:
  Archive Foundation
  Archive Root Git Migration
  Archive Docs Hierarchy
  Registry Stabilization

Ver2.0:
  Command Center
  Development Management System
  Multi-module Archive Platform
```

## Roadmap Review Points

Review the roadmap after:

- each completed Queue item;
- any Stop Gate rejection or return to planning;
- Ver1.4-B PASS/FAIL decision;
- Ver1.4-D trial review;
- Ver1.4 closeout;
- Archive Root migration design approval;
- Archive Root migration completion.

## Ver1.3-A Project Rename

Status: completed for the active environment.

Official project path:

```text
C:\GrayGhostArchive\GameGhost
```

Migration policy:

```text
GitHub Clone + User Data Migration
```

`C:\SteamAI\GrayGhost` remains a backup environment. Do not use Directory Move
as the standard Project Rename procedure.
