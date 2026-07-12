# Platform Registry Update: Plugin Architecture Standard

## Summary

Plugin Architecture Standard を GDS Platform の標準 Architecture として追加します。

## Registry Change

- Standard Name: Plugin Architecture Standard
- Type: Architecture
- Previous Status: none
- New Status: Standard
- Origin: Plugin Architecture Standard and Roadmap Q
- First Introduced: 2026-07-12
- Last Updated: 2026-07-12
- Related Rule: `docs/rules/project_rules.md`
- Related Workflow: `docs/workflow/innovation_pipeline_workflow.md`
- Related Template: `templates/platform_registry_update_template.md`
- Related Report:
  `docs/requests/gds/draft/GDS-PLUGIN-ARCH-001_plugin_architecture_standard_and_roadmap/completion_report.md`
- Used By: GDS, GameGhost, AnimeGhost, ComicGhost, Future Ghost

## Required Artifacts

- `docs/architecture/plugin_architecture_standard.md`
- `roadmap/plugin_architecture_roadmap.md`
- `docs/architecture/platform_standard_registry.md`
- `docs/requests/gds/draft/GDS-PLUGIN-ARCH-001_plugin_architecture_standard_and_roadmap/request.md`
- `docs/requests/gds/draft/GDS-PLUGIN-ARCH-001_plugin_architecture_standard_and_roadmap/completion_report.md`

## Human Review

This update is created from a user-approved Q. Implementation remains out of
scope. Future runtime work requires a separate Q and Human Approval Gate.

## Notes

The standard explicitly rejects Folder Scan, Reflection Discovery, importlib
auto discovery, Entry Point Discovery, automatic plugin loading, Plugin GUI,
Launcher modification, and `tool.py` split for this phase.
