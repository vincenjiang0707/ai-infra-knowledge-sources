# [Issue #1842] # 70B 4-bit LLM decode bottlenecked by HIP kernel (`kgemm_4bit_inference_naive`) efficiency — 49% vs 91% memory bandwidth on ROCm/gfx1151

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1842
state: open | updated: 2026-06-07T14:34:21Z
labels: ROCm

## 正文

## Summary

On AMD gfx1151 (RDNA 3.5, Strix Point UMA), the `kgemm_4bit_inference_naive` HIP kernel achieves only **49% of memory bandwidth**, while rocBLAS bf16 GEMM achieves **91%** on the same hardware.

This results in **~2.1 tok/s for 70B 4-bit decode** instead of the projected **~3.9 tok/s** if the kernel matched bf16 efficiency.

---

## Environment

- **GPU:** gfx1151 (Strix Point / Ryzen AI MAX 395), 40 CUs, LPDDR5X-8000
- **Measured peak memory bandwidth:** 210 GB/s (copy test)
- **ROCm:** 7.11
- **PyTorch:** 2.9.1+rocm7.11
- **bitsandbytes:** rocm_enabled branch

---

## Benchmark Data

### M=1 GEMV Bandwidth Efficiency (70B MLP dimensions: 8192×28672)

| Kernel | Data Size | Time | Achieved Read BW | % of Peak (210 GB/s) |
|--------|-----------|------|------------------|----------------------|
| `kgemm_4bit_inference_naive<hip_bfloat16, 128, 1>` | 117 MB | 1128 µs | 102 GB/s | **49%** |
| rocBLAS bf16 `Cijk_Ailk_Bljk_BBS_BH_...MT96x96` | 469 MB | 2450 µs | 191 GB/s | **91%** |

The 4-bit kernel reads 4× less data but is only **2.1× faster** — it should be closer to 4×.

### Path Comparison (confirming dispatch is correct)

| Path | Time | Notes |
|------|------|-------|
| Fused `gemv_4bit` | 1147 µs | ✅ Selected |
| Dequant + bf16 mm | 7574 µs | 6.6× slower (not selected) |
| Pure bf16 mm | 2459 µs | Baseline |

We are hitting the correct fused kernel path. The issue is kernel efficiency, not dispatch.

---

## Profiler Output
```
=== Fused gemv_4bit ===
void kgemm_4bit_inference_naive<hip_bfloat16, 128, 1...>   22.564ms (20 calls)   1.128ms/call

=== bf16 mm ===
Cijk_Ailk_Bljk_BBS_BH_Bias_HA_S_SAV_UserArgs_MT96x96...   48.990ms (20 calls)   2.450ms/call
```

---

## Impact on Real Workloads

**70B 4-bit LLM decode (Llama-3.3-70B-Instruct, NF4):**

| Scenario | Projected tok/s |
|----------|-----------------|
| Current (49% BW efficiency) | ~2.1 |
| If 4-bit matched bf16 efficiency (91%) | **~3.9** |
| Theoretical limit (100% BW) | ~4.3 |

This represents a **~1.85× optimization opportunity**.

---

## Analysis

The kernel name `kgemm_4bit_inference_naive` suggests this implementation has not yet been aggressively tuned for RDNA 3.5. Possible causes for the 49% bandwidth efficiency:

1. **Memory access not fully coalesced** — 4-bit packing may cause suboptimal load patterns
2. **Dequantization not pipelined with memory loads** — compute may be stalling fetches
3. **Not tuned for RDNA 3.5 wave scheduling** — occupancy, wavefront sizes, LDS usage
4. **Missing HIP-specific optimizations** — intrinsics, cache hints, vector widths

The bf16 baseline demonstrates that decode-scale GEMV on gfx1151 can achieve near-optimal memory bandwidth (91%); the gap is therefore specific to this kernel implementation rather than a platform limitation.

---

## Questions

