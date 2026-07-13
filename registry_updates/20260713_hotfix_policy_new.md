# Platform Registry Update: Hotfix Policy

## Identity

- Date: 2026-07-13
- Update Type: New Standard
- Standard Name: Hotfix Policy
- Source Q: `docs/requests/gds/draft/GDS-PARKING-LOT-001_candidates_promotion/request.md`
- Related Completion Report: `docs/requests/gds/draft/GDS-PARKING-LOT-001_candidates_promotion/completion_report.md`

## Registry Change

Add Hotfix Policy as a Standard rule.

## Registry Entry Summary

- Type: Rule
- Status: Standard
- Related Rule: `docs/rules/hotfix_policy_rules.md`
- Related Workflow: `docs/workflow/completion_checklist_workflow.md`
- Related Template: `templates/completion_report_template.md`
- Used By: GDS, GameGhost, AnimeGhost, ComicGhost, Future Ghost

## Reason

GDS needs an official policy that separates defect correction from normal
platform improvement.

## Standard Statements

```text
Hotfix = defect correction in an existing GDS asset
Normal Release = new capability or improvement
```

```text
Fix Once, Recover Everywhere.
```

## Scope Guard

This update does not create a release tag, implement automatic hotfix
distribution, edit GameGhost, or define the final Project Manifest schema.

## Verification

Repository validation is recorded in the related Completion Report.
