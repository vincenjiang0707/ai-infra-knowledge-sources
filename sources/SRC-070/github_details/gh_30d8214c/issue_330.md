# [Issue #330] [SM100/B300][BF16] bf16_gemm_nt failure with prebuilt wheel, fixed by rebuilding against current PyTorch

source: https://github.com/deepseek-ai/DeepGEMM/issues/330
state: closed | updated: 2026-05-09T22:36:29Z
labels: 

## 正文

Hi DeepGEMM team,

We hit a failure on B300/SM100 in the BF16 dense GEMM path that initially looked like an SM100 `bf16_gemm_nt` issue. After narrowing it down, the current evidence points more specifically at binary wheel / PyTorch build compatibility: the failure happens with a prebuilt DeepGEMM wheel in one PyTorch 2.11 environment, but rebuilding DeepGEMM from the same public commit against that exact PyTorch install fixes it.

I am filing this mainly to ask whether this is expected, and whether the install/docs should explicitly call out that the `deep_gemm._C` extension must be rebuilt whenever the PyTorch build changes.

## Failing environment

Observed on:

```text
GPU: NVIDIA B300 SXM6 AC
CUDA capability: (10, 3)
Host driver: 590.48.01
Python: 3.12.3
torch: 2.11.0
torch CUDA: 13.0
torch git: 70d99e998b4955e0049d13a98d77ae1b14db1f45
deep_gemm: 2.5.0+891d57b
DeepGEMM commit: 891d57b4db1071624b5c8fa0d1e51cb317fa709f
```

The container image for the failing environment is internal, so I cannot share it directly. It has a preinstalled `deep_gemm` wheel.

## Failure

A direct call to:

```python
deep_gemm.bf16_gemm_nt(a, b, d)
```

can fail with:

```text
RuntimeError: Cannot access data pointer of Tensor that doesn't have storage
```

With `TORCH_SHOW_CPP_STACKTRACES=1`, the C++ stack pointed into the BF16 dense path and the output TMA descriptor construction:

```text
deep_gemm::gemm::bf16_gemm_nt(...)
.../DeepGEMM/csrc/jit_kernels/impls/runtime_utils.hpp:238
```

The tensors are ordinary contiguous CUDA tensors, and Python can read their `data_ptr()` values immediately before the DeepGEMM call.

Representative failing layout:

```text
a.shape = (1, 5120)
a.stride = (5120, 1)
a.is_contiguous = True

a.shape storage_offset = 0

b.shape = (6144, 5120)
b.stride = (5120, 1)
b.is_contiguous = True
b.storage_offset = 0

d.shape = (1, 6144)
d.stride = (6144, 1)
d.is_contiguous = True
d.storage_offset = 0
```

## Repro script pattern

```python
import torch
import deep_gemm

torch.cuda.set_device(0)
torch.manual_seed(0)

m, n, k = 1, 6144, 5120

for i in range(100):
    a = torch.randn((m, k), device="cuda", dtype=torch.bfloat16)
    b = torch.randn((n, k), device="cuda", dtype=torch.bfloat16)
    d = torch.empty((m, n), device="cuda", dtype=torch.bfloat16)

    print(
        "iter", i,
        "a", tuple(a.shape), tuple(a.stride()), a.is_contiguous(), a.storage_offset(), hex(a.data_ptr()),
        "b", tuple(b.shape), tuple(b.stride()), b.is_contiguous(), b.storage_offset(), hex(b.data_ptr()),
        "d", tuple(d.shape), tuple(d.stride()), d.is_contiguous(), d.storage_offset(), hex(d.data_ptr()),
        flush=True,
    )

    deep_gemm.bf16_gemm_nt(a, b, d)
    torch.cuda.synchronize()
```

## What passes

The same script passes when DeepGEMM is rebuilt from source at the same commit against the current PyTorch install:

```bash
git clone --recursive https://github.com/deepseek-ai/DeepGEMM.git
cd DeepGEMM
git checkout 891d57b4db1071624b5c8fa0d1e51cb317fa709f
git submodule update --init --recursive
./install.sh
```

After rebuilding from source in the same PyTorch 2.11 / CUDA 13.0 / B300 environment, the script above passed 100/100 iterations.

We also tested public NGC images with source-built DeepGEMM at the same commit:

```text
nvcr.io/nvidia/pytorch:25.10-py3
PyTorch: 2.9.0a0+145a3a7bda.nv25.10
CUDA: 13.0
GPU: B300, capability (10, 3)
Result: passed 100/100 iterations
```

```text
nvcr.io/nvidia/pytorch:26.03-py3
PyTorch: 2.11.0a0+a6c236b9fd.nv26.03.46836102
CUDA: 13.2
GPU: B300, capability (10, 3)
Result: passed 100/100 iterations
```

## Question

Is it expected that a DeepGEMM wheel built against one PyTorch build can fail this way when loaded under a different PyTorch build, even when the DeepGEMM commit and CUDA major version are otherwise compatible?

If yes, it may be useful to document this more explicitly around installation/redeployment of DeepGEMM wheels, especially for SM100/BF16 users. The observed failure mode is confusing because it surfaces as a host-side `Tensor` storage/data pointer error while constructing the TMA descriptor, rather than as a clean extension ABI/version error.

Thanks.


## 评论 (1)

### benjibc · 2026-05-09

Follow-up: after further testing, this appears to be a downstream packaging issue on our side rather than a DeepGEMM SM100/BF16 correctness bug. Rebuilding DeepGEMM from source at the same commit against the exact PyTorch build in the affected image makes the fresh-allocation BF16 repro pass. Public NGC 25.10 and 26.03 images with source-built DeepGEMM also pass. Closing this to avoid noise; the actionable fix is for our image build to rebuild/reinstall deep_gemm after rebuilding PyTorch.
