# Notes: Product Documentation Hierarchy v2

## Source

- Original Q: `C:/Users/tanat/Downloads/Q_GDS_Product_Document_Hierarchy_v2_JP.md`
- Workspace copy: `request.md`

## Design Decision

Product Documentation Hierarchy v2 is implemented as an architecture standard
because it defines document responsibilities and decision boundaries.

Primary document:

- `docs/architecture/product_document_hierarchy_v2.md`

## Migration Approach

Existing roadmap files are not moved in this Q.

Migration strategy:

1. Classify existing roadmap content into Blueprint / Master / Domain /
   Execution / Decision / Q.
2. Keep current roadmap files as authoritative during transition.
3. Apply the new hierarchy to new roadmap and decision work.
4. Split large domain plans only when they become hard to review in the master
   roadmap.

## Out Of Scope Confirmed

- No implementation code.
- No runtime changes.
- No commit.
