# [Issue #103] Expected in.dtype() == at::kInt to be true, but got false

source: https://github.com/dropbox/hqq/issues/103
state: closed | updated: 2024-08-15T07:08:32Z
labels: 

## 正文

Using the example code provided here: https://huggingface.co/mobiuslabsgmbh/Llama-3.1-70b-instruct_4bitgs64_hqq

I _am_ using the `master` branch of this repo.

```
Traceback (most recent call last):
  File "/home/ubuntu/tmp.py", line 24, in <module>
    prepare_for_inference(model, backend="torchao_int4")
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ubuntu/.pixi/envs/default/lib/python3.12/site-packages/hqq/utils/patching.py", line 99, in prepare_for_inference
    patch_linearlayers(model, patch_hqq_to_aoint4, verbose=verbose)
  File "/home/ubuntu/.pixi/envs/default/lib/python3.12/site-packages/hqq/utils/patching.py", line 25, in patch_linearlayers
    model.base_class.patch_linearlayers(
  File "/home/ubuntu/.pixi/envs/default/lib/python3.12/site-packages/hqq/models/base.py", line 154, in patch_linearlayers
    patch_fct(tmp_mapping[name], patch_param),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ubuntu/.pixi/envs/default/lib/python3.12/site-packages/hqq/backends/torchao.py", line 323, in patch_hqq_to_aoint4
    hqq_aoint4_layer.initialize_with_hqq_quants(
  File "/home/ubuntu/.pixi/envs/default/lib/python3.12/site-packages/hqq/backends/torchao.py", line 91, in initialize_with_hqq_quants
    self.process_hqq_quants(W_q, meta)
  File "/home/ubuntu/.pixi/envs/default/lib/python3.12/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/ubuntu/.pixi/envs/default/lib/python3.12/site-packages/hqq/backends/torchao.py", line 193, in process_hqq_quants
    self.weight_int4pack = torch.ops.aten._convert_weight_to_int4pack(
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ubuntu/.pixi/envs/default/lib/python3.12/site-packages/torch/_ops.py", line 1061, in __call__
    return self_._op(*args, **(kwargs or {}))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
RuntimeError: Expected in.dtype() == at::kInt to be true, but got false.  (Could this error message be improved?  If so, please report an enhancement request to PyTorch.)
```

## 评论 (14)

### mobicham · 2024-08-14

Can you try:
- The pytorch nightly build
- Use the latest hqq from the master branch not from pip 
- make sure you use `bfloat16` not `float16` with `backend="torchao_int4"`

This should fix this issue otherwise let me know!



### jonashaag · 2024-08-14

With PyTorch nightly I'm getting

```
python tmp.py
Warning: failed to import the Marlin backend. Check if marlin is correctly installed if you want to use the Marlin backend (https://github.com/IST-DASLab/marlin).
Warning: failed to import the BitBlas backend. Check if BitBlas is correctly installed if you want to use the bitblas backend (https://github.com/microsoft/BitBLAS).
Fetching 7 files: 100%|███████████████████████████████████████████████████████████████████████████████████████| 7/7 [00:00<00:00, 65536.00it/s]
/home/ubuntu/.pixi/envs/default/lib/python3.12/site-packages/hqq/models/base.py:251: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  return torch.load(cls.get_weight_file(save_dir), map_location=map_location)
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████| 323/323 [00:00<00:00, 17418.30it/s]
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████| 561/561 [00:00<00:00, 16606.83it/s]
Traceback (most recent call last):
  File "/home/ubuntu/tmp.py", line 29, in <module>
    gen = HFGenerator(model, tokenizer, max_new_tokens=10, do_sample=True, compile="partial").warmup() #Warm-up takes a while
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ubuntu/.pixi/envs/default/lib/python3.12/site-packages/hqq/utils/generation_hf.py", line 100, in warmup
    self.generate(prompt, print_tokens=False);
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ubuntu/.pixi/envs/default/lib/python3.12/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/ubuntu/.pixi/envs/default/lib/python3.12/site-packages/hqq/utils/generation_hf.py", line 253, in generate
    return self.next_token_iterator(self.prefill(), self.max_new_tokens, verbose, print_tokens)
                                    ^^^^^^^^^^^^^^
  File "/home/ubuntu/.pixi/envs/default/lib/python3.12/site-packages/hqq/utils/generation_hf.py", line 183, in prefill
    out = self.model(
          ^^^^^^^^^^^
  File "/home/ubuntu/.pixi/envs/default/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ubuntu/.pixi/envs/default/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ubuntu/.pixi/envs/default/lib/python3.12/site-packages/transformers/models/llama/modeling_llama.py", line 1189, in forward
    outputs = self.model(
              ^^^^^^^^^^^
  File "/home/ubuntu/.pixi/envs/default/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ubuntu/.pixi/envs/default/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ubuntu/.pixi/envs/default/lib/python3.12/site-packages/transformers/models/llama/modeling_llama.py", line 971, in forward
    causal_mask = self._update_causal_mask(
                  ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ubuntu/.pixi/envs/default/lib/python3.12/site-packages/transformers/models/llama/modeling_llama.py", line 1086, in _update_causal_mask
    causal_mask = _prepare_4d_causal_attention_mask_with_cache_position(
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ubuntu/.pixi/envs/default/lib/python3.12/site-packages/transformers/models/llama/modeling_llama.py", line 102, in _prepare_4d_causal_attention_mask_with_cache_position
    padding_mask = causal_mask[:, :, :, :mask_length] + attention_mask[:, None, None, :]
                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
RuntimeError: The size of tensor a (32) must match the size of tensor b (40) at non-singleton dimension 3
```

