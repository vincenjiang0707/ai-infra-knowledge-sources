source: https://github.com/vllm-project/guidellm/pull/530

# Use total requests for throughput calculation - #530

Merged

Merged

## Conversation

Signed-off-by: Samuel Monson <smonson@redhat.com>

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/184df17d8d61032f06fdc6152d9075ba8132b182..aaacf4b624a04fda1385f8f94675d21bdd3a0f74)the fix/console_total_throughput branch from

[to](https://github.com/vllm-project/guidellm/commit/184df17d8d61032f06fdc6152d9075ba8132b182)

`184df17`


`aaacf4b`

[Compare](https://github.com/vllm-project/guidellm/compare/184df17d8d61032f06fdc6152d9075ba8132b182..aaacf4b624a04fda1385f8f94675d21bdd3a0f74)

January 16, 2026 15:49


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jan 16, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)
Collaborator


There was a problem hiding this comment.

The only reason this would not be okay is if it was misleading, but the title doesn't seem misleading, so I'm approving.

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Switches "Server Throughput Statistics" table in console output to use total request pool rather then just successful. See #529 for reasoning.

## Related Issues

## Use of AI

`## WRITTEN BY AI ##`

)