1. **Is there a more optimized kernel path** for RDNA 3.5 / gfx11 that should be selected?

2. **Are there plans to optimize the HIP 4-bit GEMV kernels** for recent AMD architectures?

3. **Would a PR with gfx1151-specific tuning be welcome?** If so, are there guidelines for the expected kernel structure?

4. **Is the `naive` suffix intentional or is it the only implementation for HIP** — i.e., is there a non-naive implementation planned or in progress?

---

## Minimal Repro
```python
import torch
import time
import bitsandbytes.functional as F

M, K, N = 1, 8192, 28672  # 70B MLP dimensions

# 4-bit path
w_fp = torch.randn(N, K, dtype=torch.bfloat16, device='cuda')
w_4bit, quant_state = F.quantize_4bit(w_fp, quant_type='nf4')
x = torch.randn(M, K, dtype=torch.bfloat16, device='cuda')

torch.cuda.synchronize()
start = time.perf_counter()
for _ in range(100):
    # Note: F.gemv_4bit invokes the same kgemm_4bit_inference_naive kernel
    # used by bnb.nn.Linear4bit during M=1 decode
    y = F.gemv_4bit(x, w_4bit.T, state=quant_state)
torch.cuda.synchronize()
print(f"4-bit: {(time.perf_counter()-start)/100*1e6:.0f} µs")

# bf16 baseline
w_bf16 = torch.randn(K, N, dtype=torch.bfloat16, device='cuda')
torch.cuda.synchronize()
start = time.perf_counter()
for _ in range(100):
    y = x @ w_bf16
torch.cuda.synchronize()
print(f"bf16:  {(time.perf_counter()-start)/100*1e6:.0f} µs")
```

**Expected output on gfx1151:**
```
4-bit: 1147 µs
bf16:  2459 µs
```

---

## Profiling Script
```python
import torch
from torch.profiler import profile, ProfilerActivity
import bitsandbytes.functional as F

M, K, N = 1, 8192, 28672

w_fp = torch.randn(N, K, dtype=torch.bfloat16, device='cuda')
w_4bit, quant_state = F.quantize_4bit(w_fp, quant_type='nf4')
x = torch.randn(M, K, dtype=torch.bfloat16, device='cuda')

for _ in range(10):
    y = F.gemv_4bit(x, w_4bit.T, state=quant_state)
torch.cuda.synchronize()

with profile(activities=[ProfilerActivity.CUDA]) as prof:
    for _ in range(20):
        y = F.gemv_4bit(x, w_4bit.T, state=quant_state)
    torch.cuda.synchronize()
print(prof.key_averages().table(sort_by="cuda_time_total"))
```
---

## Related

- Filed parallel issue with AMD/PyTorch ROCm team requesting guidance on RDNA 3.5 kernel optimization patterns
- Happy to collaborate on optimization efforts or provide additional profiling data

Thanks for your work on ROCm support!


## 评论 (4)

### BellaDoggie · 2026-01-20

## Update: Root Cause Found + 15× Speedup Achieved

After extensive profiling, I identified the bottlenecks in `kgemm_4bit_inference_naive` on RDNA3 (gfx1151 / Strix Point).

### Results

| Test | Before | After | Speedup |
|------|--------|-------|---------|
| Kernel microbench (K=8192, N=28672) | 2686 µs (43 GB/s) | 409 µs (287 GB/s) | **6.6×** |
| 70B 4-bit decode | 0.42 tok/s | 6.47 tok/s | **15×** |
| 8B 4-bit decode | 30.9 tok/s | 36.6 tok/s | 1.2× |

### Optimization Journey

**Phase 1: Float compute path (~102 → ~132 GB/s)**
- `float quant_map[16]` instead of `T` — avoids bf16↔float conversions
- `float local_B[8]` and `float local_A[8]` — all compute in float
- Early exit for out-of-bounds warps
- Fully unrolled dequant — explicit 8 statements instead of loop
- Fully unrolled FMA — explicit 8 statements instead of loop
- Removed `#if BNB_BF16_AVAILABLE` branches in hot path — always use float math

