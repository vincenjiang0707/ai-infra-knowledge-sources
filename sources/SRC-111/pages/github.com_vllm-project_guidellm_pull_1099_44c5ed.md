source: https://github.com/vllm-project/guidellm/pull/1099

# fix(openai): validate non-streaming tool calls before yielding - #1099

[mergify[bot]](https://github.com/mergify[bot])merged 3 commits into

[mergify[bot]](https://github.com/mergify[bot]) merged 3 commits into

[mergify[bot]](https://github.com/mergify[bot])merged 3 commits into

## Conversation

|
Hi |

Generated-by: OpenAI Codex GPT-5 Signed-off-by: Divyam Talwar <divyamtalwar0@gmail.com>

[DivyamTalwar](https://github.com/DivyamTalwar)

[force-pushed](https://github.com/vllm-project/guidellm/compare/cd228ab7adb501717da7e6fa98e2e0964d1a1938..45255cfac7ce0c0f3b6b76ae29f435dd083a2f60)the fix/nonstream-missing-tool-call-order branch from

[to](https://github.com/vllm-project/guidellm/commit/cd228ab7adb501717da7e6fa98e2e0964d1a1938)

`cd228ab`


`45255cf`

[Compare](https://github.com/vllm-project/guidellm/compare/cd228ab7adb501717da7e6fa98e2e0964d1a1938..45255cfac7ce0c0f3b6b76ae29f435dd083a2f60)

September 8, 2026 07:52


**previously approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Sep 9, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

Looks good. Thank you.

|
Queued — the merge queue status continues in |

Preserve upstream Responses streaming coverage and keep the non-streaming tool-call ordering regression in a dedicated test module. Generated-by: OpenAI GPT-5.6 Sol Signed-off-by: Divyam Talwar <divyamtalwar0@gmail.com>

|
Why was the test just moved to a new file? |

|
|


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Sep 9, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

Looks fine. I don't really care about breaking apart a test file, although this bothers me just a bit because the new test file name is so specific to this particular test case, and I don't think we want to degenerate towards "a file per test case". On the whole, at this point it's probably better to put that thing back where it came from ...

Move the non-streaming tool-call ordering regression back into TestOpenAIHTTPBackend and reuse its existing request-handler fixture. Remove the standalone test module and its duplicated setup. Preserve both error_stop and ignore_stop cases, all upstream HTTP tests, and the existing runtime fix without behavioral changes. Generated-by: ChatGPT Signed-off-by: Divyam Talwar <divyamtalwar0@gmail.com>

|
Thanks `mock_request_handler` fixture. Removed `test_nonstream_tool_call_order.py` and its duplicated setup. Both `error_stop` /`ignore_stop` cases and the upstream streaming tests are preserved; the runtime fix is unchanged.Syntax/source-equivalence checks and |


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Sep 9, 2026


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Sep 9, 2026

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

Non-streaming OpenAI requests that required a tool call yielded a successful response before reporting that the model omitted the tool call. This makes

`error_stop`

consistent with the documented streaming behavior: it now raises before any final response is emitted, while`ignore_stop`

still emits the compiled response once and then stops the conversation.## Details

`ignore_stop`

by yielding the compiled response once when the validation raises`CancelledError`

, then re-raising it.`error_stop`

and`ignore_stop`

yield ordering.## Test Plan

`MagicMock`

pickling tracebacks were emitted during the run.`git diff --check`

passes.The base regression failed for

`error_stop`

because one response was yielded before the expected`ValueError`

;`ignore_stop`

passed its one-yield behavior. Full tox could not finish because the locked development group installs large optional Torch/audio/vision dependencies under shared network contention. The focused checks use the real project code and direct test dependencies without mocking unavailable project internals.No existing issue or competing open/closed PR was found for this ordering defect. Merged PR #839 defines the missing-tool-call behavior but does not cover the non-streaming yield order.

## Use of AI

The code and tests were generated with OpenAI Codex and require human review before submission.

The commit includes the required

`Generated-by: OpenAI Codex GPT-5`

trailer.## git log

commit

45255cfAuthor: Divyam Talwar divyamtalwar0@gmail.com

Date: Tue Sep 8 07:03:03 2026 +0530

commit

b6e81fdAuthor: Divyam Talwar divyamtalwar0@gmail.com

Date: Thu Sep 10 00:56:33 2026 +0530

Generated-by: ChatGPT

Generated-by: OpenAI Codex GPT-5

Signed-off-by: Divyam Talwar divyamtalwar0@gmail.com