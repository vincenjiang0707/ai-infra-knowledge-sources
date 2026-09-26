source: https://github.com/vllm-project/guidellm/pull/625

# Run format job in CI - #625

Merged

Merged

## Conversation


**reviewed**

[dbutenhof](https://github.com/dbutenhof)Mar 6, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

While re-using the precommit hook is convenient... since we're not trying to commit the Action workspace changes into the repo, can we just use `ruff format --check`

here?

[.github/workflows/quality.yml](https://github.com/vllm-project/guidellm/pull/625/files#diff-b31f1e5654d027d84c24cdba2ff31ab79e3ea617091ed348a97476a27b076078)Outdated


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Mar 12, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

Granted, the objection was weak 😁 ... in any case, I prefer this approach.

[sjmonson](https://github.com/sjmonson)marked this pull request as ready for review

March 13, 2026 17:36

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Adds formatting check to CI jobs and runs formatting against all files to ensure CI passes.

## Related Issues

## Use of AI

`## WRITTEN BY AI ##`

)