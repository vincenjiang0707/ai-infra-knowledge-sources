# [Issue #4028] --cache_requests delete fails when the cache directory does not exist

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/4028
state: closed | updated: 2026-08-24T12:22:54Z
labels: 

## 正文

### Description

Request-cache deletion crashes when the configured cache directory has not been created. This is a normal state for a first-time user, a fresh CI/container environment, or a new `LM_HARNESS_CACHE_PATH`.

`delete_cache()` calls `os.listdir(PATH)` unconditionally. When `PATH` is absent, Python raises `FileNotFoundError` before evaluation can continue.

This concerns the preprocessed request cache (`--cache_requests`), not the model response cache (`--use_cache`).

### Reproduction

```python
from pathlib import Path
from tempfile import TemporaryDirectory

from lm_eval.caching import cache

with TemporaryDirectory() as tmp:
    cache.PATH = str(Path(tmp) / "never-created")
    cache.delete_cache()
```

Observed:

```text
FileNotFoundError: [Errno 2] No such file or directory
```

The same path is reached by a first-time `--cache_requests delete` invocation.

### Expected behavior

Deleting an absent cache should be an idempotent no-op. The directory should remain absent, because a cleanup operation should not create filesystem state. Invalid configurations where the cache path points to a regular file should continue raising an error.

### Suggested fix

Catch `FileNotFoundError` around `os.listdir(PATH)` and return. Catching the operation directly also handles the directory disappearing between a separate existence check and the listing operation.

Add a focused unit test verifying that deletion neither raises nor creates the missing directory.

### Related work

PR #1372 introduced request-cache deletion. PR #3588 fixed a separate CLI argument-parsing failure for `--cache_requests`. Neither handles an absent cache directory.

## 评论 (1)

### feiiiiii5 · 2026-08-22

Opened PR #4035 implementing the suggested approach: `FileNotFoundError` caught around the `os.listdir(PATH)` call so deletion is an idempotent no-op (and the directory is not created as a side effect), while a regular file at PATH keeps raising via the distinct `NotADirectoryError`. Includes focused tests for both behaviors plus a guard that unrelated files in the cache directory are untouched.
