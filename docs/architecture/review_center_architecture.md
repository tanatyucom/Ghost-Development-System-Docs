# Review Center Architecture

Q ID: GDS-REVIEW-CENTER-001
Status: Standard
Date: 2026-07-13

## Purpose

Review Center is the shared Ghost Platform architecture for human review
management.

Review Center is not an automatic judge. It is a Human Review Session Manager.

It owns:

- artifact presentation contract;
- review session progress;
- decision capture;
- persistence and resume;
- result export;
- gate readiness summary.

It does not own domain correctness.

## Core Definition

```text
Review Center = Human Review Session Manager
```

Review Center displays evidence, receives human decisions, manages progress,
saves review state, resumes interrupted sessions, and exports results to a gate
adapter.

Domain-specific judgment belongs to the human reviewer and the registered
plugin / adapter.

## Platform / Domain Boundary

Platform:

- Review session lifecycle.
- Artifact presentation contract.
- Decision field contract.
- Progress management.
- Save / resume.
- Navigation.
- Result export.
- Approval state.
- Gate readiness summary.
- Plugin registration boundary.

Domain:

- Review item preparation.
- Domain labels.
- Domain choices.
- Domain validation.
- Artifact selection.
- Source data mapping.
- Domain gate adapter.
- Repair / retry actions.

Required boundary statement:

```text
Platform:
Review session, artifact presentation contract, decision capture,
progress, persistence, navigation, result export, approval state.

Domain:
Review item preparation, domain labels, domain choices,
domain validation, domain gate adapter.
```

## Canonical Component Structure

Canonical structure:

```text
platform/
  frameworks/
    review_center/
      README.md
      review_center_gui.py
      review_session_service.py
      review_storage.py
      review_models.py
      review_result_schema.py
      review_plugin_registry.py
      review_gate_workflow.py
      artifact_viewer/
        README.md
      plugins/
        README.md
```

Adapter structure:

```text
platform/
  adapters/
    gameghost_steam_ocr_review_adapter.py
```

Rules:

- GUI entry point must be named `review_center_gui.py`.
- `app.py`, `main.py`, and `review_center.py` must not be the primary GUI entry
  point.
- Core models, storage, plugin registry, and gate workflow must be testable
  without GUI.
- GUI may be Streamlit or another toolkit, but Review Core must not depend on a
  GUI framework.

## Component Responsibilities

| Component | Responsibility | Must Not Own |
| --- | --- | --- |
| `review_center_gui.py` | Human-facing review management UI. | Domain correctness or gate execution. |
| `review_session_service.py` | Session lifecycle, current item, progress, save / next behavior. | Artifact source generation. |
| `review_storage.py` | Atomic persistence, backup, recovery, stale session detection. | Domain validation rules. |
| `review_models.py` | Review Item, Artifact, Decision Field, Session, Result data contracts. | UI rendering decisions. |
| `review_result_schema.py` | Export shape and versioned schema. | Production changes. |
| `review_plugin_registry.py` | Explicit plugin registration and compatibility checks. | Automatic uncontrolled discovery. |
| `review_gate_workflow.py` | Gate readiness summary and export handoff. | Gate approval or production execution. |
| `artifact_viewer/` | Generic rendering contract for images, overlays, text, metadata, tables. | Domain evidence selection. |
| `plugins/` | Review plugin contract examples / registry stubs. | Hidden project-specific behavior. |

## Review Item Model

Minimum fields:

| Field | Required | Notes |
| --- | --- | --- |
| `review_item_id` | Yes | Stable item identity within a session. |
| `source_type` | Yes | Domain source type, such as `steam_ocr_row`. |
| `source_record_id` | Yes | Source record identity. |
| `display_title` | Yes | Human-readable title. |
| `artifacts` | Yes | List of Review Artifact descriptors. |
| `decision_fields` | Yes | List of Review Decision Field descriptors. |
| `default_values` | No | Optional defaults from plugin. |
| `current_decision` | No | Latest saved decision. |
| `notes` | No | Human notes. |
| `status` | Yes | Unreviewed / In Review / Reviewed / Approved / Rejected / Retry Requested / Superseded. |
| `created_at` | Yes | ISO-like timestamp. |
| `updated_at` | Yes | ISO-like timestamp. |
| `plugin_id` | Yes | Registered plugin identity. |
| `source_provenance` | Yes | Source file, batch, fingerprint, or URI. |

## Review Artifact Model

Supported initial artifact types:

