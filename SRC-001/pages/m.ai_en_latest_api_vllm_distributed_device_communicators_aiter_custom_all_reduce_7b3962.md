source: https://docs.vllm.ai/en/latest/api/vllm/distributed/device_communicators/aiter_custom_all_reduce/
lastmod: 2026-09-23

#

`vllm.distributed.device_communicators.aiter_custom_all_reduce`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.aiter_custom_all_reduce)

vLLM-owned wrapper over AITER's `CustomAllreduce`

.

vLLM's `CudaCommunicator`

stores one of these as `aiter_ar_comm`

(when `VLLM_ROCM_USE_AITER_CUSTOM_AR`

is set) so the plain allreduce and the fused allreduce+RMSNorm path share a single AITER instance with its IPC buffers.

Classes:

##

`AiterCustomAllreduce`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.aiter_custom_all_reduce.AiterCustomAllreduce)

Methods:

-
–[build_supports_per_group_quant](https://docs.vllm.ai#vllm.distributed.device_communicators.aiter_custom_all_reduce.AiterCustomAllreduce.build_supports_per_group_quant)True if the running AITER build exposes the per-group AR+RMS+quant

-
–[effective_max_size](https://docs.vllm.ai#vllm.distributed.device_communicators.aiter_custom_all_reduce.AiterCustomAllreduce.effective_max_size)Max input byte size eligible for AITER custom allreduce.

-
–[use_1stage_fused_ar_rms](https://docs.vllm.ai#vllm.distributed.device_communicators.aiter_custom_all_reduce.AiterCustomAllreduce.use_1stage_fused_ar_rms)Whether AITER's fused allreduce+RMSNorm runs as its one-stage kernel.


Attributes:

-
([supports_dynamic_hidden_dim](https://docs.vllm.ai#vllm.distributed.device_communicators.aiter_custom_all_reduce.AiterCustomAllreduce.supports_dynamic_hidden_dim)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Aiter's fused_allreduce_rmsnorm kernel dispatches on hidden_dim.


## Source code in `vllm/distributed/device_communicators/aiter_custom_all_reduce.py`


|
|

###

`supports_dynamic_hidden_dim`

`property`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.aiter_custom_all_reduce.AiterCustomAllreduce.supports_dynamic_hidden_dim)

Aiter's fused_allreduce_rmsnorm kernel dispatches on hidden_dim. Before aiter v0.1.12 the launcher was template-specialized on HIDDEN_DIM and silently no-op'd for sizes outside {512, 1024, 2048, 4096}. From v0.1.12 hidden_dim is a runtime argument. Older builds are detected via AiterCustomAllreduce.supports_dynamic_hidden_dim; This function is used to skip fusion for unsupported sizes on them. Ref (old kernel): https://github.com/ROCm/aiter/blob/6a0e7b26ccf33164785531212cc2ec2cde0b9243/csrc/include/custom_all_reduce.cuh#L2590

###

`build_supports_per_group_quant()`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.aiter_custom_all_reduce.AiterCustomAllreduce.build_supports_per_group_quant)

True if the running AITER build exposes the per-group AR+RMS+quant kernel (added in ROCm/aiter PR #2823).

The pattern registration in `RocmAiterAllReduceFusionPass`

keys off this so vLLM degrades to the AR+RMS-only fusion when run against an older aiter that lacks the per-group launcher.

## Source code in `vllm/distributed/device_communicators/aiter_custom_all_reduce.py`


###

`effective_max_size()`

`classmethod`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.aiter_custom_all_reduce.AiterCustomAllreduce.effective_max_size)

###

`use_1stage_fused_ar_rms(inp)`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.aiter_custom_all_reduce.AiterCustomAllreduce.use_1stage_fused_ar_rms)

Whether AITER's fused allreduce+RMSNorm runs as its one-stage kernel.

Mirrors the launcher contract of aiter's `fused_allreduce_rmsnorm`

(csrc/include/custom_all_reduce.cuh): rows of 16-byte packs, at most 1024 packs per row, at most 80 tokens, and the byte cap of the one-stage custom allreduce for this TP size and topology. Outside it the fused op runs the two-stage variant (cross-device reduce-scatter + local norm), which is slower than an explicit `all_reduce`

+ norm, so callers that can fall back should require this. Capture-static: depends only on shape, dtype, TP size and topology.