# [Issue #2210] Quality-checking tooling: let's move to newer ones, pytype is deprecated, `ruff` is popular, etc.

source: https://github.com/AI-Hypercomputer/maxtext/issues/2210
state: closed | updated: 2026-04-28T18:18:41Z
labels: feature request

## 正文

### Feature or Model Request

13-minutes-ago I was informed that [pytype](https://google.github.io/pytype) is no longer maintained google/pytype/issues/1838

[pylint](https://pypi.org/project/pylint), [black](https://github.com/psf/black) ([`pyink`](https://github.com/google/pyink) is forked from back) have an alternative in the Rust-written much-faster and more popular [ruff](https://github.com/astral-sh/ruff).

pytype has many alternatives, like the Rust-written [Pyrefly from Meta](https://pyrefly.org) or [ty](https://github.com/astral-sh/ty) (the latter from the same people as `ruff`).

### Additional Context

I can make the changes to support this new approach, including adding new pre-commit-hooks and updating the codebase to be both conformant and compliant.

## 评论 (2)

### RissyRan · 2025-08-26

Thanks Samuel for the report. I will assign this feature to you then, also cc @shralex for viz.

### sarunsingla11722 · 2026-04-28

We are currently closing stale issues as part of a cleanup initiative. If any of these are still necessary, please feel free to reopen them.



