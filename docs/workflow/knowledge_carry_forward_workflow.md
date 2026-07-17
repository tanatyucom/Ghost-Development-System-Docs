# Knowledge Carry-Forward Workflow

**Status:** Draft Workflow

**Last Updated:** 2026-07-17

## Purpose

Knowledge Carry-Forward is the low-friction behavior where approved knowledge
promotion candidates are carried into the most relevant existing or future Q
instead of producing many standalone visible Q files.

It supports the Knowledge Promotion Engine by preserving candidates until they
can be reviewed, drafted, validated, and promoted through the correct lifecycle.

## Standard Flow

```text
Knowledge Candidate Recommendation
  -> Human Approval for Carry-Forward
  -> Target Q Selection
  -> Knowledge Promotion Actions section
  -> Completion Conditions
  -> Future Review / Draft Creation
  -> Validation
  -> Promotion or Archive
```

## Target Selection Order

1. current parent Q;
2. existing directly related child Q;
3. next scheduled implementation Q;
4. canonical artifact revision task;
5. new Q Draft only when no suitable target exists.

If multiple targets are equally plausible, apply SCW.

## Standard Section

Use this section in a Q or child-Q candidate when carry-forward is selected.

```markdown
## Knowledge Promotion Actions

### Candidates
- Candidate type:
- Summary:
- Evidence:
- Related artifacts:
- Proposed promotion target:
- Duplicate check:
- Approval state:

### Completion Conditions
- [ ] Candidate reviewed
- [ ] Canonical source checked
- [ ] Draft or revision created
- [ ] Human Approval obtained where required
- [ ] Index and lineage updated
- [ ] Validation passed
```

## Approval Meaning

When a user approves Knowledge Carry-Forward, the approval means:

```text
Register the identified candidates as governed promotion work.
```

It does not mean:

- accept an ADR;
- publish an Issa as canonical;
- modify a Rule;
- commit;
- push;
- tag;
- release;
- edit another repository.

Each mutating or canonicalizing action must remain a specific Pending Action
with its own approval boundary.

## Completion Review Integration

During Completion Review, ask:

- Did the work produce reusable knowledge?
- Is there a Knowledge Candidate?
- Is an existing canonical artifact the right target?
- Should the candidate be carried forward?
- Is Human Approval needed?
- Which future Q or artifact owns the follow-up?

## Out Of Scope

- Automatic promotion.
- Automatic Q creation without approval.
- Runtime detector implementation.
- Commit / push / tag / release.
- Cross-repository mutation.

## Related Documents

- `docs/architecture/knowledge_promotion_engine.md`
- `docs/architecture/knowledge_candidate_classification_contract.md`
- `docs/workflow/knowledge_preservation_gate.md`
- `docs/workflow/completion_report_workflow.md`
- `docs/architecture/intent_driven_workflow.md`
