# Candidate Decisions

## Next Q

Decision: Recommended.

Candidate:

```text
Q_GDS-INTENT-QUEUE-RUNTIME-001_runtime_intent_queue_and_approval_state_resolver_foundation_JP.md
```

Reason:

Runtime implementation is out of scope for this Q, but the architecture now
defines enough state to design a future resolver.

## Roadmap

Decision: Update current roadmap direction.

Reason:

Approval Request Evidence is the bridge between Completion Review Evidence and
Platform Ready Review.

## ADR

Decision: Create proposed ADR.

Artifact:

```text
docs/adr/ADR-GDS-006_approval_state_and_execution_state_separation.md
```

Reason:

Approval state and execution state separation is a durable architecture
decision, not only a workflow detail.

## ISSA / Improvement Record

Decision: Defer as explicit future candidate.

Candidate themes:

- ambiguous chained natural-language approval;
- hidden follow-up candidates;
- execution-claim mismatch.

Reason:

This Q records the rule and architecture first. Separate issue-story artifacts
can be created after dogfooding produces concrete incident examples.

## Knowledge Promotion

Decision: Promote as draft architecture, workflow, rule, template, and ADR
candidate.

Promoted concepts:

- Candidate First.
- Visible Scope Rule.
- Intent Queue.
- Execution Authority.
- No execution claim without evidence.

## MCP Execution Adapter

Decision: Future Candidate only.

Reason:

The Q explicitly prohibits runtime MCP implementation and generic arbitrary
shell execution.
