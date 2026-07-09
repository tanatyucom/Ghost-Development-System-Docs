# Authority Matrix Example

## Purpose

This example shows how to document edit authority when a Q mentions multiple
repositories or source roots.

Use it when Repository Information and Scope Guard need a clearer table.

## Authority Types

Editable:

The current Q may modify this target.

Reference Only:

The current Q may read or mention this target, but must not modify, sync, copy,
or migrate it.

Forbidden:

The current Q must not edit, sync, copy, migrate, or operate on this target
unless a later Q explicitly changes scope.

Single Source Of Truth:

The authoritative source for the current Q.

## Example Matrix

| Target | Authority | Notes |
|---|---|---|
| Ghost Development System | Target Project | Parent development foundation for the current Q. |
| Ghost-Development-System-Docs | Editable / Single Source Of Truth | Public Knowledge Base for the current Q. |
| `docs/` | Editable | Documentation root. |
| `docs/examples/` | Editable | Example library. |
| `docs/templates/` | Editable if listed in scope | Template updates only when necessary. |
| GameGhost | Reference Only | Do not edit, sync, copy, or migrate. |
| Runtime Code | Forbidden | Not in documentation-only scope. |
| Git Migration | Forbidden | Requires separate approval. |
| GitHub Actions | Forbidden | Requires separate approval. |
| Release | Forbidden | Requires separate approval. |

## Review Checklist

- Is the Single Source Of Truth explicit?
- Is the Target Project explicit?
- Are editable paths listed narrowly?
- Are related repositories marked Reference Only when appropriate?
- Is Cross Project Impact explicit?
- Are forbidden areas explicit?
- Does the matrix match the Scope Guard?
- Does the final report confirm these boundaries were respected?
