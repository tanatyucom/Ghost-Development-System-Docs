# Ghost Research Knowledge Asset

**Status:** Draft Architecture Standard

**Last Updated:** 2026-07-18

## Purpose

Ghost Research is the canonical GDS Knowledge Asset for governed intake of
external engineering knowledge.

It captures what was learned from OSS, frameworks, architectures, and
engineering practices, then evaluates which design ideas may become Future
Candidates, GG validation proposals, Platform Candidates, or GDS Standards.

Ghost Research standardizes learning. It does not authorize implementation,
dependency adoption, source-code copying, promotion, commit, push, tag, or
repository mutation.

## Core Principle

```text
External Knowledge
  -> Ghost Research
  -> Future Candidate
  -> GG Validation
  -> Evidence
  -> Platform Candidate
  -> GDS Standard
```

No external design idea becomes a GDS Standard solely because it is popular,
mature, widely adopted, or technically attractive.

## Knowledge Asset Definition

Ghost Research preserves:

- what was researched;
- which projects, frameworks, documents, or architectures were reviewed;
- which design ideas were identified;
- strengths, weaknesses, risks, and tradeoffs;
- GDS overlap;
- Ghost-native interpretation;
- possible GG validation path;
- Adoption Decisions at idea level;
- related Future Candidates, Platform Candidates, ADRs, Qs, and Evidence;
- source traceability and attribution boundaries.

## Knowledge Asset Boundary

| Asset | Responsibility |
| --- | --- |
| Ghost Research | What was learned and evaluated from external knowledge. |
| Q | What scoped work, review, or documentation update should happen now. |
| Research Mission | How an investigation task is scoped and validated. |
| Future Candidate | Ghost-native idea that may be validated later. |
| GG Validation | Safe field experiment in GameGhost or another Ghost repository. |
| Evidence | Results, failures, comparisons, and review material. |
| Platform Candidate | Validated reusable platform component or standard candidate. |
| ADR | Durable architecture decision made after review. |
| Improvement Record | Operational improvement lifecycle and reusable learning. |
| Case | Observation or evidence of a concrete situation. |
| GDS Standard | Approved canonical rule, workflow, template, schema, registry, or architecture standard. |

Ghost Research is not an external source copy, vendor documentation mirror,
implementation specification, or automatic adoption record.

## Canonical Naming And Identity

Research IDs use a stable sequence:

```text
GR-001
GR-002
GR-003
```

Canonical title format:

```text
Ghost Research GR-001 - Workflow Engines
```

Do not renumber published Research IDs. If a Research asset is replaced, mark
the older asset as `Superseded` and link both directions.

Minimum identity fields:

- Research ID.
- Title.
- Category.
- Version.
- Status.
- Created.
- Updated.
- Owner or responsible role.
- Related repository.
- Related Q.
- Related Future Candidate.
- Related Platform Candidate.
- Related Evidence.
- Supersedes.
- Superseded By.
- Source references.

## Initial Research Categories

| Research ID | Category | Initial Priority | Initial Status |
| --- | --- | --- | --- |
| GR-001 | Workflow Engines | Critical | Planned / Example |
| GR-002 | Repository Intelligence | Critical | Planned |
| GR-003 | Knowledge Graph | Critical | Planned |
| GR-004 | Rule Engines | High | Planned |
| GR-005 | Agent Memory | High | Planned |
| GR-006 | Execution Frameworks | High | Planned |
| GR-007 | Metadata / Entity Resolution | High | Planned |
| GR-008 | OCR / Vision | High | Planned |
| GR-009 | AI Governance | Critical | Planned |
| GR-010 | Developer Experience | High | Planned |

Future categories may be added without changing the core schema.

## Research Status Lifecycle

| Status | Meaning |
| --- | --- |
| `Proposed` | Research topic was suggested but not yet planned. |
| `Planned` | Topic is accepted as a research target, but work has not started. |
| `Researching` | Sources are being reviewed and evidence is being collected. |
| `Draft` | Findings exist but are not ready for review. |
| `Under Review` | Human or architecture review is evaluating the Research asset. |
| `Completed` | Research record is complete enough to preserve knowledge. This does not mean adoption. |
| `Deferred` | Topic remains useful but is not current priority. |
| `Superseded` | A newer Research asset replaces this record. |
| `Archived` | Record is preserved for history and not active. |
| `Cancelled` | Research was stopped and should not continue without a new decision. |

Completed Research may produce accepted, deferred, rejected, or research-only
decisions.

