# Review Question Findings

## Concept and Boundary

1. Yes. Durable coordination and privileged execution form an independent system purpose.
2. The proposed split is sound after removing queue, worker, transport, and Git effects from GDS Runtime.
3. Yes. MCP is an optional protocol adapter, not system identity or durable workflow owner.
4. Yes. GameGhost remains a product and has no runtime dependency on the platform.
5. Yes. They are contexts of the same ChatGPT actor, not independent trusted actors.
6. Yes. GDS is the versioned Policy Provider; the platform is a Policy Consumer.
7. Avoid cycles by keeping semantic contracts in GDS-DOCS and adapters dependent inward; operational state never becomes policy truth.

## Runtime and Orchestration

8. Add durable admission, contract validation, approval validity, lease/attempt, capacity, cancellation, timeout, and recovery states.
9. Queue is durable truth; watcher/polling produces events; MCP transports resources/tools but does not replace the queue.
10. Use a durable artifact store, inbox/outbox, acknowledgements, replay cursor, retention, and dead-letter handling.
11. Use effect-scoped idempotency keys, unique constraints, leases, attempt history, and receipts checked before retry.
12. Add Attempt ID and Artifact ID; all IDs and schema/digest references travel in every envelope.
13. Orchestrator owns retry/recovery policy; GDS defines governance constraints; adapters report retry safety.
14. Yes. Approval needs issue/expiry, target revision, scope digest, and explicit invalidation conditions.

## Git Execution

15. Partially. Remove execution from ChatGPT, not necessarily from Codex; an authorized Gateway/worker executes while ChatGPT coordinates review.
16. Canonicalize paths, hash the approved set, compare actual/staged diff, reject extras/missing/prohibited paths, and record the digest/receipt.
17. Yes. Expected repository/branch/HEAD/remote is mandatory optimistic locking.
18. Conditional pre-approval is acceptable only as separate Commit and Push units with exact scope, expiry, locks, and invalidation—not blanket approval.
19. Yes. Tag is post-Push recommendation and an independent Human Approval/effect.
20. Yes. Force push is prohibited by default; remote/branch changes require a new explicit approval.

## Security

21. Grant only typed operations for allowlisted repositories/paths and scoped credential use at execution time.
22. Necessary but not sufficient; combine typed Git operations with path validation, environment control, locks, and evidence.
23. Yes. Repository, path, operation/command, remote, and ref allowlists are required.
24. Classify/redact payloads, deny secret patterns and prohibited paths, size-limit, scan before storage/transfer, and never serialize credentials.
25. Yes. Define classification-specific retention, deletion, access, and audit exceptions.
26. Start with append-only records and hash/digest links; stronger signing/WORM storage follows risk growth.
27. Yes. Local threats include malware, stale artifacts, confused deputy, path traversal, injection, and credential leakage.

## Repository Strategy

28. Yes. Separate repositories match trust, deployment, release, and responsibility boundaries.
29. Define shared contracts first; bootstrap minimal GDS Runtime, then platform repository. Either repository bootstrap must not invent contracts.
30. Semantic source in GDS-DOCS; implementation repositories consume versioned packaged bindings.
31. Not initially. Generate/package bindings within consumers; extract a shared package only after two validated consumers need it.
32. Yes. Concept and contract decisions should precede repository creation.

## Scope Control

33. Durable artifact exchange, metadata/index, acknowledgements, audit, manual launch/return, IDs/digests, redaction, and recovery.
34. No. Execution Gateway follows reliable artifact/queue evidence.
35. Yes. This is the recommended Phase 1.
36. After Phase 2 crash/restart/recovery evidence; service installation is a separate operational decision.
37. Yes. Docker, cloud, remote worker, and multi-user operation are explicitly out of initial scope.
38. Prohibit architecture decisions, auto-approval, unrestricted shell, force push, secret storage, product-runtime dependency, Tag/Release, and self-modifying policy.
