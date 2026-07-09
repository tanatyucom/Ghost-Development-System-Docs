# Roadmap2 Knowledge Salvage Loop Workflow

## Purpose

Roadmap2 Knowledge Salvage Loop は、Roadmap2 で蓄積された設計思想、調査知識、Best Practice、CASE 候補、Evolution、Investigation、Rule Story、Concept を GDS Knowledge Base へ漏れなく移植するための最終レビュー workflow です。

この workflow は新機能追加ではありません。Roadmap2 由来の知識が GDS に完全移植されたと判断できるまで、レビュー、抽出、Q 作成、実装、再レビューを繰り返します。

## Core Loop

```text
Roadmap2 Review Request
  -> Review Result
  -> Missing Knowledge Extraction
  -> Q Artifact
  -> Codex Documentation Update
  -> GitHub Push / Review
  -> Roadmap2 Re-review
  -> Repeat Until No Missing Knowledge
  -> Roadmap2 Becomes History
  -> GDS Becomes Single Knowledge Base
```

## Review Targets

Each Roadmap2 salvage review checks for missing:

- CASE candidates
- Best Practice candidates
- Evolution candidates
- Investigation candidates
- Rule Story candidates
- Concept candidates
- PIP principles
- GDS reflection gaps
- Workflow gaps
- Rule gaps
- Template gaps
- Glossary terms
- Architecture boundaries
- History entries

## Step 1: Roadmap2 Review Request

Start from a focused review request.

The request should state:

- reviewed Roadmap2 source or evidence;
- intended salvage target;
- current GDS destination;
- known missing categories;
- whether this is final-pass review or targeted follow-up.

## Step 2: Review Result

The review result classifies findings as:

- already migrated;
- missing knowledge;
- duplicate;
- future candidate;
- not reusable;
- needs human approval;
- needs source evidence.

Do not create new implementation scope from the review result. Create a Q artifact when a change is needed.

## Step 3: Missing Knowledge Extraction

Extract missing knowledge into the smallest durable unit:

- CASE
- Best Practice
- Evolution
- Investigation
- Rule Story
- Concept
- Rule update
- Workflow update
- Glossary update
- PIP update

Each extracted item should name its source and intended destination.

## Step 4: Q Artifact

Create a Q artifact for the salvage update.

The Q should include:

- source Roadmap2 review result;
- target GDS documents;
- categories to add or update;
- scope guard;
- completion criteria;
- verification method.

## Step 5: Codex Documentation Update

Codex updates only documentation and knowledge artifacts.

Do not edit:

- GameGhost runtime code;
- Steam OCR logic;
- database files;
- import / apply logic;
- production logic.

## Step 6: GitHub Push / Review

After review and commit by a human, the knowledge becomes available for the next Roadmap2 re-review.

Commit is not part of this workflow unless explicitly approved by a human.

## Step 7: Roadmap2 Re-review

Re-review Roadmap2 after each salvage pass.

Ask:

- Are there missing CASE entries?
- Are there missing Best Practices?
- Are there missing Evolutions?
- Are there missing Investigations?
- Are there missing Rule Stories?
- Are there missing Concepts?
- Are PIP principles complete?
- Are rules and workflows complete?
- Can Roadmap2 be treated as history?

## Completion Condition

The loop ends only when the review result says:

```text
Knowledge migration complete.
No remaining Roadmap2-only knowledge.
Roadmap2 can be treated as history.
GDS Knowledge Base is the active source.
```

## Relationship To PIP

PIP is the main salvage destination for reusable Roadmap2 methodology.

Use:

- `pip/MASTER_DOCUMENT_JP.md`
- `pip/MASTER_TITLE_LIST_JP.md`
- `pip/case_index.md`
- `pip/cases/`
- `pip/best_practices/`
- `pip/evolutions/`
- `pip/investigations/`
- `pip/rule_stories/`
- `pip/concepts/`

## Completion Report Requirements

When this workflow is used, the completion report should include:

- source Roadmap2 review request;
- extracted missing knowledge;
- created or updated CASE entries;
- created or updated Best Practices;
- created or updated Evolutions;
- created or updated Investigations;
- created or updated Rule Stories;
- created or updated Concepts;
- updated rules or workflows;
- remaining Roadmap2-only knowledge;
- next re-review target;
- whether Roadmap2 can be treated as history.
