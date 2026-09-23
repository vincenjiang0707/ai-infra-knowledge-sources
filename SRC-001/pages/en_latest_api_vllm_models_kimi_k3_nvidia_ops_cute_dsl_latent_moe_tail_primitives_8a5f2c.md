source: https://docs.vllm.ai/en/latest/api/vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/primitives/
lastmod: 2026-09-23

#

`vllm.models.kimi_k3.nvidia.ops.cute_dsl.latent_moe_tail.primitives`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.cute_dsl.latent_moe_tail.primitives)

Shared CuTe DSL primitives; this module does not define a CUDA kernel.

Classes:

-
–[CUDAGraphCompatibleWrapper](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.cute_dsl.latent_moe_tail.primitives.CUDAGraphCompatibleWrapper)DLPack view that does not synchronize with the producer stream.


Functions:

-
–[finalize_top16_bf16](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.cute_dsl.latent_moe_tail.primitives.finalize_top16_bf16)Finalize one Kimi K3 top-16 vector with wide metadata loads.

-
–[fragment_is_dirty](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.cute_dsl.latent_moe_tail.primitives.fragment_is_dirty)Bit-exact upstream sentinel check: one comparison per 32-bit word.

-
–[load_global_u32x4](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.cute_dsl.latent_moe_tail.primitives.load_global_u32x4)Load one 128-bit fragment as four u32 registers.

-
–[load_shared_f32x2](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.cute_dsl.latent_moe_tail.primitives.load_shared_f32x2)Load two aligned FP32 DSM partials from local shared memory.

-
–[load_shared_f32x4](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.cute_dsl.latent_moe_tail.primitives.load_shared_f32x4)Load four aligned FP32 DSM partials from local shared memory.

-
–[map_shared_to_peer](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.cute_dsl.latent_moe_tail.primitives.map_shared_to_peer)Map a local shared-memory slot to the same slot in a peer CTA.

-
–[red_async_release_gpu_add_u32](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.cute_dsl.latent_moe_tail.primitives.red_async_release_gpu_add_u32)The exact SM100 arrival primitive used by upstream LamportFlags.

-
–[sanitize_negative_zero](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.cute_dsl.latent_moe_tail.primitives.sanitize_negative_zero)Turn real BF16 -0 into +0 so it cannot equal the empty sentinel.

-
–[stmc_bf16x8](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.cute_dsl.latent_moe_tail.primitives.stmc_bf16x8)Publish eight BF16 values through an NVLS multicast mapping.

-
–[store_global_u32x4](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.cute_dsl.latent_moe_tail.primitives.store_global_u32x4)Store four packed words to an ordinary or NVLS multicast global VA.

-
–[store_lamport_sentinel_128](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.cute_dsl.latent_moe_tail.primitives.store_lamport_sentinel_128)Reset one Lamport fragment to four FP32 negative-zero bit patterns.

-
–[to_cute_dynamic_m](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.cute_dsl.latent_moe_tail.primitives.to_cute_dynamic_m)Expose exactly one compact tensor mode as a runtime shape.

-
–[warp_sum_specialized](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.cute_dsl.latent_moe_tail.primitives.warp_sum_specialized)Warp sum supporting a compile-time partial final warp.


##

`CUDAGraphCompatibleWrapper`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.cute_dsl.latent_moe_tail.primitives.CUDAGraphCompatibleWrapper)

DLPack view that does not synchronize with the producer stream.

## Source code in `vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/primitives.py`


##

`finalize_top16_bf16(gemm2_vector, route_indices, route_weights, *, loc=None, ip=None)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.cute_dsl.latent_moe_tail.primitives.finalize_top16_bf16)

Finalize one Kimi K3 top-16 vector with wide metadata loads.

## Source code in `vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/primitives.py`


##

`fragment_is_dirty(packed)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.cute_dsl.latent_moe_tail.primitives.fragment_is_dirty)

Bit-exact upstream sentinel check: one comparison per 32-bit word.

## Source code in `vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/primitives.py`


##

`load_global_u32x4(pointer, *, volatile=False, loc=None, ip=None)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.cute_dsl.latent_moe_tail.primitives.load_global_u32x4)

Load one 128-bit fragment as four u32 registers.

The volatile form is the Lamport polling load. Marking the asm side-effecting prevents loop-invariant motion and common-subexpression elimination across polling iterations.

## Source code in `vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/primitives.py`


##

`load_shared_f32x2(pointer, *, loc=None, ip=None)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.cute_dsl.latent_moe_tail.primitives.load_shared_f32x2)

Load two aligned FP32 DSM partials from local shared memory.

## Source code in `vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/primitives.py`


##

`load_shared_f32x4(pointer, *, loc=None, ip=None)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.cute_dsl.latent_moe_tail.primitives.load_shared_f32x4)

Load four aligned FP32 DSM partials from local shared memory.

## Source code in `vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/primitives.py`


##

`map_shared_to_peer(smem_ptr, peer_rank, *, loc=None, ip=None)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.cute_dsl.latent_moe_tail.primitives.map_shared_to_peer)

Map a local shared-memory slot to the same slot in a peer CTA.

## Source code in `vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/primitives.py`


##

`red_async_release_gpu_add_u32(pointer, value, *, loc=None, ip=None)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.cute_dsl.latent_moe_tail.primitives.red_async_release_gpu_add_u32)

The exact SM100 arrival primitive used by upstream LamportFlags.

## Source code in `vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/primitives.py`


##

`sanitize_negative_zero(packed)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.cute_dsl.latent_moe_tail.primitives.sanitize_negative_zero)

Turn real BF16 -0 into +0 so it cannot equal the empty sentinel.

## Source code in `vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/primitives.py`


##

`stmc_bf16x8(address, packed, *, loc=None, ip=None)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.cute_dsl.latent_moe_tail.primitives.stmc_bf16x8)

Publish eight BF16 values through an NVLS multicast mapping.

## Source code in `vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/primitives.py`


##

`store_global_u32x4(address, packed, *, volatile=False, loc=None, ip=None)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.cute_dsl.latent_moe_tail.primitives.store_global_u32x4)

Store four packed words to an ordinary or NVLS multicast global VA.

## Source code in `vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/primitives.py`


##

`store_lamport_sentinel_128(pointer, *, loc=None, ip=None)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.cute_dsl.latent_moe_tail.primitives.store_lamport_sentinel_128)

Reset one Lamport fragment to four FP32 negative-zero bit patterns.

## Source code in `vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/primitives.py`


##

`to_cute_dynamic_m(tensor, *, mode, assumed_align=16)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.cute_dsl.latent_moe_tail.primitives.to_cute_dynamic_m)

Expose exactly one compact tensor mode as a runtime shape.

Model dimensions remain part of the compiled tensor type. Only the token mode is symbolic, so changing M within an Op's capacity reuses the same compiled kernel.

## Source code in `vllm/models/kimi_k3/nvidia/ops/cute_dsl/latent_moe_tail/primitives.py`


##

`warp_sum_specialized(value, warp_idx, lane, warps, last_warp_lanes, last_warp_mask)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.cute_dsl.latent_moe_tail.primitives.warp_sum_specialized)

Warp sum supporting a compile-time partial final warp.