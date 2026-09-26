source: https://github.com/vllm-project/guidellm/pull/800

# feat: add LiteLLM backend for multi-provider benchmarking - #800

[RheagalFire](https://github.com/RheagalFire)wants to merge 3 commits into

[RheagalFire](https://github.com/RheagalFire) wants to merge 3 commits into

[RheagalFire](https://github.com/RheagalFire)wants to merge 3 commits into

## Conversation

|
Hi |

[RheagalFire](https://github.com/RheagalFire)

[force-pushed](https://github.com/vllm-project/guidellm/compare/1b1135f0440c4193cec2b8f06def220fdd7e8fd5..8e17f9b5e1618ac26aa06167f0c8d767e81f27ec)the feat/add-litellm-provider branch 3 times, most recently from

[to](https://github.com/vllm-project/guidellm/commit/1b1135f0440c4193cec2b8f06def220fdd7e8fd5)

`1b1135f`


`8e17f9b`

[Compare](https://github.com/vllm-project/guidellm/compare/1b1135f0440c4193cec2b8f06def220fdd7e8fd5..8e17f9b5e1618ac26aa06167f0c8d767e81f27ec)

June 16, 2026 18:22

|
cc |


**requested changes**

[sjmonson](https://github.com/sjmonson)Jun 16, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

Just a quick issue I noticed. Also I am guessing you didn't run with pre-check locally since at minimum you will need to regen the lock file after changing dependencies. You can do that with `tox run -e lock`

and plain `tox run`

will run all the other CI tasks if you want to have a faster feedback loop.

[pyproject.toml](https://github.com/vllm-project/guidellm/pull/800/files#diff-50c86b7ed8ac2cf95bd48334961bf0530cdc77b5a56f852c5c61b89d735fd711)Outdated

|
|


**previously approved these changes**

[sjmonson](https://github.com/sjmonson)Jul 7, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

A few minor nits but otherwise LGTM. Needs a rebase due to lockfile changes. The easiest way I have found to do this is to run rebase and when you get to the lockfile conflict:

```
git restore --staged --worktree uv.lock
uv lock # or `tox -e lock`
git add uv.lock
git rebase --continue
```

[src/guidellm/backends/litellm/litellm.py](https://github.com/vllm-project/guidellm/pull/800/files#diff-fa3e7c0d5319a6f17da643f0c7645951e164b9cc865a39bf62aaccfde0f25b7c)Outdated

[src/guidellm/extras/litellm.pyi](https://github.com/vllm-project/guidellm/pull/800/files#diff-ea8d716d8137bd692d80946927c2f55cb967b610f00ab58c52eb3a6dfee9641d)Outdated


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Jul 7, 2026

[src/guidellm/backends/litellm/litellm.py](https://github.com/vllm-project/guidellm/pull/800/files#diff-fa3e7c0d5319a6f17da643f0c7645951e164b9cc865a39bf62aaccfde0f25b7c)

[src/guidellm/backends/litellm/litellm.py](https://github.com/vllm-project/guidellm/pull/800/files#diff-fa3e7c0d5319a6f17da643f0c7645951e164b9cc865a39bf62aaccfde0f25b7c)Outdated


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jul 8, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

I worried a moment about including the `litellm`

layer in `all`

since we build our container image that way -- however `litellm`

1.83 is already available in the AIPCC internal index and it's not enormous, so that shouldn't be an issue.


**previously requested changes**

[dbutenhof](https://github.com/dbutenhof)Jul 9, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

You need to resolve the `uv.lock`

conflict and adapt to a new backend init convention that fixes CSV benchmark reports.

[src/guidellm/backends/litellm/litellm.py](https://github.com/vllm-project/guidellm/pull/800/files#diff-fa3e7c0d5319a6f17da643f0c7645951e164b9cc865a39bf62aaccfde0f25b7c)

Generated-by: Claude claude-opus-4-6 Signed-off-by: RheagalFire <arishalam121@gmail.com>

- Bump minimum litellm version to >=1.83.0 (post supply-chain fix) - Remove <1.87.0 upper bound to allow latest releases - Regenerate uv.lock via tox run -e lock - Fix ruff formatting issues Signed-off-by: Aarish Alam <arishalam121@gmail.com>

[RheagalFire](https://github.com/RheagalFire)

[force-pushed](https://github.com/vllm-project/guidellm/compare/93c94ca22e11eaa3b5240a599c1b9e2ca568a645..a032228e1f270a776840bdd256800779f8293458)the feat/add-litellm-provider branch from

[to](https://github.com/vllm-project/guidellm/commit/93c94ca22e11eaa3b5240a599c1b9e2ca568a645)

`93c94ca`


`a032228`

[Compare](https://github.com/vllm-project/guidellm/compare/93c94ca22e11eaa3b5240a599c1b9e2ca568a645..a032228e1f270a776840bdd256800779f8293458)

August 5, 2026 18:58

|
Hi |

…, __all__ in stub Signed-off-by: Aarish Alam <arishalam121@gmail.com>

[RheagalFire](https://github.com/RheagalFire)

[force-pushed](https://github.com/vllm-project/guidellm/compare/a032228e1f270a776840bdd256800779f8293458..f848ceb2a4abb68c61e1a5a36921514f4acf80eb)the feat/add-litellm-provider branch from

[to](https://github.com/vllm-project/guidellm/commit/a032228e1f270a776840bdd256800779f8293458)

`a032228`


`f848ceb`

[Compare](https://github.com/vllm-project/guidellm/compare/a032228e1f270a776840bdd256800779f8293458..f848ceb2a4abb68c61e1a5a36921514f4acf80eb)

August 5, 2026 19:01


**approved these changes**

[sjmonson](https://github.com/sjmonson)Aug 6, 2026

|
|

## Merge Queue Status
This pull request spent
|

[src/guidellm/backends/litellm/litellm.py](https://github.com/vllm-project/guidellm/pull/800/files/f848ceb2a4abb68c61e1a5a36921514f4acf80eb#diff-fa3e7c0d5319a6f17da643f0c7645951e164b9cc865a39bf62aaccfde0f25b7c)

| messages: list[dict[str, Any]] = ( | ||
| arguments.body.get("messages", []) if arguments.body else [] | ||
| ) | ||
| return messages, arguments.model_dump_json() |

There was a problem hiding this comment.

Have you verified that we only need the messages from the format output? Looking it looks like ChatCompletionsRequestHandler.format() builds a full body (e.g. max_completion_tokens / ignore_eos from request.output_metrics.text_tokens, tools, etc.), but only messages are passed into litellm.acompletion(). The rest appears to end up in arguments.model_dump_json() for GenerationResponse.request_args. Can you confirm whether those body fields are intentionally not forwarded, or if request-level output token limits should also be sent to LiteLLM?

[src/guidellm/backends/litellm/litellm.py](https://github.com/vllm-project/guidellm/pull/800/files/f848ceb2a4abb68c61e1a5a36921514f4acf80eb#diff-fa3e7c0d5319a6f17da643f0c7645951e164b9cc865a39bf62aaccfde0f25b7c)

| usage = getattr(chunk, "usage", None) | ||
| input_tokens = getattr(usage, "prompt_tokens", None) if usage else None | ||
| output_tokens = getattr(usage, "completion_tokens", None) if usage else None | ||
|
|

There was a problem hiding this comment.

We discourage the use of `getattr`

. Have you looked into statically typing `chunk`

so that you can avoid `getattr`

? The type appears to be `ModelResponseStream`

.

|
|


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Aug 21, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

Minimal documentation on the litellm backend should be added to `docs/guides/backends.md`

(a new section under Supported Backends), describing the usage and use cases. If the documentation is extensive, spin off details into a new `.md`

file, with a link from "Supported Backends" as there is for the "vLLM Python Backend".

|
|

### This branch has not been deployed

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

Adds a new

`litellm`

backend that routes generation requests through the LiteLLM SDK, enabling benchmarking across 100+ providers (Anthropic, Gemini, Bedrock, Groq, Cohere, Mistral, etc.) via a unified interface. Timing instrumentation matches the existing OpenAI HTTP backend so benchmark results are directly comparable.## Details

`LiteLLMBackend`

and`LiteLLMBackendArgs`

following the existing`Backend`

/`BackendArgs`

registration pattern`litellm.acompletion(stream=True)`

with`drop_params=True`

for cross-provider compatibility`ChatCompletionsRequestHandler.format()`

to build messages from`GenerationRequest.columns`

`guidellm.extras.litellm`

so the optional dep doesn't break imports when not installed`litellm>=1.80.0,<1.87.0`

added as optional dependency under`[project.optional-dependencies].litellm`

## Test Plan

`pytest tests/unit/backends/litellm/ -v`

to verify unit tests`pytest tests/unit/backends/ -v`

to verify no regressions in existing backends`anthropic/claude-sonnet-4-6`

via Azure Foundry:## Related Issues

## Use of AI

## git log

commit

0dba09bAuthor: RheagalFire arishalam121@gmail.com

Date: Tue Jun 16 23:51:47 2026 +0530

commit

1bad39cAuthor: Aarish Alam arishalam121@gmail.com

Date: Wed Jul 1 20:00:26 2026 +0530

commit

f848cebAuthor: Aarish Alam arishalam121@gmail.com

Date: Thu Aug 6 00:28:49 2026 +0530

Generated-by: Claude claude-opus-4-6

Signed-off-by: RheagalFire arishalam121@gmail.com

Signed-off-by: Aarish Alam arishalam121@gmail.com