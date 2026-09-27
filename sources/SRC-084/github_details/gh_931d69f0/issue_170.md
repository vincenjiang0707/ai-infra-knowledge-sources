# [Issue #170] lm_eval | RuntimeError: expected mat1 and mat2 to have the same dtype,

source: https://github.com/dropbox/hqq/issues/170
state: closed | updated: 2026-07-20T09:42:49Z
labels: 

## 正文

Hi. I'm trying to evaluate an HQQ quantized model using `lm_eval` using the following command:

```
lm_eval --model hf --model_args pretrained={dir_path},dtype=half,device_map=auto --tasks {tasks} --batch_size auto:8 --apply_chat_template True --num_fewshot 5 --output_path {dir_path}/lm_eval --gen_kwargs do_sample=True,temperature=0.6,max_gen_toks=16000
```

I get the following error. Any ideas? I tried to play with `dtype` when running the `lm_eval`, but nothing worked.

```
Running command: lm_eval --model hf --model_args pretrained=/home/uygar/q_experiments/models/quantized_models/Phi-4-reasoning-hqq-b1-g64,dtype=half,device_map=auto --tasks mmlu --batch_size auto:8 --apply_chat_template True --num_fewshot 5 --output_path /home/uygar/q_experiments/models/quantized_models/Phi-4-reasoning-hqq-b1-g64/lm_eval --gen_kwargs do_sample=True,temperature=0.6,max_gen_toks=16000
2025-11-17:21:43:36 INFO     [__main__:446] Selected Tasks: ['mmlu']
2025-11-17:21:43:36 INFO     [evaluator:202] Setting random seed to 0 | Setting numpy seed to 1234 | Setting torch manual seed to 1234 | Setting fewshot manual seed to 1234
2025-11-17:21:43:36 WARNING  [evaluator:214] generation_kwargs: {'do_sample': True, 'temperature': 0.6, 'max_gen_toks': 16000} specified through cli, these settings will update set parameters in yaml tasks. Ensure 'do_sample=True' for non-greedy decoding!
2025-11-17:21:43:36 INFO     [evaluator:240] Initializing hf model, with arguments: {'pretrained': '/home/uygar/q_experiments/models/quantized_models/Phi-4-reasoning-hqq-b1-g64',
        'dtype': 'half', 'device_map': 'auto'}
2025-11-17:21:43:37 INFO     [models.huggingface:147] Using device 'cuda'
2025-11-17:21:43:37 INFO     [models.huggingface:420] Model parallel was set to False.
`torch_dtype` is deprecated! Use `dtype` instead!
/home/miniconda3/envs/hqq/lib/python3.12/site-packages/transformers/quantizers/auto.py:239: UserWarning: You passed `quantization_config` or equivalent parameters to `from_pretrained` but the model you're loading already has a `quantization_config` attribute. The `quantization_config` from the model will be used.
Running loglikelihood requests:   0%|               | 0/56168 [00:00<?, ?it/s]Passed argument batch_size = auto:8.0. Detecting largest batch size
Traceback (most recent call last):
  File "/home/miniconda3/envs/hqq/bin/lm_eval", line 7, in <module>
    sys.exit(cli_evaluate())
             ^^^^^^^^^^^^^^
  File "/home/miniconda3/envs/hqq/lib/python3.12/site-packages/lm_eval/__main__.py", line 455, in cli_evaluate
    results = evaluator.simple_evaluate(
              ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/miniconda3/envs/hqq/lib/python3.12/site-packages/lm_eval/utils.py", line 456, in _wrapper
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
  File "/home/miniconda3/envs/hqq/lib/python3.12/site-packages/lm_eval/evaluator.py", line 357, in simple_evaluate
    results = evaluate(
              ^^^^^^^^^
  File "/home/miniconda3/envs/hqq/lib/python3.12/site-packages/lm_eval/utils.py", line 456, in _wrapper
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
  File "/home/miniconda3/envs/hqq/lib/python3.12/site-packages/lm_eval/evaluator.py", line 585, in evaluate
    resps = getattr(lm, reqtype)(cloned_reqs)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/miniconda3/envs/hqq/lib/python3.12/site-packages/lm_eval/api/model.py", line 391, in loglikelihood
    return self._loglikelihood_tokens(new_reqs, disable_tqdm=disable_tqdm)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/miniconda3/envs/hqq/lib/python3.12/site-packages/lm_eval/models/huggingface.py", line 1177, in _loglikelihood_tokens
    for chunk in chunks:
                 ^^^^^^
  File "/home/miniconda3/envs/hqq/lib/python3.12/site-packages/lm_eval/models/utils.py", line 440, in get_batched
    yield from batch
  File "/home/miniconda3/envs/hqq/lib/python3.12/site-packages/lm_eval/models/utils.py", line 623, in get_chunks
    if len(arr) == (fn(i, _iter) if fn else n):
                    ^^^^^^^^^^^^
  File "/home/miniconda3/envs/hqq/lib/python3.12/site-packages/lm_eval/models/huggingface.py", line 1111, in _batch_scheduler
    self.batch_sizes[sched] = self._detect_batch_size(n_reordered_requests, pos)
                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/miniconda3/envs/hqq/lib/python3.12/site-packages/lm_eval/models/huggingface.py", line 820, in _detect_batch_size
    batch_size = forward_batch()
                 ^^^^^^^^^^^^^^^
  File "/home/miniconda3/envs/hqq/lib/python3.12/site-packages/accelerate/utils/memory.py", line 177, in decorator
    return function(batch_size, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/miniconda3/envs/hqq/lib/python3.12/site-packages/lm_eval/models/huggingface.py", line 812, in forward_batch
    self._model_call(test_batch, **call_kwargs),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/miniconda3/envs/hqq/lib/python3.12/site-packages/lm_eval/models/huggingface.py", line 949, in _model_call
    return self.model(inps).logits
           ^^^^^^^^^^^^^^^^
  File "/home/miniconda3/envs/hqq/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1775, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/miniconda3/envs/hqq/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1786, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/miniconda3/envs/hqq/lib/python3.12/site-packages/transformers/utils/generic.py", line 918, in wrapper
    output = func(self, *args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/miniconda3/envs/hqq/lib/python3.12/site-packages/transformers/models/phi3/modeling_phi3.py", line 465, in forward
    outputs: BaseModelOutputWithPast = self.model(
                                       ^^^^^^^^^^^
  File "/home/miniconda3/envs/hqq/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1775, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/miniconda3/envs/hqq/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1786, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/miniconda3/envs/hqq/lib/python3.12/site-packages/transformers/utils/generic.py", line 1064, in wrapper
    outputs = func(self, *args, **kwargs)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/miniconda3/envs/hqq/lib/python3.12/site-packages/transformers/models/phi3/modeling_phi3.py", line 401, in forward
    hidden_states = decoder_layer(
                    ^^^^^^^^^^^^^^
  File "/home/miniconda3/envs/hqq/lib/python3.12/site-packages/transformers/modeling_layers.py", line 94, in __call__
    return super().__call__(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/miniconda3/envs/hqq/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1775, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/miniconda3/envs/hqq/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1786, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/miniconda3/envs/hqq/lib/python3.12/site-packages/transformers/utils/deprecation.py", line 172, in wrapped_func
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/miniconda3/envs/hqq/lib/python3.12/site-packages/transformers/models/phi3/modeling_phi3.py", line 263, in forward
    hidden_states, self_attn_weights = self.self_attn(
                                       ^^^^^^^^^^^^^^^
  File "/home/miniconda3/envs/hqq/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1775, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/miniconda3/envs/hqq/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1786, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/miniconda3/envs/hqq/lib/python3.12/site-packages/transformers/utils/deprecation.py", line 172, in wrapped_func
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/miniconda3/envs/hqq/lib/python3.12/site-packages/transformers/models/phi3/modeling_phi3.py", line 176, in forward
    qkv = self.qkv_proj(hidden_states)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/miniconda3/envs/hqq/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1775, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/miniconda3/envs/hqq/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1786, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/miniconda3/envs/hqq/lib/python3.12/site-packages/hqq/core/quantize.py", line 889, in forward_pytorch_backprop
    return HQQMatmulNoCacheMul.apply(x, self.matmul, self.bias)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/miniconda3/envs/hqq/lib/python3.12/site-packages/torch/autograd/function.py", line 581, in apply
    return super().apply(*args, **kwargs)  # type: ignore[misc]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/miniconda3/envs/hqq/lib/python3.12/site-packages/hqq/core/quantize.py", line 325, in forward
    out = matmul(x, transpose=True)
          ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/miniconda3/envs/hqq/lib/python3.12/site-packages/hqq/core/quantize.py", line 882, in matmul
    return torch.matmul(x, weight.t() if (transpose) else weight)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
RuntimeError: expected mat1 and mat2 to have the same dtype, but got: c10::Half != float
Running loglikelihood requests:   0%|               | 0/56168 [00:02<?, ?it/s]
```

## 评论 (1)

### mobicham · 2025-11-19

Hey, yes that's a transformers bug not hqq: https://github.com/huggingface/transformers/issues/41455 
