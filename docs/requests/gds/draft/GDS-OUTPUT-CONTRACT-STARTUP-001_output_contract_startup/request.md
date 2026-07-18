# Q_GDS_OUTPUT_CONTRACT_STARTUP_001

Status: Draft
Priority: High
Category: AI Quality / Startup / Output Contract

## Title

Strengthen Startup and AI Response Checklist to preserve project-specific Output Contracts across new chat sessions.

---

## Background

During GDS7 planning, ChatGPT correctly completed Startup, Repository synchronization,
and the AI Response Checklist.

However, when generating a reusable project artifact for Codex review,
the output was returned inline instead of the project's standard downloadable
Markdown format.

This behavior reappeared after starting a new chat, even though similar
improvements had previously been discussed.

The issue was not a repository knowledge problem.

It was a project-specific output workflow problem.

---

## Problem

Current Startup verifies:

- Repository synchronization
- AI Repository Index
- Constraint Check
- Human Approval boundaries

However, it does not sufficiently preserve project-specific output rules.

Example:

Reusable project artifact
↓

Returned as inline text

Expected:

Reusable project artifact
↓

Markdown file
↓

Download link

---

## Goal

Introduce an Output Contract that survives Startup and is verified before
producing any reusable project artifact.

---

## Proposed Rule

If the primary deliverable is a reusable project artifact
(Q, ADR, Roadmap, Handoff, Report, Specification, Review Request, etc.),

THEN

Deliver it as a downloadable Markdown file by default.

Do not return only inline text unless explicitly requested.

---

## AI Response Checklist Addition

Output

- □ Is this a reusable project artifact?
- □ Does the project Output Contract require a downloadable file?
- □ Is an existing artifact being revised?
- □ Is inline text explicitly requested instead?

---

## Expected Result

New chat sessions should continue following the project Output Contract
without reverting to generic ChatGPT output behavior.

---

## Evidence

Observed during GDS7 planning:

- Startup completed successfully.
- Repository synchronization completed.
- AI Response Checklist executed.
- Downloadable artifact requirement was nevertheless omitted.

---

## Suggested Commit Message

docs: add output contract startup improvement proposal
