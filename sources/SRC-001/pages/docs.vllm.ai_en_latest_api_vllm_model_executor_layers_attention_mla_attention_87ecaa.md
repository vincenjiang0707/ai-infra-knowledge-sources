source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/attention/mla_attention/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.attention.mla_attention`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention)

## MLA Common Components[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention--mla-common-components)

This file implements common components for MLA implementations.

First we define:

Sq as Q sequence length Skv as KV sequence length

MLA has two possible ways of computing, a data-movement friendly approach and a compute friendly approach. We generally want to use the compute friendly approach for "prefill" (i.e. the ratio Sq / Skv is relatively large, often near 1) and the data-movement friendly approach for "decode" (i.e. the ratio Sq / Skv is small, often near 0).

NOTE what we deem small and large is currently determined by if it is labelled prefill or decode by the scheduler, but this is something we should probably tune.

Main reference: DeepseekV2 paper, and FlashInfer Implementation (https://arxiv.org/abs/2405.04434 and https://github.com/flashinfer-ai/flashinfer/pull/551).

Deepseek's MLA attention works the following way: * Use a single latent vector to represent the per-token entry of the KV cache. * For decode (i.e. the memory friendly approach) the attention "simulates" a multi-head attention, while the compute is similar to multi-query attention.

Below is an example of both paths assuming batch size = 1

### More Extent Definitions:[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention--more-extent-definitions)

C Context length, `Skv - Sq`

H hidden size N number of attention heads Lq latent dimension for Q 1536 in DSV3 Lkv latent dimension for K/V 512 in DSV3 P nope dimension, no rope. 128 in DSV3 R rope dimension, goes through rope. 64 in DSV3 V V head dim. 128 in DSV3

### Vector/Matrix Definitions[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention--vectormatrix-definitions)

h_t hidden states (input to attention) shape [Sq, H] q_c latent/compressed Q shape [Sq, Lq] q_nope uncompressed Q (no-rope) shape [Sq, N, P] q_pe uncompressed Q (rope) shape [Sq, N, R] kv_c latent/compressed KV shape [Skv, Lkv] k_pe decoupled k position embeddings shape [Skv, R] new_kv_c new kv_c from current iter shape [Sq, Lkv] new_k_pe new k_pe from current iter shape [Sq, R] cache_kv_c cached k_c from previous iters shape [C, Lkv] cache_k_pe cached k_pe from previous iters shape [C, R] W_DQ project h_t to q_c shape [H, Lq] W_UQ project q_c to q_nope shape [Lq, N * P] W_QR project q_c to q_pe shape [Lq, N * R] W_DKV project h_t to kv_c shape [H, Lkv] W_UK project kv_c to k_nope shape [Lkv, N, P] W_KR project h_t to k_pe shape [H, R] W_UV project kv_c to v shape [Lkv, N, V] W_O project v to h_t shape [N * V, H]

### Compute Friendly Approach (i.e. "forward_mha"):[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention--compute-friendly-approach-ie-forward_mha)

q_c = h_t @ W_DQ q_nope = (q_c @ W_UQ).view(Sq, N, P) q_pe = RoPE(q_c @ W_QR).view(Sq, N, R) new_kv_c = h_t @ W_DKV new_k_pe = RoPE(h_t @ W_KR) kv_c = torch.cat([new_kv_c, cache_kv_c], dim=0) k_pe = torch.cat([new_k_pe, cache_k_pe], dim=0) k_nope = (kv_c @ W_UK.view(Lkv, N * P)).view(Skv, N, P) v = (kv_c @ W_UV.view(Lkv, N * V)).view(Skv, N, V)

// MHA with QK headdim = P + R // V headdim = V // sdpa_o shape [Sq, N, V] sdpa_o = scaled_dot_product_attention( torch.cat([q_nope, q_pe], dim=-1), torch.cat([k_nope, k_pe.unsqueeze(1).expand(-1, N, -1)], dim=-1), v ) return sdpa_o @ W_O

## in the actual code,

`kv_b_proj`

is [W_UK; W_UV] concatenated per head `q_b_proj`

is [W_UQ; W_QR] concatenated per head `out_proj`

is W_O

### Data-Movement Friendly Approach (i.e. "forward_mqa"):[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention--data-movement-friendly-approach-ie-forward_mqa)

Runtime q_c = h_t @ W_DQ q_nope = (q_c @ W_UQ).view(-1, N, P) ql_nope = einsum("snh,lnh->snl", q_nope, W_UK) q_pe = RoPE(q_c @ W_QR).view(Sq, N, R) new_kv_c = h_t @ W_DKV new_k_pe = RoPE(h_t @ W_KR) kv_c = torch.cat([new_kv_c, cache_kv_c], dim=0) k_pe = torch.cat([new_k_pe, cache_k_pe], dim=0)

// MQA with QK headdim = Lkv + R // V headdim = Lkv // sdpa_o shape [Sq, N, Lkv] // NOTE: this is less compute-friendly since Lkv > P // but is more data-movement friendly since its MQA vs MHA sdpa_o = scaled_dot_product_attention( torch.cat([ql_nope, q_pe], dim=-1), torch.cat([kv_c, k_pe], dim=-1), kv_c )

o = einsum("snl,lnv->snv", sdpa_o.reshape(-1, N, Lkv), W_UV) return o.view(-1, N * V) @ W_O

### Chunked Prefill[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention--chunked-prefill)

For chunked prefill we want to use the compute friendly algorithm. We are assuming sufficiently large Sq / Skv ratio, in the future may want to switch to the data-movement friendly approach if the chunk (i.e. `Sq`

) is small.

However, the compute-friendly approach can potentially run out of memory if Skv is large due to: `k_nope = (kv_c @ W_UK).view(Skv, N, P)`


To mitigate this, we chunk the computation of attention with respect to the current context (i.e. `cache_kv_c`

and `cache_k_pe`

) so that we can used a fixed workspace size.

The chunked prefill approach is as follows:

W Workspace rows, i.e. the context rows we may gather at once, used to bound the memory usage

The context is scheduled per request: requests are packed in order, splitting the next request on an aligned boundary when needed to fill `W`

. So a chunk covers a contiguous run of prefills and only ever the tokens and context rows of those prefills — attention, up-projection and merging are charged only to the requests it covers, and no chunk contains an empty context span. See `plan_mla_context_chunks`

.

Only a chunk's first request can be a continuation, so accumulation performs at most one request-slice merge and one bulk write per chunk.

q_c = h_t @ W_DQ q_nope = (q_c @ W_UQ).view(Sq, N, P) q_pe = RoPE(q_c @ W_QR).view(Sq, N, R) new_kv_c = h_t @ W_DKV new_k_pe = RoPE(h_t @ W_KR) new_k_nope = (new_kv_c @ W_UK.view(Lkv, N * P)).view(Sq, N, P) new_v = (new_kv_c @ W_UV.view(Lkv, N * V)).view(Sq, N, V)

// MHA between queries and new KV // with QK headdim = P + R // V headdim = V // curr_o shape [Sq, N, V] // curr_lse shape [N, Sq], this is just order FA returns curr_o, curr_lse = scaled_dot_product_attention( torch.cat([q_nope, q_pe], dim=-1), torch.cat([new_k_nope, new_k_pe.unsqueeze(1).expand(-1, N, -1)], dim=-1), new_v, causal=True, return_softmax_lse=True )

// Compute attention with the already existing context. Shown for a single // request; with a batch, a chunk covers a run of requests and both `q`

and the // gathered context below are sliced to that run. for chunk_idx in range(cdiv(C, W)): chunk_start = chunk_idx * W chunk_end = min(chunk_start + W, C) Sc = chunk_end - chunk_start cache_kv_c_chunk = cache_kv_c[chunk_start:chunk_end] cache_k_pe_chunk = cache_k_pe[chunk_start:chunk_end] cache_k_nope_chunk = (cache_kv_c_chunk @ W_UK).view(-1, N, P) cache_v_chunk = (cache_kv_c_chunk @ W_UV).view(-1, N, V)

```
chunk_o, chunk_lse = scaled_dot_product_attention(
torch.cat([q_nope, q_pe], dim=-1),
torch.cat([cache_k_nope_chunk,
cache_k_pe_chunk.unsqueeze(1).expand(-1, N, -1)],
dim=-1),
cache_v_chunk,
causal=False,
return_softmax_lse=True
)
curr_o, curr_lse = merge_attn_states(
suffix_output=curr_o,
suffix_lse=curr_lse,
prefix_output=chunk_o,
prefix_lse=chunk_lse,
)
```


return curr_o @ W_O

Classes:

-
–[MLAAttention](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.MLAAttention)Multi-Head Latent Attention layer.

-
–[MLACommonBackend](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.MLACommonBackend) -
–[MLACommonBaseImpl](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.MLACommonBaseImpl)Shared MLA base providing dense-MHA prefill (via the selected

-
–[MLACommonImpl](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.MLACommonImpl)NOTE: Please read the comment at the top of the file before trying to

-
–[MLACommonMetadata](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.MLACommonMetadata)Metadata for MLACommon.

-
–[MLACommonMetadataBuilder](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.MLACommonMetadataBuilder)NOTE: Please read the comment at the top of the file before trying to

-
–[MLACommonPrefillMetadata](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.MLACommonPrefillMetadata)Prefill Specific Metadata

-
–[QueryLenSupport](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.QueryLenSupport)Defines the level of query length support for an attention backend's


Functions:

-
–[accumulate_mla_context_chunk](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.accumulate_mla_context_chunk)Fold one chunk's partial into the running context partial.

-
–[backend_supports_prefill_query_quantization](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.backend_supports_prefill_query_quantization)Check if the selected MLA prefill backend supports query quantization.

-
–[build_mla_chunked_context_metadata](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.build_mla_chunked_context_metadata)Build chunked-context metadata for an MLA prefill.

-
–[init_mla_context_partial](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.init_mla_context_partial)Allocate the running context partial over all prefill tokens.

-
–[neutralize_empty_context_partials](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.neutralize_empty_context_partials)Neutralize the partial of every prefill that no chunk covers.

-
–[plan_mla_context_chunks](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.plan_mla_context_chunks)Pack per-request contexts into workspace-sized chunks.

-
–[reorg_kvcache](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.reorg_kvcache)Reorg and unpad kvcache after cp local gather to tp layout for attn kernel.

-
–[split_kv_b_proj](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.split_kv_b_proj)Dequantize

`kv_b_proj`

and return`W_UK [L,N,P]`

,`W_UV [L,N,V]`

. -
–[unified_mla_kv_cache_update](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.unified_mla_kv_cache_update)Returns a dummy that is passed to unified_attention to signal a side effect and


##

`MLAAttention`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.MLAAttention)

Bases:

, [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)[AttentionLayerBase](https://docs.vllm.ai/attention_layer_base/#vllm.model_executor.layers.attention_layer_base.AttentionLayerBase)

Multi-Head Latent Attention layer.

NOTE: Please read the comment at the top of the file before trying to understand this class

This class takes query, and compressed key/value tensors as input. The class does the following:

- Store the input key and value tensors in the KV cache.
- Perform (multi-head/multi-query/grouped-query) attention.
- Return the output tensor.

## Source code in `vllm/model_executor/layers/attention/mla_attention.py`


|
|

##

`MLACommonBackend`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.MLACommonBackend)

Bases: [AttentionBackend](https://docs.vllm.ai/v1/attention/backend/#vllm.v1.attention.backend.AttentionBackend)

Methods:

-
–[customize_spec](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.MLACommonBackend.customize_spec)Per-token-head modes pack an inline fp32 scale pair after the


## Source code in `vllm/model_executor/layers/attention/mla_attention.py`


###

`customize_spec(spec)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.MLACommonBackend.customize_spec)

