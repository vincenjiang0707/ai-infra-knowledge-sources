source: https://github.com/vllm-project/guidellm/pull/760

# Time to first output token and related fixes - #760

[mergify[bot]](https://github.com/mergify[bot])merged 5 commits into

[mergify[bot]](https://github.com/mergify[bot]) merged 5 commits into

[mergify[bot]](https://github.com/mergify[bot])merged 5 commits into

## Conversation


[dbutenhof](https://github.com/dbutenhof)added

[internal](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Ainternal)

[bug](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Abug)

Jun 2, 2026


**requested changes**

[sjmonson](https://github.com/sjmonson)Jun 2, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

Few small nits / clarifications.

[src/guidellm/backends/openai/http.py](https://github.com/vllm-project/guidellm/pull/760/files#diff-6a56e17b4a9b1b702100f54acf336f97d4de6346ea9f696bb23602d12c1f0002)Outdated

[src/guidellm/benchmark/schemas/generative/accumulator.py](https://github.com/vllm-project/guidellm/pull/760/files#diff-238006e045e6328e3f97988050385218fad8b50295530a9afce77f7559bde7f9)

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/760/files#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/760/files#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated

Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Also added tests Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Assisted-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>

[jaredoconnell](https://github.com/jaredoconnell)

[force-pushed](https://github.com/vllm-project/guidellm/compare/bda4e51427b046523bf6b3fe8612f9fc4d87d941..a9bd3443cbd7e4d416171354edb786c1c7a20ba9)the feat/ttfot-and-responses-ttft-parity branch from

[to](https://github.com/vllm-project/guidellm/commit/bda4e51427b046523bf6b3fe8612f9fc4d87d941)

`bda4e51`


`a9bd344`

[Compare](https://github.com/vllm-project/guidellm/compare/bda4e51427b046523bf6b3fe8612f9fc4d87d941..a9bd3443cbd7e4d416171354edb786c1c7a20ba9)

June 2, 2026 19:27


**commented**

[jaredoconnell](https://github.com/jaredoconnell)Jun 2, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

Addressed review feedback.

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/760/files#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated

[src/guidellm/backends/openai/http.py](https://github.com/vllm-project/guidellm/pull/760/files#diff-6a56e17b4a9b1b702100f54acf336f97d4de6346ea9f696bb23602d12c1f0002)Outdated


**previously approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jun 2, 2026

Assisted-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>

[jaredoconnell](https://github.com/jaredoconnell)

[force-pushed](https://github.com/vllm-project/guidellm/compare/a79a7008fb70b30ceba32acc1fccd9aab91b5eb2..dd1918db44645145212fb7f58f16020fa558afd1)the feat/ttfot-and-responses-ttft-parity branch from

[to](https://github.com/vllm-project/guidellm/commit/a79a7008fb70b30ceba32acc1fccd9aab91b5eb2)

`a79a700`


`dd1918d`

[Compare](https://github.com/vllm-project/guidellm/compare/a79a7008fb70b30ceba32acc1fccd9aab91b5eb2..dd1918db44645145212fb7f58f16020fa558afd1)

June 3, 2026 04:46

|
I added a new template system to allow formatting the reasoning section to allow or anything else you could need. |

|
FYI, I pulled this and tried it with a Qwen3-0.6B deployment, and For the heck of it, I combined tool calling with reasoning, and this is chat/completions. (But responses is roughly similar.) ```
uv run guidellm benchmark --target http://<vllm> --profile constant --request-format /v1/chat/completions --max-seconds 30 --rate 2 --data "kind=synthetic_text,prompt_tokens=256,output_tokens=128,turns=5,tool_call_turns=3"
[...]
ℹ Tool Call Metrics Statistics (Completed Requests)
|===========|=======|========|=======|=======|=======|======|======|======|
| Benchmark | Output Tokens |||| Output Count ||||
| Strategy | Per Request || Per Second || Per Request || Per Second ||
| | Mdn | p95 | Mdn | Mean | Mdn | p95 | Mdn | Mean |
|-----------|-------|--------|-------|-------|-------|------|------|------|
| constant | 463.0 | 1214.0 | 328.3 | 623.7 | 1.0 | 1.0 | 1.0 | 1.3 |
|===========|=======|========|=======|=======|=======|======|======|======|
ℹ Request Token Statistics (Completed Requests)
|===========|========|========|=======|========|========|========|=======|========|=========|========|
| Benchmark | Input Tok || Output Tok || Total Tok || Stream Iter || Output Tok ||
| Strategy | Per Req || Per Req || Per Req || Per Req || Per Stream Iter ||
| | Mdn | p95 | Mdn | p95 | Mdn | p95 | Mdn | p95 | Mdn | p95 |
|-----------|--------|--------|-------|--------|--------|--------|-------|--------|---------|--------|
| constant | 1053.0 | 1902.0 | 295.0 | 1164.0 | 1451.0 | 2040.0 | 283.0 | 1152.0 | 1.0 | 1.1 |
|===========|========|========|=======|========|========|========|=======|========|=========|========|
ℹ Request Latency Statistics (Completed Requests)
|===========|=========|========|=======|=======|========|========|=====|=====|=====|=====|
| Benchmark | Request Latency || TTFT || TTFOT || ITL || TPOT ||
| Strategy | Sec || ms || ms || ms || ms ||
| | Mdn | p95 | Mdn | p95 | Mdn | p95 | Mdn | p95 | Mdn | p95 |
|-----------|---------|--------|-------|-------|--------|--------|-----|-----|-----|-----|
| constant | 1.3 | 4.2 | 168.9 | 511.4 | 1085.2 | 3475.7 | 3.4 | 4.5 | 3.8 | 7.0 |
|===========|=========|========|=======|=======|========|========|=====|=====|=====|=====|
``` |

|

Yeah; I didn't feel like messing around to figure out how the container image was built. I have a persistent volume claim I use for HF and model cache, but that wasn't working and I tried |


**approved these changes**

[sjmonson](https://github.com/sjmonson)Jun 3, 2026

|
|

## Merge Queue Status🛑 Queue command has been cancelled |

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jun 8, 2026

## Summary Adds time to first output token (TTFOT), and fixes TTFT when reasoning is included for the responses API. ## Details - Uses TTFOT as that's industry standard. I can see arguments for and against that terminology. - Updates the logic used in the responses API to properly track TTFT for the responses API. - Adds a setting to include the reasoning in the history. I have not verified that its design is perfect for that. I don't expect perfect KVCache hits with that setting because it's returning output that was already processed by a reasoning parser, changing it. This setting is off by default. - Note that if a reasoning parser isn't set in vLLM, it won't send chunks labeled as reasoning, and will instead just send raw thinking tokens, which will be processed as normal content. ## Test Plan - Run a model with reasoning only - Run a model with a zero token reasoning limit, as well as a non-zero reasoning limit. Observe how the TTFOT compares to the TTFT. - Test reasoning on both chat completions and responses API. ## Related Issues Related to[vllm-project#742]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [x] Includes code generated or substantially modified by an AI agent - [x] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. --- # git log commit[Author: Jared O'Connell <joconnel@redhat.com> Date: Fri May 29 18:47:58 2026 -0400 Add TTFOT and store reasoning tokens. Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> commit]14a0cbf[Author: Jared O'Connell <joconnel@redhat.com> Date: Fri May 29 19:27:04 2026 -0400 Fixed output behavior for reasoning tokens Also added tests Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> commit]54719fe[Author: Jared O'Connell <joconnel@redhat.com> Date: Tue Jun 2 15:26:11 2026 -0400 Address review comments Assisted-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> commit]a9bd344[Author: Jared O'Connell <joconnel@redhat.com> Date: Wed Jun 3 00:31:02 2026 -0400 Switch to template system to allow wrapping reasoning tokens Assisted-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> --------- Assisted-by: Cursor AI Claude Opus 4.6 Generated-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>]dd1918d

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

Adds time to first output token (TTFOT), and fixes TTFT when reasoning is included for the responses API.

## Details

## Test Plan

## Related Issues

Related to #742

## Use of AI

## git log

commit

14a0cbfAuthor: Jared O'Connell joconnel@redhat.com

Date: Fri May 29 18:47:58 2026 -0400

commit

54719feAuthor: Jared O'Connell joconnel@redhat.com

Date: Fri May 29 19:27:04 2026 -0400

commit

a9bd344Author: Jared O'Connell joconnel@redhat.com

Date: Tue Jun 2 15:26:11 2026 -0400

commit

dd1918dAuthor: Jared O'Connell joconnel@redhat.com

Date: Wed Jun 3 00:31:02 2026 -0400

Assisted-by: Cursor AI Claude Opus 4.6

Generated-by: Cursor AI Claude Opus 4.6

Signed-off-by: Jared O'Connell joconnel@redhat.com