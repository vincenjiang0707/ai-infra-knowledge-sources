# [Issue #2635] Training Extremely Slow on Qwen3.5-35B-A3B + 8×B300 (280s/step), py-spy Shows FlashAttention-4 CUTLASS JIT Compilation During Backward

source: https://github.com/Dao-AILab/flash-attention/issues/2635
state: closed | updated: 2026-07-04T13:15:58Z
labels: 

## 正文

Environment
Hardware
1 node
8 × NVIDIA B300 GPUs
Software
Python: 3.12.13
ms-swift (latest)
Megatron backend
FlashAttention installed from source
pip list | grep flash

flash_attn                               2.8.4
flash-attn-4                             4.0.0b17.dev0+gb02b07e.d20260608
flash-linear-attention                   0.5.0
flashinfer-cubin                         0.6.8.post1
flashinfer-python                        0.6.8.post1

Training Command
--model /mnt/wfs2139/model/Qwen3.5-35B-A3B \
--cached_dataset /opt/wfs2139/data/vlm/cache/train \
--use_distributed_optimizer true \
--save_safetensors true \
--load_from_cache_file true \
--tensor_model_parallel_size 1 \
--pipeline_model_parallel_size 1 \
--expert_model_parallel_size 8 \
--freeze_llm false \
--moe_permute_fusion true \
--moe_grouped_gemm true \
--moe_shared_expert_overlap true \
--moe_aux_loss_coeff 1e-6 \
--micro_batch_size 4 \
--global_batch_size 32 \
--recompute_granularity full \
--recompute_method uniform \
--recompute_num_layers 1 \
--num_train_epochs 1 \
--finetune true \
--cross_entropy_loss_fusion true \
--lr 1e-5 \
--lr_warmup_fraction 0.05 \
--min_lr 5e-8 \
--output_dir /mnt/wfs2139/zli/megatron_output/Qwen3.5-35B-A3B-605 \
--eval_steps 500000 \
--save_steps 1500 \
--max_length 32000 \
--dataloader_num_workers 1 \
--dataset_num_proc 32 \
--attention_backend flash \
--no_save_optim true \
--no_save_rng true \
--sequence_parallel true \
--padding_free true \
--packing true \
--dataloader_pin_memory false \
--gradient_accumulation_fusion false

Problem

Training is extremely slow.

Observed throughput
~280 seconds / step

This is much slower than expected for:
Qwen3.5-35B-A3B
EP=8
TP=1
PP=1
8×B300

py-spy Observation

I attached to one training process using:
The main thread is blocked in backward:
custom_backward
 └── backward_step
      └── forward_backward_no_pipelining
           └── train_step
However, one Python thread is actively consuming CPU and holding the GIL.
The stack trace repeatedly enters:
flash_attn/cute/interface.py
    _flash_attn_bwd

cutlass/base_dsl/compiler.py
    _compile

cutlass/base_dsl/dsl.py
    generate_mlir

flash_attn/cute/sm100_hd256_2cta_fmha_backward_dkdvkernel.py



## 评论 (18)

### Johnsonms · 2026-06-09

Thanks for reporting this issue.

Could you please provide a local and simple repro script that can reproduce the problem without the full distributed training setup?

Ideally, the repro should call FlashAttention directly with the same input shapes, dtype, head dim, causal setting, and forward/backward path used in your training run. A small single-node or single-GPU script would make it much easier for us to debug and isolate the issue.

### wangsiyu · 2026-06-09

Thanks for reporting. But CuteDSL JIT will re-compiles when input shapes dynamic. Practically, we should packed sequence input data to have same total length.

### yszhli · 2026-06-09

> Thanks for reporting. But CuteDSL JIT will re-compiles when input shapes dynamic. Practically, we should packed sequence input data to have same total length.

Thanks for the explanation.

Just to confirm, are you suggesting that CuteDSL JIT caches kernels based on the packed sequence total length, and that varying total lengths may trigger recompilation and potentially expose this issue?

In our training setup, we use sequence packing. We only constrain the maximum sequence length to 32,000 as specified in the training script, while the actual packed total length can vary from iteration to iteration.

However, when running the same training data and configuration with FlashAttention-2 on H200 GPUs, we do not observe this issue. This is why we are trying to understand whether the problem is related to CuteDSL JIT recompilation or something else specific to the current backend.


