# AI Collaboration Rules

**Version:** 2.3

**Last Updated:** 2026-07-05

## Purpose

This document defines how humans and AI collaborate on Ghost Development System
Docs.

## Collaboration Philosophy

### Human Leads

Humans approve goals, architecture, scope, naming, release decisions, and
destructive changes.

### AI Is A Partner

AI helps draft, review, compare, summarize, and propose improvements. AI should
improve quality, not replace human judgment.

### Evidence First

AI should base suggestions on visible documents, known rules, reviewed
decisions, and explicit user requests.

### Knowledge Must Be Written Down

Reusable learning should move into rules, templates, roadmap, workflow, or
architecture documents. It should not remain only in conversation.

### Artifact First

Reusable AI requests, long review prompts, Q files, design documents,
specifications, and roadmap update proposals should be generated as managed
file artifacts before execution or review.

AI should summarize the artifact in chat and provide the file path or link
instead of making the chat body the authoritative copy.

### Debug Artifact Review

For AI, OCR, recommendation, auto-detection, candidate extraction, fuzzy
matching, and visual processing work, AI should make intermediate behavior
inspectable during development.

AI should name debug artifact paths, expected normal state, review viewpoints,
and future AI review targets when Debug Mode applies.

AI should not generate debug artifacts during normal execution unless Debug
Mode is explicitly requested.

### Audit Before Repair

Before repair, cleanup, OCR result correction, DB correction, mojibake
correction, duplicate resolution, metadata correction, or other repair work, AI
should request or perform an audit step first.

AI should classify findings as `fix_candidate`, `needs_human_review`,
`generated_artifact`, `raw_data`, or `false_positive`, then create a scoped
repair Q that names the source audit artifact, exclusions, verification method,
safe commit set, and restore guidance.

AI should not broad-fix raw data, generated artifacts, OCR evidence, DB files,
or unrelated dirty workspace files without explicit human approval.

## AI Responsibilities

AI may:

- review documentation structure;
- draft and revise Markdown;
- generate Markdown and `.docx` artifacts for reusable requests or human
  review packets;
- identify missing related updates;
- propose future candidates;
- suggest commit messages;
- summarize changes;
- recommend next Q files.
- prepare future AI review handoff by listing the debug artifacts and review
  questions when intermediate evidence is needed.
- prepare audit-first repair handoff by listing source audit artifacts,
  classifications, excluded items, and remaining candidates.

AI must not:

- perform runtime implementation during documentation-only work;
- migrate repositories unless explicitly requested;
- commit unless explicitly requested;
- bypass Human Approval Gate;
- treat Future Candidates as approved implementation.
- hide uncertain intermediate behavior behind a final summary when debug
  artifacts are needed for review.
- repair broad or uncertain targets before audit, classification, evidence
  review, and required human approval.

## Multi-AI Collaboration

Different AI tools may be used for different strengths, but all AI output must
remain reviewable by humans.

Cross-review is recommended for:

- architecture boundaries;
- roadmap direction;
- public terminology;
- major rule changes;
- reusable templates.

## Communication Rules

AI should report:

- changed files;
- what changed;
- verification performed;
- debug artifact review performed, when applicable;
- audit before repair performed, when applicable;
- remaining issues;
- future candidates;
- recommended next Q;
- suggested commit message.

## Goal

The goal is a durable collaboration system where humans and AI share the same
knowledge base, reduce repeated mistakes, and improve the archive over time.
