# [Issue #1778] Reduce CUDA build matrix

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1778
state: closed | updated: 2026-06-22T22:27:48Z
labels: Build, CUDA

## 正文

We currently build and package with our kernels built against the following versions of the CUDA Toolkit on all supported platforms:
* 11.8
* 12.0, 12.1, 12.2, 12.3, 12.4, 12.5, 12.6, 12.8, 12.9
* 13.0, 13.2

This adds excessive size to our wheels, along with excessive build times.

By default we try to load the binary built with the same CUDA Toolkit version as the user's PyTorch build, but this can be overriden with the `BNB_CUDA_VERSION` env variable.

Let's align better with the official PyTorch wheels, as these will be the most commonly used. We currently support PyTorch 2.4+ on CUDA. The bold entries in the table below represent the default from PyPI.

| PyTorch Version | CUDA Toolkit Versions |
|--------|--------|
| 2.12 | [12.6, **13.0**, 13.2](https://github.com/pytorch/pytorch/issues/178665) |
| 2.11  | [12.6, 12.8, **13.0**](https://github.com/pytorch/pytorch/pull/175253) |
| 2.10  | [12.6, **12.8**, 13.0](https://github.com/pytorch/pytorch/issues/165111)|
| 2.9 | 12.6, **12.8**, 13.0 |
| 2.8 | 12.6, **12.8**, 12.9 |
| 2.7 | 11.8, **12.6**, 12.8 |
| 2.6 | [11.8, **12.4**, 12.6](https://github.com/pytorch/pytorch/issues/138609) | 
| 2.5 | 11.8, **12.1**, 12.4 |
| 2.4 | 11.8, **12.1**, 12.4 |

We would remove at least 4 of our 11 builds: CUDA 12.0, 12.2, 12.3, 12.5. When users happen to run a PyTorch built against a CUDA version without a matching BNB build available in their installation, we should then fallback to load the closest matching build version of bitsandbytes found, restricted to major CUDA version. We would first search for a compatible minor version lower than the PyTorch version, before moving on to minor versions above the PyTorch version. The `BNB_CUDA_VERSION` override would still supersede this.

| PyTorch CUDA | BNB Fallback Priority |
|----------------|-----------|
| 11.8 | - |
| 12.0 | 12.1, 12.2, ..., 12.9 |
| 12.1 | 12.0, 12.2, 12.3, ..., 12.9 |
| 12.2 | 12.1, 12.0, 12.3, ..., 12.9 |
| 12.3 | 12.2, 12.1, 12.0, 12.4, 12.5, ..., 12.9 |
| 12.4 | 12.3, 12.2, 12.1, 12.0, 12.5, ..., 12.9 |
| 12.5 | 12.4, 12.3, ..., 12.0, 12.6, 12.8, 12.9 |
| 12.6 | 12.5, 12.4, ..., 12.0, 12.8, 12.9 |
| 12.8 | 12.6, 12.5, ..., 12.0, 12.9 |
| 12.9 | 12.8, 12.6, ..., 12.0 |
| 13.0 | 13.1, 13.2, ... |
| 13.1 | 13.0, 13.2, ... |
| 13.3 | 13.2, 13.1, 13.0, ... |


## 评论 (1)

### matthewdouglas · 2025-12-09

#1820 and #1827 have reduced the build size, along #1819 on the ROCm side.

We're currently at 171.6 MiB for the unpacked Linux x86-64 wheel. Removing CUDA 12.0/12.2/12.4/12.5 builds will reduce by 62.4 MiB. Proportionally the savings calculation doesn't change, but we've improved by 18% elsewhere.

