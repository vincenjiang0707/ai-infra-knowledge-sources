source: https://github.com/vllm-project/guidellm/pull/525

# Make image_url/video_url send dictionaries - #525

Merged

Merged

## Conversation

Both vLLM and the OpenAI spec expect message content of type `image_url` to be a dictionary like `{"url": <url>}`, though the previous behaviour sent the url as a plain string. `video_url` is vLLM-only as far as I know though it follows the same schema. Signed-off-by: Vincent Brouwers <vincentbrouwers9@gmail.com>

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

This PR changes how GuideLLM sends image/video urls to the backend using the chat_completions endpoint. The current behaviour doesn't seem to follow spec, which was giving me trouble benchmarking a multimodal dataset.

Both vLLM and the OpenAI spec expect message content of type

`image_url`

to be a dictionary like`{"url": <url>}`

, though the previous behaviour sent the url as a plain string.`video_url`

is vLLM-only as far as I know though it follows the same schema.## Details

## Test Plan

## Related Issues

## Use of AI

`## WRITTEN BY AI ##`

)