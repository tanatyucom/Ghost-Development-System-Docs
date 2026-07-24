# Capability Verification Startup Specification

**Version:** 1.0
**Status:** Adopted
**Effective Date:** 2026-07-24

Before planning edits, compare every capability required by the Q with the
capabilities actually available to the executor.

Record for each required capability:

- name and purpose;
- `AVAILABLE`, `UNAVAILABLE`, or `PARTIAL`;
- read/write classification and side effects;
- authority or approval requirement;
- safe fallback;
- SCW condition.

The Startup Capability Report must also identify repository, branch, workspace
status, repository search, GitHub access, Notion access, external knowledge
access, write permission, approval-required operations, and protected scope.

Use `PASS` when every required capability is verified. Use
`PASS_WITH_LIMITATION` when only a nonessential auxiliary capability is missing
and evidence remains sufficient. Use `SCW_REQUIRED` when identity, boundary,
permission, safety, or completion evidence cannot be verified.

Technical capability is not execution authority. An available write tool does
not override a read-only or prohibited policy.
