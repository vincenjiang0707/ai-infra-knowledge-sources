source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/mamba/ops/ssu_dispatch/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.mamba.ops.ssu_dispatch`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.ssu_dispatch)

Dispatch module for Mamba selective state update (SSU) backends.

Provides a unified `selective_state_update`

function that dispatches to the Triton, FlashInfer, or CPU backend based on the configured `MambaBackendEnum`

. On CPU-only platforms (PowerPC, x86 without CUDA) the backend defaults to 'cpu'.

Classes:

-
–[CPUSSUBackend](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.ssu_dispatch.CPUSSUBackend)CPU SSU backend using the compiled C++ VSX/scalar kernel.

-
–[FlashInferSSUBackend](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.ssu_dispatch.FlashInferSSUBackend)FlashInfer-based SSU backend.

-
–[MambaSSUBackend](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.ssu_dispatch.MambaSSUBackend)Abstract base class for Mamba SSU backends.

-
–[TritonSSUBackend](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.ssu_dispatch.TritonSSUBackend)Triton-based SSU backend (vLLM's default).


Functions:

-
–[flashinfer_replayssm_autotune_supported](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.ssu_dispatch.flashinfer_replayssm_autotune_supported)Return True when FlashInfer exposes ReplaySSM autotuning.

-
–[get_mamba_ssu_backend](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.ssu_dispatch.get_mamba_ssu_backend)Get the current Mamba SSU backend. Raises if not initialized.

-
–[initialize_mamba_ssu_backend](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.ssu_dispatch.initialize_mamba_ssu_backend)Initialize the Mamba SSU backend and optional FlashInfer ReplaySSM.

-
–[reset_replayssm_ring_trackers](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.ssu_dispatch.reset_replayssm_ring_trackers)Reset selected ReplaySSM ring trackers.

-
–[selective_state_update](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.ssu_dispatch.selective_state_update)Unified dispatch for Mamba selective state update.

-
–[selective_state_update_replayssm_flashinfer](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.ssu_dispatch.selective_state_update_replayssm_flashinfer)Run FlashInfer checkpointing SSU and optionally advance shared trackers.

-
–[update_replayssm_ring_trackers](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.ssu_dispatch.update_replayssm_ring_trackers)Reset selected trackers, or advance them when a window is provided.


##

`CPUSSUBackend`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.ssu_dispatch.CPUSSUBackend)

Bases: [MambaSSUBackend](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.ssu_dispatch.MambaSSUBackend)

CPU SSU backend using the compiled C++ VSX/scalar kernel.

On CPU-only platforms (PowerPC, x86 without CUDA) this dispatches to the vectorized C++ kernel registered as `torch.ops._C.selective_state_update_cpu`

. That kernel uses vec_op SIMD intrinsics (VSX on ppc64le, AVX2 on x86, scalar fallback elsewhere) and is parallelised with OpenMP across heads.

Falls back to the pure-PyTorch implementation only if the C++ op is unavailable (e.g. a CPU-less build).

## Source code in `vllm/model_executor/layers/mamba/ops/ssu_dispatch.py`


##

`FlashInferSSUBackend`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.ssu_dispatch.FlashInferSSUBackend)

Bases: [MambaSSUBackend](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.ssu_dispatch.MambaSSUBackend)

FlashInfer-based SSU backend.

## Source code in `vllm/model_executor/layers/mamba/ops/ssu_dispatch.py`


##

`MambaSSUBackend`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.ssu_dispatch.MambaSSUBackend)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

Abstract base class for Mamba SSU backends.

## Source code in `vllm/model_executor/layers/mamba/ops/ssu_dispatch.py`


##

`TritonSSUBackend`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.ssu_dispatch.TritonSSUBackend)

Bases: [MambaSSUBackend](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.ssu_dispatch.MambaSSUBackend)

Triton-based SSU backend (vLLM's default).

## Source code in `vllm/model_executor/layers/mamba/ops/ssu_dispatch.py`


##

`flashinfer_replayssm_autotune_supported()`

`cached`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.ssu_dispatch.flashinfer_replayssm_autotune_supported)

Return True when FlashInfer exposes ReplaySSM autotuning.

## Source code in `vllm/model_executor/layers/mamba/ops/ssu_dispatch.py`


##

`get_mamba_ssu_backend()`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.ssu_dispatch.get_mamba_ssu_backend)

Get the current Mamba SSU backend. Raises if not initialized.

## Source code in `vllm/model_executor/layers/mamba/ops/ssu_dispatch.py`


##

`initialize_mamba_ssu_backend(mamba_config, kv_cache_config, *, use_replayssm=False)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.ssu_dispatch.initialize_mamba_ssu_backend)

Initialize the Mamba SSU backend and optional FlashInfer ReplaySSM.

## Source code in `vllm/model_executor/layers/mamba/ops/ssu_dispatch.py`


##

`reset_replayssm_ring_trackers(ring_start, prev_num_accepted, state_batch_indices, pad_slot_id=NULL_BLOCK_ID)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.ssu_dispatch.reset_replayssm_ring_trackers)

Reset selected ReplaySSM ring trackers.

## Source code in `vllm/model_executor/layers/mamba/ops/ssu_dispatch.py`


##

`selective_state_update(state, x, dt, A, B, C, D, dt_bias, z=None, dt_softplus=False, state_batch_indices=None, dst_state_batch_indices=None, null_block_id=NULL_BLOCK_ID, out=None, num_accepted_tokens=None, cu_seqlens=None, is_blackwell=False)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.ssu_dispatch.selective_state_update)

Unified dispatch for Mamba selective state update.

Delegates to the initialized backend (Triton or FlashInfer).

## Source code in `vllm/model_executor/layers/mamba/ops/ssu_dispatch.py`


##

`selective_state_update_replayssm_flashinfer(state, x, dt, A, B, C, out, x_cache, B_cache, dt_cache, ring_start, prev_num_accepted_tokens, logical_window, D=None, dt_bias=None, dt_softplus=False, state_batch_indices=None, null_block_id=NULL_BLOCK_ID, scratch=None, update_trackers=True, enable_stochastic_rounding=False, stochastic_rounding_philox_rounds=0)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.ssu_dispatch.selective_state_update_replayssm_flashinfer)

Run FlashInfer checkpointing SSU and optionally advance shared trackers.

## Source code in `vllm/model_executor/layers/mamba/ops/ssu_dispatch.py`


|
|

##

`update_replayssm_ring_trackers(ring_start, prev_num_accepted, state_batch_indices, logical_window=None, ring_buffer_len=None, pad_slot_id=NULL_BLOCK_ID)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.ssu_dispatch.update_replayssm_ring_trackers)

Reset selected trackers, or advance them when a window is provided.