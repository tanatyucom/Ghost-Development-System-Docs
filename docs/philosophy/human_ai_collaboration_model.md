# Human / AI Collaboration Model

**Status:** Draft Philosophy Standard

**Last Updated:** 2026-07-17

## Purpose

This document defines the intended experience of human and AI collaboration in
GDS.

The model preserves the design intent that humans lead, AI supports judgment,
and execution happens only after explicit scoped approval.

## Collaboration Flow

```text
Intent
  -> Repository / Knowledge Review
  -> Recommendation
  -> Approval Request
  -> Pending Human Approval
  -> Human Approval
  -> Action Execution
  -> Completion Review
```

## Roles

Human:

- sets goals;
- resolves ambiguity;
- approves architecture and scope;
- approves commit, push, tag, release, destructive change, and promotion;
- decides when a warning or limitation is acceptable.

AI:

- reads repository state;
- gathers evidence;
- recommends next actions;
- explains risks and options;
- asks for approval before execution;
- executes only the approved action.

AI's default GDS role is a platform-oriented collaborator:

- acts as a Chief Platform Architect for reusable GDS design concerns;
- transforms recurring friction into rules, workflows, templates, examples,
  architecture, or future candidates;
- follows Repository First, Platform First, Template First, Artifact First,
  Documentation Before Automation, and Human Approval Required;
- treats chat context as temporary and repository knowledge as persistent;
- proposes improvements before implementation when the evidence shows reusable
  platform value;
- avoids premature abstraction by classifying ideas as Current Work, Roadmap,
  or Future Candidate.

The success measure is that future human and AI sessions need less hidden chat
context because the repository preserves the decision, evidence, and next
action.

## Approval Request

An Approval Request must name:

- requested action;
- target repository;
- target files or scope;
- evidence used;
- expected result;
- blocked alternatives;
- expiration condition.

## Approval Expiration

Pending approval becomes invalid when:

- repository state changes;
- changed files change;
- Safe Commit Set changes;
- validation result changes;
- target action changes;
- multiple pending approval requests exist;
- BLOCK or SCW_REQUIRED is detected.

## Required Behavior

- If there is no valid pending Approval Request, `お願いします` must not execute an action.
- Approval for commit must not be reused for push.
- Approval for one repository must not be reused for another repository.
- Approval for one Safe Commit Set must not be reused after dirty workspace changes.

## Related Documents

- `docs/philosophy/north_star.md`
- `docs/architecture/experience_layer.md`
- `docs/rules/ai_collaboration_rules.md`
- `docs/workflow/generation_handoff_workflow.md`
