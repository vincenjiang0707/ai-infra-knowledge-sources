source: https://github.com/vllm-project/guidellm/pull/643

# Bump ujson from 5.11.0 to 5.12.0 - #643

Merged

Merged

## Conversation


[dependabot](https://github.com/apps/dependabot)Bot added

[dependencies](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Adependencies)

[python:uv](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Apython%3Auv)

Mar 18, 2026

Collaborator

|
|

[dependabot](https://github.com/apps/dependabot)Bot

[force-pushed](https://github.com/vllm-project/guidellm/compare/f98d5d21701005f732825411bfd70ea830f577ec..57ae554e7ca55ce1fa14691163742a39aaa0d50d)the dependabot/uv/ujson-5.12.0 branch from

[to](https://github.com/vllm-project/guidellm/commit/f98d5d21701005f732825411bfd70ea830f577ec)

`f98d5d2`


`57ae554`

[Compare](https://github.com/vllm-project/guidellm/compare/f98d5d21701005f732825411bfd70ea830f577ec..57ae554e7ca55ce1fa14691163742a39aaa0d50d)

March 18, 2026 18:04

Collaborator

|
|

Bumps [ujson]([https://github.com/ultrajson/ultrajson]) from 5.11.0 to 5.12.0. - [Release notes]([https://github.com/ultrajson/ultrajson/releases]) - [Commits]([ultrajson/ultrajson@]) --- updated-dependencies: - dependency-name: ujson dependency-version: 5.12.0 dependency-type: indirect ... Signed-off-by: dependabot[bot] <support@github.com>5.11.0...5.12.0

[dependabot](https://github.com/apps/dependabot)Bot

[force-pushed](https://github.com/vllm-project/guidellm/compare/57ae554e7ca55ce1fa14691163742a39aaa0d50d..b3cd1f38335cf0fab2c498a413edbb456d8e87b7)the dependabot/uv/ujson-5.12.0 branch from

[to](https://github.com/vllm-project/guidellm/commit/57ae554e7ca55ce1fa14691163742a39aaa0d50d)

`57ae554`


`b3cd1f3`

[Compare](https://github.com/vllm-project/guidellm/compare/57ae554e7ca55ce1fa14691163742a39aaa0d50d..b3cd1f38335cf0fab2c498a413edbb456d8e87b7)

March 19, 2026 15:46


**approved these changes**

[sjmonson](https://github.com/sjmonson)Mar 19, 2026

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

Bumps ujson from 5.11.0 to 5.12.0.

## Release notes

Sourced from ujson's releases.## Commits

`4baeb95`

Fix memory leak parsing large integers`486bd45`

Fix buffer overflow/infinite loop from indent handling`a465ed7`

Add leak detection to tests`32ebf66`

Remove upper bound of setuptools for PyPy (#704)`6bf41bd`

Remove upper bound of setuptools for PyPy`4a4fd73`

chore(deps): update github-actions`d708b05`

Add security policy (#699)`3d66f4d`

Add security policy`8f23cce`

[pre-commit.ci] pre-commit autoupdate (#698)`2696fc3`

[pre-commit.ci] pre-commit autoupdateDependabot will resolve any conflicts with this PR as long as you don't alter it yourself. You can also trigger a rebase manually by commenting

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