# [Issue #1859] fsdp2_aware_weight_update hides the real error with an UnboundLocalError

source: https://github.com/NVIDIA/Model-Optimizer/issues/1859
state: open | updated: 2026-08-02T22:08:34Z
labels: bug, investigating, torch.quantization

## 正文

**Before submitting an issue, please make sure it hasn't been already addressed by searching through the existing and past issues.**

## Describe the bug

`fsdp2_aware_weight_update` (in `modelopt/torch/quantization/utils/core_utils.py`) is a context manager. Its `finally` block uses three variables — `fsdp_param_mapping`, `fsdp_param_group`, and `root_module` — that are only set **after** the `unshard()` call inside the `try`.

So if `unshard()` fails (typically a CUDA OOM when a large FSDP block can't fit on one GPU), the `finally` runs before those variables exist and raises:

```
UnboundLocalError: local variable 'fsdp_param_mapping' referenced before assignment
```

In Python, an error raised inside `finally` replaces the original error. So the real failure (the OOM) is thrown away, and you only see the misleading `UnboundLocalError`. The actual problem becomes very hard to debug.

This shows up during export of large (especially MoE) models, where unsharding a block is most likely to run out of memory.

### Steps/Code to reproduce bug

The simplest deterministic repro: make the in-body `unshard()` raise and confirm the wrong error comes out.

1. Shard a model under FSDP2.
2. Patch the enclosing module's `unshard` to raise any error.
3. Enter `fsdp2_aware_weight_update(model, sharded_module)`.
4. You get `UnboundLocalError` instead of the error you raised.

In the real world this happens on its own: export a large MoE model where one block's `unshard()` all-gather exceeds GPU memory, and the OOM is replaced by the `UnboundLocalError`.

### Expected behavior

If something fails before those variables are set, the `finally` should be a no-op and the original error (e.g. the OOM) should propagate unchanged.

### Who can help?

-

## System information

- OS: Ubuntu 22.04
- CPU architecture: x86_64
- GPU name: H100
- Library versions (if applicable):
  - Python: 3.12
  - ModelOpt version or commit hash: present on current `main`
  - PyTorch: 2.x

## 评论 (4)

### github-actions[bot] · 2026-07-20

Issue has not received an update in over 14 days. Adding stale label.

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: 08c2ec68cf0daed1362b5fa46dadad2f7f1e6957ca6f29bd602f95ea923b246c

This open issue is in the ModelOpt release sweep. Owner: confirm release impact, linked fix/validation, or that it is non-blocking for this release.

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: 4cf3e306816bdf4c4acd20a8463eb087e69078bddde4fde123972a4ba891697b

This open issue is in the ModelOpt release sweep. Owner: confirm release impact, linked fix/validation, or that it is non-blocking for this release.

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: 312b77ee52445f8722a75722c302940e49574a4c6d552e5d85a0b60458c19ccb

Release follow-up: this open ModelOpt issue needs release relevance confirmed. Link its planned fix/validation, or confirm it is not a v0.46.0 blocker.
