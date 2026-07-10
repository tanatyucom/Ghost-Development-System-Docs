# AI Repository Knowledge Access Index

## Purpose

This index is the stable entry point for ChatGPT, Codex, and other AI systems
that need to read the public Ghost Development System Docs repository as a
Knowledge Source.

AI should read this file first, then follow the Raw URL entries for the
required topic. This avoids depending on normal GitHub page URLs that may be
hard for AI tools to fetch reliably.

## Repository

- Repository name: Ghost-Development-System-Docs
- Repository purpose: Public Knowledge Base for Ghost Development System rules,
  workflow, architecture, roadmap, templates, examples, glossary, history, PIP,
  CASE, Concept, and methodology.
- GitHub repository URL:
  `https://github.com/tanatyucom/Ghost-Development-System-Docs`
- Raw base URL:
  `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/`
- Default branch: `main`
- Last reviewed: 2026-07-10

## AI Usage Rule

When using the public repository as a knowledge source:

1. Read this index first.
2. Choose the Raw URL for the required topic.
3. Read the target file.
4. Follow related files only when needed.
5. If a Raw URL cannot be fetched, report that honestly and propose another
   access path such as repository checkout, attached file, or local workspace
   path.

Do not treat a partial fetch, missing file, or unreadable GitHub page as full
knowledge of the repository.

## Update Rule

Update this index when:

- a new important Markdown knowledge file is added;
- an important file is moved or renamed;
- README, roadmap, rules, workflow, templates, PIP, CASE, Concept, or
  methodology entry points change;
- a completion checklist finds that AI access would be safer with a new Raw URL
  entry.

Completion reports should mention whether this index needed an update when the
task changes public knowledge entry points.

## Entry Format

Each entry should include:

- Title
- Purpose
- Local Path
- GitHub URL
- Raw URL
- Category
- Priority
- Last Reviewed / Updated, when available

## Core Entry Points

| Title | Purpose | Local Path | GitHub URL | Raw URL | Category | Priority | Last Reviewed / Updated |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Root README | Repository overview and human / AI starting point. | `README.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/README.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/README.md` | README | High | 2026-07-10 |
| Knowledge Base Index | Main public docs index and AI entry point. | `docs/README.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/docs/README.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/docs/README.md` | README | Critical | 2026-07-10 |
| AI Repository Knowledge Access Index | Raw URL index for AI repository access. | `docs/ai_repository_index.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/docs/ai_repository_index.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/docs/ai_repository_index.md` | Index | Critical | 2026-07-10 |

## Roadmap

| Title | Purpose | Local Path | GitHub URL | Raw URL | Category | Priority | Last Reviewed / Updated |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Roadmap README | Roadmap folder guide. | `roadmap/README.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/roadmap/README.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/roadmap/README.md` | Roadmap | High | 2026-07-10 |
| Ghost Development System Roadmap | Main GDS roadmap direction. | `roadmap/ghost_development_system_roadmap.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/roadmap/ghost_development_system_roadmap.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/roadmap/ghost_development_system_roadmap.md` | Roadmap | High | 2026-07-10 |
| Roadmap | General roadmap archive. | `roadmap/roadmap.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/roadmap/roadmap.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/roadmap/roadmap.md` | Roadmap | Medium | 2026-07-10 |

## Architecture

| Title | Purpose | Local Path | GitHub URL | Raw URL | Category | Priority | Last Reviewed / Updated |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Architecture README | Architecture folder guide. | `docs/architecture/README.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/docs/architecture/README.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/docs/architecture/README.md` | Architecture | High | 2026-07-10 |
| Responsibility Boundary | Ownership boundaries for GDS architecture. | `docs/architecture/responsibility_boundary.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/docs/architecture/responsibility_boundary.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/docs/architecture/responsibility_boundary.md` | Architecture | High | 2026-07-10 |
| Design Philosophy | Accepted design principles and philosophy. | `docs/architecture/design_philosophy.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/docs/architecture/design_philosophy.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/docs/architecture/design_philosophy.md` | Architecture | High | 2026-07-10 |

## Rules

