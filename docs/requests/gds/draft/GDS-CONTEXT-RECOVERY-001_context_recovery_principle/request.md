# Q_GDS_Context_Recovery_Principle_JP

Version: 1.0
Status: Draft
Priority: High
Category: Design Principle / Context Recovery / Long-Term Maintainability
Created Date: 2026-07-13
Last Updated Date: 2026-07-13
Owner / Target AI: Codex

## Repository Context

Working Repository:
Ghost-Development-System-Docs

Working Directory:
C:\GitHub\Ghost-Development-System-Docs

Preferred Shell:
Git Bash

Target Project:
GDS only

Non-Target Project:
GameGhost

Allowed Edit Scope:
- README.md
- docs/
- roadmap/
- templates/
- examples/
- reports/repository_quality_report.md
- related request workspace

Forbidden Edit Scope:
- GameGhost repository
- implementation repositories
- unrelated scripts or runtime code
- automatic Commit
- automatic Push

## Commit / Push Policy

Commit:
Do not execute.

Push:
Do not execute.

After implementation, report:

- Changed Files
- Summary
- Verification
- Safe Commit Set
- Completion Report
- Remaining Issues
- Recommended Next Q
- Suggested Commit Message

Human review determines Commit OK / Revision Recommended / Commit NG.

## Purpose

Introduce the Context Recovery Principle as an official GDS design principle.

The principle states that GDS documentation and operational structures must not
assume that a human or AI remembers prior context.

They should instead optimize for rapid, safe recovery from a state of little or
no retained project knowledge.

## Background

Long-running development and server-style operation create a recurring condition:

- systems may remain untouched for months or years,
- maintenance may happen only when an abnormal condition occurs,
- the original operator may have forgotten previous decisions,
- a new AI session may have no chat context,
- a future contributor may have no historical knowledge,
- recovery may happen under fatigue, pressure, or reduced attention.

The practical requirement is therefore not merely good documentation.

The system must remain usable when the reader effectively knows nothing.

Recent GDS improvements already support this direction:

- AI Startup Profile
- Development Context Synchronization
- Product Documentation Hierarchy
- Current Position
- Decision Record
- Q Documents
- Completion Report
- Beginner & Future Self Test

This Q defines the common design principle that connects them.

## Official Principle

Recommended official name:

```text
Context Recovery Principle
```

Canonical statement:

```text
Repository and documentation structures should optimize for context recovery,
not memory retention.
```

Japanese canonical statement:

```text
Repositoryと文書体系は、
利用者が過去を覚えていることではなく、
忘れた状態から安全かつ迅速に現在地へ復帰できることを前提に設計する。
```

## Principle Scope

The Context Recovery Principle applies to:

- Human users
- Future Self
- New AI sessions
- Codex / ChatGPT / Claude / Gemini or other AI collaborators
- New contributors
- Long-term maintenance
- Incident recovery
- Server and infrastructure recovery
- Project resumption after long inactivity
- Handoff between projects or agents

## Required Design Expectations

A GDS-managed artifact or workflow should make it possible to recover:

1. What this artifact or system is
2. Why it exists
3. What the current position is
4. What has already been completed
5. What remains unfinished
6. What decision and evidence led to the current state
7. What action should happen next
8. Where authoritative information is located
9. What actions require Human Approval
10. What must not be changed automatically

## Recovery Scenarios

The principle must explicitly account for at least these scenarios:

### Beginner Recovery

A person or AI with no prior GDS knowledge starts from the canonical entry point.

### Future Self Recovery

The project owner returns after months or years and no longer remembers the
details of previous implementation decisions.

### Incident Recovery

A server, repository, workflow, or automation must be repaired during an abnormal
condition, potentially under time pressure.

### Low-Attention Recovery

The user is tired, distracted, or otherwise unable to reconstruct complex hidden
context.

The documentation should reduce cognitive load without oversimplifying the
technical truth.

### AI Context Loss Recovery

A new AI session begins without prior conversation state and must recover from
Repository sources rather than chat memory.

## Relationship to Existing Standards

### AI Startup Profile

Startup provides the canonical entry point and initializes Development Context.

The Context Recovery Principle explains why Startup must exist.

### Development Context Synchronization

Synchronization restores:

- Repository knowledge
- Current Approved Mission
- Current Information Package
- Current Task
- Human Goal

The Context Recovery Principle defines recovery as the quality objective.

### Product Documentation Hierarchy

The hierarchy distributes recovery responsibilities:

- Product Blueprint: identity and stable direction
- Master Roadmap / Current Position: present state
- Domain / Execution Roadmaps: active work
- Decision Record: why decisions were made
- Q Documents: intended implementation
- Completion Report: actual results and evidence

### Beginner & Future Self Test

The BFS Test verifies whether the Context Recovery Principle is working in
practice.

BFS Test is a quality check.
Context Recovery Principle is the underlying design principle.