### yszhli · 2026-06-09

> Thanks for reporting this issue.
> 
> Could you please provide a local and simple repro script that can reproduce the problem without the full distributed training setup?
> 
> Ideally, the repro should call FlashAttention directly with the same input shapes, dtype, head dim, causal setting, and forward/backward path used in your training run. A small single-node or single-GPU script would make it much easier for us to debug and isolate the issue.
By the way, when using FlashAttention-2, the training runs stably and achieves about 23 seconds per step under the same configuration.  

### Johnsonms · 2026-06-10


Thanks @yszhli for the detailed py-spy trace — that made this easy to pin down.

**TL;DR:** the kernel is *not* recompiling on every backward. The JIT cache works correctly. What you're hitting is that **the persistent (on-disk) compile cache is disabled by default**, so each of your 8 ranks compiles every kernel from scratch at startup (and re-compiles after any restart), and they contend for CPU while holding the GIL — which is exactly the stack py-spy caught.

### Fix: enable the persistent cache

```bash
export FLASH_ATTENTION_CUTE_DSL_CACHE_ENABLED=1
export FLASH_ATTENTION_CUTE_DSL_CACHE_DIR=/path/on/fast/shared/storage   # optional; lets all ranks + restarts reuse
```

With this on, kernels are compiled once, exported to disk, and loaded (not recompiled) by every subsequent rank/process/run.

### Also: please upgrade from `4.0.0b17`

`4.0.0b17` predates several JIT-cache fixes on main — notably #2402 (compile-cache correctness) and #2298 (broadcast dims added to the cache key). Worth re-testing on current `main`/latest beta.

### Evidence (reproduced on GB300, head_dim=256, varlen)

I simulated padding-free varlen training where the packed length changes every step and counted real `cute.compile` calls:

| condition | result |
|---|---|
| cache **off** (default), shapes varying each step | compiles once at step 0 (~27s), then **0 compiles / ~0.00s per step** |
| cache **on**, warm process (2nd run) | **0 compiles, 0.01s total** — everything loaded from disk |

So within a single warmed process the cost is one-time. The pain you see comes from (a) 8 ranks each paying that one-time cost with no sharing, and (b) nothing surviving restarts — both fixed by the env var above.

One minor note: the compile key intentionally distinguishes "single-tile" (very short, ≤ block-size) sequences from multi-tile ones (a correctness guard against stride specialization), so an unusually short sequence length appearing for the first time will compile one extra variant. In normal training with multi-thousand `max_seqlen` this almost never triggers, so it isn't the main cost here.

If you still see recompilation **after** enabling the persistent cache and upgrading, could you grab a py-spy across a few *steady-state* steps (not the first one) and share whether `FLASH_ATTENTION_CUTE_DSL_CACHE_ENABLED` is actually set in the worker env? That would tell us whether something in your setup (e.g. a per-step-varying attention arg) is churning the cache key.


### yszhli · 2026-06-11

