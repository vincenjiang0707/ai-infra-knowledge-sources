source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v4/cpu/cpu_compressor/
lastmod: 2026-09-24

#

`vllm.models.deepseek_v4.cpu.cpu_compressor`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.cpu_compressor)

CPU DeepSeek-V4 compressor subclass and dispatch: partial-state-cache write and the compress -> RMSNorm -> RoPE -> FP8 quant -> KV cache store step, calling `torch.ops._C.save_partial_states_cpu`

/ `compress_norm_rope_store_cpu`

/`compress_norm_rope_store_indexer_cpu`

(`csrc/cpu/sgl-kernels/compressor.cpp`

) in place of triton-cpu.

Covers both the head_dim=512 main-attention compressor path and the head_dim=128 indexer compressor path (fp8 only -- MXFP4, `use_fp4_cache`

, never occurs on CPU: the indexer's MXFP4 cache requires a Blackwell GPU).

Classes:

-
–[DeepseekV4CPUCompressor](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.cpu_compressor.DeepseekV4CPUCompressor)CPU compressor: same state/weights as the shared base, but


##

`DeepseekV4CPUCompressor`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.cpu_compressor.DeepseekV4CPUCompressor)

Bases: [DeepseekCompressor](https://docs.vllm.ai/compressor/#vllm.models.deepseek_v4.compressor.DeepseekCompressor)

CPU compressor: same state/weights as the shared base, but `forward`

's cache-write and compress->RMSNorm->RoPE->quant->store steps always dispatch straight to the ported CPU kernels above instead of through the shared method's platform-dispatch chain. This class only ever runs on CPU, and `use_fp4_cache`

is always `False`

here (the indexer's MXFP4 cache requires a Blackwell GPU), so the shared method's MXFP4/two-stage/cutedsl/triton branches never apply.

Methods:

-
–[cache_norm_weight_fp32](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.cpu_compressor.DeepseekV4CPUCompressor.cache_norm_weight_fp32)Cache a fp32 contiguous copy of

`norm.weight`

once, right after

## Source code in `vllm/models/deepseek_v4/cpu/cpu_compressor.py`


###

`cache_norm_weight_fp32()`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.cpu.cpu_compressor.DeepseekV4CPUCompressor.cache_norm_weight_fp32)

Cache a fp32 contiguous copy of `norm.weight`

once, right after weight loading (see `DeepseekV4CPUAttention.process_weights_after_loading`

) -- the CPU kernel requires fp32/contiguous but the checkpoint loads this weight in bf16, and it never changes after loading.