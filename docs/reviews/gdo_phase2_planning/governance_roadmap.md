# GDO Phase 2 Governance, Roadmap, and Risk Report

## GDS-DOCS Governance Requirements

| Candidate | Classification |
|---|---|
| Phase 2 ADR | REQUIRED_BEFORE_IMPLEMENTATION |
| Approval Binding Contract | REQUIRED_BEFORE_IMPLEMENTATION |
| Safe Commit Set Contract | REQUIRED_BEFORE_IMPLEMENTATION |
| Repository State Fingerprint Contract | REQUIRED_BEFORE_IMPLEMENTATION |
| Git Effect Request Contract | REQUIRED_BEFORE_IMPLEMENTATION |
| Git Effect Result Contract | REQUIRED_BEFORE_IMPLEMENTATION |
| Git Adapter Security Boundary | REQUIRED_BEFORE_IMPLEMENTATION |
| Git Effect Failure Classification | REQUIRED_BEFORE_IMPLEMENTATION |
| Git Effect SCW Rules | REQUIRED_BEFORE_IMPLEMENTATION |
| Completion Review Git-effect specialization | REQUIRED_BEFORE_ACTIVATION |
| Registry capability definition | REQUIRED_BEFORE_ACTIVATION |
| Commit effect examples | REQUIRED_BEFORE_ACTIVATION |
| Push effect contract | DEFERRED |
| Tag effect contract | DEFERRED |
| Release effect contract | DEFERRED |

## Ordered Sequence

1. Phase 2 Architecture / ADR
2. Approval Binding Foundation
3. Safe Commit Set Contract
4. Repository State Fingerprint
5. Git Effect Request / Result Foundation and schema v8
6. Commit Effect Adapter
7. Commit Effect E2E Validation
8. Commit Effect Activation Assessment
9. Push Effect Planning
10. Push Effect Adapter
11. Push Effect E2E Validation
12. Partial Effect / Recovery Hardening
13. Phase 2 Registry Scope Assessment
14. Post-Activation Validation
15. Phase 2 Closure

Sequence digest: `sha256:42daf162618dd3a3275836aaa85c3a9a1d4b4f3d774f52d0074ce2f910c2a6a9`. Each sequence is a separately approved bounded Q. The recommended first implementation-facing Q is `Q_AI-DEVELOPMENT-ORCHESTRATOR-PHASE2-ARCHITECTURE-DECISION-001`; it decides/adopts the ADR and governance prerequisites and must not yet execute Commit effects.

## Test Strategy

The Commit slice must test all 30 Q cases individually: exact/ambiguous/stale approval; HEAD/content/extra/missing/untracked drift; wrong branch/remote; merge/rebase/cherry-pick; symlink/junction escape; limits; hook mutation/failure; signing; Commit success/replay/conflict; verification mismatch; no automatic retry; no Push/Tag/Release/unrelated file/credential persistence/authority escalation; and full Phase 1 regression. Tests use isolated repositories only and assert bounded persisted state after every failure.

## SCW and Security Integration

SCW triggers include every repository/scope/approval drift, wrong identity, operation state, unresolved hook/signing/credential prompt, partial effect, verification mismatch, cross-repository request, Tag/Release request, authority or schema ambiguity. SCW stops before adapter invocation where possible and never grants retry or expanded scope.

No Phase 2 code, Git effect, arbitrary shell/command, credential/secret, wildcard/force, automatic approval/retry/failover, Registry/Runtime/GameGhost mutation, Codex invocation, cross-repository mutation, Tag, Release, or production test hook is permitted by this plan.

## Registry Scope

Keep `PHASE1_BOUNDED_LOCAL_ORCHESTRATION` during implementation. Consider `PHASE2_BOUNDED_HUMAN_APPROVED_GIT_EFFECT_ORCHESTRATION` only after Commit slice implementation, 30-case E2E/fault validation, independent activation assessment, Human Approval, and explicit Registry mutation Q.

## Risk Register

| Risk | Severity | Likelihood | Mitigation | Owner | Blocking | Follow-up |
|---|---|---|---|---|---|---|
| Approval ambiguity | Critical | Medium | One visible pending request; exact digest binding | GDO/GDS-DOCS | Yes | Approval foundation |
| Repository drift | Critical | High | Immediate fingerprint revalidation | GDO | Yes | Fingerprint Q |
| Git hook side effects | High | Medium | Absent or digest-allowlisted hooks; SCW | Repository owner | Yes | Adapter Q |
| Signing/credential prompts | High | Medium | Explicit noninteractive policy; SCW on prompt | Repository owner | Yes | Adapter Q |
| Incorrect staging | Critical | Medium | Exact pathspecs and post-stage tree verification | Git adapter | Yes | Adapter/E2E |
| Untracked secret inclusion | Critical | Medium | Full untracked digest, denylist/secret scan, no expansion | GDO policy | Yes | Safe Set Q |
| Partial Commit state | High | Low | Preserve evidence; no reset; SCW | GDO/operator | Yes | Recovery hardening |
| Partial Push state | Critical | Medium | Push deferred; exact remote verification | Future Push adapter | No now | Push planning |
| Branch protection | High | Medium | Push-specific preflight and approval | Future Push adapter | No now | Push planning |
| Remote mismatch | Critical | Low | Pinned canonical remote identity | GDO | Yes | Fingerprint Q |
| Cross-repository scope creep | Critical | Medium | Single repository invariant | GDS governance | Yes | Deferred architecture |
| Codex autonomy creep | Critical | Medium | Worker deferred; no implicit Git authority | GDS governance | Yes | Later worker Q |
| Automatic retry creep | High | Medium | Durable failure + new approval | GDO | Yes | Attempt specialization |
| Registry scope drift | High | Low | Update only after E2E/assessment approval | GDS-DOCS owner | Yes | Registry assessment |
| Schema migration risk | Critical | Medium | Dedicated v8 Q, atomic migration/fault matrix | GDO storage owner | Yes | Effect foundation |
| Destructive rollback | Critical | Low | No reset/clean; forward recovery only | GDO/operator | Yes | Recovery hardening |

## Failure Classification

The closed planning vocabulary is `PHASE2_PLAN_STARTUP_INVALID`, `PHASE2_PLAN_SCOPE_UNCLEAR`, `PHASE2_PLAN_AUTHORITY_AMBIGUOUS`, `PHASE2_PLAN_APPROVAL_MODEL_INVALID`, `PHASE2_PLAN_GIT_BOUNDARY_INVALID`, `PHASE2_PLAN_SAFE_COMMIT_SET_INVALID`, `PHASE2_PLAN_FINGERPRINT_INVALID`, `PHASE2_PLAN_SCHEMA_DECISION_UNRESOLVED`, `PHASE2_PLAN_REGISTRY_SCOPE_UNRESOLVED`, `PHASE2_PLAN_ROLLBACK_UNDEFINED`, `PHASE2_PLAN_RETRY_UNDEFINED`, `PHASE2_PLAN_SECURITY_BOUNDARY_INVALID`, `PHASE2_PLAN_SEQUENCE_INVALID`, `PHASE2_PLAN_FIRST_SLICE_UNDEFINED`, `PHASE2_PLAN_GOVERNANCE_INCOMPLETE`, and `PHASE2_PLAN_VERIFY_FAILED`. Durable evidence stores only codes and bounded identities.
