source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v4/cpu/cpu_sparse/
lastmod: 2026-09-23

#

`vllm.models.deepseek_v4.cpu.cpu_sparse`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.cpu_sparse)

CPU DeepSeek-V4 attention subclass.

`forward_mqa`

resolves SWA/compressed top-k indices to paged-cache slot ids and calls the fused `flash_mla_with_kvcache_cpu`

kernel. `_o_proj`

stays eager -- not on the attention hot path.

Classes:

-
–[DeepseekV4CPUAttention](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.cpu_sparse.DeepseekV4CPUAttention)CPU sparse MLA attention layer for DeepSeek V4.

-
–[DeepseekV4CPUIndexer](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.cpu_sparse.DeepseekV4CPUIndexer)CPU indexer: the C4A short-context fallback runs as eager PyTorch

-
–[DeepseekV4CPUIndexerCache](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.cpu_sparse.DeepseekV4CPUIndexerCache)CPU indexer K-cache descriptor: same fields as the shared base, just


##

`DeepseekV4CPUAttention`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.cpu_sparse.DeepseekV4CPUAttention)

Bases: [DeepseekV4Attention](https://docs.vllm.ai/attention/#vllm.models.deepseek_v4.attention.DeepseekV4Attention)

CPU sparse MLA attention layer for DeepSeek V4.

Methods:

-
–[forward](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.cpu_sparse.DeepseekV4CPUAttention.forward)CPU override: wraps attention-prep + MLA + output projection in the

-
–[process_weights_after_loading](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.cpu_sparse.DeepseekV4CPUAttention.process_weights_after_loading)Cache fp32-contiguous copies of tensors CPU kernels want that way


## Source code in `vllm/models/deepseek_v4/cpu/cpu_sparse.py`


|
|

###

`_fused_qnorm_rope_kv_insert(q, kv, positions, attn_metadata)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.cpu_sparse.DeepseekV4CPUAttention._fused_qnorm_rope_kv_insert)

CPU override: only the fp8_ds_mla (uint8) SWA cache layout is supported here, so the base method's bf16/per-tensor-fp8 branches are dropped.

## Source code in `vllm/models/deepseek_v4/cpu/cpu_sparse.py`


###

`_prepare_and_attn(hidden_states, qr, kv, qr_scale, kv_score, indexer_kv_score, indexer_weights, positions, o_padded)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.cpu_sparse.DeepseekV4CPUAttention._prepare_and_attn)

CPU override: no aux streams, so query-projection+KV-insert, the indexer, and the compressor run straight-line instead of through execute_in_parallel/maybe_execute_in_parallel.

## Source code in `vllm/models/deepseek_v4/cpu/cpu_sparse.py`


###

`_sparse_indexer_and_attn(hidden_states, index_q, index_q_scale, index_weights, q, kv, positions, out)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.cpu_sparse.DeepseekV4CPUAttention._sparse_indexer_and_attn)

CPU override: identical body, minus `@eager_break_during_capture`

(this platform never captures a CUDA graph, so it was a no-op).

## Source code in `vllm/models/deepseek_v4/cpu/cpu_sparse.py`


###

`_split_qkv_and_norm(qr_kv)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.cpu_sparse.DeepseekV4CPUAttention._split_qkv_and_norm)

CPU override: two `RMSNorm`

calls instead of the shared `fused_q_kv_rmsnorm`

, whose raw `@triton.jit`

kernel fails to link under triton-cpu (`undefined symbol: __truncdfbf2`

).

## Source code in `vllm/models/deepseek_v4/cpu/cpu_sparse.py`


###

`_wrap_wo_a_process_weights_after_loading()`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.cpu_sparse.DeepseekV4CPUAttention._wrap_wo_a_process_weights_after_loading)

Snapshot and pack `wo_a`

's weight into a bf16 copy for `bmm_cpu`

before the FP8 kernel's own `process_weights_after_loading`

VNNI-repacks it in place for row-major reads `_o_proj`

never does.

## Source code in `vllm/models/deepseek_v4/cpu/cpu_sparse.py`


###

`forward(positions, hidden_states, llama_4_scaling=None)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.cpu_sparse.DeepseekV4CPUAttention.forward)

CPU override: wraps attention-prep + MLA + output projection in the CPU-only opaque custom op (see `_deepseek_v4_cpu_prepare_and_attn`

).

## Source code in `vllm/models/deepseek_v4/cpu/cpu_sparse.py`


###

`process_weights_after_loading(act_dtype)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.cpu_sparse.DeepseekV4CPUAttention.process_weights_after_loading)

