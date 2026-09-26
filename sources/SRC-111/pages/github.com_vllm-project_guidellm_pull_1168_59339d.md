source: https://github.com/vllm-project/guidellm/pull/1168

# merge queue: checking #1159 on main (b18a987) - #1168

Closed

[mergify[bot]](https://github.com/mergify[bot])wants to merge 2 commits into

Closed

[mergify[bot]](https://github.com/mergify[bot]) wants to merge 2 commits into

[mergify[bot]](https://github.com/mergify[bot])wants to merge 2 commits into

## Conversation

vLLM reports per-request server-side timings and speculative-decoding acceptance in a `metrics` object beside `usage`, served behind `--per-request-spec-decode-metrics` since 0.29. `extract_choices_and_usage` reads only `choices` and `usage`, so the object is dropped before a `GenerationResponse` is built and never reaches the report. Record it on the handler where the raw response is already read, and carry it on `GenerationResponse.response_metrics` into `GenerativeRequestStats`. It is passed through as received rather than modelled, since its contents are the backend's own and vLLM marks the shape experimental. The completions and chat-completions handlers populate it; the responses handler leaves the default. `clear_stats_data` does not touch it, so a non-sampled request keeps its metrics like it keeps its usage. Assisted-by: Claude Code claude-opus-5 Signed-off-by: wenxuan-elastix <wenxuan@elastix.ai>

6 tasks

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

🎉 This pull request has been checked successfully and will be merged soon. 🎉#1159 is queued for merge on branch

main(b18a987).This pull request has been created by Mergify to check the mergeability of #1159.

You don't need to do anything. Mergify will close this pull request automatically when it is complete.

Required conditions of queue rule`default`

for merge:`github-review-approved`

[🛡 GitHub repository ruleset rule`Merge Requirements`

]`Merge Requirements`

]:`check-success = @github-actions/quality (3.10) / type-checks`

`check-neutral = @github-actions/quality (3.10) / type-checks`

`check-skipped = @github-actions/quality (3.10) / type-checks`

`Merge Requirements`

]:`check-success = @github-actions/quality (3.10) / precommit-checks`

`check-neutral = @github-actions/quality (3.10) / precommit-checks`

`check-skipped = @github-actions/quality (3.10) / precommit-checks`

`Merge Requirements`

]:`check-success = @github-actions/quality (3.10) / quality-checks`

`check-neutral = @github-actions/quality (3.10) / quality-checks`

`check-skipped = @github-actions/quality (3.10) / quality-checks`

`Merge Requirements`

]:`check-success = @github-actions/tests (3.10) / e2e-tests`

`check-neutral = @github-actions/tests (3.10) / e2e-tests`

`check-skipped = @github-actions/tests (3.10) / e2e-tests`

`Merge Requirements`

]:`check-success = @github-actions/tests (3.10) / integration-tests`

`check-neutral = @github-actions/tests (3.10) / integration-tests`

`check-skipped = @github-actions/tests (3.10) / integration-tests`

`Merge Requirements`

]:`check-success = @github-actions/tests (3.10) / unit-tests`

`check-neutral = @github-actions/tests (3.10) / unit-tests`

`check-skipped = @github-actions/tests (3.10) / unit-tests`

`Merge Requirements`

]:`check-success = @github-actions/update-description`

`check-neutral = @github-actions/update-description`

`check-skipped = @github-actions/update-description`

Required conditions to stay in the queue:`#approved-reviews-by >= 1`

`#changes-requested-reviews-by = 0`

`-closed`

`-draft`

`check-success = DCO`

`check-success = update-description`