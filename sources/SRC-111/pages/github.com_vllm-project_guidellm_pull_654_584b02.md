source: https://github.com/vllm-project/guidellm/pull/654

# Improve environment variables warning and validation cleanup - #654

## Conversation

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>


**commented**

[sjmonson](https://github.com/sjmonson)Mar 24, 2026

[src/guidellm/utils/env_validator.py](https://github.com/vllm-project/guidellm/pull/654/files/db85246eb76baf807233fd93b0d86fef11cc768b#diff-f8fee32b40b7c2bd386331f7100a86fd5d429cd3b47000d6f2c969d949bf313b)

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>


**requested changes**

[dbutenhof](https://github.com/dbutenhof)Mar 24, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

OK, a bunch of simplification I like. The Click CTX search is kinda wild, but I do like picking out the actual list rather than duplicating code or guessing. One comment on wording, because ALL CAPS is often taken as rude shouting and I don't think adds anything here...

[src/guidellm/__main__.py](https://github.com/vllm-project/guidellm/pull/654/files/980b354f1f23c37518cd1e9851340886cc29cfe3#diff-62e0a62289c938a74b026dbce7a0f95f26893e0aa9feedb81349e658db8af7bf)Outdated


**requested changes**

[jaredoconnell](https://github.com/jaredoconnell)Mar 25, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

It's looking good overall.

I did, however, notice that if I specify "responses" to the HTTP backend, which does not support the responses api in this branch, it just uses the endpoint `/v1/chat/completions`

. I then tested with `/v1/completions`

, and it was respected on main, and it was not respected on this branch.

So this appears to be a bug.

Signed-off-by: Samuel Monson <smonson@redhat.com>


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Mar 25, 2026

Fixed, apparently |


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Mar 25, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

Looks good. I can confirm that the latest change fixed the problem.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

`BackendArgs`

.## Details

Adds a new module to utilities for detecting environment variables supported by click and global settings. Then uses this data to split the environment into variables recognized as valid options and those that are not. This should make it easier for users to determine what environment settings are actually having an affect on GuideLLM and if any current workflows are outdated.

Also reworks some of the new

`BackendArgs`

validation. Instead of storing backend arguments directly in`BenchmarkGenerativeTextArgs`

instead have`BenchmarkGenerativeTextArgs`

construct a`BackendArgs`

for the given backend type and store that. This deduplicates some validation logic removes the need for the custom`format_backend_args_error`

helper.## Test Plan

## 1. Env Helper

Run

`GUIDELLM__LOGGING__DISABLED=true GUIDELLM__REQUEST_TIMEOUT=test GUIDELLM_RATE_TYPE=sweep GUIDELLM_TARGET=http://localhost:9 uv run guidellm benchmark run`

.Backend will fail with

`RuntimeError: Backend validation request failed...`

but will print env detection:## 2.

`BackendArgs`

ValidationWill vLLM run:

`uv run --with vllm guidellm benchmark run --backend vllm_python --model test --target http://localhost:9`

.GuideLLM should reject it will a message about target:

## Use of AI

`## WRITTEN BY AI ##`

)