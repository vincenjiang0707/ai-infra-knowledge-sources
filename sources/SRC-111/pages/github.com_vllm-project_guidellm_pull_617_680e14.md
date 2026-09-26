source: https://github.com/vllm-project/guidellm/pull/617

# Drop median from throughput metrics in console - #617

Merged

Merged

## Conversation

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/91f9deb80316a06112d3093e22484b976711783b..9c7dba87649e36b1fb84b681a6f6ff1cff7169b5)the fix/throughput_median_console branch from

[to](https://github.com/vllm-project/guidellm/commit/91f9deb80316a06112d3093e22484b976711783b)

`91f9deb`


`9c7dba8`

[Compare](https://github.com/vllm-project/guidellm/compare/91f9deb80316a06112d3093e22484b976711783b..9c7dba87649e36b1fb84b681a6f6ff1cff7169b5)

March 2, 2026 19:42


[sjmonson](https://github.com/sjmonson)changed the title

Mar 2, 2026

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/9c7dba87649e36b1fb84b681a6f6ff1cff7169b5..624274cda4256968201aed3edf8a8b5ffd830ecb)the fix/throughput_median_console branch from

[to](https://github.com/vllm-project/guidellm/commit/9c7dba87649e36b1fb84b681a6f6ff1cff7169b5)

`9c7dba8`


`624274c`

[Compare](https://github.com/vllm-project/guidellm/compare/9c7dba87649e36b1fb84b681a6f6ff1cff7169b5..624274cda4256968201aed3edf8a8b5ffd830ecb)

March 2, 2026 20:20


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Mar 2, 2026

[src/guidellm/benchmark/outputs/console.py](https://github.com/vllm-project/guidellm/pull/617/files/624274cda4256968201aed3edf8a8b5ffd830ecb#diff-f321b63a8b5258670d851eda893190e71d8f7366f4371ce7be43c1a2ccef1bf0)


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Mar 2, 2026

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Only show mean for request/token based concurrences. See #602 for reasoning.

## Details

Result of change:

## Related Issues

## Use of AI

`## WRITTEN BY AI ##`

)