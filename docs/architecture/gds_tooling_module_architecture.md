# GDS Tooling Module Architecture

**Version:** 1.0
**Status:** Adopted Design

```text
Canonical Specifications (GDS-DOCS)
  -> Runtime Core Contracts
     -> approval / draft_q / repository_registry / context / validation / audit
        -> CLI Adapter
        -> Repository Adapter
        -> Future MCP Transport Adapter
```

Core modules use typed domain models and deterministic results. They do not
perform Git, filesystem mutation, network access, approval, or transport by
themselves. Ports describe observation and mutation; adapters implement them
under separate authority.

`schemas` contains versioned machine contracts. `audit` records input identity,
policy/schema version, decision, reason, evidence references, corrections, and
side-effect result. Generated artifacts are outputs, never hidden state.

Repository-specific behavior lives in adapters or fixtures. GameGhost adapters
cannot become a dependency of core packages. MCP is a future adapter and cannot
own Approval, Draft, Registry, or Context policy.
