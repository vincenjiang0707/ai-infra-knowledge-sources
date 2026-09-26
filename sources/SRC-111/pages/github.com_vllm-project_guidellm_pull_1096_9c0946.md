source: https://github.com/vllm-project/guidellm/pull/1096

# fix: serialize audio translation filename - #1096

Merged

[mergify[bot]](https://github.com/mergify[bot])merged 1 commit into

Merged

[mergify[bot]](https://github.com/mergify[bot]) merged 1 commit into

[mergify[bot]](https://github.com/mergify[bot])merged 1 commit into

## Conversation

Assisted-by: Codex Signed-off-by: tangming1996 <ming.tang@daocloud.io>


**approved these changes**

[sjmonson](https://github.com/sjmonson)Sep 8, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)
Collaborator


There was a problem hiding this comment.

Yeah that seems like a mistake.

Contributor

|
Queued — the merge queue status continues in |


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Sep 9, 2026

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

35 tasks

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

Assisted-by: Codex

## Summary

The mock audio translation interface returns a 500 error at location: [server.py (line 277).

`"filename": {file.name}`

incorrectly constructs the filename as a set, which triggers a TypeError during JSON serialization. Valid upload requests will also fail.## Details

## Test Plan

## Related Issues

## Use of AI

## git log

commit

f9c107dAuthor: tangming1996 ming.tang@daocloud.io

Date: Mon Sep 7 16:32:48 2026 +0800

Signed-off-by: tangming1996 ming.tang@daocloud.io