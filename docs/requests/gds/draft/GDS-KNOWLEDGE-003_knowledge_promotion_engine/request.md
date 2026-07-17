# Q-GDS-KNOWLEDGE-003
# Knowledge Promotion Engine

**Status:** Draft  
**Priority:** High  
**Category:** GDS / Command Center / Repository Intelligence / Knowledge Management  
**Repository:** Ghost-Development-System-Docs  
**Execution Boundary:** Documentation and architecture foundation only unless this Q explicitly authorizes implementation  
**Human Approval:** Required for canonical promotion, repository mutation, Commit, Push, Tag, release, and cross-repository changes

---

## 1. Objective

Define the **Knowledge Promotion Engine** as the governed GDS capability that detects significant knowledge created during implementation and review, classifies it, proposes an appropriate promotion target, obtains Human Approval, and carries the approved work into a canonical artifact or a future Q.

The engine must transform development experience into reusable repository knowledge without silently promoting drafts, creating duplicate artifacts, or bypassing SCW and Human Approval First.

The target loop is:

```text
Implementation / Review Result
        ↓
Knowledge Candidate Detection
        ↓
Classification and Evidence
        ↓
Duplicate / Canonical Source Check
        ↓
Promotion Recommendation
        ↓
Human Approval
        ↓
Draft Creation or Knowledge Carry-Forward
        ↓
Validation
        ↓
Canonical Promotion
        ↓
Future Intent / Workflow / Rule Uses the Knowledge
```

---

## 2. Background

GDS-INTENT-001 established Intent-Driven Workflow:

```text
Intent
→ Recommendation
→ Pending Action
→ Human Approval
→ Action
```

GDS-KNOWLEDGE-001 established responsibility separation among:

- Q
- Issa
- ADR
- Improvement Record
- Rule
- Architecture Principle
- Workflow

ADR-GDS-005 established repository-based context reconstruction and knowledge-guided recommendations.

During completion review, GDS can already identify that implementation work may contain:

- an architectural decision;
- a newly discovered problem or origin story;
- a reusable improvement;
- a recurring safety boundary;
- a workflow improvement;
- a template improvement;
- a future implementation candidate.

However, detection, classification, approval, carry-forward, and canonical promotion are not yet defined as one governed system.

Without this Q, valuable experience remains in chat, completion reports, or request attachments and may never affect future recommendations.

---

## 3. Core Principle

The Knowledge Promotion Engine must follow:

> **Detect automatically. Explain clearly. Promote only with approval. Apply through canonical knowledge.**

The engine must not treat every observation as a new artifact.

It must prefer, in order:

1. update an existing canonical artifact;
2. attach a candidate to an active or directly related Q;
3. carry the candidate into the next appropriate Q;
4. create a new Draft artifact only when no suitable canonical target exists;
5. create a new Q Draft only when implementation work is required.

---

## 4. User Experience

The preferred user-facing interaction occurs during Codex result review or Completion Review.

Example:

```text
Knowledge Promotion Check

The result contains promotion candidates:

- ADR candidate: repository-based context reconstruction
- Issa candidate: discovery of Intent-Driven Workflow
- Workflow candidate: review → promotion → commit
- Rule candidate: approval does not equal repository mutation

Add these as governed promotion work?
```

The user may answer naturally:

```text
お願いします
```

This approval means:

> Register the identified candidates as governed promotion work.

It does **not** automatically mean:

- accept an ADR;
- publish an Issa as canonical;
- modify a Rule;
- Commit;
- Push;
- Tag;
- release;
- edit another repository.

Each mutating or canonicalizing action must remain a specific Pending Action with its own approval boundary.

---

## 5. Preferred Carry-Forward Behavior

The default behavior should be quiet and low-friction.

After approval, the system should preferably add the candidate to the most relevant existing or future Q rather than generating many visible standalone Q files.

Promotion target selection order:

1. current parent Q;
2. existing directly related child Q;
3. next scheduled implementation Q;
4. canonical artifact revision task;
5. new Q Draft only when no suitable target exists.

The selected Q should contain a standard section such as:

```markdown
## Knowledge Promotion Actions

### Candidates
- Candidate type:
- Summary:
- Evidence:
- Related artifacts:
- Proposed promotion target:
- Duplicate check:
- Approval state:

### Completion Conditions
- [ ] Candidate reviewed
- [ ] Canonical source checked
- [ ] Draft or revision created
- [ ] Human Approval obtained where required
- [ ] Index and lineage updated
- [ ] Validation passed
```

This behavior is called **Knowledge Carry-Forward**.

---

## 6. Scope

### 6.1 Knowledge Candidate Detection

Define detection signals for:

- ADR candidate
- Issa candidate
- Improvement Record candidate
- Rule candidate
- Architecture Principle candidate
- Workflow candidate
- Template candidate
- Example candidate
- Checklist candidate
- Intent Registry candidate
- Quality Gate candidate
- Capability Registry candidate
- Data Contract candidate
- Child Q candidate

Candidate detection must use concrete evidence from:

