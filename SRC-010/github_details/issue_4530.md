# [Issue #4530] [Feature] support DFlash: Block Diffusion for Flash Speculative Decoding

source: https://github.com/InternLM/lmdeploy/issues/4530
state: open | updated: 2026-09-01T03:13:39Z
labels: planned feature

## 正文

### Motivation

https://github.com/z-lab/dflash

DFlash is a lightweight block diffusion model
You can give qwen3.5 27Bvllm sglang mlx already support model modification.

The following is from the publicity introduction：


🚀 Core Breakthrough
DFlash is a lightweight Block Diffusion Model purpose-built for speculative decoding. It predicts an entire token block in a single forward pass, delivering unprecedented inference acceleration.
 
Limitations of Traditional Methods
 
Conventional speculative decoding approaches (e.g., EAGLE-3) still generate drafts in an autoregressive manner, where each token must wait for the completion of the previous one. This caps the practical speedup at only 2–3×.
 
DFlash Innovations
 
DFlash adopts a fundamentally different strategy:
 
- Parallel Draft Generation: Generates a full token block in one forward pass
- KV Injection Mechanism: Injects hidden layer features from the target model as contextual conditions into every layer of the draft model
- Feature Fusion: Fuses multi-layer hidden states via FC + RMSNorm to provide highly consistent contextual information
 
📊 Remarkable Acceleration Results
 
Qwen3-8B: 6× Lossless Acceleration
 
On the Qwen3-8B model, DFlash achieves:
 
- 6× lossless speedup
- 2.5× faster than EAGLE-3
- Acceptance rate as high as 89%+
 
Qwen3.5-9B: 4.1× Acceleration
 
On Apple Silicon platforms, the Qwen3.5-9B model delivers:
 
- 4.1× speedup
- Validates 16 tokens generated in a single batch
- Optimized with custom Metal kernels
 
🔥 Qwen3.5-27B: 5× Inference Speed Surge
 
Performance Comparison (Configuration)
 
Setup 1024 tokens 2048 tokens Speedup 
Baseline 14 tok/s 11 tok/s 1× 
8-bit Quantization 35 tok/s 26 tok/s 2.5× 
4-bit Quantization 28 tok/s 20 tok/s 2.0× 
 
Key Findings
 
1. 8-bit quantization outperforms 4-bit: Delivers superior speedup while maintaining higher precision
2. Strong long-sequence performance: Retains 2.3× speedup when generating 2048 tokens
3. Lossless decoding: Fully preserves model output quality with zero accuracy degradation

### Related resources

https://github.com/z-lab/dflash

### Additional context

<img width="812" height="906" alt="Image" src="https://github.com/user-attachments/assets/71ac3e69-8371-44e7-9462-b28856c309a1" />

<img width="773" height="679" alt="Image" src="https://github.com/user-attachments/assets/cabacde1-3747-4cfa-867e-d893b6e82b82" />

## 评论 (3)

### lvhan028 · 2026-04-18

Thank you for your suggestion and for bringing dflash to our attention! We really appreciate your recommendation. This is an interesting technology, and we will conduct a thorough investigation and evaluation of it. Thanks again for your valuable input!

### harshal-96 · 2026-09-01

Hi @lvhan028 , I'd like to work on this. I have a working implementation of DFlash support for the PyTorch engine, verified end-to-end, and wanted to check the design direction with you before opening a draft PR.

**Measured results** (RTX 4070 Laptop 8 GB, WSL2, target `thewimo/Qwen3-4B-AWQ`, draft `z-lab/Qwen3-4B-DFlash-b16`, greedy, 256 new tokens, batch 1, eager mode):

| Prompt | baseline | dflash | speedup |
|---|---|---|---|
| gsm8k-style math | 25.1 tok/s | 99.0 tok/s | **3.9x** |
| code generation | 26.1 tok/s | 79.6 tok/s | **3.0x** |

Outputs are character-identical to non-speculative decoding (lossless); mean acceptance 5.48 of 15 drafts per block (6.48 tokens per engine step), matching the paper. The draft module is numerically parity-tested against the reference implementation (cosine 0.9997 on identical weights/inputs).

**What the branch contains** ([harshal-96/lmdeploy `feat/dflash-spec-decode`](https://github.com/harshal-96/lmdeploy/tree/feat/dflash-spec-decode)):

- `DFlashDraftModel` runtime module for Qwen3 targets: non-causal block drafting over `[ctx features | noise block]`, target-feature fusion (`fc` + `hidden_norm` over 5 aux layers), reusing the target's embedding and lm_head matching the reference implementation in https://github.com/z-lab/dflash
- A `DFlashProposer` registered as spec method `dflash`. Key difference vs EAGLE-3/MTP: the whole block is drafted in ONE forward, so I added a proposer-driven `num_draft_forwards` that skips the ar_spec drafting loop (default keeps existing behavior for all current proposers).
- Target-side `aux_hidden_state_layers` capture for Qwen3 (same mechanism llama.py uses for eagle3). Note DFlash `target_layer_ids` use the HF convention (output of layer *l*), so the capture set is shifted by one.
- Weight loading verified 1:1 against `z-lab/Qwen3-4B-DFlash-b16` (58/58 tensors).

**Design questions before I harden it:**

1. Ctx-feature cache: DFlash needs fused target features for every accepted position on the draft side. Would you prefer these paged in the existing draft `CacheEngine`, or a dedicated cache abstraction for block-spec methods?
2. The draft never uses a conventional KV cache OK to add `dflash` to the `no_caches` list and guard `spec_agent._forward_impl` for `cache_engine=None`?
3. `num_speculative_tokens` should be forced to the checkpoint's `block_size - 1` best place to plumb that is probably `SpecDecodeConfig.from_config` before cache/cudagraph strategies are built. Agree?
4. Scope for a first PR: PyTorch engine, Qwen3 targets, eager mode, batch=1 → then batching + CUDA-graph capture as follow-ups. vLLM and SGLang implementations can serve as references for the varlen bidirectional attention.

If this direction works for you I'll open a draft PR and iterate there.


### RunningLeon · 2026-09-01

@harshal-96 Hi, thanks for your attention to this issue. This pr https://github.com/InternLM/lmdeploy/pull/4789 is for dflash + qwen3.5. If possible, you can review and leave your comments on the pr. Besides, welcome to PR your implementation for qwen3 model.
