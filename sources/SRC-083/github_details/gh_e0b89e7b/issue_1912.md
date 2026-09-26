# [Issue #1912] `pip install` of preview wheel uninstalls XPU PyTorch and replaces it with CUDA PyTorch

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1912
state: closed | updated: 2026-04-08T13:54:20Z
labels: 

## 正文

### System Info

## Environment

- OS: Linux x86_64 (Ubuntu 24.04)
- Python: 3.12
- PyTorch: 2.11+xpu (XPU build, installed from Intel index)
- bitsandbytes wheel: `bitsandbytes-1.33.7.preview-py3-none-manylinux_2_24_x86_64.whl` from [continuous-release_main](https://github.com/bitsandbytes-foundation/bitsandbytes/releases/tag/continuous-release_main)

## Describe the bug

Installing the latest preview wheel from GitHub releases with `--force-reinstall` silently uninstalls the user's XPU PyTorch and replaces it with CUDA PyTorch from PyPI.

```bash
pip install --force-reinstall \
  https://github.com/bitsandbytes-foundation/bitsandbytes/releases/download/continuous-release_main/bitsandbytes-1.33.7.preview-py3-none-manylinux_2_24_x86_64.whl
```

The wheel metadata declares:

```
Requires-Dist: torch<3,>=2.3
```

When pip resolves this dependency with `--force-reinstall`, it pulls `torch` from the default PyPI index, which only hosts CUDA builds. This overwrites the XPU-flavored PyTorch (e.g. `torch==2.7.0+xpu` installed from `https://pytorch-extension.intel.com/release-whl/stable/xpu/us/`) with the CUDA variant.

### Reproduction

pip install --force-reinstall \
  https://github.com/bitsandbytes-foundation/bitsandbytes/releases/download/continuous-release_main/bitsandbytes-1.33.7.preview-py3-none-manylinux_2_24_x86_64.whl

### Expected behavior

Installing the bitsandbytes wheel should not replace an already-installed XPU PyTorch with the CUDA build. Users on XPU environments should be able to install bitsandbytes without losing their PyTorch backend.

## 评论 (3)

### jiqing-feng · 2026-04-08

Hi @matthewdouglas . Would you please take a look? Thanks!

### Titus-von-Koeller · 2026-04-08

Thanks for the report @jiqing-feng. This is unfortunately expected behavior from pip rather than a bitsandbytes bug — it affects any package that declares `torch` as a dependency.

When you pass `--force-reinstall`, pip re-resolves all dependencies from scratch against PyPI, which only hosts CUDA builds of torch. Since your XPU torch was installed from Intel's custom index, pip has no memory of that index and replaces it with the default CUDA variant. Any package depending on `torch` would cause the same issue in this scenario.

**Workaround:** use `--no-deps` to avoid touching your existing torch installation:

```bash
pip install --force-reinstall --no-deps \
  https://github.com/bitsandbytes-foundation/bitsandbytes/releases/download/continuous-release_main/bitsandbytes-1.33.7.preview-py3-none-manylinux_2_24_x86_64.whl
```

Or, if you want pip to resolve other dependencies (numpy, packaging) but still keep your XPU torch, pass Intel's index so pip can find the right torch:

```bash
pip install --force-reinstall \
  --extra-index-url https://pytorch-extension.intel.com/release-whl/stable/xpu/us/ \
  <wheel-url>
```

I've updated the [pre-release notes](https://github.com/bitsandbytes-foundation/bitsandbytes/releases/tag/continuous-release_main) to call this out for users with custom PyTorch builds. Closing as resolved.

### Titus-von-Koeller · 2026-04-08

@jiqing-feng feel free to reopen, if you have a better proposal what to write
