# [Issue #3059] [BUG] kernel issue for moe model

source: https://github.com/ModelCloud/GPTQModel/issues/3059
state: closed | updated: 2026-09-07T08:13:33Z
labels: bug

## 正文

I’m not sure whether this is actually a GPTQModel issue or an AutoRound issue. Since you’re more familiar with the kernel side, I thought you might be able to help root-cause the issue more quickly.

~~~bash

(autoround) wenhuach@mlp-dgx-01:~/auto-round$ CUDA_VISIBLE_DEVICES=3 python3 -m auto_round /data2/wenhuach/chunk_acc_1/W4A16/baseline_1gpu/Qwen3.6-35B-A3B-w4g128/  --tasks piqa --eval
W0907 09:14:01.902000 1526979 site-packages/torch/utils/_pytree.py:630] <enum 'KernelPreference'> is an Enum subclass and is now natively supported by torch.compile as an opaque value type. Calling register_constant() on Enum subclasses is deprecated and will be an e
rror in a future release.
W0907 09:14:01.932000 1526979 site-packages/torch/utils/_pytree.py:630] <enum 'ScaleCalculationMode'> is an Enum subclass and is now natively supported by torch.compile as an opaque value type. Calling register_constant() on Enum subclasses is deprecated and will be
an error in a future release.
2026-09-07 09:14:03 WARNING eval_cli.py L248: Batch size 'auto' is not yet supported for hf-multimodal models, reset to 16
/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/transformers/quantizers/auto.py:271: UserWarning: You passed `quantization_config` or equivalent parameters to `from_pretrained` but the model you're loading already has a `quantization_config` att
ribute. The `quantization_config` from the model will be used.However, loading attributes (e.g. ['backend']) will be overwritten with the one you passed to `from_pretrained`. The rest will be ignored.
  warnings.warn(warning_msg)
