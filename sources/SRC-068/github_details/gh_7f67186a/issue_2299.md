# [Issue #2299] [Wheel] Pre-built flash-attn 2.8.3 for CUDA 12 + PyTorch 2.10 (Python 3.12)

source: https://github.com/Dao-AILab/flash-attention/issues/2299
state: open | updated: 2026-07-03T10:14:47Z
labels: 

## 正文

Since there is no official pre-built wheel for PyTorch 2.10 (related: #2248, #2267), I built one using a Docker sandbox.

## Download

**[flash_attn-2.8.3+cu12torch2.10cxx11abiTRUE-cp312-cp312-linux_x86_64.whl](https://github.com/lesj0610/flash-attention/releases/download/v2.8.3-cu12-torch2.10-cp312/flash_attn-2.8.3%2Bcu12torch2.10cxx11abiTRUE-cp312-cp312-linux_x86_64.whl)**

```bash
pip install "https://github.com/lesj0610/flash-attention/releases/download/v2.8.3-cu12-torch2.10-cp312/flash_attn-2.8.3%2Bcu12torch2.10cxx11abiTRUE-cp312-cp312-linux_x86_64.whl"
```

## Build environment

| | |
|---|---|
| flash-attention | v2.8.3 |
| CUDA | 12.8 |
| PyTorch | 2.10 (stable) |
| Python | 3.12 |
| CXX11 ABI | TRUE |
| OS | Ubuntu 24.04 |

## Reproducible build (Docker)

<details>
<summary>Click to expand</summary>

```bash
mkdir -p ~/flash_attn_wheel_factory

docker run --rm --gpus all \
  -v ~/flash_attn_wheel_factory:/output \
  nvidia/cuda:12.8.0-devel-ubuntu24.04 /bin/bash -c '
    apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
      curl git build-essential python3.12 python3.12-venv python3.12-dev tzdata

    curl -LsSf https://astral.sh/uv/install.sh | env UV_UNMANAGED_INSTALL="/usr/local/bin" sh
    /usr/local/bin/uv venv --seed /tmp/build_env --python 3.12
    source /tmp/build_env/bin/activate

    uv pip install torch ninja packaging wheel

    export MAX_JOBS=4
    export FLASH_ATTENTION_FORCE_BUILD=TRUE
    export FLASH_ATTENTION_FORCE_CXX11_ABI=TRUE

    pip wheel --no-build-isolation \
      git+https://github.com/Dao-AILab/flash-attention.git@v2.8.3
    cp /tmp/flash_attn*.whl /output/
  '
```

</details>

## 评论 (9)

### qingxial · 2026-03-03

may i ask could torch 2.9.1 use this wheel with home cuda 12.4 and cuda in torch 12.8

### lesj0610 · 2026-03-03

This wheel is built specifically for **PyTorch 2.10** and is **not compatible** with PyTorch 2.9.1.

The good news is that you don't need a custom wheel — the official release already includes a pre-built wheel for PyTorch 2.9:

**[flash_attn-2.8.3+cu12torch2.9cxx11abiTRUE-cp312-cp312-linux_x86_64.whl](https://github.com/Dao-AILab/flash-attention/releases/tag/v2.8.3)**

```bash
pip install flash-attn --no-build-isolation
```

Or install directly from the official release page:
https://github.com/Dao-AILab/flash-attention/releases/tag/v2.8.3

> Regarding your CUDA question: the `cu12` tag in the wheel name covers the CUDA 12.x family, so CUDA 12.4 on your system is fine.

### Camellia-hz · 2026-03-26

@lesj0610 Hello, thank you for sharing. I have a small request. My current Python environment is 3.11. Could you please provide a version that supports Flash Attn 2.8.3 + Torch 2.10.0 + Python 3.11? Thank you very much!

### Chivenh · 2026-04-08

> Since there is no official pre-built wheel for PyTorch 2.10 (related: [#2248](https://github.com/Dao-AILab/flash-attention/issues/2248), [#2267](https://github.com/Dao-AILab/flash-attention/issues/2267)), I built one using a Docker sandbox.
> 
> ## Download
> **[flash_attn-2.8.3+cu12torch2.10cxx11abiTRUE-cp312-cp312-linux_x86_64.whl](https://github.com/lesj0610/flash-attention/releases/download/v2.8.3-cu12-torch2.10-cp312/flash_attn-2.8.3%2Bcu12torch2.10cxx11abiTRUE-cp312-cp312-linux_x86_64.whl)**
> 
> pip install "https://github.com/lesj0610/flash-attention/releases/download/v2.8.3-cu12-torch2.10-cp312/flash_attn-2.8.3%2Bcu12torch2.10cxx11abiTRUE-cp312-cp312-linux_x86_64.whl"
> ## Build environment
> flash-attention	v2.8.3
> CUDA	12.8
> PyTorch	2.10 (stable)
> Python	3.12
> CXX11 ABI	TRUE
> OS	Ubuntu 24.04
> ## Reproducible build (Docker)
> Click to expand

Does it support CUDA 12.9?

### lesj0610 · 2026-04-08

Yes, it should work on CUDA 12.9.

The wheel was compiled against CUDA 12.8, but CUDA maintains forward compatibility within the same major version — binaries built for 12.8 can run on 12.9 without issue, as long as your driver supports CUDA 12.9.

Also, the `cu12` tag in the wheel name covers the entire CUDA 12.x family, so CUDA 12.9 is within the supported range.

If you run into any issues, feel free to let me know.

### tartarleft · 2026-04-11

Hi, is there a version for cu12torch2.10 and  python 3.10 like flash_attn-2.8.3+cu12torch2.10cxx11abiTRUE-cp310-cp310-linux_x86_64.whl?

### NTvan24 · 2026-05-06

Hi, is there a version for cu12torch2.10 and python 3.11 ? 

### llly1234 · 2026-06-15

> 是的，它应该能在CUDA 12.9上运行。
> 
> 该轮子是基于CUDA 12.8编译的，但CUDA在同一主要版本内保持前向兼容性——为12.8编写的二进制文件可以在12.9上运行，只要你的驱动支持CUDA 12.9。
> 
> 此外，轮名中的标签涵盖了整个CUDA 12.x系列，因此CUDA 12.9在支持范围内。`cu12`
> 
> 如果你遇到任何问题，随时告诉我。

请问一下有3.11的版本么

### NoviceStone · 2026-07-03

Hi, is there a version for CUDA 12.x + PyTorch 2.10 and python 3.13 ?
