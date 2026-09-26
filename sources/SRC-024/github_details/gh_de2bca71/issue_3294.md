# [Issue #3294] [Issue]: lacking general support for gfx1201

source: https://github.com/ROCm/aiter/issues/3294
state: open | updated: 2026-09-14T21:14:25Z
labels: 

## 正文

### Problem Description

Attempt to enable aiter kernels on vllm: `VLLM_ROCM_USE_AITER=1`

Expected result: aiter kernels are supported on R9700 and the server proceeds to launch and use the aiter kernels.

Actual result: vllm fails to start with an error related to aiter not being available for the compute type.

Note: I'm aware the issue I'm describing is in vllm, but my main point is that the AI Pro 9700 lacks support on aiter in general, when it should be a first class citizen (it has "AI Pro" in the name, after all). In reality, projects that use aiter (vllm, amd ATOM) fail to launch on the R9700.

### Operating System

Opensuse Tumbleweed

### CPU

AMD Ryzen 9 9900X3D

### GPU

2x AMD AI Pro 9700

### ROCm Version

7.13

### ROCm Component

composable_kernel

### Steps to Reproduce

Attempt to enable aiter kernels on vllm: `VLLM_ROCM_USE_AITER=1`

Expected result: aiter kernels are supported on R9700 and the server proceeds to launch and use the aiter kernels.

Actual result: vllm fails to start with an error related to aiter not being available for the compute type.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (12)

### carlushuang · 2026-05-26

@andysalerno thanks for interested in aiter as vLLM backend. We are WIP to enable gfx1201 support in aiter today, will be triton first for functional support (with decent performance), while looking for HIP kernel (opus) + flyDSL for performant kernels.

https://github.com/ROCm/ATOM/pull/811 => here is some initial attemp I've addressed and PR to aiter, hope can be a reference to you

### andysalerno · 2026-05-27

Thanks for the response!! I'm glad to hear that. I was also able to get vllm to work with aiter on the R9700 using [this hacky patch](https://github.com/andysalerno/r9700-serving/blob/main/docker/patches/GFX12x_R9700_RUNTIME.patch) (though I don't know for sure if accuracy is perfectly correct, I just know it allows aiter to run as the attention backend)

### interconnectedMe · 2026-06-10

Adding another R9700 / gfx1201 data point from a single-GPU workstation test.

Hardware / host stack:

- GPU: AMD Radeon AI PRO R9700, gfx1201, 32 GB VRAM
- OS: Ubuntu 24.04.4 HWE
- AMDGPU DKMS: 31.30.0, ROCk module 6.19.4
- Host ROCm user space: 7.2.x
- Container: `vllm/vllm-openai-rocm:latest`
- vLLM logged version: `0.20.0`
- Model: `btbtyler09/Qwen3.6-35B-A3B-GPTQ-4bit`
- Serve shape: GPTQ, `max_model_len=65536`, `max_num_seqs=1`, `max_num_batched_tokens=8192`, single R9700 visible

Result: the model server did load and respond successfully through the OpenAI-compatible `/v1/chat/completions` API. In this configuration I saw no amdgpu ring timeout, GPU reset, or KFD/DRM kernel marker during load, warmup, prompt runs, or clean stop. A medium coding prompt generated 700 completion tokens in 14.739s (~47.5 tok/s by end-to-end timing). A longer-prefill prompt used 6059 prompt tokens + 331 completion tokens in 12.376s (~26.7 completion tok/s end-to-end). Telemetry peaked around 305 W, 100% GFX activity, 96% memory activity, 29,972 MiB VRAM, and 79 C junction, then returned to idle cleanly.

The relevant optimization warnings were:

```text
Found incompatible backend(s) [TURBOQUANT] with AttentionType.DECODER. Overriding with ROCM_ATTN out of potential backends: ['ROCM_ATTN', 'TRITON_ATTN'].

Using default MoE config. Performance might be sub-optimal! Config file not found at /usr/local/lib/python3.12/dist-packages/vllm/model_executor/layers/fused_moe/configs/E=256,N=512,device_name=AMD_Radeon_R9700,dtype=int4_w4a16.json

Cannot use ROCm custom paged attention kernel, falling back to Triton implementation.
```

