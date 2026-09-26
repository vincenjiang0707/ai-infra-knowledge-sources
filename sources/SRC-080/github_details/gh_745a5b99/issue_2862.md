# [Issue #2862] GLM-5.2 (glm_moe_dsa) GPTQ: whole-MoE-layer sequential target OOMs, and sequential_targets=Linear can't fx-trace GlmMoeDsaIndexer (data-dependent control flow)

source: https://github.com/vllm-project/llm-compressor/issues/2862
state: closed | updated: 2026-07-24T15:53:13Z
labels: 

## 正文

### Summary

Quantizing **GLM-5.2** (`GlmMoeDsaForCausalLM`, 753B, 256 routed experts + DeepSeek-style sparse-attention "indexer") with GPTQ via llm-compressor hits two compounding walls that effectively block calibration at non-trivial sequence length:

1. **Default `sequential_targets` (decoder layer) OOMs on the MoE layers.** A GLM MoE decoder layer holds 256 linearized expert MLPs; processing the whole layer as one sequential subgraph on a single offload GPU (267 GB) OOMs once `max_seq_length` is more than a few K (dense prefix layers 0–2 are fine; the first MoE layer is where it dies). This forces finer `sequential_targets`.

2. **`sequential_targets=["Linear"]` then fails fx-tracing the custom indexer:**

```
RuntimeError ... <Autowrapped GlmMoeDsaIndexer ...>
  topk = min(self.index_topk, total_len)        # total_len = index_scores.shape[-1]
  topk_indices = index_scores.topk(topk, dim=-1).indices
torch.fx.proxy.TraceError: symbolically traced variables cannot be used as inputs to control flow
```

`GlmMoeDsaIndexer.forward` uses a **data-dependent `min()` on a symbolic shape** (and a `.topk(topk)`), which torch.fx can't trace. So the finer `sequential_targets` needed to avoid (1) is unavailable because of (2).

Net: on a single-GPU offload setup, GLM-5.2 GPTQ calibration is limited to very short `max_seq_length` (the only regime where the whole-MoE-layer subgraph fits), which is a real problem for long-context models.

### Repro (essentials)

```python
oneshot(
    model=<GLM-5.2 bf16>,                 # GlmMoeDsaForCausalLM, trust_remote_code
    recipe=[GPTQModifier(targets=["Linear"], scheme="W4A16_ASYM", ignore=[...])],
    dataset=<calib>, max_seq_length=8192, # >~4K triggers (1) at default targets
    pipeline="sequential", sequential_offload_device="cuda",
    moe_calibrate_all_experts=False,
)
# default sequential_targets -> CUDA OOM at first MoE layer
# sequential_targets=["Linear"] -> TraceError in GlmMoeDsaIndexer (above)
```

### Ask

Could `glm_moe_dsa` get a **traceable model definition** (like the existing
`examples/.../tracing` support for other archs), or guidance on the recommended
`sequential_targets` for GLM MoE? Specifically, making `GlmMoeDsaIndexer` fx-traceable
(e.g. wrapping the `min`/`topk` control flow, or marking the indexer as a leaf/untraced
module for the sequential pipeline) would unblock finer-grained partitioning and thus
long-context calibration of GLM-4.6/4.7/5.x.

### Environment
- llm-compressor 0.12.0, compressed-tensors 0.17.1, transformers 5.10.1, torch 2.12.0, CUDA 12.8
- 8×B300 (267 GB) / 2 TB RAM; model bf16 (~1.5 TB)
- Workaround in use: default `sequential_targets` + short `max_seq_length` (≈2–4K), which traces and fits but caps calibration context.

Happy to help test a traceable definition or contribute one for `glm_moe_dsa` if useful.


## 评论 (3)

### jayakumarpujar · 2026-06-27

Hi @HDCharles, @kylesayrs  and team!!

**Root cause & proposed fix**

The failure is a gap between two extremes of `sequential_targets`:

- **Default (whole decoder layer)** - each `GlmMoeDsaDecoderLayer` is one subgraph holding the entire MoE (128+ experts). GPTQ accumulates a Hessian per target `Linear` concurrently within a subgraph - OOM.
- **`["Linear"]`** - forces the tracer *into* `GlmMoeDsaAttention`, whose `GlmMoeDsaIndexer` has data-dependent control flow (`topk = min(self.index_topk, total_len)`, `.topk(...)` on a runtime shape) - torch.fx trace fails.

The sequential tracer treats `sequential_targets` as **leaf modules** (`SequentialTracer.is_leaf_module`) - it never traces *into* them, only into their ancesstors. So the fix is to pick boundaries that (a) keep the indexer inside a leaf and (b) split experts:

```python
sequential_targets=["GlmMoeDsaAttention", "re:.*\.mlp\.experts\.\d+$"]
```

- `GlmMoeDsaAttention` as a leaf - `GlmMoeDsaIndexer` is never traced - fixes the fx-trace failure.
- Per-expert boundary - only one expert's Hessian resident at a time - fixes the OOM. The linearizer turns the fused `GlmMoeDsaNaiveMoe` into a `LinearExperts2D` whose forward is a **static** `for ... range(num_experts)` loop, so each expert unrolls into its own subgraph cleanly.

This mirrors the existing DeepSeek-V3 pattern (`["DeepseekV3Attention", "DeepseekV3MLP"]`).

Proposed PR:
1. `examples/quantizing_moe/glm5_gptq_example.py` demonstrating the above.
2. Improve the `handle_sequential_oom` message (it currently only suggests `'Linear'`, which is exactly what breaks tracing on DSA/indexer models) to also recommend the attention + per-expert split.
3. A small regression test tracing a tiny `GlmMoeDsaConfig`.

Happy to take this on - could you assign it to me?


### kylesayrs · 2026-07-02

Hey all @pasta-paul @jayakumarpujar, thanks for the great analysis! I'll add a few other caveats and useful information:

1. There is currently a memory leak in observers fixed by https://github.com/vllm-project/llm-compressor/pull/2865 which causes memory to accumulate after each layer. I'm working to get this PR in ASAP, but you may need to rebase on it
2. [In my experiments](https://github.com/vllm-project/llm-compressor/pull/2869/changes#diff-b32039d9d0fea67dbc3a2963b9acc7433530b5d1da77b202f566c4f5b670bcfa) I've been using the below config

```python
oneshot(
    model=model,
    dataset=ds,
    batch_size=4,
    recipe=recipe,
    sequential_targets=["GlmMoeDsaAttention", "ExpertMLP"],
    sequential_targets_per_subgraph=(384 // 4 + 10),
)
```

Using the `sequential_targets_per_subgraph` argument can help reduce memory usage while keeping runtime at a manageable level

### kylesayrs · 2026-07-02

@jayakumarpujar I'll assign this ticket to you while I try to get https://github.com/vllm-project/llm-compressor/pull/2865 in. Feel free to experiment with https://huggingface.co/inference-optimization/GLM-5.2-0.8B-A0.8B and make sure the GPU memory usage is what you would expect.
