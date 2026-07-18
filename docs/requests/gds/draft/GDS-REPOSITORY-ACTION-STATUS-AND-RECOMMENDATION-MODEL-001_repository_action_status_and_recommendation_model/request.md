# Q_GDS_REPOSITORY_ACTION_STATUS_AND_RECOMMENDATION_MODEL_001

## Title

Define the Repository Action Status and Recommendation Model

## Background

Completion Reports currently may present a suggested commit message without
making the actual execution state sufficiently prominent.

This can create operational ambiguity between:

- an action being recommended
- an action awaiting approval
- an action already executed

The issue was observed when a report included:

- Suggested Commit Message
- no executed commit
- no explicit, immediately visible Commit Status

Although the information was technically present, the presentation allowed a
human reviewer to momentarily confuse recommendation with execution.

This is an operational governance defect rather than a content defect.

## Objective

Define a standard model that clearly separates:

1. Execution Status
2. Repository Recommendation
3. Approval Status
4. Suggested Action Details
5. Execution Evidence

The model should prevent humans and AI agents from confusing proposed
repository actions with completed repository actions.

## Scope

Evaluate and define a common reporting structure for repository actions
including:

- Commit
- Push
- Tag
- Release
- Promotion
- SDK Export
- Other governed execution actions

Define explicit status values such as:

- Not Evaluated
- Not Recommended
- Recommended
- Approval Required
- Pending Human Approval
- Approved
- Rejected
- Not Executed
- Executing
- Completed
- Failed
- Blocked

Clarify the required separation between:

- Repository Recommendation
- Approval Request
- Human Approval
- Execution Status
- Execution Evidence
- Suggested Commit Message
- Suggested Command
- Commit ID
- Push Result
- Tag Result

Evaluate whether suggested action details should only appear when the related
action has not yet been executed.

## Problem Statement

The following presentation is potentially ambiguous:

```text
Suggested Commit Message

docs: define command center working context model
```

A human reviewer may momentarily interpret it as an executed commit message.

The preferred structure should make actual state visible before recommendation
details.

Example:

```text
Execution Status

Commit Status: Not Executed
Push Status: Not Executed
Tag Status: Not Executed

Repository Recommendation

Commit: Recommended
Push: Hold
Tag: Hold

Suggested Commit Message

docs: define command center working context model
```

When an action has been executed, the output should instead provide execution
evidence.

Example:

```text
Execution Status

Commit Status: Completed
Commit ID: abcdef1

Push Status: Not Executed
Tag Status: Not Executed
```

## Required Design Questions

- Which status fields are mandatory in every Completion Report?
- Should Execution Status always appear before Repository Recommendation?
- Should Suggested Commit Message be omitted after commit completion?
- How should approval state be displayed when no approval has yet been requested?
- How should rejected or expired approval be represented?
- How should partial execution be represented?
- How should failed execution differ from blocked execution?
- Which actions require immutable execution evidence?
- Should the same model be reused by Command Center and Current Priority views?
- How should the model connect to Human Approval and Action Execution workflows?

## Expected Deliverables

- Repository Action Status model
- Recommendation model
- Approval state model
- Execution evidence model
- Standard Completion Report section order
- Standard field names and allowed values
- Examples for Commit, Push, and Tag
- Guidance for suggested messages and commands
- Backward compatibility assessment
- Roadmap recommendation

## Proposed Reporting Order

The review should evaluate the following default order:

1. Completion Review Result
2. Execution Status
3. Repository Recommendation
4. Approval Status
5. Suggested Action Details
6. Approval Request
7. Execution Evidence

This order is a candidate only and may be revised during review.

## Out of Scope

This Q shall not:

- execute Commit, Push, Tag, or Release
- change current repository history
- bypass Human Approval
- grant automatic execution authority
- modify GameGhost
- implement Command Center UI
- implement an Execution Adapter
- change existing approval decisions

## Success Criteria

The review is successful when:

- recommendation and execution cannot reasonably be confused
- every governed repository action has an explicit execution state
- suggested action details are clearly labeled as non-executed proposals
- completed actions include concrete execution evidence
- Human Approval remains distinct from recommendation and execution
- the model can be reused across Completion Reports and future Command Center
  views
- no automatic repository mutation is introduced

## Priority

- Current Improvement Candidate
- Governance and Reporting Model
- Architecture / Specification Only
- No repository execution

## Initial Recommendation

Adopt the following principle:

```text
Recommendation describes what should happen.
Approval authorizes what may happen.
Execution Status records what is happening or has happened.
Execution Evidence proves what happened.
```

Repository mutation must remain governed by explicit Human Approval.
