# Research Mission Startup Profile Integration Notes

## Initial Review

- Research Mission Template, Workflow, and Rules already exist.
- AI Startup Procedure already referenced Research Mission, but did not yet
  define Research Task Detection as an explicit startup branch.
- Project Profiles had a reading order, but did not yet mention Research
  Mission branch behavior.

## Design Decision

Research Task Detection is placed after Current Q / Information Package,
repository context, rules/templates, and scope confirmation.

Reason:

- The system needs the Q and current state before deciding whether the task is
  research.
- Repository and scope must still be validated before research starts.
- Normal implementation must remain unaffected when Research Task Detection is
  No.

## Scope Guard

- GameGhost profile and runtime repository were not edited.
- Command Center, CI, and runtime implementation are out of scope.

