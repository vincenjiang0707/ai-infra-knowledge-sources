source: https://github.com/vllm-project/guidellm/pull/990

# Fix multipart filenames for audio uploads - #990

Merged

[mergify[bot]](https://github.com/mergify[bot])merged 1 commit into

Merged

## Conversation

Signed-off-by: Fedir Zadniprovskyi <github.g1k56@simplelogin.com>

Contributor

|
Hi |

[fedirz](https://github.com/fedirz)

[force-pushed](https://github.com/vllm-project/guidellm/compare/80b3cc3725fcac9df68b372247d0fd25c094536a..7efdd8b65e53fdf5823cf4170696320665f1d507)the fix/983-audio-upload-filename branch from

[to](https://github.com/vllm-project/guidellm/commit/80b3cc3725fcac9df68b372247d0fd25c094536a)

`80b3cc3`


`7efdd8b`

[Compare](https://github.com/vllm-project/guidellm/compare/80b3cc3725fcac9df68b372247d0fd25c094536a..7efdd8b65e53fdf5823cf4170696320665f1d507)

August 3, 2026 17:43


**approved these changes**

[sjmonson](https://github.com/sjmonson)Aug 6, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)
Collaborator


There was a problem hiding this comment.

Sorry for the delay. I confirmed that this fixes datasets without filenames.

Collaborator

|
|

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

This was referenced Aug 6, 2026

[cmiyai](https://github.com/cmiyai)pushed a commit to cmiyai/guidellm that referenced this pull request

Aug 14, 2026

## Summary - honor explicit audio filenames before path-derived names - derive in-memory filenames from the resolved audio format - defensively provide a nonempty multipart filename in the audio request handler ## Testing - uv run tox -e tests -- targeted filename regression tests (5 passed) - uv run tox -e lint-check - uv run tox -e type-check The complete audio utility file was also attempted locally; 250 tests passed and 18 audio codec tests failed because TorchCodec could not load local FFmpeg dylibs. The new metadata-only regressions mock the codec boundary and pass. Fixes[vllm-project#983]--- # git log commit[Author: Fedir Zadniprovskyi <github.g1k56@simplelogin.com> Date: Mon Aug 3 10:42:54 2026 -0700 fix: ensure audio uploads include filenames Signed-off-by: Fedir Zadniprovskyi <github.g1k56@simplelogin.com> --------- Signed-off-by: Fedir Zadniprovskyi <github.g1k56@simplelogin.com>]7efdd8b

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

## Testing

The complete audio utility file was also attempted locally; 250 tests passed and 18 audio codec tests failed because TorchCodec could not load local FFmpeg dylibs. The new metadata-only regressions mock the codec boundary and pass.

Fixes #983

## git log

commit

7efdd8bAuthor: Fedir Zadniprovskyi github.g1k56@simplelogin.com

Date: Mon Aug 3 10:42:54 2026 -0700

Signed-off-by: Fedir Zadniprovskyi github.g1k56@simplelogin.com