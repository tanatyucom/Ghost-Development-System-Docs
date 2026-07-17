# Dependency And Sequence Map

## Dependency Classification

| Source | Target | Type | Reason |
| --- | --- | --- | --- |
| Intent Engine | Startup Enforcement | Hard dependency | Startup gate needs classified artifact/action intent. |
| Intent Engine | Workflow Resolver | Hard dependency | User intent must route to a governed workflow. |
| Workflow Resolver | Startup Enforcement | Hard dependency for artifacts | Startup gate must know which workflow governs generation. |
| Knowledge Requirement Resolver | Startup Enforcement | Hard dependency for artifacts | Startup gate must know required knowledge before generation. |
| Repository Quality | Command Center | Soft / gate input | Command Center should consume quality status, but quality does not orchestrate. |
| Repository Quality | Completion Review | Hard dependency | Completion Report must record validation and quality state. |
| Startup Enforcement | Template Engine | Hard dependency | Drafting should start only after PASS / PASS_WITH_LIMITATION. |
| Command Center | Startup Enforcement | Integration dependency | Command Center routes artifact draft requests through the gate. |
| Command Center | Knowledge Promotion | Soft / learning loop | Command Center may surface candidates; promotion still needs approval. |
| Completion Review | Knowledge Promotion | Hard dependency | Promotion candidates come from reviewed completion evidence. |
| Artifact Schema Standard | Shared Evidence Contract | Soft dependency | Existing artifact schema can inform, but does not fully define runtime execution evidence. |

## Circular Dependency Risks

| Risk | Resolution |
| --- | --- |
| Startup Enforcement tries to own Intent classification and workflow resolution. | Intent Engine owns interpretation; Startup Enforcement consumes classified intent and resolved workflow evidence. |
| Command Center owns every engine's reasoning. | Command Center orchestrates and displays outputs; engines own domain logic. |
| Repository Quality becomes a passive report only. | Repository Quality owns quality evidence and gate status, consumed by Command Center and Completion Review. |
| Knowledge Promotion enters before completion evidence exists. | Knowledge Promotion may inform required knowledge, but canonical promotion remains post-review and approval-gated. |
| STARTUP-005 creates Startup-only schema that later conflicts with Command Center evidence. | Create shared execution evidence contract first, then specialize Startup evidence. |

## Recommended Platform Core Sequence

```text
Intent Engine / Intent Registry
  -> Shared Platform Execution Evidence Contract
  -> Startup Enforcement Evidence Specialization
  -> Repository Quality Runtime Gate Contract
  -> Command Center Core Orchestration Contract
  -> Template Engine / Artifact Pipeline Preflight
  -> Completion Review
  -> Knowledge Promotion
```

## Why This Sequence

- It keeps orchestration separate from reasoning.
- It lets STARTUP-005 become a specialization rather than a competing schema.
- It keeps Repository Quality as real gate evidence.
- It gives Command Center a stable contract to consume.
- It preserves Human Approval and SCW before runtime implementation begins.
