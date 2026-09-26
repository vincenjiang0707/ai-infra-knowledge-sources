source: https://github.com/vllm-project/guidellm/pull/1170

# docs: move English docs under en - #1170

Merged

[mergify[bot]](https://github.com/mergify[bot])merged 1 commit into

Merged

## Conversation

[tangming1996](https://github.com/tangming1996)requested review from

[dbutenhof](https://github.com/dbutenhof),

[dfeddema](https://github.com/dfeddema),

[jaredoconnell](https://github.com/jaredoconnell)and

[sjmonson](https://github.com/sjmonson)as

[code owners](https://github.com/vllm-project/guidellm/blob/148c3bab4f75fe9f64fb15520d7d64fa08914a90/CODEOWNERS#L2)

September 22, 2026 07:57

Collaborator

|
|

[tangming1996](https://github.com/tangming1996)

[force-pushed](https://github.com/vllm-project/guidellm/compare/8b0f07814161f352f3db93de7b36b9be9acb6fe2..f55cbf53a85c35fbaf998f98a46b3a07c20cf410)the codex/docs-i18n-pilot branch from

[to](https://github.com/vllm-project/guidellm/commit/8b0f07814161f352f3db93de7b36b9be9acb6fe2)

`8b0f078`


`f55cbf5`

[Compare](https://github.com/vllm-project/guidellm/compare/8b0f07814161f352f3db93de7b36b9be9acb6fe2..f55cbf53a85c35fbaf998f98a46b3a07c20cf410)

September 23, 2026 01:34

## Summary Move the canonical English documentation source files into docs/en while preserving the existing public documentation routes. This keeps the multilingual layout explicit in the repository without changing how readers browse the site. ## Details - [x] Moved English markdown pages from docs root sections into docs/en. - [x] Mirrored docs/en pages back to the existing root routes during MkDocs generation. - [x] Excluded docs/en from direct MkDocs publishing so duplicate /en routes are not generated. - [x] Updated translation metadata and route generation to use docs/en as the English source while keeping browser routes unchanged. - [x] Updated repository documentation links and documentation issue template paths. ## Test Plan - tox -e translation-check - tox -e lint-check - uv run --no-sync mkdocs build --clean - Manually served the site with uv run --no-sync mkdocs serve -a 127.0.0.1:8000 and verified existing routes remained available. Assisted-by: Codex GPT-5 Signed-off-by: tangming1996 <ming.tang@daocloud.io>

[tangming1996](https://github.com/tangming1996)

[force-pushed](https://github.com/vllm-project/guidellm/compare/f55cbf53a85c35fbaf998f98a46b3a07c20cf410..c2814a465f68d4a164e2e5acb437fd6c9566104d)the codex/docs-i18n-pilot branch from

[to](https://github.com/vllm-project/guidellm/commit/f55cbf53a85c35fbaf998f98a46b3a07c20cf410)

`f55cbf5`


`c2814a4`

[Compare](https://github.com/vllm-project/guidellm/compare/f55cbf53a85c35fbaf998f98a46b3a07c20cf410..c2814a465f68d4a164e2e5acb437fd6c9566104d)

September 23, 2026 01:44

Contributor
Author

|
|

[mkdocs.yml](https://github.com/vllm-project/guidellm/pull/1170/files/c2814a465f68d4a164e2e5acb437fd6c9566104d#diff-98d0f806abc9af24e6a7c545d3d77e8f9ad57643e27211d7a7b896113e420ed2)


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Sep 23, 2026

Contributor

|
Received a single approval. Will automatically queue for merge once two maintainers approve, all change requests are resolved, and DCO passes. |

Contributor

|
Queued — the merge queue status continues in |


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Sep 23, 2026

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge |

9 tasks

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Move the canonical English documentation source files into docs/en while preserving the existing public documentation routes. This keeps the multilingual layout explicit in the repository without changing how readers browse the site.

## Details

## Test Plan

Assisted-by: Codex GPT-5

## Summary

## Details

## Test Plan

## Related Issues

## Use of AI

## git log

commit

c2814a4Author: tangming1996 ming.tang@daocloud.io

Date: Tue Sep 22 15:56:06 2026 +0800

Assisted-by: Codex GPT-5

Signed-off-by: tangming1996 ming.tang@daocloud.io