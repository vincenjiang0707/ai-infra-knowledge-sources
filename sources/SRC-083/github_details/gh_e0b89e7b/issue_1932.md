# [Issue #1932] [Intel XPU] `gemv_4bit` with NF4 has huge `bfloat16` error compared with `float16` on Intel Arc A770

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1932
state: closed | updated: 2026-05-08T02:05:39Z
labels: Intel

## 正文

### System Info

- OS: `Windows 11 Pro 25H2 26200`
- GPU: `Intel(R) Arc(TM) A770 Graphics`
- GPU driver: `32.0.101.8509`
- Python: `3.13.11`
- PyTorch: `2.11.0+xpu`
- bitsandbytes: `0.49.2`
- triton-xpu: `3.7.0`
- intel-sycl-rt: `2025.3.2`
- intel-opencl-rt: `2025.3.2`
- dpcpp-cpp-rt: `2025.3.2`
- numpy: `2.4.3`

### Reproduction

This reproducer does not require any model files. It uses random tensors only.

It compares `bitsandbytes.functional.gemv_4bit(...)` against a reference computed from the same quantized weights after `dequantize_4bit(...)`.

```python
import bitsandbytes as bnb
import bitsandbytes.functional as F
import torch

SEED = 1234
OUT_FEATURES = 2048
IN_FEATURES = 512
QUANT_TYPE = "nf4"
DEVICE = "xpu:0"

torch.manual_seed(SEED)
assert hasattr(torch, "xpu") and torch.xpu.is_available()

print(f"torch={torch.__version__}")
print(f"bitsandbytes={bnb.__version__}")
print(f"device={DEVICE}")
print(f"device_name={torch.xpu.get_device_name(0)}")

weight = torch.randn(OUT_FEATURES, IN_FEATURES, device=DEVICE, dtype=torch.float32)
qweight, qstate = F.quantize_4bit(weight, quant_type=QUANT_TYPE, compress_statistics=True)

x = torch.randn(1, IN_FEATURES, device=DEVICE, dtype=torch.float32)
dequantized_weight = F.dequantize_4bit(qweight, quant_state=qstate, quant_type=QUANT_TYPE).to(torch.float32)
reference = x @ dequantized_weight.t()

for dtype in (torch.float16, torch.bfloat16):
    out = F.gemv_4bit(x.to(dtype), qweight, state=qstate).to(torch.float32)
    mae = (out - reference).abs().mean().item()
    maxe = (out - reference).abs().max().item()
    print(f"{dtype}: gemv_4bit mae={mae:.6f}, max_error={maxe:.6f}")
```

Observed output on my machine:

```text
torch=2.11.0+xpu
bitsandbytes=0.49.2
device=xpu:0
device_name=Intel(R) Arc(TM) A770 Graphics
torch.float16: gemv_4bit mae=0.008388, max_error=0.041985
torch.bfloat16: gemv_4bit mae=12.890043, max_error=53.826134
```

This same issue also shows up at the model level when using `bnb_4bit_compute_dtype=torch.bfloat16` for NF4 inference on XPU. `torch.float16` gives correct outputs in the same environment, while `torch.bfloat16` degrades badly.

### Expected behavior

`torch.bfloat16` should have comparable numerical error to `torch.float16` for the same NF4 `gemv_4bit` operation on XPU, or at least remain in the same order of magnitude.

Instead, on this system, `bfloat16` error is more than three orders of magnitude larger than `float16` against the same dequantized reference.

At the model level, I would expect `bnb_4bit_compute_dtype=torch.bfloat16` to remain usable for XPU inference rather than producing severely degraded generation quality.

# Possible root cause

This looks specific to the XPU fast GEMV path rather than generic NF4 quantization/dequantization.

Some evidence that may help triage:

