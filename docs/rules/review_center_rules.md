# Review Center Rules

## Purpose

Review Center Rules define the operating rules for shared Ghost Platform human
review sessions.

## Core Rule

Review Center manages human review sessions. It must not decide domain
correctness automatically.

## Human Approval First

No Review Center component may automatically approve an item, gate, repair, or
production change.

Reviewed and Approved are separate states. One-person operation may record both
states in one interaction, but the exported result must preserve the approval
state explicitly.

## Platform / Domain Boundary

Platform owns:

- session lifecycle;
- artifact presentation contract;
- decision capture;
- progress;
- persistence;
- navigation;
- result export;
- approval state.

Domain plugin / adapter owns:

- item preparation;
- domain labels;
- domain choices;
- domain validation;
- gate adapter;
- repair or retry action definitions.

## GUI Rule

The canonical GUI entry point is:

```text
review_center_gui.py
```

Do not use `app.py`, `main.py`, or `review_center.py` as the primary GUI entry
point.

GUI must not contain domain correctness logic.

## Persistence Rule

Review sessions must support explicit save and resume.

Canonical v1 storage is JSON.

Autosave is allowed only after local validation succeeds and unsaved state is
visible to the reviewer.

## Missing Artifact Rule

Missing required artifacts block Approved.

Missing optional artifacts may warn and allow review to continue.

## Correction Rule

Correcting a previous decision must create a new revision and mark the previous
result Superseded.

Do not silently overwrite review history.

## Plugin Registration Rule

Review plugins and adapters must be explicitly registered.

No uncontrolled folder scanning, reflection discovery, or automatic plugin
loading is approved by this rule.

## Gate Rule

Review Center exports results to a gate adapter. It does not execute production
changes.

Gate readiness must be visible as:

- `not_ready`
- `ready_with_retry_items`
- `ready`
- `blocked`

## Legacy Rule

Legacy review entry points must remain until Review Center completes a real
review, output parity is verified, the gate consumes the new output, and a
recovery path exists.

## Related Documents

- `docs/architecture/review_center_architecture.md`
- `docs/workflow/review_center_workflow.md`
- `docs/architecture/platform_first_migration_strategy.md`
- `docs/architecture/platform_discoverability_and_component_standard.md`
- `docs/architecture/plugin_architecture_standard.md`

