# Q_GDS-REPOSITORY-EVOLUTION-002 Correction Guidance

## Resume Context

The Q may resume only after its repository declarations contain the following
verified values.

### Output Repository

- Role: `OUTPUT`
- Name: `Ghost-Development-System-Docs`
- Root: `C:\GitHub\Ghost-Development-System-Docs`
- Expected Base Branch: `origin/HEAD auto-detection`
- Mutation Policy: `DOCUMENTATION_ONLY`

### Validation Repository

- Role: `VALIDATION`
- Name: `Steam MCP Experimental Repository`
- Root: `C:\SteamAI\mcp`
- Expected Base Branch: `origin/HEAD auto-detection`
- Mutation Policy: `READ_ONLY`
- Allowed Operations: repository identity, documentation, vocabulary, branch,
  and status inspection without side effects
- Prohibited Operations: create, update, delete, format, cache, test artifact,
  Commit, Push, Tag, branch mutation, or any other Git mutation

GameGhost is the vocabulary's source history and must not be substituted for
the second/validation repository.

Commit, Push, and Tag are `PROHIBITED` for this correction stage. Missing or
ambiguous `origin/HEAD`, a nonexistent root, or any possible read-only side
effect requires SCW.
