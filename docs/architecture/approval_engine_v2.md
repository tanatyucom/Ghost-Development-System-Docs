# Approval Engine v2

**Status:** Adopted Design
**Version:** 2.0
**Effective Date:** 2026-07-24

## Purpose

Approval Engine v2 reduces governance friction without expanding authority. It
classifies a proposed operation as `AUTO`, `PROMPT`, or `REQUIRED` from the
operation, risk, current evidence, and already-approved scope.

## Design Principles

- Governance exists to accelerate safe development.
- Every manual step requires a stated safety or preference reason.
- AI performs obvious work when canonical evidence makes the result unique.
- Capability never grants authority.
- Automation may consume approval evidence but may not invent it.

## Decision Pipeline

```text
Canonical Context + Current State + Proposed Operation
  -> Boundary and Authority Check
  -> Evidence Freshness Check
  -> Operation Classification
  -> Risk Override
  -> AUTO / PROMPT / REQUIRED / SCW_REQUIRED
  -> Audit Record
```

`AUTO` means no new human prompt is required because the operation is already
authorized, bounded, reversible or non-mutating, and uniquely determined.
`PROMPT` asks for a preference or a distinct external synchronization decision.
`REQUIRED` requires explicit approval for high-impact or irreversible work.
`SCW_REQUIRED` is not an approval level; it means safe classification cannot be
determined from reliable evidence.

## Safety Invariants

1. Risk may raise an approval level but never lower it.
2. Inherited approval cannot outlive a material change in repository, branch,
   scope, authority, risk, or source evidence.
3. `AUTO` cannot expand paths, capabilities, repositories, or mutation class.
4. Commit, Push, Tag, and Release remain separate approval units.
5. External publication and destructive operations are never `AUTO`.
6. Every result records inputs, classification, reason, and invalidation check.

## Safe Auto-Correction

```text
Exact Match -> continue
Safe + Unique + Bounded -> correct, record evidence, continue
Multiple Safe Candidates -> PROMPT
Unsafe, Conflicting, or Boundary-changing -> SCW_REQUIRED
```

Safe candidates include path separator normalization, case normalization on a
case-insensitive filesystem, unique `origin/HEAD` resolution, verified
repository-root/subdirectory relationships, and context copied from a fresh
canonical artifact. Correction is prohibited when it would select another
repository, elevate authority, hide dirty changes, read secrets, infer an
external target, or choose between equally valid candidates.

## Context Inheritance

Context may be inherited only with source identity and freshness evidence.
Repository identity, roots, branch basis, workspace boundary, role, execution
mode, mutation authority, capability classification, Git policies, project
state, Safe Commit Set, and enriched follow-up data are inheritable.

Inheritance is invalid when repository, root, branch, workspace state, scope,
authority, risk, source availability, or an explicit human decision changes.
Invalidation returns the affected field to validation; it does not erase other
still-valid context.

## Relationship to Existing Architecture

- `approval_runtime_state_machine.md` owns runtime approval state transitions.
- `approval_request_intent_queue_execution_evidence.md` owns intent and evidence.
- This document owns classification and friction boundaries.
- Runtime implementation is outside this design.

## Related Documents

- `docs/standards/approval_policy_standard.md`
- `docs/rules/scw_applicability_rules_v2.md`
- `docs/workflow/approval_resolution_workflow.md`
- `docs/workflow/safe_context_correction_workflow.md`
- `examples/approval_policy_examples.md`
