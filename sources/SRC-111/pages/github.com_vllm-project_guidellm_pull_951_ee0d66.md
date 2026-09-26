source: https://github.com/vllm-project/guidellm/pull/951

# Add py.typed marker for PEP 561 compliance - #951

Merged

Merged

## Conversation

Signed-off-by: arijitroy003 <arijitroy003@gmail.com>

Collaborator

|
This is interesting -- I'd never heard of this protocol before, but it appears to be legit. On the other hand, our quality-checks run seems hung -- no indication there's any relationship to the change, and it's probably just GitHub... 🤔 |


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jul 27, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

Seems like a real thing; although I'm not sure what if anything actually depends on it, since it doesn't appear to affect our existing ruff lint/type checks.

Contributor

|
Queued — the merge queue status continues in |


**approved these changes**

[sjmonson](https://github.com/sjmonson)Jul 27, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)
Collaborator


There was a problem hiding this comment.

Thanks this was on my TODO list

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

35 tasks

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Adds a py.typed marker file to enable type checkers to use the inline type hints already present in the package.

## Changes

`py.typed`

marker file in`src/guidellm/`

`pyproject.toml`

to include`py.typed`

in package data## Testing

Verified by checking:

`src/guidellm/py.typed`

)## git log

commit

99d0de3Author: arijitroy003 arijitroy003@gmail.com

Date: Thu Jul 23 20:30:00 2026 +0530

Signed-off-by: arijitroy003 arijitroy003@gmail.com