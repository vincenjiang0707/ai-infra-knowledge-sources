source: https://github.com/vllm-project/guidellm/pull/739

# Feat/multi turn tools responses - #739

Merged

[jaredoconnell](https://github.com/jaredoconnell)merged 2 commits into

Merged

[jaredoconnell](https://github.com/jaredoconnell) merged 2 commits into

[jaredoconnell](https://github.com/jaredoconnell)merged 2 commits into

## Conversation


[dbutenhof](https://github.com/dbutenhof)added

[priority-high](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Apriority-high)

[internal](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Ainternal)

[feature](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Afeature)

May 26, 2026


**requested changes**

[sjmonson](https://github.com/sjmonson)May 26, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)
Collaborator


There was a problem hiding this comment.

Few minor nits. Otherwise looks good.

[docs/guides/multiturn.md](https://github.com/vllm-project/guidellm/pull/739/files#diff-b8c613ed380ab7cd9bd8b09b3ba7f883c2f7233af1f1a5b79bcef3c14c2ef903)Outdated

[docs/guides/multiturn.md](https://github.com/vllm-project/guidellm/pull/739/files#diff-b8c613ed380ab7cd9bd8b09b3ba7f883c2f7233af1f1a5b79bcef3c14c2ef903)Outdated

[docs/guides/tool_calling.md](https://github.com/vllm-project/guidellm/pull/739/files#diff-61af4f8d78e766b599dc58cd80c99c7b4be40899e4726feaf6deb3819f4a658b)Outdated

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/739/files#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/739/files#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated

Contributor

|
This pull request has merge conflicts that must be resolved before it can be |


**reviewed**

[dbutenhof](https://github.com/dbutenhof)May 27, 2026

[docs/guides/tool_calling.md](https://github.com/vllm-project/guidellm/pull/739/files#diff-61af4f8d78e766b599dc58cd80c99c7b4be40899e4726feaf6deb3819f4a658b)Outdated

[jaredoconnell](https://github.com/jaredoconnell)

[force-pushed](https://github.com/vllm-project/guidellm/compare/d138085f6ff60ac8aff4b544dc6ffa73f42eac30..a06851e37ed8533183879e2bcce69d5bfb6793eb)the feat/multi-turn-tools-responses branch from

[to](https://github.com/vllm-project/guidellm/commit/d138085f6ff60ac8aff4b544dc6ffa73f42eac30)

`d138085`


`a06851e`

[Compare](https://github.com/vllm-project/guidellm/compare/d138085f6ff60ac8aff4b544dc6ffa73f42eac30..a06851e37ed8533183879e2bcce69d5bfb6793eb)

May 28, 2026 19:26

[jaredoconnell](https://github.com/jaredoconnell)

[force-pushed](https://github.com/vllm-project/guidellm/compare/5c02e61ca56c8dbf3ebd3347c9156bdf84d40fc9..dd66000079cc03d0f890558421f275c3d48fe515)the feat/multi-turn-tools-responses branch 2 times, most recently from

[to](https://github.com/vllm-project/guidellm/commit/5c02e61ca56c8dbf3ebd3347c9156bdf84d40fc9)

`5c02e61`


`dd66000`

[Compare](https://github.com/vllm-project/guidellm/compare/5c02e61ca56c8dbf3ebd3347c9156bdf84d40fc9..dd66000079cc03d0f890558421f275c3d48fe515)

May 28, 2026 21:02


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)May 28, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

Still shows a conflict to resolve; but

Collaborator
Author

I don't see that on my view. |

Collaborator

Sometimes GitHub's UI is really flaky; anyway, something "caught up" and it's no longer showing. Weird. |


**approved these changes**

[sjmonson](https://github.com/sjmonson)May 29, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)
Collaborator


There was a problem hiding this comment.

Sorry forgot I was blocking

[jaredoconnell](https://github.com/jaredoconnell)

[force-pushed](https://github.com/vllm-project/guidellm/compare/dd66000079cc03d0f890558421f275c3d48fe515..90e506d85f2e7cf4b33cf8a0b301d6bfb1202e84)the feat/multi-turn-tools-responses branch from

[to](https://github.com/vllm-project/guidellm/commit/dd66000079cc03d0f890558421f275c3d48fe515)

`dd66000`


`90e506d`

[Compare](https://github.com/vllm-project/guidellm/compare/dd66000079cc03d0f890558421f275c3d48fe515..90e506d85f2e7cf4b33cf8a0b301d6bfb1202e84)

May 29, 2026 14:27

Also fixes other discrepancies. Make docs more concise. Document the tool call schema format Fix server side history for tool calls Assisted-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Filter tool choice for non-tool-call requests and other improvements This was required for later versions of vLLM. Also uses updated logic for when to show the tool stats table. Assisted-by: Cursor AI Claude Opus 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com> Co-authored-by: Cursor <cursoragent@cursor.com>

[jaredoconnell](https://github.com/jaredoconnell)

[force-pushed](https://github.com/vllm-project/guidellm/compare/90e506d85f2e7cf4b33cf8a0b301d6bfb1202e84..b51f58e820a48ac46f25379bd8976d3160d29f3c)the feat/multi-turn-tools-responses branch from

[to](https://github.com/vllm-project/guidellm/commit/90e506d85f2e7cf4b33cf8a0b301d6bfb1202e84)

`90e506d`


`b51f58e`

[Compare](https://github.com/vllm-project/guidellm/compare/90e506d85f2e7cf4b33cf8a0b301d6bfb1202e84..b51f58e820a48ac46f25379bd8976d3160d29f3c)

May 29, 2026 16:39

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Adds tool call support to the responses API. Just implements what was previously implemented for the chat completions handler. Also makes other improvements.

## Details

## Test Plan

## Related Issues

## Use of AI