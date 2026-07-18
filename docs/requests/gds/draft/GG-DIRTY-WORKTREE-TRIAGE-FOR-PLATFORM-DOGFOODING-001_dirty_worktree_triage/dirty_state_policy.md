# GameGhost Dirty-State Policy For Governed Platform Dogfooding

## Policy Result

GameGhost should target:

```text
Clean by default
```

Allowed exception:

```text
Expected Dirty
```

Expected Dirty is temporary, explicit, path-bounded, owner-assigned, and
reviewed. It is not a permanent substitute for repository hygiene.

The current GameGhost state is:

```text
UNSAFE DIRTY
```

## State Definitions

## CLEAN

Use `CLEAN` when all are true:

- no tracked mutation;
- no untracked artifact requiring review;
- no unknown-origin artifact;
- no sensitive-risk artifact;
- no unexplained deletion;
- no pending generated output in repository root;
- repository health can identify a new mutation by path identity.

This is the preferred entry state for mutating dogfooding.

## EXPECTED DIRTY

Use `EXPECTED DIRTY` only when every dirty item is:

- explicitly identified;
- tied to a known Q, workflow, or owner;
- bounded by exact path or narrow pattern;
- assigned planned disposition;
- recorded in a baseline snapshot;
- not sensitive;
- not authority-ambiguous;
- not mixed with unrelated unknown work;
- time-limited.

Expected Dirty must include:

```text
Expected Dirty ID:
Owner:
Allowed paths:
Forbidden paths:
Source Q / workflow:
Reason:
Expiration / next review:
Baseline fingerprint:
Allowed next operation:
Blocked operation:
```

## UNSAFE DIRTY

Use `UNSAFE DIRTY` when one or more are present:

- unknown origin;
- unexpected mutation;
- ambiguous authority;
- sensitive or credential-risk artifact;
- unexplained tracked modification;
- unexplained tracked deletion;
- unbounded generated output;
- mixed unrelated scope;
- incomplete baseline evidence;
- cleanup would be destructive or could lose unique human work.

Unsafe Dirty requires:

```text
SCW
Stop -> Call -> Wait
```

Mutating dogfooding is blocked.

## Artifact Retention Rules

## Ignore Candidate

Use `.gitignore` only when all are true:

- artifact is non-canonical;
- artifact is reproducible or disposable;
- artifact is not review or historical evidence;
- artifact contains no unique human-authored data;
- artifact contains no credentials or sensitive material;
- ignore rule is narrow enough not to hide future canonical or unexpected
  mutation.

Candidate examples from current inventory:

- `tmp_pycache*/`
- `codex_pycache*/`
- `*.pyc`

No ignore rule was applied in this Q.

## Keep In Git

Keep in Git when one or more are true:

- repository truth;
- approved canonical dataset;
- governed evidence;
- required review artifact;
- intentional migration result;
- release or adoption proof;
- loss would prevent reconstruction of approved project state.

Candidate examples requiring review:

- OCR montage images in repository root;
- GDS review package artifacts;
- approved Steam OCR archive outputs, if any are canonical;
- stable datasets or generated indexes, if approved.

## Archive Or Migrate

Use archive or migration when:

- artifact is legacy but potentially valuable;
- artifact belongs to older repository layout;
- artifact needs historical preservation but not active root visibility;
- artifact is too large or broad for normal working tree health.

Candidate examples:

- `GrayGhost_backup/**`
- `backups/**`
- deleted root legacy files, if superseded but historically relevant.

## SCW Required

Use SCW when:

- `.env` or other sensitive candidate is dirty;
- producer / owner is unknown;
- tracked deletion has unclear canonical status;
- database file status is unclear;
- cleanup would change runtime behavior;
- ignore rule could hide future repository truth.

## Recommended Directory Model

GameGhost may converge toward:

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

Candidate tracking policy:

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

This is a candidate policy only. Existing GameGhost architecture and canonical
ownership must be reviewed before migration.

## Current GameGhost Policy Decision

| Area | Decision |
| --- | --- |
| Current dirty state | `UNSAFE DIRTY` |
| Mutating dogfooding | Blocked |
| Documentation-only GDS evidence commit | Allowed after human review |
| GameGhost cleanup | Separate Q required |
| GameGhost `.gitignore` update | Separate Q required |
| GameGhost tracked deletion handling | Separate owner review required |
| `.env` handling | Sensitive SCW review required |

## Smallest Safe Next Step

The smallest safe next step is not cleanup. It is owner-reviewed hygiene
planning:

```text
Q_GG_GITIGNORE_HYGIENE_AND_CACHE_OUTPUT_CONTAINMENT_001
```

or, if tracked changes must be resolved first:

```text
Q_GG_TRACKED_CHANGE_OWNER_REVIEW_001
```
