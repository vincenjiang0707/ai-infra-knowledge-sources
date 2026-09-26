source: https://github.com/vllm-project/guidellm/pull/659

# Check if deserialization path is vaild safely - #659

Merged

Merged

## Conversation


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Mar 26, 2026


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Mar 26, 2026

Signed-off-by: Samuel Monson <smonson@redhat.com>

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/6e4f198fca7eb13f70a6e69dc33f7f2c3ceb1296..0d9cdfcae2013427c083572bcc211b78d968dc1b)the fix/file_deserialization branch from

[to](https://github.com/vllm-project/guidellm/commit/6e4f198fca7eb13f70a6e69dc33f7f2c3ceb1296)

`6e4f198`


`0d9cdfc`

[Compare](https://github.com/vllm-project/guidellm/compare/6e4f198fca7eb13f70a6e69dc33f7f2c3ceb1296..0d9cdfcae2013427c083572bcc211b78d968dc1b)

March 26, 2026 19:52

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Adds a check to avoid errors later in the config file deserialization code.

## Details

Deserialization will fail if the

`--data`

string is too long since we first check if the string is a path name to a config file. Fixed by adding a test at the beginning of the function which errors safely if the path is an invalid format. Note this is a temporary fix because we plan to rework this code in v0.7.0.## Related Issues

`--data`

string leads to deserialization failures #658## Use of AI

`## WRITTEN BY AI ##`

)