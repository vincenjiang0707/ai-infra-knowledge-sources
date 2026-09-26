# [Issue #236] Feature Request: Support sm_120 ( 5090 and blackwell 6000 pro )

source: https://github.com/deepseek-ai/DeepGEMM/issues/236
state: open | updated: 2026-09-16T08:56:28Z
labels: 

## 正文

I can run the following successfully with my blackwell 6000 pro:

```bash
./develop.sh
./install.sh
```

This works too:

```bash
python ./tests/test_layout.py
```

However, when I try to run a custom kernel benchmarking script:

<details>

**bench_fp8_paged_mqa_logits.py**

```py
#!/usr/bin/env python3
import os
import time

import torch
import deep_gemm

# ---------------------------------------------
# JIT logging / debug knobs
# ---------------------------------------------
# Print the full nvcc/nvrtc compile command once when the kernel is JIT-compiled.
os.environ.setdefault("DG_JIT_PRINT_COMPILER_COMMAND", "1")
# Optionally get more debug info:
# os.environ.setdefault("DG_JIT_DEBUG", "1")
# os.environ.setdefault("DG_JIT_PTXAS_VERBOSE", "1")
# os.environ.setdefault("DG_JIT_PTXAS_CHECK", "1")

device = "cuda"


def ceil_div(a: int, b: int) -> int:
    return (a + b - 1) // b


@torch.no_grad()
def bench_fp8_paged_mqa_logits(
    batch_size: int = 64,
    next_n: int = 2,
    heads: int = 64,
    index_dim: int = 128,
    avg_kv: int = 8192,
    blocksize: int = 64,
    max_model_len: int = 111 * 1000,
    is_context_lens_2d: bool = False,
    iters: int = 50,
):
    torch.manual_seed(0)

    # Shapes follow tests/test_attention.py
    q = torch.randn(
        (batch_size, next_n, heads, index_dim),
        device=device,
        dtype=torch.bfloat16,
    )
    kv_cache = torch.randn(
        (max_model_len * 3, blocksize, 1, index_dim),
        device=device,
        dtype=torch.bfloat16,
    )
    weights = torch.randn(
        (batch_size * next_n, heads),
        device=device,
        dtype=torch.float32,
    )

    # FP8 casts (same helpers as tests, but simple version here).
    q_fp8 = q.to(torch.float8_e4m3fn)
    # Quantize kv_cache per-token (very simple scale=1 for benchmarking only)
    kv_cache_fp8 = kv_cache.to(torch.float8_e4m3fn)

    # Random context lengths around avg_kv
    context_lens = torch.randint(
        int(0.7 * avg_kv),
        int(1.3 * avg_kv),
        (batch_size,),
        device=device,
        dtype=torch.int32,
    )
    context_lens_list = context_lens.tolist()
    max_block_len = ceil_div(max(context_lens_list), blocksize) * blocksize

    # Block tables
    num_blocks_total = kv_cache.shape[0]
    block_tables = torch.zeros(
        (batch_size, max_block_len),
        device=device,
        dtype=torch.int32,
    )
    counter = 0
    block_idx_pool = torch.randperm(
        num_blocks_total, device=device, dtype=torch.int32
    )
    for i in range(batch_size):
        nb = ceil_div(context_lens_list[i], blocksize)
        block_tables[i, :nb] = block_idx_pool[counter : counter + nb]
        counter += nb

    if is_context_lens_2d:
        # Build per-(batch,next_n) context lengths as in tests
        context_lens_2d = (
            (context_lens.unsqueeze(1) + 1)
            * torch.rand(batch_size, next_n, device=device)
        ).to(torch.int32)
        context_lens_2d[:, next_n - 1] = context_lens
        ctx_for_meta = context_lens_2d
    else:
        ctx_for_meta = context_lens

    # JIT metadata (this triggers paged_mqa_logits metadata specialization)
    schedule_metadata = deep_gemm.get_paged_mqa_logits_metadata(
        ctx_for_meta, blocksize, deep_gemm.get_num_sms()
    )

    # One warmup to trigger JIT & capture compile cmd
    if is_context_lens_2d:
        logits = deep_gemm.fp8_paged_mqa_logits(
            q_fp8,
            kv_cache_fp8,
            weights,
            ctx_for_meta,
            block_tables,
            schedule_metadata,
            max_model_len,
            clean_logits=False,
        )
    else:
        logits = deep_gemm.fp8_paged_mqa_logits(
            q_fp8,
            kv_cache_fp8,
            weights,
            ctx_for_meta,
            block_tables,
            schedule_metadata,
            max_model_len,
            clean_logits=True,
        )

    torch.cuda.synchronize()

    # Benchmark loop
    times = []
    for _ in range(iters):
        t0 = time.perf_counter()
        if is_context_lens_2d:
            logits = deep_gemm.fp8_paged_mqa_logits(
                q_fp8,
                kv_cache_fp8,
                weights,
                ctx_for_meta,
                block_tables,
                schedule_metadata,
                max_model_len,
                clean_logits=False,
            )
        else:
            logits = deep_gemm.fp8_paged_mqa_logits(
                q_fp8,
                kv_cache_fp8,
                weights,
                ctx_for_meta,
                block_tables,
                schedule_metadata,
                max_model_len,
                clean_logits=True,
            )
        torch.cuda.synchronize()
        t1 = time.perf_counter()
        times.append(t1 - t0)

    avg_us = 1e6 * sum(times) / len(times)

    # Rough TFLOPS estimate, same idea as test_paged_mqa_logits
    sum_lens = sum(context_lens.to(torch.int64))
    tflops = 2.0 * sum_lens * next_n * heads * index_dim / 1e12 / (avg_us * 1e-6)

    print(
        f"fp8_paged_mqa_logits benchmark:\n"
        f"  BSZ={batch_size}, NextN={next_n}, H={heads}, D={index_dim}, avg_kv={avg_kv}\n"
        f"  iters={iters}, avg time = {avg_us:.1f} us, approx {tflops:.1f} TFLOPS"
    )


if __name__ == "__main__":
    # You can toggle these to exercise both metadata modes.
    bench_fp8_paged_mqa_logits(is_context_lens_2d=False)
    bench_fp8_paged_mqa_logits(is_context_lens_2d=True)
```