- `image`
- `overlay`
- `bounding_box`
- `text`
- `structured_metadata`
- `comparison_table`
- `source_link`
- `debug_file`
- `json_fragment`
- `csv_fragment`

Minimum fields:

| Field | Required | Notes |
| --- | --- | --- |
| `artifact_id` | Yes | Stable artifact identity within item. |
| `artifact_type` | Yes | One supported type. |
| `label` | Yes | Human-facing label. |
| `path_or_uri` | Yes | File path, URI, or source reference. |
| `mime_type` | No | Required when display is ambiguous. |
| `display_order` | Yes | Stable ordering. |
| `metadata` | No | Optional structured data. |
| `required` | Yes | Missing required artifacts block approval. |
| `missing_behavior` | Yes | `block`, `warn`, or `skip`. |

## Review Decision Field Model

Supported initial field types:

- `single_choice`
- `boolean`
- `text_note`
- `read_only_comparison`
- `numeric_optional`

Minimum fields:

| Field | Required | Notes |
| --- | --- | --- |
| `field_id` | Yes | Stable field id. |
| `label` | Yes | Human-facing label. |
| `type` | Yes | Supported field type. |
| `allowed_values` | Conditional | Required for `single_choice`. |
| `required` | Yes | Required fields block Reviewed / Approved if incomplete. |
| `default` | No | Optional default. |
| `help_text` | No | Human guidance. |
| `domain_validation_ref` | No | Adapter or plugin validation reference. |

## Review Session Model

Minimum fields:

| Field | Required | Notes |
| --- | --- | --- |
| `review_session_id` | Yes | Stable session identity. |
| `plugin_id` | Yes | Registered plugin identity. |
| `source_batch_identity` | Yes | Human-readable source batch. |
| `total_items` | Yes | Total number of items. |
| `current_item_index` | Yes | Zero- or one-based index must be documented. |
| `reviewed_count` | Yes | Count of reviewed items. |
| `remaining_count` | Yes | Count of remaining items. |
| `created_at` | Yes | Creation timestamp. |
| `last_opened_at` | Yes | Last resume timestamp. |
| `completed_at` | No | Set when session is complete. |
| `reviewer` | No | Optional for one-person operation. |
| `status` | Yes | Draft / In Review / Complete / Exported / Superseded. |
| `storage_version` | Yes | Review Center storage schema version. |
| `source_fingerprint` | Yes | Detects stale source batches. |

## Review Result Model

Minimum fields:

| Field | Required | Notes |
| --- | --- | --- |
| `review_item_id` | Yes | Links result to Review Item. |
| `decision_values` | Yes | Values keyed by decision field id. |
| `notes` | No | Human notes. |
| `reviewed_at` | Yes | Timestamp. |
| `reviewer` | No | Optional for one-person operation. |
| `revision_number` | Yes | Incremented when corrected. |
| `approval_state` | Yes | Reviewed / Approved / Rejected / Retry Requested / Superseded. |
| `plugin_version` | Yes | Plugin version used for review. |
| `source_fingerprint` | Yes | Source batch fingerprint. |

## Human Approval Model

States:

```text
Unreviewed
In Review
Reviewed
Approved
Rejected
Retry Requested
Superseded
```

Decision:

- Reviewed and Approved are separate states.
- In one-person operation, a reviewer may mark a result as Approved during the
  same interaction, but the exported data must still record both review and
  approval state.
- Revised decisions supersede earlier results by increasing
  `revision_number` and marking the previous result `Superseded`.
- Required fields and required missing artifacts block Approved.
- No automatic approval is allowed.

## Persistence and Resume

Canonical storage for v1:

```text
JSON session file
```

Future optional storage:

```text
SQLite
```

JSON is canonical for v1 because it is diffable, portable, and easy to inspect
during early architecture validation.

Persistence rules:

- Save atomically by writing a temporary file and replacing the canonical file.
- Keep a timestamped backup before destructive reset or schema migration.
- Store `source_fingerprint`.
- Detect stale sessions when source fingerprint or plugin version changes.
- Missing required artifacts block approval.
- Missing optional artifacts warn but do not block review.
- Partial review is valid and resumable.
- Personal transient review state is not committed unless explicitly approved.

Resume example:

```text
11 / 93
-> close
-> reopen
-> resume from 12 / 93
```

## Navigation and Editing

Required behavior:

- Next.
- Previous.
- Jump to item.
- Save.
- Save and Next.
- Resume.
- Filter by status.
- Reopen reviewed item.
- Correct previous decision.
- Show unsaved state.
- Confirm destructive reset.

Autosave decision:

