# Repository Identity Standard

**Version:** 1.0
**Status:** Adopted

## Identity

A repository identity is established by a unique `repository_id`, canonical
name, lifecycle status, ownership, and provenance. Paths, directory names,
workspace names, remotes, and branch names are evidence, not identity by
themselves.

## Root Policies

- `fixed`: one verified local root for the governed environment.
- `machine-specific`: one identity with explicit `machine_id -> local_root`
  mappings.
- `unresolved`: no root claim; permitted for Planned or Pending entries only.

An Active mutation target must resolve exactly one root for the current machine.
No match, multiple matches, or a Git root mismatch requires SCW.

## Repository Evidence

Verification should use read-only Git evidence: top level, current/default
branch basis, remote identity when applicable, and revision. Command-scoped
safe-directory configuration is permitted when it does not persist configuration
or mutate the inspected repository.

## Provisional Identity

A Planned concept may use an explicitly provisional ID. Promotion to Active
requires a Human-approved identity review. A provisional entry cannot authorize
creation, initialization, migration, or remote configuration.
