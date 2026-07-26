# Draft Q Generation Standard

**Version:** 1.1
**Status:** Adopted

## Inputs

Required inputs are Enriched Follow-up Candidate, template version, Repository
Registry, Source Q identity, and Source Completion identity. Each supplied field
records source artifact, source field, value, observed date, freshness,
derivation type, and invalidation condition.

## Output

The output includes Q Identity, Mandatory Execution Context, work definition,
capabilities, deliverables, validation, Startup/SCW/Completion contracts, and
Generator Metadata. Unknown critical fields remain explicit and block approval.

## Generator Metadata

Required: generator version, template version, generated time, source
provenance, inherited/generated/corrected/missing/invalidated fields, warnings,
intent classification, approval state, and approval basis.

For `DRAFT_ONLY`, record `execution_authority: NONE`. For a bounded Q created
from an explicit implementation-oriented Q request, record
`APPROVED FOR IMPLEMENTATION`, `GRANTED AT Q CREATION`, and the user request as
the durable approval basis. This authority ends at Completion Review.

## Question Rule

Ask only for data absent from canonical sources and safe inspection, human
preference among safe alternatives, approval-scope change, or Critical risk.
Every question identifies the missing field, reason, known context, safe options,
free-text option, and blocking state.

## Guarantee

Generation never infers approval from ambiguous or draft-only intent and never
approves Commit, Push, Tag, Release, Registry mutation, cross-repository
mutation, or scope expansion. An explicit request to create and proceed with a
bounded implementation Q grants implementation authority only as defined by
`q_creation_implementation_approval_standard.md`.
