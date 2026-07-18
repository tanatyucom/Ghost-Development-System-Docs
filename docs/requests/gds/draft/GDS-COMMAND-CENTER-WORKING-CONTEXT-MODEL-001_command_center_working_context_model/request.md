# Q_GDS_COMMAND_CENTER_WORKING_CONTEXT_MODEL_001

## Title

**Define the Command Center Working Context Model**

## Background

Bootstrap, Startup, Repository Context Evidence, and the Command Center AI
Project Manager architecture have been established.

Working Context has emerged as the next architectural concept.

It should not become a second source of truth. Instead, it should be generated
from Repository state and evidence.

## Objective

Define the Working Context model used by the Command Center.

Determine how it should be generated, refreshed, and presented without
duplicating repository state.

Implementation is explicitly out of scope.

## Scope

Evaluate whether Working Context should include:

- Current Priority
- Current Focus
- Current Mission
- Active Q
- Repository Health
- Approval Status
- Completion Review Status
- Deferred Items
- Blocking Issues
- Recommended Next Action

Evaluate refresh triggers:

- Startup completed
- Repository changed
- Completion Review completed
- Approval state changed
- Current Mission changed

Clarify relationships between:

- Repository
- Repository Context Evidence
- Working Context
- Command Center
- Human Approval

## Out of Scope

- No implementation
- No new repository state
- No Startup modification
- No Bootstrap modification
- No Approval workflow modification

## Expected Deliverables

- Working Context architecture proposal
- Responsibility boundaries
- Refresh model
- Lifecycle proposal
- Future roadmap recommendation

## Expected Review Questions

- Should Working Context always be generated?
- Should it ever be stored?
- Should it only exist temporarily?
- What belongs in Working Context versus Repository Context Evidence?
- What should never appear in Working Context?

## Success Criteria

Determine whether Working Context should become a generated operational view
rather than a persistent project asset.

Repository remains the Single Source of Truth.

Working Context remains a derived operational model.

Implementation is deferred.

## Priority

- Future Candidate
- Architecture Only
- No implementation
