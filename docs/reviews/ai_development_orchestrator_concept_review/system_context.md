# System Context Diagram

```mermaid
flowchart LR
    H["Human"] --> CG["ChatGPT: GDS Context"]
    H --> CP["ChatGPT: GameGhost Context"]
    CG -->|"Drafts, review, approval coordination"| AO["AI Development Orchestration Platform"]
    CP -->|"Product-development context"| AO

    GD["GDS-DOCS\nCanonical governance"] -->|"Versioned policy/contracts"| GR["GDS Runtime\nPolicy Provider"]
    GD -->|"Canonical contracts"| AO
    GR -->|"Policy evaluation"| AO

    AO --> AX["Artifact Exchange"]
    AO --> Q["Durable Event Queue"]
    AO --> OR["Orchestrator / Recovery"]
    AO --> EG["Execution Gateway"]
    AO --> AL["Audit / Event Log"]
    AO --- MCP["MCP Adapter\nOptional transport"]

    OR -->|"Scoped Execution Package"| CW["Codex Worker"]
    CW -->|"Completion Package + Evidence"| AX
    EG -->|"Allowlisted Git operations"| GG["GameGhost Repository\nProduct"]
    EG -->|"Allowlisted Git operations"| FP["Future Product Repositories"]
    CW -->|"Approved scoped mutation"| GG
    CW -->|"Approved scoped mutation"| FP

    CG -. "Same ChatGPT, different context" .- CP
```

GDS is not ChatGPT. GameGhost is not Codex. MCP is neither GDS nor GameGhost
and does not connect their product functionality. It is an optional adapter
inside the orchestration boundary.
