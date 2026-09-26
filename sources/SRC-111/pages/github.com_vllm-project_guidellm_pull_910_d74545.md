source: https://github.com/vllm-project/guidellm/pull/910

# Allow TODO and HACK comments - #910

Merged

Merged

## Conversation

Signed-off-by: Samuel Monson <smonson@redhat.com>


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

Luckily I haven't had occasion to run into these, but I approve of the change!

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

This rule has driven me crazy since the moment we added it. Disallowing

`TODO`

means there is no common way to indicate planned but incomplete sections of code. Even with the rule disallowing these comments sometimes still happen but end up being marked as`NOTE`

or unmarked.This PR also drops the restriction on

`HACK`

with the idea that`HACK`

can be used for temporary workarounds. It leaves the restrictions on`FIXME`

and`XXX`

so a contributor can use them to remind themselves of in-progress pieces in a way that is caught by CI.## Use of AI

## git log

commit

7ee7c2dAuthor: Samuel Monson smonson@redhat.com

Date: Tue Jul 7 13:34:21 2026 -0400

Signed-off-by: Samuel Monson smonson@redhat.com