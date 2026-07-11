# 03 Root Cause

Root CauseはOCR EngineでもScoringでもありませんでした。

正しい候補が候補集合に生成されていませんでした。

```text
Scoring Problem
  -> Candidate Generation Problem
```

Scoringは、候補集合の中から最良を選ぶことしかできません。
正しい1行cropが候補集合に存在しない場合、Scoringをいくら改善しても正解には到達しません。

決定的だった観測:

- PASSは主に2行。
- FAILは主に3行。
- 正常な1行cropは存在しなかった。

この観測で、Scoring仮説は崩れました。
