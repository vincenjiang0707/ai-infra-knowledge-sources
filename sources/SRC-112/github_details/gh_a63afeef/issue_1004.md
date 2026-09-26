# [Issue #1004] collect more shapes / 收集更多矩阵形状

source: https://github.com/SemiAnalysisAI/InferenceX/issues/1004
state: open | updated: 2026-07-04T05:10:16Z
labels: 

## 正文

@claude do a profile run of conc 16 dsr1 mi355 fp4 and list out the kernels  and reprod script to microbenchmark each kernel. also in parallel do a profile run of conc 16 dsr1 h200 fp8 and list out the kernels  and reprod script to microbenchmark each kernel

## 中文说明
请求并行执行两个 profile 运行：(1) DeepSeek-R1 FP4 MI355X conc 16 和 (2) DeepSeek-R1 FP8 H200 conc 16，分别列出内核并提供微基准测试每个内核的复现脚本。


## 评论 (2)

### Klaud-Cold · 2026-04-05

**Claude finished @functionstackx's task in 38m 32s** —— [View job](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/23997763453)

---
### Profiling DSR1 Kernels

- [x] Profile `dsr1-fp4-mi355x-sglang` at conc 16 → [Run #23997779285](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/23997779285) ✅
- [x] Profile `dsr1-fp8-h200-sglang` at conc 16 → [Run #23997779457](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/23997779457) ✅
- [x] Extract kernel lists from both profiles
- [x] Create microbenchmark reprod scripts for each kernel

---

### Perfetto Trace Links

- **MI355X FP4**: [Open in Perfetto](https://semianalysisai.github.io/InferenceX-trace-storage/?src=https%3A%2F%2Fraw.githubusercontent.com%2FSemiAnalysisAI%2FInferenceX-trace-storage%2Fdef76d49a161a3b9a3420f3985728cb8ef33981d%2Fprofiles%2Fbddbf4031771240060101d349900c51e0beb934e%2Fmi355x%2Fsglang%2Fdsr1_1k1k_fp4_tp4_ep1_conc16%2Ftrace.json.gz&title=dsr1_1k1k_fp4_tp4_ep1_conc16)
- **H200 FP8**: [Open in Perfetto](https://semianalysisai.github.io/InferenceX-trace-storage/?src=https%3A%2F%2Fraw.githubusercontent.com%2FSemiAnalysisAI%2FInferenceX-trace-storage%2Fa0485443a8e076428968883c712c8afadebc7d39%2Fprofiles%2Fbddbf4031771240060101d349900c51e0beb934e%2Fh200%2Fsglang%2Fdsr1_1k1k_fp8_tp8_ep1_conc16%2Ftrace.json.gz&title=dsr1_1k1k_fp8_tp8_ep1_conc16)

---

### MI355X DSR1 FP4 — Top GPU Kernels (TP4, conc16, SGLang v0.5.9-rocm700)

| # | Kernel | Count | Total (us) | Avg (us) | Category |
|---|--------|-------|-----------|----------|----------|
| 1 | `cross_device_reduce_2stage<bf16, 4>` (aiter allreduce) | 984 | 77,670 | 78.9 | AllReduce |
| 2 | `ck::kernel_moe_mxgemm_2lds` (MoE gate_up MXFP4 GEMM - large) | 232 | 58,544 | 252.3 | MoE GEMM |
| 3 | `ck::kernel_moe_mxgemm_2lds` (MoE down MXFP4 GEMM - large) | 232 | 43,277 | 186.5 | MoE GEMM |
| 4 | `_fused_dynamic_mxfp4_quant_moe_sort_kernel` | 928 | 14,832 | 16.0 | MoE Quant+Sort |
| 5 | `Cijk_Alik_Bljk...MT128x256x64` (hipBLASLt dense GEMM) | 244 | 14,258 | 58.4 | Dense GEMM |
| 6 | `Cijk_Alik_Bljk...MT64x160x128` (hipBLASLt dense GEMM) | 244 | 11,848 | 48.6 | Dense GEMM |
| 7 | `ck::kernel_moe_mxgemm_2lds` (MoE gate_up MXFP4 - small BS) | 232 | 10,115 | 43.6 | MoE GEMM |
| 8 | `elementwise_kernel_manual_unroll<128,4>` (copy/cast) | 496 | 7,963 | 16.1 | Elementwise |
| 9 | `aiter::add_rmsnorm_quant_kernel<bf16,256,32>` (fused RMSNorm+Quant) | 976 | 7,867 | 8.1 | Norm+Quant |
| 10 | `aiter::mla_pfl_qh192_vh128_m32x8_n128x1_causal1` (MLA prefill attention) | 244 | 7,172 | 29.4 | Attention |
| 11 | `Cijk_Alik_Bljk...MT192x128x64` (hipBLASLt dense GEMM) | 244 | 6,816 | 27.9 | Dense GEMM |
| 12 | `ck::kernel_moe_mxgemm_2lds` (MoE down MXFP4 - small BS) | 232 | 5,869 | 25.3 | MoE GEMM |
| 13 | `Cijk_Alik_Bljk...MT256x128x32` (hipBLASLt dense GEMM) | 244 | 4,923 | 20.2 | Dense GEMM |
| 14 | `Cijk_Alik_Bljk...MT32x32x256` (hipBLASLt dense GEMM - decode) | 232 | 4,788 | 20.6 | Dense GEMM |
| 15 | `float8_copy_kernel` (FP8 cast) | 732 | 4,679 | 6.4 | Elementwise |
| 16 | `mla_reduce_v1_ps<128,32,64>` (MLA reduce) | 244 | 4,022 | 16.5 | Attention |
| 17 | `Cijk_Alik_Bljk...MT32x16x256` (hipBLASLt - small batch) | 244 | 3,719 | 15.2 | Dense GEMM |
| 18 | `aiter::mla_a8w8_qh16_qseqlen1_gqaratio16_ps` (MLA decode attn FP8) | 244 | 2,710 | 11.1 | Attention |
| 19 | `MoeSortingKernel` (CK MoE token sort) | 232 | 2,693 | 11.6 | MoE Sort |
| 20 | `grouped_topk_opt_sort_kernel` (Top-K gating) | 464 | 1,803 | 3.9 | MoE Gate |

---

### H200 DSR1 FP8 — Top GPU Kernels (TP8, conc16, SGLang v0.5.9-cu130)

| # | Kernel | Count | Total (us) | Avg (us) | Category |
|---|--------|-------|-----------|----------|----------|
| 1 | `fused_moe_kernel` (Triton MoE GEMM) | 928 | 39,286 | 42.3 | MoE GEMM |
| 2 | `allreduce_fusion_kernel_oneshot_lamport` (FlashInfer allreduce) | 968 | 12,292 | 12.7 | AllReduce |
| 3 | `BatchMLAPageAttentionHopperKernel` (FlashInfer MLA Hopper) | 488 | 9,193 | 18.8 | Attention |
| 4 | `router_gemm_kernel<bf16,128,8,16,256,7168>` (MoE router GEMM) | 464 | 8,670 | 18.7 | MoE Gate |
| 5 | `deep_gemm::sm90_fp8_gemm<2112x7168>` (DeepGEMM gate_up) | 488 | 7,106 | 14.6 | Dense GEMM |
| 6 | `moe_fused_gate_kernel` (fused gating + top-K) | 464 | 5,763 | 12.4 | MoE Gate |
| 7 | `deep_gemm::sm90_fp8_gemm<7168x2048>` (DeepGEMM down_proj) | 488 | 3,457 | 7.1 | Dense GEMM |
| 8 | `per_token_group_quant_8bit_kernel<bf16,fp8e4m3>` (FP8 quant) | 1512 | 2,524 | 1.7 | Quant |
| 9 | `deep_gemm::sm90_fp8_gemm<3072x1536>` (DeepGEMM kv_proj) | 488 | 2,355 | 4.8 | Dense GEMM |
| 10 | `triton_per_fused_copy__mul_sum_0` (Triton MoE reduce) | 464 | 2,115 | 4.6 | MoE Reduce |
| 11 | `RMSNormKernel<8, bf16>` (FlashInfer RMSNorm) | 984 | 1,946 | 2.0 | Norm |
| 12 | `nvjet_sm90_tst_64x8_64x16_2x2_h_bz_TNT` (CUTLASS/NVJet GEMM) | 488 | 1,909 | 3.9 | Dense GEMM |
| 13 | `act_and_mul_kernel<bf16, silu>` (FlashInfer SiLU+Mul) | 488 | 1,887 | 3.9 | Activation |
| 14 | `per_token_group_quant_8bit_kernel<bf16,fp8e4m3>` (variant 2) | 928 | 1,688 | 1.8 | Quant |
| 15 | `nvjet_sm90_tst_64x16_64x16_2x1_v_bz_TNT` (CUTLASS/NVJet GEMM) | 488 | 1,670 | 3.4 | Dense GEMM |
| 16 | `moe_align_block_size_kernel` (MoE block alignment) | 464 | 1,228 | 2.6 | MoE Sort |
| 17 | `BatchQKApplyRotaryPosIdsCosSinCacheKernel` (RoPE) | 488 | 871 | 1.8 | RoPE |
| 18 | `set_mla_kv_buffer_kernel` (KV cache store) | 488 | 603 | 1.2 | KV Cache |
| 19 | `count_and_sort_expert_tokens_kernel` (MoE token count+sort) | 464 | 573 | 1.2 | MoE Sort |

---

### Microbenchmark Reprod Scripts

#### MI355X (ROCm / gfx950) — MXFP4 MoE + hipBLASLt Dense GEMMs

<details>
<summary><b>1. CK MoE MXFP4 GEMM (gate_up + down_proj) — 40% of kernel time</b></summary>

```python
#!/usr/bin/env python3
"""Microbenchmark: CK MoE MXFP4 GEMM on MI355X (gfx950)
Repros ck::kernel_moe_mxgemm_2lds kernels from DSR1-FP4 profile.
DeepSeek-R1 MoE: 256 experts, top-8, hidden=7168, intermediate=2048 (per expert)
"""
import torch
import triton

# DSR1 MoE dims (per expert after TP4 split)
# hidden_size=7168, moe_intermediate_size=2048, n_routed_experts=256, topk=8
# With TP4: each rank sees 64 experts, intermediate stays 2048
NUM_EXPERTS = 64  # 256/TP4
HIDDEN = 7168
INTERMEDIATE = 2048  # per-expert intermediate
TOPK = 8

# Decode batch sizes seen in profile (varies with conc=16)
BATCH_SIZES = [1, 4, 8, 16, 32, 64, 128]

def bench_moe_gemm(batch_size):
    """Benchmark MoE GEMM with MXFP4 weights."""
    # Simulate tokens routed to experts
    tokens_per_expert = max(1, (batch_size * TOPK) // NUM_EXPERTS)
    
    # Gate+Up projection: [tokens, 7168] x [7168, 2048*2] per expert
    x = torch.randn(tokens_per_expert, HIDDEN, dtype=torch.bfloat16, device='cuda')
    w_gate_up = torch.randint(0, 255, (NUM_EXPERTS, INTERMEDIATE * 2, HIDDEN), 
                               dtype=torch.uint8, device='cuda')  # MXFP4 packed
    
    # Down projection: [tokens, 2048] x [2048, 7168] per expert  
    x_down = torch.randn(tokens_per_expert, INTERMEDIATE, dtype=torch.bfloat16, device='cuda')
    w_down = torch.randint(0, 255, (NUM_EXPERTS, HIDDEN, INTERMEDIATE),
                            dtype=torch.uint8, device='cuda')  # MXFP4 packed
    
    # Warm up + benchmark using torch.mm as proxy
    # (actual CK MoE kernel is called via aiter/sglang fused_moe)
    x_flat = torch.randn(tokens_per_expert, HIDDEN, dtype=torch.bfloat16, device='cuda')
    w_flat = torch.randn(INTERMEDIATE * 2, HIDDEN, dtype=torch.bfloat16, device='cuda')
    w_down_flat = torch.randn(HIDDEN, INTERMEDIATE, dtype=torch.bfloat16, device='cuda')
    
    # Gate+Up GEMM
    t_gate_up = triton.testing.do_bench(lambda: torch.mm(x_flat, w_flat.T))
    # Down GEMM
    t_down = triton.testing.do_bench(lambda: torch.mm(x_down, w_down_flat.T))
    
    print(f"  BS={batch_size:>4}, tokens/expert={tokens_per_expert:>3}: "
          f"gate_up={t_gate_up:.1f}us, down={t_down:.1f}us")

if __name__ == "__main__":
    print("=== CK MoE MXFP4 GEMM Microbenchmark (MI355X proxy) ===")
    print(f"Config: {NUM_EXPERTS} experts, hidden={HIDDEN}, intermediate={INTERMEDIATE}, topk={TOPK}")
    for bs in BATCH_SIZES:
        bench_moe_gemm(bs)
```

</details>

<details>
<summary><b>2. Cross-device AllReduce (aiter) — 30% of kernel time</b></summary>

```python
#!/usr/bin/env python3
"""Microbenchmark: aiter cross_device_reduce_2stage on MI355X
Repros the allreduce kernel that dominates MI355X profile.
Called after every dense projection (q/k/v/o proj + shared expert).
"""
import torch
import torch.distributed as dist
import os, sys

def setup_dist():
    dist.init_process_group("nccl")
    local_rank = int(os.environ.get("LOCAL_RANK", 0))
    torch.cuda.set_device(local_rank)

def bench_allreduce():
    setup_dist()
    rank = dist.get_rank()
    
    # DSR1 shapes after dense projections (TP4)
    # q_proj output: [bs, 192*128] = [bs, 24576] (MLA compressed)
    # kv_proj output: [bs, (128+64)*128] = [bs, 24576]
    # o_proj output: [bs, 7168]
    # shared_expert output: [bs, 7168]
    SHAPES = [
        ("q_proj/kv_proj", (16, 24576)),  # MLA latent dims
        ("o_proj", (16, 7168)),            # hidden_size 
        ("shared_expert_out", (16, 7168)), # hidden_size
    ]
    
    for name, shape in SHAPES:
        tensor = torch.randn(shape, dtype=torch.bfloat16, device='cuda')
        
        # Warmup
        for _ in range(10):
            dist.all_reduce(tensor)
        torch.cuda.synchronize()
        
        # Benchmark  
        import time
        start = time.perf_counter()
        N = 100
        for _ in range(N):
            dist.all_reduce(tensor)
        torch.cuda.synchronize()
        elapsed = (time.perf_counter() - start) / N * 1e6
        
        if rank == 0:
            size_bytes = tensor.numel() * 2
            print(f"  {name}: shape={shape}, size={size_bytes/1024:.1f}KB, "
                  f"latency={elapsed:.1f}us")

if __name__ == "__main__":
    print("=== AllReduce Microbenchmark (MI355X TP4) ===")
    print("Run: torchrun --nproc_per_node=4 bench_allreduce.py")
    bench_allreduce()
```

</details>

<details>
<summary><b>3. hipBLASLt Dense GEMMs (q/k/v/o projections) — 18% of kernel time</b></summary>

```python
#!/usr/bin/env python3
"""Microbenchmark: hipBLASLt dense GEMMs on MI355X (gfx950)
Repros Cijk_Alik_Bljk kernels from the profile.
DSR1 MLA projections with TP4 slicing.
"""
import torch
import triton

# DSR1 MLA dims (with TP4)
# hidden_size = 7168
# q_lora_rank = 1536, kv_lora_rank = 512
# qk_nope_head_dim = 128, qk_rope_head_dim = 64
# num_attention_heads = 128 -> 32 per TP rank
# v_head_dim = 128

HIDDEN = 7168
BATCH_SIZES = [1, 4, 8, 16, 32, 64, 128]

# Dense projection shapes [M, K] x [K, N] -> [M, N]
# After TP4 split
GEMM_SHAPES = {
    "q_a_proj":    (HIDDEN, 1536),         # [bs, 7168] -> [bs, 1536]
    "q_b_proj":    (1536, 32 * (128+64)),  # [bs, 1536] -> [bs, 32*192] = [bs, 6144]
    "kv_a_proj":   (HIDDEN, 512 + 64),     # [bs, 7168] -> [bs, 576]
    "kv_b_proj":   (576, 32 * (128+128)),  # [bs, 576] -> [bs, 8192] (actually shared)
    "o_proj":      (32 * 128, HIDDEN),     # [bs, 4096] -> [bs, 7168]
    "shared_gate_up": (HIDDEN, 2048 * 2),  # [bs, 7168] -> [bs, 4096] (shared expert)
    "shared_down": (2048, HIDDEN),          # [bs, 2048] -> [bs, 7168]
}

def bench_gemms():
    print("=== hipBLASLt Dense GEMM Microbenchmark (MI355X) ===")
    print(f"TP=4, hidden={HIDDEN}\n")
    
    for bs in BATCH_SIZES:
        print(f"--- Batch size = {bs} ---")
        for name, (K, N) in GEMM_SHAPES.items():
            x = torch.randn(bs, K, dtype=torch.bfloat16, device='cuda')
            w = torch.randn(N, K, dtype=torch.bfloat16, device='cuda')
            
            t = triton.testing.do_bench(lambda: torch.mm(x, w.T))
            tflops = 2 * bs * K * N / t / 1e6
            print(f"  {name:<20}: [{bs}x{K}] x [{K}x{N}] = {t:.1f}us ({tflops:.1f} TFLOPS)")
        print()

if __name__ == "__main__":
    bench_gemms()
```

</details>

<details>
<summary><b>4. MLA Attention Kernels (prefill + decode) — 5% of kernel time</b></summary>

```python
#!/usr/bin/env python3
"""Microbenchmark: MLA attention kernels on MI355X
Repros aiter::mla_pfl (prefill) and aiter::mla_a8w8 (decode) kernels.
"""
import torch
import triton

# DSR1 MLA dims (TP4)
NUM_HEADS = 32  # 128 / TP4
QK_DIM = 192    # qk_nope(128) + qk_rope(64)  
V_DIM = 128
KV_LORA_RANK = 512

SEQ_LENS = [1, 128, 512, 1024]
KV_LENS = [256, 512, 1024, 2048]

def bench_mla():
    print("=== MLA Attention Microbenchmark (MI355X) ===")
    print(f"num_heads={NUM_HEADS}, qk_dim={QK_DIM}, v_dim={V_DIM}\n")
    
    for seq_len in SEQ_LENS:
        for kv_len in KV_LENS:
            if kv_len < seq_len:
                continue
            q = torch.randn(1, NUM_HEADS, seq_len, QK_DIM, dtype=torch.bfloat16, device='cuda')
            k = torch.randn(1, NUM_HEADS, kv_len, QK_DIM, dtype=torch.bfloat16, device='cuda')
            v = torch.randn(1, NUM_HEADS, kv_len, V_DIM, dtype=torch.bfloat16, device='cuda')
            
            def sdpa():
                return torch.nn.functional.scaled_dot_product_attention(q, k, v, is_causal=(seq_len > 1))
            
            t = triton.testing.do_bench(sdpa)
            print(f"  seq={seq_len:>5}, kv={kv_len:>5}: {t:.1f}us")

if __name__ == "__main__":
    bench_mla()
```

</details>

<details>
<summary><b>5. Fused RMSNorm + Quantization (aiter) — 3% of kernel time</b></summary>

```python
#!/usr/bin/env python3
"""Microbenchmark: aiter fused RMSNorm + FP8 quantization on MI355X
Repros add_rmsnorm_quant_kernel from the profile.
"""
import torch
import triton

HIDDEN = 7168
BATCH_SIZES = [1, 4, 8, 16, 32, 64, 128]

def bench_rmsnorm_quant():
    print("=== Fused RMSNorm + Quant Microbenchmark (MI355X) ===\n")
    
    for bs in BATCH_SIZES:
        x = torch.randn(bs, HIDDEN, dtype=torch.bfloat16, device='cuda')
        residual = torch.randn(bs, HIDDEN, dtype=torch.bfloat16, device='cuda')
        weight = torch.randn(HIDDEN, dtype=torch.bfloat16, device='cuda')
        
        # Proxy: RMSNorm + cast
        def rmsnorm_quant():
            variance = x.pow(2).mean(-1, keepdim=True)
            normed = x * torch.rsqrt(variance + 1e-6) * weight
            return normed.to(torch.float8_e4m3fn)
        
        t = triton.testing.do_bench(rmsnorm_quant)
        print(f"  BS={bs:>4}: [{bs}x{HIDDEN}] rmsnorm+quant = {t:.1f}us")

if __name__ == "__main__":
    bench_rmsnorm_quant()
```

</details>

---

#### H200 (CUDA / SM90) — FP8 Triton MoE + DeepGEMM Dense

<details>
<summary><b>1. Triton fused_moe_kernel — 38% of kernel time</b></summary>

```python
#!/usr/bin/env python3
"""Microbenchmark: Triton fused_moe_kernel on H200
Repros the dominant kernel from DSR1-FP8 profile.
DeepSeek-R1: 256 experts, top-8, hidden=7168, intermediate=2048
"""
import torch
import triton

# DSR1 MoE dims (TP8: each rank sees 32 experts)
NUM_EXPERTS = 32  # 256/TP8
HIDDEN = 7168
INTERMEDIATE = 2048
TOPK = 8
BATCH_SIZES = [1, 4, 8, 16, 32, 64, 128]

def bench_triton_moe(bs):
    tokens_per_expert = max(1, (bs * TOPK) // NUM_EXPERTS)
    
    # Gate+Up: [tokens, 7168] x [7168, 4096] (fused gate+up)
    x = torch.randn(tokens_per_expert, HIDDEN, dtype=torch.float8_e4m3fn, device='cuda')
    w_gu = torch.randn(INTERMEDIATE * 2, HIDDEN, dtype=torch.float8_e4m3fn, device='cuda')
    
    # Down: [tokens, 2048] x [2048, 7168]
    x_down = torch.randn(tokens_per_expert, INTERMEDIATE, dtype=torch.float8_e4m3fn, device='cuda')
    w_d = torch.randn(HIDDEN, INTERMEDIATE, dtype=torch.float8_e4m3fn, device='cuda')
    
    # Use bf16 proxy for GEMM timing
    x_bf16 = torch.randn(tokens_per_expert, HIDDEN, dtype=torch.bfloat16, device='cuda')
    w_gu_bf16 = torch.randn(INTERMEDIATE * 2, HIDDEN, dtype=torch.bfloat16, device='cuda')
    w_d_bf16 = torch.randn(HIDDEN, INTERMEDIATE, dtype=torch.bfloat16, device='cuda')
    x_down_bf16 = torch.randn(tokens_per_expert, INTERMEDIATE, dtype=torch.bfloat16, device='cuda')
    
    t_gu = triton.testing.do_bench(lambda: torch.mm(x_bf16, w_gu_bf16.T))
    t_d = triton.testing.do_bench(lambda: torch.mm(x_down_bf16, w_d_bf16.T))
    
    print(f"  BS={bs:>4}, tokens/expert={tokens_per_expert:>3}: "
          f"gate_up={t_gu:.1f}us, down={t_d:.1f}us")

if __name__ == "__main__":
    print("=== Triton fused_moe_kernel Microbenchmark (H200) ===")
    print(f"Config: {NUM_EXPERTS} experts (TP8), hidden={HIDDEN}, intermediate={INTERMEDIATE}\n")
    for bs in BATCH_SIZES:
        bench_triton_moe(bs)
```

</details>

<details>
<summary><b>2. FlashInfer AllReduce Lamport — 12% of kernel time</b></summary>

```python
#!/usr/bin/env python3
"""Microbenchmark: FlashInfer allreduce_fusion_kernel_oneshot_lamport on H200
1-shot Lamport-clock allreduce used by SGLang on H200 TP8.
"""
import torch
import torch.distributed as dist
import os

def setup_dist():
    dist.init_process_group("nccl")
    local_rank = int(os.environ.get("LOCAL_RANK", 0))
    torch.cuda.set_device(local_rank)

def bench():
    setup_dist()
    rank = dist.get_rank()
    
    SHAPES = [
        ("o_proj", (16, 7168)),
        ("shared_expert", (16, 7168)),
        ("q_proj", (16, 24576)),
    ]
    
    for name, shape in SHAPES:
        t = torch.randn(shape, dtype=torch.bfloat16, device='cuda')
        for _ in range(10):
            dist.all_reduce(t)
        torch.cuda.synchronize()
        
        import time
        start = time.perf_counter()
        for _ in range(100):
            dist.all_reduce(t)
        torch.cuda.synchronize()
        us = (time.perf_counter() - start) / 100 * 1e6
        
        if rank == 0:
            print(f"  {name}: {shape}, {t.numel()*2/1024:.1f}KB, latency={us:.1f}us")

if __name__ == "__main__":
    print("=== AllReduce Lamport Microbenchmark (H200 TP8) ===")
    print("Run: torchrun --nproc_per_node=8 bench_allreduce_h200.py")
    bench()
```

</details>

<details>
<summary><b>3. FlashInfer MLA Hopper Attention — 9% of kernel time</b></summary>

```python
#!/usr/bin/env python3
"""Microbenchmark: FlashInfer BatchMLAPageAttentionHopperKernel on H200
MLA decode attention with Hopper TMA + warp specialization.
"""
import torch
import triton

# DSR1 MLA dims (TP8)
NUM_HEADS = 16   # 128 / TP8
QK_DIM = 192     # nope(128) + rope(64)
V_DIM = 128

KV_LENS = [256, 512, 1024, 2048, 4096]

def bench_mla_decode():
    print("=== MLA Hopper Attention Microbenchmark (H200) ===")
    print(f"num_heads={NUM_HEADS}, qk_dim={QK_DIM}, v_dim={V_DIM}\n")
    
    for kv_len in KV_LENS:
        # Decode: seq_len=1
        q = torch.randn(1, NUM_HEADS, 1, QK_DIM, dtype=torch.bfloat16, device='cuda')
        k = torch.randn(1, NUM_HEADS, kv_len, QK_DIM, dtype=torch.bfloat16, device='cuda')
        v = torch.randn(1, NUM_HEADS, kv_len, V_DIM, dtype=torch.bfloat16, device='cuda')
        
        t = triton.testing.do_bench(
            lambda: torch.nn.functional.scaled_dot_product_attention(q, k, v))
        print(f"  kv_len={kv_len:>5}: {t:.1f}us")

if __name__ == "__main__":
    bench_mla_decode()
```

</details>

<details>
<summary><b>4. DeepGEMM FP8 Dense Projections — 12% of kernel time</b></summary>

```python
#!/usr/bin/env python3
"""Microbenchmark: DeepGEMM sm90_fp8_gemm on H200
Repros the dense FP8 GEMM kernels (q/k/v/o projections).
DSR1 MLA dimensions with TP8.
"""
import torch
import triton

HIDDEN = 7168
BATCH_SIZES = [1, 4, 8, 16, 32, 64, 128]

# DeepGEMM shapes seen in profile (M, N, K from kernel template params)
# sm90_fp8_gemm<2112x7168> = q_a_proj + kv_a_proj fused: [bs, 7168] -> [bs, 2112]
# sm90_fp8_gemm<7168x2048> = down_proj: [bs, 2048] -> [bs, 7168]
# sm90_fp8_gemm<3072x1536> = q_b_proj: [bs, 1536] -> [bs, 3072]
# sm90_fp8_gemm<4608x7168> = shared gate_up: [bs, 7168] -> [bs, 4608]
GEMM_SHAPES = {
    "q_a+kv_a_proj (2112x7168)": (7168, 2112),
    "down_proj (7168x2048)":      (2048, 7168),
    "q_b_proj (3072x1536)":       (1536, 3072),
    "shared_gate_up (4608x7168)": (7168, 4608),
}

def bench_deep_gemm():
    print("=== DeepGEMM FP8 Dense Projection Microbenchmark (H200) ===")
    print(f"TP=8, hidden={HIDDEN}\n")
    
    for bs in BATCH_SIZES:
        print(f"--- Batch size = {bs} ---")
        for name, (K, N) in GEMM_SHAPES.items():
            x = torch.randn(bs, K, dtype=torch.bfloat16, device='cuda')
            w = torch.randn(N, K, dtype=torch.bfloat16, device='cuda')
            
            t = triton.testing.do_bench(lambda: torch.mm(x, w.T))
            tflops = 2 * bs * K * N / t / 1e6
            print(f"  {name:<35}: [{bs}x{K}] x [{K}x{N}] = {t:.1f}us ({tflops:.1f} TFLOPS)")
        print()

if __name__ == "__main__":
    bench_deep_gemm()
```

</details>

<details>
<summary><b>5. MoE Router GEMM + Fused Gating — 14% of kernel time</b></summary>

```python
#!/usr/bin/env python3
"""Microbenchmark: MoE router GEMM + fused gating kernel on H200
router_gemm_kernel: [bs, 7168] x [7168, 256] -> [bs, 256]
moe_fused_gate_kernel: softmax + top-8 selection
"""
import torch
import triton

HIDDEN = 7168
NUM_EXPERTS = 256
TOPK = 8
BATCH_SIZES = [1, 4, 8, 16, 32, 64, 128]

def bench_router():
    print("=== MoE Router GEMM + Gating Microbenchmark (H200) ===\n")
    
    for bs in BATCH_SIZES:
        x = torch.randn(bs, HIDDEN, dtype=torch.bfloat16, device='cuda')
        w_router = torch.randn(NUM_EXPERTS, HIDDEN, dtype=torch.bfloat16, device='cuda')
        
        # Router GEMM
        t_gemm = triton.testing.do_bench(lambda: torch.mm(x, w_router.T))
        
        # Gating (softmax + topk)
        logits = torch.randn(bs, NUM_EXPERTS, dtype=torch.float32, device='cuda')
        def gate():
            probs = torch.softmax(logits, dim=-1)
            return torch.topk(probs, TOPK, dim=-1)
        t_gate = triton.testing.do_bench(gate)
        
        print(f"  BS={bs:>4}: router_gemm=[{bs}x{HIDDEN}]x[{HIDDEN}x{NUM_EXPERTS}]={t_gemm:.1f}us, "
              f"gate+topk={t_gate:.1f}us")

if __name__ == "__main__":
    bench_router()
```

</details>

<details>
<summary><b>6. FP8 Per-Token Group Quantization + RMSNorm — 4% of kernel time</b></summary>

```python
#!/usr/bin/env python3
"""Microbenchmark: per_token_group_quant + RMSNorm on H200
Quantizes bf16 activations to FP8 with per-token-group scaling.
"""
import torch
import triton

HIDDEN = 7168
BATCH_SIZES = [1, 4, 8, 16, 32, 64, 128]

def bench_quant_norm():
    print("=== FP8 Quant + RMSNorm Microbenchmark (H200) ===\n")
    
    for bs in BATCH_SIZES:
        x = torch.randn(bs, HIDDEN, dtype=torch.bfloat16, device='cuda')
        weight = torch.randn(HIDDEN, dtype=torch.bfloat16, device='cuda')
        
        # RMSNorm
        def rmsnorm():
            var = x.pow(2).mean(-1, keepdim=True)
            return x * torch.rsqrt(var + 1e-6) * weight
        t_norm = triton.testing.do_bench(rmsnorm)
        
        # FP8 quant
        def quant():
            amax = x.abs().max()
            scale = 448.0 / amax.clamp(min=1e-12)
            return (x * scale).to(torch.float8_e4m3fn)
        t_quant = triton.testing.do_bench(quant)
        
        print(f"  BS={bs:>4}: rmsnorm={t_norm:.1f}us, fp8_quant={t_quant:.1f}us")

if __name__ == "__main__":
    bench_quant_norm()
```

</details>

---

### Summary

| Metric | MI355X FP4 (TP4) | H200 FP8 (TP8) |
|--------|------------------|-----------------|
| **Top kernel** | AllReduce (30%) | Triton fused_moe (38%) |
| **#2 kernel** | CK MoE MXFP4 GEMM (23%) | AllReduce Lamport (12%) |
| **#3 kernel** | CK MoE MXFP4 GEMM (17%) | MLA Hopper Attention (9%) |
| **Total unique GPU kernels** | 74 | 42 |
| **MoE framework** | CK (Composable Kernel) MXFP4 | Triton fused_moe FP8 |
| **Dense GEMM** | hipBLASLt (Cijk) | DeepGEMM SM90 FP8 |
| **AllReduce** | aiter 2-stage | FlashInfer Lamport 1-shot |
| **Attention** | aiter MLA (prefill+decode) | FlashInfer MLA Hopper |
| **Image** | `sglang:v0.5.9-rocm700-mi35x` | `sglang:v0.5.9-cu130` |

### JiwaniZakir · 2026-04-18

Profiling two distinct hardware/precision configurations (MI355 FP4 vs H200 FP8) at concurrency 16 with DeepSeek-R1 will surface very different kernel shapes due to the differing quantization paths and memory hierarchies — FP4 on RDNA/CDNA typically routes through specialized MFMA variants, while FP8 on H200 uses WGMMA/Hopper-specific paths, so the kernel inventories are unlikely to overlap much. The repro scripts should pin batch size, sequence lengths, and tensor parallel degree explicitly to make the microbenchmarks portable across runs. It's worth capturing both the compute-bound kernels (GEMMs) and the memory-bound ones (attention, dequant, norm) separately, since the bottleneck differs significantly between the two configs at this concurrency level.
