source: https://github.com/vllm-project/guidellm/pull/752

# Fix TypeError when streaming delta has tool_calls=null - #752

## Conversation


**reviewed**

[dbutenhof](https://github.com/dbutenhof)May 29, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

For reference, it'd be useful to know what server and model did this.

Given that this behavior has been seen, the change seems reasonable as long as we're OK with non-null falsey values silently slipping through this path -- but the comment is a bit misleading.

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/752/files#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated


[dbutenhof](https://github.com/dbutenhof)added

[community contribution](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3A%22community%20contribution%22)

[bug](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Abug)

[escape](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Aescape)

May 29, 2026

|
Thanks for the review. This happens when running |

Some OpenAI-compatible servers emit ``"tool_calls": null`` inside streaming chat completion deltas. ``dict.get("tool_calls", [])`` only returns the default when the key is missing, so for an explicit ``null`` the iteration was attempted on ``None``, raising ``TypeError: 'NoneType' object is not iterable`` and erroring the request. Coerce ``None`` to an empty list before iterating. Signed-off-by: Radoslav Gerganov <rgerganov@gmail.com>


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)May 29, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

The "correctness" of this change hinges on whether we care about bizarre falsey values (`0`

, `false`

, `{}`

, etc). However in context I'm not sure that's something we'd want to track as an "error" so I'm satisfied as long as nobody else objects.

"For the record" it might be helpful for the commit message to identify the server and model where you see this behavior.


**approved these changes**

[sjmonson](https://github.com/sjmonson)May 29, 2026

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

Some OpenAI-compatible servers emit


`"tool_calls": null`

inside streaming chat completion deltas.`dict.get("tool_calls", [])`

only returns the default when the key is missing, so for an explicit`null`

the iteration was attempted on`None`

, raising`TypeError: 'NoneType' object is not iterable`

and erroring the request. Coerce`None`

to an empty list before iterating.## Use of AI