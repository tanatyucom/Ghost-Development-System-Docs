# Q_GG_DIRTY_WORKTREE_TRIAGE_FOR_PLATFORM_DOGFOODING_001

## Title

Triage the GameGhost Dirty Worktree and Define the Normal Dirty-State Policy for Governed Platform Dogfooding

---

## Background

`Q_GG_PLATFORM_DOGFOODING_DRY_RUN_001` completed with:

```text
Decision:
PASS WITH LIMITATION
```

The GDS governance flow was successfully validated against GameGhost as a Reference Project without introducing any repository mutation.

Measured GameGhost state:

```text
Dirty / untracked count before dry run: 1924
Dirty / untracked count after dry run:  1924
New mutation caused by dry run:          0
```

This proves that the dry run itself was non-mutating.

However, the existing GameGhost worktree contains a large number of tracked changes and/or untracked files. Their origin, ownership, canonical status, regeneration characteristics, and intended repository treatment are not yet sufficiently classified.

Without this classification:

- a new unexpected mutation may be hidden inside the existing dirty set
- Repository Health cannot distinguish normal noise from actual risk
- Governed Execution cannot prove its exact mutation scope reliably
- Completion Review may depend on count comparison rather than artifact identity
- generated files may be tracked unnecessarily
- canonical outputs may be ignored accidentally
- local-only or sensitive artifacts may remain exposed
- the next mutating dogfooding could operate on an unsafe baseline

This Q creates the worktree-health baseline and defines what GameGhost may treat as a normal dirty state.

---

## Objective

Inspect and classify the current GameGhost dirty worktree, define the canonical policy for normal and abnormal dirty states, and determine the entry conditions for the first governed mutating dogfooding.

The Q must not assume that all 1924 entries should be deleted, ignored, committed, or preserved.

Each category must be evaluated according to repository authority, reproducibility, evidence value, sensitivity, and operational risk.

---

## Core Policy Direction

Use the following principle as the review baseline:

```text
Repository target state:
Clean by default

Allowed exception:
Explicitly identified, owned, bounded, and time-limited Expected Dirty state

Regenerable non-canonical artifacts:
Ignore or relocate outside tracked repository scope

Canonical artifacts and governed evidence:
Track in Git

Unknown or unexpected artifacts:
SCW
```

The current 1924-entry state must not automatically be declared normal.

The intended long-term target is a repository state where a new mutation can be identified by artifact identity and approved scope, not merely by total file count.

---

## Scope

This Q may inspect:

- tracked modified files
- deleted tracked files
- renamed files
- untracked files
- ignored files when relevant to diagnosis
- generated outputs
- temporary and debug outputs
- caches and logs
- local databases and backups
- canonical datasets
- reviewed reports and evidence
- legacy artifacts
- repository-root output sprawl
- current `.gitignore`
- generation destinations
- scripts or workflows responsible for repeated outputs
- repository documentation defining artifact ownership

This Q may update GameGhost documentation, inventory, policy, and planning artifacts only when explicitly required by the approved Q scope.

This Q must not perform broad cleanup or destructive mutation.

---

## Required Classification Model

Classify each dirty item or coherent artifact group into one of the following categories.

### 1. Tracked Intentional Change

A tracked change created for an active, known task.

Required decision:

- preserve for review
- associate with owning Q or work item
- commit separately
- revert only with explicit human approval

### 2. Generated Reproducible Artifact

An artifact that can be recreated from authoritative inputs and is not itself repository truth.

Candidate treatment:

- add to `.gitignore`
- relocate to a generated/work directory
- generate outside the repository
- retain only through an explicit evidence policy

### 3. Canonical Generated Artifact

A generated artifact that is nevertheless an approved repository asset or source of truth.

Examples may include:

- reviewed canonical CSV
- approved migration result
- required validation evidence
- stable generated index
- governed completion or audit artifact

Candidate treatment:

- retain in Git
- document the generator and authoritative inputs
- control nondeterministic fields
- verify reproducibility or intentional non-reproducibility

### 4. Temporary / Debug Artifact

Short-lived operational material with no canonical or review value.

Candidate treatment:

- delete after review
- ignore
- relocate outside governed paths

### 5. Ignore Candidate

A non-canonical artifact that should normally remain invisible to repository health checks.

Required checks:

- safe to regenerate
- safe to remove
- contains no required evidence
- contains no unique user-authored information
- contains no credentials or sensitive data
- ignore rule will not hide canonical artifacts

### 6. Legacy Artifact

An artifact from an older workflow, repository layout, database generation, or superseded implementation.

Candidate treatment:

- archive
- migrate
- retain with explicit legacy status
- remove through a separate approved cleanup Q

### 7. Unknown Origin

An item whose producer, owner, purpose, or authoritative status cannot be established.

Required treatment:

```text
SCW
Stop -> Call -> Wait
```

No deletion, ignore rule, migration, or commit decision may be inferred.

### 8. Unexpected Mutation

A change that conflicts with the expected baseline, approved operation, or known generation behavior.

Required treatment:

```text
SCW
```

Investigate before any governed execution continues.