### Completion Report

Completion Reports preserve implementation results, evidence, lessons learned,
remaining issues, and recommended next work so that future recovery does not
depend on memory.

## Scope of Changes

### 1. Add Official Design Principle

Create or revise the most appropriate GDS principles document.

Do not create a duplicate Architecture document if an existing Design Principles
or Platform Principles document can be revised.

### 2. Add Discoverability

Ensure the principle is reachable from:

- Repository root README where appropriate
- docs index
- relevant rules / architecture / principles index
- AI Repository Index

### 3. Integrate with Existing Guidance

Add concise references where appropriate to:

- AI Startup Profile
- Product Documentation Hierarchy
- Beginner & Future Self Test
- Completion Report guidance
- Current Position guidance

Do not duplicate full content across all documents.

### 4. Add Examples

Provide at least three concise examples:

- future self returning after years,
- incident recovery on a rarely touched server,
- new AI session recovering without chat history.

### 5. Add Review Guidance

A review should ask:

```text
Can this project or artifact be safely resumed by someone who remembers nothing?
```

If the answer is no, identify the smallest missing recovery aid.

Possible recovery aids include:

- Current Position
- Decision Record
- Completion Report
- canonical entry point
- README navigation
- recovery procedure
- explicit next action
- Human Approval boundary
- known blocker
- last verified state

## Out of Scope

- building a new GUI,
- implementing a recovery dashboard,
- automated incident response,
- full disaster recovery planning,
- backup system implementation,
- server configuration changes,
- mass rewriting existing documentation,
- new Architecture layer,
- GameGhost edits,
- automatic Commit or Push.

## Deliverables

Required:

- request.md
- notes.md
- completion_report.md
- official Context Recovery Principle document or approved revision
- relevant index / README updates
- examples
- BFS Test or related quality guidance cross-reference
- AI Repository Index regeneration and validation
- Repository Quality Report regeneration

Optional only when justified:

- Startup Profile lightweight reference
- Completion Report Rule reference
- Product Documentation Hierarchy reference

If an optional file is unchanged, record `Not Applicable` and why.

## AI Repository Index Update Gate

```text
Yes
```

Required:

- regenerate the AI Repository Index,
- validate it,
- confirm the principle and examples are indexed,
- record representative Raw URL verification as post-Push when applicable.

## Validation

At minimum:

```bash
cd /c/GitHub/Ghost-Development-System-Docs

python scripts/generate_ai_repository_index.py --write
python scripts/generate_ai_repository_index.py --validate
python scripts/validate_encoding_regression.py --all
python scripts/validate_encoding_regression.py --staged
python scripts/repository_quality_audit.py
git diff --check
git status --short
```

Also verify:

- the official name is consistent,
- the Japanese and English principle statements match,
- BFS Test is referenced but not duplicated,
- Startup and Context Synchronization relationships are clear,
- no new Architecture layer is introduced,
- examples cover long absence, incident recovery, and AI context loss,
- GameGhost remains unedited,
- Commit and Push are not executed.

## Safe Commit Set

Expected safe paths:

- README.md
- docs/
- roadmap/
- templates/
- examples/
- reports/repository_quality_report.md
- request workspace

Any file outside these paths requires explicit justification.

Safe Commit Set must match Changed Files.

## Acceptance Criteria

- Context Recovery Principle is formally defined.
- The principle assumes loss of memory and context.
- Long-term maintenance and incident recovery are explicitly covered.
- Future Self and AI context loss are explicitly covered.
- The relationship to Startup, Context Synchronization, Product Documentation
  Hierarchy, BFS Test, and Completion Report is documented.
- The principle is discoverable from canonical indexes.
- At least three practical examples exist.
- The review question is documented.
- No duplicate Architecture is created.
- AI Repository Index validation passes.
- Encoding regression validation passes.
- Repository Quality Audit passes.
- GDS Health validation passes where available.
- git diff --check passes.
- GameGhost remains unedited.
- Commit / Push remain unexecuted.

## Completion Report Requirements

Include:

1. Identity
2. Changed Files
3. Summary
4. Verification
5. Safe Commit Set
6. Commit / Push Status
7. Project Edit Status
8. Principle Added or Revised
9. Canonical Statements
10. Integration Points
11. Examples Added
12. Duplication Avoided
13. BFS Test Relationship
14. Improvement Review
15. Lessons Learned
16. Reusable Assets Created
17. Remaining Issues
18. Recommended Improvements
19. Future Candidates
20. Recommended Next Q
21. Suggested Commit Message

## Future Candidates

- Context recovery dashboard
- Incident recovery runbooks
- Recovery time measurement
- AI cold-start simulation
- stale Current Position detection
- documentation recovery drills
- optional server recovery profiles

Do not implement these in this Q.

## Suggested Commit Message

```text
docs: add context recovery design principle
```
