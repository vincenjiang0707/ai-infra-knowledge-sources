source: https://github.com/vllm-project/guidellm/pull/1100

# fix(benchmark): clear rejected reservoir request data - #1100

Open

[DivyamTalwar](https://github.com/DivyamTalwar)wants to merge 1 commit into

Open

[DivyamTalwar](https://github.com/DivyamTalwar) wants to merge 1 commit into

[DivyamTalwar](https://github.com/DivyamTalwar)wants to merge 1 commit into

## Conversation

Generated-by: OpenAI Codex GPT-5 Signed-off-by: Divyam Talwar <divyamtalwar0@gmail.com>

### This branch has not been deployed

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

`GenerativeRequestsAccumulator`

uses reservoir sampling to retain at most`sample_size`

request samples. When a new request is rejected by the reservoir, the accumulator previously left its`request_args`

, output, reasoning, and tool-call fields populated in`requests_stats`

. Repeated rejected requests could therefore retain unbounded heavy payload data despite the configured sample bound.The rejection branch now clears those fields while leaving the selected sample and aggregate metrics unchanged.

## Testing

`git diff --check`

: passed.The full tox environment could not be completed under shared optional dependency download contention; the focused test uses the real accumulator and schema classes without mocking the implementation.

No matching open or closed-unmerged PR was found. The nearby multipart payload report #988 concerns report serialization, not reservoir retention.

## Use of AI

The code and tests were generated with OpenAI Codex and require human review before submission. The commit includes

`Generated-by: OpenAI Codex GPT-5`

and`Signed-off-by: Divyam Talwar <divyamtalwar0@gmail.com>`

trailers.## git log

commit

1d15f09Author: Divyam Talwar divyamtalwar0@gmail.com

Date: Tue Sep 8 13:49:32 2026 +0530

Generated-by: OpenAI Codex GPT-5

Signed-off-by: Divyam Talwar divyamtalwar0@gmail.com