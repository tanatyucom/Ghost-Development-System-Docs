# Q_GDS_AI_STARTUP_REPOSITORY_SYNCHRONIZATION_ENFORCEMENT_REVIEW_001

## Title

AI Startup Repository Synchronization Enforcement Review

## Request ID

GDS-AI-STARTUP-REPOSITORY-SYNCHRONIZATION-ENFORCEMENT-REVIEW-001

## Type

Architecture Review / Regression Investigation / Governance Strengthening

## Status

Draft

## Priority

Critical

## Target Repository

Ghost-Development-System-Docs

## Objective

Review the current GDS Startup architecture and determine why AI sessions repeatedly fail to preserve the already-established meaning of Startup as an AI-facing repository synchronization protocol.

Confirm whether the required definition and controls already exist, identify any enforcement or discoverability gaps, and strengthen the canonical system only where evidence shows that improvement is necessary.

The intended invariant is:

> Before planning, creating, revising, reviewing, recommending, or executing repository work, the AI must synchronize its working context with the canonical repository and use that repository state as the Single Source of Truth.

This Q must prefer revision of existing canonical assets over creation of competing concepts or duplicate documents.

Do not change GameGhost.

Do not execute Commit / Push / Tag.

---

## Background

GDS already has a Startup concept designed for AI, not for the Human operator.

The currently supplied Startup definition states:

> Synchronize the AI with the canonical GDS knowledge before planning, creating, reviewing, or implementing work.

It also defines the public Ghost Development System repository as the Single Source of Truth and includes a Q Creation Gate requiring the AI to review:

- the canonical GDS repository;
- AI Repository Index;
- the latest Startup document;
- the latest canonical `Q_TEMPLATE.md`;
- related Rules;
- Workflows;
- ADRs;
- Roadmaps;
- Standards;
- Current Mission;
- Constraint Check.

Despite this, AI sessions repeatedly reinterpret Startup as:

- a Human checklist;
- an optional session-opening ritual;
- a conversational reminder;
- a repository scan that is separate from actual response generation.

The same explanation is then repeated in conversation until the AI again recognizes that Startup exists specifically to align AI context with repository truth.

A recent example also showed inconsistent Commit handling across adjacent Completion Reviews:

- one response emitted Commit commands;
- another emitted an Approval Request;
- another expected Recommendation only.

This inconsistency may be caused by an AI response being generated from conversational pattern recall rather than from current canonical repository policy.

---

## Problem Statement

The current architecture appears to define the desired behavior, but may not guarantee it.

There may be a difference between:

```text
Startup definition exists
```

and:

```text
Startup is actually executed and its resolved repository context governs every relevant response
```

Potential failure classes include:

1. **Definition exists but is not discoverable early enough**
2. **Startup is treated as session-only rather than task-gated**
3. **Startup completion is claimed without evidence of repository reads**
4. **AI Repository Index is read, but required canonical assets are not resolved**
5. **Q Template is assumed from memory rather than opened from the repository**
6. **Conversation context silently overrides newer repository policy**
7. **No machine-readable Startup result or context manifest exists**
8. **No Pre-Response gate verifies that required repository context was actually loaded**
9. **No freshness or revision evidence is recorded**
10. **Role, workflow state, or approval state is inferred from conversation instead of repository state**
11. **Startup and Constraint Check responsibilities overlap or leave a gap**
12. **The system defines repository-first behavior normatively but does not enforce it operationally**

---

## Core Principle Under Review

Evaluate whether GDS already formally establishes the following principle and whether it is sufficiently enforceable:

> Repository-Aware AI Principle
>
> When a canonical repository exists, the AI must not rely on conversation memory alone for repository-governed decisions. It must resolve the current canonical repository state, load the task-relevant authoritative assets, and base its response on that evidence.

Do not create this as a new standalone principle if equivalent canonical language already exists.

Prefer:

- clarification;
- consolidation;
- stronger references;
- validation;
- machine-readable evidence;
- workflow enforcement.

---

## Required Review Questions

### 1. Does the canonical definition already exist?

Locate every canonical or supporting asset that defines or governs:

- AI Startup;
- repository synchronization;
- Single Source of Truth;
- AI Repository Index synchronization;
- Current Mission synchronization;
- Q Template resolution;
- Revision First;
- Constraint Check;
- Pre-Response Verification;
- Output Contract;
- repository-aware planning and review;
- repository boundary;
- Human Approval boundary.