- `bitsandbytes.autograd._functions.matmul_4bit(...)` routes single-vector inference through `F.gemv_4bit(...)`, which is the path hit during decode.
- In `bitsandbytes/csrc/xpu_kernels.cpp`, `kgemv_4bit_inference` first materializes the dequantized lookup values into template type `T` and also loads activations into `T`.
- The inner loop then does `local_C += (float)(local_A[k] * local_B[k]);`, so the multiply appears to happen in `T` before promotion to `float`.
- That means `bfloat16` loses precision before accumulation, which matches the repro: `float16` stays accurate, while `bfloat16` becomes unusable on the same quantized weights.

I also tested a slower reference path (`dequantize_4bit(...)` followed by normal matmul), and that path did not show the same dramatic `bfloat16` failure. That suggests the issue is likely in the XPU `gemv_4bit` kernel itself, not in NF4 serialization or basic dequantization.

## 评论 (13)

### matthewdouglas · 2026-04-28

For reference, when I run this on RTX 4090:

```
torch=2.10.0+cu130
bitsandbytes=0.50.0.dev0
device=cuda:0
device_name=NVIDIA GeForce RTX 4090
torch.float16: gemv_4bit mae=0.008759, max_error=0.055462
torch.bfloat16: gemv_4bit mae=0.068209, max_error=0.342186
```

The SYCL kernel for GEMV is a lot like the CUDA kernel - so it might not really explain everything here. On Ampere+ it will also do the LUT and scale multiplication in bf16, then use fp32 for accumulation. So it's true that bf16 error should be higher than fp16, but not to the degree you're seeing on XPU.

I notice on XPU we also have a Triton path. Can you help confirm which path you're going down? E.g. renaming libbitsandbytes_xpu.dll temporarily should force down the Triton path for comparison.

cc: @jiqing-feng 

### Blackwood416 · 2026-04-28

