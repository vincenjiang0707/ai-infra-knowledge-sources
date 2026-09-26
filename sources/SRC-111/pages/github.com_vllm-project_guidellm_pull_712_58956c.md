source: https://github.com/vllm-project/guidellm/pull/712

# Multi-turn tool call chat completions conversations - #712

[jaredoconnell](https://github.com/jaredoconnell)merged 17 commits into

## Conversation


**requested changes**

[sjmonson](https://github.com/sjmonson)May 1, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

Not finished reviewing; will add more comments in a bit. Github is acting up and not letting me add to this review for some reason.

[src/guidellm/backends/openai/http.py](https://github.com/vllm-project/guidellm/pull/712/files#diff-6a56e17b4a9b1b702100f54acf336f97d4de6346ea9f696bb23602d12c1f0002)Outdated

[src/guidellm/benchmark/outputs/html.py](https://github.com/vllm-project/guidellm/pull/712/files#diff-991b1a5be8adb6d8a8d3d1bc54c2491cccd775c4ce758c43421332e9551559ec)Outdated

[src/guidellm/data/preprocessors/mappers.py](https://github.com/vllm-project/guidellm/pull/712/files#diff-2099c62bd0e1315d94f5ca565b50198a0507b9f2818feba33fd14d29641e6deb)Outdated

[src/guidellm/schemas/info.py](https://github.com/vllm-project/guidellm/pull/712/files#diff-179053f40e2947d9c41d6c3d78a225bdb58b06d99bc62c0a3bcad6e15c19adda)Outdated

[src/guidellm/scheduler/worker.py](https://github.com/vllm-project/guidellm/pull/712/files#diff-a2646f8d413b5691fb552d608e2f652695326bc23ea881bc9ab2f3ce666dc857)

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/712/files#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated

[src/guidellm/backends/openai/http.py](https://github.com/vllm-project/guidellm/pull/712/files#diff-6a56e17b4a9b1b702100f54acf336f97d4de6346ea9f696bb23602d12c1f0002)Outdated

[src/guidellm/backends/openai/http.py](https://github.com/vllm-project/guidellm/pull/712/files#diff-6a56e17b4a9b1b702100f54acf336f97d4de6346ea9f696bb23602d12c1f0002)Outdated


**requested changes**

[sjmonson](https://github.com/sjmonson)May 1, 2026

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/712/files#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/712/files#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/712/files#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/712/files#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/712/files#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated

[src/guidellm/schemas/response.py](https://github.com/vllm-project/guidellm/pull/712/files#diff-bf8affbc3c40bc61ec258c3fcb7e66cad731d220378bc86d7a364c3b7258fe42)Outdated

[src/guidellm/schemas/response.py](https://github.com/vllm-project/guidellm/pull/712/files#diff-bf8affbc3c40bc61ec258c3fcb7e66cad731d220378bc86d7a364c3b7258fe42)Outdated

[src/guidellm/__main__.py](https://github.com/vllm-project/guidellm/pull/712/files#diff-62e0a62289c938a74b026dbce7a0f95f26893e0aa9feedb81349e658db8af7bf)Outdated

[src/guidellm/__main__.py](https://github.com/vllm-project/guidellm/pull/712/files#diff-62e0a62289c938a74b026dbce7a0f95f26893e0aa9feedb81349e658db8af7bf)Outdated

[docs/guides/multiturn.md](https://github.com/vllm-project/guidellm/pull/712/files#diff-b8c613ed380ab7cd9bd8b09b3ba7f883c2f7233af1f1a5b79bcef3c14c2ef903)

|
This pull request has merge conflicts that must be resolved before it can be |


**commented**

[jaredoconnell](https://github.com/jaredoconnell)May 5, 2026

[docs/guides/multiturn.md](https://github.com/vllm-project/guidellm/pull/712/files#diff-b8c613ed380ab7cd9bd8b09b3ba7f883c2f7233af1f1a5b79bcef3c14c2ef903)

[src/guidellm/data/deserializers/synthetic.py](https://github.com/vllm-project/guidellm/pull/712/files#diff-4b48dc7631c1a28d1f1b7ca179feb42d01378082bc7c9b97bf3cd4bcc2c58a94)Outdated

[src/guidellm/scheduler/worker.py](https://github.com/vllm-project/guidellm/pull/712/files#diff-a2646f8d413b5691fb552d608e2f652695326bc23ea881bc9ab2f3ce666dc857)


**reviewed**

[dbutenhof](https://github.com/dbutenhof)May 6, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

Finally got through this. Looks good. Needs a rebase.

|
You can do this by running: |

|
augment review |

|


**reviewed**

[augmentcode](https://github.com/apps/augmentcode)BotMay 7, 2026

[src/guidellm/backends/openai/http.py](https://github.com/vllm-project/guidellm/pull/712/files#diff-6a56e17b4a9b1b702100f54acf336f97d4de6346ea9f696bb23602d12c1f0002)

[docs/guides/tool_calling.md](https://github.com/vllm-project/guidellm/pull/712/files#diff-61af4f8d78e766b599dc58cd80c99c7b4be40899e4726feaf6deb3819f4a658b)Outdated


**requested changes**

[sjmonson](https://github.com/sjmonson)May 8, 2026

[src/guidellm/scheduler/worker.py](https://github.com/vllm-project/guidellm/pull/712/files#diff-a2646f8d413b5691fb552d608e2f652695326bc23ea881bc9ab2f3ce666dc857)

[src/guidellm/scheduler/worker.py](https://github.com/vllm-project/guidellm/pull/712/files#diff-a2646f8d413b5691fb552d608e2f652695326bc23ea881bc9ab2f3ce666dc857)

[src/guidellm/data/preprocessors/mappers.py](https://github.com/vllm-project/guidellm/pull/712/files#diff-2099c62bd0e1315d94f5ca565b50198a0507b9f2818feba33fd14d29641e6deb)Outdated

[src/guidellm/backends/openai/http.py](https://github.com/vllm-project/guidellm/pull/712/files#diff-6a56e17b4a9b1b702100f54acf336f97d4de6346ea9f696bb23602d12c1f0002)

|
This pull request has merge conflicts that must be resolved before it can be |


**commented**

[jaredoconnell](https://github.com/jaredoconnell)May 12, 2026

[src/guidellm/backends/openai/http.py](https://github.com/vllm-project/guidellm/pull/712/files#diff-6a56e17b4a9b1b702100f54acf336f97d4de6346ea9f696bb23602d12c1f0002)

[docs/guides/tool_calling.md](https://github.com/vllm-project/guidellm/pull/712/files#diff-61af4f8d78e766b599dc58cd80c99c7b4be40899e4726feaf6deb3819f4a658b)Outdated

[src/guidellm/scheduler/worker.py](https://github.com/vllm-project/guidellm/pull/712/files#diff-a2646f8d413b5691fb552d608e2f652695326bc23ea881bc9ab2f3ce666dc857)

|
|

## ❌ Base branch update has failed## DetailsGit reported the following error:
|

|
I will rebase locally. I enabled |


**previously approved these changes**

[dbutenhof](https://github.com/dbutenhof)May 14, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

The code looks good; I ran it against my server with Qwen/Qwen3-0.6B and the GuideLLM sample command from `tool_calling.md`

, and it seems to run OK:

```
ℹ Tool Call Metrics Statistics (Completed Requests)
|===========|======|=======|=======|=======|======|=======|======|======|
| Benchmark | Output Tokens |||| Output Count ||||
| Strategy | Per Request || Per Second || Per Request || Per Second ||
| | Mdn | p95 | Mdn | Mean | Mdn | p95 | Mdn | Mean |
|-----------|------|-------|-------|-------|------|-------|------|------|
| constant | 77.0 | 692.0 | 152.7 | 309.4 | 1.0 | 19.0 | 1.5 | 4.8 |
|===========|======|=======|=======|=======|======|=======|======|======|
```

[jaredoconnell](https://github.com/jaredoconnell)

[force-pushed](https://github.com/vllm-project/guidellm/compare/5fb71c1c083323a54fdb1aabd72420bdacc6f623..fbc667c7990fd5e5d0a1731c66e1b47a2fbcf61a)the feat/multi-turn-tools-chat branch from

[to](https://github.com/vllm-project/guidellm/commit/5fb71c1c083323a54fdb1aabd72420bdacc6f623)

`5fb71c1`


`fbc667c`

[Compare](https://github.com/vllm-project/guidellm/compare/5fb71c1c083323a54fdb1aabd72420bdacc6f623..fbc667c7990fd5e5d0a1731c66e1b47a2fbcf61a)

May 14, 2026 22:04


**previously approved these changes**

[dbutenhof](https://github.com/dbutenhof)May 15, 2026


**previously approved these changes**

[sjmonson](https://github.com/sjmonson)May 18, 2026


**previously approved these changes**

[dbutenhof](https://github.com/dbutenhof)May 18, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

This should be safe given that `stream`

is a `Request`

object from the original connection that should only change if another call is made.

Assisted-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Assisted-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Adds variable size responses for synthetic data, and better handles edge cases for external datasets. Also improves documentation. Assisted-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Assisted-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Assisted-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Extracts functionality to new static methods. Assisted-by: Claude Code Sonnet 4.5 Signed-off-by: Jared O'Connell <joconnel@redhat.com>

These are the diffs recommended in the comments. They are untested, and require some follow-up changes. Co-authored-by: Samuel Monson <smonson@irbash.net> Signed-off-by: Jared O'Connell <46976761+jaredoconnell@users.noreply.github.com>

Moves documentation. Switches fully to exceptions to stop conversations early. Also includes info gained from vLLM contributor. Assisted-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Assisted-by: Cursor AI Claude 4.6 Opus High Thinking Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Assisted-by: Cursor AI Claude 4.6 Opus High Thinking Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Assisted-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Removed all worker logic except changed conversations to end if any exception occurs. Assisted-by: Cursor AI Claude 4.6 Opus High Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Assisted-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>

This was necessary due to the function exceeding the project's litner's limit on number of statements. Assisted-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>

[jaredoconnell](https://github.com/jaredoconnell)

[force-pushed](https://github.com/vllm-project/guidellm/compare/b5e19286d3aa6b4b0dc40c42cc45de747f7dcad2..27d1e7527a6c39115d46b4c48d6504b2a05cfef5)the feat/multi-turn-tools-chat branch from

[to](https://github.com/vllm-project/guidellm/commit/b5e19286d3aa6b4b0dc40c42cc45de747f7dcad2)

`b5e1928`


`27d1e75`

[Compare](https://github.com/vllm-project/guidellm/compare/b5e19286d3aa6b4b0dc40c42cc45de747f7dcad2..27d1e7527a6c39115d46b4c48d6504b2a05cfef5)

May 18, 2026 21:50

|
🥳 🎆 🧰 |

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

This PR adds client-side chat completions conversations to the http backend.

## Details

`auto`

or`required`

to the model. Good for testing various scenarios. Models behave differently depending on the value set.`required`

is best for predictability.## Test Plan

## Related Issues

## Use of AI

`## WRITTEN BY AI ##`

)