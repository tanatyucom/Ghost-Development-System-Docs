# GameGhost Workflow Profile

## Standard GameGhost AI Workflow

```text
Read GDS Index
  -> Read GDS Core Rules / Workflow
  -> Read GameGhost Project Profile
  -> Read Q File
  -> Startup Checklist
  -> Repository Root Validation
  -> Scope Guard
  -> Implementation / Review
  -> Verification
  -> Completion Report
  -> Completion Checklist
  -> Commit / Tag / Release Decision
```

## Repair / Cleanup Workflow

Use Audit Before Repair before changing source data, generated artifacts, OCR
results, DB files, metadata, duplicate records, or mojibake candidates.

```text
Issue
  -> Audit
  -> Classification
  -> Evidence
  -> Human Review
  -> Repair Q
  -> Verification
  -> Completion Report
```

## OCR / AI Output Workflow

For OCR, visual processing, AI recommendation, auto-detection, candidate
extraction, fuzzy matching, or title extraction:

```text
Phenomenon Check
  -> Metrics Check
  -> Human Review
  -> Debug Artifact Review, when needed
  -> Pipeline Trace
  -> First Broken Step
  -> Root Cause
  -> Fix / Tuning
```

Do not jump directly from a metric or symptom to algorithm change.

