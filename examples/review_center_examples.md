# Review Center Examples

## Good Example: Platform / Adapter Split

```text
platform/frameworks/review_center/
  review_center_gui.py
  review_session_service.py
  review_storage.py
  review_models.py
  review_result_schema.py
  review_plugin_registry.py
  review_gate_workflow.py

platform/adapters/
  gameghost_steam_ocr_review_adapter.py
```

Why this is good:

- Platform owns session, storage, models, GUI, and export.
- GameGhost owns Steam OCR source mapping and gate conversion.
- Review Center does not know whether a BBox is correct.

## Bad Example: Steam OCR Logic in Platform Core

```text
platform/frameworks/review_center/
  steam_ocr_bbox_checker.py
  steam_title_matcher.py
```

Why this is bad:

- Platform code contains GameGhost-specific correctness logic.
- Future AnimeGhost / ComicGhost adapters inherit wrong assumptions.
- Human approval boundary becomes unclear.

## Good Example: Explicit Approval State

```json
{
  "review_item_id": "steam_ocr_001_0007",
  "decision_values": {
    "target_row": "PASS",
    "bbox": "PASS",
    "ocr": "RETRY",
    "metadata": "PASS",
    "alias": "NOT APPLICABLE"
  },
  "approval_state": "Reviewed",
  "revision_number": 1
}
```

Why this is good:

- Review and approval are explicit.
- Retry state can be handed to the gate.
- The item can be corrected later with revision 2.

## Bad Example: Silent Auto Approval

```json
{
  "review_item_id": "steam_ocr_001_0007",
  "auto_approved": true
}
```

Why this is bad:

- It hides the human decision.
- It cannot explain which fields were reviewed.
- It violates Human Approval First.

## Good Example: Resume

```text
Session: steam_ocr_review_2026_07_13
Progress: 11 / 93
Action: close
Action: reopen
Resume: 12 / 93
```

Why this is good:

- Interruption is expected.
- The next item is clear.
- Human review can continue without remembering chat context.

## Bad Example: Transient State Only

```text
The GUI remembers progress until the window closes.
```

Why this is bad:

- Review progress is lost after interruption.
- Gate readiness cannot be audited.
- The result cannot be safely resumed.