- Q acceptance criteria;
- Codex completion report;
- changed files;
- validation results;
- review findings;
- explicit user decisions;
- SCW events;
- repeated friction;
- repository architecture changes.

### 6.2 Classification

Each candidate must include:

- candidate type;
- concise statement;
- evidence;
- origin;
- related Q;
- related repository;
- proposed canonical target;
- confidence;
- duplicate status;
- required approval;
- recommended next action.

### 6.3 Duplicate and Canonical Source Check

Before creating a new artifact, the engine must inspect:

- AI Repository Index;
- related canonical directories;
- existing ADRs;
- existing Rules;
- existing Workflows;
- existing templates;
- existing Improvement Records;
- existing Issa artifacts;
- active and planned Q files.

If a canonical artifact already covers the candidate, prefer revision or linkage.

If canonical ownership is unclear or conflicting:

```text
STOP
CALL
WAIT
```

### 6.4 Promotion Recommendation

The engine must explain:

- why the candidate matters;
- why the proposed artifact type is correct;
- why an existing artifact cannot absorb it, when proposing a new artifact;
- what future GDS behavior will use it;
- what approval is being requested.

### 6.5 Human Approval and Pending Action

Promotion requests must use the Intent-Driven Workflow contract.

A valid Pending Action must identify:

- repository;
- operation;
- target artifact;
- scope;
- current status;
- proposed status or mutation;
- evidence;
- expected diff;
- validation requirements.

Generic replies such as `お願いします`, `はい`, or `OK` count as approval only when one unambiguous Pending Action exists and repository state has not changed.

### 6.6 Draft Creation

After approval, the engine may:

- create a Draft using the canonical template;
- revise an existing Draft;
- append a Knowledge Promotion Action to an existing Q;
- create a child-Q candidate;
- update lineage metadata;
- update an index only when the applicable gate permits it.

Draft creation is not canonical acceptance.

### 6.7 Canonical Promotion

Canonical promotion must follow artifact-specific lifecycle rules.

Examples:

- ADR: Proposed → Accepted
- Issa: Draft → Reviewed / Accepted according to its canonical standard
- Improvement Record: Draft → Reviewed → Promoted / Completed
- Rule: Draft proposal → approved canonical Rule
- Workflow: Draft → approved canonical Workflow

No promotion may bypass:

- canonical source review;
- artifact responsibility rules;
- Human Approval;
- validation;
- repository scope;
- SCW.

### 6.8 Knowledge Application

A promoted artifact must declare where it affects future work.

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

Saving an artifact without an application path is incomplete unless the artifact is intentionally historical evidence.

---

## 7. Architecture

Define the conceptual component structure:

```text
Completion Review / Project Intelligence Review
                  ↓
      Knowledge Candidate Detector
                  ↓
        Artifact Classifier
                  ↓
 Canonical Source and Duplicate Resolver
                  ↓
       Promotion Recommendation
                  ↓
        Human Approval Gate
                  ↓
  Knowledge Carry-Forward / Draft Builder
                  ↓
      Validation and Promotion Gate
                  ↓
 Canonical Artifact + Lineage + Application Target
```

The Knowledge Promotion Engine must not directly execute unrestricted Git or cross-repository actions.

Execution must occur through governed adapters or explicit commands after approval.

---

## 8. Relationship to Command Center

Command Center should eventually contain two complementary cores:

```text
Command Center
├── Intent Engine
│   └── supports the current decision
└── Knowledge Promotion Engine
    └── improves future decision capability
```

The Intent Engine consumes canonical knowledge.

The Knowledge Promotion Engine improves the knowledge that future Intent Engine recommendations consume.

This creates the GDS learning loop:

```text
Experience
→ Capture
→ Review
→ Promotion
→ Application
→ Better Recommendation
→ New Experience
```

---

## 9. Deliverables

At minimum, this Q must produce:

1. Knowledge Promotion Engine architecture document.
2. Knowledge Candidate classification contract.
3. Knowledge Carry-Forward workflow.
4. Completion Review integration specification.
5. Pending Action and Human Approval boundaries for promotion.
6. Duplicate and canonical-source resolution rules.
7. Promotion reason codes.
8. Knowledge application target rules.
9. Child-Q plan for implementation phases.
10. Completion Report.
11. AI Repository Index update when required by the canonical gate.
12. Roadmap update reflecting the approved architecture and implementation order.

---

## 10. Required Reason Codes

Define at least the following reason codes.

### Positive

- `KNOWLEDGE_CANDIDATE_DETECTED`
- `PROMOTION_TARGET_IDENTIFIED`
- `CANONICAL_SOURCE_CONFIRMED`
- `EXISTING_ARTIFACT_REVISION_PREFERRED`
- `NEW_DRAFT_REQUIRED`
- `KNOWLEDGE_CARRY_FORWARD_SELECTED`
- `HUMAN_APPROVAL_RECEIVED`
- `PROMOTION_VALIDATION_PASSED`
- `LINEAGE_UPDATED`
- `APPLICATION_TARGET_DEFINED`

### Blocking

- `CANDIDATE_TYPE_AMBIGUOUS`
- `CANONICAL_SOURCE_UNREADABLE`
- `CANONICAL_OWNER_UNKNOWN`
- `DUPLICATE_ARTIFACT_POSSIBLE`
- `PROMOTION_TARGET_AMBIGUOUS`
- `NO_PENDING_ACTION`
- `MULTIPLE_PENDING_ACTIONS`
- `REPOSITORY_STATE_CHANGED`
- `HUMAN_APPROVAL_REQUIRED`
- `TEMPLATE_NOT_FOUND`
- `LIFECYCLE_UNDEFINED`
- `LINEAGE_TARGET_UNKNOWN`
- `VALIDATION_NOT_RUN`
- `VALIDATION_FAILED`
- `CROSS_REPOSITORY_SCOPE_UNAPPROVED`
- `SCW_REQUIRED`

---

## 11. Out of Scope

This Q does not authorize:

- autonomous canonical promotion without Human Approval;
- automatic Commit, Push, Tag, or release;
- unrestricted LLM classification;
- direct runtime implementation of every detector;
- GameGhost edits;
- cross-repository mutation;
- automatic replacement of existing Rules, ADRs, or Workflows;
- bypassing artifact-specific templates or lifecycles;
- treating chat history as canonical knowledge.

---

## 12. Acceptance Criteria

The Q is complete when:

- [ ] Knowledge Promotion Engine has a documented architecture.
- [ ] Candidate types and evidence requirements are defined.
- [ ] Duplicate and canonical source checks are defined.
- [ ] Knowledge Carry-Forward behavior is defined.
- [ ] Review-time user interaction is defined.
- [ ] Pending Action and Human Approval boundaries are explicit.
- [ ] Canonical promotion remains artifact-specific and gated.
- [ ] Knowledge application targets are required.
- [ ] SCW conditions are documented.
- [ ] Reason codes are documented.
- [ ] Child-Q implementation sequence is proposed.
- [ ] Completion Report is produced.
- [ ] AI Repository Index validates successfully.
- [ ] Encoding regression validation passes.
- [ ] `git diff --check` passes except accepted line-ending warnings.
- [ ] Dirty workspace contains only this Q's approved scope.
- [ ] Commit / Push / Tag remain unperformed without separate Human Approval.

---

## 13. Verification

Run the canonical repository verification commands, including at minimum:

```bash
python scripts/generate_ai_repository_index.py --write
python scripts/generate_ai_repository_index.py --validate
python scripts/validate_encoding_regression.py --all
git diff --check
git status --short --untracked-files=all
```

If the canonical commands differ, follow the current repository source of truth.

---

## 14. SCW Conditions

Stop and request review when:

- the canonical Knowledge Artifact Standard is missing or unreadable;
- Issa, ADR, Improvement Record, Rule, or Workflow lifecycle is unclear;
- multiple canonical promotion targets conflict;
- the candidate duplicates an existing artifact and revision ownership is unclear;
- a generic approval phrase could refer to more than one action;
- repository state changes after the recommendation;
- the operation would cross repository boundaries;
- validation fails;
- the proposed promotion would silently alter accepted architecture;
- the proposed action includes Commit, Push, Tag, or release without explicit approval.

---

## 15. Dependencies

Required or expected predecessors:

- GDS-INTENT-001 Intent-Driven Workflow Foundation
- GDS-KNOWLEDGE-001 Revolution Aftermath Knowledge Preservation
- GDS-KNOWLEDGE-002 Knowledge Artifact Standard Foundation
- ADR-GDS-005 Context Reconstruction and Knowledge-Guided Recommendations
- canonical Q template
- canonical artifact templates and lifecycle definitions
- AI Repository Index Update Gate
- Human Approval Gate
- SCW

If GDS-KNOWLEDGE-002 is incomplete or the required artifact standards remain ambiguous, this Q must remain architecture-only or stop under SCW before automation design.

---

## 16. Recommended Child Q Sequence

1. **GDS-KNOWLEDGE-003A Completion Review Knowledge Candidate Detection**
2. **GDS-KNOWLEDGE-003B Knowledge Carry-Forward Workflow**
3. **GDS-KNOWLEDGE-003C Promotion Pending Action Contract**
4. **GDS-KNOWLEDGE-003D Canonical Promotion and Lineage Adapter**
5. **GDS-KNOWLEDGE-003E Knowledge Application Registry Integration**

Child-Q identifiers may be revised to match the canonical queue and naming rules.

---

## 17. Suggested Commit Message

```text
docs(knowledge): define knowledge promotion engine
```

---

## 18. Completion Report Requirements

The Completion Report must state:

- artifacts created or revised;
- candidate types supported;
- canonical-source and duplicate checks implemented or documented;
- approval boundaries;
- Knowledge Carry-Forward behavior;
- lifecycle assumptions;
- unresolved storage or template ambiguity;
- validation results;
- dirty-workspace scope;
- recommended next Q;
- Commit readiness;
- whether Commit, Push, Tag, release, or other repositories were touched.
