source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/mamba/ops/cpu/gdn_attention/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.mamba.ops.cpu.gdn_attention`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.cpu.gdn_attention)

Functions:

-
–[cpu_gdn_attention_core](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.cpu.gdn_attention.cpu_gdn_attention_core)CPU custom op for the core GDN attention computation.


##

`_conv_buffer_view(layer)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.cpu.gdn_attention._conv_buffer_view)

Return the conv-state cache as (num_slots, dim, state_len).

## Source code in `vllm/model_executor/layers/mamba/ops/cpu/gdn_attention.py`


##

`_spec_aware_nonspec(layer, attn_metadata_i, mixed_qkv, b, a, core_attn_out, conv_buf, ssm_state, width)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.cpu.gdn_attention._spec_aware_nonspec)

Non-spec prefill/decode with a wide conv buffer.

## Source code in `vllm/model_executor/layers/mamba/ops/cpu/gdn_attention.py`


|
|

##

`_spec_aware_nonspec_subset(layer, attn_metadata_i, mixed_qkv, b, a, conv_buf, ssm_state, width)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.cpu.gdn_attention._spec_aware_nonspec_subset)

Process non-spec (prefill) tokens that coexist with spec sequences.

Returns outputs ordered like `non_spec_token_indx`

.

## Source code in `vllm/model_executor/layers/mamba/ops/cpu/gdn_attention.py`


##

`_spec_forward(layer, attn_metadata_i, mixed_qkv_spec, b_spec, a_spec, conv_buf, ssm_state, width, state_len)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.cpu.gdn_attention._spec_forward)

Run the GDN core for the multi-query (speculative) tokens.

Returns the core attention output for the spec tokens, in the same token order as `mixed_qkv_spec`

(i.e. ordered by `spec_query_start_loc`

).

## Source code in `vllm/model_executor/layers/mamba/ops/cpu/gdn_attention.py`


|
|

##

`_unpacked_conv_weight(layer)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.cpu.gdn_attention._unpacked_conv_weight)

Return the plain (dim, width) conv weight.

On AMX the conv1d weight is VNNI-packed in place at load time (only usable by the AMX C++ kernel), so the torch spec-decode path relies on the un-packed copy stashed by `dispatch_cpu_unquantized_gemm`

.

## Source code in `vllm/model_executor/layers/mamba/ops/cpu/gdn_attention.py`


##

`cpu_gdn_attention_core(mixed_qkv, b, a, core_attn_out, layer_name)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.mamba.ops.cpu.gdn_attention.cpu_gdn_attention_core)

CPU custom op for the core GDN attention computation.