Per-token-head modes pack an inline fp32 scale pair after the latent data (single-sided: `head_size_v == 0`

for MLA).

## Source code in `vllm/model_executor/layers/attention/mla_attention.py`


##

`MLACommonBaseImpl`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.MLACommonBaseImpl)

Bases:

, [MLAAttentionImpl](https://docs.vllm.ai/v1/attention/backend/#vllm.v1.attention.backend.MLAAttentionImpl)[A][Generic](https://docs.python.org/3/library/typing.html#typing.Generic)[A]

Shared MLA base providing dense-MHA prefill (via the selected MLAPrefillBackend) for both dense and sparse impls; subclasses add decode (`forward_mqa`

).

## Source code in `vllm/model_executor/layers/attention/mla_attention.py`


|
|

###

`_concat_k_nope_k_pe(k_nope, k_pe)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.MLACommonBaseImpl._concat_k_nope_k_pe)

Efficiently concatenate k_nope and k_pe tensors along the last dimension.

This function avoids the performance penalty of torch.cat with expanded non-contiguous tensors by pre-allocating the output and using direct copies.

Parameters:

-

(`k_nope`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.MLACommonBaseImpl._concat_k_nope_k_pe(k_nope))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Tensor of shape [..., nope_dim]

-

(`k_pe`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.MLACommonBaseImpl._concat_k_nope_k_pe(k_pe))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Tensor to broadcast and concatenate, typically shape [..., 1, pe_dim] or [..., pe_dim]


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Tensor of shape [..., nope_dim + pe_dim]


## Source code in `vllm/model_executor/layers/attention/mla_attention.py`


##

`MLACommonImpl`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.MLACommonImpl)

Bases:

, [MLACommonBaseImpl](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.MLACommonBaseImpl)[M][Generic](https://docs.python.org/3/library/typing.html#typing.Generic)[M]

NOTE: Please read the comment at the top of the file before trying to understand this class

## Source code in `vllm/model_executor/layers/attention/mla_attention.py`


|
|

##

`MLACommonMetadata`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.MLACommonMetadata)

Bases: `AttentionMetadata`

, [Generic](https://docs.python.org/3/library/typing.html#typing.Generic)[D]

Metadata for MLACommon.

NOTE: Please read the comment at the top of the file before trying to understand this class

## Source code in `vllm/model_executor/layers/attention/mla_attention.py`


##

`MLACommonMetadataBuilder`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.MLACommonMetadataBuilder)

Bases: [AttentionMetadataBuilder](https://docs.vllm.ai/v1/attention/backend/#vllm.v1.attention.backend.AttentionMetadataBuilder)[M]

NOTE: Please read the comment at the top of the file before trying to understand this class

Methods:

-
–[build_for_cudagraph_capture](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.MLACommonMetadataBuilder.build_for_cudagraph_capture)This method builds the metadata for full cudagraph capture.

-
–[determine_prefill_query_data_type](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.MLACommonMetadataBuilder.determine_prefill_query_data_type)Determine the query data type for prefill queries.


## Source code in `vllm/model_executor/layers/attention/mla_attention.py`


|
|

###

`build_for_cudagraph_capture(common_attn_metadata)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.MLACommonMetadataBuilder.build_for_cudagraph_capture)

