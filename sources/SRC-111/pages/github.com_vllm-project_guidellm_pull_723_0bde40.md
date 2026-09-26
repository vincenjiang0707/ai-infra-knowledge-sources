source: https://github.com/vllm-project/guidellm/pull/723

# [v0.7 CLI Refactor] Rework BackendArgs to be the authoritative config location - #723

## Conversation

Signed-off-by: Samuel Monson <smonson@redhat.com> Assisted-by: Copilot <GPT-4.1>

Signed-off-by: Samuel Monson <smonson@redhat.com> Assisted-by: Copilot <GPT-4.1>

Signed-off-by: Samuel Monson <smonson@redhat.com> Assisted-by: Copilot <GPT-4.1>

Signed-off-by: Samuel Monson <smonson@redhat.com> Generated-by: claude-code <Sonnet 4.6>

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/567812b9efa2feda30474f4f384ea3ba5984e72c..cc2a59fd0a9d82e828bc877a9c10949d605f3b6c)the refactor/schema/backend branch from

[to](https://github.com/vllm-project/guidellm/commit/567812b9efa2feda30474f4f384ea3ba5984e72c)

`567812b`


`cc2a59f`

[Compare](https://github.com/vllm-project/guidellm/compare/567812b9efa2feda30474f4f384ea3ba5984e72c..cc2a59fd0a9d82e828bc877a9c10949d605f3b6c)

May 7, 2026 19:04

[sjmonson](https://github.com/sjmonson)marked this pull request as ready for review

May 7, 2026 19:04

Signed-off-by: Samuel Monson <smonson@redhat.com>

|
|

Signed-off-by: Samuel Monson <smonson@redhat.com> Generated-by: claude-code <Sonnet 4.6>

|
augment review |

|


**reviewed**

[augmentcode](https://github.com/apps/augmentcode)BotMay 8, 2026

[src/guidellm/backends/backend.py](https://github.com/vllm-project/guidellm/pull/723/files/7ae41f6988cd2c3bd8fdeace53a09380d4dad4db#diff-5c24e7ba3bcac69581ff50255450d871c262dddfc1a230cd42aeac92882d4bc5)

[src/guidellm/backends/openai/http.py](https://github.com/vllm-project/guidellm/pull/723/files/7ae41f6988cd2c3bd8fdeace53a09380d4dad4db#diff-6a56e17b4a9b1b702100f54acf336f97d4de6346ea9f696bb23602d12c1f0002)

[src/guidellm/cli/benchmark/run.py](https://github.com/vllm-project/guidellm/pull/723/files/7ae41f6988cd2c3bd8fdeace53a09380d4dad4db#diff-310250441381ed1c3efd1052124a9ab915eb1ec368404345bc7037069660a46a)

Signed-off-by: Samuel Monson <smonson@redhat.com>


**previously approved these changes**

[dbutenhof](https://github.com/dbutenhof)May 8, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

I pulled it and tried various good and bad option values e.g. for the backend args, and all seems to work, which is one definition of "good".

[src/guidellm/backends/backend.py](https://github.com/vllm-project/guidellm/pull/723/files/7ae41f6988cd2c3bd8fdeace53a09380d4dad4db#diff-5c24e7ba3bcac69581ff50255450d871c262dddfc1a230cd42aeac92882d4bc5)

[src/guidellm/backends/openai/http.py](https://github.com/vllm-project/guidellm/pull/723/files/943cfedd21ff390a55cfc007357c5ab090af8161#diff-6a56e17b4a9b1b702100f54acf336f97d4de6346ea9f696bb23602d12c1f0002)

Signed-off-by: Samuel Monson <smonson@redhat.com> Generated-by: claude-code Sonnet 4.6

|
Forgot I was going to use this chance to move |


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)May 8, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

Looks good to me. I tested basic use cases with the HTTP and vLLM-Python backend.

[src/guidellm/backends/vllm_python/vllm.py](https://github.com/vllm-project/guidellm/pull/723/files/7ae41f6988cd2c3bd8fdeace53a09380d4dad4db#diff-6469481616de32d01585d227edd34721157d75fb5b6b89c628e0269430dd91f0)

[src/guidellm/backends/openai/http.py](https://github.com/vllm-project/guidellm/pull/723/files/943cfedd21ff390a55cfc007357c5ab090af8161#diff-6a56e17b4a9b1b702100f54acf336f97d4de6346ea9f696bb23602d12c1f0002)


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)May 8, 2026

[tests/unit/backends/test_backend.py](https://github.com/vllm-project/guidellm/pull/723/files/67ffc643bb3ca25cf559dd8e575392d90fdf31e7#diff-f20a7a1b8bad86e9f5b522325157967ed295baaebb40213f58cd4995c34f8b62)

|
This looks ready to merge. I have no further comments after seeing your responses. |

Changed my mind about this. I'll do it in a follow-up after |

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

Reworks

`BackendArgs`

into a`PydanticClassRegistry`

containing everything needed to create a backend.## Details

This is the first (or third depending on how you count) patch to refactor our CLI and the internal way submodules are configured and spawned. Since we already had a partial base for it this will likely be the simplest PR and subsequent PRs will have to rework a lot more code.

Changes to the entrypoints and CLI are temporary as that code will be refactored in a follow-up.

## Changes

I tried to keep most of the original functionality but there were a few things that just did not make sense as implemented or were planned for removal:

## Dropped

`LEGACY_API_ALIASES`

They only exist to keep existing scripts from breaking and this release those scripts will break for other reasons so might as well make the change now.

## Dropped

`request_handlers`

backend argumentThis let the user provide custom request type handlers as a backend argument. The better way to do this is to just call

`OpenAIRequestHandlerFactory.register`

on your custom handler.`validate_backend`

no longer has the option to provide a custom health check endpointYou can get nearly the same functionality by passing

`api_routes={"/health": "custom endpoint"}`

. However users usually just set`validate_backend=False`

since its too much of a hassle to provide a custom endpoint.## Test Plan

Test setting

`--backend`

and`--backend-kwargs`

with various values to make sure nothing has changed (except for exceptions detailed below).## Related Issues

`backends`

and`benchmark`

#725## Use of AI

`## WRITTEN BY AI ##`

)