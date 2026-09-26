source: https://github.com/vllm-project/guidellm/pull/908

# Move tox runner setting back into tests env - #908

Merged

Merged

## Conversation

Last minute I moved this out of the tests env and into a section for the base runner class but apparently that doesn't work. Signed-off-by: Samuel Monson <smonson@redhat.com>


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jul 7, 2026

Contributor

|
Queued — the merge queue status continues in |


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jul 7, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

Ah ... I looked at this when you posted it, figured I'd wait for the CI to test it, and then forgot about it. Looks good.

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

35 tasks

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Last minute I moved this out of the tests env and into a section for the base runner class but apparently that doesn't work.

## Use of AI

## git log

commit

8716892Author: Samuel Monson smonson@redhat.com

Date: Tue Jul 7 13:08:34 2026 -0400

Signed-off-by: Samuel Monson smonson@redhat.com