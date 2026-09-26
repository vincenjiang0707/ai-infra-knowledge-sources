source: https://github.com/vllm-project/guidellm/pull/981

# Fix non-streaming audio response parsing - #981

Merged

[mergify[bot]](https://github.com/mergify[bot])merged 1 commit into

Merged

## Conversation

Contributor

|
Hi |

Signed-off-by: Fedir Zadniprovskyi <github.g1k56@simplelogin.com>

[fedirz](https://github.com/fedirz)

[force-pushed](https://github.com/vllm-project/guidellm/compare/96a8e6c65f2070ce8af8e918547a465772487141..5dc5dac905a7948420bf4a223bf4722fdc6da660)the fix/audio-non-streaming-response branch from

[to](https://github.com/vllm-project/guidellm/commit/96a8e6c65f2070ce8af8e918547a465772487141)

`96a8e6c`


`5dc5dac`

[Compare](https://github.com/vllm-project/guidellm/compare/96a8e6c65f2070ce8af8e918547a465772487141..5dc5dac905a7948420bf4a223bf4722fdc6da660)

August 3, 2026 01:12


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

Confirmed this fixes non-streaming.

Contributor

|
Queued — the merge queue status continues in |

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

35 tasks

[cmiyai](https://github.com/cmiyai)pushed a commit to cmiyai/guidellm that referenced this pull request

Aug 14, 2026

## Summary - parse top-level text from non-streaming transcription and translation responses - preserve audio usage metrics and response IDs - accept explicit empty transcriptions while rejecting responses that omit text - add regression coverage for basic, verbose, empty, missing, and usage-bearing responses ## Testing - tox -e tests -- tests/unit/backends/openai/test_request_handlers.py -k TestAudioRequestHandler - tox -e lint-check - tox -e type-check -- src/guidellm/backends/openai/request_handlers.py Closes[vllm-project#980]--- # git log commit[Author: Fedir Zadniprovskyi <github.g1k56@simplelogin.com> Date: Sun Aug 2 18:08:11 2026 -0700 fix: parse non-streaming audio responses Signed-off-by: Fedir Zadniprovskyi <github.g1k56@simplelogin.com> --------- Signed-off-by: Fedir Zadniprovskyi <github.g1k56@simplelogin.com>]5dc5dac

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

## Testing

Closes #980

## git log

commit

5dc5dacAuthor: Fedir Zadniprovskyi github.g1k56@simplelogin.com

Date: Sun Aug 2 18:08:11 2026 -0700

Signed-off-by: Fedir Zadniprovskyi github.g1k56@simplelogin.com