# Good Q Example

Version: 1.0

Status: Documentation Update Request

Workflow: Development Workflow Version 2.0 Trial

Category: Documentation / Templates

Priority: High

Commit:

```text
Do not commit unless explicitly requested.
```

## Repository Information

### Repository

Ghost-Development-System-Docs

### Working Directory

```text
C:\GitHub\Ghost-Development-System-Docs
```

### Documentation Root

```text
C:\GitHub\Ghost-Development-System-Docs\docs
```

### Runtime Root

Not in scope.

### Single Source Of Truth

Ghost-Development-System-Docs

### Related Repository

GameGhost: reference only. Do not edit, sync, or copy files.

### Scope Guard

Edit only:

- `docs/templates/`
- `docs/examples/`

Do not edit:

- Runtime Code.
- GameGhost.
- Git Migration.
- Queue.
- Roadmap.
- Rules.

## Purpose

Improve the Q file template so future documentation requests identify the
repository, documentation root, and edit boundary before asking AI to work.

## Background

AI sometimes confuses active repositories when a task mentions both the public
knowledge base and a related implementation repository.

Repository Information should prevent that confusion.

## Approved Decisions

- Q files should include Repository Information near the top.
- Documentation-only work should explicitly mark Runtime Root as not in scope.
- Related repositories may be referenced but must not be edited unless the Q
  explicitly says so.

## Naming Policy

Use purpose-oriented names for public template sections.

Use implementation terms only when they clarify the current method.

## Scope

Documentation update only.

## Do

- Update `docs/templates/q_file_template.md`.
- Update `docs/templates/README.md` if needed.
- Add or update examples only if they clarify the standard.

## Do Not

- Do not modify runtime code.
- Do not edit GameGhost.
- Do not perform Git migration.
- Do not commit.

## Target Files

- `docs/templates/q_file_template.md`
- `docs/templates/README.md`
- `docs/examples/`

## Completion Criteria

- Repository Information is included in the template.
- Completion Criteria are included in the template.
- Related repository boundaries are clear.
- Commit is not created.
- Changed files, verification, remaining issues, and suggested commit message
  are reported.

## Review Requests

Review for:

- repository boundary clarity;
- AI execution safety;
- template reusability;
- public knowledge base quality.

## Deliverables

- Changed Files.
- Summary.
- Verification.
- Remaining Issues.
- Recommended Improvements.
- Future Candidates.
- Recommended Next Q.
- Suggested Commit Message.

## Improvement Review

Review whether this work reveals reusable improvements for:

- Documentation.
- Templates.
- Workflow.
- Roadmap.
- Rules.
- Architecture.
- Knowledge Base.

### Recommended

List improvements that should be adopted soon.

### Future Candidates

List useful ideas that should remain future work.

## Suggested Commit Message

```text
docs: standardize repository information in q template
```
