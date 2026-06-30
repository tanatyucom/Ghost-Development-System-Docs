# Roadmap

## Purpose

This roadmap is the long-term project map for Gray Ghost Archive and the Ghost
Development System.

It records version themes, architectural direction, responsibility boundaries,
major work items, future candidates, and review gates. Short-term execution
details belong in status or Queue documents. Implementation details belong in
specifications.

## Development Evolution

```text
Ver1.4
  Ghost Development Toolkit Trial

Ver1.5
  Archive Foundation

Ver2.x
  Ghost Development System

Future
  Reusable Development Platform
```

The system evolves from practical archive work. Architecture is validated by
implementation, review, and repeated operation.

## Current Direction

Gray Ghost Archive is moving from a GameGhost-centered project into an
archive-wide development platform.

The current direction is:

- Ver1.4 proves the Ghost Development Toolkit Trial through real development.
- Ver1.5 establishes Archive Foundation.
- Ver2.x formalizes Ghost Development System as an archive-wide development
  platform.
- Future work may extract reusable platform ideas after they are proven inside
  Gray Ghost Archive.

## Design Philosophy

- Archive First: design for Gray Ghost Archive before designing for external
  reuse.
- Architecture evolves through implementation.
- External reuse is a consequence of good architecture, not the primary goal.
- Human Approval Gate: AI may recommend and prepare work, but humans approve
  scope, destructive changes, architecture changes, releases, and
  standardization.
- Future Scope Guard: unvalidated or large ideas stay in Future Candidates
  until promoted by roadmap review.

## Ver1.4 Roadmap

Status: active.

Theme:

```text
Ghost Development Toolkit Trial
```

Purpose:

```text
Use the Ver1.3 Foundation in normal operation and prove the first archive-wide
development utilities.
```

Ver1.4 treats Ghost Development Toolkit as a practical trial of archive-wide
development utilities. The trial should stay small enough to learn from real
work before formal system boundaries are created.

Trial candidates include:

- Command Center direction.
- Development workflow.
- Queue operation.
- Review workflow.
- Health and validation coordination.
- Archive Target Registry.
- Documentation practices.

### Ver1.4 Work Items

| ID | Category | Priority | Title | Roadmap Role | Success Criteria | Exit Definition |
|---|---|---:|---|---|---|---|
| Ver1.4-A | Architecture / Feature | Critical | Archive Launcher and Archive Target Registry | First archive-level entry point and shared target catalog | Launcher starts, registry loads targets, and archive-level files are accounted for | Launcher and registry are reviewed, documented, and ready for the next iteration |
| Ver1.4-B | Research | High | OCR Import Health Check | Confirm whether OCR import survived structure/output changes | OCR import, review output, debug images, logs, `run_all.py`, and `tool.py health` are checked | PASS moves to normal operation; FAIL creates Ver1.4-C |
| Ver1.4-C | Maintenance | High, conditional | OCR Import Recovery | Fix only if Ver1.4-B finds breakage | Caller/path/output/import issues are repaired without expanding scope | Recovery verification passes, or blocker is documented |
| Ver1.4-D | Trial | High | Development Workflow Version 2.0 Trial | Operate the Ver1.4 cycle through the trial workflow | Multiple Queue items complete using Rev.2 flow; trial review is recorded | Promote, revise, or reject recommendation is ready |
| Ver1.4-E | Architecture | Normal | `unified_title` Migration Design | Design only; no deletion | Caller audit, migration plan, and cleanup plan are written | Ver1.5+ cleanup scope is clear |
| Ver1.4-F | Feature | Normal | Nintendo 3DS Activity Log Parser | Convert completed research into parser implementation | Parser starts or implementation specification is confirmed | Parser work is started or ready for next Queue item |

### Ver1.4 Exit Definition

Ver1.4 can close when:

- Launcher and Archive Target Registry work is complete.
- OCR Health Check is complete.
- OCR Recovery is complete if needed, or explicitly skipped because the health
  check passed.
- Workflow Trial review is complete.
- `unified_title` Migration Design is complete.
- 3DS Parser is started or its implementation specification is ready.
- Roadmap, status, Queue, and development history are aligned after the final
  retrospective.

## Ver1.5 Roadmap

Status: planned.

Theme:

```text
Archive Foundation
```

Purpose:

```text
Transform Gray Ghost Archive from a GameGhost-centered repository into an
archive-centered platform.
```

### Ver1.5-A Archive Root Git Migration

Category: Architecture / Repository Design

Priority: High

Purpose:

- Make `C:\GrayGhostArchive` the long-term Git repository root.
- Preserve existing GameGhost history.
- Avoid nested repositories.
- Use staged migration through clean clone and `git mv`.

Scope note:

Migration is a future implementation activity. This knowledge base may document
the plan, but it must not perform migration work.

### Ver1.5-B Archive Docs Hierarchy

Category: Documentation / Architecture

Priority: High

Purpose:

- Separate archive documentation from module documentation.
- Clarify document ownership.
- Prepare docs for future modules.

Ownership model:

```text
Archive docs:
  Archive-wide rules, workflow, roadmap, architecture, Command Center, DMS,
  registry, and cross-module decisions.

Module docs:
  Module-specific schema, scripts, imports, reports, GUI, validation, and
  implementation details.
```

