source: https://github.com/vllm-project/guidellm/pull/928

# Bump transformers from 5.3.0 to 5.5.0 - #928

Merged

Merged

## Conversation

Bumps [transformers]([https://github.com/huggingface/transformers]) from 5.3.0 to 5.5.0. - [Release notes]([https://github.com/huggingface/transformers/releases]) - [Commits]([huggingface/transformers@]) --- updated-dependencies: - dependency-name: transformers dependency-version: 5.5.0 dependency-type: direct:production ... Signed-off-by: dependabot[bot] <support@github.com>v5.3.0...v5.5.0


[dependabot](https://github.com/apps/dependabot)Bot added

[dependencies](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Adependencies)

[python:uv](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Apython%3Auv)

Jul 13, 2026


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jul 14, 2026

Collaborator

|
|

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

Bumps transformers from 5.3.0 to 5.5.0.

## Release notes

Sourced from transformers's releases.... (truncated)

## Commits

`c1c3424`

update`20bff68`

update release workflow`8956441`

v5.5.0`5135e5e`

casually dropping the most capable open weights on the planet (#45192)`a594e09`

Internalise the NomicBERT model (#43067)`4932e97`

Fix resized LM head weights being overwritten by post_init (#45079)`57e8413`

[Qwen3.5 MoE] Add _tp_plan to ForConditionalGeneration (#45124)`b10552e`

Fix TypeError: 'NoneType' object is not iterable in GenerationMixin.generate ...`423f2a3`

fix(models): Fix dtype mismatch in SwitchTransformers and TimmWrapperModel (#...`ade7a05`

Generalize gemma vision mask to videos (#45185)Dependabot will resolve any conflicts with this PR as long as you don't alter it yourself. You can also trigger a rebase manually by commenting

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