---

## Required Metadata

For every item or artifact group, record as much of the following as can be established:

```text
Path or pattern:
Category:
Current Git status:
Producer:
Owning workflow or Q:
Owner:
Purpose:
Canonical: Yes / No / Unknown
Regenerable: Yes / No / Unknown
Authoritative input:
Expected generation location:
Evidence value:
Sensitivity:
Git tracking decision:
Cleanup or migration action:
Dogfooding risk:
Confidence:
Notes:
```

Grouping is allowed when all files share the same producer, lifecycle, authority, and treatment.

Do not hide uncertainty through broad grouping.

---

## Normal Dirty-State Policy

Define a formal policy using at least these states.

### CLEAN

```text
No tracked mutation
No untracked artifact requiring review
No unknown-origin artifact
```

This is the preferred entry state for mutating dogfooding.

### EXPECTED DIRTY

A temporary exception where every dirty artifact is:

- explicitly identified
- tied to a known task or workflow
- assigned an owner
- bounded by path or exact artifact list
- assigned a planned disposition
- recorded in a baseline snapshot
- not sensitive or authority-ambiguous
- not mixed with unknown mutations

Expected Dirty must not become an indefinite substitute for repository hygiene.

### UNSAFE DIRTY

Any dirty state containing one or more of:

- unknown origin
- unexpected mutation
- ambiguous authority
- mixed unrelated scope
- unbounded generated output
- sensitive material
- unexplained deletion
- unexplained tracked modification
- incomplete baseline evidence

Unsafe Dirty requires SCW and blocks mutating dogfooding.

---

## Artifact Retention Rules

### Use `.gitignore` when all are true

- the artifact is non-canonical
- the artifact is reproducible or disposable
- the artifact is not required for review or historical evidence
- the artifact contains no unique user-authored information
- hiding it will not conceal future unexpected mutations
- the ignore rule is narrow enough to avoid masking authoritative files

### Keep in Git when one or more are true

- the artifact is repository truth
- the artifact is an approved canonical dataset
- the artifact is required governed evidence
- the artifact must be reviewed through diffs
- the artifact represents an intentional migration or release result
- loss would prevent reconstruction of an approved project state

### Revise the generation workflow when

- outputs are written broadly into the repository root
- canonical and temporary outputs are mixed
- every execution rewrites unchanged artifacts
- timestamps or unstable ordering create meaningless diffs
- generated outputs cannot be mapped to their producer
- local runtime data and repository assets share the same path
- a large quantity of repository noise is produced by default

---

## Recommended Directory Model to Evaluate

Evaluate whether GameGhost should converge toward a structure similar to:

```text
data/
  canonical/

artifacts/
  reviewed/
  evidence/

work/
  generated/
  temp/
  debug/

runtime/
  cache/
  logs/
```

Candidate policy:

```text
Git tracked:
data/canonical/
artifacts/reviewed/
artifacts/evidence/

Normally ignored:
work/generated/
work/temp/
work/debug/
runtime/cache/
runtime/logs/
```

This structure is a review candidate, not an automatic migration instruction.

Existing architecture and canonical ownership take precedence.

---

## Required Worktree Inventory

Produce a worktree inventory containing at least:

- total dirty and untracked count
- count by Git status type
- count by top-level directory
- count by classification
- largest coherent artifact groups
- high-risk unknown groups
- tracked generated artifacts
- untracked canonical candidates
- likely `.gitignore` candidates
- likely generation-path correction candidates
- sensitive or credential-risk findings
- files that must be associated with existing Q work before any cleanup

Counts must not replace path-level evidence for risk-bearing items.

---

## Baseline Snapshot

Create a reproducible baseline snapshot sufficient to compare future governed operations.

The snapshot should include, where practical:

- repository identity
- current branch
- current HEAD
- timestamp
- Git status porcelain output or equivalent normalized inventory
- exact dirty path set
- classification summary
- known Expected Dirty set
- Unknown Origin set
- hash or stable fingerprint of the normalized path/status set
- tool or command used to produce the snapshot

The baseline must not be treated as repository truth if it contains unresolved unknown artifacts.

---

## Dogfooding Entry Gate

Determine one explicit outcome:

### READY FOR MUTATING DOGFOODING

Allowed only when:

- worktree is CLEAN, or
- a narrowly bounded EXPECTED DIRTY baseline is explicitly approved
- no Unknown Origin remains in the approved execution area
- no sensitive or authority-ambiguous artifact is present
- the next operation's expected path-level mutation is known
- rollback or revert handling is defined
- before/after evidence can identify exact mutations

### READY WITH CONDITIONS

Allowed only for a specifically bounded, low-risk, documentation-only or non-destructive operation where:

- all baseline exceptions are recorded
- execution scope is path-constrained
- unrelated dirty artifacts are excluded
- no hidden mutation can be mistaken for approved output

### NOT READY

Use when repository hygiene or artifact ownership must be improved first.

### SCW HOLD

Use when:

- unknown or unexpected mutation is material
- sensitive artifacts may be present
- ownership is disputed
- cleanup would be destructive
- repository state cannot be reconstructed confidently