## Adoption Decision Vocabulary

Adoption Decision is required at idea level.

Allowed values:

| Decision | Meaning |
| --- | --- |
| `Accepted` | Idea is suitable for GDS direction and may move toward candidate or standardization gates. |
| `Partially Accepted` | Some parts fit GDS, but others are excluded or deferred. |
| `Deferred` | Idea may be useful later, but should not proceed now. |
| `Rejected` | Idea should not be adopted under current evidence. |
| `Merged into Existing Candidate` | Idea is already covered and should link to the existing candidate. |
| `Research Only` | Knowledge is worth preserving but should not produce a candidate. |
| `Pending Validation` | A field experiment or evidence review is required before decision. |

Every decision records:

- decision;
- subject or idea;
- reason;
- decision date;
- decision actor;
- related Future Candidate or Platform Candidate;
- conditions for reconsideration;
- supporting evidence.

## Decision Granularity

One Research asset may contain multiple design ideas and different decisions.

Example:

```text
State Machine: Accepted
Human-in-the-loop checkpoint: Accepted
Graph execution: Pending Validation
Visual workflow editor: Deferred
Framework-specific runtime dependency: Rejected
```

Do not force a single adoption decision for the whole Research topic.

## Canonical Promotion Workflow

```text
GitHub / OSS / External Architecture
  -> Ghost Research
  -> Candidate extraction
  -> Future Candidate
  -> GG Validation proposal
  -> Evidence accumulation
  -> Platform Promotion Review
  -> Platform Candidate
  -> Standardization Decision
  -> GDS Standard
```

Ghost Research must not bypass Future Candidate, Evidence, Platform Promotion,
ADR, or Human Approval gates.

When an idea already exists as a Future Candidate, link to it and use
`Merged into Existing Candidate` instead of creating a duplicate.

## GG Validation Relationship

Ghost Research should answer:

- Can this idea be safely tested in GameGhost or another Ghost repository?
- What is the smallest safe experiment?
- What evidence is required?
- What is the success condition?
- What is the failure condition?
- What must not be changed during validation?
- Is the idea domain-specific or platform-level?
- Can the result generalize beyond one Ghost?

A GG validation proposal does not authorize implementation. It should normally
produce or link to a separate Q.

## Evidence Requirements

Promotion decisions should consider:

- architectural fit;
- implementation feasibility;
- repository impact;
- test results;
- performance;
- maintainability;
- failure behavior;
- migration cost;
- operator usability;
- Human Approval compatibility;
- SCW compatibility;
- cross-repository applicability;
- comparison with existing GDS design;
- negative evidence;
- reasons not to promote.

Failed or inconclusive experiments are valid Evidence and must be preserved
when they prevent repeated work.

## Relationship To Future Candidate

Ghost Research may produce zero, one, or many Future Candidates.

Rules:

- Research finding is not automatically a Future Candidate.
- Duplicate candidates must be merged or linked.
- Candidate titles should describe the Ghost-native idea.
- External framework names may appear as sources, not necessarily as candidate identity.
- Candidate records should state which Research findings support them.
- Rejection of one implementation does not necessarily reject the underlying design principle.

Example:

```text
Research Source: LangGraph checkpointing
Ghost-native Candidate: Durable Approval Runtime Checkpoint
```

## Relationship To Platform Candidate

Ghost Research may assess Platform Candidate Potential, but cannot independently
promote an idea.

Platform Candidate should require:

- Future Candidate record;
- GG or equivalent validation;
- Evidence;
- applicability beyond one Ghost;
- architecture review;
- risk review;
- adoption rationale;
- migration direction;
- decision record.

## Relationship To ADR, Improvement Record, And Case

```text
Ghost Research = What was learned and evaluated
ADR            = What architecture decision was made
Improvement    = How an operational gap became reusable knowledge
Case           = Concrete observation or evidence
```

A completed Research asset may lead to an ADR. The ADR must reference the
Research and supporting Evidence. Do not rewrite Research to pretend an
undecided topic was already decided.

## Repository Intelligence Integration

Ghost Research is a future Repository Intelligence input.

Repository Intelligence may eventually:

- detect Research assets;
- index topics, sources, decisions, and candidate links;
- identify Research without decisions;
- identify accepted ideas without Candidate records;
- identify Candidates without validation evidence;
- detect duplicate Research topics;
- surface promotion opportunities;
- track stale Research;
- connect Research to ADRs, Qs, Evidence, and Standards.

This document does not implement automation.

## Knowledge Promotion Candidate Integration

Research findings may produce Knowledge Promotion Candidates for:

- Rule;
- Schema;
- Template;
- Example;
- Workflow;
- Architecture;
- Runtime Contract;
- Registry;
- Report;
- Checklist;
- Platform Capability.

The intended promotion target should be recorded when known. Unknown targets
may remain Future Candidates.

## Source And Attribution Rules

Each Research asset records:

- project or framework name;
- canonical repository or official documentation;
- version, branch, release, or review date where relevant;
- specific design area reviewed;
- license awareness where relevant;
- whether the finding is direct, inferred, or experimentally validated;
- access date;
- source quality.

Do not copy large portions of external documentation into GDS. Prefer summaries,
architectural interpretation, and source links.

Clearly distinguish:

```text
External Source Fact
GDS Interpretation
GDS Proposal
GG Validation Result
Adoption Decision
```

## OSS Copying Boundary

Ghost Research does not authorize code copying.

Before code reuse, dependency adoption, or direct reuse, separately review:

- license;
- dependency risk;
- maintenance status;
- security;
- compatibility;
- portability;
- vendor lock-in;
- replacement cost;
- attribution requirements.

## Research Quality Criteria

A useful Ghost Research asset has:

- clear Research Question;
- bounded Scope;
- authoritative sources;
- multiple projects when comparison is useful;
- strengths and weaknesses;
- GDS overlap analysis;
- Ghost-native interpretation;
- explicit Adoption Decisions;
- validation path;
- evidence requirements;
- source traceability;
- no unsupported claims;
- no popularity-only adoption;
- no implementation authorization hidden inside Research.

## Priority And Difficulty Scales

### Adoption Priority

| Value | Meaning |
| --- | --- |
| `Critical` | Important to near-term GDS Platform direction. |
| `High` | Strong value, but not an immediate blocker. |
| `Medium` | Useful after higher priorities mature. |
| `Low` | Limited current value. |
| `Observe` | Watch for future relevance without active work. |

Optional star display:

```text
★★★★★ = Critical
★★★★☆ = High
★★★☆☆ = Medium
★★☆☆☆ = Low
★☆☆☆☆ = Observe
```

### Implementation Difficulty

| Value | Meaning |
| --- | --- |
| `Very Low` | Documentation or small template change. |
| `Low` | Small scoped implementation or validation. |
| `Medium` | Multiple files or workflow integration. |
| `High` | Cross-component design, migration, or durable runtime work. |
| `Very High` | Platform-level architecture with long-term operational risk. |

Ratings require written rationale.

## Folder, Index, And Registry Direction

Canonical locations:

- Ghost Research architecture: `docs/architecture/ghost_research_knowledge_asset.md`
- Research assets and registry: `docs/research/`
- Ghost Research template: `templates/ghost_research_template.md`
- Ghost Research examples: `examples/ghost_research_examples.md`
- Ghost Research workflow: `docs/workflow/ghost_research_workflow.md`
- Ghost Research rules: `docs/rules/ghost_research_rules.md`

`docs/research/research_registry.md` is a lightweight index, not a second
source of truth. The detailed Research asset remains canonical.

## Machine-Readable Direction

Future machine-readable representation may use YAML front matter or a generated
schema.

Minimum direction:

```yaml
schema_version: ghost_research.v1
research_id: GR-001
title: Workflow Engines
category: workflow_engines
status: completed
adoption_priority: critical
implementation_difficulty: high
decisions:
  - idea: explicit_state_machine
    decision: accepted
    rationale: GDS approval governance already depends on explicit state.
    related_future_candidate: FC-...
sources:
  - name: Example Framework
    type: official_docs
    reviewed_at: 2026-07-18
```

The Markdown Research document remains the human-readable canonical record
until a future schema standard explicitly changes that relationship.

## Related Documents

- `docs/research/README.md`
- `docs/research/research_registry.md`
- `docs/research/GR-001_workflow_engines.md`
- `templates/ghost_research_template.md`
- `examples/ghost_research_examples.md`
- `docs/workflow/ghost_research_workflow.md`
- `docs/rules/ghost_research_rules.md`
- `docs/architecture/knowledge_artifact_responsibility_map.md`
- `docs/architecture/knowledge_promotion_engine.md`
- `docs/architecture/knowledge_candidate_classification_contract.md`
- `docs/workflow/innovation_pipeline_workflow.md`
- `docs/workflow/research_mission_workflow.md`
