# Repository Freshness and Verification Standard

**Version:** 1.0
**Status:** Adopted

## States

- `Verified`: evidence is current enough for the intended use.
- `Stale`: known identity may support read-only reference with warning; mutation prohibited.
- `Pending`: verification not completed; execution target prohibited.
- `Conflict`: observed evidence contradicts Registry; SCW required.

## Required Evidence

Each entry records `last_verified`, `verification_status`,
`verification_method`, and `verified_by`. Active entries also record a revision
or equivalent evidence in provenance/notes when locally verified.

## Use Rules

- Mutation target: Active + Verified + unique root mapping.
- Read-only reference: Stale may be used with an explicit warning.
- Planned/Pending: design reference only.
- Conflict: do not inherit or auto-correct affected fields.

Freshness is purpose-sensitive. A prior identity check does not prove a current
clean workspace, approval, or branch safety.
