source: https://github.com/vllm-project/guidellm/pull/1026

# fix: use spawn multiprocessing context on macOS - #1026

Merged

[mergify[bot]](https://github.com/mergify[bot])merged 1 commit into

Merged

## Conversation

Generated-by: OpenAI Codex GPT-5 Signed-off-by: nightcityblade <nightcityblade@gmail.com>

6 tasks


**approved these changes**

[sjmonson](https://github.com/sjmonson)Aug 13, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)
Collaborator


There was a problem hiding this comment.

LGTM, would like a test from [@jaredoconnell](https://github.com/jaredoconnell) who is a Mac user.

Contributor

|
Queued — the merge queue status continues in |


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Aug 13, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)
Collaborator


There was a problem hiding this comment.

I can confirm that this works. I agree that this is a better solution than just exclusively documenting it in the troubleshooting guide.

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

35 tasks

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Use the

`spawn`

multiprocessing context on macOS so worker startup does notoverride CPython's platform-safe default with

`fork`

. Signal-related startuperrors now also point users to the existing troubleshooting guide.

## Details

`spawn`

when`sys.platform == "darwin"`

while preserving the configured context elsewhere.## Test Plan

`tox -e test-unit`

— full unit invocation completed successfully (3,053 collected).`tox -e test-unit -- -k macos_uses_spawn_context`

— 1 passed, 3,052 deselected.`tox -e lint-check`

— Ruff format/check and mdformat passed.`tox -e type-check`

— Mypy passed for 162 source files.`git diff --check`

— passed.## Related Issues

`mp_context_type="fork"`

segfaults all workers on macOS (supported platform); actionable hint was removed from the error message #1022## Use of AI

The commit includes the required

`Generated-by: OpenAI Codex GPT-5`

trailer,and the generated regression test includes the marker required by

`AGENTS.md`

.## git log

commit

7b8941eAuthor: nightcityblade nightcityblade@gmail.com

Date: Thu Aug 13 23:29:10 2026 +0800

Generated-by: OpenAI Codex GPT-5

Signed-off-by: nightcityblade nightcityblade@gmail.com