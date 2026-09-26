source: https://github.com/vllm-project/guidellm/pull/759

# Make synthetic_text output_tokens optional and improve CLI errors - #759

Merged

Merged

## Conversation


**requested changes**

[sjmonson](https://github.com/sjmonson)Jun 1, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)
Collaborator


There was a problem hiding this comment.

Thanks for the fixes! One minor nit.

[src/guidellm/cli/benchmark/run.py](https://github.com/vllm-project/guidellm/pull/759/files#diff-310250441381ed1c3efd1052124a9ab915eb1ec368404345bc7037069660a46a)Outdated


[sjmonson](https://github.com/sjmonson)added

[priority-medium](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Apriority-medium)

[feature](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Afeature)

[cli](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Acli)

Jun 1, 2026

Synthetic data generation already handled output_tokens being absent (samplers, features, and downstream max_tokens fallback all gated on None), but the schema declared it required. This forced users benchmarking endpoints with no output tokens (e.g. /v1/embeddings) to pass a meaningless value. Make the field default to None. Also fix the misleading "Invalid value for --data: Field required" CLI error: the pydantic-to-click translation in `benchmark run` was dropping the nested field location and only reporting the top-level CLI option. Errors now include the full path (e.g. data[0].synthetic_text.prompt_tokens) and aggregate multiple validation errors into a single message. Assisted-by: Cursor AI Claude Opus 4.7 Signed-off-by: Radoslav Gerganov <rgerganov@gmail.com>


**approved these changes**

[sjmonson](https://github.com/sjmonson)Jun 1, 2026

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Synthetic data generation already handled output_tokens being absent (samplers, features, and downstream max_tokens fallback all gated on None), but the schema declared it required. This forced users benchmarking endpoints with no output tokens (e.g. /v1/embeddings) to pass a meaningless value. Make the field default to None.

Also fix the misleading "Invalid value for --data: Field required" CLI error: the pydantic-to-click translation in

`benchmark run`

was dropping the nested field location and only reporting the top-level CLI option. Errors now include the full path (e.g. data[0].synthetic_text.prompt_tokens) and aggregate multiple validation errors into a single message.Assisted-by: Cursor AI Claude Opus 4.7

## Use of AI