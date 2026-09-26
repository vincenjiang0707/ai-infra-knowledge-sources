source: https://github.com/vllm-project/guidellm/pull/541

# Add Mistral tokenizer as optional dependency - #541

Merged

Merged

## Conversation

Signed-off-by: Samuel Monson <smonson@redhat.com>


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Jan 22, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

Looks "correct" ... but with some compatibility concerns:

What's the risk here of breaking users who had an explicit `guidellm[openai]`

dependency? It does seem this is a reasonable change since the group apparently wasn't really "openai-specific" anyway; but if it's a breaking change for common use cases, maybe the rename should be deferred to 6.0 or later?

Also, are the extras defined in documentation that would need to be updated?

Collaborator
Author

|
We direct most users to use the |


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jan 22, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)
Collaborator


There was a problem hiding this comment.

The `tokenizers`

name seems less abstract and an improvement over `openai`

.

4 tasks

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Adds a library required to load Mistral models to the

`openai`

extras group. Also renames the group to`tokenizers`

to be more generic.## Related Issues

## Use of AI

`## WRITTEN BY AI ##`

)