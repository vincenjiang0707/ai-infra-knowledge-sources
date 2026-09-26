source: https://github.com/vllm-project/guidellm/pull/535

# OpenAI API-Key Support - #535

Merged

[sjmonson](https://github.com/sjmonson)merged 7 commits into

Merged

## Conversation

Assisted by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>

This code became dead with the recent backend refactor Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Generated-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/352a43bb32d8090be9bf0654975f46d172a65d7f..ad9cb41e936fea9e646d5778f523f3dfb34d96e5)the feature/openai-auth-support branch from

[to](https://github.com/vllm-project/guidellm/commit/352a43bb32d8090be9bf0654975f46d172a65d7f)

`352a43b`


`ad9cb41`

[Compare](https://github.com/vllm-project/guidellm/compare/352a43bb32d8090be9bf0654975f46d172a65d7f..ad9cb41e936fea9e646d5778f523f3dfb34d96e5)

January 16, 2026 19:25

Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>

Signed-off-by: Samuel Monson <smonson@redhat.com>


**approved these changes**

[sjmonson](https://github.com/sjmonson)Jan 16, 2026

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

A basic set of changes to add the api key as a bearer token to all relevant requests.

## Details

## Test Plan

Run a vLLM server with the option

`--api-key <your API key>`

passed in. After doing that, run a PR with this not specified, guidellm would usually fail. Try with the options as documented in this PR's content, and it should work.## Related Issues

## Use of AI

`## WRITTEN BY AI ##`

)