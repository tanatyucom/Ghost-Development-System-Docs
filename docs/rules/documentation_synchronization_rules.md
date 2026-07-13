# Documentation Synchronization Rules

Q ID: GDS-DOCSYNC-001
Status: Standard
Date: 2026-07-13

## Purpose

Documentation Synchronization is the commit-before gate that checks whether
new or changed documentation is connected to the appropriate README, index,
completion checklist, completion report, AI Repository Index, and Repository
Quality Audit.

The purpose is to prevent repeated README update omissions, index update
omissions, and invisible documentation drift.

## Formal Definition

Documentation Synchronization means:

```text
Changed documentation
  -> matching README / index entry
  -> Completion Checklist synchronization section
  -> Completion Report synchronization section
  -> AI Repository Index regeneration / validation
  -> Repository Quality Audit
  -> git diff --check
```

## README Update Targets

Update or explicitly mark not required for:

- `README.md`
- `docs/README.md`
- folder README for the changed area
- `docs/rules/README.md` when rules change
- `docs/workflow/README.md` when workflows change
- `docs/architecture/README.md` when architecture changes
- `examples/README.md` when examples change
- `templates/README.md` when templates change
- `roadmap/README.md` when roadmap changes
- `docs/health/README.md` when health documents change
- `docs/knowledge/README.md` when knowledge documents change
- `registry_updates/README.md` when registry update storage rules change

## Completion Checklist Rule

Completion Checklist must include Documentation Synchronization status when a
task creates, moves, renames, or materially changes Markdown documents.

Required checklist fields:

- README / index update required.
- README / index update completed.
- Folder README checked.
- Root README checked.
- `docs/README.md` checked.
- AI Repository Index regenerated.
- AI Repository Index validated.
- Repository Quality Audit executed.
- Documentation Synchronization Gate passed.
- Not required reason.

## Completion Report Rule

Completion Report must include Documentation Synchronization Review when a
task affects public documentation entry points.

Required report fields:

- Documentation Synchronization required.
- README / index entry points updated.
- README / index entry points intentionally not updated.
- AI Repository Index result.
- Repository Quality Audit result.
- Remaining synchronization gaps.

## Repository Quality Gate

Repository Quality Audit must include a Documentation Synchronization Gate.

The gate checks:

- synchronization rule exists;
- synchronization workflow exists;
- completion checklist includes synchronization fields;
- completion report template includes synchronization review;
- root README and docs README expose the gate;
- AI Repository Index contains the synchronization rule / workflow;
- Repository Quality Report includes synchronization gate result.

## README Reference Validation

When a new public documentation standard is added, the author must check:

- Is the document reachable from a top-level or folder README?
- Is the document reachable through `docs/README.md` or an appropriate folder
  index?
- Is the document included in AI Repository Index after regeneration?
- Does Repository Quality Audit remain Green?

This validation is a required completion gate, not a background job.

## AI Repository Index Integration

If public Markdown files are created, moved, renamed, or materially changed:

```text
python scripts/generate_ai_repository_index.py --write
python scripts/generate_ai_repository_index.py --validate
```

must be run before completion unless the Completion Report explains why it is
not required.

## Commit Block Conditions

Do not approve commit when:

- a new public rule / workflow / architecture / template / example lacks the
  matching README entry;
- AI Repository Index regeneration is required but not run;
- Repository Quality Audit reports synchronization error;
- Completion Checklist omits synchronization status;
- Completion Report omits synchronization review;
- changed documentation has no discoverable entry point and no not-required
  reason.

## Legacy README Handling

Legacy README files may remain imperfect if:

- the current task did not touch their area;
- a follow-up Q is recorded;
- Repository Quality Audit remains Green or the warning is documented;
- no new public entry point is hidden by the legacy state.

Do not silently rewrite large legacy README files only to satisfy this rule.

## Future Auto Sync

Future automation may:

- inspect changed Markdown paths;
- infer likely README targets;
- propose README snippets;
- detect missing index entries;
- check AI Repository Index freshness;
- suggest registry update artifacts.

Automation must not auto-promote, auto-commit, or silently rewrite README files
without Human Approval.

## Related Documents

- `docs/workflow/documentation_synchronization_workflow.md`
- `templates/completion_checklist_template.md`
- `templates/completion_report_template.md`
- `scripts/repository_quality_audit.py`
- `docs/ai_repository_index.md`

