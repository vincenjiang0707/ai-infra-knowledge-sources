source: https://github.com/vllm-project/guidellm/pull/1076

# build(deps): Bump transformers from 5.5.0 to 5.10.1 - #1076

Merged

Merged

## Conversation

Bumps [transformers]([https://github.com/huggingface/transformers]) from 5.5.0 to 5.10.1. - [Release notes]([https://github.com/huggingface/transformers/releases]) - [Commits]([huggingface/transformers@]) --- updated-dependencies: - dependency-name: transformers dependency-version: 5.10.1 dependency-type: direct:production ... Signed-off-by: dependabot[bot] <support@github.com>v5.5.0...v5.10.1


[dependabot](https://github.com/apps/dependabot)Bot added

[dependencies](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Adependencies)

[python:uv](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Apython%3Auv)

Sep 2, 2026


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Sep 2, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

AIPCC currently has 5.14.1 and 5.15.0 (3.6), so this should be safe and seems ultimately desirable. (Our pyproject.toml still has no version limits at all on transformers, which could be questioned given our experience -- anything less than 5.5.0 is definitely a no-no.)

Contributor

|
Queued — the merge queue status continues in |


**approved these changes**

[sjmonson](https://github.com/sjmonson)Sep 2, 2026

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

Bumps transformers from 5.5.0 to 5.10.1.

## Release notes

Sourced from transformers's releases.... (truncated)

## Commits

`90c3ae5`

Patch because we had to yank 5.10 because the release branch was not up to date`0bd94b3`

v5.10.0`1423d22`

who needs encoders? (#46385)`50eb20a`

Fix dsv4 dequant + tp/ep (#46378)`74464e8`

Fix wrong changes produced by style/repo. check bot (#46371)`1b8ec34`

Fix path traversal when saving Bark voice preset embeddings (#46237)`e820678`

Add Sapiens2 Model (#45919)`595721c`

Pass library_name/version to Hub calls via a shared HfApi (#46318)`0f0036c`

docs: update ACL Anthology URL in CITATION.cff (#46352)`fa6c830`

DeepGEMM BF16 + mixed FP8/FP4 + MegaMoE + refactor (#45634)Dependabot will resolve any conflicts with this PR as long as you don't alter it yourself. You can also trigger a rebase manually by commenting

`@dependabot rebase`

.## Dependabot commands and options

You can trigger Dependabot actions by commenting on this PR:

`@dependabot rebase`

will rebase this PR`@dependabot recreate`

will recreate this PR, overwriting any edits that have been made to it`@dependabot show <dependency name> ignore conditions`

will show all of the ignore conditions of the specified dependency`@dependabot ignore this major version`

will close this PR and stop Dependabot creating any more for this major version (unless you reopen the PR or upgrade to it yourself)`@dependabot ignore this minor version`

will close this PR and stop Dependabot creating any more for this minor version (unless you reopen the PR or upgrade to it yourself)`@dependabot ignore this dependency`

will close this PR and stop Dependabot creating any more for this dependency (unless you reopen the PR or upgrade to it yourself)You can disable automated security fix PRs for this repo from the Security Alerts page.