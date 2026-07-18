# Q_GDS_APPROVAL_STANDARD_REVISION_001

Status: Draft
Priority: High
Category: Revision / Governance / Approval

## Purpose

Revise the existing Approval Request documents rather than creating a new
approval architecture.

Architecture review has concluded PASS WITH REVISIONS.

This Q requests revision of the existing Approval Request documentation.

---

## Background

Operational validation identified a governance gap.

Observed case:

- Codex completed review.
- Repository Recommendation was not displayed.
- ChatGPT performed Completion Review.
- Human issued approval.
- Execution target became ambiguous.

The issue is caused by incomplete Rule and Template standardization rather than
a runtime defect.

---

## Scope

Revise existing Approval Request documents.

Primary targets:

- docs/rules/approval_request_rules.md
- docs/workflow/approval_request_intent_queue_workflow.md
- templates/approval_request_block_template.md

If required:

- docs/architecture/approval_request_intent_queue_execution_evidence.md

No new parallel approval system.

---

## Revision Objectives

### 1. Responsibility Boundaries

Define:

Codex
-> Repository Recommendation

ChatGPT
-> Workflow Recommendation / Completion Review

Human
-> Final Approval

Codex / Adapter
-> Governed Execution

Execution Evidence
-> Execution Proof

Codex and ChatGPT provide recommendations only.

Human performs Final Approval.

---

### 2. Approval Rules

Standardize:

- Repository Recommendation required before Human Approval
- If Repository Recommendation is missing, trigger SCW or re-display
- Commit / Push / Tag are independent Approval Units
- Review PASS does not equal Commit approval
- Commit approval does not equal Push approval
- Approval without Approval Request Block is invalid

---

### 3. Approval Request Block Revision

Extend the existing template with:

- Recommendation Source
- Repository Recommendation
- Workflow Recommendation
- Safe Commit Set
- Validation Summary
- Repository State Lock
- Approval Units
- Execution Authority
- Evidence Required After Execution

Keep one common Approval Request Block.

Do not split Codex and ChatGPT templates unless necessary.

---

### 4. Presentation

Approval Request Block should remain concise.

Detailed evidence should be referenced rather than embedded.

---

## Acceptance Criteria

- Responsibility boundaries are explicit.
- Recommendation, Approval, and Execution Evidence are separated.
- Approval Request Block is standardized.
- Commit / Push / Tag use independent approval.
- Existing documentation revised without creating duplicate architecture.

---

## Constraints

- Repository First
- Revision First
- Evidence First
- Human Approval First
- SCW (Stop -> Call -> Wait)

Repository modification only after review and approval.
