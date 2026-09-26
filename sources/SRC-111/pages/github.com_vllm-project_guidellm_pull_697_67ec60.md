source: https://github.com/vllm-project/guidellm/pull/697

# Support server-side conversation history on responses API - #697

Merged

[jaredoconnell](https://github.com/jaredoconnell)merged 1 commit into

Merged

## Conversation

Assisted-by: Cursor AI Signed-off-by: Jared O'Connell <joconnel@redhat.com>

[jaredoconnell](https://github.com/jaredoconnell)

[force-pushed](https://github.com/vllm-project/guidellm/compare/ac0d1e3e5c39aec3c8da36ba4c3b51cb8216cc80..7b6164c06bd66d998f238d6ecb97123bda646f4a)the feat/responses-server-history branch from

[to](https://github.com/vllm-project/guidellm/commit/ac0d1e3e5c39aec3c8da36ba4c3b51cb8216cc80)

`ac0d1e3`


`7b6164c`

[Compare](https://github.com/vllm-project/guidellm/compare/ac0d1e3e5c39aec3c8da36ba4c3b51cb8216cc80..7b6164c06bd66d998f238d6ecb97123bda646f4a)

April 17, 2026 23:19

6 tasks

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Add support for server-side conversation history via previous_response_id on the /v1/responses endpoint. This allows multi-turn benchmarks to offload conversation state to the server instead of replaying the full history in every request, which is critical for benchmarking servers that use response storage (e.g. vLLM with VLLM_ENABLE_RESPONSES_API_STORE=1).

## Details

`server_history`

option to OpenAIHTTPBackend, validated to only work with /v1/responses`server_history`

is enabled.## Test Plan

## Use of AI

`## WRITTEN BY AI ##`

)