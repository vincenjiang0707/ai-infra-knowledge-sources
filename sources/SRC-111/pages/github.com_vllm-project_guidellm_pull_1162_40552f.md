source: https://github.com/vllm-project/guidellm/pull/1162

# build(deps): Bump anyio from 4.12.0 to 4.14.2 - #1162

Merged

Merged

## Conversation

Bumps [anyio]([https://github.com/agronholm/anyio]) from 4.12.0 to 4.14.2. - [Release notes]([https://github.com/agronholm/anyio/releases]) - [Commits]([agronholm/anyio@]) --- updated-dependencies: - dependency-name: anyio dependency-version: 4.14.2 dependency-type: indirect ... Signed-off-by: dependabot[bot] <support@github.com>4.12.0...4.14.2


[dependabot](https://github.com/apps/dependabot)Bot added

[dependencies](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Adependencies)

[python:uv](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Apython%3Auv)

Sep 18, 2026


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Sep 19, 2026

Contributor

|
Queued — the merge queue status continues in |


**approved these changes**

[sjmonson](https://github.com/sjmonson)Sep 21, 2026

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

Bumps anyio from 4.12.0 to 4.14.2.

## Release notes

Sourced from anyio's releases.... (truncated)

## Commits

`c384f99`

Bumped up the version`dbba29d`

Fixed 100% CPU spin on cancel scope misuse (#1217)`6bbc6c3`

Fix CapacityLimiter over-granting tokens on asyncio (#1172)`6f82b25`

Refactored TestTLSStream.test_receive_invalid_max_bytes() to be less flaky`be24b04`

Relaxed timeouts to fix test flakiness`8113506`

Fix test flakiness caused by slow callback duration logging`1e988b6`

Fixed CapacityLimiter raising trio.WouldBlock instead of anyio.WouldBlock (#1...`44713f3`

Pin setup-uv to a commit sha across downstream jobs (#1213)`f1b7301`

Fixed stderr writes in a worker subprocess causing a deadlock (#1207)`212be93`

Fix flaky test_tcp_listener_same_port using a hardcoded port (#1206)Dependabot will resolve any conflicts with this PR as long as you don't alter it yourself. You can also trigger a rebase manually by commenting

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