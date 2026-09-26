source: https://github.com/vllm-project/guidellm/pull/632

# Drop RC jobs and nightly PyPi publish - #632

Merged

Merged

## Conversation

Collaborator
Author

|
|

Contributor

## ✅ Branch has been successfully rebased |

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/76d835d43e2cc75057ceaae60d54cb17c9f49e77..cd1538a6634dbfc0e71b0daa730dcd61cdafb19c)the ci/drop_rc branch 2 times, most recently from

[to](https://github.com/vllm-project/guidellm/commit/76d835d43e2cc75057ceaae60d54cb17c9f49e77)

`76d835d`


`cd1538a`

[Compare](https://github.com/vllm-project/guidellm/compare/76d835d43e2cc75057ceaae60d54cb17c9f49e77..cd1538a6634dbfc0e71b0daa730dcd61cdafb19c)

March 17, 2026 21:57

[sjmonson](https://github.com/sjmonson)marked this pull request as ready for review

March 17, 2026 21:57


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Mar 18, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

Yeah, OK: I'm good with that -- the idea of flooding PyPi with nightly builds actually seems a bit silly. RC is perhaps more debatable, if we used the concept consistently and meaningfully, but I don't have a problem with dropping it.

Collaborator

|
|

Contributor

## ❌ Unable to rebase: Mergify can't impersonate
|

Collaborator

|
|

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

Contributor

## ✅ Branch has been successfully rebased |

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Our current development workflow does not involve RC branches so drop the CI automation. The nightly PyPi builds have been failing for some time due to an issue with z-stream tags. Users can just pip install from git if they need latest or use the nightly container image.

## Related Issues

## Use of AI

`## WRITTEN BY AI ##`

)