# ADR-GDS-011: Continuity Quality And Design Context Handover

**Status:** Accepted
**Decision Date:** 2026-07-24

## Context

The GDS8 to GDS9 transition preserved decisions and next actions but did not
fully preserve the rationale, rejected options, assumptions, and terminology
behind Repository Evolution. The receiving session therefore reconstructed a
different emphasis. Execution Context was complete; Handover Context was not.

## Decision

- Manage Decision History, not only current decisions.
- Treat Handover as Design Context Transfer.
- Manage Project State with explicit canonical values.
- Adopt a mandatory Context Contract for handovers.
- Adopt Session Summary as a standard continuity artifact.
- Treat Continuity Quality as a formal GDS quality concern.

## Consequences

Later sessions gain a reproducible entry point and can distinguish fact,
decision, rationale, rejection, assumption, and unknown. Handover artifacts are
larger and require validation, but they reduce interpretive drift.

This ADR does not implement runtime memory, automatic handover generation, or
Template Validation automation. Those require separate Q files.

## Rejected Options

- Keep status-only handovers: rejected because design rationale remains absent.
- Store full chat transcripts: rejected because they are noisy, noncanonical,
  may contain secrets, and do not provide a governed decision model.
- Add Template Validation automation to this Q: rejected to preserve one Q =
  one responsibility.

## Related Documents

- `docs/architecture/handover_framework_v2.md`
- `templates/HANDOFF_TEMPLATE_V2.md`
- `docs/standards/decision_history_standard.md`
- `docs/standards/handover_context_contract.md`
- `docs/standards/project_state_standard.md`
- `docs/standards/session_summary_standard.md`
