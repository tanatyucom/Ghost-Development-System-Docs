# Repository Registry Examples and Scenario Matrix

| # | Scenario | Result |
| --- | --- | --- |
| 1 | Lookup `GDS-DOCS`. | Active/Verified; may supply identity, then Q authority is checked. |
| 2 | Lookup `GAMEGHOST`. | Active/Verified read-only evidence; dirty state does not authorize mutation. |
| 3 | Lookup planned AI artifact exchange repository. | Design reference only; root remains UNKNOWN. |
| 4 | Lookup planned AllArchive. | Design reference only; not executable. |
| 5 | Pass `C:/SteamAI/mcp` as a repository. | Reject directory-only claim; SCW if execution depends on it. |
| 6 | Unknown Repository ID. | No inference; remain UNKNOWN. |
| 7 | Duplicate Repository ID. | BLOCK Registry validation. |
| 8 | Git top-level differs from registered fixed root. | Conflict; SCW_REQUIRED. |
| 9 | Machine-specific root. | Resolve exact `machine_id`; multiple/no mapping blocks mutation. |
| 10 | Stale Active repository used for mutation. | Prohibit mutation until Verified. |
| 11 | Registry supports TARGET but Q assigns SOURCE. | Use Q assignment if supported; capability is not assignment. |
| 12 | Registry NORMAL but Q authority NONE. | Effective authority is NONE. |
| 13 | Draft Q Generator lookup. | Fill identity with provenance; leave unregistered target UNKNOWN. |
| 14 | Inherited root conflicts with Registry. | Invalidate affected inherited context and SCW. |
| 15 | Path case/separator differs but Git identity is unique. | AUTO normalize and record. |
| 16 | Planned -> Active. | REQUIRED after identity/root/branch/remote verification. |

## Machine-specific Root Example

```yaml
root_policy: machine-specific
canonical_root: null
machine_roots:
  - machine_id: developer-windows
    local_root: C:/GitHub/Example
  - machine_id: build-linux
    local_root: /srv/build/Example
```

The repository ID remains stable across both roots.
