source: https://github.com/vllm-project/guidellm/pull/742

# Fix TTFT measurement for reasoning-capable models - #742

[jaredoconnell](https://github.com/jaredoconnell)merged 2 commits into

[jaredoconnell](https://github.com/jaredoconnell) merged 2 commits into

[jaredoconnell](https://github.com/jaredoconnell)merged 2 commits into

## Conversation

[soyr-redhat](https://github.com/soyr-redhat)

[force-pushed](https://github.com/vllm-project/guidellm/compare/0cace27c331f69d6f05bd90814323201cf25036f..742291a2d8ff25e05a41584f0d349cc85b38d93a)the fix/issue-737-reasoning-tokens-ttft branch from

[to](https://github.com/vllm-project/guidellm/commit/0cace27c331f69d6f05bd90814323201cf25036f)

`0cace27`


`742291a`

[Compare](https://github.com/vllm-project/guidellm/compare/0cace27c331f69d6f05bd90814323201cf25036f..742291a2d8ff25e05a41584f0d349cc85b38d93a)

May 22, 2026 20:15

[jaredoconnell](https://github.com/jaredoconnell)

[force-pushed](https://github.com/vllm-project/guidellm/compare/742291a2d8ff25e05a41584f0d349cc85b38d93a..dedb068260ccb2ef32ba00fc01a7aa7817514eb7)the fix/issue-737-reasoning-tokens-ttft branch from

[to](https://github.com/vllm-project/guidellm/commit/742291a2d8ff25e05a41584f0d349cc85b38d93a)

`742291a`


`dedb068`

[Compare](https://github.com/vllm-project/guidellm/compare/742291a2d8ff25e05a41584f0d349cc85b38d93a..dedb068260ccb2ef32ba00fc01a7aa7817514eb7)

May 26, 2026 15:11


**requested changes**

[jaredoconnell](https://github.com/jaredoconnell)May 26, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

After talking with the team, we've determined that reasoning tokens should not be mixed with the content tokens. There are two reason for this. One, reasoning should be differentiated from content. And two, reasoning tokens should not be included in multi-turn conversations. This creates an unrealistic scenario.

For this PR the simplest option is to keep `updated = True`

, but remove the appending of reasoning tokens. Another option that's more more involved is to add a variable separate from `streaming_texts`

to track reasoning texts in the output, but not include them in the output.

|
This pull request has merge conflicts that must be resolved before it can be |

[jaredoconnell](https://github.com/jaredoconnell)

[force-pushed](https://github.com/vllm-project/guidellm/compare/dedb068260ccb2ef32ba00fc01a7aa7817514eb7..e16814ad58e9691856f9b7161d4cc2ed0e2c7c90)the fix/issue-737-reasoning-tokens-ttft branch from

[to](https://github.com/vllm-project/guidellm/commit/dedb068260ccb2ef32ba00fc01a7aa7817514eb7)

`dedb068`


`e16814a`

[Compare](https://github.com/vllm-project/guidellm/compare/dedb068260ccb2ef32ba00fc01a7aa7817514eb7..e16814ad58e9691856f9b7161d4cc2ed0e2c7c90)

May 28, 2026 22:04

Add delta.reasoning detection to ChatCompletionsRequestHandler to properly measure TTFT when reasoning tokens arrive before content tokens. Resolves[vllm-project#737]Tests assisted by: AI Signed-off-by: Sawyer Bowerman <sbowerma@redhat.com> Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Assisted-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>

[jaredoconnell](https://github.com/jaredoconnell)

[force-pushed](https://github.com/vllm-project/guidellm/compare/e16814ad58e9691856f9b7161d4cc2ed0e2c7c90..df5c8bc084318783c328dbd662fc91c3b8680efb)the fix/issue-737-reasoning-tokens-ttft branch from

[to](https://github.com/vllm-project/guidellm/commit/e16814ad58e9691856f9b7161d4cc2ed0e2c7c90)

`e16814a`


`df5c8bc`

[Compare](https://github.com/vllm-project/guidellm/compare/e16814ad58e9691856f9b7161d4cc2ed0e2c7c90..df5c8bc084318783c328dbd662fc91c3b8680efb)

May 29, 2026 16:56


**approved these changes**

[sjmonson](https://github.com/sjmonson)May 29, 2026


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)May 29, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

The primary concern is now fixed. Since I made some changes it's okay since another maintainer also merged.


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)May 29, 2026


[dbutenhof](https://github.com/dbutenhof)added

[community contribution](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3A%22community%20contribution%22)

[bug](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Abug)

[escape](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Aescape)

May 29, 2026

|
Understood. Thank you all for the help! And my apologies |

[mergify](https://github.com/apps/mergify)Bot pushed a commit that referenced this pull request

Jun 3, 2026

## Summary Adds time to first output token (TTFOT), and fixes TTFT when reasoning is included for the responses API. ## Details - Uses TTFOT as that's industry standard. I can see arguments for and against that terminology. - Updates the logic used in the responses API to properly track TTFT for the responses API. - Adds a setting to include the reasoning in the history. I have not verified that its design is perfect for that. I don't expect perfect KVCache hits with that setting because it's returning output that was already processed by a reasoning parser, changing it. This setting is off by default. - Note that if a reasoning parser isn't set in vLLM, it won't send chunks labeled as reasoning, and will instead just send raw thinking tokens, which will be processed as normal content. ## Test Plan - Run a model with reasoning only - Run a model with a zero token reasoning limit, as well as a non-zero reasoning limit. Observe how the TTFOT compares to the TTFT. - Test reasoning on both chat completions and responses API. ## Related Issues Related to[#742]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [x] Includes code generated or substantially modified by an AI agent - [x] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Jared O'Connell <joconnel@redhat.com> Date: Fri May 29 18:47:58 2026 -0400 Add TTFOT and store reasoning tokens. Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> commit]14a0cbf[Author: Jared O'Connell <joconnel@redhat.com> Date: Fri May 29 19:27:04 2026 -0400 Fixed output behavior for reasoning tokens Also added tests Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> commit]54719fe[Author: Jared O'Connell <joconnel@redhat.com> Date: Tue Jun 2 15:26:11 2026 -0400 Address review comments Assisted-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> commit]a9bd344[Author: Jared O'Connell <joconnel@redhat.com> Date: Wed Jun 3 00:31:02 2026 -0400 Switch to template system to allow wrapping reasoning tokens Assisted-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> --------- Assisted-by: Cursor AI Claude Opus 4.6 Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>]dd1918d

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jun 8, 2026

## Summary Adds time to first output token (TTFOT), and fixes TTFT when reasoning is included for the responses API. ## Details - Uses TTFOT as that's industry standard. I can see arguments for and against that terminology. - Updates the logic used in the responses API to properly track TTFT for the responses API. - Adds a setting to include the reasoning in the history. I have not verified that its design is perfect for that. I don't expect perfect KVCache hits with that setting because it's returning output that was already processed by a reasoning parser, changing it. This setting is off by default. - Note that if a reasoning parser isn't set in vLLM, it won't send chunks labeled as reasoning, and will instead just send raw thinking tokens, which will be processed as normal content. ## Test Plan - Run a model with reasoning only - Run a model with a zero token reasoning limit, as well as a non-zero reasoning limit. Observe how the TTFOT compares to the TTFT. - Test reasoning on both chat completions and responses API. ## Related Issues Related to[vllm-project#742]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [x] Includes code generated or substantially modified by an AI agent - [x] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Jared O'Connell <joconnel@redhat.com> Date: Fri May 29 18:47:58 2026 -0400 Add TTFOT and store reasoning tokens. Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> commit]14a0cbf[Author: Jared O'Connell <joconnel@redhat.com> Date: Fri May 29 19:27:04 2026 -0400 Fixed output behavior for reasoning tokens Also added tests Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> commit]54719fe[Author: Jared O'Connell <joconnel@redhat.com> Date: Tue Jun 2 15:26:11 2026 -0400 Address review comments Assisted-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> commit]a9bd344[Author: Jared O'Connell <joconnel@redhat.com> Date: Wed Jun 3 00:31:02 2026 -0400 Switch to template system to allow wrapping reasoning tokens Assisted-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> --------- Assisted-by: Cursor AI Claude Opus 4.6 Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>]dd1918d

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

Fixes TTFT (Time to First Token) measurement for reasoning-capable models that emit

`delta.reasoning`

tokens before`delta.content`

tokens.When benchmarking models through the OpenAI-compatible backend, the TTFT was incorrectly measured if the model first streams reasoning tokens before content tokens. The implementation only considered

`delta.content`

as the "first token" and ignored`delta.reasoning`

, causing TTFT to appear larger than it really is.This extends

`ChatCompletionsRequestHandler.add_streaming_line`

to detect both`delta.reasoning`

and`delta.content`

tokens, ensuring accurate TTFT measurement regardless of which token type arrives first.## Details

`delta.reasoning`

detection in`ChatCompletionsRequestHandler.add_streaming_line`

## Test Plan

`uv run pytest tests/unit/backends/openai/test_request_handlers.py::TestChatCompletionsRequestHandler`

`uv run pytest tests/unit/backends/openai/test_http.py::TestOpenAIHTTPBackend::test_resolve_stream_reasoning_tokens_ttft`

`uv run ruff check`

and`uv run ruff format --check`

)## Related Issues

`delta.reasoning`

before`delta.content`

#737## Use of AI