# [Issue #5205] [good-first-issue] lint: remove stale G004 ignores for clean connector adapters

source: https://github.com/LMCache/LMCache/issues/5205
state: open | updated: 2026-09-23T05:01:35Z
labels: good first issue, help wanted

## 正文

Follow-up for #5118 after #5125.

#5125 added temporary `G004` ignores for files that still had logging f-strings. Two connector adapter files are currently clean on `dev`, but still have stale `G004` ignore entries in `pyproject.toml`.

Claiming: please comment `/claim` and wait for assignment so we avoid duplicate PRs.

## Scope

Remove the stale `G004` ignore entries for:

- `lmcache/v1/storage_backend/connector/infinistore_adapter.py`
- `lmcache/v1/storage_backend/connector/redis_adapter.py`

## Expected change

- Delete only these two matching lines from `[tool.ruff.lint.per-file-ignores]` in `pyproject.toml`:
  - `"lmcache/v1/storage_backend/connector/infinistore_adapter.py" = ["G004"]`
  - `"lmcache/v1/storage_backend/connector/redis_adapter.py" = ["G004"]`
- Do not make unrelated logging or code changes.

## Verification

```bash
ruff check --isolated --select G004 lmcache/v1/storage_backend/connector/infinistore_adapter.py lmcache/v1/storage_backend/connector/redis_adapter.py
ruff check --select G004 lmcache/v1/storage_backend/connector/infinistore_adapter.py lmcache/v1/storage_backend/connector/redis_adapter.py pyproject.toml
pre-commit run --all-files
```

The first command should report zero findings even without repo config ignores; the second command verifies the repo config still passes after the stale ignore entries are removed.

Refs #5118
Refs #3372
Refs #5125


## 评论 (2)

### yunaremaia · 2026-09-18

/claim

### Parithosh-Varma · 2026-09-23

/claim
