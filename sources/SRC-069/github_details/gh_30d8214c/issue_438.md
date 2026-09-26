# [Issue #438] Build fails with __nv_fp8_e4m3 undefined (CUDA 12.9, H100 and B200)

source: https://github.com/deepseek-ai/DeepGEMM/issues/438
state: closed | updated: 2026-09-11T21:07:22Z
labels: 

## 正文

# Build fails with `__nv_fp8_e4m3` undefined (CUDA 12.9, H100 and B200)

I'm trying to benchmark `mega_mhc`. This is the new code that landed in [#432](https://github.com/deepseek-ai/DeepGEMM/pull/432) on September 10.

Building DeepGEMM at `66081d4` with `bash ./develop.sh` fails with:

```text
deep_gemm/include/deep_gemm/layout/mega_mhc.cuh:64:5: error: ‘__nv_fp8_e4m3’ does not name a type
   64 |     __nv_fp8_e4m3* y_fp8;
      |     ^~~~~~~~~~~~~
```

The host build never includes `cuda_fp8.h` because CUTLASS gates it behind `CUDA_FP8_ENABLED`, which requires `__CUDACC_VER_*` - undefined in host g++.

Since this is host compilation, the attached GPU shouldn't matter; I tested both to confirm. The same error occurs with stock PyTorch on H100 and B200, and with NGC PyTorch on H100. Host g++ fails while compiling `csrc/python_api.cpp`, before any GPU kernels run.

| | NGC / H100 | Stock / H100 | Stock / B200 |
|---|---|---|---|
| Image | `nvcr.io/nvidia/pytorch:25.06-py3` | `pytorch/pytorch:2.8.0-cuda12.9-cudnn9-devel` | Same stock image |
| PyTorch | `2.8.0a0+5228986c39.nv25.06` | `2.8.0+cu129` | `2.8.0+cu129` |
| Python | 3.12 | 3.11 | 3.11 |
| nvcc | 12.9.86 | 12.9.86 | 12.9.86 |
| g++ | 13.3.0 | 13.4.0 | 13.4.0 |
| GPU architecture | SM90 | SM90 | SM100, capability `(10, 0)` |
| Driver | 580.95.05 | 580.95.05 | 580.95.05 |

The containers have `libdw-dev`, `elfutils`, `libelf-dev`, `git`, and `build-essential`.

I checked the submodules against the pinned commits; neither has drifted:

```text
 f3fde58372d33e9a5650ba7b80fc48b3b49d40c8 third-party/cutlass (v4.2.1)
 e5bdee2bc4ca519eba00cfc5f0c6e950e6a96a16 third-party/deep_jit (e5bdee2)
```

To reproduce inside the container:

```sh
git clone --recursive https://github.com/deepseek-ai/DeepGEMM.git
cd DeepGEMM
git checkout 66081d4c9c7d7c44f13fea402e5b622aa0f409c2
git submodule update --init --recursive
git submodule status --recursive
git -C third-party/cutlass log -1
bash ./develop.sh
```