```bash
DG_JIT_PRINT_COMPILER_COMMAND=1 DG_JIT_PTXAS_VERBOSE=1 python bench_fp8_paged_mqa_logits.py
```
</details>

... first it fails with `Unsupported architecture`, then if I add `arch_major == 12`
it fails with this:

```
$ DG_JIT_PRINT_COMPILER_COMMAND=1 DG_JIT_PTXAS_VERBOSE=1 python bench_fp8_paged_mqa_logits.py
Warning: please use at least NVCC 12.9 for the best DeepGEMM performance
Running NVCC command: /usr/local/cuda/bin/nvcc /home/jesse/.deep_gemm/cache/kernel.smxx_paged_mqa_logits_metadata.a8d04824495f4b393f3e37abf95794af/kernel.cu -o /home/jesse/.deep_gemm/tmp/775171-79e89b64-d5c1d7aa-f29af1ce -std=c++20 --diag-suppress=39,161,174,177,186,940 --ptxas-options=--register-usage-level=10 --ptxas-options=--verbose,--warn-on-local-memory-usage -I/home/jesse/sandbox/DeepGEMM/deep_gemm/include --gpu-architecture=sm_120a --compiler-options=-fPIC,-O3,-fconcepts,-Wno-deprecated-declarations,-Wno-abi -cubin -O3 --expt-relaxed-constexpr --expt-extended-lambda
NVCC compilation failed: /home/jesse/.deep_gemm/cache/kernel.smxx_paged_mqa_logits_metadata.a8d04824495f4b393f3e37abf95794af/kernel.cu:2:10: fatal error: deep_gemm/impls/sm120_fp8_paged_mqa_logits.cuh: No such file or directory
    2 | #include <deep_gemm/impls/sm120_fp8_paged_mqa_logits.cuh>
      |          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.

Traceback (most recent call last):
  File "/home/jesse/sandbox/DeepGEMM/bench_fp8_paged_mqa_logits.py", line 175, in <module>
    bench_fp8_paged_mqa_logits(is_context_lens_2d=False)
  File "/data/conda-envs/vllm_cu128/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/jesse/sandbox/DeepGEMM/bench_fp8_paged_mqa_logits.py", line 100, in bench_fp8_paged_mqa_logits
    schedule_metadata = deep_gemm.get_paged_mqa_logits_metadata(
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
RuntimeError: Assertion error (csrc/apis/../jit_kernels/impls/../../jit/compiler.hpp:183): false and "NVCC compilation failed"
```

Please support `sm120`. I'd love to add support myself, but I'm no kernel wizard.

## 评论 (29)

### createthis · 2025-12-02

