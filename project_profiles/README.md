# Project Profiles

## Purpose

Project Profiles define project-specific operating context for AI and human
work.

GDS rules, workflows, methodologies, and templates are shared. Project Profiles
record the repository, scope, project-specific rules, AI context, and
completion policy for each child project such as GameGhost, AnimeGhost, and
ComicGhost.

## AI Reading Order

When AI works on an individual project, read sources in this order:

```text
AI Repository Knowledge Access Index
  -> Information Package, when provided
  -> Current Q File
  -> Repository Root Validation
  -> GDS Core Rules / Templates / Methodology
  -> Target Project Profile
  -> Startup Checklist
  -> Research Task Detection
  -> Normal Implementation / Review, when not research
  -> Research Mission, when research
```

This order is formalized by:

- `docs/rules/ai_startup_procedure_rules.md`
- `docs/workflow/ai_startup_procedure.md`

The Project Profile does not replace the Q file. It provides stable project
context so the Q file can focus on the current task.

When the Current Q or Information Package indicates investigation, root cause
research, hypothesis validation, evidence collection, or knowledge gap
classification, AI should branch from Startup Checklist into Research Mission
instead of normal implementation.

Research Mission entry points:

- `templates/research_mission_template.md`
- `docs/workflow/research_mission_workflow.md`
- `docs/rules/research_mission_rules.md`

## Standard Profile Shape

```text
project_profiles/<project>/
  README.md
  repository.md
  rules.md
  workflow.md
  ai_context.md
  completion_policy.md
```

Use lowercase ASCII folder names.

## Current Profiles

- `project_profiles/gameghost/`: GameGhost profile.
- `project_profiles/animeghost/`: future placeholder.
- `project_profiles/comicghost/`: future placeholder.

## Responsibility

GDS owns the Project Profile structure and shared profile rules.

Each project owns its runtime behavior, schema, data, release decisions, and
project-specific implementation. A Project Profile may summarize that context,
but it does not transfer runtime ownership to GDS.

## Update Policy

Update a Project Profile when:

- production repository location changes;
- backup / reference-only policy changes;
- project-specific Q expectations change;
- completion report expectations change;
- commit, tag, release, or review policy changes;
- AI context needed for safe work changes.

When a Project Profile changes, regenerate and validate:

```bash
python scripts/generate_ai_repository_index.py --write
python scripts/generate_ai_repository_index.py --validate
```
