# [Issue #5180] [good-first-issue] benchmarks: convert rag logging to %-format

source: https://github.com/LMCache/LMCache/issues/5180
state: closed | updated: 2026-09-23T07:49:47Z
labels: good first issue, help wanted

## 正文

Follow-up for #5118 after #5125.

#5125 enabled Ruff `G004` repo-wide and added temporary `per-file-ignores` for the files/directories that still build logging messages with f-strings. This issue is one small slice of that cleanup queue.

Claiming: please comment `/claim` and wait for assignment so we avoid duplicate PRs.

## Scope

Convert only the logging f-strings in:

- `benchmarks/rag/rag.py` (2 G004 findings)
- `benchmarks/rag/utils.py` (2 G004 findings)

Counts above were measured on `dev` at `dd5dfca` with `ruff check --isolated --select G004`.

## Expected change

- Replace logging f-strings with lazy `%`-style logging arguments, for example `logger.info("loaded %s tokens", num_tokens)`.
- Preserve the rendered log text and behavior.
- Do not change non-logging f-strings or unrelated control flow.
- Remove the matching `G004` ignore entry/entries from `pyproject.toml` once the listed paths are clean.

Matching ignore entry/entries:

- `"benchmarks/rag/rag.py" = ["G004"]`
- `"benchmarks/rag/utils.py" = ["G004"]`

For a `**` directory ignore, delete the directory entry only when the whole listed directory is clean. If a merge conflict leaves other unmigrated files in that ignored directory, replace the broad `**` entry with explicit file-level entries for the leftovers.

## Verification

```bash
ruff check --isolated --select G004 benchmarks/rag/rag.py benchmarks/rag/utils.py
ruff check --select G004 benchmarks/rag/rag.py benchmarks/rag/utils.py pyproject.toml
pre-commit run --all-files
```

The first command should report zero findings after the cleanup. The second command verifies the repo config still passes after removing the ignore entry/entries.

Refs #5118
Refs #3372
Refs #5125


## 评论 (4)

### Rudra-G-23 · 2026-09-18

/claim

### Punith968 · 2026-09-19

Hi! I’d like to work on this good-first-issue. I’ll keep the change scoped to the two benchmark files and the matching Ruff G004 ignore entries, then run the requested Ruff and pre-commit checks. Please assign/confirm before I start.

### Rudra-G-23 · 2026-09-19

Here the PR #5231 already open so I drop mine

### neevmodh · 2026-09-22

/claim
