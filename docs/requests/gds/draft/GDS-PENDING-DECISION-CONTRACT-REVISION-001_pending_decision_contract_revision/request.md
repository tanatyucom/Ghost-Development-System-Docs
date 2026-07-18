# Q_GDS_PENDING_DECISION_CONTRACT_REVISION_001

Status: Draft
Priority: High
Category: Revision / Startup Governance

## Purpose

Revise the existing GDS governance documents to introduce a Pending Decision
Contract as a temporary startup review mechanism.

This is NOT a new canonical knowledge layer.

Pending Decisions exist only as temporary records until promoted,
rejected, superseded, or archived.

---

## Background

Architecture review concluded PASS WITH REVISIONS.

Key conclusion:

Pending Decisions should be treated as:

Conversation-approved but not-yet-canonical decisions.

They must never become a second canonical repository.

---

## Scope

Revise existing governance documentation.

Do not introduce a parallel architecture.

Focus on:

- Pending Decision definition
- Startup review position
- Promotion lifecycle
- Human Approval boundary
- Relationship with Pending Insight and Pending Action

---

## Revision Objectives

### 1. Pending Decision Contract

Define:

- Purpose
- Lifetime
- Ownership
- Startup visibility
- Canonical promotion rules

---

### 2. Classification

Clarify differences between:

- Conversation Insight
- Pending Insight
- Pending Decision
- Pending Action
- Q
- ADR

---

### 3. Lifecycle

Conversation Decision
-> Human Approval To Record
-> Pending Decision
-> Startup Review
-> Classification
-> Canonical Integration / Rejected / Superseded / Archived

---

### 4. Minimum Metadata

- Decision ID
- Title
- Source Conversation
- Human Approval Evidence
- Decision Summary
- Scope
- Integration Target
- Status
- Conflict Check
- Next Action
- Review / Expiration Condition

---

### 5. Startup Integration

Startup should:

Repository Sync
-> Pending Decision Review
-> Current Mission
-> Development

Pending Decisions are reviewed only.

They are never treated as canonical knowledge.

---

## Acceptance Criteria

- Pending Decision is clearly separated from canonical knowledge.
- Startup review position is defined.
- Lifecycle is standardized.
- Pending Insight / Pending Action differences are documented.
- Repository First remains unchanged.

---

## Constraints

- Repository First
- Revision First
- Evidence First
- Human Approval First
- SCW (Stop -> Call -> Wait)

Review existing documents before adding new ones.
