# Approval Resolution Workflow

**Version:** 1.0

```text
Proposed Operation
  -> Identify Approval Unit
  -> Verify Repository / Authority / Boundary
  -> Verify Evidence Freshness
  -> Default Classification
  -> Risk Override
  -> AUTO: execute inside existing authority and record
     PROMPT: ask one focused question, then revalidate
     REQUIRED: obtain explicit approval, then revalidate
     SCW_REQUIRED: stop with resume package
```

Commit, Push, Tag, Release, migration, and destructive operations are resolved
independently. After a human decision, compare the current target and evidence
with the approved target. Material change invalidates only the affected unit.

The execution record must distinguish requested, approved, executed, failed,
and not-executed states. A recommendation is never recorded as execution.
