# [Issue #1981] Benchmarking FA on 5070Ti

source: https://github.com/Dao-AILab/flash-attention/issues/1981
state: open | updated: 2026-08-05T19:09:08Z
labels: 

## 正文

Hello, 

I wanted to test FA attention versions on 5070Ti, but the release tag  1.0.0 raised an error ( is not sm 70 or 80 or 90) I'm assuming that at that time since Blackwell was not released, it wouldn't run. What would be the best way to benchmark other versions ? Does 2.0.0 release tag onwards supported on 5070Ti ?

Thanks

Update1: I ran the ```pip install flash-attn --no-build-isolation``` command on wsl2 Ubuntu 24 and the terminal is stuck.

## 评论 (1)

### bvolpato · 2026-08-05

Tested this on an RTX 5070 Ti today. Current FA2 and FA4 both run on SM120, but their performance is different from datacenter Blackwell results.

Environment:

- RTX 5070 Ti, SM120, 16 GB; driver 595.71.05
- Python 3.12.13, PyTorch 2.9.1+cu130
- FA2 2.8.3 CUDA 13 / PyTorch 2.9 release wheel
- FA4 4.0.0.beta25 and current `main` (`5579b12`)
- BF16, warmup 10, 50 timed repetitions; JIT compilation excluded

Representative current-main results (milliseconds, lower is better):

| Workload | FA2 | FA4 | FA4 result |
|---|---:|---:|---:|
| Prefill fwd, MHA, D128, S4K, non-causal | 12.92 | 12.69 | 1.8% faster |
| Prefill bwd, MHA, D128, S4K, non-causal | 32.97 | 41.86 | 27.0% slower |
| Prefill fwd, MHA, D128, S16K, non-causal | 51.43 | 49.93 | 3.0% faster |
| Prefill bwd, MHA, D128, S16K, non-causal | 131.34 | 165.46 | 26.0% slower |
| Prefill fwd, MHA, D128, S16K, causal | 26.23 | 27.68 | 5.5% slower |
| Prefill bwd, MHA, D128, S16K, causal | 64.16 | 79.38 | 23.7% slower |
| Decode fwd, B1, Q1/KV16K, GQA8, D128 | 0.04 | 0.87 | about 22x slower |
| Decode fwd, B32, Q1/KV16K, GQA8, D128 | 0.73 | 0.90 | 23% slower |

Across a broader 1K-16K prefill sweep, FA4 forward stayed within roughly 6% of FA2. FA4 backward was 2-11% slower at D64 and 16-29% slower at D128. Batch-1 decode was much worse because this SM120 path does not support SplitKV; batch 32 reduced that gap.

Eight focused BF16 correctness cases passed for D64/D128, MHA/GQA, causal/non-causal, including backward.

You do not need to build FA2 from source for this setup. Release `v2.8.3.post1` includes this wheel:

```text
flash_attn-2.8.3+cu13torch2.9cxx11abiTRUE-cp312-cp312-linux_x86_64.whl
```

For example:

```bash
gh release download v2.8.3.post1 \
  --repo Dao-AILab/flash-attention \
  --pattern 'flash_attn-2.8.3+cu13torch2.9cxx11abiTRUE-cp312-cp312-linux_x86_64.whl'
pip install ./flash_attn-2.8.3+cu13torch2.9cxx11abiTRUE-cp312-cp312-linux_x86_64.whl
```

One benchmark issue surfaced: FA4's benchmark defaults to automatic `num_splits=0`, while the SM120 path asserted unless it was explicitly `1`. `--num-splits 1` is the current workaround. I opened draft PR #2758 to make automatic selection resolve to the only supported value on SM120.

So the short answer: current FA2 supports the 5070 Ti through the CUDA 13 release wheel. Current FA4 also runs, but on this GPU it is mainly prefill-forward parity, not the large FA4 speedups reported for SM100 datacenter Blackwell.