### Ver1.5-C Registry Stabilization

Category: Architecture / Data Contract

Priority: High

Purpose:

- Stabilize Archive Target Registry schema.
- Stabilize target naming rules.
- Add validation expectations.
- Prepare for future Registry Health without implementing full DMS behavior.

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
belongs to Ver2.x or later.

## Ver2.x Direction

Theme:

```text
Ghost Development System
```

Ghost Development System is the formal successor and expansion of Ghost
Development Toolkit Trial.

It is the official archive-wide development platform for Gray Ghost Archive. It
provides development infrastructure, coordination, knowledge management, and
quality gates across archive modules.

Roadmap and prose name:

```text
Ghost Development System
```

Future implementation or folder name candidate:

```text
DevelopmentSystem
```

`DevelopmentSystem` is a candidate implementation folder name, not a commitment
to create a folder in the current phase.

## Responsibility Boundary

### DevelopmentSystem

DevelopmentSystem owns archive-wide development infrastructure:

- Workflow.
- Queue.
- Review.
- Documentation.
- Templates.
- Database Utility Framework.
- Release Coordination.
- Backup Coordination.
- Archive Target Registry.
- Health.
- Command Center.
- DMS.

DevelopmentSystem must not own module-specific business logic, schema content,
or import rules.

### Gray Ghost Core

Gray Ghost Core owns:

- Analysis.
- Recommendation.
- Cross-module Intelligence.

Gray Ghost Core may provide insight across modules, but it should not replace
module ownership or bypass human approval.

### Archive Modules

Archive Modules own:

- Business Logic.
- Schema.
- Metadata.
- Import Rules.

Each module remains independently evolvable. Module-specific behavior belongs
inside the module unless it has been proven reusable and promoted by review.

### Launcher

Launcher owns:

- User Entry Point.

Launcher may present archive targets and start tools. It should not become the
owner of workflow, DMS, module business logic, or database utilities.

## Database Philosophy

DevelopmentSystem owns Database Utility.

This includes reusable frameworks for:

- import and export assistance;
- validation;
- backup coordination;
- migration assistance;
- schema helper tooling;
- database quality reporting;
- cross-module health checks.

Archive Modules own Schema Ownership.

This includes:

- schema definitions;
- module metadata;
- import rules;
- module-specific data contracts;
- business logic that interprets module data.

DevelopmentSystem provides tools and coordination. Modules retain content and
schema authority.

## Success Criteria

Ghost Development System is considered established when:

- shared workflow is used across archive modules;
- health operates archive-wide;
- Archive Target Registry supports all modules;
- Command Center becomes the common development entry point;
- documentation workflow is unified;
- DMS can recommend and prepare work without bypassing human approval;
- responsibility boundaries are clear enough for both humans and AI to follow.

## Future Candidates

Keep these as Future unless a later roadmap review promotes them:

- Architecture Decision Records.
- Reusable Development Platform.
- Registry Health.
- Dead Documentation Detector.
- Duplicate Idea Checker.
- Improvement Collector.
- Technical Debt Tracker.
- Knowledge Synchronization Design.
- Tool Modularization.

### Knowledge Platform

- Development Knowledge Platform.

Purpose:

Create an organized knowledge layer for development history, rules,
architecture, decisions, templates, and cross-module learning.

### Development Knowledge DB

Purpose:

Create a metadata database that manages project knowledge.

Candidate contents:

- documents;
- decisions;
- rules;
- templates;
- roadmap items;
- Queue history;
- module ownership;
- dependency metadata;
- review findings.

### Dependency Index

Purpose:

Track dependencies across:

- Python;
- JSON;
- Database;
- Documentation.

This should help humans and AI understand what may be affected before a change
is made.

### Universal Project Search

Purpose:

Search across the whole project, including code, docs, rules, templates,
schemas, metadata, and historical decisions.

### DB Impact Analyzer

Purpose:

Analyze the impact of database changes before implementation.

Candidate checks:

- schema references;
- import scripts;
- reports;
- validators;
- documentation;
- backup and migration implications.

### Documentation Impact Analyzer

Purpose:

Analyze which documents must be updated when rules, workflow, architecture, or
templates change.

### Architecture Viewer

Purpose:

Visualize dependencies, ownership boundaries, and structure across archive
modules and DevelopmentSystem.

### Rename Compatibility Analyzer

Purpose:

Analyze compatibility risks when names, paths, commands, modules, database
fields, or public document terms are renamed.

### OCR Golden Sample Calibration

Purpose:

Use expected titles or golden samples to validate and tune OCR settings.

This should remain a verification candidate until the OCR import workflow and
sample management rules are stable.

## Repository Growth Policy

Keep archive root small.

Archive root should contain only archive-level entry points, shared
infrastructure, archive-wide docs, and module directories.

Module-specific functionality belongs inside modules.

## Roadmap Review Points

Review the roadmap after:

- each completed Queue item;
- any Stop Gate rejection or return to planning;
- Ver1.4-B PASS/FAIL decision;
- Ver1.4-D trial review;
- Ver1.4 closeout;
- Archive Root migration design approval;
- Archive Root migration completion;
- any accepted change to DevelopmentSystem boundaries.