---

## Required Review Questions

- What produced the majority of the 1924 entries?
- Which entries are tracked changes versus untracked artifacts?
- Which entries are canonical?
- Which entries are reproducible?
- Which entries are evidence?
- Which entries are temporary, debug, cache, or local runtime state?
- Which entries contain unique human work?
- Which entries belong to unfinished Q work?
- Which entries are legacy but still potentially valuable?
- Which entries are safe `.gitignore` candidates?
- Would any proposed ignore rule hide future unexpected mutation?
- Which generators should write outside the repository or into dedicated work paths?
- Are generated files deterministic?
- Are timestamps, ordering, absolute paths, or machine-specific values creating noise?
- Can the worktree become clean without losing required project history?
- If not immediately clean, what exact Expected Dirty baseline can be approved temporarily?
- What is the smallest safe first governed mutation after triage?
- What must be resolved before GameGhost adoption proof can begin?

---

## Deliverables

Produce at least:

- `request.md`
- `completion_report.md`
- `dirty_worktree_inventory.md`
- `dirty_state_policy.md`
- `dogfooding_entry_gate_report.md`
- baseline snapshot or documented snapshot reference
- improvement candidate list
- recommended follow-up Q list
- updated AI Repository Index
- updated Repository Quality Report

Suggested additional deliverables when useful:

- `.gitignore` recommendation report
- generation-path remediation plan
- legacy artifact disposition plan
- sensitive-artifact review report
- repository worktree health summary

Do not modify `.gitignore`, move files, delete files, commit files, or rewrite generation paths merely because they appear in a recommendation report unless the approved Q execution scope explicitly allows that action.

---

## Expected Follow-up Q Categories

Create separate follow-up Q candidates where needed.

Examples:

```text
Q_GG_GITIGNORE_HYGIENE_001
Q_GG_GENERATED_ARTIFACT_PATH_NORMALIZATION_001
Q_GG_CANONICAL_ARTIFACT_TRACKING_REVIEW_001
Q_GG_LEGACY_ARTIFACT_ARCHIVE_001
Q_GG_UNKNOWN_WORKTREE_ORIGIN_INVESTIGATION_001
Q_GG_FIRST_GOVERNED_MUTATION_DOGFOODING_001
```

Do not create all candidates automatically.

Create only those supported by evidence.

---

## Non-Goals

This Q must not:

- bulk-delete files
- bulk-stage files
- commit existing GameGhost changes
- push or tag
- normalize the repository by force
- classify unknown artifacts by guess
- ignore broad directories without authority review
- treat generated as synonymous with disposable
- treat untracked as synonymous with safe to delete
- treat tracked as synonymous with canonical
- rewrite GameGhost implementation
- perform the first governed mutation dogfooding
- declare Platform Foundation Release complete

---

## Safety and SCW Conditions

Immediately stop and report when:

- credentials, tokens, private keys, or secrets are detected
- user-authored data may be lost
- database files have unclear canonical status
- ignored paths may contain repository truth
- file ownership cannot be established
- current dirty changes overlap unrelated active work
- a proposed cleanup would alter runtime behavior
- broad path migration is required
- repository status changes during inspection without an approved action
- baseline counts or path sets change unexpectedly

Use:

```text
Stop
Call
Wait
```

No destructive action may proceed under ambiguity.

---

## Verification

At minimum:

- AI Repository Index validation
- Encoding Regression
- Repository Quality Audit
- `git diff --check`
- character corruption marker search
- before/after GameGhost worktree count
- before/after normalized path-set comparison
- confirmation that no unintended GameGhost mutation occurred
- confirmation that Commit / Push / Tag were not executed

Known LF conversion warnings must be reported separately from whitespace errors.

---

## Success Criteria

PASS when:

- the existing dirty worktree is meaningfully classified
- normal dirty-state policy is explicit
- CLEAN, EXPECTED DIRTY, and UNSAFE DIRTY are distinguishable
- canonical and non-canonical generated artifacts are distinguished
- `.gitignore` candidates are evidence-based
- generation-workflow problems are identified separately from cleanup
- unknown and unexpected items invoke SCW
- a reproducible baseline exists
- no unintended repository mutation occurs
- the next dogfooding gate decision is explicit
- follow-up actions are split into bounded Q candidates

PASS WITH LIMITATION may be used when classification is substantially complete but a bounded set of unresolved artifacts remains under explicit SCW or follow-up ownership.

---

## Repository Action Expectations

```text
GameGhost mutation:
Hold unless explicitly authorized by this Q

Commit:
Hold until Completion Review and human approval

Push:
Hold

Tag:
Hold
```

Any GDS or GameGhost documentation commit recommendation must remain separate from execution status.

---

## Priority

Highest

Required before the first governed mutating GameGhost dogfooding.

---

## Expected Completion Recommendation

The Completion Review should recommend one of:

```text
Proceed to first governed mutation dogfooding
Proceed after bounded hygiene follow-up
Continue classification
SCW investigation required
```

The answer must include a suggested next Q only when supported by the evidence collected.
