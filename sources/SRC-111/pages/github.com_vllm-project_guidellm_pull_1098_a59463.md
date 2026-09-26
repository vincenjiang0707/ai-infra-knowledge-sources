source: https://github.com/vllm-project/guidellm/pull/1098

# Fix shared mutable fill values in argument parsing - #1098

Open

[tangming1996](https://github.com/tangming1996)wants to merge 1 commit into

Open

[tangming1996](https://github.com/tangming1996) wants to merge 1 commit into

[tangming1996](https://github.com/tangming1996)wants to merge 1 commit into

## Conversation

ArgStringParser evaluated the fill-value factory once during construction and reused that object for every sparse list position. With fill_value=list or dict, mutating one placeholder changed other positions and results from subsequent decodes using the same parser. Retain the factory and invoke it separately for every added list position. Keep a separate reference value for the existing overwrite checks. Add regression coverage for mutable list and dictionary fills, nested paths, repeated decode calls, and successive set calls. Assisted-by: Codex Signed-off-by: tangming1996 <ming.tang@daocloud.io>


**reviewed**

[sjmonson](https://github.com/sjmonson)Sep 8, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)
Collaborator


There was a problem hiding this comment.

I guess this is technically fixing a bug in the utility but it is impossible to hit this problem in the normal use of GuideLLM. Neither approving or disapproving for now.

### This branch has not been deployed

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

ArgStringParser evaluated the fill-value factory once during construction and reused that object for every sparse list position. With fill_value=list or dict, mutating one placeholder changed other positions and results from subsequent decodes using the same parser.

Retain the factory and invoke it separately for every added list position. Keep a separate reference value for the existing overwrite checks. Add regression coverage for mutable list and dictionary fills, nested paths, repeated decode calls, and successive set calls.

Assisted-by: Codex

## Summary

## Details

## Test Plan

## Related Issues

## Use of AI

## git log

commit

2153ab1Author: tangming1996 ming.tang@daocloud.io

Date: Mon Sep 7 17:17:02 2026 +0800

Assisted-by: Codex

Signed-off-by: tangming1996 ming.tang@daocloud.io