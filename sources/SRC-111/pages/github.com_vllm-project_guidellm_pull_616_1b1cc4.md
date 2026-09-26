source: https://github.com/vllm-project/guidellm/pull/616

# Add data parameter to benchmark command in README - #616

Merged

Merged

## Conversation

Signed-off-by: Matej Sirovatka <54212263+S1ro1@users.noreply.github.com>


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Mar 2, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

Thanks for catching a documentation error -- it'd be ideal if each of the examples were executable in isolation, but there's currently no automated process to ensure that.


**requested changes**

[dbutenhof](https://github.com/dbutenhof)Mar 3, 2026

Signed-off-by: Matej Sirovatka <54212263+S1ro1@users.noreply.github.com>

Contributor
Author

|
Updated the wording, feel free to directly push wording changes if needed |


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Mar 3, 2026


**approved these changes**

[sjmonson](https://github.com/sjmonson)Mar 4, 2026

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

A very tiny PR, example in the README would fail with

`ValueError: Data must be a non-empty list, got []`

and was also missing a backslash.