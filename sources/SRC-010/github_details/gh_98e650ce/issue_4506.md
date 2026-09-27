# [Issue #4506] Support NexusQuant KV cache compression for memory reduction

source: https://github.com/InternLM/lmdeploy/issues/4506
state: closed | updated: 2026-05-08T21:14:20Z
labels: 

## 正文

KV cache memory is a bottleneck at long context lengths. [NexusQuant](https://github.com/jagmarques/nexusquant) offers training-free 7–10x KV compression via E8 lattice quantization + attention-aware token eviction (up to 17x with token merging).

**Integration points:**
- After prefill, compress the KV cache in-place before storing in the paged block pool
- Use attention mask to exclude evicted tokens during generation
- API: `with nexusquant_evict(model): model.generate(...)`

**Why this matters for lmdeploy:**
lmdeploy's TurboMind engine already supports INT4/INT8 KV quant. NexusQuant's E8 lattice VQ is a natural extension — it achieves higher compression than INT4 while maintaining quality, and is drop-in since it doesn't change tensor shapes (only precision).

**Validated results:**
- Mistral-7B: 7x compression, -2.26% PPL vs baseline
- Llama-3-8B: 5.3x compression, -0.002% PPL
- Training-free, no calibration data required

**Library details:**
- pip-installable: `pip install nexusquant-kv`
- Apache 2.0 licensed
- Paper: https://github.com/jagmarques/nexusquant/blob/main/paper/nexusquant.pdf

Would you be interested in exploring this as a compression backend for TurboMind? Happy to help with the integration and provide benchmarks on your target models.

## 评论 (0)