**Phase 2: ILP and vectorization (~132 → ~154 GB/s)**
- All 32 B values dequantized upfront — more ILP for LDS reads
- `__builtin_expect` — branch hints for fast path
- Precomputed constants — moved `clz_blocksize` out of loop
- 4 vectorized A loads — `int4` loads for all 32 values at once
- Removed inner loop — everything fully unrolled

**Phase 3: Bank conflicts and accumulators (no improvement, but kept)**
- Replicated `quant_map[32]` — two copies, even/odd lanes use different copies to reduce bank conflicts
- 4 accumulators (`local_C0` through `local_C3`) — breaks FMA dependency chain for more ILP

**Phase 4: B prefetch (~154 → ~158 GB/s)**
- Prefetch first B chunk and absmax before loop
- Inside loop: use prefetched data, then prefetch next iteration's B while computing current
- Prefetch of next B overlaps with dequant+FMA compute

**Phase 5: 64 threads per block (~158 → ~287 GB/s) — THE BIG WIN**
- Changed from 128 threads to 64 threads per block (1 warp per block on RDNA3)
- Dramatically reduced register pressure and improved occupancy

### What Didn't Work

| Optimization | Result | Reason |
|--------------|--------|--------|
| Quant_map in registers | **~154 → ~43 GB/s** (massive regression!) | 16 float registers × 64 threads killed occupancy, caused spilling |
| A matrix prefetch | ~158 → ~154 GB/s | Added register pressure, hurt occupancy |
| Interleaved dequant+FMA | No change | Compiler was already scheduling well |

### Important for Users

Until this is fixed upstream:

```python
BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_use_double_quant=False,  # Avoid extra dequant overhead
)
```

Also ensure `torch.inference_mode()` is used — without it, `requires_grad=True` bypasses the fused kernel entirely.

### Optimized Kernel Code

Here's the modified `kgemm_4bit_inference_naive` function that achieves these results:

<details>
<summary>Click to expand kernel code</summary>

