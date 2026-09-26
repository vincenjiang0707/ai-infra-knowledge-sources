source: https://docs.nvidia.com/dynamo/zh-CN/contributing/getting-started
lastmod: 2026-09-23T23:30:39.914Z

# Contributor Getting Started

Use this tutorial to prepare a local checkout and create your first contribution. For the policy
that determines whether you should open an issue first, see [Contribution Flow](https://docs.nvidia.com/dynamo/contributing/contribution-flow).

### Choose a contribution

Browse [good first issues](https://github.com/ai-dynamo/dynamo/labels/good-first-issue),
[help wanted issues](https://github.com/ai-dynamo/dynamo/labels/help-wanted), or the complete
[issue list](https://github.com/ai-dynamo/dynamo/issues).

You can submit typo corrections and other focused fixes directly. Before beginning a feature,
broad refactor, or architectural change, follow the issue-first guidance in
[Contribution Flow](https://docs.nvidia.com/dynamo/contributing/contribution-flow#decide-whether-to-open-an-issue).

### Fork and clone the repository

[Fork the Dynamo repository](https://github.com/ai-dynamo/dynamo/fork), then clone your fork and
add the upstream repository:

### Prepare the development environment

Follow [Building from Source](https://docs.nvidia.com/dynamo/advanced-customizations/building-from-source) for system packages,
Rust, Python, and build instructions.

You can also use the repository’s
[development container](https://github.com/ai-dynamo/dynamo/tree/v1.4.2/.devcontainer) for a
preconfigured environment.

### Install pre-commit hooks

Install the hooks once in your checkout:

Before committing, run the hooks against the files in your change:

Use `pre-commit run --all-files`

when you need to validate the entire repository.

### Configure DCO sign-off

Configure the name and email that should appear in your commits:

Every commit must include a Developer Certificate of Origin (DCO) sign-off. Add it with `-s`

:

For the full requirement and repair instructions, see
[DCO and Licensing](https://docs.nvidia.com/dynamo/contributing/dco-and-licensing).

### Verify the commit

Confirm that the latest commit message contains a `Signed-off-by`

trailer:

The output must end with a line like:

Then inspect the change you are about to submit:

### Continue to the pull request flow

Follow [Contribution Flow](https://docs.nvidia.com/dynamo/contributing/contribution-flow) to decide whether an issue is required, push
your branch, open the pull request, and work through CI and review.