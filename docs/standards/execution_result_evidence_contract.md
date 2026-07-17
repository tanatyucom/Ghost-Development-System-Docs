# Execution Result / Evidence Contract

**Status:** Draft Standard

**Last Updated:** 2026-07-17

## Purpose

Execution Result / Evidence Contract defines how an adapter reports execution,
delegation, failure, partial success, or unknown state back to Runtime Queue.

## Minimal Shape

```yaml
execution_result:
  request_id: EXR-YYYYMMDD-XXXX
  queue_item_id: EQI-XXXX
  adapter_id: git.codex.v1
  actor: Codex
  status: SUCCEEDED
  started_at: ISO-8601
  finished_at: ISO-8601
  exit_code: 0
  evidence:
    commit_id: abcdef123456
    commit_message: "docs(intent): define runtime intent queue resolver foundation"
    changed_files:
      - docs/architecture/...
      - docs/workflow/...
  verification:
    evidence_complete: true
    scope_match: true
    dependency_match: true
  retry:
    retryable: false
    idempotency_risk: none
  message: structured summary
```

## Result Status

- `SUCCEEDED`
- `FAILED`
- `PARTIAL`
- `UNKNOWN`
- `DELEGATED`
- `WAITING_FOR_EVIDENCE`
- `BLOCKED`
- `SCW_REQUIRED`

`SUCCEEDED` is not enough for `COMPLETED` if required evidence is missing.

## Evidence Requirements

Commit evidence:

- commit ID;
- commit message;
- changed file summary;
- repository;
- branch;
- actor.

Push evidence:

- remote;
- branch or ref;
- pushed commit ID;
- push result;
- actor.

Tag evidence:

- tag name;
- target commit;
- local creation result;
- remote push result when requested.

Artifact evidence:

- artifact path;
- artifact type;
- created or revised;
- validation result;
- canonical or draft status.

## Unknown Handling

Unknown result requires SCW. Do not infer success.
