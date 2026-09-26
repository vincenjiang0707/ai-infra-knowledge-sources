source: https://github.com/vllm-project/guidellm/pull/1088

# Fix inconsistent dataset split resolving - #1088

Merged

Merged

## Conversation

If a dataset has multiple splits (train, test, etc) the dataset object is of type DatasetDict or IterableDatasetDict. Each deserializer handled split datasets differently, file based handlers would automatically detect a split dataset and atempt to determine the default split. Other deserializers would pass the dataset as-is and fail later when iteration was attempted. To solve this issue, the DatasetDeserializerFactory now uses the resolve_dataset_split function on all deserialized datasets. A user can still manually select a split using load args. Signed-off-by: Samuel Monson <smonson@redhat.com>


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Sep 4, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)
Collaborator


There was a problem hiding this comment.

Looks good. Tested with a basic dataset.

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

Thought we fixed this at some point but apparently not.

## Details

If a dataset has multiple splits (train, test, etc) the dataset object is of type DatasetDict or IterableDatasetDict. Each deserializer handled split datasets differently, file based handlers would automatically detect a split dataset and atempt to determine the default split. Other deserializers would pass the dataset as-is and fail later when iteration was attempted.

To solve this issue, the DatasetDeserializerFactory now uses the resolve_dataset_split function on all deserialized datasets. A user can still manually select a split using load args.

## Test Plan

Run with any dataset which is split. Pretty much any huggingface loaded dataset will do.

## Use of AI

## git log

commit

c5c14d7Author: Samuel Monson smonson@redhat.com

Date: Fri Sep 4 14:24:04 2026 -0400

Signed-off-by: Samuel Monson smonson@redhat.com