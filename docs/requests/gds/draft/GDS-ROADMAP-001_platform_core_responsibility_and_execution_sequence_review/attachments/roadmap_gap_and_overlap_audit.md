# Roadmap Gap And Overlap Audit

## Roadmap Reviewed

- `roadmap/ghost_development_system_roadmap.md`
- `roadmap/README.md`
- `roadmap/platform_evolution_track.md`

## Current Alignment

The Master Roadmap already identifies:

- Platform Integration Era as the current phase.
- Command Center as Repository Orchestrator.
- Intent-Driven Workflow as a priority platform candidate.
- Knowledge Promotion Engine as an architecture candidate.
- Intent-Aware Startup Enforcement as an architecture candidate.
- Repository Quality as a foundation capability and quality gate.

## Gaps

| Gap | Impact | Resolution |
| --- | --- | --- |
| STARTUP-004 runtime architecture was not reflected in roadmap current position. | Next Q could incorrectly jump to STARTUP-005 without shared contract review. | Add Platform Core sequencing priority. |
| Shared execution evidence contract is not named as a prerequisite. | Startup schema could duplicate future Command Center / Quality evidence schema. | Recommend Common Platform Execution Evidence Contract as next Q. |
| Repository Quality role is present but not explicitly tied to Platform Core runtime sequence. | Quality could be treated as report-only. | Record it as gate evidence input and completion validation owner. |
| Resolver ownership is split across Intent Engine and Startup Runtime without a shared contract. | Duplicate resolver schema risk. | Defer resolver contract to a follow-up after shared evidence contract. |

## Overlaps

| Overlap | Risk | Resolution |
| --- | --- | --- |
| Runtime Startup Enforcement includes Artifact Intent Classifier / Workflow Resolver / Knowledge Requirement Resolver components. | Could conflict with Intent Engine ownership. | Treat Startup Runtime as consumer of classified / resolved evidence, not owner of natural language interpretation. |
| Command Center can prepare drafts and recommend next Q. | Could become monolith or approval replacement. | Preserve orchestration-only boundary and Human Approval Gate. |
| Artifact Schema Standard and future execution evidence schema both describe common fields. | Duplicate schema naming risk. | Treat Artifact Schema Standard as managed artifact body schema; execution evidence contract as pre-execution runtime evidence. |
| Knowledge Promotion consumes completion evidence and influences future knowledge requirements. | Could mutate knowledge too early. | Allow advisory input; canonical promotion remains post-review and approval-gated. |

## Roadmap Revision Decision

Roadmap update is required, but only as a minimal alignment update:

- update Last Updated date;
- add Platform Core sequencing priority;
- add a Platform Core Responsibility and Execution Sequence Review section;
- keep GameGhost OCR / SDK / Project Adoption current direction visible;
- do not replace the Master Roadmap or approve runtime implementation.
