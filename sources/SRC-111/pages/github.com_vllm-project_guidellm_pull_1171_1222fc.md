source: https://github.com/vllm-project/guidellm/pull/1171

# ci: prevent broken pipe in PR formatter - #1171

Merged

[mergify[bot]](https://github.com/mergify[bot])merged 1 commit into

Merged

## Conversation

Replace the printf-to-head pipeline used to extract the user-authored PR content with sed. Unlike head, sed consumes the complete input and does not close the pipe early while printf is still writing a long PR body. Reported CI error: ./scripts/format_pr.sh: line 39: printf: write error: Broken pipe Error: Process completed with exit code 1. Tests: - tox -e lint-check - uv run --no-sync bash -c (50,000-line PR body extraction regression check) Assisted-by: Codex GPT-5 Signed-off-by: tangming1996 <ming.tang@daocloud.io>

[tangming1996](https://github.com/tangming1996)requested review from

[dbutenhof](https://github.com/dbutenhof),

[dfeddema](https://github.com/dfeddema),

[jaredoconnell](https://github.com/jaredoconnell)and

[sjmonson](https://github.com/sjmonson)as

[code owners](https://github.com/vllm-project/guidellm/blob/148c3bab4f75fe9f64fb15520d7d64fa08914a90/CODEOWNERS#L2)

September 22, 2026 08:10


**approved these changes**

[sjmonson](https://github.com/sjmonson)Sep 22, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)
Collaborator


There was a problem hiding this comment.

Awesome thanks for this fix.

Contributor

|
Received a single approval. Will automatically queue for merge once two maintainers approve, all change requests are resolved, and DCO passes. |

Contributor

|
Queued — the merge queue status continues in |


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Sep 22, 2026

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

35 tasks

8 tasks

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

Replace the printf-to-head pipeline used to extract the user-authored PR content with sed. Unlike head, sed consumes the complete input and does not close the pipe early while printf is still writing a long PR body.

Reported CI error:

./scripts/format_pr.sh: line 39: printf: write error: Broken pipe

Error: Process completed with exit code 1.

Tests:

Assisted-by: Codex GPT-5

## Summary

## Details

## Test Plan

## Related Issues

## Use of AI

## git log

commit

5c1a133Author: tangming1996 ming.tang@daocloud.io

Date: Tue Sep 22 16:08:04 2026 +0800

Assisted-by: Codex GPT-5

Signed-off-by: tangming1996 ming.tang@daocloud.io