# Repository Registry Standard

**Version:** 1.0
**Status:** Adopted

## Registry Header

Required: `registry_id`, `version`, `status`, `last_updated`, `owner`,
`human_authority`, `source_of_truth`, `schema`, `entries`, and
`validation_rules`.

## Entry Fields

| Field | Rule |
| --- | --- |
| `repository_id` | Required, stable, unique. |
| `name`, `type`, `status`, `purpose` | Required. |
| `canonical_root` | Required for Active with fixed root; `null` for unresolved Planned. |
| `root_policy` | `fixed`, `machine-specific`, or `unresolved`. |
| `machine_roots` | Required only for machine-specific policy. |
| `default_branch_basis` | `explicit`, `origin/HEAD`, or `unresolved`. |
| `default_branch` | Required when basis is explicit and status is Active. |
| `supported_roles` | Non-empty subset of SOURCE/TARGET/OUTPUT/VALIDATION/REFERENCE. |
| `mutation_class` | NONE/DOCUMENTATION_ONLY/SAFE/NORMAL/CONTROLLED. |
| `owner` | Required governance authority. |
| `hosting`, `remote_identity` | Conditional; unresolved may be `null`. |
| `last_verified`, `verification_status`, `verification_method`, `verified_by` | Required freshness evidence. |
| `provenance` | Non-empty source list. |
| `notes` | Optional clarification list. |

## Constraints

- Active entries require verified identity, owner, root policy, and branch basis.
- Planned entries use Mutation Class `NONE` and cannot be execution targets.
- Suspended and Archived entries cannot be mutation targets.
- Duplicate IDs are invalid regardless of name or path.
- `UNKNOWN` is represented as YAML `null` plus Pending/Conflict evidence, never
  as an invented string value.
- Supported roles are capability only; Q role assignment remains mandatory.
- Mutation Class never elevates Q Mutation Authority.

## Validation Result

Schema or evidence conflict produces `SCW_REQUIRED`; a known invalid field
produces `BLOCK` until corrected. Formatting-only differences may be normalized
and recorded without changing semantic values.
