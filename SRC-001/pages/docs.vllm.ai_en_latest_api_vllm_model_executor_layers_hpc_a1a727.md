source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/hpc/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.hpc`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.hpc)

Modules:

-
–[gated_mla](https://docs.vllm.ai/gated_mla/#vllm.model_executor.layers.hpc.gated_mla)Enablement gate for the HPC fused gated-MLA GEMM.

-
–[hpc_ihc](https://docs.vllm.ai/hpc_ihc/#vllm.model_executor.layers.hpc.hpc_ihc)HPC fused iHC (independent Hyper-Connections) kernels for HY V4.

-
–[rope_norm](https://docs.vllm.ai/rope_norm/#vllm.model_executor.layers.hpc.rope_norm)HPC fused RoPE + QK-Norm + KV-Cache-Write (+ optional FP8 Q quant).


Classes:

-
–[HpcIHCHead](https://docs.vllm.ai#vllm.model_executor.layers.hpc.HpcIHCHead)Fused iHC head block: merge the hc channels back into one hidden state.

-
–[HpcIHCPost](https://docs.vllm.ai#vllm.model_executor.layers.hpc.HpcIHCPost)Fused iHC post block: H_post gating plus multi-channel residual add.

-
–[HpcIHCPre](https://docs.vllm.ai#vllm.model_executor.layers.hpc.HpcIHCPre)Fused iHC pre block.

-
–[HpcRopeNorm](https://docs.vllm.ai#vllm.model_executor.layers.hpc.HpcRopeNorm)HPC fused RoPE + QK-Norm + KV-Cache-Write (+ optional FP8 Q quant).

-
–[QkNormPolicy](https://docs.vllm.ai#vllm.model_executor.layers.hpc.QkNormPolicy)Order of QK-RMSNorm relative to RoPE in the fused HPC rope_norm kernel.


Functions:

-
–[hpc_gated_mla_gemm](https://docs.vllm.ai#vllm.model_executor.layers.hpc.hpc_gated_mla_gemm)Fused

`atten_output * sigmoid(x @ weight.T)`

. -
–[hpc_gated_mla_supported](https://docs.vllm.ai#vllm.model_executor.layers.hpc.hpc_gated_mla_supported)Gate for running the MLA output gating through hpc.gated_mla_gemm.


##

`HpcIHCHead`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.hpc.HpcIHCHead)

Bases: `HpcModule`


Fused iHC head block: merge the hc channels back into one hidden state.

Same structure as HpcIHCPre but the projection emits only hc_mult gate logits and there is no H_post output. Called once per forward, after the last decoder layer.

## Source code in `vllm/model_executor/layers/hpc/hpc_ihc.py`


##

`HpcIHCPost`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.hpc.HpcIHCPost)

Bases: `HpcModule`


Fused iHC post block: H_post gating plus multi-channel residual add.

Unlike mHC there is no comb matrix, so each output channel only needs its own residual channel and the whole thing is one fused multiply-add per element.

## Source code in `vllm/model_executor/layers/hpc/hpc_ihc.py`


##

`HpcIHCPre`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.hpc.HpcIHCPre)

Bases: `HpcModule`


Fused iHC pre block.

Computes, in one kernel: x_flat = x.flatten(1) r = rsqrt(x_flat.square().mean(-1) + rms_norm_eps) mixes = (x_flat @ w.T) * r H_pre = sigmoid(mixes[:, :hc] * hc_scale[0] + hc_base[:hc]) + hc_eps H_post = magnitude * sigmoid( mixes[:, hc:] * hc_scale[1] + hc_base[hc:]) + hc_eps y = sum_i H_pre[:, i] * x[:, i, :]

Parameters:

-

(`hc_mult`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.hpc.HpcIHCPre(hc_mult))

) –[int](https://docs.python.org/3/builtins/functions.html#int)HC expand ratio.

-

(`hidden_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.hpc.HpcIHCPre(hidden_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Model hidden dimension.

-

(`magnitude`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.hpc.HpcIHCPre(magnitude))

) –[float](https://docs.python.org/3/builtins/functions.html#float)H_post multiplier (config.hc_magnitude).

-

(`hc_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.hpc.HpcIHCPre(hc_eps))

) –[float](https://docs.python.org/3/builtins/functions.html#float)Epsilon added to both gates (config.hc_eps).

-

(`norm_eps`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.hpc.HpcIHCPre(norm_eps))

) –[float](https://docs.python.org/3/builtins/functions.html#float)Epsilon inside the rsqrt (config.rms_norm_eps).

-

(`fallback_op`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.hpc.HpcIHCPre(fallback_op))

) –[Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)The eager HYV4HCPreLayer to source weights from.

-

(`norm_owner`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.hpc.HpcIHCPre(norm_owner))

, default:[Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)| None`None`

) –Optional RMSNorm that immediately follows this pre block. When given, its weight/eps are folded into the kernel so a single launch covers pre + RMSNorm (the caller then skips the separate layernorm). None keeps the original pre-only behaviour.


## Source code in `vllm/model_executor/layers/hpc/hpc_ihc.py`


##

`HpcRopeNorm`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.hpc.HpcRopeNorm)

Bases:

, [CustomOp](https://docs.vllm.ai/custom_op/#vllm.model_executor.custom_op.CustomOp)`HpcModule`


HPC fused RoPE + QK-Norm + KV-Cache-Write (+ optional FP8 Q quant).

Registered as a sub-module in model layers (e.g. HunYuanAttention). The QK-Norm weights are read directly from the fallback norm modules (built in float32 when HPC is active), eliminating the derived copy.

forward() is dispatched by CustomOp framework: - In compiled mode: forward_cuda() calls torch.ops.vllm.hpc_rope_norm_forward as a splitting point — internal Python control flow is opaque to torch.compile (its kernel launches can still be CUDA-graph captured). - In eager/native mode: forward_native() falls back to forward_cuda().

Methods:

-
–[forward_cuda](https://docs.vllm.ai#vllm.model_executor.layers.hpc.HpcRopeNorm.forward_cuda)CUDA path: invoke the torch custom op as a compile splitting point.

-
–[forward_native](https://docs.vllm.ai#vllm.model_executor.layers.hpc.HpcRopeNorm.forward_native)Native fallback path: delegates to forward_cuda().

-
–[register_layer_name](https://docs.vllm.ai#vllm.model_executor.layers.hpc.HpcRopeNorm.register_layer_name)Register layer_name and add self to the global registry.

-
–[support](https://docs.vllm.ai#vllm.model_executor.layers.hpc.HpcRopeNorm.support)Check whether HpcRopeNorm is supported for the given config.


## Source code in `vllm/model_executor/layers/hpc/rope_norm.py`


|
|

###

`_forward_impl(qkv, kv_cache, attn_metadata, attn_layer, output)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.hpc.HpcRopeNorm._forward_impl)

Actual forward logic called by the custom op.

Writes processed q into *output* and attaches extra params (e.g. FP8 scales) to *attn_layer* as attributes.

## Source code in `vllm/model_executor/layers/hpc/rope_norm.py`


|
|

###

`_kv_write_scratch(cache)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.hpc.HpcRopeNorm._kv_write_scratch)

Throwaway dense K/V pages for the stride-aware fallback path.

`hpc.rope_norm_store_kv[_fp8]`

always writes the paged cache itself (rotated K/V *and* zero padding for the tail of every request's last block), addressing it densely. When the real pages are not dense those writes would land on unrelated blocks, so they are redirected here by pairing this scratch cache with an all-zero block table; the real data is taken out through `out_k`

/`out_v`

instead.

Returns a (2, 1, block_size, num_kv_heads, head_dim) tensor: index 0 is the key scratch page, index 1 the value scratch page.

## Source code in `vllm/model_executor/layers/hpc/rope_norm.py`


###

`_scatter_kv_cache(cache, src, slot_mapping)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.hpc.HpcRopeNorm._scatter_kv_cache)

