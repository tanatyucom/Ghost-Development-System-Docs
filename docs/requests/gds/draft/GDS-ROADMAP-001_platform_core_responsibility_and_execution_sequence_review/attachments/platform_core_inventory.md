# Platform Core Inventory

## Purpose

This inventory identifies the canonical assets for the five GDS Platform Core
domains reviewed by GDS-ROADMAP-001.

## Repository State

- Working Repository: Ghost-Development-System-Docs
- Branch: `main`
- Initial dirty state: clean
- GameGhost / GrayGhostArchive: not edited

## Domain Inventory

### Startup Enforcement

| Asset | Role | Status |
| --- | --- | --- |
| `docs/architecture/intent_aware_startup_enforcement.md` | Conceptual architecture boundary for pre-generation gate. | Draft architecture foundation |
| `docs/workflow/artifact_creation_startup_enforcement_workflow.md` | Human-readable workflow for artifact generation gate. | Draft workflow |
| `docs/rules/artifact_creation_startup_enforcement_rules.md` | Rule layer for mandatory pre-generation checks. | Canonical rule |
| `templates/Q_TEMPLATE.md` | Evidence fields for Q artifact generation. | Integrated by GDS-STARTUP-003 |
| `templates/completion_report_template.md` | Completion Report evidence fields. | Integrated by GDS-STARTUP-003 |
| `docs/architecture/runtime_startup_enforcement.md` | Runtime architecture contract for executing the gate. | Draft architecture |
| `docs/workflow/runtime_startup_enforcement_workflow.md` | Runtime execution workflow. | Draft workflow |

### Intent Engine / Intent-Driven Workflow

| Asset | Role | Status |
| --- | --- | --- |
| `docs/architecture/intent_driven_workflow.md` | Natural language intent interpretation boundary. | Draft architecture foundation |
| `docs/architecture/intent_registry_and_pending_action_contract.md` | Intent registry and Pending Action contract. | Initial contract |
| `docs/workflow/intent_driven_workflow.md` | Operational workflow for routing user intent. | Draft workflow |

### Command Center

| Asset | Role | Status |
| --- | --- | --- |
| `docs/architecture/command_center_architecture.md` | Repository Orchestrator architecture. | Draft architecture specification |
| `templates/information_package_template.md` | Project / repository state package for future Command Center use. | Template |
| `docs/architecture/repository_intelligence_dashboard_foundation.md` | Read-only visibility layer foundation. | Draft architecture |

### Knowledge Promotion

| Asset | Role | Status |
| --- | --- | --- |
| `docs/architecture/knowledge_promotion_engine.md` | Governed knowledge promotion loop. | Draft architecture foundation |
| `docs/architecture/knowledge_candidate_classification_contract.md` | Candidate type and evidence contract. | Draft contract |
| `docs/workflow/knowledge_preservation_gate.md` | Gate for preserving important reasoning / decisions. | Workflow |
| `docs/workflow/knowledge_carry_forward_workflow.md` | Low-friction carry-forward workflow. | Workflow |

### Repository Quality

| Asset | Role | Status |
| --- | --- | --- |
| `docs/workflow/repository_quality_audit_workflow.md` | Repository-wide quality audit workflow. | Workflow |
| `docs/rules/quality_rules.md` | General quality rules and review standards. | Rule |
| `scripts/repository_quality_audit.py` | Audit script. | Script |
| `reports/repository_quality_report.md` | Latest quality report. | Generated report |
| `docs/workflow/documentation_synchronization_workflow.md` | Keeps README / index / reports synchronized. | Workflow |

## Inventory Conclusion

The five domains already have canonical architecture or workflow assets. The
gap is not missing domain documentation. The gap is a shared execution evidence
contract that can be consumed by Startup Enforcement, Intent Engine, Command
Center, Repository Quality, and Knowledge Promotion without duplicating schema
ownership.
