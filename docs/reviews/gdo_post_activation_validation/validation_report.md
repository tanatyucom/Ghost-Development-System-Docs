# GDO Post-Activation Validation Report

## 2. Activation Commit Verification Report

`aa8d795d5fe7d3fa21c367ef194c346712831423` is the clean, pushed GDS-DOCS `main` HEAD. Local and `origin/main` match.

## 3. Registry State Verification Report

Canonical Registry contract `1.0` validates. Six records exist; exactly one target record exists. The target is `Active`, `Verified`, and `NONE` mutation class. No Registry source mutation occurred.

## 4. Registry Digest Verification Report

RFC 8785/SHA-256 recalculation returned `sha256:1322cc66a59306cbbc6f483a62aac2f718fee64d3abf446bd14f1b25524d5027`, exactly matching the approved digest.

## 5. Registry Lookup Report

Lookup resolves one record with canonical root `C:/GitHub/ghost-development-orchestrator`, default branch `main`, and remote `https://github.com/tanatyucom/ghost-development-orchestrator.git`.

## 6. GDS-DOCS State Report

Branch/tracking/HEAD are `main` / `origin/main` / `aa8d795d5fe7d3fa21c367ef194c346712831423`. Baseline was clean and synchronized. Relevant regression: 21/21 PASS. Index and encoding checks PASS.

## 7. GDO State Report

Branch/tracking/HEAD are `main` / `origin/main` / `b207fc9e1c56ca019d99384173e672f065c7557e`. Baseline is clean and synchronized. Schema v7 and migrations 001–007 remain current.

## 8. Runtime Compatibility Report

Provider `GDS_RUNTIME_GENERIC_POLICY_PROVIDER` is READY, version `1.0.0`, revision `sha256:13f6bfe4de941b793e7928ed8a685a319b355c00b7bac6d32989c29d11761ca6`. Contract and capability pins match. Invocation is in-process, bounded, side-effect-free, and fail-closed. Runtime has no GDO dependency.

## 9. Strict Verification Report

The current GDO regression suite executed 160 tests in 18.846 seconds: PASS. It covers database integrity, foreign keys, migrations, schema v7, contracts, Artifact, Inbox/Outbox, policy, packages/exports, completions/acknowledgements, attempts/bindings, replay, Audit, and Backup/Recovery.

## 10. Smoke Validation Report

The isolated E2E suite executed 5 tests in 3.784 seconds: PASS. It exercised the complete bounded local flow through verified Backup and isolated Recovery. Provider call count remained one across replay. No real repository, Registry, dispatch, Codex, shell, Git, or external effect was used.

## 11. Authority Boundary Report

`execution_authority`, Git effect authority, Registry mutation authority, external execution authority, automatic retry, automatic failover, and automatic Human Approval acceptance remain false. Human Approval remains required.

## 12. Warning Preservation Report

The committed record retains the local dependency warning: use the pinned `runtime-policy` environment or Runtime `.policy-deps`; unavailable dependencies fail closed. The warning is activation-safe and required before operational use.

## 13. Reversibility Report

The Registry standard represents `Suspended`, and states that Suspended entries cannot be mutation targets. A future `Active -> Suspended` transition can preserve durable history and schema, but requires a separate Q and Human Approval. No transition was executed.

## 14. Phase 1 Scope Report

The active scope is exactly `PHASE1_BOUNDED_LOCAL_ORCHESTRATION`. It does not include automatic execution, Git automation, remote dispatch, cross-repository mutation, automatic approval/retry/failover, active-store replacement, or Phase 2.

## 15. Security Boundary Report

Validation used repository reads, in-process Python, isolated temporary fixtures, and evidence writes only. No network, credential, secret, dynamic plugin, Registry/Runtime/GDO/GameGhost mutation, package dispatch, Codex invocation, or external effect occurred.

## 16. Failure Classification Report

All Q-defined `POST_ACTIVATION_*` codes remain the bounded failure vocabulary. No failure was observed and no unrestricted exception text was persisted.

## 17. Determinism Report

The logical slot was RFC 8785-canonicalized over the seven Q-defined fields. Result ID is `gdo-post-activation:1b969efed1fbf315a4c8ba6bd2fee8ac9b1fe99f01418d67c6adc4486e2e731f`. Result digest excludes only `result_digest` and equals `sha256:032981e480a69574469817fcf85ac76d543b9faf7e9e11515078c05684a09191` on both recalculations.

## 18. Test Report

- Canonical Registry: PASS; six records, one target.
- Target digest: PASS, exact.
- GDS-DOCS regression: 21/21 PASS.
- GDO full regression: 160/160 PASS.
- Isolated smoke/E2E: 5/5 PASS.
- Runtime provider health and pins: PASS.
- Closed result schema and digest: PASS.
- AI Repository Index freshness, encoding regression, Python compile, security scan, and `git diff --check`: rerun at final gate and recorded in the Completion Report.

## 19. Git Diff Summary

Only this repository-owned evidence package and the canonically regenerated AI Repository Index are permitted. The Registry source and unrelated files must remain unchanged.