```text
Explicit Save is required.
Safe autosave is allowed only after a decision passes local validation.
```

The GUI must visibly indicate unsaved state.

## Gate Integration

Flow:

```text
Source Artifacts
  -> Review Plugin / Adapter
  -> Review Center Session
  -> Human Decision
  -> Review Result Export
  -> Domain Gate Adapter
  -> Gate
  -> Production Readiness
```

Canonical export format for v1:

```text
review_result_export.json
```

Export requirements:

- storage version;
- plugin id and version;
- source fingerprint;
- session summary;
- reviewed / approved / retry / rejected counts;
- per-item decisions;
- superseded revision trail;
- missing required artifact summary;
- gate readiness status;
- provenance.

Review Center does not execute production changes.

Gate readiness statuses:

- `not_ready`
- `ready_with_retry_items`
- `ready`
- `blocked`

## Steam OCR Vertical Slice

First concrete implementation target:

```text
GameGhost Steam OCR Human Review
```

Required initial artifacts:

- source screenshot;
- title crop;
- BBox overlay;
- OCR output;
- expected title;
- metadata comparison;
- alias comparison when available.

Initial decision groups:

| Group | Values |
| --- | --- |
| Target Row | PASS / WRONG TARGET / RETRY |
| BBox | PASS / MISSING TEXT / TOO TALL / TOO SHORT / OVERFLOW |
| OCR | PASS / FAIL / RETRY |
| Metadata | PASS / FAIL / NOT APPLICABLE |
| Alias | PASS / FAIL / NOT APPLICABLE |
| Notes | Free text |

Minimum Steam OCR adapter contract:

- provide Review Items from Steam OCR evidence;
- provide artifact descriptors;
- provide decision schema;
- validate required fields;
- export Review Result into Steam OCR gate input;
- preserve source screenshot and crop provenance;
- never mutate GameGhost production data directly from Review Center.

## Plugin / Adapter Contract

Review Center uses explicit registration.

Minimum plugin metadata:

| Field | Required |
| --- | --- |
| `plugin_id` | Yes |
| `display_name` | Yes |
| `version` | Yes |
| `supported_review_type` | Yes |
| `item_provider` | Yes |
| `artifact_provider` | Yes |
| `decision_schema_provider` | Yes |
| `result_exporter` | Yes |
| `gate_adapter` | Yes |
| `compatibility_version` | Yes |

No uncontrolled automatic discovery is allowed.

## Legacy Migration

Migration stages:

```text
Architecture
  -> Platform Core
  -> Steam OCR Adapter
  -> Parallel Verification
  -> Review Center production use
  -> Legacy Review Entry Point deprecation
  -> Thin redirect if needed
  -> Legacy removal
```

Do not delete legacy review behavior before:

- Review Center completes real Steam OCR review.
- Output parity is verified.
- Gate consumes new output.
- Recovery path exists.
- Human Approval is recorded.

## GUI Requirements

Minimum screen areas:

```text
Review Center Header
Source / Plugin Selector
Progress
Artifact Viewer
Comparison Area
Decision Panel
Notes
Save / Previous / Next
Session Status
Gate Readiness Summary
```

GUI rules:

- GUI is a management interface, not the source of truth.
- GUI must not contain domain correctness logic.
- GUI and Core must be separable.
- Streamlit is allowed for initial implementation if environment-compatible.
- Review Core must remain testable without GUI.

## Text Component Diagram

```text
Domain Source
  -> Review Plugin / Adapter
      -> Review Item Provider
      -> Artifact Provider
      -> Decision Schema Provider
  -> Review Center Core
      -> Session Service
      -> Storage
      -> Models
      -> Plugin Registry
  -> Review Center GUI
      -> Artifact Viewer
      -> Decision Panel
      -> Progress / Navigation
  -> Review Result Export
  -> Domain Gate Adapter
  -> Gate Readiness Summary
```

## Non-Functional Requirements

- Discoverable within 3 seconds.
- Safe for intermittent use.
- Usable after long periods of inactivity.
- Explicit error messages.
- No silent data loss.
- No silent approval.
- Portable within Ghost projects.
- UTF-8 safe.
- Testable without GUI.
- Source provenance preserved.
- Plugin failure isolated.
- Resume after interruption.

## Registry Decision

Review Center Architecture is a Platform Architecture Standard.

Review Center implementation, Steam OCR adapter implementation, analytics,
multi-user review, and Command Center integration remain future Q scope.

## Recommended Next Q

`Q_GameGhost_Review_Center_Core_and_Steam_OCR_Vertical_Slice_JP`

