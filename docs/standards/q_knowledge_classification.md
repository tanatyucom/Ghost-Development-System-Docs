# Q Knowledge Classification Standard

**Status:** Draft Standard

**Last Updated:** 2026-07-17

## Purpose

GDS Q files are not only feature requests. They may preserve philosophy,
architecture, improvement, research, investigation, and knowledge promotion.

This standard distinguishes Q Type from Knowledge Asset Type.

```text
Q Type = why / purpose of the work
Knowledge Asset Type = what artifact is produced
```

## Q Types

| Q Type | Primary Purpose | Typical Output |
| --- | --- | --- |
| `feature` | Capability addition. | feature docs, workflow, implementation |
| `architecture` | Structure, boundary, contract, schema, workflow, dependency. | architecture, schema, ADR |
| `platform_philosophy` | North Star, collaboration model, design principles. | philosophy, experience principles |
| `improvement` | Observation, root cause, recurrence prevention. | improvement record, rule updates |
| `refactoring` | Internal quality without changing external behavior. | refactor plan, validation |
| `knowledge_promotion` | Promote reusable knowledge into assets. | rule, template, workflow, ADR |
| `research` | Comparative investigation before decision. | research report, recommendation |
| `investigation` | Evidence-based analysis of unknown or inconsistent state. | findings, evidence, next action |

## Multi-Classification

A Q may have one primary type and multiple secondary types.

Example:

```yaml
q_type:
  primary: improvement
  secondary:
    - platform_philosophy
    - knowledge_promotion
origin:
  kind: observed_case
promotion_candidate: true
experience_impact: high
human_approval_required: true
```

## Knowledge Asset Types

| Asset Type | Meaning |
| --- | --- |
| Architecture | Structure or boundary. |
| Philosophy | North Star or design principle. |
| Experience | User journey or collaboration state. |
| Rule | Mandatory behavior or prohibition. |
| Schema | Data or artifact shape. |
| Template | Reusable artifact form. |
| Workflow | Repeated sequence. |
| Example | Good / bad example. |
| Case | Concrete observed situation. |
| Improvement Record | Observation to improvement lifecycle. |
| ADR | Architecture decision record. |
| Report / Evidence | Result or proof artifact. |

## Rules

- Q Type and Knowledge Asset Type must not be mixed.
- If classification is ambiguous, use SCW.
- Primary Type should explain why the Q exists.
- Secondary Types should explain important additional motives.
- Promotion candidates require Human Approval before canonical promotion.

## Related Documents

- `docs/architecture/knowledge_candidate_classification_contract.md`
- `docs/architecture/design_intent_preservation.md`
- `templates/Q_TEMPLATE.md`