So from my side this currently looks functional under the official vLLM ROCm image, but not yet first-class/tuned for R9700 AITER/MoE/decode paths. That lines up with @carlushuang's note above about gfx1201 support being WIP and Triton-first.

Question: for the missing tuned MoE config above (`E=256,N=512,device_name=AMD_Radeon_R9700,dtype=int4_w4a16.json`), is the preferred route to wait for upstream vLLM/AITER support, run an AITER/vLLM tuning workflow locally and contribute the generated JSON, or track this in a separate vLLM issue rather than here?

Happy to test patches, image tags, env flags such as `AITER_ONLINE_TUNE=1`, or candidate tuned configs on this R9700 setup if useful.

### Nero10578 · 2026-07-12

How can we still not have first class Aiter support for GFX1201? A product sold with Radeon AI Pro in the name. Is AMD even serious about being an AI hardware competitor? 

### andysalerno · 2026-07-12

> How can we still not have first class Aiter support for GFX1201? A product sold with Radeon AI Pro in the name. Is AMD even serious about being an AI hardware competitor?

One of the problems (I think) is the disconnect between AITER dev and downstream projects like VLLM. To the best of my understanding - AITER (unified attention) works basically perfectly on gfx1201. Maybe there are still issues, but in my experience it works fine. On 2x R9700, I get 3k tok/sec prefill and ~80 tok/sec generation on qwen-3.6-27B-fp8 on **patched** VLLM.

The key word is **patched**. I had to do it myself. VLLM has not been updated to understand that gfx1201 should allow AITER unified attention as the attention backend for gfx1201. This is where the disconnect is; despite AITER unified attention working seemingly okay*, no one has prioritized making sure VLLM actually lets you select it as the backend on the gfx1201. It's filtered out by checks that only care about the CDNA cards.

Here are 3 different PRs into VLLM that all do this, but they haven't moved at all:
https://github.com/vllm-project/vllm/pull/36659
https://github.com/vllm-project/vllm/pull/43615
https://github.com/vllm-project/vllm/pull/46192

