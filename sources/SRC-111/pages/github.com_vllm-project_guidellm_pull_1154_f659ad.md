source: https://github.com/vllm-project/guidellm/pull/1154

# Increase timeout for integration test - #1154

Merged

[mergify[bot]](https://github.com/mergify[bot])merged 1 commit into

Merged

## Conversation

Generated-by: Cursor AI Grok 4.6 Signed-off-by: Jared O'Connell <joconnel@redhat.com>


**approved these changes**

[sjmonson](https://github.com/sjmonson)Sep 16, 2026


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Sep 16, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

60 is long: but I guess if GitHub hangs up our runners, waiting long is better than failing.

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

This test takes 2.5 seconds locally, but only has a 10 second timeout. That's fine normally, but not on CI, where it's much slower and sometimes takes over 10 seconds.

It's bumped up to 60 seconds, which is standard in our integration test suite.

## Test Plan

Make sure it passes CI.

## Use of AI

## git log

commit

1ad23a5Author: Jared O'Connell joconnel@redhat.com

Date: Wed Sep 16 16:16:29 2026 -0400

Generated-by: Cursor AI Grok 4.6

Signed-off-by: Jared O'Connell joconnel@redhat.com