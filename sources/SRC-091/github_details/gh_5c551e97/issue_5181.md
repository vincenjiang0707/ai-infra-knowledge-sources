# [Issue #5181] [good-first-issue] benchmarks: convert storage_backend_io logging to %-format

source: https://github.com/LMCache/LMCache/issues/5181
state: closed | updated: 2026-09-24T00:31:03Z
labels: good first issue, help wanted

## 正文

Follow-up for #5118 after #5125.

#5125 enabled Ruff `G004` repo-wide and added temporary `per-file-ignores` for the files/directories that still build logging messages with f-strings. This issue is one small slice of that cleanup queue.

Claiming: please comment `/claim` and wait for assignment so we avoid duplicate PRs.

## Scope

Convert only the logging f-strings in:

- `benchmarks/storage_backend_io/storage_backend_io_benchmark.py` (8 G004 findings)

Counts above were measured on `dev` at `dd5dfca` with `ruff check --isolated --select G004`.

Note: This uses a directory-level ignore because every file below that directory was unmigrated in #5125.

## Expected change

- Replace logging f-strings with lazy `%`-style logging arguments, for example `logger.info("loaded %s tokens", num_tokens)`.
- Preserve the rendered log text and behavior.
- Do not change non-logging f-strings or unrelated control flow.
- Remove the matching `G004` ignore entry/entries from `pyproject.toml` once the listed paths are clean.

Matching ignore entry/entries:

- `"benchmarks/storage_backend_io/**" = ["G004"]`

For a `**` directory ignore, delete the directory entry only when the whole listed directory is clean. If a merge conflict leaves other unmigrated files in that ignored directory, replace the broad `**` entry with explicit file-level entries for the leftovers.

## Verification

```bash
ruff check --isolated --select G004 benchmarks/storage_backend_io/storage_backend_io_benchmark.py
ruff check --select G004 benchmarks/storage_backend_io/storage_backend_io_benchmark.py pyproject.toml
pre-commit run --all-files
```

The first command should report zero findings after the cleanup. The second command verifies the repo config still passes after removing the ignore entry/entries.

Refs #5118
Refs #3372
Refs #5125


## 评论 (3)

### xiaoba17 · 2026-09-19

/claim

### HarshRajSinghania · 2026-09-19

/claim

Opening a PR that converts the eight logging f-strings in `benchmarks/storage_backend_io/storage_backend_io_benchmark.py` and removes the directory G004 ignore.

### xiaoba17 · 2026-09-19

Hi @maobaolong, I claimed this issue earlier and have been waiting for assignment as requested. My fix is complete, with the G004 checks and pre-commit checks passing (Rust hooks skipped per the repository’s macOS guidance).

My branch: https://github.com/xiaoba17/LMCache/tree/fix/5181-storage-backend-logging

I noticed #5254 has since been opened for the same issue. Could you clarify who should proceed? I’ve held off on opening a PR to avoid duplicate work. Thanks!
