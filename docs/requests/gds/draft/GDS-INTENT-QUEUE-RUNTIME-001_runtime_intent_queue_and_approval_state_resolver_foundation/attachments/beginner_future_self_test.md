# Beginner / Future Self Test

## Questions

1. What is the difference between `お願いします` and `これ全てお願いします`?
2. What does `全て` include?
3. Why are Approval Accepted and Execution Completed separate?
4. What state should Commit have when ChatGPT lacks local Git authority?
5. What happens before Commit Evidence is received?
6. What must each queue item display?
7. What happens if scope changes after approval?
8. Is Tag always a candidate?
9. What happens if GameGhost mutation is detected?
10. Can GDS show completed without evidence?

## Expected Answers

1. `お願いします` selects Requested Operations only. `これ全てお願いします`
   selects visible Requested Operations and visible Follow-up Candidates.
2. Only displayed selectable items.
3. Approval allows an operation; evidence proves it happened.
4. `DELEGATED`, `BLOCKED_BY_AUTHORITY`, or `WAITING_FOR_EVIDENCE`, never
   `COMPLETED` without evidence.
5. The item remains waiting for evidence.
6. State, actor, authority, dependencies, evidence, and next action.
7. Approval is invalidated and SCW is required.
8. No. Tag requires release or milestone criteria.
9. Stop immediately; no commit / push / tag.
10. No.
