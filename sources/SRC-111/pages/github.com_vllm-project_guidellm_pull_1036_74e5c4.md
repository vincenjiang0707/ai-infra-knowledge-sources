source: https://github.com/vllm-project/guidellm/pull/1036

# [GitHub Actions]: Bump redhat-actions/buildah-build from 2.13 to 3 - #1036

Merged

[mergify[bot]](https://github.com/mergify[bot])merged 1 commit into

Merged

## Conversation

Bumps [redhat-actions/buildah-build]([https://github.com/redhat-actions/buildah-build]) from 2.13 to 3. - [Release notes]([https://github.com/redhat-actions/buildah-build/releases]) - [Changelog]([https://github.com/redhat-actions/buildah-build/blob/main/CHANGELOG.md]) - [Commits]([redhat-actions/buildah-build@]) --- updated-dependencies: - dependency-name: redhat-actions/buildah-build dependency-version: '3' dependency-type: direct:production update-type: version-update:semver-major ... Signed-off-by: dependabot[bot] <support@github.com>7a95fa7...3a51aad


[dependabot](https://github.com/apps/dependabot)Bot added

[build](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Abuild)

[dependencies](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Adependencies)

Aug 20, 2026


**approved these changes**

[sjmonson](https://github.com/sjmonson)Aug 21, 2026

Collaborator

|
|

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

35 tasks

[mergify](https://github.com/apps/mergify)Bot deleted the dependabot/github_actions/redhat-actions/buildah-build-3 branch

August 21, 2026 14:43

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

Bumps redhat-actions/buildah-build from 2.13 to 3.

## Release notes

Sourced from redhat-actions/buildah-build's releases.## Changelog

Sourced from redhat-actions/buildah-build's changelog.... (truncated)

## Commits

`3a51aad`

Update CHANGELOG and version for v3.0.2`69263e9`

Pass --root to containerized buildah so all invocations share storage (#177)`27e5954`

Update CHANGELOG and version for v3.0.1`6c3509d`

Detect container storage root instead of hardcoding it (#174) (#175)`3194d0c`

Document available buildah container images in README (#173)`5d84797`

Update README and CHANGELOG for v3.0.0 (#172)`464212a`

Replace deprecated link checker and fix 429 rate limiting (#171)`97fe4a5`

Fall back to podman when buildah is unavailable (#169)`3fe6dbb`

Remove defunct CRDA vulnerability scan workflow (#170)`02f342b`

Add buildah-image input to run buildah from a container (#168)Dependabot will resolve any conflicts with this PR as long as you don't alter it yourself. You can also trigger a rebase manually by commenting

`@dependabot rebase`

.## Dependabot commands and options

You can trigger Dependabot actions by commenting on this PR:

`@dependabot rebase`

will rebase this PR`@dependabot recreate`

will recreate this PR, overwriting any edits that have been made to it`@dependabot show <dependency name> ignore conditions`

will show all of the ignore conditions of the specified dependency`@dependabot ignore this major version`

will close this PR and stop Dependabot creating any more for this major version (unless you reopen the PR or upgrade to it yourself)`@dependabot ignore this minor version`

will close this PR and stop Dependabot creating any more for this minor version (unless you reopen the PR or upgrade to it yourself)`@dependabot ignore this dependency`

will close this PR and stop Dependabot creating any more for this dependency (unless you reopen the PR or upgrade to it yourself)