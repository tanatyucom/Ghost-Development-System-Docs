# AI Bootstrap Source Card

## Purpose

This card is the minimum first-read source for a new AI chat or a returning AI
session that needs to work with Ghost Development System Docs.

It does not replace Startup, AI Repository Index, rules, workflows, templates,
or Q files. It only tells the AI where to begin.

## Core Rule

```text
Memory is helpful but not authoritative.
Repository is the Single Source of Truth.
Startup synchronizes AI with repository truth before repository-governed work.
```

## Step 1: Memory Check

Before planning, creating, reviewing, recommending, or executing repository
work, check whether memory / persistent context is available.

Record:

- Memory available: Yes / No / Unknown
- Memory used as authoritative source: No
- Repository source required: Yes

If memory is unavailable, stale, or uncertain, continue from repository sources.
Do not treat chat memory, model memory, or old attachments as the official
GDS state.

## Step 2: Single Source Of Truth

Canonical source:

```text
Ghost-Development-System-Docs repository
```

Primary local entry points:

- `README.md`
- `docs/README.md`
- `docs/ai_repository_index.md`

Public Raw entry point:

```text
https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/docs/ai_repository_index.md
```

## Step 3: First Read Order

```text
README.md
  -> docs/README.md
  -> docs/ai_repository_index.md
  -> docs/workflow/ai_startup_procedure.md
  -> docs/rules/ai_startup_procedure_rules.md
  -> docs/workflow/startup_completion_evidence.md
  -> docs/workflow/startup_completion_gate.md
```

## Step 4: Task Routing

Use the task type to choose the next canonical sources.

| Task type | Required next sources |
| --- | --- |
| Q creation / revision | `templates/Q_TEMPLATE.md`, `docs/workflow/artifact_creation_startup_enforcement_workflow.md`, related rules / workflows |
| Documentation update | related README / rules / workflow / template / examples, `templates/completion_report_template.md` |
| Completion review | `templates/completion_report_template.md`, `templates/repository_recommendation_template.md`, `templates/workflow_recommendation_template.md`, `templates/approval_request_block_template.md` |
| Commit / Push / Tag recommendation | `docs/workflow/pre_response_verification_gate.md`, `docs/registries/execution_authority_registry.yaml`, `docs/registries/capability_authority_bindings.yaml` |
| Final response | `docs/workflow/pre_response_verification_gate.md`, `templates/ai_response_checklist_v2.md` |

## Step 5: Repository Context Evidence

For repository-governed work, do not only say that Startup was done.

Record the minimum evidence:

- repository name;
- working directory or repository root;
- branch or revision when available;
- AI Repository Index path and freshness / validation;
- Current Q / Mission / Information Package path;
- canonical template path when applicable;
- related rules, workflows, ADRs, architecture, standards, or registries read;
- unresolved assets;
- conflict status;
- freshness / invalidation status.

## Step 6: SCW Conditions

Apply SCW or report a visible limitation when:

- the canonical repository cannot be accessed;
- AI Repository Index cannot be read;
- Current Q or required template cannot be found;
- uploaded / copied sources conflict with repository sources;
- repository state, task type, workflow state, or approval state changed after
  Startup and context was not refreshed;
- the AI would need to rely on memory alone for a repository-governed decision.

## Boundary

This card does not approve:

- implementation;
- repository mutation;
- commit;
- push;
- tag;
- release;
- canonical promotion;
- automatic Q generation.

Human Approval and the relevant workflow remain required.

## Minimal Startup Evidence Block

```text
AI Bootstrap:
- Memory available:
- Repository source required:
- First-read sources:
- AI Repository Index:
- Current Q / Mission:
- Required canonical assets:
- Unresolved assets:
- Startup / refresh result:
- Limitation / SCW:
```

## Related Documents

- `README.md`
- `docs/README.md`
- `docs/ai_repository_index.md`
- `docs/workflow/ai_startup_procedure.md`
- `docs/rules/ai_startup_procedure_rules.md`
- `docs/workflow/startup_completion_evidence.md`
- `docs/workflow/startup_completion_gate.md`
- `docs/workflow/pre_response_verification_gate.md`
- `templates/ai_response_checklist_v2.md`
