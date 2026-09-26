# [Issue #2392] [ROCm][gfx1151] triton performance regression since migrating to aiter (PR #2230)

source: https://github.com/Dao-AILab/flash-attention/issues/2392
state: closed | updated: 2026-06-01T17:58:12Z
labels: 

## 正文

## Summary

I've been running a vision-language (VL) model through vLLM and using flash-attention (triton backend) for vision transformer (ViT) prefill attention. PR #2230 (merged March 12, 2026) migrated the ROCm Triton backend from built-in kernels to external kernels in [ROCm/aiter](https://github.com/ROCm/aiter). This change results in up to 3.7× slower ViT attention computation on a gfx1151 GPU, which affects TTFT (ViT attention is done in the encoding stage).

While I've only tested this on qwen2.5-VL-7B-Instruct, the performance hit may extend to other models and/or RDNA GPUs as well. It may be that the aiter kernel(s) haven't yet been fully optimized for this platform, and can be brought up to match the old kernel performance.

## Environment info
OS: Ubuntu 24.04.03 LTS
CPU: AMD RYZEN AI MAX+ 395 w/ Radeon 8060S
GPU: AMD RDNA (gfx1151)

ROCm: 7.12.0a20260208 nightly package (python 3.12)
triton: 3.6.0+rocm7.12.0a20260208
torch: 2.10.0+rocm7.12.0a20260208
vLLM: 0.17.0rc1.dev363+g74ae947b9.rocm712.mgehre (built from custom fork, but upstream should also work)

## Steps to reproduce (vLLM)

Build flash-attention from before PR #2230
```bash
git clone https://github.com/Dao-AILab/flash-attention.git
cd flash-attention
git checkout bbe25ba  # Last commit before #2230 merge
FLASH_ATTENTION_TRITON_AMD_ENABLE=TRUE pip install --no-build-isolation .
```

Terminal 1: start vLLM sever with profiling
```bash
FLASH_ATTENTION_TRITON_AMD_ENABLE=TRUE vllm serve Qwen/Qwen2.5-VL-7B-Instruct \
    --port 8000 \
    --max-model-len 8192 \
    --gpu-memory-utilization 0.9 \
    --dtype float16 \
    --enforce-eager \
    --max-num-seqs 1 \
    --disable-log-requests \
    --profiler-config '{"profiler": "torch", "torch_profiler_dir": "./vllm_profile"}'
```

Terminal 2: run vLLM benchmark. It may be worth running ~10 warmup prompts first for more stable data.
```bash
vllm bench serve \
    --model Qwen/Qwen2.5-VL-7B-Instruct \
    --port 8000 \
    --num-prompts 10 \
    --random-input-len 1 \ # Text tokens - minimized to isolate ViT stage
    --random-output-len 1 \
    --backend openai-chat \
    --endpoint /v1/chat/completions \
    --dataset-name random-mm \
    --random-mm-base-items-per-request 1 \
    --random-mm-limit-mm-per-prompt '{"image": 1}' \
    --random-mm-bucket-config '{(2048, 2048, 1): 1.0}' # Adjust to desired image size

# Check profiler output for vision encoder GPU time
grep "flash_attn.*varlen_forward" ./vllm_profile/profiler_out_0.txt  
```

Then update flash-attention to commit 3f94643 (or later), rebuild and repeat the benchmark.

## Performance Regression Data

### Vision Encoder GPU Time (flash_attn::_flash_attn_varlen_forward)
Note: GPU time totals show the sum of all calls over 10 prompts.

| Image Size | Tokens | Built-in Triton (pre-PR #2230) | Aiter Triton (post-PR #2230) | Regression |
|------------|--------|--------------------------------|------------------------------|------------|
| 512×512    | 341    | 45.1ms                         | 100.0ms                      | 2.2× slower |
| 1024×1024  | 1,361  | 452.8ms                        | 1,288ms                      | 2.8× slower |
| 2048×2048  | 5,329  | 5,370ms                        | 19,955ms                     | 3.7× slower |

### Mean Time to First Token (TTFT)

| Image Size | Built-in Triton | Aiter Triton | Difference |
|------------|-----------------|--------------|------------|
| 512×512    | 229ms           | 241ms        | +5% |
| 1024×1024  | 868ms           | 1,058ms      | +22% |
| 2048×2048  | 4,593ms         | 7,429ms      | +62% |


## 评论 (5)

### micmelesse · 2026-03-26

I will take a look and get back to you.

### micmelesse · 2026-03-27

I ran Qwen2.5-VL-7B 1024x1024 on gfx1100 using `rocm/vllm-dev:upstream_preview_releases_v0.17.0_20260303` and I don't see a regression. The pre and post #2230 TTFT are within noise. I think this might be gfx1151-specific.

Could you try with the latest aiter and re-run your post-#2230 benchmark? There have been RDNA kernel config updates since the version bundled in flash-attention that might help. I will try and find a gfx1151 node if it does not help

```bash
cd flash-attention
cd third_party/aiter && git fetch origin && git checkout origin/main && cd ../..
FLASH_ATTENTION_TRITON_AMD_ENABLE=TRUE pip install --no-build-isolation .
  ```

### skysnow2001 · 2026-03-30

Could you share the docker image you used @amd-callumm ?

### amd-callumm · 2026-03-31

@micmelesse I reran post-#2230 benchmarks with the latest aiter, and saw a huge improvement, getting close to the pre-migration performance. Looks like the RDNA kernel updates were one of two significant factors in the performance dip I saw.

The other factor, it turns out, is the Triton version. My pre-#2230 benchmarks were using Triton 3.6.0, whereas I see that the aiter backend includes a `triton==3.5.1` dependency. When I override this to use Triton 3.6.0, for post-migration benchmarks, with the latest aiter upstream, I see performance very similar to my pre-migration results with Triton 3.6.0.

**Triton 3.5.1 results (10-prompt total kernel time)**
| Image Size | Pre-migration | Latest aiter | Speed |
|------------|-----------------|--------------|------------|
| 512×512      | 65.4ms         | 52.3ms        | +25% |
| 1024×1024  | 664.9ms       | 504.6ms      | +32% |
| 2048×2048  | 9,594ms       | 6,418ms      | +49% |

**Results with the latest aiter (10-prompt total kernel time)**
| Image Size | Triton 3.5.1 | Triton 3.6.0 | Speed |
|------------|-----------------|--------------|------------|
| 512×512      | 52.3ms         | 44.3ms        | +18% |
| 1024×1024  | 504.6ms       | 430.5ms      | +17% |
| 2048×2048  | 6,418ms       | 5,457ms      | +18% |

Overall performance ranking: (latest aiter, 3.6.0) ~ (pre-migration, 3.6.0) > (latest aiter, 3.5.1) > (pre-migration, 3.5.1) > (post-migration + current aiter, 3.5.1 OR 3.6.0)

What this means is two-fold. First, the regression is likely GPU-specific, and can be fully recovered and them some simply by updating the aiter submodule to include recent improvements. Second, there may be further performance improvements on the table by upgrading the Triton dependency version, but confirming this seems like it would warrant a broader sweep of benchmarks/testing than just one VL model.

@skysnow2001 I unfortunately don't have a docker image to share - I've just been using a virtual environment with the needed packages.

### micmelesse · 2026-06-01

@amd-callumm Hey, sorry for the delay. I have a PR that bumps the Triton floor to `>=3.6.0` and updates the aiter submodule. See https://github.com/Dao-AILab/flash-attention/pull/2614. Can you check if everything is good for you?
