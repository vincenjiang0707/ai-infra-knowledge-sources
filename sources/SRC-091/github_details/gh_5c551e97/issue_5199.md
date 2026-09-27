# [Issue #5199] [good-first-issue] connectors: convert helper connector logging to %-format

source: https://github.com/LMCache/LMCache/issues/5199
state: closed | updated: 2026-09-21T01:15:03Z
labels: good first issue, help wanted

## 正文

Follow-up for #5118 after #5125.

#5125 enabled Ruff `G004` repo-wide and added temporary `per-file-ignores` for the files/directories that still build logging messages with f-strings. This issue is one small slice of that cleanup queue.

Claiming: please comment `/claim` and wait for assignment so we avoid duplicate PRs.

## Scope

Convert only the logging f-strings in:

- `lmcache/v1/storage_backend/connector/instrumented_connector.py` (1 G004 findings)
- `lmcache/v1/storage_backend/connector/lm_connector.py` (1 G004 findings)
- `lmcache/v1/storage_backend/connector/mock_connector.py` (5 G004 findings)

Counts above were measured on `dev` at `dd5dfca` with `ruff check --isolated --select G004`.

## Expected change

- Replace logging f-strings with lazy `%`-style logging arguments, for example `logger.info("loaded %s tokens", num_tokens)`.
- Preserve the rendered log text and behavior.
- Do not change non-logging f-strings or unrelated control flow.
- Remove the matching `G004` ignore entry/entries from `pyproject.toml` once the listed paths are clean.

Matching ignore entry/entries:

- `"lmcache/v1/storage_backend/connector/instrumented_connector.py" = ["G004"]`
- `"lmcache/v1/storage_backend/connector/lm_connector.py" = ["G004"]`
- `"lmcache/v1/storage_backend/connector/mock_connector.py" = ["G004"]`

For a `**` directory ignore, delete the directory entry only when the whole listed directory is clean. If a merge conflict leaves other unmigrated files in that ignored directory, replace the broad `**` entry with explicit file-level entries for the leftovers.

## Verification

```bash
ruff check --isolated --select G004 lmcache/v1/storage_backend/connector/instrumented_connector.py lmcache/v1/storage_backend/connector/lm_connector.py lmcache/v1/storage_backend/connector/mock_connector.py
ruff check --select G004 lmcache/v1/storage_backend/connector/instrumented_connector.py lmcache/v1/storage_backend/connector/lm_connector.py lmcache/v1/storage_backend/connector/mock_connector.py pyproject.toml
pre-commit run --all-files
```

The first command should report zero findings after the cleanup. The second command verifies the repo config still passes after removing the ignore entry/entries.

Refs #5118
Refs #3372
Refs #5125


## 评论 (4)

### gonappuccino · 2026-09-19

/claim

### SatvikMishra08 · 2026-09-19

/claim

Taking the G004 logging %-format cleanup on the helper connectors (base branch `dev`).

### HarshRajSinghania · 2026-09-19

Opened a PR with the G004 cleanup on the three helper connector files listed in this issue: converting the logging f-strings to `%-style` arguments and removing the matching `pyproject.toml` ignores.

### gonappuccino · 2026-09-19

Hi @maobaolong, I've opened #5259 for this issue. It converts the seven logging calls in the three connector files and removes the matching G004 ignores, with the ruff checks and pre-commit from the issue passing locally. One small note: the `Mock object is None` warning was passing two f-strings as separate arguments, so it also fixes that so the message renders correctly.

Would appreciate a look when you have a moment.
