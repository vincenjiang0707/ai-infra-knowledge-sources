source: https://github.com/vllm-project/guidellm/commit/73608c2574a242b008f672eb1a6394537cdd99bf

# Commit 73608c2

authored

docs: move English docs under en (

## Summary
Move the canonical English documentation source files into docs/en while preserving the existing public documentation routes. This keeps the multilingual layout explicit in the repository without changing how readers browse the site.
## Details
- [x] Moved English markdown pages from docs root sections into docs/en.
- [x] Mirrored docs/en pages back to the existing root routes during MkDocs generation.
- [x] Excluded docs/en from direct MkDocs publishing so duplicate /en routes are not generated.
- [x] Updated translation metadata and route generation to use docs/en as the English source while keeping browser routes unchanged.
- [x] Updated repository documentation links and documentation issue template paths.
## Test Plan
- tox -e translation-check
- tox -e lint-check
- uv run --no-sync mkdocs build --clean
- Manually served the site with uv run --no-sync mkdocs serve -a 127.0.0.1:8000 and verified existing routes remained available.
Assisted-by: Codex GPT-5
## Summary
## Details
- [ ]
## Test Plan
-
## Related Issues
- Resolves #
---
- [x] "I certify that all code in this PR is my own, except as noted below."
## Use of AI
- [x] Includes code generated or substantially modified by an AI agent
- [x] Includes tests generated or substantially modified by an AI agent
> NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([#1170](https://github.com/vllm-project/guidellm/pull/1170))[https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md](https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md)) file. --- # git log commit

[Author: tangming1996 <ming.tang@daocloud.io> Date: Tue Sep 22 15:56:06 2026 +0800 docs: move English docs under en ## Summary Move the canonical English documentation source files into docs/en while preserving the existing public documentation routes. This keeps the multilingual layout explicit in the repository without changing how readers browse the site. ## Details - [x] Moved English markdown pages from docs root sections into docs/en. - [x] Mirrored docs/en pages back to the existing root routes during MkDocs generation. - [x] Excluded docs/en from direct MkDocs publishing so duplicate /en routes are not generated. - [x] Updated translation metadata and route generation to use docs/en as the English source while keeping browser routes unchanged. - [x] Updated repository documentation links and documentation issue template paths. ## Test Plan - tox -e translation-check - tox -e lint-check - uv run --no-sync mkdocs build --clean - Manually served the site with uv run --no-sync mkdocs serve -a 127.0.0.1:8000 and verified existing routes remained available. Assisted-by: Codex GPT-5 Signed-off-by: tangming1996 <ming.tang@daocloud.io> --------- Assisted-by: Codex GPT-5 Signed-off-by: tangming1996 <ming.tang@daocloud.io>](https://github.com/vllm-project/guidellm/commit/c2814a465f68d4a164e2e5acb437fd6c9566104d)

`c2814a4`1 parent[948ec6e]commit 73608c2

41 files changed

Lines changed: 56 additions & 26 deletions

## File tree

- .github/ISSUE_TEMPLATE
- docs
- en
- developer
- examples
- getting-started
- guides
- multimodal


- scripts
- zh

- tests/unit/docs/scripts

## Some content is hidden

Large Commits have some content hidden by default. Use the searchbox below for content that may be hidden.

| Original file line number | Diff line number | Diff line change | |
|---|---|---|---|
| |||
`13` | `13` |
| |
`14` | `14` |
| |
`15` | `15` |
| |
`16` |
| `-` | |
| `16` | `+` | |
`17` | `17` |
| |
`18` | `18` |
| |
`19` | `19` |
| |
|

Lines changed: 1 addition & 1 deletion

## 0 commit comments