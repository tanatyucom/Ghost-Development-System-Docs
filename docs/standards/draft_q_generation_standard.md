# Draft Q Generation Standard

**Version:** 1.0
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
draft status, and `execution_authority: NONE`.

## Question Rule

Ask only for data absent from canonical sources and safe inspection, human
preference among safe alternatives, approval-scope change, or Critical risk.
Every question identifies the missing field, reason, known context, safe options,
free-text option, and blocking state.

## Guarantee

Generation never approves, executes, commits, pushes, activates a Planned
repository, elevates authority, or guesses critical input.
