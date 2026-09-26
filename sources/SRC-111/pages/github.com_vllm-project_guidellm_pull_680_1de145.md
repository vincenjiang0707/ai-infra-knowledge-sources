source: https://github.com/vllm-project/guidellm/pull/680

# Revert back to iterating over lines - #680

## Conversation

###
**
**[Copilot](https://github.com/apps/copilot-pull-request-reviewer)
AI
left a comment

**left a comment**

[Copilot](https://github.com/apps/copilot-pull-request-reviewer)AI

There was a problem hiding this comment.

## Pull request overview

This PR adjusts the OpenAI HTTP streaming implementation to iterate over decoded text lines again (instead of splitting raw byte chunks), while still skipping blank newline separators, to avoid JSON parsing failures when a single SSE line is split across multiple network reads.

**Changes:**

- Switch
`_aiter_lines()`

from`Response.aiter_bytes()`

+`split(b"\n\n")`

to`Response.aiter_lines()`

- Preserve behavior of skipping blank/whitespace-only lines during streaming

💡 [Add Copilot custom instructions](https://github.com/vllm-project/guidellm/new/main?filename=.github/instructions/*.instructions.md) for smarter, more guided reviews. [Learn how to get started](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot).

[src/guidellm/backends/openai/http.py](https://github.com/vllm-project/guidellm/pull/680/files#diff-6a56e17b4a9b1b702100f54acf336f97d4de6346ea9f696bb23602d12c1f0002)


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Apr 1, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

Looks fine. Are there any potential problems with skipping blank lines?


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Apr 1, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

Let's get this in and freeze v0.6.

There shouldn't be. Its mainly to account for the fact that every data portion ends with
It does not seem like any of the OpenAI endpoints use this feature though since all of the data is on one line. |

Signed-off-by: Samuel Monson <smonson@redhat.com>

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/e0974727487496a674a65e21229fd87528d89b0b..155efd1253fb26a361b0b422c81244b0795b1f8f)the fix/gptoss_streaming branch from

[to](https://github.com/vllm-project/guidellm/commit/e0974727487496a674a65e21229fd87528d89b0b)

`e097472`


`155efd1`

[Compare](https://github.com/vllm-project/guidellm/compare/e0974727487496a674a65e21229fd87528d89b0b..155efd1253fb26a361b0b422c81244b0795b1f8f)

April 1, 2026 20:03

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

Partially reverts #663 to iterating over lines, but keeps the skipping of blank newlines.

## Details

#663 switched the HTTP backend to iterating over byte strings. The problem is that is did not handle the case where a line was split over multiple iterations.

## Test Plan

Run a benchmark with known errored request rate (preferably 0) and ensure that there are no failed requests due to

`orjson.JSONDecodeError: unexpected end of data`

.## Use of AI

`## WRITTEN BY AI ##`

)