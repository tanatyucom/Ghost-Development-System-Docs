# Ghost Research Validation Cases

## Purpose

This attachment records the required validation cases for
`GDS-GHOST-RESEARCH-KNOWLEDGE-ASSET-STANDARDIZATION-001`.

Canonical reusable examples:

- `examples/ghost_research_examples.md`
- `docs/research/GR-001_workflow_engines.md`

## Cases

| Case | Scenario | Expected Result | Covered By |
| --- | --- | --- | --- |
| 1 | Research produces one Candidate | Research completes, one Future Candidate is linked, no direct GDS Standard promotion. | `ghost_research_examples.md` |
| 2 | Research produces multiple decisions | Idea-level decisions such as Accepted, Pending Validation, Deferred, and Rejected are supported. | `ghost_research_examples.md`, `GR-001` |
| 3 | Research produces no Candidate | `Research Only` or `Rejected` preserves knowledge without forcing a Candidate. | `ghost_research_examples.md` |
| 4 | Duplicate Future Candidate | Decision is `Merged into Existing Candidate`; duplicate is not created. | `ghost_research_examples.md` |
| 5 | GG Validation required | Decision is `Pending Validation`; separate GG Q recommended; no implementation authorization. | `ghost_research_examples.md`, `GR-001` |
| 6 | GG Validation fails | Negative Evidence is retained; Candidate Deferred or Rejected; Research preserved. | `ghost_research_examples.md` |
| 7 | Platform Promotion | Future Candidate and Evidence exist before Platform Candidate creation. | `ghost_research_examples.md` |
| 8 | ADR creation | ADR references Research and Evidence while Research remains learning record. | `ghost_research_examples.md` |
| 9 | Partial adoption | Useful and unsuitable ideas can receive different decisions. | `ghost_research_examples.md`, `GR-001` |
| 10 | Source attribution | Source identity, review date, fact, interpretation, proposal, validation, and decision are separated. | `ghost_research_examples.md`, `GR-001` |
| 11 | Copying boundary | Research does not authorize source-code copying or dependency adoption. | `ghost_research_examples.md`, rules |
| 12 | Stale Research | Research is marked for re-review when source or GDS architecture changes. | `ghost_research_examples.md` |
| 13 | Superseded Research | Stable IDs retained; old Research marked `Superseded`; links preserved. | `ghost_research_examples.md` |
| 14 | Repository Intelligence input | Research metadata can be indexed conceptually; no automation implemented. | architecture and registry |
| 15 | UTF-8 verification | Use `Get-Content -LiteralPath <path> -Encoding UTF8` before declaring mojibake. | `ghost_research_examples.md` |

## Review Result

All required cases are represented by the example file, the initial GR-001
asset, and the Ghost Research architecture / rule documents.