| Title | Purpose | Local Path | GitHub URL | Raw URL | Category | Priority | Last Reviewed / Updated |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Rules README | Rules folder guide. | `docs/rules/README.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/docs/rules/README.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/docs/rules/README.md` | Rules | High | 2026-07-10 |
| Rules Index | Official rule priority and rule entry point. | `docs/rules/rules.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/docs/rules/rules.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/docs/rules/rules.md` | Rules | Critical | 2026-07-10 |
| Core Principles | Core GDS principles. | `docs/rules/core_principles.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/docs/rules/core_principles.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/docs/rules/core_principles.md` | Rules | Critical | 2026-07-10 |
| External Source Access Rules | Rules for using public repository Raw URLs as AI knowledge sources. | `docs/rules/external_source_access_rules.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/docs/rules/external_source_access_rules.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/docs/rules/external_source_access_rules.md` | Rules | Critical | 2026-07-10 |
| Documentation Rules | Documentation structure, update timing, and review rules. | `docs/rules/documentation_rules.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/docs/rules/documentation_rules.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/docs/rules/documentation_rules.md` | Rules | High | 2026-07-10 |
| Startup Checklist Rules | Start-of-work confirmation rule. | `docs/rules/startup_checklist_rules.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/docs/rules/startup_checklist_rules.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/docs/rules/startup_checklist_rules.md` | Rules | High | 2026-07-10 |
| Repository Root Validation Rules | Git root validation rule. | `docs/rules/repository_root_validation_rules.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/docs/rules/repository_root_validation_rules.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/docs/rules/repository_root_validation_rules.md` | Rules | High | 2026-07-10 |
| Completion Checklist Rules | End-of-work confirmation rule. | `docs/rules/completion_checklist_rules.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/docs/rules/completion_checklist_rules.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/docs/rules/completion_checklist_rules.md` | Rules | High | 2026-07-10 |
| Artifact First Rules | File artifact generation rule. | `docs/rules/artifact_first_rules.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/docs/rules/artifact_first_rules.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/docs/rules/artifact_first_rules.md` | Rules | High | 2026-07-10 |

## Workflow

| Title | Purpose | Local Path | GitHub URL | Raw URL | Category | Priority | Last Reviewed / Updated |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Workflow README | Workflow folder guide and standard development flow. | `docs/workflow/README.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/docs/workflow/README.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/docs/workflow/README.md` | Workflow | Critical | 2026-07-10 |
| Startup Checklist Workflow | Start-of-work workflow. | `docs/workflow/startup_checklist_workflow.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/docs/workflow/startup_checklist_workflow.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/docs/workflow/startup_checklist_workflow.md` | Workflow | High | 2026-07-10 |
| Completion Checklist Workflow | End-of-work workflow. | `docs/workflow/completion_checklist_workflow.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/docs/workflow/completion_checklist_workflow.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/docs/workflow/completion_checklist_workflow.md` | Workflow | High | 2026-07-10 |
| Output Policy | Chat versus artifact decision policy. | `docs/workflow/output_policy.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/docs/workflow/output_policy.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/docs/workflow/output_policy.md` | Workflow | High | 2026-07-10 |
| Template Lifecycle | Knowledge promotion to templates, rules, and KB. | `docs/workflow/template_lifecycle.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/docs/workflow/template_lifecycle.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/docs/workflow/template_lifecycle.md` | Workflow | Medium | 2026-07-10 |

## Templates

| Title | Purpose | Local Path | GitHub URL | Raw URL | Category | Priority | Last Reviewed / Updated |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Templates README | Template folder guide. | `templates/README.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/templates/README.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/templates/README.md` | Templates | High | 2026-07-10 |
| Q File Template | Standard Q file template. | `templates/q_file_template.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/templates/q_file_template.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/templates/q_file_template.md` | Templates | Critical | 2026-07-10 |
| Completion Report Template | Standard completion report template. | `templates/completion_report_template.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/templates/completion_report_template.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/templates/completion_report_template.md` | Templates | High | 2026-07-10 |
| Completion Checklist Template | Standard completion checklist template. | `templates/completion_checklist_template.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/templates/completion_checklist_template.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/templates/completion_checklist_template.md` | Templates | High | 2026-07-10 |
| Review Checklist | Standard review checklist. | `templates/review_checklist.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/templates/review_checklist.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/templates/review_checklist.md` | Templates | Medium | 2026-07-10 |

## Examples

| Title | Purpose | Local Path | GitHub URL | Raw URL | Category | Priority | Last Reviewed / Updated |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Examples README | Examples folder guide. | `examples/README.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/examples/README.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/examples/README.md` | Examples | Medium | 2026-07-10 |
| Artifact First Examples | Examples for file artifact operation. | `examples/artifact_first_examples.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/examples/artifact_first_examples.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/examples/artifact_first_examples.md` | Examples | Medium | 2026-07-10 |
| Completion Checklist Examples | Examples for completion checks. | `examples/completion_checklist_examples.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/examples/completion_checklist_examples.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/examples/completion_checklist_examples.md` | Examples | Medium | 2026-07-10 |

