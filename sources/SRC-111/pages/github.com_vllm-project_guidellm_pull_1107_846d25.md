source: https://github.com/vllm-project/guidellm/pull/1107

# fix(openai): surface nested Responses streaming errors - #1107

Merged

[mergify[bot]](https://github.com/mergify[bot])merged 1 commit into

Merged

## Conversation

Propagate explicit response.failed errors while retaining terminal events without an error payload. Generated-by: OpenAI Codex Signed-off-by: git-jxj <65210887+git-jxj@users.noreply.github.com>


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Sep 9, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

This looks reasonable, and does match the documentation link.

Contributor

|
Queued — the merge queue status continues in |


**approved these changes**

[sjmonson](https://github.com/sjmonson)Sep 9, 2026

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

35 tasks

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

When a Responses API stream emits partial text followed by

`response.failed`

containing a non-empty`response.error`

, GuideLLM returns the partial text as a normal`GenerationResponse`

. If no text arrived, it instead raises the generic`UNUSABLE_BACKEND_RESPONSE`

error, losing the server's failure message. The documented failure event carries its error inside`response`

, which the existing top-level SSE error check does not inspect.## Details

`_check_streaming_error`

helper to the nested response of a`response.failed`

event, surfacing its error as`ValueError`

through the normal request-failure path.`backend.resolve()`

cases using the real Responses handler and mocked HTTP transport: explicit failures with and without partial text, failed events with null/empty errors, and completed/incomplete controls.The terminal-event tests introduced in #655 intentionally preserve partial output for failed events without an error payload. Those cases still pass. This change only raises for an explicit non-empty nested error on

`response.failed`

; it preserves the existing incomplete-event behavior.## Test Plan

`tox -e tests -- tests/unit/backends/openai`

: 330 passed, including existing failed/incomplete terminal-event tests.`tox -e tests`

: 3,065 passed, 31 skipped, 188 xfailed; 14 audio-test failures and one realtime-WebSocket setup error because this environment cannot load`libtorchcodec`

/FFmpeg shared libraries. Re-running both affected test files with unmodified main sources in the same tox environment reproduces all 14 failures and the setup error.`tox -e lint-check`

and`tox -e type-check`

: passed (222 source files for type checking).`uv run --no-project --python .tox/tests/bin/python pre-commit run --files src/guidellm/backends/openai/request_handlers.py tests/unit/backends/openai/test_http.py`

: passed.`process_startup()`

and`backend.resolve()`

: both explicit-failure cases now raise`ValueError`

containing the server message; failed events without an error or with a null error, completed events, and incomplete events all retain partial text. The partial-text failure was reproduced before applying the fix.## Related Issues

## Use of AI

Code and tests were generated with OpenAI Codex; the commit includes a

`Generated-by`

trailer.## git log

commit

4077f20Author: git-jxj 65210887+git-jxj@users.noreply.github.com

Date: Wed Sep 9 15:40:50 2026 +0800

Generated-by: OpenAI Codex

Signed-off-by: git-jxj 65210887+git-jxj@users.noreply.github.com