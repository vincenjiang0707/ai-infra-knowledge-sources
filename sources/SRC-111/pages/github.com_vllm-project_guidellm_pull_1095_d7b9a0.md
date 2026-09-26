source: https://github.com/vllm-project/guidellm/pull/1095

## Conversation

Generated-by: Codex Signed-off-by: xinjun.jiang <xinjun.jiang@daocloud.io>

[sjmonson](https://github.com/sjmonson)self-requested a review

September 8, 2026 17:32

[git-jxj](https://github.com/git-jxj)

[force-pushed](https://github.com/vllm-project/guidellm/compare/9ae118605ce2332a3c496a00c88e4e564e6fd4df..61fb74fcb372a701755ba6791bc309df3c7e6e2d)the fix/empty-data-worker branch from

[to](https://github.com/vllm-project/guidellm/commit/9ae118605ce2332a3c496a00c88e4e564e6fd4df)

`9ae1186`


`61fb74f`

[Compare](https://github.com/vllm-project/guidellm/compare/9ae118605ce2332a3c496a00c88e4e564e6fd4df..61fb74fcb372a701755ba6791bc309df3c7e6e2d)

September 9, 2026 06:50

### This branch has not been deployed

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Loading a one-row dataset with two workers fails when samples are not precached. The worker assigned no rows incorrectly reports that the dataset produced no usable results because the check counts rows assigned to other workers.

## Details

Count rows actually processed by the current worker when checking for empty results. Empty shards can finish normally, while workers whose rows produce no usable results still report an error.

Add real HuggingFace Dataset and PyTorch multiprocessing coverage for cached and uncached loading with zero, one, and two workers, plus a regression retaining empty-result validation.

## Test Plan

## Related Issues

None.

## Use of AI

## git log

commit

61fb74fAuthor: xinjun.jiang xinjun.jiang@daocloud.io

Date: Sat Sep 5 21:06:31 2026 +0800

Generated-by: Codex

Signed-off-by: xinjun.jiang xinjun.jiang@daocloud.io