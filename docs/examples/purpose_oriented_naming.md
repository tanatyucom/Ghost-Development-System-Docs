# Purpose-Oriented Naming Examples

## Purpose

This example shows how to name roadmap items and public knowledge base topics by
purpose before implementation method.

Purpose-oriented naming keeps roadmap items stable when implementation details
change.

## Rule Of Thumb

Use the public title for the outcome.

Use the body for the current implementation.

## Example 1: Legacy Play History

Before:

```text
Nintendo 3DS Activity Log Parser
```

After:

```text
Legacy Play History Recovery
```

Why:

The goal is not only to build a Nintendo 3DS parser. The goal is to recover
historical play records from legacy platforms using the best available method.

Current Targets / Current Implementations:

- Nintendo 3DS Activity Log / metadata research.
- Switch OCR / screenshots.
- FF11 / FF14 historical recovery.
- Steam / PSN / Console CSV recovery.
- Manual recovery where automated sources are unavailable.

## Example 2: OCR Implementation

Before:

```text
Switch Screenshot OCR Script
```

After:

```text
Switch Play Record Recovery
```

Why:

OCR may be the current method, but future work may use metadata, API exports,
manual correction, or another acquisition path.

## Example 3: Database Tooling

Before:

```text
SQLite Migration Script
```

After:

```text
Database Compatibility Migration
```

Why:

The purpose is compatibility and safe migration. The implementation may use a
script, manual review, schema helper, or future Database Utility Framework.

## Example 4: Documentation Tooling

Before:

```text
Markdown Link Checker
```

After:

```text
Documentation Health Check
```

Why:

Broken links are one check. Documentation health may also include duplicate
pages, missing examples, outdated roadmap references, or inconsistent naming.

## Checklist

Before accepting a public name, ask:

- Does the title describe the outcome?
- Is the title broader than one implementation technique?
- Can current implementation details move into the body?
- Would the title still make sense if the method changes later?
- Does the name help humans and AI understand the purpose quickly?
