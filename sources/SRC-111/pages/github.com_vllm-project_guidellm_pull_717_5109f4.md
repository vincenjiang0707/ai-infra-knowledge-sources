source: https://github.com/vllm-project/guidellm/pull/717

# Refactor CLI into nested structure - #717

Merged

Merged

## Conversation


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)May 5, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

It's hard to review this sort of refactoring without simply trusting that it's mostly a cut-and-paste; but that appears to be essentially the case, (and so I've avoided making some random commentary along the way that would equally apply to the current code) ... so I've really just got one minor comment comment...

[src/guidellm/__main__.py](https://github.com/vllm-project/guidellm/pull/717/files#diff-62e0a62289c938a74b026dbce7a0f95f26893e0aa9feedb81349e658db8af7bf)Outdated

Signed-off-by: Samuel Monson <smonson@redhat.com>

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/9237c13d0a9f444b25b1549a64da7334c8082a0b..4d947e682de5684577555b7077b0087ed7a8eac4)the cleanup/cli_nested branch from

[to](https://github.com/vllm-project/guidellm/commit/9237c13d0a9f444b25b1549a64da7334c8082a0b)

`9237c13`


`4d947e6`

[Compare](https://github.com/vllm-project/guidellm/compare/9237c13d0a9f444b25b1549a64da7334c8082a0b..4d947e682de5684577555b7077b0087ed7a8eac4)

May 6, 2026 15:39

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/4d947e682de5684577555b7077b0087ed7a8eac4..2fa9cca6825110e1fbe18b6bd6cf6cf44e0c9c28)the cleanup/cli_nested branch from

[to](https://github.com/vllm-project/guidellm/commit/4d947e682de5684577555b7077b0087ed7a8eac4)

`4d947e6`


`2fa9cca`

[Compare](https://github.com/vllm-project/guidellm/compare/4d947e682de5684577555b7077b0087ed7a8eac4..2fa9cca6825110e1fbe18b6bd6cf6cf44e0c9c28)

May 6, 2026 15:40


**previously approved these changes**

[dbutenhof](https://github.com/dbutenhof)May 6, 2026

Signed-off-by: Samuel Monson <smonson@redhat.com>

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/da054fbdb6c20c13393ff07d2c824c27e1c68c45..5dff887a1c2be9ec26e220bff3ea1dbcd2608c50)the cleanup/cli_nested branch from

[to](https://github.com/vllm-project/guidellm/commit/da054fbdb6c20c13393ff07d2c824c27e1c68c45)

`da054fb`


`5dff887`

[Compare](https://github.com/vllm-project/guidellm/compare/da054fbdb6c20c13393ff07d2c824c27e1c68c45..5dff887a1c2be9ec26e220bff3ea1dbcd2608c50)

May 6, 2026 15:58


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)May 6, 2026

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Migrates CLI code out of

`__main__.py`

and into its own submodule.## Details

The PR is purely refactoring. Making this change now will make the incoming CLI refactor a little cleaner to review.

## Test Plan

Run any existing CLI commands to confirm functionality.

## Use of AI

`## WRITTEN BY AI ##`

)