# GDO Phase 1 State Machines

Invalid transitions fail without partial mutation and append no success event. Recovery classification is explicit and does not silently retry external/manual work.

## Execution Package

```text
REGISTERED -> POLICY_ACCEPTED -> READY_FOR_MANUAL_LAUNCH
READY_FOR_MANUAL_LAUNCH -> LAUNCHED_MANUALLY -> COMPLETION_RECEIVED
COMPLETION_RECEIVED -> ACKNOWLEDGED -> CLOSED

REGISTERED -> INVALID
REGISTERED -> POLICY_REJECTED
any open state -> FAILED | CANCELLED | RECOVERY_REQUIRED
RECOVERY_REQUIRED -> prior safe state | FAILED | CANCELLED
```

`POLICY_REJECTED` is terminal unless a new corrected package and policy evaluation create a new workflow identity. Manual launch requires current approval and matching policy/input digest.

## Inbox Item

```text
RECEIVED -> VALIDATED -> ACCEPTED -> ACKNOWLEDGED
RECEIVED | VALIDATED -> DUPLICATE
RECEIVED | VALIDATED -> REJECTED
ACCEPTED -> RECOVERY_REQUIRED -> ACKNOWLEDGED | REJECTED
```

Identical duplicates reference prior evidence. Identity/digest conflicts are rejected and require review.

## Attempt

```text
CREATED -> STARTED -> COMPLETED
CREATED | STARTED -> FAILED
STARTED -> ABANDONED
FAILED | ABANDONED -> RETRY_ELIGIBLE
```

Retry eligibility does not relaunch work. A retry creates a new attempt ID under the same logical execution after Human/Policy gates pass.

## Outbox Item

```text
PENDING -> READY -> MANUALLY_DISPATCHED -> ACKNOWLEDGED
READY | MANUALLY_DISPATCHED -> FAILED
MANUALLY_DISPATCHED -> RECOVERY_REQUIRED
RECOVERY_REQUIRED -> ACKNOWLEDGED | READY | FAILED
```

Recovery checks acknowledgement/receipt evidence before returning an item to READY.

## Guard Inventory

Every transition checks expected current state/version, idempotency key/input digest, contract version, artifact digest, approval freshness/scope where relevant, policy decision/version, and required references. The transition, event, projection, audit and outbox intent commit atomically.
