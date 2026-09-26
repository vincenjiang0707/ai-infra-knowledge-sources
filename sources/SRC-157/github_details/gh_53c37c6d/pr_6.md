# [PR #6] docs: add complete CuTe DSL reference

source: https://github.com/mit-han-lab/KernelWiki/pull/6
state: closed | updated: 2026-08-12T22:29:59Z
labels: 

## 正文

## Summary
- add a searchable, commit-pinned compilation of the official CUTLASS Python CuTe DSL documentation and its five image assets
- connect the full reference to the CuTe DSL language page and regenerate the affected query indices

## Test plan
- [x] `python3 scripts/validate.py`
- [x] `python3 scripts/repo_size_check.py`
- [x] `python3 scripts/verify_core_prs.py`
- [x] `python3 scripts/verify_verbatim.py`
- [x] `bash tests/check_freshness_offline.sh`
- [x] query and fetch `doc-cutlass-cute-dsl` with the repository tools

## 评论 (0)