The include chain looks like the problem. [`mega_mhc.cuh`](https://github.com/deepseek-ai/DeepGEMM/blob/66081d4c9c7d7c44f13fea402e5b622aa0f409c2/deep_gemm/include/deep_gemm/layout/mega_mhc.cuh#L3-L5) includes [`common/math.cuh`](https://github.com/deepseek-ai/DeepGEMM/blob/66081d4c9c7d7c44f13fea402e5b622aa0f409c2/deep_gemm/include/deep_gemm/common/math.cuh#L3-L8), which includes CUTLASS's [`numeric_types.h`](https://github.com/NVIDIA/cutlass/blob/f3fde58372d33e9a5650ba7b80fc48b3b49d40c8/include/cutlass/numeric_types.h#L39-L48), then `float8.h`.

In the pinned CUTLASS, [`CUDA_FP8_ENABLED`](https://github.com/NVIDIA/cutlass/blob/f3fde58372d33e9a5650ba7b80fc48b3b49d40c8/include/cutlass/float8.h#L43-L46) depends on `__CUDACC_VER_MAJOR__` / `__CUDACC_VER_MINOR__`. The [`cuda_fp8.h` include](https://github.com/NVIDIA/cutlass/blob/f3fde58372d33e9a5650ba7b80fc48b3b49d40c8/include/cutlass/float8.h#L94-L97) is guarded by `CUDA_FP8_ENABLED`. Those macros aren't defined in this host build. The NGC preprocessor trace (`-E -H -dD`) contains CUTLASS's `float8.h`, but no `cuda_fp8.h` or declaration of `__nv_fp8_e4m3`.

The CUDA header is installed, and this standalone test passes with the host compilers in all three environments:

```cpp
#include <cuda_fp8.h>
static_assert(sizeof(__nv_fp8_e4m3) == 1);
```

```sh
g++ -std=c++20 -I/usr/local/cuda/include -fsyntax-only standalone-fp8-control.cpp
```

For the stock GCC 13 runs, the compiler was `/usr/bin/g++-13`. NGC used `x86_64-linux-gnu-g++` with the snippet on stdin. `/usr/local/cuda` resolves to `/usr/local/cuda-12.9`; the compiler paths point to that toolkit. The NGC preprocessed headers report `CUDA_VERSION` and `CUDART_VERSION` as `12090`.

I haven't patched DeepGEMM or forced an include, so the standalone test doesn't establish whether that would fix the whole build. Neither the Hopper test nor `test_mega_mhc.py` was reached.

Should `mega_mhc.cuh` include `cuda_fp8.h` directly?

<details>
<summary>Full compiler commands</summary>

NGC command that reaches the FP8 error:

```sh
x86_64-linux-gnu-g++ -fno-strict-overflow -Wsign-compare -DNDEBUG -g -O2 -Wall -fPIC -I/usr/local/cuda/include -I/usr/local/cuda/include/cccl -Ideep_gemm/include -Ithird-party/deep_jit/include -Ithird-party/cutlass/include -I/usr/local/lib/python3.12/dist-packages/torch/include -I/usr/local/lib/python3.12/dist-packages/torch/include/torch/csrc/api/include -I/usr/local/cuda/include -I/usr/include/python3.12 -c csrc/python_api.cpp -o build/temp.linux-x86_64-cpython-312/csrc/python_api.o -std=c++20 -O3 -fPIC -Wno-psabi -Wno-deprecated-declarations -D_GLIBCXX_USE_CXX11_ABI=1
```

Stock GCC 13 command that reaches the same FP8 error on both H100 and B200:

```sh
/usr/bin/g++-13 -DNDEBUG -fwrapv -O2 -Wall -fPIC -O2 -isystem /opt/conda/include -fPIC -O2 -isystem /opt/conda/include -fPIC -I/usr/local/cuda/include -I/usr/local/cuda/include/cccl -Ideep_gemm/include -Ithird-party/deep_jit/include -Ithird-party/cutlass/include -I/opt/conda/lib/python3.11/site-packages/torch/include -I/opt/conda/lib/python3.11/site-packages/torch/include/torch/csrc/api/include -I/usr/local/cuda/include -I/opt/conda/include/python3.11 -c csrc/python_api.cpp -o build/temp.linux-x86_64-cpython-311/csrc/python_api.o -std=c++20 -O3 -fPIC -Wno-psabi -Wno-deprecated-declarations -D_GLIBCXX_USE_CXX11_ABI=1
```

</details>

<details>
<summary>Stock Modal image definition</summary>

GCC 13 supplies the `<format>` support missing from stock GCC 11; `CC` and `CXX` select it below.

```python
import modal

image = (
    modal.Image.from_registry("pytorch/pytorch:2.8.0-cuda12.9-cudnn9-devel")
    .apt_install("libdw-dev", "elfutils", "libelf-dev", "git", "build-essential")
    .apt_install("software-properties-common")
    .run_commands(
        "add-apt-repository -y ppa:ubuntu-toolchain-r/test",
        "apt-get update && apt-get install -y --no-install-recommends gcc-13 g++-13 && rm -rf /var/lib/apt/lists/*",
    )
    .env({"CC": "/usr/bin/gcc-13", "CXX": "/usr/bin/g++-13"})
)
```

The stock base image digest was `sha256:cf5aa3f7045a68c10d80f546746591c5ccae6a33729e5e32625ff76bd2c036fe` (linux/amd64).

</details>


## 评论 (4)

### MARD1NO · 2026-09-11

Also meet this problem, 

add #include <cuda_fp8.h> in deep_gemm/include/deep_gemm/layout/mega_mhc.cuh

### XFDG · 2026-09-11

Hi maintainers, I've submitted a fix in #439.

The root cause: `mega_mhc.cuh` uses `__nv_fp8_e4m3` in `NormArgs`, which is compiled by host g++ via `csrc/python_api.cpp`. CUTLASS gates `cuda_fp8.h` behind `CUDA_FP8_ENABLED` (which requires `__CUDACC_VER_*", defined only by nvcc), so the type is invisible to g++ during host compilation.

The fix adds an explicit `#include <cuda_fp8.h>` at the top of `mega_mhc.cuh`, before any other includes. Verified to build on B200 (SM100, CUDA 13.1, gcc-13).

### XFDG · 2026-09-11

Hi, I've submitted a fix in https://github.com/deepseek-ai/DeepGEMM/pull/439.

Verified on B200 (SM100, CUDA 13.1, gcc-13): `bash ./develop.sh` completes without errors and `import deep_gemm` works correctly. Let me know if you'd like any changes.

### Sarose550 · 2026-09-11

Which TileKernels revision does `test_mega_mhc` expect?
