# [Issue #2425] [Wheel] Pre-built flash-attn 2.8.3 for CUDA 12 + PyTorch 2.11 (Python 3.10-3.13)

source: https://github.com/Dao-AILab/flash-attention/issues/2425
state: open | updated: 2026-07-30T09:20:54Z
labels: 

## 正文

Since there is no official pre-built wheel for PyTorch 2.11 (related: #2299), I built Docker-based wheels and uploaded them to a fork release.

Release page: [v2.8.3-cu12-torch2.11](https://github.com/lesj0610/flash-attention/releases/tag/v2.8.3-cu12-torch2.11)

## Download

- **Python 3.10**: [flash_attn-2.8.3+cu12torch2.11cxx11abiTRUE-cp310-cp310-linux_x86_64.whl](https://github.com/lesj0610/flash-attention/releases/download/v2.8.3-cu12-torch2.11/flash_attn-2.8.3%2Bcu12torch2.11cxx11abiTRUE-cp310-cp310-linux_x86_64.whl)
- **Python 3.11**: [flash_attn-2.8.3+cu12torch2.11cxx11abiTRUE-cp311-cp311-linux_x86_64.whl](https://github.com/lesj0610/flash-attention/releases/download/v2.8.3-cu12-torch2.11/flash_attn-2.8.3%2Bcu12torch2.11cxx11abiTRUE-cp311-cp311-linux_x86_64.whl)
- **Python 3.12**: [flash_attn-2.8.3+cu12torch2.11cxx11abiTRUE-cp312-cp312-linux_x86_64.whl](https://github.com/lesj0610/flash-attention/releases/download/v2.8.3-cu12-torch2.11/flash_attn-2.8.3%2Bcu12torch2.11cxx11abiTRUE-cp312-cp312-linux_x86_64.whl)
- **Python 3.13**: [flash_attn-2.8.3+cu12torch2.11cxx11abiTRUE-cp313-cp313-linux_x86_64.whl](https://github.com/lesj0610/flash-attention/releases/download/v2.8.3-cu12-torch2.11/flash_attn-2.8.3%2Bcu12torch2.11cxx11abiTRUE-cp313-cp313-linux_x86_64.whl)

Example:

```bash
pip install "https://github.com/lesj0610/flash-attention/releases/download/v2.8.3-cu12-torch2.11/flash_attn-2.8.3%2Bcu12torch2.11cxx11abiTRUE-cp312-cp312-linux_x86_64.whl"
```

## Build environment

| | |
|---|---|
| flash-attention | v2.8.3 |
| CUDA | 12.8 |
| PyTorch | 2.11 (stable) |
| Python | 3.10, 3.11, 3.12, 3.13 |
| CXX11 ABI | TRUE |
| OS | Ubuntu 24.04 |

## Notes

- Community build only.
- Python 3.9 is not included because upstream `torch 2.11.0+cu128` does not publish Linux x86_64 `cp39` wheels.


## 评论 (7)

### HelloWorldLTY · 2026-04-03

Thank you! Can we use torch 2.12 + cuda12.9 for this wheel?

### lesj0610 · 2026-04-03

> Thank you! Can we use torch 2.12 + cuda12.9 for this wheel?

only ensures that it works in the version described

### TianHongZXY · 2026-04-16

Could you provide wheels built for aarch64? Thanks in advance!

### kaka-Cao · 2026-04-19

i use py3.11, which vllm version shuold i choose? and why no py3.11 with torch2.10? thanks!

### remixer-dec · 2026-04-28

I'm getting ImportError: site-packages/flash_attn_2_cuda.cpython-311-x86_64-linux-gnu.so: undefined symbol: _ZN3c104cuda29c10_cuda_check_implementationEiPKcS2_jb on CUDA 12.8

UPD: oh, this build is for Pytorch 2.11 and I need 2.9 and nobody has built it in this config... #2212 what a time to be alive

### Apprisco · 2026-06-09

Why not cuda 13 btw?

### EthanJi29 · 2026-07-30

i love you bro