```cpp
#define num_values_4bit 32
template <typename T, int THREADS, int BITS> __global__ void kgemm_4bit_inference_naive(int M, int N, int K, T * __restrict__ const A, unsigned char *B,  float *absmax, const float *datatype, T * out,  int lda, int ldb, int ldc, int blocksize)
{
  typedef hipcub::WarpReduce<float, BNB_WARP_SIZE> WarpReduce;
  __shared__ typename WarpReduce::TempStorage temp_storage[THREADS/BNB_WARP_SIZE];
  
  // Replicate quant_map to reduce bank conflicts (2 copies)
  __shared__ float quant_map[32];

  const int warp_idx = threadIdx.x / BNB_WARP_SIZE;
  const int warp_lane = threadIdx.x % BNB_WARP_SIZE;
  const int row_B = (THREADS/BNB_WARP_SIZE)*blockIdx.x + warp_idx;
  const int offset_B = ldb * row_B;
  constexpr int num_values_8bit = num_values_4bit/2;
  
  // Multiple accumulators for ILP
  float local_C0 = 0.0f;
  float local_C1 = 0.0f;
  float local_C2 = 0.0f;
  float local_C3 = 0.0f;
  
  unsigned char local_B_4bit[num_values_8bit];
  float local_absmax;

  // Load quant_map twice to reduce bank conflicts
  if (threadIdx.x < 16) {
    float val = __ldg(&datatype[threadIdx.x]);
    quant_map[threadIdx.x] = val;
    quant_map[threadIdx.x + 16] = val;
  }
  __syncthreads();

  if (row_B >= M) return;

  const int stride = BNB_WARP_SIZE * num_values_4bit;
  const int clz_blocksize = 31 - __clz(blocksize);
  const int base_absidx = 2 * offset_B;
  
  // Use lane-specific offset into quant_map to reduce conflicts
  const int qm_offset = (warp_lane & 1) << 4;  // 0 or 16

  // PREFETCH: Load first B chunk before loop
  int inner_idx = warp_lane * num_values_4bit;
  int inner_idx_halved = inner_idx >> 1;
  int4 prefetch_B;
  float prefetch_absmax;
  
  if (inner_idx < K) {
    int absidx = (base_absidx + inner_idx) >> clz_blocksize;
    prefetch_absmax = __ldg(&absmax[absidx]);
    if ((inner_idx_halved + num_values_8bit) < (K >> 1)) {
      prefetch_B = reinterpret_cast<int4*>(B)[(offset_B + inner_idx_halved) / num_values_8bit];
    }
  }

  for(; inner_idx < K; inner_idx += stride)
  {
    inner_idx_halved = inner_idx >> 1;
    
    // USE prefetched B and absmax from previous iteration (or pre-loop)
    local_absmax = prefetch_absmax;
    
    if(__builtin_expect((inner_idx_halved + num_values_8bit) < (K >> 1), 1))
    {
      reinterpret_cast<int4&>(local_B_4bit[0]) = prefetch_B;
    }
    else
    {
      #pragma unroll
      for(int j = 0; j < num_values_8bit; j++)
        local_B_4bit[j] = ((inner_idx_halved + j) < (K >> 1)) ? B[offset_B + inner_idx_halved + j] : 0x77;
    }

    // PREFETCH next iteration's B (overlaps with compute below)
    int next_inner_idx = inner_idx + stride;
    int next_inner_idx_halved = next_inner_idx >> 1;
    if (next_inner_idx < K) {
      int next_absidx = (base_absidx + next_inner_idx) >> clz_blocksize;
      prefetch_absmax = __ldg(&absmax[next_absidx]);
      if ((next_inner_idx_halved + num_values_8bit) < (K >> 1)) {
        prefetch_B = reinterpret_cast<int4*>(B)[(offset_B + next_inner_idx_halved) / num_values_8bit];
      }
    }

    if(__builtin_expect(inner_idx + 32 <= K, 1))
    {
      // Load A vectors
      int4 a_vec0 = reinterpret_cast<const int4*>(A)[inner_idx / 8];
      int4 a_vec1 = reinterpret_cast<const int4*>(A)[inner_idx / 8 + 1];
      int4 a_vec2 = reinterpret_cast<const int4*>(A)[inner_idx / 8 + 2];
      int4 a_vec3 = reinterpret_cast<const int4*>(A)[inner_idx / 8 + 3];
      
      const T* a0 = reinterpret_cast<const T*>(&a_vec0);
      const T* a1 = reinterpret_cast<const T*>(&a_vec1);
      const T* a2 = reinterpret_cast<const T*>(&a_vec2);
      const T* a3 = reinterpret_cast<const T*>(&a_vec3);

      // INTERLEAVED: dequant pair + FMA pair
      float b0  = quant_map[qm_offset + (local_B_4bit[0] >> 4)] * local_absmax;
      float b1  = quant_map[qm_offset + (local_B_4bit[0] & 0xF)] * local_absmax;
      local_C0 += (float)a0[0] * b0;
      local_C1 += (float)a0[1] * b1;

      float b2  = quant_map[qm_offset + (local_B_4bit[1] >> 4)] * local_absmax;
      float b3  = quant_map[qm_offset + (local_B_4bit[1] & 0xF)] * local_absmax;
      local_C2 += (float)a0[2] * b2;
      local_C3 += (float)a0[3] * b3;

      float b4  = quant_map[qm_offset + (local_B_4bit[2] >> 4)] * local_absmax;
      float b5  = quant_map[qm_offset + (local_B_4bit[2] & 0xF)] * local_absmax;
      local_C0 += (float)a0[4] * b4;
      local_C1 += (float)a0[5] * b5;

      float b6  = quant_map[qm_offset + (local_B_4bit[3] >> 4)] * local_absmax;
      float b7  = quant_map[qm_offset + (local_B_4bit[3] & 0xF)] * local_absmax;
      local_C2 += (float)a0[6] * b6;
      local_C3 += (float)a0[7] * b7;

      float b8  = quant_map[qm_offset + (local_B_4bit[4] >> 4)] * local_absmax;
      float b9  = quant_map[qm_offset + (local_B_4bit[4] & 0xF)] * local_absmax;
      local_C0 += (float)a1[0] * b8;
      local_C1 += (float)a1[1] * b9;

      float b10 = quant_map[qm_offset + (local_B_4bit[5] >> 4)] * local_absmax;
      float b11 = quant_map[qm_offset + (local_B_4bit[5] & 0xF)] * local_absmax;
      local_C2 += (float)a1[2] * b10;
      local_C3 += (float)a1[3] * b11;

      float b12 = quant_map[qm_offset + (local_B_4bit[6] >> 4)] * local_absmax;
      float b13 = quant_map[qm_offset + (local_B_4bit[6] & 0xF)] * local_absmax;
      local_C0 += (float)a1[4] * b12;
      local_C1 += (float)a1[5] * b13;

      float b14 = quant_map[qm_offset + (local_B_4bit[7] >> 4)] * local_absmax;
      float b15 = quant_map[qm_offset + (local_B_4bit[7] & 0xF)] * local_absmax;
      local_C2 += (float)a1[6] * b14;
      local_C3 += (float)a1[7] * b15;

      float b16 = quant_map[qm_offset + (local_B_4bit[8] >> 4)] * local_absmax;
      float b17 = quant_map[qm_offset + (local_B_4bit[8] & 0xF)] * local_absmax;
      local_C0 += (float)a2[0] * b16;
      local_C1 += (float)a2[1] * b17;

      float b18 = quant_map[qm_offset + (local_B_4bit[9] >> 4)] * local_absmax;
      float b19 = quant_map[qm_offset + (local_B_4bit[9] & 0xF)] * local_absmax;
      local_C2 += (float)a2[2] * b18;
      local_C3 += (float)a2[3] * b19;

      float b20 = quant_map[qm_offset + (local_B_4bit[10] >> 4)] * local_absmax;
      float b21 = quant_map[qm_offset + (local_B_4bit[10] & 0xF)] * local_absmax;
      local_C0 += (float)a2[4] * b20;
      local_C1 += (float)a2[5] * b21;

      float b22 = quant_map[qm_offset + (local_B_4bit[11] >> 4)] * local_absmax;
      float b23 = quant_map[qm_offset + (local_B_4bit[11] & 0xF)] * local_absmax;
      local_C2 += (float)a2[6] * b22;
      local_C3 += (float)a2[7] * b23;

      float b24 = quant_map[qm_offset + (local_B_4bit[12] >> 4)] * local_absmax;
      float b25 = quant_map[qm_offset + (local_B_4bit[12] & 0xF)] * local_absmax;
      local_C0 += (float)a3[0] * b24;
      local_C1 += (float)a3[1] * b25;

      float b26 = quant_map[qm_offset + (local_B_4bit[13] >> 4)] * local_absmax;
      float b27 = quant_map[qm_offset + (local_B_4bit[13] & 0xF)] * local_absmax;
      local_C2 += (float)a3[2] * b26;
      local_C3 += (float)a3[3] * b27;

      float b28 = quant_map[qm_offset + (local_B_4bit[14] >> 4)] * local_absmax;
      float b29 = quant_map[qm_offset + (local_B_4bit[14] & 0xF)] * local_absmax;
      local_C0 += (float)a3[4] * b28;
      local_C1 += (float)a3[5] * b29;

      float b30 = quant_map[qm_offset + (local_B_4bit[15] >> 4)] * local_absmax;
      float b31 = quant_map[qm_offset + (local_B_4bit[15] & 0xF)] * local_absmax;
      local_C2 += (float)a3[6] * b30;
      local_C3 += (float)a3[7] * b31;
    }
    else
    {
      // Slow path unchanged
      float b0  = quant_map[qm_offset + (local_B_4bit[0] >> 4)] * local_absmax;
      float b1  = quant_map[qm_offset + (local_B_4bit[0] & 0xF)] * local_absmax;
      float b2  = quant_map[qm_offset + (local_B_4bit[1] >> 4)] * local_absmax;
      float b3  = quant_map[qm_offset + (local_B_4bit[1] & 0xF)] * local_absmax;
      float b4  = quant_map[qm_offset + (local_B_4bit[2] >> 4)] * local_absmax;
      float b5  = quant_map[qm_offset + (local_B_4bit[2] & 0xF)] * local_absmax;
      float b6  = quant_map[qm_offset + (local_B_4bit[3] >> 4)] * local_absmax;
      float b7  = quant_map[qm_offset + (local_B_4bit[3] & 0xF)] * local_absmax;
      float b8  = quant_map[qm_offset + (local_B_4bit[4] >> 4)] * local_absmax;
      float b9  = quant_map[qm_offset + (local_B_4bit[4] & 0xF)] * local_absmax;
      float b10 = quant_map[qm_offset + (local_B_4bit[5] >> 4)] * local_absmax;
      float b11 = quant_map[qm_offset + (local_B_4bit[5] & 0xF)] * local_absmax;
      float b12 = quant_map[qm_offset + (local_B_4bit[6] >> 4)] * local_absmax;
      float b13 = quant_map[qm_offset + (local_B_4bit[6] & 0xF)] * local_absmax;
      float b14 = quant_map[qm_offset + (local_B_4bit[7] >> 4)] * local_absmax;
      float b15 = quant_map[qm_offset + (local_B_4bit[7] & 0xF)] * local_absmax;
      float b16 = quant_map[qm_offset + (local_B_4bit[8] >> 4)] * local_absmax;
      float b17 = quant_map[qm_offset + (local_B_4bit[8] & 0xF)] * local_absmax;
      float b18 = quant_map[qm_offset + (local_B_4bit[9] >> 4)] * local_absmax;
      float b19 = quant_map[qm_offset + (local_B_4bit[9] & 0xF)] * local_absmax;
      float b20 = quant_map[qm_offset + (local_B_4bit[10] >> 4)] * local_absmax;
      float b21 = quant_map[qm_offset + (local_B_4bit[10] & 0xF)] * local_absmax;
      float b22 = quant_map[qm_offset + (local_B_4bit[11] >> 4)] * local_absmax;
      float b23 = quant_map[qm_offset + (local_B_4bit[11] & 0xF)] * local_absmax;
      float b24 = quant_map[qm_offset + (local_B_4bit[12] >> 4)] * local_absmax;
      float b25 = quant_map[qm_offset + (local_B_4bit[12] & 0xF)] * local_absmax;
      float b26 = quant_map[qm_offset + (local_B_4bit[13] >> 4)] * local_absmax;
      float b27 = quant_map[qm_offset + (local_B_4bit[13] & 0xF)] * local_absmax;
      float b28 = quant_map[qm_offset + (local_B_4bit[14] >> 4)] * local_absmax;
      float b29 = quant_map[qm_offset + (local_B_4bit[14] & 0xF)] * local_absmax;
      float b30 = quant_map[qm_offset + (local_B_4bit[15] >> 4)] * local_absmax;
      float b31 = quant_map[qm_offset + (local_B_4bit[15] & 0xF)] * local_absmax;
      
      float b_vals[32] = {b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,
                         b16,b17,b18,b19,b20,b21,b22,b23,b24,b25,b26,b27,b28,b29,b30,b31};
      #pragma unroll
      for(int k = 0; k < 32; k++)
      {
        float a_val = (inner_idx + k < K) ? (float)A[inner_idx + k] : 0.0f;
        local_C0 += a_val * b_vals[k];
      }
    }
  }

  // Combine accumulators
  float local_C = local_C0 + local_C1 + local_C2 + local_C3;
  
  local_C = WarpReduce(temp_storage[warp_idx]).Sum(local_C);
  if(warp_lane == 0)
    out[row_B] = T(local_C);
}
```

</details>

**Note:** Also requires template instantiation for 64 threads and updating the kernel launcher to use 64 threads instead of 128 for RDNA3.

I don't have bandwidth to maintain a PR, but maintainers are welcome to use this code.


### TimDettmers · 2026-02-21

Thanks for the incredibly thorough profiling and optimization work — the 15x speedup on RDNA 3.5 decode is a remarkable result, and the phase-by-phase breakdown is very useful.

We'd be very interested in a PR with these optimizations. A few notes on the integration path:

There's an active RFC (PR #1877) to unify the currently-duplicated CUDA and HIP kernel sources into a single codebase using a `compat.cuh` portability layer. Right now `kernels.cu` and `kernels.hip` are maintained as near-identical copies that inevitably drift apart — exactly the kind of thing that makes architecture-specific tuning hard to maintain.

For a PR with your optimizations, either approach would work:
1. Submit against the current `kernels.hip` (simpler, can be merged sooner)
2. Wait for the unification effort and submit against the unified source (cleaner long-term)

One consideration: the current kernel is instantiated with `THREADS=128` for all platforms. Your finding that 64 threads per block is optimal for RDNA 3 is interesting — we'd want to make sure the thread count can be architecture-dependent without regressing CDNA (MI-series) performance. A template parameter or compile-time selection based on target architecture would be the right approach.

