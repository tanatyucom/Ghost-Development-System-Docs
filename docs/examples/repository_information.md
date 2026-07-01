# Repository Information Example

## Purpose

This example shows how to define repository boundaries before asking AI to edit
documents.

Use this pattern when a request mentions multiple repositories, runtime roots,
documentation roots, or reference-only sources.

## Repository Information

### Target Project

Ghost Development System.

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

GameGhost.

Reference only.

Do not edit, sync, copy, or migrate files.

### Cross Project Impact

Reference Only.

GameGhost may be referenced to explain boundaries, but this Q does not edit
GameGhost or change GameGhost runtime behavior.

### Scope Guard

Edit only:

- `docs/examples/`
- `docs/templates/`, only if necessary.
- `README.md`, only if necessary.

Do not edit:

- Runtime Code.
- GameGhost.
- Git Migration.
- Queue.
- Roadmap.
- Rules.

## Completion Criteria

- Only files allowed by Scope Guard are changed.
- Runtime Code is not changed.
- GameGhost is not edited, synced, or copied.
- Git Migration is not performed.
- Commit is not created.
- Changed files are reported.
- Verification is reported.
- Remaining Issues are reported.
- Suggested Commit Message is provided.

## Review Checklist

- Is the active repository named?
- Is the Target Project named?
- Is the working directory absolute?
- Is the documentation root absolute?
- Is Runtime Root marked as not in scope when documentation-only?
- Is Single Source Of Truth explicit?
- Are related repositories marked as edit or reference only?
- Is Cross Project Impact explicit?
- Does Scope Guard list what can and cannot be edited?
- Are completion criteria concrete enough to verify?
