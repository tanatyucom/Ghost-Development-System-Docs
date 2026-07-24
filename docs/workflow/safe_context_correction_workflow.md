# Safe Context Correction Workflow

**Version:** 1.0

## Flow

```text
Observed Difference
  -> Locate Canonical Sources
  -> Read-only Repository Verification
  -> Test Uniqueness, Boundary, Authority, Reversibility
  -> Exact: continue
     Safe + Unique: correct and record
     Multiple Safe: PROMPT
     Unsafe / Conflicting: SCW_REQUIRED
```

The correction record contains original value, corrected value, canonical
source, verification command or method, reason it is unique, affected scope,
and invalidation condition. Correction never changes Mutation Authority,
Approval Scope, repository identity, or an external target.

Examples of eligible corrections are path/case normalization and unique branch
detection from `origin/HEAD`. A directory name alone is not repository identity.
