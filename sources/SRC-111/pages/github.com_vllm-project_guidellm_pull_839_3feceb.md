source: https://github.com/vllm-project/guidellm/pull/839

# Fix tool call turn sequence and add improved support for server tool calls - #839

[mergify[bot]](https://github.com/mergify[bot])merged 12 commits into

## Conversation


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Jun 23, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

I haven't gotten to the code, but a few doc comments rather than make them sit and wait for me to finish updating the cli doc PR...

[docs/guides/tool_calling.md](https://github.com/vllm-project/guidellm/pull/839/files#diff-61af4f8d78e766b599dc58cd80c99c7b4be40899e4726feaf6deb3819f4a658b)Outdated

[docs/guides/tool_calling.md](https://github.com/vllm-project/guidellm/pull/839/files#diff-61af4f8d78e766b599dc58cd80c99c7b4be40899e4726feaf6deb3819f4a658b)Outdated


**previously approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jun 24, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

I haven't pulled this to try running it ... but it looks plausible enough.

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/839/files#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated

[src/guidellm/schemas/request.py](https://github.com/vllm-project/guidellm/pull/839/files#diff-9257f47eca60528ee4d982b23ddd3a59847b18591b36768dccd41bc1cb1cb3d0)Outdated

|
Queued — the merge queue status continues in |


[dbutenhof](https://github.com/dbutenhof)added

[internal](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Ainternal)

[feature](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Afeature)

Jun 25, 2026

[src/guidellm/data/preprocessors/mappers.py](https://github.com/vllm-project/guidellm/pull/839/files#diff-2099c62bd0e1315d94f5ca565b50198a0507b9f2818feba33fd14d29641e6deb)


**requested changes**

[sjmonson](https://github.com/sjmonson)Jun 30, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

Still pending a full review but here is a start.

[src/guidellm/data/deserializers/synthetic.py](https://github.com/vllm-project/guidellm/pull/839/files#diff-4b48dc7631c1a28d1f1b7ca179feb42d01378082bc7c9b97bf3cd4bcc2c58a94)Outdated

[src/guidellm/data/deserializers/synthetic.py](https://github.com/vllm-project/guidellm/pull/839/files#diff-4b48dc7631c1a28d1f1b7ca179feb42d01378082bc7c9b97bf3cd4bcc2c58a94)Outdated

[sjmonson](https://github.com/sjmonson)self-requested a review

June 30, 2026 19:33

[jaredoconnell](https://github.com/jaredoconnell)

[force-pushed](https://github.com/vllm-project/guidellm/compare/747de9d4a976a50e8dd0d9504722e83cbd0ee015..453335592d9ec44a756fe09015ed23bf731bb0d1)the fix/tool-call-sequence branch from

[to](https://github.com/vllm-project/guidellm/commit/747de9d4a976a50e8dd0d9504722e83cbd0ee015)

`747de9d`


`4533355`

[Compare](https://github.com/vllm-project/guidellm/compare/747de9d4a976a50e8dd0d9504722e83cbd0ee015..453335592d9ec44a756fe09015ed23bf731bb0d1)

June 30, 2026 23:01


**requested changes**

[sjmonson](https://github.com/sjmonson)Jul 1, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

One more nit, plus a few points above have yet to be addressed.

[src/guidellm/data/finalizers/generative.py](https://github.com/vllm-project/guidellm/pull/839/files#diff-e70f1c8bcc23137c7f16b0f094c43c2a3172464840b8dfef39a9ef42bce73f34)

Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Added server side tool call examples, but only touched the ones not already updated by the other documentation update PR when possible. Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Co-authored-by: Cursor <cursoragent@cursor.com> Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com> Generated-by: Cursor AI Claude Opus 4.6

Assisted-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>

[jaredoconnell](https://github.com/jaredoconnell)

[force-pushed](https://github.com/vllm-project/guidellm/compare/eba3fd7ee01fca8eed456b8c32b66cf254738f39..39ea8e277ef6878a6b9a0d40968c8f5f47cc13ef)the fix/tool-call-sequence branch from

[to](https://github.com/vllm-project/guidellm/commit/eba3fd7ee01fca8eed456b8c32b66cf254738f39)

`eba3fd7`


`39ea8e2`

[Compare](https://github.com/vllm-project/guidellm/compare/eba3fd7ee01fca8eed456b8c32b66cf254738f39..39ea8e277ef6878a6b9a0d40968c8f5f47cc13ef)

July 1, 2026 17:44


**previously approved these changes**

[sjmonson](https://github.com/sjmonson)Jul 1, 2026


**requested changes**

[dbutenhof](https://github.com/dbutenhof)Jul 1, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

Several minor errors. I think we should repair the potentially confusing `--request-format`

reference, but the others can be ignored.

[docs/guides/tool_calling.md](https://github.com/vllm-project/guidellm/pull/839/files/39ea8e277ef6878a6b9a0d40968c8f5f47cc13ef#diff-61af4f8d78e766b599dc58cd80c99c7b4be40899e4726feaf6deb3819f4a658b)Outdated

[docs/guides/tool_calling.md](https://github.com/vllm-project/guidellm/pull/839/files/39ea8e277ef6878a6b9a0d40968c8f5f47cc13ef#diff-61af4f8d78e766b599dc58cd80c99c7b4be40899e4726feaf6deb3819f4a658b)

[src/guidellm/data/deserializers/synthetic.py](https://github.com/vllm-project/guidellm/pull/839/files/39ea8e277ef6878a6b9a0d40968c8f5f47cc13ef#diff-4b48dc7631c1a28d1f1b7ca179feb42d01378082bc7c9b97bf3cd4bcc2c58a94)Outdated

Assisted-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>


**approved these changes**

[sjmonson](https://github.com/sjmonson)Jul 1, 2026


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jul 1, 2026

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jul 2, 2026

…calls ([vllm-project#839]) ## Summary Tool calling currently doesn't have a dedicated turn to tell the server what the client came up with, and this PR adds that. It also adds a turn type for a server side tool call. ## Details - This design injects an additional generation request to inject the tool call response before the next user response. - The server side tool call feature just ensures that the tool call value is not set to none for that turn. - Includes empty responses from agent in history Here is an example set of turns with the latest code using the following command: ` guidellm run --backend '{"kind": "openai_http", "target": "http://localhost:8000", "request_format": "/v1/chat/completions", "tool_call_missing_behavior": "error_stop", "server_history": false, "extras": {"body": {"chat_template_kwargs": {"enable_thinking": false}}}}' --data '{"kind": "synthetic_text", "prompt_tokens": 20, "output_tokens": 20, "turns": 4, "tool_call_turns": 1}' --constraint '{"kind": "max_requests", "count": 6}' --constraint kind=max_duration,seconds=120 --profile kind=synchronous ` ``` [USER] 1 0 Off to message interview. Yes way plan prepare dinner whom out. General sit hold. [ASSISTANT] arguments: query: 1 0 Off to message interview. Yes way plan prepare dinner whom out. General sit hold. function: get_data id: chatcmpl-tool-9286e5297bcd5feb [TOOL] tool_call_id: chatcmpl-tool-9286e5297bcd5feb {"status": "ok"} [ASSISTANT] It seems like your message is a bit unclear or fragmented. Could you please rephrase or clarify what [USER] 1 1 Above everybody well. Second have writer final agent wonder sell. Interest order control feel write [ASSISTANT] It looks like your message is still fragmented and difficult to interpret. Could you please rephrase or provide [USER] 1 2 Fine movie standard official. World deep less college right much. None bar Mr push. [ASSISTANT] It seems like your message is still unclear and fragmented. Could you please rephrase or clarify what you [USER] 1 3 Sea low especially right throw opportunity while. Beyond issue eat good season recognize. Other difference [RESPONSE] It seems like your message is still unclear and fragmented. Could you please rephrase or clarify what you ``` ## Test Plan - Run normal benchmarks - Run tool call benchmarks. - If time allows, setup a server-side tool call stack and test server side tool calling. ## Related Issues --- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [x] Includes code generated or substantially modified by an AI agent - [x] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Jared O'Connell <joconnel@redhat.com> Date: Mon Jun 22 12:37:05 2026 -0400 Add tool response turn and add server-tool-call turn type Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> commit]12b6bdb[Author: Jared O'Connell <joconnel@redhat.com> Date: Mon Jun 22 17:23:39 2026 -0400 Include empty responses in history Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> commit]59af1f2[Author: Jared O'Connell <joconnel@redhat.com> Date: Mon Jun 22 18:50:28 2026 -0400 Make tool response turns inherit proper metric settings Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> commit]1f5aaaf[Author: Jared O'Connell <joconnel@redhat.com> Date: Mon Jun 22 23:52:22 2026 -0400 Remove outdated comment Signed-off-by: Jared O'Connell <joconnel@redhat.com> commit]0c1e64f[Author: Jared O'Connell <joconnel@redhat.com> Date: Tue Jun 23 00:01:23 2026 -0400 Fix tool calling in preprocessor Signed-off-by: Jared O'Connell <joconnel@redhat.com> commit]7db3769[Author: Jared O'Connell <joconnel@redhat.com> Date: Tue Jun 23 11:39:56 2026 -0400 Add support for other dataset formats for tool calling Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> commit]97906e3[Author: Jared O'Connell <joconnel@redhat.com> Date: Tue Jun 23 13:37:12 2026 -0400 Update documentation for tool calls Added server side tool call examples, but only touched the ones not already updated by the other documentation update PR when possible. Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> commit]85958c8[Author: Jared O'Connell <joconnel@redhat.com> Date: Tue Jun 23 14:49:45 2026 -0400 Reformat test files Signed-off-by: Jared O'Connell <joconnel@redhat.com> commit]cdf917c[Author: Jared O'Connell <joconnel@redhat.com> Date: Tue Jun 30 18:16:22 2026 -0400 Revert mapper changes and related fixes Co-authored-by: Cursor <cursoragent@cursor.com> Signed-off-by: Jared O'Connell <joconnel@redhat.com> commit]ce671ff[Author: Jared O'Connell <joconnel@redhat.com> Date: Tue Jun 30 22:53:51 2026 -0400 Added tool support to mock server and tool call E2E tests Signed-off-by: Jared O'Connell <joconnel@redhat.com> Generated-by: Cursor AI Claude Opus 4.6 commit]7e035b1[Author: Jared O'Connell <joconnel@redhat.com> Date: Wed Jul 1 13:36:11 2026 -0400 Address review comments Assisted-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> commit]39ea8e2[Author: Jared O'Connell <joconnel@redhat.com> Date: Wed Jul 1 16:43:53 2026 -0400 Address review comments Assisted-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> --------- Assisted-by: Cursor AI Claude Opus 4.6 Co-authored-by: Cursor <cursoragent@cursor.com> Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>]4187b52

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jul 6, 2026

…calls ([vllm-project#839]) ## Summary Tool calling currently doesn't have a dedicated turn to tell the server what the client came up with, and this PR adds that. It also adds a turn type for a server side tool call. ## Details - This design injects an additional generation request to inject the tool call response before the next user response. - The server side tool call feature just ensures that the tool call value is not set to none for that turn. - Includes empty responses from agent in history Here is an example set of turns with the latest code using the following command: ` guidellm run --backend '{"kind": "openai_http", "target": "http://localhost:8000", "request_format": "/v1/chat/completions", "tool_call_missing_behavior": "error_stop", "server_history": false, "extras": {"body": {"chat_template_kwargs": {"enable_thinking": false}}}}' --data '{"kind": "synthetic_text", "prompt_tokens": 20, "output_tokens": 20, "turns": 4, "tool_call_turns": 1}' --constraint '{"kind": "max_requests", "count": 6}' --constraint kind=max_duration,seconds=120 --profile kind=synchronous ` ``` [USER] 1 0 Off to message interview. Yes way plan prepare dinner whom out. General sit hold. [ASSISTANT] arguments: query: 1 0 Off to message interview. Yes way plan prepare dinner whom out. General sit hold. function: get_data id: chatcmpl-tool-9286e5297bcd5feb [TOOL] tool_call_id: chatcmpl-tool-9286e5297bcd5feb {"status": "ok"} [ASSISTANT] It seems like your message is a bit unclear or fragmented. Could you please rephrase or clarify what [USER] 1 1 Above everybody well. Second have writer final agent wonder sell. Interest order control feel write [ASSISTANT] It looks like your message is still fragmented and difficult to interpret. Could you please rephrase or provide [USER] 1 2 Fine movie standard official. World deep less college right much. None bar Mr push. [ASSISTANT] It seems like your message is still unclear and fragmented. Could you please rephrase or clarify what you [USER] 1 3 Sea low especially right throw opportunity while. Beyond issue eat good season recognize. Other difference [RESPONSE] It seems like your message is still unclear and fragmented. Could you please rephrase or clarify what you ``` ## Test Plan - Run normal benchmarks - Run tool call benchmarks. - If time allows, setup a server-side tool call stack and test server side tool calling. ## Related Issues --- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [x] Includes code generated or substantially modified by an AI agent - [x] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Jared O'Connell <joconnel@redhat.com> Date: Mon Jun 22 12:37:05 2026 -0400 Add tool response turn and add server-tool-call turn type Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> commit]12b6bdb[Author: Jared O'Connell <joconnel@redhat.com> Date: Mon Jun 22 17:23:39 2026 -0400 Include empty responses in history Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> commit]59af1f2[Author: Jared O'Connell <joconnel@redhat.com> Date: Mon Jun 22 18:50:28 2026 -0400 Make tool response turns inherit proper metric settings Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> commit]1f5aaaf[Author: Jared O'Connell <joconnel@redhat.com> Date: Mon Jun 22 23:52:22 2026 -0400 Remove outdated comment Signed-off-by: Jared O'Connell <joconnel@redhat.com> commit]0c1e64f[Author: Jared O'Connell <joconnel@redhat.com> Date: Tue Jun 23 00:01:23 2026 -0400 Fix tool calling in preprocessor Signed-off-by: Jared O'Connell <joconnel@redhat.com> commit]7db3769[Author: Jared O'Connell <joconnel@redhat.com> Date: Tue Jun 23 11:39:56 2026 -0400 Add support for other dataset formats for tool calling Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> commit]97906e3[Author: Jared O'Connell <joconnel@redhat.com> Date: Tue Jun 23 13:37:12 2026 -0400 Update documentation for tool calls Added server side tool call examples, but only touched the ones not already updated by the other documentation update PR when possible. Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> commit]85958c8[Author: Jared O'Connell <joconnel@redhat.com> Date: Tue Jun 23 14:49:45 2026 -0400 Reformat test files Signed-off-by: Jared O'Connell <joconnel@redhat.com> commit]cdf917c[Author: Jared O'Connell <joconnel@redhat.com> Date: Tue Jun 30 18:16:22 2026 -0400 Revert mapper changes and related fixes Co-authored-by: Cursor <cursoragent@cursor.com> Signed-off-by: Jared O'Connell <joconnel@redhat.com> commit]ce671ff[Author: Jared O'Connell <joconnel@redhat.com> Date: Tue Jun 30 22:53:51 2026 -0400 Added tool support to mock server and tool call E2E tests Signed-off-by: Jared O'Connell <joconnel@redhat.com> Generated-by: Cursor AI Claude Opus 4.6 commit]7e035b1[Author: Jared O'Connell <joconnel@redhat.com> Date: Wed Jul 1 13:36:11 2026 -0400 Address review comments Assisted-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> commit]39ea8e2[Author: Jared O'Connell <joconnel@redhat.com> Date: Wed Jul 1 16:43:53 2026 -0400 Address review comments Assisted-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> --------- Assisted-by: Cursor AI Claude Opus 4.6 Co-authored-by: Cursor <cursoragent@cursor.com> Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>]4187b52

[mergify](https://github.com/apps/mergify)Bot pushed a commit that referenced this pull request

Sep 9, 2026

## Summary Non-streaming OpenAI requests that required a tool call yielded a successful response before reporting that the model omitted the tool call. This makes `error_stop` consistent with the documented streaming behavior: it now raises before any final response is emitted, while `ignore_stop` still emits the compiled response once and then stops the conversation. ## Details - Validate missing tool calls before the normal non-streaming final yield. - Preserve `ignore_stop` by yielding the compiled response once when the validation raises `CancelledError`, then re-raising it. - Add a regression test for both `error_stop` and `ignore_stop` yield ordering. ## Test Plan - OpenAI HTTP unit file: 47 passed. - Tool-call scheduler integration file: 6 passed; existing multiprocessing `MagicMock` pickling tracebacks were emitted during the run. - Ruff format and lint checks pass. - Mypy on the changed source passes. - `git diff --check` passes. The base regression failed for `error_stop` because one response was yielded before the expected `ValueError`; `ignore_stop` passed its one-yield behavior. Full tox could not finish because the locked development group installs large optional Torch/audio/vision dependencies under shared network contention. The focused checks use the real project code and direct test dependencies without mocking unavailable project internals. No existing issue or competing open/closed PR was found for this ordering defect. Merged PR[#839]defines the missing-tool-call behavior but does not cover the non-streaming yield order. ## Use of AI - [x] Includes code generated or substantially modified by an AI agent - [x] Includes tests generated or substantially modified by an AI agent The code and tests were generated with OpenAI Codex and require human review before submission. The commit includes the required `Generated-by: OpenAI Codex GPT-5` trailer. --- # git log commit[Author: Divyam Talwar <divyamtalwar0@gmail.com> Date: Tue Sep 8 07:03:03 2026 +0530 fix(openai): validate non-streaming tool calls before yield Generated-by: OpenAI Codex GPT-5 Signed-off-by: Divyam Talwar <divyamtalwar0@gmail.com> commit]45255cf[Author: Divyam Talwar <divyamtalwar0@gmail.com> Date: Thu Sep 10 00:56:33 2026 +0530 test(openai): restore tool-call regression to HTTP test suite Move the non-streaming tool-call ordering regression back into TestOpenAIHTTPBackend and reuse its existing request-handler fixture. Remove the standalone test module and its duplicated setup. Preserve both error_stop and ignore_stop cases, all upstream HTTP tests, and the existing runtime fix without behavioral changes. Generated-by: ChatGPT Signed-off-by: Divyam Talwar <divyamtalwar0@gmail.com> --------- Generated-by: ChatGPT Generated-by: OpenAI Codex GPT-5 Signed-off-by: Divyam Talwar <divyamtalwar0@gmail.com>]b6e81fd

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

Tool calling currently doesn't have a dedicated turn to tell the server what the client came up with, and this PR adds that.

It also adds a turn type for a server side tool call.

## Details

Here is an example set of turns with the latest code using the following command:

`guidellm run --backend '{"kind": "openai_http", "target": "http://localhost:8000", "request_format": "/v1/chat/completions", "tool_call_missing_behavior": "error_stop", "server_history": false, "extras": {"body": {"chat_template_kwargs": {"enable_thinking": false}}}}' --data '{"kind": "synthetic_text", "prompt_tokens": 20, "output_tokens": 20, "turns": 4, "tool_call_turns": 1}' --constraint '{"kind": "max_requests", "count": 6}' --constraint kind=max_duration,seconds=120 --profile kind=synchronous`

## Test Plan

## Related Issues

## Use of AI

## git log

commit

12b6bdbAuthor: Jared O'Connell joconnel@redhat.com

Date: Mon Jun 22 12:37:05 2026 -0400

commit

59af1f2Author: Jared O'Connell joconnel@redhat.com

Date: Mon Jun 22 17:23:39 2026 -0400

commit

1f5aaafAuthor: Jared O'Connell joconnel@redhat.com

Date: Mon Jun 22 18:50:28 2026 -0400

commit

0c1e64fAuthor: Jared O'Connell joconnel@redhat.com

Date: Mon Jun 22 23:52:22 2026 -0400

commit

7db3769Author: Jared O'Connell joconnel@redhat.com

Date: Tue Jun 23 00:01:23 2026 -0400

commit

97906e3Author: Jared O'Connell joconnel@redhat.com

Date: Tue Jun 23 11:39:56 2026 -0400

commit

85958c8Author: Jared O'Connell joconnel@redhat.com

Date: Tue Jun 23 13:37:12 2026 -0400

commit

cdf917cAuthor: Jared O'Connell joconnel@redhat.com

Date: Tue Jun 23 14:49:45 2026 -0400

commit

ce671ffAuthor: Jared O'Connell joconnel@redhat.com

Date: Tue Jun 30 18:16:22 2026 -0400

commit

7e035b1Author: Jared O'Connell joconnel@redhat.com

Date: Tue Jun 30 22:53:51 2026 -0400

commit

39ea8e2Author: Jared O'Connell joconnel@redhat.com

Date: Wed Jul 1 13:36:11 2026 -0400

commit

4187b52Author: Jared O'Connell joconnel@redhat.com

Date: Wed Jul 1 16:43:53 2026 -0400

Assisted-by: Cursor AI Claude Opus 4.6

Co-authored-by: Cursor cursoragent@cursor.com

Generated-by: Cursor AI Claude Opus 4.6

Signed-off-by: Jared O'Connell joconnel@redhat.com