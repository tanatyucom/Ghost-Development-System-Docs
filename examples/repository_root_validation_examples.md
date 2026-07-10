# Repository Root Validation Examples

## Purpose

この文書は、Repository Root Validation の良い例と悪い例を示します。

## Good Example

```text
Repository Root Validation:
- Current Working Directory: C:\GitHub\Ghost-Development-System-Docs
- Git repository root: C:/GitHub/Ghost-Development-System-Docs
- Expected Working Repository: C:\GitHub\Ghost-Development-System-Docs
- Root matches Working Repository: Yes
- Production Repository: Yes
- Backup / Reference Repository: No
- Safe to start: Yes
```

## Bad Example: Home Directory Root

```text
Current Working Directory: C:\Users\tanat
Git repository root: C:\Users\tanat
Expected Working Repository: C:\GitHub\Ghost-Development-System-Docs
```

問題:

- Git 操作が home directory に対して実行される。
- repository search / status / commit 判断が誤る。
- 作業開始前に停止すべき。

## Bad Example: Backup Repository

```text
Current Working Directory: C:\SteamAI\GrayGhost_backup
Git repository root: C:\SteamAI\GrayGhost_backup
Expected Working Repository: C:\SteamAI
```

問題:

- backup directory で作業している。
- production repository の状態を確認できていない。
- commit / review / repair の判断が危険。

## Review Checklist

- `pwd` または `Get-Location` を確認しているか。
- `git rev-parse --show-toplevel` を確認しているか。
- Q の Working Repository と一致しているか。
- backup / reference-only repository ではないか。
- `git status` が意図した repository の状態か。
