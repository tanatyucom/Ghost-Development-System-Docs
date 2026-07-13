# Review Center Workflow

## Purpose

This workflow defines how a Review Center session moves from source artifacts
to human decision export and gate readiness.

## Standard Flow

```text
Source Artifacts
  -> Review Plugin / Adapter
  -> Review Item Preparation
  -> Review Center Session
  -> Artifact Display
  -> Human Decision
  -> Save / Resume
  -> Review Result Export
  -> Domain Gate Adapter
  -> Gate Readiness Summary
  -> Completion Report
```

## Startup

Before a Review Center session starts:

- Confirm plugin id and version.
- Confirm source batch identity.
- Confirm source fingerprint.
- Confirm artifact availability.
- Confirm decision schema.
- Confirm storage location.
- Confirm commit / push policy.

## Review Session

During review:

- Show current item and total count.
- Display artifacts in stable order.
- Capture required decisions.
- Capture notes.
- Validate required fields.
- Save explicitly.
- Allow previous / next / jump navigation.
- Preserve corrections as revisions.

## Resume

When reopening:

- Load session file.
- Compare source fingerprint.
- Compare plugin version.
- Detect stale session.
- Resume from the next unreviewed or selected item.
- Warn on missing artifacts.

## Export

Export only after:

- required fields are complete;
- required artifacts are present;
- retry / rejected counts are summarized;
- superseded revisions are preserved;
- reviewer / approval state is recorded.

Canonical v1 export:

```text
review_result_export.json
```

## Gate Handoff

Review Center hands the export to a domain gate adapter.

The gate adapter decides how domain readiness is interpreted. Review Center
does not repair data or perform production changes.

## Completion

Completion Report must include:

- session id;
- plugin id and version;
- source fingerprint;
- reviewed count;
- approved count;
- retry count;
- blocked count;
- export path;
- gate readiness status;
- remaining issues;
- GameGhost edit status;
- commit / push status.

