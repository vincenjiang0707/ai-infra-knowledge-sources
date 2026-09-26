source: https://github.com/vllm-project/guidellm/pull/651

# Pass mp context to strategy - #651

## Conversation

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/f532cd940c46572143068d838231abdda3722b40..d04b8f186b2ce7c79931b502b6ef7b93d8b4b3fe)the fix/mp_context branch from

[to](https://github.com/vllm-project/guidellm/commit/f532cd940c46572143068d838231abdda3722b40)

`f532cd9`


`d04b8f1`

[Compare](https://github.com/vllm-project/guidellm/compare/f532cd940c46572143068d838231abdda3722b40..d04b8f186b2ce7c79931b502b6ef7b93d8b4b3fe)

March 20, 2026 19:15

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/d04b8f186b2ce7c79931b502b6ef7b93d8b4b3fe..b31773fb256aac5db79c30fe684a4a61449d8631)the fix/mp_context branch from

[to](https://github.com/vllm-project/guidellm/commit/d04b8f186b2ce7c79931b502b6ef7b93d8b4b3fe)

`d04b8f1`


`b31773f`

[Compare](https://github.com/vllm-project/guidellm/compare/d04b8f186b2ce7c79931b502b6ef7b93d8b4b3fe..b31773fb256aac5db79c30fe684a4a61449d8631)

March 20, 2026 19:38


**previously approved these changes**

[dbutenhof](https://github.com/dbutenhof)Mar 20, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

OK, so this just does all of the multiprocessing operations through the `get_context()`

object rather than using the globals, and shouldn't actually change things.

Does anyone *call* the GuideLLM entrypoints from a Python module? Because that expands the whole issue of `__main__`

restrictions to the caller... while for our CLI we only worry about our own. (One possibility I suppose would be for our ABI entrypoints to check whether the `get_start_method()`

aligns with our expectations...)

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/b31773fb256aac5db79c30fe684a4a61449d8631..88eb29c0fb78022bc16748216bde9b7db5fc739a)the fix/mp_context branch from

[to](https://github.com/vllm-project/guidellm/commit/b31773fb256aac5db79c30fe684a4a61449d8631)

`b31773f`


`88eb29c`

[Compare](https://github.com/vllm-project/guidellm/compare/b31773fb256aac5db79c30fe684a4a61449d8631..88eb29c0fb78022bc16748216bde9b7db5fc739a)

March 20, 2026 20:25


**previously approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Mar 20, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

It appears to work fine. I have one comment.

For extra context, here is how long the command takes on my mac:

fork: 40.30 real 8.60 user 2.39 sys

forkserver: 48.44 real 7.56 user 1.39 sys

spawn: 51.70 real 50.97 user 23.85 sys

[src/guidellm/schemas/response.py](https://github.com/vllm-project/guidellm/pull/651/files#diff-bf8affbc3c40bc61ec258c3fcb7e66cad731d220378bc86d7a364c3b7258fe42)Outdated

|

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/88eb29c0fb78022bc16748216bde9b7db5fc739a..3acacc530a46d256788100b0d0e0957cf53ebc6f)the fix/mp_context branch from

[to](https://github.com/vllm-project/guidellm/commit/88eb29c0fb78022bc16748216bde9b7db5fc739a)

`88eb29c`


`3acacc5`

[Compare](https://github.com/vllm-project/guidellm/compare/88eb29c0fb78022bc16748216bde9b7db5fc739a..3acacc530a46d256788100b0d0e0957cf53ebc6f)

March 20, 2026 20:37


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Mar 20, 2026


[dbutenhof](https://github.com/dbutenhof)added

[feature](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Afeature)

[cleanup](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Acleanup)

Apr 10, 2026

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

Fixes spawn and forkserver multi-process contexts.

## Details

I was hoping that after #647 we could switch to

`forkserver`

by default. However it turns out that`forkserver`

and`spawn`

will import the calling processes entrypoint (E.g.`__main__.py`

) so we run into the same blocker as #641. However, I was able to confirm that striping every heavy import out of`__main__.py`

solves the issue. So we should be good to switch in v0.7.0.On my machine there is about a ~10s overhead for

`forkserver`

and slightly more for`spawn`

, which is not the worst for a default. However, the overhead may be more on other systems:`time guidellm benchmark run --profile poisson --rate 5 --data prompt_tokens=128,output_tokens=128 --max-seconds 30 --outputs json`

`time guidellm benchmark run --profile concurrent --rate 400 --data prompt_tokens=128,output_tokens=128 --max-seconds 30 --outputs json`

`time guidellm benchmark run --profile concurrent --rate 400 --data prompt_tokens=128,output_tokens=128 --max-seconds 120 --outputs json`

## Test Plan

Set

`GUIDELLM__MP_CONTEXT_TYPE=forkserver`

and confirm benchmarks run.## Use of AI

`## WRITTEN BY AI ##`

)