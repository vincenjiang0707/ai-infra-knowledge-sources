source: https://github.com/vllm-project/guidellm/pull/679

# Identify action versions - #679

Merged

Merged

## Conversation

dependable reads and updates commented version strings on SHA dependencies, making it a bit easier to review proposed changes. Note that it's updates are not 100% reliable, and sometimes it proposes SHA updates for unreleased commits, so we need to be vigilant. Also updating the neural magic actions, which apparently aren't released separately -- the original SHA was an action commit that wasn't the latest commit in the release, so I updated it. Signed-off-by: David Butenhof <dbutenho@redhat.com>


[dbutenhof](https://github.com/dbutenhof)added

[dependencies](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Adependencies)

[build](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Abuild)

Apr 1, 2026

Signed-off-by: David Butenhof <dbutenho@redhat.com>


**approved these changes**

[markurtz](https://github.com/markurtz)Apr 1, 2026


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Apr 1, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)
Collaborator


There was a problem hiding this comment.

This is helpful. Is the automation updated to ensure this is maintained?

Collaborator
Author

The dependabot documentation claims that it'll automatically recognize and update the version comments. Although several sources also claim that it sometimes forgets, just as it sometimes updates to SHAs that don't represent releases. Although locking to the SHA is still "best practice", we'll have to keep an eye on it. |


[dbutenhof](https://github.com/dbutenhof)added the

[cleanup](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Acleanup)

Apr 7, 2026

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Update workflow action dependencies to include commented versions to help review.

## Details

dependabot reads and updates commented version strings on SHA dependencies, making it a bit easier to review proposed changes. Note that its updates are not 100% reliable, and sometimes it proposes SHA updates for unreleased commits, so we need to be vigilant.

Also updating the neural magic actions, which apparently aren't released separately -- the original SHA was an action commit that wasn't the latest commit in the release, so I updated it.

## Test Plan

## Related Issues

## Use of AI

`## WRITTEN BY AI ##`

)