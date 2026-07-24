# Canonical Draft Q Generator

**Status:** Adopted Design
**Version:** 1.0

## Purpose

Define how an enriched follow-up becomes a complete, reviewable Canonical Q
draft without repeatedly asking for context already present in canonical
sources. This is a documentation contract, not a runtime generator.

## Inputs and Precedence

```text
Enriched Follow-up Candidate
  -> Source Q and Completion Report
  -> Handover Project State
  -> Repository Registry
  -> Canonical Q Template and Standards
  -> Current read-only Repository State
```

Conflicts follow repository canonical precedence and are surfaced; lower-order
sources never silently overwrite higher-order sources.

## Output Contract

The generated draft contains Identity, Repository Assignment, Mandatory
Execution Context, Capability Matrix, Objective, Scope, Out of Scope,
Deliverables, Validation, SCW Conditions, Completion Contract, known
placeholders, missing inputs, and provenance for inherited values.

Generation produces `Draft`, never `Approved Q`. Template Validation and Human
Approval remain mandatory lifecycle gates.

## Question-Minimization Rule

Ask only when a required value is absent from canonical sources and repository
inspection, multiple safe values remain, a human preference changes the result,
approval scope would expand, or Critical risk is involved. Known context must
be reused with provenance rather than re-entered.

## Context Inheritance Record

Each inherited field records source artifact, source revision or freshness,
value, validation method, and invalidation condition. Derived fields record the
derivation. Unknown values remain `UNKNOWN`; the generator does not invent a
repository or authority from a name.

## Completion Condition

A draft is `Draft Ready` only when all mandatory fields are present or every
missing input is explicitly listed. It becomes executable only after Template
Validation returns `ISSUE_OK` and Human Approval changes status to Approved.

## Related Documents

- `docs/standards/follow_up_candidate_contract.md`
- `docs/workflow/follow_up_to_draft_q_workflow.md`
- `templates/follow_up_candidate_template.md`
- `templates/Q_TEMPLATE.md`