This method builds the metadata for full cudagraph capture. Currently, only decode is supported for full cudagraphs with MLA.

## Source code in `vllm/model_executor/layers/attention/mla_attention.py`


###

`determine_prefill_query_data_type(vllm_config, model_dtype)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.MLACommonMetadataBuilder.determine_prefill_query_data_type)

Determine the query data type for prefill queries. Return FP8 dtype if cache is FP8 and prefill query quantization is enabled, else model dtype.

## Source code in `vllm/model_executor/layers/attention/mla_attention.py`


##

`MLACommonPrefillMetadata`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.MLACommonPrefillMetadata)

Prefill Specific Metadata

Classes:

-
–[ContextChunk](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.MLACommonPrefillMetadata.ContextChunk)One workspace-sized slice of paged context for a run of prefills.


## Source code in `vllm/model_executor/layers/attention/mla_attention.py`


###

`ContextChunk`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.MLACommonPrefillMetadata.ContextChunk)

One workspace-sized slice of paged context for a run of prefills.

## Source code in `vllm/model_executor/layers/attention/mla_attention.py`


##

`QueryLenSupport`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.QueryLenSupport)

Bases: [Enum](https://docs.python.org/3/library/enum.html#enum.Enum)

Defines the level of query length support for an attention backend's decode pipeline.

- SINGLE_ONLY: Decode pipeline only supports single-token queries (query_len=1)
- UNIFORM: Decode pipeline supports uniform multi-token queries (all requests must have same query_len > 1)
- VARLEN: Decode pipeline supports variable-length queries (mixed query lengths in same batch)

## Source code in `vllm/model_executor/layers/attention/mla_attention.py`


##

`_ContextChunkPlan`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention._ContextChunkPlan)

Request-space layout of one context chunk, before tensors are built.

## Source code in `vllm/model_executor/layers/attention/mla_attention.py`


##

`_DecodeConcatQuantFP8`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention._DecodeConcatQuantFP8)

Bases: [QuantFP8](https://docs.vllm.ai/quantization/input_quant_fp8/#vllm.model_executor.layers.quantization.input_quant_fp8.QuantFP8)

QuantFP8 variant that concatenates decode_ql_nope and decode_q_pe before quantization. When disabled, forward_native is compiled via torch.compile, fusing cat/reshape/quant/view together.

## Source code in `vllm/model_executor/layers/attention/mla_attention.py`


###

`_make_forward(quant_fn)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention._DecodeConcatQuantFP8._make_forward)

