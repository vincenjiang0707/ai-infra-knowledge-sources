source: https://github.com/vllm-project/guidellm/pull/549

# Added rampup to constant rate type - #549

Merged

[jaredoconnell](https://github.com/jaredoconnell)merged 2 commits into

Merged

## Conversation

7 tasks

Generated-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/d895b07aa307e9de1b286b9e4eb7e73d46cc7f10..eb6a8036ee35daf06b57c80a1d284f048013c8aa)the feature/constant-rampup branch from

[to](https://github.com/vllm-project/guidellm/commit/d895b07aa307e9de1b286b9e4eb7e73d46cc7f10)

`d895b07`


`eb6a803`

[Compare](https://github.com/vllm-project/guidellm/compare/d895b07aa307e9de1b286b9e4eb7e73d46cc7f10..eb6a8036ee35daf06b57c80a1d284f048013c8aa)

January 23, 2026 18:10

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Simply allows a linear rampup of the constant rate profile.

## Test Plan

The simplest test is to run a short constant test with 4 requests per second, with a long rampup. You can see how it ramps as expected.

There are also new tests.

## Related Issues

Fulfills part of the goals of #428

## Use of AI

`## WRITTEN BY AI ##`

)