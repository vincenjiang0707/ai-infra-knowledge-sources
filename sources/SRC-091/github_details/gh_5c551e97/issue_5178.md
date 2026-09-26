# [Issue #5178] [good-first-issue] buildkite: convert async_request logging to %-format

source: https://github.com/LMCache/LMCache/issues/5178
state: closed | updated: 2026-09-24T03:04:26Z
labels: good first issue, help wanted

## 正文

Follow-up for #5118 after #5125.

#5125 enabled Ruff `G004` repo-wide and added temporary `per-file-ignores` for the files/directories that still build logging messages with f-strings. This issue is one small slice of that cleanup queue.

Claiming: please comment `/claim` and wait for assignment so we avoid duplicate PRs.

## Scope

Convert only the logging f-strings in:

- `.buildkite/correctness/async_request.py` (4 G004 findings)

Counts above were measured on `dev` at `dd5dfca` with `ruff check --isolated --select G004`.

## Expected change

- Replace logging f-strings with lazy `%`-style logging arguments, for example `logger.info("loaded %s tokens", num_tokens)`.
- Preserve the rendered log text and behavior.
- Do not change non-logging f-strings or unrelated control flow.
- Remove the matching `G004` ignore entry/entries from `pyproject.toml` once the listed paths are clean.

Matching ignore entry/entries:

- `".buildkite/correctness/async_request.py" = ["G004"]`

For a `**` directory ignore, delete the directory entry only when the whole listed directory is clean. If a merge conflict leaves other unmigrated files in that ignored directory, replace the broad `**` entry with explicit file-level entries for the leftovers.

## Verification

```bash
ruff check --isolated --select G004 .buildkite/correctness/async_request.py
ruff check --select G004 .buildkite/correctness/async_request.py pyproject.toml
pre-commit run --all-files
```

The first command should report zero findings after the cleanup. The second command verifies the repo config still passes after removing the ignore entry/entries.

Refs #5118
Refs #3372
Refs #5125


## 评论 (3)

### cblh · 2026-09-18

/claim

### Chebaleomkar · 2026-09-22

/claim

### Chebaleomkar · 2026-09-22

 convert only the 4 listed logging f-strings in `.buildkite/correctness/async_request.py` to lazy `%`-style args with identical rendering (`%s` for `obj_name`/`content`/`sum(...)`, `%.2f` preserving the existing precision for the elapsed time), leave the non-logging f-strings (headers, file writes, `print`) untouched, and remove exactly the one matching `G004` ignore entry from `pyproject.toml`. Verify with the issue commands plus a rendering-equivalence check. Work is on branch `gfi/5178-async-request-logging`.
