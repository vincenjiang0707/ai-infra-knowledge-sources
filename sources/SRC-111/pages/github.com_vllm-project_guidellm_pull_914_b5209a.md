source: https://github.com/vllm-project/guidellm/pull/914

# Disable redundant auto-refresh in console progress components - #914

Merged

[mergify[bot]](https://github.com/mergify[bot])merged 1 commit into

Merged

[mergify[bot]](https://github.com/mergify[bot]) merged 1 commit into

[mergify[bot]](https://github.com/mergify[bot])merged 1 commit into

## Conversation

Explicitly set auto_refresh=False on the internal progress instances to avoid unnecessary screen updates, as the parent Live object already manages the refresh at the configured rate. Signed-off-by: wuheng <wuheng@kylinos.cn>


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jul 9, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

Interesting. This appears work just fine.

Contributor

|
Queued — the merge queue status continues in |


[dbutenhof](https://github.com/dbutenhof)added

[bug](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Abug)

[cli](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Acli)

Jul 9, 2026


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jul 9, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)
Collaborator


There was a problem hiding this comment.

I tested it and both main and this branch appear to be refreshing at around 4 hz on my laptop. But this doesn't break anything, so I'll approve.

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

35 tasks

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Explicitly set auto_refresh=False on the internal progress instances to avoid unnecessary screen updates, as the parent Live object already manages the refresh at the configured rate.

## Details

The base

`Live`

class (from Rich) is initialized with`auto_refresh=True`

and`refresh_per_second=4`

in the constructor of`GenerativeConsoleBenchmarkerProgress`

.However, the child progress components (

`self.run_progress`

and`_GenerativeProgressTasks`

) also enable`auto_refresh`

by default when they are created, leading to redundant refresh triggers.This results in more frequent redraws than intended.

## Test Plan

## Related Issues

`guidellm run`

#913## Use of AI

## git log

commit

4d73733Author: wuheng_ky wuheng@kylinos.cn

Date: Wed Jul 8 13:57:11 2026 +0800

Signed-off-by: wuheng wuheng@kylinos.cn