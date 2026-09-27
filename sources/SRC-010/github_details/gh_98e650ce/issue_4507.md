# [Issue #4507] KV cache compression for longer context support

source: https://github.com/InternLM/lmdeploy/issues/4507
state: closed | updated: 2026-05-08T21:14:23Z
labels: 

## 正文

KV cache memory is the primary bottleneck for long-context inference in lmdeploy. At BF16, a Llama-3-8B deployment on a single 80GB A100 can support roughly 128K tokens of KV cache — beyond that, session_len gets truncated as we see reported in multiple issues here. Scaling to 512K+ context requires either more hardware or a smarter approach to KV storage.

**Proposal: KV cache compression backend**

We have been developing NexusQuant (https://github.com/jagmarques/nexusquant), a training-free KV cache compression library validated on Mistral-7B and Llama-3-8B:

- Pipeline: Hadamard rotation -> E8 lattice vector quantization -> temporal predictive coding
- 7x compression with +0.03% perplexity delta on Mistral-7B; -0.002% on Llama-3-8B (net quality improvement)
- 5.3x at strict lossless quality threshold
- No calibration data required, drop-in at inference time

At 7x compression, a session that would normally require 64 GB of KV cache fits in ~9 GB, expanding the effective context window proportionally on the same hardware.

**Integration points in lmdeploy:**

lmdeploy's TurboMind backend manages KV cache in blocks. The natural integration point is:
1. Post-prefill block compression: after a KV block is filled during prefill, compress it before writing to the persistent cache pool
2. Pre-attention decompression: decompress the block when it is needed for attention computation
3. Cache budget config: expose a kv_compression parameter in TurbomindEngineConfig alongside cache_max_entry_count

The turbomind C++ backend would need compression/decompression kernels (CUDA). A PyTorch backend integration would be faster to prototype.

**Expected impact on the reported session_len truncation issues:**
With 7x KV compression, cache_max_entry_count=0.8 would support 7x more tokens — a model truncating to 42K tokens today could support ~300K tokens on the same hardware.

Is there an existing plugin interface for custom KV backends, or would this require patching the block manager directly? Happy to discuss implementation path and contribute a prototype PR.

Repo and technical details: https://github.com/jagmarques/nexusquant

## 评论 (0)
