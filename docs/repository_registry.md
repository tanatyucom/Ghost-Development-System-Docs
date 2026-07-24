# Repository Registry

**Canonical source:** `docs/registries/repository_registry.yaml`

## Current Entries

| ID | Name | Status | Root policy | Verified root | Branch | Mutation class |
| --- | --- | --- | --- | --- | --- | --- |
| `GDS-DOCS` | Ghost-Development-System-Docs | Active / Verified | fixed | `C:/GitHub/Ghost-Development-System-Docs` | `main` | DOCUMENTATION_ONLY |
| `GAMEGHOST` | GameGhost | Active / Verified | fixed | `C:/GrayGhostArchive/GameGhost` | `develop` | NORMAL |
| `AI-ARTIFACT-EXCHANGE-MCP-PROVISIONAL` | AI Artifact Exchange MCP Repository | Planned / Pending | unresolved | UNKNOWN | UNKNOWN | NONE |
| `ALLARCHIVE-PROVISIONAL` | AllArchive | Planned / Pending | unresolved | UNKNOWN | UNKNOWN | NONE |

## Interpretation

GameGhost was verified read-only at its Git top-level. Its remote repository
name differs from the nested local repository name; the verified top-level and
Registry ID preserve the distinction. A dirty GameGhost workspace was observed
but not modified.

The two Planned entries are concepts only. Neither root nor remote is asserted,
and neither may be selected as an execution target. The AI artifact exchange
concept is unrelated to Steam, and `C:/SteamAI/mcp` is not evidence of its
repository identity.

## Usage

1. Resolve by exact Repository ID.
2. Require Active and Verified for mutation assignment.
3. Resolve exactly one applicable root mapping.
4. Verify Q-specific role and Mutation Authority independently.
5. Treat conflicts as SCW; do not rewrite the Registry from observed ambiguity.
