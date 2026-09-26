source: https://github.com/vllm-project/guidellm/pull/561

# fix(cli): validate --output-path against --output-dir - #561

Merged

Merged

## Conversation


**approved these changes**

[sjmonson](https://github.com/sjmonson)Jan 28, 2026

Signed-off-by: michelia <michelia@seal.io>

[aiwantaozi](https://github.com/aiwantaozi)

[force-pushed](https://github.com/vllm-project/guidellm/compare/dd7dff9089108e56d412e022867fe37e319a2024..75b53c094a6161a78d4bd4bc7b36fd8a25947940)the fix/output-dir branch from

[to](https://github.com/vllm-project/guidellm/commit/dd7dff9089108e56d412e022867fe37e319a2024)

`dd7dff9`


`75b53c0`

[Compare](https://github.com/vllm-project/guidellm/compare/dd7dff9089108e56d412e022867fe37e319a2024..75b53c094a6161a78d4bd4bc7b36fd8a25947940)

January 29, 2026 04:10


**approved these changes**

[sjmonson](https://github.com/sjmonson)Jan 29, 2026

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Fix CLI validation so

`--output-path`

correctly conflicts with`--output-dir`

, not the mistyped`outputs_dir`

.## Details

`--output-path`

and`--output-dir`

## Test Plan

## Related Issues

## Use of AI