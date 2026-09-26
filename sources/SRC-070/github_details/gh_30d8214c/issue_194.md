# [Issue #194] Wheel is not supported in the platform

source: https://github.com/deepseek-ai/DeepGEMM/issues/194
state: open | updated: 2026-03-12T02:18:48Z
labels: 

## 正文

Hi, I am trying to install this package through `install.sh` on 79f48ee15a82dd5fad5cd9beaa393c1f755e6b55. However, I get:
```
ERROR: deep_gemm-2.0.0+79f48ee-cp310-cp310-linux_x86_64.whl is not a supported wheel on this platform.
```

I am using CUDA Version: 12.8 on H100 device. Did anyone meet this error before?

## 评论 (1)

### Lumb3 · 2026-03-12

The error indicates that the pre-built wheel `deep_gemm-2.0.0+79f48ee-cp310-cp310-linux_x86_64.whl` is not compatible with your current Python/platform environment. This often happens when:

- You are not using Python 3.10 (the wheel is built for `cp310`).
- Your `pip` version is outdated or your platform’s `manylinux` tags do not match those used to build the wheel (e.g., glibc version too old).
- You are inside a Conda environment with a different platform tag (e.g., `linux-64` vs `manylinux`).

Let’s troubleshoot step by step.

## 1. Verify your Python version
```bash
python --version
```
Must be `Python 3.10.x`. If not, switch to Python 3.10 (e.g., via `conda create -n deepgemm python=3.10` or `pyenv`).

## 2. Check your pip version and supported tags
```bash
pip --version                 # should be recent (≥21.x)
pip debug --verbose           # shows all supported wheel tags
```
Look for tags like `cp310-cp310-manylinux_*_x86_64`. Compare them with the wheel’s filename. If your system lacks a required `manylinux` tag, you’ll need to build from source.

## 3. Check glibc version
```bash
ldd --version | head -n1
```
Manylinux2014 requires glibc ≥ 2.17, manylinux_2_28 requires ≥ 2.28. If your glibc is older than what the wheel expects, you’ll get this error.

## 4. Build from source (recommended if the wheel is incompatible)
First, ensure you have CUDA 12.8 and PyTorch installed (with matching CUDA). Then, inside the repository root:
```bash
pip install .                 # builds from source
```
or, if you prefer a wheel:
```bash
pip install build
python -m build --wheel
pip install dist/deep_gemm-*.whl
```

## 5. If using Conda
Conda environments sometimes alter platform tags. Try:
```bash
conda install pip            # ensure conda’s pip is used
pip install .                # still fails? try with --no-build-isolation
```

## 6. Force installation (I would not recommended)
As a last resort, you can bypass tag checks with `--only-binary :all: --find-links . --no-index`, but this may lead to runtime errors if the wheel truly is incompatible.

Let me know which step reveals the mismatch, and we can dig deeper!