Would you be interested in submitting a PR?

### JiwaniZakir · 2026-03-25

The gap between 49% and 91% bandwidth utilization strongly suggests uncoalesced global memory accesses during nibble unpacking in `kgemm_4bit_inference_naive` (in `csrc/kernels.cu`) — threads within a wavefront are likely reading from strided or non-contiguous addresses when extracting 4-bit weights, fragmenting cache line fetches on the LPDDR5X bus. On RDNA 3.5's 64-lane wavefronts, this is especially costly since a single poorly-aligned load pattern can halve effective bandwidth. The fix typically involves restructuring the weight layout so that consecutive threads read consecutive 128-bit aligned chunks (e.g., via `uint4` vectorized loads) before unpacking, which is precisely the kind of access pattern the tuned rocBLAS kernel uses to hit 91%. It's also worth checking whether the kernel is launching with enough wavefronts per CU to hide the memory latency — with M=1, there may be insufficient parallelism to keep all 40 CUs saturated if the grid is sized for larger batch dimensions.

### h34v3nzc0dex · 2026-06-07

Confirming 4-bit works on gfx1151 once bnb is built from source, and flagging the packaging gap that's the actual blocker. Built 0.50.0.dev0 for gfx1151 (`-DROCM_VERSION=83 -DBNB_ROCM_ARCH=gfx1151`, rocm83→rocm713 shim), Radeon 8060S, ROCm 7.13, torch 2.11. nf4 quantize+dequantize, 8192×8192:

```
4bit dequantize 8192x8192: 0.89 ms/iter, ~152 GB/s effective
```

The snag for everyone else: stock PyPI bnb (0.49.2) ships ROCm binaries only up to `libbitsandbytes_rocm72.so`, but a ROCm 7.13 / gfx1151 stack wants `libbitsandbytes_rocm83.so` → load fails, no gfx1151 binary present. So today it's build-from-source or nothing on Strix Halo, which is the thing that breaks an otherwise-working `unsloth[amd]` QLoRA path. A published gfx1151 / rocm8x wheel would close it. Build recipe + datapoint: https://github.com/h34v3nzc0dex/strix-halo-llm-finetune-guide/tree/main/bnb-1842-gfx1151-4bit .

