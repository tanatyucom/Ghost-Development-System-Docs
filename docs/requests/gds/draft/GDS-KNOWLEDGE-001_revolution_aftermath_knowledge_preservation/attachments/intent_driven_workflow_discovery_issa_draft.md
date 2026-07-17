# Intent-Driven Workflow Discovery and GDS Decision Support Evolution

**Artifact Type:** Issa Draft

**Status:** Draft / Not Canonical

**Reason:** Canonical Issa storage and template are not yet standardized.

## Purpose

This draft preserves the reasoning path that led from a small usability problem
to a broader GDS architecture direction.

It is not an implementation request and does not approve runtime work.

## Starting Point

The original concern was simple:

Users should not need to remember the exact word `Startup` or a specific GDS
command in order to safely resume work.

## Expansion Path

```text
Startupを覚えなくてよい入口
  -> 自然言語からWorkflowへ到達
  -> Completion後にCommit候補を判断
  -> Push / Tagも必要性を判断して提案
  -> 「お願いします」をPending Action承認として扱う
  -> 過去の改善とRepository知識に基づく判断支援
  -> 初心者でも経験ある開発フローを利用可能
  -> 人間が忘れることを前提にしたDevelopment System
```

## Core Insight

The system should not depend on perfect human memory or perfect AI context.

GDS should preserve enough repository knowledge that a future user, beginner,
future self, or new AI session can reconstruct:

- where the project is;
- why the current architecture exists;
- what action is safe next;
- what requires Human Approval;
- what must not be executed automatically.

## Design Turn

The design shifted from command shortcuts to decision support.

```text
Command Driven
  Command -> Action

Intent Driven
  Intent -> Evidence Review -> Recommendation -> Approval -> Action
```

This shift matters because `お願いします` cannot safely mean "do whatever seems
next." It can only approve a specific, previously presented Pending Action.

## Reusable Reasoning

The reasoning is reusable beyond Intent-Driven Workflow:

- preserve why, not only what;
- treat future self as a real user;
- use repository knowledge before AI guesses;
- separate recommendation from execution;
- require Human Approval for mutating actions;
- use reason codes when making recommendations;
- create child Qs when architecture discovery exceeds implementation scope.

## Rejected Paths

### Direct Natural Language Execution

Rejected because it bypasses repository state, scope, and Human Approval.

### Commit Automation First

Rejected because Git operation automation before Pending Action and Approval
Context would turn a usability improvement into a safety risk.

### Many Separate Issa Files Immediately

Rejected for now because canonical Issa storage is not standardized and
over-fragmentation would make review harder.

## Current Recommendation

Keep this as a single parent Issa draft until Issa storage and template are
standardized.

Possible future child Issa:

- Forgetfulness-First and Future Self.
- Knowledge-Guided Beginner Development.
- Pending Action Approval Safety.

## Related Artifacts

- `docs/architecture/intent_driven_workflow.md`
- `docs/architecture/intent_registry_and_pending_action_contract.md`
- `docs/architecture/knowledge_artifact_responsibility_map.md`
- `docs/workflow/knowledge_preservation_gate.md`
- `docs/adr/ADR-GDS-005_context_reconstruction_and_knowledge_guided_recommendations.md`
