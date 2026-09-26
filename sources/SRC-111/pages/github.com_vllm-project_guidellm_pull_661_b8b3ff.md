source: https://github.com/vllm-project/guidellm/pull/661

# Support removing keys from HTTP request bodies - #661

Merged

Merged

## Conversation

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/ff32abd2760e5054fcd8867dc40d979c9a9e7c69..a18bf00f08b00e5f2a1d970ad59c88990f485941)the feat/key_deletion branch from

[to](https://github.com/vllm-project/guidellm/commit/ff32abd2760e5054fcd8867dc40d979c9a9e7c69)

`ff32abd`


`a18bf00`

[Compare](https://github.com/vllm-project/guidellm/compare/ff32abd2760e5054fcd8867dc40d979c9a9e7c69..a18bf00f08b00e5f2a1d970ad59c88990f485941)

March 26, 2026 21:17


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Mar 27, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)
Collaborator


There was a problem hiding this comment.

I like how minimal of a change this ended up being to the backend itself.

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Add the ability to omit keys from the request body by setting them to

`null`

in`--backend-kwargs`

.## Details

This PR makes it so any value in the request body that is

`None`

will be omitted from the body before being sent.## Test Plan

`--backend-kwargs '{"extras":"body":{"stream_options":{"continuous_usage_stats": None}}}'`

## Related Issues

## Use of AI

`## WRITTEN BY AI ##`

)