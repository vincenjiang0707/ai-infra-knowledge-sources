source: https://github.com/vllm-project/guidellm/pull/612

# Fix JSON serialization for binary request payloads via base64 bytes config - #612

Merged

[sjmonson](https://github.com/sjmonson)merged 1 commit into

## Conversation

Signed-off-by: Uri Shaket <ushaket@redhat.com>


**approved these changes**

[sjmonson](https://github.com/sjmonson)Feb 25, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)
Collaborator


There was a problem hiding this comment.

LGTM. Before merge can you verify that `guidellm benchmark from-file --output-formats console ./benchmarks.json`

works on an audio benchmark with this patch?

Contributor
Author

|

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

This PR fixes a serialization failure when request arguments include binary data (for example, audio bytes in multipart file payloads).

It configures Pydantic JSON byte handling to use base64 encoding so

`model_dump_json()`

no longer raises`PydanticSerializationError`

on non-UTF8 bytes.## Details

`ser_json_bytes="base64"`

`val_json_bytes="base64"`

`ReloadableBaseModel`

`StandardBaseModel`

`StandardBaseDict`

`GenerationRequestArguments(... files={"file": ("a.wav", b"...", "audio/wav")}).model_dump_json()`

## Test Plan

`uv run --no-sync python - <<'PY'`

`GenerationRequestArguments`

with non-UTF8 bytes in`files`

`model_dump_json()`

`AudioRequestHandler`

`audio_column`

`compile_streaming(...)`

## Related Issues

## Use of AI

`## WRITTEN BY AI ##`

)