2026-09-07 09:14:09 INFO device.py L1527: Before applying custom replacements 'peak_ram': 1.21GB
2026-09-07 09:14:11 INFO moe_experts_interface.py L784: [MoE Prep] Unfused 40 MOE experts modules
2026-09-07 09:14:13 INFO device.py L1527: After applying custom replacements 'peak_ram': 1.37GB
2026-09-07 09:14:13 INFO replace_modules.py L101: Prepared 40 MOE modules for quantization
2026-09-07 09:14:13 INFO replace_modules.py L160: Experts (before replacement) [model.language_model.layers.0.mlp.experts] (Qwen3_5MoeExperts):
Qwen3_5MoeExperts(
  (act_fn): SiLUActivation()
)
2026-09-07 09:14:13 INFO replace_modules.py L161: Experts (after replacement) [model.language_model.layers.0.mlp.experts] (Qwen3_5MoeExperts):
Qwen3_5MoeExperts(
  (act_fn): SiLUActivation()
  (0-255): 256 x _ExpertContainer(
    (down_proj): Linear(in_features=512, out_features=2048, bias=False)
    (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
    (up_proj): Linear(in_features=2048, out_features=512, bias=False)
  )
)

◼ Python GIL is enabled: Multi-gpu quant acceleration for MoE models is sub-optimal and multi-core accelerated cpu packing is also disabled. We recommend Python >= 3.13.3t with Pytorch > 2.8 for mult-gpu quantization and multi-cpu packing with env `PYTHON_GIL=0`.
◼ ENV: Auto setting PYTORCH_ALLOC_CONF='expandable_segments:True,max_split_size_mb:256,garbage_collection_threshold:0.7' for memory saving.
◼ ENV: Auto setting CUDA_DEVICE_ORDER=PCI_BUS_ID for correctness.
fatal: not a git repository (or any of the parent directories): .git
◼

┌─────────────┐    ┌────────────────────────┐    ┌────────────┐    ┌─────────┐
│ GPT-QModel  │ -> │ ▓▓▓▓▓▓▓▓▓▓▓▓ 16bit     │ -> │ ▒▒▒▒ 8bit  │ -> │ ░░ 4bit │
└─────────────┘    └────────────────────────┘    └────────────┘    └─────────┘
GPT-QModel   : 7.3.6
Transformers : 5.14.1
Torch        : 2.14.0+cu130
Triton       : 3.8.0
2026-09-07 09:14:32 INFO convert_model.py L910: Inference backend selection: requested=auto, packing_format=auto_round:auto_gptq, selected=gptqmodel:marlin_zp, gptqmodel:exllamav2
Loading weights: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 93726/93726 [00:46<00:00, 2032.51it/s]
[transformers] Qwen3_5MoeForConditionalGeneration LOAD REPORT from: /data2/wenhuach/chunk_acc_1/W4A16/baseline_1gpu/Qwen3.6-35B-A3B-w4g128/
Key                                                              | Status  | Details
-----------------------------------------------------------------+---------+--------
model.language_model.layers.{0...38}.linear_attn.in_proj_b.g_idx | MISSING |
model.language_model.layers.{0...38}.linear_attn.in_proj_a.g_idx | MISSING |

Notes:
- MISSING:      those params were newly initialized because missing from the checkpoint. Consider training on your downstream task.
◼ gc.collect() reclaimed 0 objects in 1.272s
INFO:httpx:HTTP Request: HEAD https://huggingface.co/datasets/baber/piqa/resolve/main/README.md "HTTP/1.1 404 Not Found"
INFO:httpx:HTTP Request: GET https://huggingface.co/api/datasets/baber/piqa "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: HEAD https://huggingface.co/datasets/baber/piqa/resolve/142f6d7367fd9877f0fb3b5734ea6a545f54cdd1/piqa.py "HTTP/1.1 404 Not Found"
INFO:httpx:HTTP Request: HEAD https://s3.amazonaws.com/datasets.huggingface.co/datasets/datasets/baber/piqa/baber/piqa.py "HTTP/1.1 404 Not Found"
INFO:httpx:HTTP Request: HEAD https://huggingface.co/datasets/baber/piqa/resolve/142f6d7367fd9877f0fb3b5734ea6a545f54cdd1/README.md "HTTP/1.1 404 Not Found"
INFO:httpx:HTTP Request: GET https://huggingface.co/api/datasets/baber/piqa/revision/142f6d7367fd9877f0fb3b5734ea6a545f54cdd1 "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: HEAD https://huggingface.co/datasets/baber/piqa/resolve/142f6d7367fd9877f0fb3b5734ea6a545f54cdd1/.huggingface.yaml "HTTP/1.1 404 Not Found"
INFO:httpx:HTTP Request: GET https://datasets-server.huggingface.co/info?dataset=baber/piqa "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: GET https://huggingface.co/api/datasets/baber/piqa/tree/142f6d7367fd9877f0fb3b5734ea6a545f54cdd1/data?recursive=true&expand=false "HTTP/1.1 404 Not Found"
INFO:httpx:HTTP Request: GET https://huggingface.co/api/datasets/baber/piqa/tree/142f6d7367fd9877f0fb3b5734ea6a545f54cdd1?recursive=false&expand=false "HTTP/1.1 200 OK"
INFO:httpx:HTTP Request: HEAD https://huggingface.co/datasets/baber/piqa/resolve/142f6d7367fd9877f0fb3b5734ea6a545f54cdd1/dataset_infos.json "HTTP/1.1 404 Not Found"
INFO:lm_eval.evaluator_utils:Selected tasks:
INFO:lm_eval.evaluator_utils:Task: piqa (piqa/piqa.yaml)
INFO:lm_eval.api.task:Building contexts for piqa on rank 0...
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1838/1838 [00:01<00:00, 1050.96it/s]
INFO:lm_eval.evaluator:Running loglikelihood requests
Tokenizing inputs: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 3676/3676 [00:00<00:00, 6133.31it/s]
◼ Marlin bf16: compiling torch.ops JIT extension in `/home/wenhuach/.cache/gptqmodel/torch_extensions/marlin_bf16/2923b73ba000d474`.
◼ Marlin bf16: torch.ops JIT extension ready in 96s (estimated ~121s, -24s).
Traceback (most recent call last):
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/home/wenhuach/auto-round/auto_round/__main__.py", line 20, in <module>
    run()
    ~~~^^
  File "/home/wenhuach/auto-round/auto_round/cli/main.py", line 517, in run
    run_eval(command_argv)
    ~~~~~~~~^^^^^^^^^^^^^^
  File "/home/wenhuach/auto-round/auto_round/cli/main.py", line 468, in run_eval
    eval(args)
    ~~~~^^^^^^
  File "/home/wenhuach/auto-round/auto_round/eval/eval_cli.py", line 251, in eval
    res = simple_evaluate(
        model="hf" if not args.mllm else "hf-multimodal",
    ...<7 lines>...
        fewshot_as_multiturn=getattr(args, "fewshot_as_multiturn", False),
    )
  File "/home/wenhuach/auto-round/auto_round/eval/evaluation.py", line 110, in simple_evaluate
    return lm_eval.simple_evaluate(
           ~~~~~~~~~~~~~~~~~~~~~~~^
        model=model,
        ^^^^^^^^^^^^
    ...<5 lines>...
        **kwargs,
        ^^^^^^^^^
    )
    ^
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/lm_eval/utils.py", line 575, in _wrapper
    return fn(*args, **kwargs)
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/lm_eval/evaluator.py", line 358, in simple_evaluate
    results = evaluate(
        lm=lm,
    ...<12 lines>...
        confirm_run_unsafe_code=confirm_run_unsafe_code,
    )
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/lm_eval/utils.py", line 575, in _wrapper
    return fn(*args, **kwargs)
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/lm_eval/evaluator.py", line 596, in evaluate
    resps = getattr(lm, reqtype)(cloned_reqs)
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/lm_eval/models/hf_vlms.py", line 408, in loglikelihood
    return super().loglikelihood(requests=requests, disable_tqdm=disable_tqdm)
           ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/lm_eval/models/huggingface.py", line 1227, in loglikelihood
    return super().loglikelihood(requests, disable_tqdm=disable_tqdm)
           ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/lm_eval/api/model.py", line 446, in loglikelihood
    return self._loglikelihood_tokens(new_reqs, disable_tqdm=disable_tqdm)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/lm_eval/models/huggingface.py", line 1507, in _loglikelihood_tokens
    self._model_call(batched_inps, **call_kwargs),
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/lm_eval/models/huggingface.py", line 1154, in _model_call
    return self.model(inps).logits
           ~~~~~~~~~~^^^^^^
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/torch/nn/modules/module.py", line 1783, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/torch/nn/modules/module.py", line 1794, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/transformers/utils/generic.py", line 911, in wrapper
    output = func(self, *args, **kwargs)
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/transformers/models/qwen3_5_moe/modeling_qwen3_5_moe.py", line 2001, in forward
    outputs = self.model(
        input_ids=input_ids,
    ...<9 lines>...
        **kwargs,
    )
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/torch/nn/modules/module.py", line 1783, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/torch/nn/modules/module.py", line 1794, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/transformers/utils/generic.py", line 911, in wrapper
    output = func(self, *args, **kwargs)
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/transformers/models/qwen3_5_moe/modeling_qwen3_5_moe.py", line 1690, in forward
    outputs = self.language_model(
        input_ids=None,
    ...<4 lines>...
        **kwargs,
    )
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/torch/nn/modules/module.py", line 1783, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/torch/nn/modules/module.py", line 1794, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/transformers/utils/generic.py", line 1040, in wrapper
    output = func(self, *args, **kwargs)
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/transformers/utils/output_capturing.py", line 262, in wrapper
    outputs = func(self, *args, **kwargs)
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/transformers/models/qwen3_5_moe/modeling_qwen3_5_moe.py", line 1316, in forward
    hidden_states = decoder_layer(
        hidden_states,
    ...<5 lines>...
        **kwargs,
    )
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/transformers/modeling_layers.py", line 110, in __call__
    return super().__call__(*args, **kwargs)
           ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/torch/nn/modules/module.py", line 1783, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/torch/nn/modules/module.py", line 1794, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/transformers/models/qwen3_5_moe/modeling_qwen3_5_moe.py", line 868, in forward
    hidden_states = self.linear_attn(
        hidden_states=hidden_states,
    ...<2 lines>...
        **kwargs,
    )
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/torch/nn/modules/module.py", line 1783, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/torch/nn/modules/module.py", line 1794, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/transformers/integrations/accelerate.py", line 941, in wrapped
    output = forward_func(self, *args, **kwargs)
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/transformers/models/qwen3_5_moe/modeling_qwen3_5_moe.py", line 536, in forward
    core_attn_out, last_recurrent_state = self.chunk_gated_delta_rule(
                                          ~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        query,
        ^^^^^^
    ...<8 lines>...
        cu_seqlens=kwargs.get("cu_seq_lens_q"),
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/torch/_dynamo/eval_frame.py", line 1548, in _fn
    return fn(*args, **kwargs)
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/fla/ops/backends/__init__.py", line 214, in wrapper
    return func(*args, **kwargs)
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/torch/_dynamo/eval_frame.py", line 1548, in _fn
    return fn(*args, **kwargs)
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/fla/ops/gated_delta_rule/chunk.py", line 567, in chunk_gated_delta_rule
    o, final_state = ChunkGatedDeltaRuleFunction.apply(
                     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        q,
        ^^
    ...<17 lines>...
        chunk_size,
        ^^^^^^^^^^^
    )
    ^
 File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/torch/_dynamo/eval_frame.py", line 1548, in _fn
    return fn(*args, **kwargs)
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/fla/ops/gated_delta_rule/chunk.py", line 567, in chunk_gated_delta_rule
    o, final_state = ChunkGatedDeltaRuleFunction.apply(
                     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        q,
        ^^
    ...<17 lines>...
        chunk_size,
        ^^^^^^^^^^^
    )
    ^
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/fla/utils/_decorators.py", line 152, in wrapper
    return fn(*processed_args, **processed_kwargs)
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/torch/amp/autocast_mode.py", line 481, in decorate_fwd
    return fwd(*args, **kwargs)  # pyrefly: ignore [not-callable]
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/fla/ops/gated_delta_rule/chunk.py", line 282, in forward
    q, q_rstd = l2norm_fwd(q)
                ~~~~~~~~~~^^^
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/torch/_dynamo/eval_frame.py", line 1548, in _fn
    return fn(*args, **kwargs)
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/fla/ops/backends/__init__.py", line 214, in wrapper
    return func(*args, **kwargs)
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/fla/modules/l2norm.py", line 178, in l2norm_fwd
    l2norm_fwd_kernel[grid](
    ~~~~~~~~~~~~~~~~~~~~~~~^
        x=x,
        ^^^^
    ...<6 lines>...
        NB=NB,
        ^^^^^^
    )
    ^
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/triton/runtime/jit.py", line 374, in <lambda>
    return lambda *args, **kwargs: self.run(grid=grid, warmup=False, *args, **kwargs)
                                   ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/fla/ops/utils/cache.py", line 378, in run
    return super().run(*args, **kwargs)
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/gptqmodel/utils/nogil_patcher.py", line 248, in patched_run
    config, used_cached_result, bench_time = _get_config_for_key(self, key, args, kwargs)
                                             ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/wenhuach/miniforge3/envs/autoround/lib/python3.13/site-packages/gptqmodel/utils/nogil_patcher.py", line 173, in _get_config_for_key
    with self._cache_lock:
         ^^^^^^^^^^^^^^^^
AttributeError: 'CachedAutotuner' object has no attribute '_cache_lock'
Running loglikelihood requests:   0%|                                                                                                      
~~~

## 评论 (5)

### wenhuach21 · 2026-09-07

opt-125m is fine, uninstalling flash_attention still have this issue

### ZX-ModelCloud · 2026-09-07

Thanks for the report. Could you share a minimal reproduction script? It would help us reproduce and fix the issue faster.

### Qubitium · 2026-09-07

This looks like my Triton autotune thread fix catching a corner case

### Qubitium · 2026-09-07

@wenhuach21  FLA creates Triton Autotuner instances before GPTQModel applies its monkeypatch. The later class-level patch changes their methods, but those existing instances never ran the patched constructor that initializes the cache/lock state, causing the crash. Oh man, this was bad. The PR should fix it. 

### wenhuach21 · 2026-09-07

> [@wenhuach21](https://github.com/wenhuach21) FLA creates Triton Autotuner instances before GPTQModel applies its monkeypatch. The later class-level patch changes their methods, but those existing instances never ran the patched constructor that initializes the cache/lock state, causing the crash. Oh man, this was bad. The PR should fix it.

Thanks for the quick response and detailed explanation! Glad to hear that it has already been fixed.

