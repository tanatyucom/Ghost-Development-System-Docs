# Script Architecture Rules

## Purpose

本ルールは Game Ghost の Script Architecture に関する恒久ルールを定義する。

本ルールは全ての Specification より優先される。

Script Structure Design や Script Refactoring は、本ルールを前提として設計・実装を行う。

---

# Rule 1

## One Script = One Responsibility

1つのスクリプトは1つの責務のみを持つ。

例

```
review_duplicate_titles.py

→ レビューのみ
```

NG

```
review_duplicate_titles.py

レビュー

DB更新

レポート生成
```

複数責務を持たせてはならない。

---

# Rule 2

## One Folder = One Domain

フォルダは役割単位で分類する。

例

```
database/

import/

review/

report/
```

目的の異なるスクリプトを混在させない。

---

# Rule 3

## Dependency Direction

依存方向は以下を原則とする。

```
Launcher / GUI
        │
        ▼
Business Scripts
        │
        ▼
Shared / Utils
```

下位レイヤーは上位レイヤーへ依存してはならない。

---

# Rule 4

## Shared Layer

shared は共通ライブラリのみ配置する。

shared は以下へ依存してはならない。

```
database

launcher

gui

report

review
```

shared は最下位レイヤーとする。

---

# Rule 5

## Utils Layer

utils は単独実行可能な補助スクリプトとする。

Business Logic を保持してはならない。

---

# Rule 6

## Launcher Responsibility

Launcher は

・実行
・メニュー
・起動制御

のみ担当する。

Business Logic を実装してはならない。

---

# Rule 7

## GUI Responsibility

GUI は

・入力

・表示

のみ担当する。

解析・DB更新・レビュー生成は既存 Script を呼び出して実行する。

GUI に Business Logic を持たせない。

---

# Rule 8

## Import Rules

許可

```
database → shared

import → shared

review → shared

report → shared
```

禁止

```
shared → database

shared → launcher

shared → gui
```

循環参照は禁止する。

---

# Rule 9

## Root Policy

scripts/ 直下には原則として .py を置かない。

例外

```
run_all.py
```

例外を追加する場合は Rule を更新する。

---

# Rule 10

## Naming Rules

役割が分かる名前を使用する。

例

```
review_*

report_*

import_*

apply_*

migrate_*

validate_*

*_gui.py
```

---

# Rule 11

## Reserved Categories

将来的なカテゴリ名として以下を予約する。

```
api/

web/

ai/
```

使用時は Specification を追加する。

---

# Rule 12

## Architecture First

新しい Script を追加する前に、

Category

Naming

Dependency

を確認する。

Rule に反する実装は禁止する。

---

# Rule Changes

本ルールの変更は

Architecture Level の変更とみなす。

変更時は

Roadmap

Decision Log

Specification

への影響を確認する。


---

# Rule 13

## Don't Duplicate Logic

同一の Business Logic を複数の Script に実装してはならない。

共通化可能な処理は `shared/` へ集約する。

---

# Rule 14

## Backward Compatibility

既存コマンド・パス・起動方法を変更する場合は、以下を同時更新する。

* README
* Documentation
* Launcher
* GUI
* Implementation Specification

互換性を失う変更は禁止する。
