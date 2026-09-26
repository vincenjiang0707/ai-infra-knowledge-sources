# [Issue #1865] Support for INT4_AWQ quantization for Nemotron-3-Nano-30B-A3B

source: https://github.com/NVIDIA/Model-Optimizer/issues/1865
state: open | updated: 2026-08-02T22:08:51Z
labels: bug, torch.quantization, fw-megatron

## 正文

**Before submitting an issue, please make sure it hasn't been already addressed by searching through the [existing and past issues](https://github.com/NVIDIA/Model-Optimizer/issues?q=is%3Aissue).**

## Describe the bug
Quantization for Nemotron-3-Nano-30B-A3B  using INT4_AWQ faces several issues. 

### Steps/Code to reproduce bug
Followed the tutorial https://github.com/NVIDIA/Model-Optimizer/tree/main/examples/megatron_bridge/tutorials/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16, then modified the flags to run on GB200 and quant config to INT4_AWQ_CFG. All steps run fine for "MAMBA_MOE_FP8_CONSERVATIVE_CFG" quantization on GB200. Issues arise when quantization flag changed to INT4_AWQ_CFG.

When I run the command

torchrun --nproc_per_node 4 quantize.py \
    --hf_model_name_or_path nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16 \
    --trust_remote_code \
    --tp_size 4 \
    --quant_cfg INT4_AWQ_CFG \
    --calib_batch_size 4 \
    --seq_length 8192 \
    --export_megatron_path /opt/Model-Optimizer/output/iter_0000800_int4_megatron \
    --skip_generate

I get several errors

**Error:**
```
AttributeError: 'QuantTEColumnParallelGroupedLinear' object has no attribute 'weight'. Did you mean: 'weight0'?
```
**File:** `modelopt/torch/quantization/model_calib.py` ~line 1358

**Root cause:** `awq_lite()` iterates all quantized linear modules and calls `AWQLiteHelper(module, name)`,
which unconditionally accesses `module.weight`. TE's fused MoE grouped linear exposes weights as
`weight0`, `weight1`, ... not `weight`. The smooth-quant path already handles this correctly
(line 755: `getattr(module, "weight", None)`) — `awq_lite` was missing the same guard.


### 2. `AssertionError: TEGroupedLinear only supports per-tensor quantization`

**Error:**
```
AssertionError: TEGroupedLinear only supports per-tensor quantization
```

**File:** `modelopt/torch/quantization/plugins/megatron.py` ~line 696

**Root cause:** `_QuantMegatronTEGroupedLinear._process_quantizer_amax` asserted `v.numel() == 1`,
written only for FP8 (per-tensor amax). INT4 AWQ per-block quantization produces a multi-element
amax tensor (block_size=128), which fails the assert during checkpoint save.

### Expected behavior

### Who can help?

<!-- To expedite the response to your issue, it would be helpful if you could identify the appropriate person(s) to tag using the @ symbol.
If you are unsure about whom to tag, you can leave it blank, and we will make sure to involve the appropriate person. -->

- ?

## System information

<!-- Run this script to automatically collect system information: https://github.com/NVIDIA/Model-Optimizer/blob/main/.github/ISSUE_TEMPLATE/get_system_info.py -->

- Container used (if applicable): nvcr.io/nvidia/nemo:26.04
- OS (e.g., Ubuntu 22.04, CentOS 7, Windows 10): Ubuntu 24.04.3 LTS
- CPU architecture (x86_64, aarch64): aarch64
- GPU name (e.g. H100, A100, L40S): NVIDIA GB200
- GPU memory size: 185.0 GB
- Number of GPUs: 4
- Library versions (if applicable):
  - Python: 3.12.3
  - ModelOpt version or commit hash: 0.44.0rc1
  - CUDA: 13.1
  - Transformers: 4.57.3
- Any other details that may help: ?


## 评论 (3)

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: 0f888e735a09b8b574e0b1b0d908952644b91205b45617b3483da2008ac728a4

This open issue is in the ModelOpt release sweep. Owner: confirm release impact, linked fix/validation, or that it is non-blocking for this release.

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: 0ebaa6d0f9ec8f721f3d2f85cd19c9c897473f9ee8d2d4d2d3691f2c637e70a4

This open issue is in the ModelOpt release sweep. Owner: confirm release impact, linked fix/validation, or that it is non-blocking for this release.

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: 22a1dedd9fd11d6760833cd0a33b5de21e968a54d1822210ea2360c106322e19

Release follow-up: this open ModelOpt issue needs release relevance confirmed. Link its planned fix/validation, or confirm it is not a v0.46.0 blocker.
