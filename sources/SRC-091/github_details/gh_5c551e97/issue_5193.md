# [Issue #5193] [good-first-issue] health: convert health and lookup logging to %-format

source: https://github.com/LMCache/LMCache/issues/5193
state: closed | updated: 2026-09-23T21:09:07Z
labels: good first issue, help wanted

## 正文

Follow-up for #5118 after #5125.

#5125 enabled Ruff `G004` repo-wide and added temporary `per-file-ignores` for the files/directories that still build logging messages with f-strings. This issue is one small slice of that cleanup queue.

Claiming: please comment `/claim` and wait for assignment so we avoid duplicate PRs.

## Scope

Convert only the logging f-strings in:

- `lmcache/v1/health_monitor/checks/remote_backend_check.py` (5 G004 findings)
- `lmcache/v1/lookup_client/hit_limit_lookup_client.py` (1 G004 findings)

Counts above were measured on `dev` at `dd5dfca` with `ruff check --isolated --select G004`.

## Expected change

- Replace logging f-strings with lazy `%`-style logging arguments, for example `logger.info("loaded %s tokens", num_tokens)`.
- Preserve the rendered log text and behavior.
- Do not change non-logging f-strings or unrelated control flow.
- Remove the matching `G004` ignore entry/entries from `pyproject.toml` once the listed paths are clean.

Matching ignore entry/entries:

- `"lmcache/v1/health_monitor/checks/remote_backend_check.py" = ["G004"]`
- `"lmcache/v1/lookup_client/hit_limit_lookup_client.py" = ["G004"]`

For a `**` directory ignore, delete the directory entry only when the whole listed directory is clean. If a merge conflict leaves other unmigrated files in that ignored directory, replace the broad `**` entry with explicit file-level entries for the leftovers.

## Verification

```bash
ruff check --isolated --select G004 lmcache/v1/health_monitor/checks/remote_backend_check.py lmcache/v1/lookup_client/hit_limit_lookup_client.py
ruff check --select G004 lmcache/v1/health_monitor/checks/remote_backend_check.py lmcache/v1/lookup_client/hit_limit_lookup_client.py pyproject.toml
pre-commit run --all-files
```

The first command should report zero findings after the cleanup. The second command verifies the repo config still passes after removing the ignore entry/entries.

Refs #5118
Refs #3372
Refs #5125


## 评论 (3)

### Michael-WhiteCapData · 2026-09-18

/claim

### Swir · 2026-09-18

/claim

Hi! I’d like to take this issue if it is still available.

The proposed fix is to replace logging f-strings with lazy %-style formatting in these two files:

* `lmcache/v1/health_monitor/checks/remote_backend_check.py`
* `lmcache/v1/lookup_client/hit_limit_lookup_client.py`

For example, `logger.info(f"loaded {num_tokens} tokens")` becomes `logger.info("loaded %s tokens", num_tokens)`.

For messages containing format specifications, I would preserve the exact output rather than mechanically replacing every expression with `%s`.

The change would also remove the corresponding `G004` ignore entries from `pyproject.toml`, while leaving non-logging f-strings and control flow unchanged.

Validation would include the isolated G004 check, the repository-configured G004 check, and `pre-commit run --all-files`, as requested.

I have not implemented or tested the patch yet. I’ll wait for assignment before proceeding to avoid duplicate work.


### VinsmokeSanji33 · 2026-09-18

/claim