### mobicham · 2024-08-14

I just tried on a fresh A100 instance and it's working fine:
-torch nightly: `pip uninstall torch -y; pip install --pre torch --index-url https://download.pytorch.org/whl/nightly/cu121;`
-hqq from master: `pip install git+https://github.com/mobiusml/hqq.git`
transformers version `4.44.0`

### jonashaag · 2024-08-14

Super weird. I have CUDA 12.4, maybe that's the problem, I'll try to downgrade.

### mobicham · 2024-08-14

You can switch between different CUDA versions like this, you don't have to replace it:
```shell
export CUDA_HOME=/usr/local/cuda-12.1
export LD_LIBRARY_PATH=${CUDA_HOME}/lib64:$LD_LIBRARY_PATH
export PATH=${CUDA_HOME}/bin:${PATH}
```

### jonashaag · 2024-08-14

Thanks! It still doesn't work

```
$ python tmp.py
Warning: failed to import the Marlin backend. Check if marlin is correctly installed if you want to use the Marlin backend (https://github.com/IST-DASLab/marlin).
Warning: failed to import the BitBlas backend. Check if BitBlas is correctly installed if you want to use the bitblas backend (https://github.com/microsoft/BitBLAS).
Fetching 7 files: 100%|██████████████████████████████████████████████████████████████████████████████████████| 7/7 [00:00<00:00, 109552.72it/s]
/home/ubuntu/env/lib/python3.10/site-packages/hqq/models/base.py:251: FutureWarning: You are using `torch.load` with `weights_only=False` (the current default value), which uses the default pickle module implicitly. It is possible to construct malicious pickle data which will execute arbitrary code during unpickling (See https://github.com/pytorch/pytorch/blob/main/SECURITY.md#untrusted-models for more details). In a future release, the default value for `weights_only` will be flipped to `True`. This limits the functions that could be executed during unpickling. Arbitrary objects will no longer be allowed to be loaded via this mode unless they are explicitly allowlisted by the user via `torch.serialization.add_safe_globals`. We recommend you start setting `weights_only=True` for any use case where you don't have full control of the loaded file. Please open an issue on GitHub for any issues related to this experimental feature.
  return torch.load(cls.get_weight_file(save_dir), map_location=map_location)
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████| 323/323 [00:00<00:00, 19289.51it/s]
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████| 561/561 [00:00<00:00, 14996.75it/s]
Traceback (most recent call last):
  File "/home/ubuntu/tmp.py", line 29, in <module>
    gen = HFGenerator(model, tokenizer, max_new_tokens=10, do_sample=True, compile="partial").warmup() #Warm-up takes a while
  File "/home/ubuntu/env/lib/python3.10/site-packages/hqq/utils/generation_hf.py", line 100, in warmup
    self.generate(prompt, print_tokens=False);
  File "/home/ubuntu/env/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
  File "/home/ubuntu/env/lib/python3.10/site-packages/hqq/utils/generation_hf.py", line 253, in generate
    return self.next_token_iterator(self.prefill(), self.max_new_tokens, verbose, print_tokens)
  File "/home/ubuntu/env/lib/python3.10/site-packages/hqq/utils/generation_hf.py", line 183, in prefill
    out = self.model(
  File "/home/ubuntu/env/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/home/ubuntu/env/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/ubuntu/env/lib/python3.10/site-packages/transformers/models/llama/modeling_llama.py", line 1189, in forward
    outputs = self.model(
  File "/home/ubuntu/env/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/home/ubuntu/env/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/ubuntu/env/lib/python3.10/site-packages/transformers/models/llama/modeling_llama.py", line 971, in forward
    causal_mask = self._update_causal_mask(
  File "/home/ubuntu/env/lib/python3.10/site-packages/transformers/models/llama/modeling_llama.py", line 1086, in _update_causal_mask
    causal_mask = _prepare_4d_causal_attention_mask_with_cache_position(
  File "/home/ubuntu/env/lib/python3.10/site-packages/transformers/models/llama/modeling_llama.py", line 102, in _prepare_4d_causal_attention_mask_with_cache_position
    padding_mask = causal_mask[:, :, :, :mask_length] + attention_mask[:, None, None, :]
RuntimeError: The size of tensor a (32) must match the size of tensor b (40) at non-singleton dimension 3

(env) ubuntu@l40s-90-gra11:~$ nvidia-smi  | grep Version
| NVIDIA-SMI 535.183.01             Driver Version: 535.183.01   CUDA Version: 12.2     |
(env) ubuntu@l40s-90-gra11:~$ dpkg -l | grep cuda | head -n 1
ii  cuda-12-1                           12.1.0-1                                amd64        CUDA 12.1 meta-package
(env) ubuntu@l40s-90-gra11:~$ dpkg -l | grep cuda-12
ii  cuda-12-1                           12.1.0-1                                amd64        CUDA 12.1 meta-package
(env) ubuntu@l40s-90-gra11:~$ pip list | grep torch
pytorch-triton           3.0.0+dedb7bdf33
torch                    2.5.0.dev20240814+cu121
(env) ubuntu@l40s-90-gra11:~$ pip list | grep hqq
hqq                      0.2.0
(env) ubuntu@l40s-90-gra11:~$ pip list | grep transf
transformers             4.44.0
```

