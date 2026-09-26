source: https://github.com/vllm-project/guidellm/pull/686

# Add a health check for the worker processes - #686

Merged

[jaredoconnell](https://github.com/jaredoconnell)merged 2 commits into

Merged

## Conversation

This is necessary because if this happens presently, it doesn't detect the failure, and continues waiting idefinitely for the process to be ready, causing a hang. Generated-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>


**previously approved these changes**

[sjmonson](https://github.com/sjmonson)Apr 4, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)
Collaborator


There was a problem hiding this comment.

Didn't test but looks fine. See minor nits below.

[src/guidellm/scheduler/worker_group.py](https://github.com/vllm-project/guidellm/pull/686/files/335f62f62c105d8e4d5051c86bf9fd36abd0d085#diff-d97e4fc87c1fc2179794b3e877ce25caee6e903da76a77650ac1c75915c521c8)Outdated

[src/guidellm/scheduler/worker_group.py](https://github.com/vllm-project/guidellm/pull/686/files/335f62f62c105d8e4d5051c86bf9fd36abd0d085#diff-d97e4fc87c1fc2179794b3e877ce25caee6e903da76a77650ac1c75915c521c8)

Signed-off-by: Jared O'Connell <joconnel@redhat.com>


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Apr 7, 2026

[src/guidellm/scheduler/worker_group.py](https://github.com/vllm-project/guidellm/pull/686/files/335f62f62c105d8e4d5051c86bf9fd36abd0d085#diff-d97e4fc87c1fc2179794b3e877ce25caee6e903da76a77650ac1c75915c521c8)

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Creates an Async IO task that polls for failure of the worker processes.

This is necessary because if this happens presently, it doesn't detect the failure, and continues waiting idefinitely for the process to be ready, causing a hang.

## Details

Here is what it looks like with a segmentation fault, which I've been getting.

In this situation, all of them had segmentation faults at the same time for some reason. The system reported a segmentation fault to me.

## Test Plan

## Use of AI

`## WRITTEN BY AI ##`

)