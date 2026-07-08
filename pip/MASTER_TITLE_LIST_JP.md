# GDS / PIP Master Title List v1.0 JP

## Purpose

この文書は、Roadmap2 で発生した Steam OCR v2 調査・改善・PIP 化の知識タイトル群です。

各項目は、今後次のいずれかへ昇格できます。

- CASE
- Best Practice
- Evolution
- Investigation
- Rule Story
- Workflow
- Template

## 1. Steam OCR v2

- Row Boundary Tuning
- Title Start Offset Tuning
- Title Cell Evaluation & Adoption
- Final Validation
- P1 Title Cell Review
- Crop Geometry Review
- Row Boundary Geometry Review
- Row Boundary Candidate Adoption
- Visual Containment Review
- Visual Band Adoption Review
- Adaptive Crop Quality Review
- Adaptive Crop Root Cause Investigation
- Target Row Tracing Audit
- Tight Title BBox Trace
- Tight Title BBox Human Review

## 2. Debug / Investigation

- Row Boundary Investigation
- Geometry Investigation
- Center Comparison
- Icon Center Validation
- Text Activity Center Validation
- Target Row Identity Audit
- Title BBox Audit
- Crop Containment Audit
- Pipeline Trace
- First Broken Step Analysis

## 3. PIP / GDS Principles

- Trace Before Tune
- First Broken Step
- Target Row Identity Drift
- Good Crop Score But Text Was Missing
- Metrics Said Single Row, Human Saw Two Rows
- Human Visual Review Can Override Automated Geometry Metrics
- Separate Visual Containment from OCR Score
- Separate Center Detection from Band Selection
- Fix Identity Before Crop
- End-to-End Traceability
- Review Entry Point Rule
- Too Many Artifacts
- Start With Human-Readable Artifact
- Evaluate What Actually Matters

## 4. Evolution

```text
Activity Extent
  -> Row Center / Pitch
  -> Visual Band
  -> Adaptive Crop
  -> Target Row Trace
  -> Tight BBox
```

## 5. Recommended Classification

### CASE Candidates

- Trace Before Tune
- First Broken Step
- Target Row Identity Drift
- Good Crop Score But Text Was Missing
- Metrics Said Single Row, Human Saw Two Rows
- Review Entry Point Rule
- Too Many Artifacts
- Evaluate What Actually Matters

### Best Practice Candidates

- Human Visual Review Can Override Automated Geometry Metrics
- Separate Visual Containment from OCR Score
- Separate Center Detection from Band Selection
- Fix Identity Before Crop
- End-to-End Traceability
- Start With Human-Readable Artifact

### Evolution Candidates

- Activity Extent -> Row Center / Pitch -> Visual Band -> Adaptive Crop -> Target Row Trace -> Tight BBox

### Investigation Candidates

- Row Boundary Investigation
- Geometry Investigation
- Center Comparison
- Icon Center Validation
- Text Activity Center Validation
- Target Row Identity Audit
- Title BBox Audit
- Crop Containment Audit
- Pipeline Trace
- First Broken Step Analysis

### Rule Story Candidates

- Trace Before Tune
- First Broken Step
- Review Entry Point Rule
- Human Visual Review Can Override Automated Geometry Metrics
- Evaluate What Actually Matters
- End-to-End Traceability
