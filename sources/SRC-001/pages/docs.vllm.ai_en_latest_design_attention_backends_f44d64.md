source: https://docs.vllm.ai/en/latest/design/attention_backends/
lastmod: 2026-09-24

# Attention Backend Feature Support[¶](https://docs.vllm.ai#attention-backend-feature-support)

The priority and feature tables on this page are auto-generated from the attention backend registry by `docs/mkdocs/gen_files/generate_attention_backends.py`

, based on the checks in `AttentionBackend.validate_configuration()`

.

## Setting the Attention Backend[¶](https://docs.vllm.ai#setting-the-attention-backend)

### Command Line[¶](https://docs.vllm.ai#command-line)

There are two ways to specify the backend from the command line:

**Option 1: Using --attention-backend (simple)**

**Option 2: Using --attention-config.backend / -ac.backend (structured config)**


# Dot notation
```bash
vllm serve <model> --attention-config.backend FLASH_ATTN
vllm serve <model> -ac.backend FLASH_ATTN
# JSON format
vllm serve <model> --attention-config '{"backend": "FLASH_ATTN"}'
vllm serve <model> -ac '{"backend": "FLASH_ATTN"}'
```



Note:`--attention-backend`

and`--attention-config.backend`

are mutually exclusive. Use one or the other, not both.

### Python API[¶](https://docs.vllm.ai#python-api)

