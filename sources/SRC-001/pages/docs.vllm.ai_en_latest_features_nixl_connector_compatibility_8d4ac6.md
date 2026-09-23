source: https://docs.vllm.ai/en/latest/features/nixl_connector_compatibility/
lastmod: 2026-09-23

# NixlConnector Compatibility Matrix[¶](https://docs.vllm.ai#nixlconnector-compatibility-matrix)

This page documents the feature compatibility of **disaggregated prefilling with the NixlConnector**. For general usage instructions, see the [NixlConnector Usage Guide](https://docs.vllm.ai/nixl_connector_usage/). For an overview of disaggregated prefilling, see [Disaggregated Prefilling](https://docs.vllm.ai/disagg_prefill/).

Note

This page reflects the current state of the codebase and is subject to change as features evolve. Entries marked 🟠 or ❌ may link to tracking issues. See the [ NIXL connector roadmap](https://github.com/vllm-project/vllm/issues/33702) for upcoming feature development.

**Legend:**

- ✅ = Fully supported
- 🟠 = Partial support (see footnotes)
- ❌ = Not supported
- ❔ = Unknown / not yet validated
- 🚧 = Work in progress

Universally supported features

The following features work with **all** model architectures when using NixlConnector PD disaggregated serving:

[Chunked Prefill](https://docs.vllm.ai/configuration/optimization/#chunked-prefill) | [APC (Prefix Caching)](https://docs.vllm.ai/automatic_prefix_caching/) | [Data Parallel](https://docs.vllm.ai/serving/data_parallel_deployment/) | CUDA graph | Logprobs | Prompt Logprobs | [Prompt Embeds](https://docs.vllm.ai/prompt_embeds/) | Multiple NIXL backends (UCX, GDS, LIBFABRIC, etc.)

## Model Architecture x Capability[¶](https://docs.vllm.ai#model-architecture-x-capability)

| Model type | Basic PD | Spec Decode | Hetero TP | Cross-layer blocks | SWA | Host buffer | Hetero block size |
|---|---|---|---|---|---|---|---|
| Dense Transformers | ✅ | ✅1 | ✅ | ✅2 | ✅ | ✅ | 🟠3 |
| MLA (e.g. DeepSeek-V2/V3) | ✅ | ✅1 | 🟠4 | ✅2 | ✅ | ✅ | 🟠3 |
| Sparse MLA (e.g. DeepSeek-V3.2) | ✅ | ✅1 | 🟠4 | ✅2 | ✅ | ✅ | 🟠3 |
| Hybrid SSM / Mamba | ✅ | ❔ | 🚧5 | ❌ | ✅ | ✅ | ❌6 |
| MoE | ✅ | ✅1 | ✅ | ✅2 | ✅ | ✅ | 🟠3 |
| Multimodal | ❔ | ❔ | ❔ | ❔ | ❔ | ❔ | ❔ |
| Encoder-Decoder | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

1 P and D instances must use compatible speculation configurations. See [Configuration Notes](https://docs.vllm.ai#configuration-notes) below for what must match and what may differ.

2 Cross-layer contiguity is achieved by using a `BLHNC`

layout (set via `VLLM_KV_CACHE_LAYOUT=BLHNC`

).

3 Supported only when HMA is **not** required (i.e., non-hybrid models). Block IDs are remapped automatically. Only P block size < D block size is supported.

4 MLA KV cache is replicated across TP workers, so heterogeneous TP works but there is no head-splitting. When P TP > D TP, only a single read is executed (redundant ranks are skipped). D TP > P TP also works.

5 Hybrid SSM (Mamba) models require **homogeneous TP** (`P TP == D TP`

). Heterogeneous TP is not yet supported for Mamba layers.

6 HMA (required by hybrid models) does not support different remote block sizes.

## Configuration Notes[¶](https://docs.vllm.ai#configuration-notes)

### What must match between P and D[¶](https://docs.vllm.ai#what-must-match-between-p-and-d)

By default, a **compatibility hash** is checked during handshake. P and D instances must agree on:

- vLLM version and NIXL connector version
- Model (architecture, dtype, number of KV heads, head size, number of hidden layers)
- Attention backend
- KV cache dtype (
`cache_dtype`

) - EAGLE/MTP-style speculative method and draft-model configuration
- NIXL transfer mode (push vs pull) — a push (WRITE) connector and a pull (READ) connector use incompatible transfer protocols and must never be paired

Warning

Disable the hash check with `--kv-transfer-config '{"kv_connector_extra_config": {"enforce_handshake_compat": false}}'`

at your own risk.

### What can safely differ between P and D[¶](https://docs.vllm.ai#what-can-safely-differ-between-p-and-d)

`tensor-parallel-size`

(heterogeneous TP, subject to model restrictions above)`block-size`

(heterogeneous block size, subject to restrictions above)- Number of KV cache blocks (determined by available memory on each instance)
`num_speculative_tokens`

(prefill and decode may use different draft depths)- Draft-model
`attention_backend`

(each instance auto-selects independently; the resulting KV block layout is validated at handshake time rather than via the compatibility hash)

### KV cache layout[¶](https://docs.vllm.ai#kv-cache-layout)

- NixlConnector defaults to
(head-major, formerly`LBHNC`

`HND`

) layout for optimal transfer performance (non-MLA models). `LBNHC`

(token-major, formerly`NHD`

) layout is supported but does**not**allow heterogeneous TP head splitting.- Experimental
`LBHNC`

↔`LBNHC`

permute: enable via`--kv-transfer-config '{"enable_permute_local_kv": true}'`

. Not supported with HMA.

### Pipeline parallelism[¶](https://docs.vllm.ai#pipeline-parallelism)

The default (pull) NixlConnector does **not** support `pipeline-parallel-size > 1`

together with a hybrid KV cache (HMA) layout: region indices are not a stable identity across the prefill/decode layer split, so the connector raises at startup. Use the push connector ([ NixlPushConnector](https://docs.vllm.ai/api/vllm/distributed/kv_transfer/kv_connector/v1/nixl/connector/#vllm.distributed.kv_transfer.kv_connector.v1.nixl.connector.NixlPushConnector)) for pipeline parallelism with hybrid KV caches — it routes transfers by layer-name (member) identity, so a PP-sharded prefiller can write into a

`PP=1`

decoder. See [NIXL push-mode KV transfer](https://docs.vllm.ai/design/nixl_kv_push_connector/).

Current push PP + HMA limitations:

- Only the prefiller (producer) may be PP-sharded; decode-side PP is not supported.
- Hybrid SSM/Mamba layouts are not supported under PP.
- HMA requires the same block size on P and D.
- Attention-HMA member routing requires decode TP to be no greater than prefill TP.

### Quantized KV cache[¶](https://docs.vllm.ai#quantized-kv-cache)

[Quantized KV cache](https://docs.vllm.ai/quantization/quantized_kvcache/) (e.g., FP8) requires both P and D instances to use the **same** `cache_dtype`

. Mismatched cache dtypes will fail the compatibility hash check during handshake.

**Static quantization**(scales loaded from checkpoint): ✅ Supported. Scales are loaded independently by each instance from the model checkpoint.**Dynamic quantization**(scales computed at runtime): ❌ Not supported. Per-block scales are not transferred alongside KV cache data.**Packed-layout scales**(scales stored inline with weights): ✅ Supported. Scales are transferred together with the KV cache blocks.