Cache fp32-contiguous copies of tensors CPU kernels want that way but that arrive bf16 (rotary cos/sin table, compressor RMSNorm weights) -- cast once here instead of per forward call.

Runs after every quantized layer's own `process_weights_after_loading`

(see `is_deferred_attention_layer`

); `wo_a`

's packing must happen *before* that phase instead, so it's a separate monkeypatch in `__init__`

.

## Source code in `vllm/models/deepseek_v4/cpu/cpu_sparse.py`


##

`DeepseekV4CPUIndexer`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.cpu_sparse.DeepseekV4CPUIndexer)

Bases: [DeepseekV4Indexer](https://docs.vllm.ai/attention/#vllm.models.deepseek_v4.attention.DeepseekV4Indexer)

CPU indexer: the C4A short-context fallback runs as eager PyTorch instead of Triton. Never constructed directly -- `__class__`

is swapped onto an existing `DeepseekV4Indexer`

instance post-construction.

Methods:

-
–[forward](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.cpu_sparse.DeepseekV4CPUIndexer.forward)CPU override: no aux streams, so wq_b_and_q_quant and the


## Source code in `vllm/models/deepseek_v4/cpu/cpu_sparse.py`


###

`forward(hidden_states, qr, compressed_kv_score, indexer_weights, positions, rotary_emb, qr_scale=None, skip_compressor=False)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.cpu_sparse.DeepseekV4CPUIndexer.forward)

CPU override: no aux streams, so wq_b_and_q_quant and the compressor run straight-line instead of through `maybe_execute_in_parallel`

; the short-context check drops the CUDA-only `is_current_stream_capturing()`

guard (always False here).

## Source code in `vllm/models/deepseek_v4/cpu/cpu_sparse.py`


##

`DeepseekV4CPUIndexerCache`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.cpu_sparse.DeepseekV4CPUIndexerCache)

Bases: `DeepseekV4IndexerCache`


CPU indexer K-cache descriptor: same fields as the shared base, just pointing `get_attn_backend()`

at `DeepseekV4CPUIndexerBackend`

instead of the shared, CUDA/XPU-oriented `DeepseekV4IndexerBackend`

.

## Source code in `vllm/models/deepseek_v4/cpu/cpu_sparse.py`


##

`_NoOpEvent`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.cpu_sparse._NoOpEvent)

Stand-in for `torch.cuda.Event`

on CPU: since CPU never sets an aux stream list, these events are constructed but never actually used.

##

`_deepseek_v4_cpu_prepare_and_attn(hidden_states, qr, kv, qr_scale, kv_score, indexer_kv_score, indexer_weights, positions, o_padded, layer_name)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.cpu_sparse._deepseek_v4_cpu_prepare_and_attn)

Opaque custom-op boundary around attention-prep + sparse-indexer + MLA attention + output projection -- CPU-only.

Wraps cache writes with no explicit tensor args (SWA/compressor/indexer state), which torch.compile can't otherwise track as mutations -- one opaque call sidesteps that. `_o_proj`

is folded in too because CPU's `DYNAMO_TRACE_ONCE`

mode traces exactly once, during warmup when `attn_metadata`

is `None`

; tracing `_o_proj`

separately would bake that warmup branch into the compiled graph permanently, dead-code- eliminating the whole attention computation upstream.

## Source code in `vllm/models/deepseek_v4/cpu/cpu_sparse.py`


##

`_dequant_linear_weight(layer)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.cpu_sparse._dequant_linear_weight)

Dequantize a linear layer's weight, including FP8 block scales.

`_o_proj`

reads `wo_a.weight`

directly (not via `quant_method.apply()`

), so the per-block FP8 scale must be applied here explicitly.

## Source code in `vllm/models/deepseek_v4/cpu/cpu_sparse.py`


##

`_fused_indexer_q_rope_quant_cpu(positions, index_q, index_q_cos_sin_cache, index_weights, index_weights_softmax_scale, index_weights_head_scale)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.cpu_sparse._fused_indexer_q_rope_quant_cpu)

CPU-only equivalent of `fused_indexer_q_rope_quant`

's FP8 path (CPU never reaches its MXFP4 arm -- Blackwell-only). Returns `(q_fp8, weights_out)`

, folding the per-token q scale into `index_weights`

. `positions`

/`index_q_cos_sin_cache`

are already contiguous int64/fp32, so no conversion is needed here.