For each asset, record:

- exact repository path;
- status or authority level;
- relevant heading;
- whether it is normative or explanatory;
- whether another asset duplicates or conflicts with it.

Answer explicitly:

```text
A. Definition is absent
B. Definition exists but is incomplete
C. Definition exists and is complete but weakly enforced
D. Definition exists, is enforced, and the observed issue is outside repository design
E. Multiple conflicting definitions exist
```

### 2. Is Startup explicitly AI-facing?

Verify whether canonical wording makes all of the following unambiguous:

- Startup is executed by or for the AI;
- Startup aligns AI working context with repository truth;
- Startup is not primarily a Human checklist;
- Startup must occur before repository-governed reasoning;
- Startup results must affect the response, not merely be acknowledged;
- inability to access required repository assets triggers SCW.

Identify wording that could reasonably cause an AI to misclassify Startup as Human-facing.

### 3. Is repository access real or merely asserted?

Determine whether current GDS controls distinguish:

```text
"I know a repository exists"
```

from:

```text
"I opened and resolved the current canonical assets required for this task"
```

Review whether Startup requires evidence such as:

- resolved repository identity;
- branch or revision when available;
- AI Repository Index revision/freshness;
- exact canonical paths loaded;
- Q Template path and revision;
- Current Mission path;
- relevant Rule / Workflow / ADR paths;
- unresolved or inaccessible assets;
- conflict status;
- timestamp or session identifier.

### 4. Is Startup session-scoped or task-scoped?

Determine when synchronization must be refreshed.

Evaluate at least these triggers:

- new chat/session;
- repository changed since last synchronization;
- user reports a Codex completion affecting canonical files;
- task type changes, such as Architecture → Q Creation → Completion Review → Execution;
- current workflow state changes;
- approval state changes;
- AI identifies missing or stale context;
- a referenced canonical asset cannot be found;
- the Human explicitly requests repository verification.

Recommend whether GDS needs:

- full Startup;
- incremental context refresh;
- task-specific context resolution;
- no additional mechanism.

### 5. Does Q Creation actually require opening `Q_TEMPLATE.md`?

Verify that the current Q Creation Gate requires the AI to read the latest canonical template, not merely follow a remembered structure.

Inspect:

- canonical template path resolution;
- revision precedence;
- duplicate template handling;
- vendor or snapshot copies in Ghost repositories;
- behavior when repository access is unavailable;
- evidence recorded in the generated Q or its completion report.

Determine whether a Q should include provenance such as:

```text
Template Source:
Template Revision:
Canonical Repository:
Related Assets Reviewed:
```

Do not add fields unless they materially improve traceability and fit the existing template architecture.

### 6. Can conversation context override repository truth?

Review current precedence rules.

The intended order should be assessed against existing architecture, for example:

```text
Canonical Repository
→ Current governed repository state
→ Explicit current Human instruction within authority boundaries
→ session context
→ model memory / generic behavior
```

Do not adopt this ordering automatically if the repository defines a different valid hierarchy.

Identify how the system should handle:

- an old conversation rule conflicting with a newer repository rule;
- Human shorthand such as `お願いします`;
- ambiguous Commit / Push / Tag state;
- remembered template structure conflicting with the current template;
- unavailable repository access.

### 7. Why did Commit output vary?

Use the Commit-operation inconsistency as a concrete regression case.

Trace which canonical assets should determine whether a Completion Review emits:

- Repository Recommendation only;
- Workflow Recommendation;
- Approval Request;
- Commit command;
- Execution Instruction;
- no execution-related output.

Determine whether the variation is caused by:

- missing Startup synchronization;
- missing workflow-state resolution;
- unclear actor responsibility;
- conflicting examples;
- obsolete documents still indexed;
- output template bypass;
- absent Pre-Response validation;
- generic AI behavior overriding GDS policy;
- another evidenced cause.

Do not assume the cause before repository review.

### 8. Is machine-readable enforcement needed?

Evaluate whether the current system would benefit from one or more of the following, or an equivalent design already present:

#### A. Startup Context Manifest

A machine-readable record of the repository context resolved for the current task.

Possible fields:

```yaml
repository:
branch_or_revision:
startup_asset:
ai_repository_index:
current_mission:
q_template:
related_assets:
workflow_state:
approval_state:
unresolved_assets:
conflicts:
freshness:
status:
```

