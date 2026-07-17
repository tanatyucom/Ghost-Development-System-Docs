# Completion Review Integration Specification

## Purpose

Define how Completion Review should surface Knowledge Promotion candidates
without silently promoting them.

## Review Prompt

```text
Knowledge Promotion Check

The result contains promotion candidates:

- Candidate type:
- Summary:
- Evidence:
- Proposed target:
- Duplicate check:
- Approval needed:

Add these as governed promotion work?
```

## User Approval Meaning

If the user says `お願いします`, `はい`, or `OK` after exactly one clear
Knowledge Carry-Forward Pending Action, the approval means:

```text
Register the identified candidates as governed promotion work.
```

It does not approve:

- ADR acceptance;
- canonical Issa publication;
- Rule mutation;
- commit;
- push;
- tag;
- release;
- cross-repository edits.

## Completion Review Checklist Additions

- Knowledge candidate detected:
- Candidate type:
- Evidence:
- Duplicate check:
- Proposed promotion target:
- Carry-forward target:
- Human Approval status:
- Canonical promotion status:
- Application target:
- Remaining promotion work:

## SCW Cases

Apply SCW when:

- more than one candidate target is plausible;
- generic approval could refer to multiple actions;
- canonical source is unreadable;
- duplicate ownership is unclear;
- lifecycle is undefined;
- repository state changed after recommendation;
- operation would mutate another repository.