## Glossary

| Title | Purpose | Local Path | GitHub URL | Raw URL | Category | Priority | Last Reviewed / Updated |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Public Glossary | Shared public terms for humans and AI. | `docs/glossary/README.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/docs/glossary/README.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/docs/glossary/README.md` | Glossary | High | 2026-07-10 |

## History

| Title | Purpose | Local Path | GitHub URL | Raw URL | Category | Priority | Last Reviewed / Updated |
| --- | --- | --- | --- | --- | --- | --- | --- |
| History README | History folder guide. | `docs/history/README.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/docs/history/README.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/docs/history/README.md` | History | Medium | 2026-07-10 |
| Knowledge Base History | Version history for GDS Knowledge Base. | `docs/history/knowledge_base_history.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/docs/history/knowledge_base_history.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/docs/history/knowledge_base_history.md` | History | High | 2026-07-10 |

## PIP

| Title | Purpose | Local Path | GitHub URL | Raw URL | Category | Priority | Last Reviewed / Updated |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PIP README | PIP folder guide. | `pip/README.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/pip/README.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/pip/README.md` | PIP | High | 2026-07-10 |
| PIP v1.1 README | Stable PIP v1.1 briefing standard. | `pip/PIP_README_v1.1.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/pip/PIP_README_v1.1.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/pip/PIP_README_v1.1.md` | PIP | High | 2026-07-10 |
| PIP Master Document JP | Japanese master document for Roadmap2-derived methodology. | `pip/MASTER_DOCUMENT_JP.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/pip/MASTER_DOCUMENT_JP.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/pip/MASTER_DOCUMENT_JP.md` | PIP | High | 2026-07-10 |
| PIP Master Title List JP | Japanese title list for PIP knowledge classification. | `pip/MASTER_TITLE_LIST_JP.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/pip/MASTER_TITLE_LIST_JP.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/pip/MASTER_TITLE_LIST_JP.md` | PIP | High | 2026-07-10 |

## CASE

| Title | Purpose | Local Path | GitHub URL | Raw URL | Category | Priority | Last Reviewed / Updated |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Case Index | Searchable PIP case index. | `pip/case_index.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/pip/case_index.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/pip/case_index.md` | CASE | High | 2026-07-10 |
| CASE Template | Standard PIP case template. | `pip/templates/case_template.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/pip/templates/case_template.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/pip/templates/case_template.md` | CASE | Medium | 2026-07-10 |
| CASE-0008 Steam OCR Root Cause Investigation | Root cause investigation case example. | `pip/cases/CASE-0008_steam_ocr_root_cause_investigation.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/pip/cases/CASE-0008_steam_ocr_root_cause_investigation.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/pip/cases/CASE-0008_steam_ocr_root_cause_investigation.md` | CASE | Medium | 2026-07-10 |

## Concept

| Title | Purpose | Local Path | GitHub URL | Raw URL | Category | Priority | Last Reviewed / Updated |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Concepts README | Concept folder guide. | `pip/concepts/README.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/pip/concepts/README.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/pip/concepts/README.md` | Concept | High | 2026-07-10 |
| Concept Index | Tracked Concept IDs and statuses. | `pip/concepts/concept_index.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/pip/concepts/concept_index.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/pip/concepts/concept_index.md` | Concept | High | 2026-07-10 |
| Concept Template | Standard individual Concept template. | `pip/templates/concept_template.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/pip/templates/concept_template.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/pip/templates/concept_template.md` | Concept | Medium | 2026-07-10 |

## Methodology

| Title | Purpose | Local Path | GitHub URL | Raw URL | Category | Priority | Last Reviewed / Updated |
| --- | --- | --- | --- | --- | --- | --- | --- |
| First Broken Step Methodology | Debugging method for finding the first broken stage. | `docs/workflow/first_broken_step_methodology.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/docs/workflow/first_broken_step_methodology.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/docs/workflow/first_broken_step_methodology.md` | Methodology | High | 2026-07-10 |
| Debug Escalation Ladder | Standard escalation order before algorithm change. | `docs/workflow/debug_escalation_ladder.md` | `https://github.com/tanatyucom/Ghost-Development-System-Docs/blob/main/docs/workflow/debug_escalation_ladder.md` | `https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/docs/workflow/debug_escalation_ladder.md` | Methodology | High | 2026-07-10 |
