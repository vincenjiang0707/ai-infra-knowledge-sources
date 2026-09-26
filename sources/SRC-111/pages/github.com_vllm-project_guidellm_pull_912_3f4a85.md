source: https://github.com/vllm-project/guidellm/pull/912

# Correct the CSV report format - #912

## Conversation

The root problem stems from attempts to serialize the Pydantic `SecretStr`. This was resolved for JSON format by serializing `BenchmarkConfig` using `model_dump(mode="json")`, but the CSV serialization breaks up the context very differently, leading to solutions that are either very specific or rather sweeping. It appears the simplest and least invasive fix is to call `model_dump(mode="json")` on the `OpenAIHTTPBackend.info` method, which is the only place we use `SecretStr`. We could benefit in the future from some refactoring. For example, it's odd that we convert the `Backend` to a `dict` when creating `BenchmarkConfig`, but then reconstruct the `Backend` when we call the benchmarker `run` method for each strategy. Signed-off-by: David Butenhof <dbutenho@redhat.com>


[dbutenhof](https://github.com/dbutenhof)added

[bug](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Abug)

[escape](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Aescape)

Jul 7, 2026


**reviewed**

[sjmonson](https://github.com/sjmonson)Jul 7, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

Seems like a reasonable fix to me but should it get applied to the other backends as well for constancy?


**previously approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jul 7, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

Looks good. If there are other places this should get applied, as Sam mentioned, let's apply it to those cases, too.

|
Queued — the merge queue status continues in |

Fair ... I kept it simple since we only have the "complicated" container object inside HTTP. (And then I read the LiteLLM PR, which will have the same issue.) If I was going a step further I might be strongly tempted to factor |

Signed-off-by: David Butenhof <dbutenho@redhat.com>


**previously approved these changes**

[sjmonson](https://github.com/sjmonson)Jul 7, 2026

Rather than annotate every args field access, we need to set `_args` as the proper type to support static type checking. (For some reason I keep thinking I'm writing in Python, when I'm actually writing in ruff...) Signed-off-by: David Butenhof <dbutenho@redhat.com>

"Amusingly" I discovered that the web socket backend was storing its This was stupidly complicated by static type checking, since I can't just store |

|
I really don't like |

😞 -- this is already a mess just to work around static type checking and make it behave like Python. I'm not a fan of routine Sigh. |

Oh, wait -- there's a better way to deal with the type checker. Foolish of me ... |

Signed-off-by: David Butenhof <dbutenho@redhat.com>


**approved these changes**

[sjmonson](https://github.com/sjmonson)Jul 7, 2026


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jul 9, 2026

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

Once again fix

`api_key`

serialization (this time for CSV).## Details

The root problem stems from attempts to serialize the Pydantic

`SecretStr`

.This was resolved for JSON format by serializing

`BenchmarkConfig`

using`model_dump(mode="json")`

, but the CSV serialization breaks up the context very differently, leading to solutions that are either very specific or rather sweeping.It appears the simplest and least invasive fix is to call

`model_dump(mode="json")`

on the`OpenAIHTTPBackend.info`

method. This is the only place we use`SecretStr`

, and feeds the JSON we serialize to CSV.`info`

is only intended for "informational" serialization, so the masked password we receive is expected and correct.We could benefit in the future from some refactoring. For example, it's odd that we convert the

`Backend`

to a`dict`

when creating`BenchmarkConfig`

, but then reconstruct the`Backend`

when we call the benchmarker`run`

method for each strategy.## Test Plan

`--backend kind=openai_http,api_key=<value>`

## Related Issues

## Use of AI

## git log

commit

e99d9a3Author: David Butenhof dbutenho@redhat.com

Date: Tue Jul 7 14:08:50 2026 -0400

commit

ba2aa23Author: David Butenhof dbutenho@redhat.com

Date: Tue Jul 7 15:40:27 2026 -0400

commit

33ed889Author: David Butenhof dbutenho@redhat.com

Date: Tue Jul 7 16:09:14 2026 -0400

commit

3b8e599Author: David Butenhof dbutenho@redhat.com

Date: Tue Jul 7 16:44:26 2026 -0400

Signed-off-by: David Butenhof dbutenho@redhat.com