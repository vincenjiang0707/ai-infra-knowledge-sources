source: https://github.com/vllm-project/guidellm/pull/1101

# fix(metrics): exclude missing values from timed distributions - #1101

Open

[DivyamTalwar](https://github.com/DivyamTalwar)wants to merge 1 commit into

Open

[DivyamTalwar](https://github.com/DivyamTalwar) wants to merge 1 commit into

[DivyamTalwar](https://github.com/DivyamTalwar)wants to merge 1 commit into

## Conversation

Exclude optional values that do not apply from rate and concurrency distributions while preserving real zero observations. Generated-by: Codex GPT-5 Signed-off-by: Divyam Talwar <divyamtalwar0@gmail.com>

9 tasks

### This branch has not been deployed

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Keep optional metric values that do not apply out of rate and concurrency distributions. Mixed-modality benchmarks previously excluded

`None`

from the value distribution but recorded the same request as a zero-valued rate and concurrency event, which distorted reported medians and sample counts.The change filters missing values consistently before building value, per-second, and concurrency inputs while preserving real zero observations.

## Test Plan

`None`

/zero test fails because the rate median is`0.0`

instead of`4.0`

.`git diff --check`

pass.The full unit suite also passes:

`uv run tox -e test-unit`

reported 3,030 passed, 31 skipped, 163 expected failures, and one existing Pydantic warning. The focused tests use the real metric summary implementation.No linked issue or competing open/closed-unmerged PR was found; warmup accounting issue #1078 is a separate scope.

## AI Disclosure

This patch and its regression test were generated with Codex GPT-5 and have not yet been reviewed by a human. The commit includes

`Generated-by: Codex GPT-5`

and`Signed-off-by: Divyam Talwar <divyamtalwar0@gmail.com>`

.## git log

commit

58eb61aAuthor: Divyam Talwar divyamtalwar0@gmail.com

Date: Tue Sep 8 14:10:53 2026 +0530

Generated-by: Codex GPT-5

Signed-off-by: Divyam Talwar divyamtalwar0@gmail.com