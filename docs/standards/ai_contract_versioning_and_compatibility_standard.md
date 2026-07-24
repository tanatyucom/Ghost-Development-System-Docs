# AI Contract Versioning and Compatibility Standard

Schemas use Semantic Versioning. The schema `$id` identifies a contract family;
`schema_version` carries `MAJOR.MINOR.PATCH`.

- Major: remove/rename a field, change type or meaning, add a required field,
  remove an enum value, or strengthen validation incompatibly.
- Minor: add an optional field or explicitly extensible enum value, or relax a
  constraint. Enum additions are compatible only where the field documents
  unknown-value handling; otherwise they are major.
- Patch: editorial/schema correction that changes no accepted instance set.

Consumers reject unsupported majors, missing required fields, invalid enums,
unknown required semantics, and digest mismatch. They accept and preserve unknown
optional fields. Higher minor versions may be accepted only when the consumer
declares forward-minor support for that schema family. Deprecated fields remain
readable for at least one major cycle.

Producers declare schema ID/version. Consumers declare supported schema families,
major versions, maximum tested minors, and unknown-field policy. Migration never
rewrites immutable evidence: it emits a new artifact linked to its source. GDS-DOCS
owns meaning and schemas; generated bindings are version pinned and traceable to
the canonical schema digest.
