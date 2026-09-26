source: https://docs.nvidia.com/dynamo/zh-CN/v-0-9-1/user-guides/multimodality-support
lastmod: 2026-09-23T23:30:39.914Z

# Multimodal Inference in Dynamo

Dynamo supports multimodal inference across multiple LLM backends, enabling models to process images, video, and audio alongside text. This section provides comprehensive documentation for deploying multimodal models.

**Security Requirement**: Multimodal processing must be explicitly enabled at startup.
See the relevant documentation for each backend for the necessary flags.

This prevents unintended processing of multimodal data from untrusted sources.

## Backend Documentation

## Support Matrix

### Backend Capabilities

* E/P/D supported in TRT-LLM with pre-computed embeddings only; image URL support is WIP ([PR #4668](https://github.com/ai-dynamo/dynamo/pull/4668))

**Pattern Key:**

**EPD**- All-in-one worker (Simple Aggregated)**E/PD**- Separate encode, combined prefill+decode**E/P/D**- All stages separate**EP/D**- Combined encode+prefill, separate decode

**Status:** ✅ Supported | 🚧 WIP | 🧪 Experimental | ❌ Not supported

### Input Format Support

## Architecture Patterns

Dynamo supports several deployment patterns for multimodal inference based on two dimensions:

-
**Encoding**: Is media encoding handled inline (within prefill) or by a separate**Encode Worker**?*Inline*: Simpler setup, encoding happens in the prefill worker*Separate (EPD)*: Dedicated encode worker transfers embeddings via**NIXL (RDMA)**, enabling independent scaling

-
**Prefill/Decode**: Are prefill and decode in the same worker or separate?*Aggregated*: Single worker handles both prefill and decode*Disaggregated*: Separate workers for prefill and decode, with KV cache transfer between them


These combine into four deployment patterns:

### EPD - Simple Aggregated

All processing happens within a single worker - the simplest setup.

**When to use:** Quick setup, smaller models, development/testing.

### E/PD - Encode Separate

Encoding happens in a separate worker; prefill and decode share the same engine.

**When to use:** Offload vision encoding to separate GPU, scale encode workers independently.

### E/P/D - Full Disaggregation

Full disaggregation with separate workers for encoding, prefill, and decode. There are two variants of this workflow:

- Prefill-first, used by vLLM
- Decode-first, used by SGLang

Prefill-first:

OR

Decode-first:

**When to use:** Maximum optimization, multi-node deployment, independent scaling of each phase.

### EP/D - Traditional Disaggregated

Encoding is combined with prefill, with decode separate.


Note:TRT-LLM’s EP/D mode skips the Python Processor - the Rust frontend handles tokenization and routes directly to the Prefill worker. For multimodal requests, the Python prefill worker still re-tokenizes/builds inputs; Rust token_ids are ignored.

**When to use:** Models without pre-computed embedding support (Llama 4), or TRT-LLM disaggregated deployment.

## Example Workflows

You can find example workflows and reference implementations for deploying multimodal models in: