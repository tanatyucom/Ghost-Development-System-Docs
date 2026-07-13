# Q_GDS_Review_Center_Architecture_JP

Version: 1.0
Status: Draft
Priority: High
Category: Platform Architecture / Review Management / Human Decision Interface
Created Date: 2026-07-13
Last Updated Date: 2026-07-13

## Identity

Q ID:

```text
GDS-REVIEW-CENTER-001
```

Title:

```text
Review Center Architecture
```

Owner / Target AI:

```text
Codex
```

## Purpose

Ghost Platform上の共通Review Management Systemとして、
Review CenterのArchitectureを正式定義する。

最初の実証対象はGameGhostのSteam OCR Human Reviewとする。

本Qでは実装そのものではなく、
Platform Core、GUI、Plugin / Adapter、Review Session、Review Result、
Human Approval、Gate連携、保存・再開・移行境界を確定する。

## Background

Steam OCRではHuman Review Gateが存在するが、
現状のレビュー作業はCSV、画像、Debug Artifact、手動確認に分散している。

一方、将来は以下にもHuman Reviewが必要になる。

- Steam OCR
- Switch OCR
- 3DS Alias
- Canonical Name
- Metadata
- Series Mapping
- Favorite Engine
- Plugin Review

このため、Steam OCR専用GUIではなく、
共通のReview Management SystemとしてReview Centerを設計する。

Review Centerは正解を判断しない。

```text
Artifactを表示する
→ Human Decisionを受け付ける
→ Progressを管理する
→ 保存・再開する
→ Gateへ結果を渡す
```

ことを担当する。

## Working Repository

```text
Ghost-Development-System-Docs
```

## Working Directory

```text
C:\GitHub\Ghost-Development-System-Docs
```

## Preferred Shell

```text
Git Bash
```

Runnable commands must begin with:

```bash
cd /c/GitHub/Ghost-Development-System-Docs
```

## Target Project

```text
GDS only
```

## Non-Target Project

```text
GameGhost
```

GameGhost must not be edited in this Q.

## Commit / Push Policy

```text
Commit: Do not execute
Push: Do not execute
```

## Existing Knowledge / Dependencies

- Platform Discoverability and Component Standard
- Platform First Migration Strategy
- Plugin Architecture Standard
- Human Approval First
- Review Entry Point Rule
- Debug Artifact Review Workflow
- Completion Report Standard v2
- Platform Standard Registry
- GameGhost Steam OCR Human Review Gate context

## Core Definition

```text
Review Center = Human Review Session Manager
```

Review Center itself does not know the correct answer.

It manages:

- what to display
- what decision options exist
- current review position
- saved progress
- decision persistence
- completion state
- gate export

Domain-specific judgment belongs to Plugin / Adapter definitions and the human reviewer.

## Scope

- Review Center responsibility
- Review Center GUI responsibility
- Review Core responsibility
- Review Plugin / Adapter boundary
- Review Item schema
- Review Artifact schema
- Review Decision schema
- Review Session schema
- Review Result schema
- Human Approval model
- Progress management
- save / resume
- previous / next navigation
- correction / undo policy
- Gate export
- Registry integration
- Steam OCR vertical slice definition
- Platform folder placement
- Legacy migration boundary
- Future Ghost compatibility
- Architecture report
- AI Repository Index update

## Out of Scope

- GameGhost code implementation
- Steam OCR review execution
- 93-item review completion
- Production integration
- Switch / 3DS implementation
- Automatic decision making
- Automatic approval
- Automatic repair
- Automatic Commit / Push
- Command Center integration implementation
- Dashboard analytics
- Role / permission management
- Multi-user review

# Part 1: Architecture Boundary

## Review Center Platform Responsibilities

Review Center Core may know:

- Review Session ID
- Review Item ID
- current index / total
- artifact descriptors
- decision field definitions
- allowed choices
- notes
- save state
- completion state
- reviewer confirmation
- export state
- plugin identity

Review Center Core must not know:

- Steam OCR BBox correctness
- 3DS Alias correctness
- Metadata matching rules
- Canonical Name policy
- Series Mapping business rules
- Favorite Engine scoring semantics

## Domain Responsibilities

GameGhost / Adapter / Plugin owns:

- how raw domain data becomes Review Items
- which artifacts are shown
- which decision options exist
- domain-specific labels
- validation rules for a decision
- conversion from Review Result to domain gate input
- domain-specific repair or retry actions

## Required Boundary Statement

```text
Platform:
Review session, artifact presentation contract, decision capture,
progress, persistence, navigation, result export, approval state

Domain:
Review item preparation, domain labels, domain choices,
domain validation, domain gate adapter
```

# Part 2: Component Structure

Use the approved Platform Component Standard.

Candidate placement:

```text
platform/
  frameworks/
    review_center/
      review_center_gui.py
      review_session.py
      review_storage.py
      review_models.py
      review_result_schema.py
      review_plugin_registry.py
      review_gate_workflow.py
      artifact_viewer/
      plugins/
```

Architecture must decide the final canonical structure.

## Naming Requirement

GUI Entry Point must include:

```text
review_center_gui.py
```

Generic names such as:

```text
app.py
main.py
review_center.py
```

must not be used as the primary GUI entry point.

# Part 3: Review Models

## Review Item

Candidate fields:

- review_item_id
- source_type
- source_record_id
- display_title
- artifact list
- decision field list
- default values
- current decision
- notes
- status
- created_at
- updated_at
- plugin_id
- source provenance

## Review Artifact

Candidate types:

- image
- overlay
- bounding box
- text
- structured metadata
- comparison table
- source link
- debug file
- JSON / CSV fragment

Candidate fields:

- artifact_id
- artifact_type
- label
- path / URI
- mime type
- display order
- optional metadata
- required / optional
- missing behavior

## Review Decision Field

Candidate fields:

- field_id
- label
- type
- allowed values
- required
- default
- help text
- domain validation reference

Supported initial field types:

- single choice
- boolean
- text note
- read-only comparison
- optional numeric value

## Review Session

Candidate fields:

- review_session_id
- plugin_id
- source batch identity
- total items
- current item index
- reviewed count
- remaining count
- created_at
- last_opened_at
- completed_at
- reviewer
- status
- storage version
- source fingerprint

## Review Result

Candidate fields:

- review_item_id
- decision values
- notes
- reviewed_at
- reviewer
- revision number
- approval state
- plugin version
- source fingerprint

# Part 4: Human Approval Model

Review Center must preserve Human Approval First.

Candidate states:

```text
Unreviewed
In Review
Reviewed
Approved
Rejected
Retry Requested
Superseded
```

Architecture must decide:

- whether Reviewed and Approved are separate
- whether one-person operation may combine them
- how a revised decision supersedes an earlier result
- how the Gate determines readiness
- how incomplete required fields block approval

No automatic approval.

# Part 5: Persistence and Resume

Review sessions must support:

```text
11 / 93
→ close
→ reopen
→ resume from 12 / 93
```

Required decisions:

- storage format
- storage location
- atomic save
- backup / recovery
- source batch fingerprint
- stale session detection
- plugin version mismatch handling
- missing artifact handling
- partial review handling

Candidate storage:

- JSON
- SQLite
- both, with one canonical source

Avoid committing transient personal review state unless explicitly approved.

# Part 6: Navigation and Editing

Required behavior:

- Next
- Previous
- Jump to item
- Save
- Save and Next
- Resume
- Filter by status
- Reopen reviewed item
- Correct previous decision
- Show unsaved state
- Confirm destructive reset

Architecture must define whether autosave is allowed.

Recommended default:

```text
Explicit Save
+
optional safe autosave after validated decision
```

The decision must be documented.

# Part 7: Gate Integration

Review Center output must be consumable by a Gate.

Flow:

```text
Source Artifacts
→ Review Plugin / Adapter
→ Review Center Session
→ Human Decision
→ Review Result Export
→ Domain Gate Adapter
→ Gate
→ Production Readiness
```

Required decisions:

- canonical export format
- completeness check
- failed / retry items
- versioning
- provenance
- gate summary
- production-ready criteria
- audit trail

Review Center does not execute Production changes.

# Part 8: Steam OCR Vertical Slice

The first concrete implementation target must be defined.

Required initial artifacts:

- source screenshot
- title crop
- BBox overlay
- OCR output
- expected title
- metadata comparison
- alias comparison when available

Required initial decision groups:

### Target Row

- PASS
- WRONG TARGET
- RETRY

### BBox

- PASS
- MISSING TEXT
- TOO TALL
- TOO SHORT
- OVERFLOW

### OCR

- PASS
- FAIL
- RETRY

### Metadata

- PASS
- FAIL
- NOT APPLICABLE

### Alias

- PASS
- FAIL
- NOT APPLICABLE

### Notes

- free text

Architecture must define the minimum Steam OCR adapter contract without editing GameGhost.

# Part 9: Registry and Plugin Interface

Review Center must use explicit registration.

Candidate plugin metadata:

- plugin_id
- display_name
- version
- supported review type
- item provider
- artifact provider
- decision schema provider
- result exporter
- gate adapter
- compatibility version

No uncontrolled automatic discovery unless the existing Plugin Standard explicitly permits it.

# Part 10: Legacy Migration

Steam OCR review currently exists in Legacy / scripts / tool.py-related flows.

Migration stages:

```text
Architecture
→ Platform Core
→ Steam OCR Adapter
→ Parallel Verification
→ Review Center production use
→ Legacy Review Entry Point deprecation
→ Thin redirect if needed
→ Legacy removal
```

Do not delete Legacy review behavior before:

- Review Center completes real Steam OCR review
- output parity is verified
- Gate consumes new output
- recovery path exists

# Part 11: GUI Requirements

The GUI is a management interface.

Minimum screen areas:

```text
Review Center Header
Source / Plugin Selector
Progress
Artifact Viewer
Comparison Area
Decision Panel
Notes
Save / Previous / Next
Session Status
Gate Readiness Summary
```

Initial implementation may use Streamlit if compatible with current environment,
but Architecture must avoid binding Review Core to one GUI toolkit.

GUI and Core must be separable.

# Part 12: Non-Functional Requirements

- discoverable within 3 seconds
- safe for intermittent use
- usable after long periods of inactivity
- explicit error messages
- no silent data loss
- no silent approval
- portable within Ghost projects
- UTF-8 safe
- testable without GUI
- source provenance preserved
- plugin failure isolated
- resume after interruption

# Required Deliverables

- `docs/architecture/review_center_architecture.md`
- `docs/rules/review_center_rules.md`
- `docs/workflow/review_center_workflow.md`
- `docs/architecture/platform_standard_registry.md` update
- registry update artifact
- `examples/review_center_examples.md`
- optional schema proposal
- optional text component diagram
- README / architecture / rules / workflow / examples index updates
- AI Repository Index update
- Repository Quality Report update
- request.md
- notes.md
- completion_report.md

## AI Repository Index Update Gate

```text
Yes
```

## Verification

Run:

```bash
cd /c/GitHub/Ghost-Development-System-Docs

python scripts/validate_encoding_regression.py --all
python scripts/validate_encoding_regression.py --staged
python scripts/generate_ai_repository_index.py --write
python scripts/generate_ai_repository_index.py --validate
python scripts/repository_quality_audit.py
git diff --check
git status --short
```

Repository Quality must remain Green.

## Completion Report Requirements

Include:

- Changed Files
- Summary
- Final component structure
- Platform / Domain boundary
- Review schemas decided
- Human Approval model
- Persistence / resume decision
- Gate integration
- Steam OCR vertical slice
- Registry / Plugin contract
- Legacy migration stages
- GUI boundary
- Verification
- Repository Quality
- Remaining Issues
- Improvement Review
- Lessons Learned
- Reusable Assets Created
- Future Candidates
- Recommended Next Q
- Safe Commit Set
- Suggested Commit Message
- Commit / Push Status
- GameGhost Edit Status

## Completion Criteria

- Review Center responsibility finalized
- Platform / Domain boundary finalized
- GUI canonical name finalized
- component structure finalized
- Review Item / Artifact / Decision / Session / Result models defined
- Human Approval model defined
- persistence / resume policy defined
- Gate export defined
- Steam OCR vertical slice defined
- Legacy migration sequence defined
- GameGhost remains unedited
- Repository Quality remains Green
- Commit / Push not executed

## Future Candidates

- Review Center implementation Q
- Steam OCR Review Adapter Q
- Switch OCR Review Adapter
- 3DS Alias Review Adapter
- Canonical Name Review Adapter
- Metadata Review Adapter
- Review Analytics
- Command Center integration
- Multi-user Review
- Review History Dashboard

## Recommended Next Q

```text
Q_GameGhost_Review_Center_Core_and_Steam_OCR_Vertical_Slice_JP
```

or an evidence-based architecture revision.

## Review Decision

Completion review must return one of:

```text
Commit OK
Revision Recommended
Minor Recommendation
```

## Suggested Commit Message

```text
docs: define review center architecture
```
