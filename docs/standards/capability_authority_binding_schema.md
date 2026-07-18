# Capability / Authority Binding Schema

**Status:** Draft Standard

**Last Updated:** 2026-07-18

## Purpose

This standard defines the fields used by:

```text
docs/registries/capability_authority_bindings.yaml
```

It is documentation-level. It does not implement runtime parsing or automated
schema validation.

## Registry Header

Required fields:

```yaml
registry_id:
version:
status:
last_updated:
source_of_truth:
related_registries:
human_readable:
principle:
capability_classes:
lifecycle_states:
capabilities:
bindings:
validation_rules:
resolution_matrix:
```

## Capability Entry

Required fields:

```yaml
capability_id:
capability_name:
provider:
provider_type:
capability_class:
lifecycle_status:
risk_level:
resource_scope:
input_contract:
output_contract:
evidence_capability:
```

Allowed lifecycle statuses:

- Available
- Unavailable
- Conditional
- Deprecated
- Revoked
- Unknown
- Draft
- Active

## Binding Entry

Required fields:

```yaml
binding_id:
capability_id:
capability_provider:
execution_actor:
authority_type:
authority_registry_actor:
resource_scope:
approval_unit:
human_approval_requirement:
evidence_type:
risk_level:
scw_conditions:
status:
source_of_truth:
```

The `capability_id` must resolve to a capability entry.

The `authority_registry_actor` must resolve to an actor entry in:

```text
docs/registries/execution_authority_registry.yaml
```

## Validation Rules

Minimum rules:

- Execution requires Active Capability and Active Authority.
- Capability Provider must match registered Execution Actor or delegated Tool.
- Capability Scope must be equal to or narrower than Authority Scope.
- Approval Request Capability requires matching Execution Capability and
  matching Execution Authority.
- Mutation Capability requires Mutation Authority and defined Resource Scope.
- High-risk Capability requires Human Approval Mapping.
- Execution Capability requires Evidence Capability or Evidence Provider.
- Deprecated / Revoked / Unknown Capability requires SCW.
- Authority exists but Capability is missing means Blocked.
- Capability exists but Authority is missing means SCW.

## Resolution Results

Recommended result values:

- `Executable`
- `PendingApproval`
- `Blocked`
- `SCW_REQUIRED`
- `DelegationRequired`
- `EvidenceMissing`

## Non-Goals

- Runtime validation code.
- YAML schema enforcement.
- External registry database.
- Git Runtime changes.
