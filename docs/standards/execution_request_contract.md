# Execution Request Contract

**Status:** Draft Standard

**Last Updated:** 2026-07-17

## Purpose

Execution Request Contract defines the minimum information required before a
Runtime Queue item can be executed or delegated.

## Minimal Shape

```yaml
execution_request:
  request_id: EXR-YYYYMMDD-XXXX
  queue_item_id: EQI-XXXX
  intent_type: COMMIT
  operation: git.commit
  approval_reference:
    approval_request_id: APR-XXXX
    approval_status: ACCEPTED
    approved_scope:
      repository: Ghost-Development-System-Docs
      paths:
        - docs/**
        - templates/**
      exclusions:
        - GameGhost/**
  requested_actor: Codex
  required_capability: git.commit
  dependency_requirements:
    - repository_quality == GREEN
    - git_diff_check == PASS
  evidence_requirements:
    - commit_id
    - commit_message
    - changed_file_summary
  idempotency_key: optional
  destructive_level: LOW
  created_at: ISO-8601
```

## Required Fields

- `request_id`
- `queue_item_id`
- `intent_type`
- `operation`
- `approval_reference`
- `approved_scope`
- `required_capability`
- `evidence_requirements`

Missing required fields block execution.

## Validation

Before execution:

- request ID is stable;
- approval reference is valid;
- approved scope is explicit;
- operation matches queue item;
- actor capability is known;
- dependencies are satisfiable;
- evidence requirements are known.

If validation fails, return `SCW_REQUIRED` or `BLOCKED_INVALID_REQUEST`.
