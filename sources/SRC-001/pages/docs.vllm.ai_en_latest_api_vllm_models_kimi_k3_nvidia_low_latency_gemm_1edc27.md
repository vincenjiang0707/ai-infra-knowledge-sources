source: https://docs.vllm.ai/en/latest/api/vllm/models/kimi_k3/nvidia/low_latency_gemm/
lastmod: 2026-09-24

#

`vllm.models.kimi_k3.nvidia.low_latency_gemm`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.low_latency_gemm)

Kimi-K3 decode GEMM selection for unquantized BF16 on SM90/SM100/SM103/SM107.

Dispatch is purely by local `(N, K)`

shape and token count `M`

— the module name plays no role. Each measured shape maps to a :class:`ProjectionSpec`

holding the winning backend per token count. The static part of the decision is resolved once per module at install time into a small `{M: call}`

plan, so the per-forward path is a single dict lookup.

The supported capabilities carry separate measured tables: :data:`KIMI_K3_PROJECTIONS`

was tuned on B300 (SM103), :data:`KIMI_K3_PROJECTIONS_SM100`

on B200 (SM100), and :data:`KIMI_K3_PROJECTIONS_SM90`

on H200 (SM90). The per-(shape, M) winners genuinely differ between the parts, so the tables must not be merged. SM107 (Rubin) reuses the SM103 table: the plan was validated end-to-end on SM107 hardware, but the per-M crossovers have not been re-measured there and may deserve their own table once retuned.

Functions:

-
–[autotune_kda_qkvg](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.low_latency_gemm.autotune_kda_qkvg)Autotune the supported QKVG GEMM before CUDA graph capture.

-
–[enable_kimi_k3_low_latency_gemm](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.low_latency_gemm.enable_kimi_k3_low_latency_gemm)Install shape-selected low-latency GEMMs and register CuTe warmups.

-
–[run_kda_projection_overlap](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.low_latency_gemm.run_kda_projection_overlap)Run the TP8 KDA decode projection branches concurrently.

-
–[select_kimi_k3_backend](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.low_latency_gemm.select_kimi_k3_backend)Backend for a local

`(N, K)`

at`num_tokens`

, or None to fall back. -
–[try_low_latency_gemm](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.low_latency_gemm.try_low_latency_gemm)Run the shape-selected low-latency kernel, or None to fall back.


##

`_KimiK3LowLatencyApply`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.low_latency_gemm._KimiK3LowLatencyApply)

Mixin: try the precomputed plan, else defer to the base method.

## Source code in `vllm/models/kimi_k3/nvidia/low_latency_gemm.py`


##

`_kda_qkvg_flashinfer_backend()`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.low_latency_gemm._kda_qkvg_flashinfer_backend)

Return the tested FlashInfer backend for the low-M QKVG branch.

FlashInfer's `cute-dsl`

BF16 GEMM supports SM100 and SM103, but rejects SM90 during backend validation. Other capabilities use `torch.mm`

for QKVG while retaining the concurrent F_A/beta and F_B branch.

## Source code in `vllm/models/kimi_k3/nvidia/low_latency_gemm.py`


##

`_low_latency_table()`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.low_latency_gemm._low_latency_table)

Measured dispatch table for the current device, or None if unsupported.

## Source code in `vllm/models/kimi_k3/nvidia/low_latency_gemm.py`


##

`autotune_kda_qkvg(model)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.low_latency_gemm.autotune_kda_qkvg)

Autotune the supported QKVG GEMM before CUDA graph capture.

## Source code in `vllm/models/kimi_k3/nvidia/low_latency_gemm.py`


##

`enable_kimi_k3_low_latency_gemm(module, dtype)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.low_latency_gemm.enable_kimi_k3_low_latency_gemm)

Install shape-selected low-latency GEMMs and register CuTe warmups.

Modules are matched purely by type, an exactly-unquantized method, and a local `(N, K)`

present in the current device's measured table (:data:`KIMI_K3_PROJECTIONS`

on SM103, :data:`KIMI_K3_PROJECTIONS_SM100`

on SM100, :data:`KIMI_K3_PROJECTIONS_SM90`

on SM90).

## Source code in `vllm/models/kimi_k3/nvidia/low_latency_gemm.py`


|
|

##

`run_kda_projection_overlap(hidden_states, packed_weight, f_b_weight, aux_stream, events)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.low_latency_gemm.run_kda_projection_overlap)

Run the TP8 KDA decode projection branches concurrently.

Parameters:

-

(`hidden_states`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.low_latency_gemm.run_kda_projection_overlap(hidden_states))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Packed BF16 input with shape

`[M, 7168]`

. -

(`packed_weight`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.low_latency_gemm.run_kda_projection_overlap(packed_weight))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Existing Q/K/V/G/F_A/beta/pad weight with shape

`[6288, 7168]`

. -

(`f_b_weight`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.low_latency_gemm.run_kda_projection_overlap(f_b_weight))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)F_B weight with shape

`[1536, 128]`

. -

(`aux_stream`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.low_latency_gemm.run_kda_projection_overlap(aux_stream))

) –[Stream](https://pytorch.org/docs/stable/generated/torch.cuda.Stream_class.html#torch.cuda.Stream)Stream for the F_A/beta then F_B branch.

-

(`events`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.low_latency_gemm.run_kda_projection_overlap(events))

) –[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Event](https://pytorch.org/docs/stable/generated/torch.cuda.Event.html#torch.cuda.Event),[Event](https://pytorch.org/docs/stable/generated/torch.cuda.Event.html#torch.cuda.Event)]Start and completion events for the stream fork and join.


Returns:

## Source code in `vllm/models/kimi_k3/nvidia/low_latency_gemm.py`


|
|

##

`select_kimi_k3_backend(num_tokens, n, k, *, has_residual=False)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.low_latency_gemm.select_kimi_k3_backend)

Backend for a local `(N, K)`

at `num_tokens`

, or None to fall back.

## Source code in `vllm/models/kimi_k3/nvidia/low_latency_gemm.py`


##

`try_low_latency_gemm(x, weight, residual=None)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.low_latency_gemm.try_low_latency_gemm)

Run the shape-selected low-latency kernel, or None to fall back.

Resolves the plan from the shape table on each call; production installs a precomputed plan (see :func:`enable_kimi_k3_low_latency_gemm`

) and does not use this path.