#### B. Repository Context Requirement Registry

Maps task types to required canonical context.

Example:

```text
Q Creation
→ Startup + AI Repository Index + Current Mission + Q Template + related Rules/Workflows

Completion Review
→ Completion Review standard + Recommendation contract + Approval workflow + current request artifacts

Execution Instruction
→ pending Approval Unit + Human approval evidence + authority registry + execution policy
```

#### C. Pre-Response Repository Context Gate

Blocks repository-governed output when required canonical context was not resolved.

#### D. Startup Evidence Block

A concise machine- or Human-readable statement proving what was loaded.

#### E. Freshness / Invalidation Rules

Defines when previously synchronized context becomes stale.

For every candidate, classify:

- Already exists;
- Extend existing asset;
- New asset justified;
- Not justified;
- Future candidate.

### 9. Can this be validated automatically?

Assess feasible validation rules, including:

- Q artifact created without canonical template provenance;
- Startup marked PASS while required assets are unresolved;
- task type lacks required context mapping;
- obsolete or noncanonical template used;
- current mission not resolved;
- AI Repository Index stale or absent;
- response emits execution command without resolved workflow and approval state;
- repository-governed recommendation emitted from conversation-only context;
- conflicting canonical assets not triggering SCW.

Distinguish:

- documentation validation;
- schema validation;
- repository consistency validation;
- runtime validation;
- AI response validation.

---

## Required Work

### Phase 1 — Canonical Asset Discovery

Use the current AI Repository Index and repository search to locate all relevant assets.

Do not rely on filenames supplied in this Q as exhaustive or current.

Apply:

- Single Source of Truth;
- Revision First;
- Knowledge Ownership Rule;
- repository boundary rules;
- SCW on conflict or uncertainty.

### Phase 2 — Current-State Architecture Map

Produce a concise architecture map showing the actual current flow.

At minimum, map:

```text
AI receives task
→ Startup / Context Synchronization
→ task-specific canonical asset resolution
→ Constraint Check
→ governed reasoning
→ Pre-Response Verification
→ response / artifact
```

If the repository currently defines a different flow, document that instead and explain the difference.

### Phase 3 — Gap and Root-Cause Analysis

Create an evidence-based matrix:

| Expected behavior | Current canonical support | Enforcement strength | Observed failure risk | Root cause | Recommendation |
|---|---|---|---|---|---|

Include the repeated AI misunderstanding and Commit-output inconsistency as test cases.

### Phase 4 — Codex Design Recommendation

Recommend the smallest coherent improvement that makes Startup behavior reliable across AI sessions and task transitions.

The recommendation must explicitly state whether to:

- make no change;
- revise existing Startup wording;
- revise Startup and AI Response Checklist;
- extend Pre-Response Verification;
- add task-specific context requirements;
- add machine-readable context evidence;
- add a Validator;
- consolidate duplicate assets;
- archive obsolete definitions;
- create a separate future Q for runtime implementation.

Codex may propose a better architecture than the candidates in this Q when supported by repository evidence.

### Phase 5 — Minimal Implementation

If and only if the review confirms a repository-level gap, implement the smallest approved coherent revision within this Q.

Permitted implementation scope:

- strengthen existing canonical definitions;
- clarify that Startup is AI-facing;
- clarify repository access evidence requirements;
- add or revise task-refresh triggers;
- strengthen Q Creation Gate wording;
- strengthen AI Response Checklist;
- strengthen Pre-Response Verification documentation;
- add a small schema or machine-readable context contract when clearly justified and consistent with existing architecture;
- update indexes, READMEs, references, examples, and Repository Quality artifacts;
- create follow-up Q candidates for runtime automation or Validator implementation.

Do not:

- create duplicate architecture when an existing asset can be revised;
- build a full runtime engine without separate review;
- modify GameGhost;
- execute Commit / Push / Tag.

If the review concludes the canonical repository is already sufficient, do not force an implementation. Produce evidence, identify the actual non-repository cause, and recommend the correct next action.

---

## Required Test Cases

### Case 1 — New Session Q Creation

Input:

```text
Qファイルお願いします
```

Expected:

