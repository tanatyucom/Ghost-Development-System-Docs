# Adapter Registry Foundation

**Status:** Draft Standard

**Last Updated:** 2026-07-17

## Purpose

Adapter Registry Foundation defines the minimum registry information needed to
select a governed execution adapter safely.

This is not an implementation or runtime database.

## Minimal Record

```yaml
adapter:
  adapter_id: git.codex.v1
  version: v1
  supported_capability: git.commit
  supported_actor:
    - Codex
  input_contract: execution_request
  output_contract: execution_result
  evidence_contract:
    - commit_id
    - changed_file_summary
  authority_requirement: explicit_human_approval
  destructive_level: LOW
  retry_policy: manual_review
  idempotency_policy: duplicate_commit_risk
  availability_state: DESIGN_ONLY
  implementation_status: DESIGN_ONLY
```

## Availability States

- `DESIGN_ONLY`
- `AVAILABLE`
- `UNAVAILABLE`
- `DEPRECATED`
- `DISABLED`

## Capability Registry Boundary

Adapter Registry may connect to a future Capability Registry, but this Q does
not implement that registry.

Capability records should identify:

- capability ID;
- adapter ID;
- actor types;
- supported operations;
- evidence types;
- destructive level;
- approval requirement;
- runtime status.

## Reference Profiles

- `docs/standards/git_adapter_registry_profile.md`: Git Commit, Push, Tag
  Create, and Tag Push documentation profile for the Git Execution Adapter
  Vertical Slice.
