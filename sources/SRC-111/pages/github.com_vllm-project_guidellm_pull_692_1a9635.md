source: https://github.com/vllm-project/guidellm/pull/692

# Apply tool calling stats to the responses API - #692

Merged

[jaredoconnell](https://github.com/jaredoconnell)merged 2 commits into

Merged

## Conversation

Assisted-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>


**previously approved these changes**

[sjmonson](https://github.com/sjmonson)Apr 14, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)
Collaborator


There was a problem hiding this comment.

Minor nits but overall code looks good.

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/692/files/15a1d5d3b673b30ca01e1fd5b681ce805b70ee6a#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/692/files/15a1d5d3b673b30ca01e1fd5b681ce805b70ee6a#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated

Inline function and fix docstring Signed-off-by: Jared O'Connell <joconnel@redhat.com>


**approved these changes**

[sjmonson](https://github.com/sjmonson)Apr 14, 2026

6 tasks

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

This PR applies the same tool counting logic to the responses API.

## Details

## Test Plan

Start vLLM with tools enabled:


`--enable-auto-tool-choice --tool-call-parser hermes`

Run a benchmark:

Here is mixed_tool_call_prompts.jsonl

The logic is different with tool call auto vs required. It appears that required typically results in tool call only responses.

## Related Issues

## Use of AI

`## WRITTEN BY AI ##`

)