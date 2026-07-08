# PIP Case Index

## Purpose

この文書は、PIP に保存する改善事例の検索入口です。

PIP Case は単なる作業ログではありません。再利用できる失敗パターン、調査手順、レビュー方法、予防知識を、後から人間と AI が短時間で参照できるようにするための Knowledge Base entry です。

## Source Evidence

- `PIP_v1.0_stable.zip`
- `GDS_PIP_v1.1_delta_package_20260708.zip`
- `GDS_PIP_Master_JP_Package_v1.0.zip`
- `MASTER_DOCUMENT_JP.md`
- `MASTER_TITLE_LIST_JP.md`

## Standard Case Location

PIP Case は次の場所に保存します。

```text
pip/cases/
```

Rule Story、Evolution、Best Practice、Template は次の場所に保存します。

```text
pip/rule_stories/
pip/evolutions/
pip/best_practices/
pip/investigations/
pip/templates/
```

## Search Keys

Case Index は、少なくとも次の軸で検索できるようにします。

- Project
- Category
- Methodology
- Priority
- Lifecycle
- Related Rule
- Related PIP

Tag の正式な値は `tagging_standard.md` に従います。

## Master Document Entry Point

Roadmap2-derived GDS / PIP methodology starts here:

- `MASTER_DOCUMENT_JP.md`
- `MASTER_TITLE_LIST_JP.md`

Classification candidate lists:

- `cases/case_candidates_from_master_title_list.md`
- `best_practices/best_practice_candidates_from_master_title_list.md`
- `evolutions/evolution_candidates_from_master_title_list.md`
- `investigations/investigation_candidates_from_master_title_list.md`
- `rule_stories/rule_story_candidates_from_master_title_list.md`

## Case Index

| Case ID | Title | Project | Category | Methodology | Priority | Lifecycle | Related Rule |
|---|---|---|---|---|---|---|---|
| CASE-0001 | Steam OCR Target Row Tracing | Steam | OCR, Debug, Review | Trace Before Tune, First Broken Step, Pipeline Trace | P1 | Standardized | Debug Artifact Review |
| CASE-0002 | Too Many Artifacts / Review Entry Point | GDS | Review, Workflow, Rule | Review Entry Point, Human Review | P1 | Standardized | Review Entry Point |
| CASE-0003 | Metrics Passed But Visual Containment Failed | Steam | OCR, Review | Human Review, Audit Before Repair | P1 | Validated | Human Visual Review |
| CASE-0004 | Target Row Identity Drift | Steam | OCR, Pipeline | First Broken Step, Pipeline Trace | P1 | Validated | Trace Before Tune |
| CASE-0005 | Title BBox Was The First Broken Step | Steam | OCR, Debug | First Broken Step, Trace Before Tune | P1 | Validated | Debug Artifact Review |
| CASE-0006 | Debug Escalation Ladder | GDS | Debug, Review, Pipeline | Trace Before Tune, First Broken Step, Pipeline Trace | P1 | Standardized | Debug Escalation Ladder |

## Candidate Index From Master Title List

| Type | File |
|---|---|
| CASE Candidates | `cases/case_candidates_from_master_title_list.md` |
| Best Practice Candidates | `best_practices/best_practice_candidates_from_master_title_list.md` |
| Evolution Candidates | `evolutions/evolution_candidates_from_master_title_list.md` |
| Investigation Candidates | `investigations/investigation_candidates_from_master_title_list.md` |
| Rule Story Candidates | `rule_stories/rule_story_candidates_from_master_title_list.md` |

## Steam OCR v2 Debugging Sequence

### Metrics Said Single Row, Human Saw Two Rows

Summary:

Automated geometry metrics reported a single-row condition, but human visual review found two-row mixing.

Reusable Lesson:

Metrics can pass while visual containment fails. Visual containment must be reviewed with contact sheets or overlays when row boundaries matter.

Related Methodology:

- Human Visual Review
- Evaluate What Actually Matters
- Review Entry Point

### Root Cause Was The Algorithm

Summary:

OCR failure was traced back to row boundary algorithm assumptions rather than only OCR recognition quality.

Reusable Lesson:

When downstream output is wrong, trace the pipeline before tuning parameters.

Related Methodology:

- Trace Before Tune
- First Broken Step
- Target Row Trace / Pipeline Trace

### Good Crop Score But Text Was Missing

Summary:

Crop quality scoring selected a candidate that could still miss the actual title text.

Reusable Lesson:

A metric must evaluate the real quality target, not a proxy that accidentally passes.

Related Methodology:

- Evaluate What Actually Matters
- Human Visual Review
- Review Entry Point

### Target Row Identity Drift

Summary:

The target row identity drifted before crop, bbox, or OCR. Downstream steps then worked on a confused target.

Reusable Lesson:

Target row identity must be traced before judging crop, bbox, or OCR quality.

Related Methodology:

- First Broken Step
- Target Row Trace / Pipeline Trace
- Trace Before Tune

### First Broken Step Was Title BBox

Summary:

Target Row Tracing identified rows where the first broken step was Title Text BBox, plus rows where Target Row Identity broke first.

Reusable Lesson:

Title bbox and target row identity should be separated in review. Fixing OCR or crop scoring first can hide the actual break point.

Related Methodology:

- First Broken Step
- Trace Before Tune
- Review Entry Point

## New Case Entry Checklist

When adding a PIP Case:

- Create a file under `pip/cases/`.
- Use `pip/templates/case_template.md`.
- Fill all required metadata fields.
- Add tags from `tagging_standard.md`.
- Add or update this Case Index.
- Link related Q, completion report, rule, PIP section, and related cases when available.

## Future Use

Future PIP template work should preserve the Case Index, standard metadata, tag search axes, and CASE template so that PIP remains a reusable improvement knowledge database.
