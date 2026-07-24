# Duplicate Delivery and Idempotent Replay

The gateway executes `effect-commit-001` once and durably stores its receipt. If
acknowledgement is lost and the same request is delivered again, it returns the
existing receipt without invoking Git. Reuse of the idempotency key with a
different request digest is rejected as an integrity conflict and produces an
Error/SCW Envelope.
