# Ghost Research

## Purpose

Ghost Research is the GDS Knowledge Asset for governed intake of external
engineering knowledge.

It records what was learned from OSS, frameworks, architectures, and
engineering practices, then evaluates which Ghost-native ideas may later become
Future Candidates, GG validation proposals, Platform Candidates, ADRs, or GDS
Standards.

## Entry Points

- Architecture standard:
  `docs/architecture/ghost_research_knowledge_asset.md`
- Workflow: `docs/workflow/ghost_research_workflow.md`
- Rules: `docs/rules/ghost_research_rules.md`
- Template: `templates/ghost_research_template.md`
- Examples: `examples/ghost_research_examples.md`
- Registry: `docs/research/research_registry.md`
- Initial example: `docs/research/GR-001_workflow_engines.md`

## Boundary

Ghost Research does not:

- authorize implementation;
- authorize dependency adoption;
- authorize source-code copying;
- directly create GDS Standards;
- bypass Future Candidate, Evidence, Platform Promotion, ADR, or Human Approval
  gates;
- replace Research Mission, ADR, Case, Improvement Record, or Q artifacts.

## Standard Flow

```text
External Source
  -> Ghost Research
  -> Future Candidate
  -> GG Validation
  -> Evidence
  -> Platform Candidate
  -> GDS Standard
```

## Registry Policy

`research_registry.md` is a lightweight index. The detailed Research asset is
the canonical source of truth.
