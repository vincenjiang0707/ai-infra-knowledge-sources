source: https://github.com/vllm-project/guidellm/pull/942

# Bump pillow from 12.2.0 to 12.3.0 - #942

Merged

Merged

## Conversation

Bumps [pillow]([https://github.com/python-pillow/Pillow]) from 12.2.0 to 12.3.0. - [Release notes]([https://github.com/python-pillow/Pillow/releases]) - [Changelog]([https://github.com/python-pillow/Pillow/blob/main/CHANGES.rst]) - [Commits]([python-pillow/Pillow@]) --- updated-dependencies: - dependency-name: pillow dependency-version: 12.3.0 dependency-type: direct:production ... Signed-off-by: dependabot[bot] <support@github.com>12.2.0...12.3.0


[dependabot](https://github.com/apps/dependabot)Bot added

[dependencies](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Adependencies)

[python:uv](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Apython%3Auv)

Jul 21, 2026


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jul 21, 2026

Contributor

|
Queued — the merge queue status continues in |

Collaborator

|
|

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

Bumps pillow from 12.2.0 to 12.3.0.

## Release notes

Sourced from pillow's releases.... (truncated)

## Commits

`bb1d8e8`

12.3.0 version bump`e63fc48`

Add release notes for SBOM and performance improvements (#9747)`13b701b`

Add release notes for #9679`5564ca7`

List methods`a0920fd`

Speed up ImageChops operations (#9738)`07e9a6c`

Speed up`Image.filter()`

(#9736)`a94578c`

Speed up`Image.getchannel()`

,`Image.merge()`

,`Image.putalpha()`

and `Image...`53e02c4`

Speed up`Image.fill()`

,`Image.linear_gradient()`

and `Image.radial_gradient...`af03747`

Speed up`Image.resample()`

(#9739)`5c9ca56`

Speed up`alpha_composite`

,`matrix`

,`negative`

,`quantize`

(#9740)Dependabot will resolve any conflicts with this PR as long as you don't alter it yourself. You can also trigger a rebase manually by commenting

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