> For reference, when I run this on RTX 4090:
> 
> ```
> torch=2.10.0+cu130
> bitsandbytes=0.50.0.dev0
> device=cuda:0
> device_name=NVIDIA GeForce RTX 4090
> torch.float16: gemv_4bit mae=0.008759, max_error=0.055462
> torch.bfloat16: gemv_4bit mae=0.068209, max_error=0.342186
> ```
> 
> The SYCL kernel for GEMV is a lot like the CUDA kernel - so it might not really explain everything here. On Ampere+ it will also do the LUT and scale multiplication in bf16, then use fp32 for accumulation. So it's true that bf16 error should be higher than fp16, but not to the degree you're seeing on XPU.
> 
> I notice on XPU we also have a Triton path. Can you help confirm which path you're going down? E.g. renaming libbitsandbytes_xpu.dll temporarily should force down the Triton path for comparison.
> 
> cc: [@jiqing-feng](https://github.com/jiqing-feng)

I tried the Triton path you mentioned and the result is normal. So this issue only appears in the certain SYCL kernel. Feel free to tell me if you need more test results.

```
torch=2.11.0+xpu
bitsandbytes=0.49.2
device=xpu:0
device_name=Intel(R) Arc(TM) A770 Graphics
torch.float16: gemv_4bit mae=0.006299, max_error=0.030600
torch.bfloat16: gemv_4bit mae=0.048875, max_error=0.245483
```

### jiqing-feng · 2026-04-29

Will check it soon.

### jiqing-feng · 2026-04-30

Verified Arc B60 and PVC 1550 is okay:
```
torch=2.11.0+xpu
bitsandbytes=0.49.2
device=xpu:0
device_name=Intel(R) Arc(TM) Pro B60 Graphics
/opt/venv/lib/python3.12/site-packages/bitsandbytes/backends/triton/ops.py:70: FutureWarning: _check_is_size will be removed in a future PyTorch release along with guard_size_oblivious.     Use _check(i >= 0) instead.
  torch._check_is_size(blocksize)
/opt/venv/lib/python3.12/site-packages/bitsandbytes/backends/triton/ops.py:18: FutureWarning: _check_is_size will be removed in a future PyTorch release along with guard_size_oblivious.     Use _check(i >= 0) instead.
  torch._check_is_size(blocksize)
torch.float16: gemv_4bit mae=0.009032, max_error=0.038576
torch.bfloat16: gemv_4bit mae=0.071656, max_error=0.346130
```

```
torch=2.11.0+xpu
bitsandbytes=0.49.2
device=xpu:0
device_name=Intel(R) Data Center GPU Max 1550
/opt/venv/lib/python3.12/site-packages/bitsandbytes/backends/triton/ops.py:70: FutureWarning: _check_is_size will be removed in a future PyTorch release along with guard_size_oblivious.     Use _check(i >= 0) instead.
  torch._check_is_size(blocksize)
/opt/venv/lib/python3.12/site-packages/bitsandbytes/backends/triton/ops.py:18: FutureWarning: _check_is_size will be removed in a future PyTorch release along with guard_size_oblivious.     Use _check(i >= 0) instead.
  torch._check_is_size(blocksize)
torch.float16: gemv_4bit mae=0.008388, max_error=0.041992
torch.bfloat16: gemv_4bit mae=0.067275, max_error=0.329460
```

The issue may happen from Windows. If would be great if I can log into your A770 node.

### Blackwood416 · 2026-04-30

> Verified Arc B60 and PVC 1550 is okay:
> ```
> torch=2.11.0+xpu
> bitsandbytes=0.49.2
> device=xpu:0
> device_name=Intel(R) Arc(TM) Pro B60 Graphics
> /opt/venv/lib/python3.12/site-packages/bitsandbytes/backends/triton/ops.py:70: FutureWarning: _check_is_size will be removed in a future PyTorch release along with guard_size_oblivious.     Use _check(i >= 0) instead.
>   torch._check_is_size(blocksize)
> /opt/venv/lib/python3.12/site-packages/bitsandbytes/backends/triton/ops.py:18: FutureWarning: _check_is_size will be removed in a future PyTorch release along with guard_size_oblivious.     Use _check(i >= 0) instead.
>   torch._check_is_size(blocksize)
> torch.float16: gemv_4bit mae=0.009032, max_error=0.038576
> torch.bfloat16: gemv_4bit mae=0.071656, max_error=0.346130
> ```
> 
> ```
> torch=2.11.0+xpu
> bitsandbytes=0.49.2
> device=xpu:0
> device_name=Intel(R) Data Center GPU Max 1550
> /opt/venv/lib/python3.12/site-packages/bitsandbytes/backends/triton/ops.py:70: FutureWarning: _check_is_size will be removed in a future PyTorch release along with guard_size_oblivious.     Use _check(i >= 0) instead.
>   torch._check_is_size(blocksize)
> /opt/venv/lib/python3.12/site-packages/bitsandbytes/backends/triton/ops.py:18: FutureWarning: _check_is_size will be removed in a future PyTorch release along with guard_size_oblivious.     Use _check(i >= 0) instead.
>   torch._check_is_size(blocksize)
> torch.float16: gemv_4bit mae=0.008388, max_error=0.041992
> torch.bfloat16: gemv_4bit mae=0.067275, max_error=0.329460
> ```
> 
> The issue may happen from Windows. If would be great if I can log into your A770 node.

Since I'm using a personal PC, setting up a direct SSH connection is a bit tricky as I can't guarantee the machine will be online when you're available. However, I’ve managed to reproduce this issue on Ubuntu 24.04, so it shouldn't be a Windows-specific problem. Other A770 users have also reported the same bug, which suggests it might be an issue unique to the Arc A-series.
![repro_on_ubuntu.png](https://github.com/user-attachments/assets/edc81e94-f333-42d4-9e93-7f4cb2e846dd)



### matthewdouglas · 2026-04-30

Interesting. A couple more asks if you don't mind:

* Can you try it with in_features being not a power of 2 (but still a multiple of 64), like 576 instead?
* Also try it with setting an env var: `IGC_DisableMixMode=1`

Do you have a reference pointing to other users with similar issues?

It sounds like this is going to be very specific to Alchemist hardware. I have a couple thoughts here but don't want to rush to judgement, but if it starts to look OK with either of these two changes, that'll help drive the direction to fix it I think.

### Blackwood416 · 2026-05-01

> Interesting. A couple more asks if you don't mind:
> 
> * Can you try it with in_features being not a power of 2 (but still a multiple of 64), like 576 instead?
> * Also try it with setting an env var: `IGC_DisableMixMode=1`
> 
> Do you have a reference pointing to other users with similar issues?
> 
> It sounds like this is going to be very specific to Alchemist hardware. I have a couple thoughts here but don't want to rush to judgement, but if it starts to look OK with either of these two changes, that'll help drive the direction to fix it I think.

I’ve tested both of your suggestions on Windows and Ubuntu. Regarding the IN_FEATURES adjustment, interestingly, it works fine at 256. 
![256_in_features.png](https://github.com/user-attachments/assets/0cfd419b-0782-4771-8c4b-5304bb521e3d)

However, the bug consistently recurs at 320 and above, and the `IGC_DisableMixMode=1` environment variable does not seem to have any effect.

![320_in_features.png](https://github.com/user-attachments/assets/2cc07f36-3484-49da-ade8-fd546b0dd0f2)


As for other A770 users, I asked people in an Intel GPU community to run the reproduction script; the results showed that the bug is stable on the A770, while the B580 operates normally.

### jiqing-feng · 2026-05-07

Hi @Blackwood416 . Do you still need me to debug it? If so, you can at the mate from Intel GPU community to see if we can work together cause I have no A770 node.

### matthewdouglas · 2026-05-07

If comfortable rebuilding from src to test I would consider changing xpu_kernels.h here:

https://github.com/bitsandbytes-foundation/bitsandbytes/blob/a57d8e27c23c9005fe8b032770aff86f2baf19c8/csrc/xpu_kernels.h#L25

With the addition of this attribute, so it is:
```c++
    [[sycl::reqd_sub_group_size(SUBG_SIZE)]]
    SYCL_EXTERNAL void operator()(sycl::nd_item<1> item) const;
```
Just a note on this: I think SUBG_SIZE in all instantiations is 32, kernel is assuming it will be, but in reality compiler can do what it wants. On A770 it might pick to 8 or 16 instead of 32, would guess because hw support for bf16 is different maybe. At minimum maybe @jiqing-feng you can help me understand if that sounds reasonable? Not familiar enough to know for sure but 256 as the cut off is a good hint it picked subgroup size of 8. At 256 dim there would be 8 active lanes (fits in any subgroup of 8/16/32). Above that you would have 8+ lanes needed, fine if subgroup actually was 32, but it probably isn't picking that, and the reduction step here seems to assume it is.

### jiqing-feng · 2026-05-07

I will check it once I got the A770 node.

### Blackwood416 · 2026-05-07

Hi @matthewdouglas ,

Thank you so much for the brilliant suggestion! I can confirm that your fix works perfectly.

I rebuilt from source with the `[[sycl::reqd_sub_group_size(SUBG_SIZE)]]` attribute added to `xpu_kernels.h`. Here are the results:

Reproduction Script: The standalone script now outputs correct values for bfloat16. The massive MAE/max_error spike when IN_FEATURES exceeds 256 is completely gone.

<img width="1920" height="1032" alt="Image" src="https://github.com/user-attachments/assets/35c64cd6-7389-4314-9e87-9824b9b9d747" />

Real Model Inference: I tested actual LLM inference on my Intel Arc A770, and the gibberish output issue is entirely resolved.

<img width="1920" height="1032" alt="Image" src="https://github.com/user-attachments/assets/7b53d4d4-0e1a-4fca-953e-73eda8222d3d" />

Your hypothesis was spot on. It seems the compiler was indeed silently picking a smaller subgroup size (likely 8) for bfloat16 on the A770, which broke the reduction assumption at higher dimensions. Enforcing the size at compile-time completely fixes the boundary condition breakdown.

It seems that this single-line modification can perfectly solve the issue. Let me know if you need me to run any further tests for a potential PR. @jiqing-feng 

### jiqing-feng · 2026-05-07

You can run `BNB_TEST_DEVICE="xpu" pytest tests` to make sure this change doesn't break anything. Please let me know if there is a PR on fixing it, I will check if it's okay for PVC and B60 for both functionality and performance. Thanks!

### Blackwood416 · 2026-05-07

Hi @jiqing-feng  and @matthewdouglas ,

I've completed the testing with the `[[sycl::reqd_sub_group_size(SUBG_SIZE)]]` fix on my Arc A770 by running `BNB_TEST_DEVICE="xpu" pytest tests` on Ubuntu 24.04, and the results are very positive:

1. Accuracy/Functionality: Tested on both the latest main commit and the recent releases commit. The fix passes significantly more tests(for the latest commit) and I can confirm there are no regressions（for the recent releases commit **f0e6ca3**) .

> [test_log_after_fix_latest_commit.txt](https://github.com/user-attachments/files/27488627/test_log_after_fix_latest_commit.txt)
> [test_log_before_fix_latest_commit.txt](https://github.com/user-attachments/files/27488630/test_log_before_fix_latest_commit.txt)
> [test_log_after_fix_commit_f0e6ca3.txt](https://github.com/user-attachments/files/27488629/test_log_after_fix_commit_f0e6ca3.txt)
> [test_log_before_fix_commit_f0e6ca3.txt](https://github.com/user-attachments/files/27488628/test_log_before_fix_commit_f0e6ca3.txt)

2. Performance: I ran micro-benchmarks for the `gemv_4bit` kernel using this script 
```python
import torch
import bitsandbytes.functional as F
import time

OUT_FEATURES = 4096
IN_FEATURES = 4096
QUANT_TYPE = "nf4"
DEVICE = "xpu:0"

print(f"Device: {torch.xpu.get_device_name(0)}")

weight = torch.randn(OUT_FEATURES, IN_FEATURES, device=DEVICE, dtype=torch.float32)
qweight, qstate = F.quantize_4bit(weight, quant_type=QUANT_TYPE, compress_statistics=True)

x_fp16 = torch.randn(1, IN_FEATURES, device=DEVICE, dtype=torch.float16)
x_bf16 = x_fp16.to(torch.bfloat16)

def benchmark_gemv(x_input, name, num_warmup=100, num_iters=1000):
    for _ in range(num_warmup):
        _ = F.gemv_4bit(x_input, qweight, state=qstate)
    torch.xpu.synchronize()
    
    start = time.perf_counter()
    for _ in range(num_iters):
        _ = F.gemv_4bit(x_input, qweight, state=qstate)
    torch.xpu.synchronize()
    end = time.perf_counter()
    
    avg_time = (end - start) / num_iters * 1000
    print(f"[{name}] Average time: {avg_time:.4f} ms")

benchmark_gemv(x_fp16, "FP16")
benchmark_gemv(x_bf16, "BF16")
```
and end-to-end token generation benchmark using the [script](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/main/benchmarking/xpu/inference_benchmark.py) in the repository(run with `--model-id Blackwood416/Qwen3-0.6B-BNB-NF4`). I can confirm there is no performance degradation for bfloat16 with this change enforced.

> [kernel_bench_after_fix_latest_commit.txt](https://github.com/user-attachments/files/27488785/kernel_bench_after_fix_latest_commit.txt)
> [kernel_bench_before_fix_latest_commit.txt](https://github.com/user-attachments/files/27488788/kernel_bench_before_fix_latest_commit.txt)
> [infer_bench_after_fix_latest_commit.txt](https://github.com/user-attachments/files/27489723/infer_bench_after_fix_latest_commit.txt)
> [infer_bench_before_fix_latest_commit.txt](https://github.com/user-attachments/files/27489722/infer_bench_before_fix_latest_commit.txt)

Since the fix was @matthewdouglas  's brilliant insight and it's a one-line change, I am more than happy to leave the PR creation to you guys.

Thanks again for the amazing support!