Not sure why `nvidia-smi` says CUDA 12.2

### mobicham · 2024-08-14

Oh I see, nightly torch actually fixed the first issue. The second issue is that, in your example, you are using `max_new_tokens=10`, you need to use a valid minimum size. In the example we published, it's using 1000 which should be enough for most use-cases. You can either keep it to 1000, or use a minimum of 128. A value of 10 would break things because it's too small I think

### jonashaag · 2024-08-14

Thank you, it seems to work now. I'm going to do quality comparisons now!

My recipe:

- Install Ubuntu 22.04
- Install `cuda-12-1` via `.deb` method 
- Install `python3-dev` and `build-essential`
- `pip install --pre torch --index-url https://download.pytorch.org/whl/nightly/cu121`
- `pip install git+https://github.com/mobiusml/hqq.git`

### jonashaag · 2024-08-14

I still have the problem even with larger `max_new_tokens`:

```
  File "/home/ubuntu/env/lib/python3.10/site-packages/transformers/models/llama/modeling_llama.py", line 102, in _prepare_4d_causal_attention_mask_with_cache_position
    padding_mask = causal_mask[:, :, :, :mask_length] + attention_mask[:, None, None, :]
RuntimeError: The size of tensor a (256) must match the size of tensor b (1873) at non-singleton dimension 3
```

The `1873` in the message varies from prompt to prompt.

Are my prompts too large?

NB: Is it possible to cache the compilation step?

### mobicham · 2024-08-14

Can you try using powers of 2 for `max_new_tokens` ? for 1873 you'd set 2048 etc., it should work fine up to 8192 new tokens.
Alternatively, you can use the native transformers `model.generate` with dynamic cache if static cache is creating issues for you. 

There are some flags to reduce the time of the compilation step: https://pytorch.org/tutorials/recipes/torch_compile_caching_tutorial.html

### jonashaag · 2024-08-14

I used `128` and got the same problem.

Should the `max_new_tokens` value include the number of expected input tokens?

### mobicham · 2024-08-14

The issue with static cache is that it needs to be initialized before hand and only once.  The cache size should be `make_multiple(max_prefill_phase_size + max_new_tokens)` where `make_multiple()` is a function making the cache shape a matmul friendly size, such as a powers of 2 (1024, 2048, etc.)
The current implementation automatically sets the cache_size as the next 2^N power of `max_new_tokens`, which should work fine as long as the input prompt is not too large. 

What is the size of your prefill step in terms of tokens? There's an extra parameter `cache_size=` that you can set manually in case your input prompts are longer: https://github.com/mobiusml/hqq/blob/master/hqq/utils/generation_hf.py#L25 
You can set it larger to  prefill_tokens + max_new_tokens and make it a nice shape number like 2048 or 4096. 
If you share a similar prompt in size I can investigate what goes wrong.

If you don't want to mess with this stuff, you can simply use `model.generate` which uses dynamic caching and should handle all use-cases.



### jonashaag · 2024-08-14

Thank you, the transformers-native generator worked fine. The quality seems to be almost on par with the BF16 version 🚀 

I want to run different kinds of queries:

- ~ 8k prefill and 16 (not 16k) output
- ~ 16k prefill and 1k output
- ~ 16k prefill (or more) and 4k output
- 128 prefill and 512 output (estimate; typical Q&A scenario)

### mobicham · 2024-08-15

Great, thanks for running an independent evaluation :+1:  !
