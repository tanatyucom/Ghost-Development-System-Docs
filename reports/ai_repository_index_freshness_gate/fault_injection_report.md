# AI Repository Index Freshness Fault-Injection Report

## Result

`PASS`

Automated tests demonstrated stale output detection for:

- a new Indexable Markdown file;
- removal of an indexed file;
- rename of an indexed file;
- category change caused by path movement;
- manual generated-file editing.

The CI contract test also verifies Canonical command ordering and the explicit
stale failure code.
