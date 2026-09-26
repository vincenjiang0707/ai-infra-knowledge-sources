source: https://github.com/vllm-project/guidellm/pull/1011

# Bump h2 from 4.3.0 to 4.4.1 - #1011

Merged

Merged

## Conversation

Bumps [h2]([https://github.com/python-hyper/h2]) from 4.3.0 to 4.4.1. - [Changelog]([https://github.com/python-hyper/h2/blob/master/CHANGELOG.rst]) - [Commits]([python-hyper/h2@]) --- updated-dependencies: - dependency-name: h2 dependency-version: 4.4.1 dependency-type: indirect ... Signed-off-by: dependabot[bot] <support@github.com>v4.3.0...v4.4.1


[dependabot](https://github.com/apps/dependabot)Bot added

[dependencies](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Adependencies)

[python:uv](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Apython%3Auv)

Aug 7, 2026


**approved these changes**

[sjmonson](https://github.com/sjmonson)Aug 7, 2026

Collaborator

|
|

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

Bumps h2 from 4.3.0 to 4.4.1.

## Changelog

Sourced from h2's changelog.## Commits

`bc239af`

v4.4.1`92b925e`

add test for duplicate host headers`292a408`

reject duplicate Host headers in request headers`04d3b87`

update changelog`439b970`

prepare for next release cycle`9a7ff74`

performance: remove consumed frames in place from data buffer (#1321)`6cce763`

v4.4.0`dfafda3`

Bump pytest from 8.4.2 to 9.0.3 (#1320)`b45207c`

dependencies and packaging++`c40145f`

parse`content-length`

headers according to RFC9110 grammar for numbers (1*DI...Dependabot will resolve any conflicts with this PR as long as you don't alter it yourself. You can also trigger a rebase manually by commenting

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