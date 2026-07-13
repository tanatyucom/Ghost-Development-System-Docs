# Platform First Migration Roadmap

Status: Draft Strategy
Date: 2026-07-13

## Purpose

This roadmap turns Platform First Migration Strategy into a staged sequence of
future Q files.

## Roadmap

| Phase | Q Candidate | Goal | Runtime Edit |
| --- | --- | --- | --- |
| 0 | GDS-PLATFORM-002 | Define migration strategy and priority | No |
| 1 | Q_GDS_Review_Center_Architecture_JP | Define Review Center platform / adapter architecture | No |
| 2 | Q_GDS_Review_Artifact_Schema_JP | Define review session / result / evidence schema | No |
| 3 | Q_GDS_GameGhost_Review_Adapter_Design_JP | Define GameGhost Steam OCR adapter boundary | No |
| 4 | Q_GameGhost_Review_Center_Compatibility_Prototype_JP | Prototype behavior-preserving adapter in GameGhost | Yes, separate Q |
| 5 | Q_GDS_Platform_Review_Center_Candidate_JP | Promote generic review contracts to platform candidate | Maybe, separate Q |
| 6 | Q_GDS_AnimeGhost_Bootstrap_Review_Check_JP | Validate that the platform model is not GameGhost-only | No |
| 7 | Q_GDS_Cross_Ghost_Review_Center_Validation_JP | Compare GameGhost / AnimeGhost / ComicGhost needs | No or separate prototype |
| 8 | Q_GameGhost_Review_Center_Legacy_Cleanup_JP | Remove duplicates after validated migration | Yes, separate Q |
| 9 | Q_GDS_Review_Center_Platform_Promotion_JP | Promote to Platform Standard if evidence supports it | No |

## Current Priority Guard

Current implementation focus remains:

```text
Complete GameGhost OCR Vertical Slice first.
```

After OCR:

- extract SDK requirements from real migration evidence;
- design SDK Foundation;
- formalize Project Adoption Model;
- issue Platform Foundation Release only after exit criteria are met.

## Project Adoption Candidate

Project Adoption is a post-OCR, post-SDK Foundation candidate.

Guiding statement:

```text
Improve Once, Adopt Many.
```

Ghost Projects should adopt formal GDS releases instead of every GDS commit.
Each project should eventually record the adopted GDS tag, commit hash,
adoption date, migration note, compatibility status, and hotfix adoption state.

This roadmap preserves the direction only. It does not finalize the manifest
schema or implement adoption validation.

## Priority Summary

P0:

- Review Center.

P1:

- Plugin Framework.
- Import Framework.
- Export Framework.

P2:

- Canonical Name Engine.
- Metadata Engine.
- Series Engine.

P3:

- Favorite Engine.
- Shared Utilities.

## Review Gate

Do not start GameGhost runtime edits before the Review Center Architecture Q is
approved.

Do not promote Review Center to Platform Standard until at least one non-GameGhost
compatibility review has been completed.

Do not formalize Project Adoption before OCR evidence has been reviewed and SDK
Foundation requirements have been extracted.