- AI resolves canonical GDS repository;
- AI reads current AI Repository Index;
- AI resolves latest canonical `Q_TEMPLATE.md`;
- AI reviews task-relevant Rules / Workflows / Current Mission;
- AI performs Constraint Check;
- AI creates the Q using repository truth;
- project Output Contract is followed;
- inaccessible canonical context triggers SCW rather than confident fabrication.

### Case 2 — Existing Definition Misclassified

AI states:

```text
Startup is a Human checklist.
```

Expected:

- repository evidence disproves or confirms the statement;
- AI corrects itself from canonical assets;
- Startup's intended actor and purpose are unambiguous.

### Case 3 — Adjacent Completion Reviews

Two consecutive completion reports have the same governance state.

Expected:

- response layer and Commit handling remain consistent;
- AI does not alternate among Recommendation, Approval Request, and Commit commands without a state transition.

### Case 4 — Repository Updated After Startup

Codex completes and commits a change affecting governance assets.

Expected:

- prior synchronized context is invalidated or refreshed before the next governed response;
- AI does not continue using stale conversation knowledge.

### Case 5 — Repository Unavailable

Required canonical assets cannot be accessed.

Expected:

- AI does not claim Startup PASS;
- AI does not claim it reviewed the current template;
- SCW or an explicit evidence limitation is emitted;
- no repository-governed execution recommendation is fabricated.

### Case 6 — Conflicting Template Copies

A Ghost repository contains an older vendored Q template while GDS contains the canonical newer template.

Expected:

- GDS canonical template wins according to Knowledge Ownership and Revision rules;
- conflict is recorded;
- obsolete local copy is not silently treated as authoritative.

---

## Deliverables

1. Canonical asset inventory with paths and authority classification.
2. Current-state Startup / repository synchronization architecture map.
3. Root-cause analysis for repeated AI misunderstanding.
4. Root-cause analysis for Commit output inconsistency.
5. Expected-vs-actual enforcement matrix.
6. Evaluation of machine-readable enforcement candidates.
7. Codex recommendation for the minimum reliable design.
8. Any justified minimal repository revisions.
9. Test case results.
10. Remaining gaps and follow-up Q candidates.
11. Completion Report.
12. AI Repository Index and Repository Quality updates when repository files change.

---

## Completion Criteria

This Q is complete when:

- the repository is searched before conclusions are drawn;
- Codex determines whether the definition already exists;
- duplicate or conflicting assets are identified;
- the AI-facing purpose of Startup is verified;
- the distinction between claimed synchronization and evidenced repository access is addressed;
- Q Template resolution behavior is verified;
- task/session refresh behavior is assessed;
- Commit-output inconsistency is traced to canonical policy and actual state requirements;
- enforcement gaps are classified;
- a minimal improvement is implemented only if justified;
- all changed documentation remains internally consistent;
- validation passes;
- GameGhost remains untouched;
- Commit / Push / Tag remain unexecuted.

---

## Verification

Run the repository's current canonical validation commands discovered through Startup and AI Repository Index.

At minimum, when applicable, verify:

- AI Repository Index validation;
- encoding regression validation;
- repository quality audit;
- Markdown link/reference consistency;
- YAML/schema validation for any machine-readable asset;
- `git diff --check`;
- mojibake marker search;
- no GameGhost changes;
- no Commit / Push / Tag.

Do not assume command names in this Q are canonical; resolve the current commands from the repository.

---

## Expected Completion Report Sections

- Changed Files
- Canonical Assets Reviewed
- Existing Definition Assessment
- Root Cause
- Architecture Findings
- Enforcement Gap Classification
- Implemented Strengthening, if any
- Test Results
- Verification
- Remaining Issues
- Future Q Candidates
- Suggested Commit Message
- Repository Recommendation

---

## Suggested Future Q Candidates

Create only when supported by this review:

- AI Startup Context Manifest
- Repository Context Requirement Registry
- Pre-Response Repository Context Validator
- Context Freshness and Invalidation Rules
- Capability / Authority / Runtime State / Repository Context Integration
- AI Response Provenance Contract
- Repository-Aware Intent Resolution
- Self Improvement Readiness Context Gate

---

## Suggested Commit Message

```text
docs: strengthen AI startup repository synchronization
```

---

## Repository Recommendation Expectation

At completion, Codex must report current repository recommendation state explicitly.

Expected default unless evidence requires otherwise:

```text
Commit: Recommended
Push: Hold
Tag: Hold
```

Codex must not execute Commit / Push / Tag.