> Thanks [@yszhli](https://github.com/yszhli) for the detailed py-spy trace — that made this easy to pin down.
> 
> **TL;DR:** the kernel is _not_ recompiling on every backward. The JIT cache works correctly. What you're hitting is that **the persistent (on-disk) compile cache is disabled by default**, so each of your 8 ranks compiles every kernel from scratch at startup (and re-compiles after any restart), and they contend for CPU while holding the GIL — which is exactly the stack py-spy caught.
> 
> ### Fix: enable the persistent cache
> export FLASH_ATTENTION_CUTE_DSL_CACHE_ENABLED=1
> export FLASH_ATTENTION_CUTE_DSL_CACHE_DIR=/path/on/fast/shared/storage   # optional; lets all ranks + restarts reuse
> With this on, kernels are compiled once, exported to disk, and loaded (not recompiled) by every subsequent rank/process/run.
> 
> ### Also: please upgrade from `4.0.0b17`
> `4.0.0b17` predates several JIT-cache fixes on main — notably [#2402](https://github.com/Dao-AILab/flash-attention/pull/2402) (compile-cache correctness) and [#2298](https://github.com/Dao-AILab/flash-attention/pull/2298) (broadcast dims added to the cache key). Worth re-testing on current `main`/latest beta.
> 
> ### Evidence (reproduced on GB300, head_dim=256, varlen)
> I simulated padding-free varlen training where the packed length changes every step and counted real `cute.compile` calls:
> 
> condition	result
> cache **off** (default), shapes varying each step	compiles once at step 0 (~27s), then **0 compiles / ~0.00s per step**
> cache **on**, warm process (2nd run)	**0 compiles, 0.01s total** — everything loaded from disk
> So within a single warmed process the cost is one-time. The pain you see comes from (a) 8 ranks each paying that one-time cost with no sharing, and (b) nothing surviving restarts — both fixed by the env var above.
> 
> One minor note: the compile key intentionally distinguishes "single-tile" (very short, ≤ block-size) sequences from multi-tile ones (a correctness guard against stride specialization), so an unusually short sequence length appearing for the first time will compile one extra variant. In normal training with multi-thousand `max_seqlen` this almost never triggers, so it isn't the main cost here.
> 
> If you still see recompilation **after** enabling the persistent cache and upgrading, could you grab a py-spy across a few _steady-state_ steps (not the first one) and share whether `FLASH_ATTENTION_CUTE_DSL_CACHE_ENABLED` is actually set in the worker env? That would tell us whether something in your setup (e.g. a per-step-varying attention arg) is churning the cache key.

Thank you for your reply. However, after upgrading FlashAttention from beta 16 to beta 17, I encountered the following problem.       [rank4]: AssertionError: SM100 forward with head_dim=256 does not support aux_tensors
[rank3]: Traceback (most recent call last):
[rank3]:   File "/usr/local/lib/python3.12/site-packages/swift/cli/_megatron/sft.py", line 7, in <module>
[rank3]:     megatron_sft_main()
[rank3]:   File "/usr/local/lib/python3.12/site-packages/swift/megatron/pipelines/train/sft.py", line 97, in megatron_sft_main
[rank3]:     return MegatronSft(args).main()
[rank3]:            ^^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/swift/pipelines/base.py", line 52, in main
[rank3]:     result = self.run()
[rank3]:              ^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/swift/megatron/pipelines/train/sft.py", line 72, in run
[rank3]:     trainer.train(train_dataset, val_dataset)
[rank3]:   File "/usr/local/lib/python3.12/site-packages/swift/megatron/trainers/base.py", line 632, in train
[rank3]:     metrics, grad_norm, update_successful = self.train_step(train_data_iterator)
[rank3]:                                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/swift/megatron/trainers/base.py", line 875, in train_step
[rank3]:     metrics = forward_backward_func(
[rank3]:               ^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/megatron/core/pipeline_parallel/schedules.py", line 686, in forward_backward_no_pipelining
[rank3]:     output_tensor, num_tokens = forward_step(
[rank3]:                                 ^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/megatron/core/pipeline_parallel/schedules.py", line 428, in forward_step
[rank3]:     output_tensor, loss_func = forward_step_func(data_iterator, model)
[rank3]:                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/swift/megatron/trainers/trainer.py", line 117, in forward_step
[rank3]:     output_tensor = model(**data)
[rank3]:                     ^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1779, in _wrapped_call_impl
[rank3]:     return self._call_impl(*args, **kwargs)
[rank3]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1790, in _call_impl
[rank3]:     return forward_call(*args, **kwargs)
[rank3]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/megatron/core/distributed/data_parallel_base.py", line 22, in forward
[rank3]:     return self.module(*inputs, **kwargs)
[rank3]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1779, in _wrapped_call_impl
[rank3]:     return self._call_impl(*args, **kwargs)
[rank3]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1790, in _call_impl
[rank3]:     return forward_call(*args, **kwargs)
[rank3]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/megatron/core/transformer/module.py", line 493, in forward
[rank3]:     outputs = self.module(*inputs, **kwargs)
[rank3]:               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1779, in _wrapped_call_impl
[rank3]:     return self._call_impl(*args, **kwargs)
[rank3]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1790, in _call_impl
[rank3]:     return forward_call(*args, **kwargs)
[rank3]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/mcore_bridge/model/mm_gpt_model.py", line 95, in forward
[rank3]:     return self.language_model(
[rank3]:            ^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1779, in _wrapped_call_impl
[rank3]:     return self._call_impl(*args, **kwargs)
[rank3]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1790, in _call_impl
[rank3]:     return forward_call(*args, **kwargs)
[rank3]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/mcore_bridge/model/gpt_model.py", line 310, in forward
[rank3]:     decoder_output = self.decoder(
[rank3]:                      ^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/megatron/core/transformer/transformer_block.py", line 643, in __call__
[rank3]:     return super().__call__(*args, **kwargs)
[rank3]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/megatron/core/transformer/module.py", line 356, in __call__
[rank3]:     return super().__call__(*args, **kwargs)
[rank3]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1779, in _wrapped_call_impl
[rank3]:     return self._call_impl(*args, **kwargs)
[rank3]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1790, in _call_impl
[rank3]:     return forward_call(*args, **kwargs)
[rank3]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/mcore_bridge/model/modules/transformer_block.py", line 445, in forward
[rank3]:     hidden_states, context = self._layer_forward(
[rank3]:                              ^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/mcore_bridge/model/modules/transformer_block.py", line 251, in _layer_forward
[rank3]:     return layer(hidden_states=hidden_states, **kwargs)
[rank3]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/megatron/core/transformer/module.py", line 356, in __call__
[rank3]:     return super().__call__(*args, **kwargs)
[rank3]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1779, in _wrapped_call_impl
[rank3]:     return self._call_impl(*args, **kwargs)
[rank3]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1790, in _call_impl
[rank3]:     return forward_call(*args, **kwargs)
[rank3]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/mcore_bridge/model/modules/transformer_layer.py", line 342, in forward
[rank3]:     hidden_states, context = self._forward_attention(*args, **kwargs)
[rank3]:                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/megatron/core/transformer/transformer_layer.py", line 615, in _forward_attention
[rank3]:     attention_output_with_bias = self.self_attention(
[rank3]:                                  ^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1779, in _wrapped_call_impl
[rank3]:     return self._call_impl(*args, **kwargs)
[rank3]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1790, in _call_impl
[rank3]:     return forward_call(*args, **kwargs)
[rank3]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/megatron/core/transformer/attention.py", line 1159, in forward
[rank3]:     core_attn_out = apply_module(self.core_attention)(
[rank3]:                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1779, in _wrapped_call_impl
[rank3]:     return self._call_impl(*args, **kwargs)
[rank3]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1790, in _call_impl
[rank3]:     return forward_call(*args, **kwargs)
[rank3]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/megatron/core/extensions/transformer_engine.py", line 1626, in forward
[rank3]:     core_attn_out = super().forward(query, key, value, attention_mask, **_fa_kwargs)
[rank3]:                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/transformer_engine/pytorch/jit.py", line 67, in wrapper
[rank3]:     return disabled_f(*args, **kwargs)
[rank3]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/torch/_dynamo/external_utils.py", line 227, in nonrecursive_disable_wrapper
[rank3]:     return fn(*args, **kwargs)
[rank3]:            ^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/transformer_engine/pytorch/attention/dot_product_attention/dot_product_attention.py", line 1519, in forward
[rank3]:     return self.flash_attention(
[rank3]:            ^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1779, in _wrapped_call_impl
[rank3]:     return self._call_impl(*args, **kwargs)
[rank3]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1790, in _call_impl
[rank3]:     return forward_call(*args, **kwargs)
[rank3]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/transformer_engine/pytorch/attention/dot_product_attention/backends.py", line 1082, in forward
[rank3]:     output = func(
[rank3]:              ^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/flash_attn/cute/interface.py", line 2317, in flash_attn_varlen_func
[rank3]:     return FlashAttnVarlenFunc.apply(
[rank3]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/torch/autograd/function.py", line 596, in apply
[rank3]:     return super().apply(*args, **kwargs)  # type: ignore[misc]
[rank3]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/flash_attn/cute/interface.py", line 2114, in forward
[rank3]:     out, lse = _flash_attn_fwd(
[rank3]:                ^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/flash_attn/cute/interface.py", line 1025, in _flash_attn_fwd
[rank3]:     _flash_attn_fwd.compile_cache[compile_key] = cute.compile(
[rank3]:                                                  ^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/flash_attn/cute/sm100_hd256_2cta_fmha_forward.py", line 197, in __call__
[rank3]:     assert aux_data.tensors is None, (
[rank3]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank3]:   File "/usr/local/lib/python3.12/site-packages/nvidia_cutlass_dsl/python_packages/cutlass/base_dsl/ast_helpers.py", line 443, in assert_executor
[rank3]:     assert test, msg
[rank3]:            ^^^^
[rank3]: AssertionError: SM100 forward with head_dim=256 does not support aux_tensors

### yszhli · 2026-06-11

By the way, I noticed a significant performance difference when using FA beta4. With CUDA 13, training takes over 200s/step, whereas with CUDA 12, it takes only around 60s/step. I'm not sure whether this is expected or related to a compatibility issue between FA beta4 and CUDA 13.  (using beta16 code to install)



### Johnsonms · 2026-06-11

@yszhli The head_dim=256 does not support aux_tensors error is a real limitation, not a build issue. On Blackwell, head_dim=256 always uses a dedicated FA4 kernel that doesn't yet support aux_tensors / score_mod / learnable_sink / softcap / local attention, and there's no fallback for hd256. The crash means your model is passing a non-None aux_tensors (i.e. a custom score_mod) into flash_attn_varlen_func.

To move forward, could you tell us what attention feature your config enables — an attention sink / gated attention, an explicit bias, or a custom scoring term? Even better, dump the kwargs Transformer-Engine passes into flash_attn_varlen_func (whether aux_tensors / score_mod / learnable_sink are set). That tells us exactly which feature to add to the hd256 kernel.

In the meantime: if that term is optional, disabling it lets the hd256 kernel run; otherwise FA2 (2.8.4) stays the supported backend for hd256.

If you need hd256 to support this feature urgently, please let me know and we can prioritize it.

For CUDA 13 vs 12 (200s vs 60s): that's a separate CUDA-13 packaging regression. Please share your nvidia-cutlass-dsl and CUDA/ptxas versions — for now the CUDA-12 build is the safe choice.

### yszhli · 2026-06-12

> [@yszhli](https://github.com/yszhli) The head_dim=256 does not support aux_tensors error is a real limitation, not a build issue. On Blackwell, head_dim=256 always uses a dedicated FA4 kernel that doesn't yet support aux_tensors / score_mod / learnable_sink / softcap / local attention, and there's no fallback for hd256. The crash means your model is passing a non-None aux_tensors (i.e. a custom score_mod) into flash_attn_varlen_func.
> 
> To move forward, could you tell us what attention feature your config enables — an attention sink / gated attention, an explicit bias, or a custom scoring term? Even better, dump the kwargs Transformer-Engine passes into flash_attn_varlen_func (whether aux_tensors / score_mod / learnable_sink are set). That tells us exactly which feature to add to the hd256 kernel.
> 
> In the meantime: if that term is optional, disabling it lets the hd256 kernel run; otherwise FA2 (2.8.4) stays the supported backend for hd256.
> 
> If you need hd256 to support this feature urgently, please let me know and we can prioritize it.
> 
> For CUDA 13 vs 12 (200s vs 60s): that's a separate CUDA-13 packaging regression. Please share your nvidia-cutlass-dsl and CUDA/ptxas versions — for now the CUDA-12 build is the safe choice.

Thanks for the clarification.

I added logging around flash_attn_varlen_func and confirmed that the model does not pass any special attention features: (usr/local/lib/python3.12/site-packages/flash_attn/cute/interface.py)

* aux_tensors = None
* aux_scalars = None
* score_mod = None
* learnable_sink = None
* softcap = None

The model is Qwen3.5-35B-A3B and does not appear to use attention sink, softcap, local attention, custom score modifications, or explicit attention bias.

However, the failure happens later during the CuteDSL compile path in:

flash_attn/cute/sm100_hd256_2cta_fmha_backward.py

Specifically around:

```python
AuxData(cute_aux_tensors, aux_scalars)
```

The assertion:

```python
assert aux_data.tensors is None or len(aux_data.tensors) == 0
```

is triggered even though aux_tensors is None at the flash_attn_varlen_func level.

After temporarily commenting out the assertion, training runs successfully.

This suggests that some internal cute_aux_tensors may be generated during the compile path even when no aux_tensors are supplied by the model.

Separately, performance is still much slower than FA2:


* FA4 beta17 + CUDA12: ~90s/step （comment on the assert)


I also enabled persistent cache but did not observe a significant improvement.

other env info: Python: 3.12.13
Torch: 2.11.0+cu130
CUDA Runtime: 13.0
GPU: NVIDIA B300 SXM6 AC
Capability: (10, 3)
flash_attn 2.8.3
transformer_engine 2.15.0+cabc6b6b 
cutlass 4.4.2 nvidia-cutlass-dsl=4.4.2  /usr/local/cuda/bin/ptxas --version
ptxas: NVIDIA (R) Ptx optimizing assembler
Copyright (c) 2005-2025 NVIDIA Corporation
Built on Wed_Aug_20_01:55:12_PM_PDT_2025
Cuda compilation tools, release 13.0, V13.0.88
Build cuda_13.0.r13.0/compiler.36424714_0

### Johnsonms · 2026-06-12

Hi @yszhli Could you please help to try this PR with notes in part one and part two in PR description ? 
https://github.com/Dao-AILab/flash-attention/pull/2647

### yszhli · 2026-06-13

> Hi [@yszhli](https://github.com/yszhli) Could you please help to try this PR with notes in part one and part two in PR description ? [#2647](https://github.com/Dao-AILab/flash-attention/pull/2647)

I’ve tested this PR following the notes in parts one and two of the description. The local cache is being hit successfully, but the training speed hasn't improved. Below are the speed logs from my test:    {'loss': 0.47705832, 'grad_norm': 1.23246276, 'learning_rate': 2e-08, 'load_balancing_loss': 1.01558769, 'iteration': '1/10635', 'elapsed_time': '3m 12s', 'remaining_time': '23d 14h 27m 6s', 'memory(GiB)': 204.12, 'train_speed(s/it)': 191.764682}
{'loss': 0.43613276, 'grad_norm': 1.75246286, 'learning_rate': 9e-08, 'load_balancing_loss': 1.04061723, 'iteration': '5/10635', 'elapsed_time': '9m 40s', 'remaining_time': '14d 6h 48m 17s', 'memory(GiB)': 258.51, 'train_speed(s/it)': 116.095699}
{'loss': 0.4270708, 'grad_norm': 1.16587019, 'learning_rate': 1.9e-07, 'load_balancing_loss': 1.04042268, 'iteration': '10/10635', 'elapsed_time': '17m 17s', 'remaining_time': '12d 18h 10m 6s', 'memory(GiB)': 258.57, 'train_speed(s/it)': 103.737077}
{'loss': 0.42510602, 'grad_norm': 0.97488004, 'learning_rate': 2.8e-07, 'load_balancing_loss': 1.03240323, 'iteration': '15/10635', 'elapsed_time': '24m 54s', 'remaining_time': '12d 5h 53m 10s', 'memory(GiB)': 258.57, 'train_speed(s/it)': 99.622367}
{'loss': 0.40979832, 'grad_norm': 0.99568218, 'learning_rate': 3.8e-07, 'load_balancing_loss': 1.0337826, 'iteration': '20/10635', 'elapsed_time': '32m 41s', 'remaining_time': '12d 1h 6m 28s', 'memory(GiB)': 258.57, 'train_speed(s/it)': 98.048812}

### Johnsonms · 2026-06-15

Thanks to @yszhli for the verification. Glad to see the first issue is resolved.

For the remaining issue, could you help narrow it down by removing unrelated code from the PR? If possible, please also provide a minimal repro. With that, I can run local tests and investigate the root cause further.


### yszhli · 2026-06-15

> Thanks to [@yszhli](https://github.com/yszhli) for the verification. Glad to see the first issue is resolved.
> 
> For the remaining issue, could you help narrow it down by removing unrelated code from the PR? If possible, please also provide a minimal repro. With that, I can run local tests and investigate the root cause further.

Thanks for investigating this.

Our training environment is based on the following MS-Swift 4.2.3 container image (any of the mirrors below should work):

* modelscope-registry.cn-hangzhou.cr.aliyuncs.com/modelscope-repo/modelscope:ubuntu22.04-cuda13.0.3-py312-torch2.11.0-vllm0.21.0-modelscope1.36.3-swift4.2.3
* modelscope-registry.cn-beijing.cr.aliyuncs.com/modelscope-repo/modelscope:ubuntu22.04-cuda13.0.3-py312-torch2.11.0-vllm0.21.0-modelscope1.36.3-swift4.2.3
* modelscope-registry.us-west-1.cr.aliyuncs.com/modelscope-repo/modelscope:ubuntu22.04-cuda13.0.3-py312-torch2.11.0-vllm0.21.0-modelscope1.36.3-swift4.2.3

Hardware / software:

* GPU: NVIDIA B300 (8 GPUs)
* Host CUDA version: 13.2
* PyTorch: 2.11.0 (from the container)
* Training framework: MS-Swift 4.2.3 + Megatron
* Model: Qwen3.5-35B-A3B

  * https://huggingface.co/Qwen/Qwen3.5-35B-A3B

FlashAttention 4 was installed from source.

To get FA4 running, we temporarily commented out the aux_data assertion related checks. In our case, aux_data is actually None during the forward/backward execution, but the compile stage appears to assume it is non-null and triggers the assertion.

The training command is:

```bash
export MASTER_PORT=29672
export FLASH_ATTENTION_CUTE_DSL_CACHE_ENABLED=1
export FLASH_ATTENTION_CUTE_DSL_CACHE_DIR=/dev/shm/fa4-cache

PYTORCH_CUDA_ALLOC_CONF='expandable_segments:True' \
USE_MCORE_GDN=1 \
nnodes=1 \
nproc_per_node=8 \
NNODES=$nnodes \
NPROC_PER_NODE=$nproc_per_node \
VIDEO_MIN_TOKEN_NUM=32 \
IMAGE_MAX_TOKEN_NUM=1600 \
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \
megatron sft \
    --model Qwen3.5-35B-A3B \
    --dataset test_data.jsonl \
    --save_safetensors true \
    --load_from_cache_file true \
    --tensor_model_parallel_size 1 \
    --pipeline_model_parallel_size 1 \
    --expert_model_parallel_size 8 \
    --freeze_llm false \
    --moe_permute_fusion true \
    --moe_grouped_gemm true \
    --moe_shared_expert_overlap true \
    --moe_aux_loss_coeff 1e-6 \
    --micro_batch_size 4 \
    --global_batch_size 32 \
    --num_train_epochs 1 \
    --finetune true \
    --cross_entropy_loss_fusion true \
    --lr 1e-5 \
    --lr_warmup_fraction 0.05 \
    --min_lr 5e-8 \
    --output_dir /output \
    --eval_steps 500 \
    --save_steps 500 \
    --max_length 32000 \
    --dataloader_num_workers 1 \
    --dataset_num_proc 32 \
    --attention_backend flash \
    --no_save_optim true \
    --no_save_rng true \
    --sequence_parallel false \
    --padding_free true \
    --packing true \
    --dataloader_pin_memory false \
    --gradient_accumulation_fusion false \
    --expert_tensor_parallel_size 1 \
    --add_non_thinking_prefix true \
    --loss_scale ignore_empty_think \
    --recompute_granularity full \
    --recompute_method uniform \
    --recompute_num_layers 1
```

One observation that may be relevant: we train with packing enabled. The maximum sequence length is fixed at 32000, but the packed total sequence length varies from iteration to iteration.

Please let me know if additional information (logs, stack traces, environment details, or a reduced repro case) would be helpful.


### yuchenwang3 · 2026-06-18

We hit this exact slowdown on a Qwen3.5-35B-A3B (MoE) run — Megatron-LM + TransformerEngine + ms-swift on Blackwell — and the cause is **not** the persistent-cache configuration. It's a non-deterministic JIT compile key in the FA4 backward.

`_flash_attn_bwd` (`flash_attn/cute/interface.py`) puts these two entries in `compile_key`:

```python
(seqlen_q_rounded // m_block_size == 1),
(seqlen_k_rounded // n_block_size == 1),
```

`seqlen_q_rounded`/`seqlen_k_rounded` derive from `max_seqlen_q/k`. When the backward is called via TE/HF varlen, **`max_seqlen` is passed as a 0-dim CUDA tensor**, so each of those entries is a 0-d `torch.Tensor`, not a Python `bool`. Then:

- In-memory cache (`JITCache` is a plain `dict`): a tensor in the key tuple hashes by **object identity**, so the lookup misses on **every** backward → the same kernel is recompiled every microbatch.
- Persistent cache (key hashed via `sha256(pickle.dumps(key))`): a freshly-created tensor pickles to different bytes each call → a **new object file every step**. So enabling the persistent cache doesn't help — the key itself is non-deterministic, which is why warming/caching didn't fix it.

Symptoms line up exactly: GPU ~0% util while a cutlass-DSL compile thread holds the GIL, ~7–8× slower steps. The predicate values are always `False` here and the kernel is identical — it's purely cache invalidation from a tensor in the key.

Same root cause as #2571, and #2507 already proposes the fix (coerce the seqlen-derived key parts to Python scalars). Cross-linking so they can be tracked together.


### yszhli · 2026-06-18

> We hit this exact slowdown on a Qwen3.5-35B-A3B (MoE) run — Megatron-LM + TransformerEngine + ms-swift on Blackwell — and the cause is **not** the persistent-cache configuration. It's a non-deterministic JIT compile key in the FA4 backward.
> 
> `_flash_attn_bwd` (`flash_attn/cute/interface.py`) puts these two entries in `compile_key`:
> 
> (seqlen_q_rounded // m_block_size == 1),
> (seqlen_k_rounded // n_block_size == 1),
> `seqlen_q_rounded`/`seqlen_k_rounded` derive from `max_seqlen_q/k`. When the backward is called via TE/HF varlen, **`max_seqlen` is passed as a 0-dim CUDA tensor**, so each of those entries is a 0-d `torch.Tensor`, not a Python `bool`. Then:
> 
> * In-memory cache (`JITCache` is a plain `dict`): a tensor in the key tuple hashes by **object identity**, so the lookup misses on **every** backward → the same kernel is recompiled every microbatch.
> * Persistent cache (key hashed via `sha256(pickle.dumps(key))`): a freshly-created tensor pickles to different bytes each call → a **new object file every step**. So enabling the persistent cache doesn't help — the key itself is non-deterministic, which is why warming/caching didn't fix it.
> 
> Symptoms line up exactly: GPU ~0% util while a cutlass-DSL compile thread holds the GIL, ~7–8× slower steps. The predicate values are always `False` here and the kernel is identical — it's purely cache invalidation from a tensor in the key.
> 
> Same root cause as [#2571](https://github.com/Dao-AILab/flash-attention/issues/2571), and [#2507](https://github.com/Dao-AILab/flash-attention/pull/2507) already proposes the fix (coerce the seqlen-derived key parts to Python scalars). Cross-linking so they can be tracked together.

I gave this method a try and confirmed that the recompilation churn is gone, with step times settling at ~30s/step. While this is a solid improvement, it's still lagging behind FA2's performance. I suspect there may be additional overhead in the backward pass beyond the compile-key issue. Have you run similar comparisons against FA2 on your side? I'd be curious to see if the gap matches what I'm observing.

### yuchenwang3 · 2026-06-18

Glad it cleared the churn on your end too — same here: we applied the `int()` coercion and the per-step recompile / GPU-at-0%-util symptom went away.

On FA4 vs FA2 steady-state, I don't have a clean number to give you — our earlier FA4/FA2 runs had other variables changing, so I can't isolate the backward gap from them. That said, a residual gap wouldn't be surprising: the FA4 CUTE / cutlass-DSL backward is much newer than FA2's mature hand-tuned CUDA bwd, so a steady-state gap *separate* from the compile-key churn (which #2507 fixes) is plausible. It feels like a distinct issue from this one — probably worth a separate perf issue with an `nsys` / py-spy backward profile so the maintainers can pinpoint it (the varlen/THD bwd path is one likely suspect).


### Johnsonms · 2026-06-21

Good. Thanks @yuchenwang3 @yszhli 

### YunfanZhang42 · 2026-07-04

I got hit with the same problem today and can firm HF transformers would trigger excessive JIT recompilations before applying PR https://github.com/Dao-AILab/flash-attention/pull/2507 . However, even after applying the PR it seems JIT recompilation still happens even on fixed batch size and sequence length - not sure why. 

Also agreeing with @yszhli and @yuchenwang3 that FA4 did not result in improvements in E2E time. FA2 is about as fast as FA4 even without considering JIT recompilation. This is with Qwen3-14B at 6K sequence size per GPU, 8x B200s. 
