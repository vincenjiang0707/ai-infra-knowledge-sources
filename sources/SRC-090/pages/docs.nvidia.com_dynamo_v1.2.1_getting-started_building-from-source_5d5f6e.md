source: https://docs.nvidia.com/dynamo/v1.2.1/getting-started/building-from-source
lastmod: 2026-09-24T19:58:16.636Z

# Building from Source

Build Dynamo from source when you want to contribute code, test features on the development branch, or customize the build. If you just want to run Dynamo, the [Local Installation](https://docs.nvidia.com/dynamo/v1.2.1/getting-started/local-installation) guide is faster.

This guide covers Ubuntu and macOS. For a containerized dev environment that handles all of this automatically, see [DevContainer](https://docs.nvidia.com/dynamo/v1.2.1/getting-started/building-from-source#devcontainer).

## 1. Install System Libraries

**Ubuntu:**

**macOS:**

## 2. Install Rust

## 3. Create a Python Virtual Environment

Install [uv](https://docs.astral.sh/uv/#installation) if you don’t have it:

Create and activate a virtual environment:

## 4. Install Build Tools

[Maturin](https://github.com/PyO3/maturin) is the Rust-Python bindings build tool.

## 5. Build the Rust Bindings

## 6. Install GPU Memory Service

## 7. Install the Wheel

## 8. Verify the Build

You should see the frontend command help output.

## DevContainer

VSCode and Cursor users can skip manual setup using pre-configured development containers. The DevContainer installs all toolchains, builds the project, and sets up the Python environment automatically.

Framework-specific containers are available for vLLM, SGLang, and TensorRT-LLM. See the [DevContainer README](https://github.com/ai-dynamo/dynamo/tree/v1.2.1/.devcontainer) for setup instructions.

## Set Up Pre-commit Hooks

Before submitting PRs, install the pre-commit hooks to ensure your code passes CI checks:

Run checks manually on all files:

## Troubleshooting

**Missing system packages**

If `maturin develop`

fails with linker errors, verify all system dependencies are installed. On Ubuntu:

**Virtual environment not activated**

Maturin builds against the active Python interpreter. If you see errors about Python or site-packages, ensure your virtual environment is activated:

**Disk space**

The Rust `target/`

directory can grow to 10+ GB during development. If builds fail with disk space errors, clean the build cache:

## Next Steps

[Contribution Guide](https://docs.nvidia.com/dynamo/v1.2.1/getting-started/contribution-guide)— Workflow for contributing code[Examples](https://github.com/ai-dynamo/dynamo/tree/v1.2.1/examples)— Explore the codebase[Good First Issues](https://github.com/ai-dynamo/dynamo/labels/good-first-issue)— Find a task to work on