Looks like one big difference is that the sm100 kernel expects 168004 ( 168k ) smem_size and sm120 only has 49152 ( 49k ) available.

### createthis · 2025-12-02

I was able to get the shared memory usage down to 46k: https://github.com/createthis/DeepGEMM/pull/1
But now it fails with `Illegal barrier arrive operation`.

### lavdnone2 · 2025-12-03

thanks man
I think they just don't have RTX PRO 6000
but next gen cards will all be SM120+ is seems

### createthis · 2025-12-04

I bought two cuda programming books, for what it’s worth. My background is in web dev and linux, so I have no illusions that I can fix this quickly or easily, but I’m going to try to at least learn as I go.

### lavdnone2 · 2025-12-04

have no time now, but can give you access to full Kimi-K2 - it knows cuda and writes best code so far; or minimax-m2 - somewhat cleaner

### fernandaspets · 2025-12-04


IISuperluminaLII  over here might have some ideas  https://github.com/IISuperluminaLII/FlashMLA_Windows_Linux_sm120

### createthis · 2025-12-04

> IISuperluminaLII over here might have some ideas https://github.com/IISuperluminaLII/FlashMLA_Windows_Linux_sm120

This repo is strange. It looks like the sparse kernels are only sm90 and sm100, just like DeepGEMM. There is a dense kernel for sm120... but... we need sparse kernels. Odd. Also, since this is FlashMLA, I don't think this repo even has an FP8 lightning indexer kernel. This is intended to cover other parts of the DSA system.

### fernandaspets · 2025-12-05

@createthis yeah i was mostly hoping they would be able to chime in here and or continue working on sm120 to make rtx blackwell folks lives easier :)

### LyricZhao · 2025-12-05

Sorry, as we don't have SM120 devices, we don't have plans or people to support this. From my perspective, adding a new architecture support is hard for us to maintain, e.g. the GEMM heuristics are hard to cover all archs. So we encourage the OSS community makes a fork and supports it. The main repo is always using the computation center GPUs.

### fernandaspets · 2025-12-05

@LyricZhao @createthis someone posted up an NVFP4 quant + a link to docker hub image (eous/vllm-sm120) with "a collection of hacks for flashmla sparse, deepgemm, and vllm to run deepseek v3.2 nvfp4 quant". I have not had time to check it out yet, below is link to discussion about quant and link to the docker is also in discussion

https://huggingface.co/eousphoros/DeepSeek-V3.2-NVFP4/discussions/1

### cyysky · 2025-12-08

https://github.com/NVIDIA/TensorRT-LLM/tree/main/cpp/tensorrt_llm/kernels/cutlass_kernels/fp8_blockscale_gemm/6kd_blockwise_gemm 

not sure if this help?

### IISuperluminaLII · 2025-12-12

> Looks like one big difference is that the sm100 kernel expects 168004 ( 168k ) smem_size and sm120 only has 49152 ( 49k ) available.

actually it has 99kb, which is not much still. Writing an agnostic kernel that is tile/quantization/fallback aware based on sm version should be "doable". It will take weeks to months, but should be doable. Will there be much gained from it performance wise, probably not 

without TMEM, you will need to move all TMEM ops to SMEM only

CUTLASS currently just fallsback to sm_80 tcgen03 alloc 

without UMMA its hard to convert native TMEM ops. you WILL need to use sm_80 fallback

tcgen05 F8/F6/F4 (narrow precision) YES (sm_120 tcgen05 with quantization overhead)
tcgen05 BF16/F16 via UMMA NO (sm_80 fallback, but with bf16 and fp16 accel)

### grimulkan · 2025-12-12

Even an implementation that falls back to sm89 style instructions where it needs to will be extremely useful IMO. Right now a lot doesn't work in sm120, including fp8 cases that work under sm89.

### createthis · 2025-12-13

> actually it has 99kb

Yeah... is that documented anywhere? I've seen that number too at a different time.

@grimulkan I'm pretty sure fp8 works under sm120a.

I considered briefly trying to write a tcgen05 emulation library, but that's probably just silly.

### grimulkan · 2025-12-13

> @grimulkan I'm pretty sure fp8 works under sm120a.

Dense, yes. Does it work for grouped/moe/sparse gemms? If so, can you suggest where I can find the implementation? Right now in vllm or trtllm that's a missing piece I think.

### createthis · 2025-12-13

> > [@grimulkan](https://github.com/grimulkan) I'm pretty sure fp8 works under sm120a.
> 
> Dense, yes. Does it work for grouped/moe/sparse gemms? If so, can you suggest where I can find the implementation? Right now in vllm or trtllm that's a missing piece I think.

I just mean as an instruction. I’m pretty sure sm_120a supports fp8. I’m not sure what dense or sparse has to do with whether or not the sm_120a target supports fp8.

### grimulkan · 2025-12-13

@createthis Oh yes, it does. I meant whether actual kernels exist for various operations in fp8 that work on sm120 GPUs to do inference on a model like Deepseek v3.1 or v3.2 in fp8, like the block-scaled gemms for the MoE section. Right now, those engines error out claiming there are missing kernels (for fp8 precision). I guess I must have said something confusing, because I thought this was your interest too! Sorry.

EDIT: Looking at it, cutlass does have some examples, but I'm referring to something like example 92 for sm120:
https://github.com/NVIDIA/cutlass/tree/main/examples/92_blackwell_moe_gemm/
Sorry if it wasn't clear.

### IISuperluminaLII · 2025-12-15

> Sorry, as we don't have SM120 devices, we don't have plans or people to support this. From my perspective, adding a new architecture support is hard for us to maintain, e.g. the GEMM heuristics are hard to cover all archs. So we encourage the OSS community makes a fork and supports it. The main repo is always using the computation center GPUs.

Not necessarily, I think writing a base tcgen0x version and then referencing that for any new arch that uses antiquated/deprecated calls for new gen cards which should work in theory. 🤔 

### Tonoken3 · 2026-04-24


Adding a concrete data point from today's DeepSeek-V4-Flash release (2026-04-24):

**SM120 is completely blocked on V4-family models** due to the mHC (Manifold-Constrained Hyper-Connections) layer calling `tf32_hc_prenorm_gemm`, which only has SM90 and SM100 implementations in the current DeepGEMM tree.

### Hardware
- 7x NVIDIA RTX PRO 6000 Blackwell (96GB), SM120, CUDA 13.0
- Image: `vllm/vllm-openai:deepseekv4-cu130` (vllm 0.1.dev15830)

### Exact failure
```
RuntimeError: Worker failed with error 'Assertion error
(/workspace/.deps/deepgemm-src/csrc/apis/hyperconnection.hpp:56):
Unsupported architecture'
```

The pre-mHC path works fine (NCCL with `NCCL_P2P_DISABLE=1`, FP8 weight loading,
V4 quantization config, MoE backend dispatch, attention backend). 149 GB of
FP8 weights load cleanly, then the assertion fires when mHC initializes.

### Kernel availability
Looking at `deep_gemm/include/deep_gemm/impls/`:
- `sm100_tf32_hc_prenorm_gemm.cuh` — uses TMEM, `tcgen05.mma`, cluster multicast → SM100 only
- `sm90_tf32_hc_prenorm_gemm.cuh` — uses WGMMA → SM90 only
- No `sm120_*` variant exists

### Why existing SM80-level MMA path should work

SM120 natively supports warp-level `mma.sync.aligned.m16n8k32` (SM80-era) plus
TMA (SM90-era). A naive port using:
- Warp-level MMA (no TMEM, no UMMA)
- TMA for GMEM→SMEM
- 99 KB SMEM limit (vs SM100's 228 KB)

...would be functionally correct for the `tf32_hc_prenorm_gemm` primitive
(one GEMM + one squared-sum). Not optimal for throughput, but unblocks the
entire V4 family on workstation Blackwell GPUs.

### Workarounds tried (none worked)

1. Python-level `_tf32_hc_prenorm_gemm_impl` override with a PyTorch fallback
   → Installed but assertion still fires (separate C++ call path)

2. `torch.cuda.get_device_capability` spoof to (10, 0)
   → Bypasses assertion, then fails with:
   `CUDA driver error: no kernel image is available for execution on the device`
   (SM100 cubin cannot execute on SM120)

3. All documented env vars (`VLLM_USE_DEEP_GEMM=0`, etc.)
   → Only affects the general FP8 GEMM path, not mHC.

### Ask

A minimal SM120 implementation of `tf32_hc_prenorm_gemm` (even a slow one)
would unblock the entire RTX 5090 / RTX PRO 6000 user base on V4-Flash / V4-Pro.
Happy to help test any proposed fix.

Full technical report:
https://github.com/lna-lab/blackwell-geforce-nvfp4-gemm/blob/main/DEEPSEEK_V4_SM120_REPORT.md

— TonoKen3 / Lna-Lab


### Tonoken3 · 2026-04-24

One additional data point from the official vLLM blog on V4:

> "Manifold-Constrained Hyper-Connections... **are not covered in this post, as they are simpler model changes that are easier to adapt.**"
> — https://vllm.ai/blog/deepseek-v4

If mHC is indeed a "simpler model change that's easy to adapt," then an SM120 port of `tf32_hc_prenorm_gemm` should be within reach. The current `sm100_tf32_hc_prenorm_gemm.cuh` hard-codes TMEM/UMMA features that SM120 doesn't have, and `sm90_tf32_hc_prenorm_gemm.cuh` requires WGMMA — but the underlying math (one GEMM + one squared-sum) doesn't require either. A warp-level `mma.sync` version (SM80-style, which SM120 supports) should suffice.

Would the DeepGEMM team consider:
1. A reference TileLang implementation in the interim, or
2. A minimal SM120 `.cuh` that prioritizes correctness over peak throughput?

Either would unblock every RTX 5090 / RTX PRO 6000 user on V4-family models.

— TonoKen3 / Lna-Lab


### ergodic-flow · 2026-04-24

I'm no CUDA wizard but I will take a look and see if I can hack up a _barely working version_ 💪 .

EDIT: not yet correct but runs! https://github.com/deepseek-ai/DeepGEMM/compare/main...ergodic-flow:DeepGEMM:feature/sm120-support-v0?expand=1

### ergodic-flow · 2026-04-25

ok after working on this for quite some hours, it's probably not a simple CUDA translation, though much of it is a "boilerplate" change. I also discovered https://github.com/ShlokVFX/Mini-Attention/ which has similar code which could be adapted. I am going to go read some docs on SM120, as there are a lot of differences between SM90 and SM100.

### tonyliu312 · 2026-04-28

Cross-link from a different angle that may help triage this:

`jasl/DeepGEMM` fork branch [`ds4-sm120`](https://github.com/jasl/DeepGEMM/tree/ds4-sm120) already lands a native SM 12.0/12.1 implementation of `tf32_hc_prenorm_gemm` (the V4 mHC kernel that hits `hyperconnection.hpp:56 Unsupported architecture` on stock DG). Hardware-verified on dual DGX Spark (GB10, SM 12.1) — direct probe gave `err_d=0.06` (bf16 normal) and `rel_err_sqsum=7.3e-7` against PyTorch reference. The fork is the kernel half of vllm-project/vllm#40991; that PR has been validated end-to-end on dual-GB10 (V4-Flash, TP=2, fp8) so the kernel is in active production use, not just compiles.

Question for the room: is jasl planning to upstream the SM12x kernel as a DeepGEMM PR, or is the plan to keep it fork-only? If upstream is the goal, happy to help with regression validation on GB10 SM 12.1 silicon, cross-arch review (sm_90/100/120), and the porting work to bring the fork commit cleanly onto current `main`. Don't want to duplicate effort if jasl has it queued.

The `ergodic-flow` WIP fork mentioned earlier in this issue ("runs but not yet correct") would also benefit from the jasl reference being upstreamed, since the math is independently verified.

Cc @jasl in case there's an intent signal you can share.


### jasl · 2026-04-28

> Cross-link from a different angle that may help triage this:
> 
> `jasl/DeepGEMM` fork branch [`ds4-sm120`](https://github.com/jasl/DeepGEMM/tree/ds4-sm120) already lands a native SM 12.0/12.1 implementation of `tf32_hc_prenorm_gemm` (the V4 mHC kernel that hits `hyperconnection.hpp:56 Unsupported architecture` on stock DG). Hardware-verified on dual DGX Spark (GB10, SM 12.1) — direct probe gave `err_d=0.06` (bf16 normal) and `rel_err_sqsum=7.3e-7` against PyTorch reference. The fork is the kernel half of [vllm-project/vllm#40991](https://github.com/vllm-project/vllm/pull/40991); that PR has been validated end-to-end on dual-GB10 (V4-Flash, TP=2, fp8) so the kernel is in active production use, not just compiles.
> 
> Question for the room: is jasl planning to upstream the SM12x kernel as a DeepGEMM PR, or is the plan to keep it fork-only? If upstream is the goal, happy to help with regression validation on GB10 SM 12.1 silicon, cross-arch review (sm_90/100/120), and the porting work to bring the fork commit cleanly onto current `main`. Don't want to duplicate effort if jasl has it queued.
> 
> The `ergodic-flow` WIP fork mentioned earlier in this issue ("runs but not yet correct") would also benefit from the jasl reference being upstreamed, since the math is independently verified.
> 
> Cc [@jasl](https://github.com/jasl) in case there's an intent signal you can share.

We're trying to contact DeepSeek

### ergodic-flow · 2026-04-28

@tonyliu312 my intent with the change I made, was to introduce a small change that is reviewable by the maintainers, rather than get it all working end to end. Personally, I think it needs some work to get it "production quality" but it does run and pass the tests. I think anyone is welcome to use the working fork of VLLM, and I am actually gonna try it out today. I also think we should wait for feedback from maintainers and see what they say about the changes. Forks can always remain forks, but upstreaming changes has to make it past review. 

### ergodic-flow · 2026-04-28

ah and it seems: https://github.com/deepseek-ai/DeepGEMM/issues/236#issuecomment-3615905328

I don't know if they still feel this way but:

> Sorry, as we don't have SM120 devices, we don't have plans or people to support this. From my perspective, adding a new architecture support is hard for us to maintain, e.g. the GEMM heuristics are hard to cover all archs. So we encourage the OSS community makes a fork and supports it. The main repo is always using the computation center GPUs.

### jasl · 2026-04-28

I'm doing plan b: implement essential kernels on the vLLM side.

### scr00ge-00 · 2026-04-29

Hitting this on NVIDIA DGX Spark (GB10, sm_121) with vLLM nightly 0.20.1rc1.dev16+g7a1eb8ac2 (FROM `vllm/vllm-openai:nightly-aarch64`) trying to serve DeepSeek-V4-Flash.

**Stack:**
- 2× DGX Spark, GB10 GPU each (compute_cap 12.1)
- TP=2 across nodes via Ray over a 100Gb fiber link (NCCL)
- DeepGEMM bundled at `vllm/third_party/deep_gemm`

**Failure path:**
- Weights load successfully (~102 s, 73.82 GiB on each node)
- Engine init then fails at `csrc/apis/hyperconnection.hpp:56`:
  ```
  RuntimeError: Assertion error (.../deepgemm-src/csrc/apis/hyperconnection.hpp:56): Unsupported architecture
  ```
- Source shows host-side dispatch only handles `arch_major == 9` (Hopper) and `arch_major == 10` (datacenter Blackwell). GB10 returns 12 → `DG_HOST_UNREACHABLE("Unsupported architecture")`.

**Tested workarounds (all fail at the same dispatch):**
- `DG_JIT_USE_NVRTC=0` + `DG_JIT_NVCC_COMPILER=/usr/local/cuda/bin/nvcc` + `VLLM_USE_FLASHINFER_MOE_FP8=1` + `VLLM_MARLIN_USE_ATOMIC_ADD=1`
- Symlink `/usr/local/cuda/include/cuda → cccl/cuda` (CUDA 13 header layout)
- `--max-model-len 16384` (per other GB10 forum reports)
- `--enforce-eager`, `--kv-cache-dtype fp8`

The dispatch fires before any kernel call so JIT compiler choice and `TORCH_CUDA_ARCH_LIST` changes can't bypass it. Looks like sm_120/121 needs new kernel source (e.g., `sm120_tf32_hc_prenorm_gemm` using mma.sync rather than tcgen05/WGMMA), not a build flag fix.

**Use case:** multi-agent inference cluster (reasoning + tool calls). Currently routing V4 Flash needs through OpenRouter as fallback while waiting on a kernel.

Happy to test patches when something lands. +1 to anyone willing to write the sm_120 variant.


### lucifer1004 · 2026-09-16

SM120 support is proposed in #447 (target: `nv_dev`): it integrates native SM120 kernels on top of the current main APIs / DeepJIT runtime — dense and grouped BF16/FP8/FP4 (incl. mixed FP8×FP4) GEMM, BF16/FP8 einsum, HC prenorm, and dense/paged/sparse (DSv4.1-style) FP8 + MXFP4 MQA logits.

Validation on sm_120a: 741 SM120 tests, with memcheck and racecheck subsets clean. Spot-verified on GB10 (sm_121a) as well. The SM120 device headers are maintained as a single source of truth in [lucifer1004/DeepGEMM-sm120](https://github.com/lucifer1004/DeepGEMM-sm120) and vendored byte-for-byte into the fork, so fixes propagate.

Note the PR targets `nv_dev`, not `main`; SM120 MegaMoE / Mega Gate / Mega mHC are not included.

