source: https://docs.nvidia.com/dynamo/contributing/contribution-flow
lastmod: 2026-09-24T19:58:16.636Z

# Contribution Flow

This guide describes the normal contribution path after your local environment is ready. If you
have not prepared a fork or configured commit sign-off, begin with
[Getting Started](https://docs.nvidia.com/dynamo/contributing/getting-started).

## Decide Whether to Open an Issue

Small, focused changes can usually go directly to a pull request. Examples include typo fixes, documentation corrections, small bug fixes, and narrow configuration changes.

Open a [Contribution Request](https://github.com/ai-dynamo/dynamo/issues/new?template=contribution_request.yml)
before implementation when a change is large, introduces a feature, spans multiple components, or
would benefit from agreement on the approach. Wait for maintainer approval before investing in a
substantial implementation.

Changes that modify public APIs, communication-plane architecture, backend integration contracts,
or multiple major components require a
[Dynamo Enhancement Proposal (DEP)](https://github.com/ai-dynamo/enhancements).

## Submit and Refine the Change

### Create a focused branch

Update your local `main`

branch and create a descriptive branch:

Keep one concern per branch and pull request.

### Implement and validate

Make the smallest complete change that solves the problem. Add or update tests when behavior
changes, and run the relevant checks from [Code Quality](https://docs.nvidia.com/dynamo/contributing/code-quality).

Commit each logical change with DCO sign-off:

### Open the pull request

Push your branch to your fork:

[Open a pull request](https://github.com/ai-dynamo/dynamo/compare) against `main`

. Link the
approved issue when one exists. Use a Conventional Commit title, such as
`fix(router): handle streaming timeout`

, and include **Summary** and **Validation** sections in
the pull request description.

### Complete automated review and CI

Respond to actionable automated review comments and fix failing checks.

For external contributions, a maintainer might need to authorize CI for the latest commit. If requested, wait for a maintainer to trigger the tests rather than repeatedly pushing unchanged commits.

You are responsible for understanding and validating all submitted code, including code produced with AI assistance.

### Request and address review

Request review from the maintainer who approved the issue when applicable. The repository
[CODEOWNERS](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/CODEOWNERS) file identifies required
reviewers for many paths.

Respond to review comments, push follow-up commits with DCO sign-off, and re-request review when the change is ready.

### Keep the branch current

If the target branch advances or the pull request develops conflicts, rebase on the current upstream branch:

Recheck DCO trailers after rewriting commits. See
[DCO and Licensing](https://docs.nvidia.com/dynamo/contributing/dco-and-licensing#verify-every-commit) for a branch-wide check.

## Issue and Review States

Common issue labels communicate the next action:

Review timing depends on the size, risk, and maintainer availability. If a pull request has had no activity for a week, leave a concise follow-up comment or contact the approving maintainer.