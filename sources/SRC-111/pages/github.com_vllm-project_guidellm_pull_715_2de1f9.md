source: https://github.com/vllm-project/guidellm/pull/715

# Refactor CSV tests - #715

Merged

[jaredoconnell](https://github.com/jaredoconnell)merged 2 commits into

Merged

## Conversation


**previously approved these changes**

[dbutenhof](https://github.com/dbutenhof)May 4, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

I like the cleaner set of test cases...

[tests/unit/benchmark/test_csv_output.py](https://github.com/vllm-project/guidellm/pull/715/files#diff-1c82d9a660db56079f70f20dd138a66d46507c19b669ddd5d9e0b8cfde575c19)Outdated


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)May 5, 2026

It now isolates specific functionality better, and covers more edge cases. Assisted-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>

[jaredoconnell](https://github.com/jaredoconnell)

[force-pushed](https://github.com/vllm-project/guidellm/compare/a0ad0c1281dd20f2b77cd39c7508d9e6884a2e44..b8dc13fa7c229857cf1ec70e6c787e1789cfc420)the refactor/csv-improvements branch from

[to](https://github.com/vllm-project/guidellm/commit/a0ad0c1281dd20f2b77cd39c7508d9e6884a2e44)

`a0ad0c1`


`b8dc13f`

[Compare](https://github.com/vllm-project/guidellm/compare/a0ad0c1281dd20f2b77cd39c7508d9e6884a2e44..b8dc13fa7c229857cf1ec70e6c787e1789cfc420)

May 5, 2026 20:21

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

It now isolates specific functionality better, and covers more edge cases.

## Details

`_align_columns`

, which can be more easily tested in isolation.## Test Plan

## Use of AI

`## WRITTEN BY AI ##`

)