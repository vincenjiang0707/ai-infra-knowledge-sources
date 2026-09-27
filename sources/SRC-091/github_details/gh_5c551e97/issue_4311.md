# [Issue #4311] [good-first-issue] storage: convert f-string log calls in redis_adapter.py to %-format

source: https://github.com/LMCache/LMCache/issues/4311
state: closed | updated: 2026-09-17T02:06:40Z
labels: 

## 正文

## Description

`lmcache/v1/storage_backend/connector/redis_adapter.py` currently has 3 `logger.*(f\"...\")` call sites. Following the maintainer preference discussed in #3372, these can be converted to lazy `%`-style interpolation so log arguments are formatted only when the record is emitted (ruff G004).

## Proposed scope

- Convert only the logger f-strings in `lmcache/v1/storage_backend/connector/redis_adapter.py`.
- Preserve the rendered log text and exception behavior.
- Do not change connector I/O, return values, or error handling.

## Verification

- `ruff check --select G004 lmcache/v1/storage_backend/connector/redis_adapter.py`
- `pre-commit run --files lmcache/v1/storage_backend/connector/redis_adapter.py` (or equivalent ruff format/check)

Refs #3372

## 评论 (2)

### zhengfeihe · 2026-07-29

Thanks for your interest and for opening issues～ I’m going to keep the first one open and close the others for now.

These f-string cleanups are small, beginner-friendly tasks, so we’d like to reserve them for different new contributors rather than having one person take all of them. In general, we encourage each contributor to complete one or two good first issues before moving on to more substantial work.

Once you’ve completed the first one, please feel free to look for a more advanced issue or propose a larger improvement.

### Ankushh0027 · 2026-08-15

Hi! I'd like to work on this issue. I can update the f-string log calls in redis_adapter.py to use the project's preferred style logging format while keeping the behavior unchanged.

I’ll also run the relevant tests/linting locally before opening a PR. Please assign this issue to me if it’s available. Thanks!
