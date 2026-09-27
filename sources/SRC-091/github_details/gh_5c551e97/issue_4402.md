# [Issue #4402] [good-first-issue] storage: convert f-string log calls in infinistore_adapter.py to %-format

source: https://github.com/LMCache/LMCache/issues/4402
state: closed | updated: 2026-09-17T09:06:20Z
labels: 

## 正文

## Description

A `logger.info(f"...")` call in `lmcache/v1/storage_backend/connector/infinistore_adapter.py` uses f-string formatting. Per Python's logging docs and ruff G004, `%`-format is preferred so the message is only built when the log actually emits.

## Scope

Per @maobaolong 's direction in #3372, limited to 3 places for first-time contributor workflow practice. The f-string log call:

- line 27 — `logger.info(f"Creating Infinistore connector for URL: {context.url}")`

Converts to `%s`. No behavior change; format style only.

Ref #3372


## 评论 (1)

### linear3735 · 2026-08-03

/claim
