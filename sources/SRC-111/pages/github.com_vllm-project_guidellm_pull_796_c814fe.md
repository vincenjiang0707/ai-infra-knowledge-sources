source: https://github.com/vllm-project/guidellm/pull/796

# fix(data): fail fast when no mappable columns are found (#787) - #796

[mergify[bot]](https://github.com/mergify[bot])merged 6 commits into

## Conversation

GenerativeColumnMapper.setup_data only logged a warning when a dataset had no mappable columns, then returned an empty mapping. Every row then produced an empty result, the scheduler started but never enqueued any request, and the benchmark hung forever (only killed by an external timeout). Raise a clear ValueError at setup time instead, listing the dataset columns that were found so the user knows to rename a column to a recognized name (e.g. 'prompt') or pass an explicit column mapping. Fixes[vllm-project#787]Signed-off-by: Tai An <antai12232931@outlook.com>

|
Hi |

Signed-off-by: Tai An <antai12232931@outlook.com>

[Anai-Guo](https://github.com/Anai-Guo)

[force-pushed](https://github.com/vllm-project/guidellm/compare/c5e7259e61fa2585655f4a6a066d152cfb379012..ce27bd3f12bf1ae6119165efa4c537348e72339a)the fix-mapper-no-columns-fail-fast branch from

[to](https://github.com/vllm-project/guidellm/commit/c5e7259e61fa2585655f4a6a066d152cfb379012)

`c5e7259`


`ce27bd3`

[Compare](https://github.com/vllm-project/guidellm/compare/c5e7259e61fa2585655f4a6a066d152cfb379012..ce27bd3f12bf1ae6119165efa4c537348e72339a)

June 16, 2026 16:08


**requested changes**

[dbutenhof](https://github.com/dbutenhof)Jun 16, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

Thanks for catching and fixing the CRLF line termination!

[src/guidellm/data/preprocessors/mappers.py](https://github.com/vllm-project/guidellm/pull/796/files#diff-2099c62bd0e1315d94f5ca565b50198a0507b9f2818feba33fd14d29641e6deb)Outdated

Signed-off-by: Tai An <antai12232931@outlook.com>

|
Thanks |


**previously approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jun 16, 2026

[src/guidellm/data/preprocessors/mappers.py](https://github.com/vllm-project/guidellm/pull/796/files#diff-2099c62bd0e1315d94f5ca565b50198a0507b9f2818feba33fd14d29641e6deb)Outdated


[dbutenhof](https://github.com/dbutenhof)added

[bug](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Abug)

[escape](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Aescape)

Jun 16, 2026


**requested changes**

[sjmonson](https://github.com/sjmonson)Jun 16, 2026

[src/guidellm/data/preprocessors/mappers.py](https://github.com/vllm-project/guidellm/pull/796/files#diff-2099c62bd0e1315d94f5ca565b50198a0507b9f2818feba33fd14d29641e6deb)Outdated


**previously approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jun 16, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

Yeah, it makes sense to switch this check from a warning to a fatal exception.

[src/guidellm/data/preprocessors/mappers.py](https://github.com/vllm-project/guidellm/pull/796/files#diff-2099c62bd0e1315d94f5ca565b50198a0507b9f2818feba33fd14d29641e6deb)Outdated

[src/guidellm/data/preprocessors/mappers.py](https://github.com/vllm-project/guidellm/pull/796/files#diff-2099c62bd0e1315d94f5ca565b50198a0507b9f2818feba33fd14d29641e6deb)Outdated

Drop the verbose column listing and hang explanation; raise a short ValueError as requested. Signed-off-by: Tai An <antai12232931@outlook.com>

|
Thanks
No column listing, no hang explanation — kept short as requested. Ready for another look. |


**previously approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jun 17, 2026

|
Hi |

…ormat) Signed-off-by: Tai An <antai12232931@outlook.com>

[Anai-Guo](https://github.com/Anai-Guo)

[force-pushed](https://github.com/vllm-project/guidellm/compare/5886ab2edd38facd34e749e6a76ceeed40b66e44..8e21fc81f7db6f50372f3d74a3b033c022321ce3)the fix-mapper-no-columns-fail-fast branch from

[to](https://github.com/vllm-project/guidellm/commit/5886ab2edd38facd34e749e6a76ceeed40b66e44)

`5886ab2`


`8e21fc8`

[Compare](https://github.com/vllm-project/guidellm/compare/5886ab2edd38facd34e749e6a76ceeed40b66e44..8e21fc81f7db6f50372f3d74a3b033c022321ce3)

June 17, 2026 07:09

Addresses review: preserve the original message wording per maintainer request, only changing the warning into a fatal ValueError. Signed-off-by: Anai-Guo <antai12232931@anaiguo.com> Signed-off-by: Tai An <antai12232931@outlook.com>

|
Thanks |

|
Hi |

[Anai-Guo](https://github.com/Anai-Guo)

[force-pushed](https://github.com/vllm-project/guidellm/compare/2739382eefbf999fb15574a1a4ba88048bf8aed1..41b1efedfcc33723989a5c5e7e524b2fa7ecd615)the fix-mapper-no-columns-fail-fast branch 2 times, most recently from

[to](https://github.com/vllm-project/guidellm/commit/2739382eefbf999fb15574a1a4ba88048bf8aed1)

`2739382`


`41b1efe`

[Compare](https://github.com/vllm-project/guidellm/compare/2739382eefbf999fb15574a1a4ba88048bf8aed1..41b1efedfcc33723989a5c5e7e524b2fa7ecd615)

June 17, 2026 10:11


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jun 17, 2026


**approved these changes**

[sjmonson](https://github.com/sjmonson)Jun 17, 2026

## Merge Queue Status
This pull request spent
|

|
This failed due to Huggingface rate limiting, which has been a recurring CI issue. I re-ran the job -- I'm not sure whether mergify will continue on its own once (if) that passes... |

|
|

## Merge Queue Status
This pull request spent
|

|
|

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jun 23, 2026

[…#787]) ([vllm-project#796]) ## Summary Fixes[vllm-project#787]. When a dataset contains only columns that `GenerativeColumnMapper` has no candidate for (e.g. a single `messages` column), `setup_data` previously just logged a warning and returned an empty mapping. Every row then produced an empty result, the scheduler started but never enqueued a request, and `guidellm benchmark run` hung forever — only killed by an external timeout. This changes `setup_data` to **fail fast**: when no columns can be mapped it raises a clear `ValueError` listing the columns that were found, so the user knows to rename a column to a recognized name (e.g. `prompt`) or pass an explicit column mapping. ## Behavior ``` ValueError: GenerativeColumnMapper found no mappable columns in the dataset(s) (columns: ['messages']). Requested mappings: default mappings. Without at least one mapped column every row produces an empty result and the benchmark would hang with no requests sent. Rename a column to a recognized name (e.g. 'prompt') or pass an explicit column mapping. ``` ## Test plan - [x] Dataset with only an unmappable column (`messages`) now raises `ValueError` at setup instead of hanging. - [x] Dataset with a mappable column (`prompt`) still maps normally (`text_column` resolved). - [x] `ruff check` passes; unused `logger` import removed. 🤖 Generated with [Claude Code]([https://claude.com/claude-code]) --- # git log commit[Author: Tai An <antai12232931@outlook.com> Date: Tue Jun 16 10:08:45 2026 +0000 fix(data): fail fast when no mappable columns are found GenerativeColumnMapper.setup_data only logged a warning when a dataset had no mappable columns, then returned an empty mapping. Every row then produced an empty result, the scheduler started but never enqueued any request, and the benchmark hung forever (only killed by an external timeout). Raise a clear ValueError at setup time instead, listing the dataset columns that were found so the user knows to rename a column to a recognized name (e.g. 'prompt') or pass an explicit column mapping. Fixes]abd7626[vllm-project#787]Signed-off-by: Tai An <antai12232931@outlook.com> commit[Author: Tai An <antai12232931@outlook.com> Date: Tue Jun 16 16:08:49 2026 +0000 fix(data): normalize line endings to LF Signed-off-by: Tai An <antai12232931@outlook.com> commit]b79d0bc[Author: Tai An <antai12232931@outlook.com> Date: Tue Jun 16 19:07:07 2026 +0000 fix(data): add trailing newline to satisfy ruff format and EOF fixer Signed-off-by: Tai An <antai12232931@outlook.com> commit]90d11ed[Author: Tai An <antai12232931@outlook.com> Date: Wed Jun 17 01:03:12 2026 +0000 fix(data): keep concise no-columns error message per review Drop the verbose column listing and hang explanation; raise a short ValueError as requested. Signed-off-by: Tai An <antai12232931@outlook.com> commit]27f298f[Author: Tai An <antai12232931@outlook.com> Date: Wed Jun 17 07:09:30 2026 +0000 style: add trailing newline to mappers.py (end-of-file-fixer + ruff format) Signed-off-by: Tai An <antai12232931@outlook.com> commit]afa5b26[Author: Tai An <antai12232931@outlook.com> Date: Wed Jun 17 10:03:15 2026 +0000 fix(data): keep original warning message text when raising ValueError Addresses review: preserve the original message wording per maintainer request, only changing the warning into a fatal ValueError. Signed-off-by: Anai-Guo <antai12232931@anaiguo.com> Signed-off-by: Tai An <antai12232931@outlook.com> --------- Signed-off-by: Tai An <antai12232931@outlook.com>]41b1efe

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jun 24, 2026

[…#787]) ([vllm-project#796]) ## Summary Fixes[vllm-project#787]. When a dataset contains only columns that `GenerativeColumnMapper` has no candidate for (e.g. a single `messages` column), `setup_data` previously just logged a warning and returned an empty mapping. Every row then produced an empty result, the scheduler started but never enqueued a request, and `guidellm benchmark run` hung forever — only killed by an external timeout. This changes `setup_data` to **fail fast**: when no columns can be mapped it raises a clear `ValueError` listing the columns that were found, so the user knows to rename a column to a recognized name (e.g. `prompt`) or pass an explicit column mapping. ## Behavior ``` ValueError: GenerativeColumnMapper found no mappable columns in the dataset(s) (columns: ['messages']). Requested mappings: default mappings. Without at least one mapped column every row produces an empty result and the benchmark would hang with no requests sent. Rename a column to a recognized name (e.g. 'prompt') or pass an explicit column mapping. ``` ## Test plan - [x] Dataset with only an unmappable column (`messages`) now raises `ValueError` at setup instead of hanging. - [x] Dataset with a mappable column (`prompt`) still maps normally (`text_column` resolved). - [x] `ruff check` passes; unused `logger` import removed. 🤖 Generated with [Claude Code]([https://claude.com/claude-code]) --- # git log commit[Author: Tai An <antai12232931@outlook.com> Date: Tue Jun 16 10:08:45 2026 +0000 fix(data): fail fast when no mappable columns are found GenerativeColumnMapper.setup_data only logged a warning when a dataset had no mappable columns, then returned an empty mapping. Every row then produced an empty result, the scheduler started but never enqueued any request, and the benchmark hung forever (only killed by an external timeout). Raise a clear ValueError at setup time instead, listing the dataset columns that were found so the user knows to rename a column to a recognized name (e.g. 'prompt') or pass an explicit column mapping. Fixes]abd7626[vllm-project#787]Signed-off-by: Tai An <antai12232931@outlook.com> commit[Author: Tai An <antai12232931@outlook.com> Date: Tue Jun 16 16:08:49 2026 +0000 fix(data): normalize line endings to LF Signed-off-by: Tai An <antai12232931@outlook.com> commit]b79d0bc[Author: Tai An <antai12232931@outlook.com> Date: Tue Jun 16 19:07:07 2026 +0000 fix(data): add trailing newline to satisfy ruff format and EOF fixer Signed-off-by: Tai An <antai12232931@outlook.com> commit]90d11ed[Author: Tai An <antai12232931@outlook.com> Date: Wed Jun 17 01:03:12 2026 +0000 fix(data): keep concise no-columns error message per review Drop the verbose column listing and hang explanation; raise a short ValueError as requested. Signed-off-by: Tai An <antai12232931@outlook.com> commit]27f298f[Author: Tai An <antai12232931@outlook.com> Date: Wed Jun 17 07:09:30 2026 +0000 style: add trailing newline to mappers.py (end-of-file-fixer + ruff format) Signed-off-by: Tai An <antai12232931@outlook.com> commit]afa5b26[Author: Tai An <antai12232931@outlook.com> Date: Wed Jun 17 10:03:15 2026 +0000 fix(data): keep original warning message text when raising ValueError Addresses review: preserve the original message wording per maintainer request, only changing the warning into a fatal ValueError. Signed-off-by: Anai-Guo <antai12232931@anaiguo.com> Signed-off-by: Tai An <antai12232931@outlook.com> --------- Signed-off-by: Tai An <antai12232931@outlook.com>]41b1efe

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jul 6, 2026

[…#787]) ([vllm-project#796]) ## Summary Fixes[vllm-project#787]. When a dataset contains only columns that `GenerativeColumnMapper` has no candidate for (e.g. a single `messages` column), `setup_data` previously just logged a warning and returned an empty mapping. Every row then produced an empty result, the scheduler started but never enqueued a request, and `guidellm benchmark run` hung forever — only killed by an external timeout. This changes `setup_data` to **fail fast**: when no columns can be mapped it raises a clear `ValueError` listing the columns that were found, so the user knows to rename a column to a recognized name (e.g. `prompt`) or pass an explicit column mapping. ## Behavior ``` ValueError: GenerativeColumnMapper found no mappable columns in the dataset(s) (columns: ['messages']). Requested mappings: default mappings. Without at least one mapped column every row produces an empty result and the benchmark would hang with no requests sent. Rename a column to a recognized name (e.g. 'prompt') or pass an explicit column mapping. ``` ## Test plan - [x] Dataset with only an unmappable column (`messages`) now raises `ValueError` at setup instead of hanging. - [x] Dataset with a mappable column (`prompt`) still maps normally (`text_column` resolved). - [x] `ruff check` passes; unused `logger` import removed. 🤖 Generated with [Claude Code]([https://claude.com/claude-code]) --- # git log commit[Author: Tai An <antai12232931@outlook.com> Date: Tue Jun 16 10:08:45 2026 +0000 fix(data): fail fast when no mappable columns are found GenerativeColumnMapper.setup_data only logged a warning when a dataset had no mappable columns, then returned an empty mapping. Every row then produced an empty result, the scheduler started but never enqueued any request, and the benchmark hung forever (only killed by an external timeout). Raise a clear ValueError at setup time instead, listing the dataset columns that were found so the user knows to rename a column to a recognized name (e.g. 'prompt') or pass an explicit column mapping. Fixes]abd7626[vllm-project#787]Signed-off-by: Tai An <antai12232931@outlook.com> commit[Author: Tai An <antai12232931@outlook.com> Date: Tue Jun 16 16:08:49 2026 +0000 fix(data): normalize line endings to LF Signed-off-by: Tai An <antai12232931@outlook.com> commit]b79d0bc[Author: Tai An <antai12232931@outlook.com> Date: Tue Jun 16 19:07:07 2026 +0000 fix(data): add trailing newline to satisfy ruff format and EOF fixer Signed-off-by: Tai An <antai12232931@outlook.com> commit]90d11ed[Author: Tai An <antai12232931@outlook.com> Date: Wed Jun 17 01:03:12 2026 +0000 fix(data): keep concise no-columns error message per review Drop the verbose column listing and hang explanation; raise a short ValueError as requested. Signed-off-by: Tai An <antai12232931@outlook.com> commit]27f298f[Author: Tai An <antai12232931@outlook.com> Date: Wed Jun 17 07:09:30 2026 +0000 style: add trailing newline to mappers.py (end-of-file-fixer + ruff format) Signed-off-by: Tai An <antai12232931@outlook.com> commit]afa5b26[Author: Tai An <antai12232931@outlook.com> Date: Wed Jun 17 10:03:15 2026 +0000 fix(data): keep original warning message text when raising ValueError Addresses review: preserve the original message wording per maintainer request, only changing the warning into a fatal ValueError. Signed-off-by: Anai-Guo <antai12232931@anaiguo.com> Signed-off-by: Tai An <antai12232931@outlook.com> --------- Signed-off-by: Tai An <antai12232931@outlook.com>]41b1efe

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

Fixes #787.

When a dataset contains only columns that

`GenerativeColumnMapper`

has no candidate for (e.g. a single`messages`

column),`setup_data`

previously just logged a warning and returned an empty mapping. Every row then produced an empty result, the scheduler started but never enqueued a request, and`guidellm benchmark run`

hung forever — only killed by an external timeout.This changes

`setup_data`

tofail fast: when no columns can be mapped it raises a clear`ValueError`

listing the columns that were found, so the user knows to rename a column to a recognized name (e.g.`prompt`

) or pass an explicit column mapping.## Behavior

## Test plan

`messages`

) now raises`ValueError`

at setup instead of hanging.`prompt`

) still maps normally (`text_column`

resolved).`ruff check`

passes; unused`logger`

import removed.🤖 Generated with Claude Code

## git log

commit

abd7626Author: Tai An antai12232931@outlook.com

Date: Tue Jun 16 10:08:45 2026 +0000

commit

b79d0bcAuthor: Tai An antai12232931@outlook.com

Date: Tue Jun 16 16:08:49 2026 +0000

commit

90d11edAuthor: Tai An antai12232931@outlook.com

Date: Tue Jun 16 19:07:07 2026 +0000

commit

27f298fAuthor: Tai An antai12232931@outlook.com

Date: Wed Jun 17 01:03:12 2026 +0000

commit

afa5b26Author: Tai An antai12232931@outlook.com

Date: Wed Jun 17 07:09:30 2026 +0000

commit

41b1efeAuthor: Tai An antai12232931@outlook.com

Date: Wed Jun 17 10:03:15 2026 +0000

Signed-off-by: Tai An antai12232931@outlook.com