Factory to create forward methods that concat before quantization.

## Source code in `vllm/model_executor/layers/attention/mla_attention.py`


##

`_detect_output_quant_key(output, output_scale, output_block_scale, output_dim)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention._detect_output_quant_key)

Detect the output quantization key from fusion pass parameters.

Returns the appropriate QuantKey, or None if no quantization is needed. Detection is based on output dtype and which scale tensors are present.

## Source code in `vllm/model_executor/layers/attention/mla_attention.py`


##

`accumulate_mla_context_chunk(chunk, attn_output, attn_softmax_lse, output, output_lse, output_written=False)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.accumulate_mla_context_chunk)

Fold one chunk's partial into the running context partial.

Only the first request may be a continuation; its tokens are merged and the remaining token range is initialized.

Parameters:

-

(`chunk`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.accumulate_mla_context_chunk(chunk))

) –[ContextChunk](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.MLACommonPrefillMetadata.ContextChunk)The context chunk being folded in.

-

(`attn_output`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.accumulate_mla_context_chunk(attn_output))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The chunk's attention output.

-

(`attn_softmax_lse`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.accumulate_mla_context_chunk(attn_softmax_lse))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The chunk's log-sum-exp values.

-

(`output`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.accumulate_mla_context_chunk(output))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Running context partial, updated in place.

