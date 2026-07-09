# PIP Investigations

## Purpose

Investigation entries preserve reusable investigation methods before they become CASE, Rule Story, Best Practice, or Workflow.

They are used when the main value is the investigation approach itself: what to inspect, in what order, and which evidence separates one failure mode from another.

## Expected Content

- Investigation ID
- Title
- Related Case
- Related Q
- Related Report
- Evidence Entry Point
- Investigation Steps
- First Broken Step Criteria
- Validation Criteria
- Promotion Candidate

## Standard Template

Use:

```text
pip/templates/investigation_pattern_template.md
```

The standard investigation flow is:

```text
Symptom
  -> Hypothesis
  -> Rejected Hypothesis
  -> New Hypothesis
  -> Evidence
  -> First Broken Step
  -> Root Cause
```

## Current Source

- `pip/MASTER_DOCUMENT_JP.md`
- `pip/MASTER_TITLE_LIST_JP.md`
- `pip/investigations/investigation_candidates_from_master_title_list.md`
- `pip/investigations/investigation_candidates_from_roadmap2_salvage.md`