(to be clear I'm not saying those PRs should merge as-is, just that there is demand for this to work but it never seems to go anywhere)

So I don't want to place blame or anything, it's not productive and I appreciate the work being done by the talented devs on these projects. Just wish someone in AMD management would realize if they allow marketing to pick the name "AI Pro", they should understand the target audience will be people who work with AI as "Pros" and would expect things like VLLM to work out of the box...

\* big disclaimer, it works ok in *my* basic scenarios using just the small amount of models I have tested (gemma 4, qwen 3.6) so possibly there are huge blockers that explains why they have not enabled it yet. That being said, even if only gemma 4 and qwen 3.6 worked, it would probably satisfy the majority...

### Nero10578 · 2026-07-12

I recently bought and returned two Intel Arc B70s because while they run in vllm they would not run with any kind of graph compilation making the performance abysmal. But these are 2-3 month old cards, meanwhile the R9700 has been available almost a year by now and the RDNA4 architecture itself has been out since the RX 9070, so I am a little disappointed that it turned out there are still many issues and not even proper support for aiter which theoretically boosts performance to usable levels. 

Like we agreed, the "AI Pro" name seems meaningless and just a marketing gimmick if popular AI software like vllm doesn't even work properly out of the box. It "runs" but what's the point if its so slow its unusable.

> Here are 3 different PRs into VLLM that all do this, but they haven't moved at all: [vllm-project/vllm#36659](https://github.com/vllm-project/vllm/pull/36659) [vllm-project/vllm#43615](https://github.com/vllm-project/vllm/pull/43615) [vllm-project/vllm#46192](https://github.com/vllm-project/vllm/pull/46192)

I tried these vllm patches, but at least on latest vllm main and latest rocm 7.2.4 right now I am getting the "AITER unified-attention kernel needs 66 KB of LDS and gfx1201 only allows 64 KB" error so I can't run anything. How did you get past that for vllm? I'd need to modify aiter itself and rebuild/install it from source to set num_stages=1?



### andysalerno · 2026-07-12

```bash
> I recently bought and returned two Intel Arc B70s because while they run in vllm they would not run with any kind of graph compilation making the performance abysmal. But these are 2-3 month old cards, meanwhile the R9700 has been available almost a year by now and the RDNA4 architecture itself has been out since the RX 9070, so I am a little disappointed that it turned out there are still many issues and not even proper support for aiter which theoretically boosts performance to usable levels.
> 
> Like we agreed, the "AI Pro" name seems meaningless and just a marketing gimmick if popular AI software like vllm doesn't even work properly out of the box. It "runs" but what's the point if its so slow its unusable.
> 
> > Here are 3 different PRs into VLLM that all do this, but they haven't moved at all: [vllm-project/vllm#36659](https://github.com/vllm-project/vllm/pull/36659) [vllm-project/vllm#43615](https://github.com/vllm-project/vllm/pull/43615) [vllm-project/vllm#46192](https://github.com/vllm-project/vllm/pull/46192)
> 
> I tried these vllm patches, but at least on latest vllm main and latest rocm 7.2.4 right now I am getting the "AITER unified-attention kernel needs 66 KB of LDS and gfx1201 only allows 64 KB" error so I can't run anything. How did you get past that for vllm? I'd need to modify aiter itself and rebuild/install it from source to set num_stages=1?
```

I think the secret is, you need more recent rocm; 7.13+ is working for me. But I am not applying any of those PR patches directly, instead I have my own patches (which I think are functionally the same). I track it all in this repo: https://github.com/andysalerno/r9700-serving

It requires some understanding of containers to make it work, but if you have [just](https://github.com/casey/just) and podman/docker installed then I think `just build-images` followed by `just up` should work. (You can check some of the configs that also let you pick nightly rocm, nightly AITER, nightly vllm, etc).

Also I know I'm repeating myself here but I'm not a gpu programming expert - I just know the patches in my repo works for my scenarios and the output is extremely fast and also correct (according to my own benchmarks).

### Nero10578 · 2026-07-12

> I think the secret is, you need more recent rocm; 7.13+ is working for me. But I am not applying any of those PR patches directly, instead I have my own patches (which I think are functionally the same). I track it all in this repo: https://github.com/andysalerno/r9700-serving

Hold on isn't the latest rocm version 7.2.4? Do you mean you're on 7.1.3? In that case I should be on an even newer rocm, but I might have to try your specific rocm 7.1.3 if that might solve the issue. Thanks for sharing your repo.

> It requires some understanding of containers to make it work, but if you have [just](https://github.com/casey/just) and podman/docker installed then I think `just build-images` followed by `just up` should work. (You can check some of the configs that also let you pick nightly rocm, nightly AITER, nightly vllm, etc).
> 
> Also I know I'm repeating myself here but I'm not a gpu programming expert - I just know the patches in my repo works for my scenarios and the output is extremely fast and also correct (according to my own benchmarks).

I'm usually anti using containers like docker and podman, but maybe with AMD GPUs or even Intel this might become neccesary. I just never needed them for Nvidia and liked my super easy bare metal installs where I can edit the code as needed easily. I'll check your repo and try to follow the instructions.



### andysalerno · 2026-07-12

@Nero10578 7.13 (and newer) are in preview and available for use: https://rocm.docs.amd.com/en/7.13.0-preview/index.html

They did a weird version number bump at some point, so now it's 7.13+.

> I'm usually anti using containers like docker and podman

it's personal bias but containers are *perfect* for exactly these problems, since you can have multiple container environments with different rocm versions to try things out. And if the containers work on my machine, it's very likely they work on yours (not guaranteed but much more likely)

### Nero10578 · 2026-07-12

> [@Nero10578](https://github.com/Nero10578) 7.13 (and newer) are in preview and available for use: https://rocm.docs.amd.com/en/7.13.0-preview/index.html
> 
> They did a weird version number bump at some point, so now it's 7.13+.

OH! What the heck...I guess I will try that, its definitely newer because its a preview build...

> > I'm usually anti using containers like docker and podman
> 
> it's personal bias but containers are _perfect_ for exactly these problems, since you can have multiple container environments with different rocm versions to try things out. And if the containers work on my machine, it's very likely they work on yours (not guaranteed but much more likely)

True, its good for these kinds of issues. I just like to be on the bleeding edge and messing with the vllm code myself so I usually don't even bother with containers on my Nvidia servers.



### xy7ra · 2026-09-05

Data point for the tracker — full stack test on 2× Radeon AI PRO R9700 (gfx1201), 2026-09-04, in a container on the **ROCm 10.1.0a20260822 wheel nightly** (HIP 7.16, torch 2.15.0a0+rocm10.1.0a20260822, triton 3.8.0+git3f6e4113) with **aiter main @ 456b9278** built from source (JIT, `GPU_ARCHS=gfx1201`) and vLLM main @ 3f41d10 built for gfx1201.

**Works on gfx1201 (correct vs torch reference):**
- HIP JIT kernels: `rms_norm`, `silu_and_mul`, `per_tensor/per_token/per_group(1x128)` FP8 quant (dtype is `float8_e4m3fn`, correct), `rope_fwd`, `moe_sorting`.
- `aiter.gemm_a8w8_blockscale` auto-dispatch → Triton; correct. Triton FP8 block-scale GEMM vs torch FP16: 1.15–1.3× at M≥256, 1.7–3× at M=1 on wide shapes (25600×5120, 7168×7168), 0.7–0.9× at M=1 for 5120×5120.
- **FlyDSL flash attention (`flydsl_flash_attn_func`, the gfx1201 backend): correct, 69 TFLOPS vs 34 for torch SDPA on B=1 S=2048 H=16 D=128 causal (2×).** It only works if `$(rocm-sdk path --root)/lib/llvm/bin` (ld.lld) is on PATH with the wheel-based ROCm; otherwise FlyDSL dies with `lld invocation failed`. Worth a friendlier error or auto-detection.
- Triton `unified_attention` at a small config, and end-to-end in vLLM as `ROCM_AITER_UNIFIED_ATTN` on Qwen3-32B-FP8 / DeepSeek-R1-Distill-Qwen-32B-FP8 TP=2 (eager) — coherent output. (Different model than #5229; no LDS overflow hit here.)

**Still not working on gfx1201:**
- CK `gemm_a8w8` (int8) and CK / CK-tile `gemm_a8w8_blockscale`: no gfx12 instances are generated (`gemm_a8w8_manifest.h`, `*_lookup.h` not found) — the Python gates in `gemm_op_a8w8.py` correctly route around them.
- Top-level `aiter.flash_attn_func`: the CK fmha module JIT-compiles for gfx1201 (134 s) then raises `invalid argument for fmha_fwd`.
- Triton `gemm_a16w16`: `configs/gfx1201/triton/gemm/gemm_a16w16/DEFAULT.json` is missing → AssertionError.
- **`fused_moe` BF16 (2-stage default → `module_moe_ck2stages_*`) JIT-compiles and runs on gfx1201 but the output is garbage** (relerr 1.4 vs `aiter.fused_moe.torch_moe`, tokens=256 E=64 topk=8 dim=2048 inter=768). Unlike the a8w8 GEMMs this path is not gated for RDNA, so it fails silently.
- **Triton `gemm_a8w8_blockscale` split-K bug** (NaN when `K/NUM_KSPLIT` is not a multiple of `BLOCK_SIZE_K`; hit by the gfx1201 `DEFAULT.json` `NUM_KSPLIT=8` at K=12800 = Qwen3-32B down_proj TP=2). Filed separately with repro + patch: see the linked issue below. With that patch, vLLM's `AiterFp8BlockScaledMMKernel` on Qwen3-32B-FP8 TP=2 is coherent and **+5/+10/+12 %** over vLLM's native Triton block-scale kernel (27.2 / 78.0 / 204.3 tok/s at 1/3/8 streams vs 25.8 / 71.1 / 182.5).

Full matrix, scripts and logs: happy to attach if useful.

Split-K bug: https://github.com/ROCm/aiter/issues/5286


### kulminaator · 2026-09-14

> ....
> I tried these vllm patches, but at least on latest vllm main and latest rocm 7.2.4 right now I am getting the "AITER unified-attention kernel needs 66 KB of LDS and gfx1201 only allows 64 KB" error so I can't run anything. How did you get past that for vllm? I'd need to modify aiter itself and rebuild/install it from source to set num_stages=1?

Btw, still stumbled on that a few weeks ago, even on patched vllm instances. The 66KB LDS issue comes up if you try to use BF16 kvcache or an W8A16 model, something along the lines. It does not show up if throw in the towel and just go for fp8.  I think i hit that path on the radiance vllm port (and perhaps there the fp8 took a special path, thus didn't crash like hell).

But fp8 is not enough for me.
