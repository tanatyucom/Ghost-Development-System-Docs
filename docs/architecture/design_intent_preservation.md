# Design Intent Preservation

**Status:** Draft Architecture

**Last Updated:** 2026-07-17

## Purpose

Design Intent Preservation prevents GDS generations from preserving files and
contracts while losing the intended human / AI collaboration experience.

The reference case is the GDS5 to GDS6 transition, where Evidence, Contract,
Review, and Ready structures were inherited, but the Approval Request and
Pending Human Approval experience temporarily became less visible.

## Root Cause Summary

| Root Cause | Meaning | Prevention |
| --- | --- | --- |
| What without Why | Structures were preserved more strongly than purpose. | Store North Star and Vision Scenario. |
| Architecture without Experience | Internal contracts existed, but user journey was not a canonical asset. | Add Experience Layer. |
| Missing Vision Scenario | Finished collaboration conversation was not testable. | Use Vision Scenario Template. |
| Startup did not resync North Star | New generation did not reread the collaboration goal. | Add Startup Goal Alignment. |
| End-to-End flow fragmented | Intent, Evidence, Review, Approval, Execution lived in separate docs. | Preserve End-to-End User Journey. |
| Handoff criteria too structural | Handoff checked files but not experience continuity. | Add Handoff Template v2 checks. |

## Improvement Record Shape

```text
Observation
  -> Evidence
  -> Root Cause
  -> Decision
  -> Improvement
  -> Verification
  -> Promotion Target
  -> Result
```

## Promotion Targets

- Handoff Rule.
- Handoff Template.
- Vision Scenario Template.
- Experience Contract.
- Platform Ready Review Checklist.
- Q Classification Rule.

## Related Documents

- `docs/architecture/experience_layer.md`
- `docs/philosophy/north_star.md`
- `templates/HANDOFF_TEMPLATE_V2.md`
- `templates/VISION_SCENARIO_TEMPLATE.md`
- `docs/standards/q_knowledge_classification.md`
