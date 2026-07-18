# Execution Authority Registry Schema

**Status:** Draft Standard

**Last Updated:** 2026-07-18

## Purpose

This standard defines the required fields for
`docs/registries/execution_authority_registry.yaml`.

The schema is documentation-level. It does not implement JSON Schema, YAML
validation code, or runtime enforcement.

## Registry Header

Required fields:

```yaml
registry_id:
version:
status:
last_updated:
source_of_truth:
human_readable:
principle:
authority_categories:
lifecycle_states:
actors:
approval_units:
validation_rules:
```

## Actor Entry

Required fields:

```yaml
actor_id:
actor_name:
actor_type:
status:
repository_scope:
authorities:
human_approval_requirement:
risk_level:
scw_conditions:
source_of_truth:
```

`actor_id` must be stable and unique.

Allowed actor types:

- ReviewActor
- ExecutionActor
- HumanAuthority
- AutomationActor
- Adapter
- Tool
- SDK
- Capability

## Authority Fields

Each actor entry should define:

```yaml
authorities:
  observe:
  analyze:
  recommend:
  request_approval:
  execute_git:
  mutate_repository:
  produce_execution_evidence:
  produce_review_evidence:
```

Allowed values are intentionally small:

- `Yes`
- `No`
- `Limited`
- `Conditional`
- `NotApplicable`
- domain-specific qualified values such as `YesWhenApproved`

Qualified values must be explained by `source_of_truth` documents.

## Approval Unit Entry

Required fields:

```yaml
approval_unit:
execution_actor:
approval_request_actor:
required_human_authority:
evidence_type:
risk_level:
default_recommendation_policy:
```

The `execution_actor` and `approval_request_actor` must resolve to registered
actor IDs.

## Validation Rule Entry

Required fields:

```yaml
rule_id:
statement:
failure_result:
```

Recommended failure results:

- `BLOCKED`
- `SCW_REQUIRED`
- `BLOCKED_OR_SCW_REQUIRED`

## Consistency Rules

- Approval Request Authority requires matching Execution Authority.
- Mutation Authority requires defined repository or resource scope.
- High-risk Execution Authority requires Human Approval Requirement.
- Execution Authority requires Evidence Responsibility.
- Recommendation Authority does not imply Execution Authority.
- Unknown or conflicting authority must stop with SCW.

## Human-Readable View

The canonical source is YAML. Human-readable documents should not duplicate the
whole registry unless necessary. They should summarize:

- purpose;
- authority categories;
- initial actor model;
- Approval Unit mapping;
- validation rules;
- lifecycle;
- related documents.
