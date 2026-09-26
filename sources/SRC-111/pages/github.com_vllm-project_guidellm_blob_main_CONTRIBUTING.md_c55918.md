source: https://github.com/vllm-project/guidellm/blob/main/CONTRIBUTING.md

Thank you for considering contributing to GuideLLM! We welcome contributions from the community to help improve and grow this project. This document outlines the process and guidelines for contributing.

There are many ways to contribute to GuideLLM:

**Reporting Bugs**: If you encounter a bug, please let us know by creating an issue.**Suggesting Features**: Have an idea for a new feature? Open an issue to discuss it.**Improving Documentation**: Help us improve our documentation by submitting pull requests.**Writing Code**: Contribute code to fix bugs, add features, or improve performance.**Reviewing Pull Requests**: Provide feedback on open pull requests to help maintain code quality.

Before contributing, ensure you have the following installed:

- Python 3.10 or higher
- pip (Python package manager)
- Tox
- Git

You can either clone the repository directly or fork it if you plan to contribute changes back:

-
Clone the repository to your local machine:

`git clone https://github.com/vllm-project/guidellm.git cd guidellm`


-
Fork the repository by clicking the "Fork" button on the repository's GitHub page.

-
Clone your forked repository to your local machine:

git clone https://github.com/<your-username>/guidellm.git cd guidellm


For detailed instructions on setting up your development environment, please refer to the [DEVELOPING.md](https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md) file. It includes step-by-step guidance on:

- Installing dependencies
- Running tests
- Using Tox for various tasks

We follow strict coding standards to ensure code quality and maintainability. Please adhere to the following guidelines:

**Code Style**: Use[Black](https://black.readthedocs.io/en/stable/)for code formatting and[Ruff](https://github.com/charliermarsh/ruff)for linting.**Type Checking**: Use[Mypy](http://mypy-lang.org/)for type checking.**Testing**: Write unit tests for new features and bug fixes. Use[pytest](https://docs.pytest.org/)for testing.**Documentation**: Update documentation for any changes to the codebase.

To check code quality locally, use the following Tox environment:

`tox -e lint-check`

To automatically fix style issues, use:

`tox -e lint-fix`

To run type checks, use:

`tox -e type-check`

-
**Create a Branch**: Create a new branch for your changes:git checkout -b feature/your-feature-name

-
**Make Changes**: Commit your changes with clear and descriptive commit messages. -
**Run Tests and Quality Checks**: Before submitting your changes, ensure all tests pass and code quality checks are satisfied:tox

-
**Push Changes**: Push your branch to your forked repository (if you forked):git push origin feature/your-feature-name

-
**Open a Pull Request**: Go to the original repository and open a pull request. Provide a clear description of your changes and link any related issues.

If you encounter a bug or have a feature request, please open an issue on GitHub. Include as much detail as possible, such as:

- Steps to reproduce the issue
- Expected and actual behavior
- Environment details (OS, Python version, etc.)

We are committed to fostering a welcoming and inclusive community. Please read and adhere to our [Code of Conduct](https://github.com/vllm-project/guidellm/blob/main/CODE_OF_CONDUCT.md).

By contributing to GuideLLM, you agree that your contributions will be licensed under the [Apache License 2.0](https://github.com/vllm-project/guidellm/blob/main/LICENSE).