-

(`output_lse`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.accumulate_mla_context_chunk(output_lse))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Running log-sum-exp, updated in place.

-

(`output_written`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.accumulate_mla_context_chunk(output_written))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –The chunk's attention output already landed in

`output[chunk.token_slice]`

because the backend was handed it as`out`

, leaving only the lse to fold. Invalid for a continuation chunk, whose leading tokens must be merged rather than overwritten.

## Source code in `vllm/model_executor/layers/attention/mla_attention.py`


##

`backend_supports_prefill_query_quantization()`

`cached`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.backend_supports_prefill_query_quantization)

Check if the selected MLA prefill backend supports query quantization.

Currently supported backends: - FlashInfer - TRT-LLM Ragged

Not supported: - FlashAttention (FA3/FA4) - Non-GB200 devices (FP8 prefill requires device capability 100)

## Source code in `vllm/model_executor/layers/attention/mla_attention.py`


##

`build_mla_chunked_context_metadata(*, context_lens_cpu, prefill_query_start_loc_cpu, chunked_prefill_workspace, chunked_prefill_workspace_size, block_size, align_chunk_to_block, device, dcp_world_size, dcp_local_block_size, dcp_virtual_block_size, dcp_manager=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.build_mla_chunked_context_metadata)

Build chunked-context metadata for an MLA prefill.

Shared by dense and sparse builders. Packs the prefill contexts into a flat list of workspace-sized per-request chunks and, under DCP, plans the per-rank interleaved local chunks the all-gather reduction consumes.

Parameters:

-

(`context_lens_cpu`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.build_mla_chunked_context_metadata(context_lens_cpu))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Per-prefill context length (seq_len - query_len).

-

(`prefill_query_start_loc_cpu`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.build_mla_chunked_context_metadata(prefill_query_start_loc_cpu))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Prefill query cumulative offsets (0-based).

-

(`chunked_prefill_workspace`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.build_mla_chunked_context_metadata(chunked_prefill_workspace))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Scratch buffer the context gather writes to.

-

(`chunked_prefill_workspace_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.build_mla_chunked_context_metadata(chunked_prefill_workspace_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Row capacity of the workspace.

-

(`block_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.build_mla_chunked_context_metadata(block_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)KV cache page size for chunk-start alignment.

-

(`align_chunk_to_block`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.build_mla_chunked_context_metadata(align_chunk_to_block))

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Round the chunk size down to

`block_size`

. -

(`device`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.build_mla_chunked_context_metadata(device))

) –[device](https://pytorch.org/docs/stable/tensor_attributes.html#torch.device)Target device for the returned tensors.

-

(`dcp_world_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.build_mla_chunked_context_metadata(dcp_world_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Decode-context-parallel world size (1 if disabled).

-

(`dcp_local_block_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.build_mla_chunked_context_metadata(dcp_local_block_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Per-rank interleave block size for DCP.

-

(`dcp_virtual_block_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.build_mla_chunked_context_metadata(dcp_virtual_block_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)`dcp_local_block_size * dcp_world_size`

. -

(`dcp_manager`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.build_mla_chunked_context_metadata(dcp_manager))

, default:[MLADCPManager](https://docs.vllm.ai/v1/attention/ops/dcp/#vllm.v1.attention.ops.dcp.MLADCPManager)| None`None`

) –Shared MLA DCP collective manager.


Returns:

-
`ChunkedContextMetadata | None`

–The chunked-context metadata, or None when no prefill has any context.


## Source code in `vllm/model_executor/layers/attention/mla_attention.py`


|
|

##

`init_mla_context_partial(chunked_context, attn_output, attn_softmax_lse, num_tokens)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.init_mla_context_partial)

Allocate the running context partial over all prefill tokens.

Laid out like the chunk partials so the final whole-batch merge against the suffix partial sees matching head strides. Callers whose backend honors an `out`

tensor already know that layout and can allocate directly, pairing it with `neutralize_empty_context_partials`

.

## Source code in `vllm/model_executor/layers/attention/mla_attention.py`


##

`neutralize_empty_context_partials(chunked_context, output, output_lse)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.neutralize_empty_context_partials)

Neutralize the partial of every prefill that no chunk covers.

A prefill without context is never gathered, so nothing would write its rows; a zero output with an `-inf`

lse carries no weight into the final merge against the suffix partial.

## Source code in `vllm/model_executor/layers/attention/mla_attention.py`


##

`plan_mla_context_chunks(context_lens, row_budget, max_context_chunk, split_alignment, padded_rows)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.plan_mla_context_chunks)

Pack per-request contexts into workspace-sized chunks.

## Source code in `vllm/model_executor/layers/attention/mla_attention.py`


|
|

##

`reorg_kvcache(allgatered_kv_c_normed, allgatered_k_pe, padded_local_chunk_seq_lens_lst, local_context_lens_allranks, local_starts, sum_seq_len, max_seq_len, toks)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.reorg_kvcache)

Reorg and unpad kvcache after cp local gather to tp layout for attn kernel. e.g. allgatered_kv_c_normed = [T0_0, T0_1, T0_2, T0_3, T1_0, T1_1, ..., T0_4, T0_5, pad, pad, T1_2, pad, ...] -> reorganized_kv_c_normed = [T0_0, T0_1, T0_2, T0_3, T0_4, T0_5, T1_0, T1_1, T1_2, ...]

Parameters:

-

(`allgatered_kv_c_normed`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.reorg_kvcache(allgatered_kv_c_normed))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)all-gathered, padded latent KV cache.

-

(`allgatered_k_pe`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.reorg_kvcache(allgatered_k_pe))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)all-gathered, padded RoPE key cache.

