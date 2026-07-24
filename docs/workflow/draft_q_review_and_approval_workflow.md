# Draft Q Review and Approval Workflow

**Version:** 1.0

```text
Generated Draft
  -> Safety Envelope Check
  -> Provenance / Registry / Precedence Review
  -> Missing-input Resolution
  -> Canonical Template Validation
  -> Human Review
  -> Approved Q or Return to Draft
  -> Startup Sequence
```

## Missing-input Resolution

- Non-blocking: preserve warning; no question required.
- Prompt-required: ask one grouped, minimal set of human-dependent questions.
- Blocking: keep Incomplete and name the exact resume evidence.
- Critical conflict: SCW with competing sources and required decision.

## Approval Boundary

Human review may approve only the visible final Q revision. Any material change
to repository, root, scope, authority, risk, prohibited operations, or Git policy
invalidates that approval. Approved does not mean Startup GO and does not prove
current workspace state.
