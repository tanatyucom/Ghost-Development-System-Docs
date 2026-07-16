# Metadata Center ADR Adoption

## Purpose

This document records the adoption result for Metadata Center architecture.

## Adoption Result

- ADR Status: Accepted.
- Architecture Status: Core architecture direction.
- Implementation Status: Not implemented by this ADR.
- Vertical Slice: Approved as future validation work.
- SDK Extraction: Future candidate only.

## Adopted Architecture Statement

Metadata Center is the canonical GDS architecture direction for Ghost Platform
metadata coordination.

It coordinates provider selection, identity resolution, confidence evaluation,
registry boundaries, adapter-mediated source access, and human review queue
coordination.

## Adopted Boundaries

Metadata Center owns coordination.

Engines own reusable logic.

Registries own reviewable records.

Adapters own provider-specific and project-specific behavior.

Human Review owns approval for ambiguous or risky metadata decisions.

## Explicit Non-Approvals

This adoption does not approve:

- runtime implementation;
- SDK extraction;
- GameGhost source migration;
- metadata write;
- DB write;
- provider API implementation;
- automatic repair;
- Human Review bypass;
- production entry point changes;
- commit or push.

## Required Future Work

Future work must use separate Q artifacts for:

- Metadata Center vertical slice;
- provider adapter validation;
- Identity Engine validation;
- confidence contract validation;
- metadata registry design;
- SDK evidence extraction;
- platform promotion review.

## Review Decision

`ADR_ACCEPTED_ARCHITECTURE_DIRECTION_CORE_IMPLEMENTATION_NOT_STARTED`
