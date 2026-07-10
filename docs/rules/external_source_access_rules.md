# External Source Access Rules

## Purpose

This rule defines how ChatGPT, Codex, and other AI systems should use the
public Ghost Development System Docs repository as an external Knowledge
Source.

The goal is to make repository knowledge stable, fetchable, and reviewable by
using Raw URLs instead of depending only on normal GitHub page URLs or chat
memory.

## Core Rule

When an AI needs to read the public GDS Docs repository from outside the local
workspace, it should start from:

```text
docs/ai_repository_index.md
```

Public Raw URL:

```text
https://raw.githubusercontent.com/tanatyucom/Ghost-Development-System-Docs/main/docs/ai_repository_index.md
```

The AI should then follow the Raw URL for the needed README, roadmap,
architecture, rules, workflow, template, example, glossary, history, PIP, CASE,
Concept, or methodology file.

## Required Behavior

AI should:

- read the AI Repository Knowledge Access Index first when using public GDS
  repository knowledge;
- prefer Raw URLs for file retrieval;
- report honestly when a file cannot be fetched or read;
- avoid claiming repository-wide knowledge from a partial fetch;
- use related files only when needed for the task;
- cite or name the files used when reporting results.

AI should not:

- rely on chat memory when the current repository file can be read;
- treat a normal GitHub HTML page as equivalent to a Raw URL file fetch;
- silently continue when a required source file could not be accessed;
- use stale copied text when the Raw URL Index indicates a newer source.

## Index Generation Rule

`docs/ai_repository_index.md` is a generated artifact.

Generate or refresh it with:

```bash
python scripts/generate_ai_repository_index.py --write
```

Validate the Markdown inventory and Raw URL structure with:

```bash
python scripts/generate_ai_repository_index.py --validate
```

Regenerate `docs/ai_repository_index.md` when:

- a new important Markdown knowledge file is added;
- an important file is moved or renamed;
- README, roadmap, rules, workflow, templates, examples, glossary, history,
  PIP, CASE, Concept, or methodology entry points change;
- a new rule or workflow expects AI to read a public repository source;
- Completion Checklist identifies that the index is missing an important
  access path.

## Validation Rule

Validation should confirm:

- Local Path entries exist;
- Raw URLs match the repository Raw URL pattern;
- duplicate Local Path entries do not exist;
- Markdown inventory coverage is complete;
- newly added Markdown files are registered.

Network access is not required for validation. The validator checks local
inventory and URL format.

## Completion Checklist Integration

At task completion, check whether the change affected public AI access.

If yes, regenerate `docs/ai_repository_index.md`, run validation, and record
the result in the completion report.

If no, record that no AI Repository Index update was required.

## Knowledge Poka-Yoke Relationship

This rule is a Knowledge Poka-Yoke control.

It prevents:

- AI reading the wrong source;
- humans pasting incomplete repository text into chat;
- stale GitHub page links becoming the only access path;
- important new public knowledge being invisible to AI reviewers;
- completion reports forgetting to update AI-access entry points.

## Decision Background

GDS Docs is not only documentation for humans. It is also a public Knowledge
Source for AI review and future AI-assisted development.

Raw URLs are easier for AI tools to fetch reliably than normal GitHub page
URLs. A maintained Raw URL Index gives AI a stable first file to read and helps
future tasks reach the correct source without copy-paste loss.
