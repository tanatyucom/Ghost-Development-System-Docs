# Canonical Draft Q Generator

**Status:** Adopted Design
**Version:** 2.0

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

## Processing Architecture

```text
Input Admission
  -> Source Identity and Freshness Validation
  -> Repository Registry Lookup
  -> Field-level Context Precedence
  -> Invalidation and Safe Correction
  -> Missing-input Classification
  -> Canonical Section Mapping
  -> Non-executable Draft Envelope
  -> Human Review and Template Validation
```

## Required Inputs

An Enriched Follow-up Candidate, Canonical Q Template version, Repository
Registry, Source Q identity, and Source Completion Report identity are required.
Handover state, Startup evidence, notes, related/dependency Qs, and explicit
Human Decisions are conditional inputs.

## Field-level Precedence

1. Explicit Human Decision.
2. Current Approved Q.
3. Canonical Repository Registry.
4. Current Completion Report.
5. Current Handover Project State.
6. Enriched Follow-up Candidate.
7. Source Q.
8. Canonical standards and rules.
9. Previous Draft Q.
10. Conversation summary.

Precedence is applied per field, never by replacing an entire higher-quality
artifact with a lower-order artifact. Critical conflict remains visible and
returns `SCW_REQUIRED`.

## Repository Lookup

Only an Active, Verified Registry entry may supply a mutation-target candidate.
Planned or Pending entries produce `Repository Assignment: UNKNOWN / Planned`,
`Execution Authority: NONE`, and an activation/approval missing input. Supported
roles are capabilities; the generated Q must still declare its assigned roles.

## Missing-input Outcomes

- Non-blocking: `Draft Ready` with warnings.
- Human preference or multiple safe candidates: `Review Required` with minimal questions.
- Critical execution context or authority missing: `Incomplete`, execution prohibited.

## Non-executable Envelope

Every generated artifact states:

```text
Status: Draft
Execution Authority: NONE
Approval Status: NOT APPROVED
Startup: NOT PERMITTED
Mutation: NOT PERMITTED
```

No Completion PASS, Registry Mutation Class, or inherited approval can change
this envelope. Human approval and subsequent Startup GO are separate gates.
