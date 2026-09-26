source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/warmup/qwen_triton_warmup/
lastmod: 2026-09-24

Warm Qwen GDN Triton kernels reported by the JIT monitor.

## Source code in `vllm/model_executor/warmup/qwen_triton_warmup.py`


| @torch.inference_mode()
def qwen_triton_warmup(
runner: "GPUModelRunner",
model_config: "ModelConfig",
) -> None:
"""Warm Qwen GDN Triton kernels reported by the JIT monitor."""
model_type = getattr(model_config.hf_text_config, "model_type", "") or getattr(
model_config.hf_config, "model_type", ""
)
if model_type not in _QWEN_MODEL_TYPES:
return
device = runner.device
logger.info("Warming up Qwen GDN Triton kernels for model_type=%s.", model_type)
gdn_config = _qwen_gdn_warmup_config(
runner.compilation_config.static_forward_context
)
if gdn_config is None:
return
max_num_tokens = max(1, int(runner.max_num_tokens))
_warm_gated_rms_norm_kernel(device, gdn_config, max_num_tokens, model_config.dtype)
_warm_causal_conv1d_fwd_kernel(device, gdn_config)
_warm_fused_post_conv_kernel(device, gdn_config)
# Pooling only runs full prefills; the decode update kernel is unused.
if not runner.is_pooling_model:
_warm_fused_sigmoid_gating_delta_rule_update_kernel(device, gdn_config)
_synchronize_device(device)
|