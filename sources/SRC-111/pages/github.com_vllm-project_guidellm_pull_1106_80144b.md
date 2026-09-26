source: https://github.com/vllm-project/guidellm/pull/1106

# fix(openai): accept SSE DONE markers without a space - #1106

Merged

[mergify[bot]](https://github.com/mergify[bot])merged 1 commit into

Merged

## Conversation

Recognize the terminator after extracting the data value in both streaming parsers. Generated-by: OpenAI Codex Signed-off-by: git-jxj <65210887+git-jxj@users.noreply.github.com>


**approved these changes**

[sjmonson](https://github.com/sjmonson)Sep 9, 2026

Contributor

|
Queued — the merge queue status continues in |


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Sep 9, 2026

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

35 tasks

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

A streaming server can return valid generated text followed by

`data:[DONE]`

, but GuideLLM attempts to JSON-decode the terminator and raises`JSONDecodeError`

. The SSE specification makes the space after the colon optional, so this should behave like`data: [DONE]`

.## Details

`[DONE]`

after the existing data-prefix removal and whitespace normalization in the text completions and Responses handlers. Chat completions inherits the text handler's parser.## Test Plan

`JSONDecodeError`

; the other 15 selected cases passed.`tox -e tests -- tests/unit/backends/openai`

: 326 passed.`tox -e tests`

: 3,061 passed, 31 skipped, 188 xfailed; 14 audio-test failures and one realtime-WebSocket setup error because this environment cannot load`libtorchcodec`

/FFmpeg shared libraries. Both affected test files reproduce the same 14 failures and one error with unmodified main sources.`tox -e lint-check`

: passed.`tox -e type-check`

: passed, 222 source files.`uv run --no-project --python .tox/tests/bin/python pre-commit run --files src/guidellm/backends/openai/request_handlers.py tests/unit/backends/openai/test_request_handlers.py`

: passed.`OpenAIHTTPBackend.process_startup()`

and`backend.resolve()`

:`/v1/completions`

,`/v1/chat/completions`

, and`/v1/responses`

each return`Hello`

for both DONE spellings (six cases).## Related Issues

## Use of AI

Code and tests were generated with OpenAI Codex; the commit includes a

`Generated-by`

trailer.## git log

commit

f2b4acaAuthor: git-jxj 65210887+git-jxj@users.noreply.github.com

Date: Wed Sep 9 15:30:28 2026 +0800

Generated-by: OpenAI Codex

Signed-off-by: git-jxj 65210887+git-jxj@users.noreply.github.com