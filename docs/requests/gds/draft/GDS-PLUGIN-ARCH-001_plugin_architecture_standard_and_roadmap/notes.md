# Notes

## Scope Confirmation

- Target Project: Ghost Development System.
- Repository: `C:\GitHub\Ghost-Development-System-Docs`.
- Related Repository: GameGhost reference only.
- Commit policy: do not commit.

## Design Decision

Plugin is treated as a reviewed Platform extension unit, not as any importable
module.

Phase 1 uses explicit registry only. Automatic discovery is intentionally out of
scope.

## First Proof Target

```text
repository_context_validation
```

Reason:

- low coupling;
- supports Startup Checklist and Repository Root Validation;
- no GameGhost database dependency;
- reusable by future Ghost projects.
