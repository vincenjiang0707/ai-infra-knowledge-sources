source: https://docs.nvidia.com/dynamo/contributing/code-quality
lastmod: 2026-09-24T19:58:16.636Z

# Code Quality

Keep pull requests focused and validate the code paths they change. Maintainers assess correctness, test coverage, architecture fit, readability, and how review feedback is addressed.

## Pre-commit Checks

The repository configures checks in
[ .pre-commit-config.yaml](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/.pre-commit-config.yaml).
Run them before pushing:

To check the complete repository, run:

## Commit Messages

Use a [Conventional Commit](https://www.conventionalcommits.org/) title. Add a scope when it makes
ownership or impact clearer.

Examples:

Every commit must also include DCO sign-off; see
[DCO and Licensing](https://docs.nvidia.com/dynamo/contributing/dco-and-licensing).

## Language Conventions

Use the formatter and linter configured by the component you change.

Follow patterns in the surrounding package. Do not introduce a new tool or convention in a focused feature or bug-fix pull request unless the change specifically targets project-wide tooling.

## Testing

Run the smallest relevant test set while iterating, then expand validation before requesting review. The correct command depends on the component.

Common starting points include:

Use package-specific test instructions when a component provides them. Include the exact commands
and results in the pull request’s **Validation** section.

## Quality Checklist

Before requesting review, confirm that the change:

- Solves one clearly stated problem.
- Includes tests for new behavior and bug fixes when practical.
- Builds without new warnings or errors.
- Contains no commented-out implementation or unrelated cleanup.
- Updates user or contributor documentation when behavior or workflows change.
- Passes relevant local checks.
- Uses signed-off commits.

CI is a final verification layer, not a replacement for targeted local testing.