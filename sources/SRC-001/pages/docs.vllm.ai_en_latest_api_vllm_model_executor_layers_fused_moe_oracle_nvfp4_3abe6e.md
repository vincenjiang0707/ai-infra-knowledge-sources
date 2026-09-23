source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/oracle/nvfp4/
lastmod: 2026-09-23

def select_nvfp4_moe_backend(
config: FusedMoEConfig,
weight_key: QuantKey | None,
activation_key: QuantKey | None,
) -> tuple[NvFp4MoeBackend, type[mk.FusedMoEExperts]]:
"""Select the primary NvFP4 MoE backend
Note: Shape-specific fallbacks may still occur at runtime.
"""
# NOTE: the kernels are selected in the following order.
# FLASHINFER_B12X is intentionally excluded from auto-selection until
# the upstream CUTLASS SM121 MMA op guard is resolved; use
# moe_backend="flashinfer_b12x" to opt in explicitly.
AVAILABLE_BACKENDS = [
NvFp4MoeBackend.FLASHINFER_TRTLLM,
NvFp4MoeBackend.FLASHINFER_CUTEDSL,
NvFp4MoeBackend.FLASHINFER_CUTEDSL_BATCHED,
NvFp4MoeBackend.FLASHINFER_CUTLASS,
NvFp4MoeBackend.VLLM_CUTLASS,
NvFp4MoeBackend.MARLIN,
NvFp4MoeBackend.HUMMING,
NvFp4MoeBackend.EMULATION,
]
NVFP4_BACKENDS_WITH_CLAMP = {
NvFp4MoeBackend.B12X,
NvFp4MoeBackend.FLASHINFER_TRTLLM,
NvFp4MoeBackend.FLASHINFER_CUTLASS,
NvFp4MoeBackend.FLASHINFER_CUTEDSL,
NvFp4MoeBackend.VLLM_CUTLASS,
NvFp4MoeBackend.MARLIN,
NvFp4MoeBackend.EMULATION,
NvFp4MoeBackend.HUMMING,
}
if config.swiglu_limit is not None:
AVAILABLE_BACKENDS = [
b for b in AVAILABLE_BACKENDS if b in NVFP4_BACKENDS_WITH_CLAMP
]
use_batched = config.moe_parallel_config.use_batched_activation_format
activation_format = (
mk.FusedMoEActivationFormat.BatchedExperts
if use_batched
else mk.FusedMoEActivationFormat.Standard
)
def _make_log_backend(backend: NvFp4MoeBackend):
available_backend_strs = [b.value for b in AVAILABLE_BACKENDS]
return (
f"Using '{backend.value}' NvFp4 MoE backend out "
f"of potential backends: {available_backend_strs}."
)
def _make_log_unsupported(backend: NvFp4MoeBackend, reason: str | None) -> str:
if reason:
return (
f"NvFp4 MoE backend '{backend.value}' does not support the "
f"deployment configuration since {reason}."
)
else:
return (
f"NvFp4 MoE backend '{backend.value}' does not support the "
"deployment configuration."
)
def _return_or_raise(
backend: NvFp4MoeBackend,
config: FusedMoEConfig,
weight_key: QuantKey | None,
activation_key: QuantKey | None,
activation_format: mk.FusedMoEActivationFormat,
) -> tuple[NvFp4MoeBackend, type[mk.FusedMoEExperts]]:
for k_cls in backend_to_kernel_cls(backend):
supported, reason = k_cls.is_supported_config(
k_cls, config, weight_key, activation_key, activation_format
)
if supported:
logger.info_once(_make_log_backend(backend))
return backend, k_cls
raise ValueError(_make_log_unsupported(backend, reason))
# Handle explicit moe_backend from user.
runner_backend = config.moe_backend
if runner_backend != "auto":
requested_backend = map_nvfp4_backend(runner_backend)
if _use_a16(requested_backend, False):
activation_key = None
# For batched activation format, use batched variant if available.
if (
activation_format == mk.FusedMoEActivationFormat.BatchedExperts
and requested_backend == NvFp4MoeBackend.FLASHINFER_CUTEDSL
):
requested_backend = NvFp4MoeBackend.FLASHINFER_CUTEDSL_BATCHED
if (
config.swiglu_limit is not None
and requested_backend not in NVFP4_BACKENDS_WITH_CLAMP
):
raise ValueError(
f"Model sets swiglu_limit={config.swiglu_limit}, but the "
f"explicitly requested moe_backend={runner_backend!r} does "
f"not apply the SwiGLU clamp. Use 'flashinfer_trtllm', "
f"'flashinfer_cutlass', 'flashinfer_cutedsl', 'cutlass', "
f"'b12x', 'marlin', or 'humming' instead."
)
return _return_or_raise(
requested_backend, config, weight_key, activation_key, activation_format
)
# Select kernels in order of backend.
for backend in AVAILABLE_BACKENDS:
for k_cls in backend_to_kernel_cls(backend):
supported, reason = k_cls.is_supported_config(
k_cls,
config,
weight_key,
activation_key,
activation_format,
)
if supported:
logger.info_once(_make_log_backend(backend))
return backend, k_cls
else:
logger.debug_once(_make_log_unsupported(backend, reason))
raise NotImplementedError(
"No NvFp4 MoE backend supports the deployment configuration."
)