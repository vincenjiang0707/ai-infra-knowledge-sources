source: https://github.com/vllm-project/guidellm/pull/666

# Lock all GitHub Actions to SHA - #666

## Conversation


[dbutenhof](https://github.com/dbutenhof)added

[dependencies](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Adependencies)

[internal](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Ainternal)

[build](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Abuild)

Mar 31, 2026

###
**
**[Copilot](https://github.com/apps/copilot-pull-request-reviewer)
AI
left a comment

**left a comment**

[Copilot](https://github.com/apps/copilot-pull-request-reviewer)AI

There was a problem hiding this comment.

## Pull request overview

This PR strengthens CI/CD supply-chain security by pinning external GitHub Actions to immutable commit SHAs and adding Dependabot configuration to keep those pins updated over time.

**Changes:**

- Replaced tag-based
`uses: owner/action@vX`

references with full commit SHAs across multiple GitHub workflows. - Pinned action references inside the repo’s composite action (
`.github/actions/python-uv`

). - Added a Dependabot config to scan GitHub Actions weekly.

### Reviewed changes

Copilot reviewed 12 out of 12 changed files in this pull request and generated 1 comment.

## Show a summary per file

| File | Description |
|---|---|
| .github/workflows/ui-testing.yml | Pins `actions/checkout` and `actions/setup-node` to SHAs for UI test workflows. |
| .github/workflows/ui-quality.yml | Pins `actions/checkout` and `actions/setup-node` to SHAs for UI quality workflows. |
| .github/workflows/testing.yml | Pins `actions/checkout` , `actions/cache` , and `docker/setup-buildx-action` to SHAs. |
| .github/workflows/release.yml | Pins checkout/artifact/pages/container-related actions (and external publish action) to SHAs. |
| .github/workflows/quality.yml | Pins `actions/checkout` and `actions/setup-python` to SHAs. |
| .github/workflows/nightly.yml | Pins actions for nightly UI publish and container build/push (but currently contains an invalid action ref; see comment). |
| .github/workflows/main.yml | Pins actions used for main-branch UI deploy to SHAs. |
| .github/workflows/development.yml | Pins actions used for dev deploys, PR commenting, caching, and container publish to SHAs. |
| .github/workflows/development-cleanup.yml | Pins actions used for cleanup workflow PR comment updates and gh-pages updates. |
| .github/workflows/container-maintenance.yml | Pins retention policy and podman login actions to SHAs. |
| .github/dependabot.yml | Adds weekly Dependabot updates for GitHub Actions. |
| .github/actions/python-uv/action.yml | Pins `actions/setup-python` and `astral-sh/setup-uv` to SHAs within composite action. |

💡 [Add Copilot custom instructions](https://github.com/vllm-project/guidellm/new/main?filename=.github/instructions/*.instructions.md) for smarter, more guided reviews. [Learn how to get started](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot).

[.github/workflows/nightly.yml](https://github.com/vllm-project/guidellm/pull/666/files#diff-0d5658b415099a82c11c03a06ca4ec765b4003a1f4b2f3f1943980a882cf8aa6)Outdated


**requested changes**

[sjmonson](https://github.com/sjmonson)Mar 31, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

Above typo needs to be addressed. I skimmed through the rest of the hashes and didn't see any obvious issues though they could be the wrong hashes.

[.github/dependabot.yml](https://github.com/vllm-project/guidellm/pull/666/files#diff-dd4fbda47e51f1e35defb9275a9cd9c212ecde0b870cba89ddaaae65c5f3cd28)

That's pretty much the worst thing about GitHub workflows & actions ... they're almost impossible to debug until merged, since even a PR can't access secrets. Obviously my cut-and-paste missed a character in that one dependency: it's reassuring that Copilot found it, and that provides some level of confidence that it'll work. |


**previously approved these changes**

[sjmonson](https://github.com/sjmonson)Mar 31, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

Soft approve. See comment.

[.github/dependabot.yml](https://github.com/vllm-project/guidellm/pull/666/files#diff-dd4fbda47e51f1e35defb9275a9cd9c212ecde0b870cba89ddaaae65c5f3cd28)Outdated

Instead of using just a version tag, consistently apply a full SHA reference to all external Actions. Set up dependabot to check them weekly. Signed-off-by: David Butenhof <dbutenho@redhat.com>

Signed-off-by: David Butenhof <dbutenho@redhat.com>

Note, some are multi-level: pattern `uses: \w+(/\w+)+@(?!\w{40})` finds non-SHA action references. Signed-off-by: David Butenhof <dbutenho@redhat.com>

Signed-off-by: David Butenhof <dbutenho@redhat.com>

Signed-off-by: David Butenhof <dbutenho@redhat.com>

[sjmonson](https://github.com/sjmonson)

[force-pushed](https://github.com/vllm-project/guidellm/compare/826a21604ff963761104c3419dd1b027846c0ebd..9b5176c8e6ae4e1ac334eba5ae16b01c2d5e1a4b)the feature/action branch from

[to](https://github.com/vllm-project/guidellm/commit/826a21604ff963761104c3419dd1b027846c0ebd)

`826a216`


`9b5176c`

[Compare](https://github.com/vllm-project/guidellm/compare/826a21604ff963761104c3419dd1b027846c0ebd..9b5176c8e6ae4e1ac334eba5ae16b01c2d5e1a4b)

March 31, 2026 20:11


**approved these changes**

[sjmonson](https://github.com/sjmonson)Mar 31, 2026


[dbutenhof](https://github.com/dbutenhof)added the

[cleanup](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Acleanup)

Apr 7, 2026

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

Loose version references to external GitHub Actions leave us potentially vulnerable to supply chain attacks. To reduce the risk, we should refer only to full SHA commits.

## Details

Instead of using just a version tag, consistently apply a full SHA reference to all external Actions.

Set up dependabot to check them weekly.

## Test Plan

Testing GitHub workflows is always tricky -- lets see if anything breaks.

## Related Issues

## Use of AI

`## WRITTEN BY AI ##`

)