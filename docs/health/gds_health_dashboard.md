# GDS Health Dashboard

## Purpose

GDS Health Dashboard makes the operating state of Ghost Development System Docs
visible.

The goal is not to add a new feature or score people. The goal is to help
humans and AI continuously understand whether Knowledge, Workflow, Templates,
Examples, Automation, CI, and Project Profiles are organized enough to support
safe daily operation.

## Status Meaning

- Green: usable and current enough for normal operation.
- Yellow: usable, but improvement or follow-up is recommended.
- Red: blocked, missing, stale, or unsafe enough that work should stop or be
  reviewed before relying on it.

## Health Summary

| Area | Status | Current State | Target State | Notes |
| --- | --- | --- | --- | --- |
| Repository Health | Green | Repository root validation, dirty workspace review, and commit safety rules exist. | Repository state can be checked before and after every task. | Keep using startup and completion checks. |
| Knowledge Health | Green | Knowledge Base has rules, workflow, architecture, history, PIP, concepts, cases, and generated AI index. | Reusable knowledge is promoted out of chat and Q files into durable documents. | Continue Improvement Review and Knowledge Promotion. |
| Rule Coverage | Green | Core rules include Project First, Artifact First, Startup, Completion, Migration First, Debug, Audit, and AI collaboration rules. | Major repeated work patterns have explicit rule or workflow entry points. | Add rules only when practice proves the need. |
| Workflow Coverage | Green | AI Startup Procedure, AI Daily Operation Cycle, Startup Checklist, Completion Checklist, and supporting workflows exist. | Daily work can move from startup to next Q without hidden steps. | Daily checklist now supports repeatable use. |
| Template Coverage | Green | Q, completion report, startup, completion, review, repository root, collaborative decision, and daily operation templates exist. | Repeated artifacts can be generated without rebuilding structure from memory. | Add examples for daily operation next. |
| Example Coverage | Yellow | Examples exist for many rules, but Daily Operation Checklist examples are not yet added. | Major workflows have good and bad examples. | Candidate next Q: Daily Operation Checklist Examples. |
| Automation Coverage | Yellow | AI Repository Index generation and validation exist. CI validation is documented. | Health checks and index freshness can be validated automatically. | Future candidate: GDS Health validation script. |
| CI Status | Yellow | AI Repository Index CI workflow is documented in the Knowledge Base. | CI status is visible in health review and completion reports. | Confirm actual CI result during repository operations. |
| Project Profile Coverage | Yellow | GameGhost profile exists. AnimeGhost and ComicGhost placeholders exist. | Active projects have complete profiles with repository, rules, workflow, AI context, and completion policy. | Expand project profiles when those projects become active. |

## Health Review Checklist

- AI Repository Index is generated and validation passes.
- README and docs index point to current major entry points.
- Rules index includes current official rules and references.
- Workflow index includes current operating flows.
- Templates index includes current reusable templates.
- Completion report template includes current completion evidence fields.
- Project Profiles exist for active projects.
- Examples exist for major workflows or are tracked as Future Candidates.
- CI / automation status is known or explicitly marked as unknown.
- Recommended Next Q is recorded when health is Yellow or Red.

## Future Extension

- Command Center.
- Repository Health Score.
- Automation Dashboard.
- Daily Health Report.
- Release Readiness.
- GDS Health validation script.

These are future candidates. This dashboard does not approve implementation by
itself.

## Related Documents

- `docs/ai_repository_index.md`
- `docs/workflow/ai_daily_operation_cycle.md`
- `templates/daily_operation_checklist_template.md`
- `docs/workflow/ai_startup_procedure.md`
- `docs/workflow/completion_checklist_workflow.md`
- `docs/rules/core_principles.md`
- `docs/rules/workflow_rules.md`
- `project_profiles/README.md`
- `docs/history/knowledge_base_history.md`