Write dense per-token K (or V) into a paged cache view.

Used on the stride-aware fallback path (see `_forward_impl`

). `cache`

is a (num_blocks, block_size, num_kv_heads, head_dim) view with arbitrary block/token/head strides; `src`

is the dense (num_tokens, num_kv_heads, head_dim) buffer produced by the fused HPC kernel. FP8 payloads are moved as raw bytes because `index_copy_`

has no FP8 kernel.

Padded tokens carry `PAD_SLOT_ID`

(-1); clamping sends them to the reserved null block instead of tripping `index_copy_`

's bounds check. This keeps the op CUDA-graph safe (static shape, no host sync), unlike masking the padded rows out.

## Source code in `vllm/model_executor/layers/hpc/rope_norm.py`


###

`_zero_pad_last_blocks(key_cache, value_cache, seq_lens, block_table)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.hpc.HpcRopeNorm._zero_pad_last_blocks)

Zero the unused tail slots of each request's last block.

The HPC attention kernels read whole blocks, so the slots past `seq_len`

must be zero. The fused op normally does this itself; on the fallback path its (densely addressed) padding writes are discarded, so the padding is reapplied here through the real, strided cache views.

Shapes are static and no value is inspected on the host, so this stays CUDA-graph capturable. It is also self-contained: each request's last block is read, masked and written back, so slots that must be preserved (and requests padded in for graph capture, whose `seq_len`

is 0) keep their previous contents instead of being redirected somewhere.

## Source code in `vllm/model_executor/layers/hpc/rope_norm.py`


###

`forward_cuda(qkv, layer_name)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.hpc.HpcRopeNorm.forward_cuda)

CUDA path: invoke the torch custom op as a compile splitting point.

## Source code in `vllm/model_executor/layers/hpc/rope_norm.py`


###

`forward_native(qkv, layer_name)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.hpc.HpcRopeNorm.forward_native)

Native fallback path: delegates to forward_cuda().

For now, the default native path will use CUDA backend path. Other platforms may override via OOT registration.

## Source code in `vllm/model_executor/layers/hpc/rope_norm.py`


###

`register_layer_name(layer_name)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.hpc.HpcRopeNorm.register_layer_name)

Register layer_name and add self to the global registry.

The global registry is needed because the bottom-level torch op (hpc_rope_norm_forward) is a module-level function and needs to route back to the correct instance via layer_name.

## Source code in `vllm/model_executor/layers/hpc/rope_norm.py`


###

`support(num_heads, num_kv_heads, head_dim, kv_cache_dtype)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.hpc.HpcRopeNorm.support)

Check whether HpcRopeNorm is supported for the given config.

## Source code in `vllm/model_executor/layers/hpc/rope_norm.py`


##

`QkNormPolicy`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.hpc.QkNormPolicy)

Bases: [IntEnum](https://docs.python.org/3/library/enum.html#enum.IntEnum)

Order of QK-RMSNorm relative to RoPE in the fused HPC rope_norm kernel.

The values are part of the HPC kernel ABI (passed through as ints), so they must stay in sync with the kernel's expectations.

## Source code in `vllm/model_executor/layers/hpc/rope_norm.py`


##

`hpc_gated_mla_gemm(x, weight, atten_output)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.hpc.hpc_gated_mla_gemm)

Fused `atten_output * sigmoid(x @ weight.T)`

.

Parameters:

-

(`x`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.hpc.hpc_gated_mla_gemm(x))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)`[m, k]`

bfloat16, contiguous. -

(`weight`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.hpc.hpc_gated_mla_gemm(weight))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)`[n, k]`

bfloat16, contiguous and row-major (the kernel transposes it).`n`

must be a multiple of 256. -

(`atten_output`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.hpc.hpc_gated_mla_gemm(atten_output))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)`[m, n]`

bfloat16, contiguous.

Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)`[m, n]`

bfloat16.

## Source code in `vllm/model_executor/layers/hpc/gated_mla.py`


##

`hpc_gated_mla_supported(gating_type, attn_output_gate)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.hpc.hpc_gated_mla_supported)

Gate for running the MLA output gating through hpc.gated_mla_gemm.