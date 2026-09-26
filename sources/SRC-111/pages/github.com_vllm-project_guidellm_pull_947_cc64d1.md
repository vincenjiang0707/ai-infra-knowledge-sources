source: https://github.com/vllm-project/guidellm/pull/947

# bug(openai): support structured chat content metadata for OpenAI backend endpoint - #947

[mergify[bot]](https://github.com/mergify[bot])merged 4 commits into

## Conversation

…tions ([vllm-project#940]) Models like `google/translategemma-12b-it` require structured text content objects with extra metadata fields (e.g., `source_lang_code` and `target_lang_code`) in `/v1/chat/completions` requests. Without these fields, server-side Jinja chat templates fail with HTTP 400 errors. This change adds support for appending custom metadata fields into structured chat content objects: - Added `content_extra_fields` to `OpenAIHTTPBackendArgs` and forwarded it to `ChatCompletionsRequestHandler._format_prompts()`. - Added the generic `--append-payloads` CLI option to pass key-value metadata. - Enabled preservation of dictionary prompt objects from custom dataset rows in `text_column`. - Updated `GenerativeRequestFinalizer.finalize_turn()` to safely extract string content from dictionary prompts when computing character and word usage metrics. - Added comprehensive unit test coverage under `tests/unit/backends/openai/` and `tests/unit/data/`. Resolves[vllm-project#940]Signed-off-by: prasanna <prasannajaga9@gmail.com>


**reviewed**

[chatgpt-codex-connector](https://github.com/apps/chatgpt-codex-connector)BotJul 22, 2026

###
**
**[chatgpt-codex-connector](https://github.com/apps/chatgpt-codex-connector)
Bot
left a comment

**left a comment**

[chatgpt-codex-connector](https://github.com/apps/chatgpt-codex-connector)Bot

There was a problem hiding this comment.

### 💡 Codex Review

Here are some automated review suggestions for this pull request.

**Reviewed commit:** `7fabc22c84`


## ℹ️ About Codex in GitHub

[Your team has set up Codex to review pull requests in this repo](https://chatgpt.com/codex/cloud/settings/general). Reviews are triggered when you

- Open a pull request for review
- Mark a draft as ready
- Comment "
[@codex](https://github.com/codex)review".

If Codex has suggestions, it will comment; otherwise it will react with 👍.

Codex can also answer questions or update the PR. Try commenting "[@codex](https://github.com/codex) address that feedback".

[src/guidellm/data/finalizers/generative.py](https://github.com/vllm-project/guidellm/pull/947/files/7fabc22c84a953ff5187af27a90d2f8e379ffc13#diff-e70f1c8bcc23137c7f16b0f094c43c2a3172464840b8dfef39a9ef42bce73f34)Outdated


**requested changes**

[dbutenhof](https://github.com/dbutenhof)Jul 23, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

I'm still evaluating some of the changes, but I'm going to put out a few high level comments first.

[src/guidellm/cli/run.py](https://github.com/vllm-project/guidellm/pull/947/files/7fabc22c84a953ff5187af27a90d2f8e379ffc13#diff-8271358a00cc5c197bc1d6039dd935cfc7eb21b1f1facac60fb9d325f1129918)Outdated

[src/guidellm/backends/openai/http.py](https://github.com/vllm-project/guidellm/pull/947/files/7fabc22c84a953ff5187af27a90d2f8e379ffc13#diff-6a56e17b4a9b1b702100f54acf336f97d4de6346ea9f696bb23602d12c1f0002)Outdated

[src/guidellm/cli/run.py](https://github.com/vllm-project/guidellm/pull/947/files/7fabc22c84a953ff5187af27a90d2f8e379ffc13#diff-8271358a00cc5c197bc1d6039dd935cfc7eb21b1f1facac60fb9d325f1129918)Outdated


**requested changes**

[dbutenhof](https://github.com/dbutenhof)Jul 23, 2026

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/947/files/7fabc22c84a953ff5187af27a90d2f8e379ffc13#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated

[src/guidellm/backends/openai/http.py](https://github.com/vllm-project/guidellm/pull/947/files/7fabc22c84a953ff5187af27a90d2f8e379ffc13#diff-6a56e17b4a9b1b702100f54acf336f97d4de6346ea9f696bb23602d12c1f0002)Outdated


[dbutenhof](https://github.com/dbutenhof)added

[community contribution](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3A%22community%20contribution%22)

[feature](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Afeature)

Jul 24, 2026

|
Hi |

Replace --append-payloads and structured dataset prompt metadata with backend extras.content. Apply the configured fields to generated text content for Chat Completions and Responses, including conversation history. Co-Authored-By: Prasanna <123716600+Prasannajaga@users.noreply.github.com> Signed-off-by: prasanna <prasannajaga9@gmail.com>

[Prasannajaga](https://github.com/Prasannajaga)

[force-pushed](https://github.com/vllm-project/guidellm/compare/6e7331c2da8dc26128db0df5a715365c9ea5b1ae..ccd9a479a5bf547c31c683eba555197432043681)the bug/gemma-payload-upgrade branch from

[to](https://github.com/vllm-project/guidellm/commit/6e7331c2da8dc26128db0df5a715365c9ea5b1ae)

`6e7331c`


`ccd9a47`

[Compare](https://github.com/vllm-project/guidellm/compare/6e7331c2da8dc26128db0df5a715365c9ea5b1ae..ccd9a479a5bf547c31c683eba555197432043681)

July 27, 2026 16:33

[src/guidellm/schemas/request.py](https://github.com/vllm-project/guidellm/pull/947/files/ccd9a479a5bf547c31c683eba555197432043681#diff-9257f47eca60528ee4d982b23ddd3a59847b18591b36768dccd41bc1cb1cb3d0)Outdated

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/947/files/ccd9a479a5bf547c31c683eba555197432043681#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated

Signed-off-by: prasanna <prasannajaga9@gmail.com>

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/947/files/4fd5f21650c8d041b785e7d962a56f43ed32b086#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated

Signed-off-by: prasanna <prasannajaga9@gmail.com>


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jul 29, 2026


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jul 29, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

Sometimes I wish Python had Javascript's `?.`

operator!

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

GuideLLM right now doesn't support structured chat content objects for models like

`google/translategemma-12b-it`

that require additional metadata fields (such as`source_lang_code`

and`target_lang_code`

) in`/v1/chat/completions`

requests. Without these fields, Jinja chat templates on inference servers fail with HTTP 400 errors (`'dict object' has no attribute ...`

).This PR details the design and implementation for supporting extra metadata fields directly in chat content objects as mentioned in issue #940. It provides:

CLI / Backend Configuration: A generic`--append-payloads`

option (and backend argument`content_extra_fields`

) to specify extra fields to inject into chat completion requests for any model or endpoint.Custom Dataset Support: Preservation of dictionary prompt objects from custom dataset rows in`text_column`

so dynamic, per-prompt metadata can be passed.## Applied Changes

## [MODIFY] http.py

`content_extra_fields: dict[str, Any] | None`

to`OpenAIHTTPBackendArgs`

.`content_extra_fields`

from backend configuration to`request_handler.format(...)`

in`_prepare_resolve_request`

.## [MODIFY] request_handlers.py

`ChatCompletionsRequestHandler.format()`

and`_format_prompts()`

to inject`content_extra_fields`

into text content objects.`text_column`

.## [MODIFY] run.py

`--append-payloads`

CLI option to append key-value fields to structured content objects in chat completion requests.## [MODIFY] generative.py

`GenerativeRequestFinalizer.finalize_turn()`

to ensure word and character metric calculation works for dictionary inputs.## [NEW] Unit Tests

`tests/unit/backends/openai/test_request_handlers.py`

: Added tests verifying`content_extra_fields`

injection and dictionary item preservation in chat completions format.`tests/unit/backends/openai/test_http.py`

: Added tests verifying backend argument handling and request resolution.`tests/unit/data/test_finalizers.py`

: Added tests for`GenerativeRequestFinalizer`

with dictionary prompt items.## Alternatives Considered:

(Empty)## Test Verified

`tox -e test-unit`

,`tox -e lint-check`

, and`tox -e type-check`

. All tests passed.## Related Issues

## Use of AI

## git log

commit

7fabc22Author: prasanna prasannajaga9@gmail.com

Date: Thu Jul 23 00:44:32 2026 +0530

commit

ccd9a47Author: prasanna prasannajaga9@gmail.com

Date: Mon Jul 27 21:46:39 2026 +0530

commit

4fd5f21Author: prasanna prasannajaga9@gmail.com

Date: Tue Jul 28 09:11:24 2026 +0530

commit

cec9221Author: prasanna prasannajaga9@gmail.com

Date: Wed Jul 29 12:24:05 2026 +0530

Co-Authored-By: Prasanna 123716600+Prasannajaga@users.noreply.github.com

Signed-off-by: prasanna prasannajaga9@gmail.com