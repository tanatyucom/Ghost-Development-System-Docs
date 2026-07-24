# AI Execution Correlation and Idempotency Standard

Delivery is at least once. Exactly-once is not claimed.

1. Preserve `correlation_id`, `q_id`, and `execution_id` across execution retries.
2. Allocate a new `attempt_id` for every worker attempt.
3. Preserve `effect_id` and `idempotency_key` only while intent, scope, expected
   HEAD, diff, and approval remain identical; otherwise create a new effect.
4. Allocate a receipt for each actual gateway attempt and query existing receipts
   before retry.
5. Use durable inbox/outbox records and acknowledge after durable processing.
6. Deduplicate artifacts/events by immutable ID and effects by idempotency key.
7. Ordering is per correlation stream and explicit sequence, never global.
8. Preserve all attempt history. Exhausted or poison delivery goes to dead letter;
   missing authority or ambiguous recovery goes to SCW.
9. Git effects require verified repository identity/root, branch, remote, expected
   HEAD, safe-set digest, diff digest, allowlist, expiry, secret check, and receipt
   lookup.
10. Duplicate completion packages update no state after the first validated
    package and never trigger an effect.
