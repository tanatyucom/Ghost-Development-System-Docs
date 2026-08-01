# Approval Policy Standard

**Version:** 2.0
**Status:** Adopted
**Effective Date:** 2026-07-24

## Classification

| Level | Meaning | Typical condition |
| --- | --- | --- |
| `AUTO` | Continue without a new prompt. | Already authorized, low risk, bounded, unique, reversible or read-only. |
| `PROMPT` | Ask one focused preference/operation question. | Multiple safe choices, minor scope choice, normal external synchronization. |
| `REQUIRED` | Obtain explicit approval before execution. | High impact, irreversible, destructive, publication, migration, release, secrets, cost. |

Classification is mutually exclusive for one approval unit. `SCW_REQUIRED` is
a separate uncertainty state, not a fourth approval level.

## Evaluation Order

1. Identify repository, operation, target, and approval unit.
2. Verify current authority and workspace boundary.
3. Verify evidence freshness and absence of conflicts.
4. Apply the default operation classification.
5. Apply the risk override; overrides only increase required human control.
6. Record result, reason, evidence, and invalidation conditions.

## Defaults

| Operation | Default |
| --- | --- |
| Read-only inspection | `AUTO` |
| Approved documentation mutation inside declared paths | `AUTO` |
| Startup, validation, report, index, or Safe Commit Set generation inside scope | `AUTO` |
| Safe and unique context correction | `AUTO` |
| Naming, grouping, timing, or multiple-safe-choice decision | `PROMPT` |
| Normal Commit after PASS | `PROMPT` unless a governed workflow explicitly includes it |
| Normal Push to the expected branch | `PROMPT` |
| New branch | `PROMPT` |
| Migration, Release, Tag, destructive Git, boundary change, DB mutation | `REQUIRED` |

## Approval Unit Separation

Commit, Push, Tag, Release, migration, external write, and destructive action
are distinct units. Approval for one does not approve another. A changed commit
set invalidates Commit approval; a changed local/remote relationship invalidates
Push approval.

When a fallback changes the execution subject, effect approval and fallback
approval are also separate units. Approval of Commit or Push does not approve
Codex or another non-equivalent executor. See
`codex-non-substitution-and-fallback-disclosure.md`.

## Audit Evidence

Record operation, repository, target, classification, default, risk override,
authority source, evidence sources, correction if any, human decision if any,
timestamp, and invalidation result.

## Prohibitions

- Never treat tool availability as approval.
- Never use `AUTO` to expand authority or repository scope.
- Never downgrade Critical or irreversible work.
- Never bundle independent approval units to reduce prompts.
- Never ask again when a fresh, unambiguous approval already covers the exact unit.
