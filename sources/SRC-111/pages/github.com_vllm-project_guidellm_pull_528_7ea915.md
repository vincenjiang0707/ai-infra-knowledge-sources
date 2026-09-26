source: https://github.com/vllm-project/guidellm/pull/528

# Fix strategy initialization deadlock - #528

Merged

Merged

## Conversation

[sjmonson](https://github.com/sjmonson)requested review from

[jaredoconnell](https://github.com/jaredoconnell)and

[markurtz](https://github.com/markurtz)and removed request for

[jaredoconnell](https://github.com/jaredoconnell)

January 14, 2026 15:29

[sjmonson](https://github.com/sjmonson)marked this pull request as ready for review

January 14, 2026 16:04


**previously approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jan 14, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)
Collaborator


There was a problem hiding this comment.

Using an event looks to be an improvement to the design. I just have one comment.

[src/guidellm/scheduler/strategies.py](https://github.com/vllm-project/guidellm/pull/528/files#diff-16f91e4a5f33891c5078faa83ccd19a17e499ab0fe3730c14d374a62f041585b)Outdated

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/44293abdd0420de1b1636b9f60a8382cc1368955..e09430343cc72ada9b0e5dff92dc280edf52499e)the fix/req_start_delay branch from

[to](https://github.com/vllm-project/guidellm/commit/44293abdd0420de1b1636b9f60a8382cc1368955)

`44293ab`


`e094303`

[Compare](https://github.com/vllm-project/guidellm/compare/44293abdd0420de1b1636b9f60a8382cc1368955..e09430343cc72ada9b0e5dff92dc280edf52499e)

January 14, 2026 20:06

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/e09430343cc72ada9b0e5dff92dc280edf52499e..9c438210bc7160380c7d95e78e86439c90f01879)the fix/req_start_delay branch from

[to](https://github.com/vllm-project/guidellm/commit/e09430343cc72ada9b0e5dff92dc280edf52499e)

`e094303`


`9c43821`

[Compare](https://github.com/vllm-project/guidellm/compare/e09430343cc72ada9b0e5dff92dc280edf52499e..9c438210bc7160380c7d95e78e86439c90f01879)

January 14, 2026 20:07


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jan 14, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)
Collaborator


There was a problem hiding this comment.

Looks good to me. I tested it with a basic setup and checked the relevant timing values in the output.

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Fixed an issue where applying the initial start time to a

`Stratagy`

could results in a deadlock. Also ensure that the recorded benchmark`start_time`

is relative to the first request and not the scheduling start time.## Details

At the start of a benchmark the main thread will set the start time in shared memory. Each worker will also attempt to poll the start time. This behavior can cause transient deadlocks that prevent the benchmark from progressing to sending requests. Additionally the recorded "start_time" used for constraint calculations and stored as the benchmark start time was relative to the scheduler start time and not the first request time. This PR implements separate fixes for each issue.

## Test Plan

The following patch is needed to observe the issue however it can be very difficult to reproduce depending on the hardware:

The following test would reliably reproduce the issue in at least one concurrency level on H200 hardware:

Example in

`output.log`

where strategy sync hit issue:## Related Issues

## Use of AI

`## WRITTEN BY AI ##`

)