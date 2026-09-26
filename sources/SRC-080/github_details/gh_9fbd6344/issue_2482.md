# [Issue #2482] [Puzzletron] KV-cache memory computes head size as n_embd // n_head instead of reading head_dim

source: https://github.com/NVIDIA/Model-Optimizer/issues/2482
state: open | updated: 2026-09-21T22:34:31Z
labels: bug

## 正文

## Describe the bug
 
Impact: should have. No error is raised, but the memory objective is wrong for a number of models.
 
`calculate_kv_dim` in `modelopt/torch/puzzletron/utils/misc.py` computes
 
```python
head_size = n_embd // n_head
kv_dim = 2 * num_kv_heads * head_size
```
 
and does not read `head_dim` from the model config. `calculate_attention_memory` uses it for the KV cache, and on `feature/puzzletron_v2` so does `calculate_additive_metrics` for `kv_cache_bytes_per_token`. For models in which `head_dim != hidden_size / num_attention_heads`, the KV cache of every attention layer is therefore mispriced, in either direction. Two of the shipped example configs are affected:
 
| config | `head_dim` | `n_embd // n_head` | KV cache estimate |
|---|---|---|---|
| `mistral-small-24b-instruct-2501_pruneffn_memory` | 128 | 5120 // 32 = 160 | 25% too high |
| `gptoss-20b_remove_experts_memory` | 64 | 2880 // 64 = 45 | 30% too low |
 
The Llama-3.x, Qwen2.5-7B and Qwen3-8B configs are not affected, given that their `head_dim` equals `hidden_size / num_attention_heads`. Models outside the shipped examples are affected as well, e.g. Gemma-3-12B (256 against 240).
 
For Mistral-Small-24B the overestimate makes attention subblocks look more expensive than they are, so under a `target_memory` constraint with attention in the search space the solver is biased towards removing attention.
 
### Steps/Code to reproduce bug
 
No run is needed. The following uses the dimensions from the models' `config.json`:
 
```python
from modelopt.torch.puzzletron.utils.misc import calculate_kv_dim
 
# (name, hidden_size, num_attention_heads, num_key_value_heads, head_dim)
for name, hidden, heads, kv_heads, head_dim in [
    ("Mistral-Small-24B-Instruct-2501", 5120, 32, 8, 128),
    ("gpt-oss-20b", 2880, 64, 8, 64),
]:
    print(name, calculate_kv_dim(kv_heads, heads, hidden), 2 * kv_heads * head_dim)
 
# Mistral-Small-24B-Instruct-2501 2560 2048
# gpt-oss-20b 720 1024
```
 
### Expected behavior
 
`kv_dim` should be `2 * num_kv_heads * head_dim`, using the model's `head_dim`. On `feature/puzzletron_v2`, the FLOP estimate in `calculate_additive_metrics` already resolves the head dimension as
 
```python
head_dim = int(subblock_config.qk_head_dim or (n_embd // n_head))
```
 
The KV path could use the same resolution, i.e. `qk_head_dim` if set, then the language-model config's `head_dim`, then `n_embd // n_head` as a fallback, for example by passing the resolved head dimension to `calculate_kv_dim` instead of `n_embd` and `n_head`.
 
### Who can help?
 
-
## System information
 
- Container used (if applicable): nvcr.io/nvidia/nemo:26.02, with ModelOpt 0.45.0 installed from source on top
- OS (e.g., Ubuntu 22.04, CentOS 7, Windows 10): Ubuntu (AWS)
- CPU architecture (x86_64, aarch64): x86_64
- GPU name (e.g. H100, A100, L40S): NVIDIA RTX PRO 6000 Blackwell Server Edition (driver 595.71.05)
- GPU memory size: 96 GB
- Number of GPUs: 1
- Library versions (if applicable):
  - Python: 3.12
  - ModelOpt version or commit hash: 0.45.0; also checked by reading the current `feature/puzzletron_v2` branch
  - CUDA: 13.0
  - PyTorch: 2.10.0a0+b558c986e8.nv25.11
  - Transformers: 4.57.6
  - TensorRT-LLM: N/A
  - ONNXRuntime: N/A
  - TensorRT: 10.14.1.48 (not used by Puzzletron)
- Any other details that may help: The bug is in a closed-form calculation and does not depend on the hardware or runtime environment.

## 评论 (1)

### musi22 · 2026-09-20

Hi @soksof and maintainers,

I have submitted a tested fix for this issue in PR #2484:
https://github.com/NVIDIA/Model-Optimizer/pull/2484

It updates calculate_kv_dim to respect explicit head_dim (with fallback to n_embd // n_head), wires it into the subblock stats calculations, and includes unit tests for Mistral Small 24B, gpt-oss 20B, and precedence resolution.
