# [Issue #5194] [good-first-issue] storage: convert package backend logging to %-format

source: https://github.com/LMCache/LMCache/issues/5194
state: closed | updated: 2026-09-24T05:47:19Z
labels: good first issue, help wanted

## 正文

Follow-up for #5118 after #5125.

#5125 enabled Ruff `G004` repo-wide and added temporary `per-file-ignores` for the files/directories that still build logging messages with f-strings. This issue is one small slice of that cleanup queue.

Claiming: please comment `/claim` and wait for assignment so we avoid duplicate PRs.

## Scope

Convert only the logging f-strings in:

- `lmcache/v1/storage_backend/__init__.py` (4 G004 findings)
- `lmcache/v1/storage_backend/p2p_backend.py` (2 G004 findings)
- `lmcache/v1/storage_backend/path_sharder.py` (1 G004 findings)

Counts above were measured on `dev` at `dd5dfca` with `ruff check --isolated --select G004`.

## Expected change

- Replace logging f-strings with lazy `%`-style logging arguments, for example `logger.info("loaded %s tokens", num_tokens)`.
- Preserve the rendered log text and behavior.
- Do not change non-logging f-strings or unrelated control flow.
- Remove the matching `G004` ignore entry/entries from `pyproject.toml` once the listed paths are clean.

Matching ignore entry/entries:

- `"lmcache/v1/storage_backend/__init__.py" = ["G004"]`
- `"lmcache/v1/storage_backend/p2p_backend.py" = ["G004"]`
- `"lmcache/v1/storage_backend/path_sharder.py" = ["G004"]`

For a `**` directory ignore, delete the directory entry only when the whole listed directory is clean. If a merge conflict leaves other unmigrated files in that ignored directory, replace the broad `**` entry with explicit file-level entries for the leftovers.

## Verification

```bash
ruff check --isolated --select G004 lmcache/v1/storage_backend/__init__.py lmcache/v1/storage_backend/p2p_backend.py lmcache/v1/storage_backend/path_sharder.py
ruff check --select G004 lmcache/v1/storage_backend/__init__.py lmcache/v1/storage_backend/p2p_backend.py lmcache/v1/storage_backend/path_sharder.py pyproject.toml
pre-commit run --all-files
```

The first command should report zero findings after the cleanup. The second command verifies the repo config still passes after removing the ignore entry/entries.

Refs #5118
Refs #3372
Refs #5125


## 评论 (4)

### liuxiaocs7 · 2026-09-18

Hi, @maobaolong, i want to have a try, could you help assign this task to me, thanks!

### liuxiaocs7 · 2026-09-18

/claim

### maobaolong · 2026-09-18

@liuxiaocs7 Take it. Look forward to see your PR.

### liuxiaocs7 · 2026-09-24

Thanks @maobaolong for the help, and thanks to @chunxiaozheng and @zhengfeihe  for reviewing. 

Through this issue and #3372, I've gotten familiar with the development workflow of LMCache, and through this [blog](https://blog.lmcache.ai/zh/2026/06/23/vllmlmcache-%e9%9b%b6-gpu-%e5%bc%80%e5%8f%91%e6%8c%87%e5%8d%97/), I've also learned how to develop and validate locally in a non-GPU environment.

Looking forward to contributing more to the community!
