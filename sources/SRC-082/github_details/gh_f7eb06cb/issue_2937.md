# [Issue #2937] [Windows] ExLlamaV2 kernels are gated to Linux, but compile and produce correct output on Windows once linking is fixed

source: https://github.com/ModelCloud/GPTQModel/issues/2937
state: closed | updated: 2026-07-09T09:31:42Z
labels: 

## 正文

## Summary

`ExllamaV2Linear` and `AwqExllamaV2Linear` declare `SUPPORTS_PLATFORM = [PLATFORM.LINUX]`, so on
Windows they are excluded from kernel auto-selection, and forcing `backend="exllama_v2"` raises:

```
ValueError: <class 'gptqmodel.nn_modules.qlinear.exllamav2_awq.AwqExllamaV2Linear'>
does not support platform: win32
```

After fixing the Windows link failure (#2936) and locally changing the gate to
`[PLATFORM.LINUX, PLATFORM.WIN32]`, both kernels build, load, and produce correct output on
Windows — and they are the fastest kernels available there.

## Measurements

Qwen2-VL-2B-Instruct, RTX 3050 Ti Laptop 4 GB (SM 8.6), Windows 11, torch 2.6.0+cu124,
gptqmodel 7.1.0, greedy decoding, mean over a fixed 3-image document-understanding set with
keyword-recall scoring against ground truth:

| Checkpoint | Kernel | Decode tok/s | s/case | Accuracy |
|---|---|---|---|---|
| GPTQ-Int4 | TritonV2 (auto-selected) | 5.3 | 14.1 | 94% |
| GPTQ-Int4 | **ExLlamaV2 (forced)** | **7.6** | **9.6** | **94%** |
| AWQ | AwqGEMMTriton (auto-selected) | 6.1 | 10.4 | 78% |
| AWQ | AwqGEMM (compiled native) | 4.9 | 13.3 | 78% |
| AWQ | **ExLlamaV2 (forced)** | **6.7** | **9.1** | **78%** |

Accuracy is identical to the other kernels in every case (same per-case keyword hits/misses),
so the numerics look correct on win32.

## Ask

Was the Linux gate a deliberate correctness decision, or just "untested on Windows"? If the
latter, would you accept a PR enabling `PLATFORM.WIN32` for the ExLlamaV2 kernels (possibly
behind an env flag until CI coverage exists)? Happy to share more benchmark details.


## 评论 (1)

### Qubitium · 2026-07-03

@xXpeira12 Yes, we do not have an windows env to deploy and test on. Feel free to submit PR to fix the kernel compat for windows. Thanks!
