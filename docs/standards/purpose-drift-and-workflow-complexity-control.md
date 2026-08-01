# Purpose Drift and Workflow Complexity Control

## Status

Canonical GDS governance standard. Applies to Q authoring, architecture review,
SCW resolution, implementation, Completion Review, and governed Git effects.

## User Intent Anchor

Every Q must preserve an immutable `USER_INTENT_ANCHOR` containing:

- `original_user_goal`
- `expected_user_experience`
- `minimum_successful_flow`
- `explicit_non_goals`
- `active_trust_profile`

Each proposed addition must be classified as `DIRECTLY_ADVANCES_INTENT`,
`OPTIONAL_ENHANCEMENT`, `ENTERPRISE_DEFERRED`, `UNRELATED`, or
`PURPOSE_DRIFT`. Only `DIRECTLY_ADVANCES_INTENT` may become an unreviewed
prerequisite.

## META-SCW: Purpose Drift

Stop expansion when work no longer directly advances the anchor, changes the
user-visible workflow or execution subject, exceeds the active trust profile,
adds a larger support mechanism than the operation it protects, or creates
another prerequisite merely to complete the current prerequisite.

The response must restate the original intent, explain the distance from the
current workflow, classify existing work as Keep, Defer, or Delete, offer the
minimum safe alternative, and wait for explicit human direction.

`META-SCW` has precedence over a local SCW. Trigger classes are:

- `PURPOSE_DRIFT`
- `SELF_REFERENTIAL_BOOTSTRAP`
- `COMPLEXITY_BUDGET_EXCEEDED`
- `TRUST_PROFILE_CONTAMINATION`
- `EXECUTION_SUBJECT_DRIFT`
- `REPEATED_PREREQUISITE_EXPANSION`
- `USER_CONFUSION_SIGNAL`

## Two-Prerequisite Trigger

When two consecutive prerequisite implementations have already been added for
the same effect, a proposed third prerequisite must not be implemented. Start
an Architecture Simplification Review with the default decision:
`DO_NOT_ADD_ANOTHER_LAYER`.

## Self-Referential Workflow Prohibition

An implementation that enables effect X must not require effect X, followed by
another implementation that itself requires X. Classify the condition as
`BOOTSTRAP_ESCAPE_REQUIRED`, `SIMPLIFICATION_REQUIRED`,
`ENTERPRISE_DEFERRED`, or `ABORT_AND_ROLLBACK`. Recursive mechanism addition
is not a resolution.

## Trust Profile Isolation

### PERSONAL_LOCAL

Assumes one user, one local machine, a registered repository, and explicit
conversational approval. It requires exact repository, branch, expected HEAD,
path set, separate Commit and Push approval, result verification, and fail
closed handling of unknown results.

It does not require enterprise identity projections, generation-specific
binding/preflight/receipt tables, short-lived bridge lifecycle, SSO, signed
actor identity, frontend attestation, or enterprise non-repudiation unless a
separate threat model demonstrates the need.

### ENTERPRISE_SHARED

Enterprise requirements belong to a separate Q that first defines the threat
model, roles, identity provider, separation of duties, audit and retention
requirements, recovery requirements, and deployment scenario. Enterprise
controls must not be imported into `PERSONAL_LOCAL` merely because they appear
safer in isolation.

## Minimum Viable Governance

Personal Local Commit:

1. Observe repository, branch, HEAD, exact paths, and commit message.
2. Obtain Human Approval.
3. Reconfirm unchanged state.
4. Stage exact paths and create one Commit.
5. Verify SHA, parent, paths, and message.
6. Stop.

Personal Local Push is a separate flow: show local/remote state, obtain a
separate approval, push once, verify equality, and stop.

Minimum durable evidence is repository, branch, expected HEAD, exact paths,
commit message, human response and time, commit SHA, and push result.

## Execution Subject Integrity

The declared execution subject and user experience must not change silently.
Using Codex as an internal executor is allowed; requiring the user to relay an
approval from ChatGPT to Codex is a user-visible workflow change and requires
explicit approval before adoption.

## Complexity Budget

Each Q declares `COMPLEXITY_BUDGET`. The `PERSONAL_LOCAL` default is:

- new approval boundaries: 0 or 1
- new projection layers: 0
- new generation-specific tables: 0
- consecutive prerequisite implementations: maximum 1

Exceeding the budget starts `ARCHITECTURE_SIMPLIFICATION_REVIEW`; the budget
must not be silently expanded.

Before adding a mechanism, identify the concrete user-visible failure, its
probability under the active trust profile, why a simpler check is insufficient,
whether total complexity decreases, and whether new authority or synchronization
duties are introduced. Reject when complexity cost exceeds practical risk
reduction.

## User Confusion Signal

Statements such as “why is this needed?”, “isn’t this a detour?”, or “this used
to work directly” are architecture signals. Stop expansion, restate the intended
outcome, show current distance and added complexity, and propose simplification
or rollback.

## Keep, Defer, Delete

Purpose-drift artifacts must be classified:

- `KEEP`: coherent, actively needed, and within the trust profile.
- `DEFER_TO_ENTERPRISE_SHARED`: potentially valuable but outside current need.
- `DELETE_OR_ROLLBACK`: harmful, duplicative, or self-referential.

Passing tests and implementation effort do not justify `KEEP`. Decisions use
future value, coherence, active need, maintenance cost, and correct trust
profile—not sunk cost.

## Current Incident Disposition

The uncommitted 83-path GDO Resume implementation is a
`ROLLBACK_CANDIDATE`. Its prior Commit approval is withdrawn by architecture
reassessment. It must not be committed, pushed, tagged, released, or destroyed
under this Q. Enterprise ideas are deferred; failure knowledge is promoted into
this standard. Rollback requires a separate bounded Q.

## Completion and Git Boundary

Tests cannot normalize purpose drift. Completion Review must verify the intent
anchor, complexity budget, trust profile, execution subject, and Keep/Defer/Delete
classification. Commit and Push remain separate Human Approval units.
