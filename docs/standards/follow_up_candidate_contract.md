# Follow-up Candidate Contract

**Version:** 1.0
**Status:** Adopted

## Rule

A Completion Review must not leave a follow-up as a name alone. A candidate is
usable for the next session only when it carries enough design and execution
context to generate a Canonical Q draft without reconstructing intent.

## Mandatory Fields

Candidate ID; Title; Source Q; Source Completion Report; Problem or Opportunity;
Objective; Scope; Out of Scope; Repository Assignment; Expected Execution Mode;
Expected Mutation Authority; Required Capabilities; Dependency; Resume
Condition; Known Inputs; Missing Inputs; Risk; Priority; Recommended Approval
Level; Suggested Q ID; Suggested Artifact Path.

## Lifecycle

```text
Observed -> Enriched -> Draft Ready -> Approved -> Executing -> Completed
                                      \-> Rejected / Deferred
```

`Observed` is permitted during work. Completion may publish a recommended next
Q only when it is at least `Enriched`. Unknown values are explicit and do not
become guessed facts.

## Validation

- Every mandatory field exists or says `UNKNOWN` with a resolution owner.
- Scope and Out of Scope do not overlap.
- Repository assignment names an identity, not only a directory.
- Approval recommendation does not grant approval.
- Source references allow reconstruction of rationale and current state.
