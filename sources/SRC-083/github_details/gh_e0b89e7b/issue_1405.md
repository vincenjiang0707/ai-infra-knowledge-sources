# [Issue #1405] Error when saving FSDP weights with cpu_offload=True [rank1]: AttributeError: 'Params4bit' object has no attribute 'absmax'

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1405
state: closed | updated: 2026-02-20T19:30:31Z
labels: FSDP

## 正文

### System Info

- Python 3.10
- torch==2.4.1 and torch==2.5.1+cu121
- bitsandbytes==0.44.1
- llama-recipes 0.4.0.post1 and 0.4.0

### Reproduction

While running:
```bash
torchrun --nnodes 1 --nproc_per_node 2 recipes/quickstart/finetuning/finetuning.py \
    --use_peft \
    --peft_method lora \
    --model_name 'meta-llama/Llama-3.1-70B-Instruct' \
    --output_dir './my_lora_weights/70B' \
    --batch_size_training 1 \
    --batching_strategy "padding" \
    --weight_decay 0.2 \
    --num_epochs 10 \
    --dataset custom_dataset
    --quantization '4bit' \
    --enable_fsdp True 
    --use_fast_kernels True
```

The code that leads to the error is from llama-recipes (https://github.com/meta-llama/llama-recipes/blob/98707b72fda091b2b20e3ab2ffaf9a86e4fccd84/src/llama_recipes/model_checkpointing/checkpoint_handler.py#L273):
```python
def save_peft_checkpoint(model, model_path):
    """save_pretrained peft model"""

    options = StateDictOptions(full_state_dict=True, cpu_offload=True)
    
    if isinstance(model, FSDP):
        state_dict = get_model_state_dict(model, options=options)
        model.save_pretrained(model_path, state_dict=state_dict)
    else:
        model.save_pretrained(model_path)
```

### Expected behavior

...
[rank1]:   File "/home/Documents/llama-recipes/src/llama_recipes/utils/train_utils.py", line 259, in train                                                                                             
[rank1]:     save_peft_checkpoint(model, train_config.output_dir)                                                                                                                                                    
[rank1]:   File "/home/Documents/llama-recipes/src/llama_recipes/model_checkpointing/checkpoint_handler.py", line 276, in save_peft_checkpoint                                                         
[rank1]:     state_dict = get_model_state_dict(model, options=options)                                                                                                                                               
[rank1]:   File "/home/miniconda3/envs/llama_recipes_new/lib/python3.10/site-packages/torch/distributed/checkpoint/state_dict.py", line 995, in get_model_state_dict                                   
[rank1]:     model_state_dict = _get_model_state_dict(model, info)                                                                                                                                                   
[rank1]:   File "/home/miniconda3/envs/llama_recipes_new/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context                                                       
[rank1]:     return func(*args, **kwargs)                                                                                                                                                                            
[rank1]:   File "/home/miniconda3/envs/llama_recipes_new/lib/python3.10/site-packages/torch/distributed/checkpoint/state_dict.py", line 475, in _get_model_state_dict
[rank1]:     fqns = _get_fqns(model, key)
[rank1]:   File "/home/miniconda3/envs/llama_recipes_new/lib/python3.10/site-packages/torch/distributed/checkpoint/state_dict.py", line 224, in _get_fqns
[rank1]:     curr_obj = getattr(curr_obj, curr_obj_name)
[rank1]: AttributeError: 'Params4bit' object has no attribute 'absmax'

Apparently as per https://github.com/meta-llama/llama-recipes/issues/674 a temporary fix is making cpu_offload=False but this is only a bandaid fix that disables CPU offloading

## 评论 (6)

### llajan · 2024-11-22

I have the same issue with Llama 70B FSDP QLora training. When cpu offloading is turned off, it runs out of memory (as one might expect).

### PanagiotisFytas · 2024-11-22

I have still not find a resolution for this for anyone wondering

### luismsgomes · 2024-12-26

I am also facing this problem :-(

### vz-2244 · 2025-01-02

Got same issue when I tried Llama-3.2-90B-Vision QLora FSDP training. Any solution? 

### smartinezai · 2025-03-24

I also get the same error when running finetuning from the llama cookbook using FSDP and 4 bit quantization
```

[rank1]:   File "/leonardo_work/EUHPC_A04_062/AI_Model/src/llama_cookbook/finetuning.py", line 429, in <module>
[rank1]:     fire.Fire(main)
[rank1]:   File "/leonardo_work/EUHPC_A04_062/vllm_env/lib/python3.11/site-packages/fire/core.py", line 135, in Fire
[rank1]:     component_trace = _Fire(component, args, parsed_flag_args, context, name)
[rank1]:                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank1]:   File "/leonardo_work/EUHPC_A04_062/vllm_env/lib/python3.11/site-packages/fire/core.py", line 468, in _Fire
[rank1]:     component, remaining_args = _CallAndUpdateTrace(
[rank1]:                                 ^^^^^^^^^^^^^^^^^^^^
[rank1]:   File "/leonardo_work/EUHPC_A04_062/vllm_env/lib/python3.11/site-packages/fire/core.py", line 684, in _CallAndUpdateTrace
[rank1]:     component = fn(*varargs, **kwargs)
[rank1]:                 ^^^^^^^^^^^^^^^^^^^^^^
[rank1]:   File "/leonardo_work/EUHPC_A04_062/AI_Model/src/llama_cookbook/finetuning.py", line 407, in main
[rank1]:     results = train(
[rank1]:               ^^^^^^
[rank1]:   File "/leonardo_work/EUHPC_A04_062/AI_Model/src/llama_cookbook/utils/train_utils.py", line 242, in train
[rank1]:     save_peft_checkpoint(model, train_config.output_dir)
[rank1]:   File "/leonardo_work/EUHPC_A04_062/AI_Model/src/llama_cookbook/model_checkpointing/checkpoint_handler.py", line 284, in save_peft_checkpoint
[rank1]:     state_dict = get_model_state_dict(model, options=options)
[rank1]:                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank1]:   File "/leonardo_work/EUHPC_A04_062/vllm_env/lib/python3.11/site-packages/torch/distributed/checkpoint/state_dict.py", line 999, in get_model_state_dict
[rank1]:     model_state_dict = _get_model_state_dict(model, info)
[rank1]:                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank1]:   File "/leonardo_work/EUHPC_A04_062/vllm_env/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
[rank1]:     return func(*args, **kwargs)
[rank1]:            ^^^^^^^^^^^^^^^^^^^^^
[rank1]:   File "/leonardo_work/EUHPC_A04_062/vllm_env/lib/python3.11/site-packages/torch/distributed/checkpoint/state_dict.py", line 475, in _get_model_state_dict
[rank1]:     fqns = _get_fqns(model, key)
[rank1]:            ^^^^^^^^^^^^^^^^^^^^^
[rank1]:   File "/leonardo_work/EUHPC_A04_062/vllm_env/lib/python3.11/site-packages/torch/distributed/checkpoint/state_dict.py", line 224, in _get_fqns
[rank1]:     curr_obj = getattr(curr_obj, curr_obj_name)
[rank1]:                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank1]: AttributeError: 'Params4bit' object has no attribute 'absmax'
[rank2]: Traceback (most recent call last):
[rank2]:   File "/leonardo_work/EUHPC_A04_062/AI_Model/src/llama_cookbook/finetuning.py", line 429, in <module>
[rank2]:     fire.Fire(main)
[rank2]:   File "/leonardo_work/EUHPC_A04_062/vllm_env/lib/python3.11/site-packages/fire/core.py", line 135, in Fire
[rank2]:     component_trace = _Fire(component, args, parsed_flag_args, context, name)
[rank2]:                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank2]:   File "/leonardo_work/EUHPC_A04_062/vllm_env/lib/python3.11/site-packages/fire/core.py", line 468, in _Fire
[rank2]:     component, remaining_args = _CallAndUpdateTrace(
[rank2]:                                 ^^^^^^^^^^^^^^^^^^^^
[rank2]:   File "/leonardo_work/EUHPC_A04_062/vllm_env/lib/python3.11/site-packages/fire/core.py", line 684, in _CallAndUpdateTrace
[rank2]:     component = fn(*varargs, **kwargs)
[rank2]:                 ^^^^^^^^^^^^^^^^^^^^^^
[rank2]:   File "/leonardo_work/EUHPC_A04_062/AI_Model/src/llama_cookbook/finetuning.py", line 407, in main
[rank2]:     results = train(
[rank2]:               ^^^^^^
[rank2]:   File "/leonardo_work/EUHPC_A04_062/AI_Model/src/llama_cookbook/utils/train_utils.py", line 242, in train
[rank2]:     save_peft_checkpoint(model, train_config.output_dir)
[rank2]:   File "/leonardo_work/EUHPC_A04_062/AI_Model/src/llama_cookbook/model_checkpointing/checkpoint_handler.py", line 284, in save_peft_checkpoint
[rank2]:     state_dict = get_model_state_dict(model, options=options)
[rank2]:                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank2]:   File "/leonardo_work/EUHPC_A04_062/vllm_env/lib/python3.11/site-packages/torch/distributed/checkpoint/state_dict.py", line 999, in get_model_state_dict
[rank2]:     model_state_dict = _get_model_state_dict(model, info)
[rank2]:                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank2]:   File "/leonardo_work/EUHPC_A04_062/vllm_env/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
[rank2]:     return func(*args, **kwargs)
[rank2]:            ^^^^^^^^^^^^^^^^^^^^^
[rank2]:   File "/leonardo_work/EUHPC_A04_062/vllm_env/lib/python3.11/site-packages/torch/distributed/checkpoint/state_dict.py", line 475, in _get_model_state_dict
[rank2]:     fqns = _get_fqns(model, key)
[rank2]:            ^^^^^^^^^^^^^^^^^^^^^
[rank2]:   File "/leonardo_work/EUHPC_A04_062/vllm_env/lib/python3.11/site-packages/torch/distributed/checkpoint/state_dict.py", line 224, in _get_fqns
[rank2]:     curr_obj = getattr(curr_obj, curr_obj_name)
[rank2]:                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank2]: AttributeError: 'Params4bit' object has no attribute 'absmax'
W0324 16:14:25.342000 1346190 torch/distributed/elastic/multiprocessing/api.py:897] Sending process 1346238 closing signal SIGTERM
W0324 16:14:25.344000 1346190 torch/distributed/elastic/multiprocessing/api.py:897] Sending process 1346239 closing signal SIGTERM
E0324 16:14:26.659000 1346190 torch/distributed/elastic/multiprocessing/api.py:869] failed (exitcode: 1) local_rank: 2 (pid: 1346240) of binary: /leonardo_work/EUHPC_A04_062/vllm_env/bin/python
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/leonardo_work/EUHPC_A04_062/vllm_env/lib/python3.11/site-packages/torch/distributed/run.py", line 922, in <module>
    main()
  File "/leonardo_work/EUHPC_A04_062/vllm_env/lib/python3.11/site-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 355, in wrapper
    return f(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^
  File "/leonardo_work/EUHPC_A04_062/vllm_env/lib/python3.11/site-packages/torch/distributed/run.py", line 918, in main
    run(args)
  File "/leonardo_work/EUHPC_A04_062/vllm_env/lib/python3.11/site-packages/torch/distributed/run.py", line 909, in run
    elastic_launch(
  File "/leonardo_work/EUHPC_A04_062/vllm_env/lib/python3.11/site-packages/torch/distributed/launcher/api.py", line 138, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/leonardo_work/EUHPC_A04_062/vllm_env/lib/python3.11/site-packages/torch/distributed/launcher/api.py", line 269, in launch_agent
    raise ChildFailedError(
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
============================================================
src/llama_cookbook/finetuning.py FAILED
------------------------------------------------------------
Failures:
  <NO_OTHER_FAILURES>
------------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2025-03-24_16:14:25
  host      : lrdn0021-net1-3.leonardo.local
  rank      : 2 (local_rank: 2)
  exitcode  : 1 (pid: 1346240)
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
============================================================
srun: error: lrdn0021: task 0: Exited with exit code 1

```

### TimDettmers · 2026-02-14

A fix for this has been submitted in #1866.

**Root cause:** PyTorch's FSDP state_dict machinery (`get_model_state_dict` with `cpu_offload=True`) uses `_get_fqns()` to resolve state dict keys back to model attributes by walking dotted paths with `getattr()`. For 4-bit quantized models, `Linear4bit._save_to_state_dict` produces keys like `weight.absmax`, `weight.quant_map`, and `weight.quant_state.bitsandbytes__nf4`. When `_get_fqns` calls `getattr(params4bit, "absmax")`, it fails because `absmax` lives inside `params4bit.quant_state`, not directly on the parameter object.

**Fix:** Add `__getattr__` to `Params4bit` that proxies known `QuantState` attributes (including the `quant_map`→`code` alias), and add `__getattr__` to `QuantState` that handles the packed `bitsandbytes__*` keys. This allows the full FQN traversal to succeed without changing how quantization works.

Verified with a single-GPU FSDP integration test using a QLoRA-style model (frozen 4-bit base + trainable adapter). The PR will be reviewed in the next days.
