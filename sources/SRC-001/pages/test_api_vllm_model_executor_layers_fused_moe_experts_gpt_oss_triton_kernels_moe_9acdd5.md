source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.fused_moe.experts.gpt_oss_triton_kernels_moe`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.gpt_oss_triton_kernels_moe)

Classes:

-
–[BaseOAITritonExperts](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.gpt_oss_triton_kernels_moe.BaseOAITritonExperts) -
–[OAITritonExperts](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.gpt_oss_triton_kernels_moe.OAITritonExperts)OAI Triton-based fused MoE expert implementation.

-
–[OAITritonMxfp4ExpertsMonolithic](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.gpt_oss_triton_kernels_moe.OAITritonMxfp4ExpertsMonolithic)Monolithic Triton MXFP4 expert. Wraps triton_kernel_moe_forward().

-
–[UnfusedOAITritonExperts](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.gpt_oss_triton_kernels_moe.UnfusedOAITritonExperts)A Triton based MoE expert class that operates on expert standard


Functions:

-
–[pack_bitmatrix](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.gpt_oss_triton_kernels_moe.pack_bitmatrix)Packs topk_ids into a bitmatrix.

-
–[remap_topk_to_local](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.gpt_oss_triton_kernels_moe.remap_topk_to_local)Fused global->local expert-id mapping over a topk_ids tensor, preserving -1.

-
–[routing_data_from_sparse_topk](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.gpt_oss_triton_kernels_moe.routing_data_from_sparse_topk)Build routing structures from the

`SparseMatrix`

returned by -
–[triton_kernel_fused_experts](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.gpt_oss_triton_kernels_moe.triton_kernel_fused_experts)Triton implementation of fused expert computation using OAI kernels.


##

`BaseOAITritonExperts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.gpt_oss_triton_kernels_moe.BaseOAITritonExperts)

Bases: [FusedMoEExpertsModular](https://docs.vllm.ai/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular)

Methods:

-
–[moe_problem_size](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.gpt_oss_triton_kernels_moe.BaseOAITritonExperts.moe_problem_size)Extract the MoE problem size from the given tensor arguments:


## Source code in `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`


|
|

###

`moe_problem_size(a1, w1, w2, topk_ids)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.gpt_oss_triton_kernels_moe.BaseOAITritonExperts.moe_problem_size)

Extract the MoE problem size from the given tensor arguments: - a: The hidden states, input to the MoE layer. - w1: The first set of expert weights. - w2: The second set of expert weights. - topk_ids: The topk ids. Note: extracting the problem shape from the weight and activation tensors is not obvious. It needs to be done this way specifically due to subtle issues with particular kernels, e.g. the int4 kernels divide the trailing dimension by two, so it's not "correct" to extract N or K from the trailing dimension of w1 or w2. Similarly, some kernels transpose the weights, so this needs to be kept in mind. Note: This implementation covers most cases. However, if experts require a specialized implementation, like MarlinExperts, they are free to override this function.

## Source code in `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`


##

`OAITritonExperts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.gpt_oss_triton_kernels_moe.OAITritonExperts)

Bases: [BaseOAITritonExperts](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.gpt_oss_triton_kernels_moe.BaseOAITritonExperts)

OAI Triton-based fused MoE expert implementation.

## Source code in `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`


|
|

##

`OAITritonMxfp4ExpertsMonolithic`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.gpt_oss_triton_kernels_moe.OAITritonMxfp4ExpertsMonolithic)

