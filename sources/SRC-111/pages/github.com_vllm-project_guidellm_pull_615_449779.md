source: https://github.com/vllm-project/guidellm/pull/615

# Fix worker status for unusable terminal backend responses - #615

[mergify[bot]](https://github.com/mergify[bot])merged 7 commits into

[mergify[bot]](https://github.com/mergify[bot]) merged 7 commits into

[mergify[bot]](https://github.com/mergify[bot])merged 7 commits into

## Conversation

[ushaket](https://github.com/ushaket)marked this pull request as draft

February 26, 2026 09:38

|
This introduce worker dependency on GenerationResponse, not sure if that's the right way to go, |

|
Hmm, yeah I am not a fan of depending on |

[ushaket](https://github.com/ushaket)marked this pull request as ready for review

March 2, 2026 21:59

|
Done |


**requested changes**

[sjmonson](https://github.com/sjmonson)Mar 3, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

Can you rebase and get rid of the merge commits?

|
You can do this by running: |

[ushaket](https://github.com/ushaket)

[force-pushed](https://github.com/vllm-project/guidellm/compare/60e1abceddfd915bab0ef0a4416242d882142483..d35b823a7810cbf9bf478f860ade6db6d07c1a09)the fix/worker-unusable-terminal-response branch from

[to](https://github.com/vllm-project/guidellm/commit/60e1abceddfd915bab0ef0a4416242d882142483)

`60e1abc`


`d35b823`

[Compare](https://github.com/vllm-project/guidellm/compare/60e1abceddfd915bab0ef0a4416242d882142483..d35b823a7810cbf9bf478f860ade6db6d07c1a09)

March 30, 2026 13:12

[ushaket](https://github.com/ushaket)

[force-pushed](https://github.com/vllm-project/guidellm/compare/d35b823a7810cbf9bf478f860ade6db6d07c1a09..d82eb51c866f3153a25b16f275fb150fe41ca39a)the fix/worker-unusable-terminal-response branch from

[to](https://github.com/vllm-project/guidellm/commit/d35b823a7810cbf9bf478f860ade6db6d07c1a09)

`d35b823`


`d82eb51`

[Compare](https://github.com/vllm-project/guidellm/compare/d35b823a7810cbf9bf478f860ade6db6d07c1a09..d82eb51c866f3153a25b16f275fb150fe41ca39a)

March 30, 2026 13:18

[ushaket](https://github.com/ushaket)

[force-pushed](https://github.com/vllm-project/guidellm/compare/d82eb51c866f3153a25b16f275fb150fe41ca39a..438814921aabeeee7c276d4c689f2eddb17138d2)the fix/worker-unusable-terminal-response branch from

[to](https://github.com/vllm-project/guidellm/commit/d82eb51c866f3153a25b16f275fb150fe41ca39a)

`d82eb51`


`4388149`

[Compare](https://github.com/vllm-project/guidellm/compare/d82eb51c866f3153a25b16f275fb150fe41ca39a..438814921aabeeee7c276d4c689f2eddb17138d2)

July 15, 2026 07:54


[dbutenhof](https://github.com/dbutenhof)added

[community contribution](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3A%22community%20contribution%22)

[bug](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Abug)

Jul 15, 2026


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Jul 15, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

I have really mixed feelings about this. I don't like the idea of hacking this into each request handler separately -- and you've only handled a subset of the http request handlers in this PR. Maybe that's OK, but it feels weird.

I like your original idea of triggering this through the worker, perhaps by delegating to a backend `validate_response`

method (which could, if necessary, delegate to individual request handlers where more specialized knowledge is required). Your check, for example, is pretty much generic and might even be a default implementation on the base `Backend`

class that everyone would get by default.

(The risk, of course, is that such a default might break some weird special handlers that don't have "normal" text/token outputs; which means a generalization would require extensive testing through all the validations.)

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/615/files#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated


**approved these changes**

[SkiHatDuckie](https://github.com/SkiHatDuckie)Jul 16, 2026

[tests/unit/backends/openai/test_request_handlers.py](https://github.com/vllm-project/guidellm/pull/615/files#diff-3286b6da9cffd79259ed9c187e72530fdb2f407c0454af81bfc5c28a79045faa)

|
I prototyped extending this to Responses (same text / tool_calls / tokens check) and Embeddings (raw data[].embedding check, since those responses never have text). Happy to include either or both in this PR if that’s useful. How would you like to proceed? Keep this PR scoped to text/chat and take broader coverage in a follow-up I’m fine with any of these, just want to align before I push more surface area into this PR. |

Yeah, the risk is the "special cases" that don't have text, like embeddings, Geospatial pooling requests (I think), and maybe others. While I like the idea of a meaningful A safer alternative is probably a base implementation that does nothing, overridden by the various backends & request format handlers as necessary... I do prefer centralizing it from the worker loop, delegating through the backend to the request format... but as most of the implementation probably falls to the request formatter, maybe it doesn't matter much. |

Dave's proposal sounds good. It can have a default implementation that is permissive, and can be overridden whenever you need to validate this. The function could maybe be called "post_validation". One thing that needs to be kept in mind is that for the chat completions endpoints and the responses API, no text is valid due to tool calls, and for other endpoints it's valid due to non-token content. |

Signed-off-by: Uri Shaket <ushaket@redhat.com>

Signed-off-by: Uri Shaket <ushaket@redhat.com>

Signed-off-by: Uri Shaket <ushaket@redhat.com> Co-authored-by: Cursor <cursoragent@cursor.com>

Add post_validation to OpenAIRequestHandler and OpenAIWSRequestHandler protocols with a permissive no-op default. TextCompletionsRequestHandler and ResponsesRequestHandler override with a check for text, tool_calls, or output_tokens. PoolingRequestHandler and EmbeddingsRequestHandler keep the default no-op since they produce non-text output. Validation is called from the backend resolve methods (http.py, websocket.py) after compile, not inside each handler's compile methods. Cancellation paths skip validation for partial responses. Fixes tool-call-only false negative: responses with tool_calls but no text are now correctly treated as valid output. Assisted-by: Claude Signed-off-by: Uri Shaket <ushaket@redhat.com> Co-authored-by: Cursor <cursoragent@cursor.com>

[ushaket](https://github.com/ushaket)

[force-pushed](https://github.com/vllm-project/guidellm/compare/509ce957dd05bfc7ba5a7d4cf49da6a7d02bc2b8..1789158ca2cedcf63d8ef55927ee77e77358c03a)the fix/worker-unusable-terminal-response branch from

[to](https://github.com/vllm-project/guidellm/commit/509ce957dd05bfc7ba5a7d4cf49da6a7d02bc2b8)

`509ce95`


`1789158`

[Compare](https://github.com/vllm-project/guidellm/compare/509ce957dd05bfc7ba5a7d4cf49da6a7d02bc2b8..1789158ca2cedcf63d8ef55927ee77e77358c03a)

July 21, 2026 18:14

|
Thanks
Kept it at the backend resolve level rather than the worker loop since the implementation lives on the request handlers anyway as |

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

This seems like an appropriate design. One thing is that `OpenAIRequestHandler`

is a protocol, so there is no default implementation. So no-op calls need to be added to `RealtimeTranscriptionWSRequestHandler`

and `EmbeddingsRequestHandler`

.

And I added a comment regarding de-duplicating the function you added.

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/615/files/1789158ca2cedcf63d8ef55927ee77e77358c03a#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)


**requested changes**

[dbutenhof](https://github.com/dbutenhof)Jul 21, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

I think there are a lot of compromises in this approach, but it's probably the lowest touch and safest. I'd like to see more consistent style in your validation methods, including docstrings; but aside from that, it's probably as good as it gets.

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/615/files/1789158ca2cedcf63d8ef55927ee77e77358c03a#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/615/files/1789158ca2cedcf63d8ef55927ee77e77358c03a#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/615/files/1789158ca2cedcf63d8ef55927ee77e77358c03a#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)

Extract _validate_text_response helper shared by TextCompletionsRequestHandler and ResponsesRequestHandler. Add docstrings to all post_validation overrides. Assisted-by: Claude Signed-off-by: Uri Shaket <ushaket@redhat.com> Co-authored-by: Cursor <cursoragent@cursor.com>


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jul 29, 2026


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jul 29, 2026

|
|


**approved these changes**

[sjmonson](https://github.com/sjmonson)Jul 30, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

My bad, forgot I blocked this.

|
|

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

This PR fixes a scheduler correctness bug where requests could be marked as

`completed`

even when the backend resolved without a usable terminal response. It adds explicit terminal-response validation in the worker so malformed/empty terminal results are surfaced as`errored`

with a clear diagnostic instead of being counted as successful requests.## Details

`WorkerProcess`

to guard final status transitions.`errored`

`[UNUSABLE_BACKEND_RESPONSE] backend resolved without a usable terminal response payload`

`GenerationResponse`

-aware usability criteria:`text`

or`output_metrics.total_tokens > 0`

`None`

terminal response is always unusable`GenerationResponse`

fallback remains`bool(response)`

for generic/test compatibility`tests/unit/scheduler/test_worker.py`

for:`errored`

`GenerationResponse`

->`errored`

`GenerationResponse`

with empty text ->`completed`

## Test Plan

`uv run pytest -q tests/unit/scheduler/test_worker.py -k "terminal_response or empty_generation_response or generation_response_with_tokens or invalid_initialization"`

`completed`

`GenerationResponse`

is not marked`completed`

`output_tokens > 0`

) is accepted as`completed`

## Related Issues

## Use of AI

`## WRITTEN BY AI ##`

)## git log

commit

ffedeceAuthor: Uri Shaket ushaket@redhat.com

Date: Mon Mar 2 23:55:49 2026 +0200

commit

03cdec7Author: Uri Shaket ushaket@redhat.com

Date: Mon Mar 2 23:57:34 2026 +0200

commit

e5fda32Author: Uri Shaket ushaket@redhat.com

Date: Wed Jul 15 11:25:12 2026 +0300

commit

d459b2eAuthor: Uri Shaket ushaket@redhat.com

Date: Wed Jul 15 13:23:05 2026 +0300

commit

36036d0Author: Uri Shaket ushaket@redhat.com

Date: Thu Jul 16 17:28:58 2026 +0300

commit

1789158Author: Uri Shaket ushaket@redhat.com

Date: Tue Jul 21 20:39:29 2026 +0300

commit

6de940aAuthor: Uri Shaket ushaket@redhat.com

Date: Thu Jul 23 09:44:58 2026 +0300

Assisted-by: Claude

Co-authored-by: Cursor cursoragent@cursor.com

Signed-off-by: Uri Shaket ushaket@redhat.com