source: https://github.com/vllm-project/guidellm/pull/884

# [GitHub Actions]: Bump docker/setup-qemu-action from 4.1.0 to 4.2.0 - #884

Merged

[mergify[bot]](https://github.com/mergify[bot])merged 1 commit into

Merged

## Conversation

Bumps [docker/setup-qemu-action]([https://github.com/docker/setup-qemu-action]) from 4.1.0 to 4.2.0. - [Release notes]([https://github.com/docker/setup-qemu-action/releases]) - [Commits]([docker/setup-qemu-action@]) --- updated-dependencies: - dependency-name: docker/setup-qemu-action dependency-version: 4.2.0 dependency-type: direct:production update-type: version-update:semver-minor ... Signed-off-by: dependabot[bot] <support@github.com>0611638...96fe6ef


[dependabot](https://github.com/apps/dependabot)Bot added

[build](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Abuild)

[dependencies](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Adependencies)

Jul 2, 2026


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jul 2, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)
Collaborator


There was a problem hiding this comment.

I notice that our commented version has gotten out of sync and dependabot isn't updating it. I'm tempted to fix that, but not quite motivated. Maybe I'll remember to catch it up later.

Contributor

|
Queued — the merge queue status continues in |

Contributor

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

34 tasks

[mergify](https://github.com/apps/mergify)Bot deleted the dependabot/github_actions/docker/setup-qemu-action-4.2.0 branch

July 2, 2026 21:46

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jul 6, 2026

[…llm-project#884]) Bumps [docker/setup-qemu-action]([https://github.com/docker/setup-qemu-action]) from 4.1.0 to 4.2.0. <details> <summary>Release notes</summary> <p><em>Sourced from <a href="[https://github.com/docker/setup-qemu-action/releases">docker/setup-qemu-action's]releases</a>.</em></p> <blockquote> <h2>v4.2.0</h2> <ul> <li>Preserve names in esbuild bundle by <a href="[https://github.com/crazy-max"><code>@crazy-max</code></a]> in <a href="[https://redirect.github.com/docker/setup-qemu-action/pull/311">docker/setup-qemu-action#311</a></li]> <li>Bump <code>@actions/core</code> from 3.0.0 to 3.0.1 in <a href="[https://redirect.github.com/docker/setup-qemu-action/pull/295">docker/setup-qemu-action#295</a></li]> <li>Bump <code>@docker/actions-toolkit</code> from 0.91.0 to 0.92.0 in <a href="[https://redirect.github.com/docker/setup-qemu-action/pull/315">docker/setup-qemu-action#315</a></li]> <li>Bump <code>@sigstore/core</code> from 3.1.0 to 3.2.1 in <a href="[https://redirect.github.com/docker/setup-qemu-action/pull/312">docker/setup-qemu-action#312</a></li]> <li>Bump js-yaml from 4.1.1 to 4.2.0 in <a href="[https://redirect.github.com/docker/setup-qemu-action/pull/310">docker/setup-qemu-action#310</a></li]> <li>Bump tmp from 0.2.6 to 0.2.7 in <a href="[https://redirect.github.com/docker/setup-qemu-action/pull/304">docker/setup-qemu-action#304</a></li]> <li>Bump undici from 6.26.0 to 6.27.0 in <a href="[https://redirect.github.com/docker/setup-qemu-action/pull/308">docker/setup-qemu-action#308</a></li]> <li>Bump vite from 7.3.2 to 7.3.6 in <a href="[https://redirect.github.com/docker/setup-qemu-action/pull/307">docker/setup-qemu-action#307</a></li]> </ul> <p><strong>Full Changelog</strong>: <a href="[https://github.com/docker/setup-qemu-action/compare/v4.1.0...v4.2.0">https://github.com/docker/setup-qemu-action/compare/v4.1.0...v4.2.0</a></p]> </blockquote> </details> <details> <summary>Commits</summary> <ul> <li><a href="[https://github.com/docker/setup-qemu-action/commit/96fe6ef7f33517b61c61be40b68a1882f3264fb8"><code>96fe6ef</code></a]> Merge pull request <a href="[https://redirect.github.com/docker/setup-qemu-action/issues/315">#315</a]> from docker/dependabot/npm_and_yarn/docker/actions-to...</li> <li><a href="[https://github.com/docker/setup-qemu-action/commit/31f08d3fc9186dbe4b4550696f2e32e9aa7f9465"><code>31f08d3</code></a]> [dependabot skip] chore: update generated content</li> <li><a href="[https://github.com/docker/setup-qemu-action/commit/4e7017a474d2cf3912bb0437f7fafec6d5fb6c52"><code>4e7017a</code></a]> build(deps): bump <code>@docker/actions-toolkit</code> from 0.91.0 to 0.92.0</li> <li><a href="[https://github.com/docker/setup-qemu-action/commit/0eca235293ca1939b58c082f69bdc981ccce8c94"><code>0eca235</code></a]> Merge pull request <a href="[https://redirect.github.com/docker/setup-qemu-action/issues/314">#314</a]> from crazy-max/fix-yarn-preapprove-actions-toolkit</li> <li><a href="[https://github.com/docker/setup-qemu-action/commit/ea66a4130b037e7961e14a0e5b155836e797cced"><code>ea66a41</code></a]> chore: allow actions-toolkit to bypass yarn age gate</li> <li><a href="[https://github.com/docker/setup-qemu-action/commit/451542b03ae7946b7082a398b11c8c315a0e4e80"><code>451542b</code></a]> Merge pull request <a href="[https://redirect.github.com/docker/setup-qemu-action/issues/308">#308</a]> from docker/dependabot/npm_and_yarn/undici-6.27.0</li> <li><a href="[https://github.com/docker/setup-qemu-action/commit/532ae0057542ec2102e2d19e9feccf85f1f69013"><code>532ae00</code></a]> [dependabot skip] chore: update generated content</li> <li><a href="[https://github.com/docker/setup-qemu-action/commit/b6f5af659afad3f9931b782668dee4595ae7e841"><code>b6f5af6</code></a]> build(deps): bump undici from 6.26.0 to 6.27.0</li> <li><a href="[https://github.com/docker/setup-qemu-action/commit/cf96b86294b57480ac6d330bd177fca87eac95bc"><code>cf96b86</code></a]> Merge pull request <a href="[https://redirect.github.com/docker/setup-qemu-action/issues/304">#304</a]> from docker/dependabot/npm_and_yarn/tmp-0.2.7</li> <li><a href="[https://github.com/docker/setup-qemu-action/commit/f0ba643f78dc96bc931fb83e5dadc39628e10047"><code>f0ba643</code></a]> [dependabot skip] chore: update generated content</li> <li>Additional commits viewable in <a href="[https://github.com/docker/setup-qemu-action/compare/06116385d9baf250c9f4dcb4858b16962ea869c3...96fe6ef7f33517b61c61be40b68a1882f3264fb8">compare]view</a></li> </ul> </details> <br /> [![Dependabot compatibility score]([https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=docker/setup-qemu-action&package-manager=github_actions&previous-version=4.1.0&new-version=4.2.0)](https://docs.github.com/en/github/managing-security-vulnerabilities/about-dependabot-security-updates#about-compatibility-scores]) Dependabot will resolve any conflicts with this PR as long as you don't alter it yourself. You can also trigger a rebase manually by commenting `@dependabot rebase`. [//]: # (dependabot-automerge-start) [//]: # (dependabot-automerge-end) --- <details> <summary>Dependabot commands and options</summary> <br /> You can trigger Dependabot actions by commenting on this PR: - `@dependabot rebase` will rebase this PR - `@dependabot recreate` will recreate this PR, overwriting any edits that have been made to it - `@dependabot show <dependency name> ignore conditions` will show all of the ignore conditions of the specified dependency - `@dependabot ignore this major version` will close this PR and stop Dependabot creating any more for this major version (unless you reopen the PR or upgrade to it yourself) - `@dependabot ignore this minor version` will close this PR and stop Dependabot creating any more for this minor version (unless you reopen the PR or upgrade to it yourself) - `@dependabot ignore this dependency` will close this PR and stop Dependabot creating any more for this dependency (unless you reopen the PR or upgrade to it yourself) </details>

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

Bumps docker/setup-qemu-action from 4.1.0 to 4.2.0.

## Release notes

Sourced from docker/setup-qemu-action's releases.## Commits

`96fe6ef`

Merge pull request #315 from docker/dependabot/npm_and_yarn/docker/actions-to...`31f08d3`

[dependabot skip] chore: update generated content`4e7017a`

build(deps): bump`@docker/actions-toolkit`

from 0.91.0 to 0.92.0`0eca235`

Merge pull request #314 from crazy-max/fix-yarn-preapprove-actions-toolkit`ea66a41`

chore: allow actions-toolkit to bypass yarn age gate`451542b`

Merge pull request #308 from docker/dependabot/npm_and_yarn/undici-6.27.0`532ae00`

[dependabot skip] chore: update generated content`b6f5af6`

build(deps): bump undici from 6.26.0 to 6.27.0`cf96b86`

Merge pull request #304 from docker/dependabot/npm_and_yarn/tmp-0.2.7`f0ba643`

[dependabot skip] chore: update generated contentDependabot will resolve any conflicts with this PR as long as you don't alter it yourself. You can also trigger a rebase manually by commenting

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