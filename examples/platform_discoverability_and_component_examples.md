# Platform Discoverability and Component Examples

## Purpose

This document shows good and bad examples for Platform folder placement,
component naming, and Review Center migration decisions.

## Good Example: Review Center Split

```text
platform/
  review/
    review_center_gui.py
    review_session_service.py
    review_result_schema.py
  adapters/
    gameghost_steam_ocr_review_adapter.py
```

Why this is good:

- generic review behavior is under `platform/review/`;
- GameGhost-specific OCR behavior is isolated in an adapter;
- filenames explain responsibility;
- future AnimeGhost / ComicGhost review flows can reuse the review center.

## Bad Example: Project-Specific Platform Code

```text
platform/
  review/
    steam_ocr_review_center.py
    steam_title_matcher.py
```

Why this is bad:

- platform folder contains GameGhost-specific nouns;
- future Ghost projects cannot tell what is reusable;
- adapter responsibility is hidden in platform code.

## Good Example: Engine / Service Split

```text
platform/
  engines/
    title_match_engine.py
  services/
    review_session_service.py
  schemas/
    review_result_schema.py
```

Why this is good:

- engine owns processing logic;
- service coordinates a bounded use case;
- schema owns the data contract.

## Bad Example: Shared Dumping Ground

```text
platform/
  shared/
    utils.py
    common.py
    helper.py
```

Why this is bad:

- responsibility is not discoverable;
- review cannot identify owner or boundary;
- policy can hide inside generic helpers.

## Good Example: Plugin Naming

```text
plugins/
  repository_context_validation/
    README.md
    plugin.py
    tests/
```

Why this is good:

- plugin id is stable;
- folder explains purpose;
- contract can follow Plugin Architecture Standard.

## Bad Example: Hidden Auto Discovery

```text
plugins/
  random_checker.py
  load_me.py
```

Why this is bad:

- plugin identity is unclear;
- registry boundary is missing;
- side effects cannot be reviewed.

## Good Example: Migration Candidate

GameGhost has a useful human review UI. It becomes a Platform migration
candidate only after:

- generic review responsibility is separated;
- GameGhost-specific OCR adapter is identified;
- target folder is agreed;
- verification is defined;
- Human Approval is recorded.

## Bad Example: Premature Migration

Moving all GameGhost review code to Platform because it worked once is not
acceptable.

Risks:

- project-specific assumptions become platform policy;
- future Ghost projects inherit wrong names;
- hidden data dependencies become harder to fix.

