# Knowledge Before Automation Example

## Purpose

This example shows how to handle an automation failure by building reusable
knowledge before adding more automation complexity.

## Principle

When automation fails, first ask:

```text
What knowledge is missing?
```

Then decide whether that knowledge should become a reviewed asset such as an
Alias, Metadata entry, Rule, Example, Review Report, or Knowledge Base update.

## Bad Example

```text
OCR failure
  -> add AI judgment
  -> add another AI judgment
  -> add more OCR profiles
  -> add hidden exceptions
  -> system becomes harder to review
```

Why this is weak:

- The same failure can repeat because no reusable knowledge was captured.
- Human judgment is hidden inside automation.
- Future projects cannot reuse the learning.
- Debugging becomes harder because the system has more moving parts but not
  more explicit knowledge.

## Good Example

```text
OCR failure
  -> Review
  -> Alias Candidate
  -> Review GUI
  -> Human Approval
  -> Knowledge
  -> Alias / Metadata / Rule
  -> next run succeeds automatically
```

Why this is stronger:

- The system learns a stable fact.
- Human approval is explicit.
- Future automation can reuse the approved knowledge.
- The same pattern can be reused by GameGhost, AnimeGhost, ComicGhost, and new
  archive projects.

## GameGhost OCR Reference

GameGhost OCR improvement initially considered adding more OCR profiles.

Measured work showed that many failures were not primarily OCR engine failures.
They were missing knowledge:

- approved aliases;
- metadata comparison rules;
- safe alias classification;
- review reports;
- Unicode comparison behavior;
- human approval state.

The improvement path became:

```text
OCR
  -> Alias Candidate
  -> Review GUI
  -> Human Approval
  -> Knowledge
  -> next OCR import can resolve the title
```

This did not remove the need for automation. It made automation better by
giving it reviewed knowledge to consume.

## Portable Pattern

Use this pattern for other projects:

```text
Failure
  -> identify missing knowledge
  -> make review visible
  -> get human approval when needed
  -> store the approved knowledge
  -> let automation consume it
```

Examples:

- AnimeGhost: episode title mismatch becomes an approved title alias or source
  rule.
- ComicGhost: volume naming mismatch becomes a metadata rule.
- Future project: import ambiguity becomes an approved mapping, not a hidden
  prompt exception.
