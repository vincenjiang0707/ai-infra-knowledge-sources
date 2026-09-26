source: https://github.com/vllm-project/guidellm/pull/902

# Minor logging cleanup - #902

Merged

Merged

## Conversation

This mostly just makes sure we're not logging pre-formatted messages where we can use the logger's deferred formatting. There were several messages where I considered adding addional context; for now, I've resisted that temptation. Signed-off-by: David Butenhof <dbutenho@redhat.com>


[dbutenhof](https://github.com/dbutenhof)added the

[cleanup](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Acleanup)

Jul 6, 2026


**approved these changes**

[sjmonson](https://github.com/sjmonson)Jul 6, 2026

Contributor

|
Queued — the merge queue status continues in |

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

35 tasks

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Trivial logging cleanup I've meant to do for a while.

## Details

This just makes sure we're not logging pre-formatted messages where we can use the logger's deferred formatting.

There were several messages where I considered adding additional context; for now, I've resisted that temptation.

## Test Plan

`guidellm preprocess dataset`

and straightforward to verify manually.## Related Issues

N/A

## Use of AI

## git log

commit

24dbae3Author: David Butenhof dbutenho@redhat.com

Date: Mon Jul 6 13:49:01 2026 -0400

Signed-off-by: David Butenhof dbutenho@redhat.com