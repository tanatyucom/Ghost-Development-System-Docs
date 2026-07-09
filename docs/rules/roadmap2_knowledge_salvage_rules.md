# Roadmap2 Knowledge Salvage Rules

## Purpose

Roadmap2 Knowledge Salvage is the rule set for moving all reusable Roadmap2 knowledge into the official GDS Knowledge Base.

This rule does not approve new runtime features. It prevents reusable knowledge from remaining only in Roadmap2 review notes, chat, or temporary Qs.

## Core Rule

Roadmap2 is history after salvage. GDS Knowledge Base is the active source.

Until Roadmap2 review produces no missing knowledge, repeat the salvage loop.

## Standard Loop

```text
Roadmap2 Review Request
  -> Review Result
  -> Missing Knowledge Extraction
  -> Q Artifact
  -> Codex Documentation Update
  -> GitHub Push / Review
  -> Roadmap2 Re-review
  -> Repeat Until No Missing Knowledge
```

## Required Review Categories

Every Roadmap2 salvage review checks:

- CASE
- Best Practice
- Evolution
- Investigation
- Rule Story
- PIP Principle
- GDS reflection gap
- Concept
- Rule update
- Workflow update
- Glossary update
- Architecture boundary
- History entry

## Classification Rule

Each finding must be classified as one of:

- already migrated;
- missing knowledge;
- duplicate;
- future candidate;
- not reusable;
- needs human approval;
- needs source evidence.

## Destination Rule

Use the smallest durable destination that fits:

- CASE: `pip/cases/`
- Best Practice: `pip/best_practices/`
- Evolution: `pip/evolutions/`
- Investigation: `pip/investigations/`
- Rule Story: `pip/rule_stories/`
- Concept: `pip/concepts/`
- PIP principle: `pip/MASTER_DOCUMENT_JP.md`
- Index: `pip/case_index.md`
- Official rule: `docs/rules/`
- Workflow: `docs/workflow/`
- Glossary: `docs/glossary/`
- History: `docs/history/knowledge_base_history.md`

## Do Not

- Do not treat Roadmap2 review notes as the active source after migration.
- Do not leave reusable knowledge only in chat.
- Do not create runtime scope from salvage review.
- Do not edit GameGhost, Steam OCR logic, DB, import / apply, or production logic.
- Do not promote future candidates as approved rules without human review.
- Do not finish the loop while any reusable Roadmap2-only knowledge remains.

## Completion Rule

The salvage loop is complete only when review can say:

```text
Knowledge migration complete.
No remaining Roadmap2-only knowledge.
Roadmap2 can be treated as history.
GDS Knowledge Base is the active source.
```

## Decision Background

Roadmap2 produced PIP, Master Document, Master Title List, CASE candidates, Best Practice candidates, Evolution candidates, Investigation candidates, Rule Story candidates, and reusable debugging methodology.

Those outputs are valuable only if they become findable, reviewed, Git-managed knowledge. This rule makes the final migration loop explicit.
