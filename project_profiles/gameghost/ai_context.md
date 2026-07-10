# GameGhost AI Context

## Purpose

This context helps AI avoid confusing GDS shared documentation work with
GameGhost runtime implementation.

## Stable Context

GameGhost is a field project supported by Ghost Development System.

GDS may define shared development rules, workflow, templates, review methods,
and knowledge promotion. GameGhost keeps ownership of project-specific runtime
behavior, schema, metadata, import rules, GUI behavior, OCR behavior, reports,
and release decisions.

## AI Expectations

Before GameGhost work, AI should know:

- which repository is editable;
- whether GameGhost is production, backup, or reference-only;
- whether the Q is documentation-only or runtime implementation;
- whether generated artifacts are in scope;
- whether human review is required;
- whether commit, tag, or release is requested.

## Common Risk Areas

- Editing GDS Docs when the Q targets GameGhost.
- Editing GameGhost when the Q is GDS documentation-only.
- Treating generated OCR or debug outputs as safe commit files.
- Treating metric success as human approval.
- Changing production logic during investigation.
- Skipping repository root validation.

## Required Honesty

If AI cannot read the target repository, target Q, Project Profile, or required
artifact, it should report the missing input instead of guessing.