Use [ AttentionConfig](https://docs.vllm.ai/api/vllm/config/attention/#vllm.config.attention.AttentionConfig) with the

[class:](https://docs.vllm.ai/api/vllm/entrypoints/llm/#vllm.entrypoints.llm.LLM)

`LLM`

from vllm import LLM
from vllm.config import AttentionConfig
from vllm.v1.attention.backends.registry import AttentionBackendEnum
# Method 1: Using AttentionConfig with enum
llm = LLM(
model="Qwen/Qwen3-0.6B",
attention_config=AttentionConfig(backend=AttentionBackendEnum.FLASH_ATTN),
)
# Method 2: Using attention_backend parameter with string
llm = LLM(
model="Qwen/Qwen3-0.6B",
attention_backend="FLASH_ATTN",
)


## Backend Selection Behavior[¶](https://docs.vllm.ai#backend-selection-behavior)

### Triton/FlashAttention Composite[¶](https://docs.vllm.ai#tritonflashattention-composite)

On Hopper, `TRITON_FLASH_ATTN`

is preferred for compatible multimodal-prefix configurations. It uses Triton when the current queries need bidirectional image attention and FlashAttention for causal text prefills and decode, with a shared KV cache. The causal child must resolve to FA4. This happens automatically for FA4-only shapes such as head size 512 and models whose version policy promotes all layers to FA4, including Gemma 4. A standalone head-size-256 configuration whose version policy selects FA3 falls back to Triton for the whole layer.

No attention override is needed for supported multimodal models:

### Triton/FlashInfer Composite[¶](https://docs.vllm.ai#tritonflashinfer-composite)

On Blackwell, `TRITON_FLASHINFER`

is preferred for compatible multimodal-prefix configurations, including Gemma 4 with BF16 or FP8 KV cache. It uses Triton when a batch's current queries require bidirectional image attention, and FlashInfer for causal text prefills and decode. Historical image tokens alone do not select Triton.

This instantiates `create_composite_attention_backend`

from `vllm/v1/attention/backends/composite.py`

with Triton, FlashInfer, and [ MMPrefixAttentionRouting](https://docs.vllm.ai/api/vllm/v1/attention/backends/composite/#vllm.v1.attention.backends.composite.MMPrefixAttentionRouting). The reusable factory owns child implementations, metadata dispatch, compatible cache requirements, and workspace sharing. The routing policy selects the child and defines graph-capture safety. Other combinations can reuse the same machinery.

The backend supports head dimensions 256/512, FP16/BF16 and FP8 KV cache, and 64-token kernel pages with a head-major cache layout. TRTLLM handles causal attention at both head dimensions; its hdim512 kernels do not support 128-token pages. For Gemma 4, full CUDA graphs cover single-token batches; multi-token batches use the non-full-graph execution path. Models whose image masks extend beyond the sliding window cannot use full attention graphs with this composite. Context parallelism, R-SWA, attention sinks, and adaptive verification are not supported by this composite.

It can also be selected explicitly:

### Manual Selection[¶](https://docs.vllm.ai#manual-selection)

When you explicitly set a backend via `--attention-backend`

or [ AttentionConfig](https://docs.vllm.ai/api/vllm/config/attention/#vllm.config.attention.AttentionConfig):

- The backend is
**validated**against your configuration (model dtype, head size, compute capability, etc.) - If the backend
**doesn't support**your configuration, an error is raised with the specific reason - If valid, the backend is used

Example error when selecting an incompatible backend:

ValueError: Selected backend FLASHMLA is not valid for this configuration.
Reason: ['compute capability not supported']


### Automatic Selection[¶](https://docs.vllm.ai#automatic-selection)

When no backend is specified (the default):

- vLLM iterates through backends in
**priority order**(see tables below) - Each backend is validated against your configuration
- The
**first compatible backend**is selected - If no backend is compatible, an error is raised listing all backends and their incompatibility reasons

## Backend Priority (CUDA)[¶](https://docs.vllm.ai#backend-priority-cuda)

When no backend is explicitly selected, vLLM chooses the first compatible backend from these priority-ordered lists.

Priority is **1 = highest** (tried first).

### Standard Attention (MHA, MQA, GQA)[¶](https://docs.vllm.ai#standard-attention-mha-mqa-gqa)

**Blackwell (SM 10.x):**

| Priority | Backend |
|---|---|
| 1 | `FLASHINFER` |
| 2 | `FLASH_ATTN` |
| 3 | `TRITON_ATTN` |
| 4 | `FLEX_ATTENTION` |
| 5 | `TURBOQUANT` |

**Ampere/Hopper (SM 8.x-9.x):**

| Priority | Backend |
|---|---|
| 1 | `FLASH_ATTN` |
| 2 | `FLASHINFER` |
| 3 | `TRITON_ATTN` |
| 4 | `FLEX_ATTENTION` |
| 5 | `TURBOQUANT` |

### MLA Attention (DeepSeek-style)[¶](https://docs.vllm.ai#mla-attention-deepseek-style)

**Blackwell (SM 10.x):**

| Priority | Backend |
|---|---|
| 1 | `FLASHINFER_MLA` |
| 2 | `TOKENSPEED_MLA` |
| 3 | `CUTLASS_MLA` |
| 4 | `FLASH_ATTN_MLA` |
| 5 | `FLASHMLA` |
| 6 | `TRITON_MLA` |
| 7 | `FLASHINFER_MLA_SPARSE` * |
| 8 | `FLASHMLA_SPARSE` |


*For sparse MLA, FP8 KV cache always prefers`FLASHINFER_MLA_SPARSE`

. With BF16 KV cache,`FLASHINFER_MLA_SPARSE`

is preferred for low query-head counts (<= 16), while`FLASHMLA_SPARSE`

is preferred otherwise.

Note:ROCm and CPU platforms have their own selection logic. See the platform-specific documentation for details.

## Legend[¶](https://docs.vllm.ai#legend)

| Column | Description |
|---|---|
Dtypes | Supported model data types (fp16, bf16, fp32) |
KV Dtypes | Supported KV cache data types (`auto` , `fp8` , `fp8_e4m3` , etc.) |
Block Sizes | Supported KV cache block sizes (%N means multiples of N) |
Head Sizes | Supported attention head sizes |
Sink | Attention sink support (for StreamingLLM) |
Non-Causal | Non-causal (bidirectional) attention support for decoder models |
Sparse | Sparse attention support (MLA only) |
MM Prefix | Multimodal prefix full attention support |
DCP | Decode Context Parallelism support (`--decode-context-parallel-size` ) |
Attention Types | Supported attention patterns (Decoder, Encoder, Enc-Dec) |
Compute Cap. | Required CUDA compute capability (N/A for non-CUDA backends) |

**Symbols:** ✅ = Supported, ❌ = Not supported

## Standard Attention (MHA, MQA, GQA) Backends[¶](https://docs.vllm.ai#standard-attention-mha-mqa-gqa-backends)

| Backend | Version | Dtypes | KV Dtypes | Block Sizes | Head Sizes | Sink | Non-Causal | MM Prefix | DCP | Attention Types | Compute Cap. |
|---|---|---|---|---|---|---|---|---|---|---|---|
`B12X` | bf16 | `auto` | Any | 64, 128, 192, 256 | ✅ | ❌ | ❌ | ❌ | Decoder | Any | |
`CPU_ATTN` | fp16, bf16, fp32 | `auto` , `fp8` , `fp8_e4m3` , `fp8_e5m2` | %32 | 32, 64, 80, 96, 112, 128, 160, 192, 224, 256, 512 | ❌ | ✅ | ❌ | ❌ | All | N/A | |
`CUTLASS_MSA` | fp16, bf16 | `auto` | Any | Any | ❌ | ❌ | ❌ | ❌ | Decoder | Any | |
`FLASHINFER` | Native† | fp16, bf16 | `auto` , `float16` , `bfloat16` , `fp8` , `fp8_e4m3` , `fp8_e5m2` , `nvfp4_4over6` | 16, 32, 64, 128, 256, 512, 1024 | 64, 128, 256, 512 | ❌ | ✅ | ❌ | ✅ | Decoder | 8.x-9.x |
`FLASHINFER` | XQA† | fp16, bf16 | `auto` , `float16` , `bfloat16` , `fp8` , `fp8_e4m3` , `fp8_e5m2` , `nvfp4_4over6` | 16, 32, 64, 128, 256, 512, 1024 | 64, 128, 256, 512 | ❌ | ❌ | ❌ | ✅ | Decoder | 9.0 |
`FLASHINFER` | trtllm-gen† | fp16, bf16 | `auto` , `float16` , `bfloat16` , `fp8` , `fp8_e4m3` , `fp8_e5m2` , `nvfp4` , `nvfp4_4over6` | 16, 32, 64, 128, 256, 512, 1024 | 64, 128, 256, 512 | ✅ | ✅ | ❌ | ✅ | Decoder | 10.x |
`FLASHMLA_MEGA_ATTN_DSV41` | fp16, bf16 | `auto` , `fp8_ds_mla` , `fp8` , `nvfp4_ds_mla` | 128 | Any | ❌ | ❌ | ❌ | ❌ | Decoder | 10.x | |
`FLASHMLA_SPARSE_DSV41` | fp16, bf16 | `auto` | Any | Any | ❌ | ❌ | ❌ | ❌ | Decoder | Any | |
`FLASH_ATTN` | FA2* | fp16, bf16 | `auto` , `float16` , `bfloat16` | %16 | Any | ❌ | ✅ | ❌ | ✅ | All | ≥8.0 |
`FLASH_ATTN` | FA3* | fp16, bf16 | `auto` , `float16` , `bfloat16` , `fp8` , `fp8_e4m3` | %16 | Any | ✅ | ✅ | ❌ | ✅ | All | 9.x |
`FLASH_ATTN` | FA4* | fp16, bf16 | `auto` , `float16` , `bfloat16` , `fp8` , `fp8_e4m3` | %16 | Any | ✅ | ✅ | ❌ | ✅ | All | ≥10.0 |
`FLASH_ATTN_DIFFKV` | fp16, bf16 | `auto` | Any | Any | ❌ | ❌ | ❌ | ✅ | Decoder | Any | |
`FLEX_ATTENTION` | fp16, bf16, fp32 | `auto` , `float16` , `bfloat16` | %16 | Any | ❌ | ✅ | ✅ | ❌ | Decoder, Encoder Only | Any | |
`HPC_ATTN` | fp16, bf16 | `auto` , `bfloat16` , `fp8_e4m3` | 64 | 128 | ❌ | ❌ | ❌ | ❌ | Decoder | Any | |
`ROCM_AITER_FA` | fp16, bf16 | `auto` , `float16` , `bfloat16` , `fp8` , `fp8_e4m3` , `fp8_e5m2` | 16, 32 | 64, 128, 256 | ✅ | ✅ | ❌ | ❌ | Decoder | N/A | |
`ROCM_AITER_UNIFIED_ATTN` | fp16, bf16 | `auto` , `float16` , `bfloat16` , `fp8` , `fp8_e4m3` , `fp8_e5m2` | %16 | Any | ✅ | ❌ | ✅ | ❌ | All | N/A | |
`ROCM_ATTN` | fp16, bf16, fp32 | `auto` , `float16` , `bfloat16` , `fp8` , `fp8_e4m3` , `fp8_e5m2` | %16 | 32, 64, 80, 96, 128, 160, 192, 224, 256 | ❌ | ✅ | ✅ | ❌ | Decoder, Encoder, Encoder Only | N/A | |
`TRITON_ATTN` | fp16, bf16, fp32 | `auto` , `float16` , `bfloat16` , `fp8` , `fp8_e4m3` , `fp8_e5m2` , `int4_per_token_head` , `int8_per_token_head` , `fp8_per_token_head` | %16 | Any | ✅ | ✅ | ✅ | ❌ | All | Any | |
`TRITON_ATTN_DIFFKV` | fp16, bf16 | `auto` , `bfloat16` | Any | Any | ❌ | ❌ | ❌ | ❌ | Decoder | Any | |
`TRITON_MSA` | fp16, bf16 | `auto` | Any | Any | ❌ | ❌ | ❌ | ❌ | Decoder | Any | |
`TURBOQUANT` | fp16, bf16 | `turboquant_k8v4` , `turboquant_4bit_nc` , `turboquant_k3v4_nc` , `turboquant_3bit_nc` | 16, 32, 64, 128 | Any | ❌ | ❌ | ❌ | ❌ | Decoder | Any |


†FlashInfer Native is the regular FlashInfer path. XQA is the SM90 decode path exposed through FlashInfer's TRTLLM decode API. trtllm-gen is used on SM100 and supports sinks. Disable XQA/trtllm-gen via`--attention-config.use_trtllm_attention=0`

.

*Specify the FlashAttention version via`--attention-config.flash_attn_version=2`

,`3`

, or`4`

. Default is FA4 on SM100+ (Blackwell), FA3 on SM90 (Hopper), FA2 otherwise.On Blackwell, when the FlashAttention backend is selected,

`head_size=256`

is served by a dedicated FA4 kernel that requires a KV cache block size of 128 (advertised automatically, so it is picked as long as`--block-size`

is not pinned) and does not support logit soft capping, attention sinks, mm_prefix/R-SWA masking, DCP, or windowed encoder attention. Those configurations transparently fall back to FA2. A pinned`--block-size`

that is not a multiple of 128 instead makes FlashAttention ineligible for such models, which is an error if the backend was requested explicitly.

### b12x[¶](https://docs.vllm.ai#b12x)

The optional [b12x](https://pypi.org/project/b12x/) backend supports causal decoder attention on NVIDIA SM120 and SM121 GPUs. Install and select it with:

## MiniMax M3 Sparse Attention Backends[¶](https://docs.vllm.ai#minimax-m3-sparse-attention-backends)

Block-sparse GQA backend used by MiniMax M3 sparse ("lightning indexer") layers. It is wired in directly by the model and is not part of the automatic priority lists above. A lightning indexer scores KV blocks, the top-k blocks (plus fixed init/local blocks) are selected, and attention attends only to those blocks; index keys live in a separate side cache.

| Backend | Dtypes | KV Dtypes | Block Sizes | Head Sizes | Sink | Non-Causal | MM Prefix | DCP | Attention Types | Compute Cap. |
|---|---|---|---|---|---|---|---|---|---|---|
`MINIMAX_M3_SPARSE` | bf16, fp16 | `bfloat16` , `fp8` , `fp8_e4m3` , `fp8_e5m2` | 128 | 128 | ❌ | ❌ | ❌ | ❌ | Decoder | Any |

## MLA (Multi-head Latent Attention) Backends[¶](https://docs.vllm.ai#mla-multi-head-latent-attention-backends)

MLA uses separate backends for prefill and decode phases.

### Prefill Backends[¶](https://docs.vllm.ai#prefill-backends)

To explicitly select a prefill backend, use `-ac.mla_prefill_backend=<BACKEND>`

(e.g., `FLASH_ATTN`

, `FLASHINFER`

). Otherwise, the prefill backend is selected automatically at runtime based on hardware and configuration.

| Backend | Description | Dtypes | Compute Cap. | Notes |
|---|---|---|---|---|
`FLASH_ATTN` ‡ | FlashAttention varlen (FA2/FA3/FA4) | fp16, bf16 | Any | (qk_nope_head_dim=128, qk_rope_head_dim=64, v_head_dim=128) or (qk_nope_head_dim=192, qk_rope_head_dim=64, v_head_dim=256) or (qk_nope_head_dim=64, qk_rope_head_dim=64, v_head_dim=128) or (qk_nope_head_dim=256, qk_rope_head_dim=0, v_head_dim=256) only |
`TRTLLM_RAGGED` | TensorRT-LLM ragged attention | fp16, bf16 | 10.x | (qk_nope_head_dim=128, qk_rope_head_dim=64, v_head_dim=128) or (qk_nope_head_dim=192, qk_rope_head_dim=64, v_head_dim=256) only |
`FLASHINFER` | FlashInfer CUTLASS backend | fp16, bf16 | 10.x | (qk_nope_head_dim=128, qk_rope_head_dim=64, v_head_dim=128) only |
`TOKENSPEED_MLA` | fp16, bf16 | 10.x | (qk_nope_head_dim=128, qk_rope_head_dim=64, v_head_dim=128) only |


‡Automatic selection tries FlashAttention first. On Blackwell (SM100), the fallback order is TRT-LLM Ragged, FlashInfer, then TokenSpeed MLA; for (qk_nope_head_dim=192, qk_rope_head_dim=64, v_head_dim=256) TRT-LLM Ragged is tried before FlashAttention. On other GPUs, only FlashAttention is considered.

### Decode Backends[¶](https://docs.vllm.ai#decode-backends)

MLA decode backends are selected using the standard `-ac.backend=<BACKEND>`

argument (e.g., `FLASHMLA`

, `TRITON_MLA`

).

| Backend | Dtypes | KV Dtypes | Block Sizes | Head Sizes | Sink | Non-Causal | Sparse | MM Prefix | DCP | Attention Types | Compute Cap. |
|---|---|---|---|---|---|---|---|---|---|---|---|
`AMX_MLA` | bf16 | `auto` | %32 | 576 | ❌ | ❌ | ❌ | ❌ | ❌ | Decoder | Any |
`CPU_MLA` | fp16, bf16, fp32 | `auto` | 16 | 576 | ❌ | ❌ | ❌ | ❌ | ❌ | Decoder | N/A |
`CUTLASS_MLA` | fp16, bf16 | `auto` , `float16` , `bfloat16` , `fp8` , `fp8_e4m3` | 128 | Any | ❌ | ❌ | ❌ | ❌ | ✅ | Decoder | 10.x |
`FLASHINFER_MLA` | fp16, bf16 | `auto` , `float16` , `bfloat16` , `fp8` , `fp8_e4m3` | 32, 64 | Any | ❌ | ✅ | ❌ | ❌ | ✅ | Decoder | 10.x |
`FLASHINFER_MLA_SPARSE` | fp16, bf16 | `auto` , `float16` , `bfloat16` , `fp8` , `fp8_e4m3` | 32, 64 | Any | ❌ | ❌ | ❌ | ❌ | ✅ | Decoder | 10.x |
`FLASHINFER_MLA_SPARSE_DSV41` | bf16 | `auto` , `bfloat16` , `fp8` , `fp8_e4m3` , `fp8_ds_mla` | 128 | 512 | ✅ | ❌ | ✅ | ❌ | ❌ | Decoder | 10.x, 12.x |
`FLASHINFER_MLA_SPARSE_SM120` | bf16 | `auto` , `fp8` , `fp8_e4m3` , `fp8_ds_mla` | 64, 256 | Any | ❌ | ❌ | ❌ | ❌ | ❌ | Decoder | 12.x |
`FLASHINFER_MLA_SPARSE_SM90` | bf16 | `auto` , `bfloat16` , `fp8` , `fp8_e4m3` | %64 | 512, 576 | ❌ | ❌ | ✅ | ❌ | ❌ | Decoder | 9.x |
`FLASHMLA` | fp16, bf16 | `auto` , `float16` , `bfloat16` , `fp8` , `fp8_e4m3` | 64 | Any | ❌ | ❌ | ❌ | ❌ | ✅ | Decoder | 9.x-10.x |
`FLASHMLA_SPARSE` | bf16 | `auto` , `bfloat16` , `fp8_ds_mla` , `nvfp4_ds_mla` | 64 | 576, 512 | ❌ | ❌ | ✅ | ❌ | ✅ | Decoder | 9.x-10.x |
`FLASH_ATTN_MLA` | fp16, bf16 | `auto` , `float16` , `bfloat16` | %16 | Any | ❌ | ❌ | ❌ | ❌ | ✅ | Decoder | 9.x |
`FLASH_ATTN_MLA_SPARSE` | fp16, bf16 | `auto` , `float16` , `bfloat16` | 64 | Any | ❌ | ❌ | ✅ | ❌ | ❌ | Decoder | 9.x |
`ROCM_AITER_MLA` | fp16, bf16 | `auto` , `float16` , `bfloat16` , `fp8` , `fp8_e4m3` , `fp8_e5m2` | %1 | Any | ❌ | ❌ | ❌ | ❌ | ✅ | Decoder | N/A |
`ROCM_AITER_MLA_SPARSE` | fp16, bf16 | `auto` , `float16` , `bfloat16` , `fp8` , `fp8_e4m3` | 1, %16 | Any | ❌ | ❌ | ✅ | ❌ | ❌ | Decoder | N/A |
`ROCM_AITER_TRITON_MLA` | fp16, bf16 | `auto` | Any | Any | ❌ | ❌ | ❌ | ❌ | ✅ | Decoder | N/A |
`TOKENSPEED_MLA` | fp16, bf16 | `fp8` , `fp8_e4m3` | 32, 64 | Any | ❌ | ✅ | ❌ | ❌ | ✅ | Decoder | 10.x |
`TRITON_MLA` | fp16, bf16 | `auto` , `float16` , `bfloat16` , `fp8` , `fp8_e4m3` | %16 | Any | ❌ | ✅ | ❌ | ❌ | ✅ | Decoder | Any |
`XPU_MLA_SPARSE` | fp16, bf16 | `auto` , `float16` , `bfloat16` | Any | 576 | ❌ | ❌ | ✅ | ❌ | ❌ | Decoder | Any |

### DeepSeek V4 Decode Backends[¶](https://docs.vllm.ai#deepseek-v4-decode-backends)

DeepSeek V4 sparse MLA uses its own decode backends, selected via `--attention-backend=<BACKEND>`

(e.g., `FLASHMLA_SPARSE_DSV4`

, `FLASHINFER_MLA_SPARSE_DSV4`

). They share the V4 sparse-index pipeline (compressor + SWA + indexer, 256-token blocks, head 512); default on NVIDIA is `FLASHINFER_MLA_SPARSE_DSV4`

on SM12x and `FLASHMLA_SPARSE_DSV4`

on other supported CUDA architectures.

| Backend | Dtypes | KV Dtypes | Block Sizes | Head Sizes | Sink | Non-Causal | Sparse | MM Prefix | DCP | Attention Types | Compute Cap. |
|---|---|---|---|---|---|---|---|---|---|---|---|
`FLASHINFER_MLA_SPARSE_DSV4` | bf16 | `auto` , `bfloat16` , `fp8` , `fp8_e4m3` , `fp8_ds_mla` | 256 | 512 | ✅ | ❌ | ✅ | ❌ | ❌ | Decoder | 10.x, 12.x |
`FLASHMLA_SPARSE_DSV4` | fp16, bf16 | `auto` | Any | Any | ❌ | ❌ | ❌ | ❌ | ❌ | Decoder | Any |
`ROCM_FLASHMLA_SPARSE_DSV4` | fp16, bf16 | `auto` | Any | Any | ❌ | ❌ | ❌ | ❌ | ❌ | Decoder | N/A |