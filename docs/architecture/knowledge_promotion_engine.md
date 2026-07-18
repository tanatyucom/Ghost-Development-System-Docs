# Knowledge Promotion Engine Architecture

**Status:** Draft Architecture Foundation

**Last Updated:** 2026-07-17

## Purpose

Knowledge Promotion Engine is the governed GDS capability that detects
significant knowledge created during implementation and review, classifies it,
checks canonical sources and duplicates, recommends a promotion target, obtains
Human Approval, and carries the approved work into a canonical artifact or a
future Q.

It transforms development experience into reusable repository knowledge without
silently promoting drafts, creating duplicate artifacts, or bypassing SCW and
Human Approval First.

## Core Principle

```text
Detect automatically.
Explain clearly.
Promote only with approval.
Apply through canonical knowledge.
```

The engine must not treat every observation as a new artifact.

Preference order:

1. update an existing canonical artifact;
2. attach a candidate to an active or directly related Q;
3. carry the candidate into the next appropriate Q;
4. create a new Draft artifact only when no suitable canonical target exists;
5. create a new Q Draft only when implementation work is required.

## Architecture Overview

```text
Completion Review / Project Intelligence Review
                  |
                  v
      Knowledge Candidate Detector
                  |
                  v
        Artifact Classifier
                  |
                  v
 Canonical Source and Duplicate Resolver
                  |
                  v
       Promotion Recommendation
                  |
                  v
        Human Approval Gate
                  |
                  v
  Knowledge Carry-Forward / Draft Builder
                  |
                  v
      Validation and Promotion Gate
                  |
                  v
 Canonical Artifact + Lineage + Application Target
```

## Core Components

### Knowledge Candidate Detector

Detects candidate knowledge from:

- Q acceptance criteria;
- Completion Report;
- Ghost Research Adoption Decisions;
- changed files;
- validation results;
- review findings;
- explicit user decisions;
- SCW events;
- repeated friction;
- repository architecture changes.

Detection is advisory. It does not create or promote artifacts by itself.

### Artifact Classifier

Classifies each candidate as one of:

- ADR candidate;
- Issa candidate;
- Improvement Record candidate;
- Rule candidate;
- Architecture Principle candidate;
- Workflow candidate;
- Template candidate;
- Example candidate;
- Ghost Research candidate;
- Checklist candidate;
- Intent Registry candidate;
- Quality Gate candidate;
- Capability Registry candidate;
- Data Contract candidate;
- Child Q candidate.

Classification follows `knowledge_candidate_classification_contract.md`.

### Canonical Source and Duplicate Resolver

Checks whether the candidate is already covered by:

- AI Repository Index;
- existing ADRs;
- existing Rules;
- existing Workflows;
- existing Templates;
- existing Knowledge Inventory;
- existing Ghost Research assets;
- existing Conversation Insights;
- existing request / child Q candidates;
- related Completion Reports.

If an existing artifact covers the candidate, prefer revision or linkage.

If ownership, lifecycle, or canonical target is unclear, apply SCW.

### Promotion Recommendation

Explains:

- why the candidate matters;
- why the proposed artifact type is correct;
- why an existing artifact cannot absorb it, when proposing a new artifact;
- what future GDS behavior will use it;
- what approval is being requested.

Recommendation is not promotion.

### Human Approval Gate

Promotion requests must follow Intent-Driven Workflow.

A generic approval phrase such as `お願いします`, `はい`, or `OK` counts as
approval only when exactly one unambiguous Pending Action exists and repository
state has not changed.

### Knowledge Carry-Forward / Draft Builder

After approval, the engine may:

- append a Knowledge Promotion Action to an existing Q;
- create or revise a Draft artifact;
- create a child-Q candidate;
- update lineage metadata;
- update an index only when the applicable gate permits it.

Draft creation is not canonical acceptance.

### Validation and Promotion Gate

Canonical promotion follows artifact-specific lifecycle rules.

Examples:

- ADR: Proposed -> Accepted.
- Issa: Draft -> Reviewed / Accepted after its canonical standard exists.
- Rule: Draft proposal -> approved canonical Rule.
- Workflow: Draft -> approved canonical Workflow.

No promotion may bypass canonical source review, Human Approval, validation,
repository scope, or SCW.

## Relationship To Command Center

Command Center should eventually contain two complementary cores:

```text
Command Center
|-- Intent Engine
|   `-- supports the current decision
`-- Knowledge Promotion Engine
    `-- improves future decision capability
```

Intent Engine consumes canonical knowledge.

Knowledge Promotion Engine improves the knowledge that future Intent Engine
recommendations consume.

This creates the GDS learning loop:

```text
Experience
  -> Capture
  -> Review
  -> Promotion
  -> Application
  -> Better Recommendation
  -> New Experience
```

## Human Approval Boundary

The engine must not automatically:

- accept ADRs;
- canonicalize Issa artifacts;
- promote Rules or Workflows;
- mutate repositories;
- commit, push, tag, merge, release, or publish;
- edit cross-repository targets;
- replace artifact-specific lifecycle rules.

## SCW Conditions

Stop, call, and wait when:

- candidate type is ambiguous;
- canonical source is unreadable;
- canonical owner is unknown;
- duplicate artifact is possible;
- promotion target is ambiguous;
- no valid Pending Action exists;
- multiple Pending Actions exist;
- repository state changed after recommendation;
- required template is missing;
- lifecycle is undefined;
- lineage target is unknown;
- validation failed or was not run;
- cross-repository scope is not approved.

## Knowledge Application Target

Every promoted artifact should declare where it will affect future work.

Possible application targets:

- Intent Engine recommendations;
- Startup;
- Completion Review;
- Q Creation Gate;
- Quality Gate;
- Template;
- Checklist;
- Workflow;
- Architecture;
- Repository Scanner;
- Capability Registry;
- Repository Health rules;
- future Q generation.

Saving an artifact without an application path is incomplete unless it is
intentionally historical evidence.

## Out Of Scope

- Runtime implementation.
- LLM classifier implementation.
- Automatic canonical promotion.
- Automatic Git operation.
- GameGhost edits.
- Cross-repository mutation.
- Replacement of existing Rules, ADRs, or Workflows.

## Related Documents

- `docs/architecture/knowledge_artifact_responsibility_map.md`
- `docs/architecture/ghost_research_knowledge_asset.md`
- `docs/architecture/intent_driven_workflow.md`
- `docs/workflow/knowledge_preservation_gate.md`
- `docs/workflow/knowledge_carry_forward_workflow.md`
- `docs/architecture/knowledge_candidate_classification_contract.md`
- `docs/adr/ADR-GDS-005_context_reconstruction_and_knowledge_guided_recommendations.md`
