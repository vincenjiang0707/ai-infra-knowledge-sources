source: https://docs.nvidia.com/dynamo/v1.2.1/getting-started/contribution-guide
lastmod: 2026-09-24T19:58:16.636Z

# Contribution Guide

Dynamo is an open-source distributed inference platform, built by a growing community of contributors. The project is licensed under [Apache 2.0](https://github.com/ai-dynamo/dynamo/blob/v1.2.1/LICENSE) and welcomes contributions of all sizes — from typo fixes to major features. Community contributions have shaped core areas of Dynamo including backend integrations, documentation, deployment tooling, and performance improvements.

With 200+ external contributors, 220+ merged community PRs, and new contributors joining every month, Dynamo is one of the fastest-growing open-source inference projects. Check out our [commit activity](https://github.com/ai-dynamo/dynamo/graphs/commit-activity) and [GitHub stars](https://github.com/ai-dynamo/dynamo/stargazers). This guide will help you get started.

Join the community:

[CNCF Slack (](https://communityinviter.com/apps/cloud-native/cncf)— join CNCF Slack and find us in`#ai-dynamo`

)`#ai-dynamo`

[Discord](https://discord.gg/D92uqZRjCZ)[GitHub Discussions](https://github.com/ai-dynamo/dynamo/discussions)[Design Proposals](https://github.com/ai-dynamo/enhancements)— RFCs for major features[Office Hours](https://www.youtube.com/playlist?list=PL5B692fm6--tgryKu94h2Zb7jTFM3Go4X)— biweekly calls[Community Meetings](https://docs.google.com/document/d/1uR8xD_hlYGwV6QspvSc36k1H-wo1BUcVmFbHH9xlXd8/view)([Youtube](https://www.youtube.com/@ai-dynamo-community)) — Weekly (Wed 10:30 AM PT) development community meetings[Dynamo Day Recordings](https://nvevents.nvidia.com/dynamoday)— deep dives from production users

## TL;DR

For experienced contributors:

- Fork and clone the repo
- For changes ≥100 lines or new features,
[open an issue](https://github.com/ai-dynamo/dynamo/issues/new?template=contribution_request.yml)first - Create a branch:
`git checkout -b yourname/fix-router-timeout`

- Make changes, run
`pre-commit run`

- Commit with DCO sign-off:
`git commit -s -m "fix: description"`

- Open a PR targeting
`main`


## Ways to Contribute

### Report a Bug

Found something broken? [Open a bug report](https://github.com/ai-dynamo/dynamo/issues/new?template=bug_report.yml) with:

- Steps to reproduce
- Expected vs. actual behavior
- Environment details (OS, GPU, Python version, Dynamo version)

### Improve Documentation

Documentation improvements are always welcome:

- Fixing typos or unclear explanations
- Adding examples or tutorials
- Improving API documentation

Small doc fixes can be submitted directly as PRs without an issue.

### Propose a Feature

Have an idea? [Open a feature request](https://github.com/ai-dynamo/dynamo/issues/new?template=feature_request.yml) to discuss it with maintainers before implementation.

### Contribute Code

Ready to write code? See the [Contribution Workflow](https://docs.nvidia.com/dynamo/v1.2.1/getting-started/contribution-guide#contribution-workflow) section below.

### Help the Community

Not all contributions are code. You can also:

- Answer questions on
[Discord](https://discord.gg/D92uqZRjCZ)or in the`#ai-dynamo`

channel on[CNCF Slack](https://communityinviter.com/apps/cloud-native/cncf) - Review pull requests
- Share how you’re using Dynamo — blog posts, talks, or social media
- Star the
[repository](https://github.com/ai-dynamo/dynamo)

## Getting Started

### Find an Issue

Browse [open issues](https://github.com/ai-dynamo/dynamo/issues) or look for:

### Fork and Clone

[Fork the repository](https://github.com/ai-dynamo/dynamo/fork)on GitHub- Clone your fork:

### Building from Source

Full build instructions are included below. Expand the accordion to set up your local development environment.

## Expand build instructions

#### 1. Install System Libraries

**Ubuntu:**

**macOS:**

#### 2. Install Rust

#### 3. Create a Python Virtual Environment

Install [uv](https://docs.astral.sh/uv/#installation) if you don’t have it:

Create and activate a virtual environment:

#### 4. Install Build Tools

[Maturin](https://github.com/PyO3/maturin) is the Rust-Python bindings build tool.

#### 5. Build the Rust Bindings

#### 6. Install GPU Memory Service

#### 7. Install the Wheel

#### 8. Verify the Build

VSCode and Cursor users can use the [ .devcontainer](https://github.com/ai-dynamo/dynamo/tree/v1.2.1/.devcontainer) folder for a pre-configured development environment. See the

[devcontainer README](https://github.com/ai-dynamo/dynamo/blob/v1.2.1/.devcontainer/README.md)for details.

### Set Up Pre-commit Hooks

You’re all set up! Get curious — explore the codebase, experiment with the [examples](https://github.com/ai-dynamo/dynamo/tree/v1.2.1/examples), and see how the pieces fit together. When you’re ready, pick an issue from the [Good First Issues](https://github.com/ai-dynamo/dynamo/labels/good-first-issue) board or read on for the full contribution workflow.

## Contribution Workflow

The contribution process depends on the size and scope of your change. Even when not required, opening an issue is a great way to start a conversation with Dynamo maintainers before investing time in a PR.

**Small changes (under 100 lines):** Submit a PR directly — no issue needed. This includes typos, simple bug fixes, and formatting. If your PR addresses an existing approved issue, link it with “Fixes #123”.

**Larger changes (≥100 lines):** [Open a Contribution Request](https://github.com/ai-dynamo/dynamo/issues/new?template=contribution_request.yml) issue first and wait for the `approved-for-pr`

label before submitting a PR.

**Architecture changes:** Changes that affect multiple components, introduce or modify public APIs, alter communication plane architecture, or affect backend integration contracts require a [Dynamo Enhancement Proposal (DEP)](https://github.com/ai-dynamo/enhancements). Open a DEP in the [ ai-dynamo/enhancements](https://github.com/ai-dynamo/enhancements) repo before starting implementation.

### Submitting a Pull Request

-
**Create a GitHub Issue**(if required) —[Open a Contribution Request](https://github.com/ai-dynamo/dynamo/issues/new?template=contribution_request.yml)and describe what you’re solving, your proposed approach, estimated PR size, and files affected. -
**Get Approval**— Wait for maintainers to review and apply the`approved-for-pr`

label. -
**Submit a Pull Request**—[Open a PR](https://github.com/ai-dynamo/dynamo/compare)that references the issue using GitHub keywords (e.g., “Fixes #123”). -
**Address Code Rabbit Review**— Respond to automated Code Rabbit suggestions, including nitpicks. -
**Trigger CI Tests**— For external contributors, a maintainer must comment`/ok to test COMMIT-ID`

to run the full CI suite, where`COMMIT-ID`

is the short SHA of your latest commit. Fix any failing tests before requesting human review. -
**Request Review**— Add the person who approved your issue as a reviewer. Check[CODEOWNERS](https://github.com/ai-dynamo/dynamo/blob/v1.2.1/CODEOWNERS)for required approvers based on files modified.

**AI-Generated Code:** While we encourage using AI tools, you must fully understand every change in your PR. Inability to explain submitted code will result in rejection.

### Branch Naming

Use a descriptive branch name that identifies you and the change:

Examples:

## Code Style & Quality

Maintainers assess contribution quality based on code style, test coverage, architecture alignment, and review responsiveness. Consistent, high-quality contributions are the foundation for building trust in the project.

### Pre-commit Hooks

All PRs are checked against [pre-commit hooks](https://github.com/ai-dynamo/dynamo/blob/v1.2.1/.pre-commit-config.yaml). After [installing pre-commit](https://docs.nvidia.com/dynamo/v1.2.1/getting-started/contribution-guide#set-up-pre-commit-hooks), run checks locally:

### Commit Message Conventions

Use [conventional commit](https://www.conventionalcommits.org/) prefixes:

Examples:

### Language Conventions

### Testing

Run the test suite before submitting a PR:

For Rust components:

For the Kubernetes operator (Go):

### General Guidelines

- Keep PRs focused — one concern per PR
- Write clean, well-documented code that future contributors can understand
- Include tests for new functionality and bug fixes
- Ensure clean builds (no warnings or errors)
- All tests must pass
- No commented-out code
- Respond to review feedback promptly and constructively

### Running GitHub Actions Locally

Use [act](https://nektosact.com/) to run workflows locally:

Or use the [GitHub Local Actions](https://marketplace.visualstudio.com/items?itemName=SanjulaGanepola.github-local-actions) VS Code extension.

## What to Expect

### Status Labels

### Response Times

We aim to:

**Respond**to new issues within a few business days**Triage**high-priority issues within a week

Issues with no activity for 30 days may be auto-closed (can be reopened).

### Review Process

After you submit a PR and complete the steps in [Submitting a Pull Request](https://docs.nvidia.com/dynamo/v1.2.1/getting-started/contribution-guide#submitting-a-pull-request):

- The reviewer will provide feedback — please respond to all comments within a reasonable timeframe
- If changes are requested, address them and ping the reviewer for re-review
- If your PR hasn’t been reviewed within 7 days, feel free to ping the reviewer or leave a comment

### Good First Issues

Issues labeled `good-first-issue`

are sized for new contributors. We provide extra guidance on these — look for clear acceptance criteria and a suggested approach in the issue description.

## DCO & Licensing

### Developer Certificate of Origin

Dynamo requires all contributions to be signed off with the [Developer Certificate of Origin (DCO)](https://developercertificate.org/). This certifies that you have the right to submit your contribution under the project’s [Apache 2.0 license](https://github.com/ai-dynamo/dynamo/blob/v1.2.1/LICENSE).

Each commit must include a sign-off line:

Add this automatically with the `-s`

flag:

**Requirements:**

- Use your real name (no pseudonyms or anonymous contributions)
- Your
`user.name`

and`user.email`

must be configured in git

**DCO Check Failed?** See our [DCO Troubleshooting Guide](https://github.com/ai-dynamo/dynamo/blob/v1.2.1/DCO.md) for step-by-step instructions to fix it.

### License

By contributing, you agree that your contributions will be licensed under the [Apache 2.0 License](https://github.com/ai-dynamo/dynamo/blob/v1.2.1/LICENSE).

## Code of Conduct

We are committed to providing a welcoming and inclusive environment. All participants are expected to abide by our [Code of Conduct](https://github.com/ai-dynamo/dynamo/blob/v1.2.1/CODE_OF_CONDUCT.md).

## Security

If you discover a security vulnerability, please follow the instructions in our [Security Policy](https://github.com/ai-dynamo/dynamo/blob/v1.2.1/SECURITY.md). Do not open a public issue for security vulnerabilities.

## Getting Help

**CNCF Slack**:[Join CNCF Slack](https://communityinviter.com/apps/cloud-native/cncf)and find us in`#ai-dynamo`

**Discord**:[Join our community](https://discord.gg/D92uqZRjCZ)**Discussions**:[GitHub Discussions](https://github.com/ai-dynamo/dynamo/discussions)**Design Proposals**:[RFCs for major features](https://github.com/ai-dynamo/enhancements)**Office Hours**:[Biweekly calls](https://www.youtube.com/playlist?list=PL5B692fm6--tgryKu94h2Zb7jTFM3Go4X)**Community Meetings**:[Weekly (Wed 10:30 AM PT) development community meetings](https://docs.google.com/document/d/1uR8xD_hlYGwV6QspvSc36k1H-wo1BUcVmFbHH9xlXd8/view)([Youtube](https://www.youtube.com/@ai-dynamo-community))**Dynamo Day Recordings**:[Deep dives from production users](https://nvevents.nvidia.com/dynamoday)**Documentation**:[docs.nvidia.com/dynamo](https://docs.nvidia.com/dynamo/)

Thank you for contributing to Dynamo!