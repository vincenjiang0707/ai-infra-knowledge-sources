source: https://github.com/vllm-project/guidellm/pull/1142

# Fix invalid format placeholder in mock server error logging - #1142

Merged

[mergify[bot]](https://github.com/mergify[bot])merged 1 commit into

Merged

## Conversation

Contributor

|
Hi |

`generic_error_handler` logged unhandled exceptions with `logger.error("Unhandled exception: {}", exception)`. The `logger` is a stdlib `logging.Logger`, which expects `%s`-style placeholders, not `{}`. Every unhandled exception therefore raised a secondary `TypeError` from inside the logging module itself, burying the real traceback under logging-internals noise. Change `{}` to `%s` so the exception logs cleanly. Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com> Generated-by: Claude Sonnet 5 Signed-off-by: Tayo Ogunbiyi <eyitayoogunbiyi@gmail.com>

[tayoogunbiyi](https://github.com/tayoogunbiyi)

[force-pushed](https://github.com/vllm-project/guidellm/compare/2847a029b0c236ad0d91fe8beaaf04c84de866b9..2de9ef7c4c1005cb9ec129fe66a76f6c570763af)the fix/mock-server-logger-format branch from

[to](https://github.com/vllm-project/guidellm/commit/2847a029b0c236ad0d91fe8beaaf04c84de866b9)

`2847a02`


`2de9ef7`

[Compare](https://github.com/vllm-project/guidellm/compare/2847a029b0c236ad0d91fe8beaaf04c84de866b9..2de9ef7c4c1005cb9ec129fe66a76f6c570763af)

September 12, 2026 11:14


**approved these changes**

[sjmonson](https://github.com/sjmonson)Sep 14, 2026

Contributor

|
Queued — the merge queue status continues in |


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Sep 14, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

Awkward having the "guidellm" code base (even though the mock server is logically separate) split between two different logging formatter styles. Ah, well.

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

35 tasks

3 tasks

[PatilHrushikesh](https://github.com/PatilHrushikesh)pushed a commit to PatilHrushikesh/guidellm that referenced this pull request

Sep 21, 2026

[…ject#1142]) ## Summary Fixes an invalid log format placeholder in the mock server's generic exception handler so unhandled exceptions log cleanly instead of raising a secondary `TypeError` from inside the logging module. ## Details - [x] `generic_error_handler` in `src/guidellm/mock_server/server.py` logged unhandled exceptions with `logger.error("Unhandled exception: {}", exception)`. `logger` is `sanic.log.logger`, which expects `%s`-style placeholders. - [x] Changed `{}` to `%s` so the exception logs cleanly. The JSON 500 response returned to the client is unaffected either way. ## Test Plan - Called `logger.error("Unhandled exception: %s", exception)` directly against `sanic.log.logger` and confirmed it formats cleanly with no `TypeError`. - `tox -e lint-check` - `tox -e type-check` ## Related Issues - Resolves # --- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [x] Includes code generated or substantially modified by an AI agent - [ ] Includes tests generated or substantially modified by an AI agent --- # git log commit[Author: Tayo Ogunbiyi <eyitayoogunbiyi@gmail.com> Date: Sat Sep 12 11:52:06 2026 +0100 Fix invalid format placeholder in mock server error logging `generic_error_handler` logged unhandled exceptions with `logger.error("Unhandled exception: {}", exception)`. The `logger` is a stdlib `logging.Logger`, which expects `%s`-style placeholders, not `{}`. Every unhandled exception therefore raised a secondary `TypeError` from inside the logging module itself, burying the real traceback under logging-internals noise. Change `{}` to `%s` so the exception logs cleanly. Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com> Generated-by: Claude Sonnet 5 Signed-off-by: Tayo Ogunbiyi <eyitayoogunbiyi@gmail.com> --------- Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com> Generated-by: Claude Sonnet 5 Signed-off-by: Tayo Ogunbiyi <eyitayoogunbiyi@gmail.com>]2de9ef7

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Fixes an invalid log format placeholder in the mock server's generic exception


handler so unhandled exceptions log cleanly instead of raising a secondary

`TypeError`

from inside the logging module.## Details

`generic_error_handler`

in`src/guidellm/mock_server/server.py`

logged unhandled exceptions with`logger.error("Unhandled exception: {}", exception)`

.`logger`

is`sanic.log.logger`

, which expects`%s`

-style placeholders.`{}`

to`%s`

so the exception logs cleanly. The JSON 500 response returned to the client is unaffected either way.## Test Plan

`logger.error("Unhandled exception: %s", exception)`

directly against`sanic.log.logger`

and confirmed it formats cleanly with no`TypeError`

.`tox -e lint-check`

`tox -e type-check`

## Related Issues

## Use of AI

## git log

commit

2de9ef7Author: Tayo Ogunbiyi eyitayoogunbiyi@gmail.com

Date: Sat Sep 12 11:52:06 2026 +0100

Co-Authored-By: Claude Sonnet 5 noreply@anthropic.com

Generated-by: Claude Sonnet 5

Signed-off-by: Tayo Ogunbiyi eyitayoogunbiyi@gmail.com