Bases: [FusedMoEExpertsMonolithic](https://docs.vllm.ai/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsMonolithic)

Monolithic Triton MXFP4 expert. Wraps triton_kernel_moe_forward().

## Source code in `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`


|
|

##

`UnfusedOAITritonExperts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.gpt_oss_triton_kernels_moe.UnfusedOAITritonExperts)

Bases:

, [LoRAExpertsMixin](https://docs.vllm.ai/lora_experts_mixin/#vllm.model_executor.layers.fused_moe.experts.lora_experts_mixin.LoRAExpertsMixin)[BaseOAITritonExperts](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.gpt_oss_triton_kernels_moe.BaseOAITritonExperts)

A Triton based MoE expert class that operates on expert standard format and explicitly keeps the activation and reduction (moe_sum) steps unfused from the matmul_ogs kernel. This exposes injection points for activation and moe_sum.

One use case for it is to inject LoRA modules on the activation and moe_sum.

## Source code in `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`


|
|

##

`_patch_legacy_routing_for_nonpow2_topk()`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.gpt_oss_triton_kernels_moe._patch_legacy_routing_for_nonpow2_topk)

Monkey-patch the legacy (v3.5.1) triton_kernels routing path to support non-power-of-2 top_k (e.g. DeepSeek-V4 top_k=6).

The bundled `_routing_compute_indx`

does `tl.arange(0, N_EXPTS_ACT * BLOCK_M)`

, which fails to compile when `N_EXPTS_ACT`

(top_k) is not a power of 2 (6 * 32 = 192). This installs a pow2-safe variant that pads the `tl.arange`

to the next power of 2, strides by the real per-block size, and masks the padded tail so it neither loads the next block's gates nor writes any output. For power-of-2 top_k it is identical to the original.

A matching `sort_tokens`

is installed that threads the padded size into the patched kernel. Only needed on the legacy path; the v3.6+ SparseMatrix path is handled by `_patch_make_bitmatrix_metadata`

.

## Source code in `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`


|
|

##

`_patch_make_bitmatrix_metadata()`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.gpt_oss_triton_kernels_moe._patch_make_bitmatrix_metadata)

Monkey-patch make_bitmatrix_metadata to support non-power-of-2 top_k.

triton's tl.arange requires a power-of-2 range. The original kernel computes BLOCK_SIZE = BLOCK_PER_TOK * TOKS_PER_ROW (= 32 * top_k). For DeepSeek-V4 with top_k=6 this gives 192, which is not a power of 2 and causes a compile error at the first forward pass.

Fix: define a drop-in replacement kernel that accepts an extra constexpr BLOCK_SIZE_PADDED (next power of 2 >= BLOCK_SIZE) and uses it for the tl.arange call while keeping the actual BLOCK_SIZE as the stride between thread-blocks so that all flat indices into NonzeroIndx stay correct. Elements beyond BLOCK_SIZE are masked out (col_indx = 0xffff) and ignored.

This function is called once at module load time and patches the function inside the triton_kernels tensor module so that SparseMatrix.**post_init** picks up the fixed version transparently.

## Source code in `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`


|
|

##

`pack_bitmatrix(bitmatrix, topk_ids, n_rows, bm_cols, n_expts_act, BLOCK_SIZE_M, BLOCK_SIZE_K)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.gpt_oss_triton_kernels_moe.pack_bitmatrix)

Packs topk_ids into a bitmatrix. code reference: https://github.com/triton-lang/triton/blob/dd1bbc52b34d202dfe5ffea1e04fb16166c5c04e/python/triton_kernels/bench/distributed.py#L264

## Source code in `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`


##

`remap_topk_to_local(topk_ids, expert_map)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.gpt_oss_triton_kernels_moe.remap_topk_to_local)

Fused global->local expert-id mapping over a topk_ids tensor, preserving -1.

Replaces `torch.where(topk_ids >= 0, expert_map[topk_ids.clamp(min=0)], -1)`

with one kernel. Returns a NEW int64 tensor -- the caller keeps the original `topk_ids`

as `global_topk_ids`

, so this must not write in place.

(Distinct from `deep_gemm_utils.apply_expert_map`

, which is a scalar `@triton.jit`

device helper called from within other kernels.)

## Source code in `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`


##

`routing_data_from_sparse_topk(sparse_topk, n_expts)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.gpt_oss_triton_kernels_moe.routing_data_from_sparse_topk)

Build routing structures from the `SparseMatrix`

returned by `triton_kernels.topk`

, reusing its precomputed bitmatrix metadata.

`make_routing_data`

re-packs a bitmatrix from the topk ids and constructs a second `SparseMatrix`

, recomputing metadata the topk call already produced; when the topk ids are used as-is (no expert-map remapping) that work is redundant.

## Source code in `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`


##

`triton_kernel_fused_experts(output_tensor, hidden_states, w1, w2, routing_data, gather_indx, scatter_indx, topk, activation=MoEActivation.SWIGLUOAI, quant_config=None, swiglu_alpha=1.702, swiglu_limit=7.0, apply_router_weight_on_input=False, global_num_experts=-1, expert_map=None, intermediate_cache=None, a1q_scale=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.gpt_oss_triton_kernels_moe.triton_kernel_fused_experts)

Triton implementation of fused expert computation using OAI kernels.

## Source code in `vllm/model_executor/layers/fused_moe/experts/gpt_oss_triton_kernels_moe.py`


|
|