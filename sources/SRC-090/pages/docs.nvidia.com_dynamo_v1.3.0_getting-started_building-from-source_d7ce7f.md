source: https://docs.nvidia.com/dynamo/v1.3.0/getting-started/building-from-source
lastmod: 2026-09-24T19:58:16.636Z

# Building from Source

Build Dynamo from source when you want to contribute code, test features on the development branch, or customize the build. If you just want to run Dynamo, the [Local Installation](https://docs.nvidia.com/dynamo/v1.3.0/getting-started/local-installation) guide is faster.

This guide covers Ubuntu and macOS. For a containerized dev environment that handles all of this automatically, see [DevContainer](https://docs.nvidia.com/dynamo/v1.3.0/getting-started/building-from-source#devcontainer).

## 1. Install System Libraries

**Ubuntu:**

**macOS:**

## 2. Install Rust

## 3. Create a Python Virtual Environment

Install [uv](https://docs.astral.sh/uv/#installation) if you don’t have it:

Create and activate a virtual environment:

## 4. Install Build Tools

[Maturin](https://github.com/PyO3/maturin) is the Rust-Python bindings build tool. The `patchelf`

extra lets maturin patch native extension library paths during the build.

## 5. Build the Rust Bindings

## 6. Install GPU Memory Service

## 7. Install the Wheel

Install Dynamo with a backend extra to pull the inference engine and its CUDA dependencies. Choose the backend you intend to run:

The base `uv pip install -e .`

installs only the Dynamo runtime and frontend. A backend extra (`[vllm]`

, or `[sglang]`

) will install the relevant framework dependencies to run an inference worker. For the TensorRT-LLM backend, use the `tensorrtllm-runtime`

container instead of installing via `uv pip`

to ensure the right dependencies are installed. See [Local Installation](https://docs.nvidia.com/dynamo/v1.3.0/getting-started/local-installation) for more details.

## 8. Verify the Build

You should see the frontend command help output.

## DevContainer

VSCode and Cursor users can skip manual setup using pre-configured development containers. The DevContainer installs all toolchains, builds the project, and sets up the Python environment automatically.

Framework-specific containers are available for vLLM, SGLang, and TensorRT-LLM. See the [DevContainer README](https://github.com/ai-dynamo/dynamo/tree/v1.3.0/.devcontainer) for setup instructions.

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

**vLLM worker fails to start: FlashInfer sampler JIT and CUDA 13 wheels**

When you run a vLLM worker from a CUDA 13 source install, the worker can abort during startup with a FlashInfer JIT error:

The CUDA wheels resolved for a CUDA 13 install can be version-skewed: `torch`

pins the runtime headers to 13.0, while vLLM’s `tilelang`

dependency pulls `nvidia-cuda-nvcc`

13.2. FlashInfer compiles its sampler kernel with `nvcc`

against those headers, and the version mismatch fails the build. This is tracked upstream at [flashinfer#3493](https://github.com/flashinfer-ai/flashinfer/issues/3493).

Set `VLLM_USE_FLASHINFER_SAMPLER=0`

so vLLM falls back to its native sampler:

## Next Steps

[Contribution Guide](https://docs.nvidia.com/dynamo/v1.3.0/getting-started/contribution-guide)— Workflow for contributing code[Examples](https://github.com/ai-dynamo/dynamo/tree/v1.3.0/examples)— Explore the codebase[Good First Issues](https://github.com/ai-dynamo/dynamo/labels/good-first-issue)— Find a task to work on