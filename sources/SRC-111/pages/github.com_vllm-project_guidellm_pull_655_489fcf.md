source: https://github.com/vllm-project/guidellm/pull/655

# Basic Responses API Support - #655

Merged

[jaredoconnell](https://github.com/jaredoconnell)merged 10 commits into

Merged

## Conversation


**requested changes**

[sjmonson](https://github.com/sjmonson)Mar 25, 2026

[src/guidellm/backends/openai/http.py](https://github.com/vllm-project/guidellm/pull/655/files#diff-6a56e17b4a9b1b702100f54acf336f97d4de6346ea9f696bb23602d12c1f0002)Outdated

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/655/files#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/655/files#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/655/files#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated

[src/guidellm/mock_server/handlers/responses.py](https://github.com/vllm-project/guidellm/pull/655/files#diff-ff1412d314b96cbf240223b119175281e62cdcdb871806ecee6f61ab9e1e2084)Outdated

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/655/files#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated


**previously approved these changes**

[dbutenhof](https://github.com/dbutenhof)Mar 26, 2026

[tests/unit/backends/openai/test_request_handlers.py](https://github.com/vllm-project/guidellm/pull/655/files#diff-3286b6da9cffd79259ed9c187e72530fdb2f407c0454af81bfc5c28a79045faa)


**previously approved these changes**

[sjmonson](https://github.com/sjmonson)Mar 26, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)
Collaborator


There was a problem hiding this comment.

LGTM I was able to run a few simple tests to confirm its working.

Basic support was added to both the backend handler and the mock server. Generated-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Generated-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Co-authored-by: Samuel Monson <smonson@irbash.net> Signed-off-by: Jared O'Connell <46976761+jaredoconnell@users.noreply.github.com>

Co-authored-by: Samuel Monson <smonson@irbash.net> Signed-off-by: Jared O'Connell <46976761+jaredoconnell@users.noreply.github.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>

[jaredoconnell](https://github.com/jaredoconnell)

[force-pushed](https://github.com/vllm-project/guidellm/compare/b94ef35d9e32ec9ff37143c4c8e52e27746ae475..119447150e418658d4008d88df775ea5be98b5e7)the feat/responses-api branch from

[to](https://github.com/vllm-project/guidellm/commit/b94ef35d9e32ec9ff37143c4c8e52e27746ae475)

`b94ef35`


`1194471`

[Compare](https://github.com/vllm-project/guidellm/compare/b94ef35d9e32ec9ff37143c4c8e52e27746ae475..119447150e418658d4008d88df775ea5be98b5e7)

March 26, 2026 19:16


**approved these changes**

[sjmonson](https://github.com/sjmonson)Mar 26, 2026


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Mar 26, 2026

5 tasks

[mergify](https://github.com/apps/mergify)Bot pushed a commit that referenced this pull request

Sep 9, 2026

## Summary When a Responses API stream emits partial text followed by `response.failed` containing a non-empty `response.error`, GuideLLM returns the partial text as a normal `GenerationResponse`. If no text arrived, it instead raises the generic `UNUSABLE_BACKEND_RESPONSE` error, losing the server's failure message. The [documented failure event]([https://developers.openai.com/api/reference/resources/responses/streaming-events#response.failed]) carries its error inside `response`, which the existing top-level SSE error check does not inspect. ## Details - [x] Apply the existing `_check_streaming_error` helper to the nested response of a `response.failed` event, surfacing its error as `ValueError` through the normal request-failure path. - [x] Add six parametrized `backend.resolve()` cases using the real Responses handler and mocked HTTP transport: explicit failures with and without partial text, failed events with null/empty errors, and completed/incomplete controls. The terminal-event tests introduced in[#655]intentionally preserve partial output for failed events without an error payload. Those cases still pass. This change only raises for an explicit non-empty nested error on `response.failed`; it preserves the existing incomplete-event behavior. ## Test Plan - Before the fix: two new regression cases failed and four controls passed. After partial text, the expected exception was absent; without partial text, the wrong generic error was raised. - `tox -e tests -- tests/unit/backends/openai`: 330 passed, including existing failed/incomplete terminal-event tests. - Full `tox -e tests`: 3,065 passed, 31 skipped, 188 xfailed; 14 audio-test failures and one realtime-WebSocket setup error because this environment cannot load `libtorchcodec`/FFmpeg shared libraries. Re-running both affected test files with unmodified main sources in the same tox environment reproduces all 14 failures and the setup error. - `tox -e lint-check` and `tox -e type-check`: passed (222 source files for type checking). - `uv run --no-project --python .tox/tests/bin/python pre-commit run --files src/guidellm/backends/openai/request_handlers.py tests/unit/backends/openai/test_http.py`: passed. - Independent localhost HTTP verification through `process_startup()` and `backend.resolve()`: both explicit-failure cases now raise `ValueError` containing the server message; failed events without an error or with a null error, completed events, and incomplete events all retain partial text. The partial-text failure was reproduced before applying the fix. ## Related Issues - Related:[#743]and[#795]established propagation of top-level streaming errors; this addresses the nested error carried by the Responses terminal event. --- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [x] Includes code generated or substantially modified by an AI agent - [x] Includes tests generated or substantially modified by an AI agent Code and tests were generated with OpenAI Codex; the commit includes a `Generated-by` trailer. --- # git log commit[Author: git-jxj <65210887+git-jxj@users.noreply.github.com> Date: Wed Sep 9 15:40:50 2026 +0800 fix(openai): surface nested Responses streaming errors Propagate explicit response.failed errors while retaining terminal events without an error payload. Generated-by: OpenAI Codex Signed-off-by: git-jxj <65210887+git-jxj@users.noreply.github.com> --------- Generated-by: OpenAI Codex Signed-off-by: git-jxj <65210887+git-jxj@users.noreply.github.com>]4077f20

6 tasks

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

This PR adds basic support for the responses API.

It does not add support for features often associated with the responses API, like tool calling.

## Details

## Test Plan

Start vLLM, and run GuideLLM with

`--request-format /v1/responses`

Example command:

## Related Issues

## Use of AI

`## WRITTEN BY AI ##`

)