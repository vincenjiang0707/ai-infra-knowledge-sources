source: https://github.com/vllm-project/guidellm/pull/589

# Drop various depricated settings and remove the default OpenAI request timeout - #589

Merged

Merged

## Conversation

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/b088a667a45d04bd58b4ab16ad633784f00cba82..76511f8ca7a2ef476ff315dd09aec2f49c6e1fe2)the fix/timeout branch from

[to](https://github.com/vllm-project/guidellm/commit/b088a667a45d04bd58b4ab16ad633784f00cba82)

`b088a66`


`76511f8`

[Compare](https://github.com/vllm-project/guidellm/compare/b088a667a45d04bd58b4ab16ad633784f00cba82..76511f8ca7a2ef476ff315dd09aec2f49c6e1fe2)

February 11, 2026 14:45


**commented**

[sjmonson](https://github.com/sjmonson)Feb 11, 2026

[src/guidellm/backends/openai/http.py](https://github.com/vllm-project/guidellm/pull/589/files/76511f8ca7a2ef476ff315dd09aec2f49c6e1fe2#diff-6a56e17b4a9b1b702100f54acf336f97d4de6346ea9f696bb23602d12c1f0002)

[sjmonson](https://github.com/sjmonson)marked this pull request as ready for review

February 11, 2026 14:54


**previously approved these changes**

[dbutenhof](https://github.com/dbutenhof)Feb 11, 2026

[src/guidellm/backends/openai/http.py](https://github.com/vllm-project/guidellm/pull/589/files/76511f8ca7a2ef476ff315dd09aec2f49c6e1fe2#diff-6a56e17b4a9b1b702100f54acf336f97d4de6346ea9f696bb23602d12c1f0002)Outdated

[src/guidellm/backends/openai/http.py](https://github.com/vllm-project/guidellm/pull/589/files/76511f8ca7a2ef476ff315dd09aec2f49c6e1fe2#diff-6a56e17b4a9b1b702100f54acf336f97d4de6346ea9f696bb23602d12c1f0002)Outdated

[src/guidellm/utils/text.py](https://github.com/vllm-project/guidellm/pull/589/files/76511f8ca7a2ef476ff315dd09aec2f49c6e1fe2#diff-a8105e52fbc0d3dc590631506ff0e5d614c08bed2667f4718c9eb5b626dc6e5e)


**previously approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Feb 11, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)
Collaborator


There was a problem hiding this comment.

Looks good. I agree with Dave's comment on the comment on the default.

[src/guidellm/backends/openai/http.py](https://github.com/vllm-project/guidellm/pull/589/files/76511f8ca7a2ef476ff315dd09aec2f49c6e1fe2#diff-6a56e17b4a9b1b702100f54acf336f97d4de6346ea9f696bb23602d12c1f0002)Outdated

Signed-off-by: Samuel Monson <smonson@redhat.com>

[sjmonson](https://github.com/sjmonson)dismissed stale reviews from

[jaredoconnell](https://github.com/jaredoconnell)and

[dbutenhof](https://github.com/dbutenhof)via

```
```[d13a9e4](https://github.com/vllm-project/guidellm/commit/d13a9e46b6f7c4bca388663dbd64ff642c7dbb93)

February 11, 2026 17:18


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Feb 11, 2026

6 tasks

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Drops the global

`GUIDELLM__REQUEST_TIMEOUT`

as it was not wired up and adjusts the OpenAI request timeout to infinte for reads and 5 seconds for all other operations, with a tunable for connect timeouts.## Details

The

`GUIDELLM__REQUEST_TIMEOUT`

setting used to configure HTTP timeouts for the OpenAI backend to a default of 5 minutes. However since v0.4.0 the backend has had its own default value of 1 minute. Rather then wire this back up I have opted to remove the global setting entirely since timeout can be configured with`--backend-kwargs '{"timeout": 6000}'`

.For the backend default httpx supports setting separate timeouts for connect, read, write, etc.

`timeout`

backend argument now only configures`read`

timeouts and defaults to no timeout. The`connect`

timeout can be configured with the backend argument`timeout_connect`

and defaults to 5 seconds (httpx default). All other timeouts are set to 5 seconds (httpx default)One major risk with this change is benchmarks that do not set any time based constraints can potentially deadlock if the the server stalls. This is very unlikely since it will require the server to hold connections open while stalled. It is also partially mitigated by setting a timeout for connect as in this case the only connection that can stall are in-progress ones where GuideLLM is waiting for a response. A functioning server should also close connections when they stall rather then holding them open.

## Test Plan

Run oversaturated server tests and confirm that timeout errors do not occur or only occur on server crash.

## Use of AI

`## WRITTEN BY AI ##`

)