# CASE Candidates From Master Title List

## Source

- `pip/MASTER_DOCUMENT_JP.md`
- `pip/MASTER_TITLE_LIST_JP.md`

## Candidates

| Candidate | Project | Category | Methodology | Priority | Lifecycle |
|---|---|---|---|---|---|
| Trace Before Tune | GDS | Debug, Pipeline, Review | Trace Before Tune | P1 | Standardized |
| First Broken Step | GDS | Debug, Pipeline, Review | First Broken Step, Pipeline Trace | P1 | Standardized |
| Target Row Identity Drift | Steam | OCR, Debug, Pipeline | First Broken Step, Pipeline Trace | P1 | Validated |
| Good Crop Score But Text Was Missing | Steam | OCR, Review | Human Review, Review Entry Point | P1 | Validated |
| Metrics Said Single Row, Human Saw Two Rows | Steam | OCR, Review | Human Review, Review Entry Point | P1 | Validated |
| Review Entry Point Rule | GDS | Review, Workflow, Rule | Review Entry Point, Human Review | P1 | Standardized |
| Too Many Artifacts | GDS | Review, Workflow | Review Entry Point, Human Review | P1 | Validated |
| Evaluate What Actually Matters | GDS | Review, Pipeline | Human Review, Pipeline Trace | P1 | Standardized |
| Debug Escalation Ladder | GDS | Debug, Review, Pipeline | Trace Before Tune, First Broken Step, Pipeline Trace | P1 | Standardized |

## Promotion Rule

Promote a candidate into a full CASE only after it has a source Q, completion report, evidence link, and validation note.
