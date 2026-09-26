# [Issue #1875] NVFP4 quantized (shared) lm_head fails fake-quant in training forward: ScaledE4M3Function 'Only support E=4 & M=3'

source: https://github.com/NVIDIA/Model-Optimizer/issues/1875
state: open | updated: 2026-08-02T22:08:36Z
labels: bug, investigating, torch.quantization

## 正文

### Summary
When an NVFP4-quantized `output_layer`/`lm_head` (weight quantizer `num_bits: e2m1`, block scale `e4m3`) is exercised in the **training forward** (not just PTQ/export), `_fake_quantize` routes into `ScaledE4M3Function.forward` (`modelopt/torch/quantization/tensor_quant.py`), which raises `NotImplementedError("Only support E=4 & M=3 for now.")` because the NVFP4 weight format is E2M1, not E4M3.

### Repro context
QAD (KD) on a hybrid-MoE model that has an MTP head, with the MTP loss enabled (#1805). The main LM head is skipped via `skip_lm_loss`, so PTQ/export never hit this path — but the MTP head shares the quantized `output_layer` and calls it during the MTP loss, triggering fake-quant in the training forward. Traceback: `process_mtp_loss -> output_layer -> quant_linear -> tensor_quantizer._fake_quantize -> tensor_quant.py:436`.

### Impact / workaround
Blocks keeping `lm_head`/`output_layer` quantized (NVFP4) when the MTP head is involved during QAD. Workaround: keep `lm_head`/`output_layer` in BF16. A proper fix would let the NVFP4 weight quantizer fake-quant correctly in the training forward instead of dispatching to the E4M3-only path.

Verified on modelopt main `973cb09cb`. cc @AAnoosheh (#1805)

## 评论 (4)

### github-actions[bot] · 2026-07-19

Issue has not received an update in over 14 days. Adding stale label.

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: 97b0dd60788e87a93314c11a9080b8aabf3bdca4eca8158fe7ae3d4dffdd9829

This open issue is in the ModelOpt release sweep. Owner: confirm release impact, linked fix/validation, or that it is non-blocking for this release.

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: 5a6c176ef4af2d69b74ad734f75f5dd4d55e4e82387278d473401ccab2973dba

This open issue is in the ModelOpt release sweep. Owner: confirm release impact, linked fix/validation, or that it is non-blocking for this release.

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: 50b1b79323ce4753f0f00dd0042dbefb42f3559799d0f791efeed6acaa051017

Release follow-up: this open ModelOpt issue needs release relevance confirmed. Link its planned fix/validation, or confirm it is not a v0.46.0 blocker.
