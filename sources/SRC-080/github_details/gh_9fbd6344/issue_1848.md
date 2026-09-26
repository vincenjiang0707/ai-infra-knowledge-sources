# [Issue #1848] [Puzzletron] Standalone export fails for heterogeneous distilled checkpoints

source: https://github.com/NVIDIA/Model-Optimizer/issues/1848
state: open | updated: 2026-08-02T22:08:33Z
labels: bug, investigating, torch.pruning

## 正文

modelopt branch: main
container: nemo 26.02

 The documented[ command](https://github.com/NVIDIA/Model-Optimizer/blob/main/examples/megatron_bridge/README.md#distillation) for exporting an intermediate distillation checkpoint fails for heterogeneous Puzzletron models:

  uv run python /opt/Megatron-Bridge/examples/conversion/convert_checkpoints.py export \
    --hf-model <pruned_hf_checkpoint> \
    --megatron-path <distillation_dir>/checkpoints/iter_0000060 \
    --hf-path <output_hf_checkpoint>

  Exporting the final checkpoint inline through distill.py --hf_export_path --student_hf_model works. 

The standalone exporter appears not to register Puzzletron’s custom Megatron-Bridge adapters or reproduce the full-model-template export path used by
distill.py.


## 评论 (4)

### github-actions[bot] · 2026-07-20

Issue has not received an update in over 14 days. Adding stale label.

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: 827342f22fb1074ada0d0e6cc98bf4a40a34f2cb41ff1ffc802c54cea0f49e97

This open issue is in the ModelOpt release sweep. Owner: confirm release impact, linked fix/validation, or that it is non-blocking for this release.

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: 7daff41e6e695381f67e9cd842491dc6aaaa083e6b38655abeb9d4c6cc207ef3

This open issue is in the ModelOpt release sweep. Owner: confirm release impact, linked fix/validation, or that it is non-blocking for this release.

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: 4c7a5d91232e6b62d6e9055f13cefd759192e5fd9d68ef4dce6e76afb81b0907

Release follow-up: this open ModelOpt issue needs release relevance confirmed. Link its planned fix/validation, or confirm it is not a v0.46.0 blocker.
