source: https://github.com/vllm-project/guidellm/pull/938

# Fix misleading CLI help text for benchmark command group - #938

Merged

[mergify[bot]](https://github.com/mergify[bot])merged 2 commits into

Merged

## Conversation

Contributor

|
Hi |

[bennyturns](https://github.com/bennyturns)

[force-pushed](https://github.com/vllm-project/guidellm/compare/8655eb80c9c339580750e7043fcb269536165908..adbe575c8d57c7edc9cfbb66ca8641b05d4bd86f)the fix/cli-help-improvements branch 2 times, most recently from

[to](https://github.com/vllm-project/guidellm/commit/8655eb80c9c339580750e7043fcb269536165908)

`8655eb8`


`adbe575`

[Compare](https://github.com/vllm-project/guidellm/compare/8655eb80c9c339580750e7043fcb269536165908..adbe575c8d57c7edc9cfbb66ca8641b05d4bd86f)

July 19, 2026 20:11


**requested changes**

[dbutenhof](https://github.com/dbutenhof)Jul 20, 2026

Collaborator


There was a problem hiding this comment.

Some nice cleanups -- thanks. One problem -- you've documented something that used to work but no longer can. We should do something about that; but for now let's just not add the misleading documentation.

You also need to *sign* your commits before our CI will accept them. (Look at the failing DCO check.)

[src/guidellm/cli/benchmark/__init__.py](https://github.com/vllm-project/guidellm/pull/938/files#diff-684e86869ce719a51e8470c766ee7155feebd284509ffc56aae74d2663fd4625)Outdated


[dbutenhof](https://github.com/dbutenhof)added

[community contribution](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3A%22community%20contribution%22)

[bug](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Abug)

[escape](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Aescape)

[cli](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Acli)

Jul 20, 2026

- Fix benchmark group help: was describing the from-file subcommand instead of the group itself - Fix grammar in --label help: "Define a labels" -> "Define a label" - Fix missing space before [repeatable] tags in --label and --override - Add missing help text for from-file --output option Fixes[vllm-project#937]Signed-off-by: bennyturns <bturner@redhat.com>

[bennyturns](https://github.com/bennyturns)

[force-pushed](https://github.com/vllm-project/guidellm/compare/adbe575c8d57c7edc9cfbb66ca8641b05d4bd86f..63b181b053a57abfa8adc6ca1d82e5a32c8a9516)the fix/cli-help-improvements branch from

[to](https://github.com/vllm-project/guidellm/commit/adbe575c8d57c7edc9cfbb66ca8641b05d4bd86f)

`adbe575`


`63b181b`

[Compare](https://github.com/vllm-project/guidellm/compare/adbe575c8d57c7edc9cfbb66ca8641b05d4bd86f..63b181b053a57abfa8adc6ca1d82e5a32c8a9516)

July 21, 2026 13:39


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jul 21, 2026

Contributor

|
Queued — the merge queue status continues in |


**approved these changes**

[SkiHatDuckie](https://github.com/SkiHatDuckie)Jul 21, 2026

Collaborator

|
|

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

35 tasks

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

`benchmark`

group help text: was describing the`from-file`

subcommand ("Load a previously saved benchmark report") instead of the group itself. Now correctly describes the group and explains the`run`

command fallback behavior.`--label`

help: "Define a labels" → "Define a label"`[repeatable]`

tags in`--label`

and`--override`

help text`from-file --output`

option## Before

## After

Fixes #937

## Test plan

`guidellm benchmark --help`

and verify updated description`guidellm run --help`

and verify`--label`

and`--override`

help text`guidellm benchmark from-file --help`

and verify`--output`

has help text🤖 Generated with Claude Code

## git log

commit

63b181bAuthor: bennyturns bturner@redhat.com

Date: Sun Jul 19 14:02:57 2026 -0400

Signed-off-by: bennyturns bturner@redhat.com