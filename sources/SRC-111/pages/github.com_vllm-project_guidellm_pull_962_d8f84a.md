source: https://github.com/vllm-project/guidellm/pull/962

# Bump urllib3 from 2.6.3 to 2.7.0 - #962

Merged

Merged

## Conversation

Bumps [urllib3]([https://github.com/urllib3/urllib3]) from 2.6.3 to 2.7.0. - [Release notes]([https://github.com/urllib3/urllib3/releases]) - [Changelog]([https://github.com/urllib3/urllib3/blob/main/CHANGES.rst]) - [Commits]([urllib3/urllib3@]) --- updated-dependencies: - dependency-name: urllib3 dependency-version: 2.7.0 dependency-type: indirect ... Signed-off-by: dependabot[bot] <support@github.com>2.6.3...2.7.0


[dependabot](https://github.com/apps/dependabot)Bot added

[dependencies](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Adependencies)

[python:uv](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Apython%3Auv)

Jul 24, 2026


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jul 24, 2026

Collaborator

|
|

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

Bumps urllib3 from 2.6.3 to 2.7.0.

## Release notes

Sourced from urllib3's releases.## Changelog

Sourced from urllib3's changelog.... (truncated)

## Commits

`9a950b9`

Release 2.7.0`5ec0de4`

Merge commit from fork`2bdcc44`

Merge commit from fork`f45b0df`

Fix a misleading example for`ProxyManager`

(#4970)`577193c`

Switch to nightly PyPy3.11 in CI for now (#4984)`e90af45`

Avoid infinite loop in`HTTPResponse.read_chunked`

when`amt=0`

(#4974)`67ed74f`

Bump dev dependencies (#4972)`3abd481`

Upgrade mypy to version 1.20.2 (#4978)`2b8725d`

Drop support for EOL PyPy3.10 (#4979)`2944b2a`

Upgrade`setup-chrome`

and`setup-firefox`

to fix warnings (#4973)Dependabot will resolve any conflicts with this PR as long as you don't alter it yourself. You can also trigger a rebase manually by commenting

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