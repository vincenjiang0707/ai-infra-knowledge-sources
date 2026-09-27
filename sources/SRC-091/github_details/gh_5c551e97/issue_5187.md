# [Issue #5187] [good-first-issue] logging: convert top-level LMCache utility logging to %-format

source: https://github.com/LMCache/LMCache/issues/5187
state: open | updated: 2026-09-22T14:41:15Z
labels: good first issue, help wanted

## 正文

Follow-up for #5118 after #5125.

#5125 enabled Ruff `G004` repo-wide and added temporary `per-file-ignores` for the files/directories that still build logging messages with f-strings. This issue is one small slice of that cleanup queue.

Claiming: please comment `/claim` and wait for assignment so we avoid duplicate PRs.

## Scope

Convert only the logging f-strings in:

- `lmcache/observability.py` (2 G004 findings)
- `lmcache/sdk/context.py` (1 G004 findings)
- `lmcache/utils.py` (1 G004 findings)

Counts above were measured on `dev` at `dd5dfca` with `ruff check --isolated --select G004`.

## Expected change

- Replace logging f-strings with lazy `%`-style logging arguments, for example `logger.info("loaded %s tokens", num_tokens)`.
- Preserve the rendered log text and behavior.
- Do not change non-logging f-strings or unrelated control flow.
- Remove the matching `G004` ignore entry/entries from `pyproject.toml` once the listed paths are clean.

Matching ignore entry/entries:

- `"lmcache/observability.py" = ["G004"]`
- `"lmcache/sdk/context.py" = ["G004"]`
- `"lmcache/utils.py" = ["G004"]`

For a `**` directory ignore, delete the directory entry only when the whole listed directory is clean. If a merge conflict leaves other unmigrated files in that ignored directory, replace the broad `**` entry with explicit file-level entries for the leftovers.

## Verification

```bash
ruff check --isolated --select G004 lmcache/observability.py lmcache/sdk/context.py lmcache/utils.py
ruff check --select G004 lmcache/observability.py lmcache/sdk/context.py lmcache/utils.py pyproject.toml
pre-commit run --all-files
```

The first command should report zero findings after the cleanup. The second command verifies the repo config still passes after removing the ignore entry/entries.

Refs #5118
Refs #3372
Refs #5125


## 评论 (3)

### taljeon · 2026-09-18

/claim

Plan: convert only the four listed logging f-strings in `lmcache/observability.py`, `lmcache/sdk/context.py`, and `lmcache/utils.py` to lazy `%`-style arguments, remove their exact `G004` ignore entries from `pyproject.toml`, and run both scoped Ruff commands plus the repository pre-commit workflow. I’ll preserve rendered messages and leave non-logging f-strings unchanged.

AI disclosure: I’m using OpenAI Codex (`gpt-5.6-sol`) to assist with source inspection and implementation. I’ll review the exact diff, keep the commit DCO-signed without AI attribution, and report the actual verification results.


### Chebaleomkar · 2026-09-22

/claim

### Chebaleomkar · 2026-09-22

Sharing my approach for this issue (awaiting assignment before opening the PR):

1. Convert only the 4 listed logging f-strings to lazy \%\-style args, preserving rendered text exactly:
   - \lmcache/observability.py\ (2): the \logger.info\/\logger.warning\ in the stats-logger shutdown path -> \%ss\ with \	imeout\
   - \lmcache/sdk/context.py\ (1): init log -> 5x \%s\ with the same attributes in the same order
   - \lmcache/utils.py\ (1): \handle_thread_exception\ -> 3x \%s\
2. Remove exactly the 3 matching \G004\ ignore entries from \pyproject.toml\.
3. Verify with the commands in the issue: \uff check --isolated --select G004\ (zero findings), config-aware \uff check\, and \pre-commit run\. I additionally executed the formatting paths to confirm the rendered messages are byte-identical.

No changes to non-logging f-strings or control flow. Work is on branch \gfi/5187-utility-logging\.