-

(`padded_local_chunk_seq_lens_lst`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.reorg_kvcache(padded_local_chunk_seq_lens_lst))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]local chunk context lengths under current CP rank.

-

(`local_context_lens_allranks`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.reorg_kvcache(local_context_lens_allranks))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]]local context lengths on each CP rank.

-

(`local_starts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.reorg_kvcache(local_starts))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]per-request local offset into the context this chunk starts at.

-

(`sum_seq_len`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.reorg_kvcache(sum_seq_len))

) –[int](https://docs.python.org/3/builtins/functions.html#int)the sum of cp_chunk_seq_lens_lst.

-

(`max_seq_len`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.reorg_kvcache(max_seq_len))

) –[int](https://docs.python.org/3/builtins/functions.html#int)the max value of cp_chunk_seq_lens_lst.

-

(`toks`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.reorg_kvcache(toks))

) –[int](https://docs.python.org/3/builtins/functions.html#int)the number of tokens for local gather cache.


## Source code in `vllm/model_executor/layers/attention/mla_attention.py`


|
|

##

`split_kv_b_proj(kv_b_proj, out_dtype, kv_lora_rank, num_heads, qk_nope_head_dim, v_head_dim)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.split_kv_b_proj)

Dequantize `kv_b_proj`

and return `W_UK [L,N,P]`

, `W_UV [L,N,V]`

.

## Source code in `vllm/model_executor/layers/attention/mla_attention.py`


##

`unified_mla_kv_cache_update(kv_c_normed, k_pe, layer_name, kv_cache_dtype, k_scale)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.attention.mla_attention.unified_mla_kv_cache_update)

Returns a dummy that is passed to unified_attention to signal a side effect and the data dependency between them to ensure torch.compile preserves ordering.