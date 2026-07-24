# Handover Context Contract

**Status:** Adopted
**Version:** 1.0

## Decision

Adopt Context Contract as a mandatory Handover Framework v2 section. It freezes
the effective vocabulary and boundaries for the receiving session; it does not
grant execution authority.

## Required Fields

- repository Name, ID, Type, Purpose, Role, Root, and revision;
- Workspace Root, Execution Root, Working Directory, and Boundary;
- validation and reference repositories;
- Execution Mode and Mutation Authority;
- allowed and prohibited paths / operations;
- approval scope and invalidation conditions;
- Commit, Push, Tag, and Release state;
- terminology definitions and aliases;
- source priority, freshness, unresolved conflicts, and SCW conditions.

The contract must distinguish `SOURCE`, `TARGET`, `VALIDATION`, `OUTPUT`, and
`REFERENCE`. The same repository may hold multiple roles, but each role and the
resulting independence limitation must be explicit.

Missing or conflicting material context makes the handover `SCW_REQUIRED`.
