source: https://github.com/vllm-project/guidellm/pull/595

# Fix /v1/chat/completions formatting - #595

Merged

Merged

## Conversation

Signed-off-by: Samuel Monson <smonson@redhat.com>


**commented**

[sjmonson](https://github.com/sjmonson)Feb 11, 2026

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/595/files/9a2a725e41d73c5ae7dd8a741dfaa93849b6203b#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)

Signed-off-by: Samuel Monson <smonson@redhat.com>


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Feb 11, 2026

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/595/files/9a2a725e41d73c5ae7dd8a741dfaa93849b6203b#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/595/files/e08b02c3ee4667c894c2466ec08f9afa9204295c#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Format each data column as content sections rather than completely separate messages.

## Details

The chat completions interface consists of a list of messages. Each message is intend to represent a turn in the conversation. Within each message there is a content section that can be a list if multiple types of content are being passed. See #594 for more complete detail of the problem.

## Test Plan

Run GuideLLM with

`--request-format /v1/chat/completions`

against a server endpoint then compare request_args format before and after patch/## Related Issues

## Use of AI

`## WRITTEN BY AI ##`

)