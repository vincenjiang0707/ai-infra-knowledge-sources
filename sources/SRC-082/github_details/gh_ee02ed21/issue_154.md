# [Issue #154] reproduce Llama2 7b failure : RuntimeError: The expanded size of the tensor (4608) must match the existing size (4096) at non-singleton dimension 3.  Target sizes: [65, 32, 512, 4608].  Tensor sizes: [65, 1, 512, 4096] 

source: https://github.com/mit-han-lab/llm-awq/issues/154
state: open | updated: 2025-10-27T06:26:52Z
labels: 

## 正文

I wanna reproduce the llama2 steps followed by the scripts/llama2_example.sh on RTX4090
I just run the commad 
`python -m awq.entry --model_path /data/models/Llama-2-7b-chat-hf --w_bit 4 --q_group_size 128  --run_awq --dump_awq awq_cache/Llama-2-7b-chat-hf-w4-g128.pt
`
it report the error :
`untimeError: The expanded size of the tensor (4608) must match the existing size (4096) at non-singleton dimension 3.  Target sizes: [65, 32, 512, 4608].  Tensor sizes: [65, 1, 512, 4096]`
here is the whole log info 
```
root@aaded0dbf149:/data/llm-awq# 
root@aaded0dbf149:/data/llm-awq# 
root@aaded0dbf149:/data/llm-awq# python -m awq.entry --model_path /data/models/Llama-2-7b-chat-hf --w_bit 4 --q_group_size 128  --run_awq --dump_awq awq_cache/Llama-2-7b-chat-hf-w4-g128.pt
Quantization config: {'zero_point': True, 'q_group_size': 128}
* Building model /data/models/Llama-2-7b-chat-hf
Loading checkpoint shards: 100%|████████████████████████████████████████| 2/2 [00:00<00:00, 13.03it/s]
Repo card metadata block was not found. Setting CardData to empty.
 * Split into 65 blocks
Running AWQ...:   0%|                                                          | 0/32 [00:01<?, ?it/s]
Traceback (most recent call last):
  File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/usr/lib/python3.10/runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "/data/llm-awq/awq/entry.py", line 299, in <module>
    main()
  File "/data/llm-awq/awq/entry.py", line 239, in main
    model, enc = build_model_and_enc(args.model_path)
  File "/data/llm-awq/awq/entry.py", line 161, in build_model_and_enc
    awq_results = run_awq(
  File "/usr/local/lib/python3.10/dist-packages/torch/utils/_contextlib.py", line 115, in decorate_context
    return func(*args, **kwargs)
  File "/data/llm-awq/awq/quantize/pre_quant.py", line 181, in run_awq
    scales_list = auto_scale_block(
  File "/usr/local/lib/python3.10/dist-packages/torch/utils/_contextlib.py", line 115, in decorate_context
    return func(*args, **kwargs)
  File "/data/llm-awq/awq/quantize/auto_scale.py", line 217, in auto_scale_block
    _auto_get_scale(
  File "/data/llm-awq/awq/quantize/auto_scale.py", line 163, in _auto_get_scale
    scales = _search_module_scale(module2inspect, layers, inp, kwargs)
  File "/data/llm-awq/awq/quantize/auto_scale.py", line 134, in _search_module_scale
    out = block(x, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1511, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1520, in _call_impl
    return forward_call(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/transformers/models/llama/modeling_llama.py", line 671, in forward
    attn_output = torch.nn.functional.scaled_dot_product_attention(
RuntimeError: The expanded size of the tensor (4608) must match the existing size (4096) at non-singleton dimension 3.  Target sizes: [65, 32, 512, 4608].  Tensor sizes: [65, 1, 512, 4096]
```

That I miss some steps ? or how can I fix it